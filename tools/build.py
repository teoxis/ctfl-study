#!/usr/bin/env python3
"""Builds data/bank-ch1..6.json and data/exam.json, and validates the bank.

Usage: python3 tools/build.py      (from the repo root)
"""
import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import qlib  # noqa: E402
import bank_ch1, bank_ch2, bank_ch3, bank_ch4, bank_ch5_6  # noqa: E402,F401
import gen_k3  # noqa: E402

gen_k3.build_all()

DATA = HERE.parent / "data"
DATA.mkdir(exist_ok=True)

# Official distribution: ISTQB "Exam Structures & Rules tables" v1.19 (2026-08-19), CTFL v4.0
BLUEPRINT = [
    (1, 1, 1, ["1.1.1", "1.2.2"]), (1, 1, 1, ["1.5.2"]), (1, 2, 1, ["1.1.2", "1.2.1", "1.2.3"]),
    (1, 2, 1, ["1.3.1"]), (1, 2, 3, ["1.4.1", "1.4.2", "1.4.3", "1.4.4", "1.4.5"]), (1, 2, 1, ["1.5.1", "1.5.3"]),
    (2, 1, 1, ["2.1.2"]), (2, 1, 1, ["2.1.3"]), (2, 2, 1, ["2.2.1", "2.2.2"]), (2, 2, 1, ["2.2.3", "2.3.1"]),
    (2, 2, 1, ["2.1.1", "2.1.6"]), (2, 2, 1, ["2.1.4", "2.1.5"]),
    (3, 1, 2, ["3.1.1", "3.2.1", "3.2.3", "3.2.5"]), (3, 2, 1, ["3.1.2", "3.1.3"]), (3, 2, 1, ["3.2.2", "3.2.4"]),
    (4, 2, 1, ["4.1.1"]), (4, 2, 2, ["4.3.1", "4.3.2", "4.3.3"]), (4, 2, 2, ["4.4.1", "4.4.2", "4.4.3"]),
    (4, 2, 1, ["4.5.1", "4.5.2"]), (4, 3, 5, ["4.2.1", "4.2.2", "4.2.3", "4.2.4", "4.5.3"]),
    (5, 1, 1, ["5.1.2", "5.1.6", "5.2.1", "5.3.1"]), (5, 2, 1, ["5.1.1", "5.1.3"]), (5, 2, 1, ["5.1.7"]),
    (5, 2, 1, ["5.2.2", "5.2.3", "5.2.4"]), (5, 2, 1, ["5.3.2", "5.3.3"]), (5, 2, 1, ["5.4.1"]),
    (5, 3, 3, ["5.1.4", "5.1.5", "5.5.1"]),
    (6, 2, 1, ["6.1.1"]), (6, 1, 1, ["6.2.1"]),
]

errors = []
bank = qlib.BANK

# ---------------- structural validation ----------------
ids = Counter(x["id"] for x in bank)
for i, c in ids.items():
    if c > 1:
        errors.append(f"duplicate id {i}")
stems = Counter((x["q"], x.get("code", ""), x["o"][0]) for x in bank)
for s, c in stems.items():
    if c > 1:
        errors.append(f"duplicate question text: {s[0][:80]}")
for x in bank:
    if len(x["o"]) != 4 or len({o.lower() for o in x["o"]}) != 4:
        errors.append(f"{x['id']}: needs 4 distinct options")
    if any(w in " ".join(x["o"]).lower() for w in ["all of the above", "none of the above"]):
        errors.append(f"{x['id']}: uses all/none of the above")
    if not x["e"] or len(x["e"]) < 20:
        errors.append(f"{x['id']}: missing explanation")
    if x["k"] != qlib.LOS[x["sec"]][0]:
        errors.append(f"{x['id']}: K-level mismatch")

per_lo = Counter(x["sec"] for x in bank)
for lo in qlib.LOS:
    if per_lo[lo] < 6:
        errors.append(f"LO {lo} has only {per_lo[lo]} questions (min 6)")

# ---------------- blueprint validation ----------------
tot = sum(n for _, _, n, _ in BLUEPRINT)
k_tot = Counter()
ch_tot = Counter()
for ch, k, n, los in BLUEPRINT:
    k_tot[k] += n
    ch_tot[ch] += n
    for lo in los:
        if qlib.LOS[lo][0] != k:
            errors.append(f"blueprint group {los} K{k} contains {lo} (K{qlib.LOS[lo][0]})")
    pool = sum(per_lo[lo] for lo in los)
    if pool < n:
        errors.append(f"group {los} has {pool} questions for {n} draws")
all_bp_los = [lo for *_, los in BLUEPRINT for lo in los]
if sorted(all_bp_los) != sorted(qlib.LOS):
    errors.append("blueprint does not list every LO exactly once")
if tot != 40 or dict(k_tot) != {1: 8, 2: 24, 3: 8} or dict(ch_tot) != {1: 8, 2: 6, 3: 4, 4: 11, 5: 9, 6: 2}:
    errors.append(f"blueprint totals wrong: {tot} {dict(k_tot)} {dict(ch_tot)}")


# ---------------- simulate 200 mock exams (same algorithm as the app) ----------------
def draw_exam(rng, seen):
    """Same algorithm as app.js: per group, least-seen questions first, then prefer LOs not yet used."""
    picked = []
    for ch, k, n, los in BLUEPRINT:
        pool = [x for x in bank if x["sec"] in los]
        chosen = []
        while len(chosen) < n:
            cands = [x for x in pool if x not in chosen]
            low = min(seen.get(x["id"], 0) for x in cands)
            best = [x for x in cands if seen.get(x["id"], 0) == low]
            used = {x["sec"] for x in chosen}
            fresh_lo = [x for x in best if x["sec"] not in used]
            chosen.append(rng.choice(fresh_lo or best))
        picked += chosen
    return picked


rng = random.Random(7)
for _ in range(200):
    ex = draw_exam(rng, {})
    if len(ex) != 40 or len({x["id"] for x in ex}) != 40:
        errors.append("simulated exam is not 40 distinct questions"); break
    if Counter(x["ch"] for x in ex) != Counter({1: 8, 2: 6, 3: 4, 4: 11, 5: 9, 6: 2}):
        errors.append("simulated exam has wrong chapter split"); break
    if Counter(x["k"] for x in ex) != Counter({1: 8, 2: 24, 3: 8}):
        errors.append("simulated exam has wrong K split"); break
    for ch, k, n, los in BLUEPRINT:
        if sum(1 for x in ex if x["sec"] in los) != n:
            errors.append(f"simulated exam wrong count for group {los}"); break

# how many exams before questions repeat (least-seen-first selection)
seen = {}
fresh_exams = 0
rng2 = random.Random(11)
while True:
    ex = draw_exam(rng2, seen)
    if any(seen.get(x["id"], 0) > 0 for x in ex):
        break
    for x in ex:
        seen[x["id"]] = seen.get(x["id"], 0) + 1
    fresh_exams += 1
# exams where at most 10% of questions are repeats
seen = {}
low_rep = 0
rng3 = random.Random(13)
for _ in range(40):
    ex = draw_exam(rng3, seen)
    reps = sum(1 for x in ex if seen.get(x["id"], 0) > 0)
    if reps > 4:
        break
    for x in ex:
        seen[x["id"]] = seen.get(x["id"], 0) + 1
    low_rep += 1

# ---------------- syllabus notes ----------------
import syllabus_notes  # noqa: E402
note_los = {}
for chap in syllabus_notes.CHAPTERS:
    for sec in chap["sections"]:
        for lo in sec["los"]:
            note_los[lo["lo"]] = lo
            if lo["k"] != qlib.LOS[lo["lo"]][0]:
                errors.append(f"notes K mismatch {lo['lo']}")
            if lo["k"] == 3 and "example" not in lo:
                errors.append(f"notes: K3 LO {lo['lo']} without worked example")
            if not lo.get("terms"):
                errors.append(f"notes: {lo['lo']} without key terms")
if set(note_los) != set(qlib.LOS):
    errors.append(f"notes LOs differ: {set(qlib.LOS) ^ set(note_los)}")

if errors:
    print("ERRORS:")
    for e in errors:
        print(" -", e)
    sys.exit(1)

# ---------------- write files ----------------
by_ch = defaultdict(list)
for x in bank:
    by_ch[x["ch"]].append(x)
for ch, items in sorted(by_ch.items()):
    (DATA / f"bank-ch{ch}.json").write_text(json.dumps(items, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
(DATA / "syllabus.json").write_text(json.dumps({
    "source": "ISTQB CTFL Syllabus v4.0.1 (2024-09-15)",
    "chapters": syllabus_notes.CHAPTERS,
}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
(DATA / "exam.json").write_text(json.dumps({
    "source": "ISTQB Exam Structures & Rules tables v1.19 (2026-08-19), CTFL v4.0",
    "questions": 40, "pass": 26, "minutes": 60, "minutesNonNative": 75,
    "groups": [{"ch": ch, "k": k, "n": n, "los": los} for ch, k, n, los in BLUEPRINT],
}, ensure_ascii=False, indent=1), encoding="utf-8")

print(f"OK: {len(bank)} questions")
print("Per K-level:", dict(sorted(Counter(x['k'] for x in bank).items())))
print("Per chapter:", dict(sorted(Counter(x['ch'] for x in bank).items())))
print("Per LO:", " ".join(f"{lo}:{per_lo[lo]}" for lo in qlib.LOS))
print("Per exam group (pool/draws):", " | ".join(f"{'+'.join(los)} {sum(per_lo[l] for l in los)}/{n}" for _, _, n, los in BLUEPRINT))
print(f"Mock exams with zero repeated questions: {fresh_exams}")
print(f"Mock exams with at most 4 repeated questions (10%): {low_rep}")
print("200 simulated exams: 40 questions, 8/6/4/11/9/2 per chapter, K1 8 / K2 24 / K3 8, exact per LO group: OK")

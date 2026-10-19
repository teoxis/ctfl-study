#!/usr/bin/env python3
"""Independent check of numeric answers: re-derives each answer from the PUBLISHED question
text (data/*.json), without using the generator's internal data."""
import json
import re
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
bank = []
for f in sorted(DATA.glob("bank-ch*.json")):
    bank += json.loads(f.read_text(encoding="utf-8"))

checked, failed = 0, []


def ok(x, cond, msg=""):
    global checked
    checked += 1
    if not cond:
        failed.append(f"{x['id']}: {msg} | {x['q'][:90]}")


def pct(n, d):
    v = 100 * n / d
    return f"{v:.0f}%" if abs(v - round(v)) < 1e-9 else f"{v:.1f}%"


def ranges(text):
    rs = []
    for a, b in re.findall(r"(-?\d+)\s*(?:–|to)\s*(-?\d+)", text):
        r = (int(a), int(b))
        if r not in rs:
            rs.append(r)
    # keep only the elementary partitions: drop any range that contains another one (overall range restatements)
    elem = [r for r in rs if not any(o != r and r[0] <= o[0] and o[1] <= r[1] for o in rs)]
    return sorted(elem)


for x in bank:
    s, ans = x["q"], x["o"][0]
    # three-point
    m = re.search(r"a = (\d+), (?:most likely )?m = (\d+)(?:,| and) (?:most pessimistic )?b = (\d+)", s)
    if m and x["sec"] == "5.1.4":
        a, mm, b = map(int, m.groups())
        E, SD = (a + 4 * mm + b) / 6, (b - a) / 6
        if "range" in s:
            ok(x, ans.startswith(f"Between {E-SD:g} and {E+SD:g}"), "three-point range")
        else:
            ok(x, ans.startswith(f"{E:g} ± {SD:g}"), "three-point")
        continue
    m = re.search(r"ratio was (\d+):(\d+).*estimated at (\d+)", s)
    if m:
        p, t, dev = map(int, m.groups())
        ok(x, ans == f"{dev*t/p:g} person-days", "ratio")
        continue
    m = re.search(r"last three iterations was (\d+), (\d+) and (\d+)", s)
    if m:
        v = list(map(int, m.groups()))
        ok(x, ans == f"{sum(v)/3:g} person-hours", "extrapolation avg")
        continue
    m = re.search(r"executing (\d+) test cases took (\d+) person-hours\. (\d+) test cases remain", s)
    if m:
        d, h, r = map(int, m.groups())
        ok(x, ans == f"{h/d*r:g} person-hours", "extrapolation rate")
        continue
    # EP minimum number of values: count ranges in the text + 2 invalid partitions
    if x["sec"] == "4.2.1" and "minimum number of test values" in s:
        rs = [r for r in ranges(s.split("Using")[0]) if r[0] <= r[1]]
        # drop the overall-range restatement (e.g. "from 0 to 100") if subranges exist
        if len(rs) > 1 and rs[0][0] == rs[1][0] and rs[0][1] > rs[1][1]:
            rs = rs[1:]
        ok(x, ans == str(len(rs) + 2), f"EP count {len(rs)+2}")
        continue
    if x["sec"] == "4.2.1" and "Each Choice" in s:
        counts = [len(g.split(",")) for g in re.findall(r"\(([^)]*)\)", s)]
        ok(x, ans == str(max(counts)), "each choice")
        continue
    if x["sec"] == "4.2.1" and "achieves 100% equivalence partition coverage" in s:
        rs = [r for r in ranges(s.split("Which")[0]) if r[0] <= r[1]]
        if len(rs) > 1 and rs[0][0] == rs[1][0] and rs[0][1] > rs[1][1]:
            rs = rs[1:]
        lo, hi = rs[0][0], rs[-1][1]
        def part(v):
            if v < lo: return -1
            if v > hi: return 99
            return next(i for i, (a, b) in enumerate(rs) if a <= v <= b)
        def full(opt):
            vals = [int(v) for v in opt.split(", ")]
            return len({part(v) for v in vals}) == len(rs) + 2
        ok(x, full(ans) and not any(full(o) for o in x["o"][1:]), "EP set")
        continue
    if x["sec"] == "4.2.1" and "What equivalence partition coverage" in s:
        rs = [r for r in ranges(s.split("The tests")[0]) if r[0] <= r[1]]
        if len(rs) > 1 and rs[0][0] == rs[1][0] and rs[0][1] > rs[1][1]:
            rs = rs[1:]
        lo, hi = rs[0][0], rs[-1][1]
        vals = [int(v) for v in re.search(r"values ([-\d, ]+)\.", s).group(1).split(", ")]
        parts = {(-1 if v < lo else 99 if v > hi else next(i for i, (a, b) in enumerate(rs) if a <= v <= b)) for v in vals}
        ok(x, ans == pct(len(parts), len(rs) + 2), "EP coverage")
        continue
    if x["sec"] == "4.2.2" and ("2-value boundary value analysis" in s or "3-value boundary" in s) and "accept" not in s:
        head = s.split(" Which")[0].split(" How many")[0].split(" The tests")[0]
        rs = [r for r in ranges(head) if r[0] <= r[1]]
        if len(rs) > 1 and rs[0][0] == rs[1][0] and rs[0][1] > rs[1][1]:
            rs = rs[1:]
        bv = sorted({rs[0][0] - 1, rs[-1][1] + 1} | {a for a, b in rs} | {b for a, b in rs})
        if "Which set" in s:
            ok(x, ans == ", ".join(map(str, bv)), "BVA set")
        elif "How many coverage items" in s:
            ok(x, ans == str(len(bv)), "BVA count")
        elif "What 2-value" in s:
            vals = [int(v) for v in re.search(r"values ([-\d, ]+)\.", s).group(1).split(", ")]
            ok(x, ans == pct(len(set(vals) & set(bv)), len(bv)), "BVA coverage")
        elif "but NOT for 2-value" in s:
            v = int(ans)
            ok(x, v not in bv and any(abs(v - b) == 1 for b in bv), "3-value only")
            ok(x, all(int(o) in bv for o in x["o"][1:]), "3-value distractors are boundary values")
        continue
    if x["sec"] == "4.2.3" and "Boolean conditions. Before any columns" in s:
        n = int(re.search(r"has (\d+) Boolean", s).group(1))
        ok(x, ans == str(2 ** n), "DT 2^n")
        continue
    if x.get("code", "").startswith("Rule ") and "Which action" in s:
        lines = x["code"].splitlines()
        conds = [l for l in lines if l.startswith("C: ")]
        acts = [l for l in lines if l.startswith("A: ")]
        want = tuple("T" if v == "true" else "F" for v in re.findall(r"= (true|false)", s))
        ncol = len(lines[0].split()) - 1
        def cell(line, j):
            return line[26 + 5 * j: 31 + 5 * j].strip()
        col = next(j for j in range(ncol) if tuple(cell(c, j) for c in conds) == want)
        names = [a[3:26].strip() for a in acts]
        marked = [names[i] for i, a in enumerate(acts) if cell(a, col) == "X"]
        ok(x, ans == (" and ".join(marked) if marked else "no action"), "DT lookup")
        continue
    if x.get("code", "").startswith("Rule ") and "decision table coverage" in s:
        tests = re.search(r"C1, C2, C3\): ([TF; ]+)\.", s).group(1).split("; ")
        ok(x, ans == pct(len(set(tests)), 8), "DT coverage")
        continue
    if x["sec"] == "4.2.4" and x.get("code", "").startswith("State"):
        lines = x["code"].splitlines()
        events = lines[0].split()[1:]
        table = {}
        sts = []
        for l in lines[1:-1]:
            parts = l.split()
            sts.append(parts[0])
            for e, tgt in zip(events, parts[1:]):
                if tgt != "–":
                    table[(parts[0], e)] = tgt
        init = re.search(r"initial state: (\w+)", lines[-1]).group(1)
        def run(seq):
            st, vis, tr = init, [init], []
            for e in seq:
                if (st, e) not in table:
                    return False, vis, tr
                tr.append((st, e)); st = table[(st, e)]; vis.append(st)
            return True, vis, tr
        if "How many coverage items are there for valid" in s:
            ok(x, ans == str(len(table)), "ST valid count")
        elif "all transitions coverage?" in s:
            ok(x, ans == str(len(sts) * len(events)), "ST all count")
        elif "valid transitions coverage does" in s:
            seq = re.search(r"events: ([\w, ]+)\. What", s).group(1).split(", ")
            v, vis, tr = run(seq)
            ok(x, v and ans == pct(len(set(tr)), len(table)), "ST valid cov")
        elif "all states coverage does" in s:
            seq = re.search(r"events: ([\w, ]+)\. What", s).group(1).split(", ")
            v, vis, tr = run(seq)
            ok(x, v and ans == pct(len(set(vis)), len(sts)), "ST states cov")
        elif "INVALID" in s:
            okc = not run(ans.split(", "))[0]
            okd = all(run(o.split(", "))[0] for o in x["o"][1:])
            ok(x, okc and okd, "ST invalid seq")
        continue
    if x["sec"] == "5.1.5" and "Depends on" in x.get("code", ""):
        rows = [l.split() for l in x["code"].splitlines()[1:] if l and not l.startswith("(")]
        prio = {r[0]: int(r[1]) for r in rows}
        deps = {r[0]: ([] if r[2] == "–" else [d.strip(",") for d in r[2:]]) for r in rows}
        done, order = set(), []
        while len(order) < len(prio):
            avail = [t for t in prio if t not in done and all(d in done for d in deps[t])]
            t = min(avail, key=lambda z: prio[z]); order.append(t); done.add(t)
        if "execution order" in s:
            ok(x, ans == ", ".join(order), "prioritization order")
        else:
            k = int(re.search(r"position (\d+)", s).group(1))
            ok(x, ans == order[k - 1], "prioritization position")
        continue
    if x["sec"] == "5.1.5" and "Requirements covered" in x.get("code", ""):
        rows = [l.split(None, 1) for l in x["code"].splitlines()[1:]]
        cs = {r[0]: set(r[1].split(", ")) for r in rows}
        cov, order = set(), []
        while len(order) < len(cs):
            t = max((t for t in cs if t not in order), key=lambda z: (len(cs[z] - cov), -int(z[1:])))
            order.append(t); cov |= cs[t]
        ok(x, ans == order[1], "additional coverage")
        continue
    if x["sec"] == "5.1.5" and "Likelihood" in x.get("code", ""):
        rows = [l.split() for l in x["code"].splitlines()[1:]]
        lvl = {r[0]: int(r[1]) * int(r[2]) for r in rows}
        ok(x, ans == ", ".join(sorted(lvl, key=lambda z: -lvl[z])), "risk order")
        continue

# BVA defect-detection questions: the answer must expose the wrong implementation; distractors must not
for x in bank:
    m = re.search(r'"if \(x (≤|≥) (\d+)\) then accept"\. The developer implemented "if \(x = \d+\)', x["q"])
    if m:
        op, lim = m.group(1), int(m.group(2))
        good = (lambda v: v <= lim) if op == "≤" else (lambda v: v >= lim)
        bad = lambda v: v == lim
        ans = int(x["o"][0])
        ok(x, good(ans) != bad(ans), "BVA defect detected")
        ok(x, all(good(int(o)) == bad(int(o)) for o in x["o"][1:]), "BVA defect distractors do not detect")

# Hand-written white-box questions: execute equivalent Python code
def stmt_branch(fn, tests):
    stmts, branches = set(), set()
    for t in tests:
        fn(*t, stmts, branches)
    return stmts, branches

def prog1(a, b, S, B):
    B.add(("d1", a > 10))
    if a > 10: S.add("x=1")
    B.add(("d2", b > 5))
    if b > 5: S.add("y=2")

ALL_S1 = {"x=1", "y=2"}; ALL_B1 = {("d1", True), ("d1", False), ("d2", True), ("d2", False)}
from itertools import combinations
cands = [(a, b) for a in (5, 11) for b in (3, 6)]
def min_tests(goal_s, goal_b):
    for n in range(1, 5):
        for combo in combinations(cands, n):
            s, br = stmt_branch(prog1, combo)
            if goal_s <= s and goal_b <= br:
                return n
for x in bank:
    if x.get("code", "").startswith("IF a > 10"):
        if "statement coverage" in x["q"]:
            ok(x, x["o"][0] == str(min_tests(ALL_S1, set())), "min stmt tests")
        else:
            ok(x, x["o"][0] == str(min_tests(ALL_S1, ALL_B1)), "min branch tests")
    if "40 executable statements" in x["q"]:
        ok(x, x["o"][0] == pct(30, 40), "stmt pct")

print(f"Numeric answers re-derived independently: {checked} checks")
if failed:
    print("FAILED:")
    for f in failed:
        print(" -", f)
    sys.exit(1)
print("All numeric answers verified.")

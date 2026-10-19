#!/usr/bin/env python3
"""Builds data/glossary.json from tools/glossary_es.txt (definitions) and tools/glossary_code.txt (code examples),
and checks that every key term listed in data/syllabus.json has an entry.

Usage: python3 tools/build_glossary.py      (from the repo root; run tools/translate.py afterwards for English)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"

rows = []
for line in (TOOLS / "glossary_es.txt").read_text(encoding="utf-8").splitlines():
    if line.strip() and not line.startswith("#"):
        term, ch, definition, work = (x.strip() for x in line.split("|", 3))
        rows.append({"term": term, "ch": int(ch), "es": {"def": definition, "work": work}})
by = {r["term"].lower(): r for r in rows}
parts = re.split(r"^### (.+)$", (TOOLS / "glossary_code.txt").read_text(encoding="utf-8"), flags=re.M)[1:]
unknown = []
for term, code in zip(parts[::2], parts[1::2]):
    if term.lower() in by:
        by[term.lower()]["code"] = code.strip("\n")
    else:
        unknown.append(term)

syl = json.loads((ROOT / "data/syllabus.json").read_text())
needed = {t.lower() for c in syl["chapters"] for s in c["sections"] for lo in s["los"] for t in lo["terms"]}
missing = sorted(needed - set(by))
if unknown or missing or len(by) != len(rows):
    print("unknown code blocks:", unknown, "| missing terms:", missing, "| duplicates:", len(rows) - len(by))
    sys.exit(1)
(ROOT / "data/glossary.json").write_text(json.dumps(rows, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"{len(rows)} terms, {sum('code' in r for r in rows)} with code examples")

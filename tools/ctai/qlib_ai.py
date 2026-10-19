"""Question helper for the CT-AI v2.0 bank (same conventions as tools/qlib.py: correct option first)."""

# Learning objectives of the CT-AI Syllabus v2.0: LO -> (K-level, page where the section starts)
LOS = {
    "1.1.1": (2, 15), "1.1.2": (2, 15), "1.1.3": (2, 16), "1.1.4": (2, 17),
    "1.1.5": (2, 18), "1.1.6": (2, 18), "1.1.7": (2, 19), "1.1.8": (2, 20),
}

BANK = []
_counter = {}


def q(lo, stem, correct, distractors, expl):
    assert lo in LOS, lo
    assert len(distractors) == 3, (lo, stem)
    opts = [correct] + list(distractors)
    assert len(set(o.strip().lower() for o in opts)) == 4, ("duplicate option", lo, stem)
    _counter[lo] = _counter.get(lo, 0) + 1
    k, page = LOS[lo]
    item = {"id": f"AI-{lo}-{_counter[lo]:02d}", "lo": "AI-" + lo, "k": k, "ch": int(lo[0]), "sec": lo, "page": page,
            "q": stem.strip(), "o": [str(o).strip() for o in opts], "e": expl.strip()}
    BANK.append(item)
    return item

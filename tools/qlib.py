"""Shared helpers for authoring the question bank.

Every question is stored with the correct option first (index 0); the app shuffles
options at display time. Each question carries its learning objective (LO), K-level,
syllabus section and page so the app can link it to the study notes.
"""

# Learning objectives of the CTFL Syllabus v4.0.1: LO -> (K-level, page where the section starts)
LOS = {
    "1.1.1": (1, 15), "1.1.2": (2, 16), "1.2.1": (2, 16), "1.2.2": (1, 17), "1.2.3": (2, 17),
    "1.3.1": (2, 17), "1.4.1": (2, 18), "1.4.2": (2, 19), "1.4.3": (2, 20), "1.4.4": (2, 20),
    "1.4.5": (2, 21), "1.5.1": (2, 21), "1.5.2": (1, 22), "1.5.3": (2, 22),
    "2.1.1": (2, 25), "2.1.2": (1, 25), "2.1.3": (1, 26), "2.1.4": (2, 26), "2.1.5": (2, 27),
    "2.1.6": (2, 28), "2.2.1": (2, 28), "2.2.2": (2, 29), "2.2.3": (2, 30), "2.3.1": (2, 31),
    "3.1.1": (1, 33), "3.1.2": (2, 33), "3.1.3": (2, 34), "3.2.1": (1, 35), "3.2.2": (2, 35),
    "3.2.3": (1, 36), "3.2.4": (2, 36), "3.2.5": (1, 37),
    "4.1.1": (2, 39), "4.2.1": (3, 39), "4.2.2": (3, 40), "4.2.3": (3, 41), "4.2.4": (3, 41),
    "4.3.1": (2, 42), "4.3.2": (2, 43), "4.3.3": (2, 43), "4.4.1": (2, 43), "4.4.2": (2, 44),
    "4.4.3": (2, 44), "4.5.1": (2, 45), "4.5.2": (2, 45), "4.5.3": (3, 46),
    "5.1.1": (2, 48), "5.1.2": (1, 48), "5.1.3": (2, 49), "5.1.4": (3, 49), "5.1.5": (3, 50),
    "5.1.6": (1, 50), "5.1.7": (2, 51), "5.2.1": (1, 52), "5.2.2": (2, 52), "5.2.3": (2, 52),
    "5.2.4": (2, 53), "5.3.1": (1, 54), "5.3.2": (2, 54), "5.3.3": (2, 55), "5.4.1": (2, 56),
    "5.5.1": (3, 56), "6.1.1": (2, 59), "6.2.1": (1, 59),
}

BANK = []
_counter = {}


def q(lo, stem, correct, distractors, expl, code=None):
    assert lo in LOS, lo
    assert len(distractors) == 3, (lo, stem)
    opts = [correct] + list(distractors)
    assert len(set(o.strip().lower() for o in opts)) == 4, ("duplicate option", lo, stem)
    _counter[lo] = _counter.get(lo, 0) + 1
    k, page = LOS[lo]
    item = {
        "id": f"{lo}-{_counter[lo]:02d}",
        "lo": "FL-" + lo,
        "k": k,
        "ch": int(lo[0]),
        "sec": lo,
        "page": page,
        "q": stem.strip(),
        "o": [str(o).strip() for o in opts],
        "e": expl.strip(),
    }
    if code:
        item["code"] = code.strip("\n")
    BANK.append(item)
    return item

"""K3 application exercises whose answers are computed in code.

Every numeric answer is derived by the functions below (not typed by hand), and the
distractors are checked to be different from the correct answer.
"""
import random
from itertools import product
from qlib import q

R = random.Random(20261019)


def distinct(correct, candidates, n=3):
    out = []
    for c in candidates:
        c = str(c)
        if c != str(correct) and c not in out:
            out.append(c)
        if len(out) == n:
            return out
    raise ValueError(f"not enough distractors for {correct}: {candidates}")


def pct(n, d):
    v = 100 * n / d
    return f"{v:.0f}%" if abs(v - round(v)) < 1e-9 else f"{v:.1f}%"


def pct_pool(n, d):
    """Other coverage percentages for the same denominator, closest first."""
    others = sorted((i for i in range(1, d + 1) if i != n), key=lambda i: abs(i - n))
    return [pct(i, d) for i in others] + ["50%", "25%", "75%", "20%", "40%", "60%"]


# ============================================================================
# Ordered integer domains used by EP and BVA
# ============================================================================
DOMAINS = [
    ("A parcel service charges by weight in whole kilograms: 1–5 kg standard rate, 6–20 kg medium rate, 21–30 kg heavy rate. Weights below 1 kg or above 30 kg are rejected.",
     [(1, 5, "standard"), (6, 20, "medium"), (21, 30, "heavy")], "weight"),
    ("A cinema sets ticket prices by age in whole years: 0–12 child, 13–17 teen, 18–64 adult, 65–120 senior. Ages below 0 or above 120 are rejected as invalid.",
     [(0, 12, "child"), (13, 17, "teen"), (18, 64, "adult"), (65, 120, "senior")], "age"),
    ("An exam grading module accepts integer scores from 0 to 100: 0–49 fail, 50–69 pass, 70–89 merit, 90–100 distinction. Scores outside 0–100 are rejected.",
     [(0, 49, "fail"), (50, 69, "pass"), (70, 89, "merit"), (90, 100, "distinction")], "score"),
    ("A thermostat accepts integer set points from 10 to 30 °C. 10–17 °C activates eco mode, 18–24 °C comfort mode and 25–30 °C boost mode. Other values are rejected.",
     [(10, 17, "eco"), (18, 24, "comfort"), (25, 30, "boost")], "temperature"),
    ("A loan application accepts an integer loan term in months from 6 to 60: 6–12 short term, 13–36 medium term, 37–60 long term. Other terms are rejected.",
     [(6, 12, "short"), (13, 36, "medium"), (37, 60, "long")], "term"),
    ("A password field accepts lengths from 8 to 64 characters. Lengths 8–11 are rated weak, 12–19 good and 20–64 strong. Shorter or longer passwords are rejected.",
     [(8, 11, "weak"), (12, 19, "good"), (20, 64, "strong")], "length"),
    ("A shop gives a quantity discount for whole units ordered: 1–9 units no discount, 10–49 units 5%, 50–99 units 10%. Orders of 0 units or more than 99 units are rejected.",
     [(1, 9, "none"), (10, 49, "5%"), (50, 99, "10%")], "quantity"),
    ("An input field accepts an integer age from 18 to 65 inclusive. Any other integer is rejected.",
     [(18, 65, "valid")], "age"),
]


def partitions(valid):
    lo, hi = valid[0][0], valid[-1][1]
    parts = [("invalid (too low)", None, lo - 1)] + [(n, a, b) for a, b, n in valid] + [("invalid (too high)", hi + 1, None)]
    return parts


def which_part(parts, v):
    for i, (_, a, b) in enumerate(parts):
        if (a is None or v >= a) and (b is None or v <= b):
            return i
    raise ValueError(v)


def rep_value(a, b):
    if a is None:
        return b - R.randint(1, 5)
    if b is None:
        return a + R.randint(1, 20)
    return R.randint(a, b)


def gen_ep():
    for text, valid, name in DOMAINS:
        parts = partitions(valid)
        n = len(parts)
        # (a) minimum number of test values for 100% EP coverage
        q("4.2.1", f"{text} Using equivalence partitioning with both valid and invalid partitions, what is the minimum number of test values needed to achieve 100% equivalence partition coverage?",
          str(n), distinct(n, [n - 2, n + 1, n - 1, 2 * n - 2, n + 2]),
          f"Particiones: {', '.join(p[0] for p in parts)}. Son {n} en total (incluidas las 2 inválidas) y basta un valor por partición: {n} valores.")
        # (b) which set achieves 100% EP coverage
        correct = [rep_value(a, b) for _, a, b in parts]
        def miss_one(skip):
            vals = []
            for i, (_, a, b) in enumerate(parts):
                if i == skip:
                    continue
                vals.append(rep_value(a, b))
            j = R.randrange(len(vals))
            # replace the dropped partition with a second value from a different partition, keeping set size
            other = R.choice([k for k in range(n) if k != skip])
            _, a, b = parts[other]
            extra = rep_value(a, b)
            while extra in vals:
                extra = rep_value(a, b)
            vals.insert(j, extra)
            return vals
        ds, tries = [], 0
        while len(ds) < 3 and tries < 50:
            tries += 1
            cand = miss_one(R.randrange(n))
            covered = {which_part(parts, v) for v in cand}
            s = ", ".join(map(str, sorted(cand)))
            if len(covered) < n and s not in ds:
                ds.append(s)
        cs = ", ".join(map(str, sorted(correct)))
        assert len({which_part(parts, v) for v in correct}) == n
        q("4.2.1", f"{text} Which set of {name} values achieves 100% equivalence partition coverage (valid and invalid partitions)?",
          cs, ds,
          f"Hay {n} particiones ({', '.join(p[0] for p in parts)}). Solo esta opción toca todas; las demás repiten una partición y se dejan otra sin cubrir.")
        # (c) coverage achieved by a given set
        k = R.randint(2, n - 1)
        chosen = R.sample(range(n), k)
        vals = [rep_value(*parts[i][1:]) for i in chosen]
        # add a duplicate-partition value
        dup = R.choice(chosen)
        v2 = rep_value(*parts[dup][1:])
        vals.append(v2)
        covered = len({which_part(parts, v) for v in vals})
        ans = pct(covered, n)
        q("4.2.1", f"{text} The tests use the {name} values {', '.join(map(str, vals))}. What equivalence partition coverage do they achieve (counting valid and invalid partitions)?",
          ans, distinct(ans, [pct(len(vals), n) if len(vals) <= n else "100%", pct(covered - 1, n), pct(covered + 1, n), "100%", pct(covered, n - 2) if covered <= n - 2 else "50%"] + pct_pool(covered, n)),
          f"Los valores tocan {covered} de las {n} particiones: cobertura = {covered}/{n} = {ans}. Dos valores de la misma partición cuentan una sola vez.")


EACH_CHOICE = [
    ("payment method (card, bank transfer, PayPal)", 3, "delivery option (standard, express)", 2),
    ("customer type (new, regular, VIP, employee)", 4, "region (EU, non-EU)", 2),
    ("file format (PDF, DOCX, TXT, ODT, RTF)", 5, "page size (A4, Letter, A3)", 3),
    ("operating system (Windows, macOS, Linux)", 3, "browser (Chrome, Firefox, Safari, Edge)", 4),
    ("account type (basic, premium)", 2, "currency (EUR, USD, GBP, CHF)", 4),
]


def gen_each_choice():
    for a, na, b, nb in EACH_CHOICE:
        ans = max(na, nb)
        q("4.2.1", f"A form has two inputs: {a} and {b}. Each listed value is a valid equivalence partition. What is the minimum number of test cases needed to achieve 100% Each Choice coverage of the valid partitions?",
          str(ans), distinct(ans, [na * nb, na + nb, min(na, nb), ans + 1]),
          f"Each Choice exige ejercitar cada partición de cada conjunto al menos una vez, sin combinar. Cada test cubre un valor de cada entrada, así que el mínimo es el mayor de los dos conjuntos: max({na}, {nb}) = {ans}. Las {na}×{nb} = {na*nb} combinaciones no son necesarias.")


def boundary_values(valid):
    lo, hi = valid[0][0], valid[-1][1]
    bvs = {lo - 1, hi + 1}
    for a, b, _ in valid:
        bvs.update({a, b})
    return sorted(bvs)


def gen_bva():
    for text, valid, name in DOMAINS:
        bvs = boundary_values(valid)
        nb = len(bvs)
        # (a) which set gives 100% 2-value BVA
        cs = ", ".join(map(str, bvs))
        d1 = sorted(set(bvs) - {bvs[0], bvs[-1]})                       # forgets invalid side
        d2 = sorted({a for a, b, _ in valid} | {b for a, b, _ in valid})  # same as d1 normally
        mids = sorted({(a + b) // 2 for a, b, _ in valid})
        d3 = sorted(set(bvs[1:-1]) | {bvs[0] - 1, bvs[-1] + 1})
        d4 = sorted(set(bvs) - {bvs[len(bvs) // 2]})
        cands = [", ".join(map(str, d)) for d in (d1, d3, d4, sorted(set(mids) | {bvs[0], bvs[-1]}), d2)]
        q("4.2.2", f"{text} Which set of {name} values achieves 100% coverage with 2-value boundary value analysis?",
          cs, distinct(cs, cands),
          f"En el BVA de 2 valores los elementos de cobertura son todos los valores frontera: el mínimo y el máximo de cada partición, incluidas las fronteras de las inválidas ({bvs[0]} y {bvs[-1]}). Resultado: {cs}.")
        # (b) number of 2-value BVA coverage items
        q("4.2.2", f"{text} How many coverage items (boundary values) must be exercised to achieve 100% 2-value boundary value analysis coverage?",
          str(nb), distinct(nb, [nb - 2, nb + 2, len(valid) * 2, len(valid) + 1, nb + 1]),
          f"Valores frontera: {cs}. Son {nb} elementos de cobertura en el BVA de 2 valores.")
        # (c) 2-value BVA coverage achieved by a test set
        k = R.randint(max(2, nb // 2), nb - 1)
        tested = sorted(R.sample(bvs, k))
        inner = [a for a, b, _ in valid if b - a >= 4]
        extra = [(a + b) // 2 for a, b, _ in valid if b - a >= 4][:1]
        test_set = sorted(set(tested + extra))
        ans = pct(len(tested), nb)
        q("4.2.2", f"{text} The tests use the {name} values {', '.join(map(str, test_set))}. What 2-value boundary value analysis coverage do they achieve?",
          ans, distinct(ans, [pct(len(test_set), nb) if len(test_set) <= nb else "100%", pct(len(tested) - 1, nb), "100%", pct(len(tested) + 1, nb) if len(tested) + 1 <= nb else "50%", pct(len(tested), nb + 2)] + pct_pool(len(tested), nb)),
          f"Valores frontera ({nb}): {cs}. Los tests ejercitan {len(tested)}" + (f" (el valor {extra[0]} no es frontera)" if extra else "") + f": cobertura = {len(tested)}/{nb} = {ans}.")
        # (d) value that is a 3-value but not 2-value coverage item
        a, b, pname = R.choice([v for v in valid if v[1] - v[0] >= 3])
        good = R.choice([a + 1, b - 1])
        notgood = [x for x in [a, b, a - 1, b + 1] if x != good]
        q("4.2.2", f"{text} Which of the following {name} values is a coverage item for 3-value boundary value analysis but NOT for 2-value boundary value analysis?",
          str(good), distinct(good, notgood),
          f"En el BVA de 3 valores se prueba cada frontera y sus dos vecinos. {good} es vecino interior de una frontera de la partición {pname} ({a}–{b}) pero no es un valor frontera, así que solo aparece en el BVA de 3 valores. Los demás son valores frontera (elementos de los dos tipos).")


def gen_bva_defects():
    cases = [
        (10, "≤", "="), (100, "≤", "="), (18, "≥", "="), (50, "<", "≠"),
    ]
    for limit, op, wrong in [(10, "x ≤ 10", "x = 10"), (100, "x ≤ 100", "x = 100"), (18, "x ≥ 18", "x = 18"), (50, "x ≥ 50", "x = 50")]:
        if "≤" in op:
            two = (limit, limit + 1); detect = limit - 1
            others = [limit, limit + 1, limit + 2]
        else:
            two = (limit - 1, limit); detect = limit + 1
            others = [limit, limit - 1, limit - 2]
        q("4.2.2", f"The requirement says \"if ({op}) then accept\". The developer implemented \"if ({wrong}) then accept\". Which test value, derived from 3-value BVA but not from 2-value BVA, is likely to detect this defect?",
          str(detect), distinct(detect, others),
          f"El BVA de 2 valores usa {two[0]} y {two[1]}, y ambos dan el mismo resultado con la implementación errónea. El BVA de 3 valores añade el vecino {detect}, que debería aceptarse y la condición \"{wrong}\" rechaza: así se detecta el defecto (es el ejemplo del syllabus, con otros números).")


# ============================================================================
# Decision tables
# ============================================================================
def gen_dt_counts():
    for n in [2, 3, 4, 5]:
        ans = 2 ** n
        q("4.2.3", f"A limited-entry decision table has {n} Boolean conditions. Before any columns are removed or merged, how many columns (rules) does the full decision table contain?",
          str(ans), distinct(ans, [n * 2, n ** 2, 2 ** (n + 1), 2 ** (n - 1), n + 1]),
          f"Una tabla completa tiene una columna por cada combinación de condiciones: 2^{n} = {ans}.")


INFEASIBLE = [
    ("an insurance quote", ["driver is under 25", "driver is over 70", "car is a sports car"], lambda c: not (c[0] and c[1]),
     "a driver cannot be both under 25 and over 70"),
    ("a booking system", ["booking is for today", "booking is for a past date", "customer is a member"], lambda c: not (c[0] and c[1]),
     "a booking cannot be both for today and for a past date"),
    ("a ticket machine", ["payment by card", "payment by cash", "ticket is a return ticket", "passenger is a student"], lambda c: c[0] != c[1],
     "exactly one payment method must be used (card XOR cash)"),
    ("a parking system", ["vehicle is a motorbike", "vehicle is a truck", "parking time exceeds 4 hours"], lambda c: not (c[0] and c[1]),
     "a vehicle cannot be both a motorbike and a truck"),
]


def gen_dt_infeasible():
    for system, conds, ok, why in INFEASIBLE:
        n = len(conds)
        feasible = sum(1 for c in product([True, False], repeat=n) if ok(c))
        q("4.2.3", f"A decision table for {system} uses the Boolean conditions: " + "; ".join(f"C{i+1}: {t}" for i, t in enumerate(conds)) + f". Note that {why}. How many test cases are needed to achieve 100% decision table coverage, if infeasible columns are removed and no columns are merged?",
          str(feasible), distinct(feasible, [2 ** n, feasible - 1, feasible + 1, 2 ** (n - 1) if 2 ** (n - 1) != feasible else feasible + 2]),
          f"La tabla completa tiene 2^{n} = {2**n} columnas. Las combinaciones imposibles se eliminan ({2**n - feasible}) y quedan {feasible} columnas factibles. Los elementos de cobertura son las columnas factibles: {feasible} tests.")


def render_table(conds, rules, actions):
    # rules: list of (cond_values tuple of 'T'/'F'/'–', action values tuple of 'X'/'')
    head = "Rule".ljust(26) + "".join(f"R{i+1}".center(5) for i in range(len(rules)))
    lines = [head]
    for ci, c in enumerate(conds):
        lines.append(("C: " + c).ljust(26)[:26] + "".join(r[0][ci].center(5) for r in rules))
    for ai, a in enumerate(actions):
        lines.append(("A: " + a).ljust(26)[:26] + "".join((r[1][ai] or "").center(5) for r in rules))
    return "\n".join(lines)


def gen_dt_lookup():
    tables = [
        ("a discount engine",
         ["member", "order > €100", "coupon used"],
         ["10% discount", "5% discount", "free shipping"],
         lambda m, o, c: ("X" if m and o else "", "X" if (m != o) else "", "X" if (o or c) else "")),
        ("an online bank transfer",
         ["amount > €1,000", "new payee", "2FA confirmed"],
         ["execute transfer", "request 2FA", "flag for review"],
         lambda a, n, t: ("X" if (t or not (a or n)) else "", "X" if ((a or n) and not t) else "", "X" if (a and n) else "")),
        ("a library loan system",
         ["has overdue books", "member card valid", "book reserved by other"],
         ["lend book", "show warning", "refuse loan"],
         lambda o, v, r: ("X" if (v and not r and not o) else "", "X" if o else "", "X" if (not v or r) else "")),
    ]
    for system, conds, actions, f in tables:
        rules = []
        for combo in product([True, False], repeat=3):
            acts = f(*combo)
            rules.append((tuple("T" if x else "F" for x in combo), acts))
        code = render_table(conds, rules, actions)
        # pick 2 lookup questions per table
        for _ in range(2):
            idx = R.randrange(len(rules))
            combo, acts = rules[idx]
            want = [actions[i] for i in range(3) if acts[i] == "X"]
            ans = " and ".join(want) if want else "no action"
            # distractors: actions of other rules
            others = []
            for j, (cb, ac) in enumerate(rules):
                w = [actions[i] for i in range(3) if ac[i] == "X"]
                s = " and ".join(w) if w else "no action"
                others.append(s)
            singles = actions + [" and ".join(actions[:2]), " and ".join(actions[1:]), "no action"]
            desc = ", ".join(f"{conds[i]} = {'true' if combo[i]=='T' else 'false'}" for i in range(3))
            q("4.2.3", f"The full decision table below specifies {system}. A test case has: {desc}. Which action(s) should the system perform?",
              ans, distinct(ans, R.sample(others, len(others)) + singles),
              f"La combinación ({''.join(combo)}) corresponde a la regla R{idx+1}, que marca: {ans}. Para leer la tabla se busca la columna con esos valores de condición y se toman las acciones marcadas con X.",
              code=code)
        # coverage of a test set
        k = R.randint(3, 6)
        exercised = R.sample(range(8), k)
        tests = [rules[i][0] for i in exercised] + [rules[exercised[0]][0]]
        ans = pct(k, 8)
        q("4.2.3", f"For the decision table of {system} below, the executed tests have the condition values (in order C1, C2, C3): {'; '.join(''.join(t) for t in tests)}. What decision table coverage has been achieved?",
          ans, distinct(ans, [pct(len(tests), 8) if len(tests) <= 8 else "100%", pct(k - 1, 8), pct(k + 1, 8), "100%"] + pct_pool(k, 8)),
          f"Los tests ejercitan {k} columnas distintas de las 8 factibles (una combinación está repetida y cuenta una vez): {k}/8 = {ans}.",
          code=code)


def gen_dt_meaning():
    q("4.2.3", "In a decision table, a column shows \"–\" for condition C2. What does this mean?",
      "The value of C2 is irrelevant for the action outcome in that rule",
      ["C2 is infeasible in that rule", "C2 must be false", "The action should not occur"],
      "\"–\" significa que el valor de la condición no influye en el resultado de esa regla; \"N/A\" indica que la condición es imposible en esa regla.")
    q("4.2.3", "In decision table testing, what are the coverage items?",
      "The columns containing feasible combinations of conditions",
      ["Each individual condition", "Each action", "All columns, including infeasible ones"],
      "Los elementos de cobertura son las columnas con combinaciones factibles; cobertura = columnas ejercitadas / columnas factibles.")


# ============================================================================
# State transition testing
# ============================================================================
MACHINES = [
    {
        "name": "a door access controller",
        "initial": "Locked",
        "events": ["validCard", "invalidCard", "open", "close", "timeout"],
        "t": {("Locked", "validCard"): "Unlocked", ("Locked", "invalidCard"): "Alarm",
              ("Unlocked", "open"): "Open", ("Unlocked", "timeout"): "Locked",
              ("Open", "close"): "Locked", ("Alarm", "validCard"): "Locked"},
    },
    {
        "name": "a media player",
        "initial": "Stopped",
        "events": ["play", "pause", "stop", "end"],
        "t": {("Stopped", "play"): "Playing", ("Playing", "pause"): "Paused",
              ("Playing", "stop"): "Stopped", ("Playing", "end"): "Stopped",
              ("Paused", "play"): "Playing", ("Paused", "stop"): "Stopped"},
    },
    {
        "name": "an online order",
        "initial": "New",
        "events": ["pay", "cancel", "ship", "deliver", "return"],
        "t": {("New", "pay"): "Paid", ("New", "cancel"): "Cancelled",
              ("Paid", "ship"): "Shipped", ("Paid", "cancel"): "Cancelled",
              ("Shipped", "deliver"): "Delivered", ("Delivered", "return"): "Returned"},
    },
    {
        "name": "a login screen",
        "initial": "LoggedOut",
        "events": ["correctPwd", "wrongPwd", "logout", "unlock"],
        "t": {("LoggedOut", "correctPwd"): "LoggedIn", ("LoggedOut", "wrongPwd"): "Warning",
              ("Warning", "correctPwd"): "LoggedIn", ("Warning", "wrongPwd"): "Blocked",
              ("Blocked", "unlock"): "LoggedOut", ("LoggedIn", "logout"): "LoggedOut"},
    },
]


def states(m):
    s = [m["initial"]]
    for (a, _), b in m["t"].items():
        for x in (a, b):
            if x not in s:
                s.append(x)
    return s


def run(m, seq):
    st, visited, trans = m["initial"], [m["initial"]], []
    for e in seq:
        nxt = m["t"].get((st, e))
        if nxt is None:
            return None, visited, trans
        trans.append((st, e))
        st = nxt
        visited.append(st)
    return st, visited, trans


def state_table(m):
    ss = states(m)
    w = max(len(s) for s in ss) + 2
    cw = max(max(len(e) for e in m["events"]), max(len(s) for s in ss)) + 2
    lines = ["State".ljust(w) + "".join(e.center(cw) for e in m["events"])]
    for s in ss:
        lines.append(s.ljust(w) + "".join((m["t"].get((s, e)) or "–").center(cw) for e in m["events"]))
    lines.append(f"(initial state: {m['initial']}; \"–\" = invalid transition)")
    return "\n".join(lines)


def random_valid_seq(m, length):
    for _ in range(200):
        st, seq = m["initial"], []
        for _ in range(length):
            opts = [e for e in m["events"] if (st, e) in m["t"]]
            if not opts:
                break
            e = R.choice(opts)
            seq.append(e)
            st = m["t"][(st, e)]
        if len(seq) == length:
            return seq
    return seq


def gen_st():
    for m in MACHINES:
        code = state_table(m)
        ss = states(m)
        nv = len(m["t"])
        cells = len(ss) * len(m["events"])
        # (a) number of coverage items for valid transitions coverage
        q("4.2.4", f"The state table below models {m['name']}. How many coverage items are there for valid transitions coverage (0-switch coverage)?",
          str(nv), distinct(nv, [len(ss), cells, cells - nv, nv + 1]),
          f"En la cobertura de transiciones válidas, cada transición válida es un elemento de cobertura. Hay {nv} celdas no vacías (transiciones válidas).",
          code=code)
        # (b) number of coverage items for all transitions coverage
        q("4.2.4", f"The state table below models {m['name']}. How many coverage items are there for all transitions coverage?",
          str(cells), distinct(cells, [nv, cells - nv, len(ss), cells + len(ss)]),
          f"En la cobertura de todas las transiciones, los elementos de cobertura son todas las celdas de la tabla: {len(ss)} estados × {len(m['events'])} eventos = {cells} ({nv} válidas + {cells - nv} inválidas).",
          code=code)
        # (c) valid transitions coverage of a test
        seq = random_valid_seq(m, R.randint(3, 5))
        _, visited, trans = run(m, seq)
        distinct_t = len(set(trans))
        ans = pct(distinct_t, nv)
        q("4.2.4", f"The state table below models {m['name']}. A test case starts in the initial state and applies the events: {', '.join(seq)}. What valid transitions coverage does this test case achieve?",
          ans, distinct(ans, [pct(len(set(visited)), nv), pct(distinct_t, cells), pct(min(distinct_t + 1, nv), nv), pct(max(distinct_t - 1, 1), nv), pct(len(set(visited)), len(ss))] + pct_pool(distinct_t, nv)),
          f"La secuencia recorre las transiciones válidas {', '.join(f'{a}–{e}' for a, e in dict.fromkeys(trans))}: {distinct_t} distintas de {nv}. Cobertura = {distinct_t}/{nv} = {ans}.",
          code=code)
        # (d) all states coverage of a test
        seq = random_valid_seq(m, R.randint(2, 4))
        _, visited, trans = run(m, seq)
        vs = len(set(visited))
        ans = pct(vs, len(ss))
        q("4.2.4", f"The state table below models {m['name']}. A test case starts in the initial state and applies the events: {', '.join(seq)}. What all states coverage does it achieve?",
          ans, distinct(ans, [pct(len(set(trans)), len(ss)), pct(vs - 1, len(ss)), pct(min(vs + 1, len(ss)), len(ss)), pct(len(set(trans)), nv)] + pct_pool(vs, len(ss))),
          f"Estados visitados (incluido el inicial): {', '.join(dict.fromkeys(visited))}. Son {vs} de {len(ss)}: {ans}.",
          code=code)
        # (e) which sequence contains an invalid transition
        valid_seqs = []
        while len(valid_seqs) < 3:
            s = random_valid_seq(m, R.randint(2, 4))
            if s and ", ".join(s) not in valid_seqs:
                valid_seqs.append(", ".join(s))
        for _ in range(200):
            base = random_valid_seq(m, R.randint(1, 3))
            st, _, _ = run(m, base)
            bad = [e for e in m["events"] if (st, e) not in m["t"]]
            if bad:
                e = R.choice(bad)
                inval = base + [e]
                break
        q("4.2.4", f"The state table below models {m['name']}. Starting from the initial state, which event sequence attempts an INVALID transition?",
          ", ".join(inval), valid_seqs,
          f"Tras {', '.join(base) or '(ningún evento)'} el sistema está en {st}, donde el evento \"{inval[-1]}\" no está definido (celda vacía): es una transición inválida. Las demás secuencias solo usan transiciones válidas.",
          code=code)


def gen_st_concepts():
    q("4.2.4", "Which statement about the state transition coverage criteria is correct?",
      "Achieving 100% valid transitions coverage guarantees 100% all states coverage",
      ["Achieving 100% all states coverage guarantees 100% valid transitions coverage",
       "All transitions coverage only exercises invalid transitions",
       "Valid transitions coverage is weaker than all states coverage"],
      "Todos los estados es más débil que transiciones válidas; el 100 % de transiciones válidas garantiza el 100 % de estados, y todas las transiciones garantiza ambas.")
    q("4.2.4", "Why should only one invalid transition be tested in a single test case when aiming for all transitions coverage?",
      "To avoid defect masking, where one defect prevents the detection of another",
      ["Because invalid transitions cannot be automated",
       "Because each invalid transition requires a new test environment",
       "Because invalid transitions are not coverage items"],
      "Probar una sola transición inválida por caso evita el enmascaramiento de defectos.")


# ============================================================================
# ATDD (handwritten scenarios)
# ============================================================================
def gen_atdd():
    q("4.5.3", "User story: \"As a shopper, I want to apply a discount code so that I pay less.\" Acceptance criterion: \"A valid code reduces the total by 10%; an expired code shows the message 'Code expired' and does not change the total.\" Following ATDD, which test case should typically be written FIRST?",
      "Apply a valid code to a €50 cart; the total becomes €45",
      ["Apply an expired code; the message 'Code expired' appears and the total is unchanged",
       "Apply 1,000 codes per second to measure response time",
       "Check that the discount code field uses the corporate font"],
      "En ATDD se empieza normalmente por los casos positivos, después los negativos y finalmente los no funcionales.")
    q("4.5.3", "In ATDD, what is the first step of the process?",
      "A specification workshop where the user story and its acceptance criteria are analysed, discussed and written",
      ["Writing the production code", "Running the regression suite", "Writing the test completion report"],
      "El primer paso es un taller de especificación donde se analizan y escriben la historia y sus criterios de aceptación, resolviendo ambigüedades.")
    q("4.5.3", "User story: \"As a registered user, I want to reset my password by email.\" Acceptance criteria: AC1 a reset link is sent to the registered email; AC2 the link expires after 30 minutes. Which test case is derived correctly using ATDD?",
      "Given a registered user requests a reset, when 31 minutes pass and the link is used, then the system rejects the link as expired",
      ["Given any user, when they log in, then the dashboard loads in under 1 second",
       "Given a registered user, when they change their profile picture, then it is saved",
       "Given the database, when it is backed up, then the backup is encrypted"],
      "Los tests de ATDD se basan en los criterios de aceptación de la historia y no van más allá de ella. Este cubre AC2; las otras opciones prueban funcionalidades fuera de la historia.")
    q("4.5.3", "Which statement about test cases created with ATDD is correct?",
      "They must cover all the characteristics of the user story and should not go beyond the story",
      ["They should cover additional features not in the story to increase coverage",
       "Two test cases should describe the same characteristic for redundancy",
       "They must always be written in a programming language"],
      "Los tests deben cubrir todas las características de la historia sin ir más allá, y no debe haber dos tests que describan la misma característica.")
    q("4.5.3", "In ATDD, after the positive test cases are done, what should the team do next?",
      "Perform negative testing",
      ["Stop testing and release", "Write the user story", "Measure statement coverage only"],
      "Orden típico: casos positivos → casos negativos → características no funcionales (p. ej., eficiencia, usabilidad).")
    q("4.5.3", "User story: \"As a bank customer, I want to withdraw cash up to my balance.\" Acceptance criteria: withdrawals up to the balance succeed; withdrawals above the balance are refused with the message 'Insufficient funds'. The balance is €200. Which pair of test cases best covers these criteria using ATDD with BVA?",
      "Withdraw €200 (succeeds) and withdraw €201 (refused with 'Insufficient funds')",
      ["Withdraw €100 (succeeds) and withdraw €150 (succeeds)",
       "Withdraw €0 (succeeds) and withdraw €1,000,000 (succeeds)",
       "Withdraw €200 (refused) and withdraw €201 (succeeds)"],
      "En el diseño de tests de ATDD pueden aplicarse técnicas como BVA: el límite (200) debe aceptarse y el siguiente valor (201) rechazarse con el mensaje.")
    q("4.5.3", "Who creates the test cases in ATDD?",
      "Team members with different perspectives, e.g., customers, developers and testers; or the tester individually after the workshop",
      ["Only an external test team after implementation", "Only the developers, after coding", "Only the product owner, alone"],
      "Los casos se crean con perspectivas distintas (cliente, desarrollador, tester); tras el taller pueden escribirlos el equipo entero o el tester.")
    q("4.5.3", "How are ATDD test cases typically expressed?",
      "In natural language understandable to stakeholders, including preconditions, inputs and postconditions",
      ["Only as assembly code", "Only as screenshots", "Only as SQL queries"],
      "Deben ser comprensibles para los stakeholders: frases en lenguaje natural con precondiciones, entradas y postcondiciones.")
    q("4.5.3", "What happens when ATDD test cases are captured in a format supported by a test automation framework?",
      "Developers can automate them while implementing the feature, and the acceptance tests become executable requirements",
      ["They can no longer be executed manually", "They replace the user story", "They must be rewritten as unit tests"],
      "Así las pruebas de aceptación se convierten en requisitos ejecutables.")
    q("4.5.3", "User story: \"As a user, I want to upload a profile photo.\" AC: JPG and PNG files up to 5 MB are accepted; other formats are rejected with 'Unsupported format'; larger files are rejected with 'File too large'. Which set of ATDD test cases covers all the acceptance criteria with no two tests describing the same characteristic?",
      "Upload a 2 MB JPG (accepted); upload a 2 MB GIF (rejected: 'Unsupported format'); upload a 6 MB PNG (rejected: 'File too large')",
      ["Upload a 2 MB JPG (accepted); upload a 3 MB JPG (accepted); upload a 4 MB JPG (accepted)",
       "Upload a 2 MB GIF (rejected); upload a 3 MB BMP (rejected)",
       "Upload a 6 MB PNG (accepted); upload a 2 MB GIF (accepted)"],
      "Hace falta un caso por característica: formato aceptado, formato no soportado y tamaño excesivo. Repetir el mismo caso positivo no aporta, y la última opción contradice los criterios.")


# ============================================================================
# 5.1.4 Estimation
# ============================================================================
def three_point_values():
    out = []
    while len(out) < 6:
        a = R.randint(2, 20)
        b = a + 6 * R.randint(1, 5)
        for m in range(a + 1, b):
            if (a + 4 * m + b) % 6 == 0 and m != (a + b) // 2:
                out.append((a, m, b))
                break
    return out


def gen_estimation():
    unit = ["person-days", "person-hours", "person-days", "person-hours", "person-days", "person-hours"]
    for i, (a, m, b) in enumerate(three_point_values()):
        E = (a + 4 * m + b) // 6
        SD = (b - a) // 6
        u = unit[i]
        if i % 2 == 0:
            ans = f"{E} ± {SD} {u}"
            ds = [f"{(a+m+b)//3} ± {SD} {u}", f"{E} ± {SD+1} {u}", f"{m} ± {SD} {u}", f"{E+1} ± {SD} {u}"]
            q("5.1.4", f"Using three-point estimation, experts estimate a test task as: most optimistic a = {a}, most likely m = {m}, most pessimistic b = {b} {u}. What are the estimate and the standard deviation?",
              ans, distinct(ans, ds),
              f"E = (a + 4m + b) / 6 = ({a} + {4*m} + {b}) / 6 = {E}. SD = (b − a) / 6 = ({b} − {a}) / 6 = {SD}. Resultado: {E} ± {SD} {u}.")
        else:
            lo, hi = E - SD, E + SD
            ans = f"Between {lo} and {hi} {u}"
            ds = [f"Between {a} and {b} {u}", f"Between {E-2*SD} and {E+2*SD} {u}", f"Between {m-SD} and {m+SD} {u}", f"Between {lo+1} and {hi+1} {u}"]
            q("5.1.4", f"Three-point estimation for a test activity gives a = {a}, m = {m} and b = {b} {u}. Using E = (a + 4m + b)/6 and SD = (b − a)/6, which range (E ± SD) should be reported?",
              ans, distinct(ans, ds),
              f"E = ({a} + 4×{m} + {b}) / 6 = {E}; SD = ({b} − {a}) / 6 = {SD}. Rango: {E} − {SD} a {E} + {SD} = {lo}–{hi} {u}.")
    # ratios
    for dev, (p, t) in [(600, (3, 2)), (450, (3, 1)), (800, (4, 1)), (360, (2, 1)), (500, (5, 2))]:
        ans = dev * t // p
        q("5.1.4", f"In previous similar projects, the development-to-test effort ratio was {p}:{t}. The development effort of the new project is estimated at {dev} person-days. Using estimation based on ratios, what is the estimated test effort?",
          f"{ans} person-days", distinct(f"{ans} person-days", [f"{dev*p//t} person-days", f"{dev - ans} person-days", f"{dev*t//(p+t)} person-days", f"{ans+dev//10} person-days"]),
          f"Esfuerzo de prueba = desarrollo × {t}/{p} = {dev} × {t}/{p} = {ans} días-persona (estimación basada en ratios, una técnica basada en métricas).")
    # extrapolation: average of last iterations
    for vals in [(30, 36, 33), (40, 44, 48), (25, 31, 28), (52, 47, 51), (18, 22, 20)]:
        s = sum(vals)
        if s % 3:
            continue
        avg = s // 3
        q("5.1.4", f"The test effort in the last three iterations was {vals[0]}, {vals[1]} and {vals[2]} person-hours. Using extrapolation as the average of the last three iterations, what is the estimated test effort for the next iteration?",
          f"{avg} person-hours", distinct(f"{avg} person-hours", [f"{vals[-1]} person-hours", f"{max(vals)} person-hours", f"{s} person-hours", f"{avg+3} person-hours", f"{vals[0]} person-hours", f"{min(vals)} person-hours", f"{avg-2} person-hours"]),
          f"Extrapolación (media de las últimas tres iteraciones): ({vals[0]} + {vals[1]} + {vals[2]}) / 3 = {avg} horas-persona.")
    # extrapolation per item
    for done, hours, remaining in [(40, 120, 60), (25, 100, 75), (50, 150, 30)]:
        rate = hours / done
        ans = int(rate * remaining)
        q("5.1.4", f"So far, executing {done} test cases took {hours} person-hours. {remaining} test cases remain, and they are of similar complexity. Using extrapolation from the data gathered in this project, how much effort will the remaining test cases need?",
          f"{ans} person-hours", distinct(f"{ans} person-hours", [f"{hours} person-hours", f"{int(rate*(done+remaining))} person-hours", f"{remaining} person-hours", f"{int(hours/remaining*done)} person-hours"]),
          f"Ritmo medido: {hours}/{done} = {rate:g} h por caso. Restantes: {remaining} × {rate:g} = {ans} horas-persona.")
    q("5.1.4", "Experts estimate the test effort in isolation. Estimates outside the agreed boundaries are discussed, and the experts estimate again in isolation until consensus is reached. Which estimation technique is this?",
      "Wideband Delphi",
      ["Three-point estimation", "Estimation based on ratios", "Extrapolation"],
      "Wideband Delphi es una técnica iterativa basada en expertos; Planning Poker es una variante.")


# ============================================================================
# 5.1.5 Test case prioritization
# ============================================================================
def order_greedy(prio, deps):
    done, order = set(), []
    while len(order) < len(prio):
        avail = [t for t in prio if t not in done and all(d in done for d in deps.get(t, []))]
        t = min(avail, key=lambda x: (prio[x], x))
        order.append(t); done.add(t)
    return order


def order_prereq_first(prio, deps):
    done, order = set(), []
    def run(t):
        for d in sorted(deps.get(t, []), key=lambda x: (prio[x], x)):
            if d not in done:
                run(d)
        if t not in done:
            order.append(t); done.add(t)
    for t in sorted(prio, key=lambda x: (prio[x], x)):
        run(t)
    return order


def gen_prioritization():
    made = 0
    attempts = 0
    while made < 7 and attempts < 5000:
        attempts += 1
        n = R.randint(5, 6)
        ts = [f"TC{i+1}" for i in range(n)]
        prios = R.sample(range(1, n + 1), n)
        prio = dict(zip(ts, prios))
        deps = {}
        for t in ts:
            if R.random() < 0.35:
                d = R.choice([x for x in ts if x != t])
                deps[t] = [d]
        # no cycles
        try:
            o1 = order_greedy(prio, deps); o2 = order_prereq_first(prio, deps)
        except (ValueError, RecursionError):
            continue
        if not deps or o1 != o2 or len(o1) != n:
            continue
        if all(prio[o1[i]] < prio[o1[i+1]] for i in range(n - 1)):
            continue  # dependencies did not change anything: too easy
        table = "Test case  Priority  Depends on\n" + "\n".join(f"{t:<10} {prio[t]:<9} {', '.join(deps.get(t, [])) or '–'}" for t in ts)
        table += "\n(priority 1 = highest)"
        ans = ", ".join(o1)
        naive = ", ".join(sorted(ts, key=lambda x: prio[x]))
        rev = ", ".join(sorted(ts, key=lambda x: -prio[x]))
        shuffled = o1[:]
        for _ in range(10):
            i, j = R.sample(range(n), 2)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
            if shuffled != o1:
                break
        q("5.1.5", "The test cases below must be executed in priority order, but a test case can only be executed after the test case it depends on. Which execution order is correct?",
          ans, distinct(ans, [naive, ", ".join(shuffled), rev, ", ".join(sorted(ts))]),
          "Se ejecuta primero la de mayor prioridad cuyas dependencias ya se hayan cumplido. Si una prueba de alta prioridad depende de otra de menor prioridad, esa otra debe ir antes. Resultado: " + ans + ".",
          code=table)
        made += 1
    # which test runs in position k
    made = 0
    while made < 3 and attempts < 10000:
        attempts += 1
        n = 6
        ts = [f"T{i+1}" for i in range(n)]
        prio = dict(zip(ts, R.sample(range(1, n + 1), n)))
        deps = {}
        for t in ts:
            if R.random() < 0.4:
                deps[t] = [R.choice([x for x in ts if x != t])]
        try:
            o1 = order_greedy(prio, deps); o2 = order_prereq_first(prio, deps)
        except (ValueError, RecursionError):
            continue
        if not deps or o1 != o2:
            continue
        k = R.randint(2, 4)
        if o1[k - 1] == sorted(ts, key=lambda x: prio[x])[k - 1]:
            continue  # the dependency must change the answer
        table = "Test  Priority  Depends on\n" + "\n".join(f"{t:<5} {prio[t]:<9} {', '.join(deps.get(t, [])) or '–'}" for t in ts) + "\n(priority 1 = highest)"
        ans = o1[k - 1]
        naive = sorted(ts, key=lambda x: prio[x])[k - 1]
        q("5.1.5", f"Considering priorities and dependencies in the table below, which test will be executed in position {k}?",
          ans, distinct(ans, [naive] + [t for t in ts if t != ans]),
          f"Orden de ejecución respetando prioridades y dependencias: {', '.join(o1)}. En la posición {k} va {ans}.",
          code=table)
        made += 1
    # additional coverage prioritization
    cov_sets = [
        {"T1": {1, 2, 3, 4}, "T2": {1, 2, 3, 4, 5}, "T3": {6, 7}, "T4": {5, 6}, "T5": {8}},
        {"T1": {1, 2}, "T2": {1, 2, 3, 4, 5, 6}, "T3": {5, 6, 7, 8}, "T4": {7, 8, 9}, "T5": {1, 9}},
    ]
    for cs in cov_sets:
        covered, order = set(), []
        while len(order) < len(cs):
            t = max((t for t in cs if t not in order), key=lambda x: (len(cs[x] - covered), -int(x[1:])))
            order.append(t); covered |= cs[t]
        table = "Test  Requirements covered\n" + "\n".join(f"{t:<5} {', '.join(f'R{r}' for r in sorted(v))}" for t, v in cs.items())
        ans = order[1]
        by_total = sorted(cs, key=lambda x: (-len(cs[x]), int(x[1:])))[1]
        q("5.1.5", "Using additional coverage prioritization (the test with the highest coverage first, then each next test is the one adding the most additional coverage), which test is executed SECOND?",
          ans, distinct(ans, [by_total] + [t for t in cs if t != ans]),
          f"Primero va {order[0]} ({len(cs[order[0]])} requisitos). Después, la que más cobertura adicional aporta es {ans}. Orden completo: {', '.join(order)}.",
          code=table)
    # risk-based prioritization (quantitative risk level)
    for _ in range(2):
        ts = ["T1", "T2", "T3", "T4"]
        while True:
            like = {t: R.randint(1, 5) for t in ts}
            imp = {t: R.randint(1, 5) for t in ts}
            lvl = {t: like[t] * imp[t] for t in ts}
            if len(set(lvl.values())) == 4:
                break
        table = "Test  Likelihood  Impact\n" + "\n".join(f"{t:<5} {like[t]:<11} {imp[t]}" for t in ts)
        order = sorted(ts, key=lambda x: -lvl[x])
        ans = ", ".join(order)
        by_imp = ", ".join(sorted(ts, key=lambda x: (-imp[x], x)))
        by_like = ", ".join(sorted(ts, key=lambda x: (-like[x], x)))
        q("5.1.5", "Using risk-based prioritization with a quantitative risk level (likelihood × impact, scale 1–5), in which order should the tests be executed?",
          ans, distinct(ans, [by_imp, by_like, ", ".join(reversed(order)), ", ".join(ts)]),
          "Nivel de riesgo = probabilidad × impacto: " + ", ".join(f"{t} = {like[t]}×{imp[t]} = {lvl[t]}" for t in ts) + f". Se ejecuta de mayor a menor: {ans}.",
          code=table)


def build_all():
    gen_ep(); gen_each_choice()
    gen_bva(); gen_bva_defects()
    gen_dt_counts(); gen_dt_infeasible(); gen_dt_lookup(); gen_dt_meaning()
    gen_st(); gen_st_concepts()
    gen_atdd()
    gen_estimation()
    gen_prioritization()

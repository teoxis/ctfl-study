#!/usr/bin/env python3
"""Builds data/i18n.json: the other-language half of every text, so the app can switch ES/EN.

The bank is written with questions/options in English and explanations in Spanish; the syllabus notes are in
Spanish with English titles. This script asks an OpenAI-compatible model for the missing half and validates
every answer mechanically (same ids, same option count, same numbers, right language). It is incremental:
items whose source text has not changed since the last run are skipped.

Usage:  LLM_URL=http://127.0.0.1:8080/v1 LLM_KEY=... LLM_MODEL=... python3 tools/translate.py [--limit N] [--chapter N] [--cert ctai]
        python3 tools/translate.py --check      (validate data/i18n.json against the bank, no model calls)
"""
import hashlib
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = DATA / "i18n.json"
BATCH = 6

# ISTQB terms with their usual Spanish rendering (SSTQB). Given to the model so both directions stay consistent.
TERMS = """test basis = base de prueba; test object = objeto de prueba; test case = caso de prueba;
test condition = condición de prueba; test procedure = procedimiento de prueba; test suite = juego de pruebas;
test plan = plan de prueba; test level = nivel de prueba; test type = tipo de prueba; test item = elemento de prueba;
test objective = objetivo de prueba; test oracle = oráculo de prueba; test data = datos de prueba;
test environment = entorno de prueba; testware = productos de prueba (testware); test completion = cierre de las pruebas;
test monitoring = monitorización de las pruebas; test control = control de las pruebas; test analysis = análisis de las pruebas;
test design = diseño de las pruebas; test implementation = implementación de las pruebas; test execution = ejecución de las pruebas; tester = tester;
defect = defecto; failure = fallo; error = error (equivocación); root cause = causa raíz; debugging = depuración;
static testing = prueba estática; dynamic testing = prueba dinámica; review = revisión; inspection = inspección;
walkthrough = revisión guiada; technical review = revisión técnica; informal review = revisión informal;
equivalence partitioning = partición de equivalencia; boundary value analysis = análisis de valores frontera;
decision table testing = prueba de tabla de decisión; state transition testing = prueba de transición de estados;
statement coverage = cobertura de sentencia; branch coverage = cobertura de rama; coverage item = elemento de cobertura;
white-box testing = prueba de caja blanca; black-box testing = prueba de caja negra;
experience-based testing = prueba basada en la experiencia; error guessing = predicción de errores;
exploratory testing = prueba exploratoria; checklist-based testing = prueba basada en listas de comprobación;
test charter = test charter; acceptance criteria = criterios de aceptación; user story = historia de usuario;
acceptance test-driven development (ATDD) = desarrollo guiado por pruebas de aceptación (ATDD);
component testing = prueba de componente; integration testing = prueba de integración; system testing = prueba de sistema;
acceptance testing = prueba de aceptación; functional testing = prueba funcional; non-functional testing = prueba no funcional;
confirmation testing = prueba de confirmación; regression testing = prueba de regresión; maintenance testing = prueba de mantenimiento;
risk = riesgo; product risk = riesgo de producto; project risk = riesgo de proyecto; risk-based testing = prueba basada en riesgos;
risk level = nivel de riesgo; entry criteria = criterios de entrada; exit criteria = criterios de salida;
test pyramid = pirámide de prueba; testing quadrants = cuadrantes de prueba; shift left = shift left (desplazamiento a la izquierda);
defect report = informe de defecto; test progress report = informe de avance de la prueba; test completion report = informe de cierre de las pruebas;
configuration management = gestión de la configuración; stakeholder = parte interesada (stakeholder);
whole team approach = enfoque de equipo completo; scribe = escriba; review leader = líder de la revisión; moderator = moderador;
verification = verificación; validation = validación; quality assurance = aseguramiento de la calidad; quality control = control de la calidad;
DevOps, CI/CD, sprint, backlog, mock, stub, driver = se dejan en inglés"""

SYSTEM = ("You are a professional technical translator for ISTQB Certified Tester Foundation Level material. "
          "Translate faithfully: keep meaning, numbers, variable names, quoted values, symbols and section numbers exactly. "
          "Do not add, drop or explain anything. Use this terminology, in either direction:\n" + TERMS +
          "\nReply with JSON only, with exactly the same keys and structure as the input.")


# Terms the model got wrong despite the list above, fixed after review: (regex, replacement) on Spanish output.
POST_FIX = [(r"enfoque de todo el equipo", "enfoque de equipo completo"), (r"Actuario \(secretario\)", "Escriba"),
            (r"(?i)\bactuario\b", "escriba"), (r"líder de la revisión o acta\b", "líder de la revisión o escriba"),
            # Literal renderings that sound unnatural in Spanish; working testers say it this way.
            (r"\bprobadores\b", "testers"), (r"\bprobador\b", "tester"), (r"\bProbadores\b", "Testers"), (r"\bProbador\b", "Tester"),
            (r"(?i)compleción de (la|las) pruebas?", "cierre de las pruebas"), (r"compleción", "cierre"), (r"Compleción", "Cierre"),
            (r"(?i)contratos? de prueba", "test charter"), (r"(?i)compleción", "cierre"), (r"\bun métrica", "una métrica"),
            (r"enfoque de equipo completo \(whole[- ]team\)", "enfoque de equipo completo"),
            (r"\b(análisis|diseño|implementación|ejecución|planificación|monitorización|control|gestión|estado|avance|valor|resultados) de la prueba\b", r"\1 de las pruebas"),
            (r"\b(plan|planes|estrategia|esfuerzo|proceso|equipo|equipos|actividades|prácticas) de prueba\b", r"\1 de pruebas")]


def postfix(x):
    if isinstance(x, str):
        for a, b in POST_FIX:
            x = re.sub(a, b, x)
        return x
    if isinstance(x, list):
        return [postfix(i) for i in x]
    if isinstance(x, dict):
        return {k: postfix(v) for k, v in x.items()}
    return x


def h(obj):
    return hashlib.sha1(json.dumps(obj, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:12]


def nums(s):
    # Decimal comma and thousands dot differ by language: compare the digits, not the separator.
    return sorted(x.replace(",", ".") for x in re.findall(r"\d+(?:[.,]\d+)?", json.dumps(s, ensure_ascii=False)))


ES_WORDS = re.compile(r"\b(el|la|los|las|que|una|un|del|de|en|y|para|es|se|por|con|no|al|lo|su|sus|pueden|puede)\b", re.I)
EN_WORDS = re.compile(r"\b(the|of|and|is|to|which|that|for|with|are|not|a|an|in|on|be|can|their|by|it|does|do)\b", re.I)


def ratio(rx, text):
    words = re.findall(r"[A-Za-zÁÉÍÓÚáéíóúñÑüÜ]+", text)
    return len(rx.findall(text)) / max(len(words), 1)


def flat(x):
    if isinstance(x, str):
        return [x]
    if isinstance(x, list):
        return [s for y in x for s in flat(y)]
    if isinstance(x, dict):
        return [s for y in x.values() for s in flat(y)]
    return []


def same_shape(a, b):
    if isinstance(a, dict):
        return isinstance(b, dict) and a.keys() == b.keys() and all(same_shape(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return isinstance(b, list) and len(a) == len(b) and all(same_shape(x, y) for x, y in zip(a, b))
    return isinstance(b, str) and b.strip() != ""


def valid(src, out, target):
    """Returns '' if out is an acceptable translation of src into target ('es' or 'en'), else the reason."""
    if not same_shape(src, out):
        return "shape"
    if nums(src) != nums(out):
        return "numbers"
    text = " ".join(flat(out))
    if text == " ".join(flat(src)):
        return "unchanged"
    es, en = ratio(ES_WORDS, text), ratio(EN_WORDS, text)
    if len(text) > 25 and ((target == "es" and es <= en) or (target == "en" and en <= es)):
        return "language"  # whichever language dominates must be the target
    la, lb = len(" ".join(flat(src))), len(text)
    if lb < 0.5 * la or lb > 2.0 * la:
        return "length"
    return ""


def jobs():
    """Every translatable unit: (key, kind, target, source dict)."""
    for f in sorted(DATA.glob("bank-ch*.json")):
        for q in json.loads(f.read_text()):
            # Pure-number options stay as they are; only words are translated.
            yield "q:" + q["id"], "es", {"q": q["q"], "o": q["o"]}
            yield "e:" + q["id"], "en", {"e": q["e"]}
    for g in json.loads((DATA / "glossary.json").read_text()):
        yield f"gl:{g['term']}", "en", g["es"]
    syl = json.loads((DATA / "syllabus.json").read_text())
    for ch in syl["chapters"]:
        yield f"ch:{ch['ch']}", "es", {"title": ch["title"]}
        for s in ch["sections"]:
            yield f"sec:{s['sec']}", "es", {"title": s["title"]}
            for lo in s["los"]:
                yield "lo:" + lo["lo"], "es", {"title": lo["title"], "stmt": lo["stmt"]}
                src = {"sum": lo["sum"]}
                if lo.get("example"):
                    src["example"] = lo["example"]
                yield "lonote:" + lo["lo"], "en", src


def call(items, target):
    lang = "Spanish (Spain)" if target == "es" else "English"
    payload = {k: v for k, v in items}
    body = {"model": os.environ.get("LLM_MODEL", "agente"), "temperature": 0.1, "max_tokens": 6000,
            "response_format": {"type": "json_object"},
            "messages": [{"role": "system", "content": SYSTEM},
                         {"role": "user", "content": f"Translate every string value into {lang}. Keep the keys.\n"
                                                     + json.dumps(payload, ensure_ascii=False)}]}
    req = urllib.request.Request(os.environ["LLM_URL"].rstrip("/") + "/chat/completions", data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json",
                                          "Authorization": "Bearer " + os.environ.get("LLM_KEY", "")})
    r = json.load(urllib.request.urlopen(req, timeout=900))
    txt = r["choices"][0]["message"]["content"].strip()
    txt = re.sub(r"^```(?:json)?\s*|\s*```$", "", txt)
    return json.loads(txt)


def load():
    return json.loads(OUT.read_text()) if OUT.exists() else {"v": 1, "items": {}}


def save(db):
    tmp = OUT.with_suffix(".tmp")  # atomic replace: a reader never sees a half-written file
    tmp.write_text(json.dumps(db, ensure_ascii=False, separators=(",", ":"), sort_keys=True), encoding="utf-8")
    tmp.replace(OUT)


def check():
    db, bad, missing = load(), 0, 0
    for key, target, src in jobs():
        it = db["items"].get(key)
        if not it or it["h"] != h(src):
            missing += 1
            continue
        # Items marked "m" were translated or reviewed by hand: only their structure and numbers are checked.
        why = ("" if same_shape(src, it["t"]) else "shape") if it.get("m") else valid(src, it["t"], target)
        if why:
            bad += 1
            print("INVALID", key, why)
    print(f"{len(db['items'])} stored · {missing} missing or stale · {bad} invalid")
    return 1 if bad or missing else 0


def main(argv):
    global DATA, OUT
    if "--cert" in argv:  # e.g. --cert ctai -> data/ctai/
        DATA = ROOT / "data" / argv[argv.index("--cert") + 1]
        OUT = DATA / "i18n.json"
    if "--check" in argv:
        return check()
    if "--fix" in argv:  # re-apply POST_FIX to stored Spanish translations
        db = load()
        for k, v in db["items"].items():
            if k.split(":")[0] in ("q", "lo", "sec", "ch"):
                v["t"] = postfix(v["t"])
        save(db)
        return 0
    limit = int(argv[argv.index("--limit") + 1]) if "--limit" in argv else 10 ** 9
    db = load()
    todo = [(k, t, s) for k, t, s in jobs() if db["items"].get(k, {}).get("h") != h(s)]
    if "--chapter" in argv:  # translate one chapter first (its questions, notes and glossary terms)
        n = argv[argv.index("--chapter") + 1]
        gl = {"gl:" + g["term"] for g in json.loads((DATA / "glossary.json").read_text()) if str(g["ch"]) in (n, "0")}
        todo = [j for j in todo if j[0] in gl or j[0] == "ch:" + n or j[0].split(":", 1)[1].startswith(n + ".")]
    todo = todo[:limit]
    print(f"{len(todo)} items to translate", flush=True)
    failed, t0 = [], time.time()
    for target in ("es", "en"):
        group = [(k, s) for k, t, s in todo if t == target]
        i = 0
        while i < len(group):
            chunk = group[i:i + BATCH]
            i += BATCH
            for attempt in range(3):
                size = len(chunk) if attempt == 0 else 1  # on failure, retry item by item
                pending = [chunk] if size == len(chunk) else [[c] for c in chunk]
                retry = []
                for part in pending:
                    try:
                        out = call(part, target)
                    except Exception as e:  # noqa: BLE001
                        print("call failed:", e, flush=True)
                        retry += part
                        continue
                    for k, s in part:
                        why = valid(s, out.get(k), target) if isinstance(out, dict) else "json"
                        if why:
                            retry.append((k, s))
                            print(f"  rejected {k}: {why}", flush=True)
                        else:
                            db["items"][k] = {"h": h(s), "t": postfix(out[k]) if target == "es" else out[k]}
                    save(db)
                chunk = retry
                if not chunk:
                    break
            failed += [k for k, _ in chunk]
            done = sum(1 for k, t, s in todo if db["items"].get(k, {}).get("h") == h(s))
            print(f"{done}/{len(todo)} · {time.time() - t0:.0f} s", flush=True)
    print("FAILED:", failed if failed else "none")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

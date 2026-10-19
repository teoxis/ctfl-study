#!/usr/bin/env python3
"""Builds data/ctai/*.json (CT-AI v2.0 bank, study notes, glossary, exam blueprint) and validates them.

Usage: python3 tools/ctai/build.py      (from the repo root; then tools/translate.py --cert ctai)
"""
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import qlib_ai  # noqa: E402
import bank_ch1  # noqa: E402,F401

OUT = HERE.parent.parent / "data" / "ctai"
OUT.mkdir(parents=True, exist_ok=True)

# Chapters available so far; the others are added as they are written.
CHAPTERS = [
    {"ch": 1, "title": "Introduction to Artificial Intelligence", "minutes": 120, "sections": [
        {"sec": "1.1", "title": "Introduction to AI", "page": 15, "los": [
            {"lo": "1.1.1", "k": 2, "title": "AI-Based and Conventional Systems", "stmt": "Differentiate between AI-based systems and conventional systems",
             "sum": "Los sistemas convencionales se programan paso a paso (if-then-else, bucles): son deterministas y transparentes. La mayoría de los sistemas de IA, sobre todo los de ML, no siguen reglas escritas: aprenden patrones de los datos (el clasificador de gatos aprende de fotos de gatos). Tres diferencias clave: razonamiento probabilístico (manejan la incertidumbre, pero sus salidas no siempre son predecibles), explicabilidad (con miles de millones de parámetros son una «caja negra», un problema en sanidad, finanzas, defensa o transporte) y adaptabilidad (pueden autoaprender, lo que exige monitorización continua).",
             "terms": ["AI-based system", "artificial intelligence", "machine learning"]},
            {"lo": "1.1.2", "k": 2, "title": "Narrow AI, General AI, and Super AI", "stmt": "Distinguish between narrow AI, general AI, and super AI",
             "sum": "IA estrecha (débil): hace tareas concretas y es TODA la IA desplegada hoy; no generaliza (el que reconoce caras no traduce sin reentrenarlo). La IA de frontera (los modelos generativos más avanzados) es un subconjunto de la estrecha. IA general (fuerte): haría casi cualquier tarea intelectual humana sin reentrenar; no existe todavía. Superinteligencia: se automejora sin control humano y supera a los humanos (no necesita internet, aunque lo ampliaría). El paso de general a súper sería la singularidad tecnológica.",
             "terms": ["narrow AI", "general AI", "super AI"]},
            {"lo": "1.1.3", "k": 2, "title": "Different Types of AI Technologies", "stmt": "Explain the different types of AI technologies",
             "sum": "IA ⊃ ML ⊃ deep learning. ML: supervisado (datos etiquetados; regresión lineal, árboles de decisión), no supervisado (sin etiquetas; clustering) y por refuerzo (un agente aprende por prueba y error). Otras técnicas de ML: redes neuronales, modelos bayesianos, SVM, random forests. Deep learning: CNN (imágenes), RNN (secuencias), transformers (dependencias largas; base de los LLM). Otras: NLP, visión por computador, lógica difusa (incertidumbre), algoritmos de búsqueda (optimización), sistemas expertos basados en reglas. La IA agéntica usa agentes autónomos que planifican, razonan y actúan.",
             "terms": ["machine learning", "artificial intelligence"]},
            {"lo": "1.1.4", "k": 2, "title": "Generative AI", "stmt": "Explain generative AI",
             "sum": "La GenAI crea contenido nuevo (texto, imágenes, vídeo, música, datos) parecido a sus datos de entrenamiento. Tecnologías: GAN (dos redes que compiten), modelos de difusión (añaden y quitan ruido) y transformers (autoatención; base de los LLM, cada vez más multimodales). Riesgos: mal uso (deepfakes, desinformación, fraude), empleo (profesiones de oficina) y sostenibilidad (mucha energía y huella de carbono). La mayoría de herramientas parten de modelos fundacionales ajustados (fine-tuning). La EU AI Act empieza a regularla.",
             "terms": ["artificial intelligence"]},
            {"lo": "1.1.5", "k": 2, "title": "Hardware for Machine Learning Systems", "stmt": "Compare the choices available for hardware to implement machine learning systems",
             "sum": "Entrenar e inferir pueden usar hardware distinto (se entrena en la nube y se ejecuta en un móvil). El ML necesita: estructuras de datos grandes, paralelismo masivo (multiplicar matrices) y baja precisión (cuantización: 4 bits en vez de 32 → más rápido, menos consumo, chips más baratos, menos ancho de banda). CPU: pocos núcleos, alta precisión que el ML no necesita. GPU: miles de núcleos simples en paralelo, la mejor opción a pequeña escala. ASIC y SoC específicos de IA: ideales para edge computing. Neuromórficos: diseños inspirados en el cerebro, sin arquitectura von Neumann.",
             "terms": ["machine learning"]},
            {"lo": "1.1.6", "k": 2, "title": "Development and Hosting of AI Models", "stmt": "Compare the options for the development and hosting of AI models",
             "sum": "Comprar a terceros (modelos preentrenados o AIaaS) = desplegar antes; desarrollar en privado = más ajuste a tus requisitos, pero exige expertos. Desarrollo local: control y privacidad (modelos pequeños en un PC, medianos con GPU dedicadas, grandes con clústeres). Nube pública: entornos listos y pago por uso; nube privada: más seguridad, más inversión. Alojamiento local: privacidad y sin licencias, pero hardware limitado. Muchas empresas usan enfoques híbridos (datos sensibles en casa, cómputo pesado en la nube). Desarrollo y alojamiento se deciden por separado según tamaño, rendimiento, presupuesto, privacidad, despliegue y regulación.",
             "terms": ["AI-based system"]},
            {"lo": "1.1.7", "k": 2, "title": "Machine Learning Development Frameworks", "stmt": "Summarize the functionality provided by ML development frameworks",
             "sum": "Un framework de ML da: manejo de datos (cargar, limpiar, transformar), construcción del modelo (algoritmos, capas), entrenamiento y optimización (ajustar parámetros), evaluación (exactitud, precisión, recall, tasas de error) y a veces despliegue (formatos para web, móvil, edge). API de bajo nivel = más control y más código; de alto nivel = más fácil, menos personalizable. Unos son generales y otros especializados. Se eligen por área de aplicación, prototipado rápido, configurabilidad, experiencia del equipo, despliegue, soporte de la comunidad y madurez del ecosistema.",
             "terms": ["ML development framework"]},
            {"lo": "1.1.8", "k": 2, "title": "Regulations and Standards for AI", "stmt": "Explain how regulations and standards affect the development and testing of AI-based systems",
             "sum": "Objetivo: confianza en la IA, aprovechando sus beneficios y mitigando daños. Soft law (no vinculante): Principios de IA de la OCDE e informe de la ONU *Governing AI for Humanity*. EU AI Act: enfoque basado en riesgo (de mínimo a inaceptable); los de alto riesgo exigen pruebas rigurosas, gobernanza de datos y supervisión humana, con multas sobre la facturación global. Fuera de la UE suele regularse de forma más ligera. Estándares técnicos (ISO, IEEE) bajan los principios a la práctica: ISO/IEC TR 29119-11 (probar sistemas de IA), serie ISO/IEC 42119 en desarrollo. Hay regulación sectorial emergente (sanidad, finanzas).",
             "terms": ["AI-based system"]},
        ]},
    ]},
]

# Official CT-AI v2.0 exam blueprint ("Exam Structures & Rules tables" v1.19): per chapter, LO groups -> questions and points.
BLUEPRINT = [
    {"ch": 1, "k": 2, "n": 6, "points": 1, "los": ["1.1.1", "1.1.2", "1.1.3", "1.1.4", "1.1.5", "1.1.6", "1.1.7", "1.1.8"]},
]

GLOSSARY = [
    # term, ch, definición, en tu trabajo, code (optional)
    ("artificial intelligence", 1, "La capacidad de un sistema de realizar tareas que normalmente requieren inteligencia humana: entender lenguaje, reconocer imágenes, decidir…", "Claude, o el Qwen que corre en tu MacBook, son IA."),
    ("AI-based system", 1, "Un sistema que incluye al menos un componente de IA. Lo normal es que la IA sea una pieza dentro de un software convencional.", "Tu agente local: opencode (convencional) + llama.cpp con un modelo (IA) + tus servidores MCP (convencionales)."),
    ("machine learning", 1, "Rama de la IA en la que el sistema aprende patrones a partir de datos en lugar de seguir reglas programadas.", "Un filtro de spam que aprende de los correos que marcas como spam."),
    ("narrow AI", 1, "IA especializada en tareas concretas. Es toda la IA que existe hoy, incluidos los LLM más avanzados.", "Un modelo de código es excelente programando, pero no conduce un coche."),
    ("general AI", 1, "IA que podría hacer casi cualquier tarea intelectual humana sin reentrenarse para cada una. Todavía no existe.", "Lo que a veces se llama AGI en las noticias."),
    ("super AI", 1, "IA que se mejoraría a sí misma sin control humano y superaría la inteligencia humana. Hipotética.", "El escenario de las discusiones sobre riesgo existencial."),
    ("ML development framework", 1, "Conjunto de librerías y herramientas para preparar datos, construir, entrenar, evaluar y desplegar modelos de ML.", "PyTorch, TensorFlow, scikit-learn; para LLM, Hugging Face Transformers."),
    ("supervised learning", 1, "ML con datos etiquetados: cada ejemplo trae la respuesta correcta. Para clasificar y predecir.", "Entrenar un clasificador con 1.000 bugs etiquetados como «UI», «API» o «datos».", "from sklearn.tree import DecisionTreeClassifier\n# X = features, y = labels (the right answer for each example)\nmodel = DecisionTreeClassifier().fit(X_train, y_train)\nmodel.predict(X_new)   # predicts labels for unseen data"),
    ("unsupervised learning", 1, "ML con datos sin etiquetar: el modelo descubre grupos o patrones por sí mismo.", "Agrupar automáticamente tickets de soporte parecidos sin haberlos clasificado antes.", "from sklearn.cluster import KMeans\n# No labels: the algorithm finds 3 groups on its own\ngroups = KMeans(n_clusters=3).fit_predict(X)"),
    ("reinforcement learning", 1, "Un agente aprende por prueba y error: actúa, recibe recompensa o castigo, y ajusta su comportamiento.", "Cómo se entrena a un modelo para jugar al ajedrez, o parte del ajuste fino de los LLM con feedback."),
    ("deep learning", 1, "Subconjunto del ML que usa redes neuronales profundas (muchas capas). CNN para imágenes, RNN para secuencias, transformers para lenguaje.", "Todos los LLM son deep learning."),
    ("transformer", 1, "Arquitectura de red neuronal basada en autoatención (self-attention): cada palabra «mira» al resto del contexto. Es la base de los LLM.", "Qwen, Llama o Claude son transformers."),
    ("generative AI", 1, "IA que crea contenido nuevo (texto, imagen, audio, vídeo) parecido a sus datos de entrenamiento.", "Un agente que escribe un spec de Cypress a partir de un ticket."),
    ("large language model", 1, "Modelo de lenguaje enorme, basado en transformers, entrenado con muchísimo texto para entender y generar lenguaje.", "El modelo que sirve llama-server en tu stack local."),
    ("foundation model", 1, "Modelo grande y general, preentrenado con muchos datos, que luego se adapta (fine-tuning) a tareas concretas.", "Partir de un Qwen base y ajustarlo para tu dominio."),
    ("fine-tuning", 1, "Seguir entrenando un modelo preentrenado con datos propios para especializarlo en una tarea.", "Ajustar un modelo con tus 556 casos de Xray para que redacte casos en tu formato."),
    ("agentic AI", 1, "Sistemas con agentes autónomos que planifican, razonan y actúan (usan herramientas) para lograr un objetivo.", "Claude Code u opencode: leen, editan, ejecutan tests y corrigen solos."),
    ("quantization", 1, "Representar los números del modelo con menos bits (p. ej., 4 en vez de 32): más rápido, menos memoria y consumo, a cambio de algo de precisión.", "Elegir un modelo Q4_K_M en llama.cpp para que quepa en tus 32 GB.", "# Same model, different precision (approx. size of a 30B model):\n# FP16 (16 bits) ~ 60 GB  -> does not fit in 32 GB of RAM\n# Q8   (8 bits)  ~ 32 GB\n# Q4   (4 bits)  ~ 18 GB  -> fits, faster, slightly less accurate\nllama-server -m qwen3-coder-30b-Q4_K_M.gguf"),
    ("inference", 1, "Usar un modelo ya entrenado para obtener una respuesta. Distinto del entrenamiento, y puede ir en otro hardware.", "Cada vez que tu agente local responde, eso es inferencia (tus 48 tok/s)."),
    ("GPU", 1, "Procesador con miles de núcleos simples en paralelo; ideal para las multiplicaciones de matrices del ML.", "El chip de tu M5 que usa llama.cpp vía Metal."),
    ("edge computing", 1, "Ejecutar el modelo en el propio dispositivo (móvil, sensor, coche) en lugar de en la nube.", "Un modelo de voz que funciona en el móvil sin conexión."),
    ("AIaaS", 1, "AI as a Service: usar modelos alojados por un proveedor a través de una API, pagando por uso.", "La API de Anthropic u OpenAI, frente a tu llama-server local.", "# Same OpenAI-compatible call, different hosting:\nclient = OpenAI(base_url=\"https://api.provider.com/v1\")   # AIaaS (cloud)\nclient = OpenAI(base_url=\"http://127.0.0.1:8080/v1\")     # local hosting"),
    ("explainability", 1, "Poder entender por qué un modelo dio una respuesta concreta. Difícil con miles de millones de parámetros («caja negra»).", "Saber por qué el modelo rechazó una solicitud de crédito: obligatorio en sistemas de alto riesgo."),
    ("EU AI Act", 1, "Reglamento europeo de IA con enfoque basado en riesgo: de mínimo a inaceptable. Los de alto riesgo exigen pruebas rigurosas, gobernanza de datos y supervisión humana.", "Si trabajas en Suiza para clientes de la UE, te afecta igual."),
]

# ---------------- validation ----------------
bank = qlib_ai.BANK
ids = [x["id"] for x in bank]
assert len(ids) == len(set(ids)), "duplicate ids"
per_lo = Counter(x["sec"] for x in bank)
los = [lo["lo"] for c in CHAPTERS for s in c["sections"] for lo in s["los"]]
short = {lo: per_lo.get(lo, 0) for lo in los if per_lo.get(lo, 0) < 6}
assert not short, f"LOs with fewer than 6 questions: {short}"
for g in BLUEPRINT:
    assert sum(per_lo[lo] for lo in g["los"]) >= g["n"], g
terms = {t.lower() for t, *_ in GLOSSARY}
missing = {t for c in CHAPTERS for s in c["sections"] for lo in s["los"] for t in lo["terms"] if t.lower() not in terms}
assert not missing, f"syllabus terms missing from the glossary: {missing}"

for ch in sorted({x["ch"] for x in bank}):
    (OUT / f"bank-ch{ch}.json").write_text(json.dumps([x for x in bank if x["ch"] == ch], ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
(OUT / "syllabus.json").write_text(json.dumps({"source": "ISTQB CT-AI Syllabus v2.0", "chapters": CHAPTERS}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
(OUT / "exam.json").write_text(json.dumps({"total": 40, "points": 44, "pass": 29, "groups": BLUEPRINT}, separators=(",", ":")), encoding="utf-8")
keywords = {t.lower() for c in CHAPTERS for s in c["sections"] for lo in s["los"] for t in lo["terms"]}
gl = []
for t, ch, d, w, *code in GLOSSARY:
    # Only syllabus keywords are in the official ISTQB glossary; the rest get no "official definition" link.
    item = {"term": t, "ch": ch, "es": {"def": d, "work": w}, "official": t.lower() in keywords}
    if code:
        item["code"] = code[0]
    gl.append(item)
(OUT / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"CT-AI: {len(bank)} questions in {len(per_lo)} LOs, {len(gl)} glossary terms")

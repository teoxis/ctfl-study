"use strict";
/* Banco CTFL — static PWA, no backend. Progress lives in localStorage and can be
   exported/imported as a text code or a .json file. */

// Each certification has its own data folder, progress and exam rules; the app shows one at a time.
const CERTS = {
  ctfl: {
    id: "ctfl", title: "Banco CTFL", eyebrow: "ISTQB® Certified Tester Foundation Level · Syllabus v4.0.1", ver: "v4.0.1",
    dir: "data/", chapters: [1, 2, 3, 4, 5, 6], loPrefix: "FL-", syllabusId: 3345, pass: 26, examReady: true,
    lsKey: "ctfl-study-v1", examKey: "ctfl-study-exam",
    facts: [["40 preguntas · 1 punto", "40 questions · 1 point"], ["60 min (75 no nativos)", "60 min (75 non-native)"], ["Aprobado: 26/40", "Pass mark: 26/40"]],
    official: [
      ["Syllabus CTFL v4.0.1 (PDF)", 3345],
      ["Sample Exam A · preguntas", 3352], ["Sample Exam A · respuestas", 3357],
      ["Sample Exam B · preguntas", 3359], ["Sample Exam B · respuestas", 3365],
      ["Sample Exam C · preguntas", 3369], ["Sample Exam C · respuestas", 3372],
      ["Sample Exam D · preguntas", 3376], ["Sample Exam D · respuestas", 3380],
      ["Exam Structures and Rules", 3829], ["Exam Structures & Rules Tables (reparto por LO)", 3832],
    ],
    names: {1: "Fundamentals of Testing", 2: "Testing Throughout the SDLC", 3: "Static Testing", 4: "Test Analysis and Design", 5: "Managing the Test Activities", 6: "Test Tools"},
  },
  ctai: {
    id: "ctai", title: "Banco CT-AI", eyebrow: "ISTQB® Certified Tester AI Testing · Syllabus v2.0", ver: "v2.0",
    dir: "data/ctai/", chapters: [1], loPrefix: "AI-", syllabusId: 9558, pass: 29, examReady: false,
    lsKey: "ctai-study-v1", examKey: "ctai-study-exam",
    facts: [["40 preguntas · 44 puntos", "40 questions · 44 points"], ["60 min (75 no nativos)", "60 min (75 non-native)"], ["Aprobado: 29/44", "Pass mark: 29/44"]],
    official: [
      ["Syllabus CT-AI v2.0 (PDF)", 9558],
      ["Sample Exam A · preguntas", 9561], ["Sample Exam A · respuestas", 9564],
      ["Exam Structures and Rules", 3829], ["Exam Structures & Rules Tables (reparto por LO)", 3832],
    ],
    names: {1: "Introduction to Artificial Intelligence", 2: "Quality Characteristics for AI-Based Systems", 3: "Machine Learning", 4: "Testing AI-Based Systems", 5: "Input Data Testing for Machine Learning Systems", 6: "Model Testing for Machine Learning Systems", 7: "Machine Learning Development Testing"},
  },
};
let CERT = CERTS.ctfl;
try { CERT = CERTS[localStorage.getItem("study-cert")] || CERTS.ctfl; } catch (e) { /* storage blocked: default */ }
const SYLLABUS_URL = "https://istqb.org/?sdm_process_download=1&download_id=" + CERT.syllabusId;
const GLOSSARY_URL = t => "https://glossary.istqb.org/en_US/search?term=" + encodeURIComponent(t);
const OFFICIAL = CERT.official;
const CHAPTER_NAMES = CERT.names;
const SYL_PAGE = (prefix = "") => L(prefix + "Syllabus v4.0.1, pág. ").replace("v4.0.1", CERT.ver);
const LETTERS = ["A", "B", "C", "D"];

const CARDS = [
 ["Test basis", "Todo lo que se usa como base para analizar y diseñar las pruebas: requisitos, historias de usuario, diseños, código, riesgos…", "Everything used as the basis for test analysis and design: requirements, user stories, designs, code, risks…"],
 ["Test condition", "Un aspecto que se puede probar de un componente o sistema. Responde a «qué probar».", "A testable aspect of a component or system. It answers \"what to test\"."],
 ["Test case", "Precondiciones, entradas, acciones, resultados esperados y postcondiciones, diseñados a partir de una condición de prueba. Responde a «cómo probarlo».", "Preconditions, inputs, actions, expected results and postconditions, derived from a test condition. It answers \"how to test it\"."],
 ["Test procedure", "Casos de prueba ordenados para ejecutarse, con lo necesario para preparar el entorno antes y dejarlo limpio después.", "Test cases in execution order, with the steps needed to set things up before and clean up after."],
 ["Testware", "Todo lo que se produce al probar: planes, casos, scripts, datos de prueba, informes…", "Everything produced by testing: plans, cases, scripts, test data, reports…"],
 ["Coverage item", "Lo que una técnica te pide cubrir (una partición, un valor frontera, una rama…). Sirve para medir la cobertura: cubiertos / identificados.", "What a technique tells you to cover (a partition, a boundary value, a branch…). It is how coverage is measured: covered / identified."],
 ["Error / Defect / Failure", "Una persona comete un error (equivocación); el error deja un defecto en el código o en un documento; al ejecutarse, el defecto puede provocar un fallo visible.", "A person makes an error (mistake); the error leaves a defect in code or a document; when executed, the defect may cause a visible failure."],
 ["Root cause", "El motivo de fondo por el que se produjo el problema. Si se corrige, se evitan defectos parecidos en el futuro.", "The underlying reason the problem happened. Fixing it prevents similar defects in the future."],
 ["Confirmation testing", "Volver a probar después de un arreglo para confirmar que el defecto original está corregido.", "Testing again after a fix to confirm the original defect is gone."],
 ["Regression testing", "Probar que un cambio no ha roto nada de lo que ya funcionaba. Es la candidata ideal para automatizar.", "Testing that a change has not broken anything that already worked. It is the prime candidate for automation."],
 ["Maintenance testing", "Probar un sistema que ya está en producción cuando se modifica, se migra a otro entorno o se retira.", "Testing a system already in production when it is modified, migrated to another environment or retired."],
 ["Shift left", "Empezar a probar lo antes posible en el ciclo de vida (revisar requisitos, escribir tests antes del código), sin abandonar las pruebas de las fases finales.", "Starting testing as early as possible in the lifecycle (reviewing requirements, writing tests before code), without dropping later testing."],
 ["TDD / ATDD / BDD", "TDD: el desarrollador escribe el test del componente antes del código. ATDD: los tests salen de los criterios de aceptación, antes de implementar. BDD: el comportamiento se describe en Given/When/Then y se convierte en tests ejecutables.", "TDD: the developer writes the component test before the code. ATDD: tests come from the acceptance criteria, before implementation. BDD: behaviour is written as Given/When/Then and turned into executable tests."],
 ["Static testing", "Probar sin ejecutar el software: revisiones y análisis estático. Encuentra defectos directamente, no fallos.", "Testing without running the software: reviews and static analysis. It finds defects directly, not failures."],
 ["Inspection", "La revisión más formal: proceso completo, métricas y el objetivo de encontrar el máximo de anomalías. El autor no puede ser líder de la revisión ni escriba.", "The most formal review: full process, metrics, and the goal of finding as many anomalies as possible. The author cannot be the review leader or the scribe."],
 ["Walkthrough", "Revisión dirigida por el autor. Sirve para evaluar, formar a los participantes, llegar a consensos, generar ideas y detectar anomalías.", "A review led by the author. Used to evaluate, educate the participants, reach consensus, generate ideas and detect anomalies."],
 ["Technical review", "Revisión hecha por personas técnicamente cualificadas, dirigida por un moderador, para llegar a un consenso y tomar decisiones sobre un problema técnico.", "A review by technically qualified reviewers, led by a moderator, to reach consensus and make decisions on a technical problem."],
 ["Equivalence partitioning", "Divide los datos en grupos (particiones) que el sistema debería tratar igual. Basta un valor de cada partición, también de las inválidas.", "Splits data into groups (partitions) the system should treat the same way. One value per partition is enough, including the invalid ones."],
 ["Boundary value analysis", "Prueba los extremos de las particiones ordenadas, donde más fallos se esconden. Con 2 valores: la frontera y su vecino de la otra partición. Con 3 valores: la frontera y sus dos vecinos.", "Tests the edges of ordered partitions, where failures tend to hide. 2-value: the boundary and its neighbour in the other partition. 3-value: the boundary and both neighbours."],
 ["Decision table testing", "Una tabla que combina condiciones y acciones; cada columna es una regla. Con n condiciones de sí/no salen 2^n columnas, y se prueban las que son posibles.", "A table combining conditions and actions; each column is a rule. With n yes/no conditions there are 2^n columns, and the feasible ones are tested."],
 ["State transition testing", "Prueba los estados del sistema y los saltos entre ellos. Coberturas: todos los estados, todas las transiciones válidas (0-switch) y todas las transiciones, incluidas las inválidas.", "Tests the system's states and the moves between them. Coverage levels: all states, all valid transitions (0-switch), and all transitions including invalid ones."],
 ["Statement coverage", "Porcentaje de líneas (sentencias) del código que tus tests han ejecutado: sentencias ejecutadas / sentencias ejecutables.", "Percentage of the code's lines (statements) your tests have run: executed statements / executable statements."],
 ["Branch coverage", "Porcentaje de caminos de decisión recorridos: cada IF tiene dos ramas, la verdadera y la falsa, y hay que pasar por ambas. Es más exigente que la de sentencias: si cubres el 100 % de las ramas, también cubres el 100 % de las sentencias, pero no al revés.", "Percentage of decision paths taken: each IF has two branches, true and false, and both must be exercised. It is stronger than statement coverage: 100% branch coverage guarantees 100% statement coverage, but not the other way round."],
 ["Exploratory testing", "Diseñar, ejecutar y evaluar las pruebas a la vez, aprendiendo el producto sobre la marcha. Se organiza en sesiones con un objetivo escrito (test charter).", "Designing, running and evaluating tests at the same time while learning the product. Organised in sessions with a written goal (test charter)."],
 ["Risk level", "Probabilidad × impacto de un riesgo. Cuanto más alto, antes y más a fondo se prueba esa parte.", "A risk's likelihood × impact. The higher it is, the earlier and more thoroughly that area is tested."],
 ["Product vs project risk", "Riesgo de producto: que el software falle en calidad (funcionalidad, rendimiento, seguridad…). Riesgo de proyecto: que falle la gestión (retrasos, personas, proveedores, herramientas).", "Product risk: the software falls short on quality (functionality, performance, security…). Project risk: the management side fails (delays, people, suppliers, tools)."],
 ["Entry / exit criteria", "Entrada: lo que debe cumplirse para empezar a probar (en ágil, Definition of Ready). Salida: lo que debe cumplirse para darlo por terminado (Definition of Done).", "Entry: what must be true to start testing (in Agile, Definition of Ready). Exit: what must be true to call it finished (Definition of Done)."],
 ["Test pyramid", "Muchos tests pequeños, rápidos y aislados en la base (componente); pocos tests lentos de extremo a extremo en la cima.", "Many small, fast, isolated tests at the bottom (component); few slow end-to-end tests at the top."],
 ["Testing quadrants", "Clasifican las pruebas con dos ejes: orientadas al negocio o a la tecnología, y de apoyo al equipo o de crítica al producto. Salen 4 cuadrantes, Q1 a Q4.", "Classify tests on two axes: business- or technology-facing, and supporting the team or critiquing the product. That gives 4 quadrants, Q1 to Q4."],
 ["Three-point estimation", "Estimación con tres valores: optimista (a), más probable (m) y pesimista (b). E = (a + 4m + b) / 6; desviación = (b − a) / 6.", "Estimate from three values: optimistic (a), most likely (m) and pessimistic (b). E = (a + 4m + b) / 6; standard deviation = (b − a) / 6."],
 ["Configuration management", "Identificar, versionar y controlar el testware y los elementos de prueba. Las líneas base permiten repetir exactamente una prueba.", "Identifying, versioning and controlling testware and test items. Baselines let you reproduce a test exactly."],
];

// ---------------- persistence ----------------
const LS_KEY = CERT.lsKey, EXAM_KEY = CERT.examKey;
const blank = () => ({ v: 1, q: {}, cards: {}, exams: [], seen: {}, updatedAt: 0 });
let P = blank();
function lsGet(k) { try { return localStorage.getItem(k); } catch { return null; } }
function lsSet(k, v) { try { localStorage.setItem(k, v); return true; } catch { return false; } }
function lsDel(k) { try { localStorage.removeItem(k); } catch {} }
function normalize(d) {
  const b = blank();
  if (!d || typeof d !== "object") return b;
  const obj = o => (o && typeof o === "object" && !Array.isArray(o)) ? o : {};
  return { v: 1, q: obj(d.q), cards: obj(d.cards), exams: Array.isArray(d.exams) ? d.exams.slice(-60) : [], seen: obj(d.seen), updatedAt: Number(d.updatedAt) || 0 };
}
function load() { try { P = normalize(JSON.parse(lsGet(LS_KEY) || "null")); } catch { P = blank(); } }
let saveWarned = false;
function save() {
  P.updatedAt = Date.now();
  if (!lsSet(LS_KEY, JSON.stringify(P)) && !saveWarned) { saveWarned = true; toast("No se puede guardar en este navegador (¿modo privado?). Exporta tu progreso antes de cerrar."); }
}
function merge(a, b) {
  const out = normalize(a), other = normalize(b);
  for (const [id, r] of Object.entries(other.q)) if (!out.q[id] || (r.last || 0) > (out.q[id].last || 0)) out.q[id] = r;
  for (const [id, r] of Object.entries(other.cards)) if (!out.cards[id] || (r.last || 0) > (out.cards[id].last || 0)) out.cards[id] = r;
  const ids = new Set(out.exams.map(e => e.id || e.at));
  for (const e of other.exams) if (!ids.has(e.id || e.at)) out.exams.push(e);
  out.exams.sort((x, y) => x.at - y.at);
  for (const [id, n] of Object.entries(other.seen)) out.seen[id] = Math.max(out.seen[id] || 0, n);
  out.updatedAt = Date.now();
  return out;
}

// export/import code: "CTFL1:" + base64(deflate-raw(json)) or "CTFL0:" + base64(json)
const b64 = bytes => { let s = ""; for (let i = 0; i < bytes.length; i += 0x8000) s += String.fromCharCode.apply(null, bytes.subarray(i, i + 0x8000)); return btoa(s); };
const unb64 = str => Uint8Array.from(atob(str), c => c.charCodeAt(0));
async function encodeProgress() {
  const bytes = new TextEncoder().encode(JSON.stringify(P));
  if (typeof CompressionStream === "function") {
    try {
      const out = new Uint8Array(await new Response(new Blob([bytes]).stream().pipeThrough(new CompressionStream("deflate-raw"))).arrayBuffer());
      return "CTFL1:" + b64(out);
    } catch {}
  }
  return "CTFL0:" + b64(bytes);
}
async function decodeProgress(code) {
  code = code.trim();
  if (code.startsWith("{")) return JSON.parse(code);
  const m = code.match(/^CTFL([01]):([A-Za-z0-9+/=\s]+)$/);
  if (!m) throw new Error("El código no tiene el formato esperado (debe empezar por CTFL1: o CTFL0:).");
  const bytes = unb64(m[2].replace(/\s+/g, ""));
  if (m[1] === "0") return JSON.parse(new TextDecoder().decode(bytes));
  if (typeof DecompressionStream !== "function") throw new Error("Este navegador no puede descomprimir el código. Usa la copia en fichero .json.");
  const txt = await new Response(new Blob([bytes]).stream().pipeThrough(new DecompressionStream("deflate-raw"))).text();
  return JSON.parse(txt);
}

// ---------------- data ----------------
let Q = [], QBY = {}, EXAM = null, SYL = null, LO_INFO = {}, I18N = {}, GLOSS = [];
async function loadData() {
  const files = CERT.chapters.map(n => `${CERT.dir}bank-ch${n}.json`).concat([CERT.dir + "exam.json", CERT.dir + "syllabus.json"]);
  const res = await Promise.all(files.map(f => fetch(f).then(r => { if (!r.ok) throw new Error(f); return r.json(); })));
  const nch = CERT.chapters.length;
  Q = res.slice(0, nch).flat();
  EXAM = res[nch]; SYL = res[nch + 1];
  // Optional: the other-language half of every text (tools/translate.py). Without it the app shows the originals.
  GLOSS = await fetch(CERT.dir + "glossary.json").then(r => r.ok ? r.json() : []).catch(() => []);
  I18N = await fetch(CERT.dir + "i18n.json").then(r => r.ok ? r.json() : {}).then(d => d.items || {}).catch(() => ({}));
  for (const x of Q) QBY[x.id] = x;
  for (const ch of SYL.chapters) for (const s of ch.sections) for (const lo of s.los) LO_INFO[lo.lo] = { ...lo, ch: ch.ch, sec: s.sec, secTitle: s.title };
}

// ---------------- language ----------------
// Originals: question + options in English, explanations and notes in Spanish. tr() picks the requested language.
let LANG = "en";
try { LANG = localStorage.getItem("ctfl-lang") === "es" ? "es" : "en"; } catch (e) { /* storage blocked: default */ }
// Interface strings are written in Spanish; UI_EN holds their English version.
const UI_EN = {"Sample Exam A · preguntas": "Sample Exam A · questions","Sample Exam B · preguntas": "Sample Exam B · questions","Sample Exam C · preguntas": "Sample Exam C · questions","Sample Exam D · preguntas": "Sample Exam D · questions","Sample Exam A · respuestas": "Sample Exam A · answers","Sample Exam B · respuestas": "Sample Exam B · answers","Sample Exam C · respuestas": "Sample Exam C · answers","Sample Exam D · respuestas": "Sample Exam D · answers","Exam Structures & Rules Tables (reparto por LO)": "Exam Structures & Rules Tables (split by LO)","No se puede guardar en este navegador (¿modo privado?). Exporta tu progreso antes de cerrar.": "This browser cannot save (private mode?). Export your progress before closing.","El código no tiene el formato esperado (debe empezar por CTFL1: o CTFL0:).": "The code is not in the expected format (it must start with CTFL1: or CTFL0:).","Este navegador no puede descomprimir el código. Usa la copia en fichero .json.": "This browser cannot decompress the code. Use the .json backup file instead."," preguntas en el banco": " questions in the bank","Dominio global: ": "Overall mastery: ","Sin simulacros todavía": "No mock exams yet","Mejor simulacro: ": "Best mock exam: ","Cap. ": "Ch. ","Correcta": "Correct","Incorrecta · correcta: ": "Incorrect · correct: ","Sin responder · correcta: ": "Not answered · correct: ","Estudia esto: ": "Study this: ","Syllabus v4.0.1, pág. ": "Syllabus v4.0.1, p. ","Pregunta": "Question","Opciones": "Options","Original": "Original","Práctica por capítulos": "Practice by chapter","Tandas de 10, primero lo que no dominas": "Sets of 10, weakest questions first"," preguntas · ": " questions · "," en examen": " in the exam","Capítulos ": "Chapters ","¿Quieres practicar un objetivo concreto? Ve a Temario y pulsa «Practicar» en cualquier LO.": "Want to practise one learning objective? Go to Syllabus and tap \"Practise\" on any LO.","Terminar": "Finish","Siguiente": "Next","Ver resultado": "See result","Elige una respuesta": "Choose an answer","Tanda terminada": "Set finished","Otra tanda": "Another set","Por encima del 65 % que exige el examen.": "Above the 65% the exam requires.","Por debajo del 65 %. Las falladas pasan a la pestaña Falladas.": "Below 65%. Wrong answers go to the Mistakes tab.","Simulacro de examen": "Mock exam","40 preguntas repartidas exactamente como el examen oficial: por capítulo (8 · 6 · 4 · 11 · 9 · 2), por grupo de objetivos y por nivel K (8 K1 · 24 K2 · 8 K3). Primero salen las preguntas que menos has visto en simulacros. No verás si aciertas hasta entregar. Cada pregunta vale 1 punto y se aprueba con 26.": "40 questions split exactly like the official exam: by chapter (8 · 6 · 4 · 11 · 9 · 2), by objective group and by K-level (8 K1 · 24 K2 · 8 K3). Questions you have seen least in mock exams come first. You will not see whether you are right until you submit. Each question is worth 1 point and the pass mark is 26.","Duración": "Duration","75 min (no nativo, +25 %)": "75 min (non-native, +25%)","60 min (estándar)": "60 min (standard)","Empezar simulacro": "Start mock exam","Navegador de preguntas": "Question navigator","/40 respondidas": "/40 answered","Pregunta ": "Question ","Anterior": "Previous","Quitar marca": "Unflag","Marcar": "Flag","Confirmar entrega": "Confirm submission","Entregar": "Submit","Quedan ": "Remaining: "," sin responder. Pulsa «Confirmar entrega» para corregir.": " unanswered. Tap \"Confirm submission\" to grade.","Abandonar simulacro": "Abandon mock exam","Pulsa otra vez para abandonar sin guardar": "Tap again to abandon without saving","Se acabó el tiempo: el simulacro se ha corregido automáticamente.": "Time is up: the mock exam was graded automatically.","Resultado del simulacro": "Mock exam result","Aprobado (26 o más).": "Pass (26 or more).","Suspenso: faltan ": "Fail: "," para el 26.": " short of 26.","Capítulo": "Chapter","Aciertos": "Correct","Nivel K": "K-level"," · recordar": " · remember"," · comprender": " · understand"," · aplicar": " · apply","Revisión pregunta a pregunta": "Question-by-question review","Cerrar simulacro": "Close mock exam","Fecha": "Date","Nota": "Score","Aprobado": "Pass","Suspenso": "Fail","Últimos simulacros": "Recent mock exams","Preguntas falladas": "Mistakes","No tienes preguntas pendientes. Cuando falles una en Práctica o en un simulacro, aparecerá aquí hasta que la aciertes dos veces seguidas.": "No questions pending. When you miss one in Practice or in a mock exam, it shows up here until you get it right twice in a row."," pendientes. Una pregunta sale de aquí cuando la aciertas dos veces seguidas.": " pending. A question leaves this list when you get it right twice in a row.","Repasar ": "Review ","Temario": "Syllabus","Resúmenes propios por objetivo de aprendizaje": "Own summaries per learning objective","Materiales oficiales (gratis, istqb.org)": "Official materials (free, istqb.org)","Estudia con el syllabus oficial delante: cada objetivo indica su página. Los niveles K indican la profundidad: K1 recordar, K2 comprender, K3 aplicar.": "Study with the official syllabus open: each objective shows its page. K-levels give the depth: K1 remember, K2 understand, K3 apply.","Glosario oficial: ": "Official glossary: "," min · ": " min · ","pág. ": "p. "," · Syllabus v4.0.1, pág. ": " · Syllabus v4.0.1, p. ","Abrir en el glosario oficial": "Open in the official glossary","Practicar (": "Practise (","Dominio ": "Mastery ","Practicando ": "Practising ","← Volver al temario: ": "← Back to the syllabus: ","Modo": "Mode","Glosario": "Glossary"," dominados": " mastered","Girar tarjeta": "Flip card","Término · toca para girar": "Term · tap to flip","Repasar otra vez": "Review again","Me lo sé": "I know it","Definición oficial ↗": "Official definition ↗","Progreso": "Progress","Dominio": "Mastery","Vistas": "Seen","Acierto": "Accuracy","Todas las K": "All K","Dominio: una pregunta cuenta como dominada cuando la aciertas tres veces seguidas; si la fallas, vuelve a cero.": "Mastery: a question counts as mastered when you get it right three times in a row; if you miss it, it goes back to zero.","Código de progreso": "Progress code","Aquí aparecerá tu código, o pega aquí el código del otro dispositivo.": "Your code appears here, or paste the code from your other device.","No se pudo leer el fichero: ": "Could not read the file: ","Copia de seguridad y sincronización": "Backup and sync","Tu progreso solo vive en este navegador. Para pasarlo al móvil (o al revés): «Copiar progreso» aquí, y «Pegar y fusionar» en el otro dispositivo. Al fusionar se conserva, para cada pregunta, la respuesta más reciente, y se juntan los simulacros de los dos.": "Your progress lives only in this browser. To move it to your phone (or back): \"Copy progress\" here, then \"Paste and merge\" on the other device. Merging keeps the most recent answer for each question and joins the mock exams from both.","Código copiado al portapapeles.": "Code copied to the clipboard.","Selecciona el texto y cópialo a mano.": "Select the text and copy it by hand.","Copiar progreso": "Copy progress","Pega primero el código del otro dispositivo en el cuadro.": "First paste the code from the other device into the box.","Progreso fusionado.": "Progress merged.","Código no válido.": "Invalid code.","Pegar y fusionar": "Paste and merge","Descargar copia (.json)": "Download backup (.json)","Copia importada y fusionada.": "Backup imported and merged.","Importar copia (.json)": "Import backup (.json)","Progreso borrado.": "Progress deleted.","Pulsa otra vez para borrar todo el progreso": "Tap again to delete all progress","Borrar progreso": "Delete progress","No se pudo cargar el banco de preguntas. Comprueba la conexión la primera vez que abras la app; después funciona sin conexión.": "Could not load the question bank. Check your connection the first time you open the app; after that it works offline.","Hay una versión nueva del banco.": "A new version is available.","Actualizar": "Update","Capítulo ": "Chapter ","Toca un capítulo para practicarlo": "Tap a chapter to practise it","Tanda mixta (todos los capítulos)": "Mixed set (all chapters)","El simulacro estará disponible cuando estén todos los capítulos. Mientras, practica por capítulos en la pestaña Practicar.": "The mock exam will be available once all chapters are ready. Meanwhile, practise by chapter in the Practice tab."};
const L = es => (LANG === "en" && UI_EN[es] != null) ? UI_EN[es] : es;
const tr = (key, field, original, lang = LANG, native = "en") => (lang !== native && I18N[key] && I18N[key].t[field] != null) ? I18N[key].t[field] : original;
const qText = (x, lang = LANG) => tr("q:" + x.id, "q", x.q, lang);
const optText = (x, i, lang = LANG) => { const o = tr("q:" + x.id, "o", null, lang); return o ? o[i] : x.o[i]; };
const expText = (x, lang = LANG) => tr("e:" + x.id, "e", x.e, lang, "es");
// Static texts in index.html carry their English version in data-en; the Spanish one is kept on first switch.
function applyStaticLang() {
  document.documentElement.lang = LANG;
  document.title = CERT.title;
  $("#certTitle").textContent = CERT.title;
  $("#certEyebrow").textContent = CERT.eyebrow;
  $("#facts").replaceChildren(...CERT.facts.map(f => el("span", { text: f[LANG === "es" ? 0 : 1] })), $("#bankSize"));
  document.querySelectorAll("[data-en]").forEach(n => {
    if (n.dataset.es == null) n.dataset.es = n.innerHTML;
    n.innerHTML = LANG === "en" ? n.dataset.en : n.dataset.es;
  });
}
function setLang(l) {
  LANG = l;
  try { localStorage.setItem("ctfl-lang", l); } catch (e) { /* ignore */ }
  applyStaticLang();
  document.querySelectorAll("#langToggle button").forEach(b => b.setAttribute("aria-pressed", String(b.dataset.lang === l)));
  render();
}

// ---------------- helpers ----------------
const $ = s => document.querySelector(s);
function el(tag, attrs = {}, ...kids) {
  const n = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (v === false || v == null) continue;
    if (k === "class") n.className = v; else if (k === "text") n.textContent = v;
    else if (k.startsWith("on") && typeof v === "function") n.addEventListener(k.slice(2), v);
    else n.setAttribute(k, v === true ? "" : v);
  }
  for (const c of kids.flat()) if (c != null && c !== false) n.append(c.nodeType ? c : document.createTextNode(String(c)));
  return n;
}
const ext = (href, text) => el("a", { href, target: "_blank", rel: "noopener" }, text);
function shuffle(a) { const r = a.slice(); for (let i = r.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [r[i], r[j]] = [r[j], r[i]]; } return r; }
const qs = id => P.q[id] || { c: 0, w: 0, box: 0, last: 0 };
function mastery(list) { return list.length ? Math.round(100 * list.reduce((s, x) => s + Math.min(qs(x.id).box, 3) / 3, 0) / list.length) : 0; }
function record(id, ok) { const s = Object.assign({ c: 0, w: 0, box: 0, last: 0 }, P.q[id]); if (ok) { s.c++; s.box = Math.min(s.box + 1, 4); } else { s.w++; s.box = 0; } s.last = Date.now(); P.q[id] = s; }
function prepare(x) { const order = shuffle([0, 1, 2, 3]); return { id: x.id, order, correct: order.indexOf(0) }; }
let toastTimer = null;
function toast(msg, action) {
  const t = $("#toast"); t.replaceChildren(el("span", { text: msg }));
  if (action) t.append(el("button", { type: "button", onclick: () => { t.hidden = true; action.fn(); } }, action.label));
  t.hidden = false; clearTimeout(toastTimer); if (!action) toastTimer = setTimeout(() => { t.hidden = true; }, 4000);
}

// ---------------- header ----------------
function renderStatus() {
  $("#bankSize").textContent = Q.length + L(" preguntas en el banco");
  $("#masteryChip").textContent = L("Dominio global: ") + mastery(Q) + " %";
  const best = P.exams.reduce((m, e) => Math.max(m, e.score), -1);
  $("#bestChip").textContent = best < 0 ? L("Sin simulacros todavía") : L("Mejor simulacro: ") + best + "/40";
}

// ---------------- routing ----------------
const VIEWS = ["practicar", "simulacro", "falladas", "temario", "glosario", "progreso"];
let current = "practicar";
// Every navigation is a history entry, so the back gesture/button returns to the previous screen and scroll position.
function go(view, opts = {}) {
  history.replaceState({ ...(history.state || {}), view: current, y: window.scrollY }, "", "#" + current);
  const same = view === current && !opts.scrollTo;
  current = view;
  (same ? history.replaceState : history.pushState).call(history, { view, y: 0, scrollTo: opts.scrollTo || null }, "", "#" + view);
  render();
  restoreScroll(history.state);
}
function restoreScroll(st) {  // runs right after render(): the new DOM is already in place
  const n = st && st.scrollTo && document.getElementById(st.scrollTo);
  if (n) { n.scrollIntoView({ block: "start" }); n.classList.add("flash-target"); setTimeout(() => n.classList.remove("flash-target"), 1600); }
  else window.scrollTo(0, (st && st.y) || 0);
}
if ("scrollRestoration" in history) history.scrollRestoration = "manual";
window.addEventListener("popstate", e => {
  if (!e.state || !VIEWS.includes(e.state.view)) return;
  current = e.state.view; render(); restoreScroll(e.state);
});
function render() {
  renderStatus();
  document.querySelectorAll("nav.tabs button").forEach(b => b.setAttribute("aria-selected", String(b.dataset.view === current)));
  if (!history.state) history.replaceState({ view: current, y: 0 }, "", "#" + current);
  const v = $("#view"); v.replaceChildren();
  ({ practicar: viewPractice, simulacro: viewExam, falladas: viewReview, temario: viewSyllabus, glosario: viewCards, progreso: viewProgress })[current](v);
}

// ---------------- question card ----------------
function questionCard(item, o) {
  const x = QBY[item.id], info = LO_INFO[x.sec] || {};
  const card = el("section", { class: "qcard", "aria-label": L("Pregunta") });
  card.append(el("div", { class: "qhead" },
    el("span", { class: "row" }, el("span", { class: "badge" + (x.k === 3 ? " k3" : ""), text: x.lo + " · K" + x.k }), el("span", { class: "eyebrow", text: L("Cap. ") + x.ch })),
    el("span", { class: "eyebrow mono", text: o.counter || x.id })));
  const stem = el("p", { class: "stem", text: qText(x) });
  card.append(stem);
  if (x.code) card.append(el("pre", { class: "code" }, x.code));
  const box = el("div", { class: "opts", role: "radiogroup", "aria-label": L("Opciones") });
  item.order.forEach((oi, pos) => {
    const b = el("button", { class: "opt", role: "radio", type: "button", "aria-checked": String(o.chosen === pos) }, el("span", { class: "k", text: LETTERS[pos] }), el("span", { class: "otext", "data-oi": oi, text: optText(x, oi) }));
    if (o.reveal) { b.disabled = true; if (pos === item.correct) b.classList.add("right"); else if (pos === o.chosen) b.classList.add("wrong"); }
    else b.addEventListener("click", () => o.onPick(pos));
    box.append(b);
  });
  card.append(box);
  if (o.reveal) {
    const ok = o.chosen === item.correct;
    card.append(el("div", { class: "explain" + (ok ? "" : " bad") },
      el("span", { class: "verdict " + (ok ? "good" : "bad"), text: o.chosen == null ? L("Sin responder · correcta: ") + LETTERS[item.correct] : ok ? L("Correcta") : L("Incorrecta · correcta: ") + LETTERS[item.correct] }),
      el("p", { class: "etext", text: expText(x) }),
      el("p", { class: "note" },
        el("a", { href: "#temario", onclick: ev => { ev.preventDefault(); openLO(x.sec); } }, L("Estudia esto: ") + x.lo + " " + (info.title || "")),
        " · ", ext(SYLLABUS_URL, SYL_PAGE() + x.page))));
  }
  // Shows this one question in the other language without switching the whole app.
  let flipped = false;
  card.querySelector(".qhead").append(el("button", { class: "btn small flipq", type: "button", onclick: ev => {
    flipped = !flipped;
    const l = flipped ? (LANG === "en" ? "es" : "en") : LANG;
    stem.textContent = qText(x, l);
    card.querySelectorAll(".otext").forEach(s => { s.textContent = optText(x, Number(s.dataset.oi), l); });
    const e = card.querySelector(".etext"); if (e) e.textContent = expText(x, l);
    ev.currentTarget.textContent = flipped ? L("Original") : (LANG === "en" ? "Ver en ES" : "See in EN");
  } }, LANG === "en" ? "Ver en ES" : "See in EN"));
  return card;
}
let openChapters = new Set();
function openLO(sec) { openChapters.add(Number(sec[0])); go("temario", { scrollTo: "lo-" + sec }); }

// ---------------- practice ----------------
let practice = null, practiceLO = null;
function startPractice(pool, label, fromLO = null) {
  const ranked = shuffle(pool).sort((a, b) => qs(a.id).box - qs(b.id).box);
  practice = { items: ranked.slice(0, 10).map(prepare), i: 0, chosen: null, right: 0, label, fromLO };
  go("practicar");
}
function viewPractice(v) {
  if (practice && practice.i < practice.items.length) return practiceRun(v);
  if (practice) return practiceDone(v);
  v.append(el("div", { class: "row spread" }, el("h2", { text: L("Práctica por capítulos") }), el("span", { class: "muted", text: L("Tandas de 10, primero lo que no dominas") })));
  v.append(el("p", { class: "note", style: "margin-top:6px", text: L("Toca un capítulo para practicarlo") }));
  const grid = el("div", { class: "chapters", style: "margin-top:12px" });
  for (const ch of CERT.chapters) {
    const list = Q.filter(x => x.ch === ch), m = mastery(list), name = tr("ch:" + ch, "title", CHAPTER_NAMES[ch]);
    const n = EXAM.groups.filter(g => g.ch === ch).reduce((s, g) => s + g.n, 0);
    grid.append(el("button", { class: "chap", type: "button", onclick: () => startPractice(list, L("Capítulo ") + ch + ". " + name) },
      el("span", { class: "name", text: ch + ". " + name }),
      el("div", { class: "bar", "aria-hidden": "true" }, el("i", { style: "width:" + m + "%" })),
      el("span", { class: "meta" }, el("span", { text: list.length + L(" preguntas · ") + n + L(" en examen") }), el("span", { text: m + " %" }))));
  }
  v.append(grid);
  v.append(el("button", { class: "btn primary", type: "button", style: "margin-top:14px", onclick: () => startPractice(Q, L("Tanda mixta (todos los capítulos)")) }, L("Tanda mixta (todos los capítulos)")));
  v.append(el("p", { class: "note", style: "margin-top:10px", text: L("¿Quieres practicar un objetivo concreto? Ve a Temario y pulsa «Practicar» en cualquier LO.") }));
}
function practiceRun(v) {
  const it = practice.items[practice.i], reveal = practice.chosen != null;
  if (practice.fromLO) v.append(el("button", { class: "btn small", type: "button", style: "margin-bottom:8px", onclick: () => openLO(practice.fromLO) }, L("← Volver al temario: ") + CERT.loPrefix + practice.fromLO));
  if (practice.label) v.append(el("p", { class: "eyebrow", style: "margin-bottom:8px", text: practice.label }));
  v.append(questionCard(it, { counter: (practice.i + 1) + " / " + practice.items.length, chosen: practice.chosen, reveal,
    onPick: pos => { practice.chosen = pos; const ok = pos === it.correct; if (ok) practice.right++; record(it.id, ok); save(); render(); } }));
  v.append(el("div", { class: "row spread", style: "margin-top:12px" },
    el("button", { class: "btn", type: "button", onclick: () => { practice = null; render(); } }, L("Terminar")),
    reveal ? el("button", { class: "btn primary", type: "button", onclick: () => { practice.i++; practice.chosen = null; render(); window.scrollTo(0, 0); } }, practice.i + 1 < practice.items.length ? L("Siguiente") : L("Ver resultado")) : el("span", { class: "muted", text: L("Elige una respuesta") })));
}
function practiceDone(v) {
  const n = practice.items.length, r = practice.right, good = r / n >= 0.65;
  v.append(el("div", { class: "score " + (good ? "pass" : "fail") }, el("span", { class: "eyebrow", text: L("Tanda terminada") }), el("span", { class: "big mono", text: r + "/" + n }), el("p", { text: good ? L("Por encima del 65 % que exige el examen.") : L("Por debajo del 65 %. Las falladas pasan a la pestaña Falladas.") })));
  v.append(el("div", { class: "row", style: "margin-top:12px" }, el("button", { class: "btn primary", type: "button", onclick: () => { practice = null; render(); } }, L("Otra tanda"))));
}

// ---------------- mock exam ----------------
let exam = null, tick = null;
function loadExam() { try { const e = JSON.parse(lsGet(EXAM_KEY) || "null"); if (e && e.items && !e.done) exam = e; } catch {} }
function saveExam() { if (exam && !exam.done) lsSet(EXAM_KEY, JSON.stringify(exam)); else lsDel(EXAM_KEY); }
function drawExam() {
  const picked = [];
  for (const g of EXAM.groups) {
    const pool = Q.filter(x => g.los.includes(x.sec)), chosen = [];
    while (chosen.length < g.n) {
      const cands = pool.filter(x => !chosen.includes(x));
      const low = Math.min(...cands.map(x => P.seen[x.id] || 0));
      const best = cands.filter(x => (P.seen[x.id] || 0) === low);
      const used = new Set(chosen.map(x => x.sec));
      const fresh = best.filter(x => !used.has(x.sec));
      const from = fresh.length ? fresh : best;
      chosen.push(from[Math.floor(Math.random() * from.length)]);
    }
    picked.push(...chosen);
  }
  picked.sort((a, b) => a.ch - b.ch);
  return picked;
}
function startExam(mins) {
  const items = drawExam().map(prepare);
  exam = { items, answers: Array(40).fill(null), flags: Array(40).fill(false), i: 0, start: Date.now(), end: Date.now() + mins * 60000, mins, done: false, confirm: false };
  saveExam(); startTick(); render();
}
function startTick() {
  clearInterval(tick);
  tick = setInterval(() => {
    if (!exam || exam.done) return clearInterval(tick);
    const left = exam.end - Date.now();
    if (left <= 0) { finishExam(true); return; }
    const t = document.getElementById("timer");
    if (t) { t.textContent = fmt(left); t.classList.toggle("low", left < 300000); }
  }, 1000);
}
const fmt = ms => String(Math.floor(ms / 60000)).padStart(2, "0") + ":" + String(Math.floor(ms / 1000) % 60).padStart(2, "0");
function viewExam(v) {
  if (!CERT.examReady) {
    v.append(el("h2", { text: L("Simulacro de examen") }));
    v.append(el("p", { class: "muted", style: "margin-top:6px", text: L("El simulacro estará disponible cuando estén todos los capítulos. Mientras, practica por capítulos en la pestaña Practicar.") }));
    return;
  }
  if (!exam) {
    v.append(el("h2", { text: L("Simulacro de examen") }));
    v.append(el("p", { class: "muted", style: "margin-top:6px", text: L("40 preguntas repartidas exactamente como el examen oficial: por capítulo (8 · 6 · 4 · 11 · 9 · 2), por grupo de objetivos y por nivel K (8 K1 · 24 K2 · 8 K3). Primero salen las preguntas que menos has visto en simulacros. No verás si aciertas hasta entregar. Cada pregunta vale 1 punto y se aprueba con 26.") }));
    const mins = el("select", { id: "examMins", class: "btn", "aria-label": L("Duración") }, el("option", { value: "75" }, L("75 min (no nativo, +25 %)")), el("option", { value: "60" }, L("60 min (estándar)")));
    v.append(el("div", { class: "row", style: "margin-top:14px" }, mins, el("button", { class: "btn primary", type: "button", onclick: () => startExam(Number(mins.value)) }, L("Empezar simulacro"))));
    if (P.exams.length) v.append(examHistory());
    return;
  }
  if (exam.done) return examResult(v);
  const left = Math.max(0, exam.end - Date.now());
  v.append(el("div", { class: "row spread" }, el("span", { class: "timer" + (left < 300000 ? " low" : ""), id: "timer", text: fmt(left) }), el("span", { class: "muted mono", text: exam.answers.filter(a => a != null).length + L("/40 respondidas") })));
  const g = el("div", { class: "examgrid", style: "margin-top:10px", "aria-label": L("Navegador de preguntas") });
  exam.items.forEach((_, i) => g.append(el("button", { type: "button", class: [exam.answers[i] != null ? "done" : "", exam.flags[i] ? "flag" : "", i === exam.i ? "cur" : ""].join(" "), "aria-label": L("Pregunta ") + (i + 1), onclick: () => { exam.i = i; saveExam(); render(); } }, String(i + 1))));
  v.append(g);
  const card = questionCard(exam.items[exam.i], { counter: (exam.i + 1) + " / 40", chosen: exam.answers[exam.i], reveal: false, onPick: pos => { exam.answers[exam.i] = pos; exam.confirm = false; saveExam(); render(); } });
  card.style.marginTop = "12px"; v.append(card);
  v.append(el("div", { class: "row spread", style: "margin-top:12px" },
    el("div", { class: "row" },
      el("button", { class: "btn", type: "button", disabled: exam.i === 0, onclick: () => { exam.i--; saveExam(); render(); } }, L("Anterior")),
      el("button", { class: "btn", type: "button", onclick: () => { exam.flags[exam.i] = !exam.flags[exam.i]; saveExam(); render(); } }, exam.flags[exam.i] ? L("Quitar marca") : L("Marcar")),
      el("button", { class: "btn", type: "button", disabled: exam.i === 39, onclick: () => { exam.i++; saveExam(); render(); } }, L("Siguiente"))),
    el("button", { class: "btn primary", type: "button", onclick: () => { if (exam.confirm) finishExam(false); else { exam.confirm = true; render(); } } }, exam.confirm ? L("Confirmar entrega") : L("Entregar"))));
  if (exam.confirm) v.append(el("p", { class: "muted", style: "margin-top:6px", text: L("Quedan ") + exam.answers.filter(a => a == null).length + L(" sin responder. Pulsa «Confirmar entrega» para corregir.") }));
  v.append(el("button", { class: "btn small danger", type: "button", style: "margin-top:16px", onclick: () => { if (exam.abandon) { exam = null; saveExam(); clearInterval(tick); render(); } else { exam.abandon = true; render(); } } }, exam.abandon ? L("Pulsa otra vez para abandonar sin guardar") : L("Abandonar simulacro")));
}
function finishExam(timeout) {
  clearInterval(tick);
  let score = 0; const ch = {}, k = {};
  exam.items.forEach((it, i) => {
    const x = QBY[it.id], ok = exam.answers[i] === it.correct;
    if (ok) score++;
    (ch[x.ch] = ch[x.ch] || [0, 0])[1]++; if (ok) ch[x.ch][0]++;
    (k[x.k] = k[x.k] || [0, 0])[1]++; if (ok) k[x.k][0]++;
    record(it.id, ok);
    P.seen[it.id] = (P.seen[it.id] || 0) + 1;
  });
  Object.assign(exam, { done: true, score, ch, k, i: 0, timeout });
  P.exams.push({ id: Date.now() + "-" + Math.random().toString(36).slice(2, 7), at: Date.now(), score, total: 40, ch, k, mins: Math.round((Date.now() - exam.start) / 60000) });
  P.exams = P.exams.slice(-60);
  save(); saveExam(); render();
  if (timeout) toast("Se acabó el tiempo: el simulacro se ha corregido automáticamente.");
}
function examResult(v) {
  const pass = exam.score >= CERT.pass;
  v.append(el("div", { class: "score " + (pass ? "pass" : "fail") }, el("span", { class: "eyebrow", text: L("Resultado del simulacro") }), el("span", { class: "big mono", text: exam.score + "/40" }), el("p", { text: pass ? L("Aprobado (26 o más).") : L("Suspenso: faltan ") + (26 - exam.score) + L(" para el 26.") })));
  const t1 = el("table", {}, el("thead", {}, el("tr", {}, el("th", { text: L("Capítulo") }), el("th", { class: "num", text: L("Aciertos") }))));
  const b1 = el("tbody");
  for (const c of CERT.chapters) { const r = exam.ch[c] || [0, 0]; b1.append(el("tr", {}, el("td", { text: c + ". " + CHAPTER_NAMES[c] }), el("td", { class: "num", text: r[0] + "/" + r[1] }))); }
  t1.append(b1);
  const t2 = el("table", {}, el("thead", {}, el("tr", {}, el("th", { text: L("Nivel K") }), el("th", { class: "num", text: L("Aciertos") }))));
  const b2 = el("tbody");
  for (const kk of [1, 2, 3]) { const r = exam.k[kk] || [0, 0]; b2.append(el("tr", {}, el("td", { text: "K" + kk + (kk === 1 ? L(" · recordar") : kk === 2 ? L(" · comprender") : L(" · aplicar")) }), el("td", { class: "num", text: r[0] + "/" + r[1] }))); }
  t2.append(b2);
  v.append(el("div", { class: "stack", style: "margin-top:12px" }, el("div", { class: "tablebox" }, t1), el("div", { class: "tablebox" }, t2)));
  v.append(el("h3", { text: L("Revisión pregunta a pregunta"), style: "margin-top:16px" }));
  const g = el("div", { class: "examgrid", style: "margin-top:8px" });
  exam.items.forEach((it, i) => g.append(el("button", { type: "button", class: (exam.answers[i] === it.correct ? "ok" : "ko") + (i === exam.i ? " cur" : ""), "aria-label": L("Pregunta ") + (i + 1), onclick: () => { exam.i = i; render(); } }, String(i + 1))));
  v.append(g);
  const card = questionCard(exam.items[exam.i], { counter: (exam.i + 1) + " / 40", chosen: exam.answers[exam.i], reveal: true });
  card.style.marginTop = "10px"; v.append(card);
  v.append(el("div", { class: "row spread", style: "margin-top:12px" },
    el("div", { class: "row" }, el("button", { class: "btn", type: "button", disabled: exam.i === 0, onclick: () => { exam.i--; render(); } }, L("Anterior")), el("button", { class: "btn", type: "button", disabled: exam.i === 39, onclick: () => { exam.i++; render(); } }, L("Siguiente"))),
    el("button", { class: "btn primary", type: "button", onclick: () => { exam = null; saveExam(); render(); } }, L("Cerrar simulacro"))));
}
function examHistory() {
  const t = el("table", {}, el("thead", {}, el("tr", {}, el("th", { text: L("Fecha") }), el("th", { class: "num", text: L("Nota") }), el("th", { class: "num", text: "K3" }), el("th", { class: "num", text: "Min" }), el("th", { text: "" }))));
  const tb = el("tbody");
  P.exams.slice().reverse().slice(0, 12).forEach(e => {
    const k3 = e.k && e.k[3] ? e.k[3][0] + "/" + e.k[3][1] : "—";
    tb.append(el("tr", {}, el("td", { text: new Date(e.at).toLocaleDateString("es-ES", { day: "2-digit", month: "short" }) }), el("td", { class: "num", text: e.score + "/40" }), el("td", { class: "num", text: k3 }), el("td", { class: "num", text: String(e.mins) }), el("td", { text: e.score >= 26 ? L("Aprobado") : L("Suspenso") })));
  });
  t.append(tb);
  return el("div", { class: "stack", style: "margin-top:20px" }, el("h3", { text: L("Últimos simulacros") }), el("div", { class: "tablebox" }, t));
}

// ---------------- wrong answers ----------------
let review = null;
function viewReview(v) {
  const failed = Q.filter(x => { const s = P.q[x.id]; return s && s.w > 0 && s.box < 2; }).sort((a, b) => qs(a.id).box - qs(b.id).box || qs(b.id).w - qs(a.id).w);
  if (!review || review.i >= review.items.length) {
    review = null;
    v.append(el("h2", { text: L("Preguntas falladas") }));
    if (!failed.length) { v.append(el("p", { class: "empty", style: "margin-top:10px", text: L("No tienes preguntas pendientes. Cuando falles una en Práctica o en un simulacro, aparecerá aquí hasta que la aciertes dos veces seguidas.") })); return; }
    v.append(el("p", { class: "muted", style: "margin-top:6px", text: failed.length + L(" pendientes. Una pregunta sale de aquí cuando la aciertas dos veces seguidas.") }));
    v.append(el("button", { class: "btn primary", type: "button", style: "margin-top:12px", onclick: () => { review = { items: failed.slice(0, 15).map(prepare), i: 0, chosen: null }; render(); } }, L("Repasar ") + Math.min(15, failed.length)));
    return;
  }
  const it = review.items[review.i], reveal = review.chosen != null;
  v.append(questionCard(it, { counter: (review.i + 1) + " / " + review.items.length, chosen: review.chosen, reveal, onPick: pos => { review.chosen = pos; record(it.id, pos === it.correct); save(); render(); } }));
  v.append(el("div", { class: "row spread", style: "margin-top:12px" }, el("button", { class: "btn", type: "button", onclick: () => { review = null; render(); } }, L("Terminar")),
    reveal ? el("button", { class: "btn primary", type: "button", onclick: () => { review.i++; review.chosen = null; render(); window.scrollTo(0, 0); } }, L("Siguiente")) : el("span", { class: "muted", text: L("Elige una respuesta") })));
}

// ---------------- syllabus (temario) ----------------
function viewSyllabus(v) {
  v.append(el("div", { class: "row spread" }, el("h2", { text: L("Temario") }), el("span", { class: "muted", text: L("Resúmenes propios por objetivo de aprendizaje") })));
  const off = el("section", { class: "panel official", style: "margin-top:12px" }, el("h3", { text: L("Materiales oficiales (gratis, istqb.org)") }),
    el("ul", {}, OFFICIAL.map(([t, id]) => el("li", {}, ext("https://istqb.org/?sdm_process_download=1&download_id=" + id, L(t))))),
    el("p", { class: "note", text: L("Estudia con el syllabus oficial delante: cada objetivo indica su página. Los niveles K indican la profundidad: K1 recordar, K2 comprender, K3 aplicar.") }),
    el("p", { class: "note" }, L("Glosario oficial: "), ext("https://glossary.istqb.org/", "glossary.istqb.org")));
  v.append(off);
  const wrap = el("div", { class: "stack", style: "margin-top:12px" });
  for (const ch of SYL.chapters) {
    const list = Q.filter(x => x.ch === ch.ch);
    const d = el("details", { class: "chapter", open: openChapters.has(ch.ch) });
    d.addEventListener("toggle", () => { d.open ? openChapters.add(ch.ch) : openChapters.delete(ch.ch); });
    d.append(el("summary", {}, el("h3", { text: ch.ch + ". " + tr("ch:" + ch.ch, "title", ch.title) }), el("span", { class: "eyebrow", text: ch.minutes + L(" min · ") + mastery(list) + " %" })));
    const body = el("div", { class: "chapbody" });
    for (const s of ch.sections) {
      body.append(el("div", { class: "row spread" }, el("h3", { text: s.sec + " " + tr("sec:" + s.sec, "title", s.title) }), ext(SYLLABUS_URL, L("pág. ") + s.page)));
      for (const lo of s.los) {
        const qlist = Q.filter(x => x.sec === lo.lo);
        const node = el("article", { class: "lo", id: "lo-" + lo.lo },
          el("div", { class: "row" }, el("span", { class: "badge" + (lo.k === 3 ? " k3" : ""), text: CERT.loPrefix + lo.lo + " · K" + lo.k }), el("strong", { text: tr("lo:" + lo.lo, "title", lo.title) })),
          el("p", { class: "note", text: "LO: " + tr("lo:" + lo.lo, "stmt", lo.stmt) + SYL_PAGE(" · ") + LO_PAGE(lo.lo) }),
          el("p", { text: tr("lonote:" + lo.lo, "sum", lo.sum, LANG, "es") }),
          el("div", { class: "terms" }, lo.terms.map(t => el("a", { href: GLOSSARY_URL(t), target: "_blank", rel: "noopener", title: L("Abrir en el glosario oficial") }, t))));
        const ex = lo.example && tr("lonote:" + lo.lo, "example", lo.example, LANG, "es");
        if (ex) node.append(el("div", { class: "example" }, el("strong", { text: ex.title }), el("p", { text: ex.problem }), el("ol", {}, ex.steps.map(s2 => el("li", { text: s2 })))));
        node.append(el("div", { class: "row" },
          el("button", { class: "btn small primary", type: "button", onclick: () => startPractice(qlist, L("Practicando ") + CERT.loPrefix + lo.lo + " " + tr("lo:" + lo.lo, "title", lo.title), lo.lo) }, L("Practicar (") + qlist.length + ")"),
          el("span", { class: "note", text: L("Dominio ") + mastery(qlist) + " %" })));
        body.append(node);
      }
    }
    d.append(body); wrap.append(d);
  }
  v.append(wrap);
}
const LO_PAGE = lo => { const x = Q.find(y => y.sec === lo); return x ? x.page : "—"; };

// ---------------- glossary cards ----------------
let cardState = null;
let glossMode = "dict", glossQuery = "";
function viewCards(v) {
  v.append(el("div", { class: "row", role: "group", "aria-label": L("Modo") },
    el("button", { class: "btn small" + (glossMode === "dict" ? " primary" : ""), type: "button", onclick: () => { glossMode = "dict"; render(); } }, LANG === "es" ? "Diccionario" : "Dictionary"),
    el("button", { class: "btn small" + (glossMode === "cards" ? " primary" : ""), type: "button", onclick: () => { glossMode = "cards"; render(); } }, LANG === "es" ? "Tarjetas" : "Flashcards")));
  if (glossMode === "dict") return viewDictionary(v);
  viewFlashcards(v);
}
const GLOSS_CH = { 0: ["Conceptos de código", "Code concepts"], 7: ["Más allá del examen: lo que oirás en el trabajo", "Beyond the exam: what you will hear at work"] };
// `text` inside backticks is shown as inline code.
const withCode = txt => String(txt).split(/`([^`]+)`/).map((part, i) => i % 2 ? el("code", { text: part }) : part);
function viewDictionary(v) {
  const es = LANG === "es";
  const q = el("input", { type: "search", class: "search", value: glossQuery, placeholder: es ? "Buscar término… (p. ej. branch)" : "Search a term… (e.g. branch)", "aria-label": es ? "Buscar término" : "Search a term" });
  const list = el("div", { class: "stack", style: "margin-top:12px" });
  const draw = () => {
    const needle = glossQuery.trim().toLowerCase();
    list.replaceChildren();
    for (const ch of [0, ...CERT.chapters, 7]) {
      const items = GLOSS.filter(g => g.ch === ch).map(g => ({ g, t: es ? g.es : (I18N["gl:" + g.term] || {}).t || g.es }))
        .filter(({ g, t }) => !needle || (g.term + " " + t.def).toLowerCase().includes(needle));
      if (!items.length) continue;
      list.append(el("h3", { text: GLOSS_CH[ch] ? GLOSS_CH[ch][es ? 0 : 1] : ch + ". " + tr("ch:" + ch, "title", CHAPTER_NAMES[ch]) }));
      for (const { g, t } of items) {
        const node = el("article", { class: "lo gloss" },
          el("div", { class: "row spread" }, el("strong", { text: g.term }), (g.official ?? (g.ch >= 1 && g.ch <= 6)) ? ext(GLOSSARY_URL(g.term), es ? "Glosario oficial ↗" : "Official glossary ↗") : ""),
          el("p", { text: t.def }),
          el("p", { class: "note" }, el("strong", { text: es ? "En tu trabajo: " : "In your work: " }), ...withCode(t.work)));
        if (g.code) node.append(el("pre", { class: "code" }, g.code));
        list.append(node);
      }
    }
    if (!list.children.length) list.append(el("p", { class: "empty", text: es ? "Ningún término coincide." : "No matching terms." }));
  };
  q.addEventListener("input", () => { glossQuery = q.value; draw(); });
  v.append(el("div", { style: "margin-top:12px" }, q));
  v.append(el("p", { class: "note", style: "margin-top:6px", text: (es ? "Explicaciones propias de " : "Own explanations of ") + GLOSS.length + (es ? " términos: los clave del syllabus y los que oirás en el trabajo, con ejemplos. El enlace lleva a la definición oficial." : " terms: the syllabus key terms and the ones you will hear at work, with examples. The link opens the official definition.") }));
  v.append(list);
  draw();
}
function viewFlashcards(v) {
  if (!cardState) cardState = { order: shuffle(CARDS.map((_, i) => i)).sort((a, b) => ((P.cards[a] || {}).box || 0) - ((P.cards[b] || {}).box || 0)), i: 0, flip: false };
  const idx = cardState.order[cardState.i % cardState.order.length], [term, defEs, defEn] = CARDS[idx], def = LANG === "es" ? defEs : defEn;
  const known = Object.values(P.cards).filter(c => c.box >= 2).length;
  v.append(el("div", { class: "row spread" }, el("h2", { text: L("Glosario") }), el("span", { class: "muted mono", text: known + "/" + CARDS.length + L(" dominados") })));
  v.append(el("button", { class: "flash", type: "button", style: "margin-top:12px", "aria-label": L("Girar tarjeta"), onclick: () => { cardState.flip = !cardState.flip; render(); } },
    el("span", { class: "eyebrow", text: cardState.flip ? (LANG === "es" ? "Definición (explicación propia)" : "Definition (own explanation)") : L("Término · toca para girar") }),
    cardState.flip ? el("span", { class: "def", text: def }) : el("span", { class: "term", text: term })));
  const mark = ok => { const c = Object.assign({ box: 0 }, P.cards[idx]); c.box = ok ? Math.min(c.box + 1, 4) : 0; c.last = Date.now(); P.cards[idx] = c; save(); cardState.i++; cardState.flip = false; render(); };
  v.append(el("div", { class: "row spread", style: "margin-top:12px" },
    el("div", { class: "row" }, el("button", { class: "btn", type: "button", onclick: () => mark(false) }, L("Repasar otra vez")), el("button", { class: "btn primary", type: "button", onclick: () => mark(true) }, L("Me lo sé"))),
    ext(GLOSSARY_URL(term.split(" / ")[0]), L("Definición oficial ↗"))));
}

// ---------------- progress & backup ----------------
let resetArmed = false;
function viewProgress(v) {
  v.append(el("h2", { text: L("Progreso") }));
  const t = el("table", {}, el("thead", {}, el("tr", {}, el("th", { text: L("Capítulo") }), el("th", { class: "num", text: L("Vistas") }), el("th", { class: "num", text: L("Acierto") }), el("th", { class: "num", text: L("Dominio") }))));
  const tb = el("tbody");
  for (const ch of CERT.chapters) {
    const list = Q.filter(x => x.ch === ch), seen = list.filter(x => P.q[x.id]).length;
    const c = list.reduce((s, x) => s + qs(x.id).c, 0), w = list.reduce((s, x) => s + qs(x.id).w, 0);
    tb.append(el("tr", {}, el("td", { text: ch + ". " + CHAPTER_NAMES[ch] }), el("td", { class: "num", text: seen + "/" + list.length }), el("td", { class: "num", text: c + w ? Math.round(100 * c / (c + w)) + " %" : "—" }), el("td", { class: "num", text: mastery(list) + " %" })));
  }
  for (const k of [1, 2, 3]) {
    const list = Q.filter(x => x.k === k);
    tb.append(el("tr", {}, el("td", { text: L("Todas las K") + k }), el("td", { class: "num", text: list.filter(x => P.q[x.id]).length + "/" + list.length }), el("td", { class: "num", text: "" }), el("td", { class: "num", text: mastery(list) + " %" })));
  }
  t.append(tb); v.append(el("div", { class: "tablebox", style: "margin-top:10px" }, t));
  v.append(el("p", { class: "note", style: "margin-top:8px", text: L("Dominio: una pregunta cuenta como dominada cuando la aciertas tres veces seguidas; si la fallas, vuelve a cero.") }));
  if (P.exams.length) v.append(examHistory());

  // backup
  const ta = el("textarea", { id: "syncCode", "aria-label": L("Código de progreso"), placeholder: L("Aquí aparecerá tu código, o pega aquí el código del otro dispositivo.") });
  const file = el("input", { type: "file", id: "importFile", accept: ".json,application/json", hidden: true });
  file.addEventListener("change", async () => {
    const f = file.files[0]; if (!f) return;
    try { P = merge(P, JSON.parse(await f.text())); save(); toast("Copia importada y fusionada."); render(); }
    catch (e) { toast("No se pudo leer el fichero: " + e.message); }
  });
  const panel = el("section", { class: "panel", style: "margin-top:20px" },
    el("h3", { text: L("Copia de seguridad y sincronización") }),
    el("p", { class: "note", text: L("Tu progreso solo vive en este navegador. Para pasarlo al móvil (o al revés): «Copiar progreso» aquí, y «Pegar y fusionar» en el otro dispositivo. Al fusionar se conserva, para cada pregunta, la respuesta más reciente, y se juntan los simulacros de los dos.") }),
    ta,
    el("div", { class: "row" },
      el("button", { class: "btn primary", type: "button", onclick: async () => {
        const code = await encodeProgress(); ta.value = code;
        try { await navigator.clipboard.writeText(code); toast("Código copiado al portapapeles."); }
        catch { ta.focus(); ta.select(); toast("Selecciona el texto y cópialo a mano."); }
      } }, L("Copiar progreso")),
      el("button", { class: "btn", type: "button", onclick: async () => {
        if (!ta.value.trim()) { toast("Pega primero el código del otro dispositivo en el cuadro."); return; }
        try { P = merge(P, await decodeProgress(ta.value)); save(); ta.value = ""; toast("Progreso fusionado."); render(); }
        catch (e) { toast(e.message || L("Código no válido.")); }
      } }, L("Pegar y fusionar"))),
    el("div", { class: "row" },
      el("button", { class: "btn", type: "button", onclick: () => {
        const blob = new Blob([JSON.stringify(P, null, 1)], { type: "application/json" });
        const a = el("a", { href: URL.createObjectURL(blob), download: "ctfl-progreso-" + new Date().toISOString().slice(0, 10) + ".json" });
        document.body.append(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(a.href), 2000);
      } }, L("Descargar copia (.json)")),
      el("button", { class: "btn", type: "button", onclick: () => file.click() }, L("Importar copia (.json)")), file),
    el("div", { class: "row", style: "margin-top:6px" },
      el("button", { class: "btn small danger", type: "button", onclick: () => { if (resetArmed) { P = blank(); save(); resetArmed = false; toast("Progreso borrado."); render(); } else { resetArmed = true; render(); } } }, resetArmed ? L("Pulsa otra vez para borrar todo el progreso") : L("Borrar progreso"))));
  v.append(panel);
}

// ---------------- boot ----------------
document.querySelectorAll("nav.tabs button").forEach(b => b.addEventListener("click", () => { resetArmed = false; go(b.dataset.view); }));
document.querySelectorAll("#certToggle button").forEach(b => {
  b.setAttribute("aria-pressed", String(b.dataset.cert === CERT.id));
  b.addEventListener("click", () => {
    if (b.dataset.cert === CERT.id) return;
    try { localStorage.setItem("study-cert", b.dataset.cert); } catch (e) { /* ignore */ }
    location.hash = ""; location.reload();
  });
});
applyStaticLang();
document.querySelectorAll("#langToggle button").forEach(b => {
  b.setAttribute("aria-pressed", String(b.dataset.lang === LANG));
  b.addEventListener("click", () => setLang(b.dataset.lang));
});
window.addEventListener("hashchange", () => { const h = location.hash.slice(1); if (VIEWS.includes(h) && h !== current) go(h); });
function onlineChip() { $("#offlineChip").hidden = navigator.onLine; }
window.addEventListener("online", onlineChip); window.addEventListener("offline", onlineChip);

(async function boot() {
  load(); onlineChip();
  try { await loadData(); }
  catch (e) { $("#view").replaceChildren(el("p", { class: "empty", text: L("No se pudo cargar el banco de preguntas. Comprueba la conexión la primera vez que abras la app; después funciona sin conexión.") })); return; }
  loadExam(); if (exam) startTick();
  const h = location.hash.slice(1); if (VIEWS.includes(h)) current = h;
  if (exam && !exam.done) current = "simulacro";
  render();
})();

if ("serviceWorker" in navigator && location.protocol !== "file:") {
  navigator.serviceWorker.register("sw.js").then(reg => {
    reg.addEventListener("updatefound", () => {
      const nw = reg.installing; if (!nw) return;
      nw.addEventListener("statechange", () => {
        if (nw.state === "installed" && navigator.serviceWorker.controller) toast("Hay una versión nueva del banco.", { label: L("Actualizar"), fn: () => nw.postMessage("skipWaiting") });
      });
    });
  }).catch(() => {});
  let reloaded = false;
  navigator.serviceWorker.addEventListener("controllerchange", () => { if (!reloaded) { reloaded = true; location.reload(); } });
}

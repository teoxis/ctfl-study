"use strict";
/* Banco CTFL — static PWA, no backend. Progress lives in localStorage and can be
   exported/imported as a text code or a .json file. */

const SYLLABUS_URL = "https://istqb.org/?sdm_process_download=1&download_id=3345";
const GLOSSARY_URL = t => "https://glossary.istqb.org/en_US/search?term=" + encodeURIComponent(t);
const OFFICIAL = [
  ["Syllabus CTFL v4.0.1 (PDF)", 3345],
  ["Sample Exam A · preguntas", 3352], ["Sample Exam A · respuestas", 3357],
  ["Sample Exam B · preguntas", 3359], ["Sample Exam B · respuestas", 3365],
  ["Sample Exam C · preguntas", 3369], ["Sample Exam C · respuestas", 3372],
  ["Sample Exam D · preguntas", 3376], ["Sample Exam D · respuestas", 3380],
  ["Exam Structures and Rules", 3829], ["Exam Structures & Rules Tables (reparto por LO)", 3832],
];
const CHAPTER_NAMES = {1: "Fundamentals of Testing", 2: "Testing Throughout the SDLC", 3: "Static Testing", 4: "Test Analysis and Design", 5: "Managing the Test Activities", 6: "Test Tools"};
const LETTERS = ["A", "B", "C", "D"];

const CARDS = [
 ["Test basis", "Todo lo que sirve de base para el análisis y diseño de pruebas: requisitos, historias de usuario, diseño, código, riesgos…"],
 ["Test condition", "Aspecto comprobable de un componente o sistema, identificado como base para las pruebas. Responde a \"qué probar\"."],
 ["Test case", "Conjunto de precondiciones, entradas, acciones, resultados esperados y postcondiciones, diseñado a partir de condiciones de prueba."],
 ["Test procedure", "Secuencia de casos de prueba en orden de ejecución, con las acciones necesarias para preparar y cerrar."],
 ["Testware", "Productos de trabajo que se generan al probar: planes, casos, scripts, datos, informes…"],
 ["Coverage item", "Atributo o combinación de atributos derivado de una o varias condiciones de prueba mediante una técnica; sirve para medir la cobertura."],
 ["Error / Defect / Failure", "Error: equivocación humana. Defecto: imperfección en un producto de trabajo. Fallo: el sistema hace algo distinto de lo esperado al ejecutarse."],
 ["Root cause", "Razón fundamental por la que ocurre un problema. Atacarla previene defectos similares."],
 ["Confirmation testing", "Comprobar que el defecto original se ha corregido."],
 ["Regression testing", "Comprobar que un cambio no ha causado efectos adversos en lo que ya funcionaba."],
 ["Maintenance testing", "Pruebas de un sistema en producción por modificaciones, migraciones del entorno o retirada."],
 ["Shift left", "Probar antes en el ciclo de vida, sin descuidar las pruebas posteriores."],
 ["TDD / ATDD / BDD", "TDD: tests de componente antes del código. ATDD: tests a partir de los criterios de aceptación, antes de implementar. BDD: comportamiento en Given/When/Then que se traduce en tests ejecutables."],
 ["Static testing", "Prueba sin ejecutar el software (revisiones y análisis estático). Encuentra defectos directamente."],
 ["Inspection", "El tipo de revisión más formal: proceso completo, métricas, objetivo de encontrar el máximo de anomalías. El autor no puede ser líder ni escriba."],
 ["Walkthrough", "Revisión dirigida por el autor. Objetivos: evaluar, formar, lograr consenso, generar ideas y detectar anomalías."],
 ["Technical review", "Revisores técnicamente cualificados dirigidos por un moderador. Objetivo: consenso y decisiones sobre un problema técnico."],
 ["Equivalence partitioning", "Divide los datos en particiones que se procesan igual. Un valor por partición basta, incluidas las inválidas."],
 ["Boundary value analysis", "Prueba los valores frontera de particiones ordenadas. 2 valores: la frontera y su vecino. 3 valores: la frontera y sus dos vecinos."],
 ["Decision table testing", "Combina condiciones y acciones en reglas. Con n condiciones booleanas hay 2^n columnas; se cubren las factibles."],
 ["State transition testing", "Coberturas: todos los estados, transiciones válidas (0-switch) y todas las transiciones (también las inválidas)."],
 ["Statement coverage", "Sentencias ejecutadas / sentencias ejecutables."],
 ["Branch coverage", "Ramas ejercitadas / total de ramas. Subsume a la cobertura de sentencias."],
 ["Exploratory testing", "Diseño, ejecución y evaluación simultáneos mientras se aprende el producto; en sesiones con un test charter."],
 ["Risk level", "Combinación de la probabilidad y el impacto del riesgo. Determina la intensidad y la prioridad de las pruebas."],
 ["Product vs project risk", "Producto: características de calidad (funcionalidad, rendimiento, seguridad…). Proyecto: gestión del proyecto (retrasos, personas, proveedores, herramientas)."],
 ["Entry / exit criteria", "Entrada: precondiciones para empezar (Definition of Ready). Salida: cuándo se da por terminado (Definition of Done)."],
 ["Test pyramid", "Muchos tests rápidos y aislados en las capas bajas; pocos tests lentos extremo a extremo en las altas."],
 ["Testing quadrants", "Cuadrantes según dos ejes: de negocio o técnicos, y de apoyo al equipo o críticos con el producto (Q1 a Q4)."],
 ["Three-point estimation", "E = (a + 4m + b) / 6; SD = (b − a) / 6."],
 ["Configuration management", "Identificar, versionar y controlar el testware y los elementos de prueba; las líneas base permiten reproducir resultados."],
];

// ---------------- persistence ----------------
const LS_KEY = "ctfl-study-v1", EXAM_KEY = "ctfl-study-exam";
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
let Q = [], QBY = {}, EXAM = null, SYL = null, LO_INFO = {};
async function loadData() {
  const files = [1, 2, 3, 4, 5, 6].map(n => `data/bank-ch${n}.json`).concat(["data/exam.json", "data/syllabus.json"]);
  const res = await Promise.all(files.map(f => fetch(f).then(r => { if (!r.ok) throw new Error(f); return r.json(); })));
  Q = res.slice(0, 6).flat();
  EXAM = res[6]; SYL = res[7];
  for (const x of Q) QBY[x.id] = x;
  for (const ch of SYL.chapters) for (const s of ch.sections) for (const lo of s.los) LO_INFO[lo.lo] = { ...lo, ch: ch.ch, sec: s.sec, secTitle: s.title };
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
  $("#bankSize").textContent = Q.length + " preguntas en el banco";
  $("#masteryChip").textContent = "Dominio global: " + mastery(Q) + " %";
  const best = P.exams.reduce((m, e) => Math.max(m, e.score), -1);
  $("#bestChip").textContent = best < 0 ? "Sin simulacros todavía" : "Mejor simulacro: " + best + "/40";
}

// ---------------- routing ----------------
const VIEWS = ["practicar", "simulacro", "falladas", "temario", "glosario", "progreso"];
let current = "practicar";
function go(view, opts = {}) { current = view; render(); if (opts.scrollTo) requestAnimationFrame(() => { const n = document.getElementById(opts.scrollTo); if (n) { n.scrollIntoView({ block: "start" }); n.classList.add("hl"); } }); else window.scrollTo(0, 0); }
function render() {
  renderStatus();
  document.querySelectorAll("nav.tabs button").forEach(b => b.setAttribute("aria-selected", String(b.dataset.view === current)));
  if (location.hash !== "#" + current) history.replaceState(null, "", "#" + current);
  const v = $("#view"); v.replaceChildren();
  ({ practicar: viewPractice, simulacro: viewExam, falladas: viewReview, temario: viewSyllabus, glosario: viewCards, progreso: viewProgress })[current](v);
}

// ---------------- question card ----------------
function questionCard(item, o) {
  const x = QBY[item.id], info = LO_INFO[x.sec] || {};
  const card = el("section", { class: "qcard", "aria-label": "Pregunta" });
  card.append(el("div", { class: "qhead" },
    el("span", { class: "row" }, el("span", { class: "badge" + (x.k === 3 ? " k3" : ""), text: x.lo + " · K" + x.k }), el("span", { class: "eyebrow", text: "Cap. " + x.ch })),
    el("span", { class: "eyebrow mono", text: o.counter || x.id })));
  card.append(el("p", { class: "stem", text: x.q }));
  if (x.code) card.append(el("pre", { class: "code" }, x.code));
  const box = el("div", { class: "opts", role: "radiogroup", "aria-label": "Opciones" });
  item.order.forEach((oi, pos) => {
    const b = el("button", { class: "opt", role: "radio", type: "button", "aria-checked": String(o.chosen === pos) }, el("span", { class: "k", text: LETTERS[pos] }), el("span", { text: x.o[oi] }));
    if (o.reveal) { b.disabled = true; if (pos === item.correct) b.classList.add("right"); else if (pos === o.chosen) b.classList.add("wrong"); }
    else b.addEventListener("click", () => o.onPick(pos));
    box.append(b);
  });
  card.append(box);
  if (o.reveal) {
    const ok = o.chosen === item.correct;
    card.append(el("div", { class: "explain" + (ok ? "" : " bad") },
      el("span", { class: "verdict " + (ok ? "good" : "bad"), text: o.chosen == null ? "Sin responder · correcta: " + LETTERS[item.correct] : ok ? "Correcta" : "Incorrecta · correcta: " + LETTERS[item.correct] }),
      el("p", { text: x.e }),
      el("p", { class: "note" },
        el("a", { href: "#temario", onclick: ev => { ev.preventDefault(); openLO(x.sec); } }, "Estudia esto: " + x.lo + " " + (info.title || "")),
        " · ", ext(SYLLABUS_URL, "Syllabus v4.0.1, pág. " + x.page))));
  }
  return card;
}
let openChapters = new Set();
function openLO(sec) { openChapters.add(Number(sec[0])); go("temario", { scrollTo: "lo-" + sec }); }

// ---------------- practice ----------------
let practice = null, selectedCh = new Set([1, 2, 3, 4, 5, 6]), practiceLO = null;
function startPractice(pool, label) {
  const ranked = shuffle(pool).sort((a, b) => qs(a.id).box - qs(b.id).box);
  practice = { items: ranked.slice(0, 10).map(prepare), i: 0, chosen: null, right: 0, label };
  go("practicar");
}
function viewPractice(v) {
  if (practice && practice.i < practice.items.length) return practiceRun(v);
  if (practice) return practiceDone(v);
  v.append(el("div", { class: "row spread" }, el("h2", { text: "Práctica por capítulos" }), el("span", { class: "muted", text: "Tandas de 10, primero lo que no dominas" })));
  const grid = el("div", { class: "chapters", style: "margin-top:12px" });
  for (const ch of [1, 2, 3, 4, 5, 6]) {
    const list = Q.filter(x => x.ch === ch), m = mastery(list);
    const n = EXAM.groups.filter(g => g.ch === ch).reduce((s, g) => s + g.n, 0);
    grid.append(el("button", { class: "chap", type: "button", "aria-pressed": String(selectedCh.has(ch)), onclick: () => { selectedCh.has(ch) ? selectedCh.delete(ch) : selectedCh.add(ch); render(); } },
      el("span", { class: "name", text: ch + ". " + CHAPTER_NAMES[ch] }),
      el("div", { class: "bar", "aria-hidden": "true" }, el("i", { style: "width:" + m + "%" })),
      el("span", { class: "meta" }, el("span", { text: list.length + " preguntas · " + n + " en examen" }), el("span", { text: m + " %" }))));
  }
  v.append(grid);
  const b = el("button", { class: "btn primary", type: "button", style: "margin-top:14px", onclick: () => startPractice(Q.filter(x => selectedCh.has(x.ch)), "Capítulos " + [...selectedCh].sort().join(", ")) }, "Empezar tanda");
  b.disabled = !selectedCh.size;
  v.append(b);
  v.append(el("p", { class: "note", style: "margin-top:10px", text: "¿Quieres practicar un objetivo concreto? Ve a Temario y pulsa «Practicar» en cualquier LO." }));
}
function practiceRun(v) {
  const it = practice.items[practice.i], reveal = practice.chosen != null;
  if (practice.label) v.append(el("p", { class: "eyebrow", style: "margin-bottom:8px", text: practice.label }));
  v.append(questionCard(it, { counter: (practice.i + 1) + " / " + practice.items.length, chosen: practice.chosen, reveal,
    onPick: pos => { practice.chosen = pos; const ok = pos === it.correct; if (ok) practice.right++; record(it.id, ok); save(); render(); } }));
  v.append(el("div", { class: "row spread", style: "margin-top:12px" },
    el("button", { class: "btn", type: "button", onclick: () => { practice = null; render(); } }, "Terminar"),
    reveal ? el("button", { class: "btn primary", type: "button", onclick: () => { practice.i++; practice.chosen = null; render(); window.scrollTo(0, 0); } }, practice.i + 1 < practice.items.length ? "Siguiente" : "Ver resultado") : el("span", { class: "muted", text: "Elige una respuesta" })));
}
function practiceDone(v) {
  const n = practice.items.length, r = practice.right, good = r / n >= 0.65;
  v.append(el("div", { class: "score " + (good ? "pass" : "fail") }, el("span", { class: "eyebrow", text: "Tanda terminada" }), el("span", { class: "big mono", text: r + "/" + n }), el("p", { text: good ? "Por encima del 65 % que exige el examen." : "Por debajo del 65 %. Las falladas pasan a la pestaña Falladas." })));
  v.append(el("div", { class: "row", style: "margin-top:12px" }, el("button", { class: "btn primary", type: "button", onclick: () => { practice = null; render(); } }, "Otra tanda")));
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
  if (!exam) {
    v.append(el("h2", { text: "Simulacro de examen" }));
    v.append(el("p", { class: "muted", style: "margin-top:6px", text: "40 preguntas repartidas exactamente como el examen oficial: por capítulo (8 · 6 · 4 · 11 · 9 · 2), por grupo de objetivos y por nivel K (8 K1 · 24 K2 · 8 K3). Primero salen las preguntas que menos has visto en simulacros. No verás si aciertas hasta entregar. Cada pregunta vale 1 punto y se aprueba con 26." }));
    const mins = el("select", { id: "examMins", class: "btn", "aria-label": "Duración" }, el("option", { value: "75" }, "75 min (no nativo, +25 %)"), el("option", { value: "60" }, "60 min (estándar)"));
    v.append(el("div", { class: "row", style: "margin-top:14px" }, mins, el("button", { class: "btn primary", type: "button", onclick: () => startExam(Number(mins.value)) }, "Empezar simulacro")));
    if (P.exams.length) v.append(examHistory());
    return;
  }
  if (exam.done) return examResult(v);
  const left = Math.max(0, exam.end - Date.now());
  v.append(el("div", { class: "row spread" }, el("span", { class: "timer" + (left < 300000 ? " low" : ""), id: "timer", text: fmt(left) }), el("span", { class: "muted mono", text: exam.answers.filter(a => a != null).length + "/40 respondidas" })));
  const g = el("div", { class: "examgrid", style: "margin-top:10px", "aria-label": "Navegador de preguntas" });
  exam.items.forEach((_, i) => g.append(el("button", { type: "button", class: [exam.answers[i] != null ? "done" : "", exam.flags[i] ? "flag" : "", i === exam.i ? "cur" : ""].join(" "), "aria-label": "Pregunta " + (i + 1), onclick: () => { exam.i = i; saveExam(); render(); } }, String(i + 1))));
  v.append(g);
  const card = questionCard(exam.items[exam.i], { counter: (exam.i + 1) + " / 40", chosen: exam.answers[exam.i], reveal: false, onPick: pos => { exam.answers[exam.i] = pos; exam.confirm = false; saveExam(); render(); } });
  card.style.marginTop = "12px"; v.append(card);
  v.append(el("div", { class: "row spread", style: "margin-top:12px" },
    el("div", { class: "row" },
      el("button", { class: "btn", type: "button", disabled: exam.i === 0, onclick: () => { exam.i--; saveExam(); render(); } }, "Anterior"),
      el("button", { class: "btn", type: "button", onclick: () => { exam.flags[exam.i] = !exam.flags[exam.i]; saveExam(); render(); } }, exam.flags[exam.i] ? "Quitar marca" : "Marcar"),
      el("button", { class: "btn", type: "button", disabled: exam.i === 39, onclick: () => { exam.i++; saveExam(); render(); } }, "Siguiente")),
    el("button", { class: "btn primary", type: "button", onclick: () => { if (exam.confirm) finishExam(false); else { exam.confirm = true; render(); } } }, exam.confirm ? "Confirmar entrega" : "Entregar")));
  if (exam.confirm) v.append(el("p", { class: "muted", style: "margin-top:6px", text: "Quedan " + exam.answers.filter(a => a == null).length + " sin responder. Pulsa «Confirmar entrega» para corregir." }));
  v.append(el("button", { class: "btn small danger", type: "button", style: "margin-top:16px", onclick: () => { if (exam.abandon) { exam = null; saveExam(); clearInterval(tick); render(); } else { exam.abandon = true; render(); } } }, exam.abandon ? "Pulsa otra vez para abandonar sin guardar" : "Abandonar simulacro"));
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
  const pass = exam.score >= 26;
  v.append(el("div", { class: "score " + (pass ? "pass" : "fail") }, el("span", { class: "eyebrow", text: "Resultado del simulacro" }), el("span", { class: "big mono", text: exam.score + "/40" }), el("p", { text: pass ? "Aprobado (26 o más)." : "Suspenso: faltan " + (26 - exam.score) + " para el 26." })));
  const t1 = el("table", {}, el("thead", {}, el("tr", {}, el("th", { text: "Capítulo" }), el("th", { class: "num", text: "Aciertos" }))));
  const b1 = el("tbody");
  for (const c of [1, 2, 3, 4, 5, 6]) { const r = exam.ch[c] || [0, 0]; b1.append(el("tr", {}, el("td", { text: c + ". " + CHAPTER_NAMES[c] }), el("td", { class: "num", text: r[0] + "/" + r[1] }))); }
  t1.append(b1);
  const t2 = el("table", {}, el("thead", {}, el("tr", {}, el("th", { text: "Nivel K" }), el("th", { class: "num", text: "Aciertos" }))));
  const b2 = el("tbody");
  for (const kk of [1, 2, 3]) { const r = exam.k[kk] || [0, 0]; b2.append(el("tr", {}, el("td", { text: "K" + kk + (kk === 1 ? " · recordar" : kk === 2 ? " · comprender" : " · aplicar") }), el("td", { class: "num", text: r[0] + "/" + r[1] }))); }
  t2.append(b2);
  v.append(el("div", { class: "stack", style: "margin-top:12px" }, el("div", { class: "tablebox" }, t1), el("div", { class: "tablebox" }, t2)));
  v.append(el("h3", { text: "Revisión pregunta a pregunta", style: "margin-top:16px" }));
  const g = el("div", { class: "examgrid", style: "margin-top:8px" });
  exam.items.forEach((it, i) => g.append(el("button", { type: "button", class: (exam.answers[i] === it.correct ? "ok" : "ko") + (i === exam.i ? " cur" : ""), "aria-label": "Pregunta " + (i + 1), onclick: () => { exam.i = i; render(); } }, String(i + 1))));
  v.append(g);
  const card = questionCard(exam.items[exam.i], { counter: (exam.i + 1) + " / 40", chosen: exam.answers[exam.i], reveal: true });
  card.style.marginTop = "10px"; v.append(card);
  v.append(el("div", { class: "row spread", style: "margin-top:12px" },
    el("div", { class: "row" }, el("button", { class: "btn", type: "button", disabled: exam.i === 0, onclick: () => { exam.i--; render(); } }, "Anterior"), el("button", { class: "btn", type: "button", disabled: exam.i === 39, onclick: () => { exam.i++; render(); } }, "Siguiente")),
    el("button", { class: "btn primary", type: "button", onclick: () => { exam = null; saveExam(); render(); } }, "Cerrar simulacro")));
}
function examHistory() {
  const t = el("table", {}, el("thead", {}, el("tr", {}, el("th", { text: "Fecha" }), el("th", { class: "num", text: "Nota" }), el("th", { class: "num", text: "K3" }), el("th", { class: "num", text: "Min" }), el("th", { text: "" }))));
  const tb = el("tbody");
  P.exams.slice().reverse().slice(0, 12).forEach(e => {
    const k3 = e.k && e.k[3] ? e.k[3][0] + "/" + e.k[3][1] : "—";
    tb.append(el("tr", {}, el("td", { text: new Date(e.at).toLocaleDateString("es-ES", { day: "2-digit", month: "short" }) }), el("td", { class: "num", text: e.score + "/40" }), el("td", { class: "num", text: k3 }), el("td", { class: "num", text: String(e.mins) }), el("td", { text: e.score >= 26 ? "Aprobado" : "Suspenso" })));
  });
  t.append(tb);
  return el("div", { class: "stack", style: "margin-top:20px" }, el("h3", { text: "Últimos simulacros" }), el("div", { class: "tablebox" }, t));
}

// ---------------- wrong answers ----------------
let review = null;
function viewReview(v) {
  const failed = Q.filter(x => { const s = P.q[x.id]; return s && s.w > 0 && s.box < 2; }).sort((a, b) => qs(a.id).box - qs(b.id).box || qs(b.id).w - qs(a.id).w);
  if (!review || review.i >= review.items.length) {
    review = null;
    v.append(el("h2", { text: "Preguntas falladas" }));
    if (!failed.length) { v.append(el("p", { class: "empty", style: "margin-top:10px", text: "No tienes preguntas pendientes. Cuando falles una en Práctica o en un simulacro, aparecerá aquí hasta que la aciertes dos veces seguidas." })); return; }
    v.append(el("p", { class: "muted", style: "margin-top:6px", text: failed.length + " pendientes. Una pregunta sale de aquí cuando la aciertas dos veces seguidas." }));
    v.append(el("button", { class: "btn primary", type: "button", style: "margin-top:12px", onclick: () => { review = { items: failed.slice(0, 15).map(prepare), i: 0, chosen: null }; render(); } }, "Repasar " + Math.min(15, failed.length)));
    return;
  }
  const it = review.items[review.i], reveal = review.chosen != null;
  v.append(questionCard(it, { counter: (review.i + 1) + " / " + review.items.length, chosen: review.chosen, reveal, onPick: pos => { review.chosen = pos; record(it.id, pos === it.correct); save(); render(); } }));
  v.append(el("div", { class: "row spread", style: "margin-top:12px" }, el("button", { class: "btn", type: "button", onclick: () => { review = null; render(); } }, "Terminar"),
    reveal ? el("button", { class: "btn primary", type: "button", onclick: () => { review.i++; review.chosen = null; render(); window.scrollTo(0, 0); } }, "Siguiente") : el("span", { class: "muted", text: "Elige una respuesta" })));
}

// ---------------- syllabus (temario) ----------------
function viewSyllabus(v) {
  v.append(el("div", { class: "row spread" }, el("h2", { text: "Temario" }), el("span", { class: "muted", text: "Resúmenes propios por objetivo de aprendizaje" })));
  const off = el("section", { class: "panel official", style: "margin-top:12px" }, el("h3", { text: "Materiales oficiales (gratis, istqb.org)" }),
    el("ul", {}, OFFICIAL.map(([t, id]) => el("li", {}, ext("https://istqb.org/?sdm_process_download=1&download_id=" + id, t)))),
    el("p", { class: "note", text: "Estudia con el syllabus oficial delante: cada objetivo indica su página. Los niveles K indican la profundidad: K1 recordar, K2 comprender, K3 aplicar." }),
    el("p", { class: "note" }, "Glosario oficial: ", ext("https://glossary.istqb.org/", "glossary.istqb.org")));
  v.append(off);
  const wrap = el("div", { class: "stack", style: "margin-top:12px" });
  for (const ch of SYL.chapters) {
    const list = Q.filter(x => x.ch === ch.ch);
    const d = el("details", { class: "chapter", open: openChapters.has(ch.ch) });
    d.addEventListener("toggle", () => { d.open ? openChapters.add(ch.ch) : openChapters.delete(ch.ch); });
    d.append(el("summary", {}, el("h3", { text: ch.ch + ". " + ch.title }), el("span", { class: "eyebrow", text: ch.minutes + " min · " + mastery(list) + " %" })));
    const body = el("div", { class: "chapbody" });
    for (const s of ch.sections) {
      body.append(el("div", { class: "row spread" }, el("h3", { text: s.sec + " " + s.title }), ext(SYLLABUS_URL, "pág. " + s.page)));
      for (const lo of s.los) {
        const qlist = Q.filter(x => x.sec === lo.lo);
        const node = el("article", { class: "lo", id: "lo-" + lo.lo },
          el("div", { class: "row" }, el("span", { class: "badge" + (lo.k === 3 ? " k3" : ""), text: "FL-" + lo.lo + " · K" + lo.k }), el("strong", { text: lo.title })),
          el("p", { class: "note", text: "LO: " + lo.stmt + " · Syllabus v4.0.1, pág. " + LO_PAGE(lo.lo) }),
          el("p", { text: lo.sum }),
          el("div", { class: "terms" }, lo.terms.map(t => el("a", { href: GLOSSARY_URL(t), target: "_blank", rel: "noopener", title: "Abrir en el glosario oficial" }, t))));
        if (lo.example) node.append(el("div", { class: "example" }, el("strong", { text: lo.example.title }), el("p", { text: lo.example.problem }), el("ol", {}, lo.example.steps.map(s2 => el("li", { text: s2 })))));
        node.append(el("div", { class: "row" },
          el("button", { class: "btn small primary", type: "button", onclick: () => startPractice(qlist, "Practicando FL-" + lo.lo + " " + lo.title) }, "Practicar (" + qlist.length + ")"),
          el("span", { class: "note", text: "Dominio " + mastery(qlist) + " %" })));
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
function viewCards(v) {
  if (!cardState) cardState = { order: shuffle(CARDS.map((_, i) => i)).sort((a, b) => ((P.cards[a] || {}).box || 0) - ((P.cards[b] || {}).box || 0)), i: 0, flip: false };
  const idx = cardState.order[cardState.i % cardState.order.length], [term, def] = CARDS[idx];
  const known = Object.values(P.cards).filter(c => c.box >= 2).length;
  v.append(el("div", { class: "row spread" }, el("h2", { text: "Glosario" }), el("span", { class: "muted mono", text: known + "/" + CARDS.length + " dominados" })));
  v.append(el("button", { class: "flash", type: "button", style: "margin-top:12px", "aria-label": "Girar tarjeta", onclick: () => { cardState.flip = !cardState.flip; render(); } },
    el("span", { class: "eyebrow", text: cardState.flip ? "Definición (resumen propio)" : "Término · toca para girar" }),
    cardState.flip ? el("span", { class: "def", text: def }) : el("span", { class: "term", text: term })));
  const mark = ok => { const c = Object.assign({ box: 0 }, P.cards[idx]); c.box = ok ? Math.min(c.box + 1, 4) : 0; c.last = Date.now(); P.cards[idx] = c; save(); cardState.i++; cardState.flip = false; render(); };
  v.append(el("div", { class: "row spread", style: "margin-top:12px" },
    el("div", { class: "row" }, el("button", { class: "btn", type: "button", onclick: () => mark(false) }, "Repasar otra vez"), el("button", { class: "btn primary", type: "button", onclick: () => mark(true) }, "Me lo sé")),
    ext(GLOSSARY_URL(term.split(" / ")[0]), "Definición oficial ↗")));
}

// ---------------- progress & backup ----------------
let resetArmed = false;
function viewProgress(v) {
  v.append(el("h2", { text: "Progreso" }));
  const t = el("table", {}, el("thead", {}, el("tr", {}, el("th", { text: "Capítulo" }), el("th", { class: "num", text: "Vistas" }), el("th", { class: "num", text: "Acierto" }), el("th", { class: "num", text: "Dominio" }))));
  const tb = el("tbody");
  for (const ch of [1, 2, 3, 4, 5, 6]) {
    const list = Q.filter(x => x.ch === ch), seen = list.filter(x => P.q[x.id]).length;
    const c = list.reduce((s, x) => s + qs(x.id).c, 0), w = list.reduce((s, x) => s + qs(x.id).w, 0);
    tb.append(el("tr", {}, el("td", { text: ch + ". " + CHAPTER_NAMES[ch] }), el("td", { class: "num", text: seen + "/" + list.length }), el("td", { class: "num", text: c + w ? Math.round(100 * c / (c + w)) + " %" : "—" }), el("td", { class: "num", text: mastery(list) + " %" })));
  }
  for (const k of [1, 2, 3]) {
    const list = Q.filter(x => x.k === k);
    tb.append(el("tr", {}, el("td", { text: "Todas las K" + k }), el("td", { class: "num", text: list.filter(x => P.q[x.id]).length + "/" + list.length }), el("td", { class: "num", text: "" }), el("td", { class: "num", text: mastery(list) + " %" })));
  }
  t.append(tb); v.append(el("div", { class: "tablebox", style: "margin-top:10px" }, t));
  v.append(el("p", { class: "note", style: "margin-top:8px", text: "Dominio: una pregunta cuenta como dominada cuando la aciertas tres veces seguidas; si la fallas, vuelve a cero." }));
  if (P.exams.length) v.append(examHistory());

  // backup
  const ta = el("textarea", { id: "syncCode", "aria-label": "Código de progreso", placeholder: "Aquí aparecerá tu código, o pega aquí el código del otro dispositivo." });
  const file = el("input", { type: "file", id: "importFile", accept: ".json,application/json", hidden: true });
  file.addEventListener("change", async () => {
    const f = file.files[0]; if (!f) return;
    try { P = merge(P, JSON.parse(await f.text())); save(); toast("Copia importada y fusionada."); render(); }
    catch (e) { toast("No se pudo leer el fichero: " + e.message); }
  });
  const panel = el("section", { class: "panel", style: "margin-top:20px" },
    el("h3", { text: "Copia de seguridad y sincronización" }),
    el("p", { class: "note", text: "Tu progreso solo vive en este navegador. Para pasarlo al móvil (o al revés): «Copiar progreso» aquí, y «Pegar y fusionar» en el otro dispositivo. Al fusionar se conserva, para cada pregunta, la respuesta más reciente, y se juntan los simulacros de los dos." }),
    ta,
    el("div", { class: "row" },
      el("button", { class: "btn primary", type: "button", onclick: async () => {
        const code = await encodeProgress(); ta.value = code;
        try { await navigator.clipboard.writeText(code); toast("Código copiado al portapapeles."); }
        catch { ta.focus(); ta.select(); toast("Selecciona el texto y cópialo a mano."); }
      } }, "Copiar progreso"),
      el("button", { class: "btn", type: "button", onclick: async () => {
        if (!ta.value.trim()) { toast("Pega primero el código del otro dispositivo en el cuadro."); return; }
        try { P = merge(P, await decodeProgress(ta.value)); save(); ta.value = ""; toast("Progreso fusionado."); render(); }
        catch (e) { toast(e.message || "Código no válido."); }
      } }, "Pegar y fusionar")),
    el("div", { class: "row" },
      el("button", { class: "btn", type: "button", onclick: () => {
        const blob = new Blob([JSON.stringify(P, null, 1)], { type: "application/json" });
        const a = el("a", { href: URL.createObjectURL(blob), download: "ctfl-progreso-" + new Date().toISOString().slice(0, 10) + ".json" });
        document.body.append(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(a.href), 2000);
      } }, "Descargar copia (.json)"),
      el("button", { class: "btn", type: "button", onclick: () => file.click() }, "Importar copia (.json)"), file),
    el("div", { class: "row", style: "margin-top:6px" },
      el("button", { class: "btn small danger", type: "button", onclick: () => { if (resetArmed) { P = blank(); save(); resetArmed = false; toast("Progreso borrado."); render(); } else { resetArmed = true; render(); } } }, resetArmed ? "Pulsa otra vez para borrar todo el progreso" : "Borrar progreso")));
  v.append(panel);
}

// ---------------- boot ----------------
document.querySelectorAll("nav.tabs button").forEach(b => b.addEventListener("click", () => { resetArmed = false; go(b.dataset.view); }));
window.addEventListener("hashchange", () => { const h = location.hash.slice(1); if (VIEWS.includes(h) && h !== current) go(h); });
function onlineChip() { $("#offlineChip").hidden = navigator.onLine; }
window.addEventListener("online", onlineChip); window.addEventListener("offline", onlineChip);

(async function boot() {
  load(); onlineChip();
  try { await loadData(); }
  catch (e) { $("#view").replaceChildren(el("p", { class: "empty", text: "No se pudo cargar el banco de preguntas. Comprueba la conexión la primera vez que abras la app; después funciona sin conexión." })); return; }
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
        if (nw.state === "installed" && navigator.serviceWorker.controller) toast("Hay una versión nueva del banco.", { label: "Actualizar", fn: () => nw.postMessage("skipWaiting") });
      });
    });
  }).catch(() => {});
  let reloaded = false;
  navigator.serviceWorker.addEventListener("controllerchange", () => { if (!reloaded) { reloaded = true; location.reload(); } });
}

/* Service worker: precaches the app and the question bank (cache-first), so the app works offline.
   Bump VERSION whenever any file changes; the page then offers "Actualizar". */
const VERSION = "ctfl-study-v1.3.0";
const FONT_CACHE = "ctfl-study-fonts";
const ASSETS = [
  "./", "index.html", "styles.css", "app.js", "manifest.webmanifest",
  "icons/icon-192.png", "icons/icon-512.png", "icons/icon-maskable-512.png", "icons/apple-touch-icon.png",
  "data/bank-ch1.json", "data/bank-ch2.json", "data/bank-ch3.json", "data/bank-ch4.json",
  "data/bank-ch5.json", "data/bank-ch6.json", "data/exam.json", "data/syllabus.json", "data/i18n.json",
];

self.addEventListener("install", event => {
  event.waitUntil(caches.open(VERSION).then(cache => cache.addAll(ASSETS)));
});

self.addEventListener("activate", event => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(k => k !== VERSION && k !== FONT_CACHE).map(k => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener("message", event => {
  if (event.data === "skipWaiting") self.skipWaiting();
});

self.addEventListener("fetch", event => {
  const req = event.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);

  // Google Fonts: stale-while-revalidate in their own cache (the app falls back to system fonts)
  if (url.hostname === "fonts.googleapis.com" || url.hostname === "fonts.gstatic.com") {
    event.respondWith((async () => {
      const cache = await caches.open(FONT_CACHE);
      const hit = await cache.match(req);
      const net = fetch(req).then(res => { if (res.ok || res.type === "opaque") cache.put(req, res.clone()); return res; }).catch(() => hit);
      return hit || net;
    })());
    return;
  }
  if (url.origin !== self.location.origin) return;

  // Same origin: cache-first; navigations fall back to the cached app shell
  event.respondWith((async () => {
    const cache = await caches.open(VERSION);
    const hit = await cache.match(req, { ignoreSearch: true });
    if (hit) return hit;
    try {
      const res = await fetch(req);
      if (res.ok && url.pathname.startsWith(self.registration.scope.replace(self.location.origin, ""))) cache.put(req, res.clone());
      return res;
    } catch (e) {
      if (req.mode === "navigate") return (await cache.match("index.html")) || Response.error();
      return Response.error();
    }
  })());
});

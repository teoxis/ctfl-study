#!/usr/bin/env python3
"""Generates the app icons (PNG) with no dependencies: a white answer-sheet with a tick on deep green."""
import math
import struct
import zlib
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "icons"
GREEN = (31, 107, 79)
WHITE = (255, 255, 255)
INK = (23, 32, 28)


def png(path, w, h, px):
    raw = b"".join(b"\x00" + bytes(px[y * w * 3:(y + 1) * w * 3]) for y in range(h))
    def chunk(t, d):
        return struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
    data = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)) + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b"")
    path.write_bytes(data)


def seg_dist(px, py, ax, ay, bx, by):
    dx, dy = bx - ax, by - ay
    t = max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
    return math.hypot(px - (ax + t * dx), py - (ay + t * dy))


def rounded_rect_inside(x, y, x0, y0, x1, y1, r):
    cx = min(max(x, x0 + r), x1 - r)
    cy = min(max(y, y0 + r), y1 - r)
    return math.hypot(x - cx, y - cy) <= r


def draw(size, sheet_scale):
    s = size
    px = bytearray(s * s * 3)
    m = (1 - sheet_scale) / 2
    sx0, sy0, sx1, sy1 = s * m, s * m, s * (1 - m), s * (1 - m)
    sw = sx1 - sx0
    r = sw * 0.10
    # tick geometry relative to the sheet
    a = (sx0 + sw * 0.24, sy0 + sw * 0.52)
    b = (sx0 + sw * 0.43, sy0 + sw * 0.70)
    c = (sx0 + sw * 0.78, sy0 + sw * 0.32)
    thick = sw * 0.075
    lines_y = [sy0 + sw * f for f in (0.20,)]
    SS = 3
    for y in range(s):
        for x in range(s):
            acc = [0, 0, 0]
            for oy in range(SS):
                for ox in range(SS):
                    fx, fy = x + (ox + .5) / SS, y + (oy + .5) / SS
                    col = GREEN
                    if rounded_rect_inside(fx, fy, sx0, sy0, sx1, sy1, r):
                        col = WHITE
                        if any(abs(fy - ly) < sw * 0.025 and sx0 + sw * 0.18 < fx < sx1 - sw * 0.18 for ly in lines_y):
                            col = (200, 214, 206)
                        d = min(seg_dist(fx, fy, *a, *b), seg_dist(fx, fy, *b, *c))
                        if d < thick:
                            col = GREEN
                    for i in range(3):
                        acc[i] += col[i]
            o = (y * s + x) * 3
            px[o:o + 3] = bytes(v // (SS * SS) for v in acc)
    return px


OUT.mkdir(exist_ok=True)
png(OUT / "icon-192.png", 192, 192, draw(192, 0.78))
png(OUT / "icon-512.png", 512, 512, draw(512, 0.78))
png(OUT / "icon-maskable-512.png", 512, 512, draw(512, 0.58))
png(OUT / "apple-touch-icon.png", 180, 180, draw(180, 0.72))
print("icons written")

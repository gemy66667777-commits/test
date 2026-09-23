# -*- coding: utf-8 -*-
"""Original figures for Lesson 2-9 : refraction and total internal reflection."""
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV
from figs_lesson import INK, MUT

DENSE = '#bae6fd'
LIGHT = '#F1F5F9'
GLASS = '#a5b4fc'


def _ray(f, x1, y1, x2, y2, c=AR, w=3):
    f.arrow(x1, y1, x2, y2, c, w)


# --------------------------------------------------------------------------- 1
def two_media(cap, top='medium (1)', bot='medium (2)', i=40.0, r=33.0,
              maxw=450, w=520, h=300):
    """a ray crossing a boundary, with the normal and the two angles."""
    f = Fig(w, h, cap, maxw)
    x0, y0, W, H = 44.0, 34.0, 432.0, 224.0
    by = y0 + H / 2.0
    f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" rx="6"/>'
          % (x0, y0, W, H / 2.0, LIGHT))
    f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" rx="6"/>'
          % (x0, by, W, H / 2.0, DENSE))
    f.line(x0, by, x0 + W, by, DK, 2.4)
    f.tbg(x0 + 18, y0 + 26, top, INK, 11.5, 'start')
    f.tbg(x0 + 18, y0 + H - 16, bot, INK, 11.5, 'start')
    px, py = x0 + W * 0.50, by
    f.line(px, y0 + 6, px, y0 + H - 6, GY, 1.6, '6 5')
    f.txt(px + 10, y0 + 20, 'normal', MUT, 10, 'start')
    ai, ar = math.radians(i), math.radians(r)
    _ray(f, px - 108 * math.sin(ai), py - 108 * math.cos(ai), px, py)
    _ray(f, px, py, px + 112 * math.sin(ar), py + 112 * math.cos(ar))
    f.circle(px, py, 5, DK, DK, 1)
    f.raw('<path d="M%.1f,%.1f A32,32 0 0 1 %.1f,%.1f" fill="none" stroke="%s" stroke-width="2"/>'
          % (px - 32 * math.sin(ai), py - 32 * math.cos(ai), px, py - 32, OR))
    f.tbg(px - 40, py - 46, 'θ₁', OR, 12, 'end')
    f.raw('<path d="M%.1f,%.1f A36,36 0 0 1 %.1f,%.1f" fill="none" stroke="%s" stroke-width="2"/>'
          % (px, py + 36, px + 36 * math.sin(ar), py + 36 * math.cos(ar), OR))
    f.tbg(px + 44, py + 44, 'θ₂', OR, 12, 'start')
    f.txt(w / 2, h - 10, 'n₁ sin θ₁ = n₂ sin θ₂   —   the frequency '
                         'never changes', PU, 11)
    return f.render()


# --------------------------------------------------------------------------- 2
def critical_angle(cap, maxw=500, w=580, h=352):
    """three rays leaving a dense medium : refracted, grazing, totally reflected."""
    f = Fig(w, h, cap, maxw)
    x0, y0, W, H = 44.0, 34.0, 492.0, 232.0
    by = y0 + H * 0.62
    f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" rx="6"/>'
          % (x0, y0, W, by - y0, LIGHT))
    f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" rx="6"/>'
          % (x0, by, W, y0 + H - by, DENSE))
    f.line(x0, by, x0 + W, by, DK, 2.4)
    f.tbg(x0 + 16, y0 + 22, 'less dense   ( n₂ )', INK, 11, 'start')
    f.tbg(x0 + W - 16, y0 + H - 12, 'denser   ( n₁ )', INK, 11, 'end')
    L = 74.0
    cases = ((150.0, 22.0, 34.0, 'below θc', GR, 'refracts out'),
             (300.0, 42.0, 90.0, 'θ = θc', OR, 'grazes the surface'),
             (452.0, 58.0, None, 'above θc', AR, 'total internal reflection'))
    for px, ii, rr, lab, col, note in cases:
        ai = math.radians(ii)
        f.line(px, by - 46, px, by + 62, GY, 1.4, '5 4')
        _ray(f, px - L * math.sin(ai), by + L * math.cos(ai), px, by, col, 2.6)
        if rr is None:
            _ray(f, px, by, px + L * math.sin(ai), by + L * math.cos(ai), col, 2.6)
        else:
            arr = math.radians(rr)
            _ray(f, px, by, px + 92 * math.sin(arr), by - 92 * math.cos(arr), col, 2.6)
        f.circle(px, by, 4.4, DK, DK, 1)
        f.tbg(px, y0 + H + 26, lab, col, 11)
        f.tbg(px, y0 + H + 48, note, col, 10)
    f.txt(w / 2, h - 10, 'sin θc = n₂ / n₁   ( and = 1 / n when the outside is air )',
          PU, 11.5)
    return f.render()


# --------------------------------------------------------------------------- 3
def optical_fibre(cap, maxw=500, w=580, h=286):
    """light trapped inside the core of an optical fibre."""
    f = Fig(w, h, cap, maxw)
    x0, cy, W = 60.0, 116.0, 470.0
    ch, cl = 34.0, 16.0
    f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#c7d2fe" rx="6"/>'
          % (x0, cy - ch - cl, W, 2 * (ch + cl)))
    f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#fef3c7" rx="4"/>'
          % (x0, cy - ch, W, 2 * ch))
    f.line(x0, cy - ch, x0 + W, cy - ch, '#4338ca', 2)
    f.line(x0, cy + ch, x0 + W, cy + ch, '#4338ca', 2)
    f.txt(x0 + W, cy - ch - cl - 14, 'cladding   n₂  ( smaller )', '#3730a3', 10.5, 'end')
    f.txt(x0, cy + ch + cl + 22, 'core   n₁  ( larger )', '#92400e', 10.5, 'start')
    # the zig-zag ray
    step = 78.0
    px, py, up = x0 + 6, cy + ch - 2, True
    pts = [(px, py)]
    while px < x0 + W - 10:
        px += step
        py = cy - ch + 2 if up else cy + ch - 2
        up = not up
        pts.append((min(px, x0 + W - 6), py))
    for k in range(len(pts) - 1):
        f.arrow(pts[k][0], pts[k][1], pts[k + 1][0], pts[k + 1][1], AR, 2.6)
    for k in range(1, len(pts) - 1):
        f.circle(pts[k][0], pts[k][1], 4, AR, AR, 1)
    f.txt(w / 2, h - 26, 'the ray always strikes the wall at an angle larger than θc ,', MUT, 10.5)
    f.txt(w / 2, h - 10, 'so it is reflected totally every time and no light leaks out', MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 4
def four_paths(cap, maxw=520, w=600, h=372):
    """the four possible paths for a ray meeting the glass-air boundary at 50 degrees."""
    f = Fig(w, h, cap, maxw)
    bw, bh = 250.0, 122.0
    opts = (('A', 60.0, 34.0, 'out, away from the normal'),
            ('B', 320.0, 34.0, 'straight on, no bending'),
            ('C', 60.0, 182.0, 'reflected back into the glass'),
            ('D', 320.0, 182.0, 'out, towards the normal'))
    ai = math.radians(50.0)
    for lab, bx, byy, note in opts:
        ty = byy + bh * 0.46
        f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" rx="5"/>'
              % (bx, byy, bw, ty - byy, LIGHT))
        f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" rx="5"/>'
              % (bx, ty, bw, byy + bh - ty, GLASS))
        f.line(bx, ty, bx + bw, ty, DK, 2)
        f.txt(bx + 8, byy + 16, 'air', INK, 10, 'start')
        f.txt(bx + 8, byy + bh - 8, 'glass', INK, 10, 'start')
        px = bx + bw * 0.46
        f.line(px, byy + 4, px, byy + bh - 4, GY, 1.2, '4 4')
        L = 62.0
        _ray(f, px - L * math.sin(ai), ty + L * math.cos(ai), px, ty, AR, 2.4)
        if lab == 'A':
            ar = math.radians(72.0)
            _ray(f, px, ty, px + 58 * math.sin(ar), ty - 58 * math.cos(ar), BL, 2.4)
        elif lab == 'B':
            _ray(f, px, ty, px + L * math.sin(ai), ty - L * math.cos(ai), BL, 2.4)
        elif lab == 'C':
            _ray(f, px, ty, px + L * math.sin(ai), ty + L * math.cos(ai), BL, 2.4)
        else:
            ar = math.radians(28.0)
            _ray(f, px, ty, px + 58 * math.sin(ar), ty - 58 * math.cos(ar), BL, 2.4)
        f.circle(px, ty, 3.6, DK, DK, 1)
        f.tbg(bx + bw - 14, byy + 20, lab, PU, 13, 'end')
        f.tbg(bx + bw - 6, byy + bh + 16, note, MUT, 10, 'end')
    f.txt(w / 2, h - 10, 'n(glass) = 1.5   →   θc = 41.8° , and the ray arrives at '
                         '50°', PU, 11)
    return f.render()


# --------------------------------------------------------------------------- 5
def disc_block(cap, maxw=470, w=540, h=300):
    """a point source under a liquid and the disc that just blocks its light."""
    f = Fig(w, h, cap, maxw)
    x0, y0, W, H = 46.0, 58.0, 448.0, 196.0
    n = 1.33
    hh = 128.0
    sy = y0 + hh
    f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" rx="6"/>'
          % (x0, y0, W, H, DENSE))
    f.line(x0, y0, x0 + W, y0, DK, 2.4)
    f.txt(x0 + 12, y0 - 16, 'air', INK, 11, 'start')
    f.txt(x0 + 12, y0 + H - 12, 'liquid   n', INK, 11, 'start')
    cx = x0 + W * 0.5
    tc = math.asin(1.0 / n)
    R = hh * math.tan(tc)
    f.circle(cx, sy, 6, AR, AR, 1)
    f.txt(cx, sy + 24, 'point source', AR, 10.5)
    for deg, col in ((18.0, GR), (34.0, GR), (math.degrees(tc), OR)):
        a = math.radians(deg)
        sr = min(n * math.sin(a), 1.0)
        rr = math.asin(sr)
        for sgn in (-1, 1):
            hx = cx + sgn * hh * math.tan(a)
            f.line(cx, sy, hx, y0, col, 2)
            f.parrow(hx, y0, 90 - sgn * math.degrees(rr), 38, col, 2)
    f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="8" fill="#334155" rx="3"/>'
          % (cx - R, y0 - 9, 2 * R))
    f.dim(cx, y0 - 34, cx + R, y0 - 34, 'r = h tan θc', PU, 0, 11, -8)
    f.guide(cx, y0 - 38, cx, sy)
    f.dim(x0 + 22, y0, x0 + 22, sy, '', PU, 0, 11)
    f.tbg(x0 + 34, (y0 + sy) / 2 + 4, 'h', PU, 11.5, 'start')
    f.txt(w / 2, h - 10, 'a larger n gives a smaller θc , so a smaller disc is enough', PU, 11)
    return f.render()

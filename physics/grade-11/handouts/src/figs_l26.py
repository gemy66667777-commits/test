# -*- coding: utf-8 -*-
"""Original figures for Lesson 2-6 : refraction of waves."""
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV
from figs_lesson import INK, MUT

DEEP = '#1e40af'
SHAL = '#7dd3fc'
SAND = '#fde68a'
LAND = '#86efac'


# --------------------------------------------------------------------------- 1
def shore_refraction(cap, maxw=500, w=580, h=330):
    """sea waves swinging round and closing up as they run into shallow water."""
    f = Fig(w, h, cap, maxw)
    x0, y0, W, H = 40.0, 40.0, 500.0, 234.0
    cid = 'sea%d' % (id(f) % 100000)
    f.raw('<defs><linearGradient id="g%s" x1="0" y1="0" x2="0" y2="1">'
          '<stop offset="0%%" stop-color="#1d4ed8"/><stop offset="55%%" stop-color="#38bdf8"/>'
          '<stop offset="100%%" stop-color="#a5f3fc"/></linearGradient>'
          '<clipPath id="%s"><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="6"/></clipPath>'
          '</defs>' % (cid, cid, x0, y0, W, H))
    f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#g%s)" rx="6"/>'
          % (x0, y0, W, H, cid))
    f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="28" fill="%s" rx="4"/>'
          % (x0, y0 + H, W, SAND))
    f.txt(x0 + W - 12, y0 + H + 20, 'the shore line', '#92400e', 10.5, 'end')
    f.raw('<g clip-path="url(#%s)">' % cid)
    yy = y0 - 40.0
    while yy < y0 + H - 6:
        t = max(0.0, min(1.0, (yy - y0) / H))
        ang = 26.0 * (1.0 - t) ** 1.6
        sp = 42.0 - 26.0 * t
        dy = (W / 2.0) * math.tan(math.radians(ang))
        f.raw('<path d="M%.1f,%.1f L%.1f,%.1f" stroke="#f8fafc" stroke-width="%.1f" '
              'stroke-linecap="round" opacity="0.95"/>'
              % (x0, yy + dy, x0 + W, yy - dy, 3.4 - 1.1 * t))
        yy += sp
    f.raw('</g>')
    f.parrow(x0 + W - 116, y0 + 34, -64, 60, AR, 3)
    f.tbg(x0 + W - 98, y0 + 26, 'deep : fast, long λ', DK, 10.5, 'start')
    f.parrow(x0 + 86, y0 + H - 64, -90, 46, AR, 3)
    f.tbg(x0 + 98, y0 + H - 52, 'shallow : slow, short λ', DK, 10.5, 'start')
    f.txt(w / 2, h - 10, 'the crests swing round until they are almost parallel to the shore',
          MUT, 10.5)
    return f.render()


def _coast(u, base):
    """the height of the coastline : a headland at u=0.18 and a bay at u=0.60."""
    return (base
            - 84.0 * math.exp(-((u - 0.18) / 0.16) ** 2)
            + 30.0 * math.exp(-((u - 0.62) / 0.20) ** 2))


# --------------------------------------------------------------------------- 2
def headland_bay(cap, maxw=500, w=580, h=320):
    """wave energy concentrated on a headland and spread out in a bay."""
    f = Fig(w, h, cap, maxw)
    x0, y0, W, H = 40.0, 34.0, 500.0, 236.0
    base = y0 + H - 58.0
    cid = 'sea%d' % (id(f) % 100000)
    f.raw('<defs><clipPath id="%s"><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="6"/>'
          '</clipPath></defs>' % (cid, x0, y0, W, H))
    f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#38bdf8" rx="6"/>'
          % (x0, y0, W, H))
    n = 160
    cs = [(x0 + W * i / float(n), _coast(i / float(n), base)) for i in range(n + 1)]
    ymean = sum(p[1] for p in cs) / len(cs)
    # the wavefronts : flat far out, copying the coast close in
    f.raw('<g clip-path="url(#%s)">' % cid)
    for k in range(9):
        dk = 16.0 + k * 25.0
        damp = math.exp(-dk / 96.0)
        pts = [(px, (ymean - dk) + (py - ymean) * damp) for px, py in cs]
        f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % q for q in pts) +
              '" fill="none" stroke="#f8fafc" stroke-width="2.6" opacity="0.95"/>')
    f.raw('</g>')
    # the land
    f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % q for q in cs) +
          ' L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="#15803d" stroke-width="2.2"/>'
          % (x0 + W, y0 + H + 26, x0, y0 + H + 26, LAND))
    f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="12" fill="%s"/>'
          % (x0, y0 + H + 14, W, SAND))
    hx = x0 + W * 0.18
    bx = x0 + W * 0.62
    f.tbg(hx, _coast(0.18, base) + 52, 'headland', '#14532d', 11)
    f.tbg(bx, _coast(0.62, base) - 18, 'bay', '#14532d', 11)
    f.parrow(hx - 46, y0 + 40, -52, 54, AR, 2.8)
    f.parrow(hx + 46, y0 + 40, -128, 54, AR, 2.8)
    f.tbg(hx, y0 + 26, 'energy concentrated', AR, 10.5)
    f.parrow(bx - 40, y0 + 52, -118, 46, GR, 2.6)
    f.parrow(bx + 40, y0 + 52, -62, 46, GR, 2.6)
    f.tbg(bx, y0 + 38, 'energy spread out', GR, 10.5)
    f.txt(w / 2, h - 10, 'shallower water at the headland → slower waves, shorter λ, '
                         'same f', MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 3
def v_lambda_graph(cap, maxw=440, w=500, h=300):
    """v against lambda for three sources : the slope is the frequency."""
    f = Fig(w, h, cap, maxw)
    x0, y0, L, Hh = 82.0, 238.0, 356.0, 184.0
    f.arrow(x0 - 12, y0, x0 + L + 30, y0, DK, 2.2)
    f.arrow(x0, y0 + 12, x0, y0 - Hh - 34, DK, 2.2)
    f.txt(x0 + L / 2, y0 + 32, 'wavelength  λ', INK, 11)
    f.txt(x0 - 6, y0 - Hh - 42, 'wave speed  v', INK, 11, 'start')
    for i in range(1, 6):
        gx = x0 + L * i / 6.0
        f.line(gx, y0 - 4, gx, y0 + 4, DK, 1.4)
        gy = y0 - Hh * i / 5.0
        f.line(x0 - 4, gy, x0 + 4, gy, DK, 1.4)
    for slope, col, lab in ((0.42, '#0ea5e9', 'f₁'), (0.68, '#ea580c', 'f₂'),
                            (0.94, '#2563eb', 'f₃')):
        ex = L * 0.94
        ey = Hh * slope * 0.94 / 0.94
        f.line(x0, y0, x0 + ex, y0 - Hh * slope, col, 2.8)
        for j in range(1, 7):
            px = x0 + ex * j / 6.0
            py = y0 - Hh * slope * j / 6.0
            f.circle(px, py, 3.4, col, col, 1)
        f.tbg(x0 + ex + 14, y0 - Hh * slope + 4, lab, col, 12, 'start')
    f.tbg(x0 + 24, y0 - Hh - 12, 'v = f λ   →   the slope is f', PU, 11.5, 'start')
    f.txt(w / 2, h - 10, 'the steeper the line, the larger the frequency', MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 4
def wavefront_def(cap, maxw=480, w=550, h=270):
    """a wavefront is the locus of points vibrating in the same phase."""
    f = Fig(w, h, cap, maxw)
    # circular wavefronts from a point source
    cx, cy = 140.0, 138.0
    f.circle(cx, cy, 6, AR, AR, 1)
    for k in range(1, 5):
        f.raw('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="#2563eb" '
              'stroke-width="2.4"/>' % (cx, cy, k * 21.0))
    f.parrow(cx, cy, 30, 104, GR, 2.4)
    f.txt(cx + 100, cy - 60, 'ray', GR, 11, 'start')
    f.txt(cx, 36, 'circular wavefronts', INK, 11)
    # plane wavefronts far away
    bx = 340.0
    for k in range(5):
        f.line(bx + k * 30.0, cy - 66, bx + k * 30.0, cy + 66, '#2563eb', 2.4)
    f.parrow(bx + 20, cy, 0, 112, GR, 2.4)
    f.txt(bx + 140, cy - 14, 'ray', GR, 11, 'start')
    f.txt(bx + 60, 36, 'plane wavefronts', INK, 11)
    f.txt(bx + 60, cy + 92, 'the ray is always ⊥ the wavefront', MUT, 10.5)
    f.txt(w / 2, h - 10, 'a wavefront joins all the points that vibrate in the same phase',
          MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 5
def wave_boundary(cap, i='45°', r='30°', maxw=460, w=530, h=330):
    """a wave crossing the boundary between two media, with the two angles."""
    f = Fig(w, h, cap, maxw)
    x0, y0, W, H = 46.0, 34.0, 438.0, 252.0
    by = y0 + H / 2.0
    f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#F1F5F9" rx="6"/>'
          % (x0, y0, W, H / 2.0))
    f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#FDE68A" rx="6"/>'
          % (x0, by, W, H / 2.0))
    f.line(x0, by, x0 + W, by, DK, 2.4)
    f.tbg(x0 + 20, y0 + 28, 'medium 1', INK, 11.5, 'start')
    f.tbg(x0 + 20, y0 + H - 16, 'medium 2', INK, 11.5, 'start')
    px, py = x0 + W * 0.52, by
    f.line(px, y0 + 6, px, y0 + H - 6, GY, 1.6, '6 5')
    f.txt(px + 10, y0 + 18, 'normal', MUT, 10, 'start')
    ai = math.radians(45.0)
    ar = math.radians(30.0)
    sx, sy = px - 112 * math.sin(ai), py - 112 * math.cos(ai)
    f.arrow(sx, sy, px, py, AR, 3)
    ex, ey = px + 122 * math.sin(ar), py + 122 * math.cos(ar)
    f.arrow(px, py, ex, ey, AR, 3)
    f.circle(px, py, 5, DK, DK, 1)
    f.txt(px + 14, py + 18, 'P', INK, 12.5, 'start')
    f.raw('<path d="M%.1f,%.1f A34,34 0 0 1 %.1f,%.1f" fill="none" stroke="%s" stroke-width="2"/>'
          % (px - 34 * math.sin(ai), py - 34 * math.cos(ai), px, py - 34, OR))
    f.tbg(px - 44, py - 58, i, OR, 12, 'end')
    f.raw('<path d="M%.1f,%.1f A38,38 0 0 1 %.1f,%.1f" fill="none" stroke="%s" stroke-width="2"/>'
          % (px, py + 38, px + 38 * math.sin(ar), py + 38 * math.cos(ar), OR))
    f.tbg(px - 12, py + 60, r, OR, 12, 'end')
    # wavefronts, perpendicular to each ray
    for k in (1, 2, 3):
        dd = 34.0 * k
        mx, my = px - dd * math.sin(ai), py - dd * math.cos(ai)
        f.line(mx - 26 * math.cos(ai), my + 26 * math.sin(ai),
               mx + 26 * math.cos(ai), my - 26 * math.sin(ai), '#475569', 1.6, '5 4')
        dd2 = 30.0 * k
        nx, ny = px + dd2 * math.sin(ar), py + dd2 * math.cos(ar)
        f.line(nx - 24 * math.cos(ar), ny + 24 * math.sin(ar),
               nx + 24 * math.cos(ar), ny - 24 * math.sin(ar), '#475569', 1.6, '5 4')
    f.txt(w / 2, h - 10, 'the ray bends towards the normal → medium 2 is the slower one',
          MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 6
def speed_change(cap, maxw=490, w=560, h=250):
    """the same frequency, a different speed, so a different wavelength."""
    f = Fig(w, h, cap, maxw)
    x0, y0, W = 46.0, 118.0, 470.0
    mid = x0 + W * 0.45
    f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="118" fill="#DBEAFE" rx="6"/>'
          % (x0, y0 - 58, mid - x0))
    f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="118" fill="#FEF3C7" rx="6"/>'
          % (mid, y0 - 58, x0 + W - mid))
    f.line(mid, y0 - 58, mid, y0 + 60, DK, 2.4)
    f.tbg(x0 + 14, y0 - 40, 'medium 1 : v = 300 m/s', INK, 11, 'start')
    f.tbg(x0 + W - 14, y0 - 40, 'medium 2 : v = 600 m/s', INK, 11, 'end')
    n = 320
    pts = []
    for k in range(n + 1):
        t = k / float(n)
        x = x0 + W * t
        if x <= mid:
            u = (x - x0) / 34.0
        else:
            u = (mid - x0) / 34.0 + (x - mid) / 68.0
        pts.append((x, y0 - 24 * math.sin(2 * math.pi * u)))
    f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % p for p in pts) +
          '" fill="none" stroke="#2563eb" stroke-width="3"/>')
    f.dim(x0 + 8, y0 + 40, x0 + 8 + 34, y0 + 40, 'λ₁ = 6 m', PU, 0, 11, 16)
    f.dim(mid + 8, y0 + 40, mid + 8 + 68, y0 + 40, 'λ₂ = 12 m', PU, 0, 11, 16)
    f.tbg(w / 2, y0 - 76, 'the frequency stays 50 Hz on both sides', AR, 11)
    f.txt(w / 2, h - 10, 'v = f λ : f is fixed by the source, so a faster medium means a '
                         'longer λ', MUT, 10.5)
    return f.render()

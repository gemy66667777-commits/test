# -*- coding: utf-8 -*-
"""Original figures for Lesson 2-5 : interference of waves and standing waves."""
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV
from figs_lesson import INK, MUT
from figs_l24 import _sine

CREST = '#2563eb'
TROUGH = '#94a3b8'


def _rings(f, cx, cy, lam, n, x1, x2, y1, y2):
    """concentric wavefronts : solid = crest, dashed = trough."""
    for k in range(1, n + 1):
        r = k * lam / 2.0
        solid = (k % 2 == 1)
        f.raw('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" stroke-width="%s"%s '
              'clip-path="url(#clip%s)"/>'
              % (cx, cy, r, CREST if solid else TROUGH, 1.7 if solid else 1.3,
                 '' if solid else ' stroke-dasharray="4 4"', id(f)))


# --------------------------------------------------------------------------- 1
def two_sources(cap, maxw=470, w=540, h=350):
    """two coherent sources, their wavefronts, and the points P and Q."""
    f = Fig(w, h, cap, maxw)
    cid = 'c%s' % (id(f) % 100000)
    f.raw('<defs><clipPath id="%s"><rect x="24" y="24" width="%d" height="%d" rx="8"/></clipPath></defs>'
          % (cid, w - 48, h - 82))
    s1 = (206.0, 296.0)
    s2 = (334.0, 296.0)
    lam = 46.0
    f.raw('<g clip-path="url(#%s)">' % cid)
    for (cx, cy) in (s1, s2):
        for k in range(1, 13):
            r = k * lam / 2.0
            solid = (k % 2 == 1)
            f.raw('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" stroke-width="%s"%s/>'
                  % (cx, cy, r, CREST if solid else TROUGH, 1.8 if solid else 1.2,
                     '' if solid else ' stroke-dasharray="4 4"'))
    f.raw('</g>')
    for (cx, cy), lab in ((s1, 'S₁'), (s2, 'S₂')):
        f.circle(cx, cy, 6, AR, AR, 1)
        f.txt(cx, cy + 24, lab, AR, 13)
    # P : a crest ring of each source crosses here  (r = 7 lam/2 from both)
    #     equal distances  ->  path difference zero  ->  constructive
    rp = 7 * lam / 2.0
    dx = (s2[0] - s1[0]) / 2.0
    p = ((s1[0] + s2[0]) / 2.0, s1[1] - math.sqrt(rp * rp - dx * dx))
    f.circle(p[0], p[1], 6, '#047857', '#047857', 1)
    f.tbg(p[0], p[1] - 18, 'P  —  crest on crest', '#047857', 11)
    # Q : a trough of S1 (r = 4 lam/2) meets a crest of S2 (r = 7 lam/2)
    r1, r2 = 4 * lam / 2.0, 7 * lam / 2.0
    dd = s2[0] - s1[0]
    aa = (dd * dd + r1 * r1 - r2 * r2) / (2.0 * dd)
    hh = math.sqrt(max(r1 * r1 - aa * aa, 1.0))
    q = (s1[0] + aa, s1[1] - hh)
    f.circle(q[0], q[1], 6, '#b45309', '#b45309', 1)
    f.tbg(q[0] - 12, q[1] - 16, 'Q  —  crest on trough', '#b45309', 11, 'end')
    f.txt(w - 30, 36, 'solid = crest', CREST, 10.5, 'end')
    f.txt(w - 30, 52, 'dashed = trough', '#64748b', 10.5, 'end')
    f.txt(w / 2, h - 10, 'crest on crest → constructive  &middot;  crest on trough → destructive',
          MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 2
def path_difference(cap, d1='S₁P = 10.0 cm', d2='S₂P = 16.0 cm', maxw=450, w=520, h=270):
    """the two paths from the sources to a point P."""
    f = Fig(w, h, cap, maxw)
    s1 = (120.0, 200.0)
    s2 = (250.0, 200.0)
    p = (390.0, 66.0)
    f.circle(s1[0], s1[1], 7, AR, AR, 1)
    f.circle(s2[0], s2[1], 7, AR, AR, 1)
    f.txt(s1[0], s1[1] + 26, 'S₁', AR, 13)
    f.txt(s2[0], s2[1] + 26, 'S₂', AR, 13)
    f.circle(p[0], p[1], 7, '#047857', '#047857', 1)
    f.txt(p[0] + 16, p[1] + 4, 'P', '#047857', 13, 'start')
    f.line(s1[0], s1[1], p[0], p[1], BL, 2.4)
    f.line(s2[0], s2[1], p[0], p[1], GR, 2.4)
    f.tbg(212, 116, d1, BL, 11, 'end')
    f.tbg(330, 160, d2, GR, 11, 'start')
    f.line(s1[0], s1[1] + 14, s2[0], s2[1] + 14, GY, 1.4, '5 4')
    f.txt(w / 2, h - 28, 'path difference   Δ = S₂P − S₁P', PU, 12)
    f.txt(w / 2, h - 10, 'Δ = mλ → constructive   &middot;   '
                         'Δ = ( m + ½ ) λ → destructive', MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 3
def superposition(cap, maxw=500, w=580, h=330):
    """two equal waves added, in phase and in antiphase."""
    f = Fig(w, h, cap, maxw)
    L, A = 220.0, 26.0
    for col, x0, ttl, ph, resA in ((0, 56.0, 'in phase  →  constructive', 0.0, 2.0),
                                   (1, 330.0, 'in antiphase  →  destructive', math.pi, 0.0)):
        f.txt(x0 + L / 2, 34, ttl, INK, 11.5)
        for row, (c, phase) in enumerate(((CREST, 0.0), ('#0f766e', ph))):
            y = 76.0 + row * 62
            f.line(x0, y, x0 + L, y, GY, 1.2, '5 5')
            _sine(f, x0, y, L, A, cycles=1.5, c=c, w=2.4, phase=phase)
        y = 232.0
        f.line(x0, y, x0 + L, y, GY, 1.2, '5 5')
        if resA > 0:
            _sine(f, x0, y, L, A * resA, cycles=1.5, c='#7c3aed', w=3)
            f.tbg(x0 + L / 2, y + 64, 'amplitude 2A', PU, 11)
        else:
            f.line(x0, y, x0 + L, y, '#7c3aed', 3)
            f.tbg(x0 + L / 2, y + 64, 'amplitude 0', PU, 11)
        f.txt(x0 - 12, 168, '+', DK, 16, 'end')
        f.txt(x0 - 12, y + 4, '=', DK, 16, 'end')
    f.txt(w / 2, h - 10, 'the principle of superposition : add the two displacements, with their signs',
          MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 4
def nodal_lines(cap, nlab='8 destructive lines', maxw=470, w=540, h=430):
    """the nodal (destructive) lines between two in-phase sources."""
    f = Fig(w, h, cap, maxw)
    s1 = (196.0, 214.0)
    s2 = (344.0, 214.0)  # the axis sits mid-canvas
    mid = (s1[0] + s2[0]) / 2.0
    f.line(s1[0], s1[1], s2[0], s2[1], DK, 2, '6 5')
    f.circle(s1[0], s1[1], 7, AR, AR, 1)
    f.circle(s2[0], s2[1], 7, AR, AR, 1)
    f.tbg(s1[0] - 18, s1[1] + 5, 'S₁', AR, 13, 'end')
    f.tbg(s2[0] + 18, s2[1] + 5, 'S₂', AR, 13, 'start')
    # four nodal lines on each side, drawn as hyperbola-like arcs
    for k in (1, 2, 3, 4):
        for sgn in (-1, 1):
            x = mid + sgn * k * 17.0
            bend = 30.0 * k * sgn
            for up in (1, -1):
                ey = 214.0 - up * 150.0
                cy2 = 214.0 - up * 78.0
                f.raw('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="#7c3aed" '
                      'stroke-width="1.7" stroke-dasharray="6 4"/>'
                      % (x, 214.0, x + bend * 0.5, cy2, x + bend, ey))
    f.dim(s1[0], 258.0, s2[0], 258.0, 'd = 8.0 cm', PU, 0, 11.5, 18)
    f.tbg(w - 34, 34, nlab, '#7c3aed', 11.5, 'end')
    f.txt(w / 2, h - 10, 'a destructive line for every odd number of half-wavelengths', MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 5
def standing_wave(cap, maxw=490, w=560, h=292):
    """a standing wave on a stretched string : nodes, antinodes and lambda/2."""
    f = Fig(w, h, cap, maxw)
    x0, y0, L, A = 70.0, 132.0, 420.0, 54.0
    f.line(x0, y0, x0 + L, y0, GY, 1.4, '5 5')
    _sine(f, x0, y0, L, A, cycles=2.0, c=CREST, w=2.8)
    _sine(f, x0, y0, L, -A, cycles=2.0, c='#93c5fd', w=2.2)
    for k in range(5):
        xn = x0 + L * k / 4.0
        f.circle(xn, y0, 6, '#dc2626', '#dc2626', 1)
    for k in range(4):
        xa = x0 + L * (2 * k + 1) / 8.0
        f.circle(xa, y0, 5, '#047857', '#047857', 1)
    f.txt(x0, y0 + 26, 'N', AR, 12)
    f.txt(x0 + L / 8.0, y0 + 26, 'A', '#047857', 12)
    f.txt(x0 + L / 4.0, y0 + 26, 'N', AR, 12)
    f.txt(x0 + 3 * L / 8.0, y0 + 26, 'A', '#047857', 12)
    f.dim(x0, y0 + 84, x0 + L / 4.0, y0 + 84, 'λ / 2', PU, 0, 11.5, -8)
    f.txt(x0 + L - 10, 40, 'N = node   &middot;   A = antinode', MUT, 10.5, 'end')
    f.txt(w / 2, h - 10, 'two successive nodes ( or two successive antinodes ) are λ/2 apart',
          MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 6
def pipe_standing(cap, maxw=470, w=540, h=250):
    """a standing wave inside a pipe closed at one end and open at the other."""
    f = Fig(w, h, cap, maxw)
    x0, y0, L, A = 90.0, 118.0, 372.0, 46.0
    # the pipe
    f.line(x0 - 6, y0 - A - 16, x0 + L + 10, y0 - A - 16, DK, 4)
    f.line(x0 - 6, y0 + A + 16, x0 + L + 10, y0 + A + 16, DK, 4)
    f.line(x0 - 6, y0 - A - 16, x0 - 6, y0 + A + 16, DK, 4)
    f.txt(x0 - 16, y0 + 4, 'closed', MUT, 10.5, 'end')
    f.txt(x0 + L + 20, y0 + 4, 'open', MUT, 10.5, 'start')
    # third harmonic of a closed pipe : node at the closed end, antinode at the open end
    n = 240
    for sgn in (1, -1):
        pts = []
        for i in range(n + 1):
            t = i / float(n)
            pts.append((x0 + L * t, y0 - sgn * A * math.sin(1.5 * math.pi * t)))
        f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % p for p in pts) +
              '" fill="none" stroke="%s" stroke-width="%s"/>'
              % (CREST if sgn > 0 else '#93c5fd', 2.6 if sgn > 0 else 2.2))
    f.line(x0, y0, x0 + L, y0, GY, 1.3, '5 5')
    xn = x0 + L * (2.0 / 3.0)          # the interior node
    f.circle(xn, y0, 6, '#dc2626', '#dc2626', 1)
    f.txt(xn, y0 - 22, 'X', '#dc2626', 14, 'middle', it=True)
    f.circle(x0, y0, 6, '#dc2626', '#dc2626', 1)
    xa = x0 + L * (1.0 / 3.0)
    f.circle(xa, y0, 5, '#047857', '#047857', 1)
    f.circle(x0 + L, y0, 5, '#047857', '#047857', 1)
    f.txt(x0 + L * 0.34, y0 + A + 34, 'antinode', '#047857', 10.5)
    f.txt(xn, y0 + A + 34, 'node', AR, 10.5)
    f.txt(w / 2, h - 10, 'at a node the air particles hardly move along the tube', MUT, 10.5)
    return f.render()

# -*- coding: utf-8 -*-
"""Original figures for Lesson 1-12 : Kepler's laws and universal gravitation."""
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV
from figs_lesson import INK, MUT, SKY, VIO, RED, GRN, AMB, IND


def two_masses(cap, m1='60 kg', m2='60 kg', rlab='r = 3.0 m', maxw=440, w=500, h=220):
    f = Fig(w, h, cap, maxw)
    y = 108.0
    x1, x2 = 130.0, 370.0
    f.circle(x1, y, 34, '#93C5FD', '#1D4ED8', 2.6)
    f.circle(x2, y, 34, '#FCA5A5', '#991B1B', 2.6)
    f.txt(x1, y + 6, 'm₁', '#1E3A8A', 15)
    f.txt(x2, y + 6, 'm₂', '#7F1D1D', 15)
    f.txt(x1, y - 50, m1, INK, 12.5)
    f.txt(x2, y - 50, m2, INK, 12.5)
    f.parrow(x1 + 40, y, 0, 52, GRN, 2.8)
    f.parrow(x2 - 40, y, 180, 52, GRN, 2.8)
    f.txt(x1 + 66, y - 14, 'F', GRN, 13, 'middle', it=True)
    f.txt(x2 - 66, y - 14, 'F', GRN, 13, 'middle', it=True)
    f.guide(x1, y + 40, x1, y + 74); f.guide(x2, y + 40, x2, y + 74)
    f.dim(x1, y + 70, x2, y + 70, rlab, PU, 0, 12.5, -7)
    f.txt(w / 2, h - 12, 'the two forces are equal and opposite (Newton’s third law)', MUT, 10.5)
    return f.render()


def elliptical_orbit(cap, maxw=500, w=620, h=340):
    f = Fig(w, h, cap, maxw)
    cx, cy = 310.0, 170.0
    a, b = 200.0, 122.0
    c = math.sqrt(a * a - b * b)
    f.raw('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="none" stroke="#94A3B8" stroke-width="2.4" '
          'stroke-dasharray="7 6"/>' % (cx, cy, a, b))
    sx = cx - c
    f.circle(sx, cy, 22, '#FDE68A', '#D97706', 2.8)
    for k in range(12):
        p1 = P(sx, cy, 24, k * 30); p2 = P(sx, cy, 32, k * 30)
        f.line(p1[0], p1[1], p2[0], p2[1], '#D97706', 1.8)
    f.txt(sx, cy + 52, 'the Sun (a focus)', '#B45309', 11.5)
    f.circle(cx + c, cy, 4, MUT, MUT, 1)
    f.txt(cx + c - 10, cy - 34, 'the other focus', MUT, 10.5)
    pn = (cx - a, cy)
    pf = (cx + a, cy)
    f.circle(pn[0], pn[1], 11, '#3B82F6', '#1D4ED8', 2.4)
    f.circle(pf[0], pf[1], 11, '#3B82F6', '#1D4ED8', 2.4)
    f.parrow(pn[0], pn[1] - 14, 90, 58, RED, 2.8)
    f.txt(pn[0], pn[1] - 86, 'fastest here', RED, 11.5)
    f.parrow(pf[0], pf[1] + 14, -90, 32, RED, 2.6)
    f.txt(pf[0], pf[1] + 82, 'slowest here', RED, 11.5)
    f.txt(pn[0] - 18, pn[1] + 4, 'nearest point', PU, 11, 'end')
    f.txt(pf[0] + 18, pf[1] + 4, 'farthest point', PU, 11, 'start')
    return f.render()


def field_lines(cap, maxw=340, w=400, h=300):
    f = Fig(w, h, cap, maxw)
    cx, cy, R = 200.0, 150.0, 58.0
    f.circle(cx, cy, R, '#BFDBFE', '#1D4ED8', 2.6)
    f.raw('<path d="M%.1f,%.1f q 18,-14 34,-4 q 16,10 30,2" fill="none" stroke="#16A34A" stroke-width="3"/>'
          % (cx - 34, cy - 12))
    f.raw('<path d="M%.1f,%.1f q 14,12 30,6" fill="none" stroke="#16A34A" stroke-width="3"/>'
          % (cx - 20, cy + 20))
    for k in range(12):
        a = k * 30
        p1 = P(cx, cy, R + 74, a)
        p2 = P(cx, cy, R + 10, a)
        f.arrow(p1[0], p1[1], p2[0], p2[1], VIO, 2.2)
    f.txt(cx, cy + 6, 'Earth', '#1E3A8A', 12)
    f.txt(w / 2, h - 12, 'the field lines point towards the centre of the Earth', MUT, 10.5)
    return f.render()


def geostationary(cap, maxw=400, w=460, h=330):
    f = Fig(w, h, cap, maxw)
    cx, cy, R = 210.0, 168.0, 54.0
    f.circle(cx, cy, R, '#BFDBFE', '#1D4ED8', 2.6)
    f.line(cx - R, cy, cx + R, cy, '#1D4ED8', 1.8, '5 4')
    f.txt(cx - R - 10, cy + 4, 'equator', MUT, 10.5, 'end')
    f.raw('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="#94A3B8" stroke-width="2" '
          'stroke-dasharray="7 6"/>' % (cx, cy, R + 68))
    sp = P(cx, cy, R + 68, 26)
    f.rect(sp[0] - 14, sp[1] - 9, 28, 18, '#CBD5E1', '#475569', 2, 3)
    f.rect(sp[0] - 34, sp[1] - 6, 18, 12, '#1D4ED8', '#1E3A8A', 1.8, 2)
    f.rect(sp[0] + 16, sp[1] - 6, 18, 12, '#1D4ED8', '#1E3A8A', 1.8, 2)
    f.txt(sp[0] + 10, sp[1] - 24, 'satellite', INK, 11.5, 'start')
    f.guide(cx, cy, sp[0], sp[1])
    p = P(cx, cy, R, 26)
    f.circle(p[0], p[1], 5, RED, RED, 1)
    f.line(p[0], p[1], p[0] + 6, p[1] + 44, RED, 1.4, '4 3')
    f.tbg(p[0] + 8, p[1] + 52, 'always above the same point', RED, 10.5, 'start')
    f.arc(cx, cy, R + 92, 46, 104, MUT, 2, arrowhead=True)
    f.txt(w / 2, h - 12, 'T(satellite) = T(Earth) = 24 h', MUT, 11)
    f.arc(cx, cy, R - 16, 120, 180, '#1E3A8A', 2, arrowhead=True)
    return f.render()


def orbits_compare(cap, maxw=420, w=480, h=300):
    f = Fig(w, h, cap, maxw)
    cx, cy = 240.0, 150.0
    f.circle(cx, cy, 24, '#FDE68A', '#D97706', 2.8)
    for k in range(12):
        p1 = P(cx, cy, 26, k * 30); p2 = P(cx, cy, 34, k * 30)
        f.line(p1[0], p1[1], p2[0], p2[1], '#D97706', 1.8)
    for R, col, lab, ang in ((78.0, '#2563eb', 'planet 1', 40), (128.0, RED, 'planet 2', 200)):
        f.raw('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" stroke-width="2" '
              'stroke-dasharray="7 6"/>' % (cx, cy, R, col))
        p = P(cx, cy, R, ang)
        f.circle(p[0], p[1], 11, col, col, 1)
        f.txt(p[0] + (18 if ang < 90 else -18), p[1] - 22, lab, col, 11.5,
              'start' if ang < 90 else 'end')
        f.parrow(p[0], p[1], ang + 90, 40 if R < 100 else 30, col, 2.4)
    f.line(cx, cy, cx, cy - 78, PU, 1.8, '6 5')
    f.tbg(cx - 20, cy - 52, 'r₁', PU, 12)
    f.line(cx, cy, cx - 128, cy, PU, 1.8, '6 5')
    f.tbg(cx - 74, cy - 14, 'r₂', PU, 12)
    f.txt(w / 2, h - 12, 'the larger the orbit, the longer the periodic time', MUT, 10.5)
    return f.render()


def g_above_surface(cap, maxw=400, w=460, h=280):
    f = Fig(w, h, cap, maxw)
    cx, cy, R = 150.0, 150.0, 74.0
    f.circle(cx, cy, R, '#BFDBFE', '#1D4ED8', 2.6)
    f.txt(cx + 16, cy - 10, 'M', '#1E3A8A', 15, 'middle', it=True)
    f.dim(cx, cy, P(cx, cy, R, 210)[0], P(cx, cy, R, 210)[1], '', PU, 0, 12)
    f.tbg(cx - 46, cy + 42, 'R', PU, 12)
    px = cx + R + 120
    f.circle(px, cy, 12, '#FCD34D', '#B45309', 2.4)
    f.txt(px, cy - 28, 'a body of mass m', INK, 11.5)
    f.parrow(px - 14, cy, 180, 56, GRN, 2.8)
    f.txt(px - 46, cy + 26, 'F', GRN, 13, 'middle', it=True)
    f.guide(cx + R, cy, cx + R, cy + 62); f.guide(px, cy + 14, px, cy + 62)
    f.dim(cx + R, cy + 58, px, cy + 58, 'r', PU, 0, 12.5, -7)
    f.guide(cx, cy, cx, cy + 96)
    f.dim(cx, cy + 92, px, cy + 92, 'R + r', PU, 0, 12.5, -7)
    f.guide(px, cy + 66, px, cy + 96)
    return f.render()

# -*- coding: utf-8 -*-
"""Original figures for Lesson 1-10 : uniform circular motion and centripetal force."""
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV
from figs_lesson import INK, MUT, SKY, VIO, RED, GRN, AMB, IND


def circle_motion(cap, rlab='r', maxw=360, w=420, h=330):
    f = Fig(w, h, cap, maxw)
    cx, cy, R = 210.0, 168.0, 108.0
    f.raw('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="#94A3B8" stroke-width="2" '
          'stroke-dasharray="7 6"/>' % (cx, cy, R))
    f.circle(cx, cy, 5, INK, INK, 1)
    f.txt(cx - 14, cy + 6, 'O', INK, 13, 'end', it=True)
    ang = 52.0
    p = P(cx, cy, R, ang)
    f.circle(p[0], p[1], 13, '#3B82F6', '#1D4ED8', 2.4)
    f.parrow(p[0], p[1], ang + 90, 74, RED, 3.2)
    t = P(p[0], p[1], 86, ang + 90)
    f.txt(t[0] + 10, t[1] - 2, 'v', RED, 14, 'start', it=True)
    f.parrow(p[0], p[1], ang + 180, 62, GRN, 3)
    t2 = P(p[0], p[1], 40, ang + 180)
    f.txt(t2[0] + 26, t2[1] - 10, 'a(c)', GRN, 12.5, 'start')
    f.dim(cx, cy, p[0], p[1], '', PU, 0, 12)
    f.tbg((cx + p[0]) / 2 - 18, (cy + p[1]) / 2 + 20, rlab, PU, 12)
    f.arc(cx, cy, R + 24, 120, 176, MUT, 2, arrowhead=True)
    f.txt(24, 34, 'the sense of rotation', MUT, 10.5, 'start')
    f.txt(w / 2, h - 10, 'the speed is constant, the direction changes at every instant', MUT, 10.5)
    return f.render()


def ball_string(cap, llab='l = 2.0 m', wlab='ω = 3.0 rad/s', mlab='0.50 kg', maxw=360, w=420, h=300):
    f = Fig(w, h, cap, maxw)
    cx, cy, R = 200.0, 150.0, 116.0
    f.raw('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="36" fill="none" stroke="#94A3B8" stroke-width="2" '
          'stroke-dasharray="7 6"/>' % (cx, cy + 50, R))
    f.circle(cx, cy - 74, 6, DK, DK, 1)
    f.line(cx, cy - 74, cx + R, cy + 50, '#A16207', 2.6)
    f.circle(cx + R, cy + 50, 14, '#FCD34D', '#B45309', 2.4)
    f.txt(cx + R + 4, cy + 84, mlab, INK, 12)
    f.tbg(cx + 96, cy - 22, llab, PU, 12)
    f.parrow(cx + R, cy + 36, 90, 0.1, RED, 1)
    f.arc(cx, cy + 50, R + 22, 20, 90, MUT, 2, arrowhead=True)
    f.txt(24, 30, wlab, MUT, 12, 'start')
    f.parrow(cx + R - 4, cy + 50, 180, 62, GRN, 2.8)
    f.txt(cx + 44, cy + 44, 'a(c)', GRN, 12, 'end')
    return f.render()


def spring_circular(cap, maxw=380, w=440, h=280):
    f = Fig(w, h, cap, maxw)
    cx, cy = 160.0, 150.0
    f.raw('<ellipse cx="%.1f" cy="%.1f" rx="200" ry="52" fill="none" stroke="#94A3B8" stroke-width="2" '
          'stroke-dasharray="7 6"/>' % (220, cy))
    f.circle(cx, cy, 8, '#475569', DK, 2)
    f.txt(cx - 14, cy - 14, 'axis', MUT, 11, 'end')
    n = 10
    x1, x2 = cx + 8, cx + 172
    pts = []
    for i in range(n * 2 + 1):
        t = i / float(n * 2)
        px = x1 + (x2 - x1) * t
        py = cy + (0 if i in (0, n * 2) else (9 if i % 2 else -9))
        pts.append((px, py))
    f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % p for p in pts) +
          '" fill="none" stroke="#475569" stroke-width="2.2"/>')
    f.circle(x2 + 16, cy, 15, '#FCD34D', '#B45309', 2.4)
    f.txt(x2 + 16, cy + 40, '0.50 kg', INK, 12)
    f.tbg(cx + 90, cy - 30, 'k = 30 N/m', PU, 12)
    f.dim(cx + 8, cy + 66, x2 + 16, cy + 66, 'r = natural length + extension', PU, 0, 11.5, -6)
    f.guide(cx + 8, cy + 14, cx + 8, cy + 70); f.guide(x2 + 16, cy + 18, x2 + 16, cy + 70)
    f.txt(w - 24, 30, 'ω = 6.0 rad/s', MUT, 12, 'end')
    return f.render()


def rotating_disc(cap, rlab='0.30 m', wlab='ω = 4π rad/s', maxw=340, w=400, h=322):
    f = Fig(w, h, cap, maxw)
    cx, cy, R = 200.0, 150.0, 104.0
    f.circle(cx, cy, R, '#EEF2F7', '#64748B', 2.6)
    f.circle(cx, cy, 10, '#94A3B8', DK, 2.2)
    for a in range(0, 360, 45):
        p1 = P(cx, cy, 14, a); p2 = P(cx, cy, R - 4, a)
        f.line(p1[0], p1[1], p2[0], p2[1], '#CBD5E1', 1.6)
    p = P(cx, cy, R, 38)
    f.circle(p[0], p[1], 8, RED, '#991B1B', 2)
    f.txt(p[0] + 14, p[1] - 10, 'A', INK, 13, 'start', it=True)
    f.dim(cx, cy, p[0], p[1], '', PU, 0, 12)
    f.tbg((cx + p[0]) / 2 + 6, (cy + p[1]) / 2 + 18, rlab, PU, 12)
    f.parrow(p[0], p[1], 38 + 90, 58, IND, 2.8)
    t = P(p[0], p[1], 70, 128)
    f.txt(t[0] - 6, t[1] - 4, 'v', IND, 13, 'end', it=True)
    f.arc(cx, cy, R + 26, 200, 270, MUT, 2, arrowhead=True)
    f.txt(cx, cy + R + 52, wlab, MUT, 12)
    return f.render()


def washing_drum(cap, maxw=380, w=440, h=300):
    f = Fig(w, h, cap, maxw)
    cx, cy, R = 210.0, 148.0, 104.0
    f.circle(cx, cy, R + 16, '#E2E8F0', '#64748B', 2.6)
    f.circle(cx, cy, R, '#F8FAFC', '#94A3B8', 2.2)
    for a in range(0, 360, 24):
        p = P(cx, cy, R, a)
        f.circle(p[0], p[1], 3.4, '#fff', '#64748B', 1.4)
    for a in (28, 96, 168, 250, 312):
        p = P(cx, cy, R - 22, a)
        f.raw('<ellipse cx="%.1f" cy="%.1f" rx="16" ry="11" fill="#BFDBFE" stroke="#1D4ED8" '
              'stroke-width="1.8" transform="rotate(%.0f %.1f %.1f)"/>' % (p[0], p[1], -a, p[0], p[1]))
    for a in (60, 140, 300):
        p1 = P(cx, cy, R + 4, a)
        p2 = P(cx, cy, R + 42, a)
        f.arrow(p1[0], p1[1], p2[0], p2[1], SKY, 2.6)
    f.txt(cx, cy + 5, 'drum', MUT, 12)
    f.txt(w / 2, h - 12, 'water leaves through the holes during the spin cycle', MUT, 10.5)
    return f.render()


def string_breaks(cap, maxw=380, w=440, h=300):
    f = Fig(w, h, cap, maxw)
    cx, cy, R = 170.0, 160.0, 96.0
    f.raw('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="#94A3B8" stroke-width="2" '
          'stroke-dasharray="7 6"/>' % (cx, cy, R))
    f.circle(cx, cy, 5, INK, INK, 1)
    ang = 40.0
    p = P(cx, cy, R, ang)
    f.line(cx, cy, p[0] - 14, p[1] + 12, '#A16207', 2.6)
    f.raw('<path d="M%.1f,%.1f l 8,-6 l -4,10 l 9,-4" fill="none" stroke="#B45309" stroke-width="2.2"/>'
          % (p[0] - 16, p[1] + 14))
    f.txt(cx + 8, cy + 44, 'the string breaks here', '#B45309', 11, 'start')
    f.circle(p[0], p[1], 12, '#FCD34D', '#B45309', 2.4)
    t = P(p[0], p[1], 104, ang + 90)
    f.arrow(p[0], p[1], t[0], t[1], RED, 3.2)
    f.txt(w - 22, 40, 'it flies off along the tangent', RED, 11.5, 'end')
    f.arc(cx, cy, R + 22, 110, 180, MUT, 2, arrowhead=True)
    return f.render()


def ring_force(cap, maxw=420, w=480, h=270):
    f = Fig(w, h, cap, maxw)
    cx, cy, R = 120.0, 140.0, 92.0
    f.raw('<path d="M %.1f,%.1f A %.1f,%.1f 0 0 1 %.1f,%.1f" fill="none" stroke="#94A3B8" '
          'stroke-width="11" stroke-linecap="round"/>'
          % (cx + R * math.cos(math.radians(60)), cy - R * math.sin(math.radians(60)), R, R,
             cx + R * math.cos(math.radians(-60)), cy - R * math.sin(math.radians(-60))))
    f.raw('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="#CBD5E1" stroke-width="1.6" '
          'stroke-dasharray="6 5"/>' % (cx, cy, R))
    f.circle(cx, cy, 4.5, INK, INK, 1)
    f.txt(cx - 12, cy + 6, 'O', INK, 12, 'end', it=True)
    for a in (-38, 0, 38):
        p = P(cx, cy, R - 12, a)
        f.circle(p[0], p[1], 10, '#FCD34D', '#B45309', 2)
    p = P(cx, cy, R - 12, 0)
    f.parrow(p[0], p[1], 90, 46, IND, 2.6)
    f.txt(p[0] + 8, p[1] - 56, 'v', IND, 12.5, 'start', it=True)
    f.txt(cx, cy + R + 46, 'top view of the ring', MUT, 11)
    opts = [('a', 330.0, 74.0, 40), ('b', 430.0, 74.0, 180), ('c', 330.0, 196.0, 0), ('d', 430.0, 196.0, -50)]
    for lab, ox, oy, a in opts:
        f.rect(ox - 44, oy - 40, 88, 76, '#FCFDFF', '#E6ECF3', 1.4, 9)
        t = P(ox, oy, 30, a)
        f.arrow(ox - (t[0] - ox) / 2, oy - (t[1] - oy) / 2, t[0], t[1], INK, 2.6)
        f.txt(ox, oy + 28, '( %s )' % lab, MUT, 11)
    return f.render()

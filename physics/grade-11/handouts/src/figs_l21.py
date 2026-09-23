# -*- coding: utf-8 -*-
"""Original figures for Lesson 2-1 : simple harmonic motion (mass-spring systems)."""
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV
from figs_lesson import INK, MUT, SKY, VIO, RED, GRN, AMB, IND

WALL = '#64748B'
COIL = '#475569'


def _wall(f, x, y0, y1, side='left'):
    """hatched fixed wall."""
    f.rect(x - 9, y0, 9, y1 - y0, '#CBD5E1', WALL, 2, 1)
    n = int((y1 - y0) / 11)
    for i in range(n + 1):
        yy = y0 + i * 11.0
        f.line(x - 9, yy, x - 1, yy - 8, WALL, 1.4)


def _spring(f, x1, x2, y, coils=11, amp=11, c=COIL, w=2.2):
    """zig-zag spring from x1 to x2 at height y."""
    pts = [(x1, y)]
    span = x2 - x1
    for i in range(1, coils * 2):
        pts.append((x1 + span * i / float(coils * 2), y + (amp if i % 2 else -amp)))
    pts.append((x2, y))
    f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % p for p in pts) +
          '" fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>' % (c, w))


def _ground(f, x1, x2, y, c=WALL):
    f.line(x1, y, x2, y, c, 2.4)
    x = x1
    while x < x2 - 6:
        f.line(x, y, x - 7, y + 8, c, 1.3)
        x += 12


# --------------------------------------------------------------------------- 1
def ruler_table(cap, maxw=440, w=520, h=300):
    """a steel ruler clamped under a stack of books at the edge of a table."""
    f = Fig(w, h, cap, maxw)
    ty = 150.0
    # table top
    f.rect(40, ty, 220, 16, '#D9A066', '#8A5A2B', 2, 3)
    f.rect(66, ty + 16, 26, 104, '#C2864F', '#8A5A2B', 2, 2)
    f.rect(214, ty + 16, 26, 104, '#C2864F', '#8A5A2B', 2, 2)
    # books
    f.rect(70, ty - 22, 128, 11, '#93C5FD', '#1D4ED8', 1.8, 2)
    f.rect(66, ty - 33, 136, 11, '#FCA5A5', '#B91C1C', 1.8, 2)
    f.rect(72, ty - 44, 124, 11, '#1E3A8A', '#0F172A', 1.8, 2)
    f.txt(134, ty - 54, 'a stack of books', MUT, 10.5)
    # ruler : straight under the books, then bent beyond the edge
    f.raw('<path d="M84,%.1f L262,%.1f Q330,%.1f 392,%.1f" fill="none" stroke="#94A3B8" '
          'stroke-width="7" stroke-linecap="round"/>' % (ty - 4, ty - 4, ty - 2, ty + 34))
    f.raw('<path d="M84,%.1f L262,%.1f Q330,%.1f 392,%.1f" fill="none" stroke="#E2E8F0" '
          'stroke-width="3"/>' % (ty - 4, ty - 4, ty - 2, ty + 34))
    # free length dimension
    f.guide(262, ty - 16, 262, ty - 74)
    f.guide(392, ty + 24, 392, ty - 74)
    f.dim(262, ty - 70, 392, ty - 70, 'the free length L', PU, 0, 11.5, -8)
    f.txt(262, ty - 92, 'the edge of the table', MUT, 10.5, 'end')
    f.guide(262, ty - 88, 262, ty - 76)
    # vibration arrows at the free end
    f.parrow(404, ty + 24, 90, 40, RED, 2.6)
    f.parrow(404, ty + 44, -90, 40, RED, 2.6)
    f.txt(404, ty + 100, 'it vibrates', RED, 11)
    # sound
    for k, r in enumerate((26, 38, 50)):
        f.raw('<path d="M%.1f,%.1f A%.1f,%.1f 0 0 1 %.1f,%.1f" fill="none" stroke="#0EA5E9" '
              'stroke-width="2" opacity="%.2f"/>'
              % (392 + r * 0.55, ty + 34 - r * 0.84, r, r, 392 + r * 0.55, ty + 34 + r * 0.84,
                 0.85 - 0.16 * k))
    f.txt(482, ty + 26, 'a note', SKY, 11)
    f.txt(482, ty + 42, 'is heard', SKY, 11)
    f.txt(w / 2, h - 12, 'the amplitude dies away, but the pitch of the note does not change', MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 2
def spring_compressed(cap, maxw=430, w=500, h=268):
    """mass pushed to the left, spring fully compressed, about to be released."""
    f = Fig(w, h, cap, maxw)
    y = 120.0
    _wall(f, 60, 56, 206)
    _ground(f, 51, 470, 206)
    _spring(f, 60, 150, y, coils=13, amp=13)
    f.circle(168, y, 19, '#3B82F6', '#1D4ED8', 2.6)
    f.txt(168, y + 5, 'm', '#FFFFFF', 14, 'middle', it=True)
    f.txt(168, y - 56, 'released from rest here', INK, 11.5)
    # equilibrium position
    f.line(330, 56, 330, 180, GY, 1.8, '6 5')
    f.txt(330, 48, 'x = 0  (equilibrium)', MUT, 10.5)
    f.dim(168, y + 70, 330, y + 70, 'maximum displacement A', PU, 0, 11.5, -8)
    f.txt(105, y + 42, 'the spring is compressed', MUT, 10.5, 'start')
    f.txt(168, y - 38, 'v = 0  at this instant', RED, 11.5)
    return f.render()


# --------------------------------------------------------------------------- 3
def shm_cycle(cap, maxw=500, w=580, h=352):
    """one complete cycle : x = 0 -> +A -> 0 -> -A -> 0."""
    f = Fig(w, h, cap, maxw)
    cx, y = 300.0, 92.0
    A = 116.0
    f.line(cx - A, y - 24, cx - A, y + 3 * 62 + 30, GY, 1.4, '5 5')
    f.line(cx + A, y - 24, cx + A, y + 3 * 62 + 30, GY, 1.4, '5 5')
    rows = (('t = 0', 0.0, 'v is maximum', 'a = 0'),
            ('t = T/4', 1.0, 'v = 0', 'a is maximum'),
            ('t = T/2', 0.0, 'v is maximum', 'a = 0'),
            ('t = 3T/4', -1.0, 'v = 0', 'a is maximum'))
    for i, (lab, s, vv, aa) in enumerate(rows):
        yy = y + i * 62
        f.line(cx - A - 26, yy + 22, cx + A + 26, yy + 22, '#CBD5E1', 2)
        f.line(cx, yy + 16, cx, yy + 28, GY, 1.6)
        px = cx + A * s
        f.circle(px, yy, 14, '#3B82F6' if s == 0 else ('#F97316' if s > 0 else '#DC2626'),
                 '#1E3A8A', 2.2)
        f.txt(cx - A - 40, yy + 5, lab, INK, 12, 'end')
        f.txt(cx + A + 44, yy - 6, vv, GRN, 10.5, 'start')
        f.txt(cx + A + 44, yy + 10, aa, VIO, 10.5, 'start')
    f.txt(cx - A, y - 34, '&#8722;A', RED, 12)
    f.txt(cx, y - 34, '0', MUT, 12)
    f.txt(cx + A, y - 34, '+A', AMB, 12)
    f.txt(w / 2, h - 12, 'after a further quarter of a cycle the body is back at x = 0 and t = T',
          MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 4
def spring_mass(cap, klab='k', mlab='m', maxw=430, w=500, h=230):
    """mass on a horizontal spring, displacement x measured from equilibrium."""
    f = Fig(w, h, cap, maxw)
    y = 104.0
    _wall(f, 60, 44, 168)
    _ground(f, 51, 470, 168)
    _spring(f, 60, 272, y, coils=13, amp=12)
    f.circle(292, y, 20, '#3B82F6', '#1D4ED8', 2.6)
    f.txt(292, y + 5, mlab, '#FFFFFF', 13, 'middle')
    f.line(222, 50, 222, 162, GY, 1.8, '6 5')
    f.txt(222, 42, 'x = 0', MUT, 11)
    f.dim(222, y + 46, 292, y + 46, 'x', PU, 0, 13, -8)
    f.tbg(150, y - 34, klab, PU, 12)
    f.txt(w - 20, 28, 'a smooth horizontal surface', MUT, 10.5, 'end')
    return f.render()


# --------------------------------------------------------------------------- 5
def restoring_force(cap, xlab='x = +0.10 m', maxw=440, w=510, h=262):
    """mass displaced in the +x direction, restoring force back towards x = 0."""
    f = Fig(w, h, cap, maxw)
    y = 112.0
    _wall(f, 60, 50, 178)
    _ground(f, 51, 486, 178)
    _spring(f, 60, 302, y, coils=14, amp=12)
    f.circle(324, y, 20, '#3B82F6', '#1D4ED8', 2.6)
    f.txt(324, y + 5, 'm', '#FFFFFF', 13, 'middle', it=True)
    f.line(232, 54, 232, 172, GY, 1.8, '6 5')
    f.txt(226, 62, 'x = 0', MUT, 11, 'end')
    f.dim(232, y + 48, 324, y + 48, xlab, PU, 0, 11.5, -8)
    f.arrow(324, y - 38, 244, y - 38, RED, 3.2)
    f.txt(284, y - 50, 'F = &#8722;k x', RED, 12.5)
    f.txt(306, y - 76, 'always towards x = 0', MUT, 10.5)
    f.txt(96, y + 40, 'the spring is stretched', MUT, 10.5, 'start')
    f.parrow(400, 216, 0, 56, '#0EA5E9', 2.4)
    f.txt(430, 206, '+x', '#0EA5E9', 12)
    return f.render()


# --------------------------------------------------------------------------- 6
def energy_bars(cap, maxw=460, w=530, h=276):
    """kinetic and potential energy at x = -A, x = 0 and x = +A."""
    f = Fig(w, h, cap, maxw)
    base = 214.0
    H = 118.0
    cols = ((92.0, 'x = &#8722;A', 0.0, 1.0), (265.0, 'x = 0', 1.0, 0.0), (438.0, 'x = +A', 0.0, 1.0))
    for cxx, lab, ke, pe in cols:
        f.rect(cxx - 54, base - H * ke, 46, max(H * ke, 3), '#A7F3D0', '#047857', 2, 3)
        f.rect(cxx + 8, base - H * pe, 46, max(H * pe, 3), '#DDD6FE', '#6D28D9', 2, 3)
        f.txt(cxx - 31, base - H * ke - 10, 'KE', GRN, 11)
        f.txt(cxx + 31, base - H * pe - 10, 'PE', VIO, 11)
        f.txt(cxx, base + 24, lab, INK, 12)
    f.line(30, base, 500, base, '#94A3B8', 2.2)
    f.line(30, base - H, 500, base - H, GY, 1.4, '5 5')
    f.tbg(498, base - H - 10, 'total energy E', MUT, 10.5, 'end')
    f.txt(w / 2, h - 10, 'E = KE + PE is the same everywhere : KE is greatest at x = 0', MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 7
def sine_curve(cap, Alab='A', maxw=460, w=530, h=270):
    """one cycle of x = A sin(wt) with the amplitude and the periodic time marked."""
    f = Fig(w, h, cap, maxw)
    x0, y0 = 70.0, 132.0
    L, A = 400.0, 74.0
    f.arrow(x0 - 14, y0, x0 + L + 26, y0, DK, 2.2)
    f.arrow(x0, y0 + A + 20, x0, y0 - A - 34, DK, 2.2)
    f.txt(x0 + L + 34, y0 + 16, 't', INK, 13, 'start', it=True)
    f.txt(x0 - 16, y0 - A - 40, 'x', INK, 13, 'middle', it=True)
    pts = []
    n = 160
    for i in range(n + 1):
        t = i / float(n)
        pts.append((x0 + L * t, y0 - A * math.sin(2 * math.pi * t)))
    f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % p for p in pts) +
          '" fill="none" stroke="#2563eb" stroke-width="3"/>')
    for frac, lab in ((0.25, 'T/4'), (0.5, 'T/2'), (0.75, '3T/4'), (1.0, 'T')):
        xx = x0 + L * frac
        f.line(xx, y0 - 5, xx, y0 + 5, DK, 1.6)
        f.txt(xx, y0 + (22 if frac in (0.25, 0.75) else 22), lab, MUT, 10.5)
    xc = x0 + L * 0.25
    f.line(x0, y0 - A, xc, y0 - A, GY, 1.4, '5 5')
    f.dim(xc + 26, y0, xc + 26, y0 - A, '', PU, 0, 12)
    f.tbg(xc + 36, y0 - A / 2 + 4, Alab, PU, 12, 'start')
    f.txt(x0 + L * 0.62, y0 - A - 18, 'one complete cycle takes T', MUT, 10.5)
    return f.render()

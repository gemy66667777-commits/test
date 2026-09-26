# -*- coding: utf-8 -*-
"""Figures for the Equilibrium of Forces handout (Grade 11) - English only."""
from figlib import Fig, AR, BL, GR, PU, OR, DK, GY, NV

WOOD = '#b7813f'


def _beam(f, x0, x1, y, h=14, fill='#fcd9a8'):
    f.rect(x0, y - h / 2, x1 - x0, h, fill, '#92400e', 2, 4)


def _support(f, x, y, lab=None):
    """a triangular knife-edge support whose tip touches (x, y)."""
    f.poly([(x, y), (x - 14, y + 24), (x + 14, y + 24)], '#94a3b8', DK, 2)
    f.line(x - 22, y + 24, x + 22, y + 24, DK, 2.5)
    if lab:
        f.txt(x, y + 42, lab, NV, 14)


def _mass(f, x, y, lab, w=46, h=34, fill='#dbeafe'):
    f.line(x, y, x, y + 22, DK, 1.8)
    f.rect(x - w / 2, y + 22, w, h, fill, '#1e3a8a', 2, 4)
    f.txt(x, y + 22 + h / 2 + 5, lab, NV, 13)


# ------------------------------------------------------------------ theory
def f_three_point(cap='Fig. 3 &mdash; three forces acting at one point'):
    f = Fig(380, 300, cap, 340)
    O = (190, 150)
    f.arrow(O[0], O[1], O[0] + 130, O[1], AR, 3.2)
    f.txt(O[0] + 130, O[1] - 12, 'F&#8321; = 30 N', AR, 14)
    f.arrow(O[0], O[1], O[0], O[1] - 120, BL, 3.2)
    f.txt(O[0] + 12, O[1] - 110, 'F&#8322; = 40 N', BL, 14, 'start')
    f.arrow(O[0], O[1], O[0] - 90, O[1] + 120, GR, 3.2)
    f.txt(O[0] - 100, O[1] + 138, 'F&#8323; = ?', GR, 14)
    f.guide(O[0], O[1], O[0] - 150, O[1], GY)
    f.angle(O[0], O[1], 40, 180, 233, '&#945;', OR)
    f.circle(O[0], O[1], 5, DK, DK, 1)
    f.txt(20, 24, 'the body stays at rest', NV, 12, 'start', bold=False, it=True)
    return f.render()


def f_seesaw(cap, llab='30 kg', rlab='40 kg', ld='2 m', rd='x = ?'):
    f = Fig(500, 220, cap, 460)
    y = 110
    _beam(f, 40, 460, y, 12)
    _support(f, 250, y + 6)
    for x, lab, c in ((70, llab, '#fecdd3'), (395, rlab, '#bfdbfe')):
        f.rect(x - 22, y - 58, 44, 50, c, DK, 2, 8)
        f.circle(x, y - 70, 12, '#fde68a', DK, 2)
        f.txt(x, y - 27, lab, NV, 12.5)
    f.dim(70, y + 34, 250, y + 34, ld, PU, dy=18)
    f.dim(250, y + 34, 395, y + 34, rd, PU, dy=18)
    f.arrow(70, y + 6, 70, y + 60, AR, 2.6)
    f.arrow(395, y + 6, 395, y + 60, AR, 2.6)
    return f.render()


def f_beam(cap, L='4 m', load='300 N', dload='1 m', W='200 N', show_R=True, loadx=0.25):
    f = Fig(520, 240, cap, 470)
    x0, x1, y = 50, 470, 95
    _beam(f, x0, x1, y)
    _support(f, x0 + 10, y + 7, 'A')
    _support(f, x1 - 10, y + 7, 'B')
    xl = x0 + 10 + (x1 - x0 - 20) * loadx
    f.arrow(xl, y - 70, xl, y - 9, AR, 3)
    f.txt(xl, y - 76, load, AR, 13.5)
    xm = (x0 + x1) / 2
    f.arrow(xm, y, xm, y + 60, DK, 3)
    f.txt(xm + 8, y + 58, 'W = ' + W, DK, 13, 'start')
    if show_R:
        f.arrow(x0 + 10, y + 70, x0 + 10, y + 10, GR, 3)
        f.txt(x0 + 24, y + 62, 'R&#8321;', GR, 14, 'start')
        f.arrow(x1 - 10, y + 70, x1 - 10, y + 10, GR, 3)
        f.txt(x1 - 24, y + 62, 'R&#8322;', GR, 14, 'end')
    f.dim(x0 + 10, y - 30, xl, y - 30, dload, PU, dy=-6)
    f.dim(x0 + 10, y + 105, x1 - 10, y + 105, L, PU, dy=-6)
    return f.render()


def f_rule(cap, pivot=40, hang=10, mlab='0.6 N'):
    """a metre rule on a knife edge with a weight hanging from it (positions in cm)."""
    f = Fig(520, 210, cap, 470)
    x0, x1, y = 40, 480, 80
    X = lambda cm: x0 + (x1 - x0) * cm / 100.0
    f.rect(x0, y - 8, x1 - x0, 16, '#fef3c7', '#a16207', 1.8, 2)
    for cm in range(0, 101, 10):
        f.line(X(cm), y - 8, X(cm), y - 1, '#a16207', 1.2)
        f.txt(X(cm), y - 12, str(cm), '#a16207', 10, bold=False)
    _support(f, X(pivot), y + 8)
    _mass(f, X(hang), y + 8, mlab, 50, 30)
    f.arrow(X(50), y + 8, X(50), y + 62, DK, 2.6)
    f.txt(X(50) + 6, y + 60, 'W (rule)', DK, 12.5, 'start')
    return f.render()


def f_hinged(cap, L='2 m', load='60 N', d='0.5 m', W='40 N'):
    f = Fig(500, 260, cap, 450)
    wx, y = 60, 150
    f.rect(wx - 30, 20, 30, 220, '#e2e8f0', '#64748b', 1.6, 2)
    for k in range(9):
        f.line(wx - 30, 30 + k * 24, wx, 20 + k * 24, '#94a3b8', 1.4)
    _beam(f, wx, 440, y, 14)
    f.circle(wx + 4, y, 7, '#fff', DK, 2.4)
    f.txt(wx + 18, y + 30, 'hinge', NV, 12)
    f.line(440, y - 7, 440, 30, '#78350f', 3)
    f.line(420, 30, 470, 30, DK, 3)
    f.arrow(452, y - 20, 452, 60, GR, 2.6)
    f.txt(460, 90, 'T', GR, 15, 'start')
    xl = wx + (440 - wx) * 0.25
    _mass(f, xl, y + 7, load, 50, 30, '#fee2e2')
    f.arrow((wx + 440) / 2, y + 7, (wx + 440) / 2, y + 62, DK, 2.6)
    f.txt((wx + 440) / 2 + 8, y + 58, 'W = ' + W, DK, 12.5, 'start')
    f.dim(wx, y - 34, xl, y - 34, d, PU, dy=-6)
    f.dim(wx, y - 64, 440, y - 64, L, PU, dy=-6)
    return f.render()


def f_block_friction(cap, flab='F = 50 N', ang='37&#176;', m='10 kg'):
    f = Fig(460, 250, cap, 400)
    gy = 190
    f.line(30, gy, 430, gy, DK, 2.5)
    for k in range(20):
        f.line(40 + k * 20, gy, 32 + k * 20, gy + 8, GY, 1.4)
    f.rect(170, gy - 70, 110, 70, '#dbeafe', '#1e3a8a', 2, 6)
    f.txt(225, gy - 30, m, NV, 15)
    cx, cy = 225, gy - 35
    f.parrow(280, gy - 50, 37, 120, AR, 3)
    f.txt(390, gy - 132, flab, AR, 14)
    f.guide(280, gy - 50, 390, gy - 50)
    f.angle(280, gy - 50, 42, 0, 37, ang, OR)
    f.arrow(170, gy - 12, 90, gy - 12, OR, 3)
    f.txt(95, gy - 22, 'f', OR, 15, it=True)
    f.arrow(cx, gy - 70, cx, gy - 140, GR, 3)
    f.txt(cx + 10, gy - 130, 'N', GR, 15, 'start', it=True)
    f.arrow(cx - 30, cy, cx - 30, gy + 45, DK, 3)
    f.txt(cx - 38, gy + 42, 'W', DK, 15, 'end', it=True)
    f.arrow(300, gy + 30, 380, gy + 30, BL, 2.2)
    f.txt(340, gy + 48, 'constant velocity', BL, 12)
    return f.render()


def f_plank_man(cap):
    f = Fig(520, 210, cap, 470)
    x0, x1, y = 40, 480, 100
    X = lambda m: x0 + (x1 - x0) * m / 5.0
    _beam(f, x0, x1, y)
    _support(f, X(0) + 8, y + 7, 'A')
    _support(f, X(4), y + 7, 'C')
    f.txt(X(5) - 6, y - 14, 'B', NV, 14)
    px = X(4.4)
    f.circle(px, y - 62, 11, '#fde68a', DK, 2)
    f.line(px, y - 51, px, y - 22, DK, 3)
    f.line(px, y - 22, px - 9, y - 7, DK, 3); f.line(px, y - 22, px + 9, y - 7, DK, 3)
    f.line(px - 12, y - 42, px + 12, y - 42, DK, 3)
    f.txt(px + 16, y - 55, '700 N', AR, 12.5, 'start')
    f.dim(X(0) + 8, y + 50, X(4), y + 50, '4 m', PU, dy=-6)
    f.dim(X(4), y + 50, X(5), y + 50, '1 m', PU, dy=-6)
    f.txt(X(2.5), y + 88, 'uniform plank : 5 m , 300 N', NV, 12.5)
    return f.render()

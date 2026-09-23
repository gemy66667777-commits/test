# -*- coding: utf-8 -*-
"""Original figures for Lesson 1-9 : momentum and mechanical energy in collisions."""
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV
from figs_lesson import INK, MUT, SKY, VIO, RED, GRN, AMB, IND


def _road(f, gy, x1, x2):
    f.line(x1, gy, x2, gy, '#475569', 3)
    for x in range(int(x1) + 10, int(x2) - 6, 26):
        f.line(x, gy + 7, x + 14, gy + 7, '#94A3B8', 2.4)


def _car(f, x, gy, w, col, edge, lab, sub=None):
    h = 26.0
    f.rect(x, gy - h - 12, w, h, col, edge, 2.2, 5)
    f.rect(x + w * 0.22, gy - h - 26, w * 0.5, 16, '#E0F2FE', edge, 2, 4)
    f.circle(x + w * 0.24, gy - 8, 9, '#334155', DK, 2)
    f.circle(x + w * 0.76, gy - 8, 9, '#334155', DK, 2)
    f.txt(x + w / 2, gy - h - 34, lab, INK, 12)
    if sub:
        f.txt(x + w / 2, gy + 26, sub, MUT, 11.5)


def car_truck(cap, maxw=470, w=540, h=270):
    f = Fig(w, h, cap, maxw)
    gy = 118.0
    _road(f, gy, 20, w - 20)
    _car(f, 56, gy, 92, '#BFDBFE', '#1D4ED8', '1000 kg', 'car A')
    _car(f, 300, gy, 150, '#FECACA', '#991B1B', '3000 kg', 'truck B  (at rest)')
    f.parrow(160, gy - 26, 0, 58, RED, 3)
    f.txt(192, gy - 38, '20 m/s', RED, 12)
    f.txt(w / 2, 30, 'before the collision', MUT, 11)
    gy2 = 236.0
    _road(f, gy2, 20, w - 20)
    _car(f, 210, gy2, 92, '#BFDBFE', '#1D4ED8', '', None)
    _car(f, 302, gy2, 150, '#FECACA', '#991B1B', '', None)
    f.parrow(462, gy2 - 26, 0, 50, RED, 3)
    f.txt(486, gy2 - 38, 'v = ?', RED, 12)
    f.txt(240, gy2 + 26, 'locked together after the collision', MUT, 11, 'start')
    return f.render()


def ball_wall(cap, v1='10 m/s', v2='6 m/s', maxw=400, w=460, h=250):
    f = Fig(w, h, cap, maxw)
    f.rect(w - 92, 34, 44, 180, '#CBD5E1', '#475569', 2.6, 3)
    for y in range(44, 210, 18):
        f.line(w - 92, y, w - 48, y, '#94A3B8', 1.2)
    f.txt(w - 70, 24, 'wall', MUT, 11)
    f.circle(150, 82, 22, '#FB923C', '#9A3412', 2.4)
    f.raw('<path d="M128,82 a22,22 0 0 0 44,0" fill="none" stroke="#9A3412" stroke-width="1.6"/>')
    f.parrow(178, 82, 0, 106, RED, 3.2)
    f.txt(230, 62, 'before : ' + v1, RED, 12)
    f.circle(180, 176, 22, '#FB923C', '#9A3412', 2.4)
    f.raw('<path d="M158,176 a22,22 0 0 0 44,0" fill="none" stroke="#9A3412" stroke-width="1.6"/>')
    f.parrow(152, 176, 180, 84, IND, 3.2)
    f.txt(96, 148, 'after : ' + v2, IND, 12, 'start')
    return f.render()


def clay_trolley(cap, maxw=470, w=540, h=270):
    f = Fig(w, h, cap, maxw)
    gy = 116.0
    f.line(20, gy, w - 20, gy, '#64748B', 4)
    f.raw('<path d="M96,%d q 14,-26 32,-16 q 16,-18 30,2 q 16,4 8,14 Z" fill="#B45309" stroke="#7C2D12" '
          'stroke-width="2.2"/>' % int(gy - 6))
    f.txt(128, gy + 24, '0.50 kg  clay', MUT, 11.5)
    f.parrow(176, gy - 22, 0, 54, RED, 3)
    f.txt(212, gy - 34, '8.0 m/s', RED, 12)
    f.rect(320, gy - 26, 120, 20, '#93C5FD', '#1D4ED8', 2.4, 4)
    f.circle(344, gy - 4, 9, '#334155', DK, 2); f.circle(416, gy - 4, 9, '#334155', DK, 2)
    f.txt(380, gy + 24, '1.50 kg  trolley  (at rest)', MUT, 11.5)
    f.txt(w / 2, 28, 'before the collision', MUT, 11)
    gy2 = 232.0
    f.line(20, gy2, w - 20, gy2, '#64748B', 4)
    f.rect(300, gy2 - 26, 120, 20, '#93C5FD', '#1D4ED8', 2.4, 4)
    f.circle(324, gy2 - 4, 9, '#334155', DK, 2); f.circle(396, gy2 - 4, 9, '#334155', DK, 2)
    f.raw('<path d="M318,%d q 12,-22 28,-14 q 14,-16 26,2 q 14,4 6,12 Z" fill="#B45309" stroke="#7C2D12" '
          'stroke-width="2.2"/>' % int(gy2 - 26))
    f.parrow(440, gy2 - 20, 0, 52, RED, 3)
    f.txt(470, gy2 - 32, "v' = ?", RED, 12)
    f.txt(200, gy2 - 10, 'the clay sticks to the trolley', MUT, 11, 'end')
    return f.render()


def collide_before_after(cap, m1='A', m2='B', v1='4.0 m/s', v2='at rest',
                         u1="v(A) = ?", u2="3.0 m/s", maxw=470, w=540, h=250):
    f = Fig(w, h, cap, maxw)
    for row, (ya, la, lb, ra, rb) in enumerate(((104.0, v1, v2, None, None), (206.0, None, None, u1, u2))):
        f.line(30, ya, w - 30, ya, '#A16207', 4)
        x1, x2 = (120.0, 300.0) if row == 0 else (170.0, 350.0)
        f.circle(x1, ya - 24, 22, '#3B82F6', '#1D4ED8', 2.4)
        f.txt(x1, ya - 18 + 5, m1, '#fff', 13)
        f.circle(x2, ya - 24, 22, '#94A3B8', '#334155', 2.4)
        f.txt(x2, ya - 18 + 5, m2, '#fff', 13)
        if row == 0:
            f.parrow(x1 + 26, ya - 24, 0, 44, RED, 2.8)
            f.txt(x1 + 4, ya + 26, la, RED, 11.5)
            f.txt(x2, ya + 26, lb, MUT, 11.5)
        else:
            f.parrow(x1 + 26, ya - 24, 0, 30, RED, 2.6)
            f.txt(x1 - 6, ya + 26, ra, RED, 11.5)
            f.parrow(x2 + 26, ya - 24, 0, 52, IND, 2.8)
            f.txt(x2 + 16, ya + 26, rb, IND, 11.5)
    f.txt(w - 40, 40, 'before', MUT, 11, 'end')
    f.txt(w - 40, 150, 'after', MUT, 11, 'end')
    return f.render()

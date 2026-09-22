# -*- coding: utf-8 -*-
"""Original figures for Lesson 1-3 : projectiles launched at an angle."""
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV
from figs_lesson import INK, MUT, SKY, VIO, RED, GRN, AMB, IND


def _traj(f, x0, y0, R, H, c=IND, w=2.2, dash='6 5', n=52):
    pts = [(x0 + R * (i / float(n)), y0 - 4 * H * (i / float(n)) * (1 - i / float(n))) for i in range(n + 1)]
    f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % p for p in pts) +
          '" fill="none" stroke="%s" stroke-width="%s" stroke-dasharray="%s"/>' % (c, w, dash))
    return pts


def _ground(f, gy, x1, x2):
    f.line(x1, gy, x2, gy, DK, 2.6)
    for x in range(int(x1) + 8, int(x2) - 4, 20):
        f.line(x, gy, x - 8, gy + 8, '#94A3B8', 1.4)


def traj_full(cap, maxw=520, w=640, h=380):
    f = Fig(w, h, cap, maxw)
    gy = 296.0; x0 = 74.0; R = 470.0; th = 55.0
    H = R * math.tan(math.radians(th)) / 4
    _ground(f, gy, 22, w - 22)
    pts = _traj(f, x0, gy, R, H)
    # launch
    f.parrow(x0, gy, th, 86, RED, 3.2)
    tp = P(x0, gy, 96, th)
    f.txt(tp[0] - 12, tp[1] - 6, 'v₀', RED, 14, 'end', it=True)
    f.angle(x0, gy, 40, 0, th, 'θ', OR, 58, 13)
    f.circle(x0, gy, 4.5, INK, INK, 1)
    f.txt(x0 - 14, gy + 18, 'O', INK, 13, 'end', it=True)
    # position 1 (rising)
    i1 = 10
    p1 = pts[i1]
    f.circle(p1[0], p1[1], 5.5, RED, RED, 1)
    f.txt(p1[0] + 6, p1[1] + 26, '( 1 )', INK, 12, 'start')
    f.parrow(p1[0], p1[1], 0, 54, GRN, 2.8)
    f.parrow(p1[0], p1[1], 90, 40, SKY, 2.8)
    f.arrow(p1[0], p1[1], p1[0] + 54, p1[1] - 40, RED, 2.8)
    f.txt(p1[0] + 34, p1[1] + 16, 'vₓ₁', GRN, 11.5)
    f.txt(p1[0] - 10, p1[1] - 26, 'vᵧ₁', SKY, 11.5, 'end')
    f.txt(p1[0] + 60, p1[1] - 48, 'v₁', RED, 12.5, 'start', it=True)
    # position 2 (top)
    i2 = 26
    p2 = pts[i2]
    f.circle(p2[0], p2[1], 5.5, RED, RED, 1)
    f.txt(p2[0], p2[1] - 16, '( 2 )', INK, 12)
    f.parrow(p2[0], p2[1], 0, 54, GRN, 2.8)
    f.txt(p2[0] + 58, p2[1] - 7, 'vₓ₂', GRN, 11.5, 'start')
    # Y and X for position 1
    f.guide(p1[0], p1[1], p1[0], gy + 44)
    f.dim(x0 - 34, gy, x0 - 34, p1[1], '', PU, 0, 12)
    f.guide(x0 - 40, p1[1], p1[0], p1[1])
    f.tbg(x0 - 34, (gy + p1[1]) / 2, 'Y', PU, 13)
    f.dim(x0, gy + 40, p1[0], gy + 40, 'X', PU, 0, 12.5, -7)
    f.guide(x0, gy, x0, gy + 44)
    # H and R
    f.guide(p2[0], p2[1], p2[0], gy + 68)
    f.dim(p2[0] + 30, gy, p2[0] + 30, p2[1], '', PU, 0, 12)
    f.guide(p2[0], p2[1], p2[0] + 36, p2[1])
    f.tbg(p2[0] + 30, (gy + p2[1]) / 2, 'H', PU, 13)
    f.guide(x0 + R, gy, x0 + R, gy + 68)
    f.dim(x0, gy + 64, x0 + R, gy + 64, 'R', PU, 0, 12.5, -7)
    return f.render()


def axes_traj(cap, ang=60.0, vlab='v₀', maxw=340, w=400, h=250, from_vertical=False):
    f = Fig(w, h, cap, maxw)
    gy = 196.0; x0 = 66.0; R = 290.0
    H = R * math.tan(math.radians(ang)) / 4
    f.arrow(x0, gy, w - 24, gy, '#94A3B8', 1.8)
    f.arrow(x0, gy, x0, 22, '#94A3B8', 1.8)
    f.txt(w - 22, gy + 20, 'x', MUT, 12, 'end', it=True)
    f.txt(x0 + 16, 30, 'y', MUT, 12, 'start', it=True)
    _ground(f, gy, 24, w - 24)
    _traj(f, x0, gy, R, H)
    f.parrow(x0, gy, ang, 96, RED, 3.2)
    tp = P(x0, gy, 108, ang)
    f.txt(tp[0] + 8, tp[1] + 2, vlab, RED, 13.5, 'start')
    if from_vertical:
        f.guide(x0, gy, x0, 40)
        f.angle(x0, gy, 46, 90, ang, '%g°' % (90 - ang), OR, 66, 12.5)
    else:
        f.angle(x0, gy, 42, 0, ang, '%g°' % ang, OR, 60, 12.5)
    f.circle(x0, gy, 4.5, INK, INK, 1)
    f.txt(x0 - 12, gy + 18, 'O', INK, 12.5, 'end', it=True)
    return f.render()


def ball_traj(cap, vlab, ang=60.0, maxw=460, w=540, h=250):
    f = Fig(w, h, cap, maxw)
    gy = 196.0; x0 = 60.0; R = 420.0
    H = R * math.tan(math.radians(ang)) / 4
    _ground(f, gy, 20, w - 20)
    pts = _traj(f, x0, gy, R, H)
    f.parrow(x0, gy, ang, 88, RED, 3.2)
    tp0 = P(x0, gy, 88, ang)
    off = P(0, 0, 30, ang - 90)
    f.txt(tp0[0] + off[0] + 6, tp0[1] + off[1] + 4, vlab, RED, 13, 'start')
    f.angle(x0, gy, 38, 0, ang, '%g°' % ang, OR, 56, 12)
    ax, ay = pts[len(pts) // 2]
    f.circle(ax, ay, 5.5, RED, RED, 1)
    f.guide(ax, ay, ax, gy + 34)
    f.dim(ax + 28, gy, ax + 28, ay, '', PU, 0, 12)
    f.guide(ax, ay, ax + 34, ay)
    f.tbg(ax + 28, (gy + ay) / 2, 'H', PU, 12.5)
    f.dim(x0, gy + 30, ax, gy + 30, 't(up)', PU, 0, 11.5, -6)
    f.dim(ax, gy + 30, x0 + R, gy + 30, 't(down)', PU, 0, 11.5, -6)
    f.guide(x0, gy, x0, gy + 34); f.guide(x0 + R, gy, x0 + R, gy + 58)
    f.dim(x0, gy + 54, x0 + R, gy + 54, 'R', PU, 0, 12, -6)
    f.circle(x0 + R, gy, 5, INK, INK, 1)
    return f.render()


def building_angle(cap, hlab, vlab, anglab, maxw=470, w=560, h=300):
    f = Fig(w, h, cap, maxw)
    gy = 246.0
    _ground(f, gy, 20, w - 20)
    bx, bw, top = 52.0, 92.0, 128.0
    f.rect(bx, top, bw, gy - top, '#E7E2D6', '#A1887F', 2.2, 3)
    for r in range(3):
        for c in range(2):
            f.rect(bx + 16 + c * 36, top + 16 + r * 32, 24, 20, '#BBDEFB', '#64B5F6', 1.4, 2)
    x0, y0 = bx + bw, top - 4
    th = 30.0
    R = 330.0
    S = R * math.tan(math.radians(th)); dh = gy - y0
    pts = [(x0 + R * (i / 52.0), y0 - S * (i / 52.0) + (S + dh) * (i / 52.0) ** 2) for i in range(53)]
    f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % p for p in pts) +
          '" fill="none" stroke="%s" stroke-width="2.2" stroke-dasharray="6 5"/>' % IND)
    f.parrow(x0, y0, th, 78, RED, 3.2)
    tp = P(x0, y0, 90, th)
    f.txt(tp[0] + 8, tp[1] - 4, vlab, RED, 12.5, 'start')
    f.guide(x0, y0, x0 + 70, y0)
    f.angle(x0, y0, 36, 0, th, anglab, OR, 54, 12)
    apex = min(pts, key=lambda p: p[1])
    f.circle(apex[0], apex[1], 5, RED, RED, 1)
    f.guide(apex[0], apex[1], apex[0] + 66, apex[1])
    f.dim(apex[0] + 58, gy, apex[0] + 58, apex[1], '', PU, 0, 12)
    f.tbg(apex[0] + 58, (gy + apex[1]) / 2, 'h(max)', PU, 12)
    f.dim(bx + 22, top, bx + 22, gy, '', PU, 0, 12)
    f.tbg(bx + 22, (top + gy) / 2, hlab, PU, 12)
    f.guide(x0, gy, x0, gy + 34); f.guide(pts[-1][0], gy, pts[-1][0], gy + 34)
    f.dim(x0, gy + 30, pts[-1][0], gy + 30, 'x', PU, 0, 12, -6)
    return f.render()


def two_angles(cap, a1=30.0, a2=60.0, maxw=440, w=520, h=250):
    f = Fig(w, h, cap, maxw)
    gy = 206.0; x0 = 70.0; R = 350.0
    _ground(f, gy, 20, w - 20)
    for ang, col, nm in ((a1, IND, 'A'), (a2, RED, 'B')):
        H = R * math.tan(math.radians(ang)) / 4
        pts = _traj(f, x0, gy, R, H, col)
        f.parrow(x0, gy, ang, 74, col, 3)
        ax, ay = pts[len(pts) // 2]
        f.tbg(ax + (0 if ang == a1 else 0), ay - 13, '%g°' % ang, col, 12)
    f.circle(x0 + R, gy, 5.5, INK, INK, 1)
    f.txt(x0 + R, gy + 26, 'same landing point', MUT, 11)
    f.txt(w - 22, 28, 'same initial speed v₀', MUT, 11, 'end')
    f.circle(x0, gy, 4.5, INK, INK, 1)
    return f.render()

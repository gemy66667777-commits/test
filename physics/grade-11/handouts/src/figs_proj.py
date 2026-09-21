# -*- coding: utf-8 -*-
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV


def _ground(f, y, x1, x2):
    f.line(x1, y, x2, y, DK, 2.6)
    x = x1
    while x < x2:
        f.line(x, y, x - 9, y + 9, '#94a3b8', 1.5)
        x += 17


def _parab(f, x0, y0, R, H, c=BL, dash='6 5', w=2.2):
    pts = []
    for i in range(49):
        t = i / 48.0
        pts.append((x0 + R * t, y0 - 4 * H * t * (1 - t)))
    d = 'M' + ' L'.join('%.1f,%.1f' % p for p in pts)
    f.raw('<path d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-dasharray="%s"/>' % (d, c, w, dash))
    return pts


def q1_fig():
    f = Fig(540, 220, 'Fig. 1', 440)
    th, R = 30.0, 400.0
    H = R * math.tan(math.radians(th)) / 4
    x0, y0 = 70.0, 178.0
    _ground(f, y0, 35, 510)
    _parab(f, x0, y0, R, H, BL)
    f.parrow(x0, y0, th, 92, AR, 3.2)
    f.txt(x0 + 92, y0 - 62, 'v₀ = 40 m/s', AR, 14, 'start')
    f.angle(x0, y0, 44, 0, th, '30°', OR, 62, 13)
    f.circle(x0 + R, y0, 5, AR, AR, 1)
    f.txt(x0 + R, y0 - 14, 'lands here', GY, 11)
    f.txt(500, 32, 'g = 10 m/s²', GY, 12, 'end')
    f.txt(270, 90, 'T = ?', NV, 14)
    return f.render()


def q2_fig():
    f = Fig(520, 250, 'Fig. 2', 430)
    th, R = 53.0, 330.0
    H = R * math.tan(math.radians(th)) / 4
    x0, y0 = 85.0, 205.0
    _ground(f, y0, 45, 490)
    _parab(f, x0, y0, R, H, BL)
    ax = x0 + R / 2
    f.guide(ax, y0 - H, x0 - 20, y0 - H)
    f.dim(ax, y0, ax, y0 - H, 'H = ?', PU, 0, 14, dy=4, dx=32)
    f.parrow(x0, y0, th, 92, AR, 3.2)
    f.txt(x0 + 98, y0 - 26, 'v₀ = 20 m/s', AR, 14, 'start')
    f.angle(x0, y0, 42, 0, th, '53°', OR, 62, 13)
    f.txt(485, 32, 'g = 10 m/s²', GY, 12, 'end')
    return f.render()


def q3_fig():
    f = Fig(420, 280, 'Fig. 3', 320)
    O = (95.0, 235.0); tipx = (245.0, 235.0); tipy = (95.0, 35.0)
    f.arrow(O[0], O[1], tipx[0], tipx[1], BL, 3.2)
    f.arrow(O[0], O[1], tipy[0], tipy[1], GR, 3.2)
    f.guide(tipx[0], tipx[1], tipx[0], tipy[1]); f.guide(tipy[0], tipy[1], tipx[0], tipy[1])
    f.arrow(O[0], O[1], tipx[0], tipy[1], AR, 3.2, dash='7 5')
    f.txt(170, 262, 'vₓ = 30 m/s', BL, 13.5)
    f.raw('<text x="85" y="120" fill="%s" font-size="13.5" text-anchor="end" font-family="Helvetica, Arial, '
          'sans-serif" font-weight="700">v<tspan dy="4" font-size="10.5">y</tspan>'
          '<tspan dy="-4"> = 40 m/s</tspan></text>' % GR)
    f.txt(252, 92, 'v₀ = ?', AR, 14, 'start')
    f.angle(O[0], O[1], 58, 0, 53.13, 'θ = ?', OR, 84, 13)
    f.circle(O[0], O[1], 4, DK, DK, 1)
    return f.render()


def q4_fig():
    f = Fig(520, 215, 'Fig. 4', 430)
    th, R = 37.0, 380.0
    H = R * math.tan(math.radians(th)) / 4
    x0, y0 = 70.0, 180.0
    _ground(f, y0, 35, 490)
    _parab(f, x0, y0, R, H, BL)
    f.parrow(x0, y0, th, 92, AR, 3.2)
    f.txt(x0 + 78, y0 - 68, 'v₀ = 50 m/s', AR, 14, 'start')
    f.angle(x0, y0, 42, 0, th, '37°', OR, 60, 13)
    ax, ay = x0 + R / 2, y0 - H
    f.circle(ax, ay, 5.5, AR, AR, 1)
    f.txt(ax, ay - 14, 'P (highest point)', NV, 12)
    f.txt(ax + 78, ay + 6, 'v = ?', NV, 14, 'start')
    f.txt(485, 30, 'g = 10 m/s²', GY, 12, 'end')
    return f.render()


def q5_fig():
    f = Fig(520, 250, 'Fig. 5', 440)
    R = 330.0
    x0, y0 = 85.0, 205.0
    _ground(f, y0, 45, 490)
    for th, c, nm, dy in ((30.0, BL, 'A  (30°)', 0), (60.0, AR, 'B  (60°)', 0)):
        H = R * math.tan(math.radians(th)) / 4
        _parab(f, x0, y0, R, H, c)
        f.parrow(x0, y0, th, 74, c, 3)
        f.txt(x0 + R / 2 + (78 if th == 30 else -66), y0 - H - 10, nm, c, 13.5)
    f.angle(x0, y0, 42, 0, 30, '30°', OR, 60, 12)
    f.angle(x0, y0, 66, 0, 60, '60°', OR, 88, 12)
    f.circle(x0 + R, y0, 5, DK, DK, 1)
    f.txt(x0 + R + 2, y0 + 26, 'same landing point', GY, 11)
    f.txt(485, 30, 'same speed v₀ , g = 10 m/s²', GY, 12, 'end')
    return f.render()

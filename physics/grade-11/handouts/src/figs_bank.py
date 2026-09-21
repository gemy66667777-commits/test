# -*- coding: utf-8 -*-
"""Figures for the 60-question bank: relative velocity + horizontal projectiles."""
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV

BODY = '#dbeafe'


def _car(f, x, y, w=76, c=BL, flip=False, lab=None):
    h = 22
    f.rect(x, y - h, w, h, '#e0e7ff', c, 2, 4)
    f.rect(x + (w * 0.22 if not flip else w * 0.30), y - h - 13, w * 0.48, 14, '#eff6ff', c, 2, 3)
    f.circle(x + w * 0.24, y + 2, 8, '#475569', DK, 2)
    f.circle(x + w * 0.76, y + 2, 8, '#475569', DK, 2)
    if lab:
        f.txt(x + w / 2, y - h - 22, lab, c, 14)


def cars_road(cap, lab1, lab2, same=True, maxw=470):
    f = Fig(560, 195, cap, maxw)
    y = 118.0
    f.line(30, y + 12, 530, y + 12, DK, 3)
    for x in range(40, 520, 34):
        f.line(x, y + 22, x + 16, y + 22, '#94a3b8', 3)
    _car(f, 70, y, 76, BL, False, 'A')
    _car(f, 330, y, 76, GR, not same, 'B')
    f.parrow(90, y - 58, 0, 66, AR, 3)
    f.txt(123, y - 76, lab1, AR, 13)
    if same:
        f.parrow(350, y - 58, 0, 66, AR, 3)
    else:
        f.parrow(416, y - 58, 180, 66, AR, 3)
    f.txt(383, y - 76, lab2, AR, 13)
    return f.render()


def cars_cross(cap, labE, labN, maxw=400):
    f = Fig(430, 290, cap, maxw)
    f.rect(40, 150, 360, 56, '#eef2f7', '#cbd5e1', 2, 4)
    f.rect(175, 30, 56, 240, '#eef2f7', '#cbd5e1', 2, 4)
    f.line(40, 178, 400, 178, '#94a3b8', 2, '14 10')
    f.line(203, 30, 203, 270, '#94a3b8', 2, '14 10')
    _car(f, 42, 196, 68, BL, False, 'A')
    f.parrow(116, 196 - 46, 0, 50, AR, 2.8)
    f.txt(141, 196 - 56, labE, AR, 12.5)
    f.circle(203, 96, 15, '#e0e7ff', GR, 2.4)
    f.rect(186, 82, 34, 30, '#e0e7ff', GR, 2.2, 4)
    f.txt(178, 70, 'B', GR, 14, 'end')
    f.parrow(203, 70, 90, 42, AR, 2.8)
    f.txt(218, 40, labN, AR, 12.5, 'start')
    f.txt(410, 178, 'E', GY, 13, 'start')
    f.txt(203, 22, 'N', GY, 13)
    return f.render()


def boat_river(cap, wlab, blab, clab, maxw=430):
    f = Fig(500, 260, cap, maxw)
    yT, yB = 55.0, 205.0
    f.rect(40, yT, 420, yB - yT, '#e0f2fe', 'none', 0, 0)
    for yy in (yT, yB):
        f.line(40, yy, 460, yy, DK, 3)
    for x in range(45, 455, 22):
        f.line(x, yB, x - 9, yB + 9, '#94a3b8', 1.6)
        f.line(x, yT, x + 9, yT - 9, '#94a3b8', 1.6)
    for yy in (95, 135, 175):
        f.parrow(150, yy, 0, 70, '#38bdf8', 2.4)
    f.txt(305, 100, clab, '#0284c7', 12.5, 'start')
    f.poly([(120, yB - 6), (152, yB - 6), (144, yB - 22), (128, yB - 22)], '#fed7aa', '#c2410c', 2)
    f.parrow(136, yB - 26, 90, 70, AR, 3)
    f.txt(126, yB - 78, blab, AR, 13, 'end')
    f.guide(136, yB - 26, 226, yT + 26)
    f.arrow(136, yB - 26, 226, yT + 26, PU, 2.6, dash='7 5')
    f.txt(238, 120, 'resultant', PU, 12, 'start')
    f.dim(66, yB, 66, yT, '', PU, 0, 13)
    f.tbg(66 - 32, (yT + yB) / 2, wlab, PU, 13)
    return f.render()


def rain_man(cap, rlab, mlab, maxw=380):
    f = Fig(420, 250, cap, maxw)
    y = 210.0
    f.line(30, y, 390, y, DK, 3)
    for x in range(40, 380, 22):
        f.line(x, y, x - 9, y + 9, '#94a3b8', 1.6)
    for x in (70, 120, 170, 300, 350):
        f.parrow(x, 35, -90, 52, '#38bdf8', 2.2)
    f.txt(60, 30, rlab, '#0284c7', 12.5, 'start')
    f.circle(235, 120, 13, '#fde68a', DK, 2)
    f.line(235, 133, 235, 172, DK, 3)
    f.line(235, 145, 218, 162, DK, 2.6); f.line(235, 145, 254, 160, DK, 2.6)
    f.line(235, 172, 220, y, DK, 2.6); f.line(235, 172, 252, y, DK, 2.6)
    f.parrow(258, 150, 0, 62, AR, 3)
    f.txt(268, 138, mlab, AR, 13, 'start')
    return f.render()


def train_man(cap, tlab, mlab, same=True, maxw=450):
    f = Fig(520, 195, cap, maxw)
    y = 130.0
    f.rect(55, y - 62, 400, 62, '#e0e7ff', DK, 2.4, 7)
    for k in range(4):
        f.rect(75 + k * 95, y - 52, 52, 30, '#eff6ff', '#64748b', 1.8, 3)
    f.line(30, y + 10, 490, y + 10, DK, 3)
    for c in (95, 175, 330, 410):
        f.circle(c, y + 4, 9, '#475569', DK, 2)
    f.parrow(200, y - 90, 0, 80, AR, 3)
    f.txt(240, y - 98, tlab, AR, 13)
    f.circle(300, y - 46, 8, '#fde68a', DK, 1.8)
    f.line(300, y - 38, 300, y - 14, DK, 2.4)
    f.parrow(312 if same else 288, y - 34, 0 if same else 180, 38, GR, 2.6)
    f.txt(340 if same else 280, y - 7, mlab, GR, 12.5, 'start' if same else 'end')
    return f.render()


def vec_pair(cap, alab, blab, ang, maxw=340):
    f = Fig(380, 240, cap, maxw)
    O = (90.0, 190.0)
    f.arrow(O[0], O[1], O[0] + 190, O[1], BL, 3.2)
    f.txt(O[0] + 100, O[1] + 26, alab, BL, 13.5)
    tip = P(O[0], O[1], 165, ang)
    f.arrow(O[0], O[1], tip[0], tip[1], GR, 3.2)
    f.txt(tip[0] + 8, tip[1] - 6, blab, GR, 13.5, 'start')
    f.angle(O[0], O[1], 52, 0, ang, '%d°' % ang, OR, 72, 13)
    f.circle(O[0], O[1], 4, DK, DK, 1)
    return f.render()


# --------------------------- horizontal projectiles ---------------------------
def _hpar(f, x0, y0, R, H, c=BL, dash='6 5'):
    pts = [(x0 + R * (i / 40.0), y0 + H * (i / 40.0) ** 2) for i in range(41)]
    f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % p for p in pts) +
          '" fill="none" stroke="%s" stroke-width="2.2" stroke-dasharray="%s"/>' % (c, dash))


def table_proj(cap, hlab, vlab, rlab='R = ?', table=True, maxw=440):
    f = Fig(520, 250, cap, maxw)
    gy = 200.0; tx, ty = 130.0, 88.0
    if table:
        f.rect(45, ty, 90, 11, '#cbd5e1', DK, 2, 2)
        f.line(60, ty + 11, 60, gy, DK, 4); f.line(122, ty + 11, 122, gy, DK, 4)
    else:
        f.rect(35, ty, 100, gy - ty, '#e2e8f0', DK, 2.2, 3)
    f.line(20, gy, 500, gy, DK, 3)
    for x in range(28, 495, 22):
        f.line(x, gy, x - 9, gy + 9, '#94a3b8', 1.6)
    f.circle(tx + 4, ty - 8, 8, AR, DK, 1.6)
    f.parrow(tx + 14, ty - 8, 0, 62, AR, 3)
    f.txt(tx + 80, ty - 16, vlab, AR, 13, 'start')
    _hpar(f, tx + 4, ty - 8, 300, gy - ty + 8)
    f.dim(38, ty, 38, gy, '', PU, 0, 13)
    f.tbg(74, (ty + gy) / 2, hlab, PU, 13)
    f.guide(tx + 4, gy, tx + 4, gy + 34); f.guide(tx + 304, gy, tx + 304, gy + 34)
    f.dim(tx + 4, gy + 30, tx + 304, gy + 30, rlab, PU, 0, 13, -7)
    return f.render()


def plane_drop(cap, hlab, vlab, rlab='x = ?', maxw=460):
    f = Fig(540, 250, cap, maxw)
    gy = 208.0; px, py = 120.0, 62.0
    f.poly([(px - 42, py), (px + 34, py), (px + 46, py - 9), (px + 4, py - 9), (px - 14, py - 24),
            (px - 26, py - 24), (px - 18, py - 9), (px - 42, py - 9)], '#cbd5e1', DK, 2)
    f.poly([(px - 16, py), (px + 6, py), (px - 6, py + 17)], '#cbd5e1', DK, 2)
    f.parrow(px + 52, py - 6, 0, 58, AR, 3)
    f.txt(px + 118, py - 14, vlab, AR, 13, 'start')
    f.circle(px, py + 22, 7, '#b45309', DK, 1.8)
    _hpar(f, px, py + 22, 290, gy - py - 22)
    f.line(20, gy, 515, gy, DK, 3)
    for x in range(28, 510, 22):
        f.line(x, gy, x - 9, gy + 9, '#94a3b8', 1.6)
    f.dim(px - 58, py + 10, px - 58, gy, hlab, PU, 0, 13, dy=4, dx=-28)
    f.guide(px - 62, py + 10, px, py + 10); f.guide(px - 62, gy, px - 20, gy)
    f.guide(px, gy, px, gy + 32); f.guide(px + 290, gy, px + 290, gy + 32)
    f.dim(px, gy + 28, px + 290, gy + 28, rlab, PU, 0, 13, -7)
    return f.render()


def two_balls(cap, maxw=400):
    f = Fig(460, 230, cap, maxw)
    gy = 190.0; ty = 60.0
    f.rect(40, ty, 80, 10, '#cbd5e1', DK, 2, 2)
    f.line(52, ty + 10, 52, gy, DK, 4); f.line(108, ty + 10, 108, gy, DK, 4)
    f.line(20, gy, 440, gy, DK, 3)
    for x in range(28, 435, 22):
        f.line(x, gy, x - 9, gy + 9, '#94a3b8', 1.6)
    f.circle(124, ty - 7, 8, AR, DK, 1.6)
    f.parrow(136, ty - 7, 0, 52, AR, 2.8)
    f.txt(200, ty - 16, 'X : projected horizontally', AR, 12, 'start')
    _hpar(f, 124, ty - 7, 250, gy - ty + 7)
    f.circle(150, ty - 7, 0.1, '#fff', 'none', 0)
    f.circle(92, ty - 7, 8, GR, DK, 1.6)
    f.line(92, ty + 4, 92, gy - 6, GR, 2.2, '6 5')
    f.txt(84, ty - 22, 'Y : dropped', GR, 12, 'end')
    f.txt(230, gy + 30, 'released at the same instant from the same height', GY, 11.5)
    return f.render()


def building_proj(cap, hlab, vlab, anglab, rlab='R = ?', maxw=450):
    f = Fig(540, 270, cap, maxw)
    gy = 222.0
    f.rect(58, 70, 86, gy - 70, '#e2e8f0', DK, 2.2, 3)
    for r in range(4):
        for c in range(2):
            f.rect(72 + c * 34, 88 + r * 32, 22, 20, '#cbd5e1', '#94a3b8', 1.4, 2)
    f.line(20, gy, 520, gy, DK, 3)
    for x in range(28, 515, 22):
        f.line(x, gy, x - 9, gy + 9, '#94a3b8', 1.6)
    x0, y0, th = 144.0, 70.0, 32.0
    f.parrow(x0, y0, th, 76, AR, 3.2)
    f.txt(x0 + 76, y0 - 58, vlab, AR, 13, 'start')
    f.guide(x0, y0, x0 + 80, y0)
    f.angle(x0, y0, 40, 0, th, anglab, OR, 58, 12.5)
    R = 320.0; S = R * math.tan(math.radians(th)); dh = gy - y0
    pts = [(x0 + R * (i / 44.0), y0 - S * (i / 44.0) + (S + dh) * (i / 44.0) ** 2) for i in range(45)]
    f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % p for p in pts) +
          '" fill="none" stroke="%s" stroke-width="2.2" stroke-dasharray="6 5"/>' % BL)
    f.dim(42, y0, 42, gy, '', PU, 0, 13)
    f.tbg(42 + 36, (y0 + gy) / 2, hlab, PU, 13)
    f.guide(x0, gy, x0, gy + 32); f.guide(x0 + R, gy, x0 + R, gy + 32)
    f.dim(x0, gy + 28, x0 + R, gy + 28, rlab, PU, 0, 13, -7)
    return f.render()


def hose_wall(cap, vlab, anglab, dlab, maxw=440):
    f = Fig(510, 255, cap, maxw)
    gy = 205.0
    f.line(20, gy, 490, gy, DK, 3)
    for x in range(28, 485, 22):
        f.line(x, gy, x - 9, gy + 9, '#94a3b8', 1.6)
    f.rect(400, 40, 62, gy - 40, '#fca5a5', '#991b1b', 2.2, 2)
    for r in range(6):
        f.line(400, 40 + r * 27, 462, 40 + r * 27, '#991b1b', 1.4)
    f.rect(56, gy - 26, 46, 20, '#94a3b8', DK, 2, 4)
    x0, y0, th = 104.0, gy - 22, 40.0
    f.parrow(x0, y0, th, 72, AR, 3.2)
    f.txt(x0 - 6, y0 - 56, vlab, AR, 13, 'end')
    f.guide(x0, y0, x0 + 70, y0)
    f.angle(x0, y0, 38, 0, th, anglab, OR, 56, 12.5)
    R = 400.0; S = R * math.tan(math.radians(th)); dh = 0.0
    pts = [(x0 + R * (i / 44.0), y0 - S * (i / 44.0) + (S + dh) * (i / 44.0) ** 2) for i in range(45)]
    pts = [p for p in pts if p[0] <= 400]
    f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % p for p in pts) +
          '" fill="none" stroke="#38bdf8" stroke-width="2.6" stroke-dasharray="6 5"/>')
    hy = pts[-1][1]
    f.dim(400, y0, 400, hy, '', PU, 0, 13)
    f.tbg(366, (y0 + hy) / 2, 'h = ?', PU, 13)
    f.guide(x0, gy + 6, x0, gy + 34); f.guide(400, gy, 400, gy + 34)
    f.dim(x0, gy + 30, 400, gy + 30, dlab, PU, 0, 13, -7)
    return f.render()


def proj_traj(cap, th, v0lab, anglab, ask=None, show_H=False, show_R=False, show_top=False, maxw=430):
    f = Fig(540, 240, cap, maxw)
    R = 360.0
    H = R * math.tan(math.radians(th)) / 4
    x0, y0 = 85.0, 200.0
    f.line(25, y0, 515, y0, DK, 3)
    for x in range(33, 510, 22):
        f.line(x, y0, x - 9, y0 + 9, '#94a3b8', 1.6)
    pts = [(x0 + R * (i / 48.0), y0 - 4 * H * (i / 48.0) * (1 - i / 48.0)) for i in range(49)]
    f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % p for p in pts) +
          '" fill="none" stroke="%s" stroke-width="2.2" stroke-dasharray="6 5"/>' % BL)
    f.parrow(x0, y0, th, 88, AR, 3.2)
    tp = P(x0, y0, 96, th)
    f.txt(tp[0] + 10, tp[1] - 4, v0lab, AR, 13.5, 'start')
    f.angle(x0, y0, 40, 0, th, anglab, OR, 58, 12.5)
    if show_H:
        ax = x0 + R / 2
        f.guide(ax, y0 - H, x0 - 22, y0 - H)
        f.dim(ax, y0, ax, y0 - H, '', PU, 0, 13)
        f.tbg(ax + 34, y0 - H / 2, 'H = ?', PU, 13)
    if show_top:
        ax = x0 + R / 2
        f.circle(ax, y0 - H, 5.5, AR, AR, 1)
        f.txt(ax, y0 - H - 13, 'P', NV, 13)
    if show_R:
        f.guide(x0, y0 + 6, x0, y0 + 30); f.guide(x0 + R, y0 + 6, x0 + R, y0 + 30)
        f.dim(x0, y0 + 26, x0 + R, y0 + 26, 'R = ?', PU, 0, 13, -7)
    f.circle(x0 + R, y0, 5, AR, AR, 1)
    if ask:
        f.txt(x0 + R / 2, 46, ask, NV, 14)
    return f.render()


def wall_kick(cap, vlab, anglab, dlab, wlab, th=45.0, maxw=440):
    f = Fig(520, 250, cap, maxw)
    gy = 200.0
    f.line(20, gy, 500, gy, DK, 3)
    for x in range(28, 495, 22):
        f.line(x, gy, x - 9, gy + 9, '#94a3b8', 1.6)
    wx = 380.0
    f.rect(wx, gy - 62, 26, 62, '#fca5a5', '#991b1b', 2.2, 2)
    for r in range(4):
        f.line(wx, gy - 62 + r * 16, wx + 26, gy - 62 + r * 16, '#991b1b', 1.3)
    f.tbg(wx + 62, gy - 34, wlab, '#991b1b', 12.5)
    x0 = 90.0
    f.circle(x0, gy - 8, 8, '#f8fafc', DK, 2)
    f.line(x0 - 5, gy - 12, x0 + 5, gy - 4, '#64748b', 1.4)
    R = 430.0
    S = R * math.tan(math.radians(th))
    pts = [(x0 + R * (i / 60.0), gy - S * (i / 60.0) + S * (i / 60.0) ** 2) for i in range(61)]
    pts = [p for p in pts if p[0] <= wx]
    f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % p for p in pts) +
          '" fill="none" stroke="%s" stroke-width="2.2" stroke-dasharray="6 5"/>' % BL)
    f.parrow(x0, gy - 8, th, 76, AR, 3.2)
    f.txt(x0 - 8, gy - 74, vlab, AR, 13.5, 'end')
    f.guide(x0, gy - 8, x0 + 62, gy - 8)
    f.angle(x0, gy - 8, 36, 0, th, anglab, OR, 54, 12.5)
    f.guide(x0, gy + 6, x0, gy + 32); f.guide(wx, gy, wx, gy + 32)
    f.dim(x0, gy + 28, wx, gy + 28, dlab, PU, 0, 13, -7)
    return f.render()

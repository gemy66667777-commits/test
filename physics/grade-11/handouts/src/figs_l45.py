# -*- coding: utf-8 -*-
"""Original figures for Lessons 1-4 (moment of a force) and 1-5 (equilibrium)."""
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV
from figs_lesson import INK, MUT, SKY, VIO, RED, GRN, AMB, IND


def lamp_cable(cap, anglab='25°', maxw=360, w=420, h=280):
    f = Fig(w, h, cap, maxw)
    # ceiling
    f.line(150, 34, w - 24, 34, DK, 3)
    for x in range(160, int(w) - 20, 18):
        f.line(x, 34, x - 8, 26, '#94A3B8', 1.4)
    # wall
    f.rect(44, 60, 26, 190, '#CBD5E1', '#64748B', 2, 3)
    for y in range(70, 240, 18):
        f.line(44, y, 70, y, '#94A3B8', 1.2)
    cx, cy = 320.0, 40.0
    ly = 168.0
    lx = cx - (ly - cy) * math.tan(math.radians(25.0))
    f.line(lx, ly, cx, cy, '#A16207', 3.4)
    f.line(lx, ly, 70, ly, '#0EA5E9', 3)
    f.circle(lx, ly, 22, '#FDE68A', '#B45309', 2.6)
    f.circle(lx, ly, 8, '#FCD34D', '#B45309', 1.6)
    f.parrow(lx, ly + 24, -90, 56, RED, 3)
    f.txt(lx + 12, ly + 92, 'W = mg', RED, 12, 'start')
    ang = math.degrees(math.atan2(ly - cy, cx - lx))
    f.parrow(lx, ly - 6, ang, 74, VIO, 3)
    f.txt(lx + 86, ly - 62, 'T', VIO, 13.5, 'start', it=True)
    f.guide(cx, cy, cx, cy + 96)
    f.angle(cx, cy, 44, 270, 180 + ang, anglab, OR, 66, 12)
    f.parrow(lx - 8, ly, 180, 62, SKY, 3)
    f.txt(lx - 78, ly - 12, 'P', SKY, 13, 'middle', it=True)
    f.txt(w / 2, h - 10, 'a lamp held by a cable and a horizontal rope', MUT, 10.5)
    return f.render()


def lamp_two_cables(cap, anglab='30°', maxw=400, w=460, h=250):
    f = Fig(w, h, cap, maxw)
    f.line(30, 36, w - 30, 36, DK, 3)
    for x in range(40, int(w) - 26, 18):
        f.line(x, 36, x - 8, 28, '#94A3B8', 1.4)
    lx, ly = w / 2.0, 150.0
    for sx in (86.0, w - 86.0):
        f.line(sx, 36, lx, ly, '#A16207', 3.2)
        a = math.degrees(math.atan2(ly - 36, abs(lx - sx))) * (1 if sx < lx else 1)
        d = 180 - a if sx < lx else a
        f.parrow(lx + (-10 if sx < lx else 10), ly - 6, d, 62, VIO, 2.8)
    f.txt(lx - 96, ly - 52, 'T', VIO, 13, 'end', it=True)
    f.txt(lx + 96, ly - 52, 'T', VIO, 13, 'start', it=True)
    f.guide(86, 36, w - 86, 36)
    f.angle(86, 36, 44, 0, -math.degrees(math.atan2(ly - 36, lx - 86)), anglab, OR, 62, 12)
    f.angle(w - 86, 36, 44, 180 + math.degrees(math.atan2(ly - 36, lx - 86)), 180, anglab, OR, 62, 12)
    f.circle(lx, ly, 22, '#FDE68A', '#B45309', 2.6)
    f.circle(lx, ly, 8, '#FCD34D', '#B45309', 1.6)
    f.parrow(lx, ly + 24, -90, 50, RED, 3)
    f.txt(lx + 12, ly + 84, 'W = mg', RED, 12, 'start')
    return f.render()


def sagging_wire(cap, maxw=430, w=500, h=250):
    f = Fig(w, h, cap, maxw)
    gy = 226.0
    f.line(20, gy, w - 20, gy, DK, 2.6)
    for x in range(28, int(w) - 24, 20):
        f.line(x, gy, x - 8, gy + 8, '#94A3B8', 1.4)
    for px in (96.0, w - 96.0):
        f.rect(px - 9, 54, 18, gy - 54, '#B45309', '#7C2D12', 2, 2)
    top = 60.0
    mid = w / 2.0
    sag = 132.0
    pts = [(96 + (w - 192) * (i / 40.0),
            top + 4 * (sag - top) * (i / 40.0) * (1 - i / 40.0)) for i in range(41)]
    f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % p for p in pts) +
          '" fill="none" stroke="#475569" stroke-width="2.6"/>')
    for px, ang in ((96.0, -52.0), (w - 96.0, 180 + 52.0)):
        f.parrow(px, top + 2, ang, 60, VIO, 3)
    f.txt(142, top + 88, 'T', VIO, 13, 'start', it=True)
    f.txt(w - 120, top + 66, 'T', VIO, 13, 'end', it=True)
    f.guide(96, top, 96, top + 92)
    f.angle(96, top, 46, 270, 308, 'θ', OR, 66, 12.5)
    f.parrow(mid, sag + 4, -90, 48, RED, 3)
    f.txt(mid + 12, sag + 66, 'W = mg', RED, 12, 'start')
    f.txt(w / 2, h - 8, 'the more the wire sags, the smaller the tension T', MUT, 10.5)
    return f.render()


def tension_components(cap, maxw=340, w=390, h=270):
    f = Fig(w, h, cap, maxw)
    ox, oy = 210.0, 170.0
    f.line(ox, oy, ox + 130, oy - 96, '#A16207', 3.2)
    f.line(ox, oy, ox - 120, oy - 88, '#A16207', 3.2)
    ang = math.degrees(math.atan2(96, 130))
    f.arrow(ox, oy, ox + 96, oy - 71, VIO, 3)
    f.txt(ox + 104, oy - 76, 'T', VIO, 13.5, 'start', it=True)
    f.parrow(ox, oy, 90, 71, SKY, 2.8, '5 4')
    f.parrow(ox, oy, 0, 96, GRN, 2.8, '5 4')
    f.guide(ox, oy - 71, ox + 96, oy - 71); f.guide(ox + 96, oy, ox + 96, oy - 71)
    f.tbg(ox - 34, oy - 44, 'T sin θ', SKY, 12)
    f.txt(ox + 48, oy + 22, 'T cos θ', GRN, 12)
    f.angle(ox, oy, 44, 0, ang, 'θ', OR, 62, 12.5)
    f.parrow(ox, oy + 6, -90, 58, RED, 3)
    f.txt(ox + 12, oy + 78, 'W = mg', RED, 12, 'start')
    f.circle(ox, oy, 4.5, INK, INK, 1)
    return f.render()


def ruler_coins(cap, right_cm=15, left_cm=5, n=3, maxw=450, w=520, h=220):
    f = Fig(w, h, cap, maxw)
    y = 120.0
    cx = w / 2.0
    S = 9.5
    f.rect(cx - 210, y - 9, 420, 18, '#E2E8F0', '#64748B', 2, 3)
    for k in range(-20, 21, 5):
        x = cx + k * S
        f.line(x, y - 9, x, y - 2, '#94A3B8', 1.2)
    f.poly([(cx, y + 9), (cx - 15, y + 34), (cx + 15, y + 34)], '#CBD5E1', DK, 2.2)
    f.line(cx - 26, y + 34, cx + 26, y + 34, DK, 2.4)
    rx = cx + right_cm * S
    f.circle(rx, y - 20, 10, '#FCD34D', '#B45309', 2)
    f.txt(rx, y - 36, '1 coin', AMB, 11)
    for i in range(n):
        f.circle(cx - left_cm * S, y - 20 - i * 15, 10, '#FCD34D', '#B45309', 2)
    f.txt(cx - left_cm * S, y - 36 - (n - 1) * 15, 'n coins', AMB, 11)
    f.guide(rx, y + 10, rx, y + 62); f.guide(cx, y + 36, cx, y + 62)
    f.guide(cx - left_cm * S, y + 10, cx - left_cm * S, y + 62)
    f.dim(cx, y + 58, rx, y + 58, '%d cm' % right_cm, PU, 0, 11.5, -6)
    f.dim(cx - left_cm * S, y + 58, cx, y + 58, '%d cm' % left_cm, PU, 0, 11.5, -6)
    return f.render()


def points_line(cap, dA='4.0 m', dB='3.0 m', ang=60.0, flab='F = 4.0 N', maxw=460, w=540, h=220):
    f = Fig(w, h, cap, maxw)
    y = 140.0
    f.guide(40, y, w - 30, y, '#94A3B8', 1.8, '8 6')
    ax, bx, px = 70.0, 300.0, 440.0
    for x, lab in ((ax, 'A'), (bx, 'B')):
        f.circle(x, y, 6, INK, INK, 1)
        f.txt(x, y + 26, lab, INK, 13, 'middle', it=True)
    f.circle(px, y, 6, RED, RED, 1)
    f.txt(px, y + 26, 'point of application', MUT, 10.5)
    tip = P(px, y, 86, ang)
    f.arrow(px, y, tip[0], tip[1], RED, 3.2)
    f.txt(tip[0] + 8, tip[1] - 2, flab, RED, 12.5, 'start')
    f.angle(px, y, 36, 0, ang, '%g°' % ang, OR, 54, 12)
    f.dim(ax, y + 56, px, y + 56, dA, PU, 0, 12, -6)
    f.dim(bx, y + 84, px, y + 84, dB, PU, 0, 12, -6)
    for x in (ax, bx, px):
        f.guide(x, y + 8, x, y + 90)
    return f.render()


def rod_slide(cap, maxw=430, w=500, h=220):
    f = Fig(w, h, cap, maxw)
    y = 110.0
    f.circle(70, y, 8, INK, INK, 1.6)
    f.txt(70, y + 26, 'O', INK, 13, 'middle', it=True)
    f.rod(70, y, 430, y, '#0F766E', 9)
    f.parrow(330, y - 6, 90, 62, RED, 3.2)
    f.txt(330, y - 80, 'F = 3.0 N', RED, 12.5)
    f.dim(70, y + 44, 330, y + 44, 'd = 0.20 m', PU, 0, 12, -6)
    f.guide(70, y + 12, 70, y + 48); f.guide(330, y + 10, 330, y + 48)
    f.arc(240, y - 28, 46, 20, 160, MUT, 2, dash='5 4', arrowhead=True)
    f.txt(176, y - 88, 'the force slides towards O', MUT, 10.5)
    return f.render()

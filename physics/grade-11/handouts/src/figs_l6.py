# -*- coding: utf-8 -*-
"""Original figures for Lesson 1-6 (power & efficiency) and the equilibrium review."""
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV
from figs_lesson import INK, MUT, SKY, VIO, RED, GRN, AMB, IND


def two_lifts(cap, maxw=430, w=500, h=280):
    f = Fig(w, h, cap, maxw)
    for k, (x0, t) in enumerate(((70.0, 't = 24 s'), (290.0, 't = 12 s'))):
        f.rect(x0, 44, 140, 186, '#F8FAFC', '#64748B', 2.4, 4)
        f.rect(x0 + 34, 158, 72, 56, '#FCD34D', '#B45309', 2.4, 3)
        f.txt(x0 + 70, 192, '600 kg', '#7C2D12', 12.5)
        f.dim(x0 + 18, 214, x0 + 18, 58, '', PU, 0, 11.5)
        f.tbg(x0 + 18, 136, 'h = 9.0 m', PU, 11.5)
        f.txt(x0 + 70, 30, 'lift ' + 'AB'[k], INK, 13)
        f.txt(x0 + 70, 252, t, IND, 12.5)
        f.parrow(x0 + 120, 150, 90, 56, GRN, 2.6)
    f.txt(w / 2, h - 8, 'the same load raised to the same height in different times', MUT, 10.5)
    return f.render()


def block_force_angle(cap, maxw=380, w=440, h=250):
    f = Fig(w, h, cap, maxw)
    gy = 186.0
    f.line(20, gy, w - 20, gy, DK, 2.6)
    for x in range(28, int(w) - 24, 20):
        f.line(x, gy, x - 8, gy + 8, '#94A3B8', 1.4)
    bx = 120.0
    f.rect(bx - 46, gy - 40, 92, 40, '#C7D2FE', '#4338CA', 2.4, 4)
    f.parrow(bx + 52, gy - 20, 0, 92, IND, 3.2)
    f.txt(bx + 150, gy - 28, 'v  (direction of motion)', IND, 12, 'start')
    th = 38.0
    f.parrow(bx, gy - 44, th, 104, RED, 3.2)
    tp = P(bx, gy - 44, 116, th)
    f.txt(tp[0] + 8, tp[1] + 2, 'F', RED, 14, 'start', it=True)
    f.guide(bx, gy - 44, bx + 120, gy - 44)
    f.angle(bx, gy - 44, 44, 0, th, 'θ', OR, 64, 13)
    return f.render()


def three_forces(cap, f1='F₁ = 10 N', f2='F₂ = 6 N', f3='F₃ = ?', maxw=300, w=340, h=280):
    f = Fig(w, h, cap, maxw)
    cx, cy = w / 2.0, 140.0
    f.rect(cx - 44, cy - 30, 88, 60, '#E0E7FF', '#4338CA', 2.4, 6)
    f.parrow(cx, cy - 34, 90, 74, GRN, 3.2)
    f.txt(cx + 12, cy - 92, f1, GRN, 12.5, 'start')
    f.parrow(cx - 18, cy + 34, -90, 62, RED, 3.2)
    f.txt(cx - 30, cy + 86, f2, RED, 12.5, 'end')
    f.parrow(cx + 18, cy + 34, -90, 62, VIO, 3.2, '6 4')
    f.txt(cx + 30, cy + 110, f3, VIO, 12.5, 'start')
    f.txt(w / 2, h - 10, 'the body stays in equilibrium', MUT, 10.5)
    return f.render()


def two_springs(cap, anglab='40°', maxw=340, w=400, h=310):
    f = Fig(w, h, cap, maxw)
    f.line(40, 38, w - 40, 38, DK, 3)
    for x in range(48, int(w) - 34, 18):
        f.line(x, 38, x - 8, 30, '#94A3B8', 1.4)
    mx, my = w / 2.0, 186.0
    for sx in (110.0, w - 110.0):
        n, x1, y1, x2, y2 = 9, sx, 38.0, mx, my
        pts = []
        for i in range(n * 2 + 1):
            t = i / float(n * 2)
            px = x1 + (x2 - x1) * t
            py = y1 + (y2 - y1) * t
            nx = -(y2 - y1); ny = (x2 - x1)
            L = math.hypot(nx, ny)
            s = 7 if i % 2 else -7
            if i in (0, n * 2):
                s = 0
            pts.append((px + nx / L * s, py + ny / L * s))
        f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % p for p in pts) +
              '" fill="none" stroke="#475569" stroke-width="2.2"/>')
        a = math.degrees(math.atan2(my - 38, abs(mx - sx)))
        d = a if sx > mx else 180 - a
        f.parrow(mx + (10 if sx > mx else -10), my - 10, d, 60, VIO, 2.8)
    f.txt(mx - 74, my - 66, 'F', VIO, 13, 'end', it=True)
    f.txt(mx + 74, my - 66, 'F', VIO, 13, 'start', it=True)
    f.guide(110, 38, 110, 120)
    _a = (-math.degrees(math.atan2(my - 38, mx - 110))) % 360
    f.angle(110, 38, 44, 270, _a, anglab, OR, 64, 12)
    f.rect(mx - 34, my, 68, 40, '#94A3B8', '#334155', 2.4, 4)
    f.txt(mx, my + 26, '1.5 kg', '#0F172A', 12)
    f.parrow(mx, my + 44, -90, 48, RED, 3)
    f.txt(mx + 12, my + 102, 'W = mg', RED, 12, 'start')
    return f.render()


def lamp_wall(cap, plab='P = 15 N', wlab='W = 39.2 N', anglab='θ', maxw=360, w=420, h=280):
    f = Fig(w, h, cap, maxw)
    f.line(150, 34, w - 24, 34, DK, 3)
    for x in range(160, int(w) - 20, 18):
        f.line(x, 34, x - 8, 26, '#94A3B8', 1.4)
    f.rect(44, 60, 26, 190, '#CBD5E1', '#64748B', 2, 3)
    for y in range(70, 240, 18):
        f.line(44, y, 70, y, '#94A3B8', 1.2)
    cx, cy = 320.0, 40.0
    ly = 172.0
    lx = cx - (ly - cy) * math.tan(math.radians(22.0))
    f.line(lx, ly, cx, cy, '#A16207', 3.4)
    f.line(lx, ly, 70, ly, '#0EA5E9', 3)
    f.circle(lx, ly, 22, '#FDE68A', '#B45309', 2.6)
    f.circle(lx, ly, 8, '#FCD34D', '#B45309', 1.6)
    f.parrow(lx, ly + 24, -90, 54, RED, 3)
    f.txt(lx + 12, ly + 90, wlab, RED, 12, 'start')
    ang = math.degrees(math.atan2(ly - cy, cx - lx))
    f.parrow(lx, ly - 6, ang, 74, VIO, 3)
    f.txt(lx + 84, ly - 58, 'T', VIO, 13.5, 'start', it=True)
    f.guide(cx, cy, cx, cy + 110)
    f.angle(cx, cy, 44, 270, 180 + ang, anglab, OR, 64, 12.5)
    f.parrow(lx - 8, ly, 180, 62, SKY, 3)
    f.txt(lx - 78, ly - 12, plab, SKY, 12, 'middle')
    return f.render()


def cables_components(cap, maxw=380, w=440, h=290):
    f = Fig(w, h, cap, maxw)
    f.line(30, 36, w - 30, 36, DK, 3)
    for x in range(38, int(w) - 26, 18):
        f.line(x, 36, x - 8, 28, '#94A3B8', 1.4)
    mx, my = w / 2.0, 170.0
    for sx, lab, side in ((78.0, 'θ₁', -1), (w - 78.0, 'θ₂', 1)):
        f.line(sx, 36, mx, my, '#A16207', 3.2)
        a = math.degrees(math.atan2(my - 36, abs(mx - sx)))
        if side < 0:
            f.angle(sx, 36, 40, 0, -a, lab, OR, 58, 12)
        else:
            f.angle(sx, 36, 40, 180, 180 + a, lab, OR, 58, 12)
    f.parrow(mx, my - 12, 90, 74, VIO, 3)
    f.txt(mx + 10, my - 96, 'T₁y + T₂y', VIO, 12, 'start')
    f.parrow(mx - 12, my, 180, 74, GRN, 3)
    f.parrow(mx + 12, my, 0, 74, GRN, 3)
    f.txt(mx - 92, my - 10, 'T₁x', GRN, 12, 'end')
    f.txt(mx + 92, my - 10, 'T₂x', GRN, 12, 'start')
    f.circle(mx, my, 20, '#FDE68A', '#B45309', 2.6)
    f.parrow(mx, my + 22, -90, 52, RED, 3)
    f.txt(mx + 12, my + 84, 'W = mg', RED, 12, 'start')
    return f.render()


def sign_cables(cap, a1=35.0, a2=65.0, mlab='10 kg', maxw=420, w=490, h=300):
    f = Fig(w, h, cap, maxw)
    f.line(40, 40, w - 40, 40, '#7C2D12', 5)
    mx, my = 250.0, 176.0
    for sx, a, lab in ((88.0, a1, 'T₁'), (w - 78.0, a2, 'T₂')):
        f.line(sx, 40, mx, my, '#A16207', 3)
        ang = math.degrees(math.atan2(my - 40, abs(mx - sx)))
        d = 180 - ang if sx < mx else ang
        f.parrow(mx + (-10 if sx < mx else 10), my - 12, d, 62, VIO, 2.8)
        f.txt(sx + (14 if sx < mx else -14), 60, lab, VIO, 12.5, 'start' if sx < mx else 'end', it=True)
        f.guide(sx, 40, sx + (90 if sx < mx else -90), 40)
        if sx < mx:
            f.angle(sx, 40, 38, 0, -ang, '%g°' % a, OR, 56, 12)
        else:
            f.angle(sx, 40, 38, 180, 180 + ang, '%g°' % a, OR, 56, 12)
    f.rect(mx - 58, my, 116, 44, '#FCD34D', '#B45309', 2.4, 4)
    f.txt(mx, my + 29, mlab, '#7C2D12', 13)
    f.parrow(mx, my + 48, -90, 46, RED, 3)
    f.txt(mx + 12, my + 104, 'W = mg', RED, 12, 'start')
    return f.render()


def book_table(cap, two=False, maxw=340, w=400, h=250):
    f = Fig(w, h, cap, maxw)
    ty = 150.0
    f.rect(48, ty, w - 96, 20, '#92400E', '#7C2D12', 2.2, 3)
    f.rect(78, ty + 20, 16, 62, '#92400E', '#7C2D12', 2, 2)
    f.rect(w - 94, ty + 20, 16, 62, '#92400E', '#7C2D12', 2, 2)
    bx = w / 2.0
    f.rect(bx - 56, ty - 30, 112, 30, '#3730A3', '#1E1B4B', 2.2, 3)
    if two:
        f.rect(bx - 56, ty - 60, 112, 30, '#4F46E5', '#1E1B4B', 2.2, 3)
    top = ty - (60 if two else 30)
    f.parrow(bx, top - 6, 90, 56, GRN, 3.2)
    f.txt(bx, top - 72, 'F(N)', GRN, 12.5)
    f.parrow(bx, ty + 22, -90, 52, RED, 3.2)
    f.txt(bx, ty + 92, 'W = mg', RED, 12.5)
    return f.render()

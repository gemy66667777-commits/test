# -*- coding: utf-8 -*-
"""Original figures for Lesson 1-11 : horizontal and vertical circular motion."""
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV
from figs_lesson import INK, MUT, SKY, VIO, RED, GRN, AMB, IND


def conical_pendulum(cap, llab='l', anglab='θ', mlab='m', comps=True, maxw=380, w=440, h=330):
    f = Fig(w, h, cap, maxw)
    cx, cy = 220.0, 44.0
    th = 32.0
    L = 168.0
    bx = cx + L * math.sin(math.radians(th))
    by = cy + L * math.cos(math.radians(th))
    f.line(96, cy, w - 60, cy, DK, 3)
    for x in range(106, int(w) - 56, 18):
        f.line(x, cy, x - 8, cy - 8, '#94A3B8', 1.4)
    f.raw('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="26" fill="none" stroke="#94A3B8" stroke-width="1.8" '
          'stroke-dasharray="7 6"/>' % (cx, by, bx - cx))
    f.guide(cx, cy, cx, by + 34)
    f.line(cx, cy, bx, by, '#A16207', 2.8)
    f.circle(bx, by, 16, '#FCD34D', '#B45309', 2.6)
    f.txt(bx + 24, by + 8, mlab, INK, 12.5, 'start')
    f.angle(cx, cy, 52, 270, 270 + th, anglab, OR, 72, 13)
    f.tbg((cx + bx) / 2 + 52, (cy + by) / 2 - 24, llab, PU, 12)
    ang = math.degrees(math.atan2(by - cy, bx - cx))
    f.parrow(bx, by - 10, 180 - ang, 96, VIO, 3)
    f.txt(bx - 96, by - 84, 'T', VIO, 13.5, 'end', it=True)
    if comps:
        f.parrow(bx, by - 10, 90, 84, SKY, 2.6, '5 4')
        f.parrow(bx, by - 10, 180, 60, GRN, 2.6, '5 4')
        f.tbg(bx + 40, by - 94, 'T cos θ', SKY, 11.5)
        f.tbg(bx - 32, by - 26, 'T sin θ', GRN, 11.5)
    f.parrow(bx, by + 16, -90, 56, RED, 3)
    f.txt(bx + 12, by + 84, 'W = mg', RED, 12, 'start')
    f.dim(cx, by + 40, bx, by + 40, 'r', PU, 0, 12, -6)
    return f.render()


def conical_vessel(cap, anglab='θ', maxw=400, w=460, h=310):
    f = Fig(w, h, cap, maxw)
    ax, ay = 230.0, 262.0
    half = 34.0
    top = 60.0
    dx = (ay - top) * math.tan(math.radians(half))
    f.line(ax - dx, top, ax, ay, '#64748B', 3)
    f.line(ax + dx, top, ax, ay, '#64748B', 3)
    f.raw('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="22" fill="none" stroke="#94A3B8" stroke-width="2.4"/>'
          % (ax, top, dx))
    hb = 148.0
    by = ay - hb
    rb = hb * math.tan(math.radians(half))
    f.raw('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="16" fill="none" stroke="#94A3B8" stroke-width="1.8" '
          'stroke-dasharray="7 6"/>' % (ax, by, rb))
    f.circle(ax + rb, by, 14, '#FCD34D', '#B45309', 2.4)
    f.guide(ax, top - 26, ax, ay + 10)
    f.angle(ax, ay, 56, 90, 90 - half, anglab, OR, 76, 12.5)
    nang = 90 - half - 90
    f.parrow(ax + rb - 8, by - 4, 180 - half, 86, VIO, 3)
    f.txt(ax + rb - 104, by - 52, 'N', VIO, 13.5, 'end', it=True)
    f.parrow(ax + rb, by + 16, -90, 52, RED, 3)
    f.txt(ax + rb + 12, by + 80, 'W = mg', RED, 12, 'start')
    f.dim(ax, by + 30, ax + rb, by + 30, 'r', PU, 0, 12, -6)
    f.dim(ax - 64, ay, ax - 64, by, '', PU, 0, 12)
    f.tbg(ax - 64, (ay + by) / 2, 'h', PU, 12.5)
    f.guide(ax - 70, by, ax - rb, by); f.guide(ax - 70, ay, ax - 16, ay)
    return f.render()


def vertical_circle(cap, rlab='r', vtop='v(top)', vbot='v(bottom)', maxw=360, w=420, h=360):
    f = Fig(w, h, cap, maxw)
    cx, cy, R = 210.0, 176.0, 116.0
    f.raw('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="#94A3B8" stroke-width="2" '
          'stroke-dasharray="7 6"/>' % (cx, cy, R))
    f.circle(cx, cy, 5, INK, INK, 1)
    f.txt(cx - 12, cy + 6, 'O', INK, 12.5, 'end', it=True)
    f.dim(cx, cy, cx + R, cy, '', PU, 0, 12)
    f.tbg(cx + R / 2, cy - 14, rlab, PU, 12)
    # top
    tp = (cx, cy - R)
    f.line(cx, cy, tp[0], tp[1], '#A16207', 2.4)
    f.circle(tp[0], tp[1], 13, '#FCD34D', '#B45309', 2.4)
    f.parrow(tp[0] + 14, tp[1], 0, 54, IND, 2.8)
    f.txt(tp[0] + 74, tp[1] - 8, vtop, IND, 12, 'start')
    f.parrow(tp[0], tp[1] + 14, -90, 40, RED, 2.6)
    f.parrow(tp[0] - 22, tp[1] + 14, -90, 30, VIO, 2.6)
    f.tbg(tp[0] - 52, tp[1] + 42, 'T', VIO, 12)
    f.tbg(tp[0] + 26, tp[1] + 52, 'mg', RED, 12)
    # bottom
    bp = (cx, cy + R)
    f.line(cx, cy, bp[0], bp[1], '#A16207', 2.4)
    f.circle(bp[0], bp[1], 13, '#FCD34D', '#B45309', 2.4)
    f.parrow(bp[0] - 14, bp[1], 180, 54, IND, 2.8)
    f.txt(bp[0] - 74, bp[1] - 8, vbot, IND, 12, 'end')
    f.parrow(bp[0], bp[1] - 14, 90, 44, VIO, 2.6)
    f.tbg(bp[0] + 24, bp[1] - 52, 'T', VIO, 12)
    f.parrow(bp[0] + 22, bp[1] + 14, -90, 34, RED, 2.6)
    f.tbg(bp[0] + 54, bp[1] + 40, 'mg', RED, 12)
    f.txt(w / 2, h - 10, 'at the top both forces point towards the centre', MUT, 10.5)
    return f.render()


def bucket_water(cap, maxw=340, w=400, h=330):
    f = Fig(w, h, cap, maxw)
    cx, cy, R = 200.0, 180.0, 106.0
    f.raw('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="#94A3B8" stroke-width="2" '
          'stroke-dasharray="7 6"/>' % (cx, cy, R))
    f.circle(cx, cy, 5, INK, INK, 1)
    # bucket upside down at the top
    tx, ty = cx, cy - R
    f.raw('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="#CBD5E1" stroke="#475569" '
          'stroke-width="2.4"/>' % (tx - 30, ty - 30, tx + 30, ty - 30, tx + 22, ty + 4, tx - 22, ty + 4))
    f.raw('<path d="M%.1f,%.1f q 22,-12 44,0" fill="none" stroke="#1D4ED8" stroke-width="2.2"/>'
          % (tx - 22, ty - 4))
    f.raw('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="#BFDBFE" stroke="none"/>'
          % (tx - 21, ty - 4, tx + 21, ty - 4, tx + 16, ty + 3, tx - 16, ty + 3))
    f.line(cx, cy, tx, ty - 30, '#A16207', 2.6)
    f.txt(tx + 52, ty + 30, 'the bucket is upside down', MUT, 10.5, 'start')
    f.parrow(tx + 34, ty - 12, 0, 40, IND, 2.6)
    f.arc(cx, cy, R + 26, 200, 260, MUT, 2, arrowhead=True)
    f.parrow(tx, ty + 10, -90, 40, RED, 2.8)
    f.tbg(tx + 26, ty + 48, 'mg', RED, 12)
    f.txt(w / 2, h - 12, 'if v ≥ √(g r) the water keeps its circular path', MUT, 10.5)
    return f.render()


def loop_track(cap, maxw=440, w=500, h=300):
    f = Fig(w, h, cap, maxw)
    gy = 262.0
    f.line(20, gy, w - 20, gy, '#475569', 3.4)
    for x in range(28, int(w) - 24, 22):
        f.line(x, gy, x - 8, gy + 8, '#94A3B8', 1.4)
    cx, cy, R = 250.0, 150.0, 104.0
    f.raw('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="#64748B" stroke-width="6"/>'
          % (cx, cy, R))
    f.raw('<path d="M20,%d Q 120,%d %.1f,%.1f" fill="none" stroke="#64748B" stroke-width="6"/>'
          % (int(gy - 4), int(gy - 4), cx - R + 6, cy + R - 10))
    f.raw('<path d="M%.1f,%.1f Q %d,%d %d,%d" fill="none" stroke="#64748B" stroke-width="6"/>'
          % (cx + R - 6, cy + R - 10, int(w) - 120, int(gy - 4), int(w) - 20, int(gy - 4)))
    tp = (cx, cy - R)
    f.rect(tp[0] - 22, tp[1] - 4, 44, 18, '#EF4444', '#991B1B', 2.2, 4)
    f.circle(tp[0] - 12, tp[1] + 16, 5, '#334155', DK, 1.6)
    f.circle(tp[0] + 12, tp[1] + 16, 5, '#334155', DK, 1.6)
    f.parrow(tp[0] + 26, tp[1] + 6, 0, 46, IND, 2.6)
    f.txt(tp[0] + 80, tp[1] - 4, 'v (top)', IND, 12, 'start')
    f.parrow(tp[0], tp[1] + 22, -90, 36, RED, 2.6)
    f.tbg(tp[0] - 32, tp[1] + 56, 'mg', RED, 12)
    f.parrow(tp[0] - 26, tp[1] + 22, -90, 26, VIO, 2.6)
    f.tbg(tp[0] - 70, tp[1] + 40, 'N', VIO, 12)
    bp = (cx, cy + R)
    f.parrow(bp[0], bp[1] - 14, 90, 42, VIO, 2.8)
    f.tbg(bp[0] + 30, bp[1] - 46, 'N', VIO, 12)
    f.txt(w / 2, 30, 'at the top N + mg supplies the centripetal force', MUT, 10.5)
    return f.render()


def semicircle_path(cap, maxw=340, w=400, h=290):
    f = Fig(w, h, cap, maxw)
    cx, cy, R = 200.0, 210.0, 116.0
    f.raw('<path d="M %.1f,%.1f A %.1f,%.1f 0 0 1 %.1f,%.1f" fill="none" stroke="#94A3B8" '
          'stroke-width="2.4" stroke-dasharray="7 6"/>' % (cx - R, cy, R, R, cx + R, cy))
    f.line(cx - R - 26, cy, cx + R + 26, cy, DK, 2.6)
    f.circle(cx - R, cy - 12, 12, '#38BDF8', '#0369A1', 2.4)
    f.txt(cx - R, cy + 24, 'A', INK, 13, 'middle', it=True)
    f.parrow(cx - R + 16, cy - 12, 0, 54, RED, 3)
    f.txt(cx - R + 44, cy - 28, 'v₀', RED, 13, 'start')
    bp = P(cx, cy, R, 52)
    f.circle(bp[0], bp[1], 10, '#FCD34D', '#B45309', 2.2)
    f.txt(bp[0] + 16, bp[1] - 10, 'B', INK, 13, 'start', it=True)
    f.circle(cx, cy - R, 10, '#FCD34D', '#B45309', 2.2)
    f.txt(cx - 6, cy - R - 16, 'C', INK, 13, 'end', it=True)
    f.dim(cx, cy, bp[0], bp[1], '', PU, 0, 12)
    f.tbg((cx + bp[0]) / 2 + 18, (cy + bp[1]) / 2 + 10, 'r', PU, 12)
    f.circle(cx, cy, 4.5, INK, INK, 1)
    f.angle(cx, cy, 44, 90, 52, 'θ', OR, 62, 12)
    f.guide(cx, cy, cx, cy - R - 12)
    return f.render()

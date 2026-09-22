# -*- coding: utf-8 -*-
"""Original figures for Lesson 1-2 : horizontal projectiles."""
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV
from figs_lesson import INK, MUT, SKY, VIO, RED, GRN, AMB, IND


def _hpar(f, x0, y0, R, H, c=IND, w=2.2, dash='6 5'):
    pts = [(x0 + R * (i / 44.0), y0 + H * (i / 44.0) ** 2) for i in range(45)]
    f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % p for p in pts) +
          '" fill="none" stroke="%s" stroke-width="%s" stroke-dasharray="%s"/>' % (c, w, dash))
    return pts


def cannon_path(cap, maxw=470, w=560, h=300):
    f = Fig(w, h, cap, maxw)
    gy = 262.0
    f.line(20, gy, w - 20, gy, DK, 2.6)
    for x in range(28, int(w) - 24, 20):
        f.line(x, gy, x - 8, gy + 8, '#94A3B8', 1.4)
    # cliff block
    f.rect(36, 74, 104, gy - 74, '#E9E4F5', '#8B7FB8', 2.2, 4)
    # cannon
    f.rect(58, 56, 52, 18, '#475569', '#1E293B', 2, 5)
    f.raw('<g transform="translate(110,60) rotate(0)"><rect x="0" y="-7" width="40" height="14" rx="4" '
          'fill="#334155" stroke="#0F172A" stroke-width="2"/></g>')
    f.circle(76, 78, 13, '#94A3B8', '#1E293B', 2.4)
    x0, y0 = 152.0, 60.0
    f.parrow(x0, y0, 0, 62, RED, 3)
    f.txt(x0 + 74, y0 - 9, 'v (initial)', RED, 12, 'start')
    pts = _hpar(f, x0, y0, 330, gy - y0)
    for k, idx in enumerate((11, 22, 33)):
        px, py = pts[idx]
        f.circle(px, py, 5.5, RED, RED, 1)
        f.txt(px - 12, py - 9, str(k + 1), INK, 12.5, 'end')
    f.circle(x0, y0, 5, INK, INK, 1)
    f.txt(x0 - 4, y0 - 18, 'A', INK, 12.5, 'end', it=True)
    bx, by = pts[-1]
    f.circle(bx, by, 5.5, INK, INK, 1)
    f.txt(bx + 10, by - 8, 'B', INK, 12.5, 'start', it=True)
    f.circle(x0, by, 5, MUT, MUT, 1)
    f.txt(x0 - 10, by + 6, 'C', MUT, 12.5, 'end', it=True)
    f.guide(x0, y0, x0, by + 6)
    f.guide(x0, by, bx, by)
    f.dim(x0, by + 26, bx, by + 26, 'horizontal distance', PU, 0, 11.5, -7)
    f.tbg(x0 + 52, (y0 + by) / 2 - 7, 'vertical', PU, 11.5)
    f.tbg(x0 + 52, (y0 + by) / 2 + 8, 'distance', PU, 11.5)
    f.dim(x0 - 16, y0, x0 - 16, by, '', PU, 0, 11.5)
    return f.render()


def cliff_drop(cap, hlab, vlab, rlab='x = ?', maxw=420, w=500, h=250, block='#E2E8F0'):
    f = Fig(w, h, cap, maxw)
    gy = h - 52.0
    f.line(20, gy, w - 20, gy, DK, 2.6)
    for x in range(28, int(w) - 24, 20):
        f.line(x, gy, x - 8, gy + 8, '#94A3B8', 1.4)
    bx, by = 40.0, 62.0
    f.rect(bx, by, 98, gy - by, block, '#94A3B8', 2.2, 4)
    x0, y0 = bx + 98, by - 4
    f.circle(x0, y0, 7, RED, '#7F1D1D', 1.6)
    f.parrow(x0 + 10, y0, 0, 58, RED, 3)
    f.txt(x0 + 76, y0 - 9, vlab, RED, 12, 'start')
    _hpar(f, x0, y0, w - x0 - 70, gy - y0)
    f.dim(bx + 20, by, bx + 20, gy, '', PU, 0, 12)
    f.tbg(bx + 56, (by + gy) / 2, hlab, PU, 12)
    f.guide(x0, gy, x0, gy + 30)
    f.guide(w - 70, gy, w - 70, gy + 30)
    f.dim(x0, gy + 26, w - 70, gy + 26, rlab, PU, 0, 12, -7)
    return f.render()


def two_heights(cap, h1, v1, h2, v2, maxw=470, w=560, h=290):
    f = Fig(w, h, cap, maxw)
    gy = 238.0
    f.line(18, gy, w - 18, gy, DK, 2.6)
    for x in range(26, int(w) - 22, 20):
        f.line(x, gy, x - 8, gy + 8, '#94A3B8', 1.4)
    for (bx, top, hl, vl, col, nm) in ((36.0, 150.0, h1, v1, IND, '1'), (300.0, 52.0, h2, v2, RED, '2')):
        f.rect(bx, top, 74, gy - top, '#EEF2F7', '#94A3B8', 2, 4)
        x0, y0 = bx + 74, top - 4
        f.circle(x0, y0, 6, col, col, 1)
        f.parrow(x0 + 8, y0, 0, 46, col, 2.8)
        f.txt(x0 + 58, y0 - 8, vl, col, 11.5, 'start')
        _hpar(f, x0, y0, 150, gy - y0, col)
        f.dim(bx + 16, top, bx + 16, gy, '', PU, 0, 11.5)
        f.tbg(bx + 46, (top + gy) / 2, hl, PU, 11.5)
        f.txt(bx + 37, gy + 34, 'projectile ' + nm, col, 11.5)
    return f.render()


def building_floors(cap, maxw=330, w=380, h=320):
    f = Fig(w, h, cap, maxw)
    gy = 290.0
    f.line(14, gy, w - 14, gy, DK, 2.6)
    for x in range(22, int(w) - 18, 18):
        f.line(x, gy, x - 7, gy + 7, '#94A3B8', 1.4)
    bx, bw = 60.0, 116.0
    top = 30.0
    fh = (gy - top) / 10.0
    f.rect(bx, top, bw, gy - top, '#EEF2F7', '#94A3B8', 2.2, 4)
    for k in range(10):
        y = gy - (k + 1) * fh
        f.line(bx, y, bx + bw, y, '#CBD5E1', 1.2)
        for c in range(3):
            f.rect(bx + 14 + c * 32, y + 7, 20, fh - 15, '#DBEAFE', '#93C5FD', 1.2, 2)
    for k, col, lab in ((3, IND, '4th floor'), (9, RED, '10th floor')):
        y = gy - (k + 1) * fh + fh / 2
        f.parrow(bx + bw + 4, y, 0, 42, col, 2.8)
        f.txt(bx + bw + 52, y - 7, lab, col, 11.5, 'start')
        _hpar(f, bx + bw + 4, y, 150, gy - y, col, 1.9)
    return f.render()


def helicopter(cap, maxw=440, w=520, h=260):
    f = Fig(w, h, cap, maxw)
    gy = 214.0
    f.line(18, gy, w - 18, gy, DK, 2.6)
    for x in range(26, int(w) - 22, 20):
        f.line(x, gy, x - 8, gy + 8, '#94A3B8', 1.4)
    hx, hy = 116.0, 60.0
    f.raw('<g transform="translate(%.1f,%.1f)">'
          '<ellipse cx="0" cy="0" rx="34" ry="19" fill="#CBD5E1" stroke="#475569" stroke-width="2"/>'
          '<path d="M26,-4 L78,-9 L78,1 L28,6 Z" fill="#CBD5E1" stroke="#475569" stroke-width="2"/>'
          '<path d="M72,-9 L84,-24 L88,-22 L80,-6 Z" fill="#CBD5E1" stroke="#475569" stroke-width="2"/>'
          '<ellipse cx="-14" cy="-3" rx="12" ry="9" fill="#BAE6FD" stroke="#0369A1" stroke-width="1.6"/>'
          '<line x1="-46" y1="-24" x2="46" y2="-24" stroke="#334155" stroke-width="3.4"/>'
          '<line x1="0" y1="-24" x2="0" y2="-19" stroke="#334155" stroke-width="3"/>'
          '<line x1="-22" y1="20" x2="24" y2="20" stroke="#334155" stroke-width="3"/>'
          '<line x1="-14" y1="18" x2="-10" y2="20" stroke="#334155" stroke-width="2.4"/>'
          '<line x1="16" y1="18" x2="12" y2="20" stroke="#334155" stroke-width="2.4"/></g>' % (hx, hy))
    f.parrow(hx + 96, hy - 6, 0, 58, RED, 3)
    f.txt(hx + 162, hy - 15, 'v', RED, 13, 'start', it=True)
    f.circle(hx, hy + 24, 7, '#B45309', '#7C2D12', 1.6)
    _hpar(f, hx, hy + 24, 230, gy - hy - 24)
    # man
    mx = hx
    f.circle(mx, gy - 42, 9, '#FDE68A', DK, 1.8)
    f.line(mx, gy - 33, mx, gy - 14, DK, 2.6)
    f.line(mx, gy - 28, mx - 12, gy - 18, DK, 2.2); f.line(mx, gy - 28, mx + 12, gy - 18, DK, 2.2)
    f.line(mx, gy - 14, mx - 10, gy, DK, 2.4); f.line(mx, gy - 14, mx + 10, gy, DK, 2.4)
    f.dim(hx - 42, hy, hx - 42, gy, '', PU, 0, 12)
    f.tbg(hx - 42, (hy + gy) / 2, 'h', PU, 12.5)
    f.guide(hx - 48, hy, hx - 8, hy); f.guide(hx - 48, gy, hx - 16, gy)
    f.txt(w - 20, 28, 'the package is released at this instant', MUT, 10.5, 'end')
    return f.render()

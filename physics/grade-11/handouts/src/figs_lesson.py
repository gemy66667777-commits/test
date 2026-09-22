# -*- coding: utf-8 -*-
"""Original figures drawn from scratch for the Lesson 1-1 worksheet."""
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV

INK = '#0B1220'; MUT = '#6B8098'; SKY = '#0EA5E9'; VIO = '#7C3AED'
RED = '#E11D48'; GRN = '#059669'; AMB = '#D97706'; IND = '#2563EB'


def _axes(f, cx, cy, x1, x2, y1, y2, xl='x', yl='y'):
    f.arrow(x1, cy, x2, cy, '#94A3B8', 1.8)
    f.arrow(cx, y2, cx, y1, '#94A3B8', 1.8)
    f.arrow(cx, cy, x1, cy, '#94A3B8', 1.8)
    f.arrow(cx, cy, cx, y2, '#94A3B8', 1.8)
    f.txt(x2 - 4, cy + 20, xl, MUT, 12, 'end')
    f.txt(cx + 20, y1 + 12, yl, MUT, 12, 'start')


def axes_vectors(cap='Figure 1'):
    f = Fig(660, 470, cap, 520)
    cx, cy = 330.0, 232.0
    _axes(f, cx, cy, 34, 626, 24, 440, 'x  (east)', 'y  (north)')
    S = 13.0
    data = [
        ('V\u2081 = 3 m/s', 3, 0, RED, None),
        ('V\u2082 = 5 m/s', 5, 180, IND, None),
        ('V\u2083 = 6 m/s', 6, 90, GRN, None),
        ('V\u2084 = 8 m/s', 8, 270, AMB, None),
        ('V\u2085 = 10 m/s', 10, 45, VIO, ('45\u00b0', 0, 45, 40)),
        ('V\u2086 = 6 m/s', 6, 120, SKY, ('60\u00b0', 180, 120, 52)),
        ('V\u2087 = 6 m/s', 6, 240, '#BE185D', ('60\u00b0', 180, 240, 40)),
        ('V\u2088 = 10 m/s', 10, 290, '#0F766E', ('20\u00b0', 270, 290, 64)),
    ]
    LOFF = {0: (16, 5, 'start'), 180: (-16, 5, 'end'), 90: (-12, -8, 'end'), 270: (-14, 16, 'end'),
            45: (14, -4, 'start'), 120: (-12, -6, 'end'), 240: (-10, 14, 'end'), 290: (14, 16, 'start')}
    for lab, mag, ang, col, arc in data:
        L = mag * S
        t = P(cx, cy, L, ang)
        f.arrow(cx, cy, t[0], t[1], col, 3)
        dx, dy, anch = LOFF[ang]
        f.txt(t[0] + dx, t[1] + dy, lab, col, 12, anch)
        if arc:
            t2, a1, a2, r = arc
            f.arc(cx, cy, r, a1, a2, OR, 1.8)
            m = P(cx, cy, r + 18, (a1 + a2) / 2.0)
            f.tbg(m[0], m[1] + 4, t2, OR, 11, pad=3)
    f.circle(cx, cy, 4, INK, INK, 1)
    return f.render()


def two_vec(cap, v1, a1, l1, v2, a2, l2, arc=None, S=17.0, maxw=330, note=None):
    pts = [P(0, 0, v1 * S + 54, a1), P(0, 0, v2 * S + 54, a2), (0, 0)]
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    w = max(260.0, max(xs) - min(xs) + 60)
    h = max(150.0, max(ys) - min(ys) + 60) + (20 if note else 0)
    ox = 30 - min(xs); oy = 30 - min(ys)
    f = Fig(w, h, cap, maxw)
    for (v, a, lab, col) in ((v1, a1, l1, AMB), (v2, a2, l2, IND)):
        t = P(ox, oy, v * S, a)
        f.arrow(ox, oy, t[0], t[1], col, 3.2)
        lp = P(ox, oy, v * S + 26, a)
        aa = a % 360
        anch = 'middle'
        if aa < 25 or aa > 335:
            anch, lp = 'start', (lp[0] - 18, lp[1] + 4)
        elif 155 < aa < 205:
            anch, lp = 'end', (lp[0] + 18, lp[1] + 4)
        else:
            lp = (lp[0], lp[1] + (10 if 200 < aa < 340 else -2))
        f.txt(lp[0], lp[1] + 4, lab, col, 12.5, anch)
    if arc:
        r = min(38.0, min(v1, v2) * S * 0.55)
        f.arc(ox, oy, r, a1, a2, OR, 1.9)
        m = P(ox, oy, r + 19, (a1 + a2) / 2.0)
        f.txt(m[0], m[1] + 4, arc, OR, 12)
    f.circle(ox, oy, 4.2, INK, INK, 1)
    if note:
        f.txt(w / 2, h - 9, note, MUT, 10.5)
    return f.render()


def _plane(f, x, y, ang, s=1.0, col='#CBD5E1', edge='#64748B'):
    body = 'M-36,0 L18,0 L34,-7 L4,-7 L-10,-23 L-21,-23 L-12,-7 L-36,-7 Z'
    tail = 'M-14,0 L2,0 L-8,14 Z'
    f.raw('<g transform="translate(%.1f,%.1f) rotate(%.1f) scale(%.2f)">'
          '<path d="%s" fill="%s" stroke="%s" stroke-width="1.6" stroke-linejoin="round"/>'
          '<path d="%s" fill="%s" stroke="%s" stroke-width="1.6" stroke-linejoin="round"/>'
          '<circle cx="6" cy="-3.5" r="2.2" fill="%s"/></g>'
          % (x, y, -ang, s, body, col, edge, tail, col, edge, edge))


def plane_launch(cap, ang, vlab, comps=False, hlab=None, ground=True, anglab=None, maxw=430,
                 w=520, h=250, extra=None):
    f = Fig(w, h, cap, maxw)
    gy = h - 46.0
    if ground:
        f.line(24, gy, w - 24, gy, DK, 2.6)
        for x in range(32, int(w) - 28, 20):
            f.line(x, gy, x - 8, gy + 8, '#94A3B8', 1.4)
    x0, y0 = 96.0, gy - 8
    L = 150.0
    tip = P(x0, y0, L, ang)
    _plane(f, tip[0] - 4, tip[1] - 4, ang, 0.92)
    f.arrow(x0, y0, tip[0], tip[1], RED, 3.2)
    off = P(0, 0, 30, ang - 90)
    f.txt(tip[0] + off[0] + 6, tip[1] + off[1] + 4, vlab, RED, 12.5, 'start')
    f.guide(x0, y0, x0 + 120, y0)
    f.angle(x0, y0, 42, 0, ang, anglab or ('%g°' % ang), OR, 60, 12)
    if comps:
        vx = L * math.cos(math.radians(ang)); vy = L * math.sin(math.radians(ang))
        f.parrow(x0, y0, 0, vx, GRN, 2.6, '5 4')
        f.parrow(x0, y0, 90, vy, SKY, 2.6, '5 4')
        f.guide(x0 + vx, y0, tip[0], tip[1]); f.guide(x0, y0 - vy, tip[0], tip[1])
        f.tbg(x0 + vx / 2, y0 - 7, 'vₓ = ?', GRN, 11.5)
        f.tbg(x0 - 32, y0 - vy / 2, 'vᵧ = ?', SKY, 11.5)
    if hlab:
        hx = w - 78.0
        f.guide(tip[0], tip[1], hx + 16, tip[1])
        f.dim(hx, gy, hx, tip[1], '', PU, 0, 12)
        f.tbg(hx + 34, (gy + tip[1]) / 2, hlab, PU, 12)
    if extra:
        f.txt(w / 2 + 40, 30, extra, MUT, 11)
    return f.render()


def comp_tri(cap, vxlab, vylab, vlab='v = ?', anglab='θ = ?', vx=3.0, vy=4.0, maxw=300):
    S = 40.0
    w, h = 340, 250
    f = Fig(w, h, cap, maxw)
    ox, oy = 90.0, h - 58.0
    tx, ty = ox + vx * S, oy - vy * S
    f.arrow(ox, oy, tx, oy, GRN, 3.2)
    f.arrow(ox, oy, ox, ty, SKY, 3.2)
    f.guide(tx, oy, tx, ty); f.guide(ox, ty, tx, ty)
    f.arrow(ox, oy, tx, ty, RED, 3.2)
    f.txt((ox + tx) / 2, oy + 22, vxlab, GRN, 12)
    f.txt(ox - 10, (oy + ty) / 2, vylab, SKY, 12, 'end')
    f.txt((ox + tx) / 2 + 26, (oy + ty) / 2 - 8, vlab, RED, 12.5, 'start')
    f.angle(ox, oy, 44, 0, math.degrees(math.atan2(vy, vx)), anglab, OR, 66, 12)
    f.circle(ox, oy, 4, INK, INK, 1)
    f.rang(tx, oy, 180, 90, 11, MUT)
    return f.render()


def cross_cars(cap, aLab, aDir, bLab, bDir, maxw=360, w=430, h=300):
    f = Fig(w, h, cap, maxw)
    cx, cy = w / 2.0, h / 2.0 - 6
    f.rect(26, cy - 30, w - 52, 60, '#F1F5F9', '#E2E8F0', 1.6, 5)
    f.rect(cx - 30, 22, 60, h - 60, '#F1F5F9', '#E2E8F0', 1.6, 5)
    f.line(26, cy, w - 26, cy, '#CBD5E1', 1.8, '13 9')
    f.line(cx, 22, cx, h - 38, '#CBD5E1', 1.8, '13 9')
    ANG = {'E': 0, 'W': 180, 'N': 90, 'S': 270}
    for lab, d, col, r in ((aLab, aDir, IND, 'A'), (bLab, bDir, GRN, 'B')):
        a = ANG[d]
        st = P(cx, cy, 58, (a + 180) % 360)
        f.rect(st[0] - 19, st[1] - 13, 38, 26, '#E0E7FF' if r == 'A' else '#DCFCE7', col, 2, 6)
        f.circle(st[0] - 10, st[1] + 13, 6, '#475569', DK, 1.6)
        f.circle(st[0] + 10, st[1] + 13, 6, '#475569', DK, 1.6)
        f.txt(st[0], st[1] - 20, r, col, 13)
        ar = P(cx, cy, 8, (a + 180) % 360)
        tip = P(cx, cy, 62, a)
        f.arrow(ar[0], ar[1], tip[0], tip[1], RED, 2.8)
        lp = P(cx, cy, 86, a)
        anch = 'middle'
        if a == 0: anch, lp = 'start', (lp[0] - 10, lp[1] - 12)
        if a == 180: anch, lp = 'end', (lp[0] + 10, lp[1] - 12)
        if a == 90: lp = (lp[0], lp[1] + 2)
        if a == 270: lp = (lp[0], lp[1] + 12)
        f.txt(lp[0], lp[1] + 4, lab, RED, 12, anch)
    for t, x, y in (('N', cx, 18), ('S', cx, h - 20), ('E', w - 16, cy + 5), ('W', 16, cy + 5)):
        f.txt(x, y, t, MUT, 11)
    return f.render()


def bus_rain(cap, maxw=440, w=520, h=260):
    f = Fig(w, h, cap, maxw)
    gy = 214.0
    f.line(22, gy, w - 22, gy, DK, 2.8)
    for x in range(30, int(w) - 26, 20):
        f.line(x, gy, x - 8, gy + 8, '#94A3B8', 1.4)
    # bus
    bx, by, bw, bh = 46.0, 96.0, 250.0, 96.0
    f.rect(bx, by, bw, bh, '#FCD34D', '#B45309', 2.4, 12)
    f.rect(bx + 14, by + 12, 56, 38, '#E0F2FE', '#0369A1', 1.8, 5)
    for k in range(3):
        f.rect(bx + 84 + k * 52, by + 12, 42, 38, '#E0F2FE', '#0369A1', 1.8, 5)
    f.rect(bx + 84, by + 12, 42, 38, '#BAE6FD', '#0369A1', 2.2, 5)
    f.circle(bx + 105, by + 34, 7, '#FDE68A', '#92400E', 1.6)
    f.line(bx + 105, by + 41, bx + 105, by + 52, '#92400E', 2)
    f.circle(bx + 54, gy - 6, 15, '#334155', DK, 2.4); f.circle(bx + 54, gy - 6, 6, '#94A3B8', DK, 1.6)
    f.circle(bx + 198, gy - 6, 15, '#334155', DK, 2.4); f.circle(bx + 198, gy - 6, 6, '#94A3B8', DK, 1.6)
    f.parrow(bx + bw + 8, by + 46, 0, 62, RED, 3.2)
    f.txt(bx + bw + 40, by + 26, 'v(bus) = 20 m/s', RED, 12)
    # rain (as seen by the passenger : slanted)
    for k in range(6):
        x = 352.0 + k * 26
        y0 = 62.0 + (k % 3) * 15
        t = P(x, y0, 66, -50)
        f.arrow(x, y0, t[0], t[1], SKY, 2.2)
    f.guide(438, 96, 438, 190)
    f.angle(438, 96, 46, 270, 310, '40°', OR, 66, 12)
    f.txt(w - 16, 26, 'the rain as the passenger sees it', MUT, 10.5, 'end')
    return f.render()


def mcq_vectors(cap, maxw=470, w=560, h=300):
    f = Fig(w, h, cap, maxw)
    # the given resultant R
    f.rect(18, 40, 148, 128, '#F8FAFC', '#E2E8F0', 1.6, 10)
    f.arrow(146, 152, 48, 58, PU, 3.2)
    f.txt(122, 74, 'R', PU, 15, 'middle', it=True)
    f.txt(92, 190, 'the given resultant', MUT, 10.5)
    opts = [('a', 250.0, 74.0, 180, 90), ('b', 420.0, 74.0, 0, 90),
            ('c', 250.0, 216.0, 0, 180), ('d', 420.0, 216.0, 0, 45)]
    for lab, ox, oy, aA, aB in opts:
        f.rect(ox - 76, oy - 56, 152, 118, '#FCFDFF', '#E6ECF3', 1.4, 10)
        bx, by = ox - 10, oy + 40
        tb = P(bx, by, 52, aA)
        f.arrow(bx, by, tb[0], tb[1], AMB, 2.8)
        lb = P(bx, by, 30, aA)
        f.txt(lb[0], lb[1] + (18 if aA in (0, 180) else 0), 'B', AMB, 11.5)
        ta = P(bx, by, 52, aB)
        f.arrow(bx, by, ta[0], ta[1], IND, 2.8)
        la = P(bx, by, 34, aB)
        f.txt(la[0] + (-14 if aB == 90 else 8), la[1] + (0 if aB == 90 else -10), 'A', IND, 11.5)
        f.txt(ox, oy + 58, '( %s )' % lab, MUT, 11)
    return f.render()


def two_planes(cap, maxw=440, w=520, h=240):
    f = Fig(w, h, cap, maxw)
    gy = 196.0
    f.line(22, gy, w - 22, gy, DK, 2.6)
    for x in range(30, int(w) - 26, 20):
        f.line(x, gy, x - 8, gy + 8, '#94A3B8', 1.4)
    x0 = 80.0
    for ang, col, nm, R in ((58.0, RED, 'A', 300.0), (30.0, IND, 'B', 380.0)):
        H = R * math.tan(math.radians(ang)) / 4
        pts = [(x0 + R * (i / 44.0), gy - 4 * H * (i / 44.0) * (1 - i / 44.0)) for i in range(45)]
        f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % p for p in pts) +
              '" fill="none" stroke="%s" stroke-width="2.2" stroke-dasharray="6 5"/>' % col)
        t = P(x0, gy, 74, ang)
        f.arrow(x0, gy, t[0], t[1], col, 3)
        f.angle(x0, gy, 34 if ang > 45 else 52, 0, ang, None, OR, 0)
        f.tbg(x0 + R / 2 + (0 if nm == 'A' else 60), gy - H - 13, 'plane ' + nm, col, 12)
    f.txt(w - 26, 26, 'both launched with the same initial speed', MUT, 10.5, 'end')
    return f.render()


def ferry(cap, aim_upstream=False, maxw=420, w=490, h=250):
    f = Fig(w, h, cap, maxw)
    yT, yB = 52.0, 200.0
    f.rect(30, yT, w - 60, yB - yT, '#E0F2FE', 'none', 0, 0)
    for yy in (yT, yB):
        f.line(30, yy, w - 30, yy, DK, 2.8)
    for x in range(36, int(w) - 32, 20):
        f.line(x, yB, x - 8, yB + 8, '#94A3B8', 1.4)
        f.line(x, yT, x + 8, yT - 8, '#94A3B8', 1.4)
    for yy in (88, 126, 164):
        f.parrow(150, yy, 0, 66, SKY, 2.2)
    f.txt(300, 152, 'river current', '#0284C7', 11, 'start')
    bx, byy = 128.0, yB - 12
    f.poly([(bx - 17, byy), (bx + 17, byy), (bx + 9, byy - 17), (bx - 9, byy - 17)], '#FDBA74', '#C2410C', 2)
    ang = 118.0 if aim_upstream else 90.0
    t = P(bx, byy - 20, 74, ang)
    f.arrow(bx, byy - 20, t[0], t[1], RED, 3)
    f.txt(t[0] - 14, t[1] + 2, 'v(boat)', RED, 11.5, 'end')
    f.guide(bx, byy - 20, bx, yT + 10)
    if aim_upstream:
        f.angle(bx, byy - 20, 44, 90, ang, 'α', OR, 62, 12)
    f.arrow(bx, byy - 20, bx + 6, yT + 14, PU, 2.6, dash='7 5')
    f.tbg(bx + 96, 96, 'resultant path', PU, 11)
    f.txt(w / 2 + 60, yB + 26, 'the boat must land exactly opposite its start', MUT, 10.5)
    return f.render()


def proj_height(cap, ang, vlab, hlab='h(max)', maxw=430, w=520, h=240):
    f = Fig(w, h, cap, maxw)
    gy = 192.0; R = 330.0
    H = R * math.tan(math.radians(ang)) / 4
    x0 = 78.0
    f.line(22, gy, w - 22, gy, DK, 2.6)
    for x in range(30, int(w) - 26, 20):
        f.line(x, gy, x - 8, gy + 8, '#94A3B8', 1.4)
    pts = [(x0 + R * (i / 48.0), gy - 4 * H * (i / 48.0) * (1 - i / 48.0)) for i in range(49)]
    f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % p for p in pts) +
          '" fill="none" stroke="%s" stroke-width="2.2" stroke-dasharray="6 5"/>' % IND)
    t = P(x0, gy, 82, ang)
    f.arrow(x0, gy, t[0], t[1], RED, 3.2)
    off = P(0, 0, 26, ang + 90)
    f.txt(t[0] + off[0] - 6, t[1] + off[1], vlab, RED, 12.5, 'end')
    f.angle(x0, gy, 40, 0, ang, '%g°' % ang, OR, 58, 12)
    ax = x0 + R / 2
    f.guide(ax, gy - H, x0 - 26, gy - H)
    f.dim(ax, gy, ax, gy - H, '', PU, 0, 12)
    f.tbg(ax + 40, gy - H / 2, hlab, PU, 12)
    f.circle(ax, gy - H, 5, RED, RED, 1)
    return f.render()


def rel_cases(cap, maxw=470, w=560, h=190):
    f = Fig(w, h, cap, maxw)
    panels = [('same direction', 0, 0), ('opposite directions', 0, 180), ('perpendicular', 0, 90)]
    for k, (t, aA, aB) in enumerate(panels):
        x0 = 30 + k * 178
        f.rect(x0 - 14, 20, 160, 118, '#FCFDFF', '#E6ECF3', 1.4, 11)
        oy = 66.0
        f.txt(x0 + 66, 34, '( %s )' % 'abc'[k], MUT, 10.5)
        ta = P(x0 + 20, oy, 66, aA)
        f.arrow(x0 + 20, oy, ta[0], ta[1], RED, 2.9)
        f.txt(x0 + 52, oy - 10, 'v(A)', RED, 11)
        oy2 = 108.0
        sb = (x0 + 20) if aB != 180 else (x0 + 96)
        tb = P(sb, oy2, 66, aB)
        f.arrow(sb, oy2, tb[0], tb[1], IND, 2.9)
        f.txt(x0 + 56, oy2 + 20 if aB != 90 else oy2 - 30, 'v(B)', IND, 11)
        f.txt(x0 + 66, 156, t, MUT, 10.5)
    return f.render()

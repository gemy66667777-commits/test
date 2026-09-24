# -*- coding: utf-8 -*-
"""Original figures for the Z BANK bank : Chapter 2, Lesson 1 - moment of a force."""
import math
import re
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV

WOOD1, WOOD2 = '#F6D39B', '#D9A15B'
STEEL1, STEEL2 = '#F1F5F9', '#94A3B8'
GRADS = ('<defs>'
         '<linearGradient id="gSteel" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F8FAFC"/>'
         '<stop offset="0.5" stop-color="#CBD5E1"/><stop offset="1" stop-color="#64748B"/></linearGradient>'
         '<linearGradient id="gWood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F9DDAE"/>'
         '<stop offset="1" stop-color="#C98B45"/></linearGradient>'
         '<linearGradient id="gRod" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#93C5FD"/>'
         '<stop offset="1" stop-color="#1D4ED8"/></linearGradient>'
         '<linearGradient id="gSky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#EFF6FF"/>'
         '<stop offset="1" stop-color="#FFFFFF"/></linearGradient>'
         '<radialGradient id="gBall" cx="0.35" cy="0.35" r="0.7"><stop offset="0" stop-color="#FDE68A"/>'
         '<stop offset="1" stop-color="#EA580C"/></radialGradient>'
         '<pattern id="hWall" width="10" height="10" patternUnits="userSpaceOnUse" '
         'patternTransform="rotate(45)"><rect width="10" height="10" fill="#E2E8F0"/>'
         '<line x1="0" y1="0" x2="0" y2="10" stroke="#94A3B8" stroke-width="3"/></pattern>'
         '</defs>')


def out(f, wmm):
    """render a figure as an inline svg of a given printed width."""
    s = f.render()
    s = s.replace('<figure class="fig">', '').replace('</figure>', '')
    s = s.replace('class="svgfig"', 'class="fg" style="width:%smm"' % wmm, 1)
    s = s.replace('<defs>', GRADS + '<defs>', 1)
    return s


def lab(f, x, y, s, c=NV, size=15, anchor='middle'):
    """a label on a soft white card, sized from the text."""
    w = 0.56 * size * len(re.sub(r'&[#a-z0-9]+;', 'x', s)) + 10
    x0 = x - w / 2 if anchor == 'middle' else (x - 5 if anchor == 'start' else x - w + 5)
    f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="5" fill="#fff" fill-opacity="0.9"/>'
          % (x0, y - size * 0.88, w, size * 1.18))
    f.txt(x, y, s, c, size, anchor)


def beam(f, x1, y1, x2, y2, w=12, fill='url(#gRod)'):
    """a rod drawn as a rounded bar with a gradient."""
    ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
    L = math.hypot(x2 - x1, y2 - y1)
    f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" rx="%d" fill="%s" stroke="#1E3A8A" '
          'stroke-width="1.6" transform="rotate(%.2f %.1f %.1f)"/>'
          % (x1, y1 - w / 2, L, w, w / 2, fill, ang, x1, y1))


def pin(f, x, y, lab_='O', dx=0, dy=30):
    f.poly([(x, y), (x - 13, y + 22), (x + 13, y + 22)], '#CBD5E1', DK, 2)
    f.line(x - 20, y + 22, x + 20, y + 22, DK, 3)
    for k in range(-2, 3):
        f.line(x + k * 8, y + 22, x + k * 8 - 6, y + 29, DK, 1.6)
    f.circle(x, y, 5.5, '#fff', DK, 2.4)
    if lab_:
        f.txt(x + dx, y + dy + 16, lab_, NV, 15)


def dot(f, x, y, s, dx=0, dy=-12, c=NV, size=15):
    f.circle(x, y, 4.5, c, '#fff', 1.6)
    if s:
        f.txt(x + dx, y + dy, s, c, size)


def graph_axes(f, x0, y0, W, H, xt, yt, xl, yl, xmax, ymax):
    """axes with a light grid : xt / yt are lists of tick values."""
    for v in xt:
        X = x0 + W * v / xmax
        f.line(X, y0, X, y0 - H, '#E2E8F0', 1.2)
        f.txt(X, y0 + 20, ('%g' % v), DK, 12.5, bold=False)
    for v in yt:
        Y = y0 - H * v / ymax
        f.line(x0, Y, x0 + W, Y, '#E2E8F0', 1.2)
        f.txt(x0 - 9, Y + 4.5, ('%g' % v), DK, 12.5, 'end', bold=False)
    f.arrow(x0, y0, x0 + W + 22, y0, DK, 2.2)
    f.arrow(x0, y0, x0, y0 - H - 22, DK, 2.2)
    f.txt(x0 + W + 26, y0 + 5, xl, NV, 14, 'start')
    f.txt(x0 + 6, y0 - H - 28, yl, NV, 14, 'start')


# =========================================================================== 1
def wrench(wmm=112):
    f = Fig(470, 210)
    cx, cy = 80, 120
    # the bolt
    hexp = [P(cx, cy, 30, 30 + 60 * k) for k in range(6)]
    f.poly(hexp, 'url(#gSteel)', '#334155', 2.4)
    f.circle(cx, cy, 11, '#E2E8F0', '#334155', 2)
    # spanner handle and jaw
    a1, a2 = math.radians(150), math.radians(-150)
    f.raw('<path d="M%.1f,%.1f A40,40 0 1 1 %.1f,%.1f" fill="none" stroke="#475569" stroke-width="19" '
          'stroke-linecap="round"/>' % (cx + 40 * math.cos(a1), cy - 40 * math.sin(a1),
                                        cx + 40 * math.cos(a2), cy - 40 * math.sin(a2)))
    f.raw('<path d="M%.1f,%.1f A40,40 0 1 1 %.1f,%.1f" fill="none" stroke="#E2E8F0" stroke-width="13" '
          'stroke-linecap="round"/>' % (cx + 40 * math.cos(a1), cy - 40 * math.sin(a1),
                                        cx + 40 * math.cos(a2), cy - 40 * math.sin(a2)))
    f.raw('<rect x="%d" y="%d" width="300" height="24" rx="12" fill="url(#gSteel)" stroke="#334155" '
          'stroke-width="2.2"/>' % (cx + 32, cy - 12))
    f.raw('<rect x="%d" y="%d" width="200" height="5" rx="2.5" fill="#fff" opacity="0.7"/>' % (cx + 70, cy - 8))
    ex = cx + 320
    f.arrow(ex, cy - 14, ex, cy - 96, AR, 4.2)
    lab(f, ex + 10, cy - 70, 'F = 80 N', AR, 16, 'start')
    f.dim(cx, cy + 52, ex, cy + 52, '25 cm', PU, 0, 15)
    f.guide(cx, cy + 12, cx, cy + 60)
    f.guide(ex, cy + 14, ex, cy + 60)
    f.txt(cx - 34, cy - 40, 'bolt', NV, 13, 'end')
    return out(f, wmm)


# =========================================================================== 2
def door_top(wmm=110):
    f = Fig(480, 230)
    hx, hy, L = 70, 150, 330
    f.rect(20, 40, 40, 170, 'url(#hWall)', '#64748B', 1.6, 2)
    f.txt(40, 30, 'wall', NV, 13)
    f.raw('<rect x="%d" y="%d" width="%d" height="16" rx="3" fill="url(#gWood)" stroke="#92400E" '
          'stroke-width="2"/>' % (hx, hy - 8, L))
    f.circle(hx, hy, 8, '#fff', DK, 2.6)
    f.circle(hx, hy, 2.6, DK, DK, 1)
    f.txt(hx - 2, hy + 34, 'hinge', NV, 13)
    f.circle(hx + L - 10, hy - 14, 6, '#FBBF24', '#92400E', 2)
    f.arrow(hx + L, hy - 10, hx + L, hy - 100, AR, 4)
    lab(f, hx + L + 8, hy - 76, 'F&#8321;', AR, 17, 'start')
    f.arrow(hx + L + 60, hy, hx + L + 6, hy, GR, 4)
    lab(f, hx + L + 40, hy + 26, 'F&#8322;', GR, 17)
    f.arrow(hx + L / 2, hy - 10, hx + L / 2, hy - 100, BL, 4)
    lab(f, hx + L / 2 + 10, hy - 76, 'F&#8323;', BL, 17, 'start')
    f.dim(hx, hy + 54, hx + L, hy + 54, '0.9 m', PU, 0, 15)
    f.txt(250, 222, 'top view', GY, 12)
    return out(f, wmm)


# =========================================================================== 3
def rod_30(wmm=100):
    f = Fig(470, 230)
    ox, oy, L = 55, 150, 250
    beam(f, ox, oy, ox + L, oy)
    pin(f, ox, oy)
    ax = ox + L
    f.guide(ax, oy, ax + 90, oy)
    fx, fy = P(ax, oy, 120, 30)
    f.arrow(ax, oy, fx, fy, AR, 4.2)
    f.angle(ax, oy, 46, 0, 30, '30&#176;', OR, 70, 14)
    lab(f, fx - 8, fy - 12, 'F = 40 N', AR, 16)
    f.txt(ax, oy + 32, 'A', NV, 16)
    f.dim(ox, oy + 58, ax, oy + 58, '0.5 m', PU, 0, 15)
    return out(f, wmm)


# =========================================================================== 5
def rod_three(wmm=120):
    f = Fig(540, 262)
    ox, oy, s = 270, 120, 190          # 0.6 m = 190 px
    beam(f, ox - s, oy, ox + s, oy)
    pin(f, ox, oy + 6, 'O', 0, 26)
    f.arrow(ox - s, oy + 6, ox - s, oy + 86, AR, 4)
    lab(f, ox - s - 10, oy + 74, '20 N', AR, 15, 'end')
    f.arrow(ox + s, oy + 6, ox + s, oy + 86, BL, 4)
    lab(f, ox + s + 10, oy + 74, '30 N', BL, 15, 'start')
    cxp = ox + s / 2
    f.arrow(cxp, oy - 6, cxp, oy - 80, GR, 4)
    lab(f, cxp + 8, oy - 62, '25 N', GR, 15, 'start')
    f.txt(ox - s, oy - 16, 'A', NV, 16)
    f.txt(ox + s, oy - 16, 'B', NV, 16)
    f.txt(cxp - 14, oy - 14, 'C', NV, 16)
    f.dim(ox - s, oy - 50, ox, oy - 50, '0.6 m', PU, 0, 14)
    f.dim(ox, 244, ox + s, 244, '0.6 m', PU, 0, 14)
    f.dim(ox, oy + 58, cxp, oy + 58, '0.3 m', OR, 0, 13)
    return out(f, wmm)


# =========================================================================== 7
def bent_handle(wmm=74):
    f = Fig(330, 330)
    ox, oy = 70, 262
    s = 480                             # px per metre
    px, py = ox + 0.3 * s, oy - 0.4 * s
    hexp = [P(ox, oy, 24, 30 + 60 * k) for k in range(6)]
    beam(f, ox, oy, px + 6, oy, 16, 'url(#gSteel)')
    beam(f, px, oy + 7, px, py, 16, 'url(#gSteel)')
    f.poly(hexp, 'url(#gSteel)', '#334155', 2.2)
    f.circle(ox, oy, 8, '#E2E8F0', '#334155', 2)
    f.txt(ox - 4, oy + 42, 'O', NV, 16)
    f.line(ox, oy, px, py, GY, 1.8, '6 5')
    dot(f, px, py, 'P', 0, -16, AR, 16)
    f.dim(ox, oy + 44, px, oy + 44, '0.3 m', PU, 0, 14)
    f.dim(px + 26, oy, px + 26, py, '', PU, 0, 14)
    f.txt(px + 36, (oy + py) / 2 + 5, '0.4 m', PU, 14, 'start')
    return out(f, wmm)


# =========================================================================== 8
def inclined_rod(wmm=100):
    f = Fig(450, 330)
    ox, oy, L = 70, 282, 330
    ax, ay = P(ox, oy, L, 30)
    gx, gy = P(ox, oy, L / 2, 30)
    f.guide(ox, oy, ox + 360, oy)
    beam(f, ox, oy, ax, ay)
    pin(f, ox, oy)
    f.angle(ox, oy, 62, 0, 30, '30&#176;', OR, 84, 14)
    f.arrow(gx, gy, gx, gy + 80, BL, 4)
    lab(f, gx + 8, gy + 66, 'W = 50 N', BL, 15, 'start')
    dot(f, gx, gy, '', 0, 0, BL)
    f.arrow(ax, ay, ax, ay - 88, AR, 4)
    lab(f, ax - 10, ay - 64, '40 N', AR, 15, 'end')
    f.txt(ax + 16, ay + 6, 'A', NV, 16, 'start')
    f.txt(gx - 8, gy - 16, 'G', NV, 14, 'end')
    lab(f, (ox + ax) / 2 - 10, (oy + ay) / 2 - 34, 'L = 2 m', PU, 14)
    return out(f, wmm)


# =========================================================================== 9
def graph_m_theta(wmm=92):
    f = Fig(440, 300)
    x0, y0, W, H = 70, 250, 320, 190
    graph_axes(f, x0, y0, W, H, [0, 30, 60, 90, 120, 150, 180], [0, 6, 12, 18, 24],
               '&#952; (&#176;)', 'M (N&#183;m)', 180, 24)
    pts = ['%.1f,%.1f' % (x0 + W * t / 180, y0 - H * math.sin(math.radians(t))) for t in range(0, 181, 3)]
    f.raw('<polyline points="%s" fill="none" stroke="#DC2626" stroke-width="3.4" stroke-linejoin="round"/>'
          % ' '.join(pts))
    return out(f, wmm)


# =========================================================================== 10
def graph_m_d(wmm=88):
    f = Fig(420, 300)
    x0, y0, W, H = 70, 250, 290, 190
    graph_axes(f, x0, y0, W, H, [0, 0.1, 0.2, 0.3, 0.4, 0.5], [0, 1.5, 3, 4.5, 6, 7.5],
               'd (m)', 'M (N&#183;m)', 0.5, 7.5)
    f.line(x0, y0, x0 + W, y0 - H, '#2563EB', 3.6)
    X, Y = x0 + W * 0.4 / 0.5, y0 - H * 6 / 7.5
    f.guide(X, y0, X, Y, '#7C3AED', 1.8)
    f.guide(x0, Y, X, Y, '#7C3AED', 1.8)
    f.circle(X, Y, 5.5, '#7C3AED', '#fff', 2)
    return out(f, wmm)


# =========================================================================== 11
def four_panels(wmm=150):
    f = Fig(700, 300)
    specs = [('(a)', 0.5, 20, 90), ('(b)', 0.5, 40, 30), ('(c)', 0.6, 25, 53), ('(d)', 0.3, 30, 90)]
    for k, (tag, L, F, th) in enumerate(specs):
        gx, gy = (k % 2) * 350, (k // 2) * 150
        f.rect(gx + 8, gy + 8, 334, 134, '#F8FAFC', '#CBD5E1', 1.4, 14)
        ox, oy = gx + 50, gy + 104
        px = ox + L * 380
        beam(f, ox, oy, px, oy, 10)
        pin(f, ox, oy, '', 0, 0)
        fx, fy = P(px, oy, 64, th)
        f.arrow(px, oy, fx, fy, AR, 3.6)
        if th != 90:
            f.guide(px, oy, px + 50, oy)
            f.angle(px, oy, 30, 0, th, '%d&#176;' % th, OR, 46, 12.5)
        lab(f, fx + (8 if th != 90 else 10), fy + 6, '%d N' % F, AR, 14, 'start')
        f.txt((ox + px) / 2, oy + 30, '%g m' % L, PU, 13.5)
        f.txt(gx + 30, gy + 34, tag, NV, 16)
    return out(f, wmm)


# =========================================================================== 12
def bicycle_crank(wmm=76):
    f = Fig(340, 330)
    cx, cy = 150, 130
    teeth = []
    for k in range(64):
        ang = k * math.pi / 32
        r = 58 if k % 2 == 0 else 52
        teeth.append('%.1f,%.1f' % (cx + r * math.cos(ang), cy + r * math.sin(ang)))
    f.raw('<polygon points="%s" fill="#E2E8F0" stroke="#475569" stroke-width="2"/>' % ' '.join(teeth))
    f.circle(cx, cy, 40, '#F8FAFC', '#475569', 2)
    for k in range(5):
        a1 = k * 72
        f.line(cx, cy, *P(cx, cy, 40, a1), c='#94A3B8', w=4)
    L = 150
    px, py = P(cx, cy, L, -30)                     # 60 deg from the downward vertical
    f.guide(cx, cy, cx, cy + 170)
    beam(f, cx, cy, px, py, 14, 'url(#gSteel)')
    f.circle(cx, cy, 9, '#fff', DK, 2.6)
    f.raw('<rect x="%.1f" y="%.1f" width="54" height="16" rx="4" fill="#334155"/>' % (px - 27, py - 8))
    f.arrow(px, py - 70, px, py - 12, AR, 4.4)
    lab(f, px + 8, py - 50, '300 N', AR, 15, 'start')
    f.angle(cx, cy, 70, -90, -30, '60&#176;', OR, 92, 14)
    f.txt(cx - 18, cy - 12, 'O', NV, 15)
    lab(f, (cx + px) / 2 + 14, (cy + py) / 2 + 30, '17 cm', PU, 14, 'start')
    return out(f, wmm)


# =========================================================================== 13
def line_of_action(wmm=96):
    f = Fig(440, 250)
    ox, oy = 70, 200
    f.circle(ox, oy, 7, '#fff', DK, 2.6)
    f.txt(ox - 14, oy + 22, 'O', NV, 16)
    # the line of action : y = 70 (horizontal), F acts to the right
    y1 = 70
    f.line(30, y1, 420, y1, GY, 1.8, '7 6')
    f.arrow(170, y1, 250, y1, AR, 4.4)
    dot(f, 170, y1, 'P', 0, -14, AR)
    dot(f, 340, y1, 'Q', 0, -14, NV)
    lab(f, 212, y1 + 26, 'F', AR, 17)
    # a parallel line nearer to O
    y2 = 140
    f.line(30, y2, 420, y2, '#A7F3D0', 1.8, '7 6')
    dot(f, 300, y2, 'R', 0, -14, GR)
    f.line(ox, oy, ox, y1, PU, 1.8)
    f.rang(ox, y1, 0, -90, 10, PU)
    f.txt(ox + 8, (oy + y1) / 2 + 30, 'd', PU, 16, 'start', it=True)
    return out(f, wmm)


# =========================================================================== 14
def two_points(wmm=96):
    f = Fig(440, 230)
    y = 150
    f.line(30, y, 410, y, GY, 2)
    xb, xa, xc = 90, 190, 340
    dot(f, xb, y, 'B', 0, 26, NV, 16)
    dot(f, xa, y, 'A', 0, 26, NV, 16)
    f.line(xc, 210, xc, 20, GY, 1.6, '7 6')
    f.arrow(xc, y, xc, y - 100, AR, 4.4)
    lab(f, xc + 10, y - 80, 'F', AR, 17, 'start')
    f.rang(xc, y, 180, 90, 11, DK)
    f.dim(xb, y - 36, xa, y - 36, '0.2 m', PU, 0, 14)
    f.txt(xc + 8, 214, 'line of action', GY, 12, 'start')
    return out(f, wmm)


# =========================================================================== 15
def square_plate(wmm=72):
    f = Fig(340, 330)
    x0, y0, s = 80, 260, 190
    A, B, C, D = (x0, y0), (x0 + s, y0), (x0 + s, y0 - s), (x0, y0 - s)
    f.raw('<rect x="%d" y="%d" width="%d" height="%d" fill="#EFF6FF" stroke="#1E3A8A" stroke-width="2.6" '
          'rx="3"/>' % (x0, y0 - s, s, s))
    f.circle(x0 + s / 2, y0 - s / 2, 4.5, NV, NV, 1)
    f.txt(x0 + s / 2 + 12, y0 - s / 2 + 5, 'O', NV, 15, 'start')
    for (x, y, n, dx, dy) in ((A[0], A[1], 'A', -16, 18), (B[0], B[1], 'B', 16, 18),
                              (C[0], C[1], 'C', 16, -8), (D[0], D[1], 'D', -16, -8)):
        f.txt(x + dx, y + dy, n, NV, 16)
    f.arrow(x0 + 50, y0, x0 + 140, y0, AR, 4)
    lab(f, x0 + 95, y0 + 26, '10 N', AR, 14)
    f.arrow(x0 + s, y0 - 50, x0 + s, y0 - 140, BL, 4)
    lab(f, x0 + s + 12, y0 - 90, '20 N', BL, 14, 'start')
    f.arrow(x0 + 140, y0 - s, x0 + 50, y0 - s, GR, 4)
    lab(f, x0 + 95, y0 - s - 14, '30 N', GR, 14)
    f.arrow(x0, y0 - 140, x0, y0 - 50, OR, 4)
    lab(f, x0 - 12, y0 - 90, '40 N', OR, 14, 'end')
    f.txt(x0 + s / 2, y0 + 52, 'side = 0.4 m', PU, 14)
    return out(f, wmm)


# =========================================================================== 16
def crane(wmm=96):
    f = Fig(450, 360)
    ox, oy = 110, 290
    f.rect(40, oy + 6, 160, 50, '#FBBF24', '#92400E', 2, 8)
    f.rect(60, oy - 50, 70, 56, '#FCD34D', '#92400E', 2, 6)
    f.rect(72, oy - 40, 34, 26, '#BAE6FD', '#0369A1', 1.6, 3)
    for x in (70, 170):
        f.circle(x, oy + 58, 14, '#334155', '#0F172A', 2)
    L = 262
    bx, by = P(ox, oy, L, 53)
    f.guide(ox, oy, ox + 250, oy)
    # lattice jib
    beam(f, ox, oy, bx, by, 16, 'url(#gRod)')
    for k in range(1, 8):
        x1, y1 = P(ox, oy, L * k / 8, 53)
        f.line(x1 - 5, y1 + 6, x1 + 6, y1 - 7, '#DBEAFE', 1.4)
    f.circle(ox, oy, 7, '#fff', DK, 2.6)
    f.txt(ox + 4, oy + 28, 'O', NV, 15)
    f.angle(ox, oy, 60, 0, 53, '53&#176;', OR, 84, 14)
    f.line(bx, by, bx, by + 110, DK, 2)
    f.rect(bx - 28, by + 110, 56, 44, '#94A3B8', '#334155', 2, 4)
    f.txt(bx, by + 138, 'load', '#fff', 12.5)
    f.arrow(bx + 46, by + 120, bx + 46, by + 186, AR, 4)
    lab(f, bx + 56, by + 168, '5000 N', AR, 14, 'start')
    f.txt(bx + 6, by - 12, 'B', NV, 15, 'start')
    lab(f, (ox + bx) / 2 - 36, (oy + by) / 2 - 6, '12 m', PU, 14, 'end')
    return out(f, wmm)


# =========================================================================== 17
def forearm(wmm=100):
    f = Fig(470, 290)
    ex, ey = 90, 170
    f.raw('<path d="M%d,%d L%d,%d" stroke="#FCD9B6" stroke-width="44" stroke-linecap="round"/>'
          % (ex - 10, 30, ex, ey))
    f.raw('<path d="M%d,%d L%d,%d" stroke="#FBC99A" stroke-width="34" stroke-linecap="round"/>'
          % (ex, ey, ex + 320, ey))
    f.raw('<path d="M%d,%d L%d,%d" stroke="#B45309" stroke-opacity="0.35" stroke-width="2"/>' % (ex, ey, ex + 320, ey))
    f.circle(ex, ey, 7, '#fff', DK, 2.6)
    f.txt(ex - 30, ey + 8, 'E', NV, 16)
    bx = ex + 40
    f.raw('<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="#DC2626" stroke-width="7" stroke-linecap="round" '
          'opacity="0.55"/>' % (ex - 6, 50, ex + 38, 100, bx, ey - 12))
    f.arrow(bx, ey - 14, bx, ey - 110, AR, 4.2)
    lab(f, bx + 10, ey - 88, 'biceps 250 N', AR, 14, 'start')
    hx = ex + 320
    f.circle(hx, ey - 34, 26, 'url(#gBall)', '#9A3412', 2)
    f.arrow(hx, ey + 22, hx, ey + 84, BL, 4)
    lab(f, hx - 10, ey + 72, '30 N', BL, 14, 'end')
    f.dim(ex, ey + 44, bx, ey + 44, '4 cm', PU, 0, 13)
    f.dim(ex, ey + 104, hx, ey + 104, '32 cm', PU, 0, 14)
    f.guide(hx, ey + 30, hx, ey + 110)
    f.guide(ex, ey + 10, ex, ey + 110)
    return out(f, wmm)


# =========================================================================== 18
def wheel(wmm=78):
    f = Fig(420, 340)
    cx, cy, R = 225, 170, 110
    f.circle(cx, cy, R + 8, '#1F2937', '#111827', 2)
    f.circle(cx, cy, R, '#F1F5F9', '#475569', 2.4)
    for k in range(8):
        f.line(cx, cy, *P(cx, cy, R, k * 45), c='#CBD5E1', w=3)
    f.circle(cx, cy, 8, '#fff', DK, 2.6)
    f.txt(cx + 14, cy + 22, 'O', NV, 15, 'start')
    f.arrow(cx, cy - R - 8, cx + 90, cy - R - 8, AR, 4)
    lab(f, cx + 64, cy - R - 22, '50 N', AR, 14)
    f.arrow(cx + R + 80, cy, cx + R + 10, cy, GR, 4)
    lab(f, cx + R + 44, cy - 14, '80 N', GR, 14)
    f.arrow(cx, cy + R + 8, cx + 90, cy + R + 8, BL, 4)
    lab(f, cx + 64, cy + R + 32, '40 N', BL, 14)
    lx, ly = cx - R - 8, cy
    fx, fy = P(lx, ly, 90, 150)
    f.arrow(lx, ly, fx, fy, OR, 4)
    f.guide(lx, ly, lx - 70, ly)
    f.angle(lx, ly, 34, 150, 180, '30&#176;', DK, 52, 13)
    lab(f, fx - 4, fy - 12, '60 N', OR, 14)
    f.line(cx, cy, cx + R * 0.7, cy + R * 0.7, PU, 2)
    lab(f, cx + 62, cy + 44, 'r = 0.3 m', PU, 13, 'start')
    return out(f, wmm)


# =========================================================================== 19
def door_two(wmm=110):
    f = Fig(480, 262)
    hx, hy, L = 70, 130, 340
    f.rect(20, 30, 40, 190, 'url(#hWall)', '#64748B', 1.6, 2)
    f.raw('<rect x="%d" y="%d" width="%d" height="16" rx="3" fill="url(#gWood)" stroke="#92400E" '
          'stroke-width="2"/>' % (hx, hy - 8, L))
    f.circle(hx, hy, 8, '#fff', DK, 2.6)
    ex, ey = hx + L, hy - 8
    fx, fy = P(ex, ey, 110, 150)
    f.arrow(ex, ey, fx, fy, AR, 4)
    f.guide(ex, ey, ex - 90, ey)
    f.angle(ex, ey, 44, 150, 180, '30&#176;', OR, 64, 13)
    lab(f, fx - 6, fy - 12, 'student 1', AR, 13.5)
    mx = hx + L / 2
    f.arrow(mx, hy + 8, mx, hy + 86, BL, 4)
    lab(f, mx + 10, hy + 70, 'student 2', BL, 13.5, 'start')
    f.dim(hx, 246, hx + L, 246, '1 m', PU, 0, 14)
    f.guide(hx + L, hy + 10, hx + L, 252)
    return out(f, wmm)


# =========================================================================== 20
def pipe_extension(wmm=112):
    f = Fig(500, 220)
    cx, cy = 70, 130
    hexp = [P(cx, cy, 26, 30 + 60 * k) for k in range(6)]
    f.poly(hexp, 'url(#gSteel)', '#334155', 2.2)
    f.circle(cx, cy, 9, '#E2E8F0', '#334155', 2)
    f.raw('<rect x="%d" y="%d" width="140" height="20" rx="10" fill="url(#gSteel)" stroke="#334155" '
          'stroke-width="2"/>' % (cx + 24, cy - 10))
    f.raw('<rect x="%d" y="%d" width="240" height="30" rx="6" fill="#A16207" fill-opacity="0.85" '
          'stroke="#713F12" stroke-width="2"/>' % (cx + 140, cy - 15))
    f.txt(cx + 280, cy + 5, 'pipe', '#fff', 13)
    ex = cx + 380
    fx, fy = P(ex, cy, 110, 120)
    f.arrow(ex, cy - 12, fx, fy, AR, 4.4)
    f.angle(ex, cy - 12, 34, 120, 180, '60&#176;', OR, 54, 13)
    lab(f, fx - 8, fy - 8, '300 N', AR, 15, 'end')
    f.dim(cx, cy + 50, ex, cy + 50, '0.6 m', PU, 0, 14)
    f.guide(ex, cy + 16, ex, cy + 58)
    return out(f, wmm)


# =========================================================================== 21
def axes_pq(wmm=74):
    f = Fig(340, 330)
    ox, oy, s = 70, 270, 250          # 1 m = 250 px
    f.arrow(ox, oy, ox + 250, oy, DK, 2.2)
    f.arrow(ox, oy, ox, oy - 250, DK, 2.2)
    f.txt(ox + 256, oy + 5, 'x', NV, 16, 'start', it=True)
    f.txt(ox - 4, oy - 256, 'y', NV, 16, 'end', it=True)
    f.txt(ox - 12, oy + 20, 'O', NV, 16)
    px, qy = ox + 0.6 * s, oy - 0.8 * s
    f.line(px + 30, oy + 40, ox - 20, qy - 50, GY, 1.6, '7 6')
    dot(f, px, oy, 'P (0.6 m, 0)', 20, 24, NV, 13)
    dot(f, ox, qy, 'Q (0, 0.8 m)', 60, -8, NV, 13)
    ux, uy = -0.6, -0.8
    f.arrow(px, oy, px + ux * 110, oy + uy * 110, AR, 4.4)
    lab(f, px - 20, oy - 110, '50 N', AR, 15, 'start')
    return out(f, wmm)


# =========================================================================== 22
def components(wmm=80):
    f = Fig(400, 300)
    ox, oy, s = 110, 240, 400
    ax, ay = ox + 0.5 * s * 0.6, oy - 0.2 * s * 0.6
    f.line(ox, oy, ox + 290, oy, GY, 1.6)
    f.circle(ox, oy, 7, '#fff', DK, 2.6)
    f.txt(ox - 14, oy + 22, 'O', NV, 16)
    f.guide(ax, ay, ax, oy)
    f.guide(ox, ay, ax, ay)
    f.dim(ox, oy + 30, ax, oy + 30, '0.5 m', PU, 0, 14)
    f.dim(ox - 30, oy, ox - 30, ay, '', PU, 0, 14)
    f.txt(ox - 40, (oy + ay) / 2 + 5, '0.2 m', PU, 13.5, 'end')
    f.arrow(ax, ay, ax + 90, ay, BL, 4)
    lab(f, ax + 60, ay + 24, '30 N', BL, 14)
    f.arrow(ax, ay, ax, ay - 120, AR, 4)
    lab(f, ax + 10, ay - 90, '40 N', AR, 14, 'start')
    dot(f, ax, ay, 'A', -14, 20)
    return out(f, wmm)


# =========================================================================== 23
def seesaw(wmm=112):
    f = Fig(520, 220)
    cx, cy, s = 260, 120, 140          # 1 m = 140 px
    beam(f, cx - 230, cy, cx + 230, cy, 12, 'url(#gWood)')
    f.poly([(cx, cy + 6), (cx - 30, cy + 70), (cx + 30, cy + 70)], '#94A3B8', DK, 2)
    f.line(cx - 60, cy + 70, cx + 60, cy + 70, DK, 3)
    lx, rx = cx - 1.5 * s, cx + 1.2 * s
    for x, w, c in ((lx, '300 N', AR), (rx, '450 N', BL)):
        f.circle(x, cy - 52, 13, '#FDE68A', '#92400E', 2)
        f.rect(x - 14, cy - 38, 28, 30, c, c, 1, 8)
        f.arrow(x, cy + 8, x, cy + 70, c, 4)
        lab(f, x, cy + 92, w, c, 14)
    f.dim(lx, cy - 84, cx, cy - 84, '1.5 m', PU, 0, 14)
    f.dim(cx, cy - 84, rx, cy - 84, '1.2 m', PU, 0, 14)
    return out(f, wmm)


# =========================================================================== 24
def rod_phi(wmm=68):
    f = Fig(360, 320)
    ox, oy, L = 100, 270, 220
    ax, ay = P(ox, oy, L, 90 - 37)
    f.guide(ox, oy, ox, oy - 250)
    beam(f, ox, oy, ax, ay)
    pin(f, ox, oy)
    f.angle(ox, oy, 60, 53, 90, '37&#176;', OR, 82, 14)
    f.arrow(ax, ay, ax + 90, ay, AR, 4.4)
    lab(f, ax + 50, ay - 14, '25 N', AR, 15)
    f.txt(ax - 6, ay - 12, 'A', NV, 16, 'end')
    lab(f, (ox + ax) / 2 + 16, (oy + ay) / 2 + 12, '0.8 m', PU, 14, 'start')
    return out(f, wmm)


# =========================================================================== 26
def sign_pole(wmm=100):
    f = Fig(470, 370)
    wx, py, L = 50, 222, 330
    f.rect(10, 20, 40, 330, 'url(#hWall)', '#64748B', 1.6, 2)
    beam(f, wx, py, wx + L, py, 12, 'url(#gSteel)')
    bx = wx + L
    cy = py - L * math.tan(math.radians(30))
    f.line(bx, py, wx, cy, DK, 2.4)
    f.circle(wx, cy, 5, DK, DK, 1)
    f.angle(bx, py, 56, 150, 180, '30&#176;', OR, 76, 14)
    f.arrow(bx, py, *P(bx, py, 90, 150), c=AR, w=4)
    lab(f, bx - 110, py - 70, 'T', AR, 16)
    f.line(bx, py + 6, bx, py + 30, DK, 2.4)
    f.rect(bx - 55, py + 30, 110, 46, '#FDE68A', '#92400E', 2.2, 8)
    f.txt(bx, py + 60, 'SHOP', '#92400E', 16)
    f.arrow(bx, py + 80, bx, py + 118, BL, 4)
    lab(f, bx + 12, py + 112, '60 N', BL, 13.5, 'start')
    mx = wx + L / 2
    f.arrow(mx, py + 6, mx, py + 60, GR, 4)
    lab(f, mx + 8, py + 56, '40 N', GR, 13.5, 'start')
    f.txt(wx + 12, py + 28, 'A', NV, 15, 'start')
    f.txt(bx + 12, py + 6, 'B', NV, 15, 'start')
    f.dim(wx, 356, bx, 356, '2 m', PU, 0, 14)
    return out(f, wmm)


# =========================================================================== 27
def moment_arm(wmm=86):
    f = Fig(400, 280)
    ox, oy = 70, 220
    s = 500                                    # px per metre
    # P at 0.5 m along a rod at 0 deg ; the line of action is 0.3 m from O
    px, py = ox + 0.5 * s * 0.6, oy
    beam(f, ox, oy, px + 10, oy, 10)
    pin(f, ox, oy)
    # the line of action : through P, at distance 0.3*0.6*s from O
    d = 0.3 * s * 0.6
    ang = math.degrees(math.asin(0.3 / 0.5))      # angle between rod and force line
    # direction of the force (up-left), making ang with the rod : 180 - ang
    th = 180 - ang
    ux, uy = math.cos(math.radians(th)), -math.sin(math.radians(th))
    f.line(px - ux * 60, py - uy * 60, px + ux * 260, py + uy * 260, GY, 1.6, '7 6')
    f.arrow(px, py, px + ux * 120, py + uy * 120, AR, 4.4)
    lab(f, px + ux * 120 + 10, py + uy * 120 - 6, 'F = 20 N', AR, 14, 'start')
    # foot of the perpendicular from O
    t = (ox - px) * ux + (oy - py) * uy
    fxp, fyp = px + ux * t, py + uy * t
    f.line(ox, oy, fxp, fyp, PU, 2.4)
    lab(f, (ox + fxp) / 2 - 12, (oy + fyp) / 2, '0.3 m', PU, 13.5, 'end')
    dot(f, px, py, 'P', 10, 24)
    f.dim(ox, oy + 50, px, oy + 50, '0.5 m', OR, 0, 13.5)
    return out(f, wmm)


# =========================================================================== 30
def trapdoor(wmm=100):
    f = Fig(460, 292)
    ox, oy, L = 60, 180, 330
    f.rect(10, oy + 8, 50, 60, 'url(#hWall)', '#64748B', 1.4, 0)
    f.rect(ox + L + 10, oy + 8, 60, 60, 'url(#hWall)', '#64748B', 1.4, 0)
    f.raw('<rect x="%d" y="%d" width="%d" height="16" rx="3" fill="url(#gWood)" stroke="#92400E" '
          'stroke-width="2"/>' % (ox, oy - 8, L))
    f.circle(ox, oy, 8, '#fff', DK, 2.6)
    f.txt(ox - 4, oy - 20, 'O', NV, 15)
    ax = ox + L
    rx, ry = P(ax, oy - 8, 170, 150)
    f.line(ax, oy - 8, rx, ry, '#78350F', 3)
    f.arrow(ax, oy - 8, *P(ax, oy - 8, 100, 150), c=AR, w=4.4)
    f.guide(ax, oy - 8, ax - 110, oy - 8)
    f.angle(ax, oy - 8, 52, 150, 180, '30&#176;', OR, 72, 14)
    lab(f, ax - 40, oy - 100, 'T = 150 N', AR, 14)
    f.txt(ax + 14, oy - 12, 'A', NV, 15, 'start')
    gx = ox + L / 2
    f.arrow(gx, oy + 8, gx, oy + 70, BL, 4)
    lab(f, gx + 8, oy + 62, 'W = 120 N', BL, 13.5, 'start')
    f.dim(ox, oy + 100, ax, oy + 100, '1.2 m', PU, 0, 14)
    return out(f, wmm)


# =========================================================================== 31
def rod_c(wmm=100):
    f = Fig(460, 190)
    ax, y, L = 50, 110, 360
    beam(f, ax, y, ax + L, y, 12)
    cx = ax + 0.3 * L
    f.arrow(cx, y - 8, cx, y - 90, AR, 4.4)
    lab(f, cx + 10, y - 66, '20 N', AR, 15, 'start')
    for x, n in ((ax, 'A'), (ax + L, 'B'), (cx, 'C')):
        dot(f, x, y, n, 0, 30)
    f.dim(ax, y + 50, cx, y + 50, '0.3 m', PU, 0, 13.5)
    f.dim(cx, y + 50, ax + L, y + 50, '0.7 m', OR, 0, 13.5)
    return out(f, wmm)


# =========================================================================== 32
def rod_40_70(wmm=86):
    f = Fig(400, 356)
    ox, oy, L = 60, 300, 250
    ax, ay = P(ox, oy, L, 40)
    f.guide(ox, oy, ox + 300, oy)
    beam(f, ox, oy, ax, ay)
    pin(f, ox, oy)
    f.angle(ox, oy, 56, 0, 40, '40&#176;', OR, 78, 14)
    fx, fy = P(ax, ay, 110, 70)
    f.guide(ax, ay, ax + 80, ay)
    f.arrow(ax, ay, fx, fy, AR, 4.4)
    f.angle(ax, ay, 34, 0, 70, '70&#176;', OR, 54, 13)
    lab(f, fx - 8, fy - 8, '20 N', AR, 15, 'end')
    f.txt(ax + 16, ay + 14, 'A', NV, 16, 'start')
    lab(f, (ox + ax) / 2 + 14, (oy + ay) / 2 + 22, '1.5 m', PU, 14, 'start')
    return out(f, wmm)


# =========================================================================== 33
def graph_m_f(wmm=88):
    f = Fig(420, 300)
    x0, y0, W, H = 70, 250, 290, 190
    graph_axes(f, x0, y0, W, H, [0, 10, 20, 30, 40, 50, 60], [0, 6, 12, 18],
               'F (N)', 'M (N&#183;m)', 60, 18)
    f.line(x0, y0, x0 + W, y0 - H * 18 / 18, '#DC2626', 3.4)     # X : 0.3 m -> 18 at 60
    f.line(x0, y0, x0 + W, y0 - H * 12 / 18, '#2563EB', 3.4)     # Y : 0.2 m -> 12 at 60
    lab(f, x0 + W - 10, y0 - H - 6, 'X', '#DC2626', 16)
    lab(f, x0 + W + 14, y0 - H * 12 / 18 + 4, 'Y', '#2563EB', 16)
    return out(f, wmm)


# =========================================================================== 35
def door_53(wmm=104):
    f = Fig(470, 220)
    hx, hy, L = 70, 150, 360
    f.rect(20, 40, 40, 170, 'url(#hWall)', '#64748B', 1.6, 2)
    f.raw('<rect x="%d" y="%d" width="%d" height="16" rx="3" fill="url(#gWood)" stroke="#92400E" '
          'stroke-width="2"/>' % (hx, hy - 8, L))
    f.circle(hx, hy, 8, '#fff', DK, 2.6)
    px = hx + 250
    fx, fy = P(px, hy - 8, 110, 53)
    f.arrow(px, hy - 8, fx, fy, AR, 4.4)
    f.guide(px, hy - 8, px + 80, hy - 8)
    f.angle(px, hy - 8, 36, 0, 53, '53&#176;', OR, 56, 13)
    lab(f, fx + 8, fy + 4, '25 N', AR, 15, 'start')
    f.dim(hx, hy + 44, px, hy + 44, 'x = ?', PU, 0, 15)
    f.guide(px, hy + 10, px, hy + 52)
    return out(f, wmm)


# =========================================================================== 36
def rod_four(wmm=120):
    f = Fig(540, 280)
    ox, oy, s = 60, 150, 360
    ax = ox + s
    beam(f, ox, oy, ax, oy)
    pin(f, ox, oy)
    f.arrow(ax, oy - 6, ax, oy - 96, AR, 4)
    lab(f, ax + 8, oy - 76, '10 N', AR, 14, 'start')
    f.arrow(ax + 6, oy, ax + 84, oy, GY, 4)
    lab(f, ax + 60, oy + 26, '30 N', '#475569', 14)
    mx = ox + s / 2
    fx, fy = P(mx, oy, 100, -30)
    f.arrow(mx, oy, fx, fy, BL, 4)
    f.guide(mx, oy, mx + 80, oy)
    f.angle(mx, oy, 40, -30, 0, '30&#176;', OR, 60, 13)
    lab(f, fx + 8, fy + 4, '20 N', BL, 14, 'start')
    qx = ox + s / 4
    gx_, gy_ = P(qx, oy, 96, 53)
    f.arrow(qx, oy, gx_, gy_, GR, 4)
    f.guide(qx, oy, qx + 70, oy)
    f.angle(qx, oy, 36, 0, 53, '53&#176;', OR, 56, 13)
    lab(f, gx_ + 8, gy_ + 4, '16 N', GR, 14, 'start')
    f.txt(ax + 8, oy + 40, 'A', NV, 15, 'start')
    f.dim(ox, 250, qx, 250, '0.25 m', PU, 0, 13)
    f.dim(qx, 250, mx, 250, '0.25 m', PU, 0, 13)
    f.dim(mx, 250, ax, 250, '0.5 m', PU, 0, 13)
    return out(f, wmm)


# =========================================================================== 37
def ladder(wmm=80):
    f = Fig(380, 340)
    ox, oy, L = 80, 300, 300
    tx, ty = P(ox, oy, L, 53)
    f.rect(tx, 20, 60, oy - 20, 'url(#hWall)', '#64748B', 1.6, 0)
    f.line(20, oy, tx + 60, oy, DK, 3)
    for k in range(9):
        f.line(30 + k * 32, oy, 22 + k * 32, oy + 10, DK, 1.6)
    # two rails and the rungs
    for d in (-7, 7):
        f.line(ox + d, oy, tx + d, ty, '#92400E', 5)
    for k in range(1, 10):
        x1, y1 = P(ox, oy, L * k / 10, 53)
        f.line(x1 - 9, y1, x1 + 9, y1, '#B45309', 3)
    f.angle(ox, oy, 46, 0, 53, '53&#176;', OR, 70, 14)
    f.txt(ox - 14, oy + 22, 'O', NV, 16)
    mx, my = P(ox, oy, L * 0.6, 53)
    f.circle(mx - 30, my - 64, 11, '#FDE68A', '#92400E', 2)
    f.line(mx - 30, my - 53, mx - 22, my - 16, '#1D4ED8', 7)
    f.line(mx - 22, my - 16, mx - 4, my - 2, '#1D4ED8', 5)
    f.line(mx - 26, my - 42, mx - 2, my - 36, '#1D4ED8', 4)
    f.circle(mx, my, 5, BL, '#fff', 1.6)
    f.arrow(mx, my, mx, my + 64, BL, 4)
    lab(f, mx + 10, my + 52, '700 N', BL, 14, 'start')
    f.arrow(tx - 6, ty, tx - 96, ty, AR, 4)
    lab(f, tx - 70, ty - 16, 'R = 400 N', AR, 13.5)
    lab(f, (ox + mx) / 2 + 26, (oy + my) / 2 + 20, '3 m', PU, 14, 'start')
    return out(f, wmm)


# =========================================================================== 39
def clock(wmm=62):
    f = Fig(300, 300)
    cx, cy, R = 150, 150, 120
    f.circle(cx, cy, R + 10, '#1E3A8A', '#1E3A8A', 1)
    f.circle(cx, cy, R, '#F8FAFC', '#93C5FD', 3)
    for k in range(12):
        x1, y1 = P(cx, cy, R - 6, 90 - 30 * k)
        x2, y2 = P(cx, cy, R - (20 if k % 3 == 0 else 13), 90 - 30 * k)
        f.line(x1, y1, x2, y2, '#1E3A8A', 4 if k % 3 == 0 else 2)
    for k, n in ((0, '12'), (3, '3'), (6, '6'), (9, '9')):
        x, y = P(cx, cy, R - 38, 90 - 30 * k)
        f.txt(x, y + 7, n, '#1E3A8A', 20)
    # the minute hand pointing at 10 (i.e. at 50 minutes : 60 deg left of 12)
    hx, hy = P(cx, cy, 96, 150)
    f.line(cx, cy, hx, hy, '#0F172A', 7)
    gx, gy = P(cx, cy, 48, 150)
    f.circle(gx, gy, 4.5, AR, '#fff', 1.6)
    f.arrow(gx, gy, gx, gy + 62, AR, 3.8)
    lab(f, gx + 8, gy + 52, 'W', AR, 15, 'start')
    f.circle(cx, cy, 8, '#0F172A', '#0F172A', 1)
    return out(f, wmm)


# =========================================================================== 40
def rod_37_h(wmm=86):
    f = Fig(400, 300)
    ox, oy, L = 70, 250, 280
    ax, ay = P(ox, oy, L, 37)
    gx, gy = P(ox, oy, L / 2, 37)
    f.guide(ox, oy, ox + 300, oy)
    beam(f, ox, oy, ax, ay)
    pin(f, ox, oy)
    f.angle(ox, oy, 60, 0, 37, '37&#176;', OR, 82, 14)
    f.arrow(gx, gy, gx, gy + 76, BL, 4)
    lab(f, gx + 8, gy + 64, '50 N', BL, 14, 'start')
    f.arrow(ax - 70, ay, ax + 70, ay, AR, 3.6, both=True)
    lab(f, ax, ay - 16, 'F = ?', AR, 15)
    f.txt(ax + 10, ay + 22, 'A', NV, 15, 'start')
    lab(f, (ox + ax) / 2 + 20, (oy + ay) / 2 + 22, '1.2 m', PU, 14, 'start')
    return out(f, wmm)

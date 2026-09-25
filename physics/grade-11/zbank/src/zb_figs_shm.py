# -*- coding: utf-8 -*-
"""Original figures for the Z BANK bank : Chapter 2, Lesson 1 - Simple Harmonic Motion."""
import math
from figlib import Fig, AR, BL, GR, PU, OR, DK, GY, NV
from zb_figs import out, lab, graph_axes

EXTRA = ('<defs><linearGradient id="gBlock" x1="0" y1="0" x2="0" y2="1">'
         '<stop offset="0" stop-color="#FDBA74"/><stop offset="1" stop-color="#EA580C"/></linearGradient>'
         '<linearGradient id="gBlock2" x1="0" y1="0" x2="0" y2="1">'
         '<stop offset="0" stop-color="#93C5FD"/><stop offset="1" stop-color="#2563EB"/></linearGradient>'
         '<linearGradient id="gTable" x1="0" y1="0" x2="0" y2="1">'
         '<stop offset="0" stop-color="#E7C08A"/><stop offset="1" stop-color="#B7813F"/></linearGradient></defs>')


def _o(f, wmm):
    return out(f, wmm).replace('<defs>', EXTRA + '<defs>', 1)


def spring(f, x0, x1, y, n=9, h=13, col='#475569'):
    """a coil spring seen from the side : a looped curve between x0 and x1."""
    L = x1 - x0 - 16
    a = L / (2 * math.pi * n) * 1.9
    pts = []
    for k in range(0, 721):
        s = k / 720
        x = x0 + 8 + L * s - a * math.sin(2 * math.pi * n * s)
        yy = y - h * math.cos(2 * math.pi * n * s) * (1 if 0.02 < s < 0.98 else 0.35)
        pts.append('%.1f,%.1f' % (x, yy))
    f.line(x0, y, x0 + 9, y, col, 2.6)
    f.line(x1 - 9, y, x1, y, col, 2.6)
    f.raw('<polyline points="%s" fill="none" stroke="%s" stroke-width="3.2" stroke-linejoin="round"/>'
          % (' '.join(pts), col))
    f.raw('<polyline points="%s" fill="none" stroke="#CBD5E1" stroke-width="1.1" stroke-linejoin="round"/>'
          % ' '.join(pts))


def wall(f, x, y0, y1):
    f.rect(x - 22, y0, 22, y1 - y0, 'url(#hWall)', '#64748B', 1.4, 2)


def floor(f, x0, x1, y):
    f.line(x0, y, x1, y, DK, 2.6)
    for k in range(int((x1 - x0) / 18)):
        f.line(x0 + 10 + k * 18, y, x0 + 2 + k * 18, y + 9, GY, 1.5)


# =========================================================================== spring - block
def spring_block(wmm=112, klab='k', mlab='m', marks=True, mark_labels=('&#8722;A', '0', '+A')):
    f = Fig(520, 210)
    wx, y = 50, 118
    wall(f, wx, 50, 170)
    floor(f, wx, 500, 170)
    bx = 290                          # equilibrium position of the block's centre
    if marks:
        for dx, t in zip((-90, 0, 90), mark_labels):
            f.line(bx + dx, 36, bx + dx, 178, PU if dx else GR, 1.8, '6 5')
            lab(f, bx + dx, 30, t, PU if dx else GR, 15)
        f.txt(bx, 198, 'smooth horizontal surface', GY, 12.5, bold=False)
    spring(f, wx, bx - 40, y)
    f.raw('<rect x="%d" y="%d" width="80" height="62" rx="8" fill="url(#gBlock)" stroke="#9A3412" '
          'stroke-width="2.2"/>' % (bx - 40, 170 - 62))
    f.txt(bx, 170 - 24, mlab, '#fff', 20, it=True)
    lab(f, (wx + bx - 40) / 2, y - 26, klab, NV, 17)
    return _o(f, wmm)


# =========================================================================== graphs
def _sine(f, x0, y0, W, H, cycles, amp_px, fn=math.sin, col='#DC2626', w=3.4):
    pts = []
    for k in range(0, 401):
        s = k / 400
        pts.append('%.1f,%.1f' % (x0 + W * s, y0 - amp_px * fn(2 * math.pi * cycles * s)))
    f.raw('<polyline points="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>'
          % (' '.join(pts), col, w))


def graph_xt(wmm=92, A=4, T=0.8, cycles=1.5, ylab='x (cm)', ticks=None, points=False, fn=math.sin,
             col='#DC2626'):
    f = Fig(500, 300)
    x0, yc, W, H = 70, 150, 360, 100          # yc = the time axis
    tmax = T * cycles
    ticks = ticks or [round(T / 4 * k, 3) for k in range(0, int(cycles * 4) + 1)]
    for t in ticks:
        X = x0 + W * t / tmax
        f.line(X, yc - H - 10, X, yc + H + 10, '#E2E8F0', 1.2)
        if t:
            f.txt(X, yc + H + 30, '%g' % t, DK, 12.5, bold=False)
    for v in (-A, A):
        Y = yc - H * v / A
        f.line(x0, Y, x0 + W, Y, '#E2E8F0', 1.2)
        f.txt(x0 - 9, Y + 4.5, '%+g' % v if v < 0 else '%g' % v, DK, 12.5, 'end', bold=False)
    f.txt(x0 - 9, yc + 4.5, '0', DK, 12.5, 'end', bold=False)
    f.arrow(x0, yc, x0 + W + 24, yc, DK, 2.2)
    f.arrow(x0, yc + H + 14, x0, yc - H - 26, DK, 2.2)
    f.txt(x0 + W + 28, yc + 5, 't (s)', NV, 14, 'start')
    f.txt(x0 + 6, yc - H - 30, ylab, NV, 14, 'start')
    _sine(f, x0, yc, W, H, cycles, H, fn, col)
    if points:
        names = 'PQRST'
        for k in range(5):
            t = T / 4 * k
            X = x0 + W * t / tmax
            Y = yc - H * fn(2 * math.pi * t / T)
            f.circle(X, Y, 5.5, '#1D4ED8', '#fff', 2)
            f.txt(X + (12 if k != 4 else -12), Y - 10 if k != 3 else Y + 22, names[k], '#1D4ED8', 15,
                  'start' if k != 4 else 'end')
    return _o(f, wmm)


def graph_line(wmm=84, xt=(0, 0.05, 0.1), yt=(0, -10, -20), xl='x (m)', yl='F (N)', neg=True, pt=None,
               through=None, col='#2563EB'):
    """a straight-line graph through the origin (optionally with negative values)."""
    f = Fig(470, 300)
    x0, yc, W, H = 90, 60 if neg else 250, 280, 190
    xmax = xt[-1]
    ymax = max(abs(v) for v in yt)
    sgn = -1 if neg else 1
    for v in xt:
        X = x0 + W * v / xmax
        f.line(X, yc, X, yc + (H if neg else -H), '#E2E8F0', 1.2)
        f.txt(X, (yc - 12) if neg else (yc + 22), '%g' % v, DK, 12.5, bold=False)
    for v in yt:
        Y = yc + H * abs(v) / ymax * (1 if neg else -1)
        f.line(x0, Y, x0 + W, Y, '#E2E8F0', 1.2)
        f.txt(x0 - 9, Y + 4.5, '%g' % v, DK, 12.5, 'end', bold=False)
    f.arrow(x0, yc, x0 + W + 24, yc, DK, 2.2)
    if neg:
        f.arrow(x0, yc - 30, x0, yc + H + 24, DK, 2.2)
    else:
        f.arrow(x0, yc, x0, yc - H - 24, DK, 2.2)
    f.txt(x0 + W + 28, yc + 5, xl, NV, 14, 'start')
    f.txt(x0 + 8, (yc + H + 26) if neg else (yc - H - 30), yl, NV, 14, 'start')
    ex, ey = through
    f.line(x0, yc, x0 + W * ex / xmax, yc + (H if neg else -H) * abs(ey) / ymax, col, 3.6)
    if pt:
        X, Y = x0 + W * pt[0] / xmax, yc + (H if neg else -H) * abs(pt[1]) / ymax
        f.guide(X, yc, X, Y, '#7C3AED', 1.8)
        f.guide(x0, Y, X, Y, '#7C3AED', 1.8)
        f.circle(X, Y, 5.5, '#7C3AED', '#fff', 2)
    return _o(f, wmm)


def graph_energy(wmm=92):
    f = Fig(460, 300)
    xc, y0, W, H = 230, 250, 170, 190          # x from -A to +A ; energy up to E
    f.arrow(xc - W - 20, y0, xc + W + 30, y0, DK, 2.2)
    f.arrow(xc, y0, xc, y0 - H - 28, DK, 2.2)
    f.txt(xc + W + 34, y0 + 5, 'x', NV, 15, 'start', it=True)
    f.txt(xc + 8, y0 - H - 30, 'energy', NV, 14, 'start')
    for v, t in ((-W, '&#8722;A'), (W, '+A')):
        f.line(xc + v, y0, xc + v, y0 - H, '#E2E8F0', 1.2)
        f.txt(xc + v, y0 + 22, t, DK, 13.5)
    f.txt(xc, y0 + 22, '0', DK, 13.5)
    f.line(xc - W, y0 - H, xc + W, y0 - H, '#059669', 3)
    lab(f, xc + W + 8, y0 - H + 5, 'E', '#059669', 15, 'start')
    pe, ke = [], []
    for k in range(0, 201):
        s = -1 + 2 * k / 200
        pe.append('%.1f,%.1f' % (xc + W * s, y0 - H * s * s))
        ke.append('%.1f,%.1f' % (xc + W * s, y0 - H * (1 - s * s)))
    f.raw('<polyline points="%s" fill="none" stroke="#2563EB" stroke-width="3.4"/>' % ' '.join(pe))
    f.raw('<polyline points="%s" fill="none" stroke="#DC2626" stroke-width="3.4"/>' % ' '.join(ke))
    lab(f, xc + W - 14, y0 - H * 0.93, '(1)', '#2563EB', 14, 'end')
    lab(f, xc - W * 0.28, y0 - H * 0.93 + 30, '(2)', '#DC2626', 14)
    s = 1 / math.sqrt(2)
    for sg in (-1, 1):
        X, Y = xc + sg * W * s, y0 - H * 0.5
        f.circle(X, Y, 5.5, '#7C3AED', '#fff', 2)
        f.guide(X, Y, X, y0, '#7C3AED', 1.6)
    lab(f, xc + W * s + 12, y0 - H * 0.5 + 18, 'P', '#7C3AED', 15, 'start')
    return _o(f, wmm)


# =========================================================================== the vibrating ruler
def ruler(wmm=96):
    f = Fig(480, 240)
    ty = 120
    f.raw('<rect x="20" y="%d" width="230" height="20" rx="3" fill="url(#gTable)" stroke="#78350F" '
          'stroke-width="1.8"/>' % ty)
    f.rect(40, ty + 20, 16, 100, '#B7813F', '#78350F', 1.6, 2)
    f.rect(214, ty + 20, 16, 100, '#B7813F', '#78350F', 1.6, 2)
    for k, (c, w) in enumerate((('#1D4ED8', 150), ('#16A34A', 140), ('#DC2626', 146))):
        f.rect(60 + k * 4, ty - 26 - k * 24, w, 24, c, '#0F172A', 1.4, 3)
    f.raw('<rect x="80" y="%d" width="370" height="7" rx="2" fill="#CBD5E1" stroke="#475569" '
          'stroke-width="1.6"/>' % (ty - 7))
    for dy, op in ((-48, 0.35), (48, 0.35)):
        f.raw('<path d="M250,%d Q360,%d 450,%d" fill="none" stroke="#94A3B8" stroke-width="5" '
              'stroke-dasharray="7 5" opacity="%s"/>' % (ty - 3, ty - 3 + dy * 0.2, ty - 3 + dy, op))
    f.arrow(462, ty - 40, 462, ty + 34, PU, 2.4, both=True)
    f.txt(470, ty + 2, 'A', PU, 16, 'start', it=True)
    f.dim(250, ty + 58, 450, ty + 58, 'free length', OR, 0, 13)
    f.guide(250, ty + 4, 250, ty + 64)
    return _o(f, wmm)


# =========================================================================== two springs / two amplitudes
def two_systems(wmm=100, labs=(('k', 'm'), ('4k', 'm')), tags=('A', 'B'), disp=None):
    f = Fig(520, 270)
    for r, (klab, mlab) in enumerate(labs):
        y0 = 30 + r * 120
        wx = 60
        wall(f, wx, y0, y0 + 90)
        floor(f, wx, 470, y0 + 90)
        bx = 300 if not disp else 280
        if disp:
            f.line(bx, y0 + 18, bx, y0 + 96, GR, 1.6, '5 4')
        spring(f, wx, bx - 32, y0 + 58, 9 if r == 0 else 12, 12, '#475569' if r == 0 else '#1E40AF')
        f.raw('<rect x="%d" y="%d" width="64" height="52" rx="7" fill="url(#%s)" stroke="#1E293B" '
              'stroke-width="2"/>' % (bx - 32, y0 + 38, 'gBlock' if r == 0 else 'gBlock2'))
        f.txt(bx, y0 + 71, mlab, '#fff', 17, it=True)
        lab(f, (wx + bx - 32) / 2, y0 + 34, klab, NV, 16)
        f.txt(24, y0 + 14, tags[r], NV, 17)
        if disp:
            d = disp[r]
            f.arrow(bx, y0 + 24, bx + d * 16, y0 + 24, PU, 2.6)
            lab(f, bx + d * 8 + 8, y0 + 16, '%d cm' % d, PU, 13.5, 'start')
    return _o(f, wmm)


# =========================================================================== vertical springs
def ceiling(f, x0, x1, y):
    f.rect(x0, y - 16, x1 - x0, 16, 'url(#hWall)', '#64748B', 1.4, 2)


def vspring(f, x, y0, y1, n=9, h=11, col='#475569'):
    """a coil spring hanging from y0 down to y1 at x."""
    f.raw('<g transform="rotate(90 %.1f %.1f)">' % (x, y0))
    spring(f, x, x + (y1 - y0), y0, n, h, col)
    f.raw('</g>')


def vertical_spring(wmm=118):
    """natural length - equilibrium (stretched e) - pulled a further A and released."""
    f = Fig(660, 330)
    top = 40
    ceiling(f, 20, 540, top)
    y_nat, e, A = 140, 70, 34            # pixels : 10 cm of static stretch, 4 cm more
    for k, (cx, L, tag) in enumerate(((95, y_nat - top, '(1)'), (280, y_nat - top + e, '(2)'),
                                      (465, y_nat - top + e + A, '(3)'))):
        vspring(f, cx, top, top + L, 9, 11)
        if k:
            f.raw('<rect x="%d" y="%d" width="64" height="46" rx="7" fill="url(#gBlock)" stroke="#9A3412" '
                  'stroke-width="2.2"/>' % (cx - 32, top + L))
            f.txt(cx, top + L + 30, 'm', '#fff', 18, it=True)
        else:
            f.raw('<circle cx="%d" cy="%d" r="4.5" fill="#475569"/>' % (cx, top + L))
        f.txt(cx, 318, tag, NV, 15)
    # reference lines
    f.line(60, y_nat, 540, y_nat, GY, 1.5, '6 5')
    f.line(240, y_nat + e, 540, y_nat + e, GR, 1.5, '6 5')
    f.dim(210, y_nat, 210, y_nat + e, '', PU)
    lab(f, 188, y_nat + e / 2 + 5, '10 cm', PU, 13.5)
    f.dim(395, y_nat + e, 395, y_nat + e + A, '', OR)
    lab(f, 372, y_nat + e + A / 2 + 5, '4 cm', OR, 13.5)
    lab(f, 548, y_nat + e + 5, 'equilibrium', GR, 13, 'start')
    lab(f, 548, y_nat + 5, 'natural length', '#64748B', 13, 'start')
    return _o(f, wmm)


def cut_spring(wmm=112):
    """(1) the whole spring with the body ; (2) the two halves side by side holding the same body."""
    f = Fig(520, 300)
    top = 40
    ceiling(f, 20, 220, top)
    ceiling(f, 300, 500, top)
    vspring(f, 120, top, top + 170, 14, 11)
    f.raw('<rect x="88" y="%d" width="64" height="46" rx="7" fill="url(#gBlock)" stroke="#9A3412" '
          'stroke-width="2.2"/>' % (top + 170))
    f.txt(120, top + 200, 'm', '#fff', 18, it=True)
    lab(f, 160, top + 80, 'k', NV, 16, 'start')
    for cx in (365, 435):
        vspring(f, cx, top, top + 95, 7, 10, '#1E40AF')
        lab(f, cx + (-26 if cx < 400 else 26), top + 52, 'half', NV, 12.5, 'end' if cx < 400 else 'start')
    f.rect(340, top + 95, 120, 9, '#64748B', '#334155', 1.4, 2)
    f.line(400, top + 104, 400, top + 118, '#334155', 2.4)
    f.raw('<rect x="368" y="%d" width="64" height="46" rx="7" fill="url(#gBlock)" stroke="#9A3412" '
          'stroke-width="2.2"/>' % (top + 118))
    f.txt(400, top + 148, 'm', '#fff', 18, it=True)
    f.txt(120, 290, '(1)', NV, 15)
    f.txt(400, 290, '(2)', NV, 15)
    return _o(f, wmm)

# -*- coding: utf-8 -*-
"""Original circuit figures for the quiz on Ohm's law for a closed circuit."""
from figlib import Fig, AR, BL, GR, PU, DK, NV

WIRE = DK
RES = '#2563eb'
BAT = '#0f172a'
AFONT = '"Noto Sans Arabic", "Noto Kufi Arabic", sans-serif'


def _gap(f, x1, y1, x2, y2):
    """knock the wire out where a component sits."""
    f.raw('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#FAFCFE" stroke-width="7"/>'
          % (x1, y1, x2, y2))


def bat_v(f, x, y, pos_up=True, c=BAT):
    """a cell on a vertical wire : long thin plate = +, short thick plate = −."""
    _gap(f, x, y - 7, x, y + 7)
    yl, ys = (y - 5, y + 5) if pos_up else (y + 5, y - 5)
    f.line(x - 17, yl, x + 17, yl, c, 2.6, cap='butt')
    f.line(x - 9, ys, x + 9, ys, c, 6, cap='butt')
    f.txt(x - 24, yl + 4, '+', c, 12, 'middle')
    f.txt(x - 24, ys + 5, '−', c, 13, 'middle')


def bat_h(f, x, y, pos_left=True, c=BAT, signs=True):
    """a cell on a horizontal wire."""
    _gap(f, x - 7, y, x + 7, y)
    xl, xs = (x - 5, x + 5) if pos_left else (x + 5, x - 5)
    f.line(xl, y - 17, xl, y + 17, c, 2.6, cap='butt')
    f.line(xs, y - 9, xs, y + 9, c, 6, cap='butt')
    if signs:
        f.txt(xl + (-7 if pos_left else 7), y - 20, '+', c, 12)
        f.txt(xs + (7 if pos_left else -7), y - 13, '−', c, 13)


def res_h(f, x1, x2, y, c=RES):
    _gap(f, x1, y, x2, y)
    n, amp = 6, 8
    step = (x2 - x1) / (2 * n)
    pts = [(x1, y)] + [(x1 + step * (2 * k + 1), y + (amp if k % 2 == 0 else -amp)) for k in range(n)]
    pts.append((x2, y))
    f.raw('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.4" stroke-linejoin="round"/>'
          % (' '.join('%.1f,%.1f' % p for p in pts), c))


def res_v(f, x, y1, y2, c=RES):
    _gap(f, x, y1, x, y2)
    n, amp = 6, 8
    step = (y2 - y1) / (2 * n)
    pts = [(x, y1)] + [(x + (amp if k % 2 == 0 else -amp), y1 + step * (2 * k + 1)) for k in range(n)]
    pts.append((x, y2))
    f.raw('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.4" stroke-linejoin="round"/>'
          % (' '.join('%.1f,%.1f' % p for p in pts), c))


def meter(f, x, y, letter, c=NV):
    f.circle(x, y, 14, '#ffffff', c, 2.2)
    f.txt(x, y + 5, letter, c, 14)


def iarrow(f, x, y, d, c='#059669'):
    """a small current arrowhead on a wire ; d in 'r','l','u','d'."""
    s = 7
    pts = {'r': [(x + s, y), (x - s, y - s * 0.8), (x - s, y + s * 0.8)],
           'l': [(x - s, y), (x + s, y - s * 0.8), (x + s, y + s * 0.8)],
           'u': [(x, y - s), (x - s * 0.8, y + s), (x + s * 0.8, y + s)],
           'd': [(x, y + s), (x - s * 0.8, y - s), (x + s * 0.8, y - s)]}[d]
    f.poly(pts, c, c, 1)


def vb(f, x, y, rest, c=NV, size=12.5, anchor='middle'):
    """V_B with a proper subscript, followed by the rest of the label."""
    f.raw('<text x="%.1f" y="%.1f" fill="%s" font-size="%s" font-weight="700" text-anchor="%s" '
          'font-family="Helvetica, Arial, sans-serif">V<tspan dy="3.5" font-size="%.1f">B</tspan>'
          '<tspan dy="-3.5">%s</tspan></text>' % (x, y, c, size, anchor, size * 0.72, rest))


def crop(svg, box):
    """trim the empty margin of a figure by tightening its viewBox."""
    import re
    return re.sub(r'viewBox="0 0 [0-9.]+ [0-9.]+"', 'viewBox="%d %d %d %d"' % box, svg, count=1)


def loop(f, x1, y1, x2, y2):
    f.rect(x1, y1, x2 - x1, y2 - y1, 'none', WIRE, 2.2, 0)


def node(f, x, y):
    f.circle(x, y, 3.6, WIRE, WIRE, 1)


# --------------------------------------------------------------------------- 1
def terminal_voltage(cap):
    """a cell with a voltmeter across it, an ammeter and a rheostat."""
    f = Fig(540, 300, cap, 470)
    x1, y1, x2, y2 = 190, 64, 430, 236
    loop(f, x1, y1, x2, y2)
    # the voltmeter branch across the cell
    f.line(x1, 104, 104, 104, WIRE, 2.2)
    f.line(104, 104, 104, 196, WIRE, 2.2)
    f.line(104, 196, x1, 196, WIRE, 2.2)
    node(f, x1, 104)
    node(f, x1, 196)
    meter(f, 104, 150, 'V')
    bat_v(f, x1, 150, True)
    vb(f, x1 + 26, 146, ' ,  r', anchor='start')
    meter(f, 310, y1, 'A')
    res_v(f, x2, 106, 194)
    f.arrow(x2 - 30, 196, x2 + 30, 104, DK, 2)          # the sliding contact of the rheostat
    f.txt(x2 + 38, 156, 'R', RES, 14, 'start', it=True)
    iarrow(f, 245, y1, 'r')
    f.txt(245, y1 - 14, 'I', '#059669', 13, it=True)
    return crop(f.render(), (76, 36, 412, 212))


# --------------------------------------------------------------------------- 2
def two_resistors(cap):
    """the same cell with a 2 Ω resistor, then with a 5 Ω resistor."""
    f = Fig(620, 250, cap, 560)
    for k, (R, I, lab) in enumerate((('2 Ω', '3 A', '(a)'), ('5 Ω', '1.5 A', '(b)'))):
        ox = 40 + k * 300
        x1, y1, x2, y2 = ox + 30, 54, ox + 240, 196
        loop(f, x1, y1, x2, y2)
        bat_v(f, x1, 125, True)
        vb(f, x1 + 26, 121, ' ,  r', anchor='start')
        res_v(f, x2, 90, 160)
        f.txt(x2 - 16, 130, 'R = ' + R, RES, 13, 'end')
        meter(f, (x1 + x2) / 2, y1, 'A')
        f.tbg((x1 + x2) / 2, y1 - 22, 'I = ' + I, '#059669', 12.5)
        iarrow(f, x1 + 50, y1, 'r')
        f.txt((x1 + x2) / 2, 232, lab, NV, 13)
    return crop(f.render(), (40, 18, 560, 222))


# --------------------------------------------------------------------------- 3
def six_cells(cap, rev_label='معكوس', rev_font=AFONT):
    """six identical cells in series, the fourth one connected the wrong way."""
    f = Fig(620, 250, cap, 560)
    x1, y1, x2, y2 = 50, 84, 570, 196
    loop(f, x1, y1, x2, y2)
    xs = [110 + 80 * k for k in range(6)]
    for k, x in enumerate(xs):
        bad = (k == 3)
        c = AR if bad else BAT
        if bad:
            f.rect(x - 30, y1 - 34, 60, 68, '#FEF2F2', '#FCA5A5', 1.4, 10)
            f.line(x - 30, y1, x + 30, y1, WIRE, 2.2)
        bat_h(f, x, y1, pos_left=not bad, c=c)
        f.txt(x, y1 + 36, str(k + 1), c, 12)
    f.txt(xs[3], y1 - 42, rev_label, AR, 12.5, fam=rev_font)
    res_h(f, 250, 370, y2)
    f.txt(310, y2 + 30, 'R = 6 Ω', RES, 13)
    return crop(f.render(), (40, 26, 540, 208))


# --------------------------------------------------------------------------- 4
def opposing_batteries(cap):
    """two batteries connected in series in opposition, with a voltmeter across battery (2)."""
    f = Fig(560, 330, cap, 480)
    x1, y1, x2, y2 = 110, 120, 450, 290
    loop(f, x1, y1, x2, y2)
    # battery (1) on the left side, + upwards
    bat_v(f, x1, 205, True)
    f.txt(x1 + 30, 198, '(1)', BAT, 13, 'start')
    vb(f, x1 + 30, 218, ' = 12 V', anchor='start')
    f.txt(x1 + 30, 236, 'r = 1 Ω', NV, 12.5, 'start')
    # battery (2) on the top wire, its + terminal facing battery (1)
    bx = 280
    bat_h(f, bx, y1, pos_left=True, c=AR)
    f.txt(bx, y1 + 44, '(2)', AR, 13)
    vb(f, bx, y1 + 62, ' = 6 V', c=AR)
    f.txt(bx, y1 + 80, 'r = 0.5 Ω', AR, 12.5)
    # the voltmeter across battery (2)
    f.line(bx - 50, y1, bx - 50, 58, WIRE, 2.2)
    f.line(bx - 50, 58, bx + 50, 58, WIRE, 2.2)
    f.line(bx + 50, 58, bx + 50, y1, WIRE, 2.2)
    node(f, bx - 50, y1)
    node(f, bx + 50, y1)
    meter(f, bx, 58, 'V')
    # the external resistor on the right side
    res_v(f, x2, 170, 240)
    f.txt(x2 + 18, 210, 'R = 4.5 Ω', RES, 13, 'start')
    return crop(f.render(), (76, 38, 470, 258))


# --------------------------------------------------------------------------- 5
def mixed_network(cap):
    """three batteries in series (one reversed) feeding 2 Ω in series with 6 Ω ∥ 3 Ω."""
    f = Fig(620, 330, cap, 560)
    x1, y1, y2 = 60, 70, 250
    xa, xb = 430, 540                          # the two parallel branches
    f.line(x1, y1, xb, y1, WIRE, 2.2)
    f.line(x1, y2, xb, y2, WIRE, 2.2)
    f.line(x1, y1, x1, y2, WIRE, 2.2)
    f.line(xa, y1, xa, y2, WIRE, 2.2)
    f.line(xb, y1, xb, y2, WIRE, 2.2)
    node(f, xa, y1)
    node(f, xa, y2)
    res_h(f, 190, 290, y1)
    f.txt(240, y1 - 18, '2 Ω', RES, 13)
    res_v(f, xa, 120, 200)
    f.txt(xa - 16, 164, '6 Ω', RES, 13, 'end')
    res_v(f, xb, 120, 200)
    f.txt(xb + 16, 164, '3 Ω', RES, 13, 'start')
    cells = ((140, True, '6 V', '0.5 Ω', BAT), (250, False, '4 V', '0.5 Ω', AR),
             (360, True, '10 V', '1 Ω', BAT))
    for x, fwd, e, r, c in cells:
        bat_h(f, x, y2, pos_left=fwd, c=c)
        vb(f, x, y2 + 40, ' = ' + e, c=c, size=12)
        f.txt(x, y2 + 58, 'r = ' + r, c, 12)
    return crop(f.render(), (44, 36, 540, 280))


# --------------------------------------------------------------------------- 6
def rheostat_parallel(cap):
    """a cell feeding R1 in series with R2 in parallel with a rheostat (a - slider S - b)."""
    f = Fig(640, 330, cap, 560)
    xl, xa, xb, xs = 90, 380, 520, 572
    yt, yb = 70, 290
    f.line(xl, yt, xb, yt, WIRE, 2.2)               # top wire
    f.line(xl, yt, xl, yb, WIRE, 2.2)               # left side, with the cell
    f.line(xl, yb, xs, yb, WIRE, 2.2)               # bottom wire
    f.line(xa, yt, xa, yb, WIRE, 2.2)               # branch with R2
    node(f, xa, yt)
    node(f, xa, yb)
    bat_v(f, xl, 180, True)
    vb(f, xl + 26, 176, ' ,  r', anchor='start', size=15)
    meter(f, 165, yt, 'A')
    iarrow(f, 118, yt, 'r')
    res_h(f, 225, 315, yt)
    f.raw('<text x="270" y="%d" fill="%s" font-size="17" font-weight="700" text-anchor="middle" '
          'font-family="Helvetica, Arial, sans-serif">R<tspan dy="4" font-size="12">1</tspan></text>'
          % (yt - 18, RES))
    # R2 with the voltmeter across it
    res_v(f, xa, 140, 220)
    f.raw('<text x="%d" y="186" fill="%s" font-size="17" font-weight="700" text-anchor="start" '
          'font-family="Helvetica, Arial, sans-serif">R<tspan dy="4" font-size="12">2</tspan></text>'
          % (xa + 16, RES))
    f.line(xa, 118, 322, 118, WIRE, 2.2)
    f.line(322, 118, 322, 242, WIRE, 2.2)
    f.line(322, 242, xa, 242, WIRE, 2.2)
    node(f, xa, 118)
    node(f, xa, 242)
    meter(f, 322, 180, 'V')
    # the rheostat : fixed ends a (connected) and b (free), sliding contact S
    f.line(xb, yt, xb, 128, WIRE, 2.2)
    res_v(f, xb, 128, 236)
    f.circle(xb, 128, 4, '#ffffff', WIRE, 2)
    f.circle(xb, 236, 4, '#ffffff', WIRE, 2)
    f.txt(xb - 14, 134, 'a', NV, 17, 'end', it=True)
    f.txt(xb - 14, 242, 'b', NV, 17, 'end', it=True)
    ys = 190
    f.line(xs, ys, xs, yb, WIRE, 2.2)
    f.arrow(xs, ys, xb + 11, ys, DK, 2.4)
    f.txt(xs + 10, ys + 6, 'S', NV, 17, 'start', it=True)
    return crop(f.render(), (60, 36, 540, 270))

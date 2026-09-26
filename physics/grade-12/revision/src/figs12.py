# -*- coding: utf-8 -*-
"""Figures for the Grade 12 revision booklet - Chapter 1 : Electric current and Ohm's law."""
import math
from circ import Circ, graph, cylinder, WIRE

OHM = '&#937;'
PU = '#7c3aed'
PK = '#db2777'
BL = '#2563eb'
GR = '#059669'
OR = '#ea580c'
RD = '#e11d48'


def row(*figs):
    return '<div class="figrow">' + ''.join(figs) + '</div>'


# ============================================================ lesson 1
def g_qt_bent(cap):
    return graph(xl='t (s)', yl='Q (C)', xt=(0, 1, 2, 3, 4, 5), yt=(0, 6, 12, 18), xmax=5.4, ymax=20,
                 lines=[([(0, 0), (2, 12), (5, 18)], RD)], pts=[(2, 12, PU), (5, 18, PU)],
                 notes=[(0.35, 3.2, 'a', PU), (2.05, 14.2, 'b', PU), (5.05, 19.6, 'c', PU)], cap=cap)


def g_it_step(cap):
    return graph(xl='t (s)', yl='I (A)', xt=(0, 5, 10), yt=(0, 2, 4), xmax=11, ymax=5,
                 lines=[([(0, 4), (5, 4), (5, 2), (10, 2), (10, 0)], BL)], cap=cap)


def g_vi_angles(cap):
    f = Circ(320, 230)
    x0, y0 = 52, 192
    f.raw('<rect x="%d" y="30" width="230" height="162" fill="#f0f9ff"/><rect x="%d" y="30" width="230" height="162" '
          'fill="url(#gGrid)"/>' % (x0, x0))
    f.arrow(x0, y0, x0 + 252, y0, '#0f172a', 2.2)
    f.arrow(x0, y0, x0, 18, '#0f172a', 2.2)
    f.txt(x0 + 256, y0 + 5, 'I', '#1e3a8a', 14, 'start', it=True)
    f.txt(x0 + 8, 22, 'V', '#1e3a8a', 14, 'start', it=True)
    f.txt(x0 - 8, y0 + 15, '0', '#334155', 12, 'end', bold=False)
    for ang, c, name, L in ((60, RD, 'x', 175), (30, BL, 'y', 230)):
        x2, y2 = x0 + L * math.cos(math.radians(ang)), y0 - L * math.sin(math.radians(ang))
        f.wire((x0, y0), (x2, y2), c=c, w=3.2)
        f.lab(x2 + 8, y2 + 4, name, c, 15, 'start')
    for r, a1, a2, s in ((46, 0, 30, '30&#176;'), (78, 30, 60, '30&#176;')):
        p1 = (x0 + r * math.cos(math.radians(a1)), y0 - r * math.sin(math.radians(a1)))
        p2 = (x0 + r * math.cos(math.radians(a2)), y0 - r * math.sin(math.radians(a2)))
        f.raw('<path d="M%.1f,%.1f A%d,%d 0 0 0 %.1f,%.1f" fill="none" stroke="%s" stroke-width="1.8"/>'
              % (p1[0], p1[1], r, r, p2[0], p2[1], OR))
        am = math.radians((a1 + a2) / 2)
        f.lab(x0 + (r + 16) * math.cos(am), y0 - (r + 16) * math.sin(am) + 4, s, OR, 12)
    return f.svg(290, cap)


def g_wq_qt(cap):
    g1 = graph(xl='Q (C)', yl='W (J)', xt=(0, 5, 10, 15, 20), yt=(0, 50, 100, 150, 200), xmax=21, ymax=210,
               lines=[([(0, 0), (20, 200)], RD)], maxw=260, cap='Graph (1)')
    g2 = graph(xl='t (s)', yl='Q (C)', xt=(0, 1, 2, 3, 4), yt=(0, 5, 10, 15, 20), xmax=4.2, ymax=21,
               lines=[([(0, 0), (4, 20)], BL)], maxw=260, cap='Graph (2)')
    return row(g1, g2) + '<div class="fcap">%s</div>' % cap


def two_rods_mass(cap):
    f = Circ(420, 150)
    cylinder(f, 60, 45, 270, 22, 'x', llab='3 L')
    cylinder(f, 60, 112, 90, 22, 'y', llab='L')
    f.lab(350, 50, 'm = 4 g', '#b45309', 13.5, 'start')
    f.lab(170, 117, 'm = 12 g', '#b45309', 13.5, 'start')
    return f.svg(390, cap)


def four_wires(cap):
    f = Circ(430, 210)
    spec = (('a', 60, 12), ('b', 120, 12), ('c', 60, 24), ('d', 120, 36))
    xb = 70
    for k, (n, L, d) in enumerate(spec):
        x = xb + k * 92
        top = 170 - L
        rx = d / 2
        f.raw('<rect x="%.1f" y="%d" width="%d" height="%d" fill="url(#gCu)" stroke="#78350f" stroke-width="1.2"/>'
              % (x - rx, top, d, L))
        f.raw('<ellipse cx="%d" cy="%d" rx="%.1f" ry="%.1f" fill="#fde2c4" stroke="#78350f" stroke-width="1.2"/>'
              % (x, top, rx, rx * 0.35))
        f.raw('<ellipse cx="%d" cy="170" rx="%.1f" ry="%.1f" fill="url(#gCu)" stroke="#78350f" stroke-width="1.2"/>'
              % (x, rx, rx * 0.35))
        f.txt(x, 196, n, '#0f172a', 15)
        f.lab(x, top - 12, {12: 'A', 24: '2A', 36: '3A'}[d], '#b45309', 13)
    f.arrow(30, 170, 30, 110, PU, 1.8, both=True)
    f.lab(30, 145, 'L', PU, 13)
    f.arrow(14, 170, 14, 50, PU, 1.8, both=True)
    f.lab(14, 115, '2L', PU, 12)
    f.wire((24, 50), (400, 50), c='#cbd5e1', w=1.2, dash='5 4')
    f.wire((24, 110), (400, 110), c='#cbd5e1', w=1.2, dash='5 4')
    return f.svg(370, cap)


def hollow(cap):
    f = Circ(420, 170)
    cx, cy = 90, 85
    f.raw('<circle cx="%d" cy="%d" r="54" fill="url(#gCu)" stroke="#78350f" stroke-width="1.6"/>' % (cx, cy))
    f.raw('<circle cx="%d" cy="%d" r="36" fill="#fff" stroke="#78350f" stroke-width="1.6"/>' % (cx, cy))
    f.arrow(cx, cy, cx + 36 * 0.6, cy - 36 * 0.8, PU, 1.8)
    f.lab(cx + 4, cy + 18, 'r&#8321; = 2 mm', PU, 12)
    f.arrow(cx, cy, cx - 54, cy, BL, 1.8)
    f.lab(cx - 30, cy - 8, '', BL, 12)
    f.lab(cx, cy + 70, 'r&#8322; = 3 mm (outer)', BL, 12)
    f.raw('<path d="M190,62 L360,62 A12,23 0 0 1 360,108 L190,108 A12,23 0 0 1 190,62 z" fill="url(#gCu)" '
          'stroke="#78350f" stroke-width="1.4"/>')
    f.raw('<ellipse cx="190" cy="85" rx="12" ry="23" fill="#fde2c4" stroke="#78350f" stroke-width="1.4"/>')
    f.raw('<ellipse cx="190" cy="85" rx="7.5" ry="15" fill="#fff" stroke="#78350f" stroke-width="1.2"/>')
    f.arrow(190, 128, 360, 128, PU, 1.8, both=True)
    f.lab(275, 133, 'L = 2 m', PU, 13)
    f.txt(90, 16, 'end view', '#475569', 12, bold=False, it=True)
    return f.svg(380, cap)


def half_cylinder(cap):
    f = Circ(400, 190)
    # a prism whose cross-section is a semicircle, drawn in oblique view
    dx, dy = 190, -95
    x0, y0, r = 60, 150, 36
    f.raw('<path d="M%d,%d A%d,%d 0 0 1 %d,%d L%d,%d A%d,%d 0 0 0 %d,%d z" fill="url(#gCu)" stroke="#78350f" '
          'stroke-width="1.4"/>' % (x0 - r + dx, y0 + dy, r, r, x0 + r + dx, y0 + dy, x0 + r, y0, r, r, x0 - r, y0))
    f.raw('<path d="M%d,%d L%d,%d L%d,%d L%d,%d z" fill="#fbbf24" fill-opacity=".55" stroke="#78350f" '
          'stroke-width="1.4"/>' % (x0 - r, y0, x0 + r, y0, x0 + r + dx, y0 + dy, x0 - r + dx, y0 + dy))
    f.raw('<path d="M%d,%d A%d,%d 0 0 1 %d,%d z" fill="#fde2c4" stroke="#78350f" stroke-width="1.6"/>'
          % (x0 - r, y0, r, r, x0 + r, y0))
    f.arrow(x0 - r, y0 + 14, x0 + r, y0 + 14, PU, 1.8, both=True)
    f.lab(x0, y0 + 30, 'd = 4 mm', PU, 13)
    f.arrow(x0 + r + 16, y0 + 4, x0 + r + dx + 16, y0 + dy + 4, BL, 1.8, both=True)
    f.lab(x0 + r + dx / 2 + 40, y0 + dy / 2 + 8, 'L = 1.57 m', BL, 13)
    return f.svg(330, cap)


def g_R_L(cap):
    return graph(xl='L (m)', yl='R (&#937;)', xt=(0, 10, 20, 30, 40), yt=(0, 3, 6, 9, 12), xmax=42, ymax=13,
                 lines=[([(0, 0), (40, 12)], RD)], pts=[(40, 12, PU)], cap=cap)


def g_P_I2(cap):
    return graph(xl='I&#178; (A&#178;)', yl='P (W)', xt=(0, 3, 6, 9), yt=(0, 12, 24, 36), xmax=9.8, ymax=40,
                 lines=[([(0, 0), (9, 36)], OR)], pts=[(9, 36, PU)], cap=cap)


def rheostat_meters(cap):
    f = Circ(300, 190)
    f.comp('B', (40, 40), (260, 40), 'V<sub>B</sub> , r = 0', pos='l')
    f.comp('Rv', (260, 40), (260, 150), 'R<sub>v</sub>', side=-1)
    f.comp('A', (260, 150), (40, 150))
    f.wire((40, 150), (40, 40))
    f.node(260, 72)
    f.node(260, 128)
    f.wire((260, 72), (205, 72), (205, 128), (260, 128))
    f.raw('')
    f.comp('V', (205, 72), (205, 128))
    return f.svg(250, cap)


def mini(kind, lab):
    """a small sketch graph used inside the choices."""
    f = Circ(150, 95)
    f.arrow(24, 80, 142, 80, '#0f172a', 1.8)
    f.arrow(24, 80, 24, 8, '#0f172a', 1.8)
    if kind == 'inv':
        p = [(30 + k * 2.2, 80 - 62 / (1 + k * 0.12)) for k in range(50)]
        p = [(x, 14 + 60 * (1 / (1 + (x - 30) * 0.09))) for x, _ in p]
    elif kind == 'lin':
        p = [(24, 80), (130, 16)]
    elif kind == 'flat':
        p = [(24, 34), (135, 34)]
    else:          # rising curve
        p = [(30 + k * 2.1, 80 - 0.024 * (k * 2.1) ** 2) for k in range(50)]
    if kind == 'inv':
        p = [(30 + k * 2.1, 18 + 55 / (1 + k * 0.18)) for k in range(50)]
    f.wire(*p, c=RD, w=2.8)
    f.txt(28, 11, lab, '#1e3a8a', 10.5, 'start')
    f.txt(140, 93, 'R<sub>v</sub>', '#1e3a8a', 10.5, 'end')
    return ('<svg viewBox="0 0 150 95" xmlns="http://www.w3.org/2000/svg" style="width:118px;vertical-align:middle">'
            + ''.join(f.o) + '</svg>')


# ============================================================ lesson 2
def four_arrangements(cap):
    f = Circ(560, 250)
    def R(p1, p2):
        f.comp('R', p1, p2, body=34)
    # (1) all in series
    x, y = 20, 45
    f.term(x, y); R((x, y), (x + 60, y)); R((x + 60, y), (x + 120, y)); R((x + 120, y), (x + 180, y))
    R((x + 180, y), (x + 240, y)); f.term(x + 240, y)
    f.txt(x + 120, y + 30, '(1)', '#7c3aed', 13)
    # (2) all in parallel
    x, y = 310, 20
    f.term(x, y + 45); f.wire((x, y + 45), (x + 25, y + 45))
    f.term(x + 215, y + 45); f.wire((x + 190, y + 45), (x + 215, y + 45))
    f.wire((x + 25, y), (x + 25, y + 90)); f.wire((x + 190, y), (x + 190, y + 90))
    for k in range(4):
        R((x + 25, y + k * 30), (x + 190, y + k * 30))
    f.txt(x + 108, y + 115, '(2)', '#7c3aed', 13)
    # (3) two parallel pairs in series
    x, y = 20, 165
    f.term(x, y + 20); f.wire((x, y + 20), (x + 20, y + 20))
    for gx in (x + 20, x + 135):
        f.wire((gx, y), (gx, y + 40)); f.wire((gx + 95, y), (gx + 95, y + 40))
        R((gx, y), (gx + 95, y)); R((gx, y + 40), (gx + 95, y + 40))
    f.wire((x + 115, y + 20), (x + 135, y + 20))
    f.term(x + 250, y + 20); f.wire((x + 230, y + 20), (x + 250, y + 20))
    f.txt(x + 125, y + 72, '(3)', '#7c3aed', 13)
    # (4) three in series, parallel to one
    x, y = 310, 165
    f.term(x, y + 20); f.wire((x, y + 20), (x + 20, y + 20)); f.wire((x + 20, y), (x + 20, y + 40))
    f.wire((x + 200, y), (x + 200, y + 40)); f.wire((x + 200, y + 20), (x + 220, y + 20)); f.term(x + 220, y + 20)
    R((x + 20, y), (x + 80, y)); R((x + 80, y), (x + 140, y)); R((x + 140, y), (x + 200, y))
    R((x + 20, y + 40), (x + 200, y + 40))
    f.txt(x + 110, y + 72, '(4)', '#7c3aed', 13)
    return f.svg(520, cap)


def cut_six(cap):
    f = Circ(420, 150)
    f.term(20, 75, 'a', dy=-12); f.wire((20, 75), (45, 75))
    for gx in (45, 225):
        f.wire((gx, 30), (gx, 120)); f.wire((gx + 130, 30), (gx + 130, 120))
        for k in range(3):
            f.comp('R', (gx, 30 + 45 * k), (gx + 130, 30 + 45 * k), body=44)
    f.wire((175, 75), (225, 75))
    f.wire((355, 75), (400, 75)); f.term(400, 75, 'b', dy=-12)
    return f.svg(360, cap)


def divider(cap):
    f = Circ(330, 150)
    f.wire((20, 75), (80, 75)); f.cur(50, 75, 'r', 'I = 2 A', ldy=-12)
    f.wire((80, 30), (80, 120)); f.wire((250, 30), (250, 120))
    f.comp('R', (80, 30), (250, 30), '6 ' + OHM)
    f.comp('R', (80, 120), (250, 120), '3 ' + OHM, side=-1)
    f.wire((250, 75), (310, 75))
    f.cur(120, 30, 'r', 'I&#8321;', ldy=-12); f.node(80, 75); f.node(250, 75)
    return f.svg(290, cap)


def shorted(cap):
    f = Circ(470, 150)
    f.term(20, 70, 'a', dy=-12)
    f.comp('R', (20, 70), (110, 70), '2 ' + OHM)
    f.wire((110, 30), (110, 110)); f.wire((250, 30), (250, 110))
    f.comp('R', (110, 30), (250, 30), '6 ' + OHM)
    f.comp('R', (110, 110), (250, 110), '3 ' + OHM, side=-1)
    f.comp('R', (250, 70), (380, 70), '4 ' + OHM, side=-1)
    f.wire((270, 70), (270, 22), (360, 22), (360, 70), c='#db2777')
    f.node(270, 70); f.node(360, 70)
    f.lab(315, 14, 'connecting wire', '#db2777', 11.5)
    f.wire((380, 70), (440, 70)); f.term(440, 70, 'b', dy=-12)
    return f.svg(420, cap)


def bridge(cap, labs=('2 ' + OHM, '4 ' + OHM, '3 ' + OHM, '6 ' + OHM), mid='10 ' + OHM, ends=('a', 'b')):
    f = Circ(380, 210)
    a, t, b, bt = (40, 105), (190, 30), (340, 105), (190, 180)
    f.term(a[0] - 22, a[1], ends[0], dy=-12); f.wire((a[0] - 22, a[1]), a)
    f.term(b[0] + 22, b[1], ends[1], dy=-12); f.wire(b, (b[0] + 22, b[1]))
    f.comp('R', a, t, labs[0], body=46)
    f.comp('R', t, b, labs[1], body=46)
    f.comp('R', a, bt, labs[2], side=-1, body=46)
    f.comp('R', bt, b, labs[3], side=-1, body=46)
    if mid:
        f.comp('R', t, bt, mid, side=-1, body=46)
    for p in (a, t, b, bt):
        f.node(*p)
    return f.svg(330, cap)


def series_voltmeter(cap):
    f = Circ(330, 190)
    f.comp('B', (40, 40), (290, 40), '12 V , r = 0', pos='l')
    f.wire((290, 40), (290, 110))
    f.comp('R', (290, 110), (165, 110), '4 ' + OHM, side=-1)
    f.comp('R', (165, 110), (40, 110), '2 ' + OHM, side=-1)
    f.wire((40, 110), (40, 40))
    f.node(290, 110); f.node(165, 110)
    f.wire((290, 110), (290, 165)); f.wire((165, 110), (165, 165))
    f.comp('V', (165, 165), (290, 165))
    return f.svg(280, cap)


def volt_parallel(cap):
    f = Circ(360, 210)
    f.comp('B', (40, 180), (320, 180), '', pos='r')
    f.wire((40, 180), (40, 60))
    f.comp('R', (40, 60), (140, 60), '2 ' + OHM)
    f.wire((140, 30), (140, 95)); f.wire((320, 30), (320, 180))
    f.comp('R', (140, 30), (320, 30), '6 ' + OHM)
    f.comp('R', (140, 95), (320, 95), '4 ' + OHM, side=-1)
    f.node(140, 60); f.node(320, 95)
    f.node(58, 60); f.node(122, 60)
    f.wire((58, 60), (58, 135)); f.wire((122, 60), (122, 135))
    f.comp('V', (58, 135), (122, 135), body=26)
    return f.svg(300, cap)


def lamps_switch(cap):
    f = Circ(360, 220)
    f.comp('B', (40, 190), (320, 190), 'r = 0', pos='r')
    f.wire((40, 190), (40, 40))
    f.comp('L', (40, 40), (140, 40), 'A')
    f.wire((140, 40), (140, 150)); f.wire((320, 40), (320, 190))
    f.comp('L', (140, 40), (320, 40), 'B')
    f.comp('L', (140, 95), (320, 95), 'C')
    f.wire((140, 150), (190, 150))
    f.comp('S', (190, 150), (240, 150), 'K', side=-1)
    f.comp('L', (240, 150), (320, 150), 'D', side=-1)
    for p in ((140, 40), (140, 95), (320, 95), (320, 40), (320, 150)):
        f.node(*p)
    return f.svg(300, cap)


def ab_network(cap):
    f = Circ(430, 170)
    f.term(20, 85, 'a', dy=-12)
    f.comp('R', (20, 85), (130, 85), '2 ' + OHM)
    f.node(130, 85, 'c')
    f.wire((130, 35), (130, 135)); f.wire((380, 35), (380, 135))
    f.comp('R', (130, 35), (380, 35), '6 ' + OHM)
    f.comp('R', (130, 135), (255, 135), '4 ' + OHM, side=-1)
    f.comp('R', (255, 135), (380, 135), '8 ' + OHM, side=-1)
    f.node(380, 85); f.wire((380, 85), (410, 85)); f.term(410, 85, 'b', dy=-12)
    return f.svg(390, cap)


def overlap_rods(cap):
    f = Circ(420, 160)
    cylinder(f, 90, 105, 260, 40, None, grad='gAl')
    cylinder(f, 90, 63, 130, 22, None, grad='gCu')
    f.txt(80, 68, 'x', '#b45309', 15, 'end')
    f.lab(290, 110, 'y', '#0f172a', 14)
    f.wire((40, 105), (90, 105)); f.term(40, 105, 'a', dy=-12)
    f.wire((357, 105), (395, 105)); f.term(395, 105, 'b', dy=-12)
    f.arrow(90, 25, 220, 25, PU, 1.8, both=True); f.lab(155, 30, 'L', PU, 13)
    f.arrow(90, 145, 350, 145, PU, 1.8, both=True); f.lab(220, 150, '2L', PU, 13)
    return f.svg(380, cap)


def three_series_v(cap):
    f = Circ(380, 230)
    y = 70
    f.comp('B', (40, 200), (340, 200), 'V<sub>B</sub> , r = 0', pos='r', side=-1)
    f.wire((40, 200), (40, y)); f.wire((340, 200), (340, y))
    f.comp('R', (40, y), (140, y), 'R', side=-1)
    f.comp('R', (140, y), (240, y), '2R', side=-1)
    f.comp('R', (240, y), (340, y), '3R', side=-1)
    for x in (52, 140, 240, 328):
        f.node(x, y)
    f.wire((52, y), (52, 25)); f.wire((240, y), (240, 25))
    f.comp('V', (52, 25), (240, 25), 'V&#8322;', loff=0, shift=0, body=26)
    f.wire((140, y), (140, 125)); f.wire((328, y), (328, 125))
    f.comp('V', (140, 125), (328, 125), 'V&#8321;', side=-1, body=26)
    return f.svg(330, cap)


def net12(cap):
    f = Circ(360, 200)
    f.comp('B', (40, 170), (320, 170), '12 V , r = 0', pos='r', side=-1)
    f.wire((40, 170), (40, 50))
    f.comp('R', (40, 50), (150, 50), '4 ' + OHM)
    f.wire((150, 25), (150, 90)); f.wire((320, 25), (320, 170))
    f.comp('R', (150, 25), (320, 25), '6 ' + OHM)
    f.comp('R', (150, 90), (320, 90), '12 ' + OHM, side=-1)
    f.node(150, 50); f.node(320, 90)
    return f.svg(300, cap)


def g_vi_combo(cap):
    return graph(xl='I (A)', yl='V (V)', xt=(0, 1, 2, 3), yt=(0, 3, 6, 9), xmax=3.3, ymax=10,
                 lines=[([(0, 0), (1, 9)], RD, '1'), ([(0, 0), (1.5, 9)], OR, '2'), ([(0, 0), (3, 9)], BL, '3'),
                        ([(0, 0), (3.3, 3.3 * 2.25)], GR, '4')], pts=[(2, 4.5, GR)], cap=cap)


def short_switch(cap):
    f = Circ(340, 200)
    f.comp('B', (40, 175), (300, 175), '12 V , r = 0', pos='r', side=-1)
    f.wire((40, 175), (40, 75))
    f.comp('R', (40, 75), (150, 75), '4 ' + OHM, side=-1)
    f.comp('R', (150, 75), (300, 75), '8 ' + OHM, side=-1)
    f.comp('A', (300, 75), (300, 175))
    f.node(150, 75); f.node(250, 75)
    f.wire((150, 75), (150, 35)); f.comp('S', (150, 35), (250, 35), 'K'); f.wire((250, 35), (250, 75))
    return f.svg(280, cap)


def unknown_R(cap):
    f = Circ(360, 200)
    f.comp('B', (40, 170), (320, 170), '24 V , r = 0', pos='r', side=-1)
    f.wire((40, 170), (40, 50))
    f.comp('A', (40, 50), (100, 50))
    f.comp('R', (100, 50), (170, 50), '2 ' + OHM, body=40)
    f.wire((170, 25), (170, 90)); f.wire((320, 25), (320, 170))
    f.comp('R', (170, 25), (320, 25), 'R = ?')
    f.comp('R', (170, 90), (320, 90), '12 ' + OHM, side=-1)
    f.node(170, 50); f.node(320, 90)
    return f.svg(300, cap)


def burnout(cap):
    f = Circ(340, 200)
    f.comp('B', (40, 170), (300, 170), 'r = 0', pos='r', side=-1)
    f.wire((40, 170), (40, 55))
    f.comp('L', (40, 55), (130, 55), 'A')
    f.wire((130, 30), (130, 95)); f.wire((300, 30), (300, 170))
    f.comp('L', (130, 30), (300, 30), 'B')
    f.comp('L', (130, 95), (300, 95), 'C', side=-1)
    f.node(130, 55); f.node(300, 95)
    return f.svg(280, cap)


def ring(cap):
    f = Circ(300, 210)
    cx, cy, r = 150, 105, 75
    f.raw('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="#f97316" stroke-width="7" opacity=".35"/>' % (cx, cy, r))
    f.raw('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="#c2410c" stroke-width="3"/>' % (cx, cy, r))
    a = (cx - r, cy)
    b = (cx, cy - r)
    f.wire((20, cy), a); f.term(20, cy, 'a', dy=-12)
    f.wire(b, (cx, 12)); f.term(cx, 12, 'b', dx=14, dy=5)
    f.node(*a); f.node(*b)
    f.raw('<path d="M%.1f,%.1f A%d,%d 0 0 1 %.1f,%.1f" fill="none" stroke="#7c3aed" stroke-width="2" '
          'stroke-dasharray="5 4" transform="translate(-10 -10)"/>' % (a[0], a[1], r, r, b[0], b[1]))
    f.lab(cx - 70, cy - 58, '&#188; of the ring', PU, 12)
    f.lab(cx, cy + 5, 'R(ring) = 16 ' + OHM, '#c2410c', 13)
    return f.svg(250, cap)


def twisted(cap):
    f = Circ(380, 200)
    a, b = (40, 100), (340, 100)
    TL, TR, BL, BR = (80, 30), (300, 30), (80, 170), (300, 170)
    f.term(a[0] - 20, a[1], 'a', dy=-12); f.wire((a[0] - 20, a[1]), a)
    f.term(b[0] + 20, b[1], 'b', dy=-12); f.wire(b, (b[0] + 20, b[1]))
    f.wire(TL, a, BL); f.wire(TR, b, BR)
    f.comp('R', TL, TR, '6 ' + OHM)
    f.comp('R', BL, BR, '3 ' + OHM, side=-1)
    f.comp('R', TL, BR, '6 ' + OHM, side=1, loff=20)
    for p in (TL, TR, BL, BR, a, b):
        f.node(*p)
    return f.svg(330, cap)


def switch_branch(cap):
    f = Circ(340, 200)
    f.comp('B', (40, 170), (300, 170), '12 V , r = 0', pos='r', side=-1)
    f.wire((40, 170), (40, 40)); f.comp('A', (40, 40), (100, 40), '', )
    f.wire((100, 40), (300, 40))
    f.wire((300, 40), (300, 170))
    f.wire((140, 40), (140, 115)); f.wire((240, 40), (240, 115))
    f.node(140, 40); f.node(240, 40)
    f.comp('R', (140, 115), (140, 170), '6 ' + OHM, side=-1)
    f.comp('R', (240, 115), (240, 170), '3 ' + OHM, side=1)
    f.comp('S', (240, 40), (240, 115), 'K', side=1, body=30)
    f.node(140, 170); f.node(240, 170)
    return f.svg(280, cap)


def rheo_lamp(cap):
    f = Circ(330, 190)
    f.comp('B', (40, 160), (290, 160), 'r = 0', pos='r', side=-1)
    f.wire((40, 160), (40, 50))
    f.comp('Rv', (40, 50), (160, 50), 'R<sub>v</sub>')
    f.comp('L', (160, 50), (290, 50), '', )
    f.wire((290, 50), (290, 160))
    f.node(185, 50); f.node(290, 50)
    f.wire((185, 50), (185, 105)); f.wire((290, 50), (290, 105))
    f.comp('V', (185, 105), (290, 105))
    return f.svg(270, cap)


def triangle_wire(cap):
    f = Circ(300, 210)
    A, B, C = (150, 25), (40, 185), (260, 185)
    f.raw('<polygon points="%d,%d %d,%d %d,%d" fill="none" stroke="#f97316" stroke-width="7" opacity=".35"/>'
          % (A + B + C))
    f.raw('<polygon points="%d,%d %d,%d %d,%d" fill="none" stroke="#c2410c" stroke-width="3"/>' % (A + B + C))
    for p, n, dx, dy in ((A, 'x', 0, -10), (B, 'y', -12, 5), (C, 'z', 12, 5)):
        f.node(*p); f.txt(p[0] + dx, p[1] + dy, n, PU, 15)
    f.lab(150, 140, 'wire of 36 ' + OHM, '#c2410c', 13)
    return f.svg(240, cap)


# ============================================================ lesson 3
def batt_circuit(cap, blab='12 V , r = 1 ' + OHM, rlab='5 ' + OHM, volt=True, amm=False, sw=False, rv=False,
                 maxw=270):
    f = Circ(330, 200)
    f.comp('B', (60, 50), (270, 50), blab, pos='l')
    f.wire((270, 50), (270, 160))
    if amm:
        f.comp('A', (270, 110), (270, 160))
        f.wire((270, 50), (270, 110))
    if sw:
        f.comp('S', (270, 160), (180, 160), 'K', side=-1)
        f.comp('Rv' if rv else 'R', (180, 160), (60, 160), rlab, side=-1)
    else:
        f.comp('Rv' if rv else 'R', (270, 160), (60, 160), rlab, side=-1)
    f.wire((60, 160), (60, 50))
    if volt:
        f.node(110, 50); f.node(220, 50)
        f.wire((110, 50), (110, 100)); f.wire((220, 50), (220, 100))
        f.comp('V', (110, 100), (220, 100), body=26)
    return f.svg(maxw, cap)


def two_circuits(cap):
    f = Circ(460, 150)
    for x0, I, R in ((20, 'I&#8321; = 2 A', '5 ' + OHM), (250, 'I&#8322; = 1 A', '11 ' + OHM)):
        f.comp('B', (x0, 30), (x0 + 190, 30), 'V<sub>B</sub> , r', pos='l')
        f.wire((x0 + 190, 30), (x0 + 190, 120)); f.wire((x0, 120), (x0, 30))
        f.comp('R', (x0 + 190, 120), (x0, 120), R, side=-1)
        f.cur(x0 + 190, 75, 'd', I, ldx=-28, ldy=5)
    return f.svg(430, cap)


def two_batteries(cap, l1, l2, rlab, oppose=False):
    f = Circ(360, 190)
    f.comp('B', (40, 45), (180, 45), l1, pos='l')
    f.comp('B', (180, 45), (320, 45), l2, pos='r' if oppose else 'l')
    f.wire((320, 45), (320, 150)); f.wire((40, 150), (40, 45))
    f.comp('R', (320, 150), (40, 150), rlab, side=-1)
    return f.svg(310, cap)


def g_terminal(cap):
    return graph(xl='I (A)', yl='V (V)', xt=(0, 2, 4, 6), yt=(0, 4, 8, 12), xmax=6.8, ymax=13.5,
                 lines=[([(0, 12), (6, 0)], RD)], cap=cap)


def cells_reversed(cap):
    f = Circ(430, 170)
    xs = [40 + k * 58 for k in range(7)]
    for k in range(6):
        f.comp('B', (xs[k], 45), (xs[k + 1], 45), None, pos='r' if k == 3 else 'l', signs=True)
    f.lab((xs[3] + xs[4]) / 2, 20, 'reversed', RD, 11.5)
    f.wire((xs[6], 45), (xs[6], 135)); f.wire((xs[0], 135), (xs[0], 45))
    f.comp('R', (xs[6], 135), (xs[0], 135), '5 ' + OHM, side=-1)
    f.lab(210, 88, 'each cell : 2 V , 0.5 ' + OHM, '#1e3a8a', 12.5)
    return f.svg(390, cap)


def bridge_battery(cap):
    f = Circ(400, 260)
    a, t, b, bt = (70, 95), (190, 30), (310, 95), (190, 160)
    for p1, p2 in ((a, t), (t, b), (a, bt), (bt, b), (t, bt)):
        f.comp('R', p1, p2, 'R', body=42)
    for q in (a, t, b, bt):
        f.node(*q)
    f.wire(a, (30, 95), (30, 230), (100, 230)); f.wire(b, (360, 95), (360, 230), (280, 230))
    f.comp('B', (100, 230), (220, 230), 'r = 1 ' + OHM, pos='l', side=-1)
    f.comp('S', (220, 230), (280, 230), 'K', side=-1)
    f.node(120, 230); f.node(200, 230)
    f.wire((120, 230), (120, 195)); f.wire((200, 230), (200, 195))
    f.comp('V', (120, 195), (200, 195))
    return f.svg(340, cap)


def balance_A2(cap):
    f = Circ(420, 230)
    P, Q = (70, 90), (350, 90)
    f.wire(P, (70, 35), (100, 35)); f.comp('R', (100, 35), (200, 35), '2 ' + OHM)
    f.comp('R', (200, 35), (320, 35), '4 ' + OHM); f.wire((320, 35), (350, 35), Q)
    f.wire(P, (70, 145), (100, 145)); f.comp('R', (100, 145), (200, 145), '3 ' + OHM, side=-1)
    f.comp('R', (200, 145), (320, 145), 'R', side=-1); f.wire((320, 145), (350, 145), Q)
    f.node(200, 35); f.node(200, 145)
    f.comp('A', (200, 35), (200, 145), 'A&#8322;', loff=20)
    f.node(*P); f.node(*Q)
    f.wire(P, (30, 90), (30, 200), (150, 200))
    f.comp('B', (150, 200), (260, 200), '23 V , r = 1 ' + OHM, pos='l', side=-1)
    f.wire((260, 200), (300, 200)); f.comp('A', (300, 200), (390, 200), 'A&#8321;', side=-1)
    f.wire((390, 200), (390, 90), Q)
    return f.svg(360, cap)


def internal_q(cap):
    f = Circ(360, 200)
    f.comp('B', (40, 170), (320, 170), '15 V', pos='r', side=-1)
    f.wire((40, 170), (40, 60))
    f.wire((40, 30), (40, 95))
    f.comp('R', (40, 30), (190, 30), '6 ' + OHM)
    f.comp('R', (40, 95), (190, 95), '3 ' + OHM, side=-1)
    f.wire((190, 30), (190, 95)); f.node(190, 60); f.node(40, 60)
    f.cur(75, 30, 'r', '1 A', ldy=-12)
    f.comp('R', (190, 60), (320, 60), '2 ' + OHM)
    f.wire((320, 60), (320, 170))
    return f.svg(300, cap)


def segments(cap):
    f = Circ(420, 150)
    for y, n1, n2, pos, tag in ((45, 'x', 'y', 'r', '(1)'), (115, 'z', 'k', 'l', '(2)')):
        f.term(60, y, n1, dy=-12)
        f.comp('B', (60, y), (300, y), '12 V , r = 2 ' + OHM, pos=pos)
        f.term(300, y, n2, dy=-12)
        f.cur(250, y, 'r', '2 A', ldy=16)
        f.txt(20, y + 5, tag, PU, 13)
    return f.svg(380, cap)


def r1r2_volt(cap):
    f = Circ(380, 220)
    f.comp('B', (60, 60), (320, 60), 'V<sub>B</sub> , r', pos='l', side=-1)
    f.node(110, 60); f.node(270, 60)
    f.wire((110, 60), (110, 20)); f.wire((270, 60), (270, 20))
    f.comp('V', (110, 20), (270, 20))
    f.wire((320, 60), (320, 170)); f.wire((60, 170), (60, 60))
    f.comp('R', (320, 170), (190, 170), 'R&#8322;', side=-1)
    f.comp('R', (190, 170), (60, 170), 'R&#8321; = 3r', side=-1)
    f.node(170, 170); f.node(80, 170)
    f.wire((170, 170), (170, 128)); f.wire((80, 170), (80, 128))
    f.comp('V', (80, 128), (170, 128), name='V&#8321;', body=26)
    return f.svg(320, cap)


def g_invI(cap):
    return graph(xl='R (&#937;)', yl='1/I (A&#8315;&#185;)', xt=(0, 2, 4, 6, 8, 10), yt=(0, 1, 2, 3), xmax=11,
                 ymax=3.4, lines=[([(0, 0.5), (10, 3)], PK)], pts=[(10, 3, PU)], notes=[(0.9, 0.78, '0.5', PU)],
                 cap=cap)


def lamp_rheo(cap):
    f = Circ(340, 190)
    f.comp('B', (40, 160), (300, 160), '9 V , r = 1 ' + OHM, pos='r', side=-1)
    f.wire((40, 160), (40, 50))
    f.comp('L', (40, 50), (160, 50), '6 V , 3 W')
    f.comp('Rv', (160, 50), (300, 50), 'R<sub>v</sub>')
    f.wire((300, 50), (300, 160))
    return f.svg(280, cap)


# ============================================================ lesson 4
def star(cap):
    f = Circ(300, 220)
    c = (150, 110)
    arms = ((180, 'b', '5 A', 'in'), (125, 'c', 'I = ?', None), (50, 'd', '8 A', 'out'), (0, 'e', '4 A', 'in'),
            (-60, 'f', '6 A', 'out'))
    for ang, n, lab, d in arms:
        a = math.radians(ang)
        x2, y2 = c[0] + 100 * math.cos(a), c[1] - 100 * math.sin(a)
        f.wire(c, (x2, y2))
        f.txt(x2 + 12 * math.cos(a), y2 - 12 * math.sin(a) + 5, n, PU, 14)
        mx, my = c[0] + 58 * math.cos(a), c[1] - 58 * math.sin(a)
        if d:
            rot = -ang if d == 'out' else 180 - ang
            f.raw('<path d="M-7,-6 L7,0 L-7,6 z" fill="%s" transform="translate(%.1f %.1f) rotate(%.1f)"/>'
                  % (GR, mx, my, rot))
        nx, ny = -math.sin(a), -math.cos(a)
        f.lab(mx + 16 * nx, my + 16 * ny + 4, lab, GR if d else RD, 12.5)
    f.node(*c, 'a', dx=-12, dy=18)
    return f.svg(250, cap)


def split(cap):
    f = Circ(360, 160)
    f.wire((20, 80), (90, 80)); f.cur(50, 80, 'r', 'I = ?', ldy=-12)
    f.wire((90, 35), (90, 125)); f.wire((270, 35), (270, 125))
    f.comp('R', (90, 35), (270, 35), '6 ' + OHM)
    f.comp('R', (90, 125), (270, 125), '12 ' + OHM, side=-1)
    f.cur(130, 35, 'r', '2 A', ldy=-12)
    f.wire((270, 80), (340, 80)); f.node(90, 80); f.node(270, 80)
    return f.svg(320, cap)


def twoloop(cap, E1, R1, E2, R2, R3, cur=True, names=True):
    f = Circ(420, 230)
    L, M, Rr, T, B = 50, 210, 370, 40, 190
    for (p1, p2, lab) in (((L, T), (M, T), R1), ((M, T), (Rr, T), R2)):
        if lab is None:
            f.wire(p1, p2)
        else:
            f.comp('R', p1, p2, lab)
    f.comp('B', (L, B), (L, T), E1, pos='r', side=-1)
    f.comp('B', (Rr, B), (Rr, T), E2, pos='r', side=1)
    f.comp('R', (M, T), (M, B), R3, side=-1)
    f.wire((L, B), (Rr, B))
    f.node(M, T); f.node(M, B)
    if names:
        f.txt(M, T - 12, 'x', PU, 14); f.txt(M, B + 20, 'y', PU, 14)
    if cur:
        f.cur(95, T, 'r', 'I&#8321;', ldy=-13); f.cur(325, T, 'l', 'I&#8322;', ldy=-13)
        f.cur(M, 150, 'd', 'I&#8323;', ldx=18, ldy=5)
    return f.svg(360, cap)


def path_ab(cap):
    f = Circ(420, 110)
    f.term(30, 60, 'a', dy=-12)
    f.comp('R', (30, 60), (200, 60), '2 ' + OHM)
    f.cur(70, 60, 'r', '3 A', ldy=18)
    f.comp('B', (200, 60), (390, 60), '10 V , r = 0', pos='r')
    f.term(390, 60, 'b', dy=-12)
    return f.svg(380, cap)


def cube(cap):
    f = Circ(330, 290)
    s, d = 150, (70, -60)
    F0 = [(60, 250), (60 + s, 250), (60 + s, 250 - s), (60, 250 - s)]
    B0 = [(x + d[0], y + d[1]) for x, y in F0]
    edges = [(F0[i], F0[(i + 1) % 4]) for i in range(4)] + [(B0[i], B0[(i + 1) % 4]) for i in range(4)] + \
            [(F0[i], B0[i]) for i in range(4)]
    for p1, p2 in edges:
        f.comp('R', p1, p2, None, body=36, n=5)
    for pt in F0 + B0:
        f.node(*pt)
    f.wire(F0[0], (F0[0][0] - 30, F0[0][1] + 25)); f.term(F0[0][0] - 30, F0[0][1] + 25, 'a', dx=-12, dy=4)
    f.wire(B0[2], (B0[2][0] + 28, B0[2][1] - 18)); f.term(B0[2][0] + 28, B0[2][1] - 18, 'b', dx=13, dy=4)
    return f.svg(280, cap)


def unbal(cap):
    f = Circ(430, 250)
    A, C, D, B = (190, 25), (90, 120), (290, 120), (190, 215)
    f.comp('R', A, C, '1 ' + OHM, body=44)
    f.comp('R', A, D, '2 ' + OHM, side=-1, body=44)
    f.comp('R', C, B, '2 ' + OHM, body=44)
    f.comp('R', D, B, '1 ' + OHM, side=-1, body=44)
    f.comp('R', C, D, '1 ' + OHM, body=44)
    for p, n, dx, dy in ((A, 'A', 0, -8), (C, 'C', -14, 5), (D, 'D', 14, 5), (B, 'B', 0, 22)):
        f.node(*p); f.txt(p[0] + dx, p[1] + dy, n, PU, 13)
    f.wire(A, (360, 25)); f.wire(B, (360, 215))
    f.comp('B', (360, 215), (360, 25), '14 V , r = 0', pos='r', side=-1)
    return f.svg(360, cap)


def given_currents(cap):
    f = Circ(430, 210)
    f.comp('B', (40, 180), (40, 40), '36 V , r = 0', pos='r', side=1)
    f.comp('R', (40, 40), (190, 40), '2 ' + OHM)
    f.cur(170, 40, 'r', '6 A', ldy=-12)
    f.wire((190, 40), (380, 40)); f.node(220, 40); f.node(220, 180)
    f.wire((190, 40), (220, 40))
    f.comp('R', (220, 40), (220, 180), '6 ' + OHM, side=1)
    f.comp('R', (380, 40), (380, 180), 'R&#8322; = ?', side=1)
    f.cur(220, 72, 'd', 'I&#8321;', ldx=-18, ldy=5); f.cur(380, 72, 'd', 'I&#8322;', ldx=-18, ldy=5)
    f.wire((40, 180), (380, 180))
    return f.svg(350, cap)


def potentiometer(cap):
    f = Circ(380, 220)
    f.comp('B', (40, 50), (340, 50), 'V<sub>B1</sub> = 12 V , r = 0', pos='l')
    f.wire((340, 50), (340, 120)); f.wire((40, 50), (40, 120))
    f.comp('R', (40, 120), (160, 120), '4 ' + OHM, side=-1)
    f.comp('R', (160, 120), (340, 120), '8 ' + OHM, side=-1)
    f.node(160, 120); f.node(340, 120)
    f.wire((160, 120), (160, 185))
    f.comp('G', (160, 185), (250, 185))
    f.comp('B', (250, 185), (340, 185), 'V<sub>B2</sub>', pos='l', side=-1)
    f.wire((340, 185), (340, 120))
    return f.svg(320, cap)


def par_batteries(cap):
    return twoloop(cap, '6 V , 1 ' + OHM, None, '6 V , 1 ' + OHM, None, '2.5 ' + OHM, cur=False, names=False)


def branches_S(cap):
    f = Circ(440, 240)
    xs = (40, 150, 260, 380)
    T, B = 30, 200
    for k, x in enumerate(xs[:3]):
        f.comp('B', (x, B), (x, 135), 'V<sub>B</sub>', pos='r', side=-1, loff=22)
        f.comp('R', (x, 135), (x, 75), 'R', side=-1)
        if k < 2:
            f.comp('S', (x, 75), (x, T), 'K&#8322;' if k == 0 else 'K&#8321;', side=-1, body=30)
        else:
            f.wire((x, 75), (x, T))
    f.comp('R', (xs[3], T), (xs[3], B), 'S = R', side=1)
    f.wire((xs[0], T), (xs[3], T)); f.wire((xs[0], B), (xs[3], B))
    for x in xs[1:3]:
        f.node(x, T); f.node(x, B)
    return f.svg(340, cap)


def loop3(cap):
    f = Circ(380, 200)
    f.comp('B', (40, 40), (150, 40), '12 V', pos='l')
    f.comp('B', (150, 40), (260, 40), '4 V', pos='l')
    f.wire((260, 40), (340, 40))
    f.comp('R', (340, 40), (340, 165), '2 ' + OHM, side=1)
    f.comp('B', (340, 165), (190, 165), '6 V', pos='r', side=-1)
    f.comp('R', (190, 165), (40, 165), '3 ' + OHM, side=-1)
    f.wire((40, 165), (40, 40))
    f.lab(190, 105, 'all : r = 0', '#475569', 12)
    return f.svg(320, cap)


def find_E2(cap):
    f = Circ(380, 200)
    f.comp('B', (40, 45), (190, 45), '10 V , 1 ' + OHM, pos='l')
    f.comp('B', (190, 45), (340, 45), 'V<sub>B2</sub> , 1 ' + OHM, pos='r')
    f.wire((340, 45), (340, 160))
    f.comp('R', (340, 160), (230, 160), '3 ' + OHM, side=-1)
    f.comp('R', (230, 160), (120, 160), '5 ' + OHM, side=-1)
    f.comp('A', (120, 160), (40, 160))
    f.wire((40, 160), (40, 45))
    f.cur(310, 45, 'r', '2 A', ldy=18)
    return f.svg(320, cap)


def ammeters_lamps(cap):
    f = Circ(380, 210)
    f.comp('B', (40, 180), (40, 40), 'r = 0', pos='r', side=1)
    f.comp('A', (40, 40), (110, 40), 'A&#8321;')
    f.wire((110, 40), (340, 40))
    for x, n in ((160, 'A&#8322;'), (250, 'A&#8323;')):
        f.comp('L', (x, 40), (x, 110), '')
        f.comp('A', (x, 110), (x, 180), n, side=1, loff=22)
        f.node(x, 40); f.node(x, 180)
    f.comp('L', (340, 40), (340, 180), '')
    f.wire((40, 180), (340, 180))
    return f.svg(300, cap)


def vab_loop(cap):
    f = Circ(340, 190)
    f.comp('B', (40, 160), (40, 40), '12 V , r = 0', pos='r', side=-1)
    f.comp('R', (40, 40), (290, 40), '4 ' + OHM)
    f.wire((290, 40), (290, 160))
    f.comp('R', (290, 160), (40, 160), '2 ' + OHM, side=-1)
    f.node(290, 100, 'a', dx=14, dy=5)
    f.node(40, 160); f.txt(52, 182, 'b', PU, 14)
    return f.svg(260, cap)


def wheat(cap):
    f = Circ(380, 240)
    a, t, b, bt = (40, 105), (190, 30), (340, 105), (190, 180)
    f.comp('R', a, t, '10 ' + OHM, body=46)
    f.comp('R', t, b, '20 ' + OHM, body=46)
    f.comp('R', a, bt, 'R', side=-1, body=46)
    f.comp('R', bt, b, '30 ' + OHM, side=-1, body=46)
    f.comp('G', t, bt)
    for p in (a, t, b, bt):
        f.node(*p)
    f.wire(a, (15, 105), (15, 200), (120, 200)); f.wire(b, (365, 105), (365, 200), (260, 200))
    f.comp('B', (120, 200), (260, 200), 'V<sub>B</sub>', pos='l', side=-1)
    return f.svg(330, cap)


def amm_branch(cap):
    f = Circ(360, 200)
    f.comp('B', (40, 170), (320, 170), 'V<sub>B</sub> , r = 0', pos='r', side=-1)
    f.wire((40, 170), (40, 60))
    f.comp('R', (40, 60), (140, 60), '4 ' + OHM)
    f.wire((140, 25), (140, 100)); f.wire((320, 25), (320, 170))
    f.comp('R', (140, 25), (240, 25), '6 ' + OHM)
    f.comp('A', (240, 25), (320, 25))
    f.comp('R', (140, 100), (320, 100), '3 ' + OHM, side=-1)
    f.node(140, 60); f.node(320, 100)
    return f.svg(300, cap)

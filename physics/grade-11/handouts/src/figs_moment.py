# -*- coding: utf-8 -*-
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV


def f_door():
    f = Fig(560, 250, 'Fig. 1 — The same force F produces a different turning effect when its distance from the hinge changes.')
    f.rod(70, 70, 505, 70, DK, 11)
    f.circle(70, 70, 7, '#fff', DK, 2.6); f.circle(70, 70, 2.5, DK, DK, 1)
    f.txt(70, 40, 'hinge (axis of rotation)', NV, 12)
    f.txt(287, 22, 'door seen from above', GY, 11)
    for x, note, dy in ((175, 'small moment', 0), (325, 'larger moment', 0), (490, 'largest moment', 0)):
        f.parrow(x, 76, -90, 52, AR, 3.2)
        f.txt(x + 15, 128, 'F', AR, 15, 'start', it=True)
        f.txt(x, 60, note, GY, 10)
    f.guide(70, 80, 70, 232); f.guide(175, 132, 175, 182)
    f.guide(325, 132, 325, 207); f.guide(490, 132, 490, 232)
    f.dim(70, 178, 175, 178, 'd₁', PU, 0, 13, -6)
    f.dim(70, 203, 325, 203, 'd₂', PU, 0, 13, -6)
    f.dim(70, 228, 490, 228, 'd₃', PU, 0, 13, -6)
    return f.render()


def f_def():
    f = Fig(540, 235, 'Fig. 2 — Moment of the force F about the point O.  M = F × L')
    f.pivot(95, 95, 'O')
    f.rod(95, 95, 420, 95)
    f.parrow(420, 95, -90, 78, AR, 3.2)
    f.rang(420, 95, 0, -90, 13, DK)
    f.txt(438, 145, 'F', AR, 17, 'start', it=True)
    f.txt(420, 80, 'A', NV, 14)
    f.guide(420, 95, 420, 200); f.guide(95, 130, 95, 200)
    f.dim(95, 192, 420, 192, 'L  (moment arm)', PU, 0, 13, -7)
    f.arc(95, 95, 64, -14, -76, GR, 2.6, arrowhead=True)
    f.txt(200, 152, 'turns clockwise', GR, 11, 'start')
    return f.render()


def f_arm():
    f = Fig(560, 300, 'Fig. 3 — The moment arm d is the PERPENDICULAR distance from O to the line of action of F.')
    ang = 20.0
    A = (330.0, 150.0)
    v = (math.cos(math.radians(ang)), -math.sin(math.radians(ang)))
    O = (140.0, 70.0)
    p1 = (A[0] - 262 * v[0], A[1] - 262 * v[1])
    p2 = (A[0] + 195 * v[0], A[1] + 195 * v[1])
    f.guide(p1[0], p1[1], p2[0], p2[1], GY, 1.8, '7 5')
    f.txt(505, 70, 'line of action', GY, 11, 'end')
    f.arrow(A[0], A[1], A[0] + 125 * v[0], A[1] + 125 * v[1], AR, 3.2)
    f.txt(A[0] + 140 * v[0], A[1] + 140 * v[1] - 8, 'F', AR, 17, 'middle', it=True)
    f.circle(A[0], A[1], 4.5, AR, AR, 1)
    f.txt(A[0] - 10, A[1] + 26, 'A', NV, 14, 'end', it=True)
    d = (O[0] - A[0]) * v[0] + (O[1] - A[1]) * v[1]
    foot = (A[0] + d * v[0], A[1] + d * v[1])
    f.circle(O[0], O[1], 7, '#fff', DK, 2.6); f.circle(O[0], O[1], 2.5, DK, DK, 1)
    f.txt(O[0] - 4, O[1] - 14, 'O', NV, 16, 'middle', it=True)
    f.dim(O[0], O[1], foot[0], foot[1], 'd', PU, 0, 15, dy=2, dx=-16)
    f.rang(foot[0], foot[1], ang, ang + 90, 12, PU)
    return f.render()


def f_sign():
    f = Fig(560, 245, 'Fig. 4 — Sign convention used everywhere in this sheet.')
    f.guide(288, 18, 288, 215, '#cbd5e1', 1.6, '7 6')
    # (a) clockwise  -> negative
    f.pivot(95, 95, 'O'); f.rod(95, 95, 235, 95)
    f.parrow(235, 95, -90, 62, AR, 3.2); f.txt(252, 150, 'F', AR, 16, 'start', it=True)
    f.arc(95, 95, 48, -16, -104, AR, 3, arrowhead=True)
    f.txt(150, 205, '(a)  clockwise', AR, 13)
    f.txt(150, 226, 'M is NEGATIVE  ( − )', AR, 13)
    # (b) anticlockwise -> positive
    f.pivot(375, 95, 'O'); f.rod(375, 95, 515, 95)
    f.parrow(515, 95, 90, 62, AR, 3.2); f.txt(532, 40, 'F', AR, 16, 'start', it=True)
    f.arc(375, 95, 48, 16, 104, GR, 3, arrowhead=True)
    f.txt(430, 205, '(b)  anticlockwise', GR, 13)
    f.txt(430, 226, 'M is POSITIVE  ( + )', GR, 13)
    return f.render()


def f_zero():
    f = Fig(560, 215, 'Fig. 5 — Two cases in which the moment about O is zero.')
    f.guide(288, 18, 288, 175, '#cbd5e1', 1.6, '7 6')
    f.guide(40, 110, 270, 110, GY, 1.6, '6 5')
    f.pivot(115, 110, 'O'); f.rod(115, 110, 250, 110)
    f.arrow(250, 110, 152, 110, AR, 3.2)
    f.txt(210, 88, 'F', AR, 16, it=True)
    f.txt(150, 178, '(a) line of action passes', DK, 12)
    f.txt(150, 197, 'through O  ⇒  d = 0  ⇒  M = 0', DK, 12)
    f.pivot(390, 110, 'O'); f.rod(390, 110, 525, 110)
    f.parrow(390, 110, -35, 95, AR, 3.2)
    f.txt(452, 132, 'F', AR, 16, it=True)
    f.txt(430, 178, '(b) force acts at the axis', DK, 12)
    f.txt(430, 197, 'itself  ⇒  d = 0  ⇒  M = 0', DK, 12)
    return f.render()


def f_perp_tilted():
    f = Fig(500, 275, 'Fig. 6 — CASE 1: the force is perpendicular to the rod, so the moment arm is the length OA itself.')
    O = (110.0, 215.0); ang = 35.0
    A = P(O[0], O[1], 280, ang)
    f.pivot(O[0], O[1], 'O')
    f.rod(O[0], O[1], A[0], A[1])
    f.parrow(A[0], A[1], ang - 90, 95, AR, 3.2)
    f.rang(A[0], A[1], ang + 180, ang - 90, 13, DK)
    t = P(A[0], A[1], 112, ang - 90)
    f.txt(t[0] + 14, t[1] + 6, 'F', AR, 17, 'start', it=True)
    f.txt(A[0] + 4, A[1] - 12, 'A', NV, 14, 'start')
    f.dim(O[0], O[1], A[0], A[1], 'L', PU, 26, 14, dy=-4, dx=-10)
    f.txt(250, 258, 'M = F × L', '#92400e', 15)
    return f.render()


def f_resolve():
    f = Fig(560, 258, 'Fig. 7 — CASE 2 (method 1): resolve F into a component ⊥ to the rod and a component along the rod.')
    O = (100.0, 165.0); A = (390.0, 165.0); th = 50.0
    f.pivot(O[0], O[1], 'O'); f.rod(O[0], O[1], A[0], A[1])
    f.guide(A[0], A[1], A[0] + 130, A[1])
    tip = P(A[0], A[1], 132, th)
    f.arrow(A[0], A[1], tip[0], tip[1], AR, 3.2)
    f.txt(tip[0] + 12, tip[1] - 4, 'F', AR, 17, 'start', it=True)
    py = A[1] - 132 * math.sin(math.radians(th))
    px = A[0] + 132 * math.cos(math.radians(th))
    f.parrow(A[0], A[1], 90, 132 * math.sin(math.radians(th)), BL, 3)
    f.parrow(A[0], A[1], 0, 132 * math.cos(math.radians(th)), GR, 3)
    f.guide(A[0], py, tip[0], tip[1]); f.guide(px, A[1], tip[0], tip[1])
    f.txt(A[0] - 10, py + 4, 'F sin θ', BL, 13.5, 'end')
    f.txt(px + 6, A[1] + 22, 'F cos θ', GR, 13.5, 'start')
    f.angle(A[0], A[1], 46, 0, th, 'θ', OR, 66)
    f.txt(A[0] - 9, A[1] + 24, 'A', NV, 14, 'end', it=True)
    f.guide(O[0], 185, O[0], 222); f.guide(A[0], A[1] + 10, A[0], 222)
    f.dim(O[0], 218, A[0], 218, 'L', PU, 0, 14, -7)
    f.txt(500, 246, 'M = (F sin θ) × L', '#92400e', 13.5, 'end')
    return f.render()


def f_perpdist():
    f = Fig(560, 300, 'Fig. 8 — CASE 2 (method 2): drop a perpendicular from O onto the line of action:  d = L sin θ.')
    O = (100.0, 95.0); A = (380.0, 95.0); th = 30.0
    v = (math.cos(math.radians(th)), -math.sin(math.radians(th)))
    f.circle(O[0], O[1], 7, '#fff', DK, 2.6); f.circle(O[0], O[1], 2.5, DK, DK, 1)
    f.txt(O[0] - 6, O[1] - 13, 'O', NV, 16, 'middle', it=True)
    f.rod(O[0], O[1], A[0], A[1])
    f.guide(A[0], A[1], A[0] + 120, A[1])
    tip = (A[0] + 132 * v[0], A[1] + 132 * v[1])
    f.arrow(A[0], A[1], tip[0], tip[1], AR, 3.2)
    f.txt(tip[0] + 12, tip[1] - 2, 'F', AR, 17, 'start', it=True)
    dd = (O[0] - A[0]) * v[0] + (O[1] - A[1]) * v[1]
    foot = (A[0] + dd * v[0], A[1] + dd * v[1])
    f.guide(A[0], A[1], foot[0] - 28 * v[0], foot[1] - 28 * v[1], GY, 1.8, '7 5')
    f.dim(O[0], O[1], foot[0], foot[1], 'd = L sin θ', PU, 0, 13.5, dy=4, dx=-42)
    f.rang(foot[0], foot[1], th, th + 90, 12, PU)
    f.angle(A[0], A[1], 46, 0, th, 'θ', OR, 64)
    f.txt(A[0] + 4, A[1] - 12, 'A', NV, 14, 'start')
    f.dim(O[0], 60, A[0], 60, 'L', PU, 0, 14, -7)
    f.guide(O[0], 70, O[0], 88); f.guide(A[0], 70, A[0], 88)
    f.txt(470, 275, 'M = F × d = F L sin θ', '#92400e', 13.5, 'end')
    return f.render()


def f_compare():
    f = Fig(620, 235, 'Fig. 9 — Same force F, same length L, different angle θ: the moment changes with sin θ.')
    data = ((90, 'θ = 90°', 'M = F L', '(maximum)'), (60, 'θ = 60°', 'M = 0.87 F L', ''), (30, 'θ = 30°', 'M = 0.50 F L', ''))
    for k, (th, t1, t2, t3) in enumerate(data):
        x0 = 25 + k * 200
        O = (x0 + 18.0, 120.0); A = (x0 + 130.0, 120.0)
        f.circle(O[0], O[1], 6, '#fff', DK, 2.4)
        f.rod(O[0], O[1], A[0], A[1], DK, 7)
        f.guide(A[0], A[1], A[0] + 42, A[1])
        tip = P(A[0], A[1], 80, th)
        f.arrow(A[0], A[1], tip[0], tip[1], AR, 2.8)
        f.angle(A[0], A[1], 32, 0, th, None, OR)
        f.txt(x0 + 90, 168, t1, OR, 13)
        f.txt(x0 + 90, 190, t2, '#92400e', 13.5)
        if t3:
            f.txt(x0 + 90, 210, t3, GY, 11)
        if k:
            f.guide(x0 - 8, 25, x0 - 8, 200, '#e2e8f0', 1.5, '6 6')
    return f.render()


def f_net():
    f = Fig(560, 300, 'Fig. 10 — Several forces acting on the same bar: add their moments about O with the correct sign.')
    y = 115.0; O = 290.0; s = 68.0
    f.rod(130, y, 505, y, DK, 10)
    f.pivot(O, y, 'O')
    # F1 down, 2 m left  -> anticlockwise (+)
    x1 = O - 2 * s
    f.parrow(x1, y - 6, 90, 58, AR, 3)
    f.txt(x1 + 14, y - 72, '20 N', AR, 13, 'start')
    f.txt(x1 - 18, y - 30, '+', GR, 20)
    # F2 down, 1 m right -> clockwise (-)
    x2 = O + 1 * s
    f.parrow(x2, y + 6, -90, 58, AR, 3)
    f.txt(x2 + 14, y + 78, '30 N', AR, 13, 'start')
    f.txt(x2 - 16, y + 44, '−', AR, 22)
    # F3 up, 3 m right -> anticlockwise (+)
    x3 = O + 3 * s
    f.parrow(x3, y - 6, 90, 58, AR, 3)
    f.txt(x3 - 12, y - 72, '40 N', AR, 13, 'end')
    f.txt(x3 + 16, y - 30, '+', GR, 20)
    for xx, yy in ((x1, 218), (x2, 250), (x3, 282)):
        f.guide(xx, y + 12, xx, yy - 8)
    f.guide(O, y + 34, O, 288)
    f.dim(x1, 214, O, 214, '2 m', PU, 0, 12.5, -6)
    f.dim(O, 246, x2, 246, '1 m', PU, 0, 12.5, -6)
    f.dim(O, 278, x3, 278, '3 m', PU, 0, 12.5, -6)
    return f.render()


# ============================= reusable question figures =============================
def rod_fig(cap, llab, flab, th=-90, anglab=None, maxw=400, dl=250.0, flen=92.0, note=None):
    """rod hinged at O with a single force at A making angle th with the rod extension."""
    h = 250 if th < 0 else 235
    W = 520
    f = Fig(W, h, cap, maxw)
    y = 105.0 if th < 0 else 150.0
    O = (95.0, y); A = (95.0 + dl, y)
    f.pivot(O[0], O[1], 'O'); f.rod(O[0], O[1], A[0], A[1])
    f.txt(A[0] + 4, A[1] - 13, 'A', NV, 13, 'start')
    if abs(th) != 90:
        f.guide(A[0], A[1], A[0] + 95, A[1])
        f.angle(A[0], A[1], 40, 0, th, anglab or f'{abs(int(th))}°', OR, 58, 13)
    else:
        f.rang(A[0], A[1], 0, th, 12, DK)
    tip = P(A[0], A[1], flen, th)
    f.arrow(A[0], A[1], tip[0], tip[1], AR, 3.1)
    if abs(th) == 90:
        f.txt(A[0] + 16, A[1] + (58 if th < 0 else -46), flab, AR, 13.5, 'start')
    else:
        lx, ly = P(A[0], A[1], flen + 26, th)
        anch = 'middle'
        if lx > W - 62:
            anch, lx = 'end', W - 8
        elif lx < 62:
            anch, lx = 'start', 8
        f.txt(lx, ly + 5, flab, AR, 13.5, anch)
    dy = y + 118 if th < 0 else y + 55
    f.guide(O[0], y + 34, O[0], dy - 6); f.guide(A[0], A[1] + 10, A[0], dy - 6)
    f.dim(O[0], dy, A[0], dy, llab, PU, 0, 13, -7)
    if note:
        f.txt(W / 2, h - 8, note, GY, 11)
    return f.render()


def spanner(cap, llab, flab, maxw=430):
    f = Fig(500, 250, cap, maxw)
    pts = [P(110, 112, 36, a) for a in range(0, 360, 60)]
    f.poly(pts, '#cbd5e1', DK, 2.4)
    f.circle(110, 112, 14, '#94a3b8', DK, 2)
    f.txt(110, 55, 'nut', NV, 12)
    f.rect(108, 100, 285, 24, '#e2e8f0', DK, 2, 5)
    f.parrow(383, 124, -90, 66, AR, 3.2)
    f.txt(400, 200, flab, AR, 13.5, 'start')
    f.arc(110, 112, 58, -24, -104, GR, 2.8, arrowhead=True)
    f.guide(110, 152, 110, 202); f.guide(383, 128, 383, 202)
    f.dim(110, 198, 383, 198, llab, PU, 0, 13, -7)
    return f.render()


def door_top(cap, wlab, flab, th, maxw=430):
    f = Fig(580, 245, cap, maxw)
    y = 88.0
    f.rod(75, y, 420, y, DK, 11)
    f.circle(75, y, 7, '#fff', DK, 2.6); f.circle(75, y, 2.5, DK, DK, 1)
    f.txt(75, y - 20, 'hinge', NV, 12)
    f.txt(250, 28, 'door seen from above', GY, 11)
    f.guide(408, y, 408 + 85, y)
    tip = P(408, y, 100, -th)
    f.arrow(408, y, tip[0], tip[1], AR, 3.2)
    f.txt(tip[0] + 12, tip[1] + 16, flab, AR, 13.5, 'start')
    f.angle(408, y, 40, 0, -th, f'{th}°', OR, 58, 13)
    f.guide(75, y + 12, 75, 196); f.guide(408, y + 12, 408, 196)
    f.dim(75, 192, 408, 192, wlab, PU, 0, 13, -7)
    return f.render()


def bar_forces(cap, items, maxw=470):
    """items: list of (metres_from_O  (+ right / - left), 'label', 'up'|'down')"""
    n = len(items)
    h = 150 + 32 * n + 30
    f = Fig(560, h, cap, maxw)
    y = 118.0; O = 285.0; s = 62.0
    xs = [O + it[0] * s for it in items]
    f.rod(min(xs + [O]) - 40, y, max(xs + [O]) + 40, y, DK, 10)
    f.pivot(O, y, 'O')
    for (m, lab, d), x in zip(items, xs):
        if d == 'up':
            f.parrow(x, y - 6, 90, 56, AR, 3)
            f.txt(x + 13, y - 44, lab, AR, 13, 'start')
        else:
            f.parrow(x, y + 6, -90, 56, AR, 3)
            f.txt(x + 13, y + 48, lab, AR, 13, 'start')
    base = 195
    for k, ((m, lab, d), x) in enumerate(zip(items, xs)):
        yy = base + 32 * k
        f.guide(x, y + 14, x, yy - 7)
        a, b = (x, O) if m < 0 else (O, x)
        f.dim(a, yy, b, yy, f'{abs(m):g} m'.replace('.0', ''), PU, 0, 12.5, -6)
    f.guide(O, y + 34, O, base + 32 * (n - 1) - 6)
    return f.render()


def wheel(cap, rlab, flab, maxw=400):
    f = Fig(470, 255, cap, maxw)
    cx, cy, r = 215.0, 118.0, 82.0
    f.circle(cx, cy, r, '#eef2f7', DK, 3)
    f.circle(cx, cy, 16, '#cbd5e1', DK, 2.4)
    for a in (30, 90, 150):
        p1 = P(cx, cy, r, a); p2 = P(cx, cy, r, a + 180)
        f.line(p1[0], p1[1], p2[0], p2[1], '#cbd5e1', 1.8)
    f.parrow(cx + r, cy, -90, 78, AR, 3.2)
    f.txt(cx + r + 14, cy + 60, flab, AR, 13.5, 'start')
    f.rang(cx + r, cy, 180, -90, 12, DK)
    f.dim(cx, cy, cx + r, cy, '', PU, -20, 13)
    f.tbg(cx + r / 2, cy - 26, rlab, PU, 13)
    f.arc(cx, cy, r + 22, -35, -125, GR, 2.8, arrowhead=True)
    f.txt(cx, 244, 'the force is tangent to the rim  ⇒  it is ⊥ to the radius', GY, 11)
    return f.render()


def two_panel(cap, a_th, a_txt, b_th, b_txt, maxw=470):
    f = Fig(560, 225, cap, maxw)
    f.guide(285, 20, 285, 190, '#cbd5e1', 1.6, '7 6')
    for k, (th, t) in enumerate(((a_th, a_txt), (b_th, b_txt))):
        x0 = 20 + k * 285
        O = (x0 + 40.0, 110.0); A = (x0 + 175.0, 110.0)
        f.pivot(O[0], O[1], 'O'); f.rod(O[0], O[1], A[0], A[1], DK, 8)
        if th == 90:
            f.rang(A[0], A[1], 0, 90, 12, DK)
        else:
            f.guide(A[0], A[1], A[0] + 55, A[1])
            f.angle(A[0], A[1], 36, 0, th, f'{th}°', OR, 54, 12.5)
        tip = P(A[0], A[1], 78, th)
        f.arrow(A[0], A[1], tip[0], tip[1], AR, 3)
        f.txt(x0 + 105, 200, t, DK, 12.5)
    f.txt(140, 40, '(a)', GY, 13); f.txt(405, 40, '(b)', GY, 13)
    return f.render()


def f_ex7():
    f = Fig(520, 265, 'Fig. 17 — An obtuse angle:  sin 150° = sin 30° = 0.5', 440)
    O = (100.0, 180.0); A = (360.0, 180.0); th = 150.0
    v = (math.cos(math.radians(th)), -math.sin(math.radians(th)))
    f.pivot(O[0], O[1], 'O'); f.rod(O[0], O[1], A[0], A[1])
    f.guide(A[0], A[1], A[0] + 90, A[1])
    tip = (A[0] + 125 * v[0], A[1] + 125 * v[1])
    f.arrow(A[0], A[1], tip[0], tip[1], AR, 3.2)
    f.txt(252, 148, 'F = 80 N', AR, 13.5, 'end')
    f.angle(A[0], A[1], 46, 0, th, '150°', OR, 66, 13)
    dd = (O[0] - A[0]) * v[0] + (O[1] - A[1]) * v[1]
    foot = (A[0] + dd * v[0], A[1] + dd * v[1])
    f.guide(A[0], A[1], foot[0] + 30 * v[0], foot[1] + 30 * v[1], GY, 1.8, '7 5')
    f.dim(O[0], O[1], foot[0], foot[1], 'd = 0.6 m', PU, 0, 13, dy=-6, dx=-44)
    f.rang(foot[0], foot[1], th, th - 90, 11, PU)
    f.txt(A[0] + 4, A[1] + 22, 'A', NV, 13, 'start')
    f.dim(O[0], 232, A[0], 232, 'L = 1.2 m', PU, 0, 13, -7)
    f.guide(O[0], 200, O[0], 226); f.guide(A[0], 190, A[0], 226)
    return f.render()


def f_along_rod():
    f = Fig(470, 195, 'Fig. 24', 380)
    f.pivot(100, 105, 'O'); f.rod(100, 105, 330, 105)
    f.guide(60, 105, 420, 105, GY, 1.6, '6 5')
    f.arrow(330, 105, 415, 105, AR, 3.2)
    f.txt(372, 84, 'F = 70 N', AR, 13)
    f.txt(330, 92, 'A', NV, 13)
    f.guide(100, 140, 100, 170); f.guide(330, 118, 330, 170)
    f.dim(100, 166, 330, 166, 'L = 0.8 m', PU, 0, 13, -7)
    return f.render()

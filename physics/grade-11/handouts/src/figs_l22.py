# -*- coding: utf-8 -*-
"""Original figures for Lessons 2-2 and 2-3 : the vertical spring and the simple pendulum."""
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV
from figs_lesson import INK, MUT, SKY, VIO, RED, GRN, AMB, IND
from figs_l21 import _wall, _spring, _ground, COIL, WALL


def _ceiling(f, x1, x2, y, c=WALL):
    f.rect(x1, y - 10, x2 - x1, 10, '#CBD5E1', c, 2, 1)
    x = x1 + 6
    while x < x2:
        f.line(x, y, x - 7, y - 9, c, 1.3)
        x += 12


def _vspring(f, x, y1, y2, coils=10, amp=11, c=COIL, w=2.2):
    pts = [(x, y1)]
    span = y2 - y1
    for i in range(1, coils * 2):
        pts.append((x + (amp if i % 2 else -amp), y1 + span * i / float(coils * 2)))
    pts.append((x, y2))
    f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % p for p in pts) +
          '" fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>' % (c, w))


# --------------------------------------------------------------------------- 1
def vertical_spring(cap, maxw=470, w=560, h=300):
    """natural length, static extension e and the oscillation about the new equilibrium."""
    f = Fig(w, h, cap, maxw)
    top = 44.0
    _ceiling(f, 60, 460, top)
    # unloaded spring
    x1 = 140.0
    _vspring(f, x1, top, top + 96, coils=8)
    f.line(90, top + 96, 210, top + 96, GY, 1.6, '5 4')
    f.txt(86, top + 100, 'natural', MUT, 10.5, 'end')
    f.txt(86, top + 114, 'length', MUT, 10.5, 'end')
    f.txt(x1, top - 22, 'no load', MUT, 11)
    # loaded spring
    x2 = 330.0
    _vspring(f, x2, top, top + 152, coils=11)
    f.rect(x2 - 26, top + 152, 52, 34, '#3B82F6', '#1D4ED8', 2.4, 4)
    f.txt(x2, top + 174, 'm', '#FFFFFF', 14, 'middle', it=True)
    f.line(270, top + 96, 404, top + 96, GY, 1.6, '5 4')
    f.line(258, top + 152, 404, top + 152, AR, 1.8, '6 5')
    f.dim(404, top + 96, 404, top + 152, '', PU, 0, 12)
    f.tbg(416, top + 128, 'e', PU, 12, 'start')
    f.txt(x2, top - 22, 'loaded', MUT, 11)
    f.txt(254, top + 156, 'new x = 0', AR, 10.5, 'end')
    # oscillation arrows about the new equilibrium
    f.parrow(x2 + 150, top + 152, 90, 34, GR, 2.4)
    f.parrow(x2 + 150, top + 152, -90, 34, GR, 2.4)
    f.txt(x2 + 150, top + 110, 'it oscillates', GR, 10.5)
    f.txt(x2 + 150, top + 206, 'about this line', GR, 10.5)
    f.txt(w / 2, h - 12, 'the weight only moves the equilibrium position — it does not enter T',
          MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 2
def horizontal_vs_vertical(cap, maxw=480, w=560, h=270):
    """the same m and k, once horizontal and once vertical : the same periodic time."""
    f = Fig(w, h, cap, maxw)
    # left : horizontal
    y = 118.0
    _wall(f, 46, 62, 182)
    _ground(f, 37, 250, 182)
    _spring(f, 46, 170, y, coils=9, amp=10)
    f.circle(190, y, 17, '#3B82F6', '#1D4ED8', 2.4)
    f.txt(190, y + 5, 'm', '#FFFFFF', 12, 'middle', it=True)
    f.txt(140, 44, 'horizontal', INK, 12)
    f.txt(140, 210, 'the spring force alone', MUT, 10.5)
    # right : vertical
    cx = 400.0
    _ceiling(f, 320, 480, 52)
    _vspring(f, cx, 52, 140, coils=8, amp=10)
    f.rect(cx - 22, 140, 44, 30, '#3B82F6', '#1D4ED8', 2.4, 4)
    f.txt(cx, 160, 'm', '#FFFFFF', 12, 'middle', it=True)
    f.parrow(cx, 176, -90, 32, AR, 2.4)
    f.txt(cx + 12, 200, 'mg', AR, 11, 'start')
    f.txt(cx, 44, 'vertical', INK, 12)
    f.txt(cx, 232, 'the spring force and the weight', MUT, 10.5)
    f.line(288, 40, 288, 226, GY, 1.4, '5 5')
    f.tbg(w / 2, h - 12, 'both give T = 2π √( m / k )', VIO, 12)
    return f.render()


# --------------------------------------------------------------------------- 3
def pendulum_geometry(cap, Llab='L', maxw=380, w=440, h=330):
    """pivot, string of length L, bob, small angle and the arc of the swing."""
    f = Fig(w, h, cap, maxw)
    px, py = 220.0, 48.0
    L = 190.0
    _ceiling(f, 130, 310, py)
    f.circle(px, py, 5, DK, DK, 1)
    ang = 22.0
    b = (px + L * math.sin(math.radians(ang)), py + L * math.cos(math.radians(ang)))
    f.line(px, py, px, py + L, GY, 1.6, '6 5')
    f.line(px, py, b[0], b[1], DK, 2.4)
    f.circle(b[0], b[1], 17, '#3B82F6', '#1D4ED8', 2.6)
    f.txt(b[0], b[1] + 5, 'm', '#FFFFFF', 12, 'middle', it=True)
    # angle at the pivot
    f.raw('<path d="M%.1f,%.1f A54,54 0 0 0 %.1f,%.1f" fill="none" stroke="%s" stroke-width="2"/>'
          % (px, py + 54, px + 54 * math.sin(math.radians(ang)), py + 54 * math.cos(math.radians(ang)), OR))
    f.txt(px + 34, py + 44, 'θ', OR, 14, 'start', it=True)
    # the arc of the swing
    f.raw('<path d="M%.1f,%.1f A%.1f,%.1f 0 0 1 %.1f,%.1f" fill="none" stroke="#94A3B8" '
          'stroke-width="2" stroke-dasharray="7 6"/>'
          % (px - L * math.sin(math.radians(ang)) - 4, py + L * math.cos(math.radians(ang)) + 22,
             L + 22, L + 22, b[0] + 4, b[1] + 22))
    f.circle(px - L * math.sin(math.radians(ang)), py + L * math.cos(math.radians(ang)), 12,
             '#DBEAFE', '#60A5FA', 2)
    f.tbg((px + b[0]) / 2 + 24, (py + b[1]) / 2 + 4, Llab, PU, 12, 'start')
    f.txt(px, py + L + 56, 'the lowest point is the equilibrium position', MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 4
def pendulum_forces(cap, maxw=400, w=460, h=330):
    """the weight resolved along the string and along the tangent."""
    f = Fig(w, h, cap, maxw)
    px, py = 190.0, 44.0
    L = 168.0
    ang = 28.0
    a = math.radians(ang)
    _ceiling(f, 110, 280, py)
    f.circle(px, py, 5, DK, DK, 1)
    b = (px + L * math.sin(a), py + L * math.cos(a))
    f.line(px, py, px, py + L + 46, GY, 1.4, '6 5')
    f.line(px, py, b[0], b[1], DK, 2.4)
    f.circle(b[0], b[1], 15, '#3B82F6', '#1D4ED8', 2.4)
    # weight straight down
    f.arrow(b[0], b[1], b[0], b[1] + 84, AR, 3)
    f.txt(b[0] - 12, b[1] + 92, 'mg', AR, 12.5, 'end')
    # component along the string (mg cos)
    cx2 = b[0] + 84 * math.sin(a)
    cy2 = b[1] + 84 * math.cos(a)
    f.arrow(b[0], b[1], cx2, cy2, PU, 2.6, '6 4')
    f.txt(cx2 + 14, cy2 + 18, 'mg cos θ', PU, 11, 'start')
    # tangential component (mg sin), perpendicular to the string, towards the centre
    tx = b[0] - 76 * math.cos(a)
    ty = b[1] + 76 * math.sin(a)
    f.arrow(b[0], b[1], tx, ty, GR, 3)
    f.txt(tx - 4, ty + 22, 'mg sin θ', GR, 11, 'end')
    # tension
    f.parrow(b[0], b[1], 90 + ang, 62, BL, 2.6)
    f.txt(b[0] + 30, b[1] - 46, 'T', BL, 12.5, 'start', it=True)
    f.txt(px + 26, py + 40, 'θ', OR, 13, 'start', it=True)
    f.raw('<path d="M%.1f,%.1f A46,46 0 0 0 %.1f,%.1f" fill="none" stroke="%s" stroke-width="2"/>'
          % (px, py + 46, px + 46 * math.sin(a), py + 46 * math.cos(a), OR))
    f.txt(w / 2, h - 26, 'the restoring force is the tangential part :  F = − mg sin θ',
          GR, 11)
    f.txt(w / 2, h - 10, 'for a small angle  sin θ ≈ θ  , so  F ∝ − x',
          MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 5
def pendulum_timing(cap, maxw=430, w=500, h=300):
    """timing n complete oscillations with a stopwatch."""
    f = Fig(w, h, cap, maxw)
    px, py = 190.0, 46.0
    L = 150.0
    _ceiling(f, 110, 280, py)
    f.circle(px, py, 5, DK, DK, 1)
    for k, ang in enumerate((-20.0, 0.0, 20.0)):
        a = math.radians(ang)
        b = (px + L * math.sin(a), py + L * math.cos(a))
        op = '1' if ang == 0 else '0.42'
        f.raw('<g opacity="%s">' % op)
        f.line(px, py, b[0], b[1], DK, 2.2)
        f.circle(b[0], b[1], 14, '#3B82F6', '#1D4ED8', 2.4)
        f.raw('</g>')
    f.raw('<path d="M%.1f,%.1f A%.1f,%.1f 0 0 1 %.1f,%.1f" fill="none" stroke="#16A34A" '
          'stroke-width="2.2" stroke-dasharray="6 5"/>'
          % (px - L * math.sin(math.radians(20)), py + L * math.cos(math.radians(20)) + 26,
             L + 26, L + 26, px + L * math.sin(math.radians(20)), py + L * math.cos(math.radians(20)) + 26))
    f.txt(px, py + L + 52, 'one complete oscillation = there and back', GR, 10.5)
    # stopwatch
    sx, sy = 400.0, 128.0
    f.circle(sx, sy, 44, '#F8FAFC', '#334155', 3)
    f.rect(sx - 8, sy - 56, 16, 12, '#CBD5E1', '#334155', 2, 2)
    for k in range(12):
        p1 = P(sx, sy, 38, k * 30); p2 = P(sx, sy, 32, k * 30)
        f.line(p1[0], p1[1], p2[0], p2[1], '#64748B', 1.6)
    f.line(sx, sy, sx + 26, sy - 20, '#DC2626', 2.6)
    f.circle(sx, sy, 4, '#334155', '#334155', 1)
    f.tbg(sx, sy + 70, 't = 14.0 s  for  n = 10', INK, 11.5)
    f.tbg(sx, sy + 96, 'T = t / n', VIO, 12)
    f.txt(w / 2, h - 10, 'timing many oscillations divides the reaction-time error by n', MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 6
def two_pendulums(cap, l1='L = 0.25 m', l2='L = 1.00 m', maxw=440, w=500, h=306):
    """two simple pendulums of different lengths at the same place."""
    f = Fig(w, h, cap, maxw)
    top = 44.0
    _ceiling(f, 50, 450, top)
    for px, L, lab, col, note in ((150.0, 68.0, l1, '#F97316', 'short → quick'),
                                  (350.0, 190.0, l2, '#2563EB', 'long → slow')):
        a = math.radians(24)
        b = (px + L * math.sin(a), top + L * math.cos(a))
        f.line(px, top, px, top + L, GY, 1.4, '5 5')
        f.line(px, top, b[0], b[1], DK, 2.2)
        f.circle(b[0], b[1], 14, col, '#1E3A8A', 2.2)
        f.circle(px, top, 4, DK, DK, 1)
        f.tbg(px - 16, top + L / 2 + 4, lab, PU, 11, 'end')
        f.txt(b[0], b[1] + 32, note, MUT, 10.5)
    f.txt(w / 2, h - 12, 'T ∝ √L  , so the periods are in the ratio √L₁ : √L₂',
          VIO, 11)
    return f.render()

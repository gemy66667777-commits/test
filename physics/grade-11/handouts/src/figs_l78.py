# -*- coding: utf-8 -*-
"""Original figures for Lessons 1-7 (momentum & impulse) and 1-8 (conservation of momentum)."""
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV
from figs_lesson import INK, MUT, SKY, VIO, RED, GRN, AMB, IND


def _ground(f, gy, x1, x2):
    f.line(x1, gy, x2, gy, DK, 2.6)
    for x in range(int(x1) + 8, int(x2) - 4, 20):
        f.line(x, gy, x - 8, gy + 8, '#94A3B8', 1.4)


def _person(f, x, gy, col, lab, face=1):
    f.circle(x, gy - 74, 11, '#FDE68A', DK, 2)
    f.line(x, gy - 63, x, gy - 34, DK, 2.8)
    f.line(x, gy - 56, x - 14 * face, gy - 44, DK, 2.4)
    f.line(x, gy - 56, x + 12 * face, gy - 46, DK, 2.4)
    f.line(x, gy - 34, x - 11, gy - 12, DK, 2.6)
    f.line(x, gy - 34, x + 11, gy - 12, DK, 2.6)
    f.rect(x - 24, gy - 12, 48, 7, col, DK, 1.8, 3)
    f.circle(x - 15, gy - 3, 5, '#334155', DK, 1.4)
    f.circle(x + 15, gy - 3, 5, '#334155', DK, 1.4)
    f.txt(x, gy + 26, lab, col, 12)


def two_movers(cap, labA='40 kg &middot; 0.3 m/s east', labB='60 kg &middot; 0.2 m/s west',
               maxw=450, w=520, h=230):
    f = Fig(w, h, cap, maxw)
    gy = 170.0
    _ground(f, gy, 20, w - 20)
    _person(f, 130, gy, '#3B82F6', 'A', 1)
    _person(f, 370, gy, '#EF4444', 'B', -1)
    f.parrow(160, gy - 96, 0, 62, IND, 3)
    f.txt(130, gy - 108, labA.split('&middot;')[1].strip(), IND, 12)
    f.parrow(340, gy - 96, 180, 62, RED, 3)
    f.txt(372, gy - 108, labB.split('&middot;')[1].strip(), RED, 12)
    f.txt(130, gy + 44, labA.split('&middot;')[0].strip(), MUT, 11)
    f.txt(370, gy + 44, labB.split('&middot;')[0].strip(), MUT, 11)
    return f.render()


def phone_drop(cap, maxw=440, w=500, h=250):
    f = Fig(w, h, cap, maxw)
    for k, (x0, soft) in enumerate(((40.0, True), (270.0, False))):
        gy = 196.0
        f.line(x0, gy, x0 + 190, gy, DK, 2.6)
        for x in range(int(x0) + 8, int(x0) + 186, 18):
            f.line(x, gy, x - 7, gy + 7, '#94A3B8', 1.3)
        if soft:
            f.raw('<ellipse cx="%.1f" cy="%.1f" rx="66" ry="22" fill="#FEF3C7" stroke="#B45309" '
                  'stroke-width="2.2"/>' % (x0 + 95, gy - 18))
        f.rect(x0 + 74, 56, 42, 76, '#1E293B', '#0F172A', 2.4, 7)
        f.rect(x0 + 79, 62, 32, 60, '#334155', 'none', 0, 3)
        f.parrow(x0 + 95, 140, -90, 34, IND, 2.8)
        f.txt(x0 + 112, 168, 'v', IND, 12.5, 'start', it=True)
        f.txt(x0 + 95, 36, 'on a cushion' if soft else 'on a hard floor', INK, 12)
        f.txt(x0 + 95, gy + 34, 'longer stopping time' if soft else 'shorter stopping time',
              GRN if soft else RED, 11)
    return f.render()


def ball_turn(cap, v1='6 m/s east', v2='6 m/s north', maxw=360, w=420, h=250):
    f = Fig(w, h, cap, maxw)
    cx, cy = 210.0, 160.0
    f.arrow(60, cy, cx - 16, cy, IND, 3.2)
    f.txt(128, cy + 24, 'before : ' + v1, IND, 12)
    f.circle(cx, cy, 13, '#FCD34D', '#B45309', 2.4)
    f.arrow(cx, cy - 18, cx, 48, RED, 3.2)
    f.txt(cx + 14, 70, 'after : ' + v2, RED, 12, 'start')
    f.raw('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f" fill="none" stroke="#94A3B8" stroke-width="2.4" '
          'stroke-linejoin="round"/>' % (cx + 40, cy + 34, cx + 58, cy + 16, cx + 74, cy + 34))
    f.txt(cx + 57, cy + 54, 'the bat', MUT, 11)
    f.arrow(76, 66, 76, 34, '#94A3B8', 1.8); f.txt(60, 52, 'N', MUT, 12, 'end')
    return f.render()


def two_pulses(cap, lab1='F , Δt', lab2='F/2 , 2Δt', maxw=450, w=520, h=240):
    f = Fig(w, h, cap, maxw)
    for k, (x0, hgt, wid, lab) in enumerate(((40.0, 108.0, 70.0, lab1), (290.0, 54.0, 140.0, lab2))):
        gy = 190.0
        f.arrow(x0, gy, x0 + 180, gy, '#94A3B8', 1.8)
        f.arrow(x0, gy, x0, 44, '#94A3B8', 1.8)
        f.txt(x0 + 178, gy + 20, 't', MUT, 12, 'end', it=True)
        f.txt(x0 - 14, 52, 'F', MUT, 12, 'end', it=True)
        f.rect(x0 + 24, gy - hgt, wid, hgt, '#FEE2E2', RED, 2.2, 2)
        f.guide(x0, gy - hgt, x0 + 24, gy - hgt)
        f.txt(x0 + 24 + wid / 2, gy - hgt / 2 + 5, 'J = area', RED, 12)
        f.txt(x0 + 90, gy + 38, '( %d )  %s' % (k + 1, lab), INK, 12)
    return f.render()


def ft_curve(cap, maxw=420, w=480, h=250):
    f = Fig(w, h, cap, maxw)
    gy = 196.0; x0 = 60.0
    f.arrow(x0, gy, w - 30, gy, '#94A3B8', 1.8)
    f.arrow(x0, gy, x0, 40, '#94A3B8', 1.8)
    f.txt(w - 28, gy + 20, 'time (s)', MUT, 11.5, 'end')
    f.txt(x0 - 12, 50, 'F (N)', MUT, 11.5, 'end')
    pts = []
    for i in range(61):
        t = i / 60.0
        x = x0 + 40 + 280 * t
        y = gy - 120 * math.exp(-((t - 0.5) ** 2) / 0.022)
        pts.append((x, y))
    f.raw('<path d="M%.1f,%.1f ' % (pts[0][0], gy) + ' '.join('L%.1f,%.1f' % p for p in pts) +
          ' L%.1f,%.1f Z" fill="#FEE2E2" stroke="none"/>' % (pts[-1][0], gy))
    f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % p for p in pts) +
          '" fill="none" stroke="%s" stroke-width="2.6"/>' % RED)
    f.txt(x0 + 180, gy - 46, 'area = impulse', RED, 12)
    return f.render()


def tri_pulse(cap, peak=6.0, t_end=6.0, maxw=420, w=470, h=260):
    f = Fig(w, h, cap, maxw)
    gy = 200.0; x0 = 62.0
    sx = 56.0; sy = 24.0
    f.arrow(x0, gy, x0 + t_end * sx + 40, gy, '#94A3B8', 1.8)
    f.arrow(x0, gy, x0, gy - peak * sy - 40, '#94A3B8', 1.8)
    f.txt(x0 + t_end * sx + 38, gy + 20, 't (s)', MUT, 11.5, 'end')
    f.txt(x0 - 12, gy - peak * sy - 30, 'F (N)', MUT, 11.5, 'end')
    for k in range(1, int(t_end) + 1):
        f.line(x0 + k * sx, gy, x0 + k * sx, gy + 5, '#94A3B8', 1.4)
        f.txt(x0 + k * sx, gy + 20, str(k), MUT, 10.5)
    for v in (3, 6):
        f.line(x0, gy - v * sy, x0 - 5, gy - v * sy, '#94A3B8', 1.4)
        f.txt(x0 - 12, gy - v * sy + 4, str(v), MUT, 10.5, 'end')
        f.guide(x0, gy - v * sy, x0 + t_end * sx, gy - v * sy, '#E2E8F0', 1.2, '5 5')
    mid = x0 + (t_end / 2) * sx
    f.raw('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="#FEE2E2" stroke="%s" stroke-width="2.6" '
          'stroke-linejoin="round"/>' % (x0, gy, mid, gy - peak * sy, x0 + t_end * sx, gy, RED))
    f.txt(mid, gy - 46, 'area = impulse', RED, 12)
    return f.render()


def boat_person(cap, maxw=440, w=500, h=240):
    f = Fig(w, h, cap, maxw)
    wy = 186.0
    f.rect(20, wy, w - 40, 44, '#BAE6FD', 'none', 0, 0)
    for k in range(6):
        f.raw('<path d="M%d,%d q 12,-8 24,0 q 12,8 24,0" fill="none" stroke="#38BDF8" stroke-width="2"/>'
              % (40 + k * 72, wy + 16))
    bx = 250.0
    f.poly([(bx - 130, wy), (bx + 130, wy), (bx + 96, wy + 34), (bx - 96, wy + 34)],
           '#B45309', '#7C2D12', 2.6)
    _person(f, bx + 10, wy, '#3B82F6', '', 1)
    f.parrow(bx + 44, wy - 96, 0, 62, RED, 3)
    f.txt(bx + 120, wy - 104, 'the passenger', RED, 11.5, 'end')
    f.parrow(bx - 60, wy + 54, 180, 62, IND, 3)
    f.txt(bx - 130, wy + 76, 'the boat', IND, 11.5, 'start')
    return f.render()


def collide_stick(cap, m1='0.50 kg', v1='6.0 m/s', m2='1.00 kg', v2='at rest', vf='v = ?',
                  maxw=470, w=540, h=250):
    f = Fig(w, h, cap, maxw)
    gy = 168.0
    f.line(24, gy, 250, gy, '#A16207', 4)
    f.line(300, gy, w - 24, gy, '#A16207', 4)
    f.circle(72, gy - 22, 22, '#3B82F6', '#1D4ED8', 2.4)
    f.circle(168, gy - 22, 22, '#EF4444', '#991B1B', 2.4)
    f.parrow(100, gy - 22, 0, 40, RED, 2.8)
    f.txt(72, gy - 58, m1, INK, 11.5); f.txt(72, gy + 24, v1, IND, 11.5)
    f.txt(168, gy - 58, m2, INK, 11.5); f.txt(168, gy + 24, v2, MUT, 11.5)
    f.txt(272, gy - 22, '→', MUT, 22)
    f.circle(352, gy - 22, 22, '#3B82F6', '#1D4ED8', 2.4)
    f.circle(396, gy - 22, 22, '#EF4444', '#991B1B', 2.4)
    f.parrow(424, gy - 22, 0, 46, RED, 2.8)
    f.txt(374, gy + 24, 'they move together', MUT, 11.5)
    f.txt(478, gy - 34, vf, RED, 12, 'middle')
    f.txt(120, 32, 'before the collision', MUT, 11)
    f.txt(410, 32, 'after the collision', MUT, 11)
    return f.render()


def collide_2d(cap, mA, vA, mB, vB, angA, angB, maxw=460, w=530, h=300):
    f = Fig(w, h, cap, maxw)
    cx, cy = 300.0, 168.0
    f.guide(40, cy, w - 30, cy, '#94A3B8', 1.6, '8 6')
    f.circle(92, cy, 15, '#EF4444', '#991B1B', 2.2)
    f.txt(92, cy + 34, mA, INK, 11.5)
    f.parrow(112, cy, 0, 58, RED, 2.8)
    f.txt(148, cy - 14, vA, RED, 11.5)
    f.circle(cx, cy, 17, '#FCD34D', '#B45309', 2.4)
    f.txt(cx, cy + 38, mB, INK, 11.5)
    if vB:
        f.parrow(cx - 60, cy, 0, 40, AMB, 2.6)
        f.txt(cx - 40, cy - 14, vB, AMB, 11.5)
    ta = P(cx, cy, 118, angA)
    f.arrow(cx + 14, cy - 6, ta[0], ta[1], '#DC2626', 3)
    f.circle(ta[0] + 8, ta[1] - 6, 13, '#EF4444', '#991B1B', 2.2)
    f.txt(ta[0] + 8, ta[1] - 26, 'A', INK, 12)
    f.angle(cx, cy, 52, 0, angA, '%g°' % angA, OR, 72, 12)
    tb = P(cx, cy, 112, -abs(angB))
    f.arrow(cx + 14, cy + 6, tb[0], tb[1], '#B45309', 3)
    f.circle(tb[0] + 8, tb[1] + 8, 14, '#FCD34D', '#B45309', 2.2)
    f.txt(tb[0] + 8, tb[1] + 32, 'B', INK, 12)
    f.angle(cx, cy, 78, 0, -abs(angB), '%g°' % abs(angB), OR, 96, 12)
    return f.render()


def explosion(cap, mt='9.0 kg', m1='5.0 kg', v1='8.0 m/s', m2='4.0 kg', v2='v = ?',
              maxw=450, w=510, h=295):
    f = Fig(w, h, cap, maxw)
    f.line(24, 96, w - 24, 96, '#475569', 4)
    f.circle(w / 2, 74, 20, '#64748B', '#334155', 2.4)
    f.txt(w / 2, 46, mt + '  (at rest)', INK, 12)
    f.txt(w / 2, 126, 'before the explosion', MUT, 11)
    gy = 210.0
    f.line(24, gy, w - 24, gy, '#475569', 4)
    f.raw('<path d="M%.1f,%.1f l 10,-16 l 6,12 l 12,-20 l 4,18 l 14,-10 l -6,16 l 12,4 l -14,8 l 8,14 '
          'l -16,-4 l -2,14 l -12,-12 l -10,12 l -2,-16 l -14,4 Z" fill="#FDBA74" stroke="#EA580C" '
          'stroke-width="2"/>' % (w / 2 - 22, gy - 24))
    f.circle(120, gy - 22, 19, '#3B82F6', '#1D4ED8', 2.4)
    f.txt(120, gy - 52, m1, INK, 11.5)
    f.parrow(96, gy - 22, 180, 56, IND, 2.8)
    f.txt(92, gy + 26, v1, IND, 11.5, 'middle')
    f.circle(w - 120, gy - 22, 18, '#16A34A', '#166534', 2.4)
    f.txt(w - 120, gy - 52, m2, INK, 11.5)
    f.parrow(w - 96, gy - 22, 0, 56, GRN, 2.8)
    f.txt(w - 92, gy + 26, v2, GRN, 11.5, 'middle')
    f.txt(w / 2, gy + 56, 'just after the explosion', MUT, 11)
    return f.render()


def cannon_recoil(cap, maxw=450, w=510, h=230):
    f = Fig(w, h, cap, maxw)
    gy = 176.0
    _ground(f, gy, 20, w - 20)
    bx = 170.0
    f.rect(bx - 60, gy - 44, 96, 26, '#3F6212', '#1A2E05', 2.4, 5)
    f.raw('<g transform="translate(%.1f,%.1f) rotate(-8)"><rect x="0" y="-9" width="104" height="18" rx="5" '
          'fill="#4D7C0F" stroke="#1A2E05" stroke-width="2.2"/></g>' % (bx + 30, gy - 40))
    f.circle(bx - 34, gy - 12, 18, '#334155', '#0F172A', 2.4)
    f.circle(bx + 16, gy - 12, 18, '#334155', '#0F172A', 2.4)
    f.parrow(bx + 152, gy - 52, 0, 80, RED, 3.2)
    f.circle(bx + 140, gy - 52, 9, '#1F2937', '#0F172A', 1.8)
    f.txt(bx + 210, gy - 66, 'the shell  (east)', RED, 12)
    f.parrow(bx - 76, gy - 66, 180, 62, IND, 3)
    f.txt(bx - 150, gy - 78, 'the cannon recoils', IND, 12, 'start')
    return f.render()

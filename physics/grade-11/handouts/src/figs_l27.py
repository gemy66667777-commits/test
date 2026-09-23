# -*- coding: utf-8 -*-
"""Original figures for Lesson 2-7 : interference of sound waves and the Doppler effect."""
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV
from figs_lesson import INK, MUT
from figs_l24 import _sine

TUBE = '#7dd3fc'
SLID = '#fcd34d'


# --------------------------------------------------------------------------- 1
def quincke(cap, xlab='X', maxw=490, w=610, h=340):
    """Quincke's tube : the sound splits at P and recombines at Q."""
    f = Fig(w, h, cap, maxw)
    cx, cy = 270.0, 150.0
    bw, bh = 200.0, 42.0          # half-width and half-height of the loop
    r = bh
    # the loop, drawn as a thick rounded rectangle outline
    f.raw('<path d="M%.1f,%.1f L%.1f,%.1f A%.1f,%.1f 0 0 1 %.1f,%.1f L%.1f,%.1f '
          'A%.1f,%.1f 0 0 1 %.1f,%.1f Z" fill="none" stroke="%s" stroke-width="15" '
          'stroke-linejoin="round"/>'
          % (cx - bw, cy - bh, cx + bw, cy - bh, r, r, cx + bw, cy + bh,
             cx - bw, cy + bh, r, r, cx - bw, cy - bh, TUBE))
    # the sliding half, in a different colour
    f.raw('<path d="M%.1f,%.1f L%.1f,%.1f A%.1f,%.1f 0 0 1 %.1f,%.1f L%.1f,%.1f" '
          'fill="none" stroke="%s" stroke-width="15" stroke-linejoin="round"/>'
          % (cx + 70, cy - bh, cx + bw, cy - bh, r, r, cx + bw, cy + bh, cx + 70, cy + bh, SLID))
    # the inlet and the outlet
    f.raw('<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="15"/>'
          % (cx - 80, cy + bh, cx - 80, cy + bh + 52, TUBE))
    f.raw('<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="15"/>'
          % (cx - 80, cy - bh, cx - 80, cy - bh - 52, TUBE))
    f.txt(cx - 62, cy + bh + 22, 'P', INK, 13, 'start')
    f.txt(cx - 62, cy - bh - 22, 'Q', INK, 13, 'start')
    f.txt(cx - 120, cy + 5, 'A', INK, 13)
    f.txt(cx + 128, cy + 5, 'B', INK, 13)
    f.parrow(cx - 80, cy + bh + 74, 90, 26, AR, 2.6)
    f.txt(cx - 62, cy + bh + 66, 'sound in', AR, 11, 'start')
    f.parrow(cx - 80, cy - bh - 66, 90, 26, GR, 2.6)
    f.txt(cx - 62, cy - bh - 72, 'sound out', GR, 11, 'start')
    # the pull
    f.parrow(cx + bw + 20, cy, 0, 48, PU, 2.8)
    f.tbg(cx + bw + 46, cy - 24, xlab, PU, 12)
    f.txt(w / 2, h - 26, 'pulling B out by X makes that path longer by 2X', MUT, 10.5)
    f.txt(w / 2, h - 10, 'first minimum :  2 X = λ / 2   →   λ = 4 X', PU, 11.5)
    return f.render()


# --------------------------------------------------------------------------- 2
def doppler_source(cap, maxw=500, w=580, h=330):
    """a source moving to the right : crowded wavefronts in front, spread out behind."""
    f = Fig(w, h, cap, maxw)
    cid = 'dp%d' % (id(f) % 100000)
    f.raw('<defs><clipPath id="%s"><rect x="24" y="24" width="%d" height="%d" rx="8"/>'
          '</clipPath></defs>' % (cid, w - 48, h - 74))
    cy = 168.0
    sx = 300.0                    # where the source is now
    vs = 22.0                     # how far it moves between emissions
    lam = 40.0
    f.raw('<g clip-path="url(#%s)">' % cid)
    for k in range(1, 7):
        ex = sx - k * vs          # where it was when it emitted ring k
        f.raw('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="#2563eb" '
              'stroke-width="2"/>' % (ex, cy, k * lam))
        f.circle(ex, cy, 2.6, GY, GY, 1)
    f.raw('</g>')
    # the source
    f.circle(sx, cy, 11, AR, AR, 1)
    f.parrow(sx + 14, cy, 0, 46, AR, 2.8)
    f.tbg(sx + 44, cy - 24, 'the source moves', AR, 10.5)
    # the two observers
    f.circle(sx + 232, cy, 9, '#047857', '#047857', 1)
    f.tbg(sx + 232, cy + 30, 'A', '#047857', 12)
    f.circle(sx - 248, cy, 9, '#b45309', '#b45309', 1)
    f.tbg(sx - 248, cy + 30, 'B', '#b45309', 12)
    f.tbg(sx + 150, cy - 108, 'crests crowded → shorter λ → higher f',
          '#047857', 11)
    f.tbg(sx - 190, cy + 112, 'crests spread out → longer λ → lower f',
          '#b45309', 11)
    f.txt(w / 2, h - 10, 'the source emits at the same f all the time — only what reaches the '
                         'listener changes', MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 3
def two_speakers_court(cap, maxw=520, w=640, h=300):
    """two loudspeakers, and the loud and quiet places along a line in front of them."""
    f = Fig(w, h, cap, maxw)
    s1 = (96.0, 96.0)
    s2 = (96.0, 196.0)
    for (px, py), lab in ((s1, 'speaker 1'), (s2, 'speaker 2')):
        f.rect(px - 22, py - 20, 34, 40, '#CBD5E1', DK, 2.2, 4)
        f.circle(px - 5, py, 11, '#94A3B8', DK, 2)
        f.txt(px - 30, py + 4, lab, AR, 10.5, 'end')
    line_x = 470.0
    f.line(line_x, 48, line_x, 250, GY, 1.8, '6 5')
    f.txt(line_x, 34, 'the listener walks along here', MUT, 10.5)
    marks = ((78, 'loud'), (118, 'quiet'), (158, 'loud'), (198, 'quiet'), (238, 'loud'))
    for yy, kind in marks:
        col = '#047857' if kind == 'loud' else '#b45309'
        f.circle(line_x, yy, 7, col, col, 1)
        f.tbg(line_x + 16, yy + 4, kind, col, 10.5, 'start')
        f.line(s1[0] + 16, s1[1], line_x, yy, col, 1.2, '4 4')
        f.line(s2[0] + 16, s2[1], line_x, yy, col, 1.2, '4 4')
    f.txt(w / 2, h - 10, 'loud where Δ = mλ , quiet where Δ = ( m + ½ )λ',
          MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 4
def noise_cancel(cap, maxw=490, w=560, h=280):
    """noise cancelling : the earphone plays the same wave turned upside down."""
    f = Fig(w, h, cap, maxw)
    x0, L, A = 224.0, 300.0, 26.0
    rows = ((70.0, 0.0, '#2563eb', 'the noise that arrives'),
            (146.0, math.pi, '#b45309', 'the wave the earphone plays'),
            (226.0, None, '#047857', 'what you hear :  silence'))
    for y, ph, col, lab in rows:
        f.line(x0, y, x0 + L, y, GY, 1.2, '5 5')
        if ph is None:
            f.line(x0, y, x0 + L, y, col, 3.4)
        else:
            _sine(f, x0, y, L, A, cycles=2.5, c=col, w=2.8, phase=ph)
        f.txt(x0 - 16, y + 4, lab, INK, 10.5, 'end')
    f.txt(x0 + L / 2, 196, '+', DK, 18)
    f.line(x0, 204, x0 + L, 204, DK, 1.6)
    f.txt(w / 2, h - 10, 'the two waves are in antiphase, so they cancel by superposition',
          MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 5
def car_wall(cap, maxw=500, w=580, h=280):
    """a police car driving towards a cliff : the direct and the reflected sound."""
    f = Fig(w, h, cap, maxw)
    gy = 208.0
    f.line(40, gy, w - 40, gy, '#94A3B8', 2.6)
    # the cliff
    f.raw('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="#a8a29e" '
          'stroke="#57534e" stroke-width="2.2"/>' % (w - 108, gy, w - 108, 52, w - 40, 36,
                                                     w - 40, gy))
    f.txt(w - 74, 94, 'cliff', '#292524', 11)
    # the car
    cxx = 170.0
    f.rect(cxx - 46, gy - 34, 92, 24, '#1D4ED8', '#1E3A8A', 2.2, 5)
    f.rect(cxx - 22, gy - 50, 44, 18, '#93C5FD', '#1E3A8A', 2, 4)
    f.circle(cxx - 26, gy - 8, 9, '#334155', '#0F172A', 2)
    f.circle(cxx + 26, gy - 8, 9, '#334155', '#0F172A', 2)
    f.circle(cxx, gy - 56, 6, AR, AR, 1)
    f.parrow(cxx + 56, gy - 22, 0, 46, AR, 2.8)
    f.tbg(cxx + 64, gy - 34, 'v', AR, 12, 'start')
    # the direct sound reaching the driver, and the sound going to the cliff
    for k, rr in enumerate((26.0, 40.0, 54.0)):
        f.raw('<path d="M%.1f,%.1f A%.1f,%.1f 0 0 1 %.1f,%.1f" fill="none" stroke="#2563eb" '
              'stroke-width="2" opacity="%.2f"/>'
              % (cxx + rr * 0.5, gy - 56 - rr * 0.87, rr, rr,
                 cxx + rr * 0.5, gy - 56 + rr * 0.87, 0.9 - 0.15 * k))
    f.parrow(cxx + 74, gy - 84, 0, 180, BL, 2.4)
    f.tbg(cxx + 160, gy - 96, 'towards the cliff', BL, 10.5)
    f.arrow(w - 118, gy - 136, cxx + 28, gy - 136, GR, 2.4)
    f.tbg(cxx + 190, gy - 148, 'the echo comes back', GR, 10.5)
    f.tbg(cxx + 6, gy - 108, 'direct sound : still f', DK, 10.5)
    f.txt(w / 2, h - 10, 'the driver moves with the horn, but he moves towards the echo',
          MUT, 10.5)
    return f.render()

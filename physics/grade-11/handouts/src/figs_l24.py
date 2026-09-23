# -*- coding: utf-8 -*-
"""Original figures for Lesson 2-4 : sinusoidal waves."""
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV
from figs_lesson import INK, MUT

WAVE = '#2563eb'


def _sine(f, x0, y0, L, A, cycles=2.0, c=WAVE, w=3, n=200, phase=0.0):
    pts = []
    for i in range(n + 1):
        t = i / float(n)
        pts.append((x0 + L * t, y0 - A * math.sin(2 * math.pi * cycles * t + phase)))
    f.raw('<path d="M' + ' L'.join('%.1f,%.1f' % p for p in pts) +
          '" fill="none" stroke="%s" stroke-width="%s"/>' % (c, w))
    return pts


# --------------------------------------------------------------------------- 1
def wave_on_rope(cap, maxw=470, w=540, h=285):
    """a source shaking one end of a rope : the wave travels, the particles do not."""
    f = Fig(w, h, cap, maxw)
    x0, y0, L, A = 96.0, 120.0, 380.0, 44.0
    f.line(x0 - 10, y0, x0 + L + 16, y0, GY, 1.4, '6 5')
    _sine(f, x0, y0, L, A, cycles=2.0)
    # the shaking source
    f.rect(x0 - 46, y0 - 30, 32, 60, '#E2E8F0', DK, 2.2, 4)
    f.parrow(x0 - 30, y0 - 36, 90, 30, AR, 2.4)
    f.parrow(x0 - 30, y0 + 36, -90, 30, AR, 2.4)
    f.txt(x0 - 30, y0 + 88, 'the source', AR, 10.5)
    f.txt(x0 - 30, y0 + 104, 'vibrates', AR, 10.5)
    # wavelength between two crests
    c1 = x0 + L * 0.125
    c2 = x0 + L * 0.625
    f.guide(c1, y0 - A - 4, c1, y0 - A - 40)
    f.guide(c2, y0 - A - 4, c2, y0 - A - 40)
    f.dim(c1, y0 - A - 34, c2, y0 - A - 34, 'λ', PU, 0, 13, -8)
    # amplitude
    f.dim(x0 + L * 0.375, y0, x0 + L * 0.375, y0 + A, '', PU, 0, 12)
    f.tbg(x0 + L * 0.375 + 14, y0 + A / 2 + 4, 'A', PU, 12, 'start')
    # the wave travels
    f.parrow(x0 + L - 46, y0 + 78, 0, 62, GR, 3)
    f.txt(x0 + L - 60, y0 + 74, 'the wave travels', GR, 10.5, 'end')
    f.txt(w / 2, h - 10, 'v = f λ = λ / T   —   the rope itself only moves up and down',
          MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 2
def transverse_longitudinal(cap, maxw=500, w=580, h=300):
    """the two kinds of mechanical wave, side by side."""
    f = Fig(w, h, cap, maxw)
    # --- transverse, on top
    x0, y0, L, A = 60.0, 86.0, 300.0, 34.0
    _sine(f, x0, y0, L, A, cycles=2.0)
    f.line(x0 - 8, y0, x0 + L + 8, y0, GY, 1.2, '5 5')
    pk = x0 + L * 0.25
    f.parrow(pk, y0 - 7, 90, 30, AR, 2.4)
    f.parrow(pk, y0 + 7, -90, 30, AR, 2.4)
    f.txt(pk + 16, y0 - 22, 'particles', AR, 10, 'start')
    f.parrow(x0 + L + 16, y0, 0, 48, GR, 2.6)
    f.txt(x0 + L + 40, y0 - 14, 'wave', GR, 10.5, 'start')
    f.txt(x0 - 8, 32, 'transverse  —  particles ⊥ the direction of travel', INK, 11, 'start')
    # --- longitudinal, below
    ly = 216.0
    for i in range(42):
        t = i / 41.0
        # bunch the coils sinusoidally
        px = x0 + L * t + 22 * math.sin(2 * math.pi * 2 * t)
        f.line(px, ly - 26, px, ly + 26, '#475569', 1.8)
    f.parrow(x0 + L * 0.12 + 4, ly + 46, 0, 30, AR, 2.2)
    f.parrow(x0 + L * 0.12 - 4, ly + 46, 180, 30, AR, 2.2)
    f.txt(x0 + L * 0.12, ly + 70, 'particles', AR, 10)
    f.parrow(x0 + L + 16, ly, 0, 48, GR, 2.6)
    f.txt(x0 + L + 40, ly - 14, 'wave', GR, 10.5, 'start')
    f.txt(x0 - 8, ly - 44, 'longitudinal  —  particles ∥ the direction of travel', INK, 11,
          'start')
    return f.render()


# --------------------------------------------------------------------------- 3
def longitudinal_dots(cap, maxw=500, w=580, h=250):
    """compressions and rarefactions on a squared grid, with a stated scale."""
    f = Fig(w, h, cap, maxw)
    gx, gy = 50.0, 60.0
    big = 32.0                      # one large square
    cols, rows = 16, 4
    gw, gh = cols * big, rows * big
    f.rect(gx, gy, gw, gh, '#FFFFFF', '#94A3B8', 1.6, 0)
    for i in range(1, cols * 5):
        x = gx + i * big / 5.0
        f.line(x, gy, x, gy + gh, '#E2E8F0', 0.6)
    for j in range(1, rows * 5):
        y = gy + j * big / 5.0
        f.line(gx, y, gx + gw, y, '#E2E8F0', 0.6)
    for i in range(1, cols):
        f.line(gx + i * big, gy, gx + i * big, gy + gh, '#94A3B8', 1.2)
    for j in range(1, rows):
        f.line(gx, gy + j * big, gx + gw, gy + j * big, '#94A3B8', 1.2)
    cy = gy + gh / 2.0
    f.line(gx, cy, gx + gw, cy, '#64748B', 1.6)
    # particle positions : equilibrium spacing 1 large square, displaced sinusoidally
    lam = 8.0                        # large squares per wavelength
    for i in range(16):
        u = i + 0.5
        px = gx + (u - 0.46 * math.sin(2 * math.pi * (u - 1.0) / lam)) * big
        if gx + 3 < px < gx + gw - 3:
            f.circle(px, cy, 4.6, '#0F172A', '#0F172A', 1)
    # the two compression centres, one wavelength apart
    c1 = gx + 1.0 * big
    c2 = gx + 9.0 * big
    for cc, lab in ((c1, 'compression'), (c2, 'compression')):
        f.guide(cc, gy - 4, cc, gy - 24)
        f.txt(cc, gy - 30, lab, AR, 10)
    f.txt(gx + 5.0 * big, gy - 30, 'rarefaction', BL, 10)
    f.dim(c1, gy + gh + 26, c2, gy + gh + 26, 'λ = ?', PU, 0, 12, -8)
    f.txt(gx, gy + gh + 56, 'scale :  one large square = 1.0 cm', MUT, 11, 'start')
    return f.render()


# --------------------------------------------------------------------------- 4
def yx_graph(cap, lam='λ = 3.0 m', amp='A = 0.50 m', maxw=470, w=560, h=280):
    """displacement against position : gives the amplitude and the wavelength."""
    f = Fig(w, h, cap, maxw)
    x0, y0, L, A = 76.0, 140.0, 360.0, 62.0
    f.arrow(x0 - 16, y0, x0 + L + 30, y0, DK, 2.2)
    f.arrow(x0, y0 + A + 34, x0, y0 - A - 40, DK, 2.2)
    f.txt(x0 + L + 40, y0 + 16, 'position x', INK, 11.5, 'start')
    f.txt(x0 - 4, y0 - A - 48, 'displacement y', INK, 11.5, 'start')
    _sine(f, x0, y0, L, A, cycles=2.0)
    c1 = x0 + L * 0.125
    c2 = x0 + L * 0.625
    f.guide(c1, y0 - A, c1, y0 - A - 34)
    f.guide(c2, y0 - A, c2, y0 - A - 34)
    f.dim(c1, y0 - A - 28, c2, y0 - A - 28, lam, PU, 0, 11.5, -8)
    tr = x0 + L * 0.375
    f.dim(tr, y0, tr, y0 + A, '', PU, 0, 12)
    f.tbg(tr + 14, y0 + A / 2 + 4, amp, PU, 11.5, 'start')
    f.txt(w / 2, h - 10, 'a snapshot of the whole rope at one instant', MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 5
def yt_graph(cap, per='T = 0.60 s', maxw=470, w=560, h=280):
    """displacement against time : gives the amplitude and the periodic time."""
    f = Fig(w, h, cap, maxw)
    x0, y0, L, A = 76.0, 140.0, 360.0, 62.0
    f.arrow(x0 - 16, y0, x0 + L + 30, y0, DK, 2.2)
    f.arrow(x0, y0 + A + 34, x0, y0 - A - 40, DK, 2.2)
    f.txt(x0 + L + 40, y0 + 16, 'time t', INK, 11.5, 'start')
    f.txt(x0 - 4, y0 - A - 48, 'displacement y', INK, 11.5, 'start')
    _sine(f, x0, y0, L, A, cycles=2.0, c='#0f766e')
    c1 = x0 + L * 0.125
    c2 = x0 + L * 0.625
    f.guide(c1, y0 - A, c1, y0 - A - 34)
    f.guide(c2, y0 - A, c2, y0 - A - 34)
    f.dim(c1, y0 - A - 28, c2, y0 - A - 28, per, PU, 0, 11.5, -8)
    f.txt(w / 2, h - 10, 'the history of one single particle', MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 6
def pq_quarter(cap, maxw=470, w=540, h=330):
    """P at the equilibrium point, Q at the crest : a quarter of a cycle apart."""
    f = Fig(w, h, cap, maxw)
    x0, y0, L, A = 86.0, 150.0, 400.0, 66.0
    f.arrow(x0 - 16, y0, x0 + L + 32, y0, DK, 2.2)
    f.arrow(x0, y0 + A + 24, x0, y0 - A - 42, DK, 2.2)
    f.txt(x0 + L + 42, y0 + 16, 'x', INK, 12, 'start', it=True)
    f.txt(x0 - 4, y0 - A - 50, 'displacement y', INK, 11.5, 'start')
    _sine(f, x0, y0, L, A, cycles=2.0)
    q = x0 + L * 0.125
    f.line(q, y0 - A + 6, q, y0 + 44, GY, 1.6, '6 5')
    f.circle(x0, y0, 5, AR, AR, 1)
    f.circle(q, y0 - A, 5, AR, AR, 1)
    f.txt(x0 - 16, y0 - 12, 'P', AR, 13, 'end')
    f.txt(q + 12, y0 - A - 12, 'Q', AR, 13, 'start')
    f.dim(x0, y0 + 44, q, y0 + 44, '', PU, 0, 11.5)
    f.txt(x0 + 4, y0 + 100, '2 m  in  0.1 s', PU, 11.5, 'start')
    f.txt(x0 + 4, y0 + 120, 'this is a quarter of a cycle', MUT, 10.5, 'start')
    f.txt(w / 2, h - 10, 'so  λ = 4 × 2 m  and  T = 4 × 0.1 s', PU, 11)
    return f.render()

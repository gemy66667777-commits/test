# -*- coding: utf-8 -*-
"""Original figures for Lessons 2-10 and 2-11 : lenses and Young's experiment."""
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV
from figs_lesson import INK, MUT

LENSC = '#93c5fd'
OBJ = '#dc2626'
IMG = '#7c3aed'


def _axis(f, x0, x1, ay):
    f.line(x0, ay, x1, ay, DK, 1.8)


def _convex(f, cx, ay, hh):
    f.raw('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="%s" '
          'fill-opacity="0.75" stroke="#1d4ed8" stroke-width="2"/>'
          % (cx, ay - hh, cx + 22, ay, cx, ay + hh, cx - 22, ay, cx, ay - hh, LENSC))


def _concave(f, cx, ay, hh):
    f.raw('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f '
          'Q%.1f,%.1f %.1f,%.1f Z" fill="%s" fill-opacity="0.75" stroke="#1d4ed8" '
          'stroke-width="2"/>'
          % (cx - 15, ay - hh, cx + 15, ay - hh, cx - 6, ay, cx + 15, ay + hh,
             cx - 15, ay + hh, cx + 6, ay, cx - 15, ay - hh, LENSC))


def _marks(f, cx, ay, fl, hh, both2f=True):
    for s in (-1, 1):
        f.circle(cx + s * fl, ay, 3.6, DK, DK, 1)
        f.txt(cx + s * fl, ay + 18, 'F', INK, 11)
        if both2f:
            f.circle(cx + s * 2 * fl, ay, 3.6, DK, DK, 1)
            f.txt(cx + s * 2 * fl, ay + 18, '2F', INK, 11)


# --------------------------------------------------------------------------- 1
def convex_far(cap, maxw=520, w=600, h=300):
    """an object beyond 2F : a real, inverted, diminished image."""
    f = Fig(w, h, cap, maxw)
    cx, ay, fl, hh = 286.0, 150.0, 56.0, 64.0
    u, ho = 168.0, 50.0
    v = u * fl / (u - fl)
    hi = ho * v / u
    _axis(f, 36, w - 36, ay)
    _convex(f, cx, ay, hh)
    _marks(f, cx, ay, fl, hh)
    ox = cx - u
    f.arrow(ox, ay, ox, ay - ho, OBJ, 3)
    f.txt(ox, ay - ho - 12, 'object', OBJ, 11)
    ex = cx + v + 56.0
    # ray 1 : parallel, then through F on the far side
    f.line(ox, ay - ho, cx, ay - ho, GR, 2)
    f.arrow(cx, ay - ho, ex, ay - ho + ho * (ex - cx) / fl, GR, 2)
    # ray 2 : straight through the optical centre
    f.arrow(ox, ay - ho, ex, ay - ho + ho * (ex - ox) / u, BL, 2)
    ix = cx + v
    f.arrow(ix, ay, ix, ay + hi, IMG, 3.4)
    f.tbg(ix + 16, ay + hi + 38, 'image : real, inverted, diminished', IMG, 10.5, 'start')
    f.txt(w / 2, h - 10, 'object beyond 2F  →  the image lies between F and 2F', MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 2
def concave_lens(cap, maxw=520, w=600, h=300):
    """a concave lens : always virtual, erect and diminished."""
    f = Fig(w, h, cap, maxw)
    cx, ay, fl, hh = 330.0, 160.0, 64.0, 64.0
    u, ho = 150.0, 50.0
    v = u * fl / (u + fl)
    hi = ho * v / u
    _axis(f, 36, w - 36, ay)
    _concave(f, cx, ay, hh)
    _marks(f, cx, ay, fl, hh, both2f=False)
    ox = cx - u
    f.arrow(ox, ay, ox, ay - ho, OBJ, 3)
    f.txt(ox, ay - ho - 12, 'object', OBJ, 11)
    ex = cx + 150.0
    fx = cx - fl
    # ray 1 : parallel, then diverging as if it came from the near F
    gx = cx + fl * (ay - ho - 34.0) / ho          # stop before the top edge
    f.line(ox, ay - ho, cx, ay - ho, GR, 2)
    f.arrow(cx, ay - ho, gx, 34.0, GR, 2)
    f.line(fx, ay, cx, ay - ho, GY, 1.6, '5 4')
    # ray 2 : straight through the optical centre
    f.arrow(ox, ay - ho, ex, ay - ho + ho * (ex - ox) / u, BL, 2)
    ix = cx - v
    f.arrow(ix, ay, ix, ay - hi, IMG, 3.4)
    f.tbg(56, ay + 66, 'image : virtual, erect, diminished', IMG, 10.5, 'start')
    f.txt(w / 2, h - 10, 'the refracted rays diverge — only their backward extensions meet',
          MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 3
def magnifier(cap, maxw=520, w=600, h=320):
    """a convex lens used as a magnifying glass : object inside F."""
    f = Fig(w, h, cap, maxw)
    cx, ay, fl, hh = 392.0, 196.0, 80.0, 68.0
    u, ho = 50.0, 26.0
    v = u * fl / (fl - u)
    hi = ho * v / u
    _axis(f, 36, w - 36, ay)
    _convex(f, cx, ay, hh)
    _marks(f, cx, ay, fl, hh, both2f=False)
    ox = cx - u
    f.arrow(ox, ay, ox, ay - ho, OBJ, 3)
    f.tbg(ox - 10, ay + 34, 'object', OBJ, 10.5, 'end')
    ex = cx + 148.0
    # ray 1 : parallel, then through the far F
    f.line(ox, ay - ho, cx, ay - ho, GR, 2)
    f.arrow(cx, ay - ho, ex, ay - ho + ho * (ex - cx) / fl, GR, 2)
    # ray 2 : straight through the optical centre
    f.arrow(ox, ay - ho, ex, ay - ho + ho * (ex - ox) / u, BL, 2)
    ix = cx - v
    # the backward extensions
    f.line(cx, ay - ho, ix, ay - hi, GY, 1.6, '5 4')
    f.line(cx, ay, ix, ay - hi, GY, 1.6, '5 4')
    f.arrow(ix, ay, ix, ay - hi, IMG, 3.4)
    f.tbg(ix, ay - hi - 14, 'image : virtual, erect, magnified', IMG, 10.5)
    f.txt(w / 2, h - 10, 'object inside F  →  the extensions meet behind the object', MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 4
def young_setup(cap, dlab='d', llab='L', ylab='Δy', maxw=520, w=600, h=324):
    """Young's double slit : the slit separation, the screen distance and the fringes."""
    f = Fig(w, h, cap, maxw)
    sx, ay = 118.0, 150.0
    scx = 470.0
    f.rect(sx - 7, 48, 14, 74, '#334155', '#0f172a', 1.6, 2)
    f.rect(sx - 7, 178, 14, 74, '#334155', '#0f172a', 1.6, 2)
    f.rect(sx - 7, 134, 14, 32, '#334155', '#0f172a', 1.6, 2)
    f.dim(sx + 26, 128, sx + 26, 172, '', PU, 0, 11)
    f.tbg(sx + 38, 154, dlab, PU, 11.5, 'start')
    f.txt(sx, 36, 'double slit', INK, 10.5)
    # incoming light
    for yy in (120, 150, 180):
        f.parrow(46, yy, 0, 44, AR, 2.2)
    f.txt(46, 100, 'light', AR, 10.5, 'start')
    # the screen with the fringes
    f.rect(scx, 44, 22, 212, '#e2e8f0', DK, 2, 3)
    sp = 26.0
    for k in range(-3, 4):
        yy = ay + k * sp
        col = '#fbbf24' if k % 2 == 0 else '#1e293b'
        f.rect(scx + 1, yy - 10, 20, 20, col, col, 0.6, 1)
    f.dim(scx + 42, ay - 2 * sp, scx + 42, ay, '', PU, 0, 11)
    f.tbg(scx + 54, ay - sp + 4, ylab, PU, 11.5, 'start')
    f.txt(scx + 11, 32, 'screen', INK, 10.5)
    # the two rays
    for yy in (128.0, 172.0):
        f.line(sx + 7, yy, scx, ay - 2 * sp, '#f59e0b', 1.8)
    f.dim(sx, 276, scx, 276, llab, PU, 0, 11.5, -8)
    f.guide(sx, 260, sx, 280)
    f.guide(scx, 260, scx, 280)
    f.txt(w / 2, h - 10, 'λ = Δy × d / L', PU, 12)
    return f.render()


# --------------------------------------------------------------------------- 5
def young_paths(cap, maxw=470, w=540, h=322):
    """the two paths from the slits to a point P and the path difference."""
    f = Fig(w, h, cap, maxw)
    sx = 110.0
    s1 = (sx, 110.0)
    s2 = (sx, 190.0)
    p = (468.0, 86.0)
    f.rect(sx - 7, 40, 14, 62, '#334155', '#0f172a', 1.6, 2)
    f.rect(sx - 7, 118, 14, 64, '#334155', '#0f172a', 1.6, 2)
    f.rect(sx - 7, 198, 14, 60, '#334155', '#0f172a', 1.6, 2)
    for (px, py), lab in ((s1, 'S₁'), (s2, 'S₂')):
        f.circle(px, py, 5, AR, AR, 1)
        f.txt(px - 16, py + 4, lab, AR, 12, 'end')
    f.rect(470.0, 40, 18, 218, '#e2e8f0', DK, 2, 3)
    f.circle(p[0], p[1], 6, '#047857', '#047857', 1)
    f.txt(p[0] - 12, p[1] - 12, 'P', '#047857', 13, 'end')
    f.line(s1[0] + 7, s1[1], p[0], p[1], BL, 2.2)
    f.line(s2[0] + 7, s2[1], p[0], p[1], GR, 2.2)
    f.tbg(270, 86, 'S₁P', BL, 11)
    f.tbg(290, 172, 'S₂P', GR, 11)
    f.txt(w / 2, h - 26, 'path difference  Δ = S₂P − S₁P', PU, 12)
    f.txt(w / 2, h - 10, 'Δ = mλ → bright fringe   &middot;   '
                         'Δ = ( m + ½ )λ → dark fringe', MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 6
def lens_screen(cap, total='90 cm', alab='a', maxw=500, w=580, h=250):
    """a convex lens sliding between a fixed object and a fixed screen."""
    f = Fig(w, h, cap, maxw)
    ox, ay = 92.0, 128.0
    scx = 500.0
    cx = 236.0
    f.raw('<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="1.6" '
          'stroke-dasharray="7 5"/>' % (54, ay, w - 46, ay, GY))
    f.arrow(ox, ay, ox, ay - 52, OBJ, 3)
    f.txt(ox, ay - 64, 'object', OBJ, 11)
    _convex(f, cx, ay, 52)
    f.arrow(cx - 30, ay - 82, cx + 30, ay - 82, DK, 1.8, both=True)
    f.txt(cx, ay - 94, 'the lens can slide', DK, 10.5)
    f.rect(scx, ay - 74, 16, 148, '#e2e8f0', DK, 2, 3)
    f.txt(scx + 8, ay - 86, 'screen', INK, 10.5)
    f.dim(ox, ay + 52, cx, ay + 52, alab, PU, 0, 11.5, -8)
    f.guide(ox, ay + 40, ox, ay + 56)
    f.guide(cx, ay + 40, cx, ay + 56)
    f.dim(ox, ay + 96, scx, ay + 96, total, PU, 0, 11.5, -8)
    f.guide(scx, ay + 80, scx, ay + 100)
    f.guide(ox, ay + 80, ox, ay + 100)
    return f.render()

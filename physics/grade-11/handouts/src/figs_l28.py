# -*- coding: utf-8 -*-
"""Original figures for Lesson 2-8 : the Doppler effect for light."""
import math
from figlib import Fig, P, AR, BL, GR, PU, OR, DK, GY, NV
from figs_lesson import INK, MUT

RED_ = '#dc2626'
BLUE_ = '#2563eb'


def _spectrum_bar(f, x0, y0, W, H, gid):
    f.raw('<defs><linearGradient id="%s" x1="0" y1="0" x2="1" y2="0">'
          '<stop offset="0%%" stop-color="#5b21b6"/><stop offset="18%%" stop-color="#2563eb"/>'
          '<stop offset="38%%" stop-color="#06b6d4"/><stop offset="55%%" stop-color="#16a34a"/>'
          '<stop offset="72%%" stop-color="#eab308"/><stop offset="86%%" stop-color="#f97316"/>'
          '<stop offset="100%%" stop-color="#b91c1c"/></linearGradient></defs>' % gid)
    f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#%s)" rx="3" '
          'stroke="#334155" stroke-width="1.6"/>' % (x0, y0, W, H, gid))


# --------------------------------------------------------------------------- 1
def spectrum_shift(cap, maxw=500, w=580, h=340):
    """the laboratory spectrum, and the same lines red-shifted and blue-shifted."""
    f = Fig(w, h, cap, maxw)
    x0, W, H = 128.0, 384.0, 42.0
    lines = (0.26, 0.31, 0.52, 0.70, 0.76)
    rows = ((58.0, 0.0, 'in the laboratory', DK, ''),
            (150.0, 0.072, 'galaxy A &mdash; red shift', RED_, 'moving away'),
            (242.0, -0.072, 'galaxy B &mdash; blue shift', BLUE_, 'moving towards us'))
    for k, (yy, sh, lab, col, note) in enumerate(rows):
        _spectrum_bar(f, x0, yy, W, H, 'sp%d%d' % (id(f) % 10000, k))
        for u in lines:
            xx = x0 + W * min(max(u + sh, 0.02), 0.98)
            f.line(xx, yy + 2, xx, yy + H - 2, '#0f172a', 3)
        f.txt(x0 - 16, yy + 20, lab, col, 11, 'end')
        if note:
            f.txt(x0 - 16, yy + 36, note, MUT, 10, 'end')
    # the arrows showing which way the lines moved
    for yy, sh in ((150.0, 1), (242.0, -1)):
        xx = x0 + W * 0.52
        f.parrow(xx + sh * 8, yy - 12, 0 if sh > 0 else 180, 36, RED_ if sh > 0 else BLUE_, 2.4)
    f.txt(x0 + W * 0.20, 40, 'blue end', BLUE_, 10.5)
    f.txt(x0 + W * 0.86, 40, 'red end', RED_, 10.5)
    f.txt(w / 2, h - 10, 'the pattern of lines is the same — the whole set has simply slid along',
          MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 2
def galaxy_motion(cap, maxw=500, w=580, h=316):
    """two galaxies, one receding and one approaching the Earth."""
    f = Fig(w, h, cap, maxw)
    cid = 'gx%d' % (id(f) % 100000)
    f.raw('<defs><clipPath id="%s"><rect x="28" y="28" width="%d" height="%d" rx="8"/></clipPath>'
          '</defs>' % (cid, w - 56, h - 84))
    f.raw('<rect x="28" y="28" width="%d" height="%d" fill="#0f172a" rx="8"/>' % (w - 56, h - 84))
    f.raw('<g clip-path="url(#%s)">' % cid)
    for i in range(46):
        sx = 40 + (i * 97) % (w - 80)
        sy = 40 + (i * 61) % (h - 100)
        f.circle(sx, sy, 1.3, '#e2e8f0', '#e2e8f0', 0.4)
    f.raw('</g>')
    ey = 150.0
    f.circle(w / 2, ey, 17, '#38bdf8', '#0ea5e9', 2.2)
    f.txt(w / 2, ey + 42, 'Earth', '#e2e8f0', 11)
    for cx, col, lab, note, ang in ((132.0, BLUE_, 'galaxy B', 'blue shift', 0),
                                    (448.0, RED_, 'galaxy A', 'red shift', 180)):
        f.raw('<ellipse cx="%.1f" cy="%.1f" rx="42" ry="17" fill="%s" opacity="0.85" '
              'transform="rotate(-18 %.1f %.1f)"/>' % (cx, ey, col, cx, ey))
        f.circle(cx, ey, 9, '#f8fafc', col, 1.6)
        f.txt(cx, ey - 40, lab, '#e2e8f0', 11.5)
        f.txt(cx, ey + 46, note, col, 11)
    f.parrow(178.0, ey + 72, 0, 66, BLUE_, 2.8)
    f.txt(211.0, ey + 96, 'towards us', BLUE_, 10.5)
    f.parrow(402.0, ey + 72, 180, 66, RED_, 2.8)
    f.txt(369.0, ey + 96, 'away from us', RED_, 10.5)
    f.txt(w / 2, h - 10, '&Delta;&lambda; / &lambda; = v / c   —   the bigger the shift, the '
                         'faster the galaxy', PU, 11)
    return f.render()


# --------------------------------------------------------------------------- 3
def car_bike(cap, maxw=510, w=600, h=340):
    """a car going east and a motorcycle going west, before and after they pass."""
    f = Fig(w, h, cap, maxw)

    def _car(px, py, col, edge):
        f.rect(px - 34, py - 20, 68, 18, col, edge, 2, 4)
        f.rect(px - 16, py - 33, 32, 14, '#BFDBFE', edge, 1.8, 3)
        f.circle(px - 20, py + 1, 7, '#334155', '#0F172A', 1.8)
        f.circle(px + 20, py + 1, 7, '#334155', '#0F172A', 1.8)

    def _bike(px, py, col, edge):
        f.circle(px - 14, py, 9, 'none', edge, 2.4)
        f.circle(px + 14, py, 9, 'none', edge, 2.4)
        f.line(px - 14, py, px + 6, py - 14, edge, 2.4)
        f.line(px + 6, py - 14, px + 14, py, edge, 2.4)
        f.circle(px + 2, py - 24, 7, col, edge, 2)

    f.tbg(168, 30, 'car  15 m/s east, 600 Hz', BL, 10.5)
    f.tbg(432, 30, 'motorcycle  20 m/s west', OR, 10.5)
    for ry, ttl, carx, bikex, note in (
            (114.0, 'before they pass  —  closing in', 208.0, 392.0,
             'the gap is closing  →  higher pitch'),
            (244.0, 'after they pass  —  drawing apart', 392.0, 208.0,
             'the gap is opening  →  lower pitch')):
        f.txt(70, ry - 48, ttl, INK, 11.5, 'start')
        f.line(70, ry + 26, w - 70, ry + 26, '#94A3B8', 2.2)
        _car(carx, ry, '#1D4ED8', '#1E3A8A')
        _bike(bikex, ry, '#F97316', '#7C2D12')
        f.parrow(carx + 44, ry - 6, 0, 40, BL, 2.6)
        f.parrow(bikex - 44, ry - 6, 180, 40, OR, 2.6)
        f.tbg(w / 2, ry + 50, note, MUT, 10.5)
    f.txt(w / 2, h - 10, 'east is to the right — the car overtakes, then they separate',
          MUT, 10.5)
    return f.render()


# --------------------------------------------------------------------------- 4
def ambulance_pass(cap, maxw=500, w=580, h=270):
    """an ambulance approaching and then receding from a stationary listener."""
    f = Fig(w, h, cap, maxw)
    gy = 188.0
    f.line(46, gy, w - 46, gy, '#94A3B8', 2.4)
    px = 300.0
    # the listener
    f.circle(px, gy - 42, 10, '#FDE68A', '#B45309', 2)
    f.line(px, gy - 32, px, gy - 10, '#B45309', 2.6)
    f.line(px, gy - 26, px - 10, gy - 16, '#B45309', 2.2)
    f.line(px, gy - 26, px + 10, gy - 16, '#B45309', 2.2)
    f.line(px, gy - 10, px - 8, gy, '#B45309', 2.2)
    f.line(px, gy - 10, px + 8, gy, '#B45309', 2.2)
    f.txt(px, gy + 20, 'the listener', MUT, 10.5)
    for cx, col, lab, note, direction in ((128.0, '#047857', 'approaching', 'pitch is higher', 0),
                                          (470.0, '#b45309', 'receding', 'pitch is lower', 0)):
        f.rect(cx - 36, gy - 40, 72, 26, '#F8FAFC', DK, 2.2, 4)
        f.rect(cx - 36, gy - 40, 26, 26, '#E2E8F0', DK, 1.8, 4)
        f.circle(cx - 20, gy - 10, 8, '#334155', '#0F172A', 2)
        f.circle(cx + 20, gy - 10, 8, '#334155', '#0F172A', 2)
        f.circle(cx + 4, gy - 48, 5, AR, AR, 1)
        f.parrow(cx + 42, gy - 26, 0, 40, AR, 2.6)
        f.tbg(cx, gy - 74, lab, col, 11)
        f.tbg(cx, gy + 22, note, col, 10.5)
    f.tbg(px, 44, 'at the instant of passing the pitch is the true f', PU, 11)
    f.txt(w / 2, h - 10, 'the loudness rises on the way in and falls on the way out, whatever the '
                         'pitch does', MUT, 10.5)
    return f.render()

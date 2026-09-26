# -*- coding: utf-8 -*-
"""Glowing circuit artwork for the cover (794 x 1123 = A4 at 96 dpi)."""
import math
import random


def zig(x, y, L, n=7, h=11):
    pts = [(x, y)]
    for k in range(n):
        pts.append((x + L * (k + 0.5) / n, y + (-h if k % 2 == 0 else h)))
    pts.append((x + L, y))
    return ' '.join('%.1f,%.1f' % p for p in pts)


def svg():
    random.seed(7)
    o = ['<svg class="art" viewBox="0 0 794 1123" xmlns="http://www.w3.org/2000/svg"><defs>'
         '<filter id="cvGlow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4" result="b"/>'
         '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
         '<radialGradient id="cvBulb" cx="50%" cy="45%" r="55%"><stop offset="0" stop-color="#fffbeb"/>'
         '<stop offset=".5" stop-color="#fde047"/><stop offset="1" stop-color="#f59e0b"/></radialGradient>'
         '<radialGradient id="cvHalo" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#fde047" stop-opacity=".8"/>'
         '<stop offset="1" stop-color="#fde047" stop-opacity="0"/></radialGradient></defs>']
    # a big circuit loop in the lower half
    c1 = '#67e8f9'
    c2 = '#f9a8d4'
    g = '<g filter="url(#cvGlow)" fill="none" stroke-linecap="round" stroke-linejoin="round">'
    T, Bt, M = 700, 960, 830
    g += '<polyline points="90,%d 90,%d 700,%d 700,%d" stroke="%s" stroke-width="4"/>' % (T, Bt, Bt, T, c1)
    g += '<polyline points="90,%d 300,%d" stroke="%s" stroke-width="4"/>' % (T, T, c1)
    g += '<polyline points="%s" stroke="#fdba74" stroke-width="5"/>' % zig(300, T, 120)
    g += '<polyline points="420,%d 520,%d" stroke="%s" stroke-width="4"/>' % (T, T, c1)
    g += '<polyline points="580,%d 700,%d" stroke="%s" stroke-width="4"/>' % (T, T, c1)
    # battery on the bottom wire
    g += '<line x1="380" y1="%d" x2="410" y2="%d" stroke="#1e1b4b" stroke-width="10"/>' % (Bt, Bt)
    g += '<line x1="386" y1="%d" x2="386" y2="%d" stroke="#fb7185" stroke-width="6"/>' % (Bt - 30, Bt + 30)
    g += '<line x1="404" y1="%d" x2="404" y2="%d" stroke="#93c5fd" stroke-width="10"/>' % (Bt - 16, Bt + 16)
    # parallel branch with a resistor
    g += '<polyline points="90,%d 200,%d" stroke="%s" stroke-width="3.5"/>' % (M, M, c2)
    g += '<polyline points="%s" stroke="#f0abfc" stroke-width="4.5"/>' % zig(200, M, 110)
    g += '<polyline points="310,%d 700,%d" stroke="%s" stroke-width="3.5"/>' % (M, M, c2)
    g += '</g>'
    o.append(g)
    # lamp
    o.append('<circle cx="550" cy="700" r="70" fill="url(#cvHalo)"/>')
    o.append('<circle cx="550" cy="700" r="28" fill="url(#cvBulb)" stroke="#78350f" stroke-width="3"/>')
    o.append('<path d="M530,680 L570,720 M530,720 L570,680" stroke="#78350f" stroke-width="3"/>')
    for k in range(10):
        a = math.radians(k * 36)
        o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#fde047" stroke-width="3" '
                 'stroke-linecap="round" opacity=".85"/>' % (550 + 40 * math.cos(a), 700 + 40 * math.sin(a),
                                                               550 + 56 * math.cos(a), 700 + 56 * math.sin(a)))
    # ammeter & voltmeter
    for (x, y, t, c) in ((700, 890, 'A', '#fcd34d'), (90, 770, 'V', '#c4b5fd')):
        o.append('<circle cx="%d" cy="%d" r="26" fill="#1e1b4b" stroke="%s" stroke-width="4" filter="url(#cvGlow)"/>'
                 % (x, y, c))
        o.append('<text x="%d" y="%d" font-size="28" font-weight="700" text-anchor="middle" fill="%s" '
                 'font-family="Liberation Sans">%s</text>' % (x, y + 10, c, t))
    # electrons drifting along the wires
    for k in range(34):
        seg = random.choice([((90, 960), (700, 960)), ((700, 960), (700, 700)), ((90, 700), (90, 960)),
                             ((310, 830), (700, 830))])
        t = random.random()
        x = seg[0][0] + (seg[1][0] - seg[0][0]) * t
        y = seg[0][1] + (seg[1][1] - seg[0][1]) * t
        o.append('<circle cx="%.1f" cy="%.1f" r="4.2" fill="#e0f2fe" opacity=".9"/>' % (x, y))
    # formula chips floating
    for (x, y, s, r) in ((655, 200, 'V = I R', -8), (650, 285, 'I = Q / t', 6), (160, 625, 'V<tspan baseline-shift="sub" '
                         'font-size="70%">B</tspan> = I ( R + r )', -5), (620, 620, '&#931; I = 0', 7),
                         (395, 640, '&#961;<tspan baseline-shift="sub" font-size="70%">e</tspan> = R A / L', -4)):
        o.append('<g transform="rotate(%d %d %d)"><rect x="%d" y="%d" width="%d" height="40" rx="20" fill="#ffffff" '
                 'fill-opacity=".13" stroke="#ffffff" stroke-opacity=".45" stroke-width="1.5"/>'
                 '<text x="%d" y="%d" font-size="21" font-weight="700" fill="#fff" text-anchor="middle" '
                 'font-family="Liberation Sans">%s</text></g>'
                 % (r, x, y, x - 95, y - 28, 190, x, y, s))
    # sparks
    for k in range(40):
        x, y = random.uniform(20, 774), random.uniform(20, 1100)
        o.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#fff" opacity="%.2f"/>'
                 % (x, y, random.uniform(0.8, 2.2), random.uniform(0.25, 0.7)))
    o.append('</svg>')
    return ''.join(o)

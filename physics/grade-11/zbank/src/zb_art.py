# -*- coding: utf-8 -*-
"""Chapter 2 (Oscillations and Waves) header and footer art for the Z BANK pages.
Fourteen themes; the page script gives every two pages the next theme."""
import math

B = '#2556A8'        # ink
D = '#1B3F85'        # deep ink
L = '#5A9BD5'        # the box-shadow blue
P = '#DCE8F8'        # pale fill
Y = '#FBBF24'        # a spark of colour

DEFS = ('<filter id="sk" x="-5%" y="-25%" width="110%" height="150%">'
        '<feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="7" result="n"/>'
        '<feDisplacementMap in="SourceGraphic" in2="n" scale="2.4" xChannelSelector="R" yChannelSelector="G"/>'
        '</filter>'
        '<pattern id="hz" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(38)">'
        '<rect width="7" height="7" fill="#DCE8F8"/><line x1="0" y1="0" x2="0" y2="7" stroke="#8DB4E6" '
        'stroke-width="2.6"/></pattern>'
        '<pattern id="hl" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(38)">'
        '<line x1="0" y1="0" x2="0" y2="6" stroke="#8DB4E6" stroke-width="1.3"/></pattern>'
        '<linearGradient id="band" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#EAF3FD"/>'
        '<stop offset="0.5" stop-color="#F7FBFF"/><stop offset="1" stop-color="#EAF3FD"/></linearGradient>')

HAND = "font-family:'Kalam';font-weight:700"


def T(x, y, s, size, rot=0, anchor='start', col=B, extra=''):
    tr = ' transform="rotate(%s %s %s)"' % (rot, x, y) if rot else ''
    return ('<text x="%s" y="%s" font-size="%s" fill="%s" text-anchor="%s" style="%s"%s>%s</text>'
            % (x, y, size, col, anchor, HAND + extra, tr, s))


def ln(x1, y1, x2, y2, w=3, c=B, extra=''):
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s" stroke-linecap="round"%s/>'
            % (x1, y1, x2, y2, c, w, extra))


def path(d, w=3, c=B, fill='none', extra=''):
    return '<path d="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round" stroke-linecap="round"%s/>' % (
        d, fill, c, w, extra)


def sine(x0, y0, W, amp, cycles, w=3, c=B, phase=0.0, n=160):
    pts = ' '.join('%.1f,%.1f' % (x0 + W * k / n, y0 - amp * math.sin(2 * math.pi * cycles * k / n + phase))
                   for k in range(n + 1))
    return '<polyline points="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>' % (pts, c, w)


def spark(x, y, r=9):
    pts = []
    for k in range(8):
        rr = r if k % 2 == 0 else r * 0.38
        a = k * math.pi / 4 - math.pi / 2
        pts.append('%.1f,%.1f' % (x + rr * math.cos(a), y + rr * math.sin(a)))
    return '<polygon points="%s" fill="%s" stroke="%s" stroke-width="1.6" stroke-linejoin="round"/>' % (
        ' '.join(pts), Y, D)


def coil(x0, y0, x1, y1, n=8, r=11, w=3):
    """a looped spring drawn between two points."""
    L_ = math.hypot(x1 - x0, y1 - y0)
    ux, uy = (x1 - x0) / L_, (y1 - y0) / L_
    vx, vy = -uy, ux
    a = L_ / (2 * math.pi * n) * 1.8
    pts = []
    for k in range(0, 481):
        s = k / 480
        t = L_ * s - a * math.sin(2 * math.pi * n * s)
        h = r * math.cos(2 * math.pi * n * s) * (1 if 0.03 < s < 0.97 else 0.3)
        pts.append('%.1f,%.1f' % (x0 + ux * t + vx * h, y0 + uy * t + vy * h))
    return '<polyline points="%s" fill="none" stroke="%s" stroke-width="%s"/>' % (' '.join(pts), B, w)


# ============================================================ icons : each fits a 300 x 140 box
def i_spring_block():
    return (path('M8,20 L8,130', 4) + ''.join(ln(8, 26 + k * 16, -4, 36 + k * 16, 2) for k in range(7)) +
            ln(8, 128, 290, 128, 3.4) + coil(8, 92, 150, 92, 9, 14) +
            '<rect x="150" y="62" width="70" height="62" rx="8" fill="url(#hz)" stroke="%s" stroke-width="3.4"/>' % B +
            T(185, 101, 'm', 26, 0, 'middle', D) + path('M232,76 L284,76', 3) + path('M272,66 L286,76 L272,86', 3) +
            path('M138,50 L160,50', 2.6) + path('M232,50 L252,50', 2.6) + T(196, 44, 'x', 22, 0, 'middle'))


def i_vertical_spring():
    return (path('M40,12 L220,12', 4) + ''.join(ln(48 + k * 22, 12, 38 + k * 22, 2, 2) for k in range(8)) +
            coil(130, 12, 130, 84, 8, 13) +
            '<rect x="100" y="84" width="60" height="46" rx="7" fill="url(#hz)" stroke="%s" stroke-width="3.4"/>' % B +
            T(130, 115, 'm', 24, 0, 'middle', D) + path('M190,40 L190,120', 2.6) + path('M182,50 L190,38 L198,50', 2.6) +
            path('M182,110 L190,122 L198,110', 2.6) + T(212, 86, 'A', 22) + spark(250, 40, 11))


def i_pendulum():
    return (path('M60,14 L240,14', 4) + ''.join(ln(68 + k * 22, 14, 58 + k * 22, 4, 2) for k in range(8)) +
            ln(150, 14, 150, 128, 1.8, B, ' stroke-dasharray="7 6"') + ln(150, 14, 212, 112, 3) +
            '<circle cx="216" cy="118" r="17" fill="url(#hz)" stroke="%s" stroke-width="3.2"/>' % B +
            path('M150,60 A46,46 0 0 0 176,54', 2.6) + T(163, 82, 'θ', 22, 0, 'middle', D) +
            path('M84,112 Q150,146 216,112', 2.4, B, 'none', ' stroke-dasharray="6 6"') + spark(94, 60, 10))


def i_wave():
    return (ln(4, 76, 294, 76, 1.8, B, ' stroke-dasharray="6 6"') + sine(4, 76, 290, 42, 1.5, 3.6) +
            T(52, 22, 'crest', 20, 0, 'middle', D) + T(150, 136, 'trough', 20, 0, 'middle', D) +
            path('M52,28 L52,34', 2.4) + path('M52,40 L65,32', 0) + ln(52, 118 - 84, 52, 118 - 84, 1) +
            path('M52,26 L246,26', 2.2, B, 'none', ' stroke-dasharray="3 5"') +
            T(250, 22, 'λ', 24, 0, 'start', D))


def i_two_sources():
    o = ''
    for cx in (80, 190):
        for r in (18, 38, 58, 78):
            o += '<circle cx="%d" cy="76" r="%d" fill="none" stroke="%s" stroke-width="2.4" opacity="%.2f"/>' % (
                cx, r, B, 1 - r / 110)
        o += '<circle cx="%d" cy="76" r="7" fill="%s"/>' % (cx, D)
    return o + T(80, 132, 'S₁', 20, 0, 'middle', D) + T(190, 132, 'S₂', 20, 0, 'middle', D) + spark(270, 30, 11)


def i_standing():
    o = ln(18, 30, 18, 122, 4) + ln(282, 30, 282, 122, 4)
    o += sine(18, 76, 264, 38, 1.5, 3.2) + sine(18, 76, 264, 38, 1.5, 2, B, math.pi)
    for k in range(4):
        x = 18 + 264 * k / 3
        o += '<circle cx="%.1f" cy="76" r="6" fill="%s"/>' % (x, D)
    return o + T(106, 136, 'N', 20, 0, 'middle', D) + T(62, 24, 'A', 20, 0, 'middle', D)


def i_refraction():
    o = '<rect x="4" y="80" width="292" height="56" fill="url(#hl)"/>' + ln(4, 80, 296, 80, 3.4)
    for k in range(5):
        x = 20 + k * 30
        o += ln(x, 12, x + 40, 80, 3)
    for k in range(5):
        x = 60 + k * 30
        o += ln(x, 80, x + 12, 134, 3)
    return o + T(230, 40, 'deep', 22, 0, 'middle', D) + T(250, 120, 'shallow', 18, 0, 'middle', D)


def i_speaker():
    return ('<rect x="20" y="52" width="40" height="46" rx="5" fill="url(#hz)" stroke="%s" stroke-width="3.4"/>' % B +
            path('M60,52 L104,20 L104,130 L60,98 Z', 3.4, B, '#fff') +
            ''.join(path('M%d,%d Q%d,75 %d,%d' % (126 + k * 34, 38 - k * 10, 146 + k * 40, 126 + k * 34, 112 + k * 10), 3)
                    for k in range(4)) + T(262, 26, '♪', 32, 0, 'middle', D) + T(284, 128, '♫', 26, 0, 'middle', D))


def i_ambulance():
    o = ''.join(path('M%d,%d Q%d,78 %d,%d' % (24 + k * 20, 48 - k * 8, 8 + k * 16, 24 + k * 20, 108 + k * 8), 2.6)
                for k in range(3))
    o += ('<rect x="90" y="50" width="130" height="58" rx="8" fill="#fff" stroke="%s" stroke-width="3.4"/>' % B +
          path('M220,64 L256,64 L276,86 L276,108 L220,108 Z', 3.4, B, 'url(#hz)') +
          path('M148,62 L148,96 M131,79 L165,79', 5, '#DC2626') +
          '<circle cx="124" cy="112" r="13" fill="#fff" stroke="%s" stroke-width="3.4"/>' % B +
          '<circle cx="246" cy="112" r="13" fill="#fff" stroke="%s" stroke-width="3.4"/>' % B +
          '<rect x="140" y="38" width="22" height="12" rx="3" fill="%s" stroke="%s" stroke-width="2"/>' % (Y, D))
    o += ''.join(path('M%d,%d Q%d,78 %d,%d' % (286 + k * 10, 56 + k * 4, 296 + k * 12, 286 + k * 10, 100 - k * 4), 2.4)
                 for k in range(2))
    return o


def i_fibre():
    o = path('M8,96 C80,96 110,40 180,40 C240,40 262,70 296,70', 22, '#8DB4E6', 'none', ' opacity="0.55"')
    o += path('M8,96 C80,96 110,40 180,40 C240,40 262,70 296,70', 3, B)
    pts = [(10, 92), (46, 104), (82, 76), (112, 58), (146, 34), (180, 50), (214, 34), (250, 58), (292, 66)]
    o += '<polyline points="%s" fill="none" stroke="#DC2626" stroke-width="3" stroke-linejoin="round"/>' % \
        ' '.join('%d,%d' % p for p in pts)
    return o + spark(40, 30, 11) + T(200, 128, 'optical fibre', 20, 0, 'middle', D)


def i_lens():
    o = path('M150,12 Q180,76 150,140 Q120,76 150,12 Z', 3.4, B, 'url(#hz)') + ln(4, 76, 296, 76, 1.8, B,
                                                                              ' stroke-dasharray="6 6"')
    for y in (36, 56, 96, 116):
        o += ln(10, y, 150, y, 2.8) + ln(150, y, 250, 76, 2.8)
    o += '<circle cx="250" cy="76" r="6" fill="%s"/>' % D
    return o + T(250, 106, 'F', 22, 0, 'middle', D) + spark(282, 30, 11)


def i_double_slit():
    o = '<rect x="96" y="6" width="16" height="44" fill="url(#hz)" stroke="%s" stroke-width="3"/>' % B
    o += '<rect x="96" y="62" width="16" height="30" fill="url(#hz)" stroke="%s" stroke-width="3"/>' % B
    o += '<rect x="96" y="104" width="16" height="40" fill="url(#hz)" stroke="%s" stroke-width="3"/>' % B
    o += ''.join(path('M%d,20 L%d,132' % (20 + k * 18, 20 + k * 18), 2.4) for k in range(4))
    for k in range(7):
        y = 18 + k * 18
        o += '<rect x="258" y="%d" width="30" height="10" rx="3" fill="%s"/>' % (y, Y if k % 2 == 0 else D)
    o += ln(112, 56, 258, 76, 1.8, B, ' stroke-dasharray="6 5"') + ln(112, 98, 258, 76, 1.8, B, ' stroke-dasharray="6 5"')
    return o


def i_tuning_fork():
    return (path('M120,130 L120,90 M100,90 L100,20 M140,90 L140,20 M100,90 Q120,110 140,90', 7, B) +
            ''.join(path('M%d,%d Q%d,55 %d,%d' % (170 + k * 26, 24 - k * 4, 184 + k * 30, 170 + k * 26, 86 + k * 4), 3)
                    for k in range(3)) +
            ''.join(path('M%d,%d Q%d,55 %d,%d' % (70 - k * 26, 24 - k * 4, 56 - k * 30, 70 - k * 26, 86 + k * 4), 3)
                    for k in range(3)))


def i_scope():
    o = '<rect x="20" y="10" width="220" height="120" rx="12" fill="#fff" stroke="%s" stroke-width="3.6"/>' % B
    o += ''.join(ln(20 + k * 44, 12, 20 + k * 44, 128, 1, '#8DB4E6') for k in range(1, 5))
    o += ''.join(ln(22, 10 + k * 30, 238, 10 + k * 30, 1, '#8DB4E6') for k in range(1, 4))
    o += sine(28, 70, 204, 40, 2, 3.4, '#DC2626')
    o += ''.join('<circle cx="268" cy="%d" r="11" fill="url(#hz)" stroke="%s" stroke-width="3"/>' % (36 + k * 36, B)
                 for k in range(3))
    return o


def i_clock():
    o = '<rect x="80" y="4" width="110" height="136" rx="16" fill="#fff" stroke="%s" stroke-width="3.6"/>' % B
    o += '<circle cx="135" cy="44" r="30" fill="url(#hz)" stroke="%s" stroke-width="3"/>' % B
    o += ln(135, 44, 135, 24, 3.4, D) + ln(135, 44, 150, 50, 3.4, D)
    o += ln(135, 76, 158, 124, 2.6) + '<circle cx="160" cy="126" r="10" fill="%s" stroke="%s" stroke-width="2"/>' % (Y, D)
    o += path('M104,120 Q135,142 166,120', 2, B, 'none', ' stroke-dasharray="5 5"')
    # T = 2π √(L/g) with a drawn radical sign and a bar over the whole L/g
    return o + ('<g transform="rotate(-8 236 60)">' + T(222, 60, 'T = 2π', 18, 0, 'end', D) +
                path('M224,53 L228,51 L233,63 L239,43 L268,43', 1.8, D) + T(241, 60, 'L/g', 18, 0, 'start', D) + '</g>')


ICONS = [i_spring_block, i_vertical_spring, i_pendulum, i_wave, i_two_sources, i_standing, i_refraction,
         i_speaker, i_ambulance, i_fibre, i_lens, i_double_slit, i_tuning_fork, i_scope, i_clock]

# (left icon, right icon, small icon, left phrase, right phrase, footer tagline)
THEMES = [
    (0, 3, 12, ('Oscillate', 'Repeat', 'Master'), ('Every', 'Cycle', 'Counts'), 'Keep Calm and Oscillate ...'),
    (1, 13, 2, ('Stretch', 'Release', 'Repeat'), ('Find', 'Your', 'Frequency'), 'Stay in Phase with Success ...'),
    (2, 14, 0, ('Swing', 'Time', 'Measure'), ('Small', 'Angles,', 'Big Ideas'), 'Life Has Its Periods ... Use Them Well'),
    (3, 7, 5, ('Crest', 'Trough', 'Wavelength'), ('Ride', 'The', 'Wave'), 'Make Waves ... Not Excuses'),
    (4, 11, 3, ('Meet', 'Overlap', 'Combine'), ('Think', 'Constructively', ''), 'In Phase ... Always Constructive'),
    (5, 12, 4, ('Nodes', 'Antinodes', 'Harmony'), ('Stand', 'Still, Keep', 'Vibrating'), 'Find Your Resonance ...'),
    (6, 10, 7, ('Enter', 'Bend', 'Continue'), ('Bend,', "Don't", 'Break'), 'Change the Medium ... Not the Frequency'),
    (7, 8, 13, ('Vibrate', 'Travel', 'Hear'), ('Sound', 'Mind,', 'Sound Physics'), 'Loud and Clear ... Physics Is Here'),
    (8, 3, 7, ('Approach', 'Pass', 'Recede'), ('Higher', 'Pitch', 'Ahead'), 'Move Closer ... Hear the Change'),
    (9, 10, 6, ('Reflect', 'Refract', 'Guide'), ('Totally', 'Internally', 'Motivated'), 'Beyond the Critical Angle ...'),
    (10, 11, 9, ('Converge', 'Diverge', 'Image'), ('Focus', 'On Your', 'Goal'), 'Sharp Focus ... Clear Future'),
    (11, 4, 10, ('Two Slits', 'One Light', 'Many Fringes'), ('Bright', 'Ideas', 'Only'),
     'Every Dark Fringe Has a Bright Neighbour'),
    (12, 7, 1, ('Strike', 'Listen', 'Tune'), ('Tune', 'In To', 'Physics'), 'Stay Tuned ... Keep Solving'),
    (13, 0, 14, ('Measure', 'Analyse', 'Solve'), ('Frequency', 'Of', 'Success'), 'Amplitude Up ... Keep Going'),
]


def _place(icon, x, y, s):
    return '<g transform="translate(%s,%s) scale(%s)">%s</g>' % (x, y, s, ICONS[icon]())


def _cascade(x, y, words, size=25, rot=-12, step=(12, 27)):
    return ''.join(T(x + k * step[0], y + k * step[1], w, size, rot) for k, w in enumerate(words) if w)


def header_svg(t):
    li, ri, si, lw, rw, _ = THEMES[t]
    o = ['<path d="M0,10 L1900,10 L1900,130 %s L0,130 Z" fill="url(#band)"/>' %
         ' '.join('L%d,%.1f' % (x, 130 + 6 * math.sin(x / (40 + 6 * t))) for x in range(1900, -1, -20))]
    o.append(_place(li, 10, 4, 0.96))
    o.append(_cascade(318, 52, lw))
    # the Z BANK logo with wave lines instead of speed lines
    for s in (-1, 1):
        cx = 950 + s * 290
        for k in range(3):
            o.append(sine(cx if s > 0 else cx - 64, 36 + k * 34, 64, 5, 1.5 + 0.5 * k, 3))
    o.append('<text x="953" y="92" font-size="96" text-anchor="middle" style="font-family:\'Titan One\'" '
             'fill="%s" opacity="0.9">Z BANK</text>' % D)
    o.append('<text x="946" y="87" font-size="96" text-anchor="middle" style="font-family:\'Titan One\'" '
             'fill="url(#hz)" stroke="%s" stroke-width="3.2">Z BANK</text>' % D)
    o.append(T(950, 127, 'Oscillations &amp; Waves&#160;&#160;·&#160;&#160;Question Bank', 27, -1.2, 'middle', D))
    o.append(spark(700, 40, 12) + spark(1206, 118, 10))
    o.append(_place(ri, 1370, 12, 0.62))
    o.append(_cascade(1570, 52, rw, 24, -12, (12, 26)))
    o.append(_place(si, 1778, 18, 0.4))
    o.append(sine(14, 146, 1872, 4, 22 + t, 3.4))
    o.append('<path d="M40,152 Q950,149 1860,153" fill="none" stroke="%s" stroke-width="1.4" opacity="0.7"/>' % B)
    return ('<svg class="hdr" viewBox="0 0 1900 158" xmlns="http://www.w3.org/2000/svg"><defs>' + DEFS +
            '</defs><g filter="url(#sk)">' + ''.join(o) + '</g></svg>')


def footer_svg(t, num='{{N}}'):
    _, ri, si, _, _, tag = THEMES[t]
    o = []
    # page number badge : circle, sun or gear, by theme
    kind = t % 3
    if kind == 1:
        for k in range(12):
            a = k * math.pi / 6
            o.append(ln(72 + 50 * math.cos(a), 62 + 50 * math.sin(a), 72 + 60 * math.cos(a), 62 + 60 * math.sin(a), 3))
    if kind == 2:
        pts = []
        for k in range(32):
            a = k * math.pi / 16
            r = 52 if (k // 2) % 2 == 0 else 44
            pts.append('%.1f,%.1f' % (72 + r * math.cos(a), 62 + r * math.sin(a)))
        o.append('<polygon points="%s" fill="url(#hl)" stroke="%s" stroke-width="3"/>' % (' '.join(pts), B))
    o.append('<circle cx="72" cy="62" r="42" fill="#fff" stroke="%s" stroke-width="3.2"/>' % B)
    o.append('<circle cx="72" cy="62" r="35" fill="none" stroke="%s" stroke-width="1.6" stroke-dasharray="4 5"/>' % B)
    o.append('<text x="75" y="84" font-size="50" text-anchor="middle" style="font-family:\'Chunk\'" fill="#111" '
             'stroke="#111" stroke-width="3">%s</text>' % num)
    o.append('<text x="72" y="81" font-size="50" text-anchor="middle" style="font-family:\'Chunk\'" fill="#fff" '
             'stroke="#111" stroke-width="3" paint-order="stroke">%s</text>' % num)
    # a travelling wave from the badge to the centre
    o.append(sine(118, 58, 690, 7, 6 + t % 4, 3))
    o.append(T(140, 96, tag, 25, 0, 'start', D, ';font-style:italic'))
    # centre box
    o.append('<rect x="824" y="30" width="252" height="56" rx="16" fill="#fff" stroke="%s" stroke-width="3.2"/>' % B)
    o.append('<rect x="832" y="37" width="236" height="42" rx="12" fill="none" stroke="%s" stroke-width="1.4"/>' % B)
    o.append(T(950, 70, 'Z&#160;&#160;BANK', 32, 0, 'middle', D))
    o.append(sine(1092, 58, 540, 7, 5 + (t + 1) % 4, 3))
    o.append(T(1480, 96, 'Oscillations &amp; Waves', 26, 0, 'middle', D, ';font-style:italic'))
    o.append(path('M1356,110 Q1500,120 1640,100', 2.6) + path('M1622,94 L1642,99 L1630,114', 2.6))
    # the chapter badge with a small icon
    o.append('<rect x="1690" y="24" width="190" height="70" rx="12" fill="url(#hz)" stroke="%s" stroke-width="3" '
             'transform="rotate(-4 1785 59)"/>' % B)
    o.append('<text x="1786" y="56" font-size="26" text-anchor="middle" style="font-family:\'Chunk\'" fill="#fff" '
             'stroke="%s" stroke-width="2.6" paint-order="stroke" transform="rotate(-4 1786 50)">CHAPTER</text>' % D)
    o.append('<text x="1786" y="90" font-size="36" text-anchor="middle" style="font-family:\'Chunk\'" fill="%s" '
             'stroke="%s" stroke-width="2" paint-order="stroke" transform="rotate(-4 1786 80)">2</text>' % (Y, D))
    o.append(spark(1680, 22, 10) + spark(1892, 96, 8))
    return ('<svg class="ftr" viewBox="0 0 1900 122" xmlns="http://www.w3.org/2000/svg"><defs>' + DEFS +
            '</defs><g filter="url(#sk)">' + ''.join(o) + '</g></svg>')

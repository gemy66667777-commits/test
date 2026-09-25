# -*- coding: utf-8 -*-
"""The Z BANK page frame : doodle header, doodle footer, and the page CSS."""

BLUE = '#2556A8'      # ink blue of the doodles
DEEP = '#1B3F85'
LIGHT = '#5C96D6'     # the solid offset shadow of every box
LINE = '#3D7CC9'      # box outline
HATCH = '#8DB4E6'

SKETCH = ('<filter id="sk" x="-5%%" y="-20%%" width="110%%" height="140%%">'
          '<feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="7" result="n"/>'
          '<feDisplacementMap in="SourceGraphic" in2="n" scale="2.6" xChannelSelector="R" '
          'yChannelSelector="G"/></filter>'
          '<pattern id="hz" width="7" height="7" patternUnits="userSpaceOnUse" '
          'patternTransform="rotate(38)"><rect width="7" height="7" fill="#DCE8F8"/>'
          '<line x1="0" y1="0" x2="0" y2="7" stroke="%s" stroke-width="2.6"/></pattern>'
          '<pattern id="hl" width="6" height="6" patternUnits="userSpaceOnUse" '
          'patternTransform="rotate(38)"><line x1="0" y1="0" x2="0" y2="6" stroke="%s" '
          'stroke-width="1.2"/></pattern>' % (HATCH, HATCH))

HAND = "font-family:'Kalam';font-weight:700"


def _t(x, y, s, size, rot=0, anchor='start', col=BLUE, fam=HAND, extra=''):
    tr = ' transform="rotate(%s %s %s)"' % (rot, x, y) if rot else ''
    return ('<text x="%s" y="%s" font-size="%s" fill="%s" text-anchor="%s" style="%s"%s%s>%s</text>'
            % (x, y, size, col, anchor, fam, tr, extra, s))


def header_svg():
    o = []
    a = o.append
    # --- the stack of books -------------------------------------------------
    for k, (lab, x0, w) in enumerate((('ENERGY', 22, 238), ('MOTION', 34, 222), ('FORCE', 26, 214))):
        y = 108 - k * 36
        a('<path d="M%d,%d h%d q10,0 10,15 q0,15 -10,15 h-%d z" fill="url(#hl)" stroke="%s" '
          'stroke-width="3"/>' % (x0, y, w, w, BLUE))
        a('<path d="M%d,%d q-12,0 -12,15 q0,15 12,15" fill="#fff" stroke="%s" stroke-width="3"/>'
          % (x0 + 4, y, BLUE))
        a('<rect x="%d" y="%d" width="%d" height="22" rx="3" fill="#fff" stroke="%s" stroke-width="2.4"/>'
          % (x0 + 70, y + 4, 124, BLUE))
        a(_t(x0 + 132, y + 21, lab, 17, 0, 'middle', BLUE, "font-family:'Kalam';font-weight:700;"
             "letter-spacing:1px;font-style:italic"))
    # --- F arrow and the ramp with the ball ----------------------------------
    a('<line x1="300" y1="130" x2="300" y2="22" stroke="%s" stroke-width="3"/>' % BLUE)
    a('<path d="M291,34 L300,16 L309,34" fill="none" stroke="%s" stroke-width="3"/>' % BLUE)
    a(_t(310, 30, 'F', 22))
    a('<path d="M306,130 L462,130 L462,64 Z" fill="url(#hl)" stroke="%s" stroke-width="3"/>' % BLUE)
    a('<circle cx="378" cy="88" r="17" fill="#fff" stroke="%s" stroke-width="3"/>' % BLUE)
    a('<path d="M386,74 L418,46" stroke="%s" stroke-width="3"/><path d="M404,44 L420,44 L417,60" '
      'fill="none" stroke="%s" stroke-width="3"/>' % (BLUE, BLUE))
    # --- Solve / Practice / Master -------------------------------------------
    a(_t(508, 70, 'Solve', 25, -12))
    a(_t(518, 100, 'Practice', 25, -12))
    a(_t(546, 128, 'Master', 25, -12))
    # --- Z BANK --------------------------------------------------------------
    for dx, dy, ang in ((-1, 1, 0),):
        pass
    for s in (-1, 1):
        cx = 950 + s * 285
        for k, (ln, yy) in enumerate(((34, 34), (46, 72), (34, 108))):
            a('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3.2" stroke-linecap="round"/>'
              % (cx, yy, cx + s * ln, yy + (-10 if k == 0 else (10 if k == 2 else 0)) * 1, BLUE))
    a('<text x="953" y="93" font-size="98" text-anchor="middle" style="font-family:\'Titan One\'" '
      'fill="%s" opacity="0.9">Z BANK</text>' % DEEP)
    a('<text x="946" y="88" font-size="98" text-anchor="middle" style="font-family:\'Titan One\'" '
      'fill="url(#hz)" stroke="%s" stroke-width="3.2">Z BANK</text>' % DEEP)
    a(_t(950, 128, 'Mechanics&#160;&#160;Question&#160;&#160;Bank', 29, -1.5, 'middle', DEEP))
    a('<path d="M780,138 Q950,128 1120,137" fill="none" stroke="%s" stroke-width="2.4"/>' % BLUE)
    # --- the lightbulb ---------------------------------------------------------
    bx, by = 1455, 62
    a('<path d="M%d,%d a34,34 0 1 1 30,0 q-6,10 -6,22 h-18 q0,-12 -6,-22 z" fill="#fff" '
      'stroke="%s" stroke-width="3.2" transform="translate(-15,0)"/>' % (bx, by + 26, BLUE))
    for k in range(3):
        a('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3"/>'
          % (bx - 13, by + 54 + k * 7, bx + 13, by + 54 + k * 7, BLUE))
    a('<path d="M%d,%d q9,-14 18,0" fill="none" stroke="%s" stroke-width="2.4"/>' % (bx - 9, by + 30, BLUE))
    for ang in (-150, -120, -90, -60, -30, 180, 0):
        import math
        r1, r2 = 50, 64
        c, s_ = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        a('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="3.2" '
          'stroke-linecap="round"/>' % (bx + r1 * c, by + 8 + r1 * s_, bx + r2 * c, by + 8 + r2 * s_, BLUE))
    # --- Good / Physics / Brighter / You -----------------------------------
    a(_t(1552, 60, 'Good', 24, -14))
    a(_t(1566, 86, 'Physics', 24, -14))
    a(_t(1580, 111, 'Brighter', 24, -14))
    a(_t(1624, 131, 'You', 22, -14))
    a('<path d="M1600,142 Q1668,140 1700,112" fill="none" stroke="%s" stroke-width="2.4"/>'
      '<path d="M1688,112 L1702,110 L1700,124" fill="none" stroke="%s" stroke-width="2.4"/>' % (BLUE, BLUE))
    # --- the gear -------------------------------------------------------------
    gx, gy, R = 1826, 76, 52
    pts = []
    import math
    for k in range(40):
        ang = k * math.pi / 20
        rr = R if (k // 2) % 2 == 0 else R - 13
        pts.append('%.1f,%.1f' % (gx + rr * math.cos(ang + 0.08), gy + rr * math.sin(ang + 0.08)))
    a('<polygon points="%s" fill="url(#hl)" stroke="%s" stroke-width="3.4" stroke-linejoin="round"/>'
      % (' '.join(pts), BLUE))
    a('<circle cx="%d" cy="%d" r="24" fill="#fff" stroke="%s" stroke-width="3.4"/>' % (gx, gy, BLUE))
    a('<circle cx="%d" cy="%d" r="10" fill="#fff" stroke="%s" stroke-width="3.4"/>' % (gx, gy, BLUE))
    for s in (-1, 1):
        a('<path d="M%d,%d q%d,40 0,80" fill="none" stroke="%s" stroke-width="2.6"/>'
          % (gx + s * 70, gy - 40, s * 16, BLUE))
        a('<path d="M%d,%d q%d,26 0,52" fill="none" stroke="%s" stroke-width="2.2"/>'
          % (gx + s * 82, gy - 26, s * 10, BLUE))
    # --- the rule under everything ------------------------------------------
    a('<path d="M14,146 Q950,142 1886,147" fill="none" stroke="%s" stroke-width="3.4"/>' % BLUE)
    a('<path d="M40,151 Q950,149 1860,152" fill="none" stroke="%s" stroke-width="1.4" opacity="0.7"/>' % BLUE)
    return ('<svg class="hdr" viewBox="0 0 1900 156" xmlns="http://www.w3.org/2000/svg"><defs>' + SKETCH +
            '</defs><g filter="url(#sk)">' + ''.join(o) + '</g></svg>')


def footer_svg(num_placeholder='{{N}}', block='Block', blockno='1'):
    o = []
    a = o.append
    # page number doodle
    a('<circle cx="72" cy="62" r="46" fill="#fff" stroke="%s" stroke-width="3.2"/>' % BLUE)
    a('<circle cx="72" cy="62" r="38" fill="none" stroke="%s" stroke-width="1.6" '
      'stroke-dasharray="4 5"/>' % BLUE)
    for (x, y, r) in ((128, 26, 7), (143, 40, 4.5), (22, 104, 5), (130, 104, 4)):
        a('<circle cx="%d" cy="%d" r="%s" fill="none" stroke="%s" stroke-width="2.2"/>' % (x, y, r, BLUE))
    a('<text x="72" y="80" font-size="50" text-anchor="middle" style="font-family:\'Chunk\'" '
      'fill="#fff" stroke="#111" stroke-width="3" paint-order="stroke">%s</text>' % num_placeholder)
    # loop squiggle then the long line
    a('<path d="M122,72 C170,40 200,110 238,70 C262,44 290,52 282,78 C276,94 256,90 262,70 '
      'C270,50 300,58 330,58" fill="none" stroke="%s" stroke-width="3"/>' % BLUE)
    a('<path d="M330,58 L800,58" stroke="%s" stroke-width="3"/>' % BLUE)
    a('<path d="M1100,58 L1640,58" stroke="%s" stroke-width="3"/>' % BLUE)
    a(_t(334, 88, 'Motion Today ... A Better Tomorrow', 26, 0, 'start', DEEP,
         "font-family:'Kalam';font-weight:700;font-style:italic"))
    # centre : Z BANK in a box with speed lines
    for s in (-1, 1):
        for k, ln in enumerate((70, 95, 70)):
            x0 = 950 + s * 128
            a('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2.6"/>'
              % (x0, 48 + k * 10, x0 + s * ln, 48 + k * 10, BLUE))
    a('<rect x="824" y="32" width="252" height="56" rx="16" fill="#fff" stroke="%s" stroke-width="3.2"/>' % BLUE)
    a('<rect x="832" y="39" width="236" height="42" rx="12" fill="none" stroke="%s" stroke-width="1.4"/>' % BLUE)
    a(_t(950, 72, 'Z&#160;&#160;BANK', 32, 0, 'middle', DEEP, "font-family:'Kalam';font-weight:700"))
    # right : Mechanics with a swoosh arrow
    a(_t(1560, 88, 'Mechanics', 27, 0, 'middle', DEEP, "font-family:'Kalam';font-weight:700;font-style:italic"))
    a('<path d="M1500,100 Q1580,108 1638,84" fill="none" stroke="%s" stroke-width="2.6"/>'
      '<path d="M1622,82 L1640,82 L1634,98" fill="none" stroke="%s" stroke-width="2.6"/>' % (BLUE, BLUE))
    # Block badge
    a('<rect x="1702" y="30" width="170" height="64" rx="10" fill="url(#hl)" stroke="%s" stroke-width="3" '
      'transform="rotate(-4 1787 62)"/>' % BLUE)
    a('<text x="1770" y="84" font-size="46" text-anchor="middle" style="font-family:\'Chunk\'" '
      'fill="#fff" stroke="%s" stroke-width="3" paint-order="stroke" transform="rotate(-4 1770 70)">%s</text>'
      % (DEEP, block))
    a('<rect x="1832" y="22" width="40" height="66" rx="5" fill="#fff" stroke="%s" stroke-width="3" '
      'transform="rotate(-4 1852 55)"/>' % DEEP)
    a('<text x="1852" y="78" font-size="48" text-anchor="middle" style="font-family:\'Chunk\'" '
      'fill="%s" transform="rotate(-4 1852 60)">%s</text>' % (DEEP, blockno))
    for (x1, y1, x2, y2) in ((1690, 40, 1676, 30), (1686, 62, 1668, 62), (1880, 20, 1892, 8), (1888, 70, 1900, 76)):
        a('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2.6" stroke-linecap="round"/>'
          % (x1, y1, x2, y2, BLUE))
    return ('<svg class="ftr" viewBox="0 0 1900 120" xmlns="http://www.w3.org/2000/svg"><defs>' + SKETCH +
            '</defs><g filter="url(#sk)">' + ''.join(o) + '</g></svg>')


def fontfaces(path='ttf'):
    """Vintage Vignette for the text ; its free edition has placeholder glyphs for 0-4, so all the
    digits 0-9 come from Comfortaa Bold (a very close rounded face).  Jackport College for the question
    numbers, Chunk Five Print for I / II / III."""
    return ("@font-face{font-family:'ZB';src:url(%(p)s/VintageVignette.ttf);font-weight:700}"
            "@font-face{font-family:'ZB';src:url(%(p)s/Comfortaa.ttf);font-weight:700;unicode-range:U+0030-0039}"
            "@font-face{font-family:'ZBsym';src:url(%(p)s/Comfortaa.ttf);font-weight:300 700}"
            "@font-face{font-family:'Jackport';src:url(%(p)s/JackportCollege.ttf)}"
            "@font-face{font-family:'Chunk';src:url(%(p)s/Chunk.ttf)}"
            "@font-face{font-family:'Kalam';src:url(%(p)s/Kalam.ttf);font-weight:700}"
            "@font-face{font-family:'Titan One';src:url(%(p)s/TitanOne.ttf)}" % dict(p=path))


BORDER = '#82A9D0'
SHADOW = '#5A9BD5'
RING = '#46638F'

CSS = """
@page { size:A4; margin:0; }
* { box-sizing:border-box; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
html, body { margin:0; padding:0; background:#fff; }
body { font-family:'ZB', 'ZBsym', sans-serif; font-weight:700; color:#111; }
#flow { position:absolute; left:-9999px; top:0; width:188.1mm; }
.page { width:210mm; height:297mm; position:relative; overflow:hidden; break-after:page; background:#fff; }
.page:last-child { break-after:auto; }
.page .hdr { position:absolute; left:4mm; top:1.2mm; width:202mm; }
.page .ftr { position:absolute; left:4mm; bottom:1.8mm; width:202mm; }
.page .body { position:absolute; left:10.2mm; right:11.7mm; top:19.3mm; bottom:18.5mm; }
.qtext { font-size:12pt; line-height:1.21; }

/* ---- one question ---- */
.q { position:relative; padding-top:4.6mm; }
.dg { -webkit-text-stroke:0.55px currentColor; text-shadow:0.3px 0.35px 0 rgba(0,0,0,0.5); }
.rt { display:inline-block; position:relative; padding:0.27em 0.12em 0 0.9em; margin:0 0.04em; line-height:1em; }
.rt > .sg { position:absolute; left:0; top:0; width:100%%; height:1.2em; overflow:hidden; }
.rt > .sg > svg { position:absolute; left:0; top:0; width:400em; height:1.2em; }
.q.cont { padding-top:0; }
.stem, .part { position:relative; background:#fff; border:0.45mm solid %(B)s; border-radius:3.2mm;
        box-shadow:2.2mm 2.1mm 0 %(S)s; }
.stem { padding:2.3mm 6.8mm 2.3mm 12.4mm; margin-bottom:3mm; }
.part { padding:2.3mm 5mm 2.3mm 12.4mm; margin-bottom:3mm; }
.bub { position:absolute; left:-2.6mm; top:-4.5mm; width:12.6mm; height:12.6mm; }
.bub svg { position:absolute; left:0; top:0; width:12.6mm; height:12.6mm; overflow:visible; }
.bub .num { position:absolute; left:0; top:0; width:12.6mm; height:12.6mm; display:flex; align-items:center;
        justify-content:center; font-family:'Chunk'; font-size:23pt; line-height:1; letter-spacing:-0.4pt; }
.bub .num i { position:relative; font-style:normal; filter:drop-shadow(0.25mm 0.3mm 0.2mm rgba(0,0,0,0.35)); }
.bub .num .b { position:absolute; left:0.6mm; top:0.6mm; color:#111; -webkit-text-stroke:1.2pt #111; }
.bub .num .f { position:relative; color:#fff; -webkit-text-stroke:1.2pt #111; paint-order:stroke fill; }
.stem .dood { position:absolute; right:-11.2mm; top:50%%; transform:translateY(-50%%); width:13mm; height:17mm; }
.part .rn { position:absolute; left:0; top:2.2mm; width:12.4mm; text-align:center; font-family:'Chunk';
        font-size:14pt; line-height:1; letter-spacing:-0.4pt; }
.rn .b { position:absolute; left:0.4mm; top:0.4mm; right:-0.4mm; color:#111; -webkit-text-stroke:0.9pt #111; }
.rn .f { position:relative; color:#fff; -webkit-text-stroke:0.9pt #111; paint-order:stroke fill; }
.space { height:26mm; }
.space.s { height:9mm; } .space.m { height:16mm; } .space.l { height:34mm; } .space.x { height:0.5mm; }
.q + .q:not(.cont) { margin-top:3mm; }
.ch { display:grid; grid-template-columns:repeat(4, 1fr); gap:1.2mm 3mm; margin-top:1.4mm; }
.ch.two { grid-template-columns:1fr 1fr; }
.ch.one { grid-template-columns:1fr; }
.ch b { color:#1B3F85; margin-right:1.2mm; }
.withfig { display:flex; gap:4mm; align-items:flex-start; }
.withfig .parts { flex:1; min-width:0; }
.withfig .figcol { flex:none; padding-top:1mm; }
.figc { text-align:center; margin:0 0 3mm; }
svg.fg { display:block; margin:0 auto; }
.dots { letter-spacing:1px; }
sub, sup { font-size:66%%; line-height:0; }
u { text-decoration-thickness:1.4px; text-underline-offset:2px; }

.lesson { position:relative; margin:1mm 0 6mm; background:#fff; border:0.45mm solid %(B)s; border-radius:4mm;
        box-shadow:2.2mm 2.1mm 0 %(S)s; padding:3.4mm 8mm 3.8mm; text-align:center; }
.lesson .lk { font-size:13pt; color:#2556A8; }
.lesson .lt { font-family:'Chunk'; font-size:25pt; color:#1B3F85; margin:1mm 0 1.2mm; letter-spacing:.3px; }
.lesson .ls { font-size:12pt; color:#334155; line-height:1.45; }
.lesson .ls b { color:#2556A8; }
.ans { position:relative; padding-top:4.6mm; }
.ans.cont { padding-top:0; }
.abox.jb { border-bottom:0; border-bottom-left-radius:0; border-bottom-right-radius:0; margin-bottom:0; padding-bottom:1.4mm; }
.abox.jt { border-top:0; border-top-left-radius:0; border-top-right-radius:0; padding-top:1.4mm; }
.abox { position:relative; background:#fff; border:0.45mm solid %(B)s; border-radius:3.2mm;
        box-shadow:2.2mm 2.1mm 0 %(S)s; padding:2.8mm 5mm 2.6mm 12.4mm; margin-bottom:3.4mm; }
.ap { position:relative; margin:0 0 2.4mm; }
.abox > .bub + .ap { padding-top:4.6mm; }
.abox > .bub + .ap > .rn { top:4.9mm; }
.ap:last-child { margin-bottom:0; }
.ap .rn { position:absolute; left:-12.4mm; top:0.3mm; width:12.4mm; text-align:center; font-family:'Chunk';
        font-size:12.5pt; line-height:1; letter-spacing:-0.4pt; }
.ap .st { font-size:12pt; line-height:1.26; color:#1F2937; }
.ap .res { display:inline-block; margin-top:1mm; background:#E8F1FC; border:0.35mm solid %(B)s;
        border-radius:2mm; padding:0.4mm 2.6mm; font-size:12pt; color:#1B3F85; }
"""


def css():
    return CSS % dict(B=BORDER, S=SHADOW)


def stem_doodle():
    """the right end of every stem box : two white lobes with the same blue shadow, and three bubbles."""
    lobes = ('M10,20 C30,15 58,17 66,27 C76,40 66,53 50,55 C40,56 28,57 21,60 C31,67 52,79 60,91 '
             'C68,103 60,115 46,113 C34,111 22,105 10,108')
    return ('<svg class="dood" viewBox="0 0 100 130" xmlns="http://www.w3.org/2000/svg">'
            '<path d="%(p)s Z" transform="translate(6,7)" fill="%(S)s"/>'
            '<path d="%(p)s Z" fill="#fff"/>'
            '<path d="%(p)s" fill="none" stroke="%(B)s" stroke-width="1.7"/>'
            '<circle cx="80" cy="14" r="6.5" fill="#fff" stroke="%(S)s" stroke-width="2.6"/>'
            '<circle cx="61" cy="76" r="3.8" fill="#fff" stroke="%(S)s" stroke-width="2.2"/>'
            '<circle cx="76" cy="86" r="4.6" fill="%(S)s"/>'
            '</svg>' % dict(p=lobes, S=SHADOW, B=BORDER))


def bubble(n):
    """the round number bubble : a dark-blue ring, a light-blue crescent on its right and a small tail."""
    return ('<div class="bub"><svg viewBox="0 0 60 60">'
            '<path d="M13,47 L6,58 L20,51 Z" fill="#fff" stroke="%s" stroke-width="2.6" stroke-linejoin="round"/>'
            '<circle cx="32" cy="31" r="27" fill="#A9CDF0"/>'
            '<circle cx="30" cy="29" r="27" fill="#fff" stroke="%s" stroke-width="3"/>'
            '<path d="M14,50 L9,56 L19,52" fill="#fff"/>'
            '</svg><div class="num"><i><span class="b">%d</span><span class="f">%d</span></i></div></div>'
            % (RING, RING, n, n))

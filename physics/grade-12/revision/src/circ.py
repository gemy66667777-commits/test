# -*- coding: utf-8 -*-
"""Bright SVG drawings for electric circuits and graphs (Grade 12 revision booklet).

Every component is drawn on a straight segment p1 -> p2 : the wire is drawn to the component,
the component sits in the middle of the segment and the wire continues to p2."""
import math

WIRE = '#1e293b'
RES = '#f97316'
RES_H = '#fed7aa'
BATP = '#e11d48'
BATN = '#2563eb'
CUR = '#059669'
LAB = '#0f172a'
FONT = "font-family:'Liberation Sans',Arial,sans-serif"

# gradients shared by every figure (placed once at the top of the page)
DEFS = ('<svg width="0" height="0" style="position:absolute"><defs>'
        '<radialGradient id="gLamp" cx="50%" cy="45%" r="60%"><stop offset="0" stop-color="#fffbeb"/>'
        '<stop offset=".55" stop-color="#fde68a"/><stop offset="1" stop-color="#f59e0b"/></radialGradient>'
        '<radialGradient id="gLampOff" cx="50%" cy="45%" r="60%"><stop offset="0" stop-color="#ffffff"/>'
        '<stop offset="1" stop-color="#cbd5e1"/></radialGradient>'
        '<radialGradient id="gGlow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#fde047" stop-opacity=".75"/>'
        '<stop offset="1" stop-color="#fde047" stop-opacity="0"/></radialGradient>'
        '<linearGradient id="gAm" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fef3c7"/>'
        '<stop offset="1" stop-color="#fcd34d"/></linearGradient>'
        '<linearGradient id="gVm" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ede9fe"/>'
        '<stop offset="1" stop-color="#c4b5fd"/></linearGradient>'
        '<linearGradient id="gGm" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#dcfce7"/>'
        '<stop offset="1" stop-color="#86efac"/></linearGradient>'
        '<linearGradient id="gCu" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fde2c4"/>'
        '<stop offset=".35" stop-color="#f59e0b"/><stop offset=".7" stop-color="#b45309"/>'
        '<stop offset="1" stop-color="#78350f"/></linearGradient>'
        '<linearGradient id="gAl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1f5f9"/>'
        '<stop offset=".4" stop-color="#94a3b8"/><stop offset="1" stop-color="#334155"/></linearGradient>'
        '<linearGradient id="gFe" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e0e7ff"/>'
        '<stop offset=".4" stop-color="#818cf8"/><stop offset="1" stop-color="#312e81"/></linearGradient>'
        '<linearGradient id="gCell" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fecdd3"/>'
        '<stop offset="1" stop-color="#bfdbfe"/></linearGradient>'
        '<pattern id="gGrid" width="10" height="10" patternUnits="userSpaceOnUse">'
        '<path d="M10,0 L0,0 0,10" fill="none" stroke="#bae6fd" stroke-width=".7"/></pattern>'
        '<marker id="mArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
        '<path d="M0,0.8 L10,5 L0,9.2 z" fill="#0f172a"/></marker>'
        '<marker id="mArrP" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
        '<path d="M0,0.8 L10,5 L0,9.2 z" fill="#7c3aed"/></marker>'
        '<marker id="mArrPs" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
        '<path d="M10,0.8 L0,5 L10,9.2 z" fill="#7c3aed"/></marker>'
        '</defs></svg>')

BODY = {'R': 50, 'Rv': 50, 'B': 18, 'L': 26, 'A': 26, 'V': 26, 'G': 26, 'S': 34, 'W': 0}


def svgtext(s):
    """html sub / sup / i inside a label -> svg tspans."""
    s = s.replace('<sub>', '<tspan baseline-shift="sub" font-size="72%">').replace('</sub>', '</tspan>')
    s = s.replace('<sup>', '<tspan baseline-shift="super" font-size="72%">').replace('</sup>', '</tspan>')
    s = s.replace('<i>', '<tspan font-style="italic">').replace('</i>', '</tspan>')
    return s


def _t(x, y, s, c=LAB, size=13, anchor='middle', bold=True, it=False, extra=''):
    s = svgtext(s)
    return ('<text x="%.1f" y="%.1f" fill="%s" font-size="%s" text-anchor="%s" style="%s;font-weight:%s%s"%s>%s</text>'
            % (x, y, c, size, anchor, FONT, 700 if bold else 400, ';font-style:italic' if it else '', extra, s))


class Circ:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.o = []
        self.ext = [0, 0, w, h]          # the drawing box grows to keep every label inside

    # ------------------------------------------------------------------ basics
    def raw(self, s):
        self.o.append(s)

    def wire(self, *pts, c=WIRE, w=2.6, dash=None):
        d = ' stroke-dasharray="%s"' % dash if dash else ''
        self.o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round" '
                      'stroke-linecap="round"%s/>' % (' '.join('%.1f,%.1f' % p for p in pts), c, w, d))

    def node(self, x, y, lab=None, dx=0, dy=-10, c=WIRE, size=13):
        self.o.append('<circle cx="%.1f" cy="%.1f" r="4" fill="%s"/>' % (x, y, c))
        if lab:
            self.lab(x + dx, y + dy, lab, '#7c3aed', size)

    def term(self, x, y, lab=None, dx=0, dy=-10):
        """an open terminal (a small ring)."""
        self.o.append('<circle cx="%.1f" cy="%.1f" r="4.5" fill="#fff" stroke="%s" stroke-width="2.2"/>' % (x, y, WIRE))
        if lab:
            self.lab(x + dx, y + dy, lab, '#7c3aed', 13.5)

    def lab(self, x, y, s, c=LAB, size=13, anchor='middle', bg=True, it=False):
        if bg:
            import re
            n = len(re.sub(r'&[#a-z0-9]+;', 'x', re.sub(r'<sub>.*?</sub>|<sup>.*?</sup>', 'x', re.sub(r'<i>|</i>', '', s))))
            w = 0.62 * size * n + 6
            x0 = x - w / 2 if anchor == 'middle' else (x - 3 if anchor == 'start' else x - w + 3)
            self.o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="4" fill="#fff" fill-opacity=".88"/>'
                          % (x0, y - size * 0.86, w, size * 1.15))
            e = self.ext
            e[0], e[1] = min(e[0], x0 - 3), min(e[1], y - size * 0.9 - 3)
            e[2], e[3] = max(e[2], x0 + w + 3), max(e[3], y + size * 0.35 + 3)
        self.o.append(_t(x, y, s, c, size, anchor, it=it))

    def txt(self, x, y, s, c=LAB, size=13, anchor='middle', bold=True, it=False):
        self.o.append(_t(x, y, s, c, size, anchor, bold, it))

    def arrow(self, x1, y1, x2, y2, c='#0f172a', w=2, dash=None, both=False):
        d = ' stroke-dasharray="%s"' % dash if dash else ''
        m = 'mArrP' if c == '#7c3aed' else 'mArr'
        s = ' marker-start="url(#mArrPs)"' if both else ''
        self.o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s"%s '
                      'marker-end="url(#%s)"%s/>' % (x1, y1, x2, y2, c, w, d, m, s))

    def cur(self, x, y, d, lab=None, ldx=0, ldy=-11, c=CUR):
        """a current arrow head on a wire pointing r / l / u / d."""
        ang = {'r': 0, 'l': 180, 'u': -90, 'd': 90}[d]
        self.o.append('<path d="M-7,-6 L7,0 L-7,6 z" fill="%s" transform="translate(%.1f %.1f) rotate(%d)"/>'
                      % (c, x, y, ang))
        if lab:
            self.lab(x + ldx, y + ldy, lab, c, 13, it=True)

    # ------------------------------------------------------------------ components
    def comp(self, kind, p1, p2, lab=None, side=1, lc=None, size=13, **kw):
        (x1, y1), (x2, y2) = p1, p2
        L = math.hypot(x2 - x1, y2 - y1)
        ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        mx, my = (x1 + x2) / 2 + kw.get('shift', 0) * ux, (y1 + y2) / 2 + kw.get('shift', 0) * uy
        b = kw.get('body', BODY[kind])
        if kind != 'W':
            self.wire((x1, y1), (mx - ux * b / 2, my - uy * b / 2))
            self.wire((mx + ux * b / 2, my + uy * b / 2), (x2, y2))
        else:
            self.wire((x1, y1), (x2, y2))
        g = getattr(self, '_' + kind.lower() if kind != 'Rv' else '_rv')
        self.o.append('<g transform="translate(%.1f %.1f) rotate(%.2f)">%s</g>' % (mx, my, ang, g(b, ang=ang, **kw)))
        if lab:
            nx, ny = -uy, ux                      # the normal, pointing "below" a left-to-right segment
            off = kw.get('loff', {'R': 17, 'Rv': 19, 'B': 25, 'L': 23, 'A': 22, 'V': 22, 'G': 22, 'S': 19, 'W': 12}[kind])
            lx, ly = mx - side * nx * off, my - side * ny * off
            if abs(uy) > 0.9:                     # a vertical segment : the label goes to the side
                anchor = 'start' if (-side * nx) > 0 else 'end'
                ly += size * 0.35
            else:
                anchor = 'middle'
                ly += size * 0.35
            self.lab(lx, ly, lab, lc or LAB, size, anchor)

    def _w(self, b, **kw):
        return ''

    def _r(self, b, n=6, **kw):
        h = 7.5
        pts = [(-b / 2, 0)]
        for k in range(n):
            x = -b / 2 + b * (k + 0.5) / n
            pts.append((x, -h if k % 2 == 0 else h))
        pts.append((b / 2, 0))
        p = ' '.join('%.1f,%.1f' % q for q in pts)
        col = kw.get('col', RES)
        return ('<polyline points="%s" fill="none" stroke="%s" stroke-width="7" stroke-linejoin="round" opacity=".6"/>'
                '<polyline points="%s" fill="none" stroke="%s" stroke-width="2.7" stroke-linejoin="round" '
                'stroke-linecap="round"/>' % (p, RES_H if col == RES else '#e9d5ff', p, col))

    def _rv(self, b, **kw):
        return (self._r(b, **kw) + '<line x1="-19" y1="15" x2="19" y2="-15" stroke="#0f172a" stroke-width="2" '
                'marker-end="url(#mArr)"/>')

    def _b(self, b, pos='l', cells=1, **kw):
        """pos : the side (in local coordinates) of the long positive plate."""
        s = -1 if pos == 'l' else 1
        o = ('<rect x="-12" y="-19" width="24" height="38" rx="5" fill="url(#gCell)" opacity=".45"/>'
             '<line x1="%d" y1="-17" x2="%d" y2="17" stroke="%s" stroke-width="3.2"/>'
             '<line x1="%d" y1="-9" x2="%d" y2="9" stroke="%s" stroke-width="6"/>'
             % (4 * s, 4 * s, BATP, -4 * s, -4 * s, BATN))
        if kw.get('signs', True):
            o += ('<text x="%d" y="-21" font-size="12" fill="%s" text-anchor="middle" style="%s;font-weight:700">+</text>'
                  % (11 * s, BATP, FONT))
        return o

    def _l(self, b, on=True, **kw):
        o = ''
        if on:
            o += '<circle r="21" fill="url(#gGlow)"/>'
        o += ('<circle r="12" fill="url(#%s)" stroke="#92400e" stroke-width="2"/>'
              '<path d="M-8.5,-8.5 L8.5,8.5 M-8.5,8.5 L8.5,-8.5" stroke="#78350f" stroke-width="1.8"/>'
              % ('gLamp' if on else 'gLampOff'))
        return o

    def _meter(self, letter, grad, ring, ang):
        return ('<circle r="12.5" fill="url(#%s)" stroke="%s" stroke-width="2.4"/>'
                '<g transform="rotate(%.2f)"><text y="5" font-size="%s" text-anchor="middle" fill="%s" '
                'style="%s;font-weight:700">%s</text></g>'
                % (grad, ring, -ang, 14 if len(letter) == 1 else 11, ring, FONT, letter))

    def _a(self, b, ang=0, **kw):
        return self._meter(kw.get('name', 'A'), 'gAm', '#b45309', ang)

    def _v(self, b, ang=0, **kw):
        return self._meter(kw.get('name', 'V'), 'gVm', '#6d28d9', ang)

    def _g(self, b, ang=0, **kw):
        return self._meter(kw.get('name', 'G'), 'gGm', '#15803d', ang)

    def _s(self, b, closed=False, **kw):
        o = ('<circle cx="-13" r="3.6" fill="#fff" stroke="%s" stroke-width="2.2"/>'
             '<circle cx="13" r="3.6" fill="#fff" stroke="%s" stroke-width="2.2"/>' % (WIRE, WIRE))
        if closed:
            o += '<line x1="-10" y1="-1" x2="11" y2="-2.5" stroke="#db2777" stroke-width="2.8" stroke-linecap="round"/>'
        else:
            o += '<line x1="-10" y1="-1.5" x2="10" y2="-14" stroke="#db2777" stroke-width="2.8" stroke-linecap="round"/>'
        return o

    # ------------------------------------------------------------------ output
    def svg(self, maxw=None, cap=None):
        body = ''.join(self.o)
        x0, y0, x1, y1 = self.ext
        if maxw:
            maxw = maxw * (x1 - x0) / self.w
        st = ' style="max-width:%dpx"' % maxw if maxw else ''
        s = ('<figure class="fig"><svg class="svgfig" viewBox="%.1f %.1f %.1f %.1f" xmlns="http://www.w3.org/2000/svg"%s>'
             '%s</svg>' % (x0, y0, x1 - x0, y1 - y0, st, body))
        if cap:
            s += '<figcaption>%s</figcaption>' % cap
        return s + '</figure>'


# ====================================================================== graphs
def graph(W=330, H=230, xl='x', yl='y', xt=(), yt=(), xmax=None, ymax=None, lines=(), grid=True,
          maxw=300, cap=None, pts=(), notes=(), x0=52, y0=None, origin='0'):
    """xt / yt : tick values ; lines : list of (list of (x, y) in data units, colour, label, dash)."""
    f = Circ(W, H)
    y0 = y0 or H - 38
    gw, gh = W - x0 - 72, y0 - 30
    xmax = xmax or max(xt)
    ymax = ymax or max(yt)
    X = lambda v: x0 + gw * v / xmax
    Y = lambda v: y0 - gh * v / ymax
    if grid:
        f.raw('<rect x="%d" y="%d" width="%.1f" height="%.1f" fill="#f0f9ff"/>' % (x0, y0 - gh, gw, gh))
        f.raw('<rect x="%d" y="%d" width="%.1f" height="%.1f" fill="url(#gGrid)"/>' % (x0, y0 - gh, gw, gh))
    for v in xt:
        if v:
            f.wire((X(v), y0), (X(v), y0 + 5), c='#334155', w=1.6)
            f.txt(X(v), y0 + 19, '%g' % v, '#334155', 12, bold=False)
    for v in yt:
        if v:
            f.wire((x0 - 5, Y(v)), (x0, Y(v)), c='#334155', w=1.6)
            f.txt(x0 - 8, Y(v) + 4.5, '%g' % v, '#334155', 12, 'end', bold=False)
    if origin:
        f.txt(x0 - 7, y0 + 15, origin, '#334155', 12, 'end', bold=False)
    f.arrow(x0, y0, x0 + gw + 24, y0, '#0f172a', 2.2)
    f.arrow(x0, y0, x0, y0 - gh - 20, '#0f172a', 2.2)
    f.txt(x0 + gw + 27, y0 + 5, xl, '#1e3a8a', 13.5, 'start')
    f.txt(x0 + 6, y0 - gh - 18, yl, '#1e3a8a', 13.5, 'start')
    for ln in lines:
        p, c = ln[0], ln[1]
        dash = ln[3] if len(ln) > 3 else None
        f.wire(*[(X(a), Y(b)) for a, b in p], c=c, w=3.2, dash=dash)
        if len(ln) > 2 and ln[2]:
            a, b = p[-1]
            f.lab(X(a) + 4, Y(b) - 8, ln[2], c, 13.5, 'start')
    for (a, b, c) in pts:
        f.wire((X(a), y0), (X(a), Y(b)), (x0, Y(b)), c=c, w=1.4, dash='5 4')
        f.raw('<circle cx="%.1f" cy="%.1f" r="4.5" fill="%s" stroke="#fff" stroke-width="1.5"/>' % (X(a), Y(b), c))
    for (a, b, s, c) in notes:
        f.lab(X(a), Y(b), s, c, 13)
    return f.svg(maxw, cap)


def cylinder(f, x, y, L, d, lab=None, grad='gCu', llab=None, alab=None):
    """a wire / rod drawn as a shaded cylinder whose left end is at (x, y) (centre line)."""
    r = d / 2
    f.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#%s)" stroke="#78350f" stroke-width="1.2"/>'
          % (x, y - r, L, d, grad))
    f.raw('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="url(#%s)" stroke="#78350f" stroke-width="1.2"/>'
          % (x + L, y, r * 0.35, r, grad))
    f.raw('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="#fde2c4" stroke="#78350f" stroke-width="1.2"/>'
          % (x, y, r * 0.35, r))
    if lab:
        f.lab(x - r * 0.35 - 10, y + 5, lab, '#0f172a', 14, 'end')
    if llab:
        f.arrow(x, y + r + 14, x + L, y + r + 14, '#7c3aed', 1.8, both=True)
        f.lab(x + L / 2, y + r + 19, llab, '#7c3aed', 13)
    if alab:
        f.lab(x + L + r * 0.35 + 8, y + 5, alab, '#b45309', 13, 'start')

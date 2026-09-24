# -*- coding: utf-8 -*-
"""Small SVG figure helper for physics handouts."""
import math

AR = '#dc2626'   # force  (red)
BL = '#2563eb'   # perpendicular component (blue)
GR = '#16a34a'   # parallel component (green)
PU = '#7c3aed'   # distances (purple)
OR = '#ea580c'   # angles (orange)
DK = '#334155'   # rods / bodies
GY = '#94a3b8'   # guides
NV = '#0f2f5b'   # labels

COLS = {'r': AR, 'b': BL, 'g': GR, 'p': PU, 'o': OR, 'd': DK, 'y': GY, 'n': NV}
KEY = {v: k for k, v in COLS.items()}


def P(cx, cy, r, ang):
    """polar -> screen point (ang in degrees, CCW positive, y flipped)."""
    a = math.radians(ang)
    return (cx + r * math.cos(a), cy - r * math.sin(a))


class Fig:
    n = 0

    def __init__(self, w, h, cap=None, maxw=None):
        Fig.n += 1
        self.i = Fig.n
        self.w, self.h = w, h
        self.cap = cap
        self.maxw = maxw
        self.o = []

    # ---------- primitives ----------
    def raw(self, s):
        self.o.append(s)
        return self

    def line(self, x1, y1, x2, y2, c=DK, w=2, dash=None, cap='round', op=1):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" '
                      f'stroke-width="{w}" stroke-linecap="{cap}" opacity="{op}"{d}/>')
        return self

    def arrow(self, x1, y1, x2, y2, c=AR, w=3, dash=None, both=False):
        k = KEY.get(c, 'r')
        d = f' stroke-dasharray="{dash}"' if dash else ''
        st = f' marker-start="url(#s{self.i}{k})"' if both else ''
        self.o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" '
                      f'stroke-width="{w}" stroke-linecap="butt"{d} marker-end="url(#m{self.i}{k})"{st}/>')
        return self

    def parrow(self, x, y, ang, ln, c=AR, w=3, dash=None):
        """arrow starting at (x,y) pointing along ang for length ln"""
        x2, y2 = P(x, y, ln, ang)
        return self.arrow(x, y, x2, y2, c, w, dash)

    def rod(self, x1, y1, x2, y2, c=DK, w=9):
        self.o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" '
                      f'stroke-width="{w}" stroke-linecap="round"/>')
        return self

    def rect(self, x, y, w, h, fill='#e2e8f0', stroke=DK, sw=2, rx=3):
        self.o.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
                      f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
        return self

    def circle(self, x, y, r, fill='#fff', stroke=DK, sw=2):
        self.o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
        return self

    def poly(self, pts, fill='#e2e8f0', stroke=DK, sw=2):
        s = ' '.join(f'{a:.1f},{b:.1f}' for a, b in pts)
        self.o.append(f'<polygon points="{s}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
        return self

    def txt(self, x, y, s, c=NV, size=15, anchor='middle', it=False, bold=True, fam=None):
        st = ' font-style="italic"' if it else ''
        fw = ' font-weight="700"' if bold else ''
        f = fam or 'Helvetica, Arial, sans-serif'
        self.o.append(f'<text x="{x:.1f}" y="{y:.1f}" fill="{c}" font-size="{size}" text-anchor="{anchor}" '
                      f'font-family="{f}"{st}{fw}>{s}</text>')
        return self

    def tbg(self, x, y, s, c=NV, size=13, anchor='middle', pad=5):
        w = 0.60 * size * len(s) + 2 * pad
        x0 = x - w / 2 if anchor == 'middle' else (x - pad if anchor == 'start' else x - w + pad)
        self.o.append(f'<rect x="{x0:.1f}" y="{y - size * 0.86 - pad * 0.5:.1f}" width="{w:.1f}" '
                      f'height="{size + pad:.1f}" rx="3" fill="#ffffff" opacity="0.92"/>')
        return self.txt(x, y, s, c, size, anchor)

    # ---------- composites ----------
    def pivot(self, x, y, lab='O', labdy=30, c=DK, size=12):
        """hinge / axis of rotation"""
        self.poly([(x, y), (x - size, y + size * 1.6), (x + size, y + size * 1.6)], '#cbd5e1', c, 2)
        self.line(x - size * 1.5, y + size * 1.6, x + size * 1.5, y + size * 1.6, c, 2.5)
        for k in range(-1, 2):
            self.line(x + k * size * 0.9, y + size * 1.6, x + k * size * 0.9 - 6, y + size * 1.6 + 7, c, 1.6)
        self.circle(x, y, 4.2, '#fff', c, 2)
        if lab:
            self.txt(x - 16, y - 8, lab, c, 15, 'middle', it=True)
        return self

    def axis(self, x, y, lab='O', r=6):
        """simple point axis (no ground)"""
        self.circle(x, y, r, '#fff', DK, 2.4)
        self.circle(x, y, 2, DK, DK, 1)
        if lab:
            self.txt(x, y - 13, lab, NV, 15, 'middle', it=True)
        return self

    def arc(self, cx, cy, r, a1, a2, c=OR, w=2.2, dash=None, arrowhead=False):
        x1, y1 = P(cx, cy, r, a1)
        x2, y2 = P(cx, cy, r, a2)
        large = 1 if abs(a2 - a1) > 180 else 0
        sweep = 0 if a2 > a1 else 1
        d = f' stroke-dasharray="{dash}"' if dash else ''
        k = KEY.get(c, 'o')
        mk = f' marker-end="url(#m{self.i}{k})"' if arrowhead else ''
        self.o.append(f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 {large} {sweep} {x2:.1f},{y2:.1f}" fill="none" '
                      f'stroke="{c}" stroke-width="{w}"{d}{mk}/>')
        return self

    def angle(self, cx, cy, r, a1, a2, lab=None, c=OR, lr=None, size=14):
        self.arc(cx, cy, r, a1, a2, c, 2.2)
        if lab:
            mx, my = P(cx, cy, (lr or r + 16), (a1 + a2) / 2.0)
            self.txt(mx, my + 5, lab, c, size)
        return self

    def rotmark(self, cx, cy, r, cw=True, c=GR, lab=None, w=3):
        """curved rotation arrow. cw=True -> clockwise"""
        if cw:
            self.arc(cx, cy, r, 130, -40, c, w, arrowhead=True)
        else:
            self.arc(cx, cy, r, 50, 220, c, w, arrowhead=True)
        if lab:
            self.txt(cx, cy + 5, lab, c, 15)
        return self

    def rang(self, px, py, a1, a2, s=11, c=DK):
        """right-angle square at point p between directions a1 and a2"""
        p1 = P(px, py, s, a1)
        p2 = P(px, py, s, a2)
        p3 = (p1[0] + p2[0] - px, p1[1] + p2[1] - py)
        self.line(p1[0], p1[1], p3[0], p3[1], c, 1.6)
        self.line(p2[0], p2[1], p3[0], p3[1], c, 1.6)
        return self

    def guide(self, x1, y1, x2, y2, c=GY, w=1.6, dash='6 5'):
        return self.line(x1, y1, x2, y2, c, w, dash)

    def dim(self, x1, y1, x2, y2, lab, c=PU, off=0, size=14, dy=-8, dx=0):
        """double-headed dimension line with label"""
        ang = math.degrees(math.atan2(-(y2 - y1), x2 - x1))
        nx, ny = P(0, 0, off, ang + 90)
        X1, Y1, X2, Y2 = x1 + nx, y1 + ny, x2 + nx, y2 + ny
        k = KEY.get(c, 'p')
        self.o.append(f'<line x1="{X1:.1f}" y1="{Y1:.1f}" x2="{X2:.1f}" y2="{Y2:.1f}" stroke="{c}" '
                      f'stroke-width="1.8" marker-end="url(#m{self.i}{k})" marker-start="url(#s{self.i}{k})"/>')
        self.txt((X1 + X2) / 2 + dx, (Y1 + Y2) / 2 + dy, lab, c, size)
        return self

    # ---------- output ----------
    def render(self):
        defs = []
        for k, c in COLS.items():
            defs.append(f'<marker id="m{self.i}{k}" viewBox="0 0 10 10" refX="9.2" refY="5" markerWidth="6.5" '
                        f'markerHeight="6.5" orient="auto"><path d="M0,0.6 L10,5 L0,9.4 z" fill="{c}"/></marker>')
            defs.append(f'<marker id="s{self.i}{k}" viewBox="0 0 10 10" refX="9.2" refY="5" markerWidth="6.5" '
                        f'markerHeight="6.5" orient="auto-start-reverse"><path d="M0,0.6 L10,5 L0,9.4 z" fill="{c}"/></marker>')
        style = f' style="max-width:{self.maxw}px"' if self.maxw else ''
        s = (f'<svg viewBox="0 0 {self.w} {self.h}" xmlns="http://www.w3.org/2000/svg" class="svgfig"{style}>'
             f'<defs>{"".join(defs)}</defs>{"".join(self.o)}</svg>')
        if self.cap:
            return f'<figure class="fig">{s}<figcaption>{self.cap}</figcaption></figure>'
        return f'<figure class="fig">{s}</figure>'

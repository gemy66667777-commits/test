# -*- coding: utf-8 -*-
"""Shared document scaffolding for the lesson worksheets (Mr. Gemy series)."""
import base64
from css_apple import CSS

_WM = ('<svg xmlns="http://www.w3.org/2000/svg" width="340" height="230">'
       '<text x="170" y="128" font-family="Helvetica,Arial,sans-serif" font-size="28" font-weight="700" '
       'fill="#0B1220" fill-opacity="0.045" text-anchor="middle" '
       'transform="rotate(-27 170 128)">Mr. Gemy</text></svg>')
WM64 = base64.b64encode(_WM.encode()).decode()


class Doc:
    def __init__(self, chip, title_html, subtitle, meta, doc_title=None):
        self.h = []
        self.n = 0
        self.a('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>' +
               (doc_title or chip) + '</title><style>' + CSS +
               'body{background-image:url("data:image/svg+xml;base64,' + WM64 + '");background-repeat:repeat;}'
               '</style></head><body>')
        self.a('<div class="hero"><span class="chip">' + chip + '</span><h1>' + title_html + '</h1>'
               '<div class="sub">' + subtitle + '</div><div class="meta">' +
               ''.join('<span>' + m + '</span>' for m in meta) +
               '</div><div class="sig"><b>Mr. Gemy</b><i>Physics</i></div></div>')

    def a(self, s):
        self.h.append(s)

    def kit(self, title, items):
        self.a('<div class="kit"><h4>' + title + '</h4><div class="grid">' +
               ''.join('<div class="f">' + f + '<small>' + s + '</small></div>' for f, s in items) +
               '</div></div>')

    def hint(self, html):
        self.a('<div class="hint">' + html + '</div>')

    def sec(self, letter, kicker, title):
        self.a('<div class="sec"><div class="no">' + letter + '</div><div class="tt"><small>' + kicker +
               '</small>' + title + '</div><div class="rule"></div></div>')

    def grp(self, t):
        self.a('<h3 class="grp">' + t + '</h3>')

    def page(self):
        self.a('<div class="pb"></div>')

    def q(self, text, tag=None, fig=None, ch=None, parts=None):
        self.n += 1
        self.a('<div class="card"><div class="qh"><div class="qno">' + str(self.n) + '</div>'
               '<div class="qtx">' + text + '</div>' +
               ('<span class="tag">' + tag + '</span>' if tag else '') + '</div>')
        if parts:
            for p in parts:
                self.a('<div class="part">' + p + '</div>')
        if fig:
            self.a(fig)
        if ch:
            self.a('<div class="ch">')
            for le, c in zip('ABCD', ch):
                self.a('<div><i>' + le + '</i>' + c + '</div>')
            self.a('</div>')
        self.a('</div>')

    def row(self, *figs):
        return '<div class="figrow">' + ''.join(figs) + '</div>'

    def sol(self, n, title, steps=None, res=None, why=None, extra=None):
        self.a('<div class="sol"><div class="sh"><div class="sn">' + str(n) + '</div>'
               '<div class="st">' + title + '</div></div>')
        if steps:
            self.a('<pre>' + steps + '</pre>')
        if why:
            self.a('<div class="why">' + why + '</div>')
        if extra:
            self.a(extra)
        if res:
            self.a('<div class="res">' + res + '</div>')
        self.a('</div>')

    def table(self, headers, rows):
        self.a('<table class="vt"><tr>' + ''.join('<th>' + x + '</th>' for x in headers) + '</tr>' +
               ''.join('<tr>' + ''.join('<td>' + c + '</td>' for c in r) + '</tr>' for r in rows) + '</table>')

    def foot(self, left, right):
        self.a('<div class="foot"><span>' + left + '</span><span>' + right + '</span></div>')

    def save(self, path):
        self.a('</body></html>')
        open(path, 'w', encoding='utf-8').write(''.join(self.h))
        return path

# -*- coding: utf-8 -*-
"""Assemble Z BANK style pages : question blocks flowed into A4 pages by a small script."""
import zb_frame as FR

import re

ROMAN = ['I', 'II', 'III', 'IV', 'V']
_TOK = re.compile(r'(<[^>]+>|&[#A-Za-z0-9]+;)')


def dg(html):
    """wrap every run of digits (outside tags and entities) so the digits can be weighted like the letters."""
    return ''.join(t if (t.startswith('<') or t.startswith('&')) else re.sub(r'([0-9]+)', r'<span class="dg">\1</span>', t)
                   for t in _TOK.split(html))


def choices(ch, cols=None, narrow=False):
    if cols is None:
        longest = max(len(c) for c in ch)
        if narrow:
            cols = 2 if longest <= 24 else 1
        else:
            cols = 4 if longest <= 16 else (2 if longest <= 44 else 1)
    cls = {4: '', 2: ' two', 1: ' one'}[cols]
    return ('<div class="ch%s">' % cls +
            ''.join('<span class="qtext"><b>%s)</b>%s</span>' % (l, dg(c)) for l, c in zip('abcd', ch)) +
            '</div>')


def part(k, p, narrow=False):
    """p : dict(t=text, ch=[choices] or None, sp='s'|'m'|''|'l')"""
    sp = p.get('sp', 's' if p.get('ch') else '')
    rn = '<span class="b">%s</span><span class="f">%s</span>' % (ROMAN[k], ROMAN[k])
    return ('<div class="part"><span class="rn">%s</span><div class="qtext">%s</div>%s</div>'
            '<div class="space %s"></div>' % (rn, dg(p['t']), choices(p['ch'], p.get('cols'), narrow)
                                              if p.get('ch') else '', sp))


def question(n, stem, parts, fig=None, figpos='below'):
    head = ('<div class="stem">' + FR.bubble(n) + '<div class="qtext">' + dg(stem) + '</div>' +
            FR.stem_doodle() + '</div>')
    if fig and figpos == 'right':
        body = ('<div class="withfig"><div class="parts">' + ''.join(part(k, p, True) for k, p in enumerate(parts)) +
                '</div><div class="figcol">' + fig + '</div></div>')
        return ['<div class="q">' + head + body + '</div>']
    first = head + ('<div class="figc">' + fig + '</div>' if fig else '') + part(0, parts[0])
    blocks = ['<div class="q">' + first + '</div>']
    for k, p in enumerate(parts[1:], 1):
        blocks.append('<div class="q cont">' + part(k, p) + '</div>')
    return blocks


SCRIPT = r"""
<script>
function build(){
  const flow = document.getElementById('flow');
  const blocks = Array.from(flow.children);
  const H = document.getElementById('tpl-h').innerHTML;
  const F = document.getElementById('tpl-f').innerHTML;
  const pages = [];
  function newPage(){
    const p = document.createElement('div'); p.className = 'page';
    p.innerHTML = H + '<div class="body"></div>' + F.replace('{{N}}', String(START + pages.length));
    document.body.appendChild(p); pages.push(p); return p.querySelector('.body');
  }
  let body = newPage();
  for (const b of blocks){
    if (b.classList.contains('newpage') && body.children.length) body = newPage();
    body.appendChild(b);
    if (body.scrollHeight > body.clientHeight + 1 && body.children.length > 1){
      body.removeChild(b); body = newPage(); body.appendChild(b);
    }
  }
  flow.remove();
  document.body.setAttribute('data-pages', pages.length);
}
document.fonts.ready.then(() => setTimeout(build, 50));
</script>
"""


def document(blocks, start=1, title='Z BANK'):
    return ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>' + title + '</title><style>' +
            FR.fontfaces() + FR.css() + '</style></head><body>'
            '<template id="tpl-h">' + FR.header_svg() + '</template>'
            '<template id="tpl-f">' + FR.footer_svg() + '</template>'
            '<div id="flow">' + ''.join(blocks) + '</div>' +
            SCRIPT.replace('START', str(start)) + '</body></html>')

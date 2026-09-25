# -*- coding: utf-8 -*-
"""Assemble Z BANK style pages : question blocks flowed into A4 pages by a small script."""
import zb_frame as FR
import zb_art as ART

import re

ROMAN = ['I', 'II', 'III', 'IV', 'V']
_TOK = re.compile(r'(<[^>]+>|&[#A-Za-z0-9]+;)')


SIGN = ('<span class="sg"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400000 1080" '
        'preserveAspectRatio="xMinYMin slice"><path fill="#111" stroke="#111" stroke-width="26" d="M95,702 '
        'c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54 '
        'c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10s173,378,173,378 '
        'c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429c69,-144,104.5,-217.7,106.5,-221 '
        'l0 -0c5.3,-9.3,12,-14,20,-14H400000v40H845.2724s-225.272,467,-225.272,467s-235,486,-235,486 '
        'c-2.7,4.7,-9,7,-19,7c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47zM834 80h400000v40h-400000z"/>'
        '</svg></span>')


def roots(html):
    """write every square root as a proper radical : the sign plus a bar over the whole radicand.
    √( ... ) takes everything up to the matching bracket, √3 / √2 / √k take the following token."""
    out, i = [], 0
    while i < len(html):
        if html[i] != '\u221a':
            out.append(html[i]); i += 1; continue
        j = i + 1
        if j < len(html) and html[j] == '(':
            depth, k = 0, j
            while k < len(html):
                if html[k] == '(':
                    depth += 1
                elif html[k] == ')':
                    depth -= 1
                    if depth == 0:
                        break
                k += 1
            inner, i = html[j + 1:k], k + 1
        else:
            m = re.match(r'[0-9A-Za-z.]+', html[j:])
            inner = m.group(0) if m else ''
            i = j + len(inner)
        out.append('<span class="rt">' + SIGN + roots(inner) + '</span>')
    return ''.join(out)


def dg(html):
    """wrap every run of digits (outside tags and entities) so the digits can be weighted like the letters."""
    html = roots(html)
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
    """the stem (with a figure drawn below it) is one block and every part is a block of its own, so a page
    can break between them ; a stem with nothing under it is kept with the block that follows."""
    head = ('<div class="stem">' + FR.bubble(n) + '<div class="qtext">' + dg(stem) + '</div>' +
            FR.stem_doodle() + '</div>')
    if fig and figpos == 'right':
        body = ('<div class="withfig"><div class="parts">' + ''.join(part(k, p, True) for k, p in enumerate(parts)) +
                '</div><div class="figcol">' + fig + '</div></div>')
        return ['<div class="q keepnext">' + head + '</div>', '<div class="q cont">' + body + '</div>']
    if fig:
        blocks = ['<div class="q">' + head + '<div class="figc">' + fig + '</div></div>']
    else:
        blocks = ['<div class="q keepnext">' + head + '</div>']
    for k, p in enumerate(parts):
        blocks.append('<div class="q cont">' + part(k, p) + '</div>')
    return blocks


SCRIPT = r"""
<script>
function build(){
  const flow = document.getElementById('flow');
  const queue = Array.from(flow.children);
  const NT = NTHEMES;
  const pages = [];
  function newPage(){
    const t = Math.floor(pages.length / 2) % NT;   // a new header and footer every two pages
    const H = document.getElementById('tpl-h-' + t).innerHTML;
    const F = document.getElementById('tpl-f-' + t).innerHTML;
    const p = document.createElement('div'); p.className = 'page';
    p.innerHTML = H + '<div class="body"></div>' + F.split('{{N}}').join(String(START + pages.length));
    document.body.appendChild(p); pages.push(p); return p.querySelector('.body');
  }
  // the pieces of one answer that share a page are drawn as a single box
  function join(b){
    const prev = body.lastElementChild;
    if (!prev || !b.dataset.q || prev.dataset.q !== b.dataset.q) return null;
    prev.querySelector('.abox').classList.add('jb'); b.querySelector('.abox').classList.add('jt');
    return prev;
  }
  function unjoin(prev, b){
    if (!prev) return;
    prev.querySelector('.abox').classList.remove('jb'); b.querySelector('.abox').classList.remove('jt');
  }
  let body = newPage();
  const over = () => body.scrollHeight > body.clientHeight + 1;
  while (queue.length){
    const b = queue.shift();
    if (b.classList.contains('newpage') && body.children.length) body = newPage();
    const jp = join(b);
    body.appendChild(b);
    if (!over() || body.children.length === 1) continue;
    // before leaving a gap, try the block with its figure drawn a little smaller
    const figs = Array.from(b.querySelectorAll('svg.fg'));
    const w0 = figs.map(f => parseFloat(f.style.width));
    let fitted = false;
    for (const s of [0.92, 0.85, 0.78, 0.72]){
      if (!figs.length) break;
      figs.forEach((f, i) => f.style.width = (w0[i] * s).toFixed(1) + 'mm');
      if (!over()){ fitted = true; break; }
    }
    if (fitted) continue;
    figs.forEach((f, i) => f.style.width = w0[i] + 'mm');
    body.removeChild(b); unjoin(jp, b);
    const wf = b.querySelector('.withfig');
    if (wf){
      // a figure beside the parts that does not fit : put the figure under the stem and let the parts flow
      const nb = [], fb = document.createElement('div');
      fb.className = 'q cont'; fb.innerHTML = '<div class="figc">' + wf.querySelector('.figcol').innerHTML + '</div>';
      nb.push(fb);
      let cur = null;
      for (const k of Array.from(wf.querySelector('.parts').children)){
        if (k.classList.contains('part')){ cur = document.createElement('div'); cur.className = 'q cont'; nb.push(cur); }
        (cur || fb).appendChild(k);
      }
      queue.unshift(...nb);
      continue;
    }
    const prev = body.lastElementChild, carry = [];
    if (prev && prev.classList.contains('keepnext') && body.children.length > 1){ body.removeChild(prev); carry.push(prev); }
    body = newPage(); carry.forEach(c => body.appendChild(c)); body.appendChild(b);
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
            + ''.join('<template id="tpl-h-%d">%s</template><template id="tpl-f-%d">%s</template>'
                      % (t, ART.header_svg(t), t, ART.footer_svg(t)) for t in range(len(ART.THEMES))) +
            '<div id="flow">' + ''.join(blocks) + '</div>' +
            SCRIPT.replace('START', str(start)).replace('NTHEMES', str(len(ART.THEMES))) + '</body></html>')

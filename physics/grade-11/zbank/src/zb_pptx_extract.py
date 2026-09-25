# -*- coding: utf-8 -*-
"""Split every page of the Z BANK PDF into
   (1) a background picture with all the art, boxes, bubbles and figures, and
   (2) the question / answer text as positioned lines that become editable text boxes
       (Vintage Vignette for the words, Comfortaa for the digits and the symbols)."""
import json, os, sys
import pymupdf

SRC, OUT = sys.argv[1], sys.argv[2]
DPI = int(sys.argv[3]) if len(sys.argv) > 3 else 200
os.makedirs(os.path.join(OUT, 'bg'), exist_ok=True)

# the ascent PowerPoint uses to place the first baseline under the top of a text box
ASC = {'Vintage Vignette': 0.874, 'Comfortaa': 1.285, 'Segoe UI Symbol': 1.08}


def face(font):
    if font.startswith('VintageVignette'):
        return 'Vintage Vignette'
    if font.startswith('Comfortaa'):
        return 'Comfortaa'
    return None


DIGITS = set('0123456789. ')


def keep(span):
    """the words, plus the digits : a stroked digit can come out as a Type3 copy, and its shadow
    as a pure black copy, so every copy is collected here and the duplicates are merged below."""
    if face(span['font']):
        return face(span['font'])
    t = ''.join(c['c'] for c in span['chars'])
    if span['font'].startswith('Type3') and 11 <= span['size'] <= 12.2 and t.strip():
        if set(t) <= DIGITS:
            return 'Comfortaa'
        if set(t) <= set('\u221d\u2713 '):     # ∝ and ✓ come from a fallback symbol font
            return 'Segoe UI Symbol'
    return None


doc = pymupdf.open(SRC)
pages = []
for pno in range(doc.page_count):
    page = doc[pno]
    chars = []
    for b in page.get_text('rawdict')['blocks']:
        for line in b.get('lines', []):
            if abs(line['dir'][1]) > 0.01:
                continue
            for s in line['spans']:
                if not keep(s):
                    continue
                col = '%06X' % s['color']
                for c in s['chars']:
                    ch = {'i': len(chars), 'c': c['c'], 'x0': c['bbox'][0], 'x1': c['bbox'][2], 'y0': c['bbox'][1],
                          'y1': c['bbox'][3], 'ox': c['origin'][0], 'by': c['origin'][1], 'f': keep(s),
                          's': round(s['size'], 2), 'col': col}
                    twin = next((d for d in chars if d['c'] == ch['c'] and abs(d['ox'] - ch['ox']) < 0.8
                                 and abs(d['by'] - ch['by']) < 0.8), None)
                    if twin is None:
                        chars.append(ch)
                    elif twin['col'] == '000000' and col != '000000':
                        twin.update(ch)            # the shadow came first : take the real colour
    for c in chars:
        if c['col'] == '000000':
            c['col'] = '111111'
    # visual lines : main-size characters grouped by baseline, small (sub / sup) ones attached to the nearest line
    big = sorted([c for c in chars if c['s'] >= 11], key=lambda c: (c['by'], c['x0']))
    lines = []
    for c in big:
        for L in lines:
            if abs(L['by'] - c['by']) < 1.5:
                L['cs'].append(c); break
        else:
            lines.append({'by': c['by'], 'cs': [c]})
    for c in chars:
        if c['s'] < 11:
            L = min(lines, key=lambda L: abs(L['by'] - c['by']))
            if abs(L['by'] - c['by']) < 9:
                L['cs'].append(c)
    boxes, redact = [], []
    for L in lines:
        cs = sorted(L['cs'], key=lambda c: (round(c['ox'], 1), c['i']))
        # split a line wherever there is a real gap (the four choices of an MCQ, for example)
        segs, cur = [], []
        for c in cs:
            if cur and c['x0'] - cur[-1]['x1'] > 14:
                segs.append(cur); cur = []
            cur.append(c)
        segs.append(cur)
        for seg in segs:
            if not ''.join(c['c'] for c in seg).strip():
                continue
            size = max(c['s'] for c in seg)
            runs = []
            prev = None
            for c in seg:
                t = c['c']
                if c['s'] < 0.9 * size and c['by'] - L['by'] < -0.15 * size:
                    va = 'sup'
                elif c['s'] < 0.9 * size and c['by'] - L['by'] > 0.1 * size:
                    va = 'sub'
                else:
                    va = ''
                if prev is not None and t != ' ' and prev['c'] != ' ' and c['x0'] - prev['x1'] > 0.2 * size:
                    t = ' ' + t              # a word break that pymupdf dropped between two runs
                key = (c['f'], c['col'], va)
                if runs and runs[-1]['k'] == key:
                    runs[-1]['t'] += t
                else:
                    runs.append({'k': key, 't': t})
                prev = c
                redact.append(pymupdf.Rect(c['x0'] + 0.2, c['y0'] + 0.1 * c['s'], c['x1'] - 0.2, c['y1'] - 0.1 * c['s']))
            out = []
            for r in runs:
                f, col, va = r['k']
                o = {'t': r['t'].replace('\xa0', ' '), 'f': f, 's': size, 'c': col, 'b': f == 'Comfortaa'}
                if va:
                    o[va] = True
                out.append(o)
            asc = max(ASC[r['f']] for r in out)
            x0 = min(c['x0'] for c in seg)
            x1 = max(c['x1'] for c in seg)
            boxes.append({'x': round(x0, 2), 'y': round(L['by'] - asc * size, 2),
                          'w': round((x1 - x0) * 1.08 + 6, 2), 'h': round(size * 2.0, 2), 'runs': out})
    for r in redact:
        page.add_redact_annot(r, fill=False, cross_out=False)
    page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE,
                          graphics=pymupdf.PDF_REDACT_LINE_ART_NONE,
                          text=pymupdf.PDF_REDACT_TEXT_REMOVE)
    name = 'bg/p%03d.png' % (pno + 1)
    page.get_pixmap(dpi=DPI).save(os.path.join(OUT, name))
    pages.append({'n': pno + 1, 'bg': name, 'w': page.rect.width, 'h': page.rect.height, 'boxes': boxes})

json.dump(pages, open(os.path.join(OUT, 'pages.json'), 'w', encoding='utf-8'), ensure_ascii=False)
print('pages', len(pages), 'text boxes', sum(len(p['boxes']) for p in pages))

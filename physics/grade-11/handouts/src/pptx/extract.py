# -*- coding: utf-8 -*-
"""Split every page of the English book into
   (1) a background picture with all the drawing, colour and figures, and
   (2) the page text as positioned, styled lines that become editable text boxes."""
import json, os, re, statistics, sys
import pymupdf

SRC = sys.argv[1]
OUT = sys.argv[2]
DPI = int(sys.argv[3]) if len(sys.argv) > 3 else 150
PAGES = None
if len(sys.argv) > 4:                      # optional page list for quick tests : "1,5,90"
    PAGES = [int(v) - 1 for v in sys.argv[4].split(',')]
os.makedirs(os.path.join(OUT, 'bg'), exist_ok=True)

FLAGS = (pymupdf.TEXT_PRESERVE_WHITESPACE | pymupdf.TEXT_PRESERVE_LIGATURES |
         pymupdf.TEXT_MEDIABOX_CLIP)


def face(font):
    f = font.lower()
    if 'mono' in f:
        return 'Courier New', 0.833
    return 'Arial', 0.905


def spacing(span):
    """the letter-spacing Chromium applied, recovered from the measured width."""
    t = span['text']
    if 'mono' in span['font'].lower() or not t:
        return 0.0
    try:
        t.encode('latin-1')
    except UnicodeEncodeError:
        return 0.0
    bold = span['flags'] & 16 or 'Bold' in span['font']
    nat = pymupdf.get_text_length(t, fontname='hebo' if bold else 'helv', fontsize=span['size'])
    real = span['bbox'][2] - span['bbox'][0]
    s = (real - nat) / len(t)
    return round(s, 2) if abs(s) > 0.06 else 0.0


CAPS = re.compile(r"[A-Z0-9 ·&.,:'’()\-–—/!?#]+")   # letter-spaced labels are all capitals


def span_text(span):
    """rebuild the text from the glyphs.  For letter-spaced headings pymupdf puts a
    space after every glyph and loses the real word breaks ; recover them from the gaps."""
    chars = span['chars']
    t = ''.join(c['c'] for c in chars)
    tok = t.strip().split(' ')
    if not CAPS.fullmatch(t) or len(tok) < 4 or sum(len(k) == 1 for k in tok) < 0.7 * len(tok):
        return t
    g = [c for c in chars if c['c'] != ' ']
    gaps = [g[i + 1]['bbox'][0] - g[i]['bbox'][2] for i in range(len(g) - 1)]
    ls = sorted(gaps)[len(gaps) // 4]          # the letter-spacing inside words
    out = g[0]['c']
    for i, gap in enumerate(gaps):
        if gap > ls + 0.16 * span['size']:
            out += ' '
        out += g[i + 1]['c']
    return out


def segments(line):
    """split a pymupdf line wherever two runs are separated by a real gap."""
    segs, cur, prev = [], [], None
    for s in line['spans']:
        if prev is not None:
            gap = s['bbox'][0] - prev['bbox'][2]
            if gap > 0.5 * max(s['size'], prev['size']):
                segs.append(cur)
                cur = []
        cur.append(s)
        prev = s
    if cur:
        segs.append(cur)
    return segs


doc = pymupdf.open(SRC)
pages = []
for pno in (PAGES if PAGES is not None else range(doc.page_count)):
    page = doc[pno]
    boxes, redact = [], []
    for b in page.get_text('rawdict', flags=FLAGS)['blocks']:
        for line in b.get('lines', []):
            for sp in line['spans']:
                sp['text'] = span_text(sp)
            if abs(line['dir'][1]) > 0.01 or line['dir'][0] < 0:
                continue                               # rotated label : keep it in the picture
            if any(s['font'].startswith('Type3') for s in line['spans']):
                continue                               # symbol glyphs : keep them in the picture
            for seg in segments(line):
                if not ''.join(s['text'] for s in seg).strip():
                    continue
                main = max(seg, key=lambda s: (s['size'], len(s['text'])))
                size = main['size']
                base = main['origin'][1]
                fam, asc = face(main['font'])
                runs = []
                for s in seg:
                    if not s['text']:
                        continue
                    r = {'t': s['text'].replace('\xa0', ' '),
                         'f': face(s['font'])[0],
                         's': round(s['size'], 2),
                         'c': '%06X' % s['color'],
                         'b': bool(s['flags'] & 16 or 'Bold' in s['font']),
                         'i': bool(s['flags'] & 2 or 'Italic' in s['font'])}
                    dy = s['origin'][1] - base
                    if s['size'] < 0.9 * size and dy < -0.18 * size:
                        r['sup'] = True
                        r['s'] = round(size, 2)
                    elif s['size'] < 0.9 * size and dy > 0.12 * size:
                        r['sub'] = True
                        r['s'] = round(size, 2)
                    cs = spacing(s)
                    if cs:
                        r['cs'] = cs
                    runs.append(r)
                    x0, y0, x1, y1 = s['bbox']
                    ins = 0.12 * s['size']
                    redact.append(pymupdf.Rect(x0 + 0.3, y0 + ins, x1 - 0.3, y1 - ins))
                x0 = min(s['bbox'][0] for s in seg)
                x1 = max(s['bbox'][2] for s in seg)
                boxes.append({'x': round(x0, 2), 'y': round(base - asc * size, 2),
                              'w': round((x1 - x0) * 1.03 + 3, 2), 'h': round(size * 1.22, 2),
                              'runs': runs})
    for r in redact:
        page.add_redact_annot(r, fill=False, cross_out=False)
    page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE,
                          graphics=pymupdf.PDF_REDACT_LINE_ART_NONE,
                          text=pymupdf.PDF_REDACT_TEXT_REMOVE)
    name = 'bg/p%03d.jpg' % (pno + 1)
    pix = page.get_pixmap(dpi=DPI)
    pix.save(os.path.join(OUT, name), jpg_quality=86)
    pages.append({'n': pno + 1, 'bg': name, 'w': page.rect.width, 'h': page.rect.height,
                  'boxes': boxes})
    if (pno + 1) % 25 == 0:
        print('page', pno + 1, flush=True)

json.dump(pages, open(os.path.join(OUT, 'pages.json'), 'w', encoding='utf-8'), ensure_ascii=False)
print('pages', len(pages), 'text boxes', sum(len(p['boxes']) for p in pages))

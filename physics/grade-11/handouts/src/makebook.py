# -*- coding: utf-8 -*-
"""Assemble every lesson handout into one book : all the questions first,
then the complete step-by-step answer key at the back."""
import os, re, subprocess, sys
import pymupdf
import bookfront
from bookmeta import LESSONS, UNITS

SRC = '/home/user/test/physics/grade-11/handouts'
OUT = os.path.join(SRC, 'Physics-Grade-11-Assessments-Book-Mr-Gemy.pdf')
CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
HERE = os.path.dirname(os.path.abspath(__file__))

NQ, NFIG = 483, 167


def topdf(html, name):
    hp = os.path.join(HERE, name + '.html')
    pp = os.path.join(HERE, name + '.pdf')
    open(hp, 'w', encoding='utf-8').write(html)
    subprocess.run([CHROME, '--headless', '--no-sandbox', '--no-pdf-header-footer',
                    '--print-to-pdf=' + pp, 'file://' + hp],
                   capture_output=True)
    return pymupdf.open(pp)


def split(stem):
    """→ (doc, index of the first answer-key page)"""
    d = pymupdf.open(os.path.join(SRC, stem + '.pdf'))
    k = next(i for i, p in enumerate(d) if 'ANSWER KEY' in p.get_text().upper())
    return d, k


def build():
    parts = [split(s) for s, *_ in LESSONS]
    qlen = [k for _, k in parts]
    alen = [d.page_count - k for d, k in parts]

    nfront = 2                     # cover + contents, re-checked below
    for _ in range(4):
        rows, p = [], nfront + 2   # 1-based : front matter, then the Unit One divider
        qstart = {}
        cur = None
        for i, (stem, unit, lab, ten, tar) in enumerate(LESSONS):
            if unit != cur:
                cur = unit
                if i:
                    p += 1         # the Unit Two divider
            qstart[stem] = p
            p += qlen[i]
        p += 1                     # the Answer Key divider
        astart = {}
        for i, (stem, *_r) in enumerate(LESSONS):
            astart[stem] = p
            p += alen[i]
        rows = [(s, u, lab, te, ta, qstart[s], astart[s])
                for s, u, lab, te, ta in LESSONS]
        front = topdf(bookfront.front_html(rows, NQ, NFIG, p - 1, nfront), 'front')
        if front.page_count == nfront:
            break
        nfront = front.page_count

    div = topdf(bookfront.dividers_html(), 'divs')
    book = pymupdf.open()
    book.insert_pdf(front)
    cur = None
    for i, (stem, unit, *_r) in enumerate(LESSONS):
        if unit != cur:
            cur = unit
            book.insert_pdf(div, from_page=unit - 1, to_page=unit - 1)
        d, k = parts[i]
        book.insert_pdf(d, from_page=0, to_page=k - 1)
    book.insert_pdf(div, from_page=2, to_page=2)
    for i, (stem, *_r) in enumerate(LESSONS):
        d, k = parts[i]
        book.insert_pdf(d, from_page=k, to_page=d.page_count - 1)
    return book, rows, nfront


def stamp(book, rows, nfront):
    """a quiet running footer : lesson on the left, page number on the right."""
    plain = re.compile(r'&[a-z]+;|&#\d+;')
    labels = {}
    for stem, unit, lab, ten, tar, qp, ap in rows:
        L = plain.sub(lambda m: {'&ndash;': '–', '&amp;': '&', '&rsquo;': '’'}.get(m.group(0), ''), lab)
        T = plain.sub(lambda m: {'&rsquo;': '’', '&amp;': '&'}.get(m.group(0), ''), ten)
        for j in range(qp, qp + rows_q[stem]):
            labels[j] = 'Lesson ' + L + '  ·  ' + T
        for j in range(ap, ap + rows_a[stem]):
            labels[j] = 'Answer key  ·  Lesson ' + L
    grey = (0.42, 0.48, 0.56)
    for i, page in enumerate(book):
        n = i + 1
        if n <= nfront:
            continue
        r = page.rect
        lab = labels.get(n)
        if not lab:                      # the unit / answer-key dividers stay clean
            continue
        page.insert_text((31, r.height - 13), lab, fontname='helv',
                         fontsize=6.8, color=grey)
        page.insert_text((r.width - 31 - 22, r.height - 13), '%d' % n, fontname='helv',
                         fontsize=6.8, color=grey)


if __name__ == '__main__':
    if '--en' in sys.argv:              # English-only edition, no Arabic anywhere
        bookfront.EN_ONLY = True
        OUT = sys.argv[sys.argv.index('--en') + 1]
    book, rows, nfront = build()
    rows_q = {}
    rows_a = {}
    for i, (stem, *_r) in enumerate(LESSONS):
        d = pymupdf.open(os.path.join(SRC, stem + '.pdf'))
        k = next(j for j, p in enumerate(d) if 'ANSWER KEY' in p.get_text().upper())
        rows_q[stem], rows_a[stem] = k, d.page_count - k
    stamp(book, rows, nfront)
    book.set_metadata({'title': 'Physics — Grade 11 Assessments Book (Mr. Gemy)',
                       'author': 'Mr. Gemy', 'subject': 'Egyptian Baccalaureate Physics'})
    try:
        book.subset_fonts()
    except Exception:
        pass
    book.save(OUT, deflate=True, deflate_fonts=True, deflate_images=True,
              garbage=4, clean=True)
    print('written', OUT, book.page_count, 'pages ; front matter', nfront)

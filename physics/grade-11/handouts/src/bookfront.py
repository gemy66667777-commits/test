# -*- coding: utf-8 -*-
"""Cover + contents + section dividers for the collected book."""
from css_apple import CSS
from docbase import WM64
from bookmeta import LESSONS, UNITS

EN_ONLY = False     # True : drop every Arabic line (for the PowerPoint edition)

EXTRA = """
@page { size:A4; margin:0; }
body { background-image:url("data:image/svg+xml;base64,%s"); background-repeat:repeat; }
.sheet { width:210mm; height:297mm; padding:16mm 15mm; position:relative;
         page-break-after:always; overflow:hidden; }
.sheet:last-child { page-break-after:auto; }
.cover { background:linear-gradient(150deg,#050A14 0%%,#0C2340 42%%,#17548C 74%%,#1E7BC0 100%%);
         color:#fff; padding:0; }
.cover .inner { position:relative; height:100%%; padding:30mm 20mm; z-index:2; display:flex;
                flex-direction:column; }
.cover:after { content:""; position:absolute; right:-120px; top:-150px; width:460px; height:460px;
        border-radius:50%%; background:radial-gradient(circle,rgba(255,255,255,.17),rgba(255,255,255,0) 70%%); }
.cover:before { content:""; position:absolute; left:-140px; bottom:-170px; width:420px; height:420px;
        border-radius:50%%; background:radial-gradient(circle,rgba(30,123,192,.55),rgba(255,255,255,0) 70%%); }
.cover .chip { align-self:flex-start; font-size:9.5pt; letter-spacing:.18em; text-transform:uppercase;
        background:rgba(255,255,255,.13); border:1px solid rgba(255,255,255,.36); border-radius:999px;
        padding:5px 16px; }
.cover h1 { margin:16mm 0 0; font-size:40pt; font-weight:700; letter-spacing:-0.025em; line-height:1.08; }
.cover h2 { margin:6mm 0 0; font-size:15pt; font-weight:600; color:#BFDCF6; letter-spacing:.01em; }
.cover .ar { margin-top:4mm; font-size:14pt; color:#9FC6E8; direction:rtl;
             text-align:left; max-width:120mm; }
.cover .rule { margin:11mm 0; height:3px; width:82px; background:#4FB3F6; border-radius:2px; }
.cover .blurb { font-size:11pt; color:#CFE2F5; max-width:118mm; line-height:1.65; }
.cover .stats { margin-top:auto; display:flex; gap:9px; flex-wrap:wrap; }
.cover .stats span { font-size:9.4pt; background:rgba(255,255,255,.12);
        border:1px solid rgba(255,255,255,.28); border-radius:999px; padding:5px 13px; }
.cover .by { margin-top:9mm; padding-top:6mm; border-top:1px solid rgba(255,255,255,.22); }
.cover .by b { font-size:19pt; letter-spacing:.01em; }
.cover .by i { display:block; font-style:normal; font-size:9.4pt; color:#AFD0EC;
        letter-spacing:.16em; text-transform:uppercase; margin-top:3px; }
.toc h2 { margin:0 0 3mm; font-size:21pt; letter-spacing:-0.02em; color:#0B1220; }
.toc .lead { margin:0 0 7mm; font-size:10pt; color:#5B718A; }
table.toc-t { width:100%%; border-collapse:collapse; font-size:9.6pt; }
table.toc-t th { background:#0C2340; color:#fff; font-size:8.6pt; letter-spacing:.09em;
        text-transform:uppercase; padding:7px 9px; text-align:left; font-weight:600; }
table.toc-t th.n, table.toc-t td.n { text-align:center; width:15mm; }
table.toc-t td { padding:6px 9px; border-bottom:1px solid #E3EAF2; vertical-align:middle; }
table.toc-t tr:nth-child(even) td { background:#F6F9FC; }
table.toc-t td.ls { font-weight:700; color:#1E7BC0; white-space:nowrap; width:24mm; }
table.toc-t td.ar { direction:rtl; color:#5B718A; font-size:9pt; }
.uhead td { background:#102A46 !important; color:#fff; font-weight:700; font-size:9.2pt;
        letter-spacing:.08em; text-transform:uppercase; }
.divider { background:linear-gradient(140deg,#071020 0%%,#0C2340 50%%,#17548C 100%%); color:#fff;
        display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; }
.divider .k { font-size:10pt; letter-spacing:.24em; text-transform:uppercase; color:#8FC2EA; }
.divider h1 { margin:6mm 0 0; font-size:38pt; font-weight:700; letter-spacing:-0.02em; }
.divider .s { margin-top:4mm; font-size:14pt; color:#CFE2F5; }
.divider .ar { margin-top:3mm; font-size:13pt; color:#8FC2EA; direction:rtl; }
.divider .rule { margin:9mm auto 0; height:3px; width:70px; background:#4FB3F6; border-radius:2px; }
""" % WM64


def _head(title):
    return ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>' + title +
            '</title><style>' + CSS + EXTRA + '</style></head><body>')


def cover(nq, nfig, npages):
    return ('<div class="sheet cover"><div class="inner">'
            '<span class="chip">Egyptian Baccalaureate &middot; Grade 11</span>'
            '<h1>Physics<br>Performance &amp;<br>Assessment Tasks</h1>'
            '<h2>The complete book, translated and solved &mdash; step by step</h2>'
            + ('' if EN_ONLY else
               '<div class="ar">كتاب الأداءات والتقييمات &mdash; ترجمة كاملة مع الحل بالخطوات</div>') +
            '<div class="rule"></div>'
            '<div class="blurb">Every lesson of the ministry assessments book, rewritten in scientific '
            'English, with every figure redrawn from scratch and every question worked through in full. '
            'The complete answer key is gathered at the back of the book.</div>'
            '<div class="stats"><span>19 handouts</span><span>' + str(nq) + ' questions</span>'
            '<span>' + str(nfig) + ' original figures</span><span>' + str(npages) + ' pages</span></div>'
            '<div class="by"><b>Mr. Gemy</b><i>Physics &middot; English Section</i></div>'
            '</div></div>')


def contents(rows, nfront):
    """rows : list of (stem, unit, label, title_en, title_ar, qpage, apage)."""
    h = ['<div class="sheet toc"><h2>Contents</h2>'
         '<p class="lead">The questions of the whole book come first, lesson by lesson; '
         'the full step-by-step answer key follows at the back.</p>'
         '<table class="toc-t"><tr><th class="n">#</th><th>Lesson</th><th>Title</th>' +
         ('' if EN_ONLY else '<th>العنوان</th>') +
         '<th class="n">Questions</th><th class="n">Answers</th></tr>']
    ncol = 5 if EN_ONLY else 6
    cur = None
    i = 0
    for stem, unit, lab, ten, tar, qp, ap in rows:
        if unit != cur:
            cur = unit
            u = UNITS[unit]
            h.append('<tr class="uhead"><td colspan="' + str(ncol) + '">' + u[0] + ' &middot; ' + u[1] + '</td></tr>')
        i += 1
        h.append('<tr><td class="n">' + str(i) + '</td><td class="ls">' + lab + '</td><td>' + ten +
                 '</td>' + ('' if EN_ONLY else '<td class="ar">' + tar + '</td>') +
                 '<td class="n">' + str(qp) + '</td><td class="n">' + str(ap) + '</td></tr>')
    h.append('</table></div>')
    return ''.join(h)


def divider(kicker, title, sub, ar):
    return ('<div class="sheet divider"><div class="k">' + kicker + '</div><h1>' + title + '</h1>'
            '<div class="rule"></div><div class="s">' + sub + '</div>' + ('' if EN_ONLY else '<div class="ar">' + ar + '</div>') + '</div>')


def front_html(rows, nq, nfig, npages, nfront):
    return _head('Physics Assessments Book') + cover(nq, nfig, npages) + \
        contents(rows, nfront) + '</body></html>'


def dividers_html():
    h = [_head('dividers')]
    for u in (1, 2):
        a, b, c = UNITS[u]
        h.append(divider('Questions', a, b, c))
    h.append(divider('The back of the book', 'Answer Key',
                     'Every question, solved step by step',
                     'مفتاح الإجابة &middot; الحل بالخطوات لكل سؤال'))
    h.append('</body></html>')
    return ''.join(h)

# -*- coding: utf-8 -*-
"""Grade 12 Physics - Chapter 1 revision booklet : 100 questions + final answers + step-by-step solutions."""
import base64
import sys
from circ import DEFS
from qlib import LET, final
import c1
SECS = [c1.S]
for name in ('c2', 'c3', 'c4'):
    try:
        SECS.append(__import__(name).S)
    except ImportError:
        pass

THEME = {'s1': ('#7c3aed', '#db2777', '#f5f3ff', '#fdf2f8'),
         's2': ('#ea580c', '#f59e0b', '#fff7ed', '#fffbeb'),
         's3': ('#0d9488', '#16a34a', '#f0fdfa', '#f0fdf4'),
         's4': ('#2563eb', '#06b6d4', '#eff6ff', '#ecfeff')}

WM = ('<svg xmlns="http://www.w3.org/2000/svg" width="330" height="215">'
      '<text x="165" y="120" font-family="Liberation Sans,Arial,sans-serif" font-size="30" font-weight="700" '
      'fill="#4c1d95" fill-opacity="0.05" text-anchor="middle" transform="rotate(-27 165 120)">Mr. Gemy</text></svg>')
WM64 = base64.b64encode(WM.encode()).decode()

CSS = """
@page { size:A4; margin:12mm 11mm 14mm 11mm;
  @bottom-left { content:"Mr. Gemy \\00B7  Grade 12 Physics \\00B7  Chapter 1 Revision"; font:600 8pt 'Liberation Sans';
                 color:#6d28d9; }
  @bottom-right { content:"page " counter(page); font:700 8.5pt 'Liberation Sans'; color:#db2777; } }
@page cover { margin:0; @bottom-left { content:none } @bottom-right { content:none } }
* { -webkit-print-color-adjust:exact; print-color-adjust:exact; box-sizing:border-box; }
html { font-size:10.8pt; }
body { margin:0; font-family:'Liberation Sans',Arial,sans-serif; color:#0f172a; line-height:1.45;
       background-image:url("data:image/svg+xml;base64,%(wm)s"); }
sup, sub { font-size:72%%; line-height:0; }

/* ---------------- cover ---------------- */
.cover { page:cover; width:210mm; height:297mm; position:relative; overflow:hidden; color:#fff; break-after:page;
  background:radial-gradient(circle at 18%% 12%%, #f472b6 0, rgba(244,114,182,0) 38%%),
             radial-gradient(circle at 88%% 30%%, #fbbf24 0, rgba(251,191,36,0) 34%%),
             radial-gradient(circle at 70%% 92%%, #22d3ee 0, rgba(34,211,238,0) 40%%),
             linear-gradient(150deg,#1e1b4b 0%%,#4c1d95 38%%,#9d174d 72%%,#c2410c 100%%); }
.cover .art { position:absolute; left:0; top:0; width:210mm; height:297mm; }
.cover .in { position:absolute; left:16mm; right:16mm; top:24mm; }
.cover .kick { display:inline-block; font-weight:700; letter-spacing:3px; font-size:11pt; padding:5px 14px;
  border-radius:30px; background:rgba(255,255,255,.14); border:1.5px solid rgba(255,255,255,.45); }
.cover h1 { font-size:52pt; line-height:1; margin:14px 0 6px; letter-spacing:1px;
  text-shadow:0 4px 0 rgba(0,0,0,.25); }
.cover h1 span { color:#fde047; text-shadow:0 4px 0 rgba(0,0,0,.25), 0 0 18px rgba(251,146,60,.8); }
.cover .t2 { font-size:21pt; font-weight:700; margin:4px 0 16px; }
.cover .count { display:flex; gap:10px; margin:18px 0; }
.cover .count div { background:rgba(255,255,255,.13); border:1.5px solid rgba(255,255,255,.4); border-radius:14px;
  padding:10px 14px; text-align:center; min-width:34mm; }
.cover .count b { display:block; font-size:24pt; color:#fde047; }
.cover .count span { font-size:9.5pt; letter-spacing:.5px; }
.cover .lessons { margin-top:10px; display:grid; grid-template-columns:1fr 1fr; gap:8px; }
.cover .lessons div { border-radius:12px; padding:9px 13px; font-weight:700; font-size:11pt;
  background:rgba(15,23,42,.35); border-left:6px solid; }
.cover .lessons small { display:block; font-weight:400; font-size:8.8pt; opacity:.9; margin-top:2px; }
.cover .who { position:absolute; left:16mm; right:16mm; bottom:16mm; display:flex; justify-content:space-between;
  align-items:flex-end; }
.cover .who .nm { font-size:30pt; font-weight:700; }
.cover .who .nm small { display:block; font-size:10.5pt; font-weight:400; letter-spacing:2px; opacity:.9; }
.cover .who .gr { text-align:right; font-size:11pt; line-height:1.5; background:rgba(255,255,255,.14);
  border-radius:12px; padding:8px 14px; border:1.5px solid rgba(255,255,255,.4); }

/* ---------------- intro ---------------- */
.data { border-radius:14px; padding:11px 15px; margin:0 0 12px; color:#fff;
  background:linear-gradient(110deg,#4c1d95,#9d174d 60%%,#c2410c); }
.data h2 { margin:0 0 5px; font-size:14pt; }
.data .row { display:flex; flex-wrap:wrap; gap:7px; }
.data .row span { background:rgba(255,255,255,.16); border:1.3px solid rgba(255,255,255,.4); border-radius:8px;
  padding:3px 10px; font-size:10pt; }
.legend { display:flex; gap:8px; margin:0 0 10px; font-size:9.6pt; }
.legend span { border-radius:20px; padding:3px 11px; font-weight:700; }

/* ---------------- sections ---------------- */
.sec { border-radius:14px; padding:11px 16px; margin:4px 0 10px; color:#fff; break-after:avoid; position:relative;
  background:linear-gradient(105deg,var(--a),var(--b)); display:flex; justify-content:space-between; align-items:center;
  box-shadow:0 3px 0 rgba(15,23,42,.12); }
.sec h2 { margin:0; font-size:16pt; }
.sec .sub { font-size:9.5pt; opacity:.95; margin-top:2px; }
.sec .cnt { font-size:10pt; font-weight:700; background:rgba(255,255,255,.2); border:1.5px solid rgba(255,255,255,.55);
  border-radius:9px; padding:5px 11px; white-space:nowrap; }
.newsec { break-before:page; }

.q { position:relative; background:rgba(255,255,255,.93); border:1.5px solid var(--line); border-left:6px solid var(--a);
  border-radius:4px 12px 12px 4px; padding:8px 12px 9px 13px; margin:8px 0; break-inside:avoid; }
.q .n { display:inline-flex; align-items:center; justify-content:center; min-width:27px; height:27px; padding:0 6px;
  border-radius:14px; color:#fff; font-weight:700; font-size:10.5pt; margin-right:7px;
  background:linear-gradient(135deg,var(--a),var(--b)); box-shadow:0 2px 0 rgba(15,23,42,.18); vertical-align:1px; }
.tag { float:right; font-size:8.3pt; font-weight:700; border-radius:20px; padding:2px 9px; margin-left:8px; }
.tag.MCQ { background:var(--soft); color:var(--a); border:1.3px solid var(--a); }
.tag.Problem { background:#ecfdf5; color:#047857; border:1.3px solid #10b981; }
.tag.HOTS { background:linear-gradient(90deg,#fef3c7,#fde68a); color:#92400e; border:1.3px solid #f59e0b; }
.qt { display:inline; }
.side { display:flex; gap:12px; align-items:flex-start; }
.side .l { flex:1; min-width:0; }
.side .r { flex:none; width:44%%; }
.ch { display:grid; grid-template-columns:1fr 1fr; gap:5px 10px; margin-top:8px; }
.ch.one { grid-template-columns:1fr; }
.ch div { border:1.3px solid var(--line); border-radius:9px; padding:4px 9px; background:#fff; font-size:10.3pt; }
.ch b { display:inline-flex; width:20px; height:20px; border-radius:50%%; align-items:center; justify-content:center;
  color:#fff; font-size:9pt; margin-right:6px; background:var(--a); }
.ch.pic div { text-align:center; padding:3px; }
.wr { border-top:1.5px dashed var(--line); margin-top:9px; height:13mm; }
.wr.l { height:22mm; }
figure.fig { margin:6px auto 2px; text-align:center; break-inside:avoid; }
svg.svgfig { width:100%%; height:auto; background:#fff; border:1.4px solid var(--line); border-radius:12px; padding:3px; }
figcaption, .fcap { font-size:8.8pt; color:#64748b; font-style:italic; text-align:center; margin-top:2px; }
.figrow { display:flex; gap:8px; justify-content:center; }
.figrow figure { flex:1; margin:4px 0 0; }

/* ---------------- answers ---------------- */
.akey { break-before:page; }
.bighead { border-radius:14px; padding:12px 16px; margin:0 0 10px; color:#fff;
  background:linear-gradient(105deg,#1e1b4b,#7c3aed 45%%,#db2777); }
.bighead h2 { margin:0; font-size:17pt; } .bighead div { font-size:9.8pt; opacity:.95; }
table.fa { width:100%%; border-collapse:separate; border-spacing:0; font-size:9.4pt; margin-bottom:8px; }
table.fa td { padding:3px 7px; border-bottom:1px solid #e2e8f0; }
table.fa td.qn { width:7%%; text-align:center; font-weight:700; color:#fff; border-radius:6px; }
.fawrap { display:grid; grid-template-columns:1fr 1fr; gap:0 12px; }
.sol { border:1.3px solid var(--line); border-left:5px solid var(--a); border-radius:4px 10px 10px 4px;
  background:rgba(255,255,255,.95); padding:5px 11px 6px; margin:6px 0; break-inside:avoid; }
.sol .sn { display:inline-block; color:#fff; border-radius:12px; padding:1px 9px; font-weight:700; font-size:9.5pt;
  margin-right:7px; background:linear-gradient(135deg,var(--a),var(--b)); }
.sol .hd { font-size:9.6pt; color:#475569; font-weight:700; }
.sol .st { font-family:'Liberation Mono','DejaVu Sans Mono',monospace; font-size:9.1pt; line-height:1.55; margin:4px 0 2px; }
.sol .fa2 { display:inline-block; margin-top:2px; font-weight:700; font-size:9.6pt; color:#065f46; background:#d1fae5;
  border:1.3px solid #10b981; border-radius:7px; padding:1px 9px; }
.solsec { border-radius:10px; padding:6px 14px; margin:12px 0 6px; color:#fff; font-weight:700; font-size:12pt;
  background:linear-gradient(105deg,var(--a),var(--b)); break-after:avoid; }
"""


def vars_(k):
    a, b, s1, s2 = THEME[k]
    return ('--a:%s;--b:%s;--soft:%s;--soft2:%s;--line:%s' % (a, b, s1, s2, {'s1': '#ddd6fe', 's2': '#fed7aa',
                                                                         's3': '#99f6e4', 's4': '#bfdbfe'}[k]))


def cover():
    import cover_art
    lessons = [('#c4b5fd', 'Lesson 1', 'Electric current &amp; Ohm&#8217;s law'),
               ('#fdba74', 'Lesson 2', 'Connecting resistors'),
               ('#5eead4', 'Lesson 3', 'Ohm&#8217;s law for a closed circuit'),
               ('#93c5fd', 'Lesson 4', 'Kirchhoff&#8217;s laws')]
    n = sum(len(s.q) for s in SECS)
    nf = sum(1 for s in SECS for q in s.q if q['fig'])
    return ('<div class="cover">' + cover_art.svg() + '<div class="in">'
            '<span class="kick">GRADE 12 &middot; PHYSICS &middot; LANGUAGES</span>'
            '<h1>Chapter 1<br><span>Revision</span></h1>'
            '<div class="t2">Electric Current &amp; Ohm&#8217;s Law</div>'
            '<div class="count"><div><b>%d</b><span>QUESTIONS</span></div><div><b>%d</b><span>FIGURES</span></div>'
            '<div><b>4</b><span>LESSONS</span></div><div><b>100%%</b><span>STEP-BY-STEP</span></div></div>'
            '<div class="lessons">%s</div></div>'
            '<div class="who"><div class="nm">Mr. Gemy<small>PHYSICS</small></div>'
            '<div class="gr">Final answers + full step-by-step<br>solutions at the end of the booklet</div></div></div>'
            % (n, nf, ''.join('<div style="border-color:%s">%s<small>%s</small></div>' % l for l in lessons)))


def qhtml(n, q, key):
    tag = '<span class="tag %s">%s</span>' % (q['tag'], {'MCQ': 'MCQ', 'Problem': 'Problem', 'HOTS': '&#9733; HOTS'}[q['tag']])
    head = tag + '<span class="n">%d</span><div class="qt">%s</div>' % (n, q['t'])
    ch = ''
    if q['ch']:
        pic = any('<svg' in c for c in q['ch'])
        longc = any(len(c) > 46 and '<svg' not in c for c in q['ch'])
        cls = 'ch' + (' pic' if pic else '') + (' one' if longc else '')
        ch = '<div class="%s">%s</div>' % (cls, ''.join('<div><b>%s</b>%s</div>' % (LET[i], c)
                                                        for i, c in enumerate(q['ch'])))
    else:
        ch = '<div class="wr%s"></div>' % (' l' if len(q['sol']) > 2 else '')
    if q['fig'] and q['side']:
        return ('<div class="q"><div class="side"><div class="l">%s%s</div><div class="r">%s</div></div></div>'
                % (head, ch, q['fig']))
    return '<div class="q">%s%s%s</div>' % (head, q['fig'] or '', ch)


def main(out='rev12.html'):
    H = ['<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Grade 12 Physics - Chapter 1 Revision'
         '</title><style>' + CSS % {'wm': WM64} + '</style></head><body>' + DEFS + cover()]
    H.append('<div class="data" style="%s"><h2>Data &amp; notes for all questions</h2><div class="row">'
             '<span>e = 1.6 &times; 10<sup>&#8722;19</sup> C</span><span>&#960; = 3.14 (unless 22/7 is given)</span>'
             '<span>ammeters : negligible resistance</span><span>voltmeters : very large resistance</span>'
             '<span>r = 0 &#8594; negligible internal resistance</span></div></div>' % vars_('s1'))
    H.append('<div class="legend"><span style="background:#f5f3ff;color:#7c3aed;border:1.3px solid #7c3aed">MCQ</span>'
             '<span style="background:#ecfdf5;color:#047857;border:1.3px solid #10b981">Problem &#8212; write the steps</span>'
             '<span style="background:#fef3c7;color:#92400e;border:1.3px solid #f59e0b">&#9733; HOTS &#8212; higher order '
             'thinking</span></div>')
    n = 0
    nums = []
    for k, s in enumerate(SECS):
        H.append('<div style="%s">' % vars_(s.key))
        H.append('<div class="sec"><div><h2>Section %d &#8212; %s</h2><div class="sub">%s</div></div>'
                 '<span class="cnt">Questions %d &#8211; %d</span></div>' % (k + 1, s.title, s.sub, n + 1, n + len(s.q)))
        for q in s.q:
            n += 1
            nums.append((n, q, s.key))
            H.append(qhtml(n, q, s.key))
        H.append('</div>')
    # ---------- final answers
    H.append('<div class="akey"><div class="bighead"><h2>Final Answers</h2><div>Check yourself first &#8212; the full '
             'step-by-step solutions follow.</div></div><div class="fawrap">')
    half = (len(nums) + 1) // 2
    for part in (nums[:half], nums[half:]):
        H.append('<table class="fa">' + ''.join(
            '<tr><td class="qn" style="background:%s">%d</td><td>%s</td></tr>' % (THEME[k][0], i, final(q))
            for i, q, k in part) + '</table>')
    H.append('</div>')
    # ---------- solutions
    cur = None
    for i, q, k in nums:
        if k != cur:
            if cur:
                H.append('</div>')
            cur = k
            s = [x for x in SECS if x.key == k][0]
            H.append('<div style="%s"><div class="solsec">Step-by-step solutions &#8212; %s</div>' % (vars_(k), s.title))
        H.append('<div class="sol"><span class="sn">Q %d</span><span class="hd">%s</span><div class="st">%s</div>'
                 '<span class="fa2">&#10004; %s</span></div>' % (i, q['title'], '<br>'.join(q['sol']), final(q)))
    H.append('</div></div></body></html>')
    open(out, 'w', encoding='utf-8').write(''.join(H))
    print(out, 'written :', n, 'questions')


if __name__ == '__main__':
    main(*sys.argv[1:])

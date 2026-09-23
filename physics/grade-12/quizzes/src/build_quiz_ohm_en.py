# -*- coding: utf-8 -*-
"""English quiz (A4, questions only) : Ohm's law for a closed circuit, cells in series, the rheostat."""
import os
import sys
# the shared drawing library and page style live with the grade-11 handouts
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..', 'grade-11', 'handouts', 'src'))
import figs_ohm as F
from css_apple import CSS
from docbase import WM64

EXTRA = """
@page { size:A4; margin:12mm 12mm 13mm 12mm; }
html { font-size:11pt; }
body { background-image:url("data:image/svg+xml;base64,%s"); background-repeat:repeat; line-height:1.55; }
.hero { padding:18px 24px 16px; }
.hero h1 { font-size:21pt; }
.hero .sub { max-width:74%%; }
.info { display:flex; gap:10px; margin:0 0 11px; }
.info div { flex:1; border:1px solid #E1E8F0; background:#fff; border-radius:12px; padding:7px 14px;
        font-size:10.4pt; color:#334155; }
.info div:first-child { flex:2.2; }
.info div b { color:#17548C; }
.note { border-left:3px solid #0EA5E9; background:#F5FBFF; border-radius:0 10px 10px 0;
        padding:7px 14px; margin:0 0 9px; font-size:9.8pt; color:#0C4A6E; }
.card { padding:10px 15px 11px; margin:9px 0; }
.qtx { font-size:10.8pt; }
.ch div { font-size:10.6pt; }
.ch.row { grid-template-columns:repeat(4,1fr); }
.ch.row3 { grid-template-columns:repeat(3,1fr); }
svg.svgfig { max-width:430px !important; }
.card.compact svg.svgfig { max-width:390px !important; }
.side { display:grid; grid-template-columns:1fr 340px; gap:14px; align-items:center; }
.side .qh { display:flex; gap:9px; align-items:flex-start; }
.side .ch { grid-template-columns:1fr 1fr; }
.side figure.fig { margin:4px 0 0; }
.side svg.svgfig { max-width:340px !important; }
figure.fig { margin:6px auto 0; }
figcaption { margin-top:2px; }
""" % WM64

h = ['<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
     '<title>Quiz - Ohm&rsquo;s Law for a Closed Circuit</title><style>', CSS, EXTRA,
     '</style></head><body>']
a = h.append
VB = 'V<sub>B</sub>'

a('<div class="hero"><span class="chip">Grade 12 &middot; Physics &middot; Current Electricity</span>'
  '<h1>Quiz &middot; Ohm&rsquo;s Law for a Closed Circuit</h1>'
  '<div class="sub">Cells connected in series and the rheostat &mdash; five challenging questions. '
  'Read every figure carefully before you choose.</div>'
  '<div class="meta"><span>5 questions</span><span>Time: 25 minutes</span><span>Mark: 5</span></div>'
  '<div class="sig"><b>Mr. Gemy</b><i>Physics</i></div></div>')
a('<div class="info"><div><b>Name:</b> ..........................................</div>'
  '<div><b>Class:</b> ............</div><div><b>Mark:</b> ........ / 5</div></div>')
a('<div class="note">Consider the connecting wires to have negligible resistance, the ammeter to be ideal '
  '(negligible resistance) and the voltmeter to be ideal (very large resistance, so it draws no '
  'current).</div>')

n = [0]


def q(text, fig, ch, side=False, cls=''):
    n[0] += 1
    head = ('<div class="qh"><div class="qno">' + str(n[0]) + '</div>'
            '<div class="qtx">' + text + '</div><span class="tag">MCQ</span></div>')
    row = 'row3' if len(ch) == 3 else 'row'
    opts = ('<div class="ch' + ('' if side else ' ' + row) + '">' +
            ''.join('<div><i>' + le + '</i>' + c + '</div>' for le, c in zip('ABCD', ch)) + '</div>')
    if side and len(ch) == 3:          # three short answers : one row under the text and figure
        opts = ('<div class="ch row3">' + ''.join('<div><i>' + le + '</i>' + c + '</div>'
                                                  for le, c in zip('ABC', ch)) + '</div>')
        a('<div class="card ' + cls + '"><div class="side"><div>' + head + '</div>' + fig +
          '</div>' + opts + '</div>')
    elif side:
        a('<div class="card ' + cls + '"><div class="side"><div>' + head + opts + '</div>' + fig +
          '</div></div>')
    else:
        a('<div class="card ' + cls + '">' + head + fig + opts + '</div>')


q('In the circuit shown, when the ammeter reads 2 A the voltmeter reads 10 V. When the slider of the '
  'rheostat is moved, the ammeter reads 4 A and the voltmeter reads 8 V. <b>The maximum current</b> '
  'that the cell can deliver (when its terminals are joined by a wire of negligible resistance) is:',
  F.terminal_voltage('Figure (1)'),
  ['5 A', '6 A', '12 A', '24 A'], side=True)

q('The terminals of a cell are connected to a 2 &Omega; resistor and a current of 3 A flows. When the '
  'resistor is replaced by a 5 &Omega; resistor, the current becomes 1.5 A. <b>The emf of the cell and its '
  'internal resistance</b> are respectively:',
  F.two_resistors('Figure (2)'),
  ['9 V , 1 &Omega;', '7.5 V , 0.5 &Omega;', '12 V , 2 &Omega;', '6 V , zero'])

q('A battery consists of 6 identical cells connected in series. The emf of each cell is 1.5 V and its '
  'internal resistance is 0.5 &Omega;, and the battery is connected to an external resistance of '
  '6 &Omega;. If the fourth cell is connected <b>in reverse</b> by mistake, as shown in the figure, the '
  'ratio of the current <b>after</b> the mistake to the current <b>before</b> it is:',
  F.six_cells('Figure (3)', 'reversed', 'Helvetica, Arial, sans-serif'),
  ['5/6', '2/3', '3/4', '1/2'])

q('In the circuit shown, two batteries are connected in series <b>in opposition</b> (the positive '
  'terminal of one is connected to the positive terminal of the other). <b>The reading of the '
  'voltmeter</b> connected across the terminals of battery (2) is:',
  F.opposing_batteries('Figure (4)'),
  ['6 V', '5.5 V', '11 V', '6.5 V'], side=True)

q('In the circuit shown, the rheostat is connected through its end (<i>a</i>) and its sliding contact '
  '(<i>S</i>), while its end (<i>b</i>) is left free. If the sliding contact S is moved <b>towards '
  'end (<i>a</i>)</b>, then <b>the reading of the voltmeter</b>:',
  F.rheostat_parallel('Figure (5)'),
  ['increases', 'decreases', 'remains constant'], side=True)

a('</body></html>')
open('quiz_ohm_en.html', 'w', encoding='utf-8').write(''.join(h))
print('quiz_ohm_en.html written -', n[0], 'questions')

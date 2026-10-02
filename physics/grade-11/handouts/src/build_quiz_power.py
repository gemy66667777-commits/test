# -*- coding: utf-8 -*-
"""Quiz - Power and Efficiency (lesson 1-6) : 5 questions, questions only (no answers). Grade 11, English."""
import figs_l6 as L6
import figs_power as P
from css import CSS
from docbase import WM64

H = []
a = H.append
a('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Quiz - Power and Efficiency</title>'
  '<style>' + CSS + """
body { background-image:url("data:image/svg+xml;base64,""" + WM64 + """"); background-repeat:repeat; }
.head2 { background:linear-gradient(100deg,#0f2f5b 0%,#1d4ed8 60%,#2563eb 100%); }
.line { display:flex; gap:14px; margin:8px 0 4px; font-size:10.5pt; }
.line span { flex:1; border-bottom:1.6px dotted #64748b; padding-bottom:2px; }
.data { background:#fffbeb; border:1.6px solid #f59e0b; border-radius:9px; padding:7px 12px; font-size:10.3pt; margin:8px 0; }
.q { background:rgba(255,255,255,.92); }
.qtext { font-size:11pt; }
.ch div { padding:5px 10px; }
.hard { float:right; font-size:8.5pt; font-weight:700; color:#92400e; background:#fef3c7; border:1.3px solid #f59e0b;
        border-radius:12px; padding:1px 9px; }
.box2 { display:inline-block; width:34px; height:26px; border:1.8px solid #0f2f5b; border-radius:6px; float:right;
        margin-left:8px; background:#fff; }
</style></head><body>""")

a('<div class="head head2"><div><h1>Quiz &mdash; Power and Efficiency</h1>'
  '<div class="sub">Physics &middot; Grade 11 &middot; Lesson 1&ndash;6 &middot; Multiple choice &middot; 5 questions'
  '</div></div><div class="badge">Mr. Gemy<br>Time: 15 min<br>Total: 5 marks</div></div>')

a('<div class="line"><span>Name: </span><span>Class: </span><span>Date: </span></div>')
a('<div class="data"><b>Data:</b> &nbsp; g = 9.8 m/s&sup2; &nbsp;|&nbsp; cos 37&deg; = 0.8 &nbsp;|&nbsp; '
  'cos 60&deg; = 0.5.<br>'
  '<b>Instructions:</b> choose the <b>one</b> correct answer for each question and write its letter in the box.</div>')

QN = [0]


def q(text, fig, choices, hard=False):
    QN[0] += 1
    a('<div class="q"><span class="box2"></span>' + ('<span class="hard">&#9733; challenging</span>' if hard else '') +
      '<div class="qtext"><span class="n">Q' + str(QN[0]) + '</span>' + text + '</div>')
    if fig:
        a(fig)
    one = any(len(c) > 38 for c in choices)
    a('<div class="ch"' + (' style="grid-template-columns:1fr"' if one else '') + '>')
    for L, c in zip('ABCD', choices):
        a('<div><b>' + L + ')</b> ' + c + '</div>')
    a('</div></div>')


q('Lift A raises a load of <b>400 kg</b> through <b>15 m</b> in <b>30 s</b>. Lift B raises the <b>same load</b> '
  'through the <b>same height</b> in <b>20 s</b>. Which statement is correct?',
  None,
  ['lift B does 1.5 times the work done by lift A',
   'they do the same work, and the power of B is 1.5 times the power of A',
   'they have the same power, and lift B does more work',
   'they do the same work, and the power of A is 1.5 times the power of B'])

q('A rope pulls a box along a horizontal floor at a constant speed of <b>5 m/s</b> with a force of <b>60 N</b> that '
  'makes <b>37&deg;</b> with the direction of motion (Fig. 1). The power of the force is:',
  L6.block_force_angle('Fig. 1'),
  ['300 W', '180 W', '240 W', '12 W'])

q('An electric kettle takes a power of <b>2500 W</b> and gives the water a useful thermal power of <b>2000 W</b>. '
  'Its efficiency is:',
  None,
  ['125 %', '80 %', '20 %', '50 %'])

q('A motor of efficiency <b>70 %</b> raises a load of <b>140 kg</b> at a <b>constant speed</b> of <b>0.25 m/s</b> '
  '(Fig. 2). The electric power taken by the motor is:',
  P.motor_lift('Fig. 2', '140 kg', 'v = 0.25 m/s'),
  ['343 W', '490 W', '240.1 W', '1372 W'], hard=True)

q('Fig. 3 shows the useful work done by two machines X and Y against time. The efficiency of X is <b>80 %</b> and '
  'the efficiency of Y is <b>60 %</b>. The ratio of the <b>input</b> powers of the two machines '
  '( P<sub>in</sub>(X) / P<sub>in</sub>(Y) ) is:',
  P.wt_graph('Fig. 3'),
  ['1.25', '5/3', '0.8', '2.22'], hard=True)

a('</body></html>')

open('quiz_power.html', 'w', encoding='utf-8').write(''.join(H))
print('quiz_power.html written :', QN[0], 'questions')

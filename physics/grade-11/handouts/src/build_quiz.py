# -*- coding: utf-8 -*-
import figs_proj as P
from css import CSS

H = []
a = H.append
a('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Quiz - Projectile at an Angle</title>'
  '<style>' + CSS + """
.head2 { background:linear-gradient(100deg,#0f2f5b 0%,#1d4ed8 60%,#2563eb 100%); }
.line { display:flex; gap:14px; margin:8px 0 4px; font-size:10.5pt; }
.line span { flex:1; border-bottom:1.6px dotted #64748b; padding-bottom:2px; }
.data { background:#fffbeb; border:1.6px solid #f59e0b; border-radius:9px; padding:7px 12px; font-size:10.3pt; margin:8px 0; }
.q { background:#fff; }
.qtext { font-size:11pt; }
.ch div { padding:5px 10px; }
.keytab td { text-align:left; }
.keytab td.c { text-align:center; font-weight:700; color:#15803d; font-size:12pt; }
</style></head><body>""")

a('<div class="head head2"><div><h1>Quiz &mdash; Projectile Motion at an Angle</h1>'
  '<div class="sub">Physics &middot; Grade 11 &middot; Multiple choice &middot; 5 questions</div></div>'
  '<div class="badge">Time: 15 min<br>Total: 5 marks</div></div>')

a('<div class="line"><span>Name: </span><span>Class: </span><span>Date: </span></div>')
a('<div class="data"><b>Data:</b> &nbsp; g = 10 m/s&sup2; &nbsp;|&nbsp; sin 30&deg; = 0.5 , cos 30&deg; = 0.866 '
  '&nbsp;|&nbsp; sin 37&deg; = 0.6 , cos 37&deg; = 0.8 &nbsp;|&nbsp; sin 53&deg; = 0.8 , cos 53&deg; = 0.6 '
  '&nbsp;|&nbsp; air resistance is neglected.<br>'
  '<b>Instructions:</b> choose the <b>one</b> correct answer for each question and write its letter in the box.</div>')

QN = [0]


def q(text, fig, choices):
    QN[0] += 1
    a('<div class="q"><div class="qtext"><span class="n">Q' + str(QN[0]) + '</span>' + text + '</div>')
    a(fig)
    a('<div class="ch">')
    for L, c in zip('ABCD', choices):
        a('<div><b>' + L + ')</b> ' + c + '</div>')
    a('</div></div>')


q('A projectile is fired from the ground with a velocity of <b>40 m/s</b> at <b>30&deg;</b> to the horizontal, '
  'as shown in Fig. 1. The total <b>time of flight T</b> is:',
  P.q1_fig(), ['2 s', '4 s', '6 s', '8 s'])

q('A ball is projected with a velocity of <b>20 m/s</b> at <b>53&deg;</b> to the horizontal (Fig. 2). '
  'The <b>maximum height H</b> reached by the ball is:',
  P.q2_fig(), ['8 m', '12.8 m', '16 m', '20 m'])

q('Fig. 3 shows the two components of the initial velocity of a projectile. '
  'The magnitude of the initial velocity <b>v<sub>0</sub></b> and the angle of projection <b>&theta;</b> are:',
  P.q3_fig(), ['50 m/s and 37&deg;', '50 m/s and 53&deg;', '70 m/s and 53&deg;', '35 m/s and 45&deg;'])

q('A projectile is launched with a velocity of <b>50 m/s</b> at <b>37&deg;</b> to the horizontal. '
  'Its <b>speed at the highest point P</b> of the path (Fig. 4) is:',
  P.q4_fig(), ['zero', '30 m/s', '40 m/s', '50 m/s'])

q('Two balls A and B are projected from the same point with the <b>same speed</b>, at <b>30&deg;</b> and '
  '<b>60&deg;</b> to the horizontal (Fig. 5). Which statement is <b>correct</b>?',
  P.q5_fig(), ['They have the same range and the same maximum height.',
               'They have the same range, but B rises higher and stays longer in the air.',
               'A has a greater range than B.',
               'B has a greater range and a shorter time of flight.'])

a('<div class="foot"><span>Quiz &mdash; Projectile Motion at an Angle &middot; Grade 11 Physics</span>'
  '<span>T = 2v&#8320;sin&theta;/g &middot; H = v&#8320;&sup2;sin&sup2;&theta;/2g &middot; R = v&#8320;&sup2;sin2&theta;/g</span></div>')

# ---------------- answer key ----------------
a('<div class="pb"></div>')
a('<h2><span class="num">&#10003;</span>Model answer &mdash; final answers</h2>')
a('<table class="keytab"><tr><th style="width:8%">Q</th><th style="width:12%">Answer</th><th>Final value</th></tr>'
  '<tr><td style="text-align:center"><b>1</b></td><td class="c">B</td><td>T = 4 s</td></tr>'
  '<tr><td style="text-align:center"><b>2</b></td><td class="c">B</td><td>H = 12.8 m</td></tr>'
  '<tr><td style="text-align:center"><b>3</b></td><td class="c">B</td><td>v<sub>0</sub> = 50 m/s , &theta; = 53&deg;</td></tr>'
  '<tr><td style="text-align:center"><b>4</b></td><td class="c">C</td><td>v = 40 m/s</td></tr>'
  '<tr><td style="text-align:center"><b>5</b></td><td class="c">B</td><td>same range ; B is higher and stays longer</td></tr>'
  '</table>')
a('</body></html>')

open('quiz.html', 'w', encoding='utf-8').write(''.join(H))
print('quiz.html written')

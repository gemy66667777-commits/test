# -*- coding: utf-8 -*-
"""Equilibrium of Forces - explanation + solved examples + exercises + final answers (Grade 11, English only).
Follows the ideas of lesson 1-5 in the assessments book : translational equilibrium only (sum of the forces = 0)."""
import figs_l45 as L45
import figs_l6 as L6
from css import CSS

H = []
a = H.append

a('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Equilibrium of Forces</title>'
  '<style>' + CSS + """
.ch { grid-template-columns:1fr 1fr; }
.ch.one { grid-template-columns:1fr; }
.tag { float:right; font-size:8.5pt; color:#64748b; border:1px solid #cbd5e1; border-radius:5px; padding:1px 7px;
       background:#f8fafc; }
.wr { border-top:1.4px dashed #cbd5e1; height:16mm; margin-top:8px; }
</style></head><body>""")

# ---------------- header ----------------
a('<div class="head"><div><h1>Equilibrium of Forces</h1>'
  '<div class="sub">The meaning of equilibrium &middot; &Sigma;F = 0 on each axis &middot; resolving forces '
  '&middot; cables, ropes &amp; springs</div></div>'
  '<div class="badge">Physics &mdash; Grade 11<br>Explanation &amp; Questions<br>g = 9.8 m/s&sup2;</div></div>')

# ---------------- 1 ----------------
a('<h2><span class="num">1</span>What does equilibrium mean?</h2>')
a('<p>A body is in <b>equilibrium</b> when the resultant of all the forces acting on it is <b>zero</b>. Its velocity '
  'then does not change, so the body either:</p>')
a('<ul><li>stays <b>at rest</b>, or</li><li>moves in a straight line with a <b>constant velocity</b>.</li></ul>')
a('<div class="box formula"><div class="big">&Sigma;F = 0</div>'
  '<div class="small">the condition of equilibrium : the vector sum of all the forces is zero</div></div>')
a('<div class="box note"><span class="t">Remember</span>Equilibrium does <b>not</b> mean &ldquo;no forces&rdquo;. '
  'Several forces may act on the body, but they cancel each other, so their <b>resultant</b> is zero.</div>')
a(L6.book_table('Fig. 1 &mdash; a book resting on a table.'))
a('<p>A book resting on a table is in equilibrium under two forces (Fig. 1):</p>')
a('<table><tr><th>Force</th><th>Direction</th><th>Source</th></tr>'
  '<tr><td>the weight W = m g</td><td>vertically downwards</td><td>the pull of the Earth on the book</td></tr>'
  '<tr><td>the normal force F<sub>N</sub></td><td>vertically upwards</td><td>the push of the table on the book '
  '(a contact force)</td></tr></table>')
a('<p>Since the book is at rest, F<sub>N</sub> = W. If a second book is placed on top, the table must support both, '
  'so the normal force on the lower book becomes 2 m g, while the weight of the lower book itself stays m g.</p>')

# ---------------- 2 ----------------
a('<h2><span class="num">2</span>Applying &Sigma;F = 0 on each axis</h2>')
a('<p>&Sigma;F = 0 is a vector equation. We apply it to each axis <b>separately</b>: the forces along the '
  'horizontal (x) axis must cancel, and the forces along the vertical (y) axis must cancel.</p>')
a('<div class="box formula"><div class="big">&Sigma;F<sub>x</sub> = 0 &nbsp;&nbsp; and &nbsp;&nbsp; '
  '&Sigma;F<sub>y</sub> = 0</div><div class="small">forces to the right = forces to the left &nbsp;|&nbsp; '
  'forces upwards = forces downwards</div></div>')
a('<p>A force that acts at an angle is first <b>resolved</b> into two perpendicular components. For a force F '
  'making an angle &theta; with the <b>horizontal</b>:</p>')
a('<div class="box formula"><div class="big">F<sub>x</sub> = F cos &theta; &nbsp;&nbsp;&nbsp; F<sub>y</sub> = F '
  'sin &theta;</div><div class="small">if the angle is measured from the <b>vertical</b>, the sin and the cos '
  'change places</div></div>')
a(L45.tension_components('Fig. 2 &mdash; a tension T resolved into a horizontal and a vertical component.'))

# ---------------- 3 ----------------
a('<h2><span class="num">3</span>Forces along one straight line</h2>')
a('<p>When all the forces act along the same vertical line, the forces upwards must equal the forces downwards. '
  'The missing force is the one that makes the sum zero; its sign tells us its direction (Fig. 3).</p>')
a(L6.three_forces('Fig. 3 &mdash; three forces along one vertical line.'))

# ---------------- 4 ----------------
a('<h2><span class="num">4</span>A weight hanging from two identical cables</h2>')
a('<p>A lamp of weight W hangs from two identical cables, each making the same angle &alpha; with the '
  '<b>horizontal</b> (Fig. 4). By symmetry the two tensions are equal:</p>')
a(L45.lamp_two_cables('Fig. 4 &mdash; a lamp supported by two symmetric cables.', '&#945;'))
a('<ul><li><b>Horizontal axis:</b> the two horizontal components T cos &alpha; are equal and opposite, so they '
  'cancel each other.</li><li><b>Vertical axis:</b> the two vertical components together carry the weight.</li></ul>')
a('<div class="box formula"><div class="big">2 T sin &alpha; = W &nbsp;&nbsp;&#8658;&nbsp;&nbsp; T = W / ( 2 sin &alpha; )'
  '</div><div class="small">&alpha; = the angle between each cable and the horizontal</div></div>')
a('<table><tr><th>&alpha; (with the horizontal)</th><th>90&deg;</th><th>60&deg;</th><th>30&deg;</th><th>10&deg;</th>'
  '<th>5&deg;</th></tr><tr><td><b>T / W</b></td><td>0.5</td><td>0.58</td><td>1</td><td>2.9</td><td>5.7</td></tr></table>')
a(L45.sagging_wire('Fig. 5 &mdash; a wire fixed between two poles carrying a weight at its middle.'))
a('<div class="box warn"><span class="t">The sagging wire</span>If the wire sags more, the angle &alpha; with the '
  'horizontal increases, sin &alpha; increases and the tension <b>decreases</b>. If the wire is pulled flatter, '
  '&alpha; &#8594; 0 and T = W / (2 sin &alpha;) becomes very large. That is why a wire carrying a weight can never '
  'be made perfectly horizontal.</div>')

# ---------------- 5 ----------------
a('<h2><span class="num">5</span>A lamp held by a cable and a horizontal rope</h2>')
a('<p>A lamp hangs from a cable fixed to the ceiling and is held aside by a light horizontal rope fixed to a wall, '
  'so that the cable makes an angle &theta; with the <b>vertical</b> (Fig. 6). Three forces act on the lamp: the '
  'tension T in the cable, the pull P of the rope and the weight W.</p>')
a(L6.lamp_wall('Fig. 6 &mdash; three forces keep the lamp in equilibrium.', 'P', 'W = mg', '&#952;'))
a('<div class="box formula"><div class="big">vertical : T cos &theta; = W &nbsp;&nbsp;&nbsp; horizontal : T sin '
  '&theta; = P</div><div class="small">&theta; with the <b>vertical</b> &nbsp;|&nbsp; T = &#8730;( W&sup2; + '
  'P&sup2; ) &nbsp;|&nbsp; tan &theta; = P / W</div></div>')
a('<div class="box tip"><span class="t">Which component carries the weight?</span>Only the <b>vertical</b> component '
  'of the tension appears in the vertical equation. The rope is horizontal, so it has no vertical component and '
  'is balanced by the horizontal component of the tension alone.</div>')

# ---------------- 6 ----------------
a('<h2><span class="num">6</span>Two cables making different angles</h2>')
a('<p>If a sign hangs from two cables making <b>different</b> angles &alpha;<sub>1</sub> and &alpha;<sub>2</sub> '
  'with the horizontal (Fig. 7), the two tensions are <b>not</b> equal. We write the two equations and solve '
  'them together:</p>')
a(L6.sign_cables('Fig. 7 &mdash; a sign supported by two cables at different angles.', 30.0, 60.0, 'm'))
a('<div class="box formula" style="text-align:left"><b>horizontal :</b> &nbsp; T<sub>1</sub> cos &alpha;<sub>1</sub> '
  '= T<sub>2</sub> cos &alpha;<sub>2</sub><br><b>vertical :</b> &nbsp;&nbsp;&nbsp;&nbsp; T<sub>1</sub> sin '
  '&alpha;<sub>1</sub> + T<sub>2</sub> sin &alpha;<sub>2</sub> = W</div>')
a('<p>The cable that is <b>closer to the vertical</b> (the larger angle with the horizontal) carries the '
  '<b>larger</b> tension.</p>')

# ---------------- 7 ----------------
a('<h2><span class="num">7</span>A body hanging from two identical springs</h2>')
a('<p>A body hangs at rest from two identical light springs, each making an angle &theta; with the '
  '<b>vertical</b> (Fig. 8). Each spring pulls with the same force F, and the two vertical components carry the '
  'weight:</p>')
a(L6.two_springs('Fig. 8 &mdash; a body hanging from two identical springs.', '&#952;', mlab='m'))
a('<div class="box formula"><div class="big">2 F cos &theta; = W &nbsp;&nbsp;&nbsp; and &nbsp;&nbsp;&nbsp; '
  'F = k x</div><div class="small">&theta; with the <b>vertical</b> &nbsp;|&nbsp; k = spring constant (N/m) '
  '&nbsp;|&nbsp; x = extension of each spring</div></div>')

# ---------------- 8 ----------------
a('<h2><span class="num">8</span>How to solve an equilibrium problem</h2>')
a('<ol><li>Draw the body alone and mark <b>every</b> force acting on it (weight, tensions, normal force, pulls).</li>'
  '<li>Change the mass into a weight : W = m g.</li>'
  '<li>Resolve every inclined force into a horizontal and a vertical component.</li>'
  '<li>Write &Sigma;F<sub>x</sub> = 0 and &Sigma;F<sub>y</sub> = 0, and solve.</li></ol>')

a('<div class="key"><h3>&#9733; Key facts you must memorise</h3><ul>'
  '<li>Equilibrium : the body is at rest or moves with a constant velocity &#8658; <b>&Sigma;F = 0</b>.</li>'
  '<li>Apply the condition to each axis : <b>&Sigma;F<sub>x</sub> = 0</b> and <b>&Sigma;F<sub>y</sub> = 0</b>.</li>'
  '<li>Components : F<sub>x</sub> = F cos &theta; , F<sub>y</sub> = F sin &theta; (&theta; from the horizontal).</li>'
  '<li>Two symmetric cables : <b>T = W / (2 sin &alpha;)</b> ; the flatter the cables, the larger the tension.</li>'
  '<li>Cable + horizontal rope : T cos &theta; = W and T sin &theta; = P (&theta; from the vertical).</li>'
  '<li>A book on a table : F<sub>N</sub> = W ; the weight comes from the Earth, the normal force from the table.</li>'
  '</ul></div>')

a('<div class="box warn"><span class="t">Common mistakes</span><ul style="margin:3px 0 0">'
  '<li>Using the mass in kilograms as a force : always write W = m g first.</li>'
  '<li>Using sin instead of cos : check whether &theta; is measured from the horizontal or from the vertical.</li>'
  '<li>Writing T = W for a cable that is not vertical.</li>'
  '<li>Adding a horizontal force into the vertical equation.</li></ul></div>')

# ============================ SOLVED EXAMPLES ============================
a('<div class="pb"></div>')
a('<h2><span class="num">9</span>Solved examples</h2>')


def ex(n, title, fig, given, steps, ans):
    a('<div class="ex"><div class="h">Example ' + str(n) + ' &nbsp;&mdash;&nbsp; ' + title + '</div><div class="b">')
    if fig:
        a(fig)
    a('<div class="given"><b>Given:</b> ' + given + '</div>')
    a('<div class="sol"><span class="t">Solution</span>' + steps + '<br><span class="ans">' + ans + '</span></div>')
    a('</div></div>')


ex(1, 'a book on a table',
   L6.book_table('Fig. 9 &mdash; two identical books on a table.', True),
   'A book of mass 0.5 kg rests on a table. Find the normal force on it. A second identical book is then placed on '
   'top of it. Find the new normal force that the table exerts on the lower book, and the weight of the lower book.',
   '<div class="calc">one book :   F(N) = W = m g = 0.5 &times; 9.8 = 4.9 N\n'
   'two books :  the table supports both books :  F(N) = 2 m g = 2 &times; 4.9 = 9.8 N\n'
   'the weight of the lower book depends only on its own mass :  W = 4.9 N (unchanged)</div>',
   'F(N) : 4.9 N &#8594; 9.8 N ; the weight stays 4.9 N')

ex(2, 'the third force along one line',
   L6.three_forces('Fig. 10 &mdash; find the third force.', 'F&#8321; = 12 N', 'F&#8322; = 5 N'),
   'A body is in equilibrium under three forces along one vertical line : 12 N upwards, 5 N downwards and a third '
   'force F<sub>3</sub>. Find F<sub>3</sub>.',
   '<div class="calc">take upwards as positive :   &Sigma;F(y) = 0\n'
   '+ 12 &#8722; 5 + F&#8323; = 0   &#8658;   F&#8323; = &#8722; 7 N</div>'
   '<p>The minus sign means that F<sub>3</sub> points <b>downwards</b>.</p>', 'F&#8323; = 7 N downwards')

ex(3, 'a lamp on two symmetric cables',
   L45.lamp_two_cables('Fig. 11 &mdash; each cable makes 30&deg; with the horizontal.', '30&#176;'),
   'A lamp of mass 0.6 kg hangs from two identical cables, each making 30&deg; with the horizontal. Find the '
   'tension in each cable.',
   '<div class="calc">W = m g = 0.6 &times; 9.8 = 5.88 N\n'
   'horizontal : the two components T cos 30&deg; cancel\n'
   'vertical :   2 T sin 30&deg; = W   &#8658;   2 T &times; 0.5 = 5.88   &#8658;   T = 5.88 N</div>'
   '<p>At 30&deg; each cable carries a tension <b>equal to the whole weight</b>.</p>', 'T = 5.88 N')

ex(4, 'a cable and a horizontal rope',
   L6.lamp_wall('Fig. 12 &mdash; the rope pulls the lamp with P = 20 N.', 'P = 20 N', 'W = 39.2 N', '&#952;'),
   'A lamp of mass 4.0 kg hangs from a cable and is held aside by a horizontal rope whose tension is 20 N. '
   'Find the tension T in the cable and the angle &theta; that the cable makes with the vertical.',
   '<div class="calc">W = m g = 4.0 &times; 9.8 = 39.2 N\n'
   'vertical :   T cos &theta; = W = 39.2 N\n'
   'horizontal : T sin &theta; = P = 20 N\n'
   'T = &#8730;( 39.2&sup2; + 20&sup2; ) = &#8730;1936.6 = 44.0 N\n'
   'tan &theta; = P / W = 20 / 39.2 = 0.51   &#8658;   &theta; = 27&deg;</div>',
   'T = 44.0 N , &theta; = 27&deg; with the vertical')

ex(5, 'two cables at different angles',
   L6.sign_cables('Fig. 13 &mdash; a sign of mass 12 kg on two cables.', 30.0, 60.0, '12 kg'),
   'A sign of mass 12 kg hangs from two cables making 30&deg; and 60&deg; with the horizontal. Find the tension '
   'in each cable. (sin 30&deg; = cos 60&deg; = 0.5 , cos 30&deg; = sin 60&deg; = 0.866)',
   '<div class="calc">W = m g = 12 &times; 9.8 = 117.6 N\n'
   'horizontal :  T&#8321; cos 30&deg; = T&#8322; cos 60&deg;   &#8658;   0.866 T&#8321; = 0.5 T&#8322;   &#8658;   T&#8322; = 1.732 T&#8321;\n'
   'vertical :    T&#8321; sin 30&deg; + T&#8322; sin 60&deg; = 117.6\n'
   '              0.5 T&#8321; + ( 1.732 T&#8321; ) ( 0.866 ) = 117.6   &#8658;   2 T&#8321; = 117.6\n'
   '              T&#8321; = 58.8 N ,  T&#8322; = 1.732 &times; 58.8 = 101.8 N</div>'
   '<p>The steeper cable (60&deg;) carries the larger tension.</p>', 'T&#8321; = 58.8 N , T&#8322; = 101.8 N')

ex(6, 'two identical springs',
   L6.two_springs('Fig. 14 &mdash; each spring makes 37&deg; with the vertical.', '37&#176;', mlab='2 kg'),
   'A body of mass 2 kg hangs at rest from two identical springs, each making 37&deg; with the vertical. The spring '
   'constant of each spring is 100 N/m. Find the force in each spring and its extension. (cos 37&deg; = 0.8)',
   '<div class="calc">W = m g = 2 &times; 9.8 = 19.6 N\n'
   'vertical :  2 F cos 37&deg; = W   &#8658;   2 F &times; 0.8 = 19.6   &#8658;   F = 12.25 N\n'
   'extension :  x = F / k = 12.25 / 100 = 0.1225 m</div>',
   'F = 12.25 N , x = 12.25 cm')

# ============================ EXERCISES ============================
a('<div class="pb"></div>')
a('<h2><span class="num">10</span>Exercises</h2>')
a('<p>20 questions. Take g = 9.8 m/s&sup2;, sin 30&deg; = 0.5 , cos 30&deg; = 0.866 , sin 37&deg; = 0.6 , '
  'cos 37&deg; = 0.8 , sin 53&deg; = 0.8 , cos 53&deg; = 0.6 , sin 60&deg; = 0.866 , cos 60&deg; = 0.5. Show every '
  'step and give every answer with its unit.</p>')

QN = [0]
ANS = []


def q(text, ans, fig=None, ch=None, tag='Problem'):
    QN[0] += 1
    if ch:
        ans = ans + ') ' + ch['ABCD'.index(ans)]
    ANS.append((QN[0], ans))
    a('<div class="q"><span class="tag">' + tag + '</span><span class="n">Q' + str(QN[0]) + '</span>' + text)
    if fig:
        a(fig)
    if ch:
        one = any(len(c) > 40 for c in ch)
        a('<div class="ch' + (' one' if one else '') + '">' +
          ''.join('<div><b>' + L + ')</b> ' + c + '</div>' for L, c in zip('ABCD', ch)) + '</div>')
    else:
        a('<div class="wr"></div>')
    a('</div>')


q('A body is in a state of equilibrium when:', 'B', None,
  ['its velocity is always zero', 'it stays at rest or moves with a constant velocity',
   'its velocity changes continuously', 'no forces act on it'], 'MCQ')
q('The condition of equilibrium of a body is written mathematically as:', 'B', None,
  ['&Sigma;F = m g', '&Sigma;F = 0', '&Sigma;F = m a , where a &#8800; 0', '&Sigma;F = F&#8321; only'], 'MCQ')
q('A car moves along a straight road with a <b>constant velocity</b>. The resultant force acting on it is:', 'B',
  None, ['in the direction of motion', 'zero', 'opposite to the motion', 'equal to its weight'], 'MCQ')
q('A body is in equilibrium under three forces along one vertical line: 15 N upwards, 9 N downwards and a third '
  'force. The third force is:', 'B', L6.three_forces('Fig. 15', 'F&#8321; = 15 N', 'F&#8322; = 9 N'),
  ['6 N upwards', '6 N downwards', '24 N upwards', 'zero'], 'MCQ')
q('A book of mass 1.2 kg rests on a horizontal table. The normal force that the table exerts on the book is:', 'C',
  None, ['1.2 N', '9.8 N', '11.76 N', 'zero'], 'MCQ')
q('For the book of Q5, a second identical book is placed on top of it. <b>State</b> which force on the lower '
  'book changes and which stays the same, and give the <b>source</b> of each force.',
  'F(N) doubles to 23.52 N (from the table) ; the weight stays 11.76 N (from the Earth)', tag='Explain')
q('A lamp of mass 2 kg hangs from two identical cables, each making 30&deg; with the horizontal. The tension in each '
  'cable is:', 'D', L45.lamp_two_cables('Fig. 16', '30&#176;'), ['9.8 N', '39.2 N', '11.3 N', '19.6 N'], 'MCQ')
q('For the lamp of Q7, if the two cables are made <b>flatter</b> (the angle with the horizontal decreases) while the '
  'load stays the same, the tension in each cable:', 'A', None,
  ['increases', 'decreases', 'stays the same', 'becomes zero'], 'MCQ')
q('A sign of mass 5 kg hangs from two identical cables, each making 60&deg; with the horizontal. Find the tension '
  'in each cable.', 'T = 28.3 N')
q('A wire fixed between two poles carries a weight at its middle. <b>Explain</b> what happens to the tension in '
  'the wire if it is allowed to sag more, and why it can never be made perfectly horizontal.',
  'more sag &#8594; larger angle with the horizontal &#8594; smaller tension ; a flat wire needs an infinite tension',
  L45.sagging_wire('Fig. 17'), tag='Explain')
q('A lamp hangs from a cable fixed to the ceiling and is held aside by a horizontal rope. The <b>vertical</b> '
  'component of the tension in the cable is equal to:', 'B', L45.lamp_cable('Fig. 18', '&#952;'),
  ['zero', 'the weight of the lamp', 'the tension in the horizontal rope', 'half the weight of the lamp'], 'MCQ')
q('A lamp of mass 3 kg is held aside by a horizontal rope, so that its cable makes 37&deg; with the vertical. Find '
  'the tension in the cable and the tension in the rope.', 'T = 36.75 N , P = 22.05 N',
  L6.lamp_wall('Fig. 19', 'P = ?', 'W = 29.4 N', '37&#176;'))
q('A lamp of weight 24 N is held aside by a horizontal rope whose tension is 7 N. Find the tension in the cable and '
  'the angle it makes with the vertical.', 'T = 25 N , &theta; = 16.3&deg; with the vertical')
q('For a lamp hanging in equilibrium from two identical cables making the same angle with the horizontal, the two '
  'horizontal components of the tensions:', 'A', L6.cables_components('Fig. 20'),
  ['are equal and opposite, so they cancel each other', 'add together', 'balance the weight',
   'are each equal to the weight'], 'MCQ')
q('A sign hangs from two cables making <b>different</b> angles with the horizontal. The larger tension is in:', 'C',
  None, ['the flatter cable', 'neither &mdash; the two tensions are always equal',
         'the steeper cable (closer to the vertical)', 'the cable fixed farther from the sign'], 'MCQ')
q('A sign of mass 10 kg hangs from two cables making 37&deg; and 53&deg; with the horizontal. Find the tension in '
  'each cable.', 'T(37&deg;) = 58.8 N , T(53&deg;) = 78.4 N', L6.sign_cables('Fig. 21', 37.0, 53.0, '10 kg'))
q('A body of mass 2.5 kg hangs at rest from two identical springs, each making 37&deg; with the vertical. The '
  'weight of the body is:', 'B', L6.two_springs('Fig. 22', '37&#176;', mlab='2.5 kg'),
  ['2.5 N', '24.5 N', '12.25 N', '49 N'], 'MCQ')
q('For the body of Q17, the spring constant of each spring is 50 N/m. Find the force in each spring and its '
  'extension.', 'F = 15.3 N , x = 30.6 cm')
q('Two identical springs hold the same body. If the angle that each spring makes with the <b>vertical</b> is '
  'increased, the force in each spring:', 'A', None,
  ['increases', 'decreases', 'stays the same', 'becomes zero'], 'MCQ')
q('A lamp hangs from two cables making 30&deg; and 60&deg; with the horizontal. The tension in the 30&deg; cable '
  'is 20 N. Find the tension in the other cable and the weight of the lamp.',
  'T(60&deg;) = 34.6 N , W = 40 N', L6.sign_cables('Fig. 23', 30.0, 60.0, 'lamp'), tag='&#9733; HOTS')

# ============================ ANSWERS ============================
a('<h2><span class="num">11</span>Model answer &mdash; final answers only</h2>')
a('<div class="box note">Use this page to correct the exercises. Only the final answer is given, so the student must '
  'write every step of the working.</div>')
a('<table><tr><th style="width:7%">Q</th><th>Final answer</th><th style="width:7%">Q</th><th>Final answer</th></tr>')
for i in range(0, len(ANS), 2):
    a('<tr>' + ''.join('<td><b>%d</b></td><td>%s</td>' % (n, s) for n, s in ANS[i:i + 2]) + '</tr>')
a('</table>')

a('<div class="foot"><span>Equilibrium of Forces &mdash; Grade 11 Physics</span><span>&Sigma;F<sub>x</sub> = 0 '
  '&middot; &Sigma;F<sub>y</sub> = 0 &middot; T = W / (2 sin &alpha;)</span></div>')
a('</body></html>')

open('equilibrium.html', 'w', encoding='utf-8').write(''.join(H))
print('equilibrium.html written :', QN[0], 'questions')

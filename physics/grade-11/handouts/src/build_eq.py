# -*- coding: utf-8 -*-
"""Equilibrium of Forces - explanation + solved examples + exercises + final answers (Grade 11, English only)."""
import figs_eq as E
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
  '<div class="sub">Translational &amp; rotational equilibrium &middot; resolving forces &middot; cables &amp; ropes '
  '&middot; beams, levers &amp; seesaws</div></div>'
  '<div class="badge">Physics &mdash; Grade 11<br>Explanation &amp; Questions<br>g = 10 m/s&sup2;</div></div>')

# ---------------- 1 ----------------
a('<h2><span class="num">1</span>What does equilibrium mean?</h2>')
a('<p>A body is in <b>equilibrium</b> when the forces acting on it produce <b>no change</b> in its state of motion: '
  'it does not start moving (or keeps moving with a constant velocity), and it does not start rotating.</p>')
a('<table><tr><th>Type</th><th>What the body does</th><th>Condition</th></tr>'
  '<tr><td><b>Translational</b> equilibrium</td><td>at rest, or moving in a straight line with a <b>constant '
  'velocity</b></td><td>&Sigma;F = 0</td></tr>'
  '<tr><td><b>Rotational</b> equilibrium</td><td>not rotating, or rotating with a constant angular speed</td>'
  '<td>&Sigma;M = 0</td></tr>'
  '<tr><td><b>Static (complete)</b> equilibrium</td><td>completely at rest</td><td>&Sigma;F = 0 <b>and</b> '
  '&Sigma;M = 0</td></tr></table>')
a(L6.book_table('Fig. 1 &mdash; a book resting on a table: the weight is balanced by the normal force.'))
a('<div class="box note"><span class="t">Remember</span>Equilibrium does <b>not</b> mean &ldquo;no forces&rdquo;. '
  'Many forces may act on the body, but their <b>resultant</b> is zero and their <b>total moment</b> is zero.</div>')

# ---------------- 2 ----------------
a('<h2><span class="num">2</span>The first condition &mdash; the resultant force is zero</h2>')
a('<p>For translational equilibrium the vector sum of all the forces must vanish. In practice we resolve every '
  'force into a horizontal (x) and a vertical (y) component and apply the condition to each direction separately:</p>')
a('<div class="box formula"><div class="big">&Sigma;F<sub>x</sub> = 0 &nbsp;&nbsp; and &nbsp;&nbsp; '
  '&Sigma;F<sub>y</sub> = 0</div><div class="small">forces to the right = forces to the left &nbsp;|&nbsp; '
  'forces upwards = forces downwards</div></div>')
a('<p>A force F that makes an angle &theta; with the horizontal has the components</p>')
a('<div class="box formula"><div class="big">F<sub>x</sub> = F cos &theta; &nbsp;&nbsp;&nbsp; F<sub>y</sub> = F '
  'sin &theta;</div><div class="small">&theta; is measured from the <b>horizontal</b></div></div>')
a(L45.tension_components('Fig. 2 &mdash; a tension T resolved into a horizontal and a vertical component.'))
a('<div class="box tip"><span class="t">Three forces at one point</span>If three forces keep a point in equilibrium, '
  'then the resultant of <b>any two</b> of them is equal in magnitude and opposite in direction to the third one.</div>')
a(E.f_three_point())

# ---------------- 3 ----------------
a('<h2><span class="num">3</span>A weight hanging from two cables</h2>')
a('<p>A lamp of weight W hangs from the middle of two identical cables, each making an angle &theta; with the '
  '<b>horizontal</b> (Fig. 4). By symmetry the two tensions are equal. The horizontal components cancel, and the two '
  'vertical components together carry the weight:</p>')
a(L45.lamp_two_cables('Fig. 4 &mdash; a lamp supported by two symmetric cables.', '&#952;'))
a('<div class="box formula"><div class="big">2 T sin &theta; = W &nbsp;&nbsp;&#8658;&nbsp;&nbsp; T = W / ( 2 sin &theta; )'
  '</div><div class="small">&theta; = angle between each cable and the horizontal</div></div>')
a('<table><tr><th>&theta; (with the horizontal)</th><th>90&deg;</th><th>60&deg;</th><th>30&deg;</th><th>10&deg;</th>'
  '<th>5&deg;</th><th>1&deg;</th></tr><tr><td><b>T / W</b></td><td>0.5</td><td>0.58</td><td>1</td><td>2.9</td>'
  '<td>5.7</td><td>28.6</td></tr></table>')
a(L45.sagging_wire('Fig. 5 &mdash; the flatter the wire, the larger the tension.'))
a('<div class="box warn"><span class="t">Why can a stretched wire never be perfectly straight?</span>As &theta; '
  '&#8594; 0, sin &theta; &#8594; 0 and T = W / (2 sin &theta;) becomes enormous. A wire carrying any weight must '
  'therefore sag a little, however strongly it is pulled.</div>')

# ---------------- 4 ----------------
a('<h2><span class="num">4</span>A lamp pulled aside by a horizontal rope</h2>')
a('<p>A lamp hangs from a cable fixed to the ceiling and is pulled aside by a horizontal rope, so that the cable '
  'makes an angle &theta; with the <b>vertical</b> (Fig. 6). Three forces act on the lamp: the tension T, the '
  'horizontal pull P and the weight W.</p>')
a(L45.lamp_cable('Fig. 6 &mdash; three forces keep the lamp in equilibrium.', '&#952;'))
a('<div class="box formula"><div class="big">vertical : T cos &theta; = W &nbsp;&nbsp;&nbsp; horizontal : T sin '
  '&theta; = P</div><div class="small">&theta; = angle between the cable and the <b>vertical</b> &nbsp;|&nbsp; '
  'dividing : tan &theta; = P / W</div></div>')

# ---------------- 5 ----------------
a('<h2><span class="num">5</span>The second condition &mdash; the total moment is zero</h2>')
a('<p>A body can have zero resultant force and still <b>rotate</b> (two equal and opposite forces that do not act '
  'along the same line). For rotational equilibrium the total moment about <b>any</b> point must be zero:</p>')
a('<div class="box formula"><div class="big">&Sigma;M = 0 &nbsp;&nbsp;&#8658;&nbsp;&nbsp; sum of clockwise moments = '
  'sum of anticlockwise moments</div><div class="small">the moments are taken about the same point</div></div>')
a(E.f_seesaw('Fig. 7 &mdash; a balanced seesaw: the two moments about the pivot are equal and opposite.'))
a('<div class="box tip"><span class="t">Choosing the point</span>You may take moments about <b>any</b> point. '
  'Choose the point where an <b>unknown force</b> acts: its moment about that point is zero, so it disappears from '
  'the equation.</div>')
a('<div class="box note"><span class="t">The weight of a uniform body</span>The weight of a <b>uniform</b> rod, beam '
  'or plank acts at its <b>middle point</b> (its centre of gravity).</div>')

# ---------------- 6 ----------------
a('<h2><span class="num">6</span>Using both conditions &mdash; a beam on two supports</h2>')
a('<p>A uniform beam rests on two supports A and B and carries a load. The supports push the beam upwards with the '
  'reactions R<sub>1</sub> and R<sub>2</sub> (Fig. 8). Two equations give the two unknowns:</p>')
a(E.f_beam('Fig. 8 &mdash; a beam in complete equilibrium.'))
a('<div class="box formula" style="text-align:left"><b>1.</b> &Sigma;F<sub>y</sub> = 0 : &nbsp; R<sub>1</sub> + '
  'R<sub>2</sub> = load + weight of the beam<br><b>2.</b> &Sigma;M = 0 about A : &nbsp; R<sub>2</sub> &times; AB = '
  '(load &times; its distance from A) + (W &times; half the length)</div>')

# ---------------- 7 ----------------
a('<h2><span class="num">7</span>How to solve an equilibrium problem</h2>')
a('<ol><li>Draw the body alone and mark <b>every</b> force acting on it (weight, tensions, reactions, pushes, '
  'friction).</li><li>Resolve the inclined forces into horizontal and vertical components.</li>'
  '<li>Write &Sigma;F<sub>x</sub> = 0 and &Sigma;F<sub>y</sub> = 0.</li>'
  '<li>If the body can rotate, take moments about a point through which an unknown force passes and write '
  '&Sigma;M = 0.</li><li>Solve, and check the answer with the equation you did not use.</li></ol>')

a('<div class="key"><h3>&#9733; Key facts you must memorise</h3><ul>'
  '<li>Translational equilibrium : <b>&Sigma;F = 0</b> (at rest or constant velocity).</li>'
  '<li>Rotational equilibrium : <b>&Sigma;M = 0</b> (clockwise moments = anticlockwise moments).</li>'
  '<li>Components : F<sub>x</sub> = F cos &theta; , F<sub>y</sub> = F sin &theta; (&theta; from the horizontal).</li>'
  '<li>Two symmetric cables : <b>T = W / (2 sin &theta;)</b> ; the flatter the cables, the larger the tension.</li>'
  '<li>Three forces in equilibrium : any two have a resultant equal and opposite to the third.</li>'
  '<li>The weight of a uniform body acts at its middle.</li></ul></div>')

a('<div class="box warn"><span class="t">Common mistakes</span><ul style="margin:3px 0 0">'
  '<li>Forgetting the <b>weight of the beam or rod</b> itself.</li>'
  '<li>Using sin instead of cos: check whether &theta; is measured from the horizontal or from the vertical.</li>'
  '<li>Writing T = W for a cable that is not vertical.</li>'
  '<li>Taking moments about different points in the same equation.</li>'
  '<li>Forgetting to change grams to kilograms and centimetres to metres.</li></ul></div>')

# ============================ SOLVED EXAMPLES ============================
a('<div class="pb"></div>')
a('<h2><span class="num">8</span>Solved examples</h2>')


def ex(n, title, fig, given, steps, ans):
    a('<div class="ex"><div class="h">Example ' + str(n) + ' &nbsp;&mdash;&nbsp; ' + title + '</div><div class="b">')
    if fig:
        a(fig)
    a('<div class="given"><b>Given:</b> ' + given + '</div>')
    a('<div class="sol"><span class="t">Solution</span>' + steps + '<br><span class="ans">' + ans + '</span></div>')
    a('</div></div>')


ex(1, 'a lamp on two cables',
   L45.lamp_two_cables('Fig. 9 &mdash; each cable makes 30&deg; with the horizontal.', '30&#176;'),
   'A lamp of mass 0.6 kg hangs from two identical cables, each making 30&deg; with the horizontal. Find the '
   'tension in each cable.',
   '<div class="calc">W = m g = 0.6 &times; 10 = 6 N\n'
   'the horizontal components cancel ; vertically :  2 T sin 30&deg; = W\n'
   '2 T &times; 0.5 = 6   &#8658;   T = 6 N</div>'
   '<p>Notice that each cable carries a tension <b>equal to the whole weight</b> at 30&deg;.</p>', 'T = 6 N')

ex(2, 'a lamp pulled aside by a rope',
   L6.lamp_wall('Fig. 10 &mdash; the cable makes 37&deg; with the vertical.', 'P = ?', 'W = 40 N', '37&#176;'),
   'A lamp of weight 40 N is pulled aside by a horizontal rope until its cable makes 37&deg; with the vertical. '
   'Find the tension T in the cable and the pull P. (sin 37&deg; = 0.6 , cos 37&deg; = 0.8)',
   '<div class="calc">vertical :    T cos 37&deg; = W   &#8658;   T = 40 / 0.8 = 50 N\n'
   'horizontal :  P = T sin 37&deg; = 50 &times; 0.6 = 30 N</div>'
   '<p><b>Check:</b> tan 37&deg; = P / W = 30 / 40 = 0.75 &#10004;</p>', 'T = 50 N , P = 30 N')

ex(3, 'the third force',
   None,
   'Two forces act on a point: 30 N towards the east and 40 N towards the north (Fig. 3). Find the third force that '
   'keeps the point in equilibrium.',
   '<div class="calc">resultant of the two forces :  R = &#8730;( 30&#178; + 40&#178; ) = &#8730;2500 = 50 N\n'
   'direction of R :  tan &#945; = 40 / 30  &#8658;  &#945; = 53&deg; north of east\n'
   'the third force is equal and opposite to R</div>',
   'F&#8323; = 50 N , at 53&deg; south of west')

ex(4, 'a box pulled at an angle with a constant velocity',
   E.f_block_friction('Fig. 11 &mdash; the box moves with a constant velocity.'),
   'A box of mass 10 kg is pulled along a horizontal floor by a force of 50 N inclined at 37&deg; above the '
   'horizontal. The box moves with a <b>constant velocity</b>. Find the friction force and the normal force.',
   '<p>Constant velocity &#8658; translational equilibrium &#8658; &Sigma;F<sub>x</sub> = 0 and '
   '&Sigma;F<sub>y</sub> = 0.</p>'
   '<div class="calc">horizontal :  f = F cos 37&deg; = 50 &times; 0.8 = 40 N\n'
   'vertical :    N + F sin 37&deg; = W   &#8658;   N = 100 &#8722; 50 &times; 0.6 = 70 N</div>'
   '<p>The upward component of the pull makes the normal force <b>less</b> than the weight.</p>',
   'f = 40 N , N = 70 N')

ex(5, 'a balanced seesaw',
   E.f_seesaw('Fig. 12 &mdash; where must the heavier child sit?'),
   'A 30 kg child sits 2 m from the pivot of a uniform seesaw pivoted at its middle. Where must a 40 kg child sit, '
   'on the other side, to balance it?',
   '<div class="calc">about the pivot :  clockwise moments = anticlockwise moments\n'
   '( 30 &times; 10 ) &times; 2 = ( 40 &times; 10 ) &times; x\n'
   '600 = 400 x   &#8658;   x = 1.5 m</div>'
   '<p>The heavier child must sit <b>nearer</b> to the pivot.</p>', 'x = 1.5 m from the pivot')

ex(6, 'the reactions on a beam',
   E.f_beam('Fig. 13 &mdash; a uniform beam on two supports at its ends.'),
   'A uniform beam of length 4 m and weight 200 N rests on supports at its ends A and B. A load of 300 N is placed '
   '1 m from A. Find the reactions R<sub>1</sub> (at A) and R<sub>2</sub> (at B).',
   '<div class="calc">moments about A (R&#8321; disappears) :\n'
   'R&#8322; &times; 4 = ( 300 &times; 1 ) + ( 200 &times; 2 ) = 700   &#8658;   R&#8322; = 175 N\n'
   'vertical forces :  R&#8321; + R&#8322; = 300 + 200 = 500   &#8658;   R&#8321; = 325 N</div>'
   '<p><b>Check</b> with moments about B: R&#8321; &times; 4 = 300 &times; 3 + 200 &times; 2 = 1300 &#8658; '
   'R&#8321; = 325 N &#10004;</p>', 'R&#8321; = 325 N , R&#8322; = 175 N')

ex(7, 'finding the weight of a metre rule',
   E.f_rule('Fig. 14 &mdash; a uniform metre rule balanced on a knife-edge at the 40 cm mark.'),
   'A uniform metre rule balances horizontally on a knife-edge at the 40 cm mark when a weight of 0.6 N hangs at '
   'the 10 cm mark. Find the weight of the rule.',
   '<div class="calc">the weight of the rule acts at its middle (50 cm), 10 cm = 0.1 m to the right of the pivot\n'
   'the 0.6 N weight is 40 &#8722; 10 = 30 cm = 0.3 m to the left\n'
   'moments about the pivot :  0.6 &times; 0.3 = W &times; 0.1   &#8658;   W = 1.8 N</div>',
   'W = 1.8 N')

# ============================ EXERCISES ============================
a('<div class="pb"></div>')
a('<h2><span class="num">9</span>Exercises</h2>')
a('<p>20 questions. Take g = 10 m/s&sup2;, sin 37&deg; = 0.6 , cos 37&deg; = 0.8 , sin 30&deg; = 0.5 , cos 30&deg; '
  '= 0.866 , sin 45&deg; = 0.707. Show every step and give every answer with its unit.</p>')

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


q('A body is in <b>complete (static)</b> equilibrium when:', 'C',
  None, ['the resultant force on it is zero only', 'the total moment on it is zero only',
         'both the resultant force and the total moment are zero', 'no forces act on it'], 'MCQ')
q('A car moves along a straight road with a <b>constant velocity</b>. The resultant force acting on it is:', 'B',
  None, ['in the direction of motion', 'zero', 'opposite to the motion', 'equal to its weight'], 'MCQ')
q('Two forces of 8 N and 6 N act at right angles on a point. The magnitude of the third force that keeps the point '
  'in equilibrium is:', 'C', None, ['2 N', '14 N', '10 N', '48 N'], 'MCQ')
q('A lamp of mass 2 kg hangs from two identical cables, each making 30&deg; with the horizontal. The tension in each '
  'cable is:', 'D', L45.lamp_two_cables('Fig. 15', '30&#176;'), ['10 N', '40 N', '11.5 N', '20 N'], 'MCQ')
q('For the lamp of Q4, if the two cables are made <b>flatter</b> (the angle with the horizontal decreases), the '
  'tension in each cable:', 'A', None, ['increases', 'decreases', 'stays the same', 'becomes zero'], 'MCQ')
q('A sign of mass 5 kg hangs from two identical cables, each making 60&deg; with the horizontal. Find the tension '
  'in each cable. (sin 60&deg; = 0.866)', 'T = 28.9 N')
q('A lamp of weight 24 N is pulled aside by a horizontal force P until its cable makes 37&deg; with the vertical. '
  'Find the tension in the cable and the force P.', 'T = 30 N , P = 18 N',
  L6.lamp_wall('Fig. 16', 'P = ?', 'W = 24 N', '37&#176;'))
q('A box is pulled along a horizontal floor by a horizontal force of 20 N and moves with a constant velocity. The '
  'friction force on the box is:', 'B', None, ['zero', '20 N', 'more than 20 N', 'less than 20 N'], 'MCQ')
q('A box of mass 8 kg is pulled along a horizontal floor by a force of 40 N at 30&deg; above the horizontal, and '
  'moves with a constant velocity. Find the friction force and the normal force.',
  'f = 34.6 N , N = 60 N', E.f_block_friction('Fig. 17', 'F = 40 N', '30&#176;', '8 kg'))
q('A 25 kg child sits 2.4 m from the pivot of a uniform seesaw pivoted at its middle. A 30 kg child can balance it '
  'by sitting on the other side at a distance of:', 'A',
  E.f_seesaw('Fig. 18', '25 kg', '30 kg', '2.4 m', 'x = ?'), ['2 m', '2.88 m', '1.2 m', '2.4 m'], 'MCQ')
q('A uniform metre rule of weight 10 N is pivoted at the 40 cm mark. The weight that must hang at the 0 cm mark to '
  'keep the rule horizontal is:', 'B', None, ['10 N', '2.5 N', '4 N', '25 N'], 'MCQ')
q('A uniform beam of length 6 m and weight 300 N rests on two supports at its ends A and B. A load of 600 N is '
  'placed 2 m from A. Find the two reactions.', 'R(A) = 550 N , R(B) = 350 N',
  E.f_beam('Fig. 19', '6 m', '600 N', '2 m', '300 N', loadx=1 / 3.))
q('A uniform beam rests on two supports at its ends and carries a load <b>exactly at its middle</b>. The two '
  'reactions are:', 'C', None, ['zero', 'different', 'equal', 'each equal to the total weight'], 'MCQ')
q('Two forces act on a point: 12 N towards the east and 5 N towards the south. Find the magnitude and the direction '
  'of the third force that keeps the point in equilibrium.', '13 N , at 22.6&deg; north of west')
q('A picture of weight 14.1 N hangs from a nail by a string whose two halves each make 45&deg; with the horizontal. '
  'The tension in the string is:', 'A', None, ['10 N', '14.1 N', '7.05 N', '20 N'], 'MCQ')
q('A uniform metre rule of weight 1.5 N is pivoted at the 60 cm mark. At which mark must a weight of 1 N hang to '
  'keep the rule horizontal?', 'at the 75 cm mark')
q('A uniform plank of length 4 m and weight 400 N rests on two supports: one at its end A and one 1 m from the other '
  'end B. The reaction of the second support is:', 'D', None, ['200 N', '133.3 N', '400 N', '266.7 N'], 'MCQ')
q('A man of weight 700 N walks along a uniform plank of length 5 m and weight 300 N, supported at its end A and at '
  'C, 1 m from the other end B (Fig. 20). How far beyond C can the man walk before the plank starts to tip?',
  '0.64 m beyond C', E.f_plank_man('Fig. 20'), tag='&#9733; HOTS')
q('When a body is in equilibrium under several forces, the total moment of these forces is zero:', 'B', None,
  ['about its centre only', 'about any point', 'about the point of support only', 'only if all the forces are '
   'vertical'], 'MCQ')
q('A uniform horizontal rod of length 2 m and weight 40 N is hinged to a wall at one end and held by a vertical rope '
  'at the other end. A load of 60 N hangs 0.5 m from the wall. Find the tension in the rope and the force of the '
  'hinge.', 'T = 35 N , hinge force = 65 N upwards', E.f_hinged('Fig. 21'), tag='&#9733; HOTS')

# ============================ ANSWERS ============================
a('<h2><span class="num">10</span>Model answer &mdash; final answers only</h2>')
a('<div class="box note">Use this page to correct the exercises. Only the final answer is given, so the student must '
  'write every step of the working.</div>')
LETTERS = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
a('<table><tr><th style="width:7%">Q</th><th>Final answer</th><th style="width:7%">Q</th><th>Final answer</th></tr>')
for i in range(0, len(ANS), 2):
    a('<tr>' + ''.join('<td><b>%d</b></td><td>%s</td>' % (n, s) for n, s in ANS[i:i + 2]) + '</tr>')
a('</table>')

a('<div class="foot"><span>Equilibrium of Forces &mdash; Grade 11 Physics</span><span>&Sigma;F = 0 &middot; '
  '&Sigma;M = 0 &middot; T = W / (2 sin &theta;)</span></div>')
a('</body></html>')

open('equilibrium.html', 'w', encoding='utf-8').write(''.join(H))
print('equilibrium.html written :', QN[0], 'questions')

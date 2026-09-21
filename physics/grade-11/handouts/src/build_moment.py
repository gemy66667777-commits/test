# -*- coding: utf-8 -*-
import figs_moment as F
from css import CSS

H = []
a = H.append

a('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Moment of a Force</title>'
  '<style>' + CSS + '</style></head><body>')

# ---------------- header ----------------
a('<div class="head"><div><h1>Moment of a Force &nbsp;(Torque)</h1>'
  '<div class="sub">Moment about a point &middot; perpendicular &amp; inclined forces &middot; sign convention</div></div>'
  '<div class="badge">Physics &mdash; Grade 11<br>Revision Sheet<br>g is not needed here</div></div>')

# ---------------- intro ----------------
a('<h2><span class="num">1</span>The turning effect of a force</h2>')
a('<p>When you push a door, the door does not move forward &mdash; it <b>rotates</b> about its hinge. '
  'A force can therefore do two different things: it can <b>move</b> a body (translation), or it can <b>turn</b> '
  'it about a fixed point (rotation).</p>')
a('<p>Try the same push in three different places on the door (Fig. 1). The force is exactly the same, '
  'but the turning effect is completely different. Push very close to the hinge and the door hardly moves; '
  'push at the far edge and it swings easily.</p>')
a(F.f_door())
a('<div class="box note"><span class="t">Conclusion</span>The turning effect of a force depends on <b>two</b> things: '
  'the <b class="k">magnitude of the force</b> (F) and the <b class="purple">perpendicular distance</b> between the '
  'force and the axis of rotation (d). This combined quantity is called the <b>moment of the force</b>.'
  '<div class="ar" style="margin-top:4px">التأثير الدوراني بيعتمد على مقدار القوة وعلى المسافة العمودية من محور الدوران.</div></div>')

# ---------------- definition ----------------
a('<h2><span class="num">2</span>Definition of the moment of a force</h2>')
a('<p><b>Definition:</b> The moment of a force about a point is <i>the product of the force and the perpendicular '
  'distance between the point and the line of action of the force.</i></p>')
a(F.f_def())
a('<div class="box formula"><div class="big">M = F &times; L</div>'
  '<div class="small">M = moment (N&middot;m) &nbsp;|&nbsp; F = force (N) &nbsp;|&nbsp; '
  'L = perpendicular distance from the point to the line of action (m)</div></div>')
a('<table><tr><th>Quantity</th><th>Symbol</th><th>SI unit</th><th>Type</th></tr>'
  '<tr><td>Force</td><td>F</td><td>newton (N)</td><td>vector</td></tr>'
  '<tr><td>Moment arm</td><td>L or d</td><td>metre (m)</td><td>scalar (a distance)</td></tr>'
  '<tr><td>Moment of a force</td><td>M</td><td>newton &middot; metre (N&middot;m)</td><td><b>vector</b></td></tr></table>')
a('<div class="box warn"><span class="t">Careful</span>The unit of the moment is <b>N&middot;m</b>, and it is '
  '<b>never</b> written as a joule, although 1 N &times; 1 m also appears in the unit of work. '
  'Moment and work are completely different physical quantities.</div>')

# ---------------- moment arm ----------------
a('<h2><span class="num">3</span>The line of action and the moment arm</h2>')
a('<p>The <b>line of action</b> of a force is the straight line drawn through the force in the direction of the '
  'force, extended as far as you like in both directions. The <b class="purple">moment arm</b> <i>d</i> is the '
  '<b>shortest</b> (that is, the perpendicular) distance from the point O to this line.</p>')
a(F.f_arm())
a('<div class="box tip"><span class="t">How to find the moment arm</span>'
  '<b>1.</b> Extend the line of action of the force (dotted line).&nbsp; '
  '<b>2.</b> From the point O drop a perpendicular onto that line.&nbsp; '
  '<b>3.</b> The length of this perpendicular is <i>d</i>.'
  '<div class="ar" style="margin-top:4px">الذراع هو دايماً العمود المرسوم من النقطة على خط عمل القوة — مش المسافة المائلة.</div></div>')

# ---------------- sign convention ----------------
a('<h2><span class="num">4</span>Sign convention &mdash; the direction of the moment</h2>')
a('<p>The moment is a <b>vector</b> quantity, so it must be given a direction. In problems about one point we do '
  'not need arrows; we only need to say whether the force turns the body <b class="green">anticlockwise</b> or '
  '<b class="red">clockwise</b>:</p>')
a('<div class="box formula"><div class="big"><span style="color:#16a34a">anticlockwise &rarr; &nbsp;M is positive ( + )</span>'
  '<br><span style="color:#dc2626">clockwise &nbsp;&rarr; &nbsp;M is negative ( &minus; )</span></div></div>')
a(F.f_sign())
a('<p>Imagine holding the body at O and letting the force act alone: look at the direction in which the body '
  'starts to turn, then give the moment its sign.</p>')

# ---------------- zero moment ----------------
a('<h2><span class="num">5</span>When is the moment equal to zero?</h2>')
a('<p>Since <i>M = F &times; L</i>, the moment vanishes in two cases:</p>')
a('<ul><li><b>F = 0</b> &mdash; there is no force at all.</li>'
  '<li><b>L = 0</b> &mdash; the <b>line of action of the force passes through the point O</b>. '
  'This happens when the force is directed along the rod, or is applied at the axis itself.</li></ul>')
a(F.f_zero())
a('<div class="box note"><span class="t">Everyday check</span>Pushing a door exactly at its hinge, or pushing it '
  'along its own plane (edge-on), never opens it &mdash; the line of action passes through the hinge, so M = 0.</div>')

# ---------------- case 1 ----------------
a('<h2><span class="num">6</span>Case 1: the force is perpendicular to the rod</h2>')
a('<p>This is the simplest &mdash; and the most common &mdash; case. If the force is perpendicular '
  '(&perp;) to the rod, then the length of the rod <b>is itself</b> the moment arm.</p>')
a(F.f_perp_tilted())
a('<div class="box formula"><div class="big">M = F &times; L &nbsp;&nbsp;(&theta; = 90&deg;)</div>'
  '<div class="small">this gives the <b>largest possible moment</b> for a given force and a given length</div></div>')
a('<div class="box warn"><span class="t">Note</span>&ldquo;Perpendicular&rdquo; means perpendicular <b>to the rod</b>, '
  'not necessarily vertical. In Fig. 6 the rod is tilted, yet the force is still &perp; to it, so M = F L.</div>')

# ---------------- case 2 ----------------
a('<h2><span class="num">7</span>Case 2: the force is inclined at an angle &theta; to the rod</h2>')
a('<h3>Method 1 &mdash; resolve the force</h3>')
a('<p>Resolve F into two components: one <b class="blue">perpendicular to the rod</b> (F sin&theta;) and one '
  '<b class="green">along the rod</b> (F cos&theta;).</p>')
a(F.f_resolve())
a('<ul><li>The component <b class="blue">F sin &theta;</b> is perpendicular to the rod &rarr; it <b>turns</b> the rod. '
  'Its moment is (F sin&theta;) &times; L.</li>'
  '<li>The component <b class="green">F cos &theta;</b> lies along the rod, so its line of action passes through O '
  '&rarr; its moment is <b>zero</b>. It only pulls or pushes the rod.</li></ul>')
a('<h3>Method 2 &mdash; use the perpendicular distance</h3>')
a('<p>Instead of resolving the force, keep the force as it is and find the perpendicular distance from O to its '
  'line of action. From the right-angled triangle, that distance is <i>d</i> = L sin&theta;.</p>')
a(F.f_perpdist())
a('<div class="box formula"><div class="big">M = F &times; L &times; sin &theta;</div>'
  '<div class="small">&theta; = the angle between the force and the rod &nbsp;&middot;&nbsp; both methods give exactly the same result</div></div>')
a('<div class="ar box note">القانون واحد: <b>M = F L sin&theta;</b> — ولو القوة عمودية (&theta; = 90&deg;) تبقى sin&theta; = 1 ويرجع القانون M = F L.</div>')
a(F.f_compare())
a('<table><tr><th>&theta;</th><th>0&deg;</th><th>30&deg;</th><th>45&deg;</th><th>60&deg;</th><th>90&deg;</th><th>150&deg;</th><th>180&deg;</th></tr>'
  '<tr><td><b>sin &theta;</b></td><td>0</td><td>0.5</td><td>0.707</td><td>0.866</td><td>1</td><td>0.5</td><td>0</td></tr>'
  '<tr><td><b>M</b></td><td>0</td><td>0.5 F L</td><td>0.71 F L</td><td>0.87 F L</td><td><b>F L (max)</b></td><td>0.5 F L</td><td>0</td></tr></table>')

# ---------------- algebraic sum ----------------
a('<h2><span class="num">8</span>Several forces acting on the same body</h2>')
a('<p>When more than one force acts on a body, the total (resultant) moment about a point is the '
  '<b>algebraic sum</b> of the separate moments &mdash; each one taken with its own sign.</p>')
a('<div class="box formula"><div class="big">M<sub>net</sub> = &Sigma; M = M<sub>1</sub> + M<sub>2</sub> + M<sub>3</sub> + &hellip;</div>'
  '<div class="small">put a + sign for every anticlockwise moment and a &minus; sign for every clockwise moment</div></div>')
a(F.f_net())
a('<div class="calc">M<sub>net</sub> = (+20 &times; 2) + (&minus;30 &times; 1) + (+40 &times; 3)\n'
  '       = +40 &minus; 30 + 120 = <b>+130 N&middot;m</b>   (the + sign means: anticlockwise)</div>')
a('<div class="box tip"><span class="t">Reading the answer</span>The <b>size</b> of the number tells you how strong '
  'the turning effect is; the <b>sign</b> tells you the direction of the turn. Always finish your answer with the '
  'word <i>clockwise</i> or <i>anticlockwise</i>.</div>')

# ---------------- key facts ----------------
a('<div class="key"><h3>&#9733; Key facts you must memorise</h3><ul>'
  '<li><b>M = F &times; L</b> &nbsp;(force &perp; to the rod) &nbsp;&nbsp;|&nbsp;&nbsp; <b>M = F &times; L sin&theta;</b> &nbsp;(force inclined at &theta;)</li>'
  '<li>Unit: <b>N&middot;m</b>. Moment is a <b>vector</b> quantity.</li>'
  '<li><b>Anticlockwise = +</b> &nbsp;,&nbsp; <b>clockwise = &minus;</b></li>'
  '<li>M = 0 when the line of action of the force passes through the point.</li>'
  '<li>M is a <b>maximum</b> when &theta; = 90&deg; and <b>zero</b> when &theta; = 0&deg; or 180&deg;.</li>'
  '<li>Total moment about a point = algebraic sum of the moments (with signs).</li></ul></div>')

a('<div class="box warn"><span class="t">Common mistakes</span><ul style="margin:3px 0 0">'
  '<li>Using the slanted distance instead of the <b>perpendicular</b> distance (forgetting sin&theta;).</li>'
  '<li>Using cos&theta; instead of sin&theta;. Remember: the component that <b>turns</b> the rod is the perpendicular one.</li>'
  '<li>Leaving the length in centimetres: 20 cm = <b>0.2 m</b>, not 20.</li>'
  '<li>Adding moments without their signs.</li>'
  '<li>Giving the answer as a number only, with no direction.</li></ul>'
  '<div class="ar" style="margin-top:4px">حوّل السنتيمتر لمتر، وخد بالك من الإشارة، واكتب الاتجاه في الإجابة النهائية.</div></div>')

# ============================ SOLVED EXAMPLES ============================
a('<div class="pb"></div>')
a('<h2><span class="num">9</span>Solved examples</h2>')


def ex(n, title, fig, given, steps, ans):
    a('<div class="ex"><div class="h">Example ' + str(n) + ' &nbsp;&mdash;&nbsp; ' + title + '</div><div class="b">')
    a(fig)
    a('<div class="given"><b>Given:</b> ' + given + '</div>')
    a('<div class="sol"><span class="t">Solution</span>' + steps + '<br><span class="ans">' + ans + '</span></div>')
    a('</div></div>')


ex(1, 'a perpendicular force (spanner)',
   F.spanner('Fig. 11 &mdash; the force is perpendicular to the handle of the spanner.', 'L = 20 cm', 'F = 50 N'),
   'F = 50 N perpendicular to the spanner, L = 20 cm. Find the moment about the centre of the nut.',
   '<p>The force is &perp; to the handle, so the moment arm is the length itself. First change cm into m:</p>'
   '<div class="calc">L = 20 cm = 0.20 m\nM = F &times; L = 50 &times; 0.20 = 10 N&middot;m\n'
   'The spanner turns clockwise  &rarr;  the sign is negative.</div>',
   'M = &minus; 10 N&middot;m &nbsp;(10 N&middot;m clockwise)')

ex(2, 'an inclined force on a rod',
   F.rod_fig('Fig. 12 &mdash; the force makes 30&deg; with the rod.', 'L = 2 m', 'F = 100 N', 30, maxw=420),
   'A rod OA of length 2 m is hinged at O. A force of 100 N acts at A at 30&deg; to the rod.',
   '<div class="calc">M = F &times; L &times; sin &theta;\nM = 100 &times; 2 &times; sin 30&deg;\n'
   'M = 100 &times; 2 &times; 0.5 = 100 N&middot;m\nThe rod turns anticlockwise  &rarr;  positive.</div>'
   '<p><b>Check with method 1:</b> F sin&theta; = 100 &times; 0.5 = 50 N, and 50 &times; 2 = 100 N&middot;m. Same answer.</p>',
   'M = + 100 N&middot;m &nbsp;(anticlockwise)')

ex(3, 'pushing a door at an angle',
   F.door_top('Fig. 13 &mdash; the push is not perpendicular to the door.', 'width = 0.8 m', 'F = 40 N', 60),
   'A door of width 0.8 m is pushed at its outer edge with a force of 40 N making 60&deg; with the door.',
   '<div class="calc">M = F L sin &theta; = 40 &times; 0.8 &times; sin 60&deg;\n'
   'M = 40 &times; 0.8 &times; 0.866 = 27.7 N&middot;m</div>'
   '<p>If the same force were applied perpendicular to the door, the moment would be 40 &times; 0.8 = '
   '<b>32 N&middot;m</b> &mdash; that is why we always push a door perpendicular to its surface.</p>',
   'M = 27.7 N&middot;m &nbsp;(clockwise in the figure)')

ex(4, 'the net moment of three forces',
   F.bar_forces('Fig. 14 &mdash; three forces act on the same bar.',
                [(-2, '25 N', 'up'), (1.5, '40 N', 'down'), (2.5, '20 N', 'up')]),
   'Find the resultant moment about O for the bar shown in Fig. 14.',
   '<p>Take each force on its own and decide its sense of rotation about O:</p>'
   '<div class="calc">25 N up, 2 m to the LEFT    &rarr; clockwise        &rarr; M&#8321; = &minus; 25 &times; 2   = &minus; 50 N&middot;m\n'
   '40 N down, 1.5 m to the RIGHT &rarr; clockwise        &rarr; M&#8322; = &minus; 40 &times; 1.5 = &minus; 60 N&middot;m\n'
   '20 N up, 2.5 m to the RIGHT   &rarr; anticlockwise    &rarr; M&#8323; = + 20 &times; 2.5 = + 50 N&middot;m\n\n'
   'M(net) = &minus;50 &minus; 60 + 50 = &minus; 60 N&middot;m</div>',
   'M<sub>net</sub> = &minus; 60 N&middot;m &nbsp;(60 N&middot;m clockwise)')

ex(5, 'a tangential force on a wheel',
   F.wheel('Fig. 15 &mdash; a force tangent to the rim is perpendicular to the radius.', 'r = 0.3 m', 'F = 25 N'),
   'A force of 25 N acts at the rim of a wheel of radius 0.3 m, along the tangent.',
   '<p>A tangent is always perpendicular to the radius at the point of contact, so &theta; = 90&deg; and the '
   'moment arm is the radius itself.</p>'
   '<div class="calc">M = F &times; r = 25 &times; 0.3 = 7.5 N&middot;m   (clockwise)</div>',
   'M = &minus; 7.5 N&middot;m &nbsp;(7.5 N&middot;m clockwise)')

ex(6, 'finding the force (an inverse problem)',
   F.two_panel('Fig. 16 &mdash; the same moment is required in two different situations.',
               90, '(a)  F is &perp; to the rod', 30, '(b)  F is at 30&deg; to the rod'),
   'A moment of 48 N&middot;m is required about O, and the rod is 1.6 m long. Find the force needed '
   '(a) when it is perpendicular to the rod, (b) when it makes 30&deg; with the rod.',
   '<div class="calc">(a)  M = F L          &rarr;  F = M / L = 48 / 1.6 = 30 N\n\n'
   '(b)  M = F L sin&theta;     &rarr;  F = M / (L sin&theta;)\n'
   '     F = 48 / (1.6 &times; sin 30&deg;) = 48 / (1.6 &times; 0.5) = 48 / 0.8 = 60 N</div>'
   '<p>The inclined force must be <b>twice</b> as large to produce the same turning effect.</p>',
   '(a) F = 30 N &nbsp;&nbsp;|&nbsp;&nbsp; (b) F = 60 N')

ex(7, 'an obtuse angle',
   F.f_ex7(),
   'A force of 80 N acts at the end A of a rod OA = 1.2 m, making an angle of 150&deg; with the rod.',
   '<div class="calc">M = F L sin &theta; = 80 &times; 1.2 &times; sin 150&deg;\n'
   'sin 150&deg; = sin (180&deg; &minus; 150&deg;) = sin 30&deg; = 0.5\n'
   'M = 80 &times; 1.2 &times; 0.5 = 48 N&middot;m</div>'
   '<p><b>Check:</b> the perpendicular distance is d = L sin150&deg; = 1.2 &times; 0.5 = 0.6 m, '
   'and M = F &times; d = 80 &times; 0.6 = 48 N&middot;m.</p>',
   'M = + 48 N&middot;m &nbsp;(anticlockwise)')

# ============================ EXERCISES ============================
a('<div class="pb"></div>')
a('<h2><span class="num">10</span>Exercises</h2>')
a('<p>18 questions. Give every answer with its <b>unit</b>, its <b>sign</b> and the <b>sense of rotation</b>. '
  'Take the anticlockwise sense as positive.</p>')

QN = [0]


def q(text, fig=None):
    QN[0] += 1
    a('<div class="q"><span class="n">Q' + str(QN[0]) + '</span>' + text)
    if fig:
        a(fig)
    a('</div>')


q('A force of 30 N acts at the end A of a rod OA, perpendicular to the rod. If OA = 0.6 m, find the moment of '
  'the force about O.',
  F.rod_fig('Fig. 18', 'L = 0.6 m', 'F = 30 N', -90, maxw=380))
q('A spanner of length 15 cm is used to tighten a nut. What force, applied perpendicular to the spanner, '
  'produces a moment of 12 N&middot;m about the nut?',
  F.spanner('Fig. 19', 'L = 15 cm', 'F = ?', 390))
q('A force of 60 N acts at the end of a rod of length 1.4 m, making an angle of 45&deg; with the rod. '
  'Find the moment of this force about the hinge O.',
  F.rod_fig('Fig. 20', 'L = 1.4 m', 'F = 60 N', 45, maxw=380))
q('A door of width 0.9 m is pushed at its edge by a force of 25 N inclined at 30&deg; to the door. '
  'Find the moment about the hinge, and state how much larger the moment would be if the force were perpendicular.',
  F.door_top('Fig. 21', 'width = 0.9 m', 'F = 25 N', 30, 400))
q('Find the resultant moment about O of the two forces acting on the bar.',
  F.bar_forces('Fig. 22', [(-1.5, '30 N', 'down'), (2, '50 N', 'down')], 430))
q('Find the resultant moment about O of the three forces acting on the bar, and state its direction.',
  F.bar_forces('Fig. 23', [(-2, '40 N', 'up'), (1, '20 N', 'down'), (3, '30 N', 'up')], 450))
q('A force of 70 N is applied at the end A of the rod OA, directed <b>along</b> the rod as shown. '
  'Find its moment about O and explain your answer.',
  F.f_along_rod())
q('A force of 40 N acts along the tangent at the rim of a wheel of radius 25 cm. Find the moment of the force '
  'about the centre of the wheel.',
  F.wheel('Fig. 25', 'r = 25 cm', 'F = 40 N', 370))
q('The same force of 40 N acts at the end of the same rod (L = 1 m) in the two positions shown. '
  'Find the moment in each case, then find the ratio M<sub>a</sub> : M<sub>b</sub>.',
  F.two_panel('Fig. 26', 90, '(a)  F &perp; to the rod', 30, '(b)  F at 30&deg; to the rod', 450))
q('A force of 50 N acts at the end of a rod of length 1.2 m and produces a moment of 30 N&middot;m about O. '
  'Find the angle &theta; between the force and the rod.',
  F.rod_fig('Fig. 27', 'L = 1.2 m', 'F = 50 N', 55, '&theta; = ?', maxw=380))

q('A force of 120 N acts at the end A of a rod OA of length 0.5 m, perpendicular to the rod as shown. '
  'Find the moment of the force about O.',
  F.rod_fig('Fig. 28', 'L = 0.5 m', 'F = 120 N', 90, maxw=380))
q('Find the resultant moment about O of the two forces acting on the bar, and state its sense of rotation.',
  F.bar_forces('Fig. 29', [(-1, '50 N', 'down'), (2, '25 N', 'up')], 430))
q('A force of 100 N acts at the end of a rod of length 1.5 m, making an angle of 60&deg; with the rod. '
  'Find the moment of the force about the hinge O.',
  F.rod_fig('Fig. 30', 'L = 1.5 m', 'F = 100 N', 60, maxw=380))
q('A force of 90 N acting perpendicular to a rod produces a moment of 36 N&middot;m about the hinge. '
  'Find the length of the rod.')
q('A door can be pushed in two ways: (i) with a force of 50 N perpendicular to the door at a distance of 0.6 m '
  'from the hinge, or (ii) with a force of 30 N perpendicular to the door at a distance of 1.0 m from the hinge. '
  'Calculate the moment in each case and say which way opens the door more easily.')
q('A force of 15 N acts along the tangent at the rim of a wheel of radius 0.4 m. Find the moment of the force '
  'about the centre of the wheel.',
  F.wheel('Fig. 31', 'r = 0.4 m', 'F = 15 N', 370))
q('A force of 80 N acts at the end of a rod of length 2 m, making an angle of 120&deg; with the rod. '
  'Find the moment of the force about O. <i>(Remember: sin 120&deg; = sin 60&deg;.)</i>',
  F.rod_fig('Fig. 32', 'L = 2 m', 'F = 80 N', 120, maxw=400))
q('Four forces act on the bar shown. Find the resultant moment about O and state whether the bar turns '
  'clockwise or anticlockwise.',
  F.bar_forces('Fig. 33', [(-3, '20 N', 'up'), (-1, '30 N', 'down'), (1.5, '40 N', 'down'), (2, '10 N', 'up')], 470))

# ============================ ANSWERS ============================
a('<h2><span class="num">11</span>Model answer &mdash; final answers only</h2>')
a('<div class="box note">Use this page to correct the exercises. Only the final answer is given, so the student '
  'must write every step of the working by himself.</div>')
rows = [
    ('1', '&minus; 18 N&middot;m &nbsp;(clockwise)'), ('2', '80 N'),
    ('3', '+ 59.4 N&middot;m &nbsp;(anticlockwise)'),
    ('4', '11.25 N&middot;m ; perpendicular force gives 22.5 N&middot;m (twice as large)'),
    ('5', '&minus; 55 N&middot;m &nbsp;(clockwise)'), ('6', '&minus; 10 N&middot;m &nbsp;(clockwise)'),
    ('7', 'M = 0'), ('8', '10 N&middot;m'),
    ('9', 'M<sub>a</sub> = 40 N&middot;m , M<sub>b</sub> = 20 N&middot;m , ratio = 2 : 1'), ('10', '&theta; = 30&deg;'),
    ('11', '+ 60 N&middot;m &nbsp;(anticlockwise)'), ('12', '+ 100 N&middot;m &nbsp;(anticlockwise)'),
    ('13', '+ 129.9 N&middot;m &nbsp;(anticlockwise)'), ('14', 'L = 0.4 m'),
    ('15', '(i) 30 N&middot;m &nbsp;,&nbsp; (ii) 30 N&middot;m &mdash; the two ways are equally easy'), ('16', '6 N&middot;m'),
    ('17', '+ 138.6 N&middot;m &nbsp;(anticlockwise)'), ('18', '&minus; 70 N&middot;m &nbsp;(clockwise)'),
]
a('<table><tr><th style="width:7%">Q</th><th>Final answer</th><th style="width:7%">Q</th><th>Final answer</th></tr>')
for i in range(0, len(rows), 2):
    a('<tr><td><b>' + rows[i][0] + '</b></td><td>' + rows[i][1] + '</td><td><b>' + rows[i + 1][0] + '</b></td><td>'
      + rows[i + 1][1] + '</td></tr>')
a('</table>')

a('<div class="foot"><span>Moment of a Force &mdash; Grade 11 Physics</span><span>M = F L sin &theta;  &middot;  '
  'anticlockwise ( + ) &middot; clockwise ( &minus; )</span></div>')
a('</body></html>')

open('moment.html', 'w', encoding='utf-8').write(''.join(H))
print('moment.html written')

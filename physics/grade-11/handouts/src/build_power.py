# -*- coding: utf-8 -*-
"""Power and Efficiency (lesson 1-6) - explanation + solved examples + exercises + step-by-step model answer.
Grade 11, English only. Follows the ideas of lesson 1-6 in the assessments book and develops them."""
import figs_l6 as L6
import figs_power as P
from css import CSS
from docbase import WM64

H = []
a = H.append

a('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Power and Efficiency</title>'
  '<style>' + CSS + """
body { background-image:url("data:image/svg+xml;base64,""" + WM64 + """"); background-repeat:repeat; }
.ch { grid-template-columns:1fr 1fr; }
.ch.one { grid-template-columns:1fr; }
.tag { float:right; font-size:8.5pt; color:#64748b; border:1px solid #cbd5e1; border-radius:5px; padding:1px 7px;
       background:#f8fafc; }
.tag.hots { color:#92400e; background:#fef3c7; border-color:#f59e0b; font-weight:700; }
.q.hard { border-left-color:#f59e0b; }
.wr { border-top:1.4px dashed #cbd5e1; height:16mm; margin-top:8px; }
.sol2 { border:1.2px solid #cbd5e1; border-left:4.5px solid #16a34a; border-radius:0 8px 8px 0;
        background:rgba(255,255,255,.9); padding:5px 11px 6px; margin:7px 0; break-inside:avoid; }
.sol2 .sn { display:inline-block; background:#16a34a; color:#fff; border-radius:5px; padding:1px 8px;
        font-weight:700; font-size:9.5pt; margin-right:7px; }
.sol2 .hd { font-size:9.6pt; color:#475569; font-weight:700; }
.sol2 pre { font-family:"Liberation Mono","DejaVu Sans Mono",monospace; font-size:9.3pt; line-height:1.5;
        margin:4px 0 0; white-space:pre-wrap; color:#0f172a; }
.sol2 .fa { display:inline-block; margin-top:3px; color:#14532d; font-weight:700; background:#dcfce7;
        border:1.3px solid #16a34a; border-radius:6px; padding:1px 9px; font-size:9.6pt; }
</style></head><body>""")

# ---------------- header ----------------
a('<div class="head"><div><h1>Power and Efficiency</h1>'
  '<div class="sub">Lesson 1&ndash;6 &middot; the rate of doing work &middot; P = &Delta;W / &Delta;t &middot; '
  'P = F v cos &theta; &middot; the efficiency of a machine</div></div>'
  '<div class="badge">Mr. Gemy<br>Physics &mdash; Grade 11<br>g = 9.8 m/s&sup2;</div></div>')

# ---------------- 1 ----------------
a('<h2><span class="num">1</span>What is power?</h2>')
a('<p><b>Power</b> is a measure of the <b>rate</b> of doing work, or the rate of transferring energy. It tells us '
  '<i>how fast</i> the work is done, not <i>how much</i> work is done.</p>')
a('<div class="box formula"><div class="big">P = &Delta;W / &Delta;t</div>'
  '<div class="small">P = average power &nbsp;|&nbsp; &Delta;W = work done (J) &nbsp;|&nbsp; &Delta;t = time taken (s)'
  '</div></div>')
a('<table><tr><th>Quantity</th><th>Symbol</th><th>SI unit</th></tr>'
  '<tr><td>work / energy</td><td>W</td><td>joule (J)</td></tr>'
  '<tr><td>power</td><td>P</td><td><b>watt (W)</b> = J / s</td></tr></table>')
a('<div class="box note"><span class="t">Remember</span>1 kW = 1000 W. A power of 1 W means that 1 J of work is '
  'done (or 1 J of energy is transferred) every second.</div>')

# ---------------- 2 ----------------
a('<h2><span class="num">2</span>The power needed to raise a load</h2>')
a('<p>To raise a load of mass m through a height h at a steady speed, the work done against its weight is</p>')
a('<div class="box formula"><div class="big">W = m g h &nbsp;&nbsp;&#8658;&nbsp;&nbsp; P = m g h / t</div>'
  '<div class="small">the same load raised to the same height always needs the same work</div></div>')
a(L6.two_lifts('Fig. 1 &mdash; two lifts raise the same load to the same height in different times.'))
a('<p>In Fig. 1 both lifts do the <b>same useful work</b> (same m, same h). Lift B finishes in half the time, so its '
  'power is <b>twice</b> as large. A faster machine is more <b>powerful</b>; it does not do more work.</p>')

# ---------------- 3 ----------------
a('<h2><span class="num">3</span>The power of a force acting on a moving body</h2>')
a('<p>If a constant force F acts on a body moving with a velocity v, and the force makes an angle &theta; with the '
  'direction of motion (Fig. 2), only the component F cos &theta; along the motion does work. The power of the '
  'force is</p>')
a(L6.block_force_angle('Fig. 2 &mdash; a force at an angle &theta; to the direction of motion.'))
a('<div class="box formula"><div class="big">P = F v cos &theta;</div>'
  '<div class="small">&theta; = the angle between the force and the direction of motion</div></div>')
a('<table><tr><th>&theta;</th><th>0&deg;</th><th>37&deg;</th><th>60&deg;</th><th>90&deg;</th></tr>'
  '<tr><td><b>P</b></td><td>F v (largest)</td><td>0.8 F v</td><td>0.5 F v</td><td>zero</td></tr></table>')
a('<div class="box tip"><span class="t">Raising a load at a constant speed</span>The pulling force equals the weight '
  '(F = m g) and acts along the motion (&theta; = 0), so P = m g v.</div>')
a(P.motor_lift('Fig. 3 &mdash; a motor raises a load at a constant speed.'))

# ---------------- 4 ----------------
a('<h2><span class="num">4</span>Reading a work&ndash;time graph</h2>')
a('<p>On a graph of the work done W against the time t, the <b>slope</b> is &Delta;W / &Delta;t, which is the '
  '<b>power</b>. The steeper line belongs to the more powerful machine (Fig. 4).</p>')
a(P.wt_graph('Fig. 4 &mdash; the slope of a W&ndash;t line is the power.'))

# ---------------- 5 ----------------
a('<h2><span class="num">5</span>Efficiency</h2>')
a('<p>No real machine turns all the energy it receives into useful work. Part of the input is always wasted, mostly '
  'as heat (Fig. 5). The <b>efficiency</b> &eta; compares the useful output with the total input:</p>')
a('<div class="box formula"><div class="big">&eta; = ( useful output / total input ) &times; 100 %</div>'
  '<div class="small">use energies (J) or powers (W) &mdash; both give the same efficiency</div></div>')
a(P.energy_flow('Fig. 5 &mdash; the input energy splits into a useful part and a wasted part.'))
a('<ul><li>useful output = &eta; &times; input</li><li>input = useful output / &eta;</li>'
  '<li>wasted energy = input &#8722; useful output</li></ul>')
a('<div class="box warn"><span class="t">An efficiency above 100 % is impossible</span>The useful output can never be '
  'larger than the input, because energy cannot be created. Any answer above 100 % means a mistake.</div>')

a('<div class="key"><h3>&#9733; Key facts you must memorise</h3><ul>'
  '<li>Power = the rate of doing work or of transferring energy : <b>P = &Delta;W / &Delta;t</b>.</li>'
  '<li>Unit : <b>watt (W) = J/s</b> ; 1 kW = 1000 W.</li>'
  '<li>Raising a load : W = m g h ; at a constant speed P = m g v.</li>'
  '<li>A force on a moving body : <b>P = F v cos &theta;</b> ; it is zero when &theta; = 90&deg;.</li>'
  '<li>Efficiency : <b>&eta; = useful output / input</b> (energies or powers), always less than 100 %.</li>'
  '<li>The slope of a W&ndash;t graph is the power.</li></ul></div>')

a('<div class="box warn"><span class="t">Common mistakes</span><ul style="margin:3px 0 0">'
  '<li>Thinking that a more powerful machine does more work &mdash; it does the same work faster.</li>'
  '<li>Leaving the time in minutes : 2 min = 120 s.</li>'
  '<li>Using the mass instead of the weight : W = m g h, not m h.</li>'
  '<li>Using sin &theta; instead of cos &theta; in P = F v cos &theta;.</li>'
  '<li>Writing the efficiency as input / output (it would be more than 100 %).</li></ul></div>')

# ============================ SOLVED EXAMPLES ============================
a('<div class="pb"></div>')
a('<h2><span class="num">6</span>Solved examples</h2>')


def ex(n, title, fig, given, steps, ans):
    a('<div class="ex"><div class="h">Example ' + str(n) + ' &nbsp;&mdash;&nbsp; ' + title + '</div><div class="b">')
    if fig:
        a(fig)
    a('<div class="given"><b>Given:</b> ' + given + '</div>')
    a('<div class="sol"><span class="t">Solution</span>' + steps + '<br><span class="ans">' + ans + '</span></div>')
    a('</div></div>')


ex(1, 'two lifts', None,
   'Lift A and lift B each raise a load of 600 kg through 9.0 m (Fig. 1). Lift A takes 24 s and lift B takes '
   '12 s. Find the useful work done by each lift and the power of each.',
   '<div class="calc">useful work (the same for both) :  W = m g h = 600 &times; 9.8 &times; 9.0 = 52 920 J\n'
   'lift A :  P = W / t = 52 920 / 24 = 2205 W\n'
   'lift B :  P = W / t = 52 920 / 12 = 4410 W</div>'
   '<p>Same work, but lift B has <b>double</b> the power because it takes half the time.</p>',
   'W = 52 920 J for both ; P(A) = 2205 W , P(B) = 4410 W')

ex(2, 'a force at an angle', None,
   'A force of 50 N pulls a box that moves at a constant speed of 4 m/s. The force makes 60&deg; with the direction '
   'of motion. Find the power of the force. (cos 60&deg; = 0.5)',
   '<div class="calc">P = F v cos &theta; = 50 &times; 4 &times; cos 60&deg; = 50 &times; 4 &times; 0.5 = 100 W</div>'
   '<p>If the same force acted along the motion (&theta; = 0), the power would be 50 &times; 4 = 200 W.</p>',
   'P = 100 W')

ex(3, 'efficiency with energies', P.energy_flow('Fig. 6 &mdash; a machine of efficiency 40 %.', 'input 250 J',
                                                 'useful 100 J', 'wasted 150 J', 0.4),
   'A machine has an efficiency of 40 %. The total input energy is 250 J. Find the useful output energy and the '
   'wasted energy.',
   '<div class="calc">useful output = &eta; &times; input = 0.40 &times; 250 = 100 J\n'
   'wasted energy = input &#8722; useful = 250 &#8722; 100 = 150 J</div>', 'useful = 100 J , wasted = 150 J')

ex(4, 'efficiency with powers', None,
   'An electric water heater receives an electric power of 2400 W and produces a useful thermal power of 2040 W. '
   'Find its efficiency and the energy wasted in 10 minutes.',
   '<div class="calc">&eta; = useful power / input power = 2040 / 2400 = 0.85 = 85 %\n'
   'wasted power = 2400 &#8722; 2040 = 360 W\n'
   'wasted energy in 10 min :  360 &times; ( 10 &times; 60 ) = 216 000 J</div>',
   '&eta; = 85 % , wasted energy = 2.16 &times; 10<sup>5</sup> J')

ex(5, 'a motor raising a load at a constant speed',
   P.motor_lift('Fig. 7 &mdash; the motor takes 1400 W from the mains.', '200 kg', 'v = 0.5 m/s'),
   'An electric motor raises a load of 200 kg at a constant speed of 0.5 m/s. The motor takes an electric power '
   'of 1400 W. Find the useful power and the efficiency of the motor.',
   '<div class="calc">constant speed &#8658; the pull equals the weight : F = m g\n'
   'useful power :  P = m g v = 200 &times; 9.8 &times; 0.5 = 980 W\n'
   '&eta; = 980 / 1400 = 0.70 = 70 %</div>', 'P(useful) = 980 W , &eta; = 70 %')

ex(6, 'comparing two machines from a graph', P.wt_graph('Fig. 8 &mdash; machines X and Y.'),
   'Fig. 8 shows the work done by two machines X and Y against time. Find the power of each machine.',
   '<div class="calc">power = slope of the W &#8211; t line\n'
   'X :  P = 1200 / 6 = 200 W\n'
   'Y :  P = 1200 / 10 = 120 W</div>'
   '<p>Both machines do 1200 J, but X does it in less time, so X is more powerful.</p>',
   'P(X) = 200 W , P(Y) = 120 W')

# ============================ EXERCISES ============================
a('<div class="pb"></div>')
a('<h2><span class="num">7</span>Exercises</h2>')
a('<p>22 questions &mdash; the last five are the most challenging (&#9733;). Take g = 9.8 m/s&sup2;, cos 37&deg; = '
  '0.8 , cos 60&deg; = 0.5. Show every step and give every answer with its unit.</p>')

QN = [0]
ANS = []


def q(text, ans, steps, fig=None, ch=None, tag='Problem'):
    QN[0] += 1
    if ch:
        ans = ans + ') ' + ch['ABCD'.index(ans)]
    ANS.append((QN[0], ans, steps))
    hard = 'HOTS' in tag
    a('<div class="q' + (' hard' if hard else '') + '"><span class="tag' + (' hots' if hard else '') + '">' + tag +
      '</span><span class="n">Q' + str(QN[0]) + '</span>' + text)
    if fig:
        a(fig)
    if ch:
        one = any(len(c) > 40 for c in ch)
        a('<div class="ch' + (' one' if one else '') + '">' +
          ''.join('<div><b>' + L + ')</b> ' + c + '</div>' for L, c in zip('ABCD', ch)) + '</div>')
    else:
        a('<div class="wr"></div>')
    a('</div>')


HT = '&#9733; HOTS'

q('Power is a measure of:', 'B',
  'power = work done / time taken : it tells how fast the work is done',
  ch=['the amount of work done only', 'the rate of doing work or of transferring energy',
      'the magnitude of the force only', 'the total displacement of the body'], tag='MCQ')
q('The watt is equivalent to:', 'C',
  'P = &Delta;W / &Delta;t  &#8658;  unit = joule / second  &#8658;  1 W = 1 J/s',
  ch=['J &middot; s', 'N &middot; m', 'J / s', 'kg &middot; m / s'], tag='MCQ')
q('A machine does 1200 J of work in 4 s. Its power is:', 'A',
  'P = W / t = 1200 / 4 = 300 W', ch=['300 W', '4800 W', '1196 W', '0.0033 W'], tag='MCQ')
q('Two lifts raise the same load to the same height, and lift B takes half the time taken by lift A. Which '
  'statement is correct?', 'C',
  'same m and same h &#8658; same work W = m g h\nB takes half the time &#8658; P(B) = W / (t/2) = 2 P(A)',
  ch=['B does more work than A', 'A has the greater power', 'they do the same work, and B has double the power',
      'they have the same power, and B does more work'], tag='MCQ')
q('The efficiency of any real machine is always:', 'B',
  'part of the input energy is always wasted (mostly as heat), so useful output &lt; input',
  ch=['exactly 100 %', 'less than 100 %', 'more than 100 %', 'zero'], tag='MCQ')
q('A machine has an efficiency of 60 %. If its input energy is 500 J, the useful output energy is:', 'D',
  'useful = &eta; &times; input = 0.60 &times; 500 = 300 J', ch=['833 J', '200 J', '560 J', '300 J'], tag='MCQ')
q('A lamp receives an electric power of 60 W and gives out 6 W as light. Its efficiency as a source of light is:',
  'A', '&eta; = useful / input = 6 / 60 = 0.10 = 10 %', ch=['10 %', '90 %', '54 %', '1000 %'], tag='MCQ')
q('A force acts on a moving body <b>perpendicular</b> to its direction of motion. The power of this force is:', 'C',
  'P = F v cos 90&deg; = F v &times; 0 = 0\n(the force has no component along the motion)',
  ch=['F v', 'F v / 2', 'zero', 'the largest possible'], tag='MCQ')
q('A crane raises a load of 500 kg through 12 m in 20 s. Find the work done and the power of the crane.',
  'W = 58 800 J , P = 2940 W',
  'W = m g h = 500 &times; 9.8 &times; 12 = 58 800 J\nP = W / t = 58 800 / 20 = 2940 W')
q('A rope pulls a box along the floor at a constant speed of 2.5 m/s with a force of 80 N that makes 37&deg; with '
  'the direction of motion. Find the power of the force.', 'P = 160 W',
  'P = F v cos &theta; = 80 &times; 2.5 &times; cos 37&deg; = 80 &times; 2.5 &times; 0.8 = 160 W',
  L6.block_force_angle('Fig. 9'))
q('An electric motor of power 1.5 kW works for 2 minutes. Find the energy it takes. If its efficiency is 80 %, '
  'find the useful work it does.', 'E = 1.8 &times; 10<sup>5</sup> J , useful = 1.44 &times; 10<sup>5</sup> J',
  'P = 1.5 kW = 1500 W ,  t = 2 min = 120 s\nE = P t = 1500 &times; 120 = 180 000 J\n'
  'useful = &eta; &times; E = 0.80 &times; 180 000 = 144 000 J')
q('<b>Explain</b> why the efficiency of a machine can never be 100 % or more, and where the wasted energy goes.',
  'part of the input is always lost (mostly as heat by friction) ; energy cannot be created',
  'the useful output can never be larger than the input, because energy cannot be created\n'
  'some of the input is always changed into heat (friction, resistance) and sound\n'
  'so useful output &lt; input  &#8658;  &eta; &lt; 100 %', tag='Explain')
q('Fig. 10 shows the work done by two machines X and Y against time. The more powerful machine is:', 'A',
  'power = slope of the W &#8211; t line ; the line of X is steeper\n(X does 1200 J in 6 s, Y in 10 s)',
  P.wt_graph('Fig. 10'), ['X', 'Y', 'both have the same power', 'it cannot be known'], tag='MCQ')
q('For the machines of Fig. 10, find the power of each machine and the ratio P<sub>X</sub> / P<sub>Y</sub>.',
  'P(X) = 200 W , P(Y) = 120 W , ratio = 5/3',
  'P(X) = 1200 / 6 = 200 W\nP(Y) = 1200 / 10 = 120 W\nP(X) / P(Y) = 200 / 120 = 5/3')
q('An electric kettle takes a power of 2000 W and has an efficiency of 84 %. Find its useful power, and the useful '
  'and the wasted energy in 5 minutes.', 'P = 1680 W ; useful = 5.04 &times; 10<sup>5</sup> J , wasted = '
  '9.6 &times; 10<sup>4</sup> J',
  'useful power = 0.84 &times; 2000 = 1680 W\nt = 5 min = 300 s\n'
  'useful energy = 1680 &times; 300 = 504 000 J\nwasted energy = ( 2000 &#8722; 1680 ) &times; 300 = 96 000 J')
q('A motor raises a load of mass m at a constant speed v. The useful power of the motor is:', 'B',
  'constant speed &#8658; the pull equals the weight m g and acts along the motion\nP = F v cos 0&deg; = m g v',
  P.motor_lift('Fig. 11'), ['m v', 'm g v', 'm g / v', 'm g h'], tag='MCQ')
q('A pump raises 300 kg of water through a height of 15 m every minute. Find its useful power. If the pump takes '
  'an electric power of 1000 W, find its efficiency.', 'P = 735 W , &eta; = 73.5 %',
  'useful work each minute :  W = m g h = 300 &times; 9.8 &times; 15 = 44 100 J\n'
  'P = W / t = 44 100 / 60 = 735 W\n&eta; = 735 / 1000 = 0.735 = 73.5 %')
q('A motor of efficiency 75 % raises a load of 120 kg at a constant speed of 0.5 m/s through a height of 10 m. Find: '
  '(i) the useful power, (ii) the input power, (iii) the electric energy taken by the motor during the lift.',
  '(i) 588 W (ii) 784 W (iii) 15 680 J',
  '(i)   P(useful) = m g v = 120 &times; 9.8 &times; 0.5 = 588 W\n'
  '(ii)  P(input) = P(useful) / &eta; = 588 / 0.75 = 784 W\n'
  '(iii) time of the lift :  t = h / v = 10 / 0.5 = 20 s\n'
  '      E = P(input) &times; t = 784 &times; 20 = 15 680 J', tag=HT)
q('Motor A raises 80 kg through 6 m in 8 s, while motor B raises 60 kg through 10 m in 12 s. Which motor is more '
  'powerful, and what is the ratio P<sub>A</sub> / P<sub>B</sub>?', 'A ; ratio = 1.2',
  'P(A) = m g h / t = 80 &times; 9.8 &times; 6 / 8 = 588 W\n'
  'P(B) = 60 &times; 9.8 &times; 10 / 12 = 490 W\n'
  'P(A) / P(B) = 588 / 490 = 1.2  &#8658;  motor A is more powerful\n'
  '( note : B does more work , 5880 J against 4704 J , but more slowly )', tag=HT)
q('A force of 100 N pulls a box along the direction of motion with a power of 300 W. If the box keeps the same '
  'speed but the force now makes 60&deg; with the direction of motion, find the speed and the new power.',
  'v = 3 m/s , P = 150 W',
  '&theta; = 0 :  P = F v  &#8658;  v = P / F = 300 / 100 = 3 m/s\n'
  '&theta; = 60&deg; :  P = F v cos 60&deg; = 100 &times; 3 &times; 0.5 = 150 W', tag=HT)
q('A heater of efficiency 80 % must give 48 000 J of useful heat every minute. Find the useful power, the input '
  'power and the energy wasted every minute.', 'P(useful) = 800 W , P(input) = 1000 W , wasted = 12 000 J',
  'useful power = 48 000 / 60 = 800 W\ninput power = 800 / 0.80 = 1000 W\n'
  'wasted energy per minute = ( 1000 &#8722; 800 ) &times; 60 = 12 000 J', tag=HT)
q('A lift and its passengers have a total mass of 500 kg. Its motor takes an electric power of 8 kW and raises the '
  'lift through 30 m in 25 s. Find the useful work, the useful power, the efficiency of the motor and the energy '
  'wasted during the lift.', 'W = 147 000 J , P = 5880 W , &eta; = 73.5 % , wasted = 53 000 J',
  'useful work :  W = m g h = 500 &times; 9.8 &times; 30 = 147 000 J\n'
  'useful power :  P = 147 000 / 25 = 5880 W\n'
  '&eta; = 5880 / 8000 = 0.735 = 73.5 %\n'
  'input energy = 8000 &times; 25 = 200 000 J  &#8658;  wasted = 200 000 &#8722; 147 000 = 53 000 J', tag=HT)

# ============================ MODEL ANSWER ============================
a('<div class="pb"></div>')
a('<h2><span class="num">8</span>Model answer &mdash; step by step</h2>')
for n, ans, steps in ANS:
    a('<div class="sol2"><span class="sn">Q' + str(n) + '</span><pre>' + steps + '</pre>'
      '<span class="fa">&#10004; ' + ans + '</span></div>')

a('<div class="foot"><span>Power and Efficiency &mdash; Grade 11 Physics &middot; Mr. Gemy</span><span>P = &Delta;W/&Delta;t '
  '&middot; P = F v cos &theta; &middot; &eta; = useful / input</span></div>')
a('</body></html>')

open('power.html', 'w', encoding='utf-8').write(''.join(H))
print('power.html written :', QN[0], 'questions')

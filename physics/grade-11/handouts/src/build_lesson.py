# -*- coding: utf-8 -*-
import base64
import figs_lesson as L
from css_apple import CSS

WM = ('<svg xmlns="http://www.w3.org/2000/svg" width="340" height="230">'
      '<text x="170" y="128" font-family="Helvetica,Arial,sans-serif" font-size="28" font-weight="700" '
      'fill="#0B1220" fill-opacity="0.045" text-anchor="middle" '
      'transform="rotate(-27 170 128)">Mr. Gemy</text></svg>')
WM64 = base64.b64encode(WM.encode()).decode()

H = []
a = H.append
a('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
  '<title>Velocity Vectors and Relative Velocity</title><style>' + CSS +
  'body{background-image:url("data:image/svg+xml;base64,' + WM64 + '");background-repeat:repeat;}'
  '</style></head><body>')

# ------------------------------- hero -------------------------------
a('<div class="hero"><span class="chip">Unit 1 &middot; Lesson 1&ndash;1</span>'
  '<h1>Velocity Vectors<br>and Relative Velocity</h1>'
  '<div class="sub">Classwork, home assignments and the weekly assessment &mdash; '
  'fully worked, step by step.</div>'
  '<div class="meta"><span>Grade 11 &middot; Egyptian Baccalaureate</span><span>35 questions</span>'
  '<span>Step-by-step solutions</span><span>g = 10 m/s&sup2;</span></div>'
  '<div class="sig"><b>Mr. Gemy</b><i>Physics</i></div></div>')

a('<div class="kit"><h4>The toolkit for this lesson</h4><div class="grid">'
  '<div class="f">v<sub>x</sub> = v cos &theta;<small>horizontal component</small></div>'
  '<div class="f">v<sub>y</sub> = v sin &theta;<small>vertical component</small></div>'
  '<div class="f">v = &radic;( v<sub>x</sub>&sup2; + v<sub>y</sub>&sup2; )<small>magnitude from components</small></div>'
  '<div class="f">tan &theta; = v<sub>y</sub> / v<sub>x</sub><small>direction of the vector</small></div>'
  '<div class="f">R = &radic;( A&sup2; + B&sup2; + 2AB cos &theta; )<small>resultant of two vectors</small></div>'
  '<div class="f">v<sub>AB</sub> = v<sub>A</sub> &minus; v<sub>B</sub><small>velocity of A relative to B</small></div>'
  '</div></div>')

a('<div class="hint"><b>Before you start.</b> Relative velocity is a <b>vector subtraction</b>, never a plain '
  'arithmetic one. Fix a positive direction first, give every velocity its sign, and only then subtract. '
  'For perpendicular velocities use Pythagoras.</div>')

QN = [0]


def sec(n, kicker, title):
    a('<div class="sec"><div class="no">' + n + '</div><div class="tt"><small>' + kicker + '</small>' +
      title + '</div><div class="rule"></div></div>')


def grp(t):
    a('<h3 class="grp">' + t + '</h3>')


def q(text, tag=None, fig=None, ch=None, parts=None, fig2=None):
    QN[0] += 1
    a('<div class="card"><div class="qh"><div class="qno">' + str(QN[0]) + '</div>'
      '<div class="qtx">' + text + '</div>' + ('<span class="tag">' + tag + '</span>' if tag else '') + '</div>')
    if parts:
        for p in parts:
            a('<div class="part">' + p + '</div>')
    if fig:
        a(fig)
    if fig2:
        a(fig2)
    if ch:
        a('<div class="ch">')
        for le, c in zip('ABCD', ch):
            a('<div><i>' + le + '</i>' + c + '</div>')
        a('</div>')
    a('</div>')


# ============================== PART A ==============================
sec('A', 'Classwork &nbsp;1', 'Resolving vectors and finding the resultant')

q('The figure shows eight velocity vectors drawn from the origin. <b>Resolve each vector</b> into its '
  'horizontal (x) component and its vertical (y) component.',
  'Resolution', L.axes_vectors('Figure 1 &nbsp;&middot;&nbsp; eight velocity vectors'))

q('Find the <b>resultant</b> of each pair of displacement vectors below, giving its magnitude and its '
  'direction, and show it on a sketch.', 'Resultant',
  '<div class="figrow">' + L.two_vec('(a)', 8, 180, '8 m', 6, 0, '6 m', maxw=300) +
  L.two_vec('(b)', 6, 90, '6 m', 8, 180, '8 m', maxw=250) +
  L.two_vec('(c)', 6, 0, '6 m', 8, 30, '8 m', '30&deg;', maxw=300) + '</div>')

# ============================== PART B ==============================
sec('B', 'Home assignment &nbsp;1', 'Components, resultants and the angle of projection')

q('An aircraft takes off with a <b>constant</b> velocity of 100 m/s directed at 60&deg; above the horizontal.',
  'Components', L.plane_launch('Figure 2', 60, 'v = 100 m/s', True),
  parts=['<b>a)</b> Calculate the horizontal component of its velocity.',
         '<b>b)</b> Calculate the vertical component of its velocity.',
         '<b>c)</b> Calculate the height it reaches 10 s after take-off.'])

q('A body moves with a velocity <i>v</i> that makes an angle &theta; with the horizontal. The horizontal '
  'component of the velocity is 3 m/s and the vertical component is 4 m/s. Find, with a sketch:',
  'Components', L.comp_tri('Figure 3', 'vₓ = 3 m/s', 'vᵧ = 4 m/s'),
  parts=['<b>1)</b> the magnitude of the velocity <i>v</i>.', '<b>2)</b> the angle &theta;.'])

q('An aircraft climbs with a constant velocity of 100 m/s at an angle &theta; to the horizontal, and reaches '
  'a height of 500 m after 10 s from take-off. <b>What is the value of &theta;?</b>', 'Angle',
  L.plane_launch('Figure 4', 30, 'v = 100 m/s', False, 'h = 500 m', anglab='θ = ?',
                 extra='after t = 10 s'))

q('Find the resultant of each of the following pairs of displacement vectors, with a sketch.', 'Resultant',
  '<div class="figrow">' + L.two_vec('(a)', 6, 0, '6 m', 8, 90, '8 m', maxw=260) +
  L.two_vec('(b)', 6, 0, '6 m', 8, 120, '8 m', '120&deg;', maxw=300) + '</div>')

q('A body is projected at 30&deg; above the horizontal and reaches a maximum height of 45 m. '
  'Its initial speed equals &hellip;&hellip; &nbsp;(g = 10 m/s&sup2;)', 'MCQ',
  L.proj_height('Figure 5', 30, 'v₀ = ?', 'h = 45 m'),
  ch=['30 m/s', '45 m/s', '60 m/s', '90 m/s'])

# ============================== PART C ==============================
sec('C', 'Classwork &nbsp;2', 'Relative velocity')

q('Two cars A and B move with speeds v<sub>A</sub> and v<sub>B</sub> respectively. <b>Write the expression '
  'for the magnitude of the velocity of B relative to A</b> in each of the following cases:', 'Concept',
  L.rel_cases('Figure 6 &nbsp;&middot;&nbsp; the three cases'),
  parts=['<b>First:</b> the two cars move in the same direction.',
         '<b>Second:</b> the two cars move in opposite directions.',
         '<b>Third:</b> the velocity of A is perpendicular to the velocity of B.'])

q('If the speed of body A (v<sub>A</sub>) is greater than the speed of body B (v<sub>B</sub>) and both move '
  'in the same direction, <b>how does the motion of A appear to an observer on B?</b> Explain your answer.',
  'Explain')

q('Car A moves at 60 m/s towards the <b>west</b>, while car B moves at 80 m/s towards the <b>north</b>. '
  'Find the magnitude and the direction of the velocity of car A relative to car B, and show your answer on '
  'a sketch.', 'Problem', L.cross_cars('Figure 7', '60 m/s', 'W', '80 m/s', 'N'))

# ============================== PART D ==============================
a('<div class="pb"></div>')
sec('D', 'Home assignment &nbsp;2', 'Relative velocity &mdash; problems and multiple choice')

q('If the speed of body A (v<sub>A</sub>) is <b>twice</b> the speed of body B (v<sub>B</sub>) and the two '
  'bodies move in <b>opposite</b> directions, what is the speed of B relative to A? Explain your answer.',
  'Explain')

q('A passenger sits beside the window of a bus moving along a straight horizontal road at 20 m/s. '
  'The rain, which is falling vertically, appears to this passenger to fall at an angle of 40&deg; to the '
  'vertical.', 'Problem', L.bus_rain('Figure 8 &nbsp;&middot;&nbsp; the bus and the rain'),
  parts=['<b>a)</b> Find the velocity of the raindrops relative to the ground.',
         '<b>b)</b> Explain why the rain does not appear to fall vertically to this passenger.'])

q('Two bodies A and B move in the same direction with speeds v<sub>A</sub> and v<sub>B</sub> respectively. '
  'Which of the following relations gives the magnitude of the velocity of A relative to B (v<sub>AB</sub>)?',
  'MCQ', ch=['v<sub>AB</sub> = v<sub>A</sub> &minus; v<sub>B</sub>',
             'v<sub>AB</sub> = &radic;( v<sub>A</sub>&sup2; &minus; v<sub>B</sub>&sup2; )',
             'v<sub>AB</sub> = v<sub>A</sub> + v<sub>B</sub>',
             'v<sub>AB</sub> = &radic;( v<sub>A</sub>&sup2; + v<sub>B</sub>&sup2; )'])

q('If the velocity of a body relative to another body equals zero, this means that the two bodies:', 'MCQ',
  ch=['move with different speeds in the same direction', 'move with equal speeds in the same direction',
      'move with equal speeds in opposite directions', 'move with different speeds in opposite directions'])

q('Two cars move in opposite directions; the speed of the first is 30 m/s and that of the second is 20 m/s. '
  'The velocity of the first car relative to the second equals &hellip;&hellip;', 'MCQ',
  ch=['10 m/s', '20 m/s', '50 m/s', '600 m/s'])

q('Car A moves at 40 m/s while car B moves at 25 m/s, both in the same direction. '
  'To the driver of car B, car A appears to:', 'MCQ',
  ch=['move in the same direction at 15 m/s', 'move in the opposite direction at 15 m/s',
      'move in the same direction at 65 m/s', 'move in the opposite direction at 65 m/s'])

q('Body A moves at 30 m/s to the right while body B moves at 20 m/s to the left. '
  'Relative to body A, how does body B appear to move?', 'MCQ',
  ch=['to the right at 10 m/s', 'to the left at 10 m/s', 'to the right at 50 m/s', 'to the left at 50 m/s'])

q('Body A moves at 30 m/s towards the east while body B moves at 40 m/s towards the north. '
  'What is the <b>direction</b> of the velocity of B relative to A?', 'MCQ',
  ch=['35&deg; north of west', '53.1&deg; north of west', '35&deg; north of east', '53.1&deg; north of east'])

q('If body A is faster than body B and both move in the same direction, then relative to B, body A appears to:',
  'MCQ', ch=['move in the opposite direction at a speed less than its actual speed',
             'move in the same direction at a speed greater than its actual speed',
             'move in the opposite direction at a speed greater than its actual speed',
             'move in the same direction at a speed less than its actual speed'])

q('Body A moves at 30 m/s to the right while body B moves at 40 m/s vertically upwards. '
  'What is the magnitude of the velocity of B relative to A?', 'MCQ',
  ch=['10 m/s', '50 m/s', '70 m/s', '120 m/s'])

# ============================== PART E ==============================
a('<div class="pb"></div>')
sec('E', 'Weekly assessment &nbsp;1', 'Groups A, B and C')

grp('Group A')
q('Two bodies A and B move in the same direction. The speed of A is 20 m/s and the speed of B is 21 m/s. '
  'What is the magnitude of the velocity of A relative to B?', 'MCQ',
  ch=['8 m/s', '32 m/s', '10 m/s', '1 m/s'])

q('The figure shows a resultant vector <b>R</b> produced by two vectors A and B. '
  'Which diagram correctly represents the pair of vectors A and B that form this resultant?', 'MCQ',
  L.mcq_vectors('Figure 9 &nbsp;&middot;&nbsp; the resultant and the four options'))

q('Two projectiles are launched with the <b>same initial speed</b> but at different angles to the horizontal. '
  'Projectile A is launched at a larger angle than projectile B. <b>Which one reaches the greater maximum '
  'height?</b> Explain your answer.', 'Explain', L.two_planes('Figure 10'))

q('A ferry captain wants his ferry to land at the point exactly opposite its starting point on the other bank '
  'of a flowing river. <b>How must he direct the ferry?</b> Explain.', 'Explain', L.ferry('Figure 11', True))

q('Car A moves at 30 m/s towards the <b>east</b> while car B moves at 40 m/s towards the <b>south</b>. '
  'Find the magnitude and the direction of the velocity of car A relative to car B.', 'Problem',
  L.cross_cars('Figure 12', '30 m/s', 'E', '40 m/s', 'S'))

grp('Group B')
q('A body is projected with an initial speed of 40 m/s and reaches a maximum height of 20 m. '
  'Its angle of projection above the horizontal is &hellip;&hellip; &nbsp;(g = 10 m/s&sup2;)', 'MCQ',
  L.proj_height('Figure 13', 30, 'v₀ = 40 m/s', 'h = 20 m'),
  ch=['15&deg;', '30&deg;', '45&deg;', '60&deg;'])

q('A body moves with a velocity <i>v</i> making an angle &theta; with the horizontal. The horizontal '
  'component of the velocity is 5 m/s and the vertical component is 5 m/s. Find, with a sketch:', 'Components',
  L.comp_tri('Figure 14', 'vₓ = 5 m/s', 'vᵧ = 5 m/s', vx=3.2, vy=3.2),
  parts=['<b>1)</b> the magnitude of the velocity <i>v</i>.', '<b>2)</b> the angle &theta;.'])

q('If the speed of body A (v<sub>A</sub>) is <b>half</b> the speed of body B (v<sub>B</sub>) and both move in '
  'the same direction, how does the motion of A appear relative to B? Explain.', 'Explain')

q('What happens to the relative velocity between two bodies moving with <b>equal speeds in the same '
  'direction</b>? Explain your answer.', 'Explain')

q('When does the resultant of two vectors that are equal in magnitude and opposite in direction vanish? '
  'Explain your answer.', 'Explain')

grp('Group C')
q('If two bodies move with equal speeds in opposite directions, the magnitude of the relative velocity '
  'between them is:', 'MCQ',
  ch=['equal to the speed of one of them', 'equal to half the speed of one of them',
      'equal to twice the speed of one of them', 'equal to four times the speed of one of them'])

q('Body A moves at 30 m/s and body B moves at 20 m/s in the same direction. Relative to body A, '
  'how does body B appear to move?', 'MCQ',
  ch=['in the same direction at 10 m/s', 'in the opposite direction at 10 m/s',
      'in the same direction at 50 m/s', 'in the opposite direction at 50 m/s'])

q('An aircraft climbs with a constant speed of 80 m/s at an angle of 30&deg; above the horizontal.',
  'Components', L.plane_launch('Figure 15', 30, 'v = 80 m/s', True),
  parts=['<b>a)</b> Calculate the horizontal component of its velocity.',
         '<b>b)</b> Calculate the vertical component of its velocity.'])

q('The current of a river stays constant, but the ferry increases its speed relative to the water while its '
  'bow is kept pointing straight across the river. <b>What happens to the drift of the ferry along the '
  'direction of the current?</b> Explain.', 'Explain', L.ferry('Figure 16', False))

q('A body is projected with a speed <i>v</i> at an angle &theta; above the horizontal, and reaches a height '
  '<i>h</i> after a time <i>t</i> from the instant of projection. <b>Explain, in two different ways,</b> how '
  'the height reached in the same time interval can be increased.', 'Explain',
  L.proj_height('Figure 17', 45, 'v', 'h'))

# ============================== SOLUTIONS ==============================
a('<div class="pb"></div>')
sec('✓', 'Answer key', 'Solutions &mdash; step by step')
a('<div class="hint">Every question is solved in full: the relation used, the substitution, then the result. '
  'Angles are given to one decimal place and g = 10 m/s&sup2; throughout.</div>')


def sol(n, title, steps=None, res=None, why=None, extra=None):
    a('<div class="sol"><div class="sh"><div class="sn">' + str(n) + '</div>'
      '<div class="st">' + title + '</div></div>')
    if steps:
        a('<pre>' + steps + '</pre>')
    if why:
        a('<div class="why">' + why + '</div>')
    if extra:
        a(extra)
    if res:
        a('<div class="res">' + res + '</div>')
    a('</div>')


grp('Part A &mdash; Classwork 1')
a('<div class="sol"><div class="sh"><div class="sn">1</div><div class="st">resolving the eight vectors &nbsp;'
  '&middot;&nbsp; v<sub>x</sub> = v cos &theta; , v<sub>y</sub> = v sin &theta; (&theta; measured from the '
  '+x axis)</div></div>'
  '<table class="vt"><tr><th>Vector</th><th>Magnitude</th><th>Direction</th>'
  '<th>v<sub>x</sub> (m/s)</th><th>v<sub>y</sub> (m/s)</th></tr>'
  '<tr><td>V<sub>1</sub></td><td>3 m/s</td><td>along +x</td><td>+ 3.00</td><td>0</td></tr>'
  '<tr><td>V<sub>2</sub></td><td>5 m/s</td><td>along &minus;x</td><td>&minus; 5.00</td><td>0</td></tr>'
  '<tr><td>V<sub>3</sub></td><td>6 m/s</td><td>along +y</td><td>0</td><td>+ 6.00</td></tr>'
  '<tr><td>V<sub>4</sub></td><td>8 m/s</td><td>along &minus;y</td><td>0</td><td>&minus; 8.00</td></tr>'
  '<tr><td>V<sub>5</sub></td><td>10 m/s</td><td>45&deg; above +x</td><td>+ 7.07</td><td>+ 7.07</td></tr>'
  '<tr><td>V<sub>6</sub></td><td>6 m/s</td><td>60&deg; above &minus;x (120&deg;)</td><td>&minus; 3.00</td><td>+ 5.20</td></tr>'
  '<tr><td>V<sub>7</sub></td><td>6 m/s</td><td>60&deg; below &minus;x (240&deg;)</td><td>&minus; 3.00</td><td>&minus; 5.20</td></tr>'
  '<tr><td>V<sub>8</sub></td><td>10 m/s</td><td>20&deg; from &minus;y (290&deg;)</td><td>+ 3.42</td><td>&minus; 9.40</td></tr>'
  '</table><div class="why">A component is <b>positive</b> along +x (east) or +y (north) and '
  '<b>negative</b> along &minus;x or &minus;y. A vector lying on an axis has one component only.</div></div>')

sol(2, 'resultant of each pair',
    '(a)  the two vectors are along the same line, in opposite directions :\n'
    '     R = 8 &minus; 6 = 2 m , in the direction of the 8 m vector\n\n'
    '(b)  the two vectors are perpendicular :\n'
    '     R = &radic;( 6&sup2; + 8&sup2; ) = &radic;100 = 10 m\n'
    '     tan &alpha; = 6 / 8 = 0.75   &rarr;   &alpha; = 36.9&deg; measured from the 8 m vector\n\n'
    '(c)  the angle between them is 30&deg; :\n'
    '     R = &radic;( 6&sup2; + 8&sup2; + 2 &times; 6 &times; 8 &times; cos 30&deg; )\n'
    '       = &radic;( 100 + 83.14 ) = &radic;183.14 = 13.53 m\n'
    '     tan &alpha; = ( 8 sin 30&deg; ) / ( 6 + 8 cos 30&deg; ) = 4 / 12.93 = 0.309\n'
    '     &alpha; = 17.2&deg; from the 6 m vector',
    '(a) 2 m &nbsp;&middot;&nbsp; (b) 10 m at 36.9&deg; &nbsp;&middot;&nbsp; (c) 13.53 m at 17.2&deg;')

grp('Part B &mdash; Home assignment 1')
sol(3, 'aircraft climbing at 60&deg;',
    'a)  vₓ = v cos &theta; = 100 &times; cos 60&deg; = 100 &times; 0.5 = 50 m/s\n'
    'b)  vᵧ = v sin &theta; = 100 &times; sin 60&deg; = 100 &times; 0.866 = 86.6 m/s\n'
    'c)  the velocity is constant, so the vertical motion is uniform :\n'
    '    h = vᵧ &times; t = 86.6 &times; 10 = 866 m',
    'vₓ = 50 m/s , vᵧ = 86.6 m/s , h = 866 m')

sol(4, 'magnitude and direction from the components',
    '1)  v = &radic;( vₓ&sup2; + vᵧ&sup2; ) = &radic;( 3&sup2; + 4&sup2; ) = &radic;25 = 5 m/s\n'
    '2)  tan &theta; = vᵧ / vₓ = 4 / 3 = 1.333   &rarr;   &theta; = 53.1&deg;',
    'v = 5 m/s at 53.1&deg; above the horizontal')

sol(5, 'finding the angle of climb',
    'the climb is at constant velocity, so the vertical motion is uniform :\n'
    'vᵧ = h / t = 500 / 10 = 50 m/s\n'
    'vᵧ = v sin &theta;   &rarr;   sin &theta; = 50 / 100 = 0.5\n'
    '&theta; = 30&deg;', '&theta; = 30&deg;')

sol(6, 'resultant of each pair',
    '(a)  perpendicular vectors :\n'
    '     R = &radic;( 6&sup2; + 8&sup2; ) = 10 m\n'
    '     tan &alpha; = 8 / 6 = 1.333   &rarr;   &alpha; = 53.1&deg; from the 6 m vector\n\n'
    '(b)  the angle between them is 120&deg; :\n'
    '     R = &radic;( 6&sup2; + 8&sup2; + 2 &times; 6 &times; 8 &times; cos 120&deg; )\n'
    '       = &radic;( 100 &minus; 48 ) = &radic;52 = 7.21 m\n'
    '     tan &alpha; = ( 8 sin 120&deg; ) / ( 6 + 8 cos 120&deg; ) = 6.93 / 2 = 3.464\n'
    '     &alpha; = 73.9&deg; from the 6 m vector',
    '(a) 10 m at 53.1&deg; &nbsp;&middot;&nbsp; (b) 7.21 m at 73.9&deg;')

sol(7, 'initial speed from the maximum height',
    'at the highest point the vertical component of the velocity = 0 :\n'
    'h = ( v₀ sin &theta; )&sup2; / ( 2 g )\n'
    '45 = ( v₀ &times; sin 30&deg; )&sup2; / ( 2 &times; 10 ) = ( 0.5 v₀ )&sup2; / 20\n'
    '0.25 v₀&sup2; = 900   &rarr;   v₀&sup2; = 3600   &rarr;   v₀ = 60 m/s', 'C) 60 m/s')

grp('Part C &mdash; Classwork 2')
sol(8, 'the three cases of relative velocity',
    'the general rule is a vector subtraction :   v(B rel A) = v(B) &minus; v(A)\n\n'
    'First   (same direction)      :  v(BA) = | v(B) &minus; v(A) |\n'
    'Second  (opposite directions) :  v(BA) = v(B) + v(A)\n'
    'Third   (perpendicular)       :  v(BA) = &radic;( v(A)&sup2; + v(B)&sup2; )',
    why='In the second case one of the two velocities is negative, so subtracting it is the same as adding '
        'the two magnitudes. In the third case the subtraction is carried out with Pythagoras’ theorem.')

sol(9, 'how A appears to an observer on B',
    'v(A rel B) = v(A) &minus; v(B)\n'
    'since v(A) > v(B) the result is positive, and it is smaller than v(A)',
    'A appears to move in the same direction, but more slowly, at ( v<sub>A</sub> &minus; v<sub>B</sub> )',
    why='The observer on B subtracts his own velocity from that of A, so only the <b>difference</b> between '
        'the two speeds is seen. This is why a car overtaking you on the motorway seems to crawl past.')

sol(10, 'car A west, car B north',
    'v(A rel B) = v(A) &minus; v(B) = 60 (west) + 80 (south)\n'
    'the two components are perpendicular :\n'
    '| v(AB) | = &radic;( 60&sup2; + 80&sup2; ) = &radic;10000 = 100 m/s\n'
    'tan &theta; = 60 / 80 = 0.75   &rarr;   &theta; = 36.9&deg; from the south direction',
    '100 m/s , 53.1&deg; south of west',
    why='Reversing the velocity of B (north &rarr; south) is what turns the subtraction into an ordinary '
        'vector addition.')

grp('Part D &mdash; Home assignment 2')
sol(11, 'A twice as fast as B, opposite directions',
    'take the direction of A as positive :   v(A) = 2 v(B) ,  v(B) = &minus; v(B)\n'
    'v(B rel A) = v(B) &minus; v(A) = &minus; v(B) &minus; 2 v(B) = &minus; 3 v(B)',
    'speed of B relative to A = 3 v<sub>B</sub> &nbsp;( = 1.5 v<sub>A</sub> ) , opposite to the motion of A',
    why='The minus sign only tells us the direction: to an observer on A, body B rushes backwards at three '
        'times its own speed.')

sol(12, 'the bus and the rain',
    'for the passenger :   v(rain rel bus) = v(rain) &minus; v(bus)\n'
    'so the apparent velocity has a horizontal component of 20 m/s pointing backwards,\n'
    'and a vertical component equal to the true speed of the rain.\n\n'
    'a)  tan 40&deg; = 20 / v(rain)\n'
    '    v(rain) = 20 / tan 40&deg; = 20 / 0.839 = 23.8 m/s  (vertically downwards)\n'
    '    [ the apparent speed itself = 20 / sin 40&deg; = 31.1 m/s ]',
    'v(rain) = 23.8 m/s vertically downwards',
    why='<b>b)</b> The passenger is a <b>moving observer</b>. His own velocity is subtracted from the velocity '
        'of every raindrop, which adds a backward horizontal component of 20 m/s to the vertical fall. '
        'The sum of the two is a slanted velocity, so the rain is seen falling at 40&deg; to the vertical. '
        'A person standing still on the pavement sees the same rain falling vertically.')

sol(13, 'same direction', 'v(AB) = v(A) &minus; v(B)   (plain subtraction, both velocities have the same sign)',
    'A) v<sub>AB</sub> = v<sub>A</sub> &minus; v<sub>B</sub>')
sol(14, 'zero relative velocity', 'v(A) &minus; v(B) = 0   &rarr;   v(A) = v(B)  in magnitude and direction',
    'B) equal speeds in the same direction')
sol(15, 'opposite directions', 'v(1 rel 2) = 30 &minus; ( &minus; 20 ) = 50 m/s', 'C) 50 m/s')
sol(16, 'overtaking car', 'v(A rel B) = 40 &minus; 25 = + 15 m/s   (positive &rarr; same direction)',
    'A) same direction at 15 m/s')
sol(17, 'bodies approaching', 'take right as positive :  v(B) = &minus; 20 , v(A) = + 30\n'
    'v(B rel A) = &minus; 20 &minus; 30 = &minus; 50 m/s   (negative &rarr; to the left)',
    'D) to the left at 50 m/s')
sol(18, 'perpendicular velocities',
    'v(B rel A) = v(B) &minus; v(A) = 40 (north) + 30 (west)\n'
    'tan &theta; = 30 / 40 = 0.75  &rarr;  &theta; = 36.9&deg; west of north , i.e. 53.1&deg; north of west',
    'B) 53.1&deg; north of west')
sol(19, 'the faster body seen from the slower one',
    'v(A rel B) = v(A) &minus; v(B) > 0  and  ( v(A) &minus; v(B) ) < v(A)',
    'D) same direction, at a speed less than its actual speed')
sol(20, 'perpendicular velocities',
    'v(B rel A) = 40 (up) + 30 (left)\n| v | = &radic;( 40&sup2; + 30&sup2; ) = &radic;2500 = 50 m/s', 'B) 50 m/s')

grp('Part E &mdash; Weekly assessment 1 &nbsp;&middot;&nbsp; Group A')
sol(21, 'very close speeds', 'v(A rel B) = 20 &minus; 21 = &minus; 1 m/s   &rarr;   magnitude = 1 m/s',
    'D) 1 m/s', why='The minus sign means that A falls slowly behind B.')
sol(22, 'which pair gives the resultant',
    'the given R points upwards and to the left, so it must have :\n'
    '    a component towards the west   &rarr;  vector B directed west\n'
    '    a component towards the north  &rarr;  vector A directed north\n'
    'only diagram (a) has this pair; completing the parallelogram gives R.',
    'A) the pair in diagram (a)')
sol(23, 'which projectile rises higher',
    'h(max) = ( v sin &theta; )&sup2; / ( 2 g )\n'
    'the speed v is the same for both, so h depends on sin &theta; only,\n'
    'and sin &theta; increases as &theta; increases (up to 90&deg;)',
    'Projectile A , because it is launched at the larger angle',
    why='A larger angle puts a larger share of the same speed into the <b>vertical</b> component, '
        'so the body rises higher (although its horizontal range may be smaller).')
sol(24, 'steering the ferry',
    'the ferry must be aimed <b>upstream</b> at an angle &alpha; to the line joining the two points, where\n'
    '    v(boat) sin &alpha; = v(river)      &rarr;   sin &alpha; = v(river) / v(boat)\n'
    'then the upstream component exactly cancels the current, and what is left is\n'
    '    v(resultant) = &radic;( v(boat)&sup2; &minus; v(river)&sup2; )   straight across the river',
    'aim upstream at &alpha; = sin&#8315;&sup1; ( v<sub>river</sub> / v<sub>boat</sub> )')
sol(25, 'car A east, car B south',
    'v(A rel B) = v(A) &minus; v(B) = 30 (east) + 40 (north)\n'
    '| v(AB) | = &radic;( 30&sup2; + 40&sup2; ) = 50 m/s\n'
    'tan &theta; = 40 / 30 = 1.333   &rarr;   &theta; = 53.1&deg;',
    '50 m/s , 53.1&deg; north of east')

grp('Group B')
sol(26, 'angle from the maximum height',
    'h = ( v₀ sin &theta; )&sup2; / ( 2 g )\n'
    '20 = ( 40 sin &theta; )&sup2; / 20   &rarr;   ( 40 sin &theta; )&sup2; = 400\n'
    '40 sin &theta; = 20   &rarr;   sin &theta; = 0.5   &rarr;   &theta; = 30&deg;', 'B) 30&deg;')
sol(27, 'equal components',
    '1)  v = &radic;( 5&sup2; + 5&sup2; ) = &radic;50 = 7.07 m/s\n'
    '2)  tan &theta; = 5 / 5 = 1   &rarr;   &theta; = 45&deg;', 'v = 7.07 m/s at 45&deg;',
    why='Whenever the two components are equal the angle is 45&deg;, whatever their size.')
sol(28, 'A is half as fast as B',
    'v(A rel B) = v(A) &minus; v(B) = 0.5 v(B) &minus; v(B) = &minus; 0.5 v(B)',
    'A appears to move <b>backwards</b> at half the speed of B ( = its own speed )',
    why='To an observer on the faster body B, the slower body A is falling behind, so it seems to travel in '
        'the opposite direction.')
sol(29, 'equal speeds, same direction', 'v(A rel B) = v &minus; v = 0',
    'the relative velocity is zero',
    why='Each body appears at rest to an observer on the other one — exactly like two cars keeping the '
        'same speed side by side on the road.')
sol(30, 'two equal and opposite vectors',
    'R = &radic;( A&sup2; + A&sup2; + 2 A&sup2; cos 180&deg; ) = &radic;( 2A&sup2; &minus; 2A&sup2; ) = 0',
    'the resultant is <b>always</b> zero',
    why='Equal magnitudes with opposite directions cancel completely, so the resultant vanishes for any two '
        'such vectors acting at the same point — no special condition is needed.')

grp('Group C')
sol(31, 'equal speeds, opposite directions', 'v(A rel B) = v &minus; ( &minus; v ) = 2 v',
    'C) twice the speed of one of them')
sol(32, 'slower body seen from the faster one',
    'v(B rel A) = 20 &minus; 30 = &minus; 10 m/s   (negative &rarr; opposite direction)',
    'B) opposite direction at 10 m/s')
sol(33, 'components of the aircraft velocity',
    'a)  vₓ = 80 cos 30&deg; = 80 &times; 0.866 = 69.28 m/s\n'
    'b)  vᵧ = 80 sin 30&deg; = 80 &times; 0.5 = 40 m/s', 'vₓ = 69.28 m/s , vᵧ = 40 m/s')
sol(34, 'a faster ferry, same current',
    'time of crossing :   t = width / v(boat)\n'
    'drift along the current :   d = v(river) &times; t = v(river) &times; width / v(boat)\n'
    'v(river) and the width do not change, while v(boat) increases',
    'the drift <b>decreases</b>',
    why='The faster the ferry crosses, the less time the current has to carry it downstream, so the landing '
        'point moves closer to the point directly opposite the start.')
sol(35, 'raising the height reached in the same time',
    'h = ( v sin &theta; ) t &minus; &frac12; g t&sup2;\n'
    'for a fixed time t, h grows only if the vertical component ( v sin &theta; ) grows :\n\n'
    'Way 1 :  increase the speed of projection v , keeping the angle &theta; the same\n'
    'Way 2 :  increase the angle of projection &theta; towards 90&deg; , keeping v the same',
    'increase v , or increase &theta;  (both increase v sin &theta;)')

a('<div class="foot"><span>Lesson 1&ndash;1 &middot; Velocity Vectors and Relative Velocity &middot; Mr. Gemy</span>'
  '<span>v<sub>AB</sub> = v<sub>A</sub> &minus; v<sub>B</sub></span></div>')
a('</body></html>')
open('lesson.html', 'w', encoding='utf-8').write(''.join(H))
print('lesson.html written -', QN[0], 'questions')

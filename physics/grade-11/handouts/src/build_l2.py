# -*- coding: utf-8 -*-
import figs_l2 as F
import figs_bank as B
from docbase import Doc

d = Doc('Unit 1 &middot; Lesson 1&ndash;2', 'Horizontal<br>Projectile Motion',
        'Classwork, home assignments and the weekly assessment &mdash; fully worked, step by step.',
        ['Grade 11 &middot; Egyptian Baccalaureate', '25 questions', 'Step-by-step solutions',
         'g = 10 m/s&sup2; unless stated'], 'Horizontal Projectile Motion')

d.kit('The toolkit for this lesson', [
    ('a<sub>x</sub> = 0 &nbsp;,&nbsp; a<sub>y</sub> = g', 'the two motions are independent'),
    ('h = &frac12; g t&sup2;', 'vertical distance fallen'),
    ('t = &radic;( 2h / g )', 'time of flight &mdash; height only'),
    ('x = v t', 'horizontal range'),
    ('v<sub>y</sub> = g t', 'vertical component at any instant'),
    ('v = &radic;( v&sup2; + v<sub>y</sub>&sup2; )', 'speed at any instant'),
])
d.hint('<b>The one idea behind the whole lesson.</b> A horizontal projectile falls exactly like a body '
       'dropped from rest, while at the same time it travels horizontally with a <b>constant</b> velocity. '
       'So the <b>time of flight depends on the height only</b>, never on the launch speed.')

# ---------------- A ----------------
d.sec('A', 'Classwork &nbsp;1', 'Horizontal projectile motion')
d.q('The figure shows the path of a projectile fired horizontally from a cannon with an initial velocity '
    '<i>v</i> until it reaches the point B.', 'Concept',
    F.cannon_path('Figure 1 &nbsp;&middot;&nbsp; the path of a horizontal projectile'),
    parts=['<b>a)</b> At which of the points 1, 2 and 3 is the <b>horizontal</b> component of the velocity '
           'the greatest? Explain.',
           '<b>b)</b> At which of the points 1, 2 and 3 is the <b>vertical</b> component of the velocity '
           'the greatest? Explain.',
           '<b>c)</b> Write the relation used to calculate the horizontal distance AB.',
           '<b>d)</b> Write the relation used to calculate the vertical distance CB.',
           '<b>e)</b> If the projectile is fired from the same height with a doubled speed (2v), what happens '
           'to: <b>(1)</b> the time it takes to reach the ground? <b>(2)</b> its horizontal range?'])

d.q('A body is projected horizontally with a velocity of 14.7 m/s from a height of 19.6 m above the ground. '
    'Taking g = 9.8 m/s&sup2;, find:', 'Problem',
    F.cliff_drop('Figure 2', 'h = 19.6 m', 'v = 14.7 m/s'),
    parts=['<b>a)</b> the time the body takes to reach the ground, in seconds.',
           '<b>b)</b> the horizontal range of the body, in metres.',
           '<b>c)</b> the speed of the body just before it strikes the ground, in m/s.'])

# ---------------- B ----------------
d.sec('B', 'Home assignment &nbsp;1', 'The two independent motions')
d.q('The <b>horizontal</b> motion of a projectile launched horizontally from a certain height is '
    'characterised by:', 'MCQ',
    ch=['a constant acceleration', 'a constant velocity', 'an increasing acceleration', 'an increasing velocity'])
d.q('Doubling the initial horizontal velocity of a horizontal projectile, while keeping the height constant, '
    'leads to:', 'MCQ',
    ch=['doubling the time of flight', 'halving the time of flight',
        'doubling the horizontal range', 'increasing the horizontal range four times'])
d.q('A body is projected horizontally with a velocity of 4.0 m/s from a certain height and reaches the ground '
    'after 2.0 s. Calculate the height from which it was projected and its horizontal range.', 'Problem',
    F.cliff_drop('Figure 3', 'h = ?', 'v = 4 m/s', 'x = ?'))
d.q('What happens to the horizontal range of a horizontally projected body if the <b>height</b> of the point '
    'of projection increases while the initial horizontal velocity stays constant? Explain.', 'Explain')
d.q('A body is projected horizontally from the top of a building of height 45 m with an initial horizontal '
    'velocity of 20 m/s, neglecting air resistance and taking g = 10 m/s&sup2;. Calculate:', 'Problem',
    F.cliff_drop('Figure 4', 'h = 45 m', 'v = 20 m/s'),
    parts=['<b>1)</b> the time the body takes to reach the ground.',
           '<b>2)</b> the horizontal distance covered before it reaches the ground.'])

# ---------------- C ----------------
d.sec('C', 'Classwork &nbsp;2', 'The laws of horizontal projectiles')
d.q('Two projectiles are fired horizontally from two different heights as follows:', 'Ratios',
    F.two_heights('Figure 5', 'h = 20 m', 'v = 10 m/s', 'h = 80 m', 'v = 20 m/s'),
    parts=['<b>&#9675;</b> the first from a height of 20 m with a horizontal velocity of 10 m/s.',
           '<b>&#9675;</b> the second from a height of 80 m with a horizontal velocity of 20 m/s.',
           'Neglecting air resistance and taking g = 10 m/s&sup2;, <b>find the ratio between:</b>',
           '<b>1)</b> the time of flight of the first projectile and that of the second.',
           '<b>2)</b> the horizontal range of the first projectile and that of the second.'])
d.q('What happens to the time of flight and to the horizontal range of a body if it is projected horizontally '
    'from the <b>same height</b> but with a <b>greater</b> horizontal velocity? Explain.', 'Explain')

# ---------------- D ----------------
d.page()
d.sec('D', 'Home assignment &nbsp;2', 'More on the laws of horizontal projectiles')
d.q('The motion of a body projected horizontally from a certain height is characterised by:', 'MCQ',
    ch=['zero acceleration during the horizontal motion', 'zero acceleration during the vertical motion',
        'an acceleration equal to g during the horizontal motion',
        'an acceleration equal to &frac12; g during the vertical motion'])
d.q('What happens when the initial horizontal velocity of a horizontal projectile increases while the height '
    'is kept constant?', 'MCQ',
    ch=['the time of flight increases', 'the time of flight stays constant',
        'the horizontal range stays constant', 'the horizontal range decreases'])
d.q('Two projectiles are fired horizontally from two different heights: the first from a height <i>h</i> with '
    'an initial horizontal velocity <i>v</i>, and the second from a height <b>4h</b> with an initial '
    'horizontal velocity <b>2v</b>. Taking g as constant, find the ratio between:', 'Ratios',
    F.two_heights('Figure 6', 'h', 'v', '4h', '2v'),
    parts=['<b>1)</b> the time of flight of the first projectile and that of the second.',
           '<b>2)</b> the horizontal range of the first projectile and that of the second.'])
d.q('A billiard ball rolls off a table of height 0.60 m with an initial horizontal velocity of 2.4 m/s. '
    'Find the time the ball takes to hit the floor, and the horizontal distance between the edge of the table '
    'and the point where the ball lands.', 'Problem',
    B.table_proj('Figure 7', 'h = 0.60 m', 'v = 2.4 m/s', 'x = ?'))

# ---------------- E ----------------
d.sec('E', 'Weekly assessment &nbsp;2', 'Groups A, B and C')
d.grp('Group A')
d.q('A body is projected horizontally from the <b>fourth</b> floor of a building of ten floors. If the same '
    'body is projected horizontally from the <b>tenth</b> floor with the same initial horizontal velocity, '
    'then the time to reach the ground and the horizontal range respectively:', 'MCQ',
    F.building_floors('Figure 8'),
    ch=['stay constant &nbsp;&middot;&nbsp; stay constant', 'stay constant &nbsp;&middot;&nbsp; increase',
        'increase &nbsp;&middot;&nbsp; increase', 'increase &nbsp;&middot;&nbsp; stay constant'])
d.q('A helicopter flies horizontally with a velocity <i>v</i> at a height <i>h</i> and drops a food package so '
    'that it lands on a man standing on the ground. What is the distance between the helicopter and the man at '
    'the instant the package is released?', 'MCQ',
    F.helicopter('Figure 9'),
    ch=['&radic;( 2gh / v&sup2; + h&sup2; )', '&radic;( 2v&sup2;h / g + h&sup2; )',
        '&radic;( 2ghv&sup2; + h&sup2; )', '&radic;( ( 2ghv&sup2; + 1 ) / h&sup2; )'])
d.q('A body is projected horizontally with a velocity of 6.0 m/s from a certain height and reaches the ground '
    'after 3.0 s. Calculate the height from which it was projected and its horizontal range.', 'Problem',
    F.cliff_drop('Figure 10', 'h = ?', 'v = 6 m/s', 'x = ?'))
d.q('What happens to the time of flight and to the horizontal range of a body if it is projected horizontally '
    'from the same height but with a <b>smaller</b> horizontal velocity? Explain.', 'Explain')
d.q('A billiard ball rolls off a table of height 0.75 m with an initial horizontal velocity of 1.5 m/s. '
    'What is the horizontal distance between the edge of the table and the point where the ball lands?',
    'Problem', B.table_proj('Figure 11', 'h = 0.75 m', 'v = 1.5 m/s', 'x = ?'))

d.grp('Group B')
d.q('A body is projected horizontally from a certain height with an initial velocity <i>v</i>. If the initial '
    'horizontal velocity is doubled while the height is kept constant, the time the body takes to reach the '
    'ground:', 'MCQ', ch=['is doubled', 'is halved', 'does not change', 'becomes four times as large'])
d.q('The motion of a body projected horizontally from a certain height is characterised by:', 'MCQ',
    ch=['a positive acceleration during the horizontal motion',
        'a negative acceleration during the horizontal motion',
        'an acceleration equal to g during the vertical motion',
        'an acceleration equal to &frac14; g during the vertical motion'])
d.q('A body is projected horizontally from a height <i>h</i> with an initial horizontal velocity <i>v</i>, '
    'neglecting air resistance. What happens to the time it takes to reach the ground and to its horizontal '
    'range if the height is increased to <b>4h</b> while the initial horizontal velocity stays constant? '
    'Explain.', 'Explain')
d.q('The figure shows two coins A and B. Coin A is projected horizontally with an initial velocity '
    'v<sub>0</sub>, while coin B is released to fall freely from the same height at the same instant. '
    '<b>Which coin reaches the ground first?</b> Explain.', 'Explain', B.two_balls('Figure 12'))
d.q('A body is projected horizontally with a velocity of 8 m/s from a height of 30 m above the ground. '
    'Taking g = 10 m/s&sup2;, find:', 'Problem',
    F.cliff_drop('Figure 13', 'h = 30 m', 'v = 8 m/s'),
    parts=['<b>a)</b> the time the body takes to reach the ground, in seconds.',
           '<b>b)</b> the horizontal range of the body, in metres.'])

d.grp('Group C')
d.q('Halving the initial horizontal velocity of a horizontal projectile, while keeping the height constant, '
    'leads to:', 'MCQ',
    ch=['halving the time of flight', 'doubling the time of flight',
        'halving the horizontal range', 'doubling the horizontal range'])
d.q('The motion of a body projected horizontally from a certain height, while it is falling towards the '
    'ground, is characterised by:', 'MCQ',
    ch=['its horizontal velocity increases with time', 'its horizontal velocity decreases with time',
        'its vertical velocity decreases with time', 'its vertical velocity increases with time'])

# ============================ SOLUTIONS ============================
d.page()
d.sec('✓', 'Answer key', 'Solutions &mdash; step by step')
d.hint('Every question is solved in full. Remember the golden rule: <b>the vertical motion decides the time, '
       'the horizontal motion decides the range.</b>')

d.grp('Part A &mdash; Classwork 1')
d.sol(1, 'reading the path of a horizontal projectile',
      'a)  no force acts along the horizontal direction  &rarr;  a(x) = 0\n'
      '    so v(x) is the same at 1 , 2 and 3  (and at every point of the path)\n\n'
      'b)  the vertical motion is a free fall :  v(y) = g t\n'
      '    t is largest at point 3 , so v(y) is greatest at point 3\n\n'
      'c)  AB = v &times; t            (uniform horizontal motion)\n'
      'd)  CB = &frac12; g t&sup2;           (free fall from rest, vertically)\n\n'
      'e) 1)  t = &radic;( 2h / g )  does not contain v  &rarr;  the time does not change\n'
      '   2)  x = v t , with t unchanged  &rarr;  the range is doubled',
      'a) equal at 1, 2, 3 &nbsp;&middot;&nbsp; b) point 3 &nbsp;&middot;&nbsp; e) time unchanged, range doubled',
      why='This is the heart of the lesson: the two motions are completely independent, and only the height '
          'decides how long the flight lasts.')
d.sol(2, 'projectile from 19.6 m at 14.7 m/s &nbsp;(g = 9.8 m/s&sup2;)',
      'a)  h = &frac12; g t&sup2;   &rarr;   t = &radic;( 2h / g ) = &radic;( 2 &times; 19.6 / 9.8 ) = &radic;4 = 2 s\n'
      'b)  x = v t = 14.7 &times; 2 = 29.4 m\n'
      'c)  v(y) = g t = 9.8 &times; 2 = 19.6 m/s\n'
      '    v = &radic;( v&sup2; + v(y)&sup2; ) = &radic;( 14.7&sup2; + 19.6&sup2; ) = &radic;600.25 = 24.5 m/s',
      'a) 2 s &nbsp;&middot;&nbsp; b) 29.4 m &nbsp;&middot;&nbsp; c) 24.5 m/s')

d.grp('Part B &mdash; Home assignment 1')
d.sol(3, 'the horizontal motion', 'a(x) = 0  &rarr;  the horizontal velocity never changes',
      'B) a constant velocity')
d.sol(4, 'doubling the launch speed',
      't = &radic;( 2h / g )  is independent of v  &rarr;  t stays the same\n'
      'x = v t   &rarr;   doubling v doubles x', 'C) doubling the horizontal range')
d.sol(5, 'height and range from the time of flight',
      'h = &frac12; g t&sup2; = &frac12; &times; 10 &times; ( 2 )&sup2; = 20 m\n'
      'x = v t = 4 &times; 2 = 8 m', 'h = 20 m , x = 8 m')
d.sol(6, 'raising the point of projection',
      't = &radic;( 2h / g )   &rarr;   a larger h gives a larger t\n'
      'x = v t , with v unchanged   &rarr;   x increases',
      'the horizontal range increases',
      why='The body keeps the same horizontal speed, but it now stays in the air for a longer time, so it '
          'travels further before landing.')
d.sol(7, 'projectile from a 45 m building',
      '1)  t = &radic;( 2h / g ) = &radic;( 2 &times; 45 / 10 ) = &radic;9 = 3 s\n'
      '2)  x = v t = 20 &times; 3 = 60 m', 't = 3 s , x = 60 m')

d.grp('Part C &mdash; Classwork 2')
d.sol(8, 'two projectiles from 20 m and 80 m',
      'first :   t&#8321; = &radic;( 2 &times; 20 / 10 ) = &radic;4 = 2 s      x&#8321; = 10 &times; 2 = 20 m\n'
      'second :  t&#8322; = &radic;( 2 &times; 80 / 10 ) = &radic;16 = 4 s     x&#8322; = 20 &times; 4 = 80 m\n\n'
      '1)  t&#8321; : t&#8322; = 2 : 4 = 1 : 2\n'
      '2)  x&#8321; : x&#8322; = 20 : 80 = 1 : 4', '1) 1 : 2 &nbsp;&middot;&nbsp; 2) 1 : 4')
d.sol(9, 'same height, greater speed',
      't = &radic;( 2h / g )  does not contain v  &rarr;  the time of flight does not change\n'
      'x = v t   &rarr;   the range increases in the same ratio as v',
      'the time stays the same, the range increases',
      why='Two bodies leaving the same table with different speeds hit the floor at the same instant — '
          'only the landing points are different.')

d.grp('Part D &mdash; Home assignment 2')
d.sol(10, 'the acceleration of a horizontal projectile',
      'horizontally : no force  &rarr;  a(x) = 0\nvertically : the weight only  &rarr;  a(y) = g',
      'A) zero acceleration during the horizontal motion')
d.sol(11, 'increasing the launch speed', 't = &radic;( 2h / g )  is independent of v',
      'B) the time of flight stays constant')
d.sol(12, 'the two projectiles h , v and 4h , 2v',
      '1)  t&#8321; = &radic;( 2h / g )         t&#8322; = &radic;( 2 &times; 4h / g ) = 2 &radic;( 2h / g )\n'
      '    t&#8321; : t&#8322; = 1 : 2\n\n'
      '2)  x&#8321; = v t&#8321;                x&#8322; = 2v &times; t&#8322; = 2v &times; 2 t&#8321; = 4 v t&#8321;\n'
      '    x&#8321; : x&#8322; = 1 : 4', '1) 1 : 2 &nbsp;&middot;&nbsp; 2) 1 : 4',
      why='The time follows the <b>square root</b> of the height, so four times the height only doubles the '
          'time; the range then gains a second factor of 2 from the doubled speed.')
d.sol(13, 'the billiard ball',
      't = &radic;( 2h / g ) = &radic;( 2 &times; 0.60 / 10 ) = &radic;0.12 = 0.35 s\n'
      'x = v t = 2.4 &times; 0.35 = 0.83 m', 't = 0.35 s , x = 0.83 m')

d.grp('Part E &mdash; Weekly assessment 2 &nbsp;&middot;&nbsp; Group A')
d.sol(14, 'from the tenth floor instead of the fourth',
      'the tenth floor is higher  &rarr;  h increases\n'
      't = &radic;( 2h / g )   &rarr;   t increases\n'
      'x = v t , with v unchanged   &rarr;   x increases as well',
      'C) both the time and the range increase')
d.sol(15, 'the helicopter and the man',
      'the package needs   t = &radic;( 2h / g )   to fall\n'
      'in that time it travels horizontally   x = v t = v &radic;( 2h / g )\n'
      'at the instant of release the helicopter is exactly above the release point, so the\n'
      'distance to the man is the hypotenuse of a right angle :\n'
      'd = &radic;( x&sup2; + h&sup2; ) = &radic;( v&sup2; &times; 2h / g + h&sup2; ) = &radic;( 2v&sup2;h / g + h&sup2; )',
      'B) &radic;( 2v&sup2;h / g + h&sup2; )')
d.sol(16, 'height and range from t = 3 s',
      'h = &frac12; g t&sup2; = &frac12; &times; 10 &times; 9 = 45 m\nx = v t = 6 &times; 3 = 18 m', 'h = 45 m , x = 18 m')
d.sol(17, 'same height, smaller speed',
      't = &radic;( 2h / g )  &rarr;  unchanged\nx = v t  &rarr;  smaller v gives a smaller x',
      'the time stays the same, the range decreases')
d.sol(18, 'the billiard ball from 0.75 m',
      't = &radic;( 2 &times; 0.75 / 10 ) = &radic;0.15 = 0.387 s\nx = v t = 1.5 &times; 0.387 = 0.58 m',
      'x = 0.58 m &nbsp;( t = 0.39 s )')

d.grp('Group B')
d.sol(19, 'doubling the speed', 't = &radic;( 2h / g )  contains h and g only', 'C) it does not change')
d.sol(20, 'the vertical acceleration',
      'the only force acting is the weight, directed downwards  &rarr;  a(y) = g = 10 m/s&sup2;',
      'C) an acceleration equal to g during the vertical motion')
d.sol(21, 'raising the height from h to 4h',
      't&#8321; = &radic;( 2h / g )      t&#8322; = &radic;( 2 &times; 4h / g ) = 2 &radic;( 2h / g ) = 2 t&#8321;\n'
      'x&#8321; = v t&#8321;              x&#8322; = v t&#8322; = 2 v t&#8321; = 2 x&#8321;',
      'both the time and the range are doubled',
      why='Four times the height does not give four times the time, because the time depends on the '
          '<b>square root</b> of the height.')
d.sol(22, 'the projected coin and the dropped coin',
      'vertically the two coins start with v(y) = 0 and have the same a = g and the same h\n'
      'h = &frac12; g t&sup2;  gives the same t for both\n'
      'the horizontal velocity of A does not affect its vertical motion',
      'the two coins reach the ground at the same instant',
      why='This is the classic experiment that proves the independence of the two motions: A lands far away '
          'from the table, B lands just below it, but both land at the same moment.')
d.sol(23, 'projectile from 30 m at 8 m/s',
      'a)  t = &radic;( 2h / g ) = &radic;( 2 &times; 30 / 10 ) = &radic;6 = 2.45 s\n'
      'b)  x = v t = 8 &times; 2.45 = 19.6 m', 'a) 2.45 s &nbsp;&middot;&nbsp; b) 19.6 m')

d.grp('Group C')
d.sol(24, 'halving the launch speed',
      't is independent of v  &rarr;  unchanged\nx = v t  &rarr;  halving v halves x', 'C) halving the horizontal range')
d.sol(25, 'the velocity during the fall',
      'v(x) = v = constant          (no horizontal force)\nv(y) = g t  &rarr;  grows steadily with time',
      'D) its vertical velocity increases with time')

d.foot('Lesson 1&ndash;2 &middot; Horizontal Projectile Motion &middot; Mr. Gemy',
       't = &radic;(2h/g) &nbsp;&middot;&nbsp; x = v t')
d.save('l2.html')
print('l2.html written -', d.n, 'questions')

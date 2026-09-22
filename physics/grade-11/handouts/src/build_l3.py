# -*- coding: utf-8 -*-
import figs_l3 as F
from docbase import Doc

d = Doc('Unit 1 &middot; Lesson 1&ndash;3', 'Projectile Motion<br>at an Angle',
        'Two-dimensional motion &mdash; analysis, applications and the weekly assessment, fully worked.',
        ['Grade 11 &middot; Egyptian Baccalaureate', '27 questions', 'Step-by-step solutions',
         'g = 10 m/s&sup2; unless stated'], 'Projectile Motion at an Angle')

d.kit('The toolkit for this lesson', [
    ('v<sub>0x</sub> = v<sub>0</sub> cos &theta;', 'constant all the way'),
    ('v<sub>0y</sub> = v<sub>0</sub> sin &theta;', 'changes by g each second'),
    ('t<sub>up</sub> = v<sub>0</sub> sin &theta; / g', 'time to the highest point'),
    ('T = 2 v<sub>0</sub> sin &theta; / g', 'total time of flight'),
    ('H = v<sub>0</sub>&sup2; sin&sup2;&theta; / 2g', 'maximum height'),
    ('R = v<sub>0</sub>&sup2; sin 2&theta; / g', 'horizontal range'),
])
d.hint('<b>The rule of the lesson.</b> Split the initial velocity into a horizontal part that never changes '
       'and a vertical part that behaves exactly like a body thrown straight up. At the highest point '
       'v<sub>y</sub> = 0, but the body is still moving horizontally with v<sub>0</sub> cos &theta;.')

# ---------------- A ----------------
d.sec('A', 'Classwork &nbsp;1', 'Analysing the motion of a projectile fired at an angle')
d.q('The figure shows a body projected from the ground with an initial velocity v<sub>0</sub> at an angle '
    '&theta; to the horizontal. Write the relation used to calculate each of the following:', 'Derivations',
    F.traj_full('Figure 1 &nbsp;&middot;&nbsp; the complete path of a projectile fired at an angle'),
    parts=['<b>a)</b> the horizontal component of the initial velocity (v<sub>0x</sub>).',
           '<b>b)</b> the vertical component of the initial velocity (v<sub>0y</sub>).',
           '<b>At position (1):</b> &nbsp; <b>c)</b> the horizontal component v<sub>x1</sub> &nbsp;&middot;&nbsp; '
           '<b>d)</b> the vertical component v<sub>y1</sub> &nbsp;&middot;&nbsp; '
           '<b>e)</b> the magnitude of the resultant velocity v<sub>1</sub>.',
           '<b>f)</b> the horizontal distance X covered from the start up to position (1).',
           '<b>g)</b> the vertical height Y risen from the start up to position (1).',
           '<b>h)</b> the maximum height H reached by the body.',
           '<b>i)</b> the horizontal range R of the body.',
           '<b>j)</b> at position (2): the two components v<sub>x2</sub> and v<sub>y2</sub>.'])

# ---------------- B ----------------
d.sec('B', 'Home assignment &nbsp;1', 'The two motions of an angled projectile')
d.q('The <b>horizontal</b> motion of a projectile fired at an angle is characterised by:', 'MCQ',
    ch=['a constant acceleration', 'a constant velocity', 'an increasing acceleration', 'an increasing velocity'])
d.q('The horizontal acceleration of a projectile fired at an angle equals:', 'MCQ',
    ch=['zero', 'half the acceleration due to gravity', 'the acceleration due to gravity',
        'twice the acceleration due to gravity'])
d.q('A small ball is projected from the ground with an initial velocity of 15 m/s at 60&deg; to the horizontal. '
    'Neglecting air resistance and taking g = 10 m/s&sup2;, and knowing that the ball returns to the same '
    'level of projection, calculate:', 'Problem',
    F.ball_traj('Figure 2', 'v₀ = 15 m/s', 60),
    parts=['<b>a)</b> the time needed to reach the maximum height.', '<b>b)</b> the total time of flight.',
           '<b>c)</b> the horizontal range of the ball.', '<b>d)</b> the maximum height reached by the ball.'])

# ---------------- C ----------------
d.sec('C', 'Classwork &nbsp;2', 'Applications on projectiles fired at an angle')
d.q('The figure shows a body of mass <i>m</i> projected from the ground with an initial velocity '
    'v<sub>0</sub> at 60&deg; to the horizontal, neglecting air resistance. '
    '<b>Write two different ways to increase the total time of flight</b> of the body.', 'Explain',
    F.axes_traj('Figure 3', 60, 'v₀'))
d.q('For the same body of the previous question, write <b>two different ways</b> to increase the maximum '
    'height reached by the body.', 'Explain')
d.q('For the same body, write <b>two different ways</b> to increase the horizontal range of the body.',
    'Explain')
d.q('What is the angle of projection needed for the body to reach its <b>greatest possible horizontal '
    'range</b>, keeping the initial speed constant? Explain.', 'Explain')
d.q('What other angle of projection, used instead of 60&deg;, gives the body the <b>same horizontal range</b> '
    'shown in the figure, keeping the initial speed constant? Explain.', 'Explain',
    F.two_angles('Figure 4'))

# ---------------- D ----------------
d.page()
d.sec('D', 'Home assignment &nbsp;2', 'The vertical motion and a full calculation')
d.q('The <b>upward vertical</b> motion of a projectile fired at an angle is characterised by:', 'MCQ',
    ch=['a decreasing acceleration', 'a decreasing velocity', 'an increasing acceleration',
        'an increasing velocity'])
d.q('At the maximum height, the vertical component of the velocity of a projectile fired at an angle equals:',
    'MCQ', ch=['zero', 'a maximum value', 'half the initial vertical component',
               'the same as the initial vertical component'])
d.q('A small ball is projected from the ground with an initial velocity of 20 m/s at 60&deg; to the horizontal. '
    'Neglecting air resistance and taking g = 9.8 m/s&sup2;, and knowing that the ball returns to the same '
    'level of projection, calculate:', 'Problem',
    F.ball_traj('Figure 5', 'v₀ = 20 m/s', 60),
    parts=['<b>a)</b> the time needed to reach the maximum height.', '<b>b)</b> the total time of flight.',
           '<b>c)</b> the horizontal range of the ball.', '<b>d)</b> the maximum height reached by the ball.'])

# ---------------- E ----------------
d.sec('E', 'Weekly assessment &nbsp;3', 'Groups A, B and C')
d.grp('Group A')
d.q('At the maximum height, the magnitude of the velocity of a projectile fired at an angle equals:', 'MCQ',
    ch=['zero', 'a maximum value', 'the initial vertical component of the velocity',
        'the horizontal component of the initial velocity'])
d.q('A body is projected from the ground with a constant initial velocity v<sub>0</sub> at 30&deg; to the '
    'horizontal. At which other angle, with the same initial velocity, does it reach the same horizontal range?',
    'MCQ', F.two_angles('Figure 6'), ch=['30&deg;', '45&deg;', '60&deg;', '75&deg;'])
d.q('The figure shows a body of mass <i>m</i> projected from the ground with an initial velocity '
    'v<sub>0</sub> at 60&deg; to the horizontal. <b>Write a way to double the total time of flight</b> of the '
    'body, and explain it.', 'Explain', F.axes_traj('Figure 7', 60, 'v₀'))
d.q('A football is kicked with an initial velocity of 30 m/s at 60&deg; to the <b>vertical</b>. '
    'Find the horizontal range of the ball.', 'Problem',
    F.axes_traj('Figure 8', 30, 'v₀ = 30 m/s', from_vertical=True))
d.q('The figure shows a body projected from the top of a building of height 50 m with a velocity of 15 m/s at '
    '30&deg; to the horizontal. <b>What is the total time of flight</b> until the body reaches the ground?',
    'Problem', F.building_angle('Figure 9', 'h = 50 m', 'v₀ = 15 m/s', '30&deg;'))

d.grp('Group B')
d.q('When a body is projected at an angle to the horizontal, and air resistance is neglected, its '
    '<b>vertical</b> motion is characterised by:', 'MCQ',
    ch=['a constant velocity and zero acceleration', 'a varying velocity and a constant acceleration',
        'an increasing velocity and an increasing acceleration',
        'a constant velocity and a constant acceleration'])
d.q('A body is projected from the ground with an initial velocity v<sub>0</sub> at an angle &theta; to the '
    'horizontal. At which angle &theta; is the <b>maximum height equal to the horizontal range</b>?', 'MCQ',
    ch=['24&deg;', '45&deg;', '76&deg;', '90&deg;'])
d.q('For the body shown in Figure 7, write a way to <b>double the maximum height</b> reached by the body, '
    'and explain it.', 'Explain')
d.q('A football is kicked with an initial velocity of 25 m/s at 60&deg; to the horizontal. '
    'Find its total time of flight.', 'Problem')
d.q('A body is projected from the top of a building of height 50 m with a velocity of 15 m/s at 30&deg; to the '
    'horizontal. <b>What is the maximum height reached above the ground?</b>', 'Problem',
    F.building_angle('Figure 10', 'h = 50 m', 'v₀ = 15 m/s', '30&deg;'))

d.grp('Group C')
d.q('A body is projected with an initial velocity v<sub>0</sub> at an angle &theta; to the horizontal, '
    'neglecting air resistance. <b>What happens to the vertical velocity of the projectile while it rises?</b>',
    'MCQ', ch=['it increases continuously', 'it decreases gradually until it becomes zero at the highest point',
               'it stays constant', 'it becomes equal to the horizontal velocity'])
d.q('A body is projected from the ground with an initial velocity v<sub>0</sub> at an angle &theta; to the '
    'horizontal. Which angle of projection gives the projectile the <b>greatest horizontal range</b> without '
    'changing the speed of projection?', 'MCQ', ch=['30&deg;', '45&deg;', '60&deg;', '90&deg;'])
d.q('For the body shown in Figure 7, write a way to <b>double the horizontal range</b> reached by the body, '
    'and explain it.', 'Explain')
d.q('A football is kicked with an initial velocity of 20 m/s at 30&deg; to the <b>vertical</b>. '
    'Find the maximum height reached by the ball.', 'Problem',
    F.axes_traj('Figure 11', 60, 'v\u2080 = 20 m/s', from_vertical=True))
d.q('A body is projected from the top of a building of height 50 m with a velocity of 15 m/s at 30&deg; to the '
    'horizontal. <b>What is its horizontal range</b> measured from the base of the building?', 'Problem',
    F.building_angle('Figure 12', 'h = 50 m', 'v\u2080 = 15 m/s', '30&deg;'))

# ============================ SOLUTIONS ============================
d.page()
d.sec('✓', 'Answer key', 'Solutions &mdash; step by step')
d.hint('The whole lesson comes from two facts: the horizontal velocity never changes, and the vertical '
       'motion is a body thrown straight up with an initial speed v<sub>0</sub> sin &theta;.')

d.grp('Part A &mdash; Classwork 1')
d.sol(1, 'the relations that describe the whole path',
      'a)  v(0x) = v₀ cos θ                    (stays the same all the way)\n'
      'b)  v(0y) = v₀ sin θ\n\n'
      'at position (1) , after a time t₁ :\n'
      'c)  v(x1) = v₀ cos θ                    (no horizontal force)\n'
      'd)  v(y1) = v₀ sin θ − g t₁\n'
      'e)  v₁   = √( v(x1)² + v(y1)² )\n'
      'f)  X    = ( v₀ cos θ ) t₁\n'
      'g)  Y    = ( v₀ sin θ ) t₁ − ½ g t₁²\n\n'
      'h)  H    = ( v₀ sin θ )² / ( 2 g ) = v₀² sin²θ / ( 2 g )\n'
      'i)  R    = v₀² sin 2θ / g\n\n'
      'at position (2) , the highest point :\n'
      'j)  v(x2) = v₀ cos θ        and        v(y2) = 0',
      why='At the highest point only the vertical component vanishes; the body keeps moving horizontally, '
          'which is why its speed there is v<sub>0</sub> cos &theta; and not zero.')

d.grp('Part B &mdash; Home assignment 1')
d.sol(2, 'the horizontal motion', 'a(x) = 0  &rarr;  v(x) never changes', 'B) a constant velocity')
d.sol(3, 'the horizontal acceleration',
      'gravity acts vertically only, so it has no horizontal component', 'A) zero')
d.sol(4, 'ball projected at 15 m/s , 60&deg; &nbsp;(g = 10)',
      'v(0x) = 15 cos 60° = 15 × 0.5  = 7.5 m/s\n'
      'v(0y) = 15 sin 60° = 15 × 0.866 = 12.99 m/s\n\n'
      'a)  t(up) = v(0y) / g = 12.99 / 10 = 1.3 s\n'
      'b)  T = 2 t(up) = 2.6 s\n'
      'c)  R = v(0x) × T = 7.5 × 2.6 = 19.5 m\n'
      'd)  H = v(0y)² / ( 2 g ) = 168.75 / 20 = 8.44 m',
      'a) 1.3 s &nbsp;&middot;&nbsp; b) 2.6 s &nbsp;&middot;&nbsp; c) 19.5 m &nbsp;&middot;&nbsp; d) 8.44 m')

d.grp('Part C &mdash; Classwork 2')
d.sol(5, 'doubling down on the time of flight',
      'T = 2 v₀ sin θ / g   &rarr;   T grows when ( v₀ sin θ ) grows\n\n'
      'Way 1 :  increase the speed of projection v₀ , keeping θ = 60°\n'
      'Way 2 :  increase the angle θ towards 90° , keeping v₀ the same',
      'increase v₀ , or increase θ')
d.sol(6, 'increasing the maximum height',
      'H = v₀² sin²θ / ( 2 g )\n\n'
      'Way 1 :  increase v₀  (H grows with the square of the speed)\n'
      'Way 2 :  increase θ towards 90°', 'increase v₀ , or increase θ')
d.sol(7, 'increasing the horizontal range',
      'R = v₀² sin 2θ / g\n\n'
      'Way 1 :  increase v₀\n'
      'Way 2 :  bring the angle closer to 45° (here : decrease θ from 60° towards 45°),\n'
      '         because sin 2θ is a maximum at θ = 45°', 'increase v₀ , or move θ towards 45°')
d.sol(8, 'the angle of maximum range',
      'R = v₀² sin 2θ / g  is a maximum when  sin 2θ = 1\n2θ = 90°   &rarr;   θ = 45°', 'θ = 45°',
      why='At 45&deg; the speed is shared equally between the horizontal and the vertical directions, which is '
          'the best compromise between staying long in the air and moving fast forward.')
d.sol(9, 'the angle that gives the same range',
      'two angles give the same range when they are <b>complementary</b> :\n'
      'sin 2( 90° − θ ) = sin ( 180° − 2θ ) = sin 2θ\n'
      '90° − 60° = 30°', 'θ = 30°',
      why='The 30&deg; throw is flatter and faster, the 60&deg; throw is higher and slower, and the two effects '
          'cancel exactly in the range.')

d.grp('Part D &mdash; Home assignment 2')
d.sol(10, 'the upward vertical motion',
      'v(y) = v₀ sin θ − g t   &rarr;   the vertical velocity decreases steadily\n'
      'while the acceleration stays constant ( = g )', 'B) a decreasing velocity')
d.sol(11, 'at the maximum height', 'the body stops rising, so  v(y) = 0', 'A) zero')
d.sol(12, 'ball projected at 20 m/s , 60&deg; &nbsp;(g = 9.8)',
      'v(0x) = 20 cos 60° = 10 m/s\n'
      'v(0y) = 20 sin 60° = 17.32 m/s\n\n'
      'a)  t(up) = 17.32 / 9.8 = 1.77 s\n'
      'b)  T = 2 × 1.77 = 3.54 s\n'
      'c)  R = 10 × 3.54 = 35.4 m\n'
      'd)  H = 17.32² / ( 2 × 9.8 ) = 300 / 19.6 = 15.3 m',
      'a) 1.77 s &nbsp;&middot;&nbsp; b) 3.54 s &nbsp;&middot;&nbsp; c) 35.4 m &nbsp;&middot;&nbsp; d) 15.3 m')

d.grp('Part E &mdash; Weekly assessment 3 &nbsp;&middot;&nbsp; Group A')
d.sol(13, 'the speed at the top',
      'at the highest point  v(y) = 0 , so\nv = v(x) = v₀ cos θ',
      'D) the horizontal component of the initial velocity')
d.sol(14, 'the complementary angle', '90° − 30° = 60°  gives the same range', 'C) 60&deg;')
d.sol(15, 'doubling the time of flight',
      'T = 2 v₀ sin θ / g ,  with θ fixed at 60° :   T is proportional to v₀\n'
      'so the speed of projection must be doubled  ( v₀ → 2 v₀ )',
      'double the initial speed of projection',
      why='Raising the angle cannot do it here: T would need sin &theta; to double, and 2 sin 60&deg; is '
          'greater than 1, which is impossible for any angle.')
d.sol(16, 'an angle measured from the vertical',
      'the angle with the horizontal = 90° − 60° = 30°\n'
      'R = v₀² sin 2θ / g = ( 30 )² × sin 60° / 10\n'
      'R = 900 × 0.866 / 10 = 77.9 m', 'R = 77.9 m',
      why='Always convert an angle given with the vertical into an angle with the horizontal before using the '
          'projectile relations.')
d.sol(17, 'projected from the top of a building',
      'v(0x) = 15 cos 30° = 12.99 m/s        v(0y) = 15 sin 30° = 7.5 m/s\n\n'
      'taking upwards as positive, the final vertical displacement is − 50 m :\n'
      '− 50 = 7.5 t − 5 t²\n'
      '5 t² − 7.5 t − 50 = 0      ÷ 5   &rarr;   t² − 1.5 t − 10 = 0\n'
      't = [ 1.5 + √( 2.25 + 40 ) ] / 2 = ( 1.5 + 6.5 ) / 2 = 4 s', 'T = 4 s',
      why='T = 2 v<sub>0</sub> sin &theta; / g cannot be used here, because the body does not return to the '
          'level it started from.')

d.grp('Group B')
d.sol(18, 'the vertical motion',
      'v(y) changes every second, while a = g is constant in size and direction',
      'B) a varying velocity and a constant acceleration')
d.sol(19, 'when the height equals the range',
      'H = R\n'
      'v₀² sin²θ / ( 2 g ) = v₀² sin 2θ / g = 2 v₀² sin θ cos θ / g\n'
      'sin²θ = 4 sin θ cos θ    &rarr;    tan θ = 4\n'
      'θ = 76°', 'C) 76&deg;')
d.sol(20, 'doubling the maximum height',
      'H = v₀² sin²θ / ( 2 g ) ,  with θ fixed :   H is proportional to v₀²\n'
      'to double H :   v₀² must double   &rarr;   v₀ × √2  ( about 1.41 v₀ )',
      'multiply the speed of projection by √2',
      why='Doubling the speed itself would make the height <b>four</b> times as large, not twice.')
d.sol(21, 'time of flight of the football',
      'v(0y) = 25 sin 60° = 21.65 m/s\nT = 2 v(0y) / g = 2 × 21.65 / 10 = 4.33 s', 'T = 4.33 s')
d.sol(22, 'the maximum height above the ground',
      'v(0y) = 15 sin 30° = 7.5 m/s\n'
      'height risen above the roof :  H = v(0y)² / ( 2 g ) = 56.25 / 20 = 2.81 m\n'
      'height above the ground = 50 + 2.81 = 52.81 m', 'h(max) = 52.81 m above the ground',
      why='The relation for H always measures the rise <b>above the point of projection</b>, so the height of '
          'the building must be added afterwards.')

d.grp('Group C')
d.sol(23, 'the vertical velocity while rising',
      'v(y) = v₀ sin θ − g t  keeps falling until it reaches zero at the top',
      'B) it decreases gradually until it becomes zero at the highest point')
d.sol(24, 'the angle of greatest range',
      'R = v₀² sin 2θ / g  is a maximum when 2θ = 90°', 'B) 45&deg;')

d.sol(25, 'doubling the horizontal range',
      'R = v\u2080\u00b2 sin 2\u03b8 / g ,  with \u03b8 fixed at 60\u00b0 :   R is proportional to v\u2080\u00b2\n'
      'to double R :   v\u2080\u00b2 must double   &rarr;   v\u2080 \u00d7 \u221a2',
      'multiply the speed of projection by \u221a2',
      why='Changing the angle alone cannot double it: the largest possible value of sin 2&theta; is 1, while '
          'sin 120&deg; is already 0.87, so the angle can add at most about 15 %.')
d.sol(26, 'kicked at 30&deg; to the vertical',
      'the angle with the horizontal = 90\u00b0 \u2212 30\u00b0 = 60\u00b0\n'
      'v(0y) = 20 sin 60\u00b0 = 17.32 m/s\n'
      'H = v(0y)\u00b2 / ( 2 g ) = 300 / 20 = 15 m', 'H = 15 m')
d.sol(27, 'the range from the top of the building',
      'v(0x) = 15 cos 30\u00b0 = 12.99 m/s\n'
      'the total time of flight was found in question 17 :  t = 4 s\n'
      'x = v(0x) \u00d7 t = 12.99 \u00d7 4 = 51.96 m', 'x \u2248 52 m')

d.foot('Lesson 1&ndash;3 &middot; Projectile Motion at an Angle &middot; Mr. Gemy',
       'H = v₀&sup2;sin&sup2;&theta;/2g &nbsp;&middot;&nbsp; R = v₀&sup2;sin2&theta;/g')
d.save('l3.html')
print('l3.html written -', d.n, 'questions')

# -*- coding: utf-8 -*-
import figs_l11 as F
from docbase import Doc

d = Doc('Unit 1 &middot; Lesson 1&ndash;11', 'Horizontal and Vertical<br>Circular Motion',
        'The conical pendulum, motion inside a conical vessel, and a body whirled in a vertical circle.',
        ['Grade 11 &middot; Egyptian Baccalaureate', '27 questions', 'Step-by-step solutions',
         'g = 9.8 m/s&sup2;'], 'Horizontal and Vertical Circular Motion')

d.kit('The toolkit for this lesson', [
    ('T cos &theta; = mg', 'conical pendulum &mdash; vertical'),
    ('T sin &theta; = m v&sup2; / r', 'conical pendulum &mdash; horizontal'),
    ('r = l sin &theta;', 'radius of the horizontal circle'),
    ('top : T + mg = m v&sup2; / r', 'both forces point to the centre'),
    ('bottom : T &minus; mg = m v&sup2; / r', 'the tension is largest here'),
    ('v(min) = &radic;( g r )', 'at the top, when T = 0'),
])
d.hint('<b>One habit solves this whole lesson.</b> Draw the body at the position asked about, mark every '
       'force, then ask: <i>which way is the centre?</i> The resultant along that direction is always '
       'm v&sup2; / r &mdash; nothing else.')

# ---------------- A ----------------
d.sec('A', 'Classwork &nbsp;1', 'The vertical circular path')
d.q('The minimum value of the speed needed at the highest point of a vertical circular path of radius r, so '
    'that the body keeps moving on its circular path (that is, the tension in the string becomes T = 0), is '
    'given by the relation:', 'MCQ', F.vertical_circle('Figure 1'),
    ch=['v(min) = &radic;( 2 g r )', 'v(min) = &radic;( g r )', 'v(min) = g r',
        'v(min) = &radic;( g / r )'])
d.q('<b>Determine the reason</b> why the water stays inside a bucket that is whirled in a vertical circular '
    'path, even at the instant when the bucket is upside down at the highest point of the path.', 'Explain',
    F.bucket_water('Figure 2'))
d.q('A small ball of mass 0.50 kg is tied to a string and moves in a vertical circular path of radius 0.80 m. '
    'At the lowest point of the path its speed is 4.0 m/s. <b>Calculate the tension in the string at this '
    'point.</b>', 'Problem')

# ---------------- B ----------------
d.sec('B', 'Home assignment &nbsp;1', 'The conical vessel and the minimum speed')
d.q('A small ball moves in uniform circular motion at a height h inside a vessel with a smooth conical inner '
    'surface, where the axis of the cone makes an angle &theta; with the slant (generating) line of the cone.',
    'Problem', F.conical_vessel('Figure 3'),
    parts=['<b>a)</b> Determine the normal force N acting on the ball, in terms of m, &theta; and g.',
           '<b>b)</b> Determine the speed of the ball, in terms of h and g.'])
d.q('A small ball of mass 0.50 kg is tied to a string and whirled in a vertical circular path of radius '
    '0.80 m. <b>Determine the minimum speed needed at the highest point</b> of the circular path so that the '
    'string remains taut.', 'Problem')
d.q('<b>Explain why</b> the water in the whirling-bucket experiment begins to spill first at the <b>upper</b> '
    'part of the circular path rather than at the lower part.', 'Explain')

# ---------------- C ----------------
d.sec('C', 'Classwork &nbsp;2', 'The conical pendulum')
d.q('A small ball of mass 0.40 kg is tied to a string and moves in a vertical circle of radius 0.60 m. '
    'At the lowest point of the circle its speed is 4.0 m/s. The tension in the string at the lowest point '
    'equals:', 'MCQ', ch=['12.6 N', '13.4 N', '14.6 N', '15.4 N'])
d.q('<b>Describe the forces</b> acting on a conical pendulum, and <b>determine which component</b> of the '
    'tension force provides the centripetal force.', 'Explain', F.conical_pendulum('Figure 4'))
d.q('A small ball moves in uniform circular motion on the smooth inner surface of a conical vessel, along a '
    'horizontal circular path of radius r, where the slant side of the cone makes an angle &theta; with the '
    'horizontal plane.', 'Problem',
    parts=['<b>a)</b> Write the equation of vertical equilibrium for the ball.',
           '<b>b)</b> Write the equation of the centripetal force acting on the ball.'])

# ---------------- D ----------------
d.page()
d.sec('D', 'Home assignment &nbsp;2', 'Tension, normal force and the loop')
d.q('One end of a string of length 1 m is fixed to the ceiling, and a small ball of mass 0.5 kg tied to its '
    'other end moves in uniform circular motion in a smooth horizontal plane. If the angle between the string '
    'and the vertical is 30&deg; and g = 9.8 m/s&sup2;, then the tension in the string is approximately:',
    'MCQ', ch=['4.90 N', '5.66 N', '2.54 N', '9.80 N'])
d.q('One end of a string of length <i>l</i> is fixed to the ceiling, and a ball of mass m tied to its other '
    'end moves in uniform circular motion in a horizontal plane, so that the string makes an angle &theta; '
    'with the vertical and the angular velocity is &omega;.', 'Problem',
    parts=['<b>a)</b> Determine the tension in the string.',
           '<b>b)</b> Determine the normal force acting on the ball if it also rests on a horizontal surface.'])
d.q('<b>Explain why</b> a car that almost loses contact with the track at the top of a circular loop is '
    'subjected to a very large normal force at the bottom of the loop.', 'Explain', F.loop_track('Figure 5'))

# ---------------- E ----------------
d.sec('E', 'Weekly assessment', 'Groups A, B and C')
d.grp('Group A')
d.q('At the highest point of a vertical circular path, the resultant of the tension force (T) and the weight '
    '(mg) must be directed:', 'MCQ',
    ch=['tangentially, in the direction of motion', 'directly away from the centre of the circle',
        'directly towards the centre of the circle', 'vertically upwards, balancing gravity'])
d.q('The tension in a string whirling a body in a vertical circular path reaches its <b>maximum</b> value at:',
    'MCQ', ch=['the highest point of the path', 'the lowest point of the path',
               'the horizontal position level with the centre', 'the point at which the speed is zero'])
d.q('<b>Evaluate and discuss</b> the correctness of the following statement: &ldquo;The minimum value of the '
    'speed at the top of a vertical circular path occurs when the normal force (or the tension) becomes '
    'infinite.&rdquo;', 'Explain')
d.q('A stone tied to a string moves in a horizontal circular path with a constant speed v. The figure shows '
    'the stone at two different positions X and Y. <b>Show, by drawing, the direction of the change in the '
    'velocity</b> of the stone as it moves from position X to position Y.', 'Explain',
    F.semicircle_path('Figure 6'))
d.q('A body moves with an initial speed v<sub>0</sub> along a semicircular path from A, passing through B and '
    'C as shown. If the radius of the path is reduced to half while the initial speed v<sub>0</sub> stays '
    'constant, <b>what happens to the speed of the body at the point B?</b>', 'Explain')

d.grp('Group B')
d.q('In vertical circular motion, the minimum speed at the highest point of the loop is derived from the '
    'physical condition that the tension in the string becomes:', 'MCQ',
    ch=['equal to twice the weight', 'zero &nbsp;(T = 0)', 'equal to the centripetal force only', 'infinite'])
d.q('A real roller-coaster loop is designed as a teardrop-shaped curve rather than a complete circle, in '
    'order to:', 'MCQ',
    ch=['increase the maximum speed at the top',
        'change the radius of curvature gradually and control the centripetal acceleration on the riders',
        'cancel the gravitational force completely',
        'keep the force on the track constant all along the path'])
d.q('<b>Analyse the forces</b> acting on a conical pendulum, and explain why the <b>horizontal</b> component '
    'of the tension &mdash; and not the vertical component &mdash; is the one that provides the centripetal '
    'force.', 'Explain')
d.q('What happens in each of the following cases?', 'Explain',
    parts=['<b>a)</b> whirling a bucket of water in a vertical circular path too slowly to maintain the '
           'speed required at the highest point.',
           '<b>b)</b> increasing the angle that the string of a conical pendulum makes with the vertical.'])
d.q('A mass of 0.60 kg is tied to a string of length 1.0 m and rotates in a vertical circular path. '
    '<b>Determine the minimum speed at the highest point</b> of the path needed to keep the string taut.',
    'Problem')

d.grp('Group C')
d.q('In a conical pendulum, the component of the tension force that provides the required centripetal force '
    'is:', 'MCQ', ch=['T cos &theta; &nbsp;(the vertical component)',
                      'T sin &theta; &nbsp;(the horizontal component)', 'T tan &theta;',
                      'the whole tension T acting vertically'])
d.q('<b>Explain the effect</b> of the tension force and the gravitational force acting in the <b>same</b> '
    'direction at the highest point of a vertical circular path.', 'Explain')
d.q('<b>Discuss the wrong idea</b> which says that &ldquo;the water spills out of a bucket whirled too slowly '
    'in a vertical circle because of an outward centrifugal force&rdquo;. Give the correct physical '
    'explanation, based on the concept of inertia.', 'Explain')
d.q('State the reason for each of the following:', 'Explain',
    parts=['<b>a)</b> roller-coaster loops are designed as teardrop-shaped curves instead of perfect circles.',
           '<b>b)</b> the tension in the string whirling a ball in a vertical circular path has its maximum '
           'value at the lowest point of the path.'])
d.q('A conical pendulum consists of a bob of mass 0.30 kg hanging from a string of length 0.80 m, making an '
    'angle of 30&deg; with the vertical.', 'Problem',
    parts=['<b>a)</b> Calculate the tension in the string.', '<b>b)</b> Calculate the speed of the bob.'])

# ============================ SOLUTIONS ============================
d.page()
d.sec('✓', 'Answer key', 'Solutions &mdash; step by step')
d.hint('For a vertical circle, remember that the <b>speed changes</b> around the loop (energy conservation), '
       'while for a conical pendulum the speed is constant and the two equilibrium equations do all the work.')

d.grp('Part A &mdash; Classwork 1')
d.sol(1, 'the minimum speed at the top',
      'at the highest point both the tension and the weight point downwards, towards the centre :\n'
      '    T + mg = m v² / r\n'
      'the slowest possible motion is the one in which the string is just about to go slack, T = 0 :\n'
      '    mg = m v² / r      &rarr;      v² = g r      &rarr;      v(min) = √( g r )',
      'B) v(min) = &radic;( g r )')
d.sol(2, 'why the water does not fall out',
      'at the top the water needs a downward force of  m v² / r  to stay on its circular path.\n'
      'gravity supplies mg, and the bottom of the bucket supplies whatever is still missing.\n'
      'as long as  v² / r ≥ g  ( that is v ≥ √(g r) ), the weight is not more than what the\n'
      'circular path needs, so the water never gets the chance to fall away from the bucket.',
      'because gravity is being used up as the centripetal force needed for the circular path',
      why='The water <b>is</b> falling all the time — it simply falls along the circle, and the bucket '
          'falls with it.')
d.sol(3, 'tension at the lowest point',
      'at the lowest point the tension points up (to the centre) and the weight points down :\n'
      '    T − mg = m v² / r\n'
      '    T = m ( g + v² / r ) = 0.50 ( 9.8 + 16 / 0.80 )\n'
      '    T = 0.50 ( 9.8 + 20 ) = 0.50 × 29.8 = 14.9 N', 'T = 14.9 N',
      why='The tension is about three times the weight of the ball ( mg = 4.9 N ) — this is why strings '
          'snap at the bottom of the swing, never at the top.')

d.grp('Part B &mdash; Home assignment 1')
d.sol(4, 'the ball inside the conical vessel',
      'the surface is smooth, so only two forces act : the weight mg and the normal force N,\n'
      'which is perpendicular to the slant side. with θ measured between the axis and the slant :\n\n'
      'a)  vertical :     N sin θ = mg        &rarr;    N = mg / sin θ\n\n'
      'b)  horizontal :   N cos θ = m v² / r\n'
      '    ( mg / sin θ ) cos θ = m v² / r      &rarr;    v² = g r cot θ\n'
      '    and from the geometry of the cone :  r = h tan θ\n'
      '    v² = g ( h tan θ ) cot θ = g h      &rarr;    v = √( g h )',
      'N = mg / sin &theta; &nbsp;,&nbsp; v = &radic;( g h )',
      why='The neat result is that the speed depends on the <b>height</b> only, not on the angle of the cone '
          'nor on the mass.')
d.sol(5, 'the minimum speed for a taut string',
      'v(min) = √( g r ) = √( 9.8 × 0.80 ) = √7.84 = 2.8 m/s', 'v(min) = 2.8 m/s')
d.sol(6, 'where the water spills first',
      'at the top the only force available is the weight, and the path needs m v² / r.\n'
      'if v² / r < g the weight is more than the circle needs, so the water leaves the\n'
      'circular path and falls out.\n'
      'at the bottom the bucket can push the water inwards as hard as necessary\n'
      '( T − mg = m v² / r ), so there is no tendency to spill there.',
      'because the top is the only place where gravity alone has to supply the centripetal force')

d.grp('Part C &mdash; Classwork 2')
d.sol(7, 'tension at the lowest point',
      'T = m ( g + v² / r ) = 0.40 ( 9.8 + 16 / 0.60 )\n'
      'T = 0.40 ( 9.8 + 26.7 ) = 0.40 × 36.5 = 14.6 N', 'C) 14.6 N')
d.sol(8, 'the forces on a conical pendulum',
      'only two forces act on the bob :\n'
      '   the weight mg , vertically downwards\n'
      '   the tension T , along the string\n\n'
      'the bob has no vertical acceleration, so the vertical parts must cancel :\n'
      '   T cos θ = mg\n'
      'the bob does accelerate horizontally, towards the centre of its circle :\n'
      '   T sin θ = m v² / r',
      'the horizontal component T sin &theta; supplies the centripetal force',
      why='The weight has no horizontal part at all, so the only candidate left for the centripetal force is '
          'the horizontal component of the tension.')
d.sol(9, 'the equations for the conical vessel',
      'here θ is measured between the slant side and the <b>horizontal</b>, so the normal force\n'
      'makes the angle θ with the vertical :\n\n'
      'a)  vertical equilibrium :   N cos θ = mg\n'
      'b)  centripetal force   :   N sin θ = m v² / r',
      'N cos &theta; = mg &nbsp;,&nbsp; N sin &theta; = m v&sup2; / r',
      why='Dividing the second equation by the first gives tan &theta; = v&sup2; / (r g), which is the same '
          'relation as for the conical pendulum.')

d.grp('Part D &mdash; Home assignment 2')
d.sol(10, 'the tension in the string',
      'the ball has no vertical acceleration :\n'
      'T cos 30° = mg = 0.5 × 9.8 = 4.9 N\n'
      'T = 4.9 / 0.866 = 5.66 N', 'B) 5.66 N')
d.sol(11, 'tension and normal force together',
      'the radius of the circle is  r = l sin θ\n\n'
      'a)  horizontal :  T sin θ = m ω² r = m ω² l sin θ\n'
      '    T = m ω² l            ( the angle cancels out )\n\n'
      'b)  vertical :    T cos θ + N = mg\n'
      '    N = mg − T cos θ = m ( g − ω² l cos θ )',
      'T = m &omega;&sup2; l &nbsp;,&nbsp; N = m ( g &minus; &omega;&sup2; l cos &theta; )',
      why='As &omega; grows, N falls; when &omega;&sup2; l cos &theta; reaches g the ball leaves the surface '
          'altogether and the problem becomes an ordinary conical pendulum.')
d.sol(12, 'the large force at the bottom of the loop',
      'at the top ( just keeping contact ) :   N ≈ 0   and   v(top)² = g r\n'
      'from the top to the bottom the car falls a height 2r, so by conservation of energy :\n'
      '    v(bottom)² = v(top)² + 4 g r = g r + 4 g r = 5 g r\n\n'
      'at the bottom :   N − mg = m v(bottom)² / r = 5 mg\n'
      '    N = 6 mg',
      'the normal force at the bottom is about six times the weight',
      why='Two effects add up: the car is moving much faster at the bottom, and the track must also carry '
          'the whole weight there instead of being helped by it.')

d.grp('Part E &mdash; Weekly assessment &middot; Group A')
d.sol(13, 'the direction of the resultant at the top',
      'the body is moving on a circle, so its acceleration — and the resultant force —\n'
      'must point towards the centre, which at the highest point means straight down.',
      'C) directly towards the centre of the circle')
d.sol(14, 'where the tension is largest',
      'bottom :  T = m ( g + v²/r )     top :  T = m ( v²/r − g )\n'
      'the speed is also largest at the bottom, so both effects push T to its maximum there.',
      'B) at the lowest point of the path')
d.sol(15, 'judging the statement',
      'the statement is <b>wrong</b>.\n'
      'the minimum speed at the top is obtained by letting the tension ( or the normal\n'
      'force ) fall to <b>zero</b>, not grow to infinity :\n'
      '    T = 0   &rarr;   mg = m v² / r   &rarr;   v(min) = √( g r )\n'
      'an infinite force is physically impossible, and a larger force would mean a larger\n'
      'speed, not a smaller one.',
      'wrong — the correct condition is T = 0, giving v(min) = √( g r )')
d.sol(16, 'the change of velocity between two positions',
      'the speed is the same at X and at Y, but the <b>directions</b> differ.\n'
      'Δv = v(Y) − v(X) , which is drawn by reversing v(X) and adding it to v(Y).\n'
      'the resulting arrow points <b>into</b> the circle, along the bisector of the two\n'
      'positions, and for a quarter of a circle its length is v√2.',
      'Δv points towards the inside of the path, with magnitude v√2 for a quarter circle',
      why='This is the geometric reason why the acceleration of uniform circular motion points to the centre.')
d.sol(17, 'halving the radius of the path',
      'from A to B the body rises a height equal to the radius, so by energy conservation :\n'
      '    v(B)² = v₀² − 2 g r\n'
      'if r becomes r/2 with v₀ unchanged :\n'
      '    v(B)² = v₀² − g r      ( a smaller amount is subtracted )',
      'the speed at B increases',
      why='A smaller loop means less height to climb, so less kinetic energy is converted into potential '
          'energy on the way up.')

d.grp('Group B')
d.sol(18, 'the condition used in the derivation',
      'the string can only pull; the slowest circular motion is the one in which it is\n'
      'just about to go slack, T = 0, leaving gravity alone to bend the path.', 'B) zero (T = 0)')
d.sol(19, 'why the loop is teardrop-shaped',
      'a circular loop would need a very large radius at the bottom entry, giving the riders\n'
      'a violent centripetal acceleration there. the teardrop ( clothoid ) shape changes the\n'
      'radius of curvature gradually, so a(c) = v² / r stays within safe limits everywhere.',
      'B) to change the radius of curvature gradually and control the centripetal acceleration')
d.sol(20, 'the analysis of the conical pendulum',
      'the weight mg is vertical, so it has <b>no horizontal component</b> at all.\n'
      'the bob moves in a horizontal circle, so the resultant force must be horizontal,\n'
      'pointing to the centre. the only horizontal force available is T sin θ.\n'
      'the vertical component T cos θ is fully used up in balancing the weight.',
      'T sin &theta; supplies the centripetal force ; T cos &theta; balances the weight')
d.sol(21, 'two changes',
      'a)  too slow at the top :  v² / r < g , so the weight is greater than the force the\n'
      '    circular path needs. the water can no longer follow the circle — it leaves the\n'
      '    bucket and falls as a projectile.\n\n'
      'b)  increasing θ :  r = l sin θ increases , T = mg / cos θ increases,\n'
      '    and since tan θ = v² / ( r g ) the speed must increase as well.',
      'a) the water spills out &nbsp;&middot;&nbsp; b) r , T and the required speed all increase')
d.sol(22, 'the minimum speed at the top',
      'v(min) = √( g r ) = √( 9.8 × 1.0 ) = 3.13 m/s', 'v(min) = 3.13 m/s',
      why='The mass does not appear: a heavy ball and a light ball need exactly the same minimum speed.')

d.grp('Group C')
d.sol(23, 'the component that turns the bob',
      'the circle is horizontal, so the centripetal force must be horizontal : T sin θ.',
      'B) T sin &theta; (the horizontal component)')
d.sol(24, 'both forces pointing the same way at the top',
      'at the highest point the tension and the weight are both directed downwards, i.e.\n'
      'both towards the centre, so they add :\n'
      '    T + mg = m v² / r      &rarr;      T = m ( v² / r − g )\n'
      'gravity is therefore <b>helping</b> to bend the path, which is why the tension is at its\n'
      'smallest there, and why a minimum speed exists at all.',
      'they add together, so T is smallest at the top and vanishes at v = &radic;(g r)')
d.sol(25, 'the centrifugal misconception',
      'there is no outward force acting on the water. the correct picture is inertia :\n'
      'the water tends to keep moving in a <b>straight line</b> ( Newton’s first law ), and the\n'
      'bucket must keep pulling it inwards to bend that line into a circle.\n'
      'when the bucket is too slow at the top, the inward force available ( the weight ) is\n'
      'larger than the circle needs, so the water follows a projectile path and separates\n'
      'from the bucket — it is not thrown outwards; it is simply left behind.',
      'no outward force exists — the water only keeps its straight-line inertia')
d.sol(26, 'two reasons',
      'a)  the teardrop shape lets the radius of curvature change gradually, keeping the\n'
      '    centripetal acceleration v² / r on the riders within safe limits.\n\n'
      'b)  at the lowest point T = m ( g + v² / r ) : the tension must both carry the weight\n'
      '    and bend the path, and the speed is also largest there.',
      'a) to control the g-forces &nbsp;&middot;&nbsp; b) T carries the weight and bends the path together')
d.sol(27, 'the conical pendulum with numbers',
      'a)  T cos 30° = mg = 0.30 × 9.8 = 2.94 N\n'
      '    T = 2.94 / 0.866 = 3.39 N\n\n'
      'b)  r = l sin 30° = 0.80 × 0.5 = 0.40 m\n'
      '    T sin 30° = m v² / r\n'
      '    3.39 × 0.5 = 0.30 v² / 0.40\n'
      '    1.70 = 0.75 v²      &rarr;      v² = 2.26      &rarr;      v = 1.50 m/s',
      'T = 3.39 N , v = 1.50 m/s',
      why='A quicker route for (b) is v&sup2; = g r tan &theta; = 9.8 &times; 0.40 &times; 0.577 = 2.26.')

d.foot('Lesson 1&ndash;11 &middot; Horizontal and Vertical Circular Motion &middot; Mr. Gemy',
       'T cos &theta; = mg &nbsp;&middot;&nbsp; v(min) = &radic;(g r)')
d.save('l11.html')
print('l11.html written -', d.n, 'questions')

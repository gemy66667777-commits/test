# -*- coding: utf-8 -*-
import figs_l10 as F
from docbase import Doc

d = Doc('Unit 1 &middot; Lesson 1&ndash;10', 'Uniform Circular Motion<br>and Centripetal Force',
        'Periodic time, frequency, angular velocity, centripetal acceleration and the force that keeps a '
        'body on its circular path.',
        ['Grade 11 &middot; Egyptian Baccalaureate', '21 questions', 'Step-by-step solutions',
         '&pi; = 3.14'], 'Uniform Circular Motion')

d.kit('The toolkit for this lesson', [
    ('T = time / number of revolutions', 'periodic time (s)'),
    ('f = 1 / T', 'frequency (Hz)'),
    ('&omega; = 2&pi; / T = 2&pi; f', 'angular velocity (rad/s)'),
    ('v = &omega; r = 2&pi;r / T', 'linear (tangential) speed'),
    ('a<sub>c</sub> = v&sup2; / r = &omega;&sup2; r', 'centripetal acceleration'),
    ('F<sub>c</sub> = m v&sup2; / r = m &omega;&sup2; r', 'centripetal force, towards the centre'),
])
d.hint('<b>The idea that the whole lesson turns on.</b> In uniform circular motion the <b>speed</b> never '
       'changes, but the <b>velocity</b> does, because its direction turns at every instant. A changing '
       'velocity means an acceleration, and that acceleration always points towards the centre.')

# ---------------- A ----------------
d.sec('A', 'Classwork &nbsp;2', 'Describing uniform circular motion')
d.q('Which of the following accurately describes uniform circular motion and the reason for the acceleration '
    'of the body that moves in this way?', 'MCQ', F.circle_motion('Figure 1'),
    ch=['the velocity vector is constant, so the acceleration equals zero',
        'the magnitude of the velocity changes while its direction stays constant',
        'the speed is constant, but the direction of the velocity changes continuously towards the centre',
        'the body is acted on by an outward centrifugal force that produces a tangential acceleration'])
d.q('A body moves in uniform circular motion, completing 10 revolutions in 2.0 s on a circular path of radius '
    '0.40 m.', 'Problem',
    parts=['<b>a)</b> Determine the periodic time of the body.',
           '<b>b)</b> Determine the angular velocity of the body.'])
d.q('A small ball of mass 0.50 kg is fixed to a string of length 2.0 m and moves in uniform circular motion '
    'with an angular velocity of 3.0 rad/s. <b>Calculate its centripetal acceleration.</b>', 'Problem',
    F.ball_string('Figure 2'))

# ---------------- B ----------------
d.sec('B', 'Home assignment &nbsp;2', 'Speed, force and a rotating spring')
d.q('A body moves in uniform circular motion, completing 20 revolutions in 5.0 s on a circular path of radius '
    '0.20 m.', 'Problem',
    parts=['<b>a)</b> Calculate the periodic time.', '<b>b)</b> Calculate the linear speed.'])
d.q('A small ball of mass 0.50 kg is fixed to a string of length 2.0 m and moves with an angular velocity of '
    '3.0 rad/s.', 'Problem',
    parts=['<b>a)</b> Determine its linear speed.',
           '<b>b)</b> Determine the magnitude of the force needed to maintain the circular motion.'])
d.q('A small ball of mass 0.50 kg is fixed to a spring of natural length 0.10 m and spring constant 30 N/m, '
    'and moves in a circular path with an angular velocity of 6.0 rad/s. '
    '<b>Determine the extension of the spring.</b>', 'Problem', F.spring_circular('Figure 3'))

# ---------------- C ----------------
d.page()
d.sec('C', 'Weekly assessment', 'Groups A, B and C')
d.grp('Group A')
d.q('The angular velocity (&omega;) of a body moving in a circular path is defined as:', 'MCQ',
    ch=['the linear displacement per unit time', 'the angular displacement per unit time',
        'the total number of revolutions in one second', 'the time taken to complete one full revolution'])
d.q('The centripetal force acting on a body of mass m moving in a circular path of radius r with a speed v is '
    'given by the relation:', 'MCQ',
    ch=['F = m v r', 'F = m v&sup2; / r', 'F = m v / r&sup2;', 'F = m&sup2; v / r'])
d.q('A horizontal disc rotates with a constant angular velocity of 4&pi; rad/s. The point A lies on the rim '
    'of the disc, at a distance of 0.30 m from the centre. Calculate:', 'Problem',
    F.rotating_disc('Figure 4'),
    parts=['<b>a)</b> the periodic time T.', '<b>b)</b> the linear speed of the point.'])
d.q('<b>Explain the physical mechanism</b> that makes the water leave the drum of a washing machine through '
    'the holes in its wall during the drying (fast spin) cycle.', 'Explain', F.washing_drum('Figure 5'))
d.q('A body of mass 3.0 kg moves in a circular path of radius 2.0 m, completing one revolution in 4.0 s. '
    '&nbsp;(&pi; = 3.14)', 'Problem',
    parts=['<b>a)</b> Determine the magnitude of its acceleration.',
           '<b>b)</b> Determine the magnitude of the centripetal force required.'])

d.grp('Group B')
d.q('The periodic time (T) of a body moving in a circular path is defined as the time taken to complete:',
    'MCQ', ch=['one revolution', '2&pi; revolutions', '10 revolutions',
               'a fraction of a revolution in one second'])
d.q('Which of the following statements correctly describes the resultant of the forces acting on a body '
    'moving in uniform circular motion?', 'MCQ',
    ch=['an outward centrifugal force balances the inward force',
        'there is no outward force; the resultant of the forces is always directed towards the centre',
        'the resultant of the forces acts tangentially, along the direction of the velocity',
        'the resultant of the forces equals zero because the speed is constant'])
d.q('<b>Describe the path</b> of a ball being whirled in a circle at the instant the string holding it '
    'breaks, and <b>explain why</b> it does not fly off directly outwards, away from the centre.', 'Explain',
    F.string_breaks('Figure 6'))
d.q('What happens in each of the following cases?', 'Explain',
    parts=['<b>a)</b> a sudden break of the string that holds a ball moving in a circular path.',
           '<b>b)</b> increasing the radius of the circular path while the angular velocity of the body stays '
           'constant.'])
d.q('A body moves in uniform circular motion, completing 15 revolutions in 3.0 s on a circular path of radius '
    '0.30 m.', 'Problem',
    parts=['<b>a)</b> Calculate the periodic time and the frequency.',
           '<b>b)</b> Calculate the linear speed.'])

d.grp('Group C')
d.q('The centripetal acceleration (a<sub>c</sub>) of a body moving in a circular path can be calculated using:',
    'MCQ', ch=['a<sub>c</sub> = &omega;&sup2; r &nbsp;or&nbsp; a<sub>c</sub> = v&sup2; / r',
               'a<sub>c</sub> = &omega; / r &nbsp;or&nbsp; a<sub>c</sub> = v r',
               'a<sub>c</sub> = &omega; r&sup2; &nbsp;or&nbsp; a<sub>c</sub> = v&sup2; r',
               'a<sub>c</sub> = &omega;&sup2; / r &nbsp;or&nbsp; a<sub>c</sub> = v / r&sup2;'])
d.q('A ball moves along the inner surface of a horizontal semicircular ring as shown in the top view. '
    '<b>Which arrow represents the direction of the average force acting on the ball?</b>', 'MCQ',
    F.ring_force('Figure 7'),
    ch=['arrow (a)', 'arrow (b)', 'arrow (c)', 'arrow (d)'])
d.q('<b>Explain why</b> a body that moves in a circular path with a constant speed possesses an acceleration '
    'that is not equal to zero.', 'Explain')
d.q('State the reason for each of the following:', 'Explain',
    parts=['<b>a)</b> a body moving in a circular path with a constant speed is said to be in a state of '
           'acceleration.',
           '<b>b)</b> there is no "centrifugal force" directed outwards acting on a body in circular motion.'])
d.q('A ball of mass 0.40 kg moves in a horizontal circular path of radius 0.50 m with a speed of 2.0 m/s.',
    'Problem',
    parts=['<b>a)</b> Determine the value of the centripetal acceleration.',
           '<b>b)</b> Determine the value of the centripetal force required.'])

# ============================ SOLUTIONS ============================
d.page()
d.sec('✓', 'Answer key', 'Solutions &mdash; step by step')
d.hint('Most of these questions are one substitution away from the answer once you have written down T, '
       '&omega; and v. Start every problem by finding the periodic time.')

d.grp('Part A &mdash; Classwork 2')
d.sol(1, 'what "uniform" really means',
      'uniform circular motion : the <b>speed</b> ( a scalar ) is constant,\n'
      'but the <b>velocity</b> ( a vector ) changes, because its direction turns\n'
      'continuously  &rarr;  there is an acceleration, directed towards the centre',
      'C) the speed is constant, but the direction of the velocity changes towards the centre')
d.sol(2, 'periodic time and angular velocity',
      'a)  T = total time / number of revolutions = 2.0 / 10 = 0.20 s\n'
      'b)  ω = 2π / T = ( 2 × 3.14 ) / 0.20 = 31.4 rad/s',
      'T = 0.20 s , ω = 31.4 rad/s')
d.sol(3, 'centripetal acceleration from ω',
      'a(c) = ω² r = ( 3.0 )² × 2.0 = 9 × 2.0 = 18 m/s²', 'a(c) = 18 m/s²',
      why='The mass is not needed for the <b>acceleration</b>; it is only needed for the force.')

d.grp('Part B &mdash; Home assignment 2')
d.sol(4, 'periodic time and linear speed',
      'a)  T = 5.0 / 20 = 0.25 s\n'
      'b)  v = 2π r / T = ( 2 × 3.14 × 0.20 ) / 0.25 = 1.256 / 0.25 = 5.03 m/s',
      'T = 0.25 s , v = 5.03 m/s')
d.sol(5, 'speed and force of the whirling ball',
      'a)  v = ω r = 3.0 × 2.0 = 6.0 m/s\n'
      'b)  F = m ω² r = 0.50 × 9 × 2.0 = 9.0 N      (or F = m v²/r = 0.50 × 36 / 2 = 9.0 N)',
      'v = 6.0 m/s , F = 9.0 N')
d.sol(6, 'the rotating spring',
      'the spring supplies the centripetal force, and the radius is the <b>stretched</b> length :\n'
      '    r = natural length + extension = 0.10 + x\n\n'
      'k x = m ω² r\n'
      '30 x = 0.50 × ( 6.0 )² × ( 0.10 + x )\n'
      '30 x = 18 ( 0.10 + x ) = 1.8 + 18 x\n'
      '12 x = 1.8      &rarr;      x = 0.15 m',
      'the extension = 0.15 m',
      why='The commonest mistake here is to use r = 0.10 m; the spring is stretched while it turns, so the '
          'radius is 0.25 m.')

d.grp('Part C &mdash; Weekly assessment &middot; Group A')
d.sol(7, 'the definition of ω', 'ω = Δθ / Δt   ( radians per second )',
      'B) the angular displacement per unit time')
d.sol(8, 'the centripetal force',
      'F = m a(c)  and  a(c) = v² / r   &rarr;   F = m v² / r', 'B) F = m v&sup2; / r')
d.sol(9, 'the rotating disc',
      'a)  T = 2π / ω = 2π / 4π = 0.5 s\n'
      'b)  v = ω r = 4π × 0.30 = 4 × 3.14 × 0.30 = 3.77 m/s', 'T = 0.5 s , v = 3.77 m/s')
d.sol(10, 'the washing machine',
      'the wall of the drum pushes the clothes inwards and supplies the centripetal force\n'
      'that keeps them on the circular path.\n'
      'the drops of water are not held by the wall: when a drop reaches a hole there is\n'
      'nothing left to push it towards the centre, so by its inertia it continues in a\n'
      'straight line along the tangent and escapes through the hole.',
      'the wall cannot supply a centripetal force through the holes, so the water leaves along the tangent',
      why='Nothing throws the water outwards; it simply keeps going straight while the drum keeps curving '
          'away from it.')
d.sol(11, 'acceleration and force from the periodic time',
      'v = 2π r / T = ( 2 × 3.14 × 2.0 ) / 4.0 = 3.14 m/s\n'
      'a)  a(c) = v² / r = ( 3.14 )² / 2.0 = 9.86 / 2.0 = 4.93 m/s²\n'
      'b)  F = m a(c) = 3.0 × 4.93 = 14.8 N', 'a(c) = 4.93 m/s² , F = 14.8 N')

d.grp('Group B')
d.sol(12, 'the definition of T', 'T is the time of <b>one complete revolution</b>', 'A) one revolution')
d.sol(13, 'the resultant force',
      'the body is accelerating towards the centre, so by Newton’s second law the\n'
      'resultant force must point towards the centre as well. no real force pushes\n'
      'the body outwards.',
      'B) there is no outward force; the resultant is always directed towards the centre')
d.sol(14, 'when the string breaks',
      'while the string is intact it pulls the ball towards the centre and keeps bending\n'
      'its path. the instant it breaks, no horizontal force is left, so by Newton’s first\n'
      'law the ball keeps the velocity it had at that instant : a straight line <b>tangent</b>\n'
      'to the circle, with the same speed.',
      'it moves in a straight line along the tangent, not radially outwards',
      why='It does not fly outwards along the radius because it never had a velocity in that direction; the '
          'velocity was always tangential.')
d.sol(15, 'two changes in the motion',
      'a)  the string breaks  &rarr;  the centripetal force disappears  &rarr;  the ball moves\n'
      '    in a straight line along the tangent with a constant speed.\n\n'
      'b)  r increases with ω constant :\n'
      '    v = ω r        &rarr;  the linear speed increases\n'
      '    a(c) = ω² r     &rarr;  the centripetal acceleration increases\n'
      '    F = m ω² r     &rarr;  the required force increases',
      'a) straight line along the tangent &nbsp;&middot;&nbsp; b) v , a(c) and F all increase')
d.sol(16, 'periodic time, frequency and speed',
      'a)  T = 3.0 / 15 = 0.20 s\n'
      '    f = 1 / T = 1 / 0.20 = 5.0 Hz\n'
      'b)  v = 2π r / T = ( 2 × 3.14 × 0.30 ) / 0.20 = 1.884 / 0.20 = 9.42 m/s',
      'T = 0.20 s , f = 5.0 Hz , v = 9.42 m/s')

d.grp('Group C')
d.sol(17, 'the two forms of a(c)',
      'a(c) = v² / r   and   v = ω r   &rarr;   a(c) = ( ω r )² / r = ω² r',
      'A) a(c) = &omega;&sup2; r or v&sup2; / r')
d.sol(18, 'the force on the ball inside the ring',
      'the ball follows a circular arc, so its acceleration — and therefore the resultant\n'
      'force from the wall — must point towards the <b>centre</b> of that arc, which lies to\n'
      'the left of the ball in the figure.', 'B) the arrow directed towards the centre',
      why='The tangential arrows (c) and (d) would change the <b>speed</b> of the ball, and the outward arrow '
          '(a) would push it off the wall altogether.')
d.sol(19, 'constant speed but non-zero acceleration',
      'acceleration = the rate of change of the <b>velocity</b>, and the velocity is a vector.\n'
      'in circular motion the direction of the velocity changes at every instant, so the\n'
      'velocity changes even though its magnitude does not  &rarr;  a ≠ 0 , directed to the centre.',
      'because the direction of the velocity keeps changing')
d.sol(20, 'two reasons',
      'a)  the velocity is a vector: a change of direction alone is a change of velocity,\n'
      '    so the body is accelerating even with a constant speed.\n\n'
      'b)  the only real force acting is the inward one ( the string, the wall, gravity ... ).\n'
      '    the outward "push" that a rotating passenger feels is the effect of his own\n'
      '    <b>inertia</b> in a rotating frame, not a force acting on the body.',
      'a) the direction of v changes &nbsp;&middot;&nbsp; b) the outward feeling is inertia, not a real force')
d.sol(21, 'acceleration and force of the ball',
      'a)  a(c) = v² / r = ( 2.0 )² / 0.50 = 4.0 / 0.50 = 8.0 m/s²\n'
      'b)  F = m a(c) = 0.40 × 8.0 = 3.2 N', 'a(c) = 8.0 m/s² , F = 3.2 N')

d.foot('Lesson 1&ndash;10 &middot; Uniform Circular Motion &middot; Mr. Gemy',
       'a<sub>c</sub> = v&sup2;/r = &omega;&sup2;r &nbsp;&middot;&nbsp; F<sub>c</sub> = m&omega;&sup2;r')
d.save('l10.html')
print('l10.html written -', d.n, 'questions')

# -*- coding: utf-8 -*-
import figs_l78 as F
from docbase import Doc

d = Doc('Unit 1 &middot; Lessons 1&ndash;7 and 1&ndash;8', 'Momentum, Impulse<br>and Its Conservation',
        'Two lessons in one sheet: the impulse of a force on a body, and the conservation of momentum in '
        'collisions and explosions.',
        ['Grade 11 &middot; Egyptian Baccalaureate', '22 questions', 'Step-by-step solutions',
         'smooth horizontal surfaces'], 'Momentum and Impulse')

d.kit('The toolkit for these two lessons', [
    ('p = m v', 'momentum &mdash; unit : kg&middot;m/s'),
    ('J = F &times; &Delta;t', 'impulse of a force &mdash; unit : N&middot;s'),
    ('J = &Delta;p = m v<sub>f</sub> &minus; m v<sub>i</sub>', 'impulse&ndash;momentum theorem'),
    ('F = &Delta;p / &Delta;t', 'a longer contact means a smaller force'),
    ('J = area under the F&ndash;t curve', 'whatever the shape of the pulse'),
    ('&Sigma;p (before) = &Sigma;p (after)', 'conservation of momentum'),
])
d.hint('<b>Momentum is a vector.</b> Before you add or subtract any two momenta, fix a positive direction and '
       'give every velocity its sign; for motion in two dimensions, apply the conservation law to the x and y '
       'directions <b>separately</b>.')

# ---------------- A ----------------
d.sec('A', 'Lesson 1&ndash;7 &middot; Classwork 1', 'Momentum and impulse')
d.q('A person A of mass 40 kg moves at 0.3 m/s towards the east, while a person B of mass 60 kg moves at '
    '0.2 m/s towards the west along the same straight line. <b>Which of them has the greater momentum in '
    'magnitude?</b>', 'MCQ', F.two_movers('Figure 1'),
    ch=['person A', 'person B', 'they are equal', 'it cannot be decided without choosing a positive direction'])
d.q('A phone falls from the same height once onto a hard floor and once onto a cushion, and it comes to rest '
    'in both cases.', 'Explain', F.phone_drop('Figure 2'),
    parts=['<b>a)</b> Explain why the average collision force on the cushion is smaller, although the change '
           'in momentum is the same in the two cases.',
           '<b>b)</b> What happens to the average force if the stopping time of the phone is doubled?'])
d.q('A ball of mass 0.10 kg moves eastwards at 6 m/s, then it is struck so that it moves northwards with the '
    'same speed. <b>What is the magnitude of the impulse given to the ball, and its direction?</b>', 'MCQ',
    F.ball_turn('Figure 3'),
    ch=['0.6 N&middot;s northwards', '0.6&radic;2 N&middot;s north-west', '1.2 N&middot;s north-east',
        '0.6&radic;2 N&middot;s south-west'])

# ---------------- B ----------------
d.sec('B', 'Lesson 1&ndash;7 &middot; Home assignment 1', 'The force&ndash;time relation')
d.q('If an airbag increases the stopping time of a passenger to <b>three times</b> its value, while the change '
    'in his momentum stays the same, then the average force becomes:', 'MCQ',
    ch=['three times as large', 'half as large', 'one third as large', 'unchanged'])
d.q('A dynamics trolley collides with a spring bumper connected to a force sensor, and then rebounds in the '
    'opposite direction. The sensor records the force&ndash;time curve shown.', 'Explain',
    F.ft_curve('Figure 4'),
    parts=['<b>a)</b> Explain how the force&ndash;time curve is used to determine the impulse given to the '
           'trolley.',
           '<b>b)</b> How does the shape of the force pulse change when the bumper is replaced by a softer '
           'one, while the change in momentum stays the same?'])

# ---------------- C ----------------
d.sec('C', 'Lesson 1&ndash;8 &middot; Classwork 1', 'Conservation of momentum')
d.q('A passenger stands at the middle of a boat that is at rest on a calm lake, then he walks slowly towards '
    'the bow of the boat.', 'Explain', F.boat_person('Figure 5'),
    parts=['<b>a)</b> Describe the total momentum of the system before the passenger starts to walk.',
           '<b>b)</b> Explain why the boat moves in the direction opposite to the motion of the passenger, '
           'stating the reason.'])
d.q('A body of mass m<sub>1</sub> = 0.50 kg moving at 6.0 m/s towards the east collides with a body of mass '
    'm<sub>2</sub> = 1.00 kg at rest, and the two bodies stick together and move as one body after the '
    'collision.', 'Problem', F.collide_stick('Figure 6'),
    parts=['<b>a)</b> Calculate the common velocity of the two bodies after the collision.',
           '<b>b)</b> Compare the total momentum of the system before the collision with that after it, and '
           'state what you conclude.'])

# ---------------- D ----------------
d.page()
d.sec('D', 'Lesson 1&ndash;8 &middot; Home assignment 1', 'Collisions in one and two dimensions')
d.q('A body A of mass 2.0 kg moving at + 6.0 m/s collides with a body B of mass 4.0 kg moving in the opposite '
    'direction at 2.0 m/s. If the two bodies stick together after the collision, what is their common speed '
    'and its direction?', 'MCQ',
    ch=['0.67 m/s in the direction of A', '0.67 m/s in the direction of B',
        '2.0 m/s in the direction of A', '2.0 m/s in the direction of B'])
d.q('On a smooth horizontal surface, a body A of mass 1.5 kg moves at 6.0 m/s along the positive direction of '
    'the horizontal axis and collides with a body B of mass 3.0 kg at rest. After the collision, body A is '
    'deflected through 30&deg; above the original line of motion, while body B is deflected through 60&deg; '
    'below it. <b>Find the final speed of each of the two bodies.</b>', 'Problem',
    F.collide_2d('Figure 7', '1.5 kg', '6.0 m/s', '3.0 kg', None, 30, 60))

# ---------------- E ----------------
d.sec('E', 'Weekly assessment', 'Groups A, B and C')
d.grp('Group A')
d.q('A tennis player strikes a ball with a racket, so that the average force acts on the ball for '
    '4 &times; 10&#8315;&sup3; s, which is just enough to give it a speed of 50 m/s from rest in the direction '
    'of the stroke. If the mass of the ball is 0.060 kg, what is the magnitude of the impulse it receives?',
    'MCQ', ch=['3.0 N&middot;s', '5.0 N&middot;s', '7.5 N&middot;s', '15 N&middot;s'])
d.q('For a constant change in momentum, if the time of the collision is doubled, then the average force:',
    'MCQ', ch=['is doubled', 'is halved', 'does not change', 'becomes four times as large'])
d.q('A body of mass 9.0 kg at rest explodes into a body A of mass 5.0 kg and a body B of mass 4.0 kg. '
    'If body A moves towards the left at 8.0 m/s after the explosion, <b>find the velocity of body B</b> '
    'and its direction.', 'Problem', F.explosion('Figure 8'))
d.q('On a smooth horizontal surface, a body A of mass 0.30 kg moving at 4.0 m/s collides with a body B of '
    'mass 0.60 kg at rest. Immediately after the collision, body A moves <b>perpendicular</b> to its original '
    'line of motion, while body B is deflected through 60&deg; below that line. '
    '<b>Find the final speed of each body.</b>', 'Problem',
    F.collide_2d('Figure 9', '0.30 kg', '4.0 m/s', '0.60 kg', None, 90, 60))

d.grp('Group B')
d.q('A ball of mass 0.20 kg moves eastwards at 5 m/s, then it is struck so that it moves westwards at 3 m/s. '
    'What is the magnitude of the impulse acting on the ball and its direction?', 'MCQ',
    ch=['0.4 N&middot;s westwards', '1.0 N&middot;s eastwards', '1.6 N&middot;s westwards',
        '1.6 N&middot;s eastwards'])
d.q('For a constant change in momentum, if the time of the collision is reduced to half, then the average '
    'force:', 'MCQ', ch=['is doubled', 'is halved', 'does not change', 'becomes four times as large'])
d.q('On a smooth horizontal surface, a body A of mass 0.40 kg moving at 6.0 m/s collides with a body B of '
    'mass 0.80 kg moving at 1.5 m/s in the <b>same</b> direction. After the collision, body A is deflected '
    'through 53&deg; above the original line of motion and body B through 30&deg; below it. '
    '<b>Find the final speed of each body.</b>', 'Problem',
    F.collide_2d('Figure 10', '0.40 kg', '6.0 m/s', '0.80 kg', '1.5 m/s', 53, 30))
d.q('A large artillery shell is fired horizontally towards the east from a cannon standing on horizontal '
    'ground.', 'Explain', F.cannon_recoil('Figure 11'),
    parts=['<b>a)</b> Describe the total momentum of the system before the shell is fired.',
           '<b>b)</b> Explain the backward recoil of the cannon after firing, and state the relation between '
           'the recoil speed of the cannon and its mass.'])

d.grp('Group C')
d.q('A ball of mass 0.10 kg moves at 8 m/s, then it is struck so that it moves at 6 m/s in a direction '
    '<b>perpendicular</b> to its original direction of motion. What is the magnitude of the impulse acting on '
    'the ball?', 'MCQ', ch=['20 N&middot;s', '0.60 N&middot;s', '1.00 N&middot;s', '1.40 N&middot;s'])
d.q('For a constant change in momentum, if the time of the collision becomes <b>four times</b> its value, '
    'then the average force:', 'MCQ',
    ch=['is doubled', 'is halved', 'does not change', 'is reduced to one quarter'])
d.q('On a smooth horizontal surface, a body A of mass 0.30 kg moving at 5 m/s collides with a body B of mass '
    '0.60 kg at rest. If body A moves at 3 m/s perpendicular to its original direction immediately after the '
    'collision, then the speed of body B after the collision and the angle &theta; that its direction makes '
    'below the original line of motion are:', 'MCQ',
    F.collide_2d('Figure 12', '0.30 kg', '5.0 m/s', '0.60 kg', None, 90, 31),
    ch=['3.25 m/s , &theta; &asymp; 26.6&deg;', '2.92 m/s , &theta; &asymp; 31.0&deg;',
        '3.25 m/s , &theta; &asymp; 31.0&deg;', '2.92 m/s , &theta; &asymp; 26.6&deg;'])
d.q('The two graphs show the force&ndash;time relation for two bodies 1 and 2. '
    '<b>Find the ratio between the impulse in the two cases</b> &nbsp;( J<sub>1</sub> : J<sub>2</sub> ).',
    'Problem', F.two_pulses('Figure 13'))
d.q('The graph shows the force acting on a body of mass 1.50 kg during the time from 0 to 6 s. '
    'If the initial velocity of the body was zero, what is its speed at t = 6 s?', 'MCQ',
    F.tri_pulse('Figure 14'), ch=['6.0 m/s', '9.0 m/s', '12 m/s', '18 m/s'])

# ============================ SOLUTIONS ============================
d.page()
d.sec('✓', 'Answer key', 'Solutions &mdash; step by step')
d.hint('Two relations carry this whole sheet: <b>J = &Delta;p = F &Delta;t</b> for a single body, and '
       '<b>&Sigma;p before = &Sigma;p after</b> for a system of bodies.')

d.grp('Part A &mdash; Lesson 1-7 &middot; Classwork 1')
d.sol(1, 'comparing two momenta',
      'p = m v\np(A) = 40 × 0.3 = 12 kg·m/s\np(B) = 60 × 0.2 = 12 kg·m/s',
      'C) they are equal in magnitude',
      why='They are equal in <b>magnitude</b> but opposite in direction, so the total momentum of the two '
          'persons together is zero.')
d.sol(2, 'the phone on a hard floor and on a cushion',
      'a)  the phone arrives with the same speed, so the change in momentum Δp is the same.\n'
      '    F = Δp / Δt\n'
      '    the cushion makes the phone stop over a longer time Δt , so the same Δp is\n'
      '    delivered by a smaller average force.\n\n'
      'b)  Δt doubled , Δp fixed   &rarr;   F becomes half its value',
      'the cushion increases Δt , so F decreases ; doubling Δt halves F',
      why='This is the physics behind airbags, crash helmets, knee pads and the way a fielder pulls his hands '
          'back while catching a ball.')
d.sol(3, 'impulse when the direction changes',
      'J = Δp = m v(final) − m v(initial)\n'
      'm v(final)   = 0.10 × 6 = 0.6 kg·m/s   northwards\n'
      'm v(initial) = 0.10 × 6 = 0.6 kg·m/s   eastwards\n\n'
      'J = 0.6 (north) − 0.6 (east) = 0.6 (north) + 0.6 (west)\n'
      '| J | = √( 0.6² + 0.6² ) = 0.6√2 = 0.85 N·s , directed north-west',
      'B) 0.6&radic;2 N&middot;s north-west',
      why='Even though the <b>speed</b> did not change, the velocity did, so there is a large impulse; '
          'momentum is a vector.')

d.grp('Part B &mdash; Lesson 1-7 &middot; Home assignment 1')
d.sol(4, 'the airbag', 'F = Δp / Δt , with Δp fixed\nΔt × 3   &rarr;   F ÷ 3',
      'C) one third as large')
d.sol(5, 'reading the force&ndash;time curve',
      'a)  J = F × Δt for a constant force, and for a changing force the product\n'
      '    becomes the <b>area enclosed between the curve and the time axis</b>.\n'
      '    so : impulse = area under the force–time curve = Δp of the trolley\n\n'
      'b)  a softer bumper lengthens the contact time and lowers the peak force,\n'
      '    so the pulse becomes <b>wider and flatter</b> — but the area stays the same,\n'
      '    because Δp has not changed.',
      'impulse = the area under the curve ; a softer bumper gives a wider, lower pulse of the same area')

d.grp('Part C &mdash; Lesson 1-8 &middot; Classwork 1')
d.sol(6, 'the passenger walking in the boat',
      'a)  both the boat and the passenger are at rest :\n'
      '    p(total) = 0\n\n'
      'b)  the water exerts no horizontal force on the system, so momentum is conserved :\n'
      '    m(p) v(p) + m(b) v(b) = 0   &rarr;   v(b) = − m(p) v(p) / m(b)\n'
      '    the minus sign means the boat moves backwards.',
      'the total momentum stays zero, so the boat must move the opposite way',
      why='The boat is much heavier than the passenger, so its backward speed is much smaller than his '
          'forward speed.')
d.sol(7, 'a perfectly inelastic collision',
      'a)  &Sigma;p (before) = &Sigma;p (after)\n'
      '    m₁ v₁ + m₂ v₂ = ( m₁ + m₂ ) v\n'
      '    ( 0.50 × 6.0 ) + ( 1.00 × 0 ) = ( 1.50 ) v\n'
      '    3.0 = 1.5 v    &rarr;    v = 2.0 m/s  eastwards\n\n'
      'b)  before : 3.0 kg·m/s        after : 1.5 × 2.0 = 3.0 kg·m/s',
      'v = 2.0 m/s ; the total momentum is the same before and after',
      why='The kinetic energy is <b>not</b> conserved here (9.0 J before, 3.0 J after): part of it becomes '
          'heat and sound. Momentum, however, is always conserved when no external force acts.')

d.grp('Part D &mdash; Lesson 1-8 &middot; Home assignment 1')
d.sol(8, 'a head-on collision',
      'take the direction of A as positive :\n'
      '&Sigma;p (before) = ( 2.0 × + 6.0 ) + ( 4.0 × − 2.0 ) = 12 − 8 = + 4.0 kg·m/s\n'
      '&Sigma;p (after)  = ( 2.0 + 4.0 ) v = 6.0 v\n'
      '6.0 v = 4.0   &rarr;   v = + 0.67 m/s   (the + sign : the direction of A)',
      'A) 0.67 m/s in the direction of A')
d.sol(9, 'a collision in two dimensions',
      'take x along the original motion and y perpendicular to it.\n\n'
      'y :   0 = 1.5 v(A) sin 30° − 3.0 v(B) sin 60°\n'
      '      0.75 v(A) = 2.598 v(B)      &rarr;   v(A) = 3.46 v(B)\n\n'
      'x :   1.5 × 6.0 = 1.5 v(A) cos 30° + 3.0 v(B) cos 60°\n'
      '      9 = 1.299 v(A) + 1.5 v(B)\n'
      '      9 = 1.299 ( 3.46 v(B) ) + 1.5 v(B) = 6.0 v(B)\n'
      '      v(B) = 1.5 m/s        v(A) = 3.46 × 1.5 = 5.2 m/s',
      'v(A) = 5.2 m/s , v(B) = 1.5 m/s',
      why='Always start with the axis that has <b>zero</b> total momentum (here the y axis): it gives the '
          'simplest relation between the two unknowns.')

d.grp('Part E &mdash; Weekly assessment &middot; Group A')
d.sol(10, 'the impulse on the tennis ball',
      'J = Δp = m ( v(f) − v(i) ) = 0.060 ( 50 − 0 ) = 3.0 N·s', 'A) 3.0 N&middot;s',
      why='The contact time is not needed for the impulse itself; it is only needed if the <b>average force</b> '
          'is asked for ( F = 3.0 / 4&times;10&#8315;&sup3; = 750 N ).')
d.sol(11, 'doubling the collision time', 'F = Δp / Δt , Δp fixed   &rarr;   Δt × 2 gives F ÷ 2', 'B) is halved')
d.sol(12, 'the explosion',
      'the body was at rest, so   &Sigma;p (before) = 0\n'
      'taking the right as positive :\n'
      '0 = ( 5.0 × − 8.0 ) + ( 4.0 × v(B) )\n'
      '0 = − 40 + 4 v(B)    &rarr;    v(B) = + 10 m/s',
      'v(B) = 10 m/s towards the right',
      why='In an explosion the momenta of the fragments always add up to the momentum before the explosion '
          '— here zero — so the two pieces must fly apart in opposite directions.')
d.sol(13, 'A leaves perpendicular to its original path',
      'x :   0.30 × 4.0 = 0 + 0.60 v(B) cos 60°\n'
      '      1.2 = 0.60 v(B) × 0.5 = 0.30 v(B)    &rarr;    v(B) = 4.0 m/s\n\n'
      'y :   0 = 0.30 v(A) − 0.60 v(B) sin 60°\n'
      '      0.30 v(A) = 0.60 × 4.0 × 0.866 = 2.08   &rarr;   v(A) = 6.93 m/s',
      'v(A) = 6.93 m/s , v(B) = 4.0 m/s',
      why='<b>Note for the teacher:</b> these particular data are not energy-consistent (the kinetic energy '
          'after the collision would be larger than before it). The question is meant as a drill on '
          'conservation of momentum in two dimensions, and the working above is the answer it asks for.')

d.grp('Group B')
d.sol(14, 'impulse when the ball is sent back',
      'take the east as positive :\n'
      'J = m ( v(f) − v(i) ) = 0.20 ( − 3 − 5 ) = − 1.6 N·s\n'
      'the minus sign : the impulse is directed westwards', 'C) 1.6 N&middot;s westwards',
      why='The two velocities must carry opposite signs; forgetting that gives 0.4 N&middot;s, which is the '
          'commonest wrong answer here.')
d.sol(15, 'halving the collision time', 'F = Δp / Δt   &rarr;   Δt ÷ 2 gives F × 2', 'A) is doubled')
d.sol(16, 'both bodies moving before the collision',
      '&Sigma;p (before) = ( 0.40 × 6.0 ) + ( 0.80 × 1.5 ) = 2.4 + 1.2 = 3.6 kg·m/s   (along x)\n\n'
      'y :   0.40 v(A) sin 53° = 0.80 v(B) sin 30°\n'
      '      0.319 v(A) = 0.40 v(B)      &rarr;   v(A) = 1.25 v(B)\n\n'
      'x :   0.40 v(A) cos 53° + 0.80 v(B) cos 30° = 3.6\n'
      '      0.241 ( 1.25 v(B) ) + 0.693 v(B) = 3.6\n'
      '      0.994 v(B) = 3.6    &rarr;    v(B) = 3.62 m/s\n'
      '      v(A) = 1.25 × 3.62 = 4.53 m/s',
      'v(A) = 4.53 m/s , v(B) = 3.62 m/s',
      why='<b>Note for the teacher:</b> as in question 13, the angles given here are not energy-consistent; '
          'the solution applies conservation of momentum exactly as the question intends.')
d.sol(17, 'the recoil of the cannon',
      'a)  the cannon and the shell are both at rest :  p(total) = 0\n\n'
      'b)  no external horizontal force acts, so momentum is conserved :\n'
      '    0 = m(shell) v(shell) + M(cannon) v(cannon)\n'
      '    v(cannon) = − m(shell) v(shell) / M(cannon)',
      'the cannon recoils backwards, and its recoil speed is inversely proportional to its mass',
      why='This is why a field gun is made heavy and anchored to the ground: the same shell momentum then '
          'produces a much smaller recoil speed.')

d.grp('Group C')
d.sol(18, 'a perpendicular change of velocity',
      'p(initial) = 0.10 × 8 = 0.8 kg·m/s\np(final)   = 0.10 × 6 = 0.6 kg·m/s , perpendicular to it\n'
      '| J | = √( 0.8² + 0.6² ) = √1.00 = 1.00 N·s', 'C) 1.00 N&middot;s')
d.sol(19, 'four times the collision time', 'F = Δp / Δt   &rarr;   Δt × 4 gives F ÷ 4',
      'D) is reduced to one quarter')
d.sol(20, 'finding both the speed and the angle',
      'x :   0.30 × 5 = 0.60 v(B) cos θ\n'
      '      v(B) cos θ = 1.5 / 0.60 = 2.5\n\n'
      'y :   0.30 × 3 = 0.60 v(B) sin θ\n'
      '      v(B) sin θ = 0.9 / 0.60 = 1.5\n\n'
      'v(B) = √( 2.5² + 1.5² ) = √8.5 = 2.92 m/s\n'
      'tan θ = 1.5 / 2.5 = 0.6    &rarr;    θ = 31.0°  below the original line',
      'B) 2.92 m/s , &theta; &asymp; 31&deg;')
d.sol(21, 'comparing two force pulses',
      'J = area under the force–time graph\n\n'
      'J₁ = F × Δt\n'
      'J₂ = ( F / 2 ) × ( 2 Δt ) = F × Δt\n\n'
      'J₁ : J₂ = 1 : 1', 'J₁ : J₂ = 1 : 1',
      why='Halving the force while doubling the time leaves the impulse untouched — exactly the trick that '
          'crumple zones and airbags use.')
d.sol(22, 'impulse from a triangular graph',
      'J = area of the triangle = ½ × base × height\n'
      'J = ½ × 6 s × 6 N = 18 N·s\n\n'
      'J = Δp = m ( v − 0 )\n18 = 1.50 v    &rarr;    v = 12 m/s', 'C) 12 m/s')

d.foot('Lessons 1&ndash;7 and 1&ndash;8 &middot; Momentum and Impulse &middot; Mr. Gemy',
       'J = &Delta;p = F&Delta;t &nbsp;&middot;&nbsp; &Sigma;p before = &Sigma;p after')
d.save('l78.html')
print('l78.html written -', d.n, 'questions')

# -*- coding: utf-8 -*-
import figs_l9 as F
import figs_l78 as G
from docbase import Doc

d = Doc('Unit 1 &middot; Lesson 1&ndash;9', 'Momentum and<br>Mechanical Energy',
        'Elastic and inelastic collisions, the coefficient of restitution, and the kinetic energy lost in a '
        'collision.',
        ['Grade 11 &middot; Egyptian Baccalaureate', '13 questions', 'Step-by-step solutions',
         'smooth horizontal surfaces'], 'Momentum and Mechanical Energy')

d.kit('The toolkit for this lesson', [
    ('&Sigma;p before = &Sigma;p after', 'always true for an isolated system'),
    ('KE = &frac12; m v&sup2;', 'kinetic energy of each body'),
    ('e = separation speed / approach speed', 'coefficient of restitution'),
    ('e = 1', 'perfectly elastic &mdash; KE conserved'),
    ('0 &lt; e &lt; 1', 'inelastic &mdash; part of the KE is lost'),
    ('e = 0', 'perfectly inelastic &mdash; the bodies move together'),
])
d.hint('<b>The key distinction of this lesson.</b> Momentum is conserved in <b>every</b> collision of an '
       'isolated system, elastic or not. Kinetic energy is conserved only in a perfectly elastic collision; '
       'in any other collision part of it turns into internal energy, sound and permanent deformation.')

# ---------------- A ----------------
d.sec('A', 'Classwork &nbsp;1', 'Collisions and the coefficient of restitution')
d.q('In an <b>inelastic</b> collision of an isolated system, which of the following statements is correct?',
    'MCQ',
    ch=['both the momentum and the kinetic energy are conserved',
        'the momentum is not conserved while the kinetic energy is conserved',
        'the momentum is conserved while the kinetic energy decreases',
        'both the momentum and the total energy decrease'])
d.q('A car A of mass 1000 kg moving at 20 m/s towards the east collides with a stationary truck B of mass '
    '3000 kg at a traffic signal. The car and the truck lock together immediately after the collision and '
    'move as one body.', 'Problem', F.car_truck('Figure 1'),
    parts=['<b>a)</b> Calculate the speed of the combined body (car + truck) just after the collision.',
           '<b>b)</b> Calculate the coefficient of restitution (e) for this collision, and deduce the type of '
           'the collision from its value.',
           '<b>c)</b> Calculate the amount of kinetic energy lost as a result of this collision.'])

# ---------------- B ----------------
d.sec('B', 'Home assignment &nbsp;1', 'Energy lost and the restitution coefficient')
d.q('Two balls collide and then separate after the collision, and the sum of their kinetic energies '
    'decreases. We conclude that the collision is:', 'MCQ',
    ch=['perfectly elastic, because the two balls separated',
        'inelastic, and it is not necessary for the two bodies to stick together',
        'perfectly inelastic', 'not obeying the conservation of momentum'])
d.q('A ball A of mass 2.0 kg moving at 6.0 m/s towards the east collides with a ball B of mass 3.0 kg at '
    'rest. The two balls stick together after the collision and move together in the same direction.',
    'Problem', G.collide_stick('Figure 2', '2.0 kg', '6.0 m/s', '3.0 kg', 'at rest', "v' = ?"),
    parts=['<b>a)</b> Calculate their common speed after the collision.',
           '<b>b)</b> Calculate the decrease in the total kinetic energy as a result of the collision.'])
d.q('A rubber ball collides perpendicularly with a smooth wall. Its speed before the collision was 10 m/s '
    'towards the wall, and it rebounded after the collision at 6 m/s in the opposite direction. '
    '<b>What is the value of the coefficient of restitution e?</b>', 'Problem', F.ball_wall('Figure 3'))

# ---------------- C ----------------
d.page()
d.sec('C', 'Weekly assessment', 'Groups A, B and C')
d.grp('Group A')
d.q('A lump of clay of mass 0.50 kg moves at 8.0 m/s towards a stationary trolley of mass 1.50 kg on a smooth '
    'horizontal surface. After the collision the clay sticks to the trolley and the two move together. '
    '<b>Calculate their common speed after the collision.</b>', 'Problem', F.clay_trolley('Figure 4'))
d.q('For the collision of the previous question, which statement describes it correctly?', 'MCQ',
    ch=['both the momentum and the kinetic energy are conserved',
        'the momentum is not conserved, because the two bodies stuck together',
        'the two masses move with one common speed after the collision',
        'the trolley rebounds in the opposite direction and the clay stays separate'])
d.q('A car collides with a barrier, so that its front is deformed and the temperature of some of its parts '
    'rises. The kinetic energy that was lost was mainly converted into:', 'MCQ',
    ch=['potential energy only', 'internal energy, sound and deformation', 'extra momentum',
        'extra mass for the car'])
d.q('A ball A moves at 4.0 m/s along a straight line towards a stationary ball B. Immediately after the '
    'collision the speed of ball B is 3.0 m/s in the original direction of motion, and the coefficient of '
    'restitution is 0.50. <b>What is the speed of ball A after the collision?</b>', 'MCQ',
    F.collide_before_after('Figure 5'),
    ch=['zero', '0.5 m/s', '1.0 m/s', '2.0 m/s'])

d.grp('Group B')
d.q('For the two balls of question 4 (2.0 kg at 6.0 m/s striking 3.0 kg at rest and sticking to it), '
    '<b>what percentage of the original kinetic energy is lost</b> in the collision?', 'Problem')
d.q('Hearing a loud sound during an inelastic collision is an evidence of:', 'MCQ',
    ch=['the destruction of part of the energy', 'the conversion of part of the kinetic energy into sound energy',
        'the non-conservation of momentum', 'the increase of the total kinetic energy'])

d.grp('Group C')
d.q('A trolley A of mass 2.0 kg moves at 4.0 m/s towards the east and collides with a stationary trolley B of '
    'mass 3.0 kg. After the collision the two trolleys lock together and move in the same direction with a '
    "common speed v'. <b>Find this common speed.</b>", 'Problem',
    G.collide_stick('Figure 6', '2.0 kg', '4.0 m/s', '3.0 kg', 'at rest', "v' = ?"))
d.q('If the total kinetic energy of two bodies decreases by 30 J during a collision in an isolated system, '
    'then the most accurate explanation is that:', 'MCQ',
    ch=['30 J of energy has disappeared',
        '30 J has been converted into other forms of energy inside the system and its near surroundings',
        'the momentum has decreased by 30 kg&middot;m/s', 'the mass of the system has decreased'])

# ============================ SOLUTIONS ============================
d.page()
d.sec('✓', 'Answer key', 'Solutions &mdash; step by step')
d.hint('In every collision start with the same line: <b>&Sigma;p before = &Sigma;p after</b>. Only after the '
       'velocities are known should you go on to compare the kinetic energies.')

d.grp('Part A &mdash; Classwork 1')
d.sol(1, 'what survives an inelastic collision',
      'no external force acts on an isolated system  &rarr;  momentum is always conserved\n'
      'the collision is inelastic  &rarr;  part of the kinetic energy turns into internal\n'
      'energy, sound and deformation, so the kinetic energy decreases',
      'C) the momentum is conserved while the kinetic energy decreases',
      why='The <b>total</b> energy is still conserved; it is only the <b>kinetic</b> part that goes down.')
d.sol(2, 'the car and the truck',
      'a)  &Sigma;p (before) = &Sigma;p (after)\n'
      '    ( 1000 × 20 ) + ( 3000 × 0 ) = ( 1000 + 3000 ) v\n'
      '    20 000 = 4000 v      &rarr;      v = 5 m/s   eastwards\n\n'
      'b)  the two bodies move together, so they never separate :\n'
      '    e = separation speed / approach speed = 0 / 20 = 0\n'
      '    e = 0   &rarr;   a perfectly inelastic collision\n\n'
      'c)  KE (before) = ½ × 1000 × 20² = 200 000 J = 200 kJ\n'
      '    KE (after)  = ½ × 4000 × 5²  =  50 000 J =  50 kJ\n'
      '    loss = 200 − 50 = 150 kJ',
      'v = 5 m/s , e = 0 (perfectly inelastic) , loss = 150 kJ',
      why='Three quarters of the kinetic energy disappears here — it is exactly this energy that crushes '
          'the metal and heats it, which is why crumple zones are designed to absorb it.')

d.grp('Part B &mdash; Home assignment 1')
d.sol(3, 'reading the type of collision',
      'the kinetic energy decreased  &rarr;  the collision is not perfectly elastic.\n'
      'the two balls separated  &rarr;  it is not perfectly inelastic either.',
      'B) inelastic, and the two bodies need not stick together',
      why='Sticking together is only the <b>extreme</b> case of an inelastic collision (e = 0); any collision '
          'with 0 &lt; e &lt; 1 is inelastic while the bodies still separate.')
d.sol(4, 'two balls that stick together',
      'a)  ( 2.0 × 6.0 ) + ( 3.0 × 0 ) = ( 2.0 + 3.0 ) v\n'
      '    12 = 5 v      &rarr;      v = 2.4 m/s   eastwards\n\n'
      'b)  KE (before) = ½ × 2.0 × 6.0² = 36 J\n'
      '    KE (after)  = ½ × 5.0 × 2.4² = 14.4 J\n'
      '    loss = 36 − 14.4 = 21.6 J',
      "v' = 2.4 m/s , loss = 21.6 J")
d.sol(5, 'the ball and the wall',
      'the wall does not move, so :\n'
      'e = speed of separation / speed of approach = 6 / 10 = 0.6', 'e = 0.6',
      why='e has no unit, and it always lies between 0 and 1 for a real collision; 0.6 tells us the collision '
          'is inelastic but the ball still bounces well.')

d.grp('Part C &mdash; Weekly assessment &middot; Group A')
d.sol(6, 'the clay and the trolley',
      '( 0.50 × 8.0 ) + ( 1.50 × 0 ) = ( 0.50 + 1.50 ) v\n'
      '4.0 = 2.0 v      &rarr;      v = 2.0 m/s', "v' = 2.0 m/s")
d.sol(7, 'describing the collision',
      'the clay sticks to the trolley, so after the collision there is only one body\n'
      'moving with one velocity  (a perfectly inelastic collision, e = 0)',
      'C) the two masses move with one common speed after the collision',
      why='Momentum <b>is</b> conserved here, which rules out option B; the kinetic energy is not, which '
          'rules out option A.')
d.sol(8, 'where the lost energy goes',
      'the deformation of the metal and the rise of temperature are the record of the\n'
      'kinetic energy that was transferred into internal energy, sound and the work of\n'
      'permanent deformation', 'B) internal energy, sound and deformation')
d.sol(9, 'using the coefficient of restitution',
      "e = ( v'(B) − v'(A) ) / ( v(A) − v(B) )\n"
      "0.50 = ( 3.0 − v'(A) ) / ( 4.0 − 0 )\n"
      "3.0 − v'(A) = 0.50 × 4.0 = 2.0\n"
      "v'(A) = 3.0 − 2.0 = 1.0 m/s", 'C) 1.0 m/s',
      why='Ball A keeps moving forwards, but more slowly than B — which is exactly what must happen if the '
          'two are not to overlap after the collision.')

d.grp('Group B')
d.sol(10, 'the percentage of energy lost',
      'from question 4 :   KE (before) = 36 J ,  KE (after) = 14.4 J\n'
      'loss = 21.6 J\n\n'
      'percentage = ( 21.6 / 36 ) × 100 % = 60 %', '60 % of the kinetic energy is lost',
      why='Notice that the momentum did not change at all during the same collision — the two quantities '
          'behave completely differently.')
d.sol(11, 'the meaning of the sound',
      'the sound carries energy away from the system, and that energy can only come\n'
      'from the kinetic energy of the two colliding bodies',
      'B) part of the kinetic energy is converted into sound energy')

d.grp('Group C')
d.sol(12, 'the two trolleys',
      '( 2.0 × 4.0 ) + ( 3.0 × 0 ) = ( 2.0 + 3.0 ) v\n'
      "8.0 = 5.0 v      &rarr;      v' = 1.6 m/s   eastwards", "v' = 1.6 m/s eastwards")
d.sol(13, 'the 30 J that vanished from the kinetic energy',
      'energy is never destroyed; the 30 J left the kinetic store and appeared as\n'
      'internal energy (heat), sound and the work done in deforming the two bodies',
      'B) it was converted into other forms inside the system and its surroundings',
      why='Option C mixes two different quantities: joules cannot be subtracted from a momentum measured in '
          'kg&middot;m/s, and in an isolated system the momentum does not change at all.')

d.foot('Lesson 1&ndash;9 &middot; Momentum and Mechanical Energy &middot; Mr. Gemy',
       'e = separation / approach &nbsp;&middot;&nbsp; &Sigma;p before = &Sigma;p after')
d.save('l9.html')
print('l9.html written -', d.n, 'questions')

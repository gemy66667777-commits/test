# -*- coding: utf-8 -*-
import figs_l45 as F
import figs_moment as M
from docbase import Doc

d = Doc('Unit 1 &middot; Lessons 1&ndash;4 and 1&ndash;5', 'Moment of a Force<br>and Equilibrium',
        'Two lessons in one sheet: the turning effect of a force, and the equilibrium of a body under '
        'several forces.',
        ['Grade 11 &middot; Egyptian Baccalaureate', '30 questions', 'Step-by-step solutions',
         'g = 9.8 m/s&sup2; where stated'], 'Moment of a Force and Equilibrium')

d.kit('The toolkit for these two lessons', [
    ('M = F &times; d', 'force &perp; to the arm'),
    ('M = F L sin &theta;', 'force inclined at &theta; to the arm'),
    ('unit : N&middot;m', 'moment is a vector quantity'),
    ('&Sigma;F = 0', 'condition of translational equilibrium'),
    ('&Sigma;F<sub>x</sub> = 0 , &Sigma;F<sub>y</sub> = 0', 'applied on both axes separately'),
    ('T sin &theta; = W', 'the vertical component carries the weight'),
])
d.hint('<b>Two ideas, one sheet.</b> A moment measures how strongly a force <b>turns</b> a body about a point, '
       'and it needs the <b>perpendicular</b> distance. Equilibrium means the forces cancel on <b>each axis '
       'separately</b>, which is why an inclined force must always be resolved first.')

# ---------------- A ----------------
d.sec('A', 'Lesson 1&ndash;4 &middot; Classwork 1', 'The moment of a force')
d.q('The expression for the moment M of a force when the force is <b>perpendicular</b> to the arm is:', 'MCQ',
    ch=['M = F / d', 'M = F d', 'M = F + d', 'M = F &minus; d'])
d.q('The moment of a force is a measure of:', 'MCQ',
    ch=['the magnitude of the force only', 'the turning effect of the force about a point',
        'the speed of the body', 'the energy stored in the body'])
d.q('The SI unit of the moment of a force is:', 'MCQ',
    ch=['newton (N)', 'joule (J)', 'newton &middot; metre (N&middot;m)', 'metre / second (m/s)'])
d.q('The law of the lever was formulated in antiquity by:', 'MCQ',
    ch=['Newton', 'Archimedes', 'Galileo', 'Kepler'])
d.q('A force of 5.0 N acts <b>perpendicular</b> to an arm of length 2.0 m measured from the point of support. '
    'Calculate the moment of the force.', 'Problem',
    M.rod_fig('Figure 1', 'L = 2.0 m', 'F = 5.0 N', -90, maxw=380))

# ---------------- B ----------------
d.sec('B', 'Lesson 1&ndash;4 &middot; Home assignment 1', 'Using the moment relation')
d.q('If the perpendicular distance is doubled while the force stays constant, then the moment of the force:',
    'MCQ', ch=['is halved', 'is doubled', 'stays constant', 'is reduced to a quarter'])
d.q('A door opens most easily when it is pushed at:', 'MCQ',
    M.door_top('Figure 2', 'width of the door', 'F', 90, 400),
    ch=['the hinge itself', 'the handle, far from the hinge', 'the middle of the door only',
        'any point &mdash; it makes no difference'])
d.q('A moment of 12 N&middot;m is produced by a force of 4.0 N acting perpendicular to its arm. '
    'The length of the perpendicular arm equals:', 'MCQ', ch=['3.0 m', '8.0 m', '48 m', '33 m'])
d.q('A force of 3.0 N acts perpendicular at the end of a horizontal rod, at a distance of 20 m from the '
    'point O. Calculate the moment of the force about O.', 'Problem',
    M.rod_fig('Figure 3', 'L = 20 m', 'F = 3.0 N', 90, maxw=380))

# ---------------- C ----------------
d.sec('C', 'Lesson 1&ndash;5 &middot; Classwork 2', 'The equilibrium of a body')
d.q('A body is in a state of equilibrium when:', 'MCQ',
    ch=['its velocity is always zero', 'it stays at rest or moves with a constant velocity',
        'its velocity changes continuously', 'its mass vanishes'])
d.q('The condition of <b>translational</b> equilibrium of a body is written mathematically as:', 'MCQ',
    ch=['&Sigma;F = mg', '&Sigma;F = 0', '&Sigma;F = ma , where a &ne; 0', '&Sigma;F = F&#8321; &minus; F&#8322; only'])
d.q('To deal with a force acting at an angle, it is resolved into two perpendicular components, and the two '
    'equilibrium equations are then applied to:', 'MCQ',
    ch=['one axis only', 'both axes x and y : &Sigma;F<sub>x</sub> = 0 and &Sigma;F<sub>y</sub> = 0',
        'the angle &theta; only', 'the mass only'])
d.q('The figure shows a wire fixed between two poles, carrying a weight at its middle. <b>Explain how the '
    'angle &theta; at the two fixing points changes</b> if the wire is allowed to sag more at its middle, '
    'and what is the expected effect on the tension T.', 'Explain', F.sagging_wire('Figure 4'))

# ---------------- D ----------------
d.page()
d.sec('D', 'Lesson 1&ndash;5 &middot; Home assignment 2', 'Hanging bodies and the tension in cables')
d.q('A lamp hangs from a cable fixed to the ceiling, together with a light horizontal rope fixed to a wall. '
    'The cable makes an angle of 25&deg; with the vertical. The <b>vertical</b> component of the tension in '
    'the cable must be equal to:', 'MCQ', F.lamp_cable('Figure 5'),
    ch=['zero', 'the weight of the lamp', 'the tension in the horizontal rope', 'half the weight of the lamp'])
d.q('A lamp of mass 0.6 kg hangs from two identical cables, each making an angle of 30&deg; with the '
    'horizontal. If g = 9.8 m/s&sup2;, then the weight of the lamp is approximately:', 'MCQ',
    F.lamp_two_cables('Figure 6'), ch=['0.6 N', '58.8 N', '4.29 N', '5.88 N'])
d.q('If the angle that each cable makes with the horizontal is increased (so that the two cables become '
    'closer to the vertical) while the load stays constant, then the tension in each cable:', 'MCQ',
    ch=['increases', 'decreases', 'stays constant', 'becomes zero'])
d.q('The figure shows the tension in a cable resolved into two components. <b>Explain which of the two '
    'components</b> (the horizontal one or the vertical one) is responsible for balancing the weight of the '
    'hanging body, and <b>why the other component is left out</b> of the vertical equilibrium equation.',
    'Explain', F.tension_components('Figure 7'))

# ---------------- E ----------------
d.sec('E', 'Weekly assessment &nbsp;3', 'Groups A, B and C')
d.grp('Group A')
d.q('If the force is doubled while the perpendicular distance stays constant, then the moment of the force:',
    'MCQ', ch=['is doubled', 'is halved', 'stays constant', 'cannot be determined'])
d.q('A wheel-nut spanner loosens the nut more easily when it is:', 'MCQ',
    M.spanner('Figure 8', 'a longer arm', 'F', 380),
    ch=['shorter', 'longer', 'without an arm', 'its length makes no difference'])
d.q('<b>Compare</b> the moment of a force acting perpendicular to its arm (&theta; = 90&deg;) with the moment '
    'of the <b>same</b> force acting at an angle smaller than 90&deg; on the <b>same</b> arm, in terms of the '
    'magnitude of the moment and the relation used in each case.', 'Compare')
d.q('The figure shows a force F acting at the end of a lever. <b>How can the moment of this force about the '
    'other end of the lever be increased in three different ways</b>, without changing the magnitude of the '
    'force itself?', 'Explain', M.rod_fig('Figure 9', 'L = 0.50 m', 'F = 6.0 N', 30, maxw=390))

d.grp('Group B')
d.q('A force of 4.0 N acts at the end of an arm of length 0.30 m, making an angle of 45&deg; with the arm. '
    'The moment of the force about the point of support is approximately: &nbsp;(sin 45&deg; &asymp; 0.71)',
    'MCQ', M.rod_fig('Figure 10', 'L = 0.30 m', 'F = 4.0 N', 45, maxw=380),
    ch=['0.85 N&middot;m', '1.2 N&middot;m', '1.7 N&middot;m', '6.0 N&middot;m'])
d.q('A ruler is balanced on a point of support. One coin placed at a distance of 15 cm on the right-hand side '
    'balances <i>n</i> identical coins placed at a distance of 5 cm on the left-hand side. '
    'The number of coins <i>n</i> equals:', 'MCQ', F.ruler_coins('Figure 11'),
    ch=['1', '2', '3', '5'])
d.q('<b>Compare</b> the effect of pushing a door at the handle far from the hinge with the effect of pushing '
    'it close to the hinge, in terms of the length of the moment arm and the magnitude of the resulting '
    'moment, with the same applied force.', 'Compare')
d.q('Using the figure, explain &mdash; <b>without any numerical calculation</b> &mdash; why the magnitude of '
    'the moment of the same force differs according to the point (A or B) about which the moment is '
    'calculated, although the force has the same magnitude and the same direction in both cases.', 'Explain',
    F.points_line('Figure 12'))

d.grp('Group C')
d.q('When a spanner with a <b>longer</b> arm is used to produce the same required moment, the force needed is:',
    'MCQ', ch=['larger', 'smaller', 'exactly the same', 'zero'])
d.q('A force of 6.0 N acts at the end of a lever of length 0.50 m, at an angle of 30&deg; to the lever. '
    'The moment of the force about the other end equals approximately: &nbsp;(sin 30&deg; = 0.5)', 'MCQ',
    ch=['1.5 N&middot;m', '0.3 N&middot;m', '0.5 N&middot;m', '0.9 N&middot;m'])
d.q('A force F = 4.0 N acts at an angle of 60&deg; at a point which is 4.0 m from A and 3.0 m from B, '
    'where A and B lie on the same straight line. &nbsp;(sin 60&deg; &asymp; 0.87)', 'MCQ',
    F.points_line('Figure 13'),
    parts=['<b>1)</b> The moment of the force about A equals approximately: &nbsp; '
           '<b>a)</b> 13.9 N&middot;m anticlockwise &nbsp; <b>b)</b> 10.4 N&middot;m clockwise &nbsp; '
           '<b>c)</b> 13.9 N&middot;m clockwise &nbsp; <b>d)</b> 4.0 N&middot;m anticlockwise',
           '<b>2)</b> The moment of the same force about B equals approximately: &nbsp; '
           '<b>a)</b> 13.9 N&middot;m anticlockwise &nbsp; <b>b)</b> 10.4 N&middot;m clockwise &nbsp; '
           '<b>c)</b> 10.4 N&middot;m anticlockwise &nbsp; <b>d)</b> zero'])
d.q('<b>Compare</b> a positive moment with a negative moment, in terms of the sense of rotation that each '
    'one represents.', 'Compare')
d.q('Using the figure, explain &mdash; <b>without any numerical calculation</b> &mdash; how the moment of the '
    'force about O changes if the point of application of F slides along the rod towards O, while the '
    'direction and the magnitude of the force stay the same.', 'Explain', F.rod_slide('Figure 14'))

# ============================ SOLUTIONS ============================
d.page()
d.sec('✓', 'Answer key', 'Solutions &mdash; step by step')
d.hint('Remember the two habits that save marks here: always use the <b>perpendicular</b> distance in a '
       'moment, and always resolve an inclined force before writing an equilibrium equation.')

d.grp('Part A &mdash; Lesson 1-4 &middot; Classwork 1')
d.sol(1, 'the basic relation', 'moment = force &times; perpendicular distance    M = F d', 'B) M = F d')
d.sol(2, 'what a moment measures',
      'a force can move a body (translation) or turn it about a point (rotation);\n'
      'the moment measures the second effect', 'B) the turning effect of the force about a point')
d.sol(3, 'the unit', 'M = F &times; d = newton &times; metre = N&middot;m', 'C) newton &middot; metre',
      why='It is never written as a joule, even though a joule is also a newton &times; a metre; work and '
          'moment are different physical quantities.')
d.sol(4, 'the law of the lever', 'formulated by Archimedes in antiquity', 'B) Archimedes')
d.sol(5, 'a perpendicular force',
      'the force is perpendicular to the arm, so the arm itself is the moment arm :\nM = F &times; L = 5.0 &times; 2.0 = 10 N&middot;m',
      'M = 10 N&middot;m')

d.grp('Part B &mdash; Lesson 1-4 &middot; Home assignment 1')
d.sol(6, 'doubling the arm', 'M = F d , with F constant  &rarr;  M is proportional to d', 'B) it is doubled')
d.sol(7, 'where to push a door',
      'pushing at the handle gives the largest perpendicular distance from the hinge,\nso it gives the largest moment',
      'B) the handle, far from the hinge')
d.sol(8, 'finding the arm', 'M = F d   &rarr;   d = M / F = 12 / 4.0 = 3.0 m', 'A) 3.0 m')
d.sol(9, 'moment about O', 'M = F &times; d = 3.0 &times; 20 = 60 N&middot;m', 'M = 60 N&middot;m')

d.grp('Part C &mdash; Lesson 1-5 &middot; Classwork 2')
d.sol(10, 'the meaning of equilibrium',
      'equilibrium means zero resultant force, so the velocity does not change :\nthe body is either at rest or moving uniformly in a straight line',
      'B) it stays at rest or moves with a constant velocity')
d.sol(11, 'the mathematical condition', '&Sigma;F = 0   (the vector sum of all the forces is zero)', 'B) &Sigma;F = 0')
d.sol(12, 'how the condition is applied',
      'a vector equation is equivalent to one equation for each axis :\n&Sigma;F(x) = 0    and    &Sigma;F(y) = 0',
      'B) on both axes x and y')
d.sol(13, 'the sagging wire',
      'at the lowest point, the two tensions carry the weight between them :\n'
      '    2 T sin α = W          ( α = the angle between the wire and the horizontal )\n'
      '    T = W / ( 2 sin α )\n\n'
      'more sag  &rarr;  α becomes larger  &rarr;  sin α becomes larger  &rarr;  T becomes smaller\n'
      'measured from the pole (the vertical), the angle θ becomes smaller.',
      'a bigger sag makes θ smaller and reduces the tension T',
      why='This is why a clothes line that is pulled almost perfectly horizontal snaps so easily: as the '
          'angle with the horizontal goes to zero, the tension needed to carry the same weight grows without '
          'limit.')

d.grp('Part D &mdash; Lesson 1-5 &middot; Home assignment 2')
d.sol(14, 'the lamp on a cable and a rope',
      'the lamp is in equilibrium, so for the vertical axis :\n'
      '    &Sigma;F(y) = 0   &rarr;   T cos 25° − W = 0\n'
      'the horizontal rope is horizontal, so it adds nothing to the vertical equation',
      'B) the weight of the lamp')
d.sol(15, 'the weight of the lamp', 'W = m g = 0.6 &times; 9.8 = 5.88 N', 'D) 5.88 N',
      why='The mass in kilograms is not a weight; it must be multiplied by g to give a force in newtons.')
d.sol(16, 'raising the angle of the cables',
      '2 T sin α = W   &rarr;   T = W / ( 2 sin α )\n'
      'α increases  &rarr;  sin α increases  &rarr;  T decreases', 'B) decreases')
d.sol(17, 'which component carries the weight',
      'vertical axis :   &Sigma;F(y) = 0   &rarr;   T sin θ = W\n'
      'horizontal axis : &Sigma;F(x) = 0   &rarr;   T cos θ is balanced by another horizontal force',
      'the vertical component T sin &theta; balances the weight',
      why='The horizontal component has no projection on the vertical axis at all, so it simply does not '
          'appear in the vertical equation — it is not "neglected", it is balanced separately by the '
          'other horizontal force.')

d.grp('Part E &mdash; Weekly assessment 3 &middot; Group A')
d.sol(18, 'doubling the force', 'M = F d , with d constant  &rarr;  M is proportional to F', 'A) it is doubled')
d.sol(19, 'the length of the spanner',
      'M = F d : a longer spanner gives a larger d, so the same force produces a larger moment',
      'B) longer')
d.sol(20, 'perpendicular force against an inclined force',
      'θ = 90° :   M = F L        ( sin 90° = 1 )   → the largest possible moment\n'
      'θ < 90° :   M = F L sin θ   ( sin θ < 1 )   → a smaller moment',
      'the perpendicular force always gives the larger moment',
      why='Only the component of the force perpendicular to the arm turns the body; the component along the '
          'arm pulls or pushes it and has no moment.')
d.sol(21, 'three ways to increase the moment',
      'M = F L sin θ , with F fixed :\n\n'
      '1)  use a longer arm L\n'
      '2)  change the direction of the force so that θ = 90°  ( sin θ = 1 )\n'
      '3)  apply the force at the point farthest from the axis of rotation,\n'
      '    which is the same as increasing the perpendicular distance d = L sin θ',
      'longer arm , θ = 90° , or a point farther from the axis')

d.grp('Group B')
d.sol(22, 'an inclined force on a short arm',
      'M = F L sin θ = 4.0 &times; 0.30 &times; sin 45°\n'
      'M = 4.0 &times; 0.30 &times; 0.71 = 0.85 N&middot;m', 'A) 0.85 N&middot;m',
      why='The common trap here is to answer 1.2 N&middot;m, which is F &times; L without sin &theta; — '
          'that value only applies when the force is perpendicular to the arm.')
d.sol(23, 'the balanced ruler',
      'the two moments about the point of support are equal :\n'
      '    ( 1 coin ) &times; 15 = ( n coins ) &times; 5\n'
      '    15 = 5 n   &rarr;   n = 3', 'C) 3 coins')
d.sol(24, 'pushing a door near and far from the hinge',
      'far from the hinge :  large moment arm  &rarr;  large moment  &rarr;  the door turns easily\n'
      'close to the hinge :  small moment arm  &rarr;  small moment  &rarr;  the door hardly turns',
      'the same force gives a much larger moment when it is applied far from the hinge')
d.sol(25, 'why the moment changes with the point',
      'M = F &times; d , and d is the perpendicular distance from the <b>chosen point</b>\n'
      'to the line of action of the force.\n'
      'A and B are at different distances from that line, so each gives a different d,\n'
      'and a point lying on the line of action itself gives d = 0 and M = 0.',
      'because each point has its own perpendicular distance d',
      why='The force never changes; what changes is the geometry between the force and the point you choose '
          'to turn about.')

d.grp('Group C')
d.sol(26, 'a longer spanner for the same moment',
      'M = F d , with M fixed  &rarr;  F = M / d\nd larger  &rarr;  F smaller', 'B) smaller')
d.sol(27, 'inclined force on a lever',
      'M = F L sin θ = 6.0 &times; 0.50 &times; sin 30°\nM = 6.0 &times; 0.50 &times; 0.5 = 1.5 N&middot;m',
      'A) 1.5 N&middot;m')
d.sol(28, 'the same force about two different points',
      '1)  about A :   d(A) = 4.0 sin 60° = 4.0 &times; 0.87 = 3.48 m\n'
      '    M(A) = F &times; d(A) = 4.0 &times; 3.48 = 13.9 N&middot;m\n'
      '    the force turns the line anticlockwise about A\n\n'
      '2)  about B :   d(B) = 3.0 sin 60° = 2.61 m\n'
      '    M(B) = 4.0 &times; 2.61 = 10.4 N&middot;m , anticlockwise as well',
      '1) a) 13.9 N&middot;m anticlockwise &nbsp;&middot;&nbsp; 2) c) 10.4 N&middot;m anticlockwise')
d.sol(29, 'the sign of a moment',
      'positive moment  &rarr;  anticlockwise rotation\nnegative moment  &rarr;  clockwise rotation',
      'the sign is only a label for the sense of rotation',
      why='The sign lets moments be added like ordinary numbers: a positive and a negative moment of the same '
          'size cancel each other exactly.')
d.sol(30, 'sliding the force towards O',
      'M = F &times; d , with F fixed in size and direction\n'
      'as the point of application slides towards O, the perpendicular distance d gets smaller,\n'
      'so the moment decreases in the same ratio, until d = 0 at O and the moment vanishes',
      'the moment decreases steadily and becomes zero at O',
      why='At O the line of action of the force passes through the point itself, and a force whose line of '
          'action passes through a point can never turn the body about that point.')

d.foot('Lessons 1&ndash;4 and 1&ndash;5 &middot; Moment and Equilibrium &middot; Mr. Gemy',
       'M = F L sin &theta; &nbsp;&middot;&nbsp; &Sigma;F = 0')
d.save('l45.html')
print('l45.html written -', d.n, 'questions')

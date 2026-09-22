# -*- coding: utf-8 -*-
import figs_l6 as F
from docbase import Doc

d = Doc('Unit 1 &middot; Lesson 1&ndash;6 + Review', 'Power and Efficiency<br>&amp; Equilibrium Review',
        'The rate of doing work, the efficiency of a machine, and a full review of a body held in '
        'equilibrium by cables and springs.',
        ['Grade 11 &middot; Egyptian Baccalaureate', '22 questions', 'Step-by-step solutions',
         'g = 9.8 m/s&sup2;'], 'Power and Efficiency')

d.kit('The toolkit for this sheet', [
    ('P = &Delta;W / &Delta;t', 'average power &mdash; unit : watt'),
    ('P = F v cos &theta;', 'power of a force on a moving body'),
    ('&eta; = useful output / total input', 'efficiency, always &lt; 100 %'),
    ('W = m g h', 'work done in raising a load'),
    ('&Sigma;F<sub>x</sub> = 0 , &Sigma;F<sub>y</sub> = 0', 'equilibrium on each axis'),
    ('T = W / ( 2 sin &alpha; )', 'two symmetric cables carrying a weight'),
])
d.hint('<b>Watch the difference.</b> Work tells you <i>how much</i> energy was transferred; power tells you '
       '<i>how fast</i> it was transferred. Two machines can do exactly the same work and still have very '
       'different powers.')

# ---------------- A ----------------
d.sec('A', 'Lesson 1&ndash;6 &middot; Classwork 1', 'Power and efficiency')
d.q('Power is a measure of:', 'MCQ',
    ch=['the amount of work done only', 'the rate of doing work or of transferring energy',
        'the magnitude of the force only', 'the total displacement of the body'])
d.q('The mathematical expression used to calculate the average power from the work and the time is:', 'MCQ',
    ch=['P = W &times; t', 'P = &Delta;W / &Delta;t', 'P = W + t', 'P = W / t&sup2;'])
d.q('The SI unit of power is:', 'MCQ', ch=['the joule (J)', 'the watt (W)', 'the newton (N)',
                                           'the kilogram (kg)'])
d.q('The figure shows two lifts A and B raising the <b>same</b> load through the <b>same</b> height, but in '
    'different times. <b>Explain which lift has the greater power</b>, and <b>which one does the greater '
    'useful work.</b> &nbsp;(g = 9.8 m/s&sup2;)', 'Explain', F.two_lifts('Figure 1'))

# ---------------- B ----------------
d.sec('B', 'Lesson 1&ndash;6 &middot; Home assignment 1', 'Using power and efficiency')
d.q('When two lifts raise the same load through the same vertical height, but one of them finishes the lift '
    'in a shorter time, then this lift has:', 'MCQ',
    ch=['a greater useful work', 'a greater power', 'necessarily a greater efficiency',
        'the same work and the same power'])
d.q('A machine has an efficiency of 40 %. If the total input energy supplied to it is 250 J, then the useful '
    'output energy equals:', 'MCQ', ch=['100 J', '250 J', '62.5 J', '400 J'])
d.q('An electric water heater receives an electric power of 2400 W and produces a useful thermal power of '
    '2040 W. Its efficiency equals:', 'MCQ', ch=['85 %', '15 %', '117 %', '60 %'])
d.q('The figure shows a force F acting at an angle &theta; to the direction of motion of a body moving with a '
    'velocity v. <b>Explain what happens to the power produced by the force as &theta; gets closer to '
    '90&deg;</b>, compared with the case in which the force acts exactly along the direction of motion '
    '(&theta; = 0&deg;).', 'Explain', F.block_force_angle('Figure 2'))

# ---------------- C ----------------
d.page()
d.sec('C', 'Review &amp; weekly assessment', 'A body in equilibrium under several forces')
d.q('A rigid body is in equilibrium under the action of three forces only: F<sub>1</sub> = 10 N upwards and '
    'F<sub>2</sub> = 6 N downwards. The third force F<sub>3</sub> needed to keep the body in equilibrium '
    '(on the same vertical line) must be:', 'MCQ', F.three_forces('Figure 3'),
    ch=['4 N upwards', '4 N downwards', '16 N upwards', 'zero'])
d.q('A lamp of mass 3.0 kg hangs from a cable fixed to the ceiling together with a light horizontal rope '
    'fixed to a wall, and the cable makes an angle of 25&deg; with the vertical. The weight of the lamp is '
    '29.4 N, so the tension T in the cable is approximately:', 'MCQ',
    ch=['26.8 N', '32.3 N', '12.4 N', '29.4 N'])
d.q('For a lamp hanging in equilibrium from two identical cables that make the <b>same</b> angle with the '
    'horizontal, the two horizontal components of the tensions:', 'MCQ',
    ch=['are equal in magnitude and opposite in direction, so they cancel each other',
        'add together', 'have nothing to do with the equilibrium', 'each one equals the weight'])
d.q('If the angle that each cable makes with the horizontal is <b>decreased</b> (so that the two cables '
    'become closer to the horizontal) while the weight of the load stays constant, then the tension in each '
    'cable:', 'MCQ', ch=['increases', 'decreases', 'stays constant', 'becomes zero'])
d.q('If the angle that each cable makes with the horizontal is <b>increased</b> (so that the two cables '
    'become closer to the vertical) while the weight of the load stays constant, then the tension in each '
    'cable:', 'MCQ', ch=['increases', 'decreases', 'stays constant', 'becomes zero'])
d.q('A metal piece of mass 1.5 kg hangs at rest from two identical light springs, each making an angle of '
    '40&deg; with the vertical, the spring constant of each being 60 N/m. The weight of the piece is '
    'approximately: &nbsp;(g = 9.8 m/s&sup2;)', 'MCQ', F.two_springs('Figure 4'),
    ch=['1.5 N', '14.7 N', '6.0 N', '60 N'])
d.q('For the same metal piece of the previous question, calculate the force F in <b>each</b> spring. '
    '&nbsp;(cos 40&deg; &asymp; 0.77)', 'Problem')
d.q('The figure shows a lamp of mass 4.0 kg hanging from a cable fixed to the ceiling and a light horizontal '
    'rope fixed to a wall. The tension measured in the horizontal rope is P = 15 N. '
    '<b>Calculate the tension T in the cable.</b>', 'Problem', F.lamp_wall('Figure 5'))
d.q('For the same lamp of the previous question, <b>find the angle &theta;</b> that the cable makes with the '
    'vertical.', 'Problem')
d.q('Using the figure, <b>explain how the diagram shows</b> that the sum of the two vertical components of '
    'the tensions equals the weight of the lamp, while the two horizontal components cancel each other.',
    'Explain', F.cables_components('Figure 6'))
d.q('<b>Compare</b> the case of a lamp hanging from two identical cables making the same angle with the case '
    'of another lamp of the same weight hanging from two cables making <b>different</b> angles, in terms of '
    'whether the tensions in the two cables are equal or different.', 'Compare')
d.q('The figure shows a shop sign of mass 10 kg hanging from two light cables attached to a horizontal beam. '
    'The first cable makes an angle of 35&deg; with the horizontal and the second makes 65&deg; with the '
    'horizontal. <b>Find the tension in each cable.</b> &nbsp;(g = 9.8 m/s&sup2;)', 'Problem',
    F.sign_cables('Figure 7'))
d.q('For a lamp of weight W hanging in equilibrium from two identical cables making the same angle with the '
    'horizontal, calculate the <b>sum of the two vertical components</b> of the tensions.', 'Problem')
d.q('The figure shows a book resting on a table. <b>What changes in this diagram</b> if another book of the '
    'same weight is placed on top of the first one? State clearly which of the two forces changes in value '
    'and which one stays the same, and identify the <b>source</b> of each force.', 'Explain',
    F.book_table('Figure 8'))

# ============================ SOLUTIONS ============================
d.page()
d.sec('✓', 'Answer key', 'Solutions &mdash; step by step')
d.hint('For every hanging body, write the two equilibrium equations separately: the horizontal one and the '
       'vertical one. Almost every question in this sheet falls out of those two lines.')

d.grp('Part A &mdash; Power and efficiency')
d.sol(1, 'what power measures',
      'work tells how much energy was transferred;\npower tells how fast it was transferred',
      'B) the rate of doing work or of transferring energy')
d.sol(2, 'the relation', 'P = ΔW / Δt      ( work done ÷ time taken )', 'B) P = &Delta;W / &Delta;t')
d.sol(3, 'the unit', '1 watt = 1 joule / second', 'B) the watt (W)')
d.sol(4, 'the two lifts',
      'the two lifts raise the same load through the same height, so the useful work is the same :\n'
      '    W = m g h = 600 × 9.8 × 9.0 = 52 920 J  ≈ 5.3 × 10⁴ J\n\n'
      'lift A :  P = W / t = 52 920 / 24 = 2205 W\n'
      'lift B :  P = W / t = 52 920 / 12 = 4410 W',
      'the same useful work; lift B has double the power',
      why='Power is not "more work", it is the <b>same</b> work delivered in less time. Lift B finishes in '
          'half the time, so its power is twice as large.')

d.grp('Part B &mdash; Home assignment 1')
d.sol(5, 'the faster lift', 'same W , smaller t   &rarr;   P = W / t is larger', 'B) a greater power')
d.sol(6, 'useful output from the efficiency',
      'η = useful output / total input\nuseful output = η × input = 0.40 × 250 = 100 J', 'A) 100 J')
d.sol(7, 'the efficiency of the heater',
      'η = useful power / input power = 2040 / 2400 = 0.85 = 85 %', 'A) 85 %',
      why='An efficiency greater than 100 % is impossible, which rules out the 117 % option immediately.')
d.sol(8, 'the power of an inclined force',
      'P = F v cos θ\n\n'
      'θ = 0°   :  cos θ = 1   &rarr;  P = F v          (the largest possible power)\n'
      'θ → 90° :  cos θ → 0   &rarr;  P → zero',
      'the power falls from its maximum F v down to zero',
      why='Only the component of the force along the motion, F cos &theta;, transfers energy to the body; '
          'a force perpendicular to the motion does no work at all.')

d.grp('Part C &mdash; Equilibrium: review and weekly assessment')
d.sol(9, 'the third force',
      '&Sigma;F(y) = 0\n+ 10 − 6 + F₃ = 0   &rarr;   F₃ = − 4 N\nthe minus sign means: directed downwards',
      'B) 4 N downwards')
d.sol(10, 'the tension in the cable',
      'the rope is horizontal, so the vertical equation contains the cable only :\n'
      'T cos 25° = W = 29.4 N\n'
      'T = 29.4 / 0.906 = 32.4 N', 'B) 32.3 N')
d.sol(11, 'the horizontal components',
      '&Sigma;F(x) = 0 , and the two cables are symmetric, so the two horizontal\n'
      'components have the same size and opposite directions',
      'A) equal and opposite, so they cancel each other')
d.sol(12, 'cables closer to the horizontal',
      'T = W / ( 2 sin α )\nα decreases  &rarr;  sin α decreases  &rarr;  T increases', 'A) increases',
      why='As the cables approach the horizontal, sin &alpha; approaches zero and the tension grows without '
          'limit — this is why a washing line pulled dead straight snaps so easily.')
d.sol(13, 'cables closer to the vertical',
      'T = W / ( 2 sin α )\nα increases  &rarr;  sin α increases  &rarr;  T decreases', 'B) decreases')
d.sol(14, 'the weight of the metal piece', 'W = m g = 1.5 × 9.8 = 14.7 N', 'B) 14.7 N',
      why='The spring constant and the angle are not needed for the weight; they are needed for the next '
          'question.')
d.sol(15, 'the force in each spring',
      'the two springs are identical, so each carries the same force F.\n'
      'each spring makes 40° with the <b>vertical</b>, so its vertical component is F cos 40° :\n\n'
      '&Sigma;F(y) = 0   &rarr;   2 F cos 40° = W\n'
      '2 F × 0.77 = 14.7\n'
      'F = 14.7 / 1.54 = 9.5 N', 'F ≈ 9.5 N in each spring')
d.sol(16, 'the tension from the horizontal rope',
      'the cable has to balance both the weight and the pull of the rope :\n'
      '    vertical   : T cos θ = W = m g = 4.0 × 9.8 = 39.2 N\n'
      '    horizontal : T sin θ = P = 15 N\n\n'
      'T = √( W² + P² ) = √( 39.2² + 15² ) = √1761.6 = 42.0 N', 'T = 42.0 N')
d.sol(17, 'the angle of the cable',
      'tan θ = P / W = 15 / 39.2 = 0.3827\nθ = 20.9°', 'θ ≈ 20.9° with the vertical')
d.sol(18, 'reading the component diagram',
      'vertical axis   : &Sigma;F(y) = 0  &rarr;  T₁y + T₂y − W = 0  &rarr;  T₁y + T₂y = W\n'
      'horizontal axis : &Sigma;F(x) = 0  &rarr;  T₁x = T₂x  (opposite directions)',
      'the vertical components carry the weight, the horizontal ones cancel',
      why='The weight has no horizontal component at all, so nothing is left for the horizontal components to '
          'balance except each other.')
d.sol(19, 'equal angles against different angles',
      'equal angles   : by symmetry the two tensions are equal , T = W / ( 2 sin α )\n'
      'different angles : the tensions are <b>not</b> equal; the cable that is closer to the\n'
      '                   vertical (the larger angle with the horizontal) carries the larger tension',
      'equal angles → equal tensions ; different angles → different tensions')
d.sol(20, 'the shop sign on two cables',
      'W = m g = 10 × 9.8 = 98 N\n\n'
      'horizontal : T₁ cos 35° = T₂ cos 65°\n'
      '             0.819 T₁ = 0.423 T₂      &rarr;   T₁ = 0.516 T₂\n\n'
      'vertical   : T₁ sin 35° + T₂ sin 65° = 98\n'
      '             0.574 ( 0.516 T₂ ) + 0.906 T₂ = 98\n'
      '             1.202 T₂ = 98      &rarr;   T₂ = 81.5 N\n'
      '             T₁ = 0.516 × 81.5 = 42.1 N',
      'T₁ = 42.1 N , T₂ = 81.5 N',
      why='The steeper cable (65&deg;) carries almost twice the tension, because it has to supply the larger '
          'share of the vertical support.')
d.sol(21, 'the sum of the vertical components',
      '&Sigma;F(y) = 0   &rarr;   T₁y + T₂y = W = m g',
      'the sum equals the weight of the lamp')
d.sol(22, 'a second book on the table',
      'the table now has to support two books, so the normal force becomes :\n'
      '    F(N) = 2 m g        (it doubles)\n'
      'the weight of the first book is still m g , because it depends only on its own\n'
      'mass and on g.',
      'F(N) doubles, the weight of the book itself does not change',
      why='The two forces have different <b>sources</b>: the weight is the gravitational pull of the Earth '
          'on that one book, while the normal force is a contact reaction from the table that adjusts itself '
          'to carry whatever rests on it.')

d.foot('Lesson 1&ndash;6 &middot; Power, Efficiency and Equilibrium &middot; Mr. Gemy',
       'P = &Delta;W/&Delta;t &nbsp;&middot;&nbsp; &eta; = useful / input')
d.save('l6.html')
print('l6.html written -', d.n, 'questions')

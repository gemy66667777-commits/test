# -*- coding: utf-8 -*-
import figs_l22 as F
from docbase import Doc

d = Doc('Unit 2 &middot; Lessons 2&ndash;2 and 2&ndash;3',
        'The Vertical Spring and<br>the Simple Pendulum',
        'Why the weight does not enter the periodic time of a spring, and the periodic time of a simple '
        'pendulum T = 2&pi;&radic;(L/g).',
        ['Grade 11 &middot; Egyptian Baccalaureate', '28 questions', 'Step-by-step solutions',
         'g = 9.8 m/s&sup2; &middot; &pi; = 3.14'],
        'The Vertical Spring and the Simple Pendulum')

d.kit('The toolkit for these two lessons', [
    ('T = 2&pi; &radic;( m / k )', 'a spring pendulum &mdash; horizontal or vertical'),
    ('T = 2&pi; &radic;( L / g )', 'a simple pendulum, small angle only'),
    ('k e = m g', 'the static extension of a loaded vertical spring'),
    ('T = t / n', 'time n complete oscillations, then divide'),
    ('T &prop; &radic;m &nbsp;,&nbsp; T &prop; 1/&radic;k', 'for the spring pendulum'),
    ('T &prop; &radic;L &nbsp;,&nbsp; T &prop; 1/&radic;g', 'for the simple pendulum'),
])
d.hint('<b>Two things never appear in a periodic time.</b> The <b>amplitude</b> never appears in either '
       'formula, and the <b>mass of the bob</b> never appears in the pendulum formula. Whenever a question '
       'changes one of those two, the answer is &ldquo;no change&rdquo; &mdash; and whenever it changes m, '
       'k, L or g, use a <b>ratio</b> rather than a full substitution.')

# ---------------- A : lesson 2-2 classwork ----------------
d.sec('A', 'Lesson 2&ndash;2 &middot; Classwork &nbsp;1', 'The vertical mass&ndash;spring system')
d.q('A mass of magnitude 0.20 kg is fixed to a spring whose force constant is '
    'k = 80 N&middot;m&#8315;&sup1;, and it vibrates with simple harmonic motion. <b>Calculate the periodic '
    'time of the vibration</b>, using &pi; = 3.14.', 'Problem')
d.q('For a body vibrating with simple harmonic motion on a spring, which of the following statements is '
    'correct for the periodic time T?', 'MCQ', F.horizontal_vs_vertical('Figure 1'),
    ch=['it depends on the acceleration due to gravity g only',
        'T = 2&pi;&radic;(k/m)',
        'T = 2&pi;&radic;(m/k) , and it does not depend on the acceleration due to gravity g',
        'it increases with the increase of the amplitude A only'])

# ---------------- B : lesson 2-2 home assignment ----------------
d.sec('B', 'Lesson 2&ndash;2 &middot; Home assignment &nbsp;1', 'The role of the weight')
d.q('In a system of a mass hung vertically from a spring, the equilibrium position changes because of the '
    'weight of the mass. <b>Explain why</b> the periodic time of the vibration is the same as that of a '
    'horizontal system having the same mass and the same spring constant, showing the role of the '
    'acceleration due to gravity in this.', 'Explain', F.vertical_spring('Figure 2'))
d.q('A mass was hung from a vertical spring and began to vibrate with simple harmonic motion about the '
    'equilibrium position. If the mass of the body is increased while the spring constant stays as it is, '
    '<b>how does the periodic time of the vibration change?</b> Explain your answer using the mathematical '
    'relation for the periodic time.', 'Explain')
d.q('A mass of magnitude 0.50 kg was hung from a vertical spring whose force constant is k = 20 N/m, and '
    'was left to move with simple harmonic motion. <b>Calculate the periodic time of the vibration</b>, '
    'taking &pi; = 3.14.', 'Problem')
d.q('In an experiment on a spring pendulum, a mass of magnitude 0.40 kg was hung from a spring of force '
    'constant 40 N/m. If the mass is replaced by another one of magnitude 0.80 kg while the spring stays '
    'the same, what is the ratio between the new periodic time and the original periodic time?', 'MCQ',
    ch=['2 : 1', '&radic;2 : 1', '1 : &radic;2', '1 : 2'])

# ---------------- C : lesson 2-3 classwork ----------------
d.sec('C', 'Lesson 2&ndash;3 &middot; Classwork &nbsp;2', 'The simple pendulum')
d.q('In the simple pendulum, <b>why</b> is its motion considered to be approximately simple harmonic when '
    'the angle of displacement is small?', 'Explain', F.pendulum_forces('Figure 3'))
d.q('For a simple pendulum vibrating through a small angle, the periodic time T depends basically on:',
    'MCQ', F.pendulum_geometry('Figure 4'),
    ch=['the mass of the bob and the amplitude of the vibration',
        'the length of the string and the acceleration due to gravity',
        'the mass of the bob and the length of the string',
        'the amplitude of the vibration and the mass of the bob'])
d.q('A simple pendulum has a string of length L = 1.8 m, the acceleration due to gravity is '
    'g = 9.8 m/s&sup2;, and &pi; = 3.14. <b>Calculate the periodic time T to the nearest two decimal '
    'places</b>, showing the law and the substitution.', 'Problem')

# ---------------- D : lesson 2-3 home assignment ----------------
d.sec('D', 'Lesson 2&ndash;3 &middot; Home assignment &nbsp;2', 'Measuring and changing T')
d.q('If the length of the string of a simple pendulum is increased while the acceleration due to gravity of '
    'the Earth stays constant, <b>how does the periodic time of the pendulum change?</b> Give the reason.',
    'Explain')
d.q('<b>Describe a suitable practical method</b> for measuring the periodic time of a simple pendulum with '
    'greater accuracy, showing the role of timing a large number of oscillations.', 'Explain',
    F.pendulum_timing('Figure 5'))
d.q('A simple pendulum took a time of magnitude 14.0 s to complete 10 full oscillations. <b>Calculate the '
    'periodic time of one oscillation</b>, then state the relation that connects the measured time with the '
    'number of oscillations and the periodic time.', 'Problem')
d.q('If the length of the string of a simple pendulum is increased to <b>four times</b> its value, while '
    'the acceleration due to gravity stays constant and the angle of vibration stays small, then the '
    'periodic time becomes:', 'MCQ',
    ch=['half its value', 'twice its value', 'four times its value', 'as it is, without change'])

# ---------------- E : weekly assessment ----------------
d.sec('E', 'Weekly assessment', 'Groups A, B and C')
d.grp('Group A')
d.q('A simple pendulum of length 1.0 m vibrates through small angles. If the length of the string is '
    'increased to 4.0 m while g stays constant, then the periodic time becomes:', 'MCQ',
    ch=['T / 4', 'T / 2', '2T', '4T'])
d.q('A mass of magnitude 0.50 kg is attached to a spring whose constant is 20 N/m. The periodic time of the '
    'spring pendulum depends on:', 'MCQ',
    ch=['the mass and the spring constant', 'the amplitude only',
        'the acceleration due to gravity only', 'the weight of the body only'])
d.q('<b>Explain briefly why</b> the periodic time of a simple pendulum, at small angles, does not depend on '
    'the mass of the bob.', 'Explain')
d.q('<b>Calculate:</b> find the periodic time of a simple pendulum whose length is 0.40 m, if '
    'g = 9.8 m/s&sup2; and &pi; = 3.14, writing the law and the unit.', 'Problem')
d.q('<b>Compare</b>, in two or three lines, between the factors on which the periodic time of the simple '
    'pendulum depends and the factors on which the periodic time of the spring pendulum depends.', 'Explain')

d.grp('Group B')
d.q('Two simple pendulums are in the same place; the length of the first is 0.25 m and the length of the '
    'second is 1.00 m. The ratio between their periodic times respectively equals:', 'MCQ',
    F.two_pendulums('Figure 6'),
    ch=['1 / 4', '1 / 2', '2', '4'])
d.q('If the mass of the body hung from a vertical spring is doubled while the spring constant stays as it '
    'is, then the periodic time:', 'MCQ',
    ch=['decreases to half', 'does not change', 'increases by a factor of &radic;2',
        'becomes four times as large'])
d.q('<b>State an important condition</b> that makes the motion of a simple pendulum approximately simple '
    'harmonic, and <b>state the effect</b> of increasing the small amplitude on the periodic time, '
    'approximately.', 'Explain')
d.q('<b>Calculate:</b> a body of mass 0.20 kg is attached to a horizontal spring whose constant is '
    '80 N/m. Find the periodic time of the vibration using &pi; = 3.14, showing the steps of the solution.',
    'Problem')
d.q('<b>Analyse the following situation:</b> a simple pendulum is moved to a place in which the '
    'acceleration due to gravity is smaller. Does the periodic time increase or decrease? Explain using the '
    'mathematical relation.', 'Explain')

d.grp('Group C')
d.q('If the spring constant becomes four times its value while the mass stays constant, then the periodic '
    'time of the spring pendulum becomes:', 'MCQ', ch=['4T', '2T', 'T / 2', 'T / 4'])
d.q('Which of the following changes does <b>not</b> affect, approximately, the time of one cycle of a '
    'simple pendulum at small angles?', 'MCQ',
    ch=['increasing the length of the string', 'changing the acceleration due to gravity',
        'changing the mass of the bob', 'using another place on the Earth'])
d.q('<b>Explain:</b> on hanging a mass from a vertical spring the equilibrium position changes, but the '
    'periodic time does not depend on the magnitude of the static extension.', 'Explain')
d.q('<b>Calculate:</b> a simple pendulum whose length is 0.90 m vibrates through small angles, with '
    'g = 9.8 m/s&sup2; and &pi; = 3.14. Find the periodic time to the nearest two decimal places.',
    'Problem')
d.q('<b>Compare analytically:</b> if we want to double the periodic time, what do we do with the length of '
    'the simple pendulum? And what do we do with the mass of the spring pendulum while the spring constant '
    'stays fixed? State the relations used.', 'Explain')

# ---------------- solutions ----------------
d.page()
d.sec('✓', 'Answer key', 'Solutions — step by step')
d.hint('<b>Work with ratios.</b> Almost every question in these two lessons changes one quantity and asks '
       'what happens to T. Write the law, see which power the quantity carries, and take the square root: '
       'T &prop; &radic;m , T &prop; 1/&radic;k , T &prop; &radic;L , T &prop; 1/&radic;g. Nothing else is '
       'needed.')

d.grp('Part A — Lesson 2–2, Classwork 1')
d.sol(1, 'the periodic time of the 0.20 kg mass on an 80 N/m spring',
      '    T = 2π √( m / k )\n'
      '    T = 2 × 3.14 × √( 0.20 / 80 )\n'
      '    T = 6.28 × √0.0025 = 6.28 × 0.05\n'
      '    T = 0.314 s',
      'T = 0.314 s',
      why='Do the division inside the root <b>first</b>. Taking each square root separately and then '
          'dividing is the commonest slip here.')
d.sol(2, 'which statement is true for T',
      'the periodic time of a spring pendulum is :\n'
      '    T = 2π √( m / k )\n'
      'it contains only m and k — there is no g and no amplitude in it.\n'
      'choice (B) is upside down : √(k/m) is ω , not T.',
      'C) T = 2&pi;&radic;(m/k) , and it does not depend on g',
      why='Hanging the spring vertically brings gravity into the problem, but only to <b>move</b> the '
          'equilibrium position. Once the body oscillates about that new position, g has no further part '
          'to play — which is the subject of question 3.')

d.grp('Part B — Lesson 2–2, Home assignment 1')
d.sol(3, 'why the vertical system has the same periodic time as the horizontal one',
      'at the new equilibrium position the spring is already stretched by e , and :\n'
      '    k e = m g          →          e = m g / k\n'
      'now measure the displacement x from that new position. the stretch is ( e + x ),\n'
      'so the resultant force on the body is :\n'
      '    F = m g − k ( e + x ) = ( m g − k e ) − k x = 0 − k x = − k x\n'
      'which is exactly the horizontal equation, so  T = 2π √( m / k )  as well.',
      'because the weight is exactly cancelled by the initial stretch, leaving F = &minus;kx again',
      why='<b>The role of g.</b> Gravity does one job only: it decides <b>where</b> the equilibrium '
          'position is ( e = mg/k ). It does not change the <b>stiffness</b> of the restoring force, and '
          'the stiffness is what sets the timing. That is why the same mass on the same spring keeps time '
          'identically lying on a bench or hanging from the ceiling — and why it would keep the same '
          'time on the Moon.')
d.sol(4, 'increasing the mass at constant k',
      '    T = 2π √( m / k )        →        T ∝ √ m\n'
      'so a larger m gives a larger T : the vibration becomes slower.\n'
      'quantitatively, multiplying m by n multiplies T by √n :\n'
      '    m → 4m   gives   T → 2T          m → 9m   gives   T → 3T',
      'the periodic time increases, in proportion to &radic;m',
      why='The extra mass adds inertia without adding any restoring force, so the same spring needs longer '
          'to turn the body round at each end of the swing.')
d.sol(5, 'the 0.50 kg mass on a 20 N/m vertical spring',
      '    T = 2π √( m / k )\n'
      '    T = 6.28 × √( 0.50 / 20 ) = 6.28 × √0.025\n'
      '    T = 6.28 × 0.1581\n'
      '    T = 0.993 ≈ 0.99 s',
      'T &asymp; 0.99 s',
      why='The spring is vertical, but as question 3 showed, that changes nothing in the formula — '
          'g never appears.')
d.sol(6, 'doubling the mass on the same spring',
      '    T ∝ √ m        ( the spring is unchanged )\n'
      '    T(new) / T(old) = √( 0.80 / 0.40 ) = √2\n'
      'so the ratio of the new periodic time to the original one is √2 : 1',
      'B) &radic;2 : 1',
      why='&radic;2 &asymp; 1.41, so the vibration becomes about 41 % slower — not twice as slow. '
          'Doubling the periodic time would need <b>four</b> times the mass.')

d.grp('Part C — Lesson 2–3, Classwork 2')
d.sol(7, 'why a small swing of a pendulum is simple harmonic',
      'resolve the weight along the string and along the tangent of the path :\n'
      '    along the string   :  mg cos θ    ( balanced by the tension )\n'
      '    along the tangent  :  mg sin θ    ( this is the restoring force )\n'
      'so        F = − m g sin θ\n'
      'for a small angle measured in radians,  sin θ ≈ θ = x / L , so :\n'
      '    F ≈ − m g x / L = − ( m g / L ) x        →        F ∝ − x',
      'because for a small angle sin &theta; &asymp; &theta;, which turns F = &minus;mg sin &theta; into '
      'F = &minus;(mg/L) x',
      why='<b>This is the whole approximation.</b> The definition of simple harmonic motion is that the '
          'restoring force is proportional to the displacement and opposite to it. The exact pendulum '
          'force goes with sin&theta;, which is <b>not</b> proportional to &theta; — but for small '
          'angles the two are almost equal (at 10&deg;, sin&theta; and &theta; differ by only about '
          '0.5 %). Comparing with F = &minus;kx gives an effective k = mg/L, and substituting in '
          'T = 2&pi;&radic;(m/k) gives T = 2&pi;&radic;(L/g) — with the mass cancelling out.')
d.sol(8, 'what T of a simple pendulum depends on',
      '    T = 2π √( L / g )\n'
      'the only two quantities in the formula are the length of the string L and the\n'
      'acceleration due to gravity g. the mass of the bob and the amplitude are absent.',
      'B) the length of the string and the acceleration due to gravity')
d.sol(9, 'the periodic time for L = 1.8 m',
      '    T = 2π √( L / g )\n'
      '    T = 2 × 3.14 × √( 1.8 / 9.8 )\n'
      '    T = 6.28 × √0.1837\n'
      '    T = 6.28 × 0.4286\n'
      '    T = 2.6914 ≈ 2.69 s',
      'T = 2.69 s',
      why='A useful benchmark to remember: a pendulum about 1 m long has a periodic time of about 2 s, so '
          'a 1.8 m pendulum taking a little under 2.7 s is exactly the right size of answer.')

d.grp('Part D — Lesson 2–3, Home assignment 2')
d.sol(10, 'lengthening the string',
      '    T = 2π √( L / g )        →        T ∝ √ L      ( g fixed )\n'
      'so a longer string gives a longer periodic time — but only as the square root,\n'
      'so L must be made four times larger to double T.',
      'the periodic time increases, in proportion to &radic;L',
      why='A longer string means a gentler arc: the restoring force per unit displacement, mg/L, becomes '
          'smaller, so the bob is pulled back more weakly and takes longer to return.')
d.sol(11, 'measuring the periodic time accurately',
      'method :\n'
      '  1  set the pendulum swinging through a <b>small</b> angle ( less than about 10° )\n'
      '  2  start the stopwatch as the bob passes the <b>lowest point</b>, where it is fastest\n'
      '  3  count n = 10 ( or 20 ) <b>complete</b> oscillations, there and back\n'
      '  4  read the total time t , then        T = t / n\n'
      '  5  repeat and take the mean',
      'T = t / n , timing n complete oscillations rather than a single one',
      why='<b>Why n oscillations?</b> The uncertainty of a stopwatch reading comes almost entirely from '
          'the experimenter’s reaction time, roughly 0.2 s, and that error is the <b>same</b> whether '
          'you time one oscillation or twenty. Dividing the total time by n divides the error by n as '
          'well: timing 20 swings turns a 0.2 s error into a 0.01 s error. Starting at the lowest point '
          'helps for the same reason — the bob is moving fastest there, so the instant of passing is '
          'the easiest to judge.')
d.sol(12, '10 oscillations in 14.0 s',
      '    T = t / n\n'
      '    T = 14.0 / 10\n'
      '    T = 1.40 s',
      'T = 1.40 s &nbsp;&middot;&nbsp; the relation is T = t / n',
      why='Reading it backwards, t = n T is a quick way to predict how long an experiment will take.')
d.sol(13, 'four times the length',
      '    T ∝ √ L\n'
      '    T(new) / T(old) = √( 4L / L ) = √4 = 2\n'
      '    T(new) = 2 T(old)',
      'B) twice its value')

d.grp('Part E — Weekly assessment, Group A')
d.sol(14, 'from 1.0 m to 4.0 m',
      '    T ∝ √ L        →        T(new) = √( 4.0 / 1.0 ) × T = 2 T',
      'C) 2T')
d.sol(15, 'what T of a spring pendulum depends on',
      '    T = 2π √( m / k )\n'
      'only m and k appear — not the amplitude, not g, not the weight.',
      'A) the mass and the spring constant')
d.sol(16, 'why the mass of the bob does not matter',
      'the restoring force along the tangent is proportional to the mass :\n'
      '    F = − m g sin θ\n'
      'but the acceleration it produces divides by that same mass :\n'
      '    a = F / m = − g sin θ        ( no m left )',
      'because the mass appears in both the restoring force and the inertia, and cancels out',
      why='It is the same reason why all bodies fall freely with the same acceleration. A heavier bob is '
          'pulled back harder, but it is also that much harder to move, and the two effects cancel exactly '
          '— which is why T = 2&pi;&radic;(L/g) has no m in it.')
d.sol(17, 'the periodic time for L = 0.40 m',
      '    T = 2π √( L / g )\n'
      '    T = 6.28 × √( 0.40 / 9.8 ) = 6.28 × √0.0408\n'
      '    T = 6.28 × 0.2020\n'
      '    T = 1.2688 ≈ 1.27 s',
      'T = 1.27 s',
      why='The unit matters: L in metres and g in m/s&sup2; make L/g a time squared, so the square root is '
          'a time in <b>seconds</b>.')
d.sol(18, 'the two periodic times compared',
      '    simple pendulum :   T = 2π √( L / g )    →  L and g only\n'
      '    spring pendulum :   T = 2π √( m / k )    →  m and k only\n'
      'neither of them contains the amplitude.',
      'the pendulum depends on L and g; the spring depends on m and k; neither depends on the amplitude',
      why='The clearest difference is the <b>mass</b>: it is absent from the pendulum and present in the '
          'spring. The second is <b>gravity</b>: a pendulum clock runs slow on a mountain and would run '
          'very slow on the Moon, while a spring-driven watch keeps the same time everywhere.')

d.grp('Part E — Weekly assessment, Group B')
d.sol(19, 'two pendulums of 0.25 m and 1.00 m',
      '    T ∝ √ L\n'
      '    T₁ / T₂ = √( 0.25 / 1.00 ) = √0.25 = 0.5\n'
      '    T₁ : T₂ = 1 : 2        that is  1/2',
      'B) 1 / 2',
      why='The lengths are in the ratio 1 : 4, so the periodic times are in the ratio 1 : 2 — the '
          'square root always shrinks the ratio.')
d.sol(20, 'doubling the hung mass',
      '    T ∝ √ m        →        T(new) = √2 × T(old)',
      'C) it increases by a factor of &radic;2')
d.sol(21, 'the condition, and the effect of a larger small amplitude',
      'the condition :  the angle of swing must be <b>small</b> ( about 10° or less ),\n'
      'so that  sin θ ≈ θ  and the restoring force becomes proportional to x.\n'
      'the effect :  T = 2π √(L/g) contains no amplitude, so within this range\n'
      'increasing the small amplitude leaves the periodic time practically unchanged.',
      'a small angle of swing; and increasing the small amplitude does not change T appreciably',
      why='Strictly the periodic time does creep up as the angle grows — by roughly 0.2 % at 10&deg; '
          'and about 2 % at 30&deg; — because sin&theta; falls behind &theta;. That is precisely why '
          'the condition is written as &ldquo;small angle&rdquo;, and why pendulum clocks are built to '
          'swing through only a few degrees.')
d.sol(22, 'the 0.20 kg body on an 80 N/m horizontal spring',
      '    T = 2π √( m / k )\n'
      '    T = 6.28 × √( 0.20 / 80 ) = 6.28 × √0.0025\n'
      '    T = 6.28 × 0.05\n'
      '    T = 0.314 s',
      'T = 0.314 s')
d.sol(23, 'moving the pendulum to a place of smaller g',
      '    T = 2π √( L / g )        →        T ∝ 1 / √ g\n'
      'g is in the <b>denominator</b>, so a smaller g gives a <b>larger</b> T :\n'
      'the pendulum swings more slowly and a pendulum clock would lose time.',
      'the periodic time increases, because T is inversely proportional to &radic;g',
      why='On the Moon g is about 1.6 m/s&sup2;, roughly one sixth of its value here, so &radic;g is about '
          '2.5 times smaller and the same pendulum would take about 2.5 times as long for each swing.')

d.grp('Part E — Weekly assessment, Group C')
d.sol(24, 'four times the spring constant',
      '    T = 2π √( m / k )        →        T ∝ 1 / √ k\n'
      '    T(new) = T / √4 = T / 2',
      'C) T / 2',
      why='A stiffer spring pulls back harder for the same displacement, so the body is turned round '
          'sooner and the vibration is quicker.')
d.sol(25, 'the change that does not matter',
      '    T = 2π √( L / g )\n'
      'L appears, g appears — and a different place on the Earth changes g slightly.\n'
      'the mass of the bob appears nowhere in the formula.',
      'C) changing the mass of the bob')
d.sol(26, 'why the static extension does not enter T',
      'at the new equilibrium position :        k e = m g\n'
      'measuring x from that position, the resultant force is :\n'
      '    F = m g − k ( e + x ) = − k x\n'
      'the terms mg and ke cancel, so e has disappeared from the equation of motion,\n'
      'and  T = 2π √( m / k )  contains no e.',
      'because mg and ke cancel at the equilibrium position, leaving F = &minus;kx with no e in it',
      why='The static extension tells you <b>where</b> the body hangs at rest; the spring constant tells '
          'you <b>how quickly</b> it comes back. Only the second of those sets the timing. Notice, though, '
          'that e is a handy way of <b>measuring</b> k in the laboratory: k = mg/e.')
d.sol(27, 'the periodic time for L = 0.90 m',
      '    T = 2π √( L / g )\n'
      '    T = 6.28 × √( 0.90 / 9.8 ) = 6.28 × √0.0918\n'
      '    T = 6.28 × 0.3030\n'
      '    T = 1.9031 ≈ 1.90 s',
      'T = 1.90 s')
d.sol(28, 'what to change in order to double T',
      'simple pendulum :\n'
      '    T ∝ √ L      →      2 T needs  √( L′ / L ) = 2      →      L′ = 4 L\n\n'
      'spring pendulum ( k fixed ) :\n'
      '    T ∝ √ m      →      2 T needs  √( m′ / m ) = 2      →      m′ = 4 m',
      'make the length of the pendulum four times as large; make the mass on the spring four times as large',
      why='Both answers are &ldquo;four times&rdquo; for the same reason — the quantity you are '
          'changing sits under a square root, so you must multiply it by the <b>square</b> of the factor '
          'you want in T.')

d.foot('Lessons 2&ndash;2 and 2&ndash;3 &middot; The Vertical Spring and the Simple Pendulum &middot; '
       'Mr. Gemy',
       'T = 2&pi;&radic;(m/k) &nbsp;&middot;&nbsp; T = 2&pi;&radic;(L/g)')
d.save('l22.html')
print('l22.html written -', d.n, 'questions')

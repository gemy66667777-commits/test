# -*- coding: utf-8 -*-
import figs_l25 as F
from docbase import Doc

d = Doc('Unit 2 &middot; Lesson 2&ndash;5', 'Interference of Waves<br>and Standing Waves',
        'Coherent sources, path difference, constructive and destructive interference, nodes and '
        'antinodes &mdash; with the end-of-part review.',
        ['Grade 11 &middot; Egyptian Baccalaureate', '40 questions', 'Step-by-step solutions',
         '&Delta; = m&lambda; or ( m + &frac12; )&lambda;'],
        'Interference of Waves and Standing Waves')

d.kit('The toolkit for this lesson', [
    ('&Delta; = | S&#8322;P &minus; S&#8321;P |', 'the path difference'),
    ('&Delta; = m &lambda;', 'constructive &mdash; an <b>even</b> number of &lambda;/2'),
    ('&Delta; = ( m + &frac12; ) &lambda;', 'destructive &mdash; an <b>odd</b> number of &lambda;/2'),
    ('A(res) = A&#8321; + A&#8322; &nbsp;or&nbsp; | A&#8321; &minus; A&#8322; |',
     'the resultant amplitude'),
    ('node &harr; antinode', 'spaced &lambda;/4 apart'),
    ('N&ndash;N = A&ndash;A = &lambda; / 2', 'in a standing wave'),
])
d.hint('<b>Count half-wavelengths, not wavelengths.</b> Divide the path difference by &lambda;/2. An '
       '<b>even</b> answer means the two waves arrive in step &rarr; constructive. An <b>odd</b> answer '
       'means they arrive exactly out of step &rarr; destructive. And if the two <b>sources</b> themselves '
       'are in antiphase, the whole rule turns over.')

# ---------------- A ----------------
d.sec('A', 'Classwork &nbsp;1', 'Path difference and the type of interference')
d.q('Two coherent sources, vibrating in phase, emit waves of wavelength 4.0 cm. At a point P, the path '
    'length from the first source is 10.0 cm and from the second source is 16.0 cm.', 'Problem',
    F.path_difference('Figure 1'),
    parts=['<b>a)</b> Calculate the path difference.',
           '<b>b)</b> Determine the number of half-wavelengths it contains, and state whether the '
           'interference at P is constructive or destructive.'])
d.q('Two coherent sources S&#8321; and S&#8322;, a distance of 8.0 cm apart, vibrate in phase and emit '
    'waves of wavelength 2.0 cm. <b>Determine the number of destructive interference lines lying between '
    'S&#8321; and S&#8322;.</b>', 'Problem', F.nodal_lines('Figure 2'))

# ---------------- B ----------------
d.sec('B', 'Home assignment &nbsp;1', 'The principle of superposition')
d.q('Two coherent sources vibrating in phase emit waves of wavelength &lambda;. Constructive interference '
    'occurs at the points at which the path difference is equal to:', 'MCQ',
    ch=['( m + &frac12; ) &lambda;', 'm &times; &lambda;', '( 2m + 1 ) &lambda; / 2', '&lambda; / 4'])
d.q('The principle of superposition states that the resultant displacement at a point where two waves '
    'interfere is equal to:', 'MCQ', F.superposition('Figure 3'),
    ch=['the product of their two displacements',
        'the vector sum of their two individual displacements',
        'the difference between their two frequencies',
        'the average of their two amplitudes'])
d.q('Two coherent sources vibrating in phase produce waves of wavelength 5.0 cm and amplitude 1.0 cm. At a '
    'point P, S&#8321;P = 30.0 cm and S&#8322;P = 37.5 cm. <b>Calculate the resultant amplitude at the '
    'point P</b> when:', 'Problem',
    parts=['<b>a)</b> the two sources vibrate in phase.',
           '<b>b)</b> the two sources vibrate in antiphase (opposite phases).'])
d.q('Two waves of wavelength 6.0 cm and amplitude 0.40 cm are emitted in phase from the two sources '
    'S&#8321; and S&#8322;. For a point P at which S&#8321;P = 20.0 cm and S&#8322;P = 35.0 cm, '
    '<b>calculate:</b>', 'Problem',
    parts=['<b>a)</b> the path difference.', '<b>b)</b> the resultant amplitude at P.'])
d.q('The opposite figure shows two waves spreading out in phase from the two sources S&#8321; and '
    'S&#8322;. <b>What is the result of the superposition of the two waves at the two points P and Q?</b> '
    'Justify your answer.', 'Explain', F.two_sources('Figure 4'))

# ---------------- C ----------------
d.sec('C', 'Classwork &nbsp;2', 'Counting the half-wavelengths')
d.q('Two coherent sources emit waves of wavelength 6.0 cm and amplitude 0.50 cm. At a point P, '
    'S&#8321;P = 28.0 cm and S&#8322;P = 37.0 cm. <b>Determine the path difference and the number of '
    'half-wavelengths that it contains.</b>', 'Problem')
d.q('Two coherent sources vibrating in phase are separated by a distance of 10 cm and emit waves of '
    'wavelength 2.5 cm. At a point P the path difference is 5.0 cm. <b>Determine whether P is a point of '
    'constructive or destructive interference, and state the number of half-wavelengths.</b>', 'Problem')

# ---------------- D ----------------
d.sec('D', 'Home assignment &nbsp;2', 'Nodes and the reversed rule')
d.q('Two coherent sources vibrate in phase with a wavelength of 4.0 cm. If the path difference to a point '
    'P equals 6.0 cm, then the path difference contains:', 'MCQ',
    ch=['1.5 wavelengths', '2.0 wavelengths', '1.0 wavelength', '0.5 wavelength'])
d.q('The node in a standing wave is defined as a point of:', 'MCQ', F.standing_wave('Figure 5'),
    ch=['maximum displacement', 'a displacement equal to zero', 'maximum amplitude and energy',
        'a changing frequency'])
d.q('Two coherent sources vibrating in phase emit waves of amplitude 0.40 cm and wavelength 3.0 cm. At a '
    'point Q the path difference is 9.0 cm. <b>Calculate the resultant amplitude at Q.</b>', 'Problem')
d.q('Two coherent sources vibrate in <b>antiphase</b> (opposite phases) with waves of wavelength 4.0 cm. '
    'At a point R the path difference is 8.0 cm. <b>Determine whether the point R undergoes constructive '
    'or destructive interference.</b>', 'Problem')

# ---------------- E ----------------
d.sec('E', 'Standing waves', 'Inside a pipe')
d.q('The opposite figure shows a standing wave formed inside a pipe that is open at one end. '
    '<b>Explain the nature of the vibration of the air particles near the point X.</b>', 'Explain',
    F.pipe_standing('Figure 6'))

# ---------------- F ----------------
d.page()
d.sec('F', 'Review', 'Choose the correct answer')
d.q('What happens to the speed of a transverse wave pulse travelling along a stretched string if the '
    'tension force in the string is increased?', 'MCQ',
    ch=['it decreases', 'it increases', 'it stays without change', 'it becomes zero'])
d.q('Increasing the amplitude of a wave while its frequency stays constant leads to:', 'MCQ',
    ch=['an increase in the speed of the wave',
        'an increase in the energy transported by the wave',
        'a decrease in the wavelength', 'an increase in the periodic time of the wave'])
d.q('Electromagnetic waves can travel through vacuum, while mechanical waves cannot, because:', 'MCQ',
    ch=['electromagnetic waves have an infinite wavelength',
        'electromagnetic waves do not require material media',
        'electromagnetic waves are longitudinal waves',
        'electromagnetic waves travel more slowly than mechanical waves'])
d.q('During an earthquake, the primary seismic waves (P-waves) reach the observation station before the '
    'secondary waves (S-waves) because:', 'MCQ',
    ch=['P-waves are transverse and travel with a greater speed',
        'P-waves are longitudinal and travel with a greater speed than S-waves',
        'S-waves travel through liquids only',
        'S-waves carry more energy than P-waves'])
d.q('Which of the following pairs contains transverse waves only?', 'MCQ',
    ch=['sound waves and light waves',
        'light waves and waves along a stretched string',
        'waves along a stretched string and sound waves',
        'water surface waves and sound waves'])
d.q('The correct relation connecting the speed of a wave (v), the frequency (f) and the wavelength '
    '(&lambda;) is:', 'MCQ',
    ch=['v = f / &lambda;', 'v = f &times; &lambda;', 'v = &lambda; / f',
        'v = 1 / ( f &times; &lambda; )'])
d.q('Destructive interference occurs when two interfering waves arrive at a point with a phase difference '
    'of:', 'MCQ',
    ch=['0 &nbsp;(in phase)', '180&deg; &nbsp;(out of phase / in antiphase)', '360&deg;', '90&deg;'])
d.q('In an experiment on the interference of two waves, the formation of regions in which the resultant '
    'displacement is as large as possible is due to:', 'MCQ',
    ch=['destructive interference', 'constructive interference', 'refraction of the waves',
        'reflection of the waves'])
d.q('A standing wave is formed as a result of the interference of two travelling waves that are '
    'characterised by:', 'MCQ',
    ch=['different frequencies, travelling in the same direction',
        'the same frequency and amplitude, travelling in two opposite directions',
        'different amplitudes, travelling in two opposite directions',
        'the same wavelength, travelling in two perpendicular directions'])
d.q('The distance between two successive nodes (or two successive antinodes) in a standing wave equals:',
    'MCQ',
    ch=['a complete wavelength', 'half a wavelength', 'a quarter of a wavelength', 'two wavelengths'])
d.q('If two coherent sources vibrating in phase produce waves of amplitude A, then the maximum resultant '
    'amplitude at a point of constructive interference is:', 'MCQ', ch=['A', '0', '2A', '4A'])
d.q('What happens to the separation between the adjacent nodal lines in a ripple tank experiment when the '
    'frequency of vibration of the two sources is increased?', 'MCQ',
    ch=['it increases', 'it decreases', 'it stays without change', 'it becomes zero everywhere'])

# ---------------- G ----------------
d.sec('G', 'Review', 'Answer the following questions')
d.q('What happens to the speed of a wave pulse travelling along a stretched rope when the tension force in '
    'the rope is increased?', 'Explain')
d.q('What happens to the energy transported from a vibrating source producing a wave motion when the '
    'amplitude of the wave is doubled, its frequency staying constant?', 'Explain')
d.q('What happens to the periodic time of a simple harmonic oscillator if its frequency is doubled?',
    'Explain')
d.q('What happens to the speed of a sound wave when it passes from a material medium into a perfect '
    'vacuum?', 'Explain')
d.q('What happens to the speed of the observed wave if the frequency of the wave source is doubled while '
    'the properties of the medium stay as they are, without change?', 'Explain')
d.q('What happens to the amplitude of a particle in a medium as a wave passes through it, as regards the '
    '<b>total displacement</b> of the particle after the wave has passed and the medium has settled?',
    'Explain')
d.q('What happens to the pitch (sharpness / frequency) of the musical note given out by a plucked string '
    'when the tension force in the string is increased?', 'Explain')
d.q('What happens to the amplitude of vibration at a node on a stretched string on which a standing wave '
    'is formed?', 'Explain')
d.q('What happens to the positions of constructive and destructive interference if the state of two '
    'coherent sources, which were vibrating in phase, is changed so that they vibrate in antiphase (a '
    'phase difference of 180&deg;)?', 'Explain')
d.q('A tuning fork produces a wave of frequency 250 Hz which travels with a speed of 340 m/s in air. '
    '<b>Find the wavelength and the periodic time of the sound wave.</b>', 'Problem')
d.q('A wave source produces 120 complete waves in 30 seconds along a stretched spring. If the distance '
    'between two successive crests is 0.5 m, <b>find:</b>', 'Problem',
    parts=['<b>a)</b> the frequency.', '<b>b)</b> the periodic time.'])
d.q('A wave source produces 100 complete waves in 20 seconds along a stretched spring. If the distance '
    'between two successive crests is 0.4 m, <b>calculate the speed of the wave.</b>', 'Problem')
d.q('Two loudspeakers separated by a distance of 2.0 m emit coherent sound waves, in phase, of wavelength '
    '0.50 m. A listener stands at a place at which the path difference is 1.25 m. <b>Determine whether the '
    'listener hears a loud sound (constructive interference) or a faint sound (destructive '
    'interference).</b>', 'Problem')
d.q('Two coherent sources vibrating in phase emit waves of wavelength 5.0 cm. At a point P the path '
    'difference is 12.5 cm. <b>Determine whether P is a point of constructive or destructive interference, '
    'and justify your answer.</b>', 'Problem')

# ---------------- solutions ----------------
d.page()
d.sec('✓', 'Answer key', 'Solutions — step by step')
d.hint('<b>The same three lines solve almost every problem here.</b> (1) Find the path difference '
       '&Delta;. (2) Divide by &lambda;/2 to count the half-wavelengths. (3) Even &rarr; constructive, '
       'odd &rarr; destructive — then reverse the verdict if the two sources are in antiphase.')

d.grp('Part A — Classwork 1')
d.sol(1, 'path difference for λ = 4.0 cm',
      'a)  Δ = S₂P − S₁P\n'
      '    Δ = 16.0 − 10.0\n'
      '    Δ = 6.0 cm\n\n'
      'b)  λ / 2 = 4.0 / 2 = 2.0 cm\n'
      '    number of half-wavelengths = 6.0 / 2.0 = 3        ( an <b>odd</b> number )\n'
      '    equivalently  Δ = 1.5 λ = ( 1 + ½ ) λ    →  <b>destructive</b>',
      'a) &Delta; = 6.0 cm &nbsp;&nbsp; b) 3 half-wavelengths &rarr; destructive interference',
      why='Three half-wavelengths means the two waves arrive exactly out of step: a crest of one meets a '
          'trough of the other, and if the amplitudes are equal the point stays permanently still.')
d.sol(2, 'the destructive lines between two sources 8.0 cm apart',
      'a destructive line needs an <b>odd</b> number of half-wavelengths :\n'
      '    λ / 2 = 2.0 / 2 = 1.0 cm\n'
      '    Δ = 1.0 , 3.0 , 5.0 , 7.0 cm        ( odd multiples of 1.0 cm )\n'
      'between the two sources the path difference can only run from 0 up to d = 8.0 cm,\n'
      'so Δ = 9.0 cm and beyond is impossible. that gives 4 values on one side of the\n'
      'centre line, and 4 mirror values on the other side :\n'
      '    total = 4 + 4 = 8 destructive lines',
      '8 destructive (nodal) lines',
      why='A quick formula for in-phase sources: the number of nodal lines is '
          '2 &times; the whole-number part of ( d/&lambda; + &frac12; ) = 2 &times; int( 4 + 0.5 ) = 8. '
          'Note that the central line, where &Delta; = 0, is always a <b>constructive</b> line, never a '
          'nodal one.')

d.grp('Part B — Home assignment 1')
d.sol(3, 'the condition for constructive interference',
      'the two waves must arrive in step, so the extra path must hold a <b>whole</b>\n'
      'number of wavelengths :\n'
      '    Δ = m λ        ( m = 0 , 1 , 2 , 3 ... )',
      'B) m &times; &lambda;',
      why='Choices (A) and (C) are the same thing written two ways, and both are the condition for '
          '<b>destructive</b> interference, not constructive.')
d.sol(4, 'the principle of superposition',
      'where two waves meet, the displacement of the medium at each instant is the\n'
      '<b>algebraic (vector) sum</b> of the two displacements the waves would produce\n'
      'separately — taking the signs into account.',
      'B) the vector sum of their two individual displacements',
      why='Two equal crests give 2A; a crest meeting an equal trough gives A &minus; A = 0. That single '
          'rule of signs is the whole of interference.')
d.sol(5, 'the resultant amplitude at P for λ = 5.0 cm',
      '    Δ = 37.5 − 30.0 = 7.5 cm\n'
      '    Δ / λ = 7.5 / 5.0 = 1.5        →  Δ = ( 1 + ½ ) λ\n'
      '    number of half-wavelengths = 7.5 / 2.5 = 3      ( odd )\n\n'
      'a)  sources in phase   →  destructive\n'
      '    A(res) = | A₁ − A₂ | = | 1.0 − 1.0 | = 0\n\n'
      'b)  sources in antiphase →  the verdict is reversed → constructive\n'
      '    A(res) = A₁ + A₂ = 1.0 + 1.0 = 2.0 cm',
      'a) A = 0 &nbsp;&nbsp; b) A = 2.0 cm',
      why='Part (b) is the whole point of the question. Putting the sources in antiphase adds an extra '
          'half-wavelength of its own to the journey, so every point that was quiet becomes loud and '
          'every point that was loud becomes quiet — the whole pattern simply swaps over.')
d.sol(6, 'path difference and amplitude for λ = 6.0 cm',
      'a)  Δ = 35.0 − 20.0\n'
      '    Δ = 15.0 cm\n\n'
      'b)  λ / 2 = 3.0 cm\n'
      '    number of half-wavelengths = 15.0 / 3.0 = 5        ( odd )\n'
      '    → destructive , and the amplitudes are equal :\n'
      '    A(res) = 0.40 − 0.40 = 0',
      'a) &Delta; = 15.0 cm &nbsp;&nbsp; b) A(res) = 0 &nbsp;(destructive)',
      why='Check it the other way as well: 15.0 / 6.0 = 2.5 wavelengths, and any “point five” '
          'answer is always destructive for in-phase sources.')
d.sol(7, 'the superposition at P and at Q',
      'read the figure :\n'
      '    at P  a crest of S₁ falls on a crest of S₂   ( P lies on the centre line,\n'
      '          so the two paths are equal and Δ = 0 )\n'
      '    at Q  a crest of one source falls on a trough of the other',
      'P is a point of constructive interference; Q is a point of destructive interference',
      why='<b>At P.</b> Two solid (crest) circles cross there, so the two waves arrive in step and the '
          'displacements add: the water rises to 2A and then falls to &minus;2A. P lies on the '
          'perpendicular bisector of S&#8321;S&#8322;, where &Delta; = 0 &mdash; the central bright line '
          'of every interference pattern.<br><br>'
          '<b>At Q.</b> A solid circle of one source crosses a dashed (trough) circle of the other, so '
          'the path difference is an odd number of half-wavelengths. The crest of one wave is cancelled '
          'by the trough of the other, and if the amplitudes are equal the point Q stays permanently at '
          'rest.')

d.grp('Part C — Classwork 2')
d.sol(8, 'path difference and half-wavelengths for λ = 6.0 cm',
      '    Δ = 37.0 − 28.0 = 9.0 cm\n'
      '    λ / 2 = 3.0 cm\n'
      '    number of half-wavelengths = 9.0 / 3.0 = 3        ( odd → destructive )',
      '&Delta; = 9.0 cm , containing 3 half-wavelengths &rarr; destructive interference',
      why='The amplitude 0.50 cm was not needed here — but if it were asked for, equal amplitudes '
          'and destructive interference would give a resultant of zero.')
d.sol(9, 'constructive or destructive for λ = 2.5 cm',
      '    λ / 2 = 1.25 cm\n'
      '    number of half-wavelengths = 5.0 / 1.25 = 4        ( <b>even</b> )\n'
      'or, more directly :\n'
      '    Δ / λ = 5.0 / 2.5 = 2        ( a whole number of wavelengths )',
      'P is a point of constructive interference, containing 4 half-wavelengths',
      why='The separation of 10 cm is not needed for the verdict; it only limits how far out the pattern '
          'can extend.')

d.grp('Part D — Home assignment 2')
d.sol(10, 'how many wavelengths are in 6.0 cm',
      '    Δ / λ = 6.0 / 4.0 = 1.5',
      'A) 1.5 wavelengths',
      why='And 1.5 wavelengths is ( 1 + &frac12; )&lambda;, so this point is a destructive one — a '
          'useful thing to notice even though the question only asked for the number.')
d.sol(11, 'the definition of a node',
      'a standing wave is the interference of two identical waves travelling in opposite\n'
      'directions. at a <b>node</b> the two always arrive out of step, so they cancel :\n'
      '    the displacement stays zero at all times',
      'B) a point of a displacement equal to zero',
      why='The opposite point is the <b>antinode</b>, where the two waves always arrive in step and the '
          'displacement swings between +2A and &minus;2A. A node and the next antinode are &lambda;/4 '
          'apart.')
d.sol(12, 'the resultant amplitude at Q for λ = 3.0 cm',
      '    Δ / λ = 9.0 / 3.0 = 3        ( a whole number → constructive )\n'
      '    A(res) = A₁ + A₂ = 0.40 + 0.40\n'
      '    A(res) = 0.80 cm',
      'A(res) = 0.80 cm',
      why='Counting half-wavelengths gives the same verdict: 9.0 / 1.5 = 6, an even number.')
d.sol(13, 'antiphase sources with Δ = 8.0 cm',
      '    Δ / λ = 8.0 / 4.0 = 2        ( a whole number of wavelengths )\n'
      'for sources <b>in phase</b> that would be constructive.\n'
      'but the sources here are in <b>antiphase</b>, which adds an extra half a wave\n'
      'to the difference, so the verdict is turned over :\n'
      '    R is a point of <b>destructive</b> interference',
      'R undergoes destructive interference',
      why='A neat way to keep it straight: total difference = path difference + source phase difference. '
          'Here 2&lambda; from the path plus &lambda;/2 from the sources gives 2.5&lambda; — an odd '
          'number of half-wavelengths, so destructive.')

d.grp('Part E — Standing waves')
d.sol(14, 'the air particles near the point X',
      'X lies where the two envelope curves cross, so X is a <b>node</b> :\n'
      '    the two waves travelling in opposite directions always arrive there out of\n'
      '    step, and their displacements cancel at every instant.',
      'X is a node: the air particles there stay practically at rest, with zero displacement amplitude '
      '&mdash; while the pressure variation there is at its maximum',
      why='<b>Displacement and pressure are out of step.</b> At a displacement node the air layers on '
          'either side move towards X together and then away from X together, so the air at X itself '
          'never moves along the tube — but it is alternately squeezed and stretched, which makes '
          'the node a point of <b>maximum pressure variation</b>. The opposite holds at an antinode: the '
          'air there swings backwards and forwards with the greatest amplitude, while the pressure hardly '
          'changes. In a pipe closed at one end the closed end is always a displacement node and the open '
          'end is always an antinode.')

d.grp('Part F — Review, choose the correct answer')
d.sol(15, 'tension and the speed of a pulse',
      'for a stretched string :      v = √( F / μ )\n'
      'a larger tension F gives a larger v ( v ∝ √F ).',
      'B) it increases')
d.sol(16, 'a larger amplitude at constant frequency',
      'the energy carried by a wave is proportional to the <b>square</b> of the amplitude :\n'
      '    E ∝ A²\n'
      'the speed and the wavelength are set by the medium and the frequency, not by A.',
      'B) an increase in the energy transported by the wave')
d.sol(17, 'why electromagnetic waves cross a vacuum',
      'a mechanical wave is a disturbance passed from particle to particle, so it needs\n'
      'a material medium. an electromagnetic wave is an oscillating electric and magnetic\n'
      'field, which needs no medium at all.',
      'B) electromagnetic waves do not require material media')
d.sol(18, 'why P-waves arrive first',
      'P-waves are <b>longitudinal</b> ( compressions and rarefactions ) and travel faster\n'
      'than the <b>transverse</b> S-waves through the rocks of the Earth.',
      'B) P-waves are longitudinal and travel with a greater speed than S-waves',
      why='It is the delay between the two arrivals that lets a seismologist work out how far away the '
          'earthquake was.')
d.sol(19, 'which pair is transverse only',
      'light  → transverse ( electromagnetic )\n'
      'a wave on a stretched string → transverse\n'
      'sound  → <b>longitudinal</b>, so any pair containing sound is ruled out.',
      'B) light waves and waves along a stretched string')
d.sol(20, 'the wave equation',
      '    v = f × λ',
      'B) v = f &times; &lambda;')
d.sol(21, 'the phase difference for destructive interference',
      'the two waves must arrive exactly out of step : crest against trough.\n'
      'that is half a cycle, which is a phase difference of 180° ( π radians ).',
      'B) 180&deg; ( out of phase / in antiphase )')
d.sol(22, 'regions of the largest resultant displacement',
      'the displacements add instead of cancelling, which is <b>constructive</b> interference.',
      'B) constructive interference')
d.sol(23, 'how a standing wave is formed',
      'two waves of the <b>same frequency and the same amplitude</b> travelling in\n'
      '<b>opposite</b> directions along the same line interfere and produce a pattern\n'
      'of fixed nodes and antinodes that does not travel.',
      'B) the same frequency and amplitude, travelling in two opposite directions')
d.sol(24, 'the distance between two successive nodes',
      'in a standing wave :\n'
      '    node to node   =  λ / 2\n'
      '    antinode to antinode = λ / 2\n'
      '    node to the next antinode = λ / 4',
      'B) half a wavelength')
d.sol(25, 'the maximum resultant amplitude',
      'at a constructive point the two displacements add :\n'
      '    A(res) = A + A = 2A',
      'C) 2A',
      why='And at a destructive point with equal amplitudes the result is A &minus; A = 0, which is why '
          'choice (B) is there.')
d.sol(26, 'raising the frequency in a ripple tank',
      'the speed is fixed by the water, so :\n'
      '    f increases   →   λ = v / f decreases\n'
      'the spacing of the nodal lines is proportional to λ, so it becomes smaller.',
      'B) it decreases',
      why='This is exactly why a higher-pitched sound gives a finer interference pattern, and why blue '
          'light gives narrower fringes than red light in Young’s experiment.')

d.grp('Part G — Review, answer the following')
d.sol(27, 'tension and the speed of a pulse on a rope',
      '    v = √( F / μ )        →        v ∝ √F',
      'the speed increases &mdash; in proportion to the square root of the tension',
      why='Four times the tension gives only twice the speed.')
d.sol(28, 'doubling the amplitude',
      '    E ∝ A²\n'
      '    A → 2A        gives        E → ( 2 )² E = 4 E',
      'the energy transported becomes four times as large',
      why='This is why a sound twice as “loud” in amplitude carries four times the energy.')
d.sol(29, 'doubling the frequency of an oscillator',
      '    T = 1 / f\n'
      '    f → 2f        gives        T → T / 2',
      'the periodic time is halved')
d.sol(30, 'sound entering a perfect vacuum',
      'sound is a <b>mechanical</b> wave : it needs particles of matter to pass the\n'
      'disturbance along. a perfect vacuum has none, so the wave cannot propagate\n'
      'at all and simply stops at the boundary.',
      'the wave does not travel at all &mdash; its speed in vacuum is zero, because sound needs a '
      'material medium',
      why='This is the classic bell-in-a-vacuum-jar demonstration: as the air is pumped out the bell is '
          'seen to be ringing but is no longer heard.')
d.sol(31, 'doubling the source frequency in the same medium',
      'the speed of a wave is fixed by the <b>medium</b>, not by the source :\n'
      '    v stays the same\n'
      'what changes is the wavelength :\n'
      '    λ = v / f        →        f → 2f  gives  λ → λ / 2',
      'the speed stays without change; it is the wavelength that halves',
      why='A common mistake is to think a “faster vibration” makes a faster wave. It does not '
          '— it makes a <b>shorter</b> one.')
d.sol(32, 'the particle after the wave has passed',
      'each particle of the medium only vibrates about its own fixed position; it is\n'
      'not carried along. when the wave has gone by and the medium settles :\n'
      '    the amplitude falls back to zero , and the total displacement = zero',
      'the particle returns to its original position &mdash; its total displacement is zero',
      why='The wave transports <b>energy</b> across the medium, never matter. A floating cork bobs and '
          'then rests exactly where it started.')
d.sol(33, 'tightening a plucked string',
      '    v = √( F / μ )    increases\n'
      '    f = v / ( 2 L )      increases as well ( L unchanged )',
      'the pitch rises &mdash; the note becomes sharper',
      why='It is precisely what a guitarist does when tuning: tightening the peg raises the pitch, '
          'loosening it lowers the pitch.')
d.sol(34, 'the amplitude at a node',
      'at a node the two waves always arrive out of step and cancel exactly :\n'
      '    amplitude = 0  at all times',
      'the amplitude of vibration at a node is zero &mdash; the point stays permanently at rest')
d.sol(35, 'turning the sources into antiphase',
      'changing the sources to antiphase adds an extra half a wavelength to every\n'
      'journey, so every condition is turned over :\n'
      '    points that were constructive become destructive\n'
      '    points that were destructive become constructive',
      'the two sets of positions swap over completely &mdash; the whole pattern is inverted',
      why='The <b>spacing</b> of the lines does not change, because &lambda; and the separation of the '
          'sources are untouched; only the labels on them are exchanged. In particular the centre line, '
          'which used to be the brightest, becomes a nodal line.')
d.sol(36, 'a 250 Hz tuning fork',
      '    v = f λ        →        λ = v / f\n'
      '    λ = 340 / 250 = 1.36 m\n\n'
      '    T = 1 / f = 1 / 250\n'
      '    T = 0.004 s = 4 × 10⁻³ s',
      '&lambda; = 1.36 m , T = 4 &times; 10&#8315;&sup3; s')
d.sol(37, '120 waves in 30 s',
      'a)  f = number of waves / time\n'
      '    f = 120 / 30\n'
      '    f = 4 Hz\n\n'
      'b)  T = 1 / f = 1 / 4\n'
      '    T = 0.25 s',
      'a) f = 4 Hz &nbsp;&nbsp; b) T = 0.25 s',
      why='The 0.5 m between successive crests is the wavelength; it is not needed for either part here, '
          'but it would give v = f&lambda; = 4 &times; 0.5 = 2.0 m/s.')
d.sol(38, '100 waves in 20 s with λ = 0.4 m',
      '    f = 100 / 20 = 5 Hz\n'
      '    v = f λ = 5 × 0.4\n'
      '    v = 2.0 m/s',
      'v = 2.0 m/s')
d.sol(39, 'the listener between two loudspeakers',
      '    Δ / λ = 1.25 / 0.50 = 2.5\n'
      '    Δ = ( 2 + ½ ) λ        ( an odd number of half-wavelengths : 5 )\n'
      '→ the two sounds arrive exactly out of step and cancel',
      'the listener hears a faint sound &mdash; destructive interference',
      why='Walking a little to one side would bring the listener to a place where &Delta; is a whole '
          'number of wavelengths, and the sound would become loud again. This is why the loud and quiet '
          'patches in a hall move as you walk about.')
d.sol(40, 'P with Δ = 12.5 cm and λ = 5.0 cm',
      '    Δ / λ = 12.5 / 5.0 = 2.5\n'
      'or, counting half-wavelengths :\n'
      '    λ / 2 = 2.5 cm    and    12.5 / 2.5 = 5        ( an <b>odd</b> number )',
      'P is a point of destructive interference, because the path difference contains 5 half-wavelengths '
      '( &Delta; = 2.5&lambda; )',
      why='For sources vibrating in phase, any path difference ending in “.5 of a '
          'wavelength” is destructive, and any whole number of wavelengths is constructive.')

d.foot('Lesson 2&ndash;5 &middot; Interference of Waves and Standing Waves &middot; Mr. Gemy',
       '&Delta; = m&lambda; &rarr; constructive &nbsp;&middot;&nbsp; '
       '&Delta; = (m+&frac12;)&lambda; &rarr; destructive')
d.save('l25.html')
print('l25.html written -', d.n, 'questions')

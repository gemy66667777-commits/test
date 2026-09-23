# -*- coding: utf-8 -*-
import figs_l24 as F
from docbase import Doc

d = Doc('Unit 2 &middot; Lesson 2&ndash;4', 'Sinusoidal Waves',
        'Wavelength, periodic time, frequency and the wave equation v = f&lambda;, for transverse and '
        'longitudinal waves.',
        ['Grade 11 &middot; Egyptian Baccalaureate', '14 questions', 'Step-by-step solutions',
         'v = f &lambda;'], 'Sinusoidal Waves')

d.kit('The toolkit for this lesson', [
    ('v = f &lambda;', 'the wave equation'),
    ('v = &lambda; / T', 'the same thing, written with T'),
    ('f = 1 / T', 'frequency and periodic time'),
    ('y &ndash; x graph', 'gives the amplitude A and the wavelength &lambda;'),
    ('y &ndash; t graph', 'gives the amplitude A and the periodic time T'),
    ('transverse / longitudinal', 'particles &perp; / &parallel; to the travel direction'),
])
d.hint('<b>A wave carries energy, not matter.</b> Every particle of the medium simply vibrates about its '
       'own fixed position; nothing travels along with the wave except the disturbance and the energy it '
       'carries. And one equation, v = f&lambda;, answers almost every numerical question in this lesson '
       '&mdash; the only skill is deciding which two of the three quantities you have been given.')

# ---------------- A ----------------
d.sec('A', 'Classwork &nbsp;1', 'Frequency, wavelength and speed')
d.q('A vibrating body completes one full oscillation in a periodic time of 0.20 s. <b>Find its '
    'frequency.</b>', 'Problem', F.wave_on_rope('Figure 1'))
d.q('A sinusoidal wave has a wavelength of 0.2 m and a frequency of 0.3 Hz. <b>Calculate the speed with '
    'which the wave travels.</b>', 'Problem')

# ---------------- B ----------------
d.sec('B', 'Home assignment &nbsp;1', 'What a wave carries')
d.q('Which of the following is transported by a mechanical wave as it travels through the medium?', 'MCQ',
    ch=['matter', 'energy', 'the particles of the medium', 'the total displacement'])
d.q('A wave has a periodic time equal to 0.25 second. What is its frequency?', 'MCQ',
    ch=['0.25 hertz', '2.5 hertz', '4.0 hertz', '0.4 hertz'])
d.q('A wave travels along a string; its periodic time is 0.10 s and its wavelength is 1.5 m. '
    '<b>Calculate the speed of the wave.</b>', 'Problem')
d.q('A wave pulse travels along a rope with a speed of 4.0 m/s and a wavelength of 0.80 m. <b>Find its '
    'frequency and its periodic time.</b>', 'Problem')
d.q('The opposite figure shows the vibration of the particles of a material medium for a longitudinal wave '
    'motion. <b>Using the scale shown in the figure, calculate the wavelength of the longitudinal '
    'wave.</b>', 'Problem', F.longitudinal_dots('Figure 2'))

# ---------------- C ----------------
d.sec('C', 'Classwork &nbsp;2', 'Using the wave equation')
d.q('A sinusoidal wave has a wavelength of 0.60 m, and its periodic time equals 0.20 s. <b>Calculate:</b>',
    'Problem',
    parts=['<b>a)</b> the frequency', '<b>b)</b> the speed of the wave'])
d.q('A wave source vibrates with a periodic time of 0.25 s, and produces a wave whose wavelength is 1.2 m. '
    '<b>Calculate the speed of the wave.</b>', 'Problem')

# ---------------- D ----------------
d.sec('D', 'Home assignment &nbsp;2', 'Reading the two graphs')
d.q('Which of the graphs is used to determine <b>both</b> the amplitude and the wavelength of a wave '
    'motion made by a vibrating body, directly?', 'MCQ', F.yx_graph('Figure 3', '&lambda;', 'A'),
    ch=['the displacement &ndash; time graph ( y &ndash; t )',
        'the displacement &ndash; position graph ( y &ndash; x )',
        'the velocity &ndash; time graph', 'the frequency &ndash; periodic time graph'])
d.q('In a longitudinal wave, the particles of the medium vibrate:', 'MCQ',
    F.transverse_longitudinal('Figure 4'),
    ch=['perpendicular to the direction of propagation of the wave',
        'in a direction parallel to the direction of propagation of the wave',
        'in circular paths opposite to the direction of transfer of the energy',
        'with a constant speed equal to the speed of light'])
d.q('A sound wave travels through air with a speed of 340 m/s and a frequency of 500 Hz. <b>Calculate its '
    'wavelength.</b>', 'Problem')
d.q('The displacement &ndash; position graph of a sinusoidal wave shows a wavelength of 3.0 m and an '
    'amplitude of 0.50 m, while the displacement &ndash; time graph shows a periodic time of 0.60 s. '
    '<b>Find the speed of the wave.</b>', 'Problem',
    d.row(F.yx_graph('Figure 5', '&lambda; = 3.0 m', 'A = 0.50 m', maxw=330),
          F.yt_graph('Figure 6', 'T = 0.60 s', maxw=330)))
d.q('The opposite figure represents a sinusoidal wave motion. If the distance between the two points P and '
    'Q is 2 m, covered in a time interval of 0.1 s, <b>calculate:</b>', 'Problem',
    F.pq_quarter('Figure 7'),
    parts=['<b>a)</b> the wavelength', '<b>b)</b> the speed of propagation of the wave'])

# ---------------- solutions ----------------
d.page()
d.sec('✓', 'Answer key', 'Solutions — step by step')
d.hint('<b>One equation, three faces.</b> v = f&lambda; , f = 1/T and v = &lambda;/T are the same statement '
       'written three ways. Read the question, write down which two quantities you were handed, and the '
       'third one follows in a single line.')

d.grp('Part A — Classwork 1')
d.sol(1, 'the frequency for a periodic time of 0.20 s',
      '    f = 1 / T\n'
      '    f = 1 / 0.20\n'
      '    f = 5 Hz',
      'f = 5 Hz',
      why='The frequency is simply how many complete oscillations happen each second. One oscillation every '
          'fifth of a second means five of them every second.')
d.sol(2, 'the speed of a wave with λ = 0.2 m and f = 0.3 Hz',
      '    v = f λ\n'
      '    v = 0.3 × 0.2\n'
      '    v = 0.06 m/s',
      'v = 0.06 m/s',
      why='Each second the source sends out 0.3 of a wavelength, and each wavelength is 0.2 m long, so the '
          'front of the wave advances 0.06 m in that second. That is what v = f&lambda; is saying.')

d.grp('Part B — Home assignment 1')
d.sol(3, 'what a mechanical wave transports',
      'each particle of the medium vibrates about its own fixed position and stays there.\n'
      'what moves forward is the disturbance, and with it the <b>energy</b> of the vibration.',
      'B) energy',
      why='A cork floating on a ripple bobs up and down, it does not travel across the pond. The matter '
          'stays put; only the energy is passed on from one particle to the next.')
d.sol(4, 'the frequency for T = 0.25 s',
      '    f = 1 / T = 1 / 0.25 = 4.0 Hz',
      'C) 4.0 hertz')
d.sol(5, 'a wave on a string, T = 0.10 s and λ = 1.5 m',
      '    v = λ / T\n'
      '    v = 1.5 / 0.10\n'
      '    v = 15 m/s',
      'v = 15 m/s',
      why='You could also find f = 1/0.10 = 10 Hz first, then v = f&lambda; = 10 &times; 1.5 = 15 m/s. The '
          'two routes are the same equation.')
d.sol(6, 'a pulse of v = 4.0 m/s and λ = 0.80 m',
      '    v = f λ        →        f = v / λ\n'
      '    f = 4.0 / 0.80 = 5 Hz\n\n'
      '    T = 1 / f = 1 / 5\n'
      '    T = 0.20 s',
      'f = 5 Hz , T = 0.20 s')
d.sol(7, 'the wavelength of the longitudinal wave from the figure',
      'in a longitudinal wave the wavelength is the distance between the centres of two\n'
      '<b>successive compressions</b> ( or two successive rarefactions ).\n'
      'from the figure, the two compression centres are 8 large squares apart :\n'
      '    λ = 8 × 1.0 cm\n'
      '    λ = 8.0 cm = 0.080 m',
      '&lambda; = 8.0 cm = 0.080 m',
      why='<b>Note on the printed figure.</b> The figure in the book is drawn on a squared grid but no '
          'numerical scale is printed beside it, so the question cannot be answered from the book as it '
          'stands. The figure has been redrawn here with the scale stated explicitly (one large square = '
          '1.0 cm). The physics is unchanged: find two successive compressions, count the squares between '
          'their centres, and multiply by the scale. Measuring between a compression and the '
          '<b>next rarefaction</b> would give only half a wavelength — that is the usual mistake.')

d.grp('Part C — Classwork 2')
d.sol(8, 'λ = 0.60 m and T = 0.20 s',
      'a)  f = 1 / T\n'
      '    f = 1 / 0.20 = 5 Hz\n\n'
      'b)  v = f λ\n'
      '    v = 5 × 0.60\n'
      '    v = 3.0 m/s',
      'a) f = 5 Hz &nbsp;&nbsp; b) v = 3.0 m/s',
      why='Check it the short way: v = &lambda;/T = 0.60/0.20 = 3.0 m/s, the same answer without finding f '
          'at all.')
d.sol(9, 'a source of T = 0.25 s producing λ = 1.2 m',
      '    v = λ / T\n'
      '    v = 1.2 / 0.25\n'
      '    v = 4.8 m/s',
      'v = 4.8 m/s',
      why='Notice that the source decides the <b>frequency</b> and the medium decides the <b>speed</b>; '
          'the wavelength is then whatever v/f happens to be.')

d.grp('Part D — Home assignment 2')
d.sol(10, 'which graph gives A and λ',
      'the y – x graph is a <b>snapshot</b> of the whole medium at one instant, so :\n'
      '    the height of a crest above the axis  →  the amplitude A\n'
      '    the distance between two crests       →  the wavelength λ\n'
      'the y – t graph follows one single particle, so it gives A and T , not λ.',
      'B) the displacement &ndash; position graph ( y &ndash; x )',
      why='The two graphs look identical, and that is exactly the trap. Always read the <b>horizontal '
          'axis</b> first: if it is a distance, the repeat length is &lambda;; if it is a time, the repeat '
          'length is T.')
d.sol(11, 'the vibration of the particles in a longitudinal wave',
      'longitudinal  →  each particle vibrates <b>along</b> the same line on which the\n'
      'wave travels, producing compressions and rarefactions ( sound is the example ).\n'
      'transverse    →  each particle vibrates <b>across</b> that line ( a rope, light ).',
      'B) in a direction parallel to the direction of propagation of the wave')
d.sol(12, 'the wavelength of a 500 Hz sound wave',
      '    v = f λ        →        λ = v / f\n'
      '    λ = 340 / 500\n'
      '    λ = 0.68 m',
      '&lambda; = 0.68 m',
      why='This is about the length of your forearm — and it is why a 500 Hz sound bends easily round '
          'a doorway, while light, with a wavelength a million times smaller, does not.')
d.sol(13, 'reading the speed from the two graphs',
      'the y – x graph gives      λ = 3.0 m      ( and A = 0.50 m )\n'
      'the y – t graph gives      T = 0.60 s\n'
      '    v = λ / T\n'
      '    v = 3.0 / 0.60\n'
      '    v = 5.0 m/s',
      'v = 5.0 m/s',
      why='The amplitude 0.50 m is not needed for the speed — it is there to see whether you know '
          'that the amplitude never enters v = f&lambda;.')
d.sol(14, 'P and Q a quarter of a cycle apart',
      'from the figure, P is at the equilibrium level and Q is at the next crest, so PQ\n'
      'is a <b>quarter</b> of a complete wave :\n\n'
      'a)  λ / 4 = 2 m\n'
      '    λ = 4 × 2 = 8 m\n\n'
      'b)  T / 4 = 0.1 s        →        T = 0.4 s\n'
      '    v = λ / T = 8 / 0.4\n'
      '    v = 20 m/s',
      'a) &lambda; = 8 m &nbsp;&nbsp; b) v = 20 m/s',
      why='The quarter-cycle is the whole question. From the equilibrium level to the next crest is a '
          'quarter of a wave, from crest to the next crest is a whole wave, and from crest to trough is '
          'half a wave. Get that right and both parts follow at once. As a check, f = 1/0.4 = 2.5 Hz and '
          'v = f&lambda; = 2.5 &times; 8 = 20 m/s.')

d.foot('Lesson 2&ndash;4 &middot; Sinusoidal Waves &middot; Mr. Gemy',
       'v = f&lambda; &nbsp;&middot;&nbsp; f = 1/T')
d.save('l24.html')
print('l24.html written -', d.n, 'questions')

# -*- coding: utf-8 -*-
import figs_l27 as F
from figs_l26 import wave_boundary
from docbase import Doc

d = Doc('Unit 2 &middot; Lesson 2&ndash;7', 'Interference of Sound<br>and the Doppler Effect',
        'Loud and quiet places in a room, Quincke&rsquo;s tube and noise cancelling &mdash; and why a '
        'siren changes its pitch as it passes you.',
        ['Grade 11 &middot; Egyptian Baccalaureate', '28 questions', 'Step-by-step solutions',
         '&lambda; = 4X &nbsp;&middot;&nbsp; v = f&lambda;'],
        'Interference of Sound and the Doppler Effect')

d.kit('The toolkit for this lesson', [
    ('&Delta;d = m&lambda;', 'loud &mdash; constructive'),
    ('&Delta;d = ( m + &frac12; )&lambda;', 'quiet &mdash; destructive'),
    ('Quincke : &lambda; = 4X', 'pulling the slide by X adds 2X to the path'),
    ('approaching', '&lambda; shorter &rarr; f apparent is <b>higher</b>'),
    ('receding', '&lambda; longer &rarr; f apparent is <b>lower</b>'),
    ('v of sound', 'set by the air, never by the motion of the source'),
])
d.hint('<b>Doppler changes what arrives, not what is sent.</b> The horn keeps sounding at the same '
       'frequency and the sound keeps travelling through the air at the same speed. What the motion does '
       'is squeeze the crests together in front of the source and stretch them out behind it &mdash; so '
       'only the <b>wavelength that reaches the listener</b>, and therefore the pitch they hear, is '
       'changed.')

# ---------------- A ----------------
d.sec('A', 'Classwork &nbsp;2', 'Loud and quiet places')
d.q('When you walk slowly across a wide courtyard while a continuous note is being played from two '
    'sources, what do you notice about the intensity of the sound you receive?', 'MCQ',
    F.two_speakers_court('Figure 1'),
    ch=['hearing the same sound with the same intensity everywhere in the courtyard',
        'a gradual and continuous decrease in the intensity the further you move from the source',
        'a repeated pattern of rising and falling sound intensity',
        'a complete cutting off of the sound as soon as you move a few steps away from the source'])
d.q('<b>Compare</b> between constructive interference and destructive interference for sound waves coming '
    'from two coherent sources vibrating in the same phase, as regards:', 'Explain',
    parts=['<b>a)</b> the intensity of the sound.', '<b>b)</b> the path difference.'])

# ---------------- B ----------------
d.sec('B', 'Home assignment &nbsp;2', 'Where the sound disappears')
d.q('<b>Explain the following:</b> when designing national theatres and large concert halls, sound '
    'engineers noticed that there are certain points among the seats at which the intensity of the music '
    'is very faint and muffled, in spite of the presence of large, highly efficient loudspeakers on both '
    'sides of the stage.', 'Explain')
d.q('The figure shows an instrument used in physical measurements.', 'Explain', F.quincke('Figure 2'),
    parts=['<b>a)</b> What is the name of the instrument?', '<b>b)</b> What is its function?',
           '<b>c)</b> What is the scientific principle on which the idea of its operation is based?',
           '<b>d)</b> Explain briefly the way in which the instrument works.'])
d.q('A student carries out an experiment in the physics laboratory to verify the phenomenon of the '
    'interference of sound waves, using loudspeakers and sensitive microphones. The students switched on '
    'one loudspeaker and moved the microphone slowly across the courtyard, then repeated the experiment '
    'with the two loudspeakers switched on together and sounding the same note. Which of the following '
    'correctly represents the change in the sound intensity measured by the microphone as it is moved '
    'across the courtyard in the two cases?', 'MCQ',
    ch=['with one loudspeaker the intensity is exactly uniform, and with the two loudspeakers the '
        'intensity increases to several times its value, steadily, everywhere',
        'with one loudspeaker the intensity decreases gradually with distance, and with the two '
        'loudspeakers a repeated pattern of rise and fall in the intensity appears',
        'with one loudspeaker the sound is cut off completely, and with the two loudspeakers the sound '
        'becomes loud at one single point and faint everywhere else in the courtyard',
        'with one loudspeaker or with two, the level of the sound stays constant and does not change at '
        'any point'])
d.q('Destructive interference occurs between the waves coming from two coherent sources vibrating in the '
    'same phase when the path difference (&Delta;d) between them equals &hellip;&hellip;', 'MCQ',
    ch=['&lambda;', '1.5 &lambda;', '2 &lambda;', '3 &lambda;'])
d.q('Two coherent sound sources vibrate in the same phase; the wavelength of the waves emitted by each of '
    'them is 2 m. Constructive interference occurs between the waves coming from them when the path '
    'difference (&Delta;d) between them equals &hellip;&hellip;', 'MCQ',
    ch=['1 m', '2 m', '3 m', '5 m'])

# ---------------- C ----------------
d.page()
d.sec('C', 'Weekly assessment', 'Group A')
d.q('A light ray travels from material (X), whose refractive index is n&#8321; = 1.33, into material (Y), '
    'whose refractive index is n&#8322; = 1.5. Given that the speed of light in (X) is v&#8321; and in '
    '(Y) is v&#8322;, and that the wavelength in (X) is &lambda;&#8321; and in (Y) is &lambda;&#8322;, '
    'which of the following relations correctly expresses the behaviour of the light at this passage?',
    'MCQ',
    ch=['v&#8321; &gt; v&#8322; , &lambda;&#8321; &gt; &lambda;&#8322;',
        'v&#8321; &lt; v&#8322; , &lambda;&#8321; &lt; &lambda;&#8322;',
        'v&#8321; &gt; v&#8322; , &lambda;&#8321; &lt; &lambda;&#8322;',
        'v&#8322; = v&#8321; , &lambda;&#8321; &gt; &lambda;&#8322;'])
d.q('Constructive interference occurs between the waves coming from two coherent sources vibrating in the '
    'same phase when the path difference (&Delta;d) between them equals &hellip;&hellip;', 'MCQ',
    ch=['0.5 &lambda;', '&lambda;', '1.5 &lambda;', '2.5 &lambda;'])
d.q('<b>What happens</b> to the speed of sea waves, to their wavelength and to their direction of '
    'propagation, when they pass at an oblique angle from deep water into shallow water near the shore? '
    'Give the scientific explanation of each of them.', 'Explain')
d.q('The figure shows Quincke&rsquo;s tube. The sound entering at P is split into two paths and is '
    'recombined at Q. When the tube B is pushed fully in, the two paths are equal in length. As the tube B '
    'is slowly pulled out, the first minimum in the sound intensity occurs when the tube is pulled out by '
    'an amount X = 10 cm. Taking the speed of sound as 330 m/s, <b>calculate:</b>', 'Problem',
    F.quincke('Figure 3', 'X = 10 cm'),
    parts=['<b>a)</b> the wavelength of the sound, in metres.',
           '<b>b)</b> the frequency of the sound, in hertz.'])
d.q('<b>Explain:</b> why are the positions of <b>minimum</b> intensity of a wave, rather than the '
    'positions of maximum intensity, the strongest evidence that sound is a wave?', 'Explain')

# ---------------- D ----------------
d.sec('D', 'Weekly assessment', 'Group B')
d.q('Ultrasound waves are used in medical examinations to follow the foetus and the internal organs. When '
    'an ultrasound wave passes from a soft tissue (such as muscle) into another tissue of higher density '
    '(such as bone), part of the wave is reflected and the other part is refracted inside the bone. Which '
    'of the following physical changes takes place in the refracted part of the wave as it enters the '
    'bone?', 'MCQ',
    ch=['its frequency increases and its speed increases, while its wavelength decreases',
        'its frequency stays constant, and its speed and its wavelength increase',
        'its frequency and its speed decrease, while its wavelength increases',
        'its speed and its wavelength stay constant, while its frequency increases'])
d.q('Two coherent sound sources vibrate in the same phase; the wavelength of the waves emitted by each of '
    'them is 4 m. Destructive interference occurs between the waves coming from them when the path '
    'difference (&Delta;d) between them equals &hellip;&hellip;', 'MCQ',
    ch=['2 m', '4 m', '8 m', '12 m'])
d.q('The figure shows Quincke&rsquo;s tube. The sound entering at P is split into two paths and is '
    'recombined at Q. When the tube B is pushed fully in, the two paths are equal in length. As the tube B '
    'is slowly pulled out, the first minimum in the sound intensity occurs when the tube is pulled out by '
    'an amount X = 12 cm, the frequency of the sound being 1000 Hz. <b>Calculate:</b>', 'Problem',
    F.quincke('Figure 4', 'X = 12 cm'),
    parts=['<b>a)</b> the wavelength of the sound, in metres.',
           '<b>b)</b> the speed of the sound, in metres per second.'])
d.q('<b>Explain briefly</b> the way in which noise-cancelling headphones work.', 'Explain',
    F.noise_cancel('Figure 5'))
d.q('A wave crosses a boundary separating two media as shown in the figure. <b>Calculate the ratio</b> '
    'between the wavelength of the wave in medium 1 and the wavelength of the wave in medium 2.',
    'Problem', wave_boundary('Figure 6'))

# ---------------- E ----------------
d.sec('E', 'Weekly assessment', 'Group C')
d.q('A light wave of frequency 6 &times; 10&sup1;&#8308; Hz travels in the first medium with a speed of '
    '3 &times; 10&#8312; m/s. On being refracted and passing into the second medium its speed becomes '
    '2 &times; 10&#8312; m/s. Which of the following statements is <b>not</b> correct?', 'MCQ',
    ch=['the frequency of the wave in the second medium = 6 &times; 10&sup1;&#8308; Hz',
        'the wavelength of the wave in the first medium = 1.5 &times; its wavelength in the second medium',
        'the refractive index of the first medium = 1.5 &times; the refractive index of the second medium',
        'the sine of the angle of incidence in the first medium = 1.5 &times; the sine of the angle of '
        'refraction in the second medium'])
d.q('Constructive interference occurs between the waves coming from two coherent sources vibrating in the '
    'same phase when the path difference (&Delta;d) between them equals &hellip;&hellip;', 'MCQ',
    ch=['an odd number of quarter wavelengths', 'an even number of quarter wavelengths',
        'an odd number of half wavelengths', 'an even number of half wavelengths'])
d.q('The figure shows Quincke&rsquo;s tube. The sound entering at P is split into two paths and is '
    'recombined at Q. When the tube B is pushed fully in, the two paths are equal in length. As the tube B '
    'is slowly pulled out, the first minimum in the sound intensity occurs when the tube is pulled out by '
    'an amount X. Given that the frequency of the sound is 1200 Hz and the speed of sound is 360 m/s, '
    '<b>calculate:</b>', 'Problem', F.quincke('Figure 7'),
    parts=['<b>a)</b> the wavelength of the sound, in metres.',
           '<b>b)</b> the magnitude of the distance X, in metres.'])
d.q('<b>Explain:</b> why do noise-cancelling headphones reduce the steady hum of an engine much more '
    'effectively than a sudden sound such as the slamming of a door?', 'Explain')
d.q('A wave crosses a boundary separating two media as shown in the figure. <b>Calculate:</b>', 'Problem',
    wave_boundary('Figure 8'),
    parts=['<b>a)</b> the ratio between the frequency of the wave in medium 1 and its frequency in '
           'medium 2.',
           '<b>b)</b> the ratio between the wavelength of the wave in medium 1 and its wavelength in '
           'medium 2.'])

# ---------------- F ----------------
d.page()
d.sec('F', 'The Doppler effect &middot; Classwork &nbsp;1', 'A moving source of sound')
d.q('The figure shows a student carrying a phone that gives out a note of constant frequency f, moving '
    'towards / away from another, stationary student (the listener). Using the figure and what you have '
    'studied about the properties of waves, <b>explain the changes that take place in the pitch of the '
    'note</b> during the approach and during the recession, as recorded by the listener.', 'Explain',
    F.doppler_source('Figure 9'))
d.q('The student carrying the phone moved with a greater speed (a faster walk), about 4 m/s instead of '
    '2 m/s, towards the stationary student. Which of the following changes takes place in the properties '
    'of the sound wave as recorded by the stationary student (the listener), compared with the first '
    'case?', 'MCQ',
    ch=['the apparent frequency decreases and the sound becomes sharper',
        'the apparent frequency increases and the sound becomes even sharper',
        'the apparent frequency stays constant and only the speed of sound increases',
        'the apparent frequency decreases and the sound becomes deeper'])

# ---------------- G ----------------
d.sec('G', 'The Doppler effect &middot; Home assignment &nbsp;1', 'Approaching, passing, receding')
d.q('While a student carrying a phone that gives out a note of constant frequency moves with a speed '
    'towards a stationary student, which of the following changes takes place in the apparent wavelength '
    '(&lambda;) of the sound waves in front of the phone, as received by the stationary student?', 'MCQ',
    ch=['the wavelength increases because the speed of the source increases',
        'the wavelength decreases because the waves are given out closer together in front of the moving '
        'source',
        'the wavelength stays constant because the original frequency of the phone is constant',
        'the wavelength is doubled because the speed of sound in air increases'])
d.q('When a car sounding a horn of constant frequency f approaches, with a uniform speed, a person '
    'standing at the side of the road, then passes him and moves away from him: how does the apparent '
    'frequency of the sound ( f&rsquo; ) that the person notices at the instant the car passes exactly in '
    'front of him change, compared with the instant of its approach and the instant of its recession?',
    'MCQ',
    ch=['the frequency is as high as possible during the approach, equals the original frequency f at the '
        'instant of passing, and falls below f during the recession',
        'the frequency is as low as possible during the approach, equals the original frequency f at the '
        'instant of passing, and increases during the recession',
        'the frequency stays higher than the original frequency f continuously, at every instant',
        'the frequency stays equal to the original frequency f throughout the motion of the car'])
d.q('A police car sounding a siren of constant frequency f moves steadily, with a uniform speed v, '
    'towards a vertical mountain wall. What does the driver of the car notice as regards (the frequency of '
    'the direct sound coming from the car) and (the frequency of the sound reflected from the mountain, '
    'which he hears after its reflection)?', 'MCQ', F.car_wall('Figure 10'),
    ch=['the direct frequency equals f, and the reflected frequency falls below f',
        'the direct frequency rises above f, and the reflected frequency equals f',
        'the direct frequency equals f, and the reflected frequency rises above f',
        'the direct frequency falls below f, and the reflected frequency falls below f'])
d.q('A girl stands at the side of the road listening to the siren of a speeding ambulance. She noticed '
    'that the note of the sound was very sharp while the car was approaching her, but as soon as the car '
    'passed in front of her and moved away, she noticed that the note of the sound suddenly became deep.',
    'Explain',
    parts=['<b>a)</b> How does the physics of relative motion explain this sudden change in the pitch of '
           'the sound at the instant the car passes the listener?',
           '<b>b)</b> What change takes place in the speed of propagation of the sound in air during this '
           'whole process? Explain your answer.'])

# ---------------- solutions ----------------
_HD = ['', 'constructive interference', 'destructive interference']
_RW = [['the sound heard', 'loud &mdash; maximum intensity', 'faint or silent &mdash; minimum intensity'],
       ['the path difference &Delta;d', 'm&lambda; &nbsp;( a whole number of &lambda; )',
        '( m + &frac12; )&lambda; &nbsp;( an odd number of &lambda;/2 )'],
       ['the two waves arrive', 'in step &mdash; crest on crest', 'out of step &mdash; crest on trough'],
       ['the resultant amplitude', 'A&#8321; + A&#8322;', '| A&#8321; &minus; A&#8322; |']]
_TBL = ('<table class="vt"><tr>' + ''.join('<th>' + hh + '</th>' for hh in _HD) + '</tr>' +
        ''.join('<tr>' + ''.join('<td>' + c + '</td>' for c in r) + '</tr>' for r in _RW) + '</table>')

d.page()
d.sec('✓', 'Answer key', 'Solutions — step by step')
d.hint('<b>Two rules carry the whole lesson.</b> For interference, divide the path difference by '
       '&lambda;/2: an even answer is loud, an odd answer is quiet. For Doppler, ask one question only '
       '— is the gap between source and listener <b>closing</b> or <b>opening</b>? Closing means a '
       'higher pitch, opening means a lower one.')

d.grp('Part A — Classwork 2')
d.sol(1, 'walking across the courtyard',
      'the two sources are coherent and in phase, so at each point the path difference\n'
      'decides what is heard :\n'
      '    Δd = mλ              →  the two waves arrive in step   →  loud\n'
      '    Δd = ( m + ½ )λ      →  they arrive out of step       →  quiet\n'
      'as you walk, Δd changes steadily, so loud and quiet places alternate.',
      'C) a repeated pattern of rising and falling sound intensity',
      why='This is the single most convincing classroom demonstration that sound is a <b>wave</b>: two '
          'loudspeakers, both switched on, can produce places that are <b>quieter</b> than one '
          'loudspeaker alone. Nothing made of particles could do that.')
d.sol(2, 'constructive compared with destructive',
      'both depend on the same quantity — the path difference Δd — and on nothing\n'
      'else, as long as the two sources are coherent and vibrate in the same phase.',
      'a) loud for constructive, faint for destructive &nbsp;&nbsp; b) &Delta;d = m&lambda; for '
      'constructive, ( m + &frac12; )&lambda; for destructive',
      extra=_TBL,
      why='Note that energy is not destroyed at the quiet places. It is simply redistributed: whatever is '
          'missing at the quiet points turns up at the loud points, so the total energy in the room is '
          'exactly what the two loudspeakers put into it.')

d.grp('Part B — Home assignment 2')
d.sol(3, 'the dead seats in a concert hall',
      'the two loudspeakers are fed by the same amplifier, so they are <b>coherent</b> and\n'
      'in phase. a seat at which the distances from the two loudspeakers differ by\n'
      '    Δd = ( m + ½ ) λ\n'
      'receives the two waves exactly out of step, and they cancel each other.',
      'because those seats lie on lines of destructive interference between the two loudspeakers',
      why='The effect is worst for low notes, whose wavelengths are metres long, so the quiet patches are '
          'large enough to swallow a whole seat. Concert halls are designed with this in mind — '
          'delaying one channel slightly, or scattering the sound from the walls, breaks the coherence '
          'and washes the dead spots out.')
d.sol(4, "Quincke's tube",
      'the sound entering at P is split into two paths — the fixed arm A and the sliding\n'
      'arm B — and the two parts meet again at Q.\n'
      'pulling B out by a distance X lengthens that path by <b>2X</b> ( out and back ),\n'
      'so the path difference becomes  Δd = 2X , and :\n'
      '    first minimum :   2X = λ / 2        →        λ = 4 X',
      'a) Quincke&rsquo;s tube &nbsp; b) it measures the wavelength (and hence the speed or the '
      'frequency) of sound &nbsp; c) the interference of sound waves &nbsp; d) see the note below',
      why='<b>d) How it works.</b> A single source of sound is sent in at P. The tube splits it into two '
          'parts that travel along the two arms and are brought together again at a detector (or the '
          'ear) at Q. Because both parts come from the same source they are perfectly coherent. Sliding '
          'B out changes the length of one path only, so the path difference &Delta;d = 2X can be dialled '
          'to any value. The listener hears the sound rise and fall; at the <b>first</b> minimum '
          '2X = &lambda;/2, so &lambda; = 4X, and successive minima come every further half wavelength, '
          'that is every extra &lambda;/4 of pull. Knowing &lambda; and either f or v gives the other '
          'from v = f&lambda;.')
d.sol(5, 'one loudspeaker compared with two',
      'one loudspeaker  → no second wave to interfere with, so the intensity simply\n'
      '                   falls off steadily as the microphone moves further away.\n'
      'two loudspeakers → the path difference changes as the microphone moves, giving\n'
      '                   alternate maxima and minima.',
      'B) with one loudspeaker the intensity decreases gradually with distance, and with two a repeated '
      'pattern of rise and fall appears',
      why='The first half of the statement matters as much as the second: it rules out any explanation '
          'based on the room alone, because the pattern only appears when the <b>second</b> source is '
          'switched on.')
d.sol(6, 'the path difference for destructive interference',
      'destructive needs an <b>odd</b> number of half-wavelengths :\n'
      '    Δd = 0.5λ , 1.5λ , 2.5λ , ...\n'
      'of the four choices, only 1.5λ is of this form ( λ , 2λ and 3λ are whole\n'
      'numbers of wavelengths, which give constructive interference ).',
      'B) 1.5 &lambda;')
d.sol(7, 'constructive interference with λ = 2 m',
      'constructive needs a whole number of wavelengths :\n'
      '    Δd = m λ = m × 2 = 2 , 4 , 6 , ... m\n'
      'of the four choices only 2 m is a whole multiple of 2 m.',
      'B) 2 m',
      why='Check the others: 1 m and 3 m are odd multiples of &lambda;/2 = 1 m, so they are destructive; '
          '5 m is 2.5&lambda;, also destructive.')

d.grp('Part C — Weekly assessment, Group A')
d.sol(8, 'light from n = 1.33 into n = 1.5',
      '    n = c / v        →        a larger n means a smaller v\n'
      '    n₁ = 1.33 < n₂ = 1.5        →        v₁ > v₂\n'
      'the frequency does not change, so  λ = v / f  follows the speed :\n'
      '    λ₁ > λ₂',
      'A) v&#8321; &gt; v&#8322; and &lambda;&#8321; &gt; &lambda;&#8322;',
      why='Speed and wavelength always move <b>together</b>; the frequency never moves at all. Any choice '
          'in which v and &lambda; go opposite ways, such as (C), can be rejected at a glance.')
d.sol(9, 'the path difference for constructive interference',
      'constructive needs a whole number of wavelengths :  Δd = m λ\n'
      '0.5λ , 1.5λ and 2.5λ are all odd numbers of half-wavelengths → destructive.',
      'B) &lambda;')
d.sol(10, 'sea waves entering shallow water',
      'the speed of a water wave depends on the <b>depth</b> :\n'
      '    depth decreases   →   v decreases\n'
      'the frequency is fixed by the source far out at sea :\n'
      '    f unchanged        →   λ = v / f decreases\n'
      'and the end of each crest that reaches the shallow water first slows down\n'
      'while the other end is still moving faster, so the crest is turned round.',
      'v decreases, &lambda; decreases, f is unchanged, and the direction bends until the crests are '
      'almost parallel to the shore',
      why='This is refraction. The three facts hang together in one chain: the depth sets the speed, the '
          'source sets the frequency, and v = f&lambda; then fixes the wavelength. The bending is just '
          'the sideways consequence of one end of the crest being slower than the other.')
d.sol(11, 'Quincke: X = 10 cm and v = 330 m/s',
      'a)  pulling the slide out by X lengthens that path by 2X, so at the first minimum :\n'
      '        2 X = λ / 2        →        λ = 4 X\n'
      '        λ = 4 × 0.10\n'
      '        λ = 0.40 m\n\n'
      'b)  v = f λ        →        f = v / λ\n'
      '        f = 330 / 0.40\n'
      '        f = 825 Hz',
      'a) &lambda; = 0.40 m &nbsp;&nbsp; b) f = 825 Hz',
      why='Take care with the factor of <b>4</b>. The commonest mistake is to write &lambda; = 2X, '
          'forgetting either that the sound travels the extension twice, or that the <b>first</b> minimum '
          'needs only half a wavelength of path difference.')
d.sol(12, 'why the quiet points are the stronger evidence',
      'a loud point could be explained without any wave idea at all — two sources simply\n'
      'deliver more energy than one. but a <b>quiet</b> point cannot :\n'
      '    switching on a <b>second</b> source makes the sound <b>disappear</b>.',
      'because two sources producing silence can only be explained by waves cancelling, whereas two '
      'sources producing a loud sound could be explained by simple addition of energy',
      why='If sound were a stream of particles, adding a second stream could only ever make the sound '
          'louder. Cancellation is a property that belongs to waves alone, which is why the minima, not '
          'the maxima, settle the argument.')

d.grp('Part D — Weekly assessment, Group B')
d.sol(13, 'ultrasound entering bone',
      'the frequency is set by the transducer and cannot change at a boundary :\n'
      '    f unchanged\n'
      'sound travels <b>faster</b> in a denser, stiffer material such as bone :\n'
      '    v increases        →        λ = v / f  increases as well',
      'B) its frequency stays constant, and its speed and its wavelength increase',
      why='Be careful: for <b>sound</b>, a stiffer and denser medium such as bone is the <b>faster</b> '
          'one (sound goes at about 1500 m/s in soft tissue and about 3500 m/s in bone). That is the '
          'opposite of the rule for <b>light</b>, where a denser medium is the slower one.')
d.sol(14, 'destructive interference with λ = 4 m',
      '    λ / 2 = 2 m\n'
      'destructive needs an odd number of half-wavelengths :\n'
      '    Δd = 2 , 6 , 10 , ... m\n'
      'of the four choices only 2 m is of this form ( 4, 8 and 12 m are whole numbers\n'
      'of wavelengths → constructive ).',
      'A) 2 m')
d.sol(15, 'Quincke: X = 12 cm and f = 1000 Hz',
      'a)  λ = 4 X = 4 × 0.12\n'
      '        λ = 0.48 m\n\n'
      'b)  v = f λ = 1000 × 0.48\n'
      '        v = 480 m/s',
      'a) &lambda; = 0.48 m &nbsp;&nbsp; b) v = 480 m/s',
      why='<b>Note on the printed data.</b> The answer that follows from the book’s numbers is '
          '480 m/s, but the speed of sound in air at ordinary temperatures is about 340 m/s, so these '
          'figures do not describe sound in air. Treat it as an exercise in the method: the relation '
          '&lambda; = 4X and then v = f&lambda; are what is being tested, and both are applied correctly '
          'here.')
d.sol(16, 'how noise-cancelling headphones work',
      'a small microphone on the outside of the earcup picks up the incoming noise.\n'
      'the electronics invert it — that is, produce a wave of the same amplitude and\n'
      'the same frequency but <b>180° out of phase</b> — and the loudspeaker in the\n'
      'earcup plays it into the ear.\n'
      'by the principle of superposition the two add to ( almost ) zero.',
      'the headphone plays a wave in antiphase with the noise, so the two cancel by superposition',
      why='This is destructive interference put to work. Cancellation can never be perfect, because the '
          'inverted wave has to be produced in the microsecond or two before the noise reaches the '
          'eardrum — which is exactly the point of the next question.')
d.sol(17, 'the wavelength ratio at the boundary',
      'from the figure :   i = 45°  in medium 1 ,   r = 30°  in medium 2\n'
      'the frequency is the same in both media, so λ ∝ v , and :\n'
      '    λ₁ / λ₂ = v₁ / v₂ = sin i / sin r\n'
      '    λ₁ / λ₂ = sin 45° / sin 30° = 0.7071 / 0.5\n'
      '    λ₁ / λ₂ = 1.41   ( = √2 )',
      '&lambda;&#8321; : &lambda;&#8322; = &radic;2 : 1 &asymp; 1.41')

d.grp('Part E — Weekly assessment, Group C')
d.sol(18, 'which statement is not correct',
      '    λ₁ = v₁ / f = 3×10⁸ / 6×10¹⁴ = 5.0 × 10⁻⁷ m\n'
      '    λ₂ = v₂ / f = 2×10⁸ / 6×10¹⁴ = 3.33 × 10⁻⁷ m\n'
      '    n = c / v :   n₁ = 3×10⁸/3×10⁸ = 1 ,   n₂ = 3×10⁸/2×10⁸ = 1.5\n\n'
      '  (A)  f is the same in both media                         ✓ correct\n'
      '  (B)  λ₁ / λ₂ = 5.0 / 3.33 = 1.5                            ✓ correct\n'
      '  (D)  sin i / sin r = v₁ / v₂ = 1.5                         ✓ correct\n'
      '  (C)  n₁ = 1 and n₂ = 1.5 , so n₂ = 1.5 n₁ — the other way round  ✗ wrong',
      'C) &mdash; the refractive index of the first medium is not 1.5 times that of the second; it is the '
      '<b>second</b> that is 1.5 times the first',
      why='The trap is that the ratio 1.5 really does appear three times in this question — for the '
          'wavelengths, for the sines and for the refractive indices — but for the refractive '
          'indices it points the <b>other way</b>, because n is inversely proportional to v.')
d.sol(19, 'constructive interference in words',
      '    Δd = m λ = m × ( 2 × λ/2 ) = 2m × λ/2\n'
      'so a whole number of wavelengths is the same thing as an <b>even</b> number of\n'
      'half-wavelengths.',
      'D) an even number of half wavelengths',
      why='And destructive interference is an <b>odd</b> number of half-wavelengths. Counting in '
          'half-wavelengths is the quickest way to answer every question of this kind.')
d.sol(20, 'Quincke: f = 1200 Hz and v = 360 m/s',
      'a)  v = f λ        →        λ = v / f\n'
      '        λ = 360 / 1200\n'
      '        λ = 0.30 m\n\n'
      'b)  at the first minimum :   2 X = λ / 2        →        X = λ / 4\n'
      '        X = 0.30 / 4\n'
      '        X = 0.075 m = 7.5 cm',
      'a) &lambda; = 0.30 m &nbsp;&nbsp; b) X = 0.075 m = 7.5 cm',
      why='This is question 11 run backwards: there &lambda; = 4X gave the wavelength from the pull, here '
          'X = &lambda;/4 gives the pull from the wavelength.')
d.sol(21, 'a steady hum compared with a sudden bang',
      'the headphone has to <b>measure</b> the incoming sound and then produce its exact\n'
      'mirror image before the sound reaches the eardrum.\n'
      'a steady hum repeats itself thousands of times a second, so the next cycle is\n'
      'completely predictable and can be cancelled accurately.\n'
      'a door slam is a single short pulse with no repeat and a very wide range of\n'
      'frequencies — by the time the electronics have analysed it, it has already gone.',
      'because a steady hum is repetitive and therefore predictable, while a sudden bang is over before '
      'the headphone can produce the cancelling wave',
      why='It is also a matter of wavelength. Low, steady hums have long wavelengths, so the small phase '
          'errors caused by the few centimetres between the microphone and the eardrum hardly matter. For '
          'the high frequencies inside a bang, those same few centimetres can be a whole wavelength, and '
          'the “cancelling” wave might even add to the noise.')
d.sol(22, 'the two ratios at the boundary',
      'from the figure :   i = 45°  in medium 1 ,   r = 30°  in medium 2\n\n'
      'a)  the frequency is fixed by the source, and a boundary cannot change it :\n'
      '        f₁ / f₂ = 1\n\n'
      'b)  λ₁ / λ₂ = v₁ / v₂ = sin i / sin r\n'
      '        λ₁ / λ₂ = sin 45° / sin 30° = 0.7071 / 0.5 = 1.41',
      'a) f&#8321; : f&#8322; = 1 : 1 &nbsp;&nbsp; b) &lambda;&#8321; : &lambda;&#8322; &asymp; 1.41')

d.grp('Part F — The Doppler effect, Classwork 1')
d.sol(23, 'the pitch heard as the phone approaches and recedes',
      'the phone keeps giving out the same frequency f, and the sound keeps travelling\n'
      'through the air at the same speed v. what changes is the <b>spacing</b> of the\n'
      'crests that reach the listener :\n'
      '    approaching  → each new crest is sent from a point nearer the listener,\n'
      '                   so the crests are crowded : λ is shorter, f′ = v/λ is higher\n'
      '    receding     → each new crest is sent from a point further away,\n'
      '                   so the crests are stretched : λ is longer, f′ is lower',
      'the listener hears a pitch <b>higher</b> than f while the phone approaches and <b>lower</b> than f '
      'while it recedes',
      why='<b>What does not change.</b> Three things stay exactly as they were: the frequency the phone '
          'produces, the speed of sound in the air, and the number of crests sent out per second. Only '
          'the number of crests <b>arriving</b> per second is altered, because the listener and the '
          'crests are closing on one another. Note also that the change is a step from high to low as the '
          'phone goes past — not a gradual slide.')
d.sol(24, 'doubling the speed of the moving source',
      'the faster the source closes the gap, the more tightly the crests in front of it\n'
      'are crowded together :\n'
      '    λ′ = ( v − v(s) ) / f        →  a larger v(s) gives a smaller λ′\n'
      '    f′ = v / λ′                   →  so f′ is larger still',
      'B) the apparent frequency increases and the sound becomes even sharper',
      why='The pitch was already raised at 2 m/s; walking at 4 m/s simply raises it further. A useful '
          'check on any Doppler answer: the direction of the shift is fixed by whether the gap is '
          'closing or opening, and the <b>size</b> of the shift grows with the speed.')

d.grp('Part G — The Doppler effect, Home assignment 1')
d.sol(25, 'the apparent wavelength in front of the moving source',
      'in the time of one cycle the source sends out one crest and then moves forward\n'
      'a distance v(s) T before sending the next one, so the gap between them is :\n'
      '    λ′ = v T − v(s) T = ( v − v(s) ) / f        <  λ',
      'B) the wavelength decreases, because the waves are given out closer together in front of the '
      'moving source',
      why='Choice (D) contains the standard misconception: the motion of the source has <b>no effect '
          'whatever</b> on the speed of sound in air, which is fixed by the air itself.')
d.sol(26, 'approaching, passing, and receding',
      'while approaching  :  the gap is closing  →  f′ > f   ( highest )\n'
      'at the instant of passing :  the car is moving straight <b>across</b> the line of\n'
      '                   sight, so the distance is momentarily neither growing nor\n'
      '                   shrinking  →  f′ = f\n'
      'while receding     :  the gap is opening  →  f′ < f',
      'A) highest during the approach, equal to f at the instant of passing, and below f while receding',
      why='Only the part of the velocity <b>along the line joining the source to the listener</b> counts. '
          'At the moment of passing, the whole of the car’s velocity is at right angles to that '
          'line, so there is no shift at all — which is why the drop in pitch sounds so sudden.')
d.sol(27, 'the police car and the mountain wall',
      'the <b>direct</b> sound : the driver sits with the siren, so there is no relative\n'
      'motion between them at all  →  he hears the true frequency f.\n\n'
      'the <b>reflected</b> sound : it is shifted <b>twice</b> —\n'
      '    1  the car is approaching the wall, so the wall receives a raised frequency\n'
      '    2  the wall re-emits that raised frequency, and the car is now approaching\n'
      '       those returning crests as well\n'
      '→  the echo comes back at a frequency clearly higher than f.',
      'C) the direct frequency equals f, and the reflected frequency rises above f',
      why='The two shifts combine to give f&rsquo; = f ( v + v(car) ) / ( v &minus; v(car) ). The driver '
          'therefore hears <b>two</b> different pitches at once, the true one from his own siren and a '
          'higher one from the cliff, and the small difference between them produces audible beats '
          '— a practical way of measuring the car’s speed.')
d.sol(28, 'the ambulance siren passing the girl',
      None,
      'a) the component of the velocity along the line of sight reverses at the instant of passing, so '
      'the shift flips from + to &minus; &nbsp;&nbsp; b) the speed of sound in the air does not change '
      'at all',
      why='<b>a)</b> The pitch heard depends on how fast the gap between the siren and the ear is '
          'changing. On the way in, that gap is closing at nearly the full speed of the ambulance, so the '
          'crests pile up and the note is sharp. At the instant the ambulance is level with the girl its '
          'velocity is entirely <b>across</b> the line of sight, so the gap is momentarily not changing '
          'and she hears the true note. A moment later the gap is opening at nearly the full speed, the '
          'crests are stretched out, and the note is deep. Because the ambulance sweeps past in a '
          'fraction of a second, the whole reversal is squeezed into that instant and is heard as a '
          'sudden drop.<br><br>'
          '<b>b)</b> The speed of sound in air is decided by the air alone — essentially by its '
          'temperature — and is about 340 m/s throughout. It is completely unaffected by how fast '
          'the source is moving. The motion changes the <b>wavelength</b> of the sound in the air, and '
          'therefore the frequency that arrives, but never the speed at which it travels.')

d.foot('Lesson 2&ndash;7 &middot; Interference of Sound and the Doppler Effect &middot; Mr. Gemy',
       '&lambda; = 4X &nbsp;&middot;&nbsp; closing gap &rarr; higher pitch')
d.save('l27.html')
print('l27.html written -', d.n, 'questions')

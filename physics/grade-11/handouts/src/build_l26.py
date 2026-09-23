# -*- coding: utf-8 -*-
import figs_l26 as F
from docbase import Doc

d = Doc('Unit 2 &middot; Lesson 2&ndash;6', 'Refraction of Waves',
        'Why a wave changes speed, wavelength and direction on crossing into a new medium &mdash; while '
        'its frequency never changes.',
        ['Grade 11 &middot; Egyptian Baccalaureate', '10 questions', 'Step-by-step solutions',
         'f is the same in both media'], 'Refraction of Waves')

d.kit('The toolkit for this lesson', [
    ('v = f &lambda;', 'and f is set by the <b>source</b>'),
    ('f&#8321; = f&#8322;', 'the frequency never changes on refraction'),
    ('v&#8321;/v&#8322; = &lambda;&#8321;/&lambda;&#8322;', 'so speed and wavelength change together'),
    ('sin i / sin r = v&#8321; / v&#8322;', 'the law of refraction'),
    ('n = c / v', 'a slower medium has a larger n'),
    ('shallow water', 'slower waves, shorter &lambda;, same f'),
])
d.hint('<b>One thing is fixed and everything else follows.</b> The <b>frequency</b> of a refracted wave is '
       'fixed by the source, so it is the same in both media. Since v = f&lambda;, the speed and the '
       'wavelength must therefore change <b>by the same factor</b> &mdash; and it is that change of speed '
       'that bends the direction of travel.')

# ---------------- A ----------------
d.sec('A', 'Classwork &nbsp;1', 'Sea waves approaching the shore')
d.q('The figure shows the change in the shape, the direction, the behaviour and the properties of sea '
    'waves as they travel from deep water into shallow water near the shore. Using the figure and what you '
    'have studied about the properties of waves:', 'Explain', F.shore_refraction('Figure 1'),
    parts=['<b>a)</b> Explain the changes that take place in each of: the speed of the waves, their '
           'wavelength, and their direction of propagation, as they pass from deep water into shallow '
           'water.',
           '<b>b)</b> Explain the reason for the bending of the waves and the adjustment of their '
           'direction so that they become parallel to the shore line near the beach.',
           '<b>c)</b> Deduce the physical concept that this phenomenon describes, and state its definition '
           'in your own words.'])
d.q('Which of the following changes take place in sea waves as they pass from deep water into shallow '
    'water near the shore?', 'MCQ',
    ch=['their speed increases, their wavelength increases, and they continue in a straight line without '
        'any bending',
        'their speed decreases, their wavelength decreases, and their direction bends so that they become '
        'parallel to the shore line',
        'their speed stays constant, their wavelength decreases, and they bend away completely from the '
        'shore line',
        'their speed decreases, their wavelength increases, and they are completely reflected back towards '
        'the deep water'])

# ---------------- B ----------------
d.sec('B', 'Home assignment &nbsp;1', 'Refraction in general')
d.q('The figure shows the refraction of sea waves at different coastal shapes. Given that the depth of the '
    'water at the headland is less than its depth at the bay, <b>draw a table comparing the properties of '
    'the water waves at the &ldquo;headland&rdquo; and at the &ldquo;bay&rdquo;</b> as regards:',
    'Explain', F.headland_bay('Figure 2'),
    parts=['<b>a)</b> the wave speed ( v ).', '<b>b)</b> the wavelength ( &lambda; ).',
           '<b>c)</b> the wave frequency ( f ).'])
d.q('Which of the following statements correctly describes what happens to a light wave or a water wave '
    'when it is refracted while passing at an oblique angle from one medium into another medium of '
    'different properties?', 'MCQ',
    ch=['the frequency of the wave changes, while its speed and its wavelength stay constant',
        'the speed of the wave and its wavelength change, while its frequency stays constant',
        'the speed of the wave, its wavelength and its frequency all increase',
        'the speed of the wave, its wavelength and its frequency all decrease'])
d.q('The graph shows the relation between the speed of a wave (v) and its wavelength (&lambda;) for three '
    'waves from different sources, as the wave passes between media of different properties. <b>Which of '
    'the frequencies has the largest value?</b> Give the explanation.', 'Problem',
    F.v_lambda_graph('Figure 3'))
d.q('When a wave spreads through vacuum or through a medium, the locus of all the points that vibrate in '
    'the same phase is called the &hellip;&hellip;&hellip;', 'MCQ', F.wavefront_def('Figure 4'),
    ch=['frequency of the wave', 'wavelength', 'speed of the wave', 'wavefront'])
d.q('A wave crosses a boundary separating two media as shown in the figure. <b>Calculate the '
    'following:</b>', 'Problem', F.wave_boundary('Figure 5'),
    parts=['<b>a)</b> the ratio &nbsp; ( the frequency of the wave in medium 1 ) / ( the frequency of the '
           'wave in medium 2 ) &nbsp; = &hellip;&hellip;',
           '<b>b)</b> the ratio &nbsp; ( the wavelength of the wave in medium 1 ) / ( the wavelength of '
           'the wave in medium 2 ) &nbsp; = &hellip;&hellip;'])
d.q('A wave of frequency 50 Hz travels in medium (1) with a speed of 300 m/s. On passing into medium (2) '
    'its speed changes to 600 m/s. Which of the following statements is <b>not</b> correct?', 'MCQ',
    F.speed_change('Figure 6'),
    ch=['the frequency of the wave in medium (2) equals 50 Hz',
        'the wavelength of the wave in medium (1) equals half its value in medium (2)',
        'the angle of incidence of the wave in medium (1) equals half the angle of refraction in medium (2)',
        'the refractive index of medium (1) equals twice the refractive index of medium (2)'])
d.q('A light ray passes at an oblique angle from medium (1) into medium (2). Given that the absolute '
    'refractive index of medium (1) is greater than the absolute refractive index of medium (2), that is '
    'n&#8321; &gt; n&#8322;, which of the following physical changes correctly describes what happens to '
    'the light ray on entering medium (2)?', 'MCQ',
    ch=['the ray is refracted towards the normal, and its speed and wavelength decrease',
        'the ray is refracted away from the normal, and its speed and wavelength increase',
        'the ray is refracted away from the normal, its speed increases and its frequency decreases',
        'the ray passes straight on without any deviation, and its speed and wavelength stay constant'])
d.q('A light ray travels from material (A) into material (B), so that the angle of incidence in material '
    '(A) equals 30&deg; and the angle of refraction in material (B) equals 45&deg;. Which of the following '
    'statements correctly describes the behaviour of the light and the physical properties of the two '
    'materials?', 'MCQ',
    ch=['the refractive index of (A) is greater than that of (B), and the speed of light in (A) is less '
        'than it is in (B)',
        'the refractive index of (A) is less than that of (B), and the speed of light in (A) is greater '
        'than it is in (B)',
        'the refractive index of (A) is greater than that of (B), and the speed of light in (A) is greater '
        'than it is in (B)',
        'the refractive index of (A) equals that of (B), and the frequency in (A) is doubled in (B)'])

# ---------------- solutions ----------------
_HD = ['property', 'at the headland (shallow)', 'at the bay (deeper)']
_RW = [['wave speed v', 'smaller', 'larger'],
       ['wavelength &lambda;', 'shorter', 'longer'],
       ['frequency f', 'the same', 'the same'],
       ['wave energy', 'concentrated', 'spread out']]
_TBL = ('<table class="vt"><tr>' + ''.join('<th>' + hh + '</th>' for hh in _HD) + '</tr>' +
        ''.join('<tr>' + ''.join('<td>' + c + '</td>' for c in r) + '</tr>' for r in _RW) + '</table>')

d.page()
d.sec('✓', 'Answer key', 'Solutions — step by step')
d.hint('<b>Start every refraction question the same way.</b> Write f&#8321; = f&#8322;. Then '
       'v = f&lambda; forces &lambda; to follow the speed: a slower medium means a shorter wavelength, '
       'and the ray bends <b>towards</b> the normal.')

d.grp('Part A — Classwork 1')
d.sol(1, 'sea waves running into shallow water',
      None,
      'a) v decreases, λ decreases, f stays the same, and the direction bends towards the shore '
      'b) because the shallow end of each crest slows down first c) refraction',
      why='<b>a) The three changes.</b> The speed of a water wave depends on the <b>depth</b>: the '
          'shallower the water the slower the wave, so on moving inshore <b>v decreases</b>. The '
          'frequency is set by whatever produced the waves far out at sea, so <b>f does not change</b>. '
          'Since v = f&lambda; and f is fixed, the wavelength must fall in the same proportion as the '
          'speed: <b>&lambda; decreases</b>, which is why the crests are drawn closer and closer together '
          'in the figure. The <b>direction</b> swings round until the crests are almost parallel to the '
          'shore line.<br><br>'
          '<b>b) Why they bend.</b> A crest arriving obliquely does not meet the shallow water all at '
          'once. The end of the crest that is already in shallow water slows down, while the other end is '
          'still in deeper water and keeps moving faster. The faster end therefore swings forward about '
          'the slower one, exactly as a marching line wheels about its inner end, and the crest is turned '
          'until it lies along the depth contours &mdash; that is, along the shore line.<br><br>'
          '<b>c) The concept.</b> This is <b>refraction</b>: the change in the direction of a wave when '
          'it passes obliquely from one medium into another in which its speed is different, its '
          'frequency staying the same.')
d.sol(2, 'what changes from deep to shallow water',
      'depth decreases  →  v decreases\n'
      'f is fixed by the source, so from  v = f λ :\n'
      '    λ = v / f        →  λ decreases as well\n'
      'and the oblique crests swing round towards the shore line.',
      'B) the speed decreases, the wavelength decreases, and the direction bends to become parallel to '
      'the shore line',
      why='Choice (D) is the tempting wrong one: it gets the speed right but then makes &lambda; increase, '
          'which would need the frequency to fall — and the frequency cannot change.')

d.grp('Part B — Home assignment 1')
d.sol(3, 'the headland compared with the bay',
      'the water at the headland is <b>shallower</b>, so the waves there are slower :\n'
      '    v(headland) < v(bay)\n'
      'the frequency is the same everywhere ( the same source out at sea ) :\n'
      '    f(headland) = f(bay)\n'
      'so from  λ = v / f  :\n'
      '    λ(headland) < λ(bay)',
      'the headland has the smaller v and the shorter &lambda;, and the same f as the bay',
      extra=_TBL,
      why='Look at the figure: because the crests slow down over the shallow water off the headland, they '
          'bend round it from both sides. The rays therefore <b>converge</b> on the headland and '
          '<b>diverge</b> in the bay. That is why headlands are attacked and worn away by the sea while '
          'bays stay calm and collect sand — the wave energy per metre of coast is far greater at '
          'the headland.')
d.sol(4, 'what refraction changes and what it does not',
      'the source sets the frequency, and the boundary cannot create or destroy cycles :\n'
      '    f₁ = f₂          ( the frequency never changes )\n'
      'the new medium sets a new speed, so from  v = f λ  with f fixed :\n'
      '    v changes   →   λ changes by the same factor',
      'B) the speed of the wave and its wavelength change, while its frequency stays constant',
      why='Think of the boundary as a turnstile: the same number of crests arrive every second as leave '
          'every second, otherwise crests would pile up at the boundary. That is the whole reason why f '
          'cannot change.')
d.sol(5, 'which frequency is the largest',
      'the wave equation  v = f λ  can be read as the equation of a straight line :\n'
      '    v = f × λ        →        ( y = slope × x )\n'
      'so for each source the graph of v against λ is a straight line through the\n'
      'origin whose <b>slope is the frequency</b>.\n'
      'the steepest of the three lines is the one belonging to f₃ .',
      'f&#8323; has the largest value, because its line has the greatest slope and the slope of a '
      'v &ndash; &lambda; graph is the frequency',
      why='Read one point off any line to get a number: if a line passes through &lambda; = 4.0 m at '
          'v = 200 m/s, then f = v/&lambda; = 50 Hz. The three lines all pass through the origin, which '
          'is the graphical way of saying that a wave of zero wavelength would have zero speed.')
d.sol(6, 'the name of the locus of points in the same phase',
      'all the points of a <b>wavefront</b> have been disturbed by the source for the\n'
      'same length of time, so they are all at the same stage of their vibration.\n'
      'near a point source the wavefronts are circles ( or spheres ) ; far away they\n'
      'are practically straight lines ( or planes ). the ray is always ⊥ the wavefront.',
      'D) the wavefront')
d.sol(7, 'the two ratios at the boundary',
      'from the figure :      i = 45°   in medium 1        r = 30°   in medium 2\n\n'
      'a)  the frequency is set by the source and cannot change at a boundary :\n'
      '        f₁ / f₂ = 1\n\n'
      'b)  since f is the same,  λ ∝ v , and the law of refraction gives :\n'
      '        λ₁ / λ₂ = v₁ / v₂ = sin i / sin r\n'
      '        λ₁ / λ₂ = sin 45° / sin 30° = 0.7071 / 0.5\n'
      '        λ₁ / λ₂ = 1.41   ( = √2 )',
      'a) f&#8321; : f&#8322; = 1 : 1 &nbsp;&nbsp; b) &lambda;&#8321; : &lambda;&#8322; = &radic;2 : 1 '
      '&asymp; 1.41',
      why='The ray bends <b>towards</b> the normal (45&deg; &rarr; 30&deg;), so medium 2 is the slower, '
          'optically denser one — and a slower medium always carries the shorter wavelength, which '
          'is exactly what the ratio 1.41 says.')
d.sol(8, 'which statement is not correct',
      'check each statement against  f₁ = f₂ = 50 Hz  and  λ = v / f :\n'
      '    λ₁ = 300 / 50 = 6 m          λ₂ = 600 / 50 = 12 m\n\n'
      '  (A)  f in medium 2 = 50 Hz                        ✓ correct\n'
      '  (B)  λ₁ = 6 m = half of λ₂ = 12 m                 ✓ correct\n'
      '  (D)  n = c / v , so  n₁ / n₂ = v₂ / v₁ = 600/300 = 2   ✓ correct\n'
      '  (C)  the law of refraction gives\n'
      '           sin i / sin r = v₁ / v₂ = 1 / 2 ,  that is  sin r = 2 sin i\n'
      '       which is <b>not</b> the same as  i = r / 2                ✗ wrong',
      'C) &mdash; the statement that the angle of incidence equals half the angle of refraction',
      why='The relation between the two angles involves their <b>sines</b>, not the angles themselves. '
          'Test it with numbers: for i = 20&deg;, sin r = 2 sin 20&deg; = 0.684, so r = 43.2&deg; '
          '— not 40&deg;.')
d.sol(9, 'entering a medium of smaller refractive index',
      '    n₁ > n₂        and        n = c / v        →        v₁ < v₂\n'
      'so the ray speeds up on entering medium 2, which means it bends <b>away</b> from\n'
      'the normal. with f unchanged,  λ = v / f  increases as well.',
      'B) the ray is refracted away from the normal, and its speed and wavelength increase',
      why='Choice (C) says the frequency decreases — the one thing refraction can never do. Remember '
          'the pair: <b>into a denser medium</b> means slower, shorter &lambda;, bending towards the '
          'normal; <b>into a less dense medium</b> means faster, longer &lambda;, bending away from it.')
d.sol(10, 'comparing the two materials A and B',
      'apply the law of refraction between the two materials :\n'
      '    n(A) sin i = n(B) sin r\n'
      '    n(A) sin 30° = n(B) sin 45°\n'
      '    n(A) × 0.5 = n(B) × 0.7071\n'
      '    n(A) / n(B) = 0.7071 / 0.5 = 1.41        →   n(A) > n(B)\n'
      'and since  v = c / n  :\n'
      '    a larger n means a smaller v        →   v(A) < v(B)',
      'A) the refractive index of (A) is greater than that of (B), and the speed of light in (A) is less '
      'than in (B)',
      why='A quick sanity check without any algebra: the ray bends <b>away</b> from the normal on going '
          'from A into B (30&deg; &rarr; 45&deg;), so it must have <b>sped up</b> — B is the faster, '
          'less dense material. Everything else follows from that one observation.')

d.foot('Lesson 2&ndash;6 &middot; Refraction of Waves &middot; Mr. Gemy',
       'f&#8321; = f&#8322; &nbsp;&middot;&nbsp; sin i / sin r = v&#8321;/v&#8322; = '
       '&lambda;&#8321;/&lambda;&#8322;')
d.save('l26.html')
print('l26.html written -', d.n, 'questions')

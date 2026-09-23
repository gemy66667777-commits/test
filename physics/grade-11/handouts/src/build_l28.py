# -*- coding: utf-8 -*-
import figs_l28 as F
from figs_l27 import doppler_source
from docbase import Doc

d = Doc('Unit 2 &middot; Lesson 2&ndash;8', 'The Doppler Effect<br>for Light',
        'Red shift and blue shift, &Delta;&lambda;/&lambda; = v/c, and how the pitch of a siren tells you '
        'which way a source is moving.',
        ['Grade 11 &middot; Egyptian Baccalaureate', '22 questions', 'Step-by-step solutions',
         'c = 3 &times; 10&#8312; m/s &middot; v(sound) = 340 m/s'],
        'The Doppler Effect for Light')

d.kit('The toolkit for this lesson', [
    ('&Delta;&lambda; / &lambda; = v / c', 'the radial speed of a star or galaxy'),
    ('red shift', '&lambda;&rsquo; &gt; &lambda; &rarr; the source is moving <b>away</b>'),
    ('blue shift', '&lambda;&rsquo; &lt; &lambda; &rarr; the source is moving <b>towards</b> us'),
    ('f&rsquo; = f &middot; v / ( v &minus; v<sub>s</sub> )', 'a sound source approaching'),
    ('f&rsquo; = f &middot; v / ( v + v<sub>s</sub> )', 'a sound source receding'),
    ('c is always c', 'the speed of light never changes with the motion'),
])
d.hint('<b>Ask one question first: is the gap closing or opening?</b> Closing gives a shorter wavelength '
       '&mdash; a higher pitch for sound, a blue shift for light. Opening gives a longer wavelength &mdash; '
       'a lower pitch, a red shift. Everything else in this lesson is arithmetic on top of that one idea.')

# ---------------- A ----------------
d.sec('A', 'Classwork &nbsp;2', 'Red shift and blue shift')
d.q('In an experiment simulating the Doppler effect for light in the astronomy laboratory, two detectors '
    'recorded the spectral state of two stars (X) and (Y):<br>&nbsp;&nbsp;1. The first detector found that '
    'the spectral line of star (X) had <b>increased</b> in wavelength by an amount '
    '&Delta;&lambda;.<br>&nbsp;&nbsp;2. The second detector found that the spectral line of star (Y) had '
    '<b>decreased</b> in wavelength by an amount &Delta;&lambda;.', 'Explain',
    F.spectrum_shift('Figure 1'),
    parts=['<b>a)</b> Determine which of them represents a &ldquo;red shift&rdquo; and which represents a '
           '&ldquo;blue shift&rdquo;.',
           '<b>b)</b> Explain how astronomers deduce, from these spectral changes, the speed and the '
           'direction of motion of the stars in the universe.'])
d.q('On observing light coming from a distant galaxy, a shift of its spectral lines towards the red colour '
    'is noticed. What is the physical reason for this shift, based on the Doppler effect?', 'MCQ',
    ch=['the galaxy receding from the Earth leads to an increase in the wavelength',
        'the galaxy approaching the Earth leads to an increase in the wavelength',
        'the galaxy receding from the Earth leads to a decrease in the wavelength',
        'the galaxy staying fixed in its position leads to an increase in the wavelength'])

# ---------------- B ----------------
d.sec('B', 'Home assignment &nbsp;2', 'Measuring the speed of a galaxy')
d.q('The spectrum of the element hydrogen taken in the laboratory shows a spectral line at a wavelength '
    '&lambda; = 656 nm. On observing the same spectral line in light coming from a moving galaxy, the '
    'magnitude of the shift in the wavelength was found to equal '
    '&Delta;&lambda; = 1.312 nm. <b>Calculate the radial speed (v) of the galaxy relative to the '
    'observer</b>, given that the speed of light c = 3 &times; 10&#8312; m/s.', 'Problem',
    F.galaxy_motion('Figure 2'))
d.q('When a galaxy moves towards the planet Earth with a high speed, the apparent frequency of the light '
    'recorded by astronomers is:', 'MCQ',
    ch=['higher than the original frequency, and the lines shift towards the blue colour',
        'lower than the original frequency, and the lines shift towards the red colour',
        'higher than the original frequency, and the lines shift towards the red colour',
        'lower than the original frequency, and the lines shift towards the blue colour'])
d.q('What happens to the speed of light (c) in vacuum when it is emitted from a star moving with a great '
    'speed towards the observer?', 'MCQ',
    ch=['it stays constant and does not change',
        'it increases by an amount equal to the speed of motion of the approaching star',
        'it decreases by an amount equal to the speed of motion of the approaching star',
        'it changes depending on the apparent frequency of the observed light'])
d.q('A car moving eastwards with a speed of 15 m/s gives out a sound of frequency 600 Hz, and a motorcycle '
    'moving westwards with a speed of 20 m/s passes beside it. <b>Find the frequency of the sound heard by '
    'the rider of the motorcycle after they have passed each other</b>, taking the speed of sound in air '
    'as 340 m/s.', 'Problem', F.car_bike('Figure 3'))
d.q('The phenomenon in which the observed frequency differs from the frequency of the source because of '
    'the relative motion between the source and the observer is called &hellip;&hellip;', 'MCQ',
    ch=['interference of waves', 'the Doppler effect', 'diffraction of waves', 'refraction of waves'])

# ---------------- C ----------------
d.page()
d.sec('C', 'Weekly assessment', 'Group A')
d.q('An ambulance sounding its siren at a constant frequency moves with a uniform speed towards a person '
    'standing at the side of the road. What happens to the <b>intensity</b> of the sound (its loudness) '
    'and to the <b>pitch</b> of the sound (its frequency) as noticed by the stationary person while the '
    'car approaches him?', 'MCQ', F.ambulance_pass('Figure 4'),
    ch=['the intensity of the sound increases, and the apparent frequency increases',
        'the intensity of the sound increases, and the apparent frequency decreases',
        'the intensity of the sound decreases, and the apparent frequency increases',
        'both the intensity and the frequency stay constant without change'])
d.q('The figure shows the observation of light coming from a galaxy; a shift of its spectral lines towards '
    'the red colour is noticed compared with the same spectrum in the laboratory. What is the physical '
    'reason for this shift, based on the Doppler effect?', 'MCQ',
    ch=['the galaxy receding from the Earth leads to an increase in the wavelength',
        'the galaxy approaching the Earth leads to an increase in the wavelength',
        'the galaxy receding from the Earth leads to a decrease in the wavelength',
        'the galaxy staying fixed in its position leads to an increase in the wavelength'])
d.q('A sound source moving with a speed of 25 m/s approaches a stationary observer while giving out a '
    'sound of frequency 600 Hz. <b>Find the frequency of the sound heard by the observer</b>, given that '
    'the speed of sound in air is 340 m/s.', 'Problem', doppler_source('Figure 5'))
d.q('On observing the light coming from one of the distant galaxies, scientists noticed that all the '
    'colours of its spectrum were shifted slightly towards the red colour. <b>What do we conclude from '
    'this observation about the motion of the galaxy?</b> Explain the reason for this shift, based on the '
    'Doppler effect for light.', 'Explain')
d.q('An increase is noticed in the sharpness of the whistle of a speeding train while it approaches the '
    'stopping station, while the sharpness of the sound decreases as soon as it passes the station and '
    'moves away from it. <b>Give the reason</b> for this observation, based on the concept of the Doppler '
    'effect.', 'Explain')

# ---------------- D ----------------
d.sec('D', 'Weekly assessment', 'Group B')
d.q('When an ambulance sounding a horn of constant frequency passes a shore on which a listener is '
    'standing, and begins to move away from him with a uniform speed: how do the pitch of the sound (its '
    'apparent frequency) and the intensity of the sound measured by the listener change while the car is '
    'moving away?', 'MCQ',
    ch=['the apparent frequency decreases, and the intensity of the sound decreases',
        'the apparent frequency increases, and the intensity of the sound increases',
        'the apparent frequency decreases, and the intensity of the sound increases',
        'the apparent frequency increases, and the intensity of the sound decreases'])
d.q('If the wavelength of a spectral line observed for a galaxy equals (&lambda;&rsquo;) and the reference '
    'wavelength in the laboratory equals (&lambda;), then the case that expresses the galaxy approaching '
    'with a radial speed (v) is:', 'MCQ',
    ch=['&lambda;&rsquo; &lt; &lambda; , and the spectral lines shift towards the blue colour',
        '&lambda;&rsquo; &gt; &lambda; , and the spectral lines shift towards the red colour',
        '&lambda;&rsquo; &lt; &lambda; , and the spectral lines shift towards the red colour',
        '&lambda;&rsquo; &gt; &lambda; , and the spectral lines shift towards the blue colour'])
d.q('A sound source moving with a speed of 20 m/s recedes from a stationary observer while giving out a '
    'sound of frequency 600 Hz. <b>Find the frequency of the sound heard by the observer</b>, given that '
    'the speed of sound in air is 340 m/s.', 'Problem')
d.q('On observing the electromagnetic spectrum of light coming from a distant galaxy, one of the '
    'astronomers noticed that the absorption spectrum lines of the element sodium had shifted towards the '
    'side of the lower frequencies (the red colour). <b>What conclusion does the astronomer reach about '
    'the direction of motion of this galaxy relative to the Earth?</b> Explain your answer.', 'Explain')
d.q('An ambulance approaches a person standing at the side of the road while sounding its siren, then '
    'passes him and moves away from him. <b>Compare</b> between the pitch (sharpness) of the sound that '
    'the person hears while the ambulance is approaching him, and the pitch of the sound after it has '
    'passed him and moved away.', 'Explain')

# ---------------- E ----------------
d.sec('E', 'Weekly assessment', 'Group C')
d.q('When an ambulance sounding a horn of constant frequency f approaches a person standing at the side of '
    'the road, the apparent wavelength (&lambda;) of the sound waves that the person receives, compared '
    'with the original wavelength (&lambda;) of the wave in air, is:', 'MCQ',
    ch=['larger; because of the piling up of the sound waves behind the source',
        'smaller; because of the compression of the sound waves in front of the source',
        'equal; because the frequency of the sound of the source is constant and does not change',
        'smaller; because of the increase in the speed of propagation of sound in air'])
d.q('The spectral shift of the light of galaxies towards the longer wavelengths is known as:', 'MCQ',
    ch=['the red shift, and it indicates that the galaxy is receding from the Earth',
        'the blue shift, and it indicates that the galaxy is receding from the Earth',
        'the red shift, and it indicates that the galaxy is approaching the Earth',
        'the blue shift, and it indicates that the galaxy is approaching the Earth'])
d.q('A car moving eastwards with a speed of 15 m/s gives out a sound of frequency 600 Hz, and a motorcycle '
    'moving westwards with a speed of 20 m/s passes beside it. <b>Find the frequency of the sound heard by '
    'the rider of the motorcycle before they have passed each other</b>, taking the speed of sound in air '
    'as 340 m/s.', 'Problem')
d.q('The siren of a fire engine is heard at a high (sharp) frequency while it approaches a person standing '
    'at the side of the road, while the same siren is heard at a low (deep) frequency after it has passed '
    'him and moved away from him. <b>State the name of the physical phenomenon</b> responsible for this '
    'observation.', 'Explain')
d.q('On observing the light spectrum coming from two different galaxies (A) and (B), it was noticed that '
    'the spectral lines of galaxy (A) were shifted towards the red colour, while the spectral lines of '
    'galaxy (B) were shifted towards the blue colour. <b>Explain the direction of motion of each of the '
    'two galaxies</b> relative to the observer.', 'Explain')

# ---------------- solutions ----------------
_HD = ['', 'red shift', 'blue shift']
_RW = [['the wavelength', '&lambda;&rsquo; &gt; &lambda; &nbsp;( longer )',
        '&lambda;&rsquo; &lt; &lambda; &nbsp;( shorter )'],
       ['the frequency', 'lower than f', 'higher than f'],
       ['the motion', 'the source is receding', 'the source is approaching'],
       ['the speed from it', 'v = c &Delta;&lambda; / &lambda;', 'v = c &Delta;&lambda; / &lambda;']]
_TBL = ('<table class="vt"><tr>' + ''.join('<th>' + hh + '</th>' for hh in _HD) + '</tr>' +
        ''.join('<tr>' + ''.join('<td>' + c + '</td>' for c in r) + '</tr>' for r in _RW) + '</table>')

d.page()
d.sec('✓', 'Answer key', 'Solutions — step by step')
d.hint('<b>One sentence covers the whole lesson.</b> A <b>closing</b> gap squeezes the waves: shorter '
       '&lambda;, higher f, blue shift. An <b>opening</b> gap stretches them: longer &lambda;, lower f, '
       'red shift. For light, &Delta;&lambda;/&lambda; = v/c turns the size of the shift into a speed.')

d.grp('Part A — Classwork 2')
d.sol(1, 'the two stars X and Y',
      'star X :  λ increased   →  the light has been stretched  →  <b>red shift</b>\n'
      'star Y :  λ decreased   →  the light has been squeezed   →  <b>blue shift</b>',
      'a) X shows a red shift (moving away) and Y shows a blue shift (moving towards us) &nbsp;&nbsp; '
      'b) from the size of &Delta;&lambda; : v = c &Delta;&lambda; / &lambda;',
      extra=_TBL,
      why='<b>b) How astronomers use it.</b> Every element gives out (or absorbs) light at a fixed set of '
          'wavelengths, and that pattern is measured in the laboratory. When the same pattern is found in '
          'the light of a star, the whole set of lines is seen to have slid along the spectrum without '
          'changing its <b>spacing</b> &mdash; which is what proves it is a Doppler shift rather than a '
          'different element. The <b>direction</b> of the slide gives the direction of motion: towards '
          'the red for a receding star, towards the blue for an approaching one. The <b>size</b> of the '
          'slide gives the speed, from &Delta;&lambda;/&lambda; = v/c. Note that this measures only the '
          '<b>radial</b> component of the velocity &mdash; motion straight across the line of sight '
          'produces no shift at all.')
d.sol(2, 'the reason for a red shift',
      'red is the <b>long</b> wavelength end of the visible spectrum, so a shift towards\n'
      'the red means  λ′ > λ  — the waves have been stretched out.\n'
      'waves are stretched when the gap between source and observer is <b>opening</b>.',
      'A) the galaxy receding from the Earth leads to an increase in the wavelength',
      why='Choices (B) and (C) each get one half right and one half wrong, which is exactly what makes '
          'them tempting. Fix the pair in your memory: <b>red = receding = longer</b>.')

d.grp('Part B — Home assignment 2')
d.sol(3, 'the radial speed of the galaxy',
      '    Δλ / λ = v / c        →        v = c Δλ / λ\n'
      '    v = ( 3 × 10⁸ ) × 1.312 / 656\n'
      '    1.312 / 656 = 0.002\n'
      '    v = ( 3 × 10⁸ ) × 0.002\n'
      '    v = 6 × 10⁵ m/s   =  600 km/s',
      'v = 6 &times; 10&#8309; m/s = 600 km/s',
      why='The two wavelengths are both in nanometres, so the units cancel in the ratio and there is no '
          'need to convert either of them. Notice how small the shift is — 0.2 % — and yet it '
          'corresponds to 600 km/s, because it is being compared with the speed of light.')
d.sol(4, 'a galaxy approaching at high speed',
      'the gap is <b>closing</b>, so the waves are squeezed :\n'
      '    λ′ < λ        and        f′ = c / λ′  >  f\n'
      'a shorter wavelength is nearer the blue end of the spectrum.',
      'A) higher than the original frequency, and the lines shift towards the blue colour')
d.sol(5, 'the speed of light from a moving star',
      'the speed of light in vacuum is the <b>same for every observer</b>, whatever the\n'
      'motion of the source or of the observer :\n'
      '    c = 3 × 10⁸ m/s   always\n'
      'the motion changes λ and f, and they change together so that  c = f λ  still holds.',
      'A) it stays constant and does not change',
      why='This is the one place where light differs completely from sound. The speed of <b>sound</b> is '
          'fixed by the air, so a wind can change it; the speed of <b>light</b> in vacuum is a constant '
          'of nature and is the foundation of the special theory of relativity.')
d.sol(6, 'the motorcycle rider after they pass',
      'after passing, the car goes on eastwards and the motorcycle goes on westwards,\n'
      'so the two are <b>separating</b> : both motions lower the pitch.\n'
      '    f′ = f × ( v − vₒ ) / ( v + vₛ )\n'
      '    f′ = 600 × ( 340 − 20 ) / ( 340 + 15 )\n'
      '    f′ = 600 × 320 / 355\n'
      '    f′ = 540.8 ≈ 541 Hz',
      'f&rsquo; &asymp; 541 Hz',
      why='<b>Which sign goes where.</b> The observer’s speed is <b>subtracted</b> on the top when '
          'the observer is running away; the source’s speed is <b>added</b> on the bottom when the '
          'source is running away. Both effects lower the pitch here, which is why the answer is well '
          'below 600 Hz. <b>Note on the printed question:</b> the speed of sound is not stated in this '
          'item; 340 m/s has been used, the value the book gives in the other questions of this same '
          'lesson.')
d.sol(7, 'the name of the phenomenon',
      'a difference between the observed frequency and the frequency of the source,\n'
      'caused purely by relative motion, is the <b>Doppler effect</b>.',
      'B) the Doppler effect')

d.grp('Part C — Weekly assessment, Group A')
d.sol(8, 'loudness and pitch as the ambulance approaches',
      'two separate things are happening :\n'
      '    the car is getting <b>closer</b>   →  the same energy is spread over a\n'
      '                                        smaller area  →  the sound is louder\n'
      '    the gap is <b>closing</b>          →  the waves are squeezed  →  higher f′',
      'A) the intensity of the sound increases, and the apparent frequency increases',
      why='Keep loudness and pitch apart in your mind. Loudness depends on the <b>distance</b>, so it '
          'rises all the way in and falls all the way out. Pitch depends on whether the distance is '
          '<b>changing</b>, so it is high on the way in, true at the instant of passing, and low on the '
          'way out.')
d.sol(9, 'the red shift of a galaxy',
      'red   →  longer λ   →  λ′ > λ   →  the gap is opening\n'
      '→  the galaxy is moving away from the Earth.',
      'A) the galaxy receding from the Earth leads to an increase in the wavelength')
d.sol(10, 'a source approaching at 25 m/s',
      'the source is approaching, so the wavelength in front of it is shortened :\n'
      '    f′ = f × v / ( v − vₛ )\n'
      '    f′ = 600 × 340 / ( 340 − 25 )\n'
      '    f′ = 600 × 340 / 315\n'
      '    f′ = 647.6 ≈ 648 Hz',
      'f&rsquo; &asymp; 648 Hz',
      why='Check the direction before you check the arithmetic: the source is coming closer, so the answer '
          '<b>must</b> be above 600 Hz. If your calculator gives less than 600, you have put the minus '
          'sign in the wrong place.')
d.sol(11, 'all the colours shifted towards the red',
      'the whole pattern of lines has moved to longer wavelengths :\n'
      '    λ′ > λ        →        the gap is opening',
      'the galaxy is moving away from us, and the faster it recedes the bigger the shift',
      why='The key point is that <b>all</b> the lines moved, and by the same <b>fraction</b> of their own '
          'wavelength. A change of the source itself would move some lines and not others; only motion '
          'slides the whole pattern in step. This is how Hubble discovered that almost every distant '
          'galaxy is receding, and that the further away a galaxy is the faster it goes — the '
          'evidence that the universe is expanding.')
d.sol(12, "the train's whistle at the station",
      'approaching : each crest is sent from a point nearer the station, so the crests\n'
      '              arrive crowded  →  λ′ is shorter  →  f′ is higher — a sharp note\n'
      'receding    : each crest is sent from a point further away, so they arrive\n'
      '              stretched out   →  λ′ is longer   →  f′ is lower — a deep note',
      'the Doppler effect: the gap closes on the way in (higher pitch) and opens on the way out (lower '
      'pitch)',
      why='The whistle itself never changes. Neither does the speed of sound in the air. The only thing '
          'that changes is the <b>spacing of the crests that reach the ear</b>.')

d.grp('Part D — Weekly assessment, Group B')
d.sol(13, 'the ambulance moving away',
      'the car is getting <b>further</b>     →  the sound is fainter\n'
      'the gap is <b>opening</b>            →  the waves are stretched  →  lower f′',
      'A) the apparent frequency decreases, and the intensity of the sound decreases')
d.sol(14, 'the case that means the galaxy is approaching',
      'approaching  →  the gap is closing  →  the waves are squeezed :\n'
      '    λ′ < λ        and a shorter λ is nearer the <b>blue</b> end',
      'A) &lambda;&rsquo; &lt; &lambda; , and the spectral lines shift towards the blue colour')
d.sol(15, 'a source receding at 20 m/s',
      'the source is receding, so the wavelength behind it is stretched :\n'
      '    f′ = f × v / ( v + vₛ )\n'
      '    f′ = 600 × 340 / ( 340 + 20 )\n'
      '    f′ = 600 × 340 / 360\n'
      '    f′ = 566.7 ≈ 567 Hz',
      'f&rsquo; &asymp; 567 Hz',
      why='Compare with question 10: there the source approached at 25 m/s and the pitch rose by about '
          '48 Hz; here it recedes at 20 m/s and the pitch falls by about 33 Hz. The shift is always '
          'towards the observer’s side of 600 Hz.')
d.sol(16, 'the sodium lines shifted to lower frequencies',
      'lower frequency  →  longer wavelength  →  a <b>red</b> shift\n'
      '→  the gap between the galaxy and the Earth is opening.',
      'the galaxy is moving away from the Earth',
      why='The sodium lines are a good marker precisely because their laboratory wavelengths are known to '
          'great accuracy (the familiar orange-yellow pair at about 589 nm), so even a small displacement '
          'can be measured with confidence and converted into a speed with '
          '&Delta;&lambda;/&lambda; = v/c.')
d.sol(17, 'the pitch before and after the ambulance passes',
      'approaching : the gap is closing  →  λ′ shorter  →  f′ > f   ( sharp )\n'
      'at the instant of passing : the motion is across the line of sight  →  f′ = f\n'
      'receding    : the gap is opening  →  λ′ longer   →  f′ < f   ( deep )',
      'the pitch is higher than the true note while approaching and lower than it after passing, and the '
      'change is sudden',
      why='The drop is heard as a sudden step rather than a slide, because the whole reversal from '
          '“closing fast” to “opening fast” happens in the fraction of a second in '
          'which the ambulance sweeps past.')

d.grp('Part E — Weekly assessment, Group C')
d.sol(18, 'the apparent wavelength in front of an approaching source',
      'in the time of one cycle the source emits one crest and then moves forward before\n'
      'emitting the next, so the crests in front of it are closer together :\n'
      '    λ′ = ( v − vₛ ) / f   <   λ',
      'B) smaller; because of the compression of the sound waves in front of the source',
      why='Choice (D) contains the standard misconception. The speed of sound in air is decided by the '
          'air alone; the motion of the source changes the <b>spacing</b> of the crests, never their '
          'speed.')
d.sol(19, 'the name of a shift to longer wavelengths',
      'longer λ  →  towards the red end  →  a <b>red shift</b>\n'
      'and stretching happens when the gap is opening  →  the galaxy is receding.',
      'A) the red shift, and it indicates that the galaxy is receding from the Earth')
d.sol(20, 'the motorcycle rider before they pass',
      'before passing, the car is still to the west of the motorcycle : the car drives\n'
      'east towards it and the motorcycle drives west towards the car, so the two are\n'
      '<b>closing</b> — both motions raise the pitch.\n'
      '    f′ = f × ( v + vₒ ) / ( v − vₛ )\n'
      '    f′ = 600 × ( 340 + 20 ) / ( 340 − 15 )\n'
      '    f′ = 600 × 360 / 325\n'
      '    f′ = 664.6 ≈ 665 Hz',
      'f&rsquo; &asymp; 665 Hz',
      why='Put this beside question 6, which is the same pair of vehicles after they have passed: the '
          'rider hears about 665 Hz on the way in and about 541 Hz on the way out — a drop of some '
          '124 Hz in an instant, which is why such a pass sounds so dramatic. <b>Note on the printed '
          'question:</b> the speed of sound is again not stated here, so 340 m/s has been used.')
d.sol(21, 'the name of the phenomenon',
      'the pitch changes only because the fire engine is <b>moving</b> relative to the\n'
      'listener — the siren itself is unaltered.',
      'the Doppler effect')
d.sol(22, 'the two galaxies A and B',
      'galaxy A : lines shifted towards the <b>red</b>    →  λ′ > λ  →  stretched\n'
      '           →  the gap is opening  →  A is moving <b>away</b> from the observer\n\n'
      'galaxy B : lines shifted towards the <b>blue</b>   →  λ′ < λ  →  squeezed\n'
      '           →  the gap is closing  →  B is moving <b>towards</b> the observer',
      'A is receding from the observer and B is approaching the observer',
      why='Almost every galaxy we can see shows a red shift, so a blue-shifted galaxy such as B is '
          'unusual and means it is close enough for its own motion within the local group to beat the '
          'general expansion. The Andromeda galaxy is the famous example — it is blue-shifted, and '
          'is approaching us at about 110 km/s.')

d.foot('Lesson 2&ndash;8 &middot; The Doppler Effect for Light &middot; Mr. Gemy',
       '&Delta;&lambda;/&lambda; = v/c &nbsp;&middot;&nbsp; red = receding, blue = approaching')
d.save('l28.html')
print('l28.html written -', d.n, 'questions')

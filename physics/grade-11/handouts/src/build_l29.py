# -*- coding: utf-8 -*-
import figs_l29 as F
from docbase import Doc

d = Doc('Unit 2 &middot; Lesson 2&ndash;9', 'Refraction and Total<br>Internal Reflection',
        'The absolute refractive index, Snell&rsquo;s law, the critical angle, optical fibres and the '
        'blocking disc.',
        ['Grade 11 &middot; Egyptian Baccalaureate', '30 questions', 'Step-by-step solutions',
         'sin &theta;c = n&#8322; / n&#8321;'],
        'Refraction and Total Internal Reflection')

d.kit('The toolkit for this lesson', [
    ('n = c / v', 'the absolute refractive index'),
    ('n&#8321; sin &theta;&#8321; = n&#8322; sin &theta;&#8322;', 'Snell&rsquo;s law of refraction'),
    ('sin &theta;c = n&#8322; / n&#8321;', 'the critical angle, n&#8321; &gt; n&#8322;'),
    ('sin &theta;c = 1 / n', 'when the outside medium is air'),
    ('&lambda;&#8321; / &lambda;&#8322; = v&#8321; / v&#8322; = n&#8322; / n&#8321;',
     'f never changes'),
    ('r = h tan &theta;c', 'the radius of the blocking disc'),
])
d.hint('<b>A denser medium is a slower medium.</b> n = c/v, so a bigger n always means a smaller v, a '
       'shorter &lambda; and a ray that bends <b>towards</b> the normal. Going the other way &mdash; out '
       'of the denser medium &mdash; the ray bends away from the normal, and once the angle inside passes '
       '&theta;c it cannot get out at all.')

# ---------------- A ----------------
d.sec('A', 'Classwork &nbsp;1', 'Refraction between two media')
d.q('The opposite diagram shows a light ray passing between two media A and B. When the ray passes from '
    'medium A into medium B, <b>what happens to the speed of light and to the wavelength?</b>', 'Explain',
    F.two_media('Figure 1', 'medium A', 'medium B'))
d.q('The absolute refractive index (n) of a transparent medium is given by the relation &hellip;&hellip;',
    'Explain')

# ---------------- B ----------------
d.sec('B', 'Home assignment &nbsp;1', 'The refractive index')
d.q('Light falls from water into glass with an angle of incidence of 55&deg;. Given that the relative '
    'refractive index between water and glass equals 1.15, <b>calculate the angle of refraction of the '
    'light in the glass.</b>', 'Problem')
d.q('<b>Compare between</b> the optically denser medium and the optically less dense medium as regards: '
    'the speed of light in it, and the absolute refractive index.', 'Explain')
d.q('If the speed of light in air is 3 &times; 10&#8312; m/s and its speed in glass is '
    '2 &times; 10&#8312; m/s, <b>calculate the absolute refractive index of the glass.</b>', 'Problem')
d.q('When light passes from a less optically dense medium into a more optically dense medium, then '
    '&hellip;&hellip;', 'MCQ',
    ch=['both the frequency and the wavelength decrease',
        'the frequency increases and the wavelength decreases',
        'the frequency does not change and the wavelength increases',
        'the frequency does not change and the wavelength decreases'])
d.q('A light ray falls from medium (1), whose absolute refractive index is 1.3, into medium (2), whose '
    'absolute refractive index is 1.5, as in the figure. Which of the choices shows what will happen to '
    'both the wavelength and the speed of light in medium (2)?', 'MCQ',
    F.two_media('Figure 2', 'medium (1)&nbsp; n = 1.3', 'medium (2)&nbsp; n = 1.5'),
    ch=['both the wavelength and the speed increase',
        'both the wavelength and the speed decrease',
        'the wavelength increases and the speed decreases',
        'the wavelength decreases and the speed increases'])

# ---------------- C ----------------
d.sec('C', 'Classwork &nbsp;2', 'The critical angle')
d.q('When light passes from a more optically dense medium into a less dense medium, <b>what is the '
    'greatest value of the angle of refraction</b> in the less dense medium?', 'Explain',
    F.critical_angle('Figure 3'))
d.q('To calculate the critical angle between two media ( n&#8321; &gt; n&#8322; ) we use the relation '
    '&hellip;&hellip;', 'Explain')

# ---------------- D ----------------
d.page()
d.sec('D', 'Home assignment &nbsp;2', 'Total internal reflection')
d.q('<b>Give the scientific reason:</b> the outer cladding of an optical fibre is made of a material whose '
    'refractive index is less than the refractive index of the inner core.', 'Explain',
    F.optical_fibre('Figure 4'))
d.q('<b>What happens when</b> a narrow beam of light is directed upwards through the side of a glass of '
    'water towards the (water &ndash; air) surface, and the angle of incidence is gradually increased?',
    'Explain')
d.q('If the refractive index of the core in an optical fibre is 1.6 and that of the cladding is 1.4, then '
    'sin &theta;c between them equals:', 'MCQ',
    ch=['1.4 / 1.6', '1.6 / 1.4', '1 / 1.6', '1 / 1.4'])
d.q('Total internal reflection occurs when light passes from a medium:', 'MCQ',
    ch=['of lower optical density into a medium of higher optical density',
        'of higher optical density into a medium of lower optical density',
        'into another of equal density', 'that is opaque into one that is transparent'])
d.q('Given that the refractive index of glass is 1.5, which of the following figures shows the correct '
    'path of a light ray falling on the boundary separating the glass and the air at an angle of '
    '50&deg;?', 'MCQ', F.four_paths('Figure 5'),
    ch=['figure A', 'figure B', 'figure C', 'figure D'])

# ---------------- E ----------------
d.sec('E', 'Weekly assessment', 'Group A')
d.q('An optical fibre whose material has a refractive index of 2.1 is covered with an outer layer of '
    'cryolite. The refractive index of the outer layer that makes the critical angle between the two '
    'layers equal 32&deg; is &hellip;&hellip;', 'MCQ', ch=['1.11', '2.25', '3.96', '4.32'])
d.q('In the experiment of blocking light with a disc, if the water is replaced by another liquid of '
    'greater refractive index, then the area of the disc needed for the blocking:', 'MCQ',
    F.disc_block('Figure 6'),
    ch=['increases', 'decreases', 'does not change', 'becomes zero'])
d.q('<b>Give the scientific reason:</b> a light ray bends away from the normal when it passes from water '
    'into air.', 'Explain')
d.q('<b>What happens when</b> a light ray falls from a more optically dense medium into a less optically '
    'dense medium at an angle of incidence equal to the critical angle?', 'Explain')
d.q('Light whose speed in vacuum is c passes into two media A and B; its speed in A is 0.8 c and in B is '
    '0.6 c. <b>Calculate the critical angle</b> when light passes between the two media.', 'Problem')

# ---------------- F ----------------
d.sec('F', 'Weekly assessment', 'Group B')
d.q('A light ray falls on the boundary separating two media whose absolute refractive indices are '
    'respectively n&#8321; and n&#8322;, where n&#8321; &gt; n&#8322;. What is the correct choice that '
    'expresses the condition required for total internal reflection to occur?', 'MCQ',
    ch=['the ray must fall in the medium n&#8321; at an angle greater than the critical angle',
        'the ray must fall in the medium n&#8322; at an angle greater than the critical angle',
        'the ray must fall in the medium n&#8321; at an angle less than the critical angle',
        'the ray must fall in the medium n&#8322; at an angle less than the critical angle'])
d.q('If a light ray falls on a rectangular glass block with an angle of incidence equal to 60&deg;, and '
    'the absolute refractive index of the glass = &radic;3, then the angle of refraction of the light '
    'equals &hellip;&hellip;', 'MCQ', ch=['90&deg;', '60&deg;', '30&deg;', '45&deg;'])
d.q('<b>What happens when</b> a light ray falls from a more optically dense medium into a less optically '
    'dense medium at an angle of incidence greater than the critical angle?', 'Explain')
d.q('<b>Compare between</b> the more optically dense medium and the less optically dense medium as '
    'regards: the speed of light in it, and the absolute refractive index.', 'Explain')
d.q('<b>Give the scientific reason:</b> the reflected ray inside the water does not disappear when light '
    'passes from water into air; rather it increases in brightness as the angle of incidence increases.',
    'Explain')
d.q('A light ray passes from a material into air. If the angle of incidence is 30&deg; and the angle of '
    'refraction is 50&deg;, <b>calculate the refractive index of the material.</b>', 'Problem')

# ---------------- G ----------------
d.sec('G', 'Weekly assessment', 'Group C')
d.q('If a light ray passes from a less optically dense medium into a medium of higher optical density, '
    'then the ratio between the wavelength of the incident light and the wavelength of the refracted light '
    'is &hellip;&hellip;', 'MCQ',
    ch=['less than one', 'greater than one', 'equal to one', 'zero'])
d.q('When light passes from a more optically dense medium into a less dense medium, then the greatest '
    'value of the angle of refraction in the less dense medium is &hellip;&hellip;', 'MCQ',
    ch=['180&deg;', '90&deg;', '42&deg;', '45&deg;'])
d.q('<b>Compare between</b> the passage of light from air into water and its passage from water into air '
    'as regards: the frequency, and the wavelength.', 'Explain')
d.q('<b>Give the scientific reason:</b> the radius of the disc needed to block the light of a point source '
    'under the surface of a liquid decreases as the refractive index of that liquid increases.', 'Explain')
d.q('If the critical angle of glass with air is 42&deg;, and the critical angle of water with air is '
    '49&deg;, <b>which of them is optically denser? And why, mathematically?</b>', 'Problem')

# ---------------- solutions ----------------
_HD = ['', 'optically denser medium', 'optically less dense medium']
_RW = [['the speed of light v', 'smaller', 'larger'],
       ['the absolute index n = c/v', 'larger', 'smaller'],
       ['the wavelength &lambda;', 'shorter', 'longer'],
       ['the frequency f', 'the same', 'the same'],
       ['a ray entering it', 'bends <b>towards</b> the normal', 'bends <b>away</b> from the normal']]
_TBL = ('<table class="vt"><tr>' + ''.join('<th>' + hh + '</th>' for hh in _HD) + '</tr>' +
        ''.join('<tr>' + ''.join('<td>' + c + '</td>' for c in r) + '</tr>' for r in _RW) + '</table>')

d.page()
d.sec('✓', 'Answer key', 'Solutions — step by step')
d.hint('<b>Everything follows from n = c/v.</b> Decide first which medium is the denser one; then the '
       'speed, the wavelength and the direction of bending all follow automatically. And remember that '
       '&theta;c only exists for light trying to <b>leave</b> the denser medium.')

d.grp('Part A — Classwork 1')
d.sol(1, 'passing from medium A into medium B',
      'the figure shows the ray bending <b>towards</b> the normal in B, so B is the\n'
      'optically denser medium :\n'
      '    n(B) > n(A)        and        n = c / v      →      v(B) < v(A)\n'
      'the frequency is set by the source and cannot change at a boundary, so :\n'
      '    λ = v / f        →        λ(B) < λ(A)',
      'both the speed of light and the wavelength <b>decrease</b> in B, while the frequency stays the same',
      extra=_TBL,
      why='The three always move together: slower, shorter, bent towards the normal. The one quantity '
          'that never moves is the frequency — the boundary cannot create or destroy wave crests.')
d.sol(2, 'the definition of the absolute refractive index',
      'the absolute refractive index of a medium is the ratio of the speed of light\n'
      'in vacuum to its speed in that medium :\n'
      '    n = c / v\n'
      'it can also be written from the law of refraction, for light going from vacuum :\n'
      '    n = sin ( angle in vacuum ) / sin ( angle in the medium )\n'
      'and, since f is unchanged,    n = λ(vacuum) / λ(medium)',
      'n = c / v &nbsp;&mdash;&nbsp; a pure number, never less than 1',
      why='Because nothing travels faster than c, v is always less than or equal to c and so n &ge; 1. '
          'For air n &asymp; 1.0003, which is why air is treated as vacuum in school problems.')

d.grp('Part B — Home assignment 1')
d.sol(3, 'water into glass at 55°',
      'the relative refractive index from water to glass is :\n'
      '    n(water → glass) = sin i / sin r = 1.15\n'
      '    sin r = sin 55° / 1.15\n'
      '    sin r = 0.8192 / 1.15 = 0.7123\n'
      '    r = 45.4°   ≈  45°',
      'r &asymp; 45&deg;',
      why='The relative index is greater than 1, so the glass is the denser of the two and the ray must '
          'bend <b>towards</b> the normal — and indeed 45° is smaller than 55°. If your '
          'answer had come out bigger than 55° you would know the ratio had been used upside down.')
d.sol(4, 'denser compared with less dense',
      '    n = c / v        →        n and v always move in <b>opposite</b> directions',
      'the denser medium has the smaller speed of light and the larger refractive index',
      extra=_TBL)
d.sol(5, 'the refractive index of the glass',
      '    n = c / v\n'
      '    n = ( 3 × 10⁸ ) / ( 2 × 10⁸ )\n'
      '    n = 1.5',
      'n = 1.5',
      why='A refractive index is a ratio of two speeds, so it has no unit. 1.5 is the standard value for '
          'ordinary glass, and it makes the critical angle with air about 41.8° — a number worth '
          'remembering.')
d.sol(6, 'entering a denser medium',
      'the frequency is fixed by the source :        f unchanged\n'
      'the denser medium is the slower one :         v decreases\n'
      '    λ = v / f        →        λ decreases as well',
      'D) the frequency does not change and the wavelength decreases')
d.sol(7, 'from n = 1.3 into n = 1.5',
      '    n₂ = 1.5 > n₁ = 1.3        →  medium (2) is the denser one\n'
      '    n = c / v          →  v₂ < v₁\n'
      '    λ = v / f ( f fixed ) →  λ₂ < λ₁',
      'B) both the wavelength and the speed decrease',
      why='<b>Note on the printed question.</b> In the book the four choices are given as small diagrams '
          'rather than as sentences; they have been written out here in words, with the same meaning, so '
          'that the question can be answered from the text alone.')

d.grp('Part C — Classwork 2')
d.sol(8, 'the greatest angle of refraction',
      'going into the <b>less</b> dense medium the ray bends away from the normal, so the\n'
      'angle of refraction is always larger than the angle of incidence.\n'
      'the refracted ray can at most run along the surface itself :\n'
      '    greatest angle of refraction = 90°\n'
      'and the angle of incidence that produces it is the <b>critical angle</b> θc.',
      '90&deg; &mdash; the refracted ray grazes along the surface',
      why='Beyond that there is no refracted ray at all: every ray arriving at more than &theta;c is '
          'reflected back into the denser medium, which is total internal reflection.')
d.sol(9, 'the relation for the critical angle',
      'at the critical angle the refracted ray grazes the surface, so θ₂ = 90° :\n'
      '    n₁ sin θc = n₂ sin 90° = n₂\n'
      '    sin θc = n₂ / n₁        ( n₁ > n₂ )\n'
      'and when the second medium is air ( n₂ ≈ 1 ) :\n'
      '    sin θc = 1 / n',
      'sin &theta;c = n&#8322; / n&#8321; &nbsp;( = 1/n with air outside )')

d.grp('Part D — Home assignment 2')
d.sol(10, 'why the cladding has the smaller refractive index',
      'total internal reflection can only happen when light tries to leave the\n'
      '<b>denser</b> medium, so the core must be the denser of the two :\n'
      '    n(core) > n(cladding)\n'
      'then a critical angle exists at the core–cladding boundary, and every ray that\n'
      'strikes it at more than θc is reflected back into the core.',
      'so that a critical angle exists at the core&ndash;cladding boundary and the light is totally '
      'reflected instead of leaking out',
      why='If the cladding were the denser one there would be <b>no</b> critical angle at all, and light '
          'would escape at every bounce. The cladding also keeps the core surface clean and prevents '
          'light from leaking into a neighbouring fibre.')
d.sol(11, 'raising the angle inside a glass of water',
      'the light is going from water ( denser ) to air ( less dense ) :\n'
      '  small angles  → most of the light refracts out, bending away from the normal,\n'
      '                  and a weak reflected ray stays in the water\n'
      '  θ = θc ≈ 49° → the refracted ray grazes along the surface ( 90° ) and the\n'
      '                  reflected ray is at its brightest so far\n'
      '  θ > θc      → the refracted ray disappears completely : <b>total internal\n'
      '                  reflection</b>, all the light stays in the water',
      'the refracted ray bends further and further away until, at &theta;c, it grazes the surface and '
      'then vanishes &mdash; beyond &theta;c all the light is reflected back into the water')
d.sol(12, 'sin θc for a 1.6 / 1.4 fibre',
      '    sin θc = n₂ / n₁        ( n₁ = core , n₂ = cladding )\n'
      '    sin θc = 1.4 / 1.6\n'
      '    sin θc = 0.875        →        θc = 61°',
      'A) 1.4 / 1.6',
      why='The smaller index always goes on top — otherwise the sine would come out greater than 1, '
          'which is impossible, and that is exactly how you can spot the wrong choices (B) and (D).')
d.sol(13, 'when total internal reflection happens',
      'two conditions are needed together :\n'
      '  1  the light must be going from the <b>denser</b> medium to the less dense one\n'
      '  2  the angle of incidence must be <b>greater</b> than the critical angle',
      'B) from a medium of higher optical density into a medium of lower optical density')
d.sol(14, 'the correct path at 50° in glass',
      'find the critical angle for glass and air :\n'
      '    sin θc = 1 / n = 1 / 1.5 = 0.6667\n'
      '    θc = 41.8°\n'
      'the ray arrives at 50°, and  50° > 41.8° :\n'
      '→ no light gets out — the ray is reflected back into the glass, with the angle\n'
      '  of reflection equal to the angle of incidence.',
      'C) &mdash; the ray is totally reflected back into the glass at 50&deg;',
      why='Figures A and D would need a refracted ray to exist, which it does not above &theta;c, and B '
          'would need the two media to have the same index. <b>Note on the printed question:</b> the four '
          'choices in the book are diagrams without letters; they are drawn here as four labelled panels '
          'so that the answer can be given as a letter.')

d.grp('Part E — Weekly assessment, Group A')
d.sol(15, 'the cryolite cladding for θc = 32°',
      '    sin θc = n₂ / n₁        →        n₂ = n₁ sin θc\n'
      '    n₂ = 2.1 × sin 32°\n'
      '    n₂ = 2.1 × 0.5299\n'
      '    n₂ = 1.11',
      'A) n = 1.11',
      why='The other three choices are all <b>larger</b> than 2.1, and a cladding denser than the core '
          'would make total internal reflection impossible — so they can be rejected before any '
          'arithmetic is done.')
d.sol(16, 'a liquid of greater refractive index',
      '    sin θc = 1 / n        →  a larger n gives a <b>smaller</b> θc\n'
      '    r = h tan θc        →  a smaller θc gives a smaller r\n'
      '    area = π r²          →  and therefore a smaller area',
      'B) it decreases',
      why='The escaping light is confined to a cone of half-angle &theta;c. Making the liquid denser '
          'narrows that cone, so a smaller lid is enough to cover it.')
d.sol(17, 'why a ray bends away going from water to air',
      '    n(water) ≈ 1.33  >  n(air) ≈ 1\n'
      '    n = c / v        →        v(air) > v(water)\n'
      'the light speeds up as it enters the air. from  n₁ sin θ₁ = n₂ sin θ₂ :\n'
      '    sin θ₂ = ( n₁ / n₂ ) sin θ₁ > sin θ₁        →        θ₂ > θ₁',
      'because air is the optically less dense medium, so the light travels faster in it and the ray '
      'turns away from the normal',
      why='A picture that helps: think of the wavefront as a line of marchers. The end that reaches the '
          'faster medium first pulls ahead, and the whole line swings round — away from the normal '
          'when the new medium is the faster one.')
d.sol(18, 'incidence exactly at the critical angle',
      '    n₁ sin θc = n₂ sin θ₂        with  θ₂ = 90°\n'
      'the refracted ray leaves along the surface itself, at 90° to the normal, and is\n'
      'extremely faint; at the same time the reflected ray inside the denser medium is\n'
      'at its brightest so far.',
      'the refracted ray grazes along the surface at 90&deg; &mdash; the borderline case just before total '
      'internal reflection')
d.sol(19, 'the critical angle between A and B',
      '    n = c / v :\n'
      '        n(A) = c / 0.8c = 1.25\n'
      '        n(B) = c / 0.6c = 1.667\n'
      'B is the denser one, so the light must be going from B into A :\n'
      '    sin θc = n(A) / n(B) = 1.25 / 1.667\n'
      '    sin θc = 0.75\n'
      '    θc = 48.6°',
      '&theta;c &asymp; 48.6&deg;',
      why='Notice the short cut: sin &theta;c = n(A)/n(B) = v(B)/v(A) = 0.6c/0.8c = 0.75, so the speeds '
          'can be used directly without working out either index.')

d.grp('Part F — Weekly assessment, Group B')
d.sol(20, 'the condition for total internal reflection',
      'the light must start in the <b>denser</b> medium, which is n₁ here, and must\n'
      'arrive at the boundary at more than the critical angle :\n'
      '    the ray is in n₁   and   θ > θc',
      'A) the ray must fall in the medium n&#8321; at an angle greater than the critical angle',
      why='Choices (B) and (D) put the ray in the <b>less</b> dense medium, where no critical angle even '
          'exists; choice (C) has the inequality the wrong way round, and would simply give ordinary '
          'refraction.')
d.sol(21, 'refraction into glass of n = √3 at 60°',
      '    n = sin i / sin r        →        sin r = sin i / n\n'
      '    sin r = sin 60° / √3 = 0.8660 / 1.7321\n'
      '    sin r = 0.5\n'
      '    r = 30°',
      'C) 30&deg;',
      why='Choice (A), 90°, is impossible for light <b>entering</b> a denser medium, and (B) would '
          'mean no bending at all. The ray must bend towards the normal, so the answer has to be less '
          'than 60°.')
d.sol(22, 'incidence greater than the critical angle',
      'above θc the law of refraction would need  sin θ₂ > 1 , which is impossible,\n'
      'so no refracted ray can exist :\n'
      '→ all the light is reflected back into the denser medium, obeying the ordinary\n'
      '  law of reflection ( angle of reflection = angle of incidence ).',
      'total internal reflection takes place &mdash; 100 % of the light is reflected back inside the '
      'denser medium',
      why='This is the only kind of reflection that is complete. An ordinary mirror always absorbs a few '
          'per cent, which is why optical fibres and reflecting prisms in binoculars use total internal '
          'reflection instead of mirrors.')
d.sol(23, 'denser compared with less dense, again',
      '    n = c / v        →        larger n  ↔  smaller v',
      'the denser medium: smaller v, larger n. the less dense medium: larger v, smaller n',
      extra=_TBL)
d.sol(24, 'why the internally reflected ray gets brighter',
      'at every boundary the light divides into a refracted part and a reflected part.\n'
      'as θ grows towards θc, less and less energy goes into the refracted ray, so more\n'
      'and more is left for the reflected one. at θ = θc the refracted ray vanishes and\n'
      'beyond it <b>all</b> the energy is reflected.',
      'because the share of the energy taken by the refracted ray falls as the angle grows, so the share '
      'left for the reflected ray rises &mdash; reaching 100 % at and beyond &theta;c',
      why='So the reflected ray was always there; it is simply too faint to notice at small angles. This '
          'is the same effect that makes a lake look transparent when you look straight down and like a '
          'mirror when you look across it at a glancing angle.')
d.sol(25, 'the index from 30° inside to 50° in air',
      'the light goes from the material into air :\n'
      '    n sin i = n(air) sin r = 1 × sin r\n'
      '    n × sin 30° = sin 50°\n'
      '    n × 0.5 = 0.7660\n'
      '    n = 1.53',
      'n &asymp; 1.53',
      why='The ray bent away from the normal ( 30° → 50° ), so the material must be the '
          'denser one and n must come out greater than 1 — a quick check that the fraction was not '
          'written upside down.')

d.grp('Part G — Weekly assessment, Group C')
d.sol(26, 'the ratio of the two wavelengths',
      'going into a denser medium the light slows down, so the wavelength shortens :\n'
      '    λ(incident) / λ(refracted) = v₁ / v₂ = n₂ / n₁\n'
      'and n₂ > n₁ , so the ratio is <b>greater than one</b>.',
      'B) greater than one')
d.sol(27, 'the greatest angle of refraction',
      'the refracted ray bends away from the normal and can at most lie along the\n'
      'surface itself :\n'
      '    greatest angle of refraction = 90°',
      'B) 90&deg;',
      why='Choice (C), 42°, is the critical angle of glass with air — an angle of '
          '<b>incidence</b>, not of refraction. It is put there to catch anyone answering from memory.')
d.sol(28, 'air to water compared with water to air',
      'the frequency is fixed by the source in both directions :\n'
      '    f is the same going either way\n'
      'the wavelength follows the speed :\n'
      '    air → water :  v decreases  →  λ decreases , ray bends towards the normal\n'
      '    water → air :  v increases  →  λ increases , ray bends away from the normal',
      'the frequency is unchanged in both cases; the wavelength decreases going into the water and '
      'increases coming out of it',
      why='<b>Note on the printed questions.</b> This exact comparison appears twice in Group C of the '
          'book (as questions 3 and 5, word for word); the two have been merged into this single item.')
d.sol(29, 'why a denser liquid needs a smaller disc',
      '    sin θc = 1 / n        →  n larger  →  θc smaller\n'
      '    r = h tan θc        →  θc smaller  →  r smaller',
      'because a larger n gives a smaller critical angle, which narrows the cone of escaping light, so a '
      'smaller disc covers it',
      why='Worth seeing with numbers: for water ( n = 1.33 ) &theta;c = 48.8° and r = 1.14 h, while '
          'for a liquid with n = 1.6 &theta;c = 38.7° and r = 0.80 h — the disc is about 30 % '
          'smaller in radius and only half the area.')
d.sol(30, 'glass with θc = 42° against water with θc = 49°',
      '    sin θc = 1 / n        →        n = 1 / sin θc\n'
      '    glass :  n = 1 / sin 42° = 1 / 0.6691 = 1.49\n'
      '    water :  n = 1 / sin 49° = 1 / 0.7547 = 1.33\n'
      '    1.49 > 1.33        →        the glass is the denser one',
      'the glass is optically denser, because n = 1/sin&theta;c and the smaller critical angle gives the '
      'larger refractive index',
      why='The rule to carry away: <b>the smaller the critical angle, the denser the medium</b>. A '
          'diamond, with n = 2.42, has a critical angle of only 24°, which is why so much light is '
          'trapped inside it and why it sparkles as it does.')

d.foot('Lesson 2&ndash;9 &middot; Refraction and Total Internal Reflection &middot; Mr. Gemy',
       'n = c/v &nbsp;&middot;&nbsp; sin &theta;c = n&#8322;/n&#8321;')
d.save('l29.html')
print('l29.html written -', d.n, 'questions')

# -*- coding: utf-8 -*-
import figs_l30 as F
from docbase import Doc

d = Doc('Unit 2 &middot; Lessons 2&ndash;10 and 2&ndash;11',
        'Lenses and Images<br>Young&rsquo;s Double-Slit Experiment',
        'Converging and diverging lenses, the lens equation and magnification, and the interference '
        'of light through two narrow slits.',
        ['Grade 11 &middot; Egyptian Baccalaureate', '31 questions', 'Step-by-step solutions',
         '&Delta;y = &lambda;L / d'],
        'Lenses and Young&rsquo;s Double-Slit Experiment')

d.kit('The toolkit for these two lessons', [
    ('1 / f = 1 / a + 1 / b', 'the lens equation, a = object distance'),
    ('M = b / a = h&rsquo; / h', 'the linear magnification'),
    ('b &gt; 0 &rarr; real, inverted', 'b &lt; 0 &rarr; virtual, erect'),
    ('f &gt; 0 convex &nbsp;&middot;&nbsp; f &lt; 0 concave', 'the sign of the focal length'),
    ('&Delta;y = &lambda; L / d', 'the fringe separation in Young&rsquo;s experiment'),
    ('&Delta; = m&lambda; &rarr; bright', '&Delta; = ( m + &frac12; )&lambda; &rarr; dark'),
])
d.hint('<b>Two lessons, two pictures.</b> A lens bends <b>one</b> beam so that it meets again at an image '
       '&mdash; everything there comes out of 1/f = 1/a + 1/b. Young&rsquo;s experiment splits '
       '<b>one</b> beam into two and lets them meet again as fringes &mdash; everything there comes out '
       'of the path difference. Keep the two pictures apart and the whole unit becomes easy.')

# ---------------- A ----------------
d.sec('A', 'Classwork &nbsp;1', 'Lesson 2&ndash;10 &middot; the parts of a lens')
d.q('<b>What is the name of the lens</b> that is thicker at its centre than at its edges?', 'Explain')
d.q('The point at which rays parallel to the principal axis collect after being refracted by a convex '
    'lens is called:', 'MCQ',
    ch=['the optical centre', 'the principal focus', 'the centre of curvature', 'the pole of the lens'])
d.q('The straight line that passes through the optical centre of the lens and is perpendicular to its '
    'plane is known as:', 'MCQ',
    ch=['the focal length', 'the principal axis', 'the radius', 'the incident ray'])

# ---------------- B ----------------
d.sec('B', 'Home assignment &nbsp;1', 'Lesson 2&ndash;10 &middot; images formed by lenses')
d.q('Using the ray diagram opposite, <b>explain why the image formed by a concave lens is always '
    'virtual, erect and diminished.</b>', 'Explain',
    F.concave_lens('Figure 1 &middot; a diverging (concave) lens'))
d.q('<b>Draw the path of the rays</b> for a magnifying (convex) lens used to look at an object placed at '
    'a small distance from it (inside the focal length), showing the ray that passes through the optical '
    'centre, the ray parallel to the principal axis, and how their extensions meet.', 'Explain',
    F.magnifier('Figure 2 &middot; a convex lens used as a magnifier'))
d.q('An object is placed at a distance <b>a</b> from a convex lens and a virtual image is formed. The '
    'lens is then replaced by a concave lens having the <b>same focal length (f)</b>, without moving the '
    'object, and another virtual image is formed. If the distance between the position of the first image '
    'and the position of the second image equals the focal length f, <b>find the object distance a in '
    'terms of f.</b>', 'Problem')
d.q('If an object is placed at a distance much greater than twice the focal length (2F) of a convex lens, '
    'the image formed for it is:', 'MCQ',
    F.convex_far('Figure 3 &middot; an object beyond 2F'),
    ch=['real, inverted, diminished', 'real, inverted, magnified',
        'virtual, erect, diminished', 'real, inverted, equal to the object'])
d.q('If the magnification ( M = 0.5 ), this means that the image is:', 'MCQ',
    ch=['magnified to twice the object', 'equal to the object',
        'diminished to half the object', 'always inverted'])

# ---------------- C ----------------
d.page()
d.sec('C', 'Classwork &nbsp;2', 'Lesson 2&ndash;11 &middot; Young&rsquo;s experiment')
d.q('The figure opposite shows Young&rsquo;s double-slit experiment. If the distance between two '
    'successive bright fringes is <b>5 mm</b>, <b>calculate the wavelength of the light used.</b>',
    'Problem',
    F.young_setup('Figure 4 &middot; the double-slit arrangement',
                  'd = 0.3 mm', 'L = 3 m', '&Delta;y = 5 mm'))
d.q('The wavelength &lambda; of any monochromatic light in Thomas Young&rsquo;s double-slit experiment is '
    'determined from the relation &hellip;&hellip; &nbsp;(R is the distance from the double slit to the '
    'screen)', 'MCQ',
    ch=['&lambda; = &Delta;y R / d', 'R = &Delta;y d / &lambda;',
        '&Delta;y = &lambda; d / R', 'd = &lambda; &Delta;y / R'])
d.q('A monochromatic ray falls in Thomas Young&rsquo;s experiment and the distance between the two '
    'openings of the double slit is d&#8321;. The double slit is then replaced by another one whose slit '
    'separation is <b>half</b> the first. The distance between two successive fringes of the same kind '
    'in the second case is:', 'MCQ',
    ch=['&Delta;y&#8321; / 2 = &Delta;y&#8322;', '&Delta;y&#8321; = &Delta;y&#8322;',
        '4 &Delta;y&#8321; = &Delta;y&#8322;', '2 &Delta;y&#8321; = &Delta;y&#8322;'])

# ---------------- D ----------------
d.sec('D', 'Home assignment &nbsp;2', 'Lesson 2&ndash;11 &middot; fringes and their separation')
d.q('Monochromatic light of wavelength 450 nm passes through two parallel slits separated by 0.3 mm, and '
    'the bright fringes can be observed on a screen 2 m away. <b>Calculate, in millimetres, the distance '
    'between two successive fringes of the same kind.</b>', 'Problem',
    F.young_setup('Figure 5 &middot; not to scale', 'd = 0.30 mm', 'L = 2.0 m', '&Delta;y = ?'))
d.q('From the figure opposite, which represents Young&rsquo;s double-slit experiment: with both slits '
    'open, <b>will two bright patches appear on the wall</b> &mdash; one for each slit &mdash; <b>or a '
    'row of many bright fringes? And where is the brightest one?</b>', 'Explain',
    F.young_setup('Figure 6 &middot; both slits open'))
d.q('Monochromatic light of wavelength 600 nm was used in Young&rsquo;s experiment, and interference '
    'fringes were formed on a screen 1.2 m away. If the separation between successive bright fringes is '
    '2.4 mm, <b>calculate the distance (d) between the two slits.</b>', 'Problem')
d.q('Which of the following methods can increase the distance between the interference fringes in '
    'Young&rsquo;s double-slit experiment, using a green monochromatic light source?', 'MCQ',
    ch=['decreasing the distance between the screen that receives the fringes and the two narrow slits',
        'increasing the distance between the source and the two narrow slits',
        'increasing the separating distance between the two narrow slits',
        'replacing the light source with a red monochromatic light source'])
d.q('In Thomas Young&rsquo;s experiment, when the distance between the double-slit screen and the screen '
    'prepared to receive the fringes is doubled, then the distance between every two successive fringes '
    'of the same kind &hellip;&hellip;', 'MCQ',
    ch=['doubles and the clarity of the fringes decreases',
        'doubles and the clarity of the fringes increases',
        'halves and the clarity of the fringes increases',
        'halves and the clarity of the fringes decreases'])

# ---------------- E ----------------
d.page()
d.sec('E', 'Review', 'Group A')
d.q('A convex lens whose focal length is 10 cm; an object is placed at a distance of 15 cm from it. The '
    'image formed is:', 'MCQ',
    ch=['virtual, magnified', 'real, magnified', 'real, diminished', 'real, equal to the object'])
_TB17 = ('<table class="vt"><tr><th></th><th>the wavelength</th>'
         '<th>the distance between the two<br>coherent sources</th>'
         '<th>the distance of the screen<br>from the double slit</th></tr>'
         '<tr><td><b>A</b></td><td>500 nm</td><td>2 d</td><td>0.5 m</td></tr>'
         '<tr><td><b>B</b></td><td>400 nm</td><td>d</td><td>1 m</td></tr>'
         '<tr><td><b>C</b></td><td>600 nm</td><td>3 d</td><td>1.5 m</td></tr>'
         '<tr><td><b>D</b></td><td>450 nm</td><td>0.5 d</td><td>1.1 m</td></tr></table>')
d.q('Four students were allowed to choose among several sources of different wavelength, several double '
    'slits, and a suitable screen distance, in order to carry out the double-slit experiment. '
    '<b>For which student will the fringes be the clearest (the most widely separated)?</b>', 'MCQ',
    _TB17, ch=['choice A', 'choice B', 'choice C', 'choice D'])
d.q('A student carries out an experiment to demonstrate the interference of light using the double-slit '
    'experiment as in the figure, but he found that the interference fringes observed on the screen are '
    'so close together that they cannot be told apart. <b>What changes could help the student to '
    'distinguish between the fringes? (two are enough)</b>', 'Explain',
    F.young_setup('Figure 7 &middot; the fringes are too close together'))
d.q('An object of length h is placed between a screen and a convex lens. When the position of the lens is '
    'changed, it is found that there are two positions that give a clear image on the screen. If the '
    'magnification at the first position is M&#8321; = 4 and the magnification at the second position is '
    'M&#8322; = 0.25, <b>calculate the length of the first image and of the second image.</b>', 'Problem')
d.q('<b>How can you increase the distance between the interference fringes</b> in Young&rsquo;s '
    'double-slit experiment, using a green monochromatic light source?', 'Explain')

# ---------------- F ----------------
d.sec('F', 'Review', 'Group B')
d.q('An image is formed on a wall by a lens. If the distance between the lens and the wall is 30 cm and '
    'the magnification is M = 2, then <b>the type of the lens and the object distance</b> are:', 'MCQ',
    ch=['concave, a = 15 cm', 'convex, a = 60 cm', 'convex, a = 15 cm', 'concave, a = 60 cm'])
d.q('In an experiment on the interference of light by Young, the distance between the two narrow slits is '
    '0.2 mm, the wavelength of the monochromatic light used is 600 nm, and the distance between the two '
    'narrow slits and the screen prepared to receive the fringes is 1 m. Then the distance between two '
    'successive fringes of the same kind equals &hellip;&hellip;', 'MCQ',
    ch=['3 mm', '6 mm', '30 mm', '1 m'])
d.q('A convex lens gives, for an object placed in front of it, an erect image magnified 4 times. The '
    'object is then moved away from the lens through a distance of 6 cm, and the image becomes real, '
    'inverted and magnified 4 times as well. <b>Calculate the focal length of the lens.</b>', 'Problem')
d.q('A screen is placed at a distance of 90 cm from an object, and a convex lens of focal length 20 cm '
    'moves between the object and the screen. <b>Find all the values of the distance a between the lens '
    'and the object at which a clear image is formed on the screen.</b>', 'Problem',
    F.lens_screen('Figure 8 &middot; the lens slides between object and screen'))
d.q('The drawing opposite shows the paths of two waves from the two slits S&#8321; and S&#8322; meeting at '
    'a point P. If the wavelength is &lambda; and the distance S&#8322;P exceeds S&#8321;P by 1.5 '
    '&lambda;, <b>what type of fringe is formed at the point P? And why?</b>', 'Explain',
    F.young_paths('Figure 9 &middot; the two paths to the point P'))

# ---------------- G ----------------
d.sec('G', 'Review', 'Group C')
d.q('When red light is used instead of blue light in Young&rsquo;s experiment, the distance between the '
    'fringes:', 'MCQ',
    ch=['increases, because the wavelength of red is larger',
        'decreases, because the wavelength of red is smaller',
        'does not change', 'the fringes disappear'])
d.q('A concave lens whose focal length is 20 cm; an object is placed at a distance of 20 cm from it. The '
    'image is:', 'MCQ',
    ch=['at infinity', 'virtual, erect, diminished',
        'real, equal to the object', 'virtual, magnified'])
d.q('In the double-slit experiment, monochromatic light of wavelength 6000 &Aring; was used and fringes '
    'were formed on a screen at a distance (R) from the double slit, the distance between every two '
    'successive bright fringes being &Delta;y&#8321;. If monochromatic light of wavelength 4000 &Aring; '
    'is then used and the distance between the double slit and the screen is doubled, the distance '
    'between every two successive bright fringes becoming &Delta;y&#8322;, <b>find the ratio '
    '&Delta;y&#8321; / &Delta;y&#8322;.</b>', 'Problem')
d.q('An object is placed beyond 2F of a convex lens, then it moves with a uniform velocity v towards the '
    'focus F. <b>Prove that the speed of the image formed is variable, and that it increases as the '
    'object approaches the focus.</b>', 'Problem')
d.q('<b>Give the scientific reason:</b> the central fringe in Young&rsquo;s double-slit experiment is '
    'always a bright fringe.', 'Explain')

# ---------------- solutions ----------------
_LT = ('<table class="vt"><tr><th>position of the object</th><th>position of the image</th>'
       '<th>nature of the image</th></tr>'
       '<tr><td>beyond 2F</td><td>between F and 2F</td><td>real, inverted, diminished</td></tr>'
       '<tr><td>at 2F</td><td>at 2F</td><td>real, inverted, equal</td></tr>'
       '<tr><td>between F and 2F</td><td>beyond 2F</td><td>real, inverted, magnified</td></tr>'
       '<tr><td>at F</td><td>at infinity</td><td>no image is formed</td></tr>'
       '<tr><td>inside F</td><td>same side as the object</td><td>virtual, erect, magnified</td></tr>'
       '</table>')

d.page()
d.sec('&#10003;', 'Answer key', 'Solutions &mdash; step by step')
d.hint('<b>Two equations run this whole handout.</b> For every lens question write '
       '1/f = 1/a + 1/b and M = b/a, put f negative for a concave lens and b negative for a virtual '
       'image, and the algebra does the rest. For every Young question write &Delta;y = &lambda;L/d and '
       'ask only which of the three letters on the right has changed.')

d.grp('Part A — Classwork 1')
d.sol(1, 'the lens that is thicker at the centre',
      'a lens that is thicker at its centre than at its edges is the\n'
      '    convex  ( converging )  lens\n'
      'parallel rays that strike it are bent inwards and really meet at a point,\n'
      'so its principal focus is a real focus and its focal length is positive.',
      'the <b>convex</b> (converging) lens',
      why='The mirror image of this rule is just as useful: a lens that is <b>thinner</b> at its centre '
          'than at its edges is the concave (diverging) lens, its rays spread apart, its focus is '
          'virtual and its focal length is taken as negative.')
d.sol(2, 'where parallel rays collect',
      'rays parallel to the principal axis are refracted by a convex lens and meet\n'
      'at one point on the axis ; that point is the  principal focus  ( F ).\n'
      'the distance from the optical centre to F is the focal length  f.',
      'choice <b>B</b> &mdash; the principal focus',
      why='Do not confuse the three points on the axis. The <b>optical centre</b> is the middle of the '
          'lens itself and a ray through it goes straight on; the <b>centre of curvature</b> is the '
          'centre of the sphere the surface was cut from; the <b>principal focus</b> is where the '
          'parallel rays actually gather.')
d.sol(3, 'the line through the optical centre',
      'the straight line through the optical centre, perpendicular to the plane of\n'
      'the lens, is the  principal axis.\n'
      'it is the reference line from which every distance ( a , b , f , 2f ) is measured.',
      'choice <b>B</b> &mdash; the principal axis',
      why='<b>Note on the printed lesson.</b> In the book the questions of this classwork are numbered '
          '1, 3, 4 &mdash; number 2 is missing from the printed page. Nothing is lost; the numbering '
          'here has simply been made continuous.')

d.grp('Part B — Home assignment 1')
d.sol(4, 'why a concave lens always gives a virtual, erect, diminished image',
      'take the two standard rays from the top of the object :\n'
      '  ray 1 : parallel to the axis, then refracted so that it seems to come from\n'
      '          the principal focus F on the  same  side as the object.\n'
      '  ray 2 : straight through the optical centre, undeviated.\n'
      'after the lens the two rays  diverge , so they can never really cross :\n'
      '    → only their backward extensions meet   →   the image is  VIRTUAL\n'
      'both extensions meet  above  the axis, on the same side as the object :\n'
      '    → the image is  ERECT\n'
      'algebraically, with f negative and a positive :\n'
      '    1/b = − 1/f − 1/a        →        b = − a f / ( a + f )\n'
      '    M = | b | / a = f / ( a + f )   <  1     for every positive a\n'
      '    → the image is  DIMINISHED , and it always lies between F and the lens',
      'always virtual, erect and diminished &mdash; whatever the object distance',
      why='The last line is the real proof: f/(a+f) is a fraction whose denominator is bigger than its '
          'numerator for <b>any</b> positive a, so M can never reach 1. This is exactly why a diverging '
          'lens is used in spectacles for short sight, and in a door viewer &mdash; it shrinks a wide '
          'scene into a small erect picture.')
d.sol(5, 'the ray diagram of the magnifying glass',
      'the object is placed  inside  the focal length :     a < f\n'
      '  ray 1 : parallel to the axis, then refracted through the far focus F′.\n'
      '  ray 2 : straight through the optical centre O.\n'
      'after the lens the two refracted rays are still  diverging , so they are\n'
      'traced  backwards  ( dashed ) until their extensions meet.\n'
      '    1/b = 1/f − 1/a ,   and   a < f    →    b is negative\n'
      '    b = − a f / ( f − a )            M = f / ( f − a )  >  1',
      'the extensions meet on the object side &rarr; a <b>virtual, erect, magnified</b> image',
      extra=_LT,
      why='The closer the object creeps towards F, the smaller ( f &minus; a ) becomes and the larger M '
          'grows &mdash; which is exactly what you feel when you slide a magnifying glass until the print '
          'suddenly leaps in size just before it blurs.')
d.sol(6, 'the two virtual images a focal length apart',
      'convex lens, virtual image ( so a < f ) :\n'
      '    1/b₁ = 1/f − 1/a = ( a − f ) / ( a f )\n'
      '    | b₁ | = a f / ( f − a )          on the object side\n'
      'concave lens of the same f  ( f is negative ) :\n'
      '    1/b₂ = − 1/f − 1/a = − ( a + f ) / ( a f )\n'
      '    | b₂ | = a f / ( a + f )          also on the object side\n'
      'both images lie on the same side, so the distance between them is\n'
      '    | b₁ | − | b₂ | = a f / ( f − a ) − a f / ( a + f )\n'
      '                    = a f [ ( a + f ) − ( f − a ) ] / ( f − a )( f + a )\n'
      '                    = 2 a² f / ( f² − a² )\n'
      'this distance is given equal to f :\n'
      '    2 a² f / ( f² − a² ) = f\n'
      '    2 a² = f² − a²\n'
      '    3 a² = f²\n'
      '    a = f / √3 = ( √3 / 3 ) f ≈ 0.58 f',
      'a = f / &radic;3 &asymp; 0.58 f',
      why='The answer had to come out smaller than f, and it does &mdash; a convex lens can only make a '
          'virtual image when the object is inside the focus. Notice also that the convex image is the '
          'farther of the two: a f/(f&minus;a) is always bigger than a f/(a+f), which is why the '
          'subtraction was taken in that order.')
d.sol(7, 'an object far beyond 2F',
      '    1/b = 1/f − 1/a ,        with  a  very large\n'
      '    1/a → very small      →      b → f\n'
      'so the image settles just outside the focus, between F and 2F :\n'
      '    M = b / a ≈ f / a   ≪  1\n'
      'b is positive → the image is real and inverted',
      'choice <b>A</b> &mdash; real, inverted and diminished',
      extra=_LT,
      why='This is the camera and the eye. A very distant object throws its image practically <b>at</b> '
          'the focus, tiny and upside down &mdash; which is why the sensor of a camera sits one focal '
          'length behind the lens when you photograph a far-away mountain.')
d.sol(8, 'the meaning of M = 0.5',
      '    M = h′ / h = 0.5        →        h′ = 0.5 h\n'
      'the image height is half the object height.',
      'choice <b>C</b> &mdash; the image is diminished to half the object',
      why='M answers only one question: <b>how big</b>. Whether the image is erect or inverted is carried '
          'by the <b>sign</b>, and the printed M = 0.5 carries no sign, so nothing at all can be said '
          'here about the orientation &mdash; which is why choice D is wrong.')

d.grp('Part C — Classwork 2')
d.sol(9, 'the wavelength from the fringe separation',
      'from the figure :    d = 0.3 mm = 0.3 × 10⁻³ m ,    L = 3 m\n'
      'given :              Δy = 5 mm = 5 × 10⁻³ m\n'
      '    Δy = λ L / d        →        λ = Δy · d / L\n'
      '    λ = ( 5 × 10⁻³ × 0.3 × 10⁻³ ) / 3\n'
      '    λ = ( 1.5 × 10⁻⁶ ) / 3\n'
      '    λ = 5 × 10⁻⁷ m  =  500 nm',
      '&lambda; = 5 &times; 10<sup>&minus;7</sup> m = 500 nm &nbsp;(green light)',
      why='A sanity check you should always make: visible light runs from about 400 nm (violet) to about '
          '700 nm (red). An answer of 500 nm sits comfortably in the middle, in the green. If a '
          'double-slit calculation ever hands you microns or nanometres by the thousand, a power of ten '
          'has slipped.')
d.sol(10, 'which relation gives λ',
      'the fringe separation in Young’s experiment is\n'
      '    Δy = λ R / d\n'
      'rearranged, the three correct forms are\n'
      '    λ = Δy · d / R          R = Δy · d / λ          d = λ R / Δy\n'
      'testing the four printed choices :\n'
      '    A)  λ = Δy R / d     ✗   ( R and d are interchanged )\n'
      '    B)  R = Δy d / λ     ✓\n'
      '    C)  Δy = λ d / R     ✗   ( d and R are interchanged )\n'
      '    D)  d = λ Δy / R     ✗   ( Δy and R are interchanged )',
      'choice <b>B</b> &mdash; it is the only algebraically correct relation of the four',
      why='<b>Note on the printed question.</b> The wording asks for the relation that gives &lambda;, '
          'which points at choice A &mdash; but A has R and d the wrong way round and is wrong. The only '
          'sound statement among the four is B. Keep the master form &Delta;y = &lambda;R/d in your head '
          'and read the others off it: &lambda; and R are always <b>upstairs</b> together, d is always '
          '<b>downstairs</b>.')
d.sol(11, 'halving the slit separation',
      '    Δy = λ R / d        →        Δy  ∝  1 / d       ( λ and R unchanged )\n'
      '    d₂ = d₁ / 2\n'
      '    Δy₂ / Δy₁ = d₁ / d₂ = d₁ / ( d₁ / 2 ) = 2\n'
      '    Δy₂ = 2 Δy₁',
      'choice <b>D</b> &mdash; 2 &Delta;y&#8321; = &Delta;y&#8322;, the fringes spread to twice their '
      'separation',
      why='Inverse proportion is the trap here. Squeezing the two slits <b>closer</b> pushes the fringes '
          '<b>farther</b> apart &mdash; the same reason a very narrow gap spreads a wave over a wide '
          'angle. Everything that makes the geometry tighter makes the pattern wider.')

d.grp('Part D — Home assignment 2')
d.sol(12, 'the fringe separation for 450 nm',
      '    λ = 450 nm = 450 × 10⁻⁹ m = 4.5 × 10⁻⁷ m\n'
      '    d = 0.3 mm = 3 × 10⁻⁴ m ,        L = 2.0 m\n'
      '    Δy = λ L / d\n'
      '    Δy = ( 4.5 × 10⁻⁷ × 2.0 ) / ( 3 × 10⁻⁴ )\n'
      '    Δy = ( 9 × 10⁻⁷ ) / ( 3 × 10⁻⁴ )\n'
      '    Δy = 3 × 10⁻³ m  =  3 mm',
      '&Delta;y = 3 mm',
      why='Three millimetres between fringes on a screen two metres away is typical for a school set-up, '
          'and it is why the slits have to be a fraction of a millimetre apart. Open them to a '
          'millimetre and &Delta;y drops to under a millimetre &mdash; the pattern becomes a blur.')
d.sol(13, 'two patches, or a row of fringes?',
      'each slit is narrow enough to  diffract  the light, so the two beams spread\n'
      'out and  overlap  on the wall ; being cut from one wavefront they are\n'
      'coherent  ( a constant phase difference ).\n'
      'wherever the path difference is        Δ = m λ        → constructive → bright\n'
      'wherever the path difference is  Δ = ( m + ½ ) λ      → destructive → dark\n'
      'these conditions repeat right across the wall, so the result is a  row  of\n'
      'many bright and dark fringes, not two separate patches.\n'
      'at the centre  ( point O )     S₁O = S₂O     →     Δ = 0     → always bright',
      'a <b>row of many bright fringes</b> separated by dark ones, and the <b>brightest is the central '
      'fringe</b> opposite the midpoint between the two slits',
      why='Two patches is what you would get from two <b>independent</b> lamps, because their phase '
          'difference would change millions of times a second and the fringes would wash out. The whole '
          'point of Young&rsquo;s single source lighting both slits is to make the two beams coherent.')
d.sol(14, 'finding the slit separation',
      '    λ = 600 nm = 6 × 10⁻⁷ m ,     L = 1.2 m ,     Δy = 2.4 mm = 2.4 × 10⁻³ m\n'
      '    Δy = λ L / d        →        d = λ L / Δy\n'
      '    d = ( 6 × 10⁻⁷ × 1.2 ) / ( 2.4 × 10⁻³ )\n'
      '    d = ( 7.2 × 10⁻⁷ ) / ( 2.4 × 10⁻³ )\n'
      '    d = 3 × 10⁻⁴ m  =  0.3 mm',
      'd = 3 &times; 10<sup>&minus;4</sup> m = 0.3 mm',
      why='Notice how small d has to be. The slit separation comes out about 500 wavelengths &mdash; and '
          'that is exactly why Young&rsquo;s experiment had to wait for careful ruling: any wider and the '
          'fringes crowd into an unreadable band.')
d.sol(15, 'how to widen the fringes',
      '    Δy = λ L / d\n'
      'to make Δy bigger :   increase λ ,   increase L ,   or  decrease d.\n'
      'checking the printed choices :\n'
      '    A)  decrease L              → Δy decreases        ✗\n'
      '    B)  source-to-slit distance does not appear in the law   ✗\n'
      '    C)  increase d              → Δy decreases        ✗\n'
      '    D)  green → red , λ larger  → Δy increases        ✓',
      'choice <b>D</b> &mdash; replace the green source by a red one',
      why='Red is the long-wavelength end of the visible spectrum (&asymp; 700 nm against &asymp; 530 nm '
          'for green), so simply swapping the colour stretches the pattern by about a third. Choice B is '
          'the distractor worth naming: the distance from the lamp to the slits changes the '
          '<b>brightness</b>, never the fringe spacing.')
d.sol(16, 'doubling the screen distance',
      '    Δy = λ L / d        →        Δy  ∝  L\n'
      '    L₂ = 2 L₁        →        Δy₂ = 2 Δy₁\n'
      'but the same amount of light is now spread over twice the area, so each\n'
      'fringe is fainter and its edges are less sharp :\n'
      '    → the separation doubles , the clarity ( contrast ) decreases',
      'choice <b>A</b> &mdash; the separation doubles and the clarity of the fringes decreases',
      why='This is the trade-off every experimenter meets: you can always spread a pattern out, but you '
          'pay for the space with brightness. Doubling L spreads the same energy over four times the '
          'area, so the fringes are about four times dimmer.')

d.grp('Part E — Review, Group A')
d.sol(17, 'convex lens, f = 10 cm, a = 15 cm',
      '    1/f = 1/a + 1/b\n'
      '    1/b = 1/10 − 1/15 = ( 3 − 2 ) / 30 = 1 / 30\n'
      '    b = + 30 cm        ( positive → real, on the far side )\n'
      '    M = b / a = 30 / 15 = 2        ( magnified )',
      'choice <b>B</b> &mdash; a real, magnified (and inverted) image, 30 cm from the lens',
      extra=_LT,
      why='Read the position first and the answer follows without any arithmetic: f = 10 so 2F = 20, and '
          'the object at 15 cm sits <b>between F and 2F</b> &mdash; the one region that always gives a '
          'real, inverted, magnified image. This is the projector setting.')
d.sol(18, 'which student gets the clearest fringes',
      'the fringes are easiest to tell apart when Δy = λ L / d is  largest.\n'
      'taking d as the common unit :\n'
      '    A)  Δy = 500 × 10⁻⁹ × 0.5 / ( 2 d )   = 1.25 × 10⁻⁷ / d\n'
      '    B)  Δy = 400 × 10⁻⁹ × 1.0 / ( 1 d )   = 4.00 × 10⁻⁷ / d\n'
      '    C)  Δy = 600 × 10⁻⁹ × 1.5 / ( 3 d )   = 3.00 × 10⁻⁷ / d\n'
      '    D)  Δy = 450 × 10⁻⁹ × 1.1 / ( 0.5 d ) = 9.90 × 10⁻⁷ / d     ← the largest',
      'choice <b>D</b> &nbsp;&mdash;&nbsp; 450 nm, 0.5 d, 1.1 m gives about 2.5 times the fringe '
      'separation of choice B',
      why='Do not be tempted by the longest wavelength alone. Choice C has the reddest light of the four '
          'and still loses, because its slits are six times farther apart than D&rsquo;s. In &lambda;L/d '
          'all three letters vote, and here the small d carries the day.')
d.sol(19, 'the fringes are too close together',
      '    Δy = λ L / d\n'
      'so Δy can be made larger by\n'
      '  1. moving the screen  farther  from the double slit  ( increase L ) ,\n'
      '  2. using a double slit whose two openings are  closer  ( decrease d ) ,\n'
      '  3. using light of a  longer  wavelength — swap the red filter for nothing\n'
      '     less than red, i.e. use the reddest source available ( increase λ ).',
      'any <b>two</b> of: increase the slit&ndash;screen distance L, use a double slit with a smaller '
      'separation d, or use light of a longer wavelength &lambda;',
      why='The figure shows a red filter already in place, so the wavelength is close to the visible '
          'maximum and little more can be won there. The two changes with real room to move are L and d '
          '&mdash; which is why they are the two answers a marker will be looking for.')
d.sol(20, 'the two lens positions',
      'the magnification is defined by\n'
      '    M = h′ / h        →        h′ = M h\n'
      'first position :     h′₁ = M₁ h = 4 h\n'
      'second position :    h′₂ = M₂ h = 0.25 h = h / 4',
      'the first image is <b>4 h</b> long and the second is <b>0.25 h</b> long',
      why='The pair is no accident: for a fixed object&ndash;screen distance the two lens positions are '
          'mirror images of each other (object and image distances simply swap), so the two '
          'magnifications are always reciprocals &mdash; 4 and &frac14;. Multiply them and you get '
          'exactly 1, which is a quick check on any answer of this type.')
d.sol(21, 'widening the fringes with a green source',
      '    Δy = λ L / d\n'
      'to increase Δy, change any one of the three :\n'
      '  • increase  L  — move the screen farther from the double slit ,\n'
      '  • decrease  d  — use a double slit with the two openings closer together ,\n'
      '  • increase  λ  — replace the green source with a red one\n'
      '                    ( λ red ≈ 700 nm  >  λ green ≈ 530 nm ).',
      'increase L, decrease d, or move to a longer wavelength (green &rarr; red)',
      why='The one thing that will <b>not</b> work is turning the lamp up. Intensity changes how bright '
          'the fringes are, not where they fall; the geometry of &Delta;y = &lambda;L/d contains no term '
          'for the power of the source.')

d.grp('Part F — Review, Group B')
d.sol(22, 'the image on the wall',
      'an image caught  on a wall  is a real image, and only a convex lens can\n'
      'make one  →  the lens is  convex.\n'
      '    b = 30 cm        ( lens-to-wall distance )\n'
      '    M = b / a = 2        →        a = b / 2 = 30 / 2\n'
      '    a = 15 cm\n'
      'check :   1/f = 1/15 + 1/30 = 3/30   →   f = 10 cm   ( a sensible convex lens )',
      'choice <b>C</b> &mdash; a convex lens with the object 15 cm away',
      why='The single word &ldquo;wall&rdquo; settles half the question before any algebra: a concave '
          'lens produces only virtual images, and a virtual image cannot be caught on a screen. That '
          'kills choices A and D immediately.')
d.sol(23, 'Young with d = 0.2 mm, λ = 600 nm, L = 1 m',
      '    λ = 6 × 10⁻⁷ m ,      d = 0.2 mm = 2 × 10⁻⁴ m ,      L = 1 m\n'
      '    Δy = λ L / d\n'
      '    Δy = ( 6 × 10⁻⁷ × 1 ) / ( 2 × 10⁻⁴ )\n'
      '    Δy = 3 × 10⁻³ m  =  3 mm',
      'choice <b>A</b> &mdash; &Delta;y = 3 mm',
      why='Choice D (1 m) is there to catch a slip in the powers of ten, and choice C (30 mm) a slip of '
          'one power. The habit that protects you is to turn every length into metres in the first line, '
          'before anything is divided.')
d.sol(24, 'the lens that magnifies 4 times twice over',
      'first position — erect, magnified 4 ×  →  the image is  virtual , b is negative :\n'
      '    M = | b | / a₁ = 4        →        | b | = 4 a₁\n'
      '    1/f = 1/a₁ − 1/( 4 a₁ ) = 3 / ( 4 a₁ )        →        a₁ = 3 f / 4\n'
      'second position — real, inverted, magnified 4 ×  →  b is positive :\n'
      '    M = b / a₂ = 4        →        b = 4 a₂\n'
      '    1/f = 1/a₂ + 1/( 4 a₂ ) = 5 / ( 4 a₂ )        →        a₂ = 5 f / 4\n'
      'the object was moved away by 6 cm :\n'
      '    a₂ − a₁ = 6\n'
      '    5f/4 − 3f/4 = 6\n'
      '    2f/4 = 6        →        f / 2 = 6\n'
      '    f = 12 cm\n'
      'check :   a₁ = 9 cm ( inside F = 12 , virtual ✓ )   a₂ = 15 cm ( between F and 2F ✓ )',
      'f = 12 cm &nbsp;&mdash;&nbsp; the object moves from 9 cm to 15 cm',
      why='The two positions straddle the focus, one on each side, and that is what makes the problem '
          'work: the same lens gives the same size of image twice, once virtually (inside F) and once '
          'really (between F and 2F). The check at the end is worth writing every time &mdash; it '
          'confirms both positions land in the regions the wording described.')
d.sol(25, 'the two lens positions for a fixed 90 cm',
      'let the object-to-lens distance be  a ;  the screen is 90 cm from the object,\n'
      'so the lens-to-screen distance is        b = 90 − a\n'
      '    1/f = 1/a + 1/b\n'
      '    1/20 = 1/a + 1/( 90 − a )\n'
      '    1/20 = ( 90 − a + a ) / [ a ( 90 − a ) ]\n'
      '    1/20 = 90 / [ a ( 90 − a ) ]\n'
      '    a ( 90 − a ) = 1800\n'
      '    a² − 90 a + 1800 = 0\n'
      '    a = [ 90 ± √( 8100 − 7200 ) ] / 2 = ( 90 ± 30 ) / 2\n'
      '    a = 60 cm      or      a = 30 cm',
      'a = <b>30 cm</b> or <b>60 cm</b> &mdash; two lens positions give a sharp image',
      why='The two roots add up to 90, and that is the whole story: the object and image distances simply '
          'swap between the two positions (30 &amp; 60, then 60 &amp; 30). One gives a magnified image '
          '(M = 2), the other a diminished one (M = &frac12;) &mdash; this is the standard '
          '&ldquo;displacement method&rdquo; for measuring a focal length.')
d.sol(26, 'the fringe at P when Δ = 1.5 λ',
      '    Δ = S₂P − S₁P = 1.5 λ\n'
      'write it in the standard form :\n'
      '    1.5 λ = ( 1 + ½ ) λ        →        m = 1\n'
      'this matches the  destructive  condition      Δ = ( m + ½ ) λ\n'
      'so the two waves arrive at P exactly  out of phase  ( half a cycle apart ),\n'
      'a crest of one meeting a trough of the other, and they cancel.',
      'a <b>dark fringe</b> &mdash; the path difference is an odd number of half wavelengths, so the two '
      'waves arrive out of phase and interfere destructively',
      why='The rule to carry into the exam: divide the path difference by &lambda;. A <b>whole</b> number '
          '(0, 1, 2 &hellip;) means bright; a whole number <b>and a half</b> (0.5, 1.5, 2.5 &hellip;) '
          'means dark. Here 1.5 is the second dark fringe out from the centre.')

d.grp('Part G — Review, Group C')
d.sol(27, 'red light instead of blue',
      '    Δy = λ L / d        →        Δy  ∝  λ        ( L and d unchanged )\n'
      '    λ red ≈ 700 nm        λ blue ≈ 450 nm\n'
      '    λ red  >  λ blue        →        Δy increases',
      'choice <b>A</b> &mdash; the separation increases, because the wavelength of red light is larger',
      why='Roughly, &Delta;y grows by the ratio 700/450 &asymp; 1.6, so the pattern stretches by about '
          'half again. This is also why a white-light double slit shows a white centre with coloured '
          'edges: every colour makes its own pattern, all sharing the same central fringe.')
d.sol(28, 'concave lens, f = 20 cm, a = 20 cm',
      'for a concave lens  f  is negative :      f = − 20 cm\n'
      '    1/f = 1/a + 1/b\n'
      '    − 1/20 = 1/20 + 1/b\n'
      '    1/b = − 1/20 − 1/20 = − 2/20 = − 1/10\n'
      '    b = − 10 cm        ( negative → virtual, on the object side )\n'
      '    M = | b | / a = 10 / 20 = 0.5        ( diminished )\n'
      '    b negative with a positive  →  erect',
      'choice <b>B</b> &mdash; virtual, erect and diminished, 10 cm from the lens',
      why='Choice A is the trap: &ldquo;the object is at the focal distance&rdquo; sends the image to '
          'infinity only for a <b>convex</b> lens. A concave lens has no such special position &mdash; '
          'it gives the same three adjectives for every object distance, as question 4 proved.')
d.sol(29, 'the ratio of the two fringe separations',
      '    λ₁ = 6000 Å = 6 × 10⁻⁷ m          R₁ = R\n'
      '    λ₂ = 4000 Å = 4 × 10⁻⁷ m          R₂ = 2 R\n'
      'the slit separation d is the same in both cases :\n'
      '    Δy₁ = λ₁ R₁ / d = 6000 R / d\n'
      '    Δy₂ = λ₂ R₂ / d = 4000 × 2 R / d = 8000 R / d\n'
      '    Δy₁ / Δy₂ = 6000 / 8000\n'
      '    Δy₁ / Δy₂ = 3 / 4  =  0.75',
      '&Delta;y&#8321; / &Delta;y&#8322; = 3 : 4',
      why='Because it is a ratio, the ångströms never have to be converted &mdash; the units cancel, and '
          'so does d and the unknown R. Always look for that before reaching for a calculator: two of '
          'the three letters in &lambda;R/d dropped out here on their own.')
d.sol(30, 'why the image speeds up near the focus',
      'for a convex lens        1/f = 1/a + 1/b        →        b = a f / ( a − f )\n'
      'differentiate b with respect to a  ( f is a constant ) :\n'
      '    db/da = [ f ( a − f ) − a f ] / ( a − f )²\n'
      '    db/da = − f² / ( a − f )²\n'
      'the object moves at a uniform speed        v = | da / dt |\n'
      'so the speed of the image is\n'
      '    v′ = | db/dt | = | db/da | × | da/dt |\n'
      '    v′ =  f² / ( a − f )²  ×  v\n'
      'and since        M = f / ( a − f ) :\n'
      '    v′ = M² v\n'
      'as the object approaches F , ( a − f ) → 0 , so M grows without limit :\n'
      '    → v′ depends on a , therefore it is  VARIABLE\n'
      '    → v′ grows as the object nears the focus , and → ∞ at a = f',
      'v&prime; = M&sup2; v &nbsp;&mdash;&nbsp; the image speed depends on the object position, so it is '
      'variable, and it increases without limit as the object approaches F',
      why='The minus sign in db/da carries its own meaning: as the object comes <b>towards</b> the lens '
          'the image runs <b>away</b> from it. And because the factor is M&sup2;, not M, the effect is '
          'dramatic &mdash; at M = 10 the image is already moving a hundred times faster than the object. '
          'This is exactly why focusing a camera on something very close is so delicate.')
d.sol(31, 'why the central fringe is always bright',
      'the central point O lies on the perpendicular bisector of S₁S₂ , so\n'
      '    S₁O = S₂O\n'
      '    Δ = S₂O − S₁O = 0 = 0 × λ        →        m = 0\n'
      'a zero path difference means the two waves arrive exactly  in phase ,\n'
      'crest on crest, for  every  wavelength in the beam ,\n'
      'so they reinforce and the centre is always the  brightest  fringe.',
      'because the two distances from the slits to the centre are equal, the path difference there is '
      'zero for every wavelength &mdash; the waves always arrive in phase and interfere constructively',
      why='&ldquo;For every wavelength&rdquo; is the part worth remembering. Every other fringe sits at a '
          'position that depends on &lambda;, so in white light they spread into colours; only the '
          'central fringe is fixed at &Delta; = 0 for all of them, which is why it comes out white and '
          'why it is used as the reference point of the whole pattern.')

d.foot('Lessons 2&ndash;10 and 2&ndash;11 &middot; Lenses and Young&rsquo;s Experiment &middot; Mr. Gemy',
       '1/f = 1/a + 1/b &nbsp;&middot;&nbsp; &Delta;y = &lambda;L/d')
d.save('l30.html')
print('l30.html written -', d.n, 'questions')

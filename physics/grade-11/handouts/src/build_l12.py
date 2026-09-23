# -*- coding: utf-8 -*-
import figs_l12 as F
from docbase import Doc

d = Doc('Unit 1 &middot; Lesson 1&ndash;12', "Kepler's Laws and<br>Universal Gravitation",
        'Newton&rsquo;s law of gravitation, the gravitational field, the three laws of Kepler and the '
        'geostationary satellite.',
        ['Grade 11 &middot; Egyptian Baccalaureate', '27 questions', 'Step-by-step solutions',
         'G = 6.67 &times; 10&#8315;&sup1;&sup1; N&middot;m&sup2;/kg&sup2;'], "Kepler's Laws and Gravitation")

d.kit('The toolkit for this lesson', [
    ('F = G m<sub>1</sub>m<sub>2</sub> / r&sup2;', 'Newton&rsquo;s law of gravitation'),
    ('g = F / m', 'field strength = force per unit mass'),
    ('g = G M / ( R + r )&sup2;', 'at a height r above the surface'),
    ('1st law : an ellipse', 'the Sun at one focus'),
    ('2nd law : equal areas', 'v r = constant &rarr; fastest when nearest'),
    ('3rd law : T&sup2; &prop; r&sup3;', 'T&sup2; / r&sup3; is the same for one central body'),
])
d.hint('<b>Two shortcuts worth memorising.</b> For Kepler&rsquo;s third law with the Earth&rsquo;s year and '
       'the astronomical unit, T (years) = [ a (AU) ]<sup>3/2</sup>. For the second law, a comet&rsquo;s '
       'speeds obey v<sub>1</sub> r<sub>1</sub> = v<sub>2</sub> r<sub>2</sub> at the nearest and farthest '
       'points.')

# ---------------- A ----------------
d.sec('A', 'Classwork &nbsp;1', "Newton's law of gravitation")
d.q('Newton&rsquo;s law of universal gravitation states that the magnitude of the gravitational force between '
    'two <b>identical</b> masses m separated by a distance of 1 metre is given by the relation:', 'MCQ',
    F.two_masses('Figure 1', 'm', 'm', 'r = 1 m'),
    ch=['F = G m&sup2;', 'F = G m', 'F = m / G', 'F = G / m'])
d.q('Two bodies, each of mass 60 kg, are placed so that the distance between them is 3.0 m. Using '
    'G = 6.67 &times; 10&#8315;&sup1;&sup1; N&middot;m&sup2;/kg&sup2;, <b>determine the magnitude of the '
    'gravitational force between them.</b>', 'Problem')
d.q('The length of the semi-major axis of the orbit of a planet is 9.0 astronomical units. Using the values '
    'for the Earth (a semi-major axis of 1.0 AU and a periodic time of 1.0 year), <b>determine the orbital '
    'periodic time of the planet.</b>', 'Problem')

# ---------------- B ----------------
d.sec('B', 'Home assignment &nbsp;1', 'The gravitational field and the second law')
d.q('<b>Define</b> the concept of the gravitational field of the Earth, and <b>explain</b> how it can be '
    'represented using field lines.', 'Explain', F.field_lines('Figure 2'))
d.q('Two bodies, each of mass 40 kg, are separated by a distance of 3.0 m. Using '
    'G = 6.67 &times; 10&#8315;&sup1;&sup1; N&middot;m&sup2;/kg&sup2;, <b>calculate the gravitational force '
    'between them.</b>', 'Problem')
d.q('The distance between a comet and the Sun at its farthest point is 2.5 astronomical units, and at its '
    'nearest point it is 1.5 astronomical units. <b>Determine the ratio between its speed at the nearest '
    'point and its speed at the farthest point.</b>', 'Problem', F.elliptical_orbit('Figure 3'))

# ---------------- C ----------------
d.sec('C', 'Classwork &nbsp;2', "Kepler's third law and the geostationary satellite")
d.q('Kepler&rsquo;s third law states that, for any satellite or planet revolving around a central body, the '
    'square of the orbital periodic time (T&sup2;) is directly proportional to:', 'MCQ',
    ch=['the semi-major axis (r)', 'the square of the semi-major axis (r&sup2;)',
        'the cube of the semi-major axis (r&sup3;)', 'the square root of the semi-major axis (&radic;r)'])
d.q('The length of the semi-major axis of the orbit of a planet is 7.0 astronomical units. Using the values '
    'for the Earth, <b>determine the orbital periodic time of the planet.</b>', 'Problem')
d.q('<b>Explain why</b> the orbital periodic time of a geostationary satellite must be equal to the periodic '
    'time of the rotation of the Earth about its own axis.', 'Explain', F.geostationary('Figure 4'))

# ---------------- D ----------------
d.sec('D', 'Home assignment &nbsp;2', 'Applying the laws')
d.q('According to Newton&rsquo;s law of universal gravitation, if the distance between two bodies is '
    'increased to <b>three times</b> the original distance while their two masses stay constant, which of the '
    'following statements correctly describes the relation between the gravitational force and the distance '
    'separating the two bodies?', 'MCQ',
    ch=['it is directly proportional to the distance',
        'it is directly proportional to the square of the distance',
        'it is inversely proportional to the distance',
        'it is inversely proportional to the square of the distance'])
d.q('<b>Explain the reason</b> for the constancy of the ratio T&sup2;/r&sup3; for the four largest moons of '
    'Jupiter, even though they revolve in orbits of different radii.', 'Explain')
d.q('<b>Explain how</b> Kepler&rsquo;s third law helps in explaining the difference between the orbital '
    'periodic times of the planets and the asteroids that revolve around the Sun, showing why the distant '
    'bodies take a longer time to complete one revolution.', 'Explain', F.orbits_compare('Figure 5'))

# ---------------- E ----------------
d.sec('E', 'Weekly assessment', 'Groups A, B and C')
d.grp('Group A')
d.q('According to Newton&rsquo;s law of universal gravitation, the force of attraction between two point '
    'masses:', 'MCQ',
    ch=['is inversely proportional to the separating distance r',
        'is directly proportional to the product of their masses and inversely proportional to r&sup2;',
        'is directly proportional to the sum of their masses',
        'is independent of the distance between them'])
d.q('The gravitational field strength g at a distance r <b>above the surface</b> of a spherical body of mass '
    'M and radius R is given by the relation:', 'MCQ', F.g_above_surface('Figure 6'),
    ch=['g = G M / r&sup2;', 'g = G M / ( R + r )&sup2;', 'g = G M&sup2; / r', 'g = G / ( M r&sup2; )'])
d.q('<b>State</b> Kepler&rsquo;s second law of planetary motion, and <b>explain its physical origin</b> in '
    'terms of the principle of conservation of angular momentum.', 'Explain')
d.q('<b>Explain why</b> the planets that have larger orbital radii have longer orbital periodic times '
    'according to Kepler&rsquo;s third law, comparing this with simple uniform linear motion.', 'Explain')
d.q('A comet revolves around the Sun in an elliptical orbit. If the distance between the comet and the Sun at '
    'the farthest point is <b>five times</b> the distance at the nearest point:', 'Problem',
    parts=['<b>a)</b> Calculate the ratio between the speed of the comet at the farthest point and its speed '
           'at the nearest point.',
           '<b>b)</b> If the speed of the comet at the nearest point is 30 km/s, what is its speed at the '
           'farthest point?'])

d.grp('Group B')
d.q('Kepler&rsquo;s third law states that the square of the periodic time (T&sup2;) of a planet is directly '
    'proportional to:', 'MCQ',
    ch=['the orbital speed (v)', 'the cube of the length of the semi-major axis (r&sup3;)',
        'the mass of the planet (m)', 'the reciprocal of the square of the orbital radius (1/r&sup2;)'])
d.q('A satellite that is launched around the Earth in a circular equatorial orbit with a periodic time of '
    '24 hours, so that it appears fixed relative to an observer on the surface of the Earth, is called:',
    'MCQ', ch=['a polar satellite', 'a geostationary satellite', 'a low Earth orbit (LEO) satellite',
               'a satellite in an elliptical orbit'])
d.q('<b>Explain why</b> the unit newton / kilogram (N/kg) is equivalent to the unit metre per second squared '
    '(m/s&sup2;).', 'Explain')
d.q('What happens in each of the following cases?', 'Explain',
    parts=['<b>a)</b> doubling the distance between two masses, according to Newton&rsquo;s law of universal '
           'gravitation.',
           '<b>b)</b> moving a satellite into a larger circular orbit around the Earth.'])
d.q('Two bodies, each of mass 80 kg, are separated by a distance of 2.0 m. <b>Calculate the gravitational '
    'force between them</b>, given that G = 6.67 &times; 10&#8315;&sup1;&sup1; N&middot;m&sup2;/kg&sup2;.',
    'Problem')

d.grp('Group C')
d.q('The gravitational field strength (g) at a point in space is defined as:', 'MCQ',
    ch=['the gravitational potential energy per unit volume',
        'the gravitational force acting per unit mass placed at that point',
        'the total gravitational force between two planets',
        'the gravitational acceleration multiplied by the mass'])
d.q('According to Kepler&rsquo;s first law, where does the Sun lie in the orbit of a planet?', 'MCQ',
    ch=['at the centre of the circular orbit', 'at one of the two foci of the elliptical orbit',
        'completely outside the elliptical orbit', 'at the midpoint of the minor axis of the orbit'])
d.q('Two bodies, each of mass 100 kg, are separated by a distance of 5.0 m. Using '
    'G = 6.67 &times; 10&#8315;&sup1;&sup1; N&middot;m&sup2;/kg&sup2;, <b>calculate the gravitational force '
    'between them.</b>', 'Problem')
d.q('Give the reason for each of the following:', 'Explain',
    parts=['<b>a)</b> a geostationary satellite appears fixed above one single point on the surface of the '
           'Earth.',
           '<b>b)</b> a comet moves with its maximum speed when it is as close as possible to the Sun.'])
d.q('The length of the semi-major axis of the orbit of a planet around a star is <b>4.0 times</b> the length '
    'of the semi-major axis of the orbit of a second planet around the same star. Given that the periodic '
    'time of the second planet is 2.0 years, <b>calculate the periodic time of the first planet.</b>',
    'Problem')

# ---------------- solutions ----------------
d.page()
d.sec('✓', 'Answer key', 'Solutions &mdash; step by step')
d.hint('Two habits make this whole lesson easy. For <b>gravitation</b>, always substitute in SI units and '
       'collect the powers of ten at the very end. For <b>Kepler</b>, never substitute G and M when a '
       '<b>ratio</b> will do: T<sub>1</sub>&sup2;/T<sub>2</sub>&sup2; = r<sub>1</sub>&sup3;/r<sub>2</sub>&sup3;.')

d.grp('Part A &mdash; Classwork 1')
d.sol(1, 'the force between two identical masses 1 m apart',
      'Newton’s law of universal gravitation :\n'
      '    F = G m₁ m₂ / r²\n'
      'the two masses are identical,  m₁ = m₂ = m , and the separation is r = 1 m :\n'
      '    F = G × m × m / (1)² = G m²',
      'A) F = G m²',
      why='Notice that the force depends on the <b>product</b> of the masses, never on their sum — which '
          'is why choice (C) is the classic trap.')
d.sol(2, 'two 60 kg bodies, 3.0 m apart',
      '    F = G m₁ m₂ / r²\n'
      '    F = ( 6.67 × 10⁻¹¹ × 60 × 60 ) / (3.0)²\n'
      '    F = ( 6.67 × 10⁻¹¹ × 3600 ) / 9\n'
      '    F = 6.67 × 10⁻¹¹ × 400\n'
      '    F = 2.67 × 10⁻⁸ N',
      'F = 2.67 &times; 10&#8315;&#8312; N',
      why='About 27 nanonewtons — roughly the weight of a grain of dust. Gravitation is by far the '
          '<b>weakest</b> of the fundamental forces; it only becomes noticeable when one of the masses is '
          'astronomically large.')
d.sol(3, 'the periodic time of a planet at 9.0 AU',
      'Kepler’s third law, written for this planet and for the Earth :\n'
      '    T² / r³ = Tₑ² / rₑ³\n'
      'for the Earth  Tₑ = 1.0 year  and  rₑ = 1.0 AU , so the right-hand side equals 1 :\n'
      '    T² = r³ = (9.0)³ = 729\n'
      '    T = √729 = 27 years',
      'T = 27 years',
      why='With years and astronomical units the law collapses to T = ( a )<sup>3/2</sup>. Here '
          '9<sup>3/2</sup> = ( √9 )³ = 3³ = 27.')

d.grp('Part B &mdash; Home assignment 1')
d.sol(4, 'the gravitational field of the Earth and its field lines',
      None,
      'a region of space in which any mass experiences a gravitational force of attraction towards the Earth',
      why='<b>Definition.</b> The gravitational field of the Earth is the region of space surrounding it in '
          'which any body placed at a point feels a force of attraction directed towards the centre of the '
          'Earth. Its strength at a point is defined as the force acting on <b>unit mass</b> placed there, '
          'g = F / m , measured in N/kg.<br><br>'
          '<b>Field lines.</b> The field is drawn as a set of lines that are <b>radial</b> and point '
          '<b>inwards</b>, towards the centre of the Earth, because that is the direction of the force on a '
          'test mass. The <b>tangent</b> to a line at any point gives the direction of the field there, and '
          'the <b>crowding</b> of the lines measures the strength: the lines are closest together near the '
          'surface (strong field) and spread further apart as the distance increases (weak field), which is '
          'the geometrical picture of the inverse-square law. Field lines never cross, because the field at '
          'a point has one single direction. Close to the surface, over a small region, the lines look '
          'practically parallel and equally spaced — this is why g is taken as a constant 9.8 N/kg in '
          'everyday problems.')
d.sol(5, 'two 40 kg bodies, 3.0 m apart',
      '    F = G m₁ m₂ / r²\n'
      '    F = ( 6.67 × 10⁻¹¹ × 40 × 40 ) / (3.0)²\n'
      '    F = ( 6.67 × 10⁻¹¹ × 1600 ) / 9\n'
      '    F = 6.67 × 10⁻¹¹ × 177.8\n'
      '    F = 1.19 × 10⁻⁸ N',
      'F = 1.19 &times; 10&#8315;&#8312; N')
d.sol(6, 'the comet: nearest speed compared with farthest speed',
      'Kepler’s second law (equal areas in equal times) gives, at the two ends of the\n'
      'major axis, where the velocity is perpendicular to the radius :\n'
      '    v(near) × r(near) = v(far) × r(far)\n'
      'so the speed ratio is the <b>inverse</b> of the distance ratio :\n'
      '    v(near) / v(far) = r(far) / r(near) = 2.5 / 1.5\n'
      '    v(near) / v(far) = 5 / 3 ≈ 1.67',
      'v(near) : v(far) = 5 : 3 &nbsp;&rarr;&nbsp; the comet is about 1.67 times faster at the nearest point',
      why='This is conservation of <b>angular momentum</b> in disguise: m v r stays constant because the '
          'gravitational pull is always directed along the radius, so it exerts no moment about the Sun.')

d.grp('Part C &mdash; Classwork 2')
d.sol(7, "the statement of Kepler's third law",
      'the square of the periodic time is directly proportional to the cube of the semi-major axis :\n'
      '    T² ∝ r³        or        T² / r³ = constant',
      'C) the cube of the semi-major axis ( r&sup3; )')
d.sol(8, 'the periodic time of a planet at 7.0 AU',
      '    T² / r³ = 1   ( using years and astronomical units )\n'
      '    T² = (7.0)³ = 343\n'
      '    T = √343 = 18.5 years',
      'T &asymp; 18.5 years',
      why='A useful check: the planet is 7 times further out than the Earth but takes 18.5 times longer, not '
          '7 times — the period grows faster than the radius.')
d.sol(9, 'why a geostationary satellite has a 24-hour period',
      None,
      'so that it turns through exactly the same angle as the Earth in the same time, and therefore stays '
      'above one fixed point',
      why='“Geostationary” means the satellite appears <b>motionless</b> to an observer standing on '
          'the ground. For that to happen the satellite and the observer must have the same <b>angular '
          'velocity</b>, ω = 2π / T. If the two angular velocities are equal, the two periodic '
          'times must be equal as well, so T must equal the period of rotation of the Earth about its own '
          'axis (one sidereal day ≈ 24 h). Any other period would make the satellite drift steadily '
          'eastwards or westwards relative to the ground. Two extra conditions follow: the orbit must lie '
          'in the <b>plane of the equator</b> (otherwise the satellite would swing north and south), and '
          'the satellite must move in the <b>same sense</b> as the rotation of the Earth. Kepler’s '
          'third law then fixes the radius of that orbit at about 42 × 10³ km from the centre of '
          'the Earth, roughly 36 × 10³ km above the surface.')

d.grp('Part D &mdash; Home assignment 2')
d.sol(10, 'tripling the separating distance',
      'the law itself does not change :\n'
      '    F = G m₁ m₂ / r²      →      F ∝ 1 / r²\n'
      'with the masses unchanged, replacing r by 3r :\n'
      '    F′ = G m₁ m₂ / (3r)² = ( G m₁ m₂ / r² ) / 9 = F / 9',
      'D) inversely proportional to the square of the distance &nbsp;( the force drops to F / 9 )',
      why='Tripling the distance does not make the force three times smaller — it makes it '
          '<b>nine</b> times smaller. This is what “inverse square” means in practice.')
d.sol(11, "why T&sup2;/r&sup3; is the same for all the moons of Jupiter",
      'for a moon of mass m in a circular orbit of radius r around Jupiter\n'
      '( of mass M ), the gravitational pull is the centripetal force :\n'
      '    G M m / r² = m v² / r        and        v = 2π r / T\n'
      '    G M / r² = ( 4π² r² / T² ) / r = 4π² r / T²\n'
      '    T² / r³ = 4π² / ( G M )',
      'T&sup2;/r&sup3; = 4&pi;&sup2;/(G M) &mdash; it contains only G and the mass of Jupiter, so it is the '
      'same for every moon',
      why='The mass of the moon <b>cancels out</b> of the equation, and the radius of its own orbit is not '
          'in the final expression either. All four Galilean moons share the same central body, so they all '
          'share the same constant — even though Io is close in with a period of 1.8 days and '
          'Callisto is far out with a period of 16.7 days.')
d.sol(12, 'planets and asteroids: why distant bodies are slower',
      'for any body orbiting the Sun :\n'
      '    T² = ( 4π² / G M ) r³        →        T ∝ r^( 3/2 )\n'
      'compare an asteroid in the belt ( r ≈ 2.8 AU ) with the Earth ( r = 1.0 AU ) :\n'
      '    T = ( 2.8 )^(3/2) ≈ 4.7 years',
      'because T grows as r<sup>3/2</sup>, a body that is further out has both a longer path and a slower '
      'speed, so its periodic time is much longer',
      why='There are <b>two</b> effects working in the same direction. First, the circumference of the orbit '
          'is larger, so there is simply more distance to cover. Second, the Sun’s pull is weaker far '
          'away, so the orbital speed itself is smaller ( v = √( G M / r ) ). Combining a longer path '
          'with a slower speed makes the period rise faster than the radius — exactly the '
          'r<sup>3/2</sup> dependence of Kepler’s third law. Mercury takes 88 days, the Earth 365 '
          'days, and Neptune 165 years.')

d.grp('Part E &mdash; Weekly assessment, Group A')
d.sol(13, 'the statement of the law of gravitation',
      '    F = G m₁ m₂ / r²\n'
      'so  F ∝ m₁ m₂  ( the product, not the sum )  and  F ∝ 1 / r²',
      'B) directly proportional to the product of the masses and inversely proportional to r&sup2;')
d.sol(14, 'the field strength at a height above the surface',
      'the distance in the law is always measured from the <b>centre</b> of the body, not from its surface.\n'
      'a point at a height r above the surface of a sphere of radius R lies\n'
      'at a distance ( R + r ) from the centre, so :\n'
      '    g = G M / ( R + r )²',
      'B) g = G M / ( R + r )&sup2;',
      why='Choice (A) is what the formula becomes only when r is measured from the centre. Read the '
          'question carefully: “above the surface” always means add R.')
d.sol(15, "Kepler's second law and angular momentum",
      'angular momentum about the Sun :        L = m v r  ( with v ⊥ r )\n'
      'the gravitational pull acts along the line joining the planet to the Sun, so its moment about\n'
      'the Sun is zero  →  L is conserved :\n'
      '    m v₁ r₁ = m v₂ r₂        →        v r = constant',
      'the line joining a planet to the Sun sweeps out equal areas in equal intervals of time',
      why='<b>The link.</b> In a short time Δt the planet moves a distance vΔt, and the thin '
          'triangle it sweeps has area ≈ ½ r ( v Δt ). So the rate of sweeping area is '
          '½ v r = L / 2m. Because no external moment acts about the Sun, L is constant, therefore the '
          'area swept per second is constant — which is precisely the second law. The physical '
          'consequence is that the planet must move <b>fastest at perihelion</b> (small r) and '
          '<b>slowest at aphelion</b> (large r).')
d.sol(16, 'why a larger orbit means a longer period',
      'from  T² = ( 4π² / G M ) r³ :\n'
      '    T ∝ r^( 3/2 )\n'
      'while for uniform motion in a straight line at a fixed speed,  t = d / v ,\n'
      'so the time would only be <b>directly</b> proportional to the distance.',
      'the period rises as r<sup>3/2</sup>, faster than the simple proportionality t &prop; d of uniform '
      'linear motion',
      why='In uniform linear motion doubling the distance doubles the time, because the speed is the same. '
          'In orbital motion doubling the radius multiplies the time by 2<sup>3/2</sup> ≈ 2.83, '
          'because the speed itself drops as 1/√r.')
d.sol(17, 'the comet with r(far) = 5 r(near)',
      'a)  Kepler’s second law at the two ends of the major axis :\n'
      '        v(near) × r(near) = v(far) × r(far)\n'
      '        v(far) / v(near) = r(near) / r(far) = r(near) / ( 5 r(near) ) = 1/5 = 0.2\n\n'
      'b)  v(near) = 30 km/s :\n'
      '        v(far) = 0.2 × 30 = 6 km/s',
      'a) v(far) : v(near) = 1 : 5 &nbsp;&nbsp; b) v(far) = 6 km/s',
      why='Halley’s comet behaves exactly like this: it races past the Sun at about 54 km/s and crawls '
          'at under 1 km/s out beyond Neptune.')

d.grp('Part E &mdash; Weekly assessment, Group B')
d.sol(18, "what T&sup2; is proportional to",
      '    T² ∝ r³',
      'B) the cube of the length of the semi-major axis ( r&sup3; )')
d.sol(19, 'the name of the 24-hour equatorial satellite',
      'a period equal to the rotation period of the Earth,  an equatorial orbit,\n'
      'and the same sense of rotation  →  the satellite appears fixed in the sky',
      'B) a geostationary satellite')
d.sol(20, 'why N/kg is the same as m/s&sup2;',
      'start from the definition of the field strength and from Newton’s second law :\n'
      '    g = F / m            and            F = m a\n'
      'substituting the unit of force, 1 N = 1 kg·m/s² :\n'
      '    1 N / kg = ( 1 kg · m/s² ) / kg = 1 m/s²',
      '1 N/kg &equiv; 1 m/s&sup2;',
      why='The two units describe the <b>same</b> quantity seen from two sides. N/kg is the '
          "<b>field</b> point of view — the pull on each kilogram; m/s² is the <b>motion</b> "
          'point of view — the acceleration that pull produces on a freely falling body. Because the '
          'mass cancels in a = F/m = g, every body falls with the same acceleration, which is why a feather '
          'and a hammer land together on the Moon.')
d.sol(21, 'two changes and their effects',
      'a)  F ∝ 1 / r² , so replacing r by 2r :\n'
      '        F′ = G m₁ m₂ / (2r)² = F / 4\n\n'
      'b)  a larger circular orbit means a larger r, so from\n'
      '        v = √( G M / r )        →   v decreases\n'
      '        T² ∝ r³            →   T increases',
      'a) the force falls to a quarter of its value &nbsp;&nbsp; b) the orbital speed decreases and the '
      'periodic time increases',
      why='Part (b) is the reason a geostationary satellite at 42 000 km moves at only about 3.1 km/s, '
          'while the International Space Station at 6 800 km races round at 7.7 km/s.')
d.sol(22, 'two 80 kg bodies, 2.0 m apart',
      '    F = G m₁ m₂ / r²\n'
      '    F = ( 6.67 × 10⁻¹¹ × 80 × 80 ) / (2.0)²\n'
      '    F = ( 6.67 × 10⁻¹¹ × 6400 ) / 4\n'
      '    F = 6.67 × 10⁻¹¹ × 1600\n'
      '    F = 1.07 × 10⁻⁷ N',
      'F = 1.07 &times; 10&#8315;&#8311; N')

d.grp('Part E &mdash; Weekly assessment, Group C')
d.sol(23, 'the definition of the gravitational field strength',
      '    g = F / m        →        the force acting on each unit of mass, in N/kg',
      'B) the gravitational force acting per unit mass placed at that point')
d.sol(24, "the position of the Sun in Kepler's first law",
      'every planet moves in an <b>ellipse</b>, and the Sun occupies <b>one of the two foci</b> of that\n'
      'ellipse — never the centre.',
      'B) at one of the two foci of the elliptical orbit',
      why='The other focus is empty. For most planets the ellipse is so nearly circular that the two foci '
          'sit very close together — which is why a circle is a good first approximation for the Earth.')
d.sol(25, 'two 100 kg bodies, 5.0 m apart',
      '    F = G m₁ m₂ / r²\n'
      '    F = ( 6.67 × 10⁻¹¹ × 100 × 100 ) / (5.0)²\n'
      '    F = ( 6.67 × 10⁻¹¹ × 10⁴ ) / 25\n'
      '    F = 6.67 × 10⁻¹¹ × 400\n'
      '    F = 2.67 × 10⁻⁸ N',
      'F = 2.67 &times; 10&#8315;&#8312; N')
d.sol(26, 'two reasons',
      None,
      'a) equal angular velocities &nbsp;&nbsp; b) conservation of angular momentum ( v r = constant )',
      why='<b>a)</b> A geostationary satellite has a periodic time equal to the period of rotation of the '
          'Earth and orbits in the plane of the equator in the same sense. Its angular velocity '
          'ω = 2π/T therefore matches that of the point below it, so the line joining the two '
          'never turns: the satellite stays fixed above that single point and a dish on the ground can be '
          'aimed once and left alone.<br><br>'
          '<b>b)</b> The gravitational pull of the Sun acts along the radius, so it has no moment about the '
          'Sun and the angular momentum m v r of the comet is conserved. Since v r must stay constant, the '
          'smallest r goes with the largest v — the comet is at its fastest at the point of closest '
          'approach. This is Kepler’s second law seen from the side of the forces.')
d.sol(27, 'the period of the planet whose axis is 4.0 times larger',
      'Kepler’s third law as a ratio, so G and M never appear :\n'
      '    T₁² / T₂² = r₁³ / r₂³ = ( r₁ / r₂ )³ '
      '= (4.0)³ = 64\n'
      '    T₁ / T₂ = √64 = 8\n'
      '    T₁ = 8 × T₂ = 8 × 2.0 = 16 years',
      'T&#8321; = 16 years',
      why='Both planets orbit the <b>same</b> star, which is what allows the constant 4π²/GM to '
          'cancel. Always look for this shortcut before reaching for a calculator.')

d.foot('Lesson 1&ndash;12 &middot; Kepler&rsquo;s Laws and Universal Gravitation &middot; Mr. Gemy',
       'F = G m&#8321;m&#8322;/r&sup2; &nbsp;&middot;&nbsp; T&sup2; &prop; r&sup3;')
d.save('l12.html')
print('l12.html written -', d.n, 'questions')

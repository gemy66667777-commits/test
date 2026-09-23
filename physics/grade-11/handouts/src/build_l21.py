# -*- coding: utf-8 -*-
import figs_l21 as F
from docbase import Doc

d = Doc('Unit 2 &middot; Lesson 2&ndash;1', 'Simple Harmonic<br>Motion',
        'The restoring force F = &minus;kx, the angular frequency, the periodic time of a mass&ndash;spring '
        'system and the displacement equation x = A sin(&omega;t).',
        ['Grade 11 &middot; Egyptian Baccalaureate', '28 questions', 'Step-by-step solutions',
         '&pi; = 3.14'], 'Simple Harmonic Motion')

d.kit('The toolkit for this lesson', [
    ('F = &minus; k x', 'the restoring force, always towards x = 0'),
    ('&omega; = &radic;( k / m )', 'the angular frequency, in rad/s'),
    ('T = 2&pi; &radic;( m / k )', 'the periodic time of a mass&ndash;spring system'),
    ('f = 1 / T', 'the frequency, in hertz'),
    ('x = A sin( &omega; t )', 'displacement from the equilibrium position'),
    ('v(max) = &omega; A', 'the speed at x = 0, where KE = E'),
])
d.hint('<b>Read the equation, do not memorise the numbers.</b> Whenever a question gives you '
       'x = A sin(&omega;t), the number in front of the sine <b>is</b> the amplitude A and the number '
       'multiplying t <b>is</b> &omega;. Everything else follows in one line: T = 2&pi;/&omega; , '
       'f = 1/T and v(max) = &omega;A.')

# ---------------- A ----------------
d.sec('A', 'Classwork &nbsp;1', 'Investigating a vibrating ruler')
d.q('A student carried out the exploration shown in the figure: a steel ruler was clamped under a stack of '
    'books at the edge of a table so that most of its length projected beyond the edge. The free end was '
    'pushed downwards and released, and it vibrated. The student noticed that the <b>pitch</b> of the note '
    'given out by the ruler stayed practically constant throughout the vibration, even though the amplitude '
    '(the distance travelled by the free end) went on decreasing because of air resistance, until the ruler '
    'came to rest completely.', 'Explain', F.ruler_table('Figure 1'),
    parts=['<b>a)</b> Based on this observation, what is the scientific explanation of the constancy of the '
           'pitch of the note in spite of the continuous decrease of the amplitude?',
           '<b>b)</b> The student then moved the ruler so that the projecting part beyond the edge became '
           '<b>shorter</b> than before, and repeated the experiment. The pitch of the note given out rose '
           '(it became sharper). What is the explanation of this?'])
d.q('When the end of the vibrating ruler reaches the point of maximum displacement, it stops moving for one '
    'instant (v = 0). At that very instant the restoring force and the acceleration have their maximum '
    'values. What is the direct scientific reason for this?', 'MCQ',
    ch=['because a speed equal to zero forces the acceleration and the force to reach their greatest values',
        'because the restoring force depends on the magnitude of the displacement from the equilibrium '
        'position, and the displacement is greatest at this point',
        'because the energy of the motion is greatest at the point of instantaneous rest',
        'because the mass of the ruler increases momentarily on stopping, which increases the force and '
        'the acceleration'])

# ---------------- B ----------------
d.sec('B', 'Home assignment &nbsp;1', 'The periodic time and the mass')
d.q('A mass&ndash;spring system has a periodic time T<sub>1</sub> = 1.2 s.', 'Problem',
    parts=['<b>a)</b> The student replaced the original mass by another one whose magnitude is <b>four '
           'times</b> the first mass (4 m), keeping the same spring. Predict first: will the new periodic '
           'time increase or decrease? Then find the ratio between the new periodic time T<sub>2</sub> and '
           'the original periodic time T<sub>1</sub> <b>without</b> needing the numerical values of m and k.',
           '<b>b)</b> Based on the ratio you reached in part (a), calculate the numerical value of the new '
           'periodic time T<sub>2</sub>.'])
d.q('Can it be said that multiplying the mass by a certain number of times leads to multiplying the periodic '
    'time by the same number of times? <b>Explain your answer</b> by going back to the mathematical form of '
    'the relation between the periodic time and the mass.', 'Explain')
d.q('A body attached to a horizontal spring vibrates with simple harmonic motion. It starts from the '
    'equilibrium position (x = 0) at the instant t = 0 moving towards the maximum positive displacement '
    '(+A), which it reaches at the instant t = T/4; it then returns to x = 0 at the instant t = T/2, then '
    'reaches the maximum negative displacement (&minus;A) at the instant t = 3T/4, and finally returns to '
    'x = 0 on the completion of the full periodic time at the instant t = T. <b>State the displacement, the '
    'speed and the acceleration of the body at each of these five instants</b>, and give the reason in each '
    'case.', 'Explain', F.shm_cycle('Figure 2'))
d.q('A mass attached to a horizontal spring was displaced towards the left until the spring was compressed '
    'to the greatest possible displacement, and was then released from rest at that instant. At this instant '
    'exactly (the instant of release), the restoring force acting on the mass is:', 'MCQ',
    F.spring_compressed('Figure 3'),
    ch=['directed towards the left, because the mass is about to move in that direction',
        'directed towards the right (towards the equilibrium position), and it has the greatest possible '
        'value at this instant exactly',
        'completely zero, because the mass is still in a state of complete rest at the instant of release',
        'directed towards the right, but it has the smallest possible value at this instant exactly'])
d.q('A student hung a mass of magnitude 0.9 kg from a vertical spring of force constant k = 40 N/m, and left '
    'it to vibrate with simple harmonic motion about its equilibrium position. The student then <b>increased '
    'the amplitude</b> of the vibration without changing either the mass or the spring. Which of the '
    'following statements is correct?', 'MCQ',
    ch=['the periodic time increases with the increase of the amplitude, and its value becomes about 0.94 s',
        'the periodic time decreases with the increase of the amplitude, and its value becomes about 0.94 s',
        'the periodic time does not change with the increase of the amplitude, and its value is about 0.94 s',
        'the periodic time does not change with the increase of the amplitude, and its value is about '
        '1.41 s'])

# ---------------- C ----------------
d.sec('C', 'Classwork &nbsp;2', 'The angular frequency and the periodic time')
d.q('A small block of mass m = 0.50 kg is attached to a spring of force constant k = 20 N&middot;m&#8315;&sup1; '
    'on a smooth horizontal path. When the block is displaced from the equilibrium position, a restoring '
    'force acts on it according to the relation F = &minus;kx. <b>Calculate the angular frequency &omega; of '
    'the vibration.</b>', 'Problem', F.spring_mass('Figure 4', 'k = 20 N/m', 'm'))
d.q('A small block of mass m = 0.20 kg slides on a smooth horizontal path and is attached to a spring of '
    'force constant k = 80 N&middot;m&#8315;&sup1;. A restoring force of magnitude F = &minus;kx acts on the '
    'block when its displacement from the equilibrium position is x. Given that &pi; = 3.14, <b>find the '
    'periodic time of the vibration</b> using the relation T = 2&pi;&radic;(m/k).', 'Problem')

# ---------------- D ----------------
d.sec('D', 'Home assignment &nbsp;2', 'Applying the relations')
d.q('A mass&ndash;spring system has a mass m = 0.30 kg and a spring constant k = 30 N/m. Taking '
    '&pi; = 3.14, <b>calculate the periodic time T</b> using the relation T = 2&pi;&radic;(m/k).', 'Problem')
d.q('A body moves with simple harmonic motion according to the relation x = A sin(&omega;t). If the '
    'displacement is x = 0.15 m at the time t = &pi;/4 s, and the angular frequency is &omega; = 2 rad/s, '
    '<b>find the amplitude A.</b>', 'Problem')
d.q('In a mass&ndash;spring system moving with simple harmonic motion, what is the kinetic energy KE at the '
    'equilibrium position x = 0?', 'MCQ', F.energy_bars('Figure 5'),
    ch=['KE = 0', 'KE = E / 4', 'KE = E / 2', 'KE = E'])
d.q('In an experiment on a small block attached to a spring on a smooth horizontal path, the spring constant '
    'was k = 20 N/m and the periodic time of the vibration was T = 1.256 s. If the relation is '
    'T = 2&pi;&radic;(m/k) and &pi; = 3.14, what is the value of the mass m of the block?', 'MCQ',
    ch=['0.8 kg', '1.0 kg', '1.2 kg', '1.6 kg'])

# ---------------- E ----------------
d.sec('E', 'Weekly assessment', 'Groups A, B and C')
d.grp('Group A')
d.q('When a body moving with simple harmonic motion reaches the maximum displacement from the equilibrium '
    'position, its speed is:', 'MCQ',
    ch=['the greatest value it has', 'zero', 'constant and not equal to zero',
        'equal to the acceleration'])
d.q('A body moves with simple harmonic motion, and the periodic time of its motion is T = 0.25 s. What is '
    'its frequency f?', 'MCQ', ch=['0.25 Hz', '2 Hz', '4 Hz', '8 Hz'])
d.q('If the displacement of a body moving with simple harmonic motion is given by the relation '
    'x(t) = 0.06 sin(8&pi;t) m, <b>find the amplitude of the motion A, the periodic time T, the frequency f '
    'and the maximum speed v<sub>max</sub>.</b>', 'Problem', F.sine_curve('Figure 6'))
d.q('A small block of mass m = 0.20 kg attached to a smooth horizontal spring oscillates, and the spring '
    'constant is k = 80 N&middot;m&#8315;&sup1;. <b>Find the periodic time T and then the frequency f</b> of '
    'the motion, given that &pi; = 3.14.', 'Problem')
d.q('A body of mass m = 0.50 kg moves with simple harmonic motion under the action of a restoring force that '
    'obeys the relation F = &minus;kx, where k = 40 N&middot;m&#8315;&sup1;. If its displacement is '
    'x = +0.10 m, <b>find the restoring force F and the acceleration a</b>, and determine the direction of '
    'each of them with respect to the equilibrium position.', 'Problem',
    F.restoring_force('Figure 7', 'x = +0.10 m'))

d.grp('Group B')
d.q('When a body moving with simple harmonic motion passes through the equilibrium position, its '
    'acceleration is:', 'MCQ',
    ch=['zero', 'the greatest positive value', 'the greatest negative value', 'equal to the amplitude'])
d.q('If the frequency of a body moving with simple harmonic motion is f = 5.0 Hz, then the periodic time of '
    'its motion equals:', 'MCQ', ch=['0.20 s', '0.50 s', '5.0 s', '25 s'])
d.q('If the displacement of a body moving with simple harmonic motion is given by the relation '
    'x(t) = 0.04 sin(10&pi;t) m, <b>find the amplitude of the motion A, the periodic time T, the frequency f '
    'and the maximum speed v<sub>max</sub>.</b>', 'Problem')
d.q('A mass m = 0.40 kg attached to a spring of constant k = 40 N&middot;m&#8315;&sup1; moves with simple '
    'harmonic motion. <b>Find the periodic time T and the frequency f</b>, given that &pi; = 3.14.',
    'Problem')
d.q('A body of mass m = 0.25 kg moves with simple harmonic motion under the action of a restoring force that '
    'obeys the relation F = &minus;kx, where k = 20 N&middot;m&#8315;&sup1;. If its displacement is '
    'x = &minus;0.15 m, <b>find the restoring force F and the acceleration a</b>, and determine the '
    'direction of each of them with respect to the equilibrium position.', 'Problem')

d.grp('Group C')
d.q('When the displacement of a body in simple harmonic motion is equal to the amplitude and in the positive '
    'direction, the restoring force is:', 'MCQ',
    ch=['the greatest value it has, and directed towards the equilibrium position', 'zero',
        'the greatest value it has, and directed away from the equilibrium position',
        'constant and in the direction of the motion'])
d.q('A body moves with simple harmonic motion, and the periodic time of its motion is T = 0.80 s. What is '
    'its frequency f?', 'MCQ', ch=['0.80 Hz', '1.25 Hz', '2.50 Hz', '8.00 Hz'])
d.q('If the displacement of a body moving with simple harmonic motion is given by the relation '
    'x(t) = 0.05 sin(5&pi;t) m, <b>find the amplitude of the motion A, the periodic time T, the frequency f '
    'and the maximum speed v<sub>max</sub>.</b>', 'Problem')
d.q('A mass m = 0.90 kg attached to a spring of constant k = 40 N&middot;m&#8315;&sup1; oscillates with '
    'simple harmonic motion. <b>Find the periodic time T and the frequency f</b>, given that &pi; = 3.14.',
    'Problem')
d.q('A body of mass m = 0.40 kg moves with simple harmonic motion under the action of a restoring force that '
    'obeys the relation F = &minus;kx, where k = 32 N&middot;m&#8315;&sup1;. If its displacement is '
    'x = +0.125 m, <b>find the restoring force F and the acceleration a</b>, and determine the direction of '
    'each of them with respect to the equilibrium position.', 'Problem')

_HD = ['instant', 'displacement x', 'speed v', 'acceleration a']
_RW = [['t = 0', '0', 'greatest, towards +x', '0'],
       ['t = T/4', '+A', '0', 'greatest, towards &minus;x'],
       ['t = T/2', '0', 'greatest, towards &minus;x', '0'],
       ['t = 3T/4', '&minus;A', '0', 'greatest, towards +x'],
       ['t = T', '0', 'greatest, towards +x', '0']]
_TBL = ('<table class="vt"><tr>' + ''.join('<th>' + h + '</th>' for h in _HD) + '</tr>' +
        ''.join('<tr>' + ''.join('<td>' + c + '</td>' for c in r) + '</tr>' for r in _RW) + '</table>')

# ---------------- solutions ----------------
d.page()
d.sec('✓', 'Answer key', 'Solutions — step by step')
d.hint('<b>One idea runs through the whole lesson.</b> Because F = &minus;kx, the acceleration is '
       'a = &minus;(k/m)x. So a and x are always <b>opposite in sign</b>, both vanish together at x = 0, '
       'and both reach their maximum together at x = &plusmn;A. Every conceptual question in this lesson '
       'is an application of that one sentence.')

d.grp('Part A — Classwork 1')
d.sol(1, 'the vibrating ruler',
      None,
      'a) because the frequency of a vibrating body does not depend on the amplitude  '
      'b) because a shorter free length is stiffer, so the frequency rises',
      why='<b>a)</b> The pitch of a note is decided by its <b>frequency</b>, and the frequency of the ruler '
          'is fixed by the properties of the system itself — the free length, the stiffness of the '
          'steel and the mass that is vibrating. It is <b>not</b> fixed by how far the end swings. This is '
          'the defining property of simple harmonic motion: the periodic time is <b>independent of the '
          'amplitude</b> (isochronism). Air resistance removes energy, so the amplitude dies away and the '
          'note becomes <b>quieter</b>, but every swing still takes the same time, so the note keeps the '
          'same pitch until it fades out.<br><br>'
          '<b>b)</b> Shortening the projecting part makes the ruler much <b>harder to bend</b> — the '
          'effective force constant k becomes larger — while the length of steel that is actually '
          'moving becomes smaller, so the effective mass m becomes smaller as well. Since '
          'f = ( 1 / 2&pi; ) &radic;( k / m ), both changes push the frequency <b>up</b>, and a higher '
          'frequency is heard as a sharper note. It is exactly the same reason why a short guitar string, '
          'or a string pressed close to the bridge, gives a higher note.')
d.sol(2, 'why the force and the acceleration are greatest at the extreme',
      'the restoring force obeys :\n'
      '    F = − k x        and therefore        a = F / m = − ( k / m ) x\n'
      'so both F and a are proportional to the <b>displacement</b> x, not to the speed.\n'
      'at the point of maximum displacement x = ±A , so |F| and |a| are greatest there.',
      'B) because the restoring force depends on the displacement, which is greatest at this point',
      why='Choice (A) reverses cause and effect: a zero speed does not <b>make</b> the force large, the two '
          'simply happen at the same point. Choice (C) is wrong because at the extreme the energy is '
          'entirely <b>potential</b>, not kinetic, and choice (D) is wrong because mass never changes.')

d.grp('Part B — Home assignment 1')
d.sol(3, 'quadrupling the mass',
      'a)  T = 2π √( m / k )        →        T ∝ √ m   ( same spring, k fixed )\n'
      '    T₂ / T₁ = √( 4m / m ) = √4 = 2     →  the periodic time <b>increases</b>\n\n'
      'b)  T₂ = 2 × T₁ = 2 × 1.2 = 2.4 s',
      'a) T&#8322; : T&#8321; = 2 : 1 &nbsp;&nbsp; b) T&#8322; = 2.4 s',
      why='Notice that k cancels in the ratio, which is why part (a) can be answered without a single '
          'number. A heavier mass has more inertia, so it is slower to be turned round by the same spring '
          'and each cycle takes longer.')
d.sol(4, 'does n times the mass give n times the periodic time?',
      'T = 2π √( m / k )    contains √ m , not m , so :\n'
      '    m → n m        gives        T → √ n × T\n'
      'for example  n = 4  gives  √4 = 2  ( not 4 ) , and  n = 9  gives  3  ( not 9 ).',
      'no &mdash; multiplying the mass by n multiplies the periodic time by &radic;n only',
      why='To <b>double</b> the periodic time you must make the mass <b>four times</b> as large. The square '
          'root is what makes the mass–spring system so forgiving: even a big change of mass produces '
          'only a modest change of timing.')
d.sol(5, 'one complete cycle, instant by instant',
      'the key relation is    a = − ( k / m ) x , together with    E = KE + PE = constant :\n'
      '    at x = 0     all the energy is kinetic   →  v is greatest , a = 0\n'
      '    at x = ±A    all the energy is potential →  v = 0 , |a| is greatest',
      'v is greatest at x = 0 and zero at x = &plusmn;A; a is zero at x = 0 and greatest at x = &plusmn;A',
      extra=_TBL,
      why='The body is never “pushed along” by the spring at x = 0 — it passes through with '
          'the spring exerting no force at all, carried by its own inertia. Everything the spring does is '
          'to slow it down on the way out and speed it up on the way back.')

d.sol(6, 'the instant of release from full compression',
      'at the instant of release the displacement has its greatest magnitude, x = −A :\n'
      '    F = − k x = − k ( −A ) = + k A\n'
      'a positive force means a force towards the <b>right</b>, that is towards x = 0 ,\n'
      'and its magnitude kA is the largest value the restoring force ever takes.',
      'B) towards the right, towards the equilibrium position, and greatest at this instant',
      why='Choice (C) is the classic mistake: the body is momentarily at rest, but <b>rest does not mean '
          'no force</b>. It is precisely because the force is largest here that the body will not stay at '
          'rest for more than an instant.')
d.sol(7, 'increasing the amplitude of a 0.9 kg mass on a 40 N/m spring',
      'the periodic time of a mass–spring system does not contain the amplitude at all :\n'
      '    T = 2π √( m / k ) = 2 × 3.14 × √( 0.9 / 40 )\n'
      '    T = 6.28 × √0.0225 = 6.28 × 0.15\n'
      '    T = 0.942 ≈ 0.94 s      ( unchanged by the larger amplitude )',
      'C) the periodic time does not change, and its value is about 0.94 s',
      why='A larger amplitude means the body travels further, but it also travels <b>faster</b> (a larger '
          'restoring force). The two effects cancel exactly, which is what makes this motion so useful for '
          'clocks.')

d.grp('Part C — Classwork 2')
d.sol(8, 'the angular frequency of the 0.50 kg block',
      '    ω = √( k / m )\n'
      '    ω = √( 20 / 0.50 ) = √40\n'
      '    ω = 6.32 rad/s',
      '&omega; = 6.32 rad/s',
      why='<b>Note on the printed question.</b> The book writes the relation as &omega; = &radic;(m/k); '
          'this is a misprint. The angular frequency is &omega; = &radic;(<b>k/m</b>), which is the one '
          'used here. A quick check settles it: &omega; must get <b>larger</b> for a stiffer spring and '
          '<b>smaller</b> for a heavier mass, and only k/m does that. Note also that &radic;(m/k) would '
          'come out as 0.158, which has the units of a time, not of rad/s.')
d.sol(9, 'the periodic time of the 0.20 kg block on an 80 N/m spring',
      '    T = 2π √( m / k )\n'
      '    T = 2 × 3.14 × √( 0.20 / 80 )\n'
      '    T = 6.28 × √0.0025 = 6.28 × 0.05\n'
      '    T = 0.314 s',
      'T = 0.314 s &nbsp;&asymp;&nbsp; 0.31 s',
      why='<b>Note on the printed question.</b> The four options printed in the book (61.0 s, 13.0 s, '
          '36.0 s and 62.1 s) do not match these data at all — they are hundreds of times too large, '
          'and the given values cannot produce any of them. The question has therefore been set here as a '
          'straight calculation. A stiff spring with a light block vibrates several times a second, so a '
          'periodic time of a fraction of a second is exactly what we should expect.')

d.grp('Part D — Home assignment 2')
d.sol(10, 'the periodic time of the 0.30 kg system',
      '    T = 2π √( m / k )\n'
      '    T = 2 × 3.14 × √( 0.30 / 30 )\n'
      '    T = 6.28 × √0.01 = 6.28 × 0.1\n'
      '    T = 0.628 s',
      'T = 0.628 s')
d.sol(11, 'finding the amplitude from x = A sin(ωt)',
      '    x = A sin( ω t )\n'
      '    0.15 = A sin( 2 × π/4 ) = A sin( π/2 )\n'
      '    sin( π/2 ) = 1        ( the angle is in radians, π/2 rad = 90° )\n'
      '    0.15 = A × 1        →        A = 0.15 m',
      'A = 0.15 m',
      why='At this particular instant the body happens to be exactly at the end of its swing, so its '
          'displacement <b>is</b> the amplitude. Keep the calculator in radian mode for this kind of '
          'question.')
d.sol(12, 'the kinetic energy at the equilibrium position',
      'the total energy is constant :        E = KE + PE\n'
      'at  x = 0  the spring is neither stretched nor compressed, so  PE = 0 :\n'
      '    KE = E − 0 = E        ( and the speed there is v(max) = ωA )',
      'D) KE = E',
      why='The equilibrium position is the one place where the body owns all of the energy of the system '
          'as energy of motion — and it is therefore the place where it is moving fastest.')
d.sol(13, 'finding the mass from the periodic time',
      'square both sides of the relation and make m the subject :\n'
      '    T = 2π √( m / k )      →      T² = 4π² m / k\n'
      '    m = k T² / ( 4π² )\n'
      '    m = 20 × (1.256)² / ( 4 × (3.14)² )\n'
      '    m = 20 × 1.5775 / 39.44 = 31.55 / 39.44\n'
      '    m = 0.80 kg',
      'A) m = 0.8 kg',
      why='A neat shortcut: 1.256 s is exactly 4 &times; 0.314 s, and 0.314 s belongs to '
          '&radic;(m/k) = 0.05. So &radic;(m/k) here is 0.2, giving m/k = 0.04 and m = 0.8 kg.')

d.grp('Part E — Weekly assessment, Group A')
d.sol(14, 'the speed at the maximum displacement',
      'at  x = ±A  the body reverses its direction, so it must pass through rest :\n'
      '    all the energy is potential there    →    KE = 0    →    v = 0',
      'B) zero')
d.sol(15, 'the frequency for T = 0.25 s',
      '    f = 1 / T = 1 / 0.25 = 4 Hz',
      'C) f = 4 Hz')
d.sol(16, 'reading x(t) = 0.06 sin(8πt)',
      'compare with the standard form  x = A sin( ω t ) :\n'
      '    A = 0.06 m            ω = 8π rad/s\n'
      '    T = 2π / ω = 2π / 8π = 0.25 s\n'
      '    f = 1 / T = 4 Hz\n'
      '    v(max) = ω A = 8π × 0.06 = 0.48π = 1.51 m/s',
      'A = 0.06 m , T = 0.25 s , f = 4 Hz , v(max) = 1.51 m/s',
      why='No calculator is needed for T: the &pi; in &omega; always cancels the &pi; in 2&pi;, so '
          'T = 2/8 = 0.25 s straight away.')
d.sol(17, 'T and f for m = 0.20 kg on k = 80 N/m',
      '    T = 2π √( m / k ) = 6.28 × √( 0.20 / 80 )\n'
      '    T = 6.28 × √0.0025 = 6.28 × 0.05 = 0.314 s\n'
      '    f = 1 / T = 1 / 0.314 = 3.18 Hz',
      'T = 0.314 s , f = 3.18 Hz')
d.sol(18, 'the force and the acceleration at x = +0.10 m',
      '    F = − k x = − 40 × ( +0.10 ) = − 4.0 N\n'
      '    a = F / m = − 4.0 / 0.50 = − 8.0 m/s²\n'
      'the minus sign means the direction is opposite to the displacement,\n'
      'that is <b>towards</b> the equilibrium position.',
      'F = 4.0 N and a = 8.0 m/s&sup2;, both directed towards the equilibrium position',
      why='Always quote the sign as well as the size. The minus sign in F = &minus;kx is the whole physics '
          'of the lesson: it is what turns a push into an <b>oscillation</b> instead of an escape.')

d.grp('Part E — Weekly assessment, Group B')
d.sol(19, 'the acceleration at the equilibrium position',
      '    a = − ( k / m ) x        and at the equilibrium position  x = 0 :\n'
      '    a = 0        ( the spring exerts no force there )',
      'A) zero')
d.sol(20, 'the periodic time for f = 5.0 Hz',
      '    T = 1 / f = 1 / 5.0 = 0.20 s',
      'A) T = 0.20 s')
d.sol(21, 'reading x(t) = 0.04 sin(10πt)',
      '    A = 0.04 m            ω = 10π rad/s\n'
      '    T = 2π / 10π = 0.2 s\n'
      '    f = 1 / 0.2 = 5 Hz\n'
      '    v(max) = ω A = 10π × 0.04 = 0.4π = 1.26 m/s',
      'A = 0.04 m , T = 0.20 s , f = 5 Hz , v(max) = 1.26 m/s')
d.sol(22, 'T and f for m = 0.40 kg on k = 40 N/m',
      '    T = 6.28 × √( 0.40 / 40 ) = 6.28 × √0.01\n'
      '    T = 6.28 × 0.1 = 0.628 s\n'
      '    f = 1 / 0.628 = 1.59 Hz',
      'T = 0.628 s , f = 1.59 Hz')
d.sol(23, 'the force and the acceleration at x = −0.15 m',
      '    F = − k x = − 20 × ( −0.15 ) = + 3.0 N\n'
      '    a = F / m = + 3.0 / 0.25 = + 12 m/s²\n'
      'the plus sign here means the direction is the positive one — and since the body\n'
      'is on the negative side, that is again <b>towards</b> the equilibrium position.',
      'F = 3.0 N and a = 12 m/s&sup2;, both directed towards the equilibrium position',
      why='The sign of F is always <b>opposite</b> to the sign of x. That is the only thing you have to '
          'watch when the displacement is given as a negative number.')

d.grp('Part E — Weekly assessment, Group C')
d.sol(24, 'the restoring force at x = +A',
      '    F = − k x = − k A        ( largest magnitude, negative direction )\n'
      'so the force has its greatest value, and it points back towards x = 0.',
      'A) the greatest value it has, directed towards the equilibrium position')
d.sol(25, 'the frequency for T = 0.80 s',
      '    f = 1 / T = 1 / 0.80 = 1.25 Hz',
      'B) f = 1.25 Hz')
d.sol(26, 'reading x(t) = 0.05 sin(5πt)',
      '    A = 0.05 m            ω = 5π rad/s\n'
      '    T = 2π / 5π = 0.4 s\n'
      '    f = 1 / 0.4 = 2.5 Hz\n'
      '    v(max) = ω A = 5π × 0.05 = 0.25π = 0.785 m/s',
      'A = 0.05 m , T = 0.40 s , f = 2.5 Hz , v(max) = 0.785 m/s')
d.sol(27, 'T and f for m = 0.90 kg on k = 40 N/m',
      '    T = 6.28 × √( 0.90 / 40 ) = 6.28 × √0.0225\n'
      '    T = 6.28 × 0.15 = 0.942 s\n'
      '    f = 1 / 0.942 = 1.06 Hz',
      'T = 0.942 s , f = 1.06 Hz',
      why='This is the same system as question 7 — a good place to check that you get the same answer '
          'by both routes.')
d.sol(28, 'the force and the acceleration at x = +0.125 m',
      '    F = − k x = − 32 × ( +0.125 ) = − 4.0 N\n'
      '    a = F / m = − 4.0 / 0.40 = − 10 m/s²',
      'F = 4.0 N and a = 10 m/s&sup2;, both directed towards the equilibrium position')

d.foot('Lesson 2&ndash;1 &middot; Simple Harmonic Motion &middot; Mr. Gemy',
       'F = &minus;kx &nbsp;&middot;&nbsp; T = 2&pi;&radic;(m/k)')
d.save('l21.html')
print('l21.html written -', d.n, 'questions')

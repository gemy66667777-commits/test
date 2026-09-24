# -*- coding: utf-8 -*-
"""Chapter 2 - Lesson 1 : Simple Harmonic Motion.  40 questions with step-by-step model answers.
Take pi = 3.14 throughout."""
import math
import zb_figs_shm as G

DOTS = ' <span class="dots">............</span>'


def mcq(t, ch, ok, steps, sp='x', cols=None):
    return dict(t=t, ch=ch, ok=ok, steps=steps, sp=sp, cols=cols)


def ess(t, steps, res, sp=''):
    return dict(t=t, steps=steps, res=res, sp=sp)


Q = []


def q(stem, parts, fig=None, figpos='below'):
    Q.append(dict(stem=stem, parts=parts, fig=fig, figpos=figpos))


# ------------------------------------------------------------------ medium 1 - 5
q('A block of mass 0.5 kg is attached to a horizontal spring of spring constant 50 N/m on a smooth horizontal '
  'surface. The block is pulled aside and released, so it oscillates in simple harmonic motion:',
  [mcq('The angular frequency of the oscillation equals' + DOTS, ['5 rad/s', '10 rad/s', '25 rad/s', '100 rad/s'], 1,
       ['ω = √(k / m) = √(50 / 0.5) = √100', 'ω = 10 rad/s']),
   mcq('The periodic time of the oscillation equals' + DOTS, ['0.628 s', '0.314 s', '1.59 s', '6.28 s'], 0,
       ['T = 2π / ω = (2 × 3.14) / 10', 'T = 0.628 s'])],
  G.spring_block(100))

q('The displacement of a body moving in simple harmonic motion is given by the equation '
  'x = 0.05 sin (20 t), where x is in metres and t in seconds:',
  [mcq('The amplitude of the motion equals' + DOTS, ['20 m', '0.05 m', '0.1 m', '1 m'], 1,
       ['Comparing with x = A sin (ωt) :', 'A = 0.05 m']),
   mcq('The frequency of the motion equals' + DOTS, ['20 Hz', '0.314 Hz', '3.18 Hz', '126 Hz'], 2,
       ['ω = 20 rad/s', 'f = ω / 2π = 20 / 6.28 = 3.18 Hz'])])

q('Choose the correct answer:',
  [mcq('In simple harmonic motion, the restoring force is always' + DOTS,
       ['in the direction of motion', 'directed towards the equilibrium position and proportional to the displacement',
        'constant in magnitude', 'proportional to the velocity'], 1,
       ['F = −k x : proportional to the displacement x,', 'and the negative sign means it points towards x = 0.']),
   mcq('The speed of the body is maximum at' + DOTS,
       ['the equilibrium position', 'the two extreme positions', 'halfway between them', 'every point equally'], 0,
       ['At x = 0 all the energy is kinetic, so the speed is maximum : v<sub>max</sub> = ωA.']),
   mcq('The acceleration of the body is maximum at' + DOTS,
       ['the equilibrium position', 'halfway to the extremes', 'the two extreme positions', 'no point'], 2,
       ['a = −ω² x : its magnitude is largest where |x| is largest, at x = ±A.'])])

q('The graph shows how the displacement of a body in simple harmonic motion changes with time:',
  [mcq('The amplitude of the motion is' + DOTS, ['8 cm', '4 cm', '2 cm', '0.8 cm'], 1,
       ['The largest displacement read from the graph is 4 cm.', 'A = 4 cm']),
   mcq('The frequency of the motion is' + DOTS, ['0.8 Hz', '2.5 Hz', '1.25 Hz', '7.85 Hz'], 2,
       ['One complete cycle takes T = 0.8 s', 'f = 1 / T = 1 / 0.8 = 1.25 Hz']),
   ess('Calculate the angular frequency.', ['ω = 2π / T = 6.28 / 0.8 = 7.85 rad/s'], 'ω = 7.85 rad/s', 's')],
  G.graph_xt(86, A=4, T=0.8, cycles=1.5), 'right')

q('The graph shows the restoring force F acting on a body attached to a spring against its displacement x '
  'from the equilibrium position:',
  [mcq('The spring constant equals' + DOTS, ['2 N/m', '20 N/m', '200 N/m', '2000 N/m'], 2,
       ['F = −k x → k = |F| / x', 'k = 20 / 0.1 = 200 N/m']),
   mcq('If the mass of the body is 2 kg, its periodic time is' + DOTS, ['0.628 s', '0.314 s', '6.28 s', '0.1 s'], 0,
       ['T = 2π √(m / k) = 6.28 × √(2 / 200)', 'T = 6.28 × 0.1 = 0.628 s']),
   ess('What does the negative slope of the line mean?',
       ['The restoring force is always opposite to the displacement (F = −kx):',
        'it always pulls the body back towards the equilibrium position.'],
       'F is always opposite to x', 's')],
  G.graph_line(82, through=(0.1, -20), pt=(0.1, -20)), 'right')

# ------------------------------------------------------------------ hard 6 - 40
q('A body oscillates in simple harmonic motion with an amplitude of 8 cm and a periodic time of 0.4 s:',
  [mcq('Its maximum speed equals' + DOTS, ['1.256 m/s', '0.2 m/s', '3.14 m/s', '19.7 m/s'], 0,
       ['ω = 2π / T = 6.28 / 0.4 = 15.7 rad/s', 'v<sub>max</sub> = ωA = 15.7 × 0.08 = 1.256 m/s']),
   ess('Calculate its maximum acceleration.',
       ['a<sub>max</sub> = ω² A = (15.7)² × 0.08', 'a<sub>max</sub> = 246.5 × 0.08 = 19.7 m/s²'],
       'a<sub>max</sub> ≈ 19.7 m/s²', 'm'),
   mcq('The ratio a<sub>max</sub> / v<sub>max</sub> equals' + DOTS, ['T', 'A', 'ω', 'f'], 2,
       ['a<sub>max</sub> / v<sub>max</sub> = ω² A / ωA = ω = 15.7 rad/s'])])

q('A body in simple harmonic motion has a maximum speed of 2 m/s and a maximum acceleration of 40 m/s²:',
  [mcq('Its angular frequency equals' + DOTS, ['80 rad/s', '20 rad/s', '0.05 rad/s', '40 rad/s'], 1,
       ['a<sub>max</sub> / v<sub>max</sub> = ω² A / ωA = ω', 'ω = 40 / 2 = 20 rad/s']),
   ess('Find the amplitude and the periodic time.',
       ['A = v<sub>max</sub> / ω = 2 / 20 = 0.1 m', 'T = 2π / ω = 6.28 / 20 = 0.314 s'],
       'A = 0.1 m ,  T = 0.314 s', 'm')])

q('A body of mass m attached to a horizontal spring oscillates with a periodic time of 0.6 s:',
  [mcq('If another mass of 3m is fixed to the body, the new periodic time is' + DOTS,
       ['0.3 s', '0.6 s', '2.4 s', '1.2 s'], 3,
       ['T = 2π √(m / k) → T ∝ √m', 'the mass becomes 4m → T′ = √4 × 0.6 = 1.2 s']),
   mcq('To make the periodic time 0.3 s with the same spring, the mass must be' + DOTS,
       ['m / 2', 'm / 4', '2m', '4m'], 1,
       ['T′ / T = 0.3 / 0.6 = 1/2 = √(m′ / m)', 'm′ / m = 1/4 → m′ = m / 4']),
   ess('With the original mass, what is the periodic time if the spring is replaced by one 4 times stiffer?',
       ['T ∝ 1 / √k → T′ = T / √4 = 0.6 / 2 = 0.3 s'], 'T′ = 0.3 s', 's')])

q('Two identical bodies, each of mass m, oscillate horizontally on two springs: spring A of constant k and '
  'spring B of constant 4k, as shown:',
  [mcq('The ratio of the periodic times T<sub>A</sub> / T<sub>B</sub> equals' + DOTS,
       ['4', '1/2', '1/4', '2'], 3,
       ['T ∝ 1 / √k → T<sub>A</sub> / T<sub>B</sub> = √(4k / k) = 2']),
   ess('What mass must be fixed to spring B so that its periodic time equals that of A?',
       ['T<sub>B</sub> = 2π √(M / 4k) must equal T<sub>A</sub> = 2π √(m / k)', 'M / 4k = m / k → M = 4m'],
       'M = 4m', 'm')],
  G.two_systems(96))

q('A body of mass 0.2 kg oscillates on a horizontal spring of constant 80 N/m with an amplitude of 10 cm:',
  [mcq('The total mechanical energy of the oscillator is' + DOTS, ['0.8 J', '0.4 J', '4 J', '0.04 J'], 1,
       ['E = ½ k A² = ½ × 80 × (0.1)²', 'E = 0.4 J']),
   ess('Calculate the maximum speed of the body.',
       ['At x = 0 all the energy is kinetic : ½ m v<sub>max</sub>² = E', 'v<sub>max</sub> = √(2E / m) = √(2 × 0.4 / 0.2) = 2 m/s'],
       'v<sub>max</sub> = 2 m/s', 'm'),
   ess('Calculate its speed when the displacement is 5 cm.',
       ['PE = ½ k x² = ½ × 80 × (0.05)² = 0.1 J', 'KE = E − PE = 0.4 − 0.1 = 0.3 J',
        'v = √(2 KE / m) = √(2 × 0.3 / 0.2) = √3 ≈ 1.73 m/s'],
       'v ≈ 1.73 m/s', 'm')])

q('The graph shows two energy curves (1) and (2) of a body in simple harmonic motion against its displacement x, '
  'together with the total energy E:',
  [mcq('The curve that represents the kinetic energy is' + DOTS, ['curve (1)', 'curve (2)', 'the line E', 'none of them'], 1,
       ['The kinetic energy is maximum at x = 0 and zero at x = ±A → curve (2).',
        'Curve (1) is the potential energy ½kx², zero at x = 0.']),
   mcq('At point P the kinetic and potential energies are equal. Its displacement is' + DOTS,
       ['A / 2', 'A / 4', 'A / √2', 'A'], 2,
       ['PE = KE = E/2 → ½ k x² = ½ (½ k A²)', 'x² = A² / 2 → x = A / √2 ≈ 0.71 A']),
   ess('Find the ratio KE : PE when x = A/2.',
       ['PE = ½ k (A/2)² = E / 4', 'KE = E − E/4 = 3E / 4', 'KE : PE = 3 : 1'], 'KE : PE = 3 : 1', 's')],
  G.graph_energy(84), 'right')

q('A body oscillates in simple harmonic motion with a periodic time of 1.2 s, starting from the equilibrium '
  'position (x = A sin ωt):',
  [mcq('The shortest time taken to move from x = 0 to x = A/2 is' + DOTS, ['0.3 s', '0.15 s', '0.1 s', '0.2 s'], 2,
       ['A/2 = A sin (ωt) → sin (ωt) = 0.5 → ωt = π/6', 't = (π/6) / (2π/T) = T / 12 = 1.2 / 12 = 0.1 s']),
   ess('Find the time taken to move from x = A/2 to x = A, and explain why it is longer than the first half.',
       ['from 0 to A takes T/4 = 0.3 s', 'from A/2 to A : 0.3 − 0.1 = 0.2 s',
        'the body slows down as it approaches the extreme position, so the second half takes longer'],
       't = 0.2 s', 'm')])

q('The graph shows the acceleration a of a body in simple harmonic motion against its displacement x:',
  [mcq('The angular frequency of the motion is' + DOTS, ['400 rad/s', '4 rad/s', '0.05 rad/s', '20 rad/s'], 3,
       ['a = −ω² x → ω² = |a| / x = 8 / 0.02 = 400', 'ω = 20 rad/s']),
   ess('Calculate the periodic time.', ['T = 2π / ω = 6.28 / 20 = 0.314 s'], 'T = 0.314 s', 's'),
   ess('What property of simple harmonic motion does this graph show?',
       ['The acceleration is proportional to the displacement and always opposite to it (a = −ω²x).'],
       'a ∝ −x', 's')],
  G.graph_line(80, xt=(0, 0.01, 0.02), yt=(0, -4, -8), xl='x (m)', yl='a (m/s&#178;)',
               through=(0.02, -8), pt=(0.02, -8)), 'right')

q('The displacement of a body in simple harmonic motion is x = 0.1 sin (5π t), where x is in metres and t in seconds:',
  [mcq('The displacement of the body at t = 0.1 s is' + DOTS, ['zero', '0.05 m', '0.1 m', '−0.1 m'], 2,
       ['x = 0.1 sin (5π × 0.1) = 0.1 sin (π/2)', 'x = 0.1 × 1 = 0.1 m (an extreme position)']),
   ess('Find the velocity and the acceleration of the body at that instant.',
       ['At an extreme position the body stops for an instant : v = 0',
        'a = −ω² x = −(5 × 3.14)² × 0.1 = −246.5 × 0.1 ≈ −24.6 m/s²'],
       'v = 0 ,  a ≈ −24.6 m/s²', 'm'),
   ess('Find the periodic time.', ['ω = 5π → T = 2π / ω = 2π / 5π = 0.4 s'], 'T = 0.4 s', 's')])

q('A steel ruler is clamped at the edge of a table and its free end is set vibrating, as shown:',
  [mcq('As the amplitude of the vibration slowly decreases, the periodic time' + DOTS,
       ['increases', 'decreases', 'remains constant', 'becomes zero'], 2,
       ['The periodic time of simple harmonic motion does not depend on the amplitude;',
        'that is why the pitch of the sound stays the same.']),
   ess('If the free length of the ruler is made shorter, what happens to the frequency? Explain.',
       ['A shorter free length is stiffer (a larger k),',
        'f = (1 / 2π) √(k / m) → the frequency increases (a higher pitch).'],
       'the frequency increases', 'm')],
  G.ruler(92))

q('Two identical bodies on two identical springs are displaced from equilibrium by 2 cm (A) and 5 cm (B) and '
  'released at the same moment, as shown:',
  [mcq('The body that reaches the equilibrium position first is' + DOTS,
       ['A', 'B', 'both at the same time', 'it cannot be known'], 2,
       ['Both take T/4, and T = 2π √(m / k) does not depend on the amplitude.']),
   ess('Find the ratio of their maximum speeds v<sub>A</sub> : v<sub>B</sub>.',
       ['v<sub>max</sub> = ωA, with the same ω', 'v<sub>A</sub> : v<sub>B</sub> = 2 : 5'], '2 : 5', 's'),
   ess('Find the ratio of their total energies E<sub>A</sub> : E<sub>B</sub>.',
       ['E = ½ k A² → E ∝ A²', 'E<sub>A</sub> : E<sub>B</sub> = 2² : 5² = 4 : 25'], '4 : 25', 's')],
  G.two_systems(96, labs=(('k', 'm'), ('k', 'm')), disp=(2, 5)))

q('The amplitude of a mass&ndash;spring oscillator is doubled, the mass and the spring being unchanged:',
  [mcq('Which of the following is correct?',
       ['the periodic time is doubled', 'the maximum speed is doubled',
        'the total energy is doubled', 'the maximum acceleration is quadrupled'], 1,
       ['T = 2π √(m/k) : unchanged', 'v<sub>max</sub> = ωA : doubled',
        'E = ½kA² : ×4', 'a<sub>max</sub> = ω²A : doubled']),
   mcq('The total energy becomes' + DOTS, ['2 times', 'the same', '4 times', 'half'], 2,
       ['E ∝ A² → E′ / E = 2² = 4'])])

q('The spring of a mass&ndash;spring oscillator is replaced by one 4 times stiffer, and the mass is doubled:',
  [mcq('The new periodic time T′ in terms of the old one T is' + DOTS, ['T / √2', 'T / 2', 'T √2', '2T'], 0,
       ['T′ / T = √(m′ / m) × √(k / k′) = √2 × √(1/4)', 'T′ / T = √2 / 2 = 1 / √2']),
   ess('How does the frequency change?', ['f ∝ 1 / T → f′ = √2 f ≈ 1.41 f'], 'f′ = √2 f', 's')])

q('A body of mass 0.2 kg is acted upon by a force F that depends on its displacement x:',
  [mcq('The body moves in simple harmonic motion if the force is' + DOTS,
       ['F = −5 x²', 'F = 5 x', 'F = −5 x', 'F = −5'], 2,
       ['SHM needs a force proportional to x and opposite to it : F = −k x.']),
   ess('For this force, find the angular frequency and the periodic time.',
       ['k = 5 N/m', 'ω = √(k / m) = √(5 / 0.2) = √25 = 5 rad/s', 'T = 2π / ω = 6.28 / 5 = 1.256 s'],
       'ω = 5 rad/s ,  T = 1.256 s', 'm')])

q('The graph shows the displacement of a body in simple harmonic motion against time. P, Q, R, S and T are '
  'five points on the curve:',
  [mcq('The speed of the body is maximum at' + DOTS, ['P, R and T', 'Q and S', 'Q only', 'S only'], 0,
       ['The speed is maximum where x = 0 (the steepest parts of the curve) : P, R and T.']),
   mcq('The acceleration is maximum and positive at' + DOTS, ['Q', 'S', 'R', 'P'], 1,
       ['a = −ω² x is largest and positive where x = −A : point S.']),
   ess('At which points is the restoring force zero?', ['F = −k x = 0 where x = 0 : P, R and T.'], 'P, R and T', 's')],
  G.graph_xt(86, A=5, T=0.4, cycles=1, points=True), 'right')

q('A body oscillates in simple harmonic motion with an angular frequency of 10 rad/s:',
  [mcq('When its displacement is −3 cm, its acceleration is' + DOTS, ['−3 m/s²', '+3 m/s²', '−0.3 m/s²', '+30 m/s²'], 1,
       ['a = −ω² x = −(10)² × (−0.03)', 'a = +3 m/s² (towards the equilibrium position)']),
   ess('If the mass of the body is 0.5 kg, find the restoring force when x = +3 cm.',
       ['a = −ω² x = −100 × 0.03 = −3 m/s²', 'F = m a = 0.5 × (−3) = −1.5 N'], 'F = −1.5 N', 's')])

q('A body of mass 2 kg attached to a horizontal spring of constant 200 N/m is pulled 10 cm from its '
  'equilibrium position and released:',
  [mcq('The restoring force at the moment of release is' + DOTS, ['2 N', '20 N', '200 N', '2000 N'], 1,
       ['|F| = k x = 200 × 0.1 = 20 N (towards the equilibrium position)']),
   ess('Find its acceleration at the moment of release.', ['a = F / m = 20 / 2 = 10 m/s²'], 'a = 10 m/s²', 's'),
   ess('Find its speed as it passes the equilibrium position.',
       ['ω = √(k / m) = √(200 / 2) = 10 rad/s', 'v<sub>max</sub> = ωA = 10 × 0.1 = 1 m/s'], 'v = 1 m/s', 's')],
  G.spring_block(96, mark_labels=('&#8722;10 cm', '0', '+10 cm')))

q('A body oscillates with a frequency of 2.5 Hz and an amplitude of 5 cm, starting from the equilibrium position:',
  [mcq('The number of complete oscillations it makes in one minute is' + DOTS, ['25', '150', '2.5', '60'], 1,
       ['N = f × t = 2.5 × 60 = 150 oscillations']),
   ess('Find the distance it travels in 2 s, and its displacement at the end of these 2 s.',
       ['in 2 s it makes 2.5 × 2 = 5 complete oscillations', 'each oscillation covers 4A = 20 cm',
        'distance = 5 × 20 = 100 cm = 1 m', 'after whole oscillations it is back where it started : displacement = 0'],
       'distance = 1 m ,  displacement = 0', 'm')])

q('A body oscillates with an amplitude of 10 cm and an angular frequency of 10 rad/s:',
  [mcq('Its speed when its displacement is 6 cm equals' + DOTS, ['1 m/s', '0.6 m/s', '0.8 m/s', '0.36 m/s'], 2,
       ['energy : ½ k A² = ½ k x² + ½ m v² → v = ω √(A² − x²)', 'v = 10 × √(0.01 − 0.0036) = 10 × 0.08 = 0.8 m/s']),
   ess('At what displacement is its speed half the maximum speed?',
       ['v = v<sub>max</sub> / 2 → ω √(A² − x²) = ωA / 2', 'A² − x² = A² / 4 → x = (√3 / 2) A',
        'x = 0.866 × 10 = 8.66 cm'], 'x ≈ 8.66 cm', 'm')])

q('The speed of a body in simple harmonic motion is 0.8 m/s when its displacement is 6 cm, and 0.6 m/s when '
  'its displacement is 8 cm:',
  [ess('Find the angular frequency of the motion.',
       ['v² = ω² (A² − x²) for both positions',
        '0.64 = ω² (A² − 0.0036)  and  0.36 = ω² (A² − 0.0064)',
        'subtracting : 0.28 = ω² × 0.0028 → ω² = 100 → ω = 10 rad/s'], 'ω = 10 rad/s', 'm'),
   ess('Find the amplitude.', ['A² = 0.64 / 100 + 0.0036 = 0.0064 + 0.0036 = 0.01', 'A = 0.1 m = 10 cm'],
       'A = 10 cm', 'm')])

q('The graph shows how the velocity of a body in simple harmonic motion changes with time:',
  [ess('Find the angular frequency.', ['T = 0.2 s (one complete cycle)', 'ω = 2π / T = 6.28 / 0.2 = 31.4 rad/s'],
       'ω = 31.4 rad/s', 's'),
   mcq('The amplitude of the motion is' + DOTS, ['1.59 cm', '15.7 cm', '0.1 cm', '3.14 cm'], 0,
       ['v<sub>max</sub> = ωA → A = 0.5 / 31.4 = 0.0159 m ≈ 1.59 cm']),
   ess('Where is the body at t = 0?', ['At t = 0 the speed is maximum, so the body is at the equilibrium position.'],
       'at the equilibrium position', 's')],
  G.graph_xt(84, A=0.5, T=0.2, cycles=1.5, ylab='v (m/s)', fn=math.cos, col='#2563EB'), 'right')

q('Choose the correct answer:',
  [mcq('When the displacement of a body in simple harmonic motion is A/3, the ratio KE : PE equals' + DOTS,
       ['3', '8', '9', '1/8'], 1,
       ['PE = ½ k (A/3)² = E / 9', 'KE = E − E/9 = 8E / 9', 'KE : PE = 8']),
   mcq('A body of mass 0.5 kg oscillates with an amplitude of 4 cm and a frequency of 5 Hz. The maximum restoring '
       'force on it is' + DOTS, ['19.7 N', '9.86 N', '39.4 N', '0.63 N'], 0,
       ['ω = 2π f = 31.4 rad/s', 'F<sub>max</sub> = m ω² A = 0.5 × 986 × 0.04 ≈ 19.7 N'])])

q('A student finds that a body of unknown mass m<sub>1</sub> on a spring oscillates with a periodic time of 0.5 s. '
  'When a mass of 0.3 kg is added, the periodic time becomes 0.7 s:',
  [ess('Find the mass m<sub>1</sub>.',
       ['T² ∝ m → (0.7 / 0.5)² = (m<sub>1</sub> + 0.3) / m<sub>1</sub>', '1.96 m<sub>1</sub> = m<sub>1</sub> + 0.3',
        '0.96 m<sub>1</sub> = 0.3 → m<sub>1</sub> ≈ 0.31 kg'], 'm<sub>1</sub> ≈ 0.31 kg', 'm'),
   ess('Find the spring constant.', ['k = 4π² m<sub>1</sub> / T² = 39.44 × 0.3125 / 0.25', 'k ≈ 49.3 N/m'],
       'k ≈ 49.3 N/m', 'm')])

q('The graph shows the square of the periodic time T² of a mass&ndash;spring oscillator against the mass m:',
  [mcq('The spring constant equals' + DOTS, ['49.3 N/m', '0.8 N/m', '24.6 N/m', '98.6 N/m'], 0,
       ['T² = (4π² / k) m → slope = 4π² / k', 'slope = 0.4 / 0.5 = 0.8 s²/kg',
        'k = 4π² / 0.8 = 39.44 / 0.8 ≈ 49.3 N/m']),
   ess('Find the periodic time when a mass of 0.8 kg is used.', ['T² = 0.8 × 0.8 = 0.64 s²', 'T = 0.8 s'],
       'T = 0.8 s', 's')],
  G.graph_line(80, xt=(0, 0.25, 0.5), yt=(0, 0.2, 0.4), xl='m (kg)', yl='T&#178; (s&#178;)', neg=False,
               through=(0.5, 0.4), pt=(0.5, 0.4)), 'right')

q('The graph shows the displacement&ndash;time curve of a body in simple harmonic motion:',
  [mcq('The angular frequency of the motion is' + DOTS, ['6.28 rad/s', '3.14 rad/s', '12.56 rad/s', '2 rad/s'], 2,
       ['T = 0.5 s', 'ω = 2π / T = 6.28 / 0.5 = 12.56 rad/s']),
   ess('Write the equation of the displacement in metres.', ['A = 3 cm = 0.03 m , ω = 12.56 rad/s'],
       'x = 0.03 sin (12.56 t)', 's')],
  G.graph_xt(86, A=3, T=0.5, cycles=2), 'right')

q('A body starts its simple harmonic motion from the equilibrium position (x = A sin ωt):',
  [mcq('At t = T/8 the ratio KE : PE equals' + DOTS, ['1 : 1', '1 : 3', '3 : 1', '1 : 2'], 0,
       ['x = A sin (2π/T × T/8) = A sin 45° = A / √2', 'PE = ½ k A² / 2 = E / 2 → KE = E / 2', 'KE : PE = 1 : 1']),
   mcq('A body oscillates with an amplitude of 2.5 cm and a maximum acceleration of 10 m/s². Its frequency is' + DOTS,
       ['3.18 Hz', '20 Hz', '0.314 Hz', '400 Hz'], 0,
       ['ω² = a<sub>max</sub> / A = 10 / 0.025 = 400 → ω = 20 rad/s', 'f = ω / 2π = 20 / 6.28 = 3.18 Hz'])])

q('Give the scientific reason for each of the following:',
  [ess('The periodic time of a mass&ndash;spring oscillator does not depend on the amplitude.',
       ['A larger amplitude gives a larger restoring force and a larger acceleration,',
        'so the longer path is covered faster in the same time : T = 2π √(m/k) contains no A.'],
       'T depends only on m and k', 'm'),
   ess('The speed of the oscillating body is maximum at the equilibrium position.',
       ['There the potential energy is zero, so all the energy is kinetic.'], 'PE = 0 → KE is maximum', 'm'),
   ess('A horizontal mass&ndash;spring oscillator has the same periodic time on the Moon as on the Earth.',
       ['T = 2π √(m/k) does not contain g; the mass and the spring do not change.'],
       'T does not depend on g', 'm')])

q('A body of mass 1 kg oscillates on a horizontal spring of constant 100 N/m with an amplitude of 20 cm:',
  [mcq('Its speed at a displacement of 12 cm equals' + DOTS, ['2 m/s', '1.6 m/s', '1.2 m/s', '0.8 m/s'], 1,
       ['ω = √(100 / 1) = 10 rad/s', 'v = ω √(A² − x²) = 10 × √(0.04 − 0.0144) = 10 × 0.16 = 1.6 m/s']),
   ess('Find the kinetic and potential energies at that point, and check that their sum is constant.',
       ['KE = ½ m v² = ½ × 1 × (1.6)² = 1.28 J', 'PE = ½ k x² = ½ × 100 × (0.12)² = 0.72 J',
        'KE + PE = 2 J = ½ k A² = ½ × 100 × (0.2)² ✓'], 'KE = 1.28 J ,  PE = 0.72 J', 'm')],
  G.spring_block(96, mark_labels=('&#8722;20 cm', '0', '+20 cm')))

q('The total energy of a mass&ndash;spring oscillator is 0.9 J. The mass is 0.2 kg and the amplitude is 15 cm:',
  [ess('Find the maximum speed.', ['½ m v<sub>max</sub>² = E → v<sub>max</sub> = √(2 × 0.9 / 0.2) = 3 m/s'],
       'v<sub>max</sub> = 3 m/s', 's'),
   ess('Find the spring constant.', ['E = ½ k A² → k = 2E / A² = 1.8 / 0.0225 = 80 N/m'], 'k = 80 N/m', 's'),
   mcq('The periodic time equals' + DOTS, ['0.314 s', '0.628 s', '0.05 s', '3.14 s'], 0,
       ['T = 2π √(m / k) = 6.28 × √(0.2 / 80) = 6.28 × 0.05 = 0.314 s'])])

q('Choose the correct answer:',
  [mcq('If the mass of a mass&ndash;spring oscillator is made 4 times as large, its frequency becomes' + DOTS,
       ['4f', '2f', 'f / 2', 'f / 4'], 2, ['f ∝ 1 / √m → f′ = f / √4 = f / 2']),
   mcq('The SI unit of the spring constant is' + DOTS, ['N·m', 'N/m', 'N/s', 'N'], 1,
       ['k = F / x → newton / metre = N/m']),
   mcq('During one complete oscillation, the displacement of the body is' + DOTS, ['4A', '2A', 'A', 'zero'], 3,
       ['After one complete oscillation the body returns to its starting point, so the displacement is zero',
        '(the distance travelled is 4A).'])])

q('The displacement of a body is x = 6 sin (π t), where x is in cm and t in seconds:',
  [mcq('The first moment at which x = 3 cm is' + DOTS, ['0.5 s', '1/6 s', '1/3 s', '1/12 s'], 1,
       ['3 = 6 sin (πt) → sin (πt) = 0.5 → πt = π/6', 't = 1/6 s ≈ 0.167 s']),
   ess('Find the speed of the body at that moment.',
       ['v = ω √(A² − x²) = π √(36 − 9) = 3.14 × 5.2', 'v ≈ 16.3 cm/s'], 'v ≈ 16.3 cm/s', 'm')])

q('A body in simple harmonic motion passes its equilibrium position with a speed of 0.6 m/s. Its amplitude is 3 cm:',
  [mcq('Its angular frequency equals' + DOTS, ['0.2 rad/s', '2 rad/s', '18 rad/s', '20 rad/s'], 3,
       ['v<sub>max</sub> = ωA → ω = 0.6 / 0.03 = 20 rad/s']),
   ess('Find its periodic time.', ['T = 2π / ω = 6.28 / 20 = 0.314 s'], 'T = 0.314 s', 's'),
   ess('Find its acceleration when its displacement is 1.5 cm.', ['a = −ω² x = −400 × 0.015 = −6 m/s²'],
       'a = −6 m/s²', 's')])

q('A body of mass 0.4 kg is attached to a horizontal spring, pulled 5 cm from its equilibrium position and '
  'released. It makes 20 complete oscillations in 8 s:',
  [mcq('The periodic time equals' + DOTS, ['2.5 s', '0.4 s', '160 s', '0.8 s'], 1,
       ['T = time / number of oscillations = 8 / 20 = 0.4 s']),
   ess('Find the spring constant.', ['k = 4π² m / T² = 39.44 × 0.4 / 0.16', 'k ≈ 98.6 N/m'], 'k ≈ 98.6 N/m', 'm'),
   ess('Find its maximum speed.', ['ω = 2π / T = 15.7 rad/s', 'v<sub>max</sub> = ωA = 15.7 × 0.05 ≈ 0.785 m/s'],
       'v<sub>max</sub> ≈ 0.785 m/s', 's')])

q('A body in simple harmonic motion has an acceleration of magnitude 8 m/s² when its displacement is 2 cm:',
  [mcq('Its angular frequency equals' + DOTS, ['400 rad/s', '4 rad/s', '2 rad/s', '20 rad/s'], 3,
       ['|a| = ω² x → ω² = 8 / 0.02 = 400', 'ω = 20 rad/s']),
   ess('At what displacement is the magnitude of its acceleration 12 m/s²?',
       ['x = |a| / ω² = 12 / 400 = 0.03 m'], 'x = 3 cm', 's'),
   ess('Find the periodic time.', ['T = 2π / ω = 6.28 / 20 = 0.314 s'], 'T = 0.314 s', 's')])

q('Two bodies, each of mass 1 kg, oscillate on two springs of constants k<sub>1</sub> = 100 N/m and '
  'k<sub>2</sub> = 400 N/m, both with the same amplitude of 5 cm:',
  [mcq('The ratio of their frequencies f<sub>1</sub> / f<sub>2</sub> equals' + DOTS, ['2', '4', '1/4', '1/2'], 3,
       ['ω<sub>1</sub> = √(100 / 1) = 10 rad/s ,  ω<sub>2</sub> = √(400 / 1) = 20 rad/s',
        'f<sub>1</sub> / f<sub>2</sub> = ω<sub>1</sub> / ω<sub>2</sub> = 1/2']),
   ess('Find the ratio of their total energies E<sub>1</sub> / E<sub>2</sub>.',
       ['E = ½ k A², with the same A → E ∝ k', 'E<sub>1</sub> / E<sub>2</sub> = 100 / 400 = 1/4',
        '(E<sub>1</sub> = 0.125 J ,  E<sub>2</sub> = 0.5 J)'], 'E<sub>1</sub> / E<sub>2</sub> = 1/4', 'm'),
   ess('Find the ratio of their maximum speeds.',
       ['v<sub>max</sub> = ωA → v<sub>1</sub> / v<sub>2</sub> = 10 / 20 = 1/2',
        '(v<sub>1</sub> = 0.5 m/s ,  v<sub>2</sub> = 1 m/s)'], '1/2', 's')])

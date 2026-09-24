# -*- coding: utf-8 -*-
"""Chapter 2 - Lesson 1 : Moment of a Force.  40 questions with step-by-step model answers.
Sign convention used throughout : anticlockwise moment (+), clockwise moment (-)."""
import zb_figs as G

DOTS = ' <span class="dots">............</span>'


def mcq(t, ch, ok, steps, sp='s', cols=None):
    return dict(t=t, ch=ch, ok=ok, steps=steps, sp=sp, cols=cols)


def ess(t, steps, res, sp=''):
    return dict(t=t, steps=steps, res=res, sp=sp)


Q = []


def q(stem, parts, fig=None, figpos='below'):
    Q.append(dict(stem=stem, parts=parts, fig=fig, figpos=figpos))


# ------------------------------------------------------------------ medium 1 - 5
q('A mechanic tightens a bolt using a spanner of length 25 cm. He applies a force of 80 N at the end of the '
  'spanner, perpendicular to it, as shown in the figure:',
  [mcq('The moment of the force about the axis of the bolt equals' + DOTS,
       ['320 N·m', '20 N·m', '2000 N·m', '3.2 N·m'], 1,
       ['The force is perpendicular to the spanner, so the moment arm is the whole length :',
        'd = 25 cm = 0.25 m',
        'M = F × d = 80 × 0.25 = 20 N·m']),
   mcq('If he applies the same force at the middle of the spanner, the moment becomes' + DOTS,
       ['40 N·m', '20 N·m', '5 N·m', '10 N·m'], 3,
       ['d = 0.25 / 2 = 0.125 m',
        'M = F × d = 80 × 0.125 = 10 N·m',
        'M ∝ d : halving the arm halves the moment.'])],
  G.wrench(104))

q('The figure shows the top view of a door of width 0.9 m hinged at one side. Three forces F<sub>1</sub>, '
  'F<sub>2</sub> and F<sub>3</sub> act on the door, each separately:',
  [ess('Which of the three forces has <u>no</u> moment about the hinge? Explain your answer.',
       ['F<sub>2</sub> acts along the door, towards the hinge.',
        'Its line of action passes through the hinge, so its moment arm d = 0.',
        'M = F × d = F<sub>2</sub> × 0 = 0'],
       'F<sub>2</sub> : its line of action passes through the hinge', 'm'),
   mcq('If F<sub>1</sub> = F<sub>3</sub> = 30 N, the ratio between their moments M<sub>1</sub> : M<sub>3</sub> '
       'equals' + DOTS, ['1 : 2', '2 : 1', '1 : 1', '4 : 1'], 1,
       ['M<sub>1</sub> = 30 × 0.9 = 27 N·m',
        'M<sub>3</sub> = 30 × 0.45 = 13.5 N·m',
        'M<sub>1</sub> : M<sub>3</sub> = 27 : 13.5 = 2 : 1'])],
  G.door_top(104))

q('A light rod OA of length 0.5 m can rotate about a pivot at O. A force of 40 N acts at the end A, '
  'making an angle of 30° with the rod as shown:',
  [mcq('The moment arm of the force about O (the perpendicular distance from O to the line of action) '
       'equals' + DOTS, ['0.5 m', '0.43 m', '0.25 m', '0.87 m'], 2,
       ['d = L sin θ = 0.5 × sin 30°',
        'd = 0.5 × 0.5 = 0.25 m']),
   mcq('The moment of the force about O equals' + DOTS,
       ['+10 N·m', '+17.3 N·m', '+20 N·m', '−10 N·m'], 0,
       ['M = F L sin θ = 40 × 0.5 × sin 30° = 10 N·m',
        'The force turns the rod anticlockwise, so the moment is positive : M = +10 N·m'])],
  G.rod_30(96))

q('Choose the correct answer:',
  [mcq('The SI unit of the moment of a force is' + DOTS, ['N', 'N/m', 'J', 'N·m'], 3,
       ['M = F × d → newton × metre = N·m']),
   mcq('The moment of a force about a point equals zero when' + DOTS,
       ['the force is perpendicular to the arm', 'the line of action of the force passes through the point',
        'the force is very large', 'the arm is very long'], 1,
       ['If the line of action passes through the point, the moment arm d = 0,',
        'so M = F × 0 = 0 whatever the size of the force.']),
   mcq('Door handles are fixed at the edge farthest from the hinges in order to' + DOTS,
       ['increase the force needed to open the door', 'decrease the moment of the force',
        'increase the moment arm, so a smaller force gives the needed moment', 'make the door lighter'], 2,
       ['M = F × d : for the same moment, a larger arm d needs a smaller force F.'])])

q('A light rod AB of length 1.2 m is pivoted at its midpoint O. Three forces act on it as shown: 20 N '
  'downwards at A, 30 N downwards at B, and 25 N upwards at C, where OC = 0.3 m:',
  [mcq('The moment of the 30 N force about O equals' + DOTS, ['+18 N·m', '−9 N·m', '−18 N·m', '+9 N·m'], 2,
       ['M = F × d = 30 × 0.6 = 18 N·m',
        'B is to the right of O and the force is downwards → clockwise',
        'M = −18 N·m']),
   ess('Calculate the net moment about O, and state the direction in which the rod starts to rotate.',
       ['20 N at A : +20 × 0.6 = +12 N·m   (anticlockwise)',
        '30 N at B : −30 × 0.6 = −18 N·m   (clockwise)',
        '25 N at C : +25 × 0.3 = +7.5 N·m   (anticlockwise)',
        'ΣM = 12 − 18 + 7.5 = +1.5 N·m'],
       'ΣM = +1.5 N·m → the rod starts to rotate anticlockwise', 'm')],
  G.rod_three(112))

# ------------------------------------------------------------------ hard 6 - 40
q('A force F = 60 N acts at point P of a rigid body that can rotate about O, where OP = 0.5 m. '
  'The magnitude of the moment of F about O is 15 N·m:',
  [mcq('The angle between the force and the line OP could be' + DOTS,
       ['30° only', '60° only', '90°', '30° or 150°'], 3,
       ['M = F r sin θ → sin θ = M / (F r) = 15 / (60 × 0.5) = 0.5',
        'sin θ = 0.5 has two answers between 0° and 180° :',
        'θ = 30°  or  θ = 150°']),
   ess('Find the smallest force that, acting at P, gives the same moment, and state its direction.',
       ['M = F r sin θ is largest for a given F when sin θ = 1 (θ = 90°)',
        'F<sub>min</sub> = M / r = 15 / 0.5 = 30 N'],
       'F<sub>min</sub> = 30 N, perpendicular to OP', 'm')])

q('A stuck nut needs a moment of 36 N·m to loosen it. The only handle available is bent, and a force can '
  'be applied only at its end P, which is 0.3 m horizontally and 0.4 m vertically from the centre O of '
  'the nut, as shown:',
  [ess('Find the minimum force needed at P, and state its direction.',
       ['OP = √(0.3² + 0.4²) = √0.25 = 0.5 m',
        'The largest moment arm possible is OP itself, reached when F ⊥ OP',
        'F<sub>min</sub> = M / OP = 36 / 0.5 = 72 N'],
       'F<sub>min</sub> = 72 N, perpendicular to OP', 'm'),
   mcq('If the force at P must be <u>horizontal</u>, its magnitude is' + DOTS,
       ['90 N', '72 N', '120 N', '60 N'], 0,
       ['For a horizontal force the moment arm is the vertical distance of P from O : d = 0.4 m',
        'F = M / d = 36 / 0.4 = 90 N']),
   mcq('If the force at P must be <u>vertical</u>, its magnitude is' + DOTS,
       ['72 N', '90 N', '150 N', '120 N'], 3,
       ['For a vertical force the moment arm is the horizontal distance of P from O : d = 0.3 m',
        'F = M / d = 36 / 0.3 = 120 N'])],
  G.bent_handle(74), 'right')

q('A uniform rod OA of length 2 m and weight 50 N is pivoted at O and held at 30° above the horizontal. '
  'A vertical force of 40 N acts upwards at its end A:',
  [ess('Calculate the moment of the weight about O.',
       ['The weight acts at the midpoint G, 1 m from O along the rod',
        'moment arm = horizontal distance of G = 1 × cos 30° = 0.866 m',
        'M<sub>W</sub> = −50 × 0.866 = −43.3 N·m   (clockwise)'],
       'M<sub>W</sub> = −43.3 N·m', 'm'),
   ess('Calculate the moment of the 40 N force about O.',
       ['moment arm = horizontal distance of A = 2 × cos 30° = 1.732 m',
        'M = +40 × 1.732 = +69.3 N·m   (anticlockwise)'],
       'M = +69.3 N·m', 'm'),
   mcq('The net moment about O is' + DOTS,
       ['+26 N·m, the rod rises', '−26 N·m, the rod falls', '+113 N·m, the rod rises', 'zero'], 0,
       ['ΣM = +69.3 − 43.3 = +26 N·m',
        'positive → anticlockwise → the rod starts to rise'])],
  G.inclined_rod(92))

q('The graph shows how the moment of a constant force F about the hinge of a door changes with the angle θ '
  'between F and the door, when F always acts at the handle, 0.8 m from the hinge:',
  [mcq('The magnitude of F is' + DOTS, ['19.2 N', '24 N', '30 N', '38.4 N'], 2,
       ['The maximum moment (at θ = 90°) is M<sub>max</sub> = F × d',
        'F = M<sub>max</sub> / d = 24 / 0.8 = 30 N']),
   mcq('The moment when θ = 30° is' + DOTS, ['6 N·m', '12 N·m', '20.8 N·m', '24 N·m'], 1,
       ['M = F d sin θ = 24 × sin 30° = 12 N·m']),
   ess('At which two angles does the moment equal 20.8 N·m?',
       ['sin θ = M / M<sub>max</sub> = 20.8 / 24 = 0.866',
        'θ = 60°  or  θ = 180° − 60° = 120°'],
       'θ = 60° and θ = 120°', 'm')],
  G.graph_m_theta(88), 'right')

q('A force of constant magnitude acts on a rod pivoted at O, always making an angle of 30° with the rod. '
  'The graph shows the moment of the force about O against the distance d between O and the point where '
  'the force acts:',
  [mcq('The slope of the line represents' + DOTS, ['F', 'F sin θ', 'F cos θ', 'F / d'], 1,
       ['M = F d sin θ = (F sin θ) × d',
        'M is proportional to d, and the constant of proportionality (the slope) is F sin θ']),
   mcq('The magnitude of the force is' + DOTS, ['15 N', '17.3 N', '30 N', '7.5 N'], 2,
       ['slope = 6 / 0.4 = 15 N',
        'F sin 30° = 15  →  F = 15 / 0.5 = 30 N'])],
  G.graph_m_d(86), 'right')

q('In each of the four figures a force acts at the end of a light rod pivoted at one end. '
  '(Take sin 53° = 0.8)',
  [mcq('The figure in which the force has the <u>largest</u> moment about the pivot is' + DOTS,
       ['(a)', '(b)', '(c)', '(d)'], 2,
       ['(a) M = 20 × 0.5 = 10 N·m',
        '(b) M = 40 × 0.5 × sin 30° = 10 N·m',
        '(c) M = 25 × 0.6 × sin 53° = 25 × 0.6 × 0.8 = 12 N·m',
        '(d) M = 30 × 0.3 = 9 N·m',
        'The largest is (c), although (b) has the largest force.']),
   mcq('The two figures in which the forces have equal moments are' + DOTS,
       ['(a) and (d)', '(b) and (c)', '(c) and (d)', '(a) and (b)'], 3,
       ['From part I : (a) and (b) both give 10 N·m.'])],
  G.four_panels(150))

q('A cyclist pushes vertically downwards on a pedal with a constant force of 300 N. The crank that joins '
  'the pedal to the axle O is 17 cm long:',
  [mcq('The maximum moment of this force about the axle is' + DOTS, ['25.5 N·m', '44.2 N·m', '51 N·m', '5100 N·m'], 2,
       ['The moment arm is largest (= 0.17 m) when the crank is horizontal',
        'M<sub>max</sub> = 300 × 0.17 = 51 N·m']),
   ess('Calculate the moment when the crank makes 60° with the vertical, as in the figure.',
       ['The force is vertical, so the angle between F and the crank = 60°',
        'M = F L sin θ = 300 × 0.17 × sin 60° = 44.2 N·m'],
       'M ≈ 44.2 N·m', 'm'),
   ess('In which position of the crank is the moment of this force zero? Why?',
       ['When the crank is vertical (pedal at the top or at the bottom),',
        'the vertical force acts along the crank and its line of action passes through O → d = 0'],
       'crank vertical → M = 0', 's')],
  G.bicycle_crank(78), 'right')

q('A force F acts at point P as shown. The dashed line is its line of action, and O is a fixed point:',
  [mcq('If the force (same magnitude and direction) is moved to point Q on its line of action, its moment '
       'about O' + DOTS, ['increases', 'decreases', 'does not change', 'becomes zero'], 2,
       ['M = F × d, where d is the perpendicular distance from O to the line of action',
        'Moving the force along its own line of action does not change d, so M stays the same.']),
   mcq('If the force is moved to point R on a parallel line nearer to O, its moment about O' + DOTS,
       ['increases', 'decreases', 'does not change', 'is reversed'], 1,
       ['The new line of action is nearer to O, so d is smaller → M = F d decreases.'])],
  G.line_of_action(90))

q('A force F acts perpendicular to a straight line on which the points A and B lie, as shown. The moment of F '
  'about A is 12 N·m, and its moment about B, which is 0.2 m farther from the line of action, is 20 N·m:',
  [mcq('The magnitude of F is' + DOTS, ['40 N', '60 N', '100 N', '160 N'], 0,
       ['M<sub>A</sub> = F d<sub>A</sub>  and  M<sub>B</sub> = F (d<sub>A</sub> + 0.2)',
        'M<sub>B</sub> − M<sub>A</sub> = F × 0.2',
        '20 − 12 = 0.2 F  →  F = 40 N']),
   ess('Find the distance between A and the line of action of F.',
       ['d<sub>A</sub> = M<sub>A</sub> / F = 12 / 40 = 0.3 m'], 'd<sub>A</sub> = 0.3 m', 's')],
  G.two_points(90))

q('ABCD is a square plate of side 0.4 m. Four forces act along its sides as shown: 10 N along AB, 20 N along '
  'BC, 30 N along CD and 40 N along DA:',
  [mcq('The net moment of the four forces about A is' + DOTS,
       ['+28 N·m', '+20 N·m', '+40 N·m', 'zero'], 1,
       ['10 N and 40 N act along lines through A → zero moment',
        '20 N (up the side BC) : +20 × 0.4 = +8 N·m',
        '30 N (along CD, 0.4 m above A) : +30 × 0.4 = +12 N·m',
        'ΣM<sub>A</sub> = 8 + 12 = +20 N·m (anticlockwise)']),
   ess('Calculate the net moment about B.',
       ['10 N and 20 N act along lines through B → zero moment',
        '30 N along CD, 0.4 m above B : +30 × 0.4 = +12 N·m',
        '40 N along DA, 0.4 m to the left of B : +40 × 0.4 = +16 N·m',
        'ΣM<sub>B</sub> = 12 + 16 = +28 N·m'],
       'ΣM<sub>B</sub> = +28 N·m', 'm'),
   ess('Calculate the net moment about the centre O of the plate.',
       ['Each force is 0.2 m from O, and all of them turn the plate anticlockwise',
        'ΣM<sub>O</sub> = 0.2 × (10 + 20 + 30 + 40) = +20 N·m',
        'The same forces give different net moments about different points.'],
       'ΣM<sub>O</sub> = +20 N·m', 'm')],
  G.square_plate(76), 'right')

q('The jib OB of a crane is 12 m long, pivoted at O and inclined at 53° to the horizontal. A load of '
  'weight 5000 N hangs from its end B. (Take sin 53° = 0.8, cos 53° = 0.6)',
  [mcq('The moment of the load about O is' + DOTS,
       ['−4.8 × 10<sup>4</sup> N·m', '−3.6 × 10<sup>4</sup> N·m', '−6.0 × 10<sup>4</sup> N·m', 'zero'], 1,
       ['The weight is vertical, so its moment arm is the horizontal distance of B from O',
        'd = 12 cos 53° = 12 × 0.6 = 7.2 m',
        'M = −5000 × 7.2 = −3.6 × 10<sup>4</sup> N·m   (clockwise)']),
   mcq('If the jib is lowered to 37° with the horizontal, the magnitude of the moment of the load' + DOTS,
       ['increases to 4.8 × 10<sup>4</sup> N·m', 'decreases to 2.4 × 10<sup>4</sup> N·m',
        'does not change', 'becomes zero'], 0,
       ['d = 12 cos 37° = 12 × 0.8 = 9.6 m',
        '|M| = 5000 × 9.6 = 4.8 × 10<sup>4</sup> N·m → it increases']),
   ess('At what position of the jib is the moment of the load about O equal to zero?',
       ['When the jib is vertical, B is directly above O,',
        'so the weight\'s line of action passes through O → d = 0'],
       'jib vertical (90° with the horizontal)', 's')],
  G.crane(82), 'right')

q('The forearm is held horizontal. The biceps muscle pulls vertically upwards with a force of 250 N at a point '
  '4 cm from the elbow E, and the hand holds a ball of weight 30 N at 32 cm from E. '
  '(Neglect the weight of the forearm.)',
  [mcq('The moment of the ball\'s weight about the elbow is' + DOTS,
       ['−9.6 N·m', '+9.6 N·m', '−0.96 N·m', '−96 N·m'], 0,
       ['M = −30 × 0.32 = −9.6 N·m   (clockwise)']),
   ess('Calculate the net moment about the elbow, and state what happens to the forearm.',
       ['biceps : M = +250 × 0.04 = +10 N·m   (anticlockwise)',
        'ΣM = +10 − 9.6 = +0.4 N·m'],
       'ΣM = +0.4 N·m → the forearm starts to rise', 'm'),
   ess('Explain why the biceps must exert a force much larger than the weight of the ball.',
       ['Its moment arm (4 cm) is 8 times shorter than that of the ball (32 cm),',
        'so to give a comparable moment its force must be about 8 times larger.'],
       'the moment arm of the muscle is very short', 's')],
  G.forearm(100))

q('A wheel of radius 0.3 m can rotate about its axle O. Four forces act on its rim as shown:',
  [ess('What is the moment of the 80 N force about O? Why?',
       ['The 80 N force acts along the radius, towards O,',
        'so its line of action passes through O → d = 0 → M = 0'],
       'zero', 's'),
   mcq('The moment of the 60 N force about O equals' + DOTS,
       ['−18 N·m', '+9 N·m', '−9 N·m', '−15.6 N·m'], 2,
       ['Only the component perpendicular to the radius turns the wheel :',
        'F<sub>⊥</sub> = 60 sin 30° = 30 N  (vertically upwards at the left point)',
        'M = −30 × 0.3 = −9 N·m   (clockwise)']),
   ess('Calculate the net moment about O and the direction of rotation.',
       ['50 N at the top, to the right : −50 × 0.3 = −15 N·m',
        '40 N at the bottom, to the right : +40 × 0.3 = +12 N·m',
        '80 N : 0      60 N : −9 N·m',
        'ΣM = −15 + 12 + 0 − 9 = −12 N·m'],
       'ΣM = −12 N·m → clockwise', 'm')],
  G.wheel(82), 'right')

q('A door of width 1 m is hinged at one side. Student 1 pushes at the handle with a force making 30° with '
  'the door, while student 2 pushes perpendicular to the door at its middle, as shown:',
  [mcq('If the two students produce moments of equal magnitude, the ratio F<sub>1</sub> / F<sub>2</sub> is' + DOTS,
       ['1/2', '2', '1', '4'], 2,
       ['M<sub>1</sub> = F<sub>1</sub> × 1 × sin 30° = 0.5 F<sub>1</sub>',
        'M<sub>2</sub> = F<sub>2</sub> × 0.5',
        '0.5 F<sub>1</sub> = 0.5 F<sub>2</sub>  →  F<sub>1</sub> / F<sub>2</sub> = 1']),
   ess('If F<sub>1</sub> = 60 N and F<sub>2</sub> = 50 N, find the net moment about the hinge and state whose push '
       'wins.',
       ['M<sub>1</sub> = +60 × 1 × 0.5 = +30 N·m',
        'M<sub>2</sub> = −50 × 0.5 = −25 N·m',
        'ΣM = +5 N·m'],
       'ΣM = +5 N·m → the door turns in the direction of student 1', 'm')],
  G.door_two(100))

q('A nut needs a moment of 120 N·m to loosen it. A mechanic can exert a force of at most 300 N:',
  [mcq('The shortest spanner he can use (pushing perpendicular to it) has length' + DOTS,
       ['0.25 m', '0.6 m', '2.5 m', '0.4 m'], 3,
       ['d<sub>min</sub> = M / F<sub>max</sub> = 120 / 300 = 0.4 m']),
   ess('He has only a 0.25 m spanner, so he slips a pipe over it to make its effective length 0.6 m. '
       'Because of the space around the nut, his 300 N force makes 60° with the handle, as shown. '
       'Will the nut be loosened? Show your calculation.',
       ['M = F L sin θ = 300 × 0.6 × sin 60°',
        'M = 300 × 0.6 × 0.866 = 155.9 N·m',
        '155.9 N·m > 120 N·m'],
       'yes : M ≈ 156 N·m, more than the 120 N·m needed', 'l')],
  G.pipe_extension(104))

q('A force of 50 N acts along the line joining the points P (0.6 m, 0) and Q (0, 0.8 m), directed from P '
  'towards Q, as shown:',
  [mcq('The perpendicular distance from the origin O to the line of action is' + DOTS,
       ['0.6 m', '0.8 m', '0.48 m', '0.5 m'], 2,
       ['OPQ is a right-angled triangle with legs 0.6 m and 0.8 m, so PQ = 1.0 m',
        'twice its area = 0.6 × 0.8 = PQ × d',
        'd = 0.48 / 1.0 = 0.48 m']),
   ess('Calculate the moment of the force about O, and check your answer by resolving the force at P.',
       ['M = F d = 50 × 0.48 = 24 N·m, anticlockwise → +24 N·m',
        'check : at P the force has components 30 N (horizontal) and 40 N (vertical)',
        'the horizontal component lies along the x-axis, through O → no moment',
        'the vertical component : M = +40 × 0.6 = +24 N·m ✓'],
       'M = +24 N·m', 'l')],
  G.axes_pq(78), 'right')

q('A force whose horizontal component is 30 N and vertical component is 40 N acts at point A, which is 0.5 m '
  'to the right of and 0.2 m above the pivot O, as shown:',
  [ess('Calculate the moment of each component about O.',
       ['vertical 40 N : arm = 0.5 m → M = +40 × 0.5 = +20 N·m',
        'horizontal 30 N (to the right, above O) : arm = 0.2 m → M = −30 × 0.2 = −6 N·m'],
       '+20 N·m and −6 N·m', 'm'),
   mcq('The moment of the force itself about O equals' + DOTS,
       ['+26 N·m', '+25 N·m', '+14 N·m', '+20 N·m'], 2,
       ['The moment of a force = the sum of the moments of its components',
        'M = +20 − 6 = +14 N·m']),
   ess('Find the moment arm of the force about O.',
       ['F = √(30² + 40²) = 50 N',
        'd = M / F = 14 / 50 = 0.28 m'],
       'd = 0.28 m', 's')],
  G.components(80), 'right')

q('Two children sit on a light plank pivoted at its centre: a child of weight 300 N sits 1.5 m to the left '
  'of the pivot, and a child of weight 450 N sits 1.2 m to the right:',
  [mcq('The net moment about the pivot is' + DOTS,
       ['+90 N·m, anticlockwise', 'zero', '−990 N·m, clockwise', '−90 N·m, clockwise'], 3,
       ['left child : +300 × 1.5 = +450 N·m',
        'right child : −450 × 1.2 = −540 N·m',
        'ΣM = 450 − 540 = −90 N·m → clockwise']),
   ess('Where should a third child of weight 200 N sit to make the net moment zero?',
       ['an extra +90 N·m is needed → the child sits on the left',
        '200 × d = 90  →  d = 0.45 m'],
       '0.45 m to the left of the pivot', 'm'),
   mcq('Without the third child, if the 450 N child moves 0.2 m towards the pivot, the plank' + DOTS,
       ['turns clockwise', 'turns anticlockwise', 'does not start to rotate', 'turns about the child'], 2,
       ['right child : −450 × 1.0 = −450 N·m',
        'ΣM = +450 − 450 = 0 → no rotation'])],
  G.seesaw(104))

q('A rod OA of length 0.8 m is pivoted at O and makes 37° with the vertical. A constant horizontal force of '
  '25 N acts at A as shown. (Take sin 37° = 0.6, cos 37° = 0.8)',
  [mcq('The moment of the force about O is' + DOTS, ['−16 N·m', '−12 N·m', '+16 N·m', '−20 N·m'], 0,
       ['For a horizontal force, the moment arm is the vertical height of A above O',
        'd = 0.8 cos 37° = 0.8 × 0.8 = 0.64 m',
        'M = −25 × 0.64 = −16 N·m   (clockwise)']),
   mcq('The moment of this force about O is largest when the rod is' + DOTS,
       ['horizontal', 'at 45°', 'vertical', 'at 37° with the horizontal'], 2,
       ['The arm (the height of A) is largest when the rod is vertical : d = 0.8 m',
        'M<sub>max</sub> = 25 × 0.8 = 20 N·m']),
   ess('At what position of the rod is the moment of this force zero? Why?',
       ['When the rod is horizontal, the horizontal force acts along the rod,',
        'its line of action passes through O → d = 0'],
       'rod horizontal → M = 0', 's')],
  G.rod_phi(72), 'right')

q('Give the scientific reason for each of the following:',
  [ess('Door handles are placed at the edge of the door farthest from the hinges.',
       ['M = F × d : the largest moment arm gives the needed moment with the smallest force.'],
       'largest moment arm → smallest force needed', 'm'),
   ess('Pushing a door towards its hinges does not open it, however large the force is.',
       ['The line of action of the force passes through the axis of rotation (the hinges),',
        'so d = 0 and M = F × 0 = 0.'],
       'the moment arm is zero', 'm'),
   ess('The moment of a force is measured in N·m but not in joules, although 1 N·m = 1 J.',
       ['The joule is the unit of work and energy, where the distance is along the displacement.',
        'In the moment, the distance is perpendicular to the force and nothing is displaced by it;',
        'the moment measures a turning effect (a vector), not energy.'],
       'the moment is a turning effect, not work or energy', 'm')])

q('A uniform horizontal pole AB of length 2 m and weight 40 N is fixed to a wall at A. A sign of weight 60 N '
  'hangs from its end B, and a cable attached at B makes 30° with the pole, as shown:',
  [mcq('The total moment of the two weights about A is' + DOTS,
       ['−100 N·m', '−200 N·m', '−160 N·m', '−120 N·m'], 2,
       ['pole weight at its middle : −40 × 1 = −40 N·m',
        'sign at B : −60 × 2 = −120 N·m',
        'total = −160 N·m (clockwise)']),
   ess('If the tension in the cable is 250 N, calculate the net moment about A.',
       ['moment of T : +T × 2 × sin 30° = +250 × 2 × 0.5 = +250 N·m',
        'ΣM = +250 − 160 = +90 N·m'],
       'ΣM = +90 N·m', 'm'),
   mcq('The tension that makes the net moment about A equal to zero is' + DOTS,
       ['160 N', '80 N', '320 N', '185 N'], 0,
       ['T × 2 × sin 30° = 160',
        'T × 1 = 160  →  T = 160 N'])],
  G.sign_pole(88), 'right')

q('A force F = 20 N acts at point P of a rod pivoted at O, where OP = 0.5 m. The line of action of the force '
  'passes at a perpendicular distance of 0.3 m from O, as shown:',
  [mcq('The moment arm of the force about O is' + DOTS, ['0.5 m', '0.3 m', '0.4 m', '0.8 m'], 1,
       ['The moment arm is the perpendicular distance from O to the line of action,',
        'not the distance OP : d = 0.3 m']),
   ess('Calculate the moment of the force about O and the angle between F and the rod.',
       ['M = F × d = 20 × 0.3 = 6 N·m, anticlockwise → +6 N·m',
        'd = OP sin θ → sin θ = 0.3 / 0.5 = 0.6 → θ = 37°'],
       'M = +6 N·m ,  θ = 37°', 'm')],
  G.moment_arm(86), 'right')

q('Two forces F<sub>1</sub> and F<sub>2</sub> act on a rod pivoted at O. F<sub>1</sub> acts perpendicular to the '
  'rod at a distance d from O, while F<sub>2</sub> acts at a distance 3d, making 30° with the rod:',
  [mcq('If the two moments are equal in magnitude, then F<sub>1</sub> / F<sub>2</sub> equals' + DOTS,
       ['1/3', '3', '2/3', '3/2'], 3,
       ['F<sub>1</sub> × d = F<sub>2</sub> × 3d × sin 30°',
        'F<sub>1</sub> = 1.5 F<sub>2</sub>  →  F<sub>1</sub> / F<sub>2</sub> = 3/2']),
   mcq('If F<sub>2</sub> is turned (at the same point) to become perpendicular to the rod, its moment becomes' + DOTS,
       ['half its value', 'twice its value', 'three times its value', 'unchanged'], 1,
       ['M ∝ sin θ : sin 90° / sin 30° = 1 / 0.5 = 2'])])

q('Choose the correct answer:',
  [mcq('The force acting on a rod is doubled, the distance from the pivot to its point of application is doubled, '
       'and the angle between the force and the rod changes from 90° to 30°. The moment becomes' + DOTS,
       ['four times', 'twice', 'the same', 'half'], 1,
       ['M = F L sin θ',
        'M′ / M = (2 × 2 × sin 30°) / (1 × 1 × sin 90°) = 4 × 0.5 = 2']),
   mcq('A force is halved while its angle with the rod changes from 30° to 90° (same point). Its moment' + DOTS,
       ['is halved', 'is doubled', 'does not change', 'is quartered'], 2,
       ['M′ / M = (0.5 × sin 90°) / (1 × sin 30°) = 0.5 / 0.5 = 1'])])

q('A uniform trapdoor OA of length 1.2 m and weight 120 N is hinged at O and held horizontal. A rope pulls '
  'its free end A with a tension of 150 N at 30° to the door, as shown:',
  [ess('Calculate the net moment about O, and state whether the trapdoor starts to rise or to fall.',
       ['weight at the middle : −120 × 0.6 = −72 N·m',
        'rope at A : +150 × 1.2 × sin 30° = +90 N·m',
        'ΣM = −72 + 90 = +18 N·m → anticlockwise'],
       'ΣM = +18 N·m → the trapdoor starts to rise', 'm'),
   mcq('If the rope were tied at the middle of the door instead (same tension, same angle), the trapdoor' + DOTS,
       ['would start to rise', 'would stay at rest', 'would start to fall', 'would slide'], 2,
       ['rope : +150 × 0.6 × 0.5 = +45 N·m',
        'ΣM = −72 + 45 = −27 N·m → clockwise → it falls']),
   mcq('With the rope at A and at 30°, the smallest tension that just starts to raise the door is (just above)' + DOTS,
       ['60 N', '144 N', '240 N', '120 N'], 3,
       ['T × 1.2 × sin 30° = 72',
        '0.6 T = 72  →  T = 120 N'])],
  G.trapdoor(96))

q('A force of 20 N acts upwards, perpendicular to a rod AB of length 1 m, at point C where AC = 0.3 m, '
  'as shown:',
  [mcq('The moment of the force about A is' + DOTS, ['+6 N·m', '−6 N·m', '+14 N·m', '−14 N·m'], 0,
       ['C is 0.3 m to the right of A and the force is upwards → anticlockwise',
        'M<sub>A</sub> = +20 × 0.3 = +6 N·m']),
   ess('Calculate the moment of the same force about B and about C.',
       ['about B : C is 0.7 m to the left of B, force upwards → clockwise',
        'M<sub>B</sub> = −20 × 0.7 = −14 N·m',
        'about C : the force passes through C → M<sub>C</sub> = 0'],
       'M<sub>B</sub> = −14 N·m ,  M<sub>C</sub> = 0', 'm'),
   ess('What do you conclude?',
       ['The moment of a force depends on the point it is taken about :',
        'its value and even its sign can change.'],
       'the moment depends on the chosen point', 's')],
  G.rod_c(92))

q('A rod OA of length 1.5 m is pivoted at O and makes 40° with the horizontal. A force of 20 N acts at A '
  'at 70° above the horizontal, as shown:',
  [mcq('The moment of the force about O is' + DOTS, ['−15 N·m', '+15 N·m', '+26 N·m', '+28.2 N·m'], 1,
       ['The angle between the force and the rod = 70° − 40° = 30°',
        'M = F L sin θ = 20 × 1.5 × sin 30° = 15 N·m',
        'The force is turned anticlockwise relative to the rod → M = +15 N·m']),
   ess('The force keeps its magnitude but is turned to act at 10° above the horizontal. Find the new moment.',
       ['The angle between the force and the rod = 40° − 10° = 30°, but now on the other side of the rod',
        'M = 20 × 1.5 × sin 30° = 15 N·m, clockwise'],
       'M = −15 N·m', 'm')],
  G.rod_40_70(82), 'right')

q('The graph shows the moment M against the force F for two spanners X and Y, when the force is always '
  'applied perpendicular to the end of each spanner:',
  [mcq('The longer spanner is' + DOTS, ['X', 'Y', 'both are equal', 'it cannot be known'], 0,
       ['M = F d → the slope of each line equals the length d of the spanner',
        'X has the steeper line → X is longer']),
   ess('Find the length of each spanner.',
       ['X : d = 18 / 60 = 0.3 m', 'Y : d = 12 / 60 = 0.2 m'], 'X = 0.3 m ,  Y = 0.2 m', 'm'),
   ess('What force is needed with spanner Y to produce a moment of 18 N·m?',
       ['F = M / d = 18 / 0.2 = 90 N'], 'F = 90 N', 's')],
  G.graph_m_f(86), 'right')

q('A force acting on a body pivoted at O produces a clockwise moment of 12 N·m:',
  [mcq('If the force is reversed in direction (same line of action), its moment becomes' + DOTS,
       ['+12 N·m', '−12 N·m', 'zero', '−24 N·m'], 0,
       ['Reversing the force reverses the sense of rotation:',
        '−12 N·m (clockwise) → +12 N·m (anticlockwise)']),
   mcq('If instead the force is doubled and its line of action is moved parallel to itself halfway towards O, '
       'the moment becomes' + DOTS, ['−24 N·m', '−6 N·m', '+12 N·m', '−12 N·m'], 3,
       ['M′ = (2F) × (d / 2) = F d',
        'The moment is unchanged : −12 N·m'])])

q('A force of 25 N acts on a door at 53° to the plane of the door, at an unknown distance x from the hinge. '
  'Its moment about the hinge is 16 N·m. (Take sin 53° = 0.8)',
  [mcq('The distance x equals' + DOTS, ['0.64 m', '1.07 m', '0.8 m', '0.6 m'], 2,
       ['M = F x sin θ',
        '16 = 25 × x × 0.8  →  x = 16 / 20 = 0.8 m']),
   ess('Find the force acting perpendicular to the door at the same point that gives the same moment.',
       ['F<sub>⊥</sub> × 0.8 = 16  →  F<sub>⊥</sub> = 20 N',
        '(it equals the perpendicular component of the 25 N force : 25 × 0.8 = 20 N)'],
       'F<sub>⊥</sub> = 20 N', 'm')],
  G.door_53(96))

q('Four forces act on a light rod OA of length 1 m pivoted at O, as shown: 16 N at 0.25 m making 53° with the '
  'rod, 20 N at the middle making 30° below the rod, 10 N at A perpendicular to the rod, and 30 N at A along '
  'the rod. (Take sin 53° = 0.8)',
  [ess('What is the moment of the 30 N force about O? Why?',
       ['It acts along the rod, so its line of action passes through O → d = 0 → M = 0'], 'zero', 's'),
   mcq('The net moment about O is' + DOTS, ['+18.2 N·m', '+8.2 N·m', '−8.2 N·m', '+11.8 N·m'], 1,
       ['16 N : +16 × 0.25 × sin 53° = +16 × 0.25 × 0.8 = +3.2 N·m',
        '20 N : −20 × 0.5 × sin 30° = −5 N·m (it turns the rod clockwise)',
        '10 N : +10 × 1 = +10 N·m      30 N : 0',
        'ΣM = 3.2 − 5 + 10 + 0 = +8.2 N·m (anticlockwise)'])],
  G.rod_four(112))

q('A ladder 5 m long rests with its foot O on the ground and its top against a smooth wall, making 53° with '
  'the ground. A man of weight 700 N stands 3 m up the ladder, and the wall pushes the top of the ladder '
  'horizontally with a force R = 400 N. (Take sin 53° = 0.8, cos 53° = 0.6)',
  [mcq('The moment of the man\'s weight about O is' + DOTS,
       ['−2100 N·m', '−1680 N·m', '−1260 N·m', '−1470 N·m'], 2,
       ['moment arm = horizontal distance of the man from O = 3 cos 53° = 1.8 m',
        'M = −700 × 1.8 = −1260 N·m   (clockwise)']),
   ess('Calculate the moment of R about O.',
       ['R is horizontal, so its arm is the height of the top of the ladder : 5 sin 53° = 4 m',
        'M = +400 × 4 = +1600 N·m   (anticlockwise)'],
       'M<sub>R</sub> = +1600 N·m', 'm'),
   mcq('As the man climbs higher, the moment of his weight about O' + DOTS,
       ['increases', 'decreases', 'does not change', 'becomes zero'], 0,
       ['His horizontal distance from O increases as he climbs → the moment arm increases.'])],
  G.ladder(80), 'right')

q('Choose the correct answer:',
  [mcq('If the moment of a force about a point O is zero, then the force' + DOTS,
       ['must be zero', 'is perpendicular to the arm', 'is zero or its line of action passes through O',
        'must be very small'], 2,
       ['M = F d = 0 → either F = 0 or d = 0 (line of action through O).']),
   mcq('Which of the following does <u>not</u> change the moment of a force about a point?',
       ['changing the magnitude of the force', 'changing the angle between the force and the arm',
        'moving the point about which the moment is taken', 'sliding the force along its line of action'], 3,
       ['Sliding along the line of action keeps the perpendicular distance d the same.']),
   mcq('The moment of a force about a point equals the force multiplied by' + DOTS,
       ['the perpendicular distance between the point and the line of action',
        'the distance between the point and the point of application',
        'the length of the body', 'the displacement of the body'], 0,
       ['This is the definition : M = F × d, with d the perpendicular distance.'])])

q('The minute hand of a wall clock has a weight of 0.2 N acting at its midpoint, 6 cm from the centre of the '
  'clock. In the figure the hand points at the 10 o\'clock mark (50 minutes):',
  [mcq('The moment of the weight of the hand about the centre is largest when the hand points at' + DOTS,
       ['12', '6', '3 or 9', '10'], 2,
       ['The weight is vertical, so its arm is the horizontal distance of the midpoint from the centre,',
        'largest (= 6 cm) when the hand is horizontal : at 3 or 9',
        'M<sub>max</sub> = 0.2 × 0.06 = 1.2 × 10<sup>−2</sup> N·m']),
   ess('Calculate the moment of the weight about the centre in the position shown.',
       ['The hand makes 60° with the vertical',
        'arm = 0.06 × sin 60° = 0.052 m',
        'M = 0.2 × 0.052 = 1.04 × 10<sup>−2</sup> N·m',
        'the weight is to the left of the centre → anticlockwise'],
       'M = +1.04 × 10<sup>−2</sup> N·m', 'm'),
   ess('At which marks is this moment zero?',
       ['When the hand is vertical (at 12 or 6), the weight acts along the hand, through the centre.'],
       'at 12 and at 6', 's')],
  G.clock(66), 'right')

q('A uniform rod OA of length 1.2 m and weight 50 N is pivoted at O and makes 37° with the horizontal. '
  'A horizontal force F acts at its end A. (Take sin 37° = 0.6, cos 37° = 0.8)',
  [ess('Calculate the moment of the weight about O.',
       ['arm = horizontal distance of the midpoint = 0.6 cos 37° = 0.6 × 0.8 = 0.48 m',
        'M<sub>W</sub> = −50 × 0.48 = −24 N·m   (clockwise)'],
       'M<sub>W</sub> = −24 N·m', 'm'),
   mcq('To make the net moment about O equal to zero, the force F must be' + DOTS,
       ['33.3 N to the right', '41.7 N to the left', '25 N to the left', '33.3 N to the left'], 3,
       ['A is 1.2 sin 37° = 0.72 m above O',
        'a horizontal force to the right at A turns the rod clockwise (like the weight),',
        'so F must point to the left to give an anticlockwise moment',
        'F × 0.72 = 24  →  F = 33.3 N to the left'])],
  G.rod_37_h(84), 'right')

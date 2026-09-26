# -*- coding: utf-8 -*-
"""Section 1 : electric current, potential difference, Ohm's law, resistivity, energy and power."""
from qlib import Section
import figs12 as F

S = Section('s1', 'Electric Current &amp; Ohm&#8217;s Law', 'Lesson 1 &middot; current &middot; p.d. &middot; '
            'resistance &middot; resistivity &middot; energy &amp; power')
m, p = S.mcq, S.prob
O = '&#937;'
D = ' ..........'

m('2 &times; 10<sup>20</sup> electrons pass through a cross-section of a wire in 8 s. The intensity of the electric '
  'current in the wire equals' + D,
  ['4 A', '0.25 A', '2.5 A', '40 A'], 'A',
  ['Q = N e = 2 &times; 10<sup>20</sup> &times; 1.6 &times; 10<sup>&#8722;19</sup> = 32 C',
   'I = Q / t = 32 / 8 = 4 A'], title='current from the number of electrons')

m('The graph shows the quantity of charge (Q) passing through a cross-section of a conductor against time (t). '
  'The ratio between the current in part ab and the current in part bc ( I<sub>ab</sub> / I<sub>bc</sub> ) is' + D,
  ['3', '1/3', '2', '6'], 'A',
  ['the slope of the Q &#8211; t graph is the current : I = &#916;Q / &#916;t',
   'I(ab) = 12 / 2 = 6 A        I(bc) = ( 18 &#8722; 12 ) / ( 5 &#8722; 2 ) = 2 A',
   'I(ab) / I(bc) = 6 / 2 = 3'], F.g_qt_bent('Fig. 1'), title='slope of a Q&#8211;t graph', side=True)

m('The graph shows the current (I) in a conductor against time (t). The number of electrons that pass through a '
  'cross-section of the conductor during the first 10 s is' + D,
  ['3.125 &times; 10<sup>19</sup>', '1.25 &times; 10<sup>20</sup>', '1.875 &times; 10<sup>20</sup>',
   '4.8 &times; 10<sup>&#8722;18</sup>'], 'C',
  ['the area under the I &#8211; t graph is the charge',
   'Q = ( 4 &times; 5 ) + ( 2 &times; 5 ) = 20 + 10 = 30 C',
   'N = Q / e = 30 / 1.6 &times; 10<sup>&#8722;19</sup> = 1.875 &times; 10<sup>20</sup> electrons'],
  F.g_it_step('Fig. 2'), title='area under an I&#8211;t graph', side=True)

m('The work done to transfer 5 &times; 10<sup>19</sup> electrons between two points of a conductor is 48 J. '
  'The potential difference between the two points equals' + D,
  ['8 V', '6 V', '0.6 V', '384 V'], 'B',
  ['Q = N e = 5 &times; 10<sup>19</sup> &times; 1.6 &times; 10<sup>&#8722;19</sup> = 8 C',
   'V = W / Q = 48 / 8 = 6 V'], title='potential difference')

p('The potential difference across the filament of a lamp is 12 V and the resistance of the filament is 4 ' + O +
  '. <b>Calculate</b> the number of electrons that pass through a cross-section of the filament in one minute.',
  '1.125 &times; 10<sup>21</sup> electrons',
  ['I = V / R = 12 / 4 = 3 A', 'Q = I t = 3 &times; 60 = 180 C',
   'N = Q / e = 180 / 1.6 &times; 10<sup>&#8722;19</sup> = 1.125 &times; 10<sup>21</sup> electrons'],
  title='electrons through a filament')

m('The graph shows the relation between the potential difference (V) and the current (I) for two conductors x and '
  'y. The ratio of their resistances ( R<sub>x</sub> / R<sub>y</sub> ) is' + D,
  ['1/3', '&#8730;3', '3', '1/&#8730;3'], 'C',
  ['on a V &#8211; I graph the slope is the resistance : R = V / I = tan &#952;',
   'line x makes 60&#176; with the I-axis and line y makes 30&#176;',
   'R(x) / R(y) = tan 60&#176; / tan 30&#176; = 1.732 / 0.577 = 3'], F.g_vi_angles('Fig. 3'),
  tag='HOTS', title='slopes of V&#8211;I lines', side=True)

m('Graph (1) shows the work done (W) to move charge (Q) through a conductor, and graph (2) shows the charge passing '
  'through the same conductor against time. The resistance of the conductor equals' + D,
  ['0.5 ' + O, '2 ' + O, '5 ' + O, '15 ' + O], 'B',
  ['graph (1) : slope = W / Q = V = 200 / 20 = 10 V',
   'graph (2) : slope = Q / t = I = 20 / 4 = 5 A',
   'R = V / I = 10 / 5 = 2 ' + O], F.g_wq_qt('Fig. 4'), title='two graphs, one resistance')

m('A copper wire has a length of 20 m and a cross-sectional area of 0.5 mm&#178;. If the resistivity of copper is '
  '1.7 &times; 10<sup>&#8722;8</sup> ' + O + '&middot;m, the resistance of the wire equals' + D,
  ['0.68 ' + O, '6.8 ' + O, '0.068 ' + O, '0.34 ' + O], 'A',
  ['A = 0.5 mm&#178; = 0.5 &times; 10<sup>&#8722;6</sup> m&#178;',
   'R = &#961;<sub>e</sub> L / A = 1.7 &times; 10<sup>&#8722;8</sup> &times; 20 / 0.5 &times; 10<sup>&#8722;6</sup> = 0.68 ' + O],
  title='resistance from resistivity')

m('A wire of length 6.28 m and radius 1 mm is made of a material of resistivity 5 &times; 10<sup>&#8722;7</sup> ' + O +
  '&middot;m. It is connected across a 3 V battery of negligible internal resistance. The current in the wire is' + D,
  ['1.5 A', '0.33 A', '6 A', '3 A'], 'D',
  ['A = &#960; r&#178; = 3.14 &times; ( 10<sup>&#8722;3</sup> )&#178; = 3.14 &times; 10<sup>&#8722;6</sup> m&#178;',
   'R = &#961;<sub>e</sub> L / A = 5 &times; 10<sup>&#8722;7</sup> &times; 6.28 / 3.14 &times; 10<sup>&#8722;6</sup> = 1 ' + O,
   'I = V / R = 3 / 1 = 3 A'], title='wire across a battery')

m('A metal wire is stretched uniformly until its length is doubled (its volume stays constant). Which row shows what '
  'happens to its resistance and to the conductivity of its material?',
  ['R doubles , &#963; unchanged', 'R quadruples , &#963; unchanged', 'R quadruples , &#963; halves',
   'R unchanged , &#963; doubles'], 'B',
  ['constant volume : L doubles &#8594; A becomes A / 2',
   'R = &#961;<sub>e</sub> L / A &#8594; R&#8242; = &#961;<sub>e</sub> ( 2L ) / ( A / 2 ) = 4 R',
   'the conductivity depends only on the material and the temperature &#8594; unchanged'],
  title='stretching a wire')

m('A wire of resistance 5 ' + O + ' is drawn through a die so that its radius becomes half its original value '
  '(the volume stays constant). Its new resistance is' + D,
  ['10 ' + O, '20 ' + O, '40 ' + O, '80 ' + O], 'D',
  ['r &#8594; r/2 &#8658; A &#8594; A/4 , and constant volume &#8658; L &#8594; 4L',
   'R&#8242; / R = ( L&#8242; / L ) &times; ( A / A&#8242; ) = 4 &times; 4 = 16',
   'R&#8242; = 16 &times; 5 = 80 ' + O], tag='HOTS', title='drawing a wire thinner')

m('Two wires x and y are made of the same metal. Wire x has a length of 3L and a mass of 4 g, while wire y has a '
  'length L and a mass of 12 g. The ratio of their resistances ( R<sub>x</sub> / R<sub>y</sub> ) equals' + D,
  ['9', '27', '3', '1/27'], 'B',
  ['A = volume / L = ( m / &#961; ) / L &#8658; R = &#961;<sub>e</sub> L / A = &#961;<sub>e</sub> &#961; L&#178; / m',
   'R &#8733; L&#178; / m  (same metal)',
   'R(x) / R(y) = ( 9L&#178; / 4 ) / ( L&#178; / 12 ) = ( 9 / 4 ) &times; 12 = 27'],
  F.two_rods_mass('Fig. 5'), tag='HOTS', title='resistance from length and mass')

p('A wire of cross-sectional area 0.2 mm&#178; and resistivity 5 &times; 10<sup>&#8722;7</sup> ' + O + '&middot;m is '
  'wound into a circular coil of 100 turns, each of radius 7 cm. <b>Find:</b> (i) the length of the wire, '
  '(ii) its resistance, (iii) the current in the coil when it is connected to 220 V. (&#960; = 22/7)',
  '(i) 44 m &nbsp; (ii) 110 ' + O + ' &nbsp; (iii) 2 A',
  ['(i)   L = 2 &#960; r N = 2 &times; ( 22 / 7 ) &times; 0.07 &times; 100 = 44 m',
   '(ii)  R = &#961;<sub>e</sub> L / A = 5 &times; 10<sup>&#8722;7</sup> &times; 44 / 0.2 &times; 10<sup>&#8722;6</sup> = 110 ' + O,
   '(iii) I = V / R = 220 / 110 = 2 A'], title='a wire wound into a coil')

p('The graph shows how the resistance (R) of a uniform wire changes with its length (L). The cross-sectional area '
  'of the wire is 0.2 mm&#178;. <b>Find:</b> (i) the resistivity of its material, (ii) the length of this wire '
  'that has a resistance of 4.5 ' + O + '.',
  '(i) 6 &times; 10<sup>&#8722;8</sup> ' + O + '&middot;m &nbsp; (ii) 15 m',
  ['(i)  slope = R / L = 12 / 40 = 0.3 ' + O + '/m     and  R = ( &#961;<sub>e</sub> / A ) L  &#8658;  slope = &#961;<sub>e</sub> / A',
   '     &#961;<sub>e</sub> = slope &times; A = 0.3 &times; 0.2 &times; 10<sup>&#8722;6</sup> = 6 &times; 10<sup>&#8722;8</sup> ' + O + '&middot;m',
   '(ii) L = R / slope = 4.5 / 0.3 = 15 m'], F.g_R_L('Fig. 6'), title='resistivity from an R&#8211;L graph', side=True)

m('The temperature of a metal wire connected across a constant potential difference is raised. Which row is correct?',
  ['R increases , I decreases , &#963; decreases', 'R increases , I increases , &#963; decreases',
   'R decreases , I increases , &#963; increases', 'R increases , I decreases , &#963; unchanged'], 'A',
  ['a higher temperature makes the atoms vibrate more &#8594; more collisions with the free electrons',
   'so the resistivity rises &#8594; R increases and &#963; = 1 / &#961;<sub>e</sub> decreases',
   'V is constant &#8594; I = V / R decreases'], title='effect of temperature')

m('The figure shows four wires a, b, c and d made of the same metal (their lengths and cross-sectional areas are '
  'marked). When each is connected alone across the same potential difference, the correct order of the currents is'
  + D,
  ['a &gt; b &gt; c &gt; d', 'c &gt; d &gt; a &gt; b', 'd &gt; c &gt; a &gt; b', 'b &gt; a &gt; d &gt; c'], 'B',
  ['I = V / R = V A / ( &#961;<sub>e</sub> L ) &#8658; I &#8733; A / L',
   'a : A / L = 1     b : A / 2L = 0.5     c : 2A / L = 2     d : 3A / 2L = 1.5',
   'c &gt; d &gt; a &gt; b'], F.four_wires('Fig. 7'), side=True, title='ranking four wires')

m('A hollow copper tube has a length of 2 m, an inner radius of 2 mm and an outer radius of 3 mm. The resistivity '
  'of its material is 3.14 &times; 10<sup>&#8722;8</sup> ' + O + '&middot;m. The resistance between its two ends is' + D,
  ['2 &times; 10<sup>&#8722;3</sup> ' + O, '4 &times; 10<sup>&#8722;3</sup> ' + O, '8 &times; 10<sup>&#8722;3</sup> ' + O,
   '1.6 &times; 10<sup>&#8722;3</sup> ' + O], 'B',
  ['the current flows through the ring-shaped area only',
   'A = &#960; ( r&#8322;&#178; &#8722; r&#8321;&#178; ) = 3.14 &times; ( 9 &#8722; 4 ) &times; 10<sup>&#8722;6</sup> = 1.57 &times; 10<sup>&#8722;5</sup> m&#178;',
   'R = &#961;<sub>e</sub> L / A = 3.14 &times; 10<sup>&#8722;8</sup> &times; 2 / 1.57 &times; 10<sup>&#8722;5</sup> = 4 &times; 10<sup>&#8722;3</sup> ' + O],
  F.hollow('Fig. 8'), tag='HOTS', title='a hollow tube')

m('A conductor of length 1.57 m has a semicircular cross-section of diameter 4 mm, as shown. If the resistivity of '
  'its material is 2 &times; 10<sup>&#8722;6</sup> ' + O + '&middot;m, its resistance equals' + D,
  ['0.25 ' + O, '1 ' + O, '0.5 ' + O, '2 ' + O], 'C',
  ['r = 2 mm , the area is half a circle : A = &#960; r&#178; / 2 = 3.14 &times; 4 &times; 10<sup>&#8722;6</sup> / 2 = 6.28 &times; 10<sup>&#8722;6</sup> m&#178;',
   'R = &#961;<sub>e</sub> L / A = 2 &times; 10<sup>&#8722;6</sup> &times; 1.57 / 6.28 &times; 10<sup>&#8722;6</sup> = 0.5 ' + O],
  F.half_cylinder('Fig. 9'), side=True, title='a semicircular cross-section')

m('A lamp is labelled (220 V , 100 W). If it is connected to a 110 V source (its resistance stays constant), the '
  'power it consumes is' + D,
  ['50 W', '25 W', '100 W', '12.5 W'], 'B',
  ['R = V&#178; / P = 220&#178; / 100 = 484 ' + O,
   'P&#8242; = V&#8242;&#178; / R = 110&#178; / 484 = 25 W   (half the voltage &#8594; a quarter of the power)'],
  title='a lamp on half its rated voltage')

m('The graph shows the power (P) consumed in a resistor against the square of the current (I&#178;). If this '
  'resistor is connected alone across a 10 V source, the power it consumes is' + D,
  ['25 W', '40 W', '2.5 W', '400 W'], 'A',
  ['P = I&#178; R &#8658; the slope of the P &#8211; I&#178; graph is R = 36 / 9 = 4 ' + O,
   'P = V&#178; / R = 10&#178; / 4 = 25 W'], F.g_P_I2('Fig. 10'), side=True, title='slope of a P&#8211;I&#178; graph')

m('An electric heater of resistance 22 ' + O + ' works on 220 V for 10 minutes. The electric energy it consumes is'
  + D,
  ['2.2 &times; 10<sup>3</sup> J', '1.32 &times; 10<sup>5</sup> J', '1.32 &times; 10<sup>6</sup> J',
   '2.64 &times; 10<sup>6</sup> J'], 'C',
  ['P = V&#178; / R = 220&#178; / 22 = 2200 W',
   'W = P t = 2200 &times; ( 10 &times; 60 ) = 1.32 &times; 10<sup>6</sup> J'], title='energy of a heater')

m('Two wires of the same metal and the same length have radii in the ratio 1 : 2. They are connected in parallel '
  'across the same source. The ratio of the powers they consume ( P<sub>1</sub> / P<sub>2</sub> ) is' + D,
  ['1/2', '2', '1/4', '4'], 'C',
  ['same V : P = V&#178; / R &#8658; P &#8733; 1 / R',
   'R &#8733; 1 / r&#178; &#8658; P &#8733; r&#178;',
   'P&#8321; / P&#8322; = ( 1 / 2 )&#178; = 1 / 4'], title='power in parallel wires')

m('In the circuit shown, the battery has negligible internal resistance. Which graph shows the <b>ammeter</b> '
  'reading against the resistance R<sub>v</sub> taken from the rheostat?',
  [F.mini('inv', 'I'), F.mini('rise', 'I'), F.mini('flat', 'I'), F.mini('lin', 'I')], 'A',
  ['r = 0 &#8658; the p.d. across the rheostat always equals V<sub>B</sub>',
   'I = V<sub>B</sub> / R<sub>v</sub> &#8658; I is inversely proportional to R<sub>v</sub> (a falling curve)'],
  F.rheostat_meters('Fig. 11'), side=True, title='ammeter reading and R<sub>v</sub>',
  fa='a falling curve ( I &#8733; 1 / R<sub>v</sub> )')

m('For the circuit of Fig. 11, which graph shows the <b>voltmeter</b> reading against R<sub>v</sub>?',
  [F.mini('inv', 'V'), F.mini('rise', 'V'), F.mini('lin', 'V'), F.mini('flat', 'V')], 'D',
  ['the voltmeter is connected across the rheostat, and the ammeter has negligible resistance',
   'r = 0 &#8658; V = V<sub>B</sub> &#8722; I r = V<sub>B</sub> whatever R<sub>v</sub> is &#8594; a horizontal line'],
  title='voltmeter reading and R<sub>v</sub>', fa='a horizontal line ( V = V<sub>B</sub> )')

m('Conductor x has a length L, a cross-sectional area A and a conductivity &#963;. Conductor y has a length 2L, a '
  'cross-sectional area 3A and a conductivity &#963;/2. When each is connected across the same potential '
  'difference, the ratio of the currents ( I<sub>x</sub> / I<sub>y</sub> ) is' + D,
  ['4/3', '3/4', '3', '1/3'], 'A',
  ['R = L / ( &#963; A ) &#8658; I = V / R = V &#963; A / L &#8658; I &#8733; &#963; A / L',
   'x : &#963; A / L        y : ( &#963; / 2 ) ( 3A ) / ( 2L ) = 3 &#963; A / 4L',
   'I(x) / I(y) = 1 / ( 3 / 4 ) = 4 / 3'], tag='HOTS', title='conductivity, length and area together')

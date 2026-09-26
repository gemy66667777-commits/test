# -*- coding: utf-8 -*-
"""Section 2 : connecting resistors (series, parallel, networks, lamps)."""
from qlib import Section
import figs12 as F

S = Section('s2', 'Connecting Resistors', 'Lesson 2 &middot; series &middot; parallel &middot; networks &middot; '
            'lamps &amp; switches')
m, p = S.mcq, S.prob
O = '&#937;'
D = ' ..........'

m('Four identical resistors are connected in the four ways shown. The correct order of the equivalent resistances '
  'from the <b>largest</b> to the <b>smallest</b> is' + D,
  ['(1) , (3) , (4) , (2)', '(2) , (4) , (3) , (1)', '(1) , (4) , (3) , (2)', '(3) , (1) , (2) , (4)'], 'A',
  ['(1) all in series : 4R',
   '(3) two parallel pairs in series : R/2 + R/2 = R',
   '(4) 3R in parallel with R : ( 3R &times; R ) / 4R = 3R/4',
   '(2) all in parallel : R/4',
   '4R &gt; R &gt; 3R/4 &gt; R/4'], F.four_arrangements('Fig. 12'), title='four ways of connecting four resistors')

m('A uniform wire of resistance 90 ' + O + ' is cut into six equal parts, which are connected as shown. The '
  'equivalent resistance between a and b is' + D,
  ['15 ' + O, '5 ' + O, '10 ' + O, '30 ' + O], 'C',
  ['each part : 90 / 6 = 15 ' + O,
   'three equal parts in parallel : 15 / 3 = 5 ' + O,
   'the two groups are in series : 5 + 5 = 10 ' + O], F.cut_six('Fig. 13'), title='a wire cut into six parts')

m('A current of 2 A enters two resistors of 6 ' + O + ' and 3 ' + O + ' connected in parallel. The current '
  'I<sub>1</sub> in the 6 ' + O + ' resistor is' + D,
  ['4/3 A', '2/3 A', '1 A', '2 A'], 'B',
  ['R&#8242; = ( 6 &times; 3 ) / ( 6 + 3 ) = 2 ' + O + '  &#8658;  V = I R&#8242; = 2 &times; 2 = 4 V',
   'I&#8321; = V / 6 = 4 / 6 = 2/3 A     ( and I&#8322; = 4 / 3 A through the 3 ' + O + ' )'],
  F.divider('Fig. 14'), side=True, title='current divider')

m('In the network shown, the ends of the 4 ' + O + ' resistor are joined by a connecting wire of negligible '
  'resistance. The equivalent resistance between a and b is' + D,
  ['8 ' + O, '4 ' + O, '6 ' + O, '2 ' + O], 'B',
  ['the wire joins the two ends of 4 ' + O + ' : no p.d. across it &#8594; it carries no current and is ignored',
   '6 ' + O + ' // 3 ' + O + ' = ( 6 &times; 3 ) / 9 = 2 ' + O,
   'R(ab) = 2 + 2 = 4 ' + O], F.shorted('Fig. 15'), title='a short-circuited resistor')

m('In the network shown, the equivalent resistance between a and b is' + D,
  ['4.5 ' + O, '2.5 ' + O, '15 ' + O, '3.6 ' + O], 'D',
  ['2 / 4 = 3 / 6 = 0.5 &#8658; the two middle points have the same potential',
   'so the 10 ' + O + ' resistor carries no current and is ignored',
   'R(ab) = ( 2 + 4 ) // ( 3 + 6 ) = ( 6 &times; 9 ) / 15 = 3.6 ' + O], F.bridge('Fig. 16'), side=True,
  tag='HOTS', title='a balanced bridge')

m('In the circuit shown, the reading of the voltmeter is' + D,
  ['4 V', '6 V', '8 V', '12 V'], 'C',
  ['series : R = 2 + 4 = 6 ' + O + '  &#8658;  I = 12 / 6 = 2 A',
   'V(4 ' + O + ') = I R = 2 &times; 4 = 8 V'], F.series_voltmeter('Fig. 17'), side=True, title='voltmeter in a series circuit')

m('In the circuit shown, the voltmeter reads 4 V. The current in the 6 ' + O + ' resistor is' + D,
  ['0.8 A', '1.2 A', '1 A', '2 A'], 'A',
  ['the voltmeter is across the 2 ' + O + ' resistor : I = 4 / 2 = 2 A (the total current)',
   'this current divides between 6 ' + O + ' and 4 ' + O + ' :',
   'I(6) = I &times; 4 / ( 6 + 4 ) = 2 &times; 0.4 = 0.8 A'], F.volt_parallel('Fig. 18'), side=True,
  title='from a voltmeter reading to a branch current')

m('In the circuit shown, the four lamps are identical. When switch K is closed, what happens to the brightness of '
  'lamps A and B?',
  ['A increases , B decreases', 'A decreases , B increases', 'both increase', 'A unchanged , B decreases'], 'A',
  ['K open : B // C = R/2 , total = 1.5 R , I = V / 1.5R = 0.67 V/R',
   'K closed : B // C // D = R/3 , total = 4R/3 , I = 0.75 V/R  &#8594; A (carries I) is brighter',
   'p.d. across the group : before V/3 , after I &times; R/3 = V/4  &#8594; B is dimmer'],
  F.lamps_switch('Fig. 19'), side=True, tag='HOTS', title='closing a switch in a lamp network')

m('Two lamps rated (220 V , 100 W) and (220 V , 60 W) are connected <b>in series</b> to a 220 V source. The '
  'brighter lamp is' + D,
  ['the 100 W lamp', 'the 60 W lamp', 'both are equally bright', 'neither lamp lights'], 'B',
  ['R = V&#178; / P :  R(100) = 484 ' + O + '   R(60) = 807 ' + O,
   'in series both carry the same current &#8658; P = I&#178; R &#8733; R',
   'the 60 W lamp (larger R) consumes more power &#8594; it is brighter'], title='rated lamps in series')

m('Two identical resistors connected in series to a source of constant p.d. consume a total power P. If they are '
  'connected in parallel to the same source, the total power becomes' + D,
  ['P / 4', '2P', '4P', 'P'], 'C',
  ['series : 2R &#8658; P = V&#178; / 2R',
   'parallel : R/2 &#8658; P&#8242; = V&#178; / ( R/2 ) = 2V&#178; / R',
   'P&#8242; / P = ( 2 / R ) / ( 1 / 2R ) = 4 &#8658; P&#8242; = 4P'], title='series vs parallel power')

m('In the network shown, the equivalent resistance between a and b is' + D,
  ['6 ' + O, '20 ' + O, '8 ' + O, '4 ' + O], 'A',
  ['4 ' + O + ' and 8 ' + O + ' are in series : 12 ' + O,
   '12 ' + O + ' // 6 ' + O + ' = ( 12 &times; 6 ) / 18 = 4 ' + O,
   'R(ab) = 2 + 4 = 6 ' + O], F.ab_network('Fig. 20'), title='a mixed network')

m('Conductor x (length L, area A, conductivity 4&#963;) lies in perfect contact along the first half of conductor '
  'y (length 2L, area 2A, conductivity &#963;), as shown. If the resistance of x is 5 ' + O + ', the resistance '
  'between a and b is' + D,
  ['7.5 ' + O, '15 ' + O, '20 ' + O, '13.3 ' + O], 'D',
  ['R = L / ( &#963; A ) :  R(x) = L / ( 4 &#963; A ) = 5 ' + O + '  &#8658;  L / ( &#963; A ) = 20 ' + O,
   'each half of y : L / ( &#963; &times; 2A ) = 10 ' + O,
   'the first half of y is in parallel with x : ( 5 &times; 10 ) / 15 = 3.33 ' + O,
   'then the second half of y in series : R(ab) = 3.33 + 10 = 13.3 ' + O], F.overlap_rods('Fig. 21'),
  tag='HOTS', title='two conductors in contact')

m('Using <b>all three</b> of three identical 6 ' + O + ' resistors, which of the following values <b>cannot</b> '
  'be obtained?',
  ['18 ' + O, '9 ' + O, '4 ' + O, '12 ' + O], 'D',
  ['all in series : 18 ' + O + '      all in parallel : 2 ' + O,
   '6 + ( 6 // 6 ) = 6 + 3 = 9 ' + O,
   '6 // ( 6 + 6 ) = ( 6 &times; 12 ) / 18 = 4 ' + O,
   '12 ' + O + ' needs only two resistors in series &#8594; it cannot be made with all three'],
  title='possible combinations')

m('In the circuit shown, the ratio of the voltmeter readings ( V<sub>1</sub> / V<sub>2</sub> ) is' + D,
  ['3/5', '5/3', '2/3', '1'], 'B',
  ['series : the same current I flows through R , 2R and 3R',
   'V&#8321; is across 2R + 3R = 5R  &#8658; V&#8321; = 5 I R',
   'V&#8322; is across R + 2R = 3R    &#8658; V&#8322; = 3 I R',
   'V&#8321; / V&#8322; = 5 / 3'], F.three_series_v('Fig. 22'), side=True, title='two voltmeters on one series line')

p('In the circuit shown, <b>find:</b> (i) the total current, (ii) the current in each of the 6 ' + O + ' and '
  '12 ' + O + ' resistors, (iii) the power consumed in the 4 ' + O + ' resistor.',
  'I = 1.5 A ; I(6) = 1 A , I(12) = 0.5 A ; P = 9 W',
  ['(i)   6 // 12 = ( 6 &times; 12 ) / 18 = 4 ' + O + '  &#8658;  R = 4 + 4 = 8 ' + O + '  &#8658;  I = 12 / 8 = 1.5 A',
   '(ii)  V(parallel) = 1.5 &times; 4 = 6 V  &#8658;  I(6) = 6 / 6 = 1 A ,  I(12) = 6 / 12 = 0.5 A',
   '(iii) P = I&#178; R = 1.5&#178; &times; 4 = 9 W'], F.net12('Fig. 23'), side=True, title='solving a whole circuit')

m('In the V &#8211; I graph (the marked point is on line 4), lines 1 and 3 belong to two resistors x and y. Which line can represent x and y '
  'connected <b>in parallel</b>?',
  ['line 1', 'line 2', 'line 3', 'line 4'], 'D',
  ['R = slope :  x = 9 / 1 = 9 ' + O + '   y = 9 / 3 = 3 ' + O,
   'parallel : ( 9 &times; 3 ) / 12 = 2.25 ' + O + '  (smaller than both, so below both lines)',
   'line 4 passes through ( 2 A , 4.5 V ) : slope = 4.5 / 2 = 2.25 ' + O + '  &#8594; line 4'],
  F.g_vi_combo('Fig. 24'), side=True, tag='HOTS', title='a parallel combination on a V&#8211;I graph')

m('In the circuit shown, when switch K is closed, the ammeter reading changes' + D,
  ['from 1 A to 3 A', 'from 3 A to 1 A', 'from 1 A to 1.5 A', 'it stays 1 A'], 'A',
  ['K open : R = 4 + 8 = 12 ' + O + '  &#8658;  I = 12 / 12 = 1 A',
   'K closed : the switch short-circuits the 8 ' + O + ' resistor  &#8658;  R = 4 ' + O,
   'I = 12 / 4 = 3 A'], F.short_switch('Fig. 25'), side=True, title='a switch across a resistor')

p('In the circuit shown, the ammeter reads 4 A. <b>Find</b> the value of the resistance R.',
  'R = 6 ' + O,
  ['total resistance = V / I = 24 / 4 = 6 ' + O,
   'the parallel group = 6 &#8722; 2 = 4 ' + O,
   '1 / R + 1 / 12 = 1 / 4  &#8658;  1 / R = 3/12 &#8722; 1/12 = 2/12',
   'R = 6 ' + O], F.unknown_R('Fig. 26'), side=True, title='finding an unknown resistance')

m('In the circuit shown, the three lamps are identical. If lamp C burns out (its filament breaks), what happens to '
  'the brightness of lamps A and B?',
  ['A increases , B decreases', 'both decrease', 'A decreases , B increases', 'both go off'], 'C',
  ['before : B // C = R/2 , total 1.5R , I = V / 1.5R  &#8594; B carries V / 3R',
   'after : A and B in series , total 2R , I = V / 2R',
   'A : V/1.5R &#8594; V/2R (less current, dimmer)     B : V/3R &#8594; V/2R (more current, brighter)'],
  F.burnout('Fig. 27'), side=True, title='a lamp burns out')

m('A uniform wire of resistance 16 ' + O + ' is bent into a circle. The resistance between points a and b, which '
  'are a quarter of the circle apart, is' + D,
  ['3 ' + O, '4 ' + O, '8 ' + O, '12 ' + O], 'A',
  ['the short arc is 1/4 of the wire : 4 ' + O + '      the long arc is 3/4 : 12 ' + O,
   'the two arcs are in parallel between a and b',
   'R(ab) = ( 4 &times; 12 ) / 16 = 3 ' + O], F.ring('Fig. 28'), side=True, tag='HOTS', title='a ring of wire')

m('In the network shown, the equivalent resistance between a and b is' + D,
  ['15 ' + O, '1.5 ' + O, '2 ' + O, '3 ' + O], 'B',
  ['follow the wires : every resistor has one end joined to a and the other end joined to b',
   'so the three resistors are all in parallel',
   '1 / R = 1/6 + 1/3 + 1/6 = 4/6  &#8658;  R = 1.5 ' + O], F.twisted('Fig. 29'), side=True, tag='HOTS',
  title='redraw before you calculate')

p('n identical resistors give an equivalent resistance of 50 ' + O + ' when connected in series and 2 ' + O +
  ' when connected in parallel. <b>Find</b> n and the resistance of each resistor.',
  'n = 5 , R = 10 ' + O,
  ['series : n R = 50        parallel : R / n = 2',
   'multiply : R&#178; = 100  &#8658;  R = 10 ' + O,
   'n = 50 / 10 = 5'], title='series and parallel together')

m('In the circuit shown, when switch K is closed, which row is correct?',
  ['ammeter reading increases , I(6 ' + O + ') unchanged', 'ammeter reading unchanged , I(6 ' + O + ') decreases',
   'ammeter reading increases , I(6 ' + O + ') increases', 'ammeter reading decreases , I(6 ' + O + ') unchanged'],
  'A',
  ['r = 0 : each branch has the full 12 V across it',
   'I(6) = 12 / 6 = 2 A before and after closing K (unchanged)',
   'K closed : the 3 ' + O + ' branch adds 12 / 3 = 4 A  &#8594; ammeter : 2 A &#8594; 6 A'],
  F.switch_branch('Fig. 30'), side=True, title='adding a parallel branch')

p('Three resistors of 2 ' + O + ', 3 ' + O + ' and 6 ' + O + ' are connected in parallel to a 6 V battery of '
  'negligible internal resistance. <b>Find</b> the power consumed in each resistor and the total power.',
  '18 W , 12 W , 6 W ; total 36 W',
  ['in parallel each resistor has V = 6 V :  P = V&#178; / R',
   'P(2) = 36 / 2 = 18 W     P(3) = 36 / 3 = 12 W     P(6) = 36 / 6 = 6 W',
   'total = 18 + 12 + 6 = 36 W   ( check : R&#8242; = 1 ' + O + ' , P = 36 / 1 = 36 W )'], title='power in parallel')

m('In the circuit shown, the resistance taken from the rheostat is <b>decreased</b>. Which row is correct?',
  ['lamp brighter , voltmeter reading increases', 'lamp dimmer , voltmeter reading increases',
   'lamp brighter , voltmeter reading decreases', 'lamp unchanged , voltmeter reading unchanged'], 'A',
  ['R<sub>v</sub> decreases &#8594; the total resistance decreases &#8594; the current increases',
   'the lamp carries a larger current &#8594; brighter',
   'the voltmeter is across the lamp : V = I R(lamp) increases'], F.rheo_lamp('Fig. 31'), side=True,
  title='a rheostat in series with a lamp')

m('A uniform wire of resistance 36 ' + O + ' is bent into an equilateral triangle xyz. The resistance between '
  'two corners x and y is' + D,
  ['8 ' + O, '12 ' + O, '18 ' + O, '24 ' + O], 'A',
  ['each side : 36 / 3 = 12 ' + O,
   'between x and y : one side (12 ' + O + ') in parallel with two sides (24 ' + O + ')',
   'R = ( 12 &times; 24 ) / 36 = 8 ' + O], F.triangle_wire('Fig. 32'), side=True, title='a triangle of wire')

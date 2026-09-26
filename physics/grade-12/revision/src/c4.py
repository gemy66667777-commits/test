# -*- coding: utf-8 -*-
"""Section 4 : Kirchhoff's laws."""
from qlib import Section
import figs12 as F

S = Section('s4', 'Kirchhoff&#8217;s Laws', 'Lesson 4 &middot; junction rule &middot; loop rule &middot; '
            'multi-loop circuits &middot; potentials')
m, p = S.mcq, S.prob
O = '&#937;'
D = ' ..........'

m('The figure shows five wires meeting at junction a. The current I in wire c is' + D,
  ['3 A , from a to c', '5 A , from c to a', '5 A , from a to c', '23 A , from c to a'], 'B',
  ['Kirchhoff&#8217;s first law : &#931; I(in) = &#931; I(out)',
   'known : in = 5 + 4 = 9 A        out = 8 + 6 = 14 A',
   'the missing 5 A must flow <b>into</b> a : I = 5 A , from c to a'], F.star('Fig. 48'), side=True,
  title='the junction rule')

m('Kirchhoff&#8217;s first law and Kirchhoff&#8217;s second law are based on the conservation of' + D,
  ['energy , charge', 'charge , energy', 'charge , mass', 'mass , energy'], 'B',
  ['1st law : charge does not pile up at a junction &#8594; conservation of charge',
   '2nd law : the energy given by the sources in a loop = the energy used &#8594; conservation of energy'],
  title='the principles behind the two laws')

m('In the figure, the current in the 6 ' + O + ' resistor is 2 A. The current I is' + D,
  ['1 A', '2 A', '4 A', '3 A'], 'D',
  ['V = 2 &times; 6 = 12 V across both resistors (parallel)',
   'I(12 ' + O + ') = 12 / 12 = 1 A',
   'junction : I = 2 + 1 = 3 A'], F.split('Fig. 49'), side=True, title='junction and parallel branches')

m('When a closed loop is followed through a resistor R <b>in the same direction</b> as the current I, the change '
  'in potential is written in the loop equation as' + D,
  ['+ I R', '&#8722; I R', 'zero', '+ V<sub>B</sub>'], 'B',
  ['moving with the current through a resistor, the potential falls (from high to low)',
   'so the term is &#8722; I R  (and + I R if we move against the current)'], title='sign convention')

p('In the circuit shown, both batteries have negligible internal resistance. Use Kirchhoff&#8217;s laws to '
  '<b>find</b> the currents I<sub>1</sub>, I<sub>2</sub> and I<sub>3</sub>.',
  'I&#8321; = 4 A , I&#8322; = &#8722;1 A (1 A the other way) , I&#8323; = 3 A',
  ['junction x :  I&#8321; + I&#8322; = I&#8323;',
   'left loop :   20 &#8722; 2 I&#8321; &#8722; 4 I&#8323; = 0',
   'right loop :  10 &#8722; 2 I&#8322; &#8722; 4 I&#8323; = 0',
   'subtract the loop equations : 10 &#8722; 2 I&#8321; + 2 I&#8322; = 0  &#8658;  I&#8321; = I&#8322; + 5',
   'left loop : 20 &#8722; 2 ( I&#8322; + 5 ) &#8722; 4 ( 2 I&#8322; + 5 ) = 0  &#8658;  &#8722;10 I&#8322; &#8722; 10 = 0',
   'I&#8322; = &#8722;1 A , I&#8321; = 4 A , I&#8323; = 3 A'],
  F.twoloop('Fig. 50', '20 V', '2 ' + O, '10 V', '2 ' + O, '4 ' + O), tag='HOTS', title='a two-loop circuit')

m('For the circuit of Fig. 50, the power consumed in the 4 ' + O + ' resistor is' + D,
  ['36 W', '12 W', '64 W', '9 W'], 'A',
  ['from question 80 : I&#8323; = 3 A',
   'P = I&#178; R = 3&#178; &times; 4 = 36 W'], title='power in the middle branch')

m('For the circuit of Fig. 50, which statement about the 10 V battery is correct?',
  ['it discharges with a current of 1 A', 'it is being charged with a current of 1 A',
   'it carries no current', 'it discharges with a current of 3 A'], 'B',
  ['I&#8322; = &#8722;1 A : the real current is opposite to the arrow drawn',
   'so 1 A enters the 10 V battery through its positive terminal &#8594; it is being charged'],
  title='which battery is charged?')

m('In the circuit shown, the current in the 1 ' + O + ' resistor is' + D,
  ['4.5 A', '1.5 A', '6 A', '3 A'], 'C',
  ['let the potential of x (with y = 0) be V :',
   '( 24 &#8722; V ) / 4 + ( 12 &#8722; V ) / 4 = V / 1  &#8658;  36 &#8722; 2V = 4V  &#8658;  V = 6 V',
   'I(1 ' + O + ') = 6 / 1 = 6 A   ( I&#8321; = 4.5 A , I&#8322; = 1.5 A : 4.5 + 1.5 = 6 &#10004; )'],
  F.twoloop('Fig. 51', '24 V', '4 ' + O, '12 V', '4 ' + O, '1 ' + O), side=True, title='two batteries feeding one resistor')

m('Between points a and b, a 2 ' + O + ' resistor carries 3 A in the direction shown, followed by a 10 V battery '
  '(r = 0). The potential difference V<sub>ab</sub> = V<sub>a</sub> &#8722; V<sub>b</sub> is' + D,
  ['16 V', '4 V', '&#8722;4 V', '&#8722;16 V'], 'C',
  ['walk from a to b : through 2 ' + O + ' with the current &#8594; &#8722; 3 &times; 2 = &#8722;6 V',
   'through the battery from &#8722; to + &#8594; + 10 V',
   'V<sub>b</sub> = V<sub>a</sub> &#8722; 6 + 10  &#8658;  V<sub>a</sub> &#8722; V<sub>b</sub> = &#8722;4 V'],
  F.path_ab('Fig. 52'), tag='HOTS', title='walking along a branch')

m('Twelve identical resistors, each R, form the edges of a cube. The equivalent resistance between two opposite '
  'corners a and b is' + D,
  ['R/2', '5R/6', '3R/2', 'R'], 'B',
  ['by symmetry the current I entering a divides equally into 3 edges : I/3 each',
   'at the next corners each current divides into 2 : I/6 on each of the 6 middle edges',
   'the last 3 edges carry I/3 each into b',
   'V(ab) = ( I/3 ) R + ( I/6 ) R + ( I/3 ) R = 5 I R / 6  &#8658;  R(ab) = 5R/6'],
  F.cube('Fig. 53'), side=True, tag='HOTS', title='a cube of resistors')

p('In the network shown, the battery has an emf of 14 V and negligible internal resistance. Use Kirchhoff&#8217;s '
  'laws to <b>find</b>: (i) the current in the 1 ' + O + ' resistor CD, (ii) the current from the battery, '
  '(iii) the equivalent resistance of the network.',
  'I(CD) = 2 A from C to D ; I = 10 A ; R = 1.4 ' + O,
  ['take V(B) = 0 , V(A) = 14 V , and the unknown potentials V(C) , V(D)',
   'junction C : ( 14 &#8722; C ) / 1 = ( C &#8722; D ) / 1 + C / 2',
   'junction D : ( 14 &#8722; D ) / 2 + ( C &#8722; D ) / 1 = D / 1',
   'solving : V(C) = 8 V , V(D) = 6 V',
   '(i)   I(CD) = ( 8 &#8722; 6 ) / 1 = 2 A , from C to D',
   '(ii)  I = I(AC) + I(AD) = ( 14 &#8722; 8 ) / 1 + ( 14 &#8722; 6 ) / 2 = 6 + 4 = 10 A',
   '(iii) R = 14 / 10 = 1.4 ' + O], F.unbal('Fig. 54'), side=True, tag='HOTS', title='an unbalanced bridge')

p('In the circuit shown, the 2 ' + O + ' resistor carries 6 A. <b>Find</b> I<sub>1</sub>, I<sub>2</sub> and '
  'R<sub>2</sub>.',
  'I&#8321; = 4 A , I&#8322; = 2 A , R&#8322; = 12 ' + O,
  ['loop (battery , 2 ' + O + ' , 6 ' + O + ') :  36 &#8722; 6 &times; 2 &#8722; 6 I&#8321; = 0  &#8658;  I&#8321; = 4 A',
   'junction :  6 = I&#8321; + I&#8322;  &#8658;  I&#8322; = 2 A',
   'the 6 ' + O + ' and R&#8322; have the same p.d. : 24 V  &#8658;  R&#8322; = 24 / 2 = 12 ' + O],
  F.given_currents('Fig. 55'), side=True, title='from one known current')

m('In the circuit shown, the galvanometer G reads zero. The emf V<sub>B2</sub> of the second battery equals' + D,
  ['4 V', '12 V', '8 V', '6 V'], 'C',
  ['G reads zero &#8594; no current in the lower loop, so V<sub>B2</sub> equals the p.d. across 8 ' + O,
   'upper loop : I = 12 / ( 4 + 8 ) = 1 A',
   'V(8 ' + O + ') = 1 &times; 8 = 8 V  &#8658;  V<sub>B2</sub> = 8 V'], F.potentiometer('Fig. 56'), side=True,
  tag='HOTS', title='a galvanometer that reads zero')

m('Two identical batteries (6 V , 1 ' + O + ') are connected in parallel, as shown, to a 2.5 ' + O + ' resistor. '
  'The current in each battery is' + D,
  ['2 A', '1 A', '2.4 A', '0.5 A'], 'B',
  ['identical batteries in parallel &#8594; they share the current equally : I&#8321; = I&#8322; = I / 2',
   'loop (one battery + the resistor) : 6 &#8722; 1 &times; ( I / 2 ) &#8722; 2.5 I = 0  &#8658;  3 I = 6',
   'I = 2 A in the resistor  &#8658;  1 A in each battery'], F.par_batteries('Fig. 57'), side=True,
  title='identical batteries in parallel')

m('In the circuit shown, the three batteries are identical (r = 0) and all resistors equal R. When both switches '
  'K<sub>1</sub> and K<sub>2</sub> are closed, the power consumed in S becomes n times its value when both are '
  'open, where n equals' + D,
  ['3/2', '9/4', '3', '9/16'], 'B',
  ['let V be the p.d. across S. Each connected branch gives ( V<sub>B</sub> &#8722; V ) / R and S takes V / R',
   'both open (1 branch) :  V<sub>B</sub> &#8722; V = V  &#8658;  V = V<sub>B</sub> / 2',
   'both closed (3 branches) :  3 ( V<sub>B</sub> &#8722; V ) = V  &#8658;  V = 3 V<sub>B</sub> / 4',
   'P &#8733; V&#178; :  n = ( 3/4 )&#178; / ( 1/2 )&#178; = 9/4'], F.branches_S('Fig. 58'), side=True, tag='HOTS',
  title='adding sources in parallel')

m('In the single loop shown (all batteries have r = 0), the current in the circuit is' + D,
  ['4.4 A', '2 A', '1.2 A', '3.2 A'], 'B',
  ['the 12 V and 4 V batteries push the current the same way, the 6 V battery opposes them',
   '&#931; V<sub>B</sub> = &#931; I R :  12 + 4 &#8722; 6 = I ( 2 + 3 )',
   'I = 10 / 5 = 2 A'], F.loop3('Fig. 59'), side=True, title='one loop, three batteries')

m('A battery (12 V , 1 ' + O + ') and a battery (6 V , 1 ' + O + ') are connected in parallel (positive to '
  'positive) to a 4 ' + O + ' resistor, as shown. The current in the 4 ' + O + ' resistor is' + D,
  ['2 A', '4 A', '3.6 A', '1 A'], 'A',
  ['let V be the p.d. across the 4 ' + O + ' resistor :',
   '( 12 &#8722; V ) / 1 + ( 6 &#8722; V ) / 1 = V / 4  &#8658;  72 &#8722; 8V = V  &#8658;  V = 8 V',
   'I(4 ' + O + ') = 8 / 4 = 2 A   ( the 12 V battery gives 4 A , the 6 V battery is charged by 2 A )'],
  F.twoloop('Fig. 60', '12 V , 1 ' + O, None, '6 V , 1 ' + O, None, '4 ' + O, cur=False, names=False), side=True,
  title='unequal batteries in parallel')

p('In the circuit shown, the ammeter reads 2 A and the current flows in the direction shown. Each battery has an '
  'internal resistance of 1 ' + O + '. <b>Find</b> the emf V<sub>B2</sub>.',
  'V<sub>B2</sub> = 30 V',
  ['the two batteries oppose each other and the current flows the way V<sub>B2</sub> pushes it',
   'loop :  V<sub>B2</sub> &#8722; 10 = I ( 3 + 5 + 1 + 1 ) = 2 &times; 10 = 20',
   'V<sub>B2</sub> = 30 V   (the 10 V battery is being charged)'], F.find_E2('Fig. 61'), side=True,
  title='finding an unknown emf')

m('For the circuit of Fig. 50, which equation is the correct loop equation for the left loop (the 20 V battery, '
  'the 2 ' + O + ' and the 4 ' + O + ' resistors)?',
  ['20 + 2 I<sub>1</sub> &#8722; 4 I<sub>3</sub> = 0', '20 &#8722; 2 I<sub>1</sub> + 4 I<sub>3</sub> = 0',
   '20 &#8722; 2 I<sub>1</sub> &#8722; 4 I<sub>3</sub> = 0', '20 &#8722; 10 = 2 I<sub>1</sub> + 2 I<sub>2</sub>'], 'C',
  ['go round the left loop in the direction of I&#8321; :',
   'through the battery from &#8722; to + : + 20 ;  through 2 ' + O + ' with I&#8321; : &#8722; 2 I&#8321; ;  '
   'down through 4 ' + O + ' with I&#8323; : &#8722; 4 I&#8323;',
   '20 &#8722; 2 I&#8321; &#8722; 4 I&#8323; = 0   ( check : 20 &#8722; 8 &#8722; 12 = 0 &#10004; )'],
  title='writing a loop equation')

m('In the circuit shown, A<sub>1</sub> reads 5 A and A<sub>2</sub> reads 2 A, while the lamp on the right carries '
  '1.5 A. The reading of A<sub>3</sub> is' + D,
  ['3.5 A', '1.5 A', '3 A', '0.5 A'], 'B',
  ['the main current 5 A divides into the three lamp branches',
   '5 = 2 + I(A&#8323;) + 1.5  &#8658;  I(A&#8323;) = 1.5 A'], F.ammeters_lamps('Fig. 62'), side=True,
  title='the junction rule with ammeters')

m('In the circuit shown, the potential difference between point a and point b (the negative terminal of the '
  'battery) is' + D,
  ['8 V', '4 V', '12 V', '2 V'], 'B',
  ['I = 12 / ( 4 + 2 ) = 2 A',
   'from a to b the current passes only through the 2 ' + O + ' resistor',
   'V(ab) = I &times; 2 = 4 V'], F.vab_loop('Fig. 63'), side=True, title='potential of a point')

m('In the bridge shown, the galvanometer reads zero. The resistance R equals' + D,
  ['60 ' + O, '6.7 ' + O, '15 ' + O, '20 ' + O], 'C',
  ['G reads zero &#8594; the two ends of G are at the same potential (balanced bridge)',
   '10 / 20 = R / 30',
   'R = 15 ' + O], F.wheat('Fig. 64'), side=True, title='a balanced bridge with a galvanometer')

m('In the circuit shown (both batteries have r = 0), the current in the middle branch xy is' + D,
  ['3 A', '1 A', '2 A', '4 A'], 'C',
  ['let V be the potential of x (y = 0) :',
   '( 18 &#8722; V ) / 2 + ( 6 &#8722; V ) / 6 = V / 6  &#8658;  54 &#8722; 3V + 6 &#8722; V = V  &#8658;  V = 12 V',
   'I(middle) = 12 / 6 = 2 A   ( I&#8321; = 3 A ; the 6 V battery is charged by 1 A )'],
  F.twoloop('Fig. 65', '18 V', '2 ' + O, '6 V', '6 ' + O, '6 ' + O), side=True, title='another two-loop circuit')

p('A battery (12 V , 0.5 ' + O + ') is used to charge a battery (9 V , 0.5 ' + O + ') through a 2 ' + O +
  ' resistor. <b>Find:</b> (i) the charging current, (ii) the terminal p.d. of the battery being charged, '
  '(iii) the power stored in it and the power turned into heat.',
  'I = 1 A ; V = 9.5 V ; 9 W stored , 3 W heat',
  ['(i)   I = ( 12 &#8722; 9 ) / ( 2 + 0.5 + 0.5 ) = 3 / 3 = 1 A',
   '(ii)  the 9 V battery is charged : V = 9 + 1 &times; 0.5 = 9.5 V',
   '(iii) stored : V<sub>B</sub> I = 9 &times; 1 = 9 W      heat : I&#178; ( R + r&#8321; + r&#8322; ) = 1 &times; 3 = 3 W',
   '      ( the 12 V battery gives 12 &times; 1 = 12 W = 9 + 3 &#10004; )'],
  F.two_batteries('Fig. 66', '12 V , 0.5 ' + O, '9 V , 0.5 ' + O, '2 ' + O, oppose=True), side=True, tag='HOTS',
  title='one battery charging another')

m('In the circuit shown, the ammeter reads 0.5 A. The emf V<sub>B</sub> of the battery is' + D,
  ['9 V', '6 V', '3 V', '4.5 V'], 'A',
  ['V(6 ' + O + ') = 0.5 &times; 6 = 3 V = V(3 ' + O + ')  &#8658;  I(3) = 3 / 3 = 1 A',
   'junction : I = 0.5 + 1 = 1.5 A through the 4 ' + O,
   'loop : V<sub>B</sub> = 1.5 &times; 4 + 3 = 9 V'], F.amm_branch('Fig. 67'), side=True, title='working backwards to the emf')

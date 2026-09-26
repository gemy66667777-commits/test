# -*- coding: utf-8 -*-
"""Section 3 : Ohm's law for the closed circuit (emf, internal resistance, batteries)."""
from qlib import Section
import figs12 as F

S = Section('s3', 'Ohm&#8217;s Law for the Closed Circuit', 'Lesson 3 &middot; emf &middot; internal resistance '
            '&middot; terminal p.d. &middot; batteries together')
m, p = S.mcq, S.prob
O = '&#937;'
D = ' ..........'

m('A battery of emf 12 V and internal resistance r is being <b>charged</b> by a current I. The potential difference '
  'between its terminals is' + D,
  ['less than 12 V', 'equal to 12 V', 'more than 12 V', 'zero'], 'C',
  ['while charging, the current enters the battery through its positive terminal',
   'V = V<sub>B</sub> + I r  &#8658;  V &gt; 12 V',
   '(while discharging V = V<sub>B</sub> &#8722; I r &lt; V<sub>B</sub>)'], title='charging a battery')

m('In the circuit shown, the reading of the voltmeter is' + D,
  ['12 V', '10 V', '2 V', '8 V'], 'B',
  ['I = V<sub>B</sub> / ( R + r ) = 12 / ( 5 + 1 ) = 2 A',
   'the voltmeter is across the battery terminals : V = V<sub>B</sub> &#8722; I r = 12 &#8722; 2 &times; 1 = 10 V',
   '( = I R = 2 &times; 5 = 10 V )'], F.batt_circuit('Fig. 33'), side=True, title='terminal potential difference')

p('In the circuit shown, the voltmeter reads 12 V when switch K is open and 10 V when K is closed, while the '
  'ammeter then reads 2 A. <b>Find:</b> (i) the emf of the battery, (ii) its internal resistance, (iii) the '
  'resistance R.',
  'V<sub>B</sub> = 12 V , r = 1 ' + O + ' , R = 5 ' + O,
  ['(i)   K open : no current, so the voltmeter reads the emf : V<sub>B</sub> = 12 V',
   '(ii)  K closed : V = V<sub>B</sub> &#8722; I r  &#8658;  10 = 12 &#8722; 2 r  &#8658;  r = 1 ' + O,
   '(iii) R = V / I = 10 / 2 = 5 ' + O],
  F.batt_circuit('Fig. 34', 'V<sub>B</sub> , r', 'R', amm=True, sw=True), side=True, title='open and closed switch')

p('A battery gives a current of 2 A when it is connected to a 5 ' + O + ' resistor, and a current of 1 A when it is '
  'connected to an 11 ' + O + ' resistor. <b>Find</b> its emf and its internal resistance.',
  'V<sub>B</sub> = 12 V , r = 1 ' + O,
  ['V<sub>B</sub> = I&#8321; ( R&#8321; + r ) = 2 ( 5 + r )',
   'V<sub>B</sub> = I&#8322; ( R&#8322; + r ) = 1 ( 11 + r )',
   '10 + 2 r = 11 + r  &#8658;  r = 1 ' + O,
   'V<sub>B</sub> = 2 ( 5 + 1 ) = 12 V'], F.two_circuits('Fig. 35'), title='two resistors, one battery')

m('The voltmeter across the terminals of a battery reads V<sub>0</sub> when no current flows, and 0.75 '
  'V<sub>0</sub> when an external resistor R is connected. The ratio R / r is' + D,
  ['1/3', '3', '4', '0.75'], 'B',
  ['with R connected : V = I R = V<sub>0</sub> R / ( R + r )',
   'R / ( R + r ) = 0.75  &#8658;  R = 0.75 R + 0.75 r  &#8658;  0.25 R = 0.75 r',
   'R / r = 3'], title='terminal p.d. as a fraction of the emf')

p('Two batteries (6 V , 0.5 ' + O + ') and (9 V , 1 ' + O + ') are connected in series, supporting each other, '
  'with a 3.5 ' + O + ' resistor. <b>Find:</b> (i) the current, (ii) the p.d. across each battery.',
  'I = 3 A ; V&#8321; = 4.5 V , V&#8322; = 6 V',
  ['(i)  I = ( 6 + 9 ) / ( 3.5 + 0.5 + 1 ) = 15 / 5 = 3 A',
   '(ii) both discharge : V&#8321; = 6 &#8722; 3 &times; 0.5 = 4.5 V     V&#8322; = 9 &#8722; 3 &times; 1 = 6 V',
   '     check : 4.5 + 6 = 10.5 V = 3 &times; 3.5 &#10004;'],
  F.two_batteries('Fig. 36', '6 V , 0.5 ' + O, '9 V , 1 ' + O, '3.5 ' + O), side=True, title='batteries in series')

m('A battery (12 V , 1 ' + O + ') and a battery (6 V , 1 ' + O + ') are connected in <b>opposition</b> with a '
  '4 ' + O + ' resistor. The potential difference across the terminals of the 6 V battery is' + D,
  ['5 V', '6 V', '7 V', '11 V'], 'C',
  ['opposing : I = ( 12 &#8722; 6 ) / ( 4 + 1 + 1 ) = 6 / 6 = 1 A',
   'the current enters the 6 V battery through its positive terminal &#8594; it is being charged',
   'V = V<sub>B</sub> + I r = 6 + 1 &times; 1 = 7 V'],
  F.two_batteries('Fig. 37', '12 V , 1 ' + O, '6 V , 1 ' + O, '4 ' + O, oppose=True), side=True, tag='HOTS',
  title='two batteries in opposition')

m('The graph shows the terminal potential difference (V) of a battery against the current (I) it delivers. The '
  'internal resistance of the battery is' + D,
  ['2 ' + O, '0.5 ' + O, '6 ' + O, '12 ' + O], 'A',
  ['V = V<sub>B</sub> &#8722; I r : the intercept on the V-axis is V<sub>B</sub> = 12 V',
   'the slope is &#8722; r :  r = 12 / 6 = 2 ' + O,
   '( 6 A is the short-circuit current V<sub>B</sub> / r )'], F.g_terminal('Fig. 38'), side=True,
  title='a terminal-p.d. graph')

m('For the battery of Fig. 38, the current it delivers to an external resistor of 4 ' + O + ' is' + D,
  ['3 A', '1.5 A', '2 A', '6 A'], 'C',
  ['from the graph : V<sub>B</sub> = 12 V , r = 2 ' + O,
   'I = V<sub>B</sub> / ( R + r ) = 12 / ( 4 + 2 ) = 2 A'], title='using the graph')

m('In the circuit shown, when the resistance taken from the rheostat is <b>increased</b>, the reading of the '
  'voltmeter across the battery' + D,
  ['increases', 'decreases', 'stays constant', 'becomes zero'], 'A',
  ['R<sub>v</sub> &#8593; &#8594; I = V<sub>B</sub> / ( R<sub>v</sub> + r ) decreases',
   'V = V<sub>B</sub> &#8722; I r : a smaller I r is lost inside the battery',
   'so V increases (towards V<sub>B</sub>)'],
  F.batt_circuit('Fig. 39', 'V<sub>B</sub> , r', 'R<sub>v</sub>', rv=True), side=True, title='the rheostat and the terminal p.d.')

m('Four identical cells, each of emf 1.5 V and internal resistance 0.5 ' + O + ', are connected in series with a '
  '4 ' + O + ' resistor. The current in the circuit is' + D,
  ['1.5 A', '0.75 A', '1 A', '3 A'], 'C',
  ['total emf = 4 &times; 1.5 = 6 V        total internal resistance = 4 &times; 0.5 = 2 ' + O,
   'I = 6 / ( 4 + 2 ) = 1 A'], title='cells in series')

m('Six identical cells (2 V , 0.5 ' + O + ' each) are connected in series with a 5 ' + O + ' resistor, but one '
  'cell is connected the wrong way round, as shown. The current in the circuit is' + D,
  ['1.5 A', '1 A', '0.5 A', '2 A'], 'B',
  ['the reversed cell cancels one correct cell : emf = ( 5 &#8722; 1 ) &times; 2 = 8 V',
   'the internal resistances all add up : 6 &times; 0.5 = 3 ' + O,
   'I = 8 / ( 5 + 3 ) = 1 A'], F.cells_reversed('Fig. 40'), tag='HOTS', title='a reversed cell')

m('In the circuit shown, the five resistors are identical and the battery has an internal resistance of 1 ' + O +
  '. The voltmeter reads 12 V when K is open and 9 V when K is closed. The value of R is' + D,
  ['1.5 ' + O, '6 ' + O, '4 ' + O, '3 ' + O], 'D',
  ['K open : V<sub>B</sub> = 12 V        K closed : 9 = 12 &#8722; I &times; 1  &#8658;  I = 3 A',
   'external resistance = 9 / 3 = 3 ' + O,
   'the bridge is balanced (R / R = R / R) &#8594; the middle resistor carries no current',
   'network = ( R + R ) // ( R + R ) = R  &#8658;  R = 3 ' + O], F.bridge_battery('Fig. 41'), side=True, tag='HOTS',
  title='a battery feeding a bridge')

m('A battery of emf V<sub>B</sub> and internal resistance r is short-circuited by a thick wire of negligible '
  'resistance. The voltmeter connected across its terminals reads' + D,
  ['V<sub>B</sub>', 'V<sub>B</sub> / 2', 'zero', 'more than V<sub>B</sub>'], 'C',
  ['short circuit : R = 0 &#8658; I = V<sub>B</sub> / r',
   'V = V<sub>B</sub> &#8722; I r = V<sub>B</sub> &#8722; ( V<sub>B</sub> / r ) r = 0'], title='a short circuit')

m('In the circuit shown, the ammeter A<sub>2</sub> reads zero. The reading of the ammeter A<sub>1</sub> is' + D,
  ['4 A', '5 A', '6.4 A', '2.5 A'], 'B',
  ['A&#8322; reads zero &#8658; balanced : 2 / 4 = 3 / R  &#8658;  R = 6 ' + O,
   'branches : 2 + 4 = 6 ' + O + '  and  3 + 6 = 9 ' + O + '  &#8658;  ( 6 &times; 9 ) / 15 = 3.6 ' + O,
   'I = V<sub>B</sub> / ( R&#8242; + r ) = 23 / ( 3.6 + 1 ) = 5 A'], F.balance_A2('Fig. 42'), tag='HOTS',
  title='an ammeter that reads zero')

p('In the circuit shown, the 6 ' + O + ' resistor carries 1 A. Is the internal resistance of the 15 V battery '
  'considered or neglected? <b>Explain</b> with calculation.',
  'considered : r = 1 ' + O,
  ['V(6 ' + O + ') = 1 &times; 6 = 6 V = V(3 ' + O + ')  &#8658;  I(3) = 6 / 3 = 2 A',
   'total current I = 1 + 2 = 3 A  &#8658;  V(2 ' + O + ') = 3 &times; 2 = 6 V',
   'external p.d. = 6 + 6 = 12 V &lt; 15 V &#8594; 3 V is lost inside the battery',
   'r = 3 / 3 = 1 ' + O + '  &#8594; the internal resistance is considered'], F.internal_q('Fig. 43'), side=True,
  title='is r neglected?')

m('Figures (1) and (2) are parts of two closed circuits; in each, a current of 2 A flows in the direction shown. '
  'The ratio V<sub>xy</sub> / V<sub>zk</sub> is' + D,
  ['1/2', '2', '1', '3/4'], 'A',
  ['(1) the current leaves through the positive terminal &#8594; discharging : V = 12 &#8722; 2 &times; 2 = 8 V',
   '(2) the current enters through the positive terminal &#8594; charging : V = 12 + 2 &times; 2 = 16 V',
   'V(xy) / V(zk) = 8 / 16 = 1/2'], F.segments('Fig. 44'), tag='HOTS', title='discharging vs charging')

m('A battery of emf 24 V and internal resistance 1 ' + O + ' is connected to a 7 ' + O + ' resistor. The heat '
  'produced inside the battery in one minute is' + D,
  ['540 J', '9 J', '3780 J', '4320 J'], 'A',
  ['I = 24 / ( 7 + 1 ) = 3 A',
   'W = I&#178; r t = 3&#178; &times; 1 &times; 60 = 540 J'], title='energy lost inside a battery')

p('In the circuit shown, R<sub>1</sub> = 3r and the voltmeter V across the battery reads four times the '
  'voltmeter V<sub>1</sub> across R<sub>1</sub>. <b>Find</b> R<sub>2</sub> in terms of r.',
  'R&#8322; = 9 r',
  ['the same current I flows through R&#8321; and R&#8322;',
   'V (terminal) = I ( R&#8321; + R&#8322; )      V&#8321; = I R&#8321;',
   'V = 4 V&#8321;  &#8658;  R&#8321; + R&#8322; = 4 R&#8321;  &#8658;  R&#8322; = 3 R&#8321;',
   'R&#8322; = 3 &times; 3r = 9 r'], F.r1r2_volt('Fig. 45'), side=True, title='two voltmeters')

m('A battery is connected to a variable resistor R and the graph of 1/I against R is plotted. The emf and the '
  'internal resistance of the battery are' + D,
  ['4 V , 2 ' + O, '2 V , 4 ' + O, '4 V , 0.5 ' + O, '0.25 V , 2 ' + O], 'A',
  ['V<sub>B</sub> = I ( R + r )  &#8658;  1 / I = R / V<sub>B</sub> + r / V<sub>B</sub>',
   'slope = 1 / V<sub>B</sub> = ( 3 &#8722; 0.5 ) / 10 = 0.25  &#8658;  V<sub>B</sub> = 4 V',
   'intercept = r / V<sub>B</sub> = 0.5  &#8658;  r = 0.5 &times; 4 = 2 ' + O], F.g_invI('Fig. 46'), side=True,
  tag='HOTS', title='a 1/I &#8211; R graph')

m('A battery of emf 6 V and internal resistance 0.5 ' + O + ' is charged by a current of 2 A. The potential '
  'difference across its terminals is' + D,
  ['5 V', '6 V', '7 V', '8 V'], 'C',
  ['charging : V = V<sub>B</sub> + I r = 6 + 2 &times; 0.5 = 7 V'], title='the charging voltage')

m('The largest current that a battery of emf 9 V and internal resistance 0.5 ' + O + ' can deliver (when it is '
  'short-circuited) is' + D,
  ['4.5 A', '9 A', '18 A', 'infinite'], 'C',
  ['short circuit : R = 0',
   'I(max) = V<sub>B</sub> / r = 9 / 0.5 = 18 A'], title='the short-circuit current')

p('A lamp labelled (6 V , 3 W) is connected in series with a rheostat to a battery of emf 9 V and internal '
  'resistance 1 ' + O + '. <b>Find</b> the resistance that must be taken from the rheostat for the lamp to work '
  'normally.',
  'R<sub>v</sub> = 5 ' + O,
  ['normal working : I = P / V = 3 / 6 = 0.5 A ,  R(lamp) = V&#178; / P = 36 / 3 = 12 ' + O,
   'V<sub>B</sub> = I ( R(lamp) + R<sub>v</sub> + r )  &#8658;  9 = 0.5 ( 12 + R<sub>v</sub> + 1 )',
   '18 = 13 + R<sub>v</sub>  &#8658;  R<sub>v</sub> = 5 ' + O], F.lamp_rheo('Fig. 47'), side=True,
  title='making a lamp work normally')

p('A battery delivers the same power to an external resistor of 4 ' + O + ' as to one of 9 ' + O + '. '
  '<b>Find</b> its internal resistance.',
  'r = 6 ' + O,
  ['P = I&#178; R = V<sub>B</sub>&#178; R / ( R + r )&#178;',
   '4 / ( 4 + r )&#178; = 9 / ( 9 + r )&#178;  &#8658;  2 / ( 4 + r ) = 3 / ( 9 + r )',
   '18 + 2 r = 12 + 3 r  &#8658;  r = 6 ' + O,
   'check : 4 / 100 = 9 / 225 = 0.04 &#10004;'], tag='HOTS', title='equal power in two resistors')

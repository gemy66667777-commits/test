# -*- coding: utf-8 -*-
import base64
import figs_bank as B
import figs_moment as M
from css import CSS

WM = ('<svg xmlns="http://www.w3.org/2000/svg" width="330" height="215">'
      '<text x="165" y="120" font-family="Helvetica,Arial,sans-serif" font-size="30" font-weight="700" '
      'fill="#0f2f5b" fill-opacity="0.055" text-anchor="middle" '
      'transform="rotate(-27 165 120)">Mr. Gemy</text></svg>')
WM64 = base64.b64encode(WM.encode()).decode()

H = []
a = H.append
a('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Physics Question Bank</title><style>'
  + CSS + """
body { background-image:url("data:image/svg+xml;base64,%s"); background-repeat:repeat; }
.head3 { background:linear-gradient(100deg,#0f2f5b 0%%,#155e75 55%%,#0e7490 100%%); }
h2 { border-left-color:#0e7490; }
.sec { background:linear-gradient(100deg,#0f2f5b,#1d4ed8); color:#fff; border-radius:9px; padding:8px 14px;
       margin:16px 0 9px; display:flex; justify-content:space-between; align-items:center; break-after:avoid; }
.sec h2 { all:unset; font-size:14pt; font-weight:700; }
.sec .cnt { font-size:9.5pt; background:rgba(255,255,255,.18); border:1.4px solid rgba(255,255,255,.45);
            border-radius:6px; padding:3px 9px; }
.q { background:rgba(255,255,255,.72); }
.q .n { background:#0e7490; }
.ch b { color:#0e7490; }
.ch div { background:rgba(255,255,255,.85); }
.tag { float:right; font-size:8.5pt; color:#64748b; border:1px solid #cbd5e1; border-radius:5px;
       padding:1px 7px; background:#f8fafc; }
.anstab td { font-size:9.6pt; padding:4px 7px; }
.anstab td.qn { font-weight:700; color:#0e7490; width:5%%; text-align:center; }
.sol2 { border:1.2px solid #cbd5e1; border-left:4.5px solid #0e7490; border-radius:0 8px 8px 0;
        background:rgba(255,255,255,.78); padding:5px 11px 6px; margin:7px 0; break-inside:avoid; }
.sol2 .sn { display:inline-block; background:#0e7490; color:#fff; border-radius:5px; padding:1px 8px;
        font-weight:700; font-size:9.5pt; margin-right:7px; }
.sol2 .hd { font-size:9.6pt; color:#475569; }
.sol2 pre { font-family:"Liberation Mono","DejaVu Sans Mono",monospace; font-size:9.3pt; line-height:1.5;
        margin:4px 0 0; white-space:pre-wrap; color:#0f172a; }
.sol2 .fa { color:#15803d; font-weight:700; }
""" % WM64 + '</style></head><body>')

a('<div class="head head3"><div><h1>Physics Question Bank &mdash; 60 Questions</h1>'
  '<div class="sub">Relative Velocity &middot; Horizontal Projectiles &middot; Projectiles at an Angle &middot; '
  'Moment of a Force</div></div>'
  '<div class="badge">Mr. Gemy<br>Grade 11 &middot; Physics<br>Questions only</div></div>')

a('<div class="box formula" style="text-align:left"><b>Data used in all questions:</b> &nbsp; g = 10 m/s&sup2; '
  '&nbsp;|&nbsp; air resistance is neglected &nbsp;|&nbsp; 1 km/h = 1/3.6 m/s<br>'
  'sin 30&deg; = 0.5 , cos 30&deg; = 0.866 &nbsp;|&nbsp; sin 37&deg; = 0.6 , cos 37&deg; = 0.8 &nbsp;|&nbsp; '
  'sin 40&deg; = 0.643 , cos 40&deg; = 0.766 &nbsp;|&nbsp; sin 45&deg; = cos 45&deg; = 0.707 &nbsp;|&nbsp; '
  'sin 53&deg; = 0.8 , cos 53&deg; = 0.6 &nbsp;|&nbsp; sin 60&deg; = 0.866 , cos 60&deg; = 0.5</div>')

QN = [0]
ANS = []


def sec(title, rng):
    a('<div class="sec"><h2>' + title + '</h2><span class="cnt">Questions ' + rng + '</span></div>')


def q(text, ans, fig=None, ch=None, tag=None):
    QN[0] += 1
    ANS.append((QN[0], ans))
    a('<div class="q">' + ('<span class="tag">' + tag + '</span>' if tag else '') +
      '<span class="n">' + str(QN[0]) + '</span>' + text)
    if fig:
        a(fig)
    if ch:
        a('<div class="ch">')
        for L, c in zip('ABCD', ch):
            a('<div><b>' + L + ')</b> ' + c + '</div>')
        a('</div>')
    a('</div>')


# ======================= SECTION 1 : RELATIVE VELOCITY =======================
sec('Section 1 &nbsp;&mdash;&nbsp; Relative Velocity (vectors)', '1 &ndash; 15')

q('Two cars A and B move along a straight road <b>in the same direction</b> with velocities of 90 km/h and '
  '60 km/h. The velocity of car A relative to car B is:',
  'B) 30 km/h',
  B.cars_road('Fig. 1', 'A : 90 km/h', 'B : 60 km/h', True),
  ['150 km/h', '30 km/h', '75 km/h', 'zero'], 'MCQ')

q('Two cars move along the same straight road <b>in opposite directions</b> with velocities of 20 m/s and '
  '15 m/s. The magnitude of the velocity of one of them relative to the other is:',
  'C) 35 m/s',
  B.cars_road('Fig. 2', 'A : 20 m/s', 'B : 15 m/s', False),
  ['5 m/s', '20 m/s', '35 m/s', '300 m/s'], 'MCQ')

q('Car A moves at 72 km/h and car B moves at 54 km/h in the same direction, and car A is 150 m behind car B. '
  'Find: <b>(i)</b> the velocity of A relative to B in m/s, &nbsp;<b>(ii)</b> the time taken by A to catch up with B.',
  '(i) 5 m/s &nbsp; (ii) 30 s')

q('Two cars approach each other along a straight road with velocities of 30 m/s and 20 m/s, and the distance '
  'between them is 500 m. Find: <b>(i)</b> the relative velocity, &nbsp;<b>(ii)</b> the time before they meet.',
  '(i) 50 m/s &nbsp; (ii) 10 s')

q('A train moves horizontally at 20 m/s, and a man inside it walks at 1.5 m/s <b>in the direction of motion</b> '
  'of the train. The velocity of the man relative to the ground is:',
  'C) 21.5 m/s',
  B.train_man('Fig. 3', 'v = 20 m/s', '1.5 m/s', True),
  ['1.5 m/s', '18.5 m/s', '21.5 m/s', '30 m/s'], 'MCQ')

q('A train moves at 15 m/s, and a man inside it walks at 2 m/s in a direction <b>opposite</b> to the motion of '
  'the train. The velocity of the man relative to the ground is:',
  'B) 13 m/s',
  B.train_man('Fig. 4', 'v = 15 m/s', '2 m/s', False),
  ['17 m/s', '13 m/s', '2 m/s', 'zero'], 'MCQ')

q('Two cars move side by side along a straight road with <b>equal velocities in the same direction</b>. '
  'The velocity of one of them relative to the other is:',
  'A) zero', None,
  ['zero', 'double the velocity of each car', 'equal to the velocity of each car', 'cannot be determined'], 'MCQ')

q('Car A moves eastwards at 30 m/s and car B moves northwards at 40 m/s as shown. Find the magnitude and the '
  'direction of the velocity of car A relative to car B.',
  '50 m/s , 53&deg; south of east',
  B.cars_cross('Fig. 5', '30 m/s', '40 m/s'))

q('A boat whose velocity in still water is 4 m/s crosses a river of width 80 m, heading <b>perpendicular</b> to '
  'the bank, while the river flows at 3 m/s. Find: <b>(i)</b> the resultant velocity of the boat, '
  '<b>(ii)</b> the time of crossing, <b>(iii)</b> the drift along the river.',
  '(i) 5 m/s &nbsp; (ii) 20 s &nbsp; (iii) 60 m',
  B.boat_river('Fig. 6', 'w = 80 m', '4 m/s', '3 m/s'))

q('For the same boat and the same river of question 9, the boat must land at the point exactly opposite to the '
  'starting point. Find: <b>(i)</b> the angle at which the boat must be directed upstream, '
  '<b>(ii)</b> its resultant velocity, <b>(iii)</b> the time of crossing.',
  '(i) 48.6&deg; upstream &nbsp; (ii) 2.65 m/s &nbsp; (iii) 30.2 s')

q('A boat crosses a river heading perpendicular to the bank. The time taken to cross the river depends on:',
  'B) the width of the river and the velocity of the boat only', None,
  ['the velocity of the river current only',
   'the width of the river and the velocity of the boat only',
   'the width of the river and the resultant velocity',
   'the drift along the river'], 'MCQ')

q('Rain falls vertically downwards with a velocity of 8.66 m/s, while a man runs horizontally at 5 m/s. '
  'Find the magnitude and the direction of the velocity of the rain relative to the man.',
  '10 m/s , 30&deg; from the vertical',
  B.rain_man('Fig. 7', 'rain : 8.66 m/s', '5 m/s'))

q('A man walks horizontally at 4 m/s, and the rain appears to him to fall at 45&deg; to the vertical. '
  'Find the actual velocity of the rain falling vertically.',
  '4 m/s')

q('The velocity of a boat has two perpendicular components: 6 m/s directed east and 8 m/s directed north. '
  'The magnitude of the resultant velocity of the boat is:',
  'B) 10 m/s',
  B.vec_pair('Fig. 8', 'v&#8321; = 6 m/s', 'v&#8322; = 8 m/s', 90),
  ['2 m/s', '10 m/s', '14 m/s', '48 m/s'], 'MCQ')

q('Two velocities of magnitudes 5 m/s and 3 m/s act at a point, and the angle between them is 60&deg;. '
  'Find the magnitude of the resultant velocity and its direction relative to the larger velocity.',
  '7 m/s , 21.8&deg; from the 5 m/s velocity',
  B.vec_pair('Fig. 9', 'v&#8321; = 5 m/s', 'v&#8322; = 3 m/s', 60))

# ================= SECTION 2 : HORIZONTAL PROJECTILES & FREE FALL =================
sec('Section 2 &nbsp;&mdash;&nbsp; Projection without an angle (horizontal projectiles &amp; free fall)', '16 &ndash; 30')

q('A ball rolls off the edge of a table of height 1.25 m with a horizontal velocity of 3 m/s. '
  'The time taken by the ball to reach the floor is:',
  'B) 0.5 s',
  B.table_proj('Fig. 10', 'h = 1.25 m', 'v = 3 m/s'),
  ['0.25 s', '0.5 s', '1.25 s', '2.5 s'], 'MCQ')

q('For the ball of question 16, the horizontal distance covered before reaching the floor equals:',
  'B) 1.5 m', None, ['0.75 m', '1.5 m', '3 m', '6 m'], 'MCQ')

q('For the same ball of question 16, find the magnitude of the velocity with which the ball hits the floor and '
  'its direction with the horizontal.',
  '5.83 m/s , 59&deg; below the horizontal')

q('Two balls X and Y are released at the same instant from the same height: X is projected horizontally and Y '
  'is dropped from rest. Neglecting air resistance:',
  'C) both reach the ground at the same instant',
  B.two_balls('Fig. 11'),
  ['X reaches the ground first', 'Y reaches the ground first',
   'both reach the ground at the same instant', 'it depends on the mass of each ball'], 'MCQ')

q('A stone is thrown horizontally with a velocity of 20 m/s from the top of a cliff of height 45 m. Find: '
  '<b>(i)</b> the time of flight, <b>(ii)</b> the horizontal distance from the base of the cliff, '
  '<b>(iii)</b> the magnitude of the velocity on hitting the ground.',
  '(i) 3 s &nbsp; (ii) 60 m &nbsp; (iii) 36.06 m/s',
  B.table_proj('Fig. 12', 'h = 45 m', 'v = 20 m/s', 'R = ?', False))

q('An aeroplane flies horizontally at 100 m/s at a height of 500 m above the ground and releases a package. '
  'The time taken by the package to reach the ground is:',
  'C) 10 s',
  B.plane_drop('Fig. 13', '500 m', 'v = 100 m/s'),
  ['5 s', '7.07 s', '10 s', '50 s'], 'MCQ')

q('For the package of question 21, the horizontal distance covered by the package from the instant of release '
  'until it reaches the ground equals:',
  'D) 1000 m', None, ['100 m', '250 m', '500 m', '1000 m'], 'MCQ')

q('For the package of question 21, and as seen by the pilot of the aeroplane, the package falls:',
  'C) vertically downwards, always directly below the aeroplane', None,
  ['backwards, behind the aeroplane', 'forwards, in front of the aeroplane',
   'vertically downwards, always directly below the aeroplane', 'in a horizontal straight line'], 'MCQ')

q('A ball leaves the edge of a table with a horizontal velocity of 5 m/s and lands on the floor at a horizontal '
  'distance of 2 m from the base of the table. Find the height of the table.',
  'h = 0.8 m',
  B.table_proj('Fig. 14', 'h = ?', 'v = 5 m/s', 'R = 2 m'))

q('For a body projected horizontally, the horizontal component of its velocity during the flight:',
  'C) remains constant', None,
  ['increases uniformly', 'decreases uniformly', 'remains constant', 'becomes zero at the ground'], 'MCQ')

q('A body is projected horizontally with a velocity of 15 m/s from a height of 20 m. '
  'Find the magnitude of its velocity 1 second after projection.',
  '18.03 m/s')

q('A body projected horizontally reaches the ground after 4 s. The height from which it was projected equals:',
  'C) 80 m', None, ['20 m', '40 m', '80 m', '160 m'], 'MCQ')

q('A body falls freely from rest. Find: <b>(i)</b> the distance it covers during the first 3 seconds, '
  '<b>(ii)</b> its velocity at the end of this time.',
  '(i) 45 m &nbsp; (ii) 30 m/s')

q('A ball is dropped from rest from a height of 20 m. The time taken to reach the ground and the velocity with '
  'which it hits the ground are:',
  'B) 2 s and 20 m/s', None,
  ['1 s and 10 m/s', '2 s and 20 m/s', '2 s and 10 m/s', '4 s and 40 m/s'], 'MCQ')

q('Two balls are projected horizontally from the same height with velocities of 10 m/s and 20 m/s. '
  'Compare: <b>(i)</b> their times of flight, <b>(ii)</b> their horizontal ranges.',
  '(i) equal times &nbsp; (ii) ranges in the ratio 1 : 2')

# ================= SECTION 3 : PROJECTILES AT AN ANGLE =================
a('<div class="pb"></div>')
sec('Section 3 &nbsp;&mdash;&nbsp; Projection at an angle to the horizontal', '31 &ndash; 45')

q('A projectile is fired from the ground with a velocity of 40 m/s at 30&deg; to the horizontal. '
  'Its total time of flight is:',
  'B) 4 s',
  B.proj_traj('Fig. 15', 30, 'v&#8320; = 40 m/s', '30&deg;', ask='T = ?'),
  ['2 s', '4 s', '6 s', '8 s'], 'MCQ')

q('For the projectile of question 31, the maximum height reached above the ground equals:',
  'B) 20 m',
  B.proj_traj('Fig. 16', 30, 'v&#8320; = 40 m/s', '30&deg;', show_H=True),
  ['10 m', '20 m', '40 m', '80 m'], 'MCQ')

q('For the same projectile of question 31, find its horizontal range.',
  'R = 138.6 m',
  B.proj_traj('Fig. 17', 30, 'v&#8320; = 40 m/s', '30&deg;', show_R=True))

q('A body is projected with a fixed initial speed. The horizontal range is a <b>maximum</b> when the angle of '
  'projection to the horizontal equals:',
  'C) 45&deg;', None, ['30&deg;', '37&deg;', '45&deg;', '90&deg;'], 'MCQ')

q('A projectile is fired at 25&deg; to the horizontal with an initial speed v. It reaches the <b>same horizontal '
  'range</b> when it is fired with the same speed at an angle of:',
  'C) 65&deg;', None, ['35&deg;', '45&deg;', '65&deg;', '75&deg;'], 'MCQ')

q('A ball is projected with a velocity of 50 m/s at 53&deg; to the horizontal. Find: <b>(i)</b> the two '
  'components of the initial velocity, <b>(ii)</b> the time taken to reach the maximum height, '
  '<b>(iii)</b> the total time of flight, <b>(iv)</b> the maximum height, <b>(v)</b> the horizontal range.',
  '(i) 30 m/s , 40 m/s &nbsp; (ii) 4 s &nbsp; (iii) 8 s &nbsp; (iv) 80 m &nbsp; (v) 240 m',
  B.proj_traj('Fig. 18', 53, 'v&#8320; = 50 m/s', '53&deg;'))

q('For the ball of question 36, its speed at the highest point P of the path equals:',
  'B) 30 m/s',
  B.proj_traj('Fig. 19', 53, 'v&#8320; = 50 m/s', '53&deg;', show_top=True),
  ['zero', '30 m/s', '40 m/s', '50 m/s'], 'MCQ')

q('For the same ball of question 36, find the magnitude and the direction of its velocity 2 seconds after the '
  'instant of projection.',
  '36.06 m/s , 33.7&deg; above the horizontal')

q('A boy standing on the roof of a building of height 45 m throws a ball with a velocity of 20 m/s at 30&deg; '
  'to the horizontal. Find: <b>(i)</b> the time taken by the ball to reach the ground, <b>(ii)</b> the '
  'horizontal distance R from the base of the building.',
  '(i) 4.16 s &nbsp; (ii) 72.05 m',
  B.building_proj('Fig. 20', 'h = 45 m', 'v&#8320; = 20 m/s', '30&deg;'))

q('A hose sprays a water jet at 20 m/s at 40&deg; to the horizontal, towards a wall at a horizontal distance of '
  '8 m from the nozzle. Find the height h at which the water hits the wall above the level of the nozzle.',
  'h = 5.35 m',
  B.hose_wall('Fig. 21', 'v&#8320; = 20 m/s', '40&deg;', '8 m'))

q('At the highest point of the path of a projectile fired at an angle to the horizontal, the acceleration of '
  'the projectile is:',
  'C) 10 m/s&sup2; directed vertically downwards', None,
  ['zero', '10 m/s&sup2; directed vertically upwards', '10 m/s&sup2; directed vertically downwards',
   'directed along the path'], 'MCQ')

q('A football is kicked from the ground with a velocity of 20 m/s at 45&deg; to the horizontal, towards a wall '
  'of height 4 m standing at a horizontal distance of 30 m. Find the height of the ball when it reaches the '
  'wall, and decide whether the ball passes over the wall or not.',
  'y = 7.5 m , so the ball passes over the wall',
  B.wall_kick('Fig. 22', 'v&#8320; = 20 m/s', '45&deg;', '30 m', 'wall : 4 m'))

q('A body is projected at an angle &theta; to the horizontal with an initial velocity v<sub>i</sub>. '
  'If v<sub>ix</sub> = v<sub>iy</sub> = 20 m/s, then v<sub>i</sub> and &theta; are:',
  'B) 28.3 m/s and 45&deg;', None,
  ['40 m/s and 60&deg;', '28.3 m/s and 45&deg;', '40 m/s and 45&deg;', '28.3 m/s and 30&deg;'], 'MCQ')

q('A projectile fired from the ground has a total time of flight of 6 s and a horizontal range of 300 m. '
  'Find its initial velocity and its angle of projection.',
  'v&#8320; = 58.3 m/s , &theta; = 31&deg;')

q('A body is projected at an angle &theta; to the horizontal. If v<sub>iy</sub> = 2 v<sub>ix</sub>, '
  'then the value of &theta; is:',
  'C) 63.43&deg;', None, ['26.57&deg;', '30&deg;', '63.43&deg;', '75&deg;'], 'MCQ')

# ================= SECTION 4 : MOMENT OF A FORCE =================
a('<div class="pb"></div>')
sec('Section 4 &nbsp;&mdash;&nbsp; Moment of a force about a point', '46 &ndash; 60')
a('<p style="font-size:10pt;color:#475569;margin:2px 0 8px">In this section take the <b>anticlockwise</b> '
  'moment as positive and the <b>clockwise</b> moment as negative.</p>')

q('A force of 40 N acts at the end A of a rod OA of length 0.5 m, perpendicular to the rod as shown. '
  'The moment of the force about O is:',
  'B) &minus; 20 N&middot;m (clockwise)',
  M.rod_fig('Fig. 23', 'L = 0.5 m', 'F = 40 N', -90, maxw=370),
  ['+ 20 N&middot;m', '&minus; 20 N&middot;m', '&minus; 80 N&middot;m', 'zero'], 'MCQ')

q('A spanner of length 0.25 m is used to loosen a nut. Find the force that must be applied perpendicular to the '
  'spanner to produce a moment of 15 N&middot;m about the centre of the nut.',
  'F = 60 N',
  M.spanner('Fig. 24', 'L = 0.25 m', 'F = ?', 390))

q('A force of 50 N acts at the end of a rod of length 2 m, making an angle of 30&deg; with the rod. '
  'Find the moment of the force about the hinge O.',
  '+ 50 N&middot;m (anticlockwise)',
  M.rod_fig('Fig. 25', 'L = 2 m', 'F = 50 N', 30, maxw=380))

q('A force of 60 N acts at the end of a rod of length 1.5 m, making an angle of 120&deg; with the rod. '
  'Find the moment of the force about O.',
  '+ 77.9 N&middot;m (anticlockwise)',
  M.rod_fig('Fig. 26', 'L = 1.5 m', 'F = 60 N', 120, maxw=390))

q('The moment of a force about a point is equal to zero when:',
  'C) the line of action of the force passes through the point', None,
  ['the force is perpendicular to the rod', 'the force makes 45&deg; with the rod',
   'the line of action of the force passes through the point', 'the force is large and the arm is small'], 'MCQ')

q('Find the resultant moment about O of the two forces acting on the bar shown, and state its sense of rotation.',
  '+ 110 N&middot;m (anticlockwise)',
  M.bar_forces('Fig. 27', [(-2, '25 N', 'down'), (1.5, '40 N', 'up')], 440))

q('Find the resultant moment about O of the three forces acting on the bar shown.',
  '&minus; 50 N&middot;m (clockwise)',
  M.bar_forces('Fig. 28', [(-2, '30 N', 'up'), (1, '50 N', 'down'), (3, '20 N', 'up')], 460))

q('A force of 45 N acts along the tangent at the rim of a wheel of radius 0.2 m. Find the moment of the force '
  'about the centre of the wheel.',
  '9 N&middot;m',
  M.wheel('Fig. 29', 'r = 0.2 m', 'F = 45 N', 360))

q('A door of width 0.8 m is pushed at its outer edge by a force of 30 N making an angle of 40&deg; with the '
  'door. Find the moment of the force about the hinge.',
  '15.4 N&middot;m',
  M.door_top('Fig. 30', 'width = 0.8 m', 'F = 30 N', 40, 400))

q('The SI unit of the moment of a force is:',
  'B) N&middot;m', None, ['N', 'N&middot;m', 'N/m', 'm/N'], 'MCQ')

q('A force of 40 N acts at the end of a rod of length 1.2 m and produces a moment of 24 N&middot;m about O. '
  'Find the angle between the force and the rod.',
  '&theta; = 30&deg;',
  M.rod_fig('Fig. 31', 'L = 1.2 m', 'F = 40 N', 55, '&theta; = ?', maxw=370))

q('For a given force acting at the end of a given rod, the moment of the force about the hinge is a maximum '
  'when the angle between the force and the rod equals:',
  'D) 90&deg;', None, ['zero', '30&deg;', '60&deg;', '90&deg;'], 'MCQ')

q('The same force of 60 N acts at the end of the same rod of length 1 m in the two positions shown. '
  'Find the moment in each case, then find the ratio M<sub>a</sub> : M<sub>b</sub>.',
  'M<sub>a</sub> = 60 N&middot;m , M<sub>b</sub> = 42.4 N&middot;m , ratio = 1.41 : 1',
  M.two_panel('Fig. 32', 90, '(a)  F &perp; to the rod', 45, '(b)  F at 45&deg; to the rod', 450))

q('Find the resultant moment about O of the two forces acting on the bar shown, and state the sense of rotation '
  'of the bar.',
  '&minus; 120 N&middot;m (clockwise)',
  M.bar_forces('Fig. 33', [(-2.5, '20 N', 'up'), (2, '35 N', 'down')], 440))

q('A force F acts at the end of a rod hinged at O. Which of the following angles between the force and the rod '
  'gives the <b>smallest</b> moment about O?',
  'A) 20&deg;', None, ['20&deg;', '45&deg;', '60&deg;', '90&deg;'], 'MCQ')

# ============================ ANSWERS ============================
a('<div class="pb"></div>')
a('<h2><span class="num">&#10003;</span>Model answer &mdash; final answers only</h2>')
a('<div class="box note">Only the final answer of every question is given. All the steps of the solution must '
  'be written by the student.</div>')
a('<table class="anstab"><tr><th style="width:5%">Q</th><th>Final answer</th>'
  '<th style="width:5%">Q</th><th>Final answer</th></tr>')
half = (len(ANS) + 1) // 2
for i in range(half):
    l = ANS[i]; r = ANS[i + half] if i + half < len(ANS) else ('', '')
    a('<tr><td class="qn">' + str(l[0]) + '</td><td>' + l[1] + '</td>'
      '<td class="qn">' + str(r[0]) + '</td><td>' + r[1] + '</td></tr>')
a('</table>')


# ============================ STEP-BY-STEP SOLUTIONS ============================
a('<div class="pb"></div>')
a('<h2><span class="num">&#9998;</span>Solutions &mdash; step by step</h2>')
a('<div class="box note">The full working of every question, from the first step to the final answer. '
  'Use it only after trying the question by yourself.</div>')


def sol(n, hd, steps, fa):
    a('<div class="sol2"><span class="sn">' + str(n) + '</span><span class="hd">' + hd + '</span>'
      '<pre>' + steps + '\n<span class="fa">Final answer : ' + fa + '</span></pre></div>')


a('<h3>Section 1 &mdash; Relative velocity</h3>')
sol(1, 'same direction', 'v(A rel B) = v(A) &minus; v(B)\n            = 90 &minus; 60 = 30 km/h', 'B) 30 km/h')
sol(2, 'opposite directions', 'v(A rel B) = v(A) &minus; ( &minus; v(B) ) = v(A) + v(B)\n'
    '            = 20 + 15 = 35 m/s', 'C) 35 m/s')
sol(3, 'catching up', 'v(A) = 72 / 3.6 = 20 m/s        v(B) = 54 / 3.6 = 15 m/s\n'
    '(i)  v(A rel B) = 20 &minus; 15 = 5 m/s\n(ii) t = d / v(rel) = 150 / 5 = 30 s', '(i) 5 m/s   (ii) 30 s')
sol(4, 'approaching cars', '(i)  v(rel) = 30 + 20 = 50 m/s   (opposite directions)\n'
    '(ii) t = 500 / 50 = 10 s', '(i) 50 m/s   (ii) 10 s')
sol(5, 'man inside a train', 'v(man rel ground) = v(man rel train) + v(train)\n'
    '                  = 1.5 + 20 = 21.5 m/s', 'C) 21.5 m/s')
sol(6, 'man walking backwards', 'v(man rel ground) = 15 &minus; 2 = 13 m/s', 'B) 13 m/s')
sol(7, 'equal velocities', 'v(A rel B) = v(A) &minus; v(B) = v &minus; v = 0', 'A) zero')
sol(8, 'perpendicular velocities', 'v(A rel B) = v(A) &minus; v(B) = 30 (east) + 40 (south)\n'
    '| v | = &radic;( 30&sup2; + 40&sup2; ) = &radic;2500 = 50 m/s\n'
    'tan &theta; = 40 / 30 = 1.333   &rarr;   &theta; = 53&deg;', '50 m/s , 53&deg; south of east')
sol(9, 'boat heading straight across', '(i)   v = &radic;( 4&sup2; + 3&sup2; ) = 5 m/s\n'
    '(ii)  t = width / v(boat) = 80 / 4 = 20 s      (the current does not affect the time)\n'
    '(iii) drift = v(river) &times; t = 3 &times; 20 = 60 m', '(i) 5 m/s   (ii) 20 s   (iii) 60 m')
sol(10, 'landing exactly opposite', '(i)   sin &alpha; = v(river) / v(boat) = 3 / 4 = 0.75  &rarr;  &alpha; = 48.6&deg; upstream\n'
    '(ii)  v = &radic;( 4&sup2; &minus; 3&sup2; ) = &radic;7 = 2.65 m/s\n'
    '(iii) t = 80 / 2.65 = 30.2 s', '(i) 48.6&deg;   (ii) 2.65 m/s   (iii) 30.2 s')
sol(11, 'time of crossing', 't = width / v(boat)   &mdash;  only the component perpendicular to the bank\n'
    'carries the boat across, so the current changes the drift, not the time.',
    'B) the width and the velocity of the boat only')
sol(12, 'rain relative to a man', 'v(rain rel man) = v(rain) &minus; v(man)\n'
    '| v | = &radic;( 8.66&sup2; + 5&sup2; ) = &radic;100 = 10 m/s\n'
    'tan &theta; = 5 / 8.66 = 0.577   &rarr;   &theta; = 30&deg; from the vertical', '10 m/s , 30&deg; from the vertical')
sol(13, 'finding the rain speed', 'tan 45&deg; = v(man) / v(rain)\n1 = 4 / v(rain)   &rarr;   v(rain) = 4 m/s', '4 m/s')
sol(14, 'perpendicular components', 'v = &radic;( 6&sup2; + 8&sup2; ) = &radic;100 = 10 m/s', 'B) 10 m/s')
sol(15, 'two velocities at 60&deg;', 'v = &radic;( 5&sup2; + 3&sup2; + 2 &times; 5 &times; 3 &times; cos 60&deg; )\n'
    '  = &radic;( 25 + 9 + 15 ) = &radic;49 = 7 m/s\n'
    'tan &alpha; = ( 3 sin 60&deg; ) / ( 5 + 3 cos 60&deg; ) = 2.598 / 6.5 = 0.3997\n'
    '&alpha; = 21.8&deg;', '7 m/s , 21.8&deg; from the 5 m/s velocity')

a('<h3>Section 2 &mdash; Projection without an angle</h3>')
sol(16, 'time of fall', 'the vertical motion is a free fall :   h = &frac12; g t&sup2;\n'
    't = &radic;( 2h / g ) = &radic;( 2 &times; 1.25 / 10 ) = &radic;0.25 = 0.5 s', 'B) 0.5 s')
sol(17, 'horizontal distance', 'x = v &times; t = 3 &times; 0.5 = 1.5 m    (the horizontal velocity is constant)', 'B) 1.5 m')
sol(18, 'landing velocity', 'v(y) = g t = 10 &times; 0.5 = 5 m/s        v(x) = 3 m/s\n'
    'v = &radic;( 3&sup2; + 5&sup2; ) = &radic;34 = 5.83 m/s\n'
    'tan &theta; = 5 / 3   &rarr;   &theta; = 59&deg;', '5.83 m/s , 59&deg; below the horizontal')
sol(19, 'dropped and projected', 'both bodies have the same vertical motion :  v(y) = 0 at the start and a = g\n'
    'the horizontal velocity of X does not change its time of fall.', 'C) both reach the ground at the same instant')
sol(20, 'stone from a cliff', '(i)   t = &radic;( 2h / g ) = &radic;( 2 &times; 45 / 10 ) = &radic;9 = 3 s\n'
    '(ii)  R = v t = 20 &times; 3 = 60 m\n'
    '(iii) v(y) = g t = 30 m/s   &rarr;  v = &radic;( 20&sup2; + 30&sup2; ) = &radic;1300 = 36.06 m/s',
    '(i) 3 s   (ii) 60 m   (iii) 36.06 m/s')
sol(21, 'package from a plane', 't = &radic;( 2h / g ) = &radic;( 2 &times; 500 / 10 ) = &radic;100 = 10 s', 'C) 10 s')
sol(22, 'horizontal distance', 'x = v t = 100 &times; 10 = 1000 m', 'D) 1000 m')
sol(23, 'as seen by the pilot', 'the package keeps the horizontal velocity of the plane (100 m/s),\n'
    'so plane and package always have the same horizontal position.',
    'C) vertically downwards, below the aeroplane')
sol(24, 'height of the table', 't = x / v = 2 / 5 = 0.4 s\nh = &frac12; g t&sup2; = &frac12; &times; 10 &times; 0.16 = 0.8 m', 'h = 0.8 m')
sol(25, 'horizontal component', 'no horizontal force acts  &rarr;  a(x) = 0  &rarr;  v(x) is constant', 'C) remains constant')
sol(26, 'velocity after 1 s', 'v(y) = g t = 10 &times; 1 = 10 m/s        v(x) = 15 m/s\n'
    'v = &radic;( 15&sup2; + 10&sup2; ) = &radic;325 = 18.03 m/s', '18.03 m/s')
sol(27, 'height of projection', 'h = &frac12; g t&sup2; = &frac12; &times; 10 &times; 4&sup2; = 80 m', 'C) 80 m')
sol(28, 'free fall', '(i)  d = &frac12; g t&sup2; = &frac12; &times; 10 &times; 9 = 45 m\n(ii) v = g t = 10 &times; 3 = 30 m/s',
    '(i) 45 m   (ii) 30 m/s')
sol(29, 'dropped ball', 't = &radic;( 2h / g ) = &radic;( 2 &times; 20 / 10 ) = 2 s\nv = g t = 10 &times; 2 = 20 m/s', 'B) 2 s and 20 m/s')
sol(30, 'two horizontal projectiles', '(i)  t = &radic;( 2h / g )  &mdash; depends on the height only  &rarr;  equal times\n'
    '(ii) R = v t   &rarr;   R&#8321; : R&#8322; = 10 : 20 = 1 : 2', '(i) equal   (ii) 1 : 2')

a('<h3>Section 3 &mdash; Projection at an angle</h3>')
sol(31, 'time of flight', 'v(iy) = v&#8320; sin &theta; = 40 &times; sin 30&deg; = 20 m/s\n'
    'T = 2 v(iy) / g = ( 2 &times; 20 ) / 10 = 4 s', 'B) 4 s')
sol(32, 'maximum height', 'H = v(iy)&sup2; / ( 2 g ) = 20&sup2; / 20 = 400 / 20 = 20 m', 'B) 20 m')
sol(33, 'horizontal range', 'v(ix) = 40 cos 30&deg; = 34.64 m/s\nR = v(ix) &times; T = 34.64 &times; 4 = 138.6 m',
    'R = 138.6 m')
sol(34, 'maximum range', 'R = v&#8320;&sup2; sin 2&theta; / g   is a maximum when sin 2&theta; = 1\n'
    '2&theta; = 90&deg;   &rarr;   &theta; = 45&deg;', 'C) 45&deg;')
sol(35, 'complementary angles', 'sin 2( 90&deg; &minus; &theta; ) = sin ( 180&deg; &minus; 2&theta; ) = sin 2&theta;\n'
    'so the partner of 25&deg; is  90&deg; &minus; 25&deg; = 65&deg;', 'C) 65&deg;')
sol(36, 'complete projectile', '(i)   v(ix) = 50 cos 53&deg; = 30 m/s      v(iy) = 50 sin 53&deg; = 40 m/s\n'
    '(ii)  t(up) = v(iy) / g = 40 / 10 = 4 s\n(iii) T = 2 t(up) = 8 s\n'
    '(iv)  H = v(iy)&sup2; / 2g = 1600 / 20 = 80 m\n(v)   R = v(ix) &times; T = 30 &times; 8 = 240 m',
    '30 , 40 m/s ; 4 s ; 8 s ; 80 m ; 240 m')
sol(37, 'speed at the top', 'at the highest point  v(y) = 0\nv = v(x) = 30 m/s', 'B) 30 m/s')
sol(38, 'velocity after 2 s', 'v(y) = v(iy) &minus; g t = 40 &minus; 10 &times; 2 = 20 m/s      v(x) = 30 m/s\n'
    'v = &radic;( 30&sup2; + 20&sup2; ) = &radic;1300 = 36.06 m/s\n'
    'tan &theta; = 20 / 30   &rarr;   &theta; = 33.7&deg;', '36.06 m/s , 33.7&deg; above the horizontal')
sol(39, 'thrown from a building', 'v(ix) = 20 cos 30&deg; = 17.32 m/s     v(iy) = 20 sin 30&deg; = 10 m/s\n'
    'taking upwards positive, the final displacement is &minus; 45 m :\n'
    '&minus;45 = 10 t &minus; 5 t&sup2;    &rarr;    t&sup2; &minus; 2 t &minus; 9 = 0\n'
    't = 1 + &radic;10 = 4.16 s        ( the negative root is rejected )\n'
    'R = v(ix) &times; t = 17.32 &times; 4.16 = 72.05 m', '(i) 4.16 s   (ii) 72.05 m')
sol(40, 'water jet and a wall', 'v(ix) = 20 cos 40&deg; = 15.32 m/s     v(iy) = 20 sin 40&deg; = 12.86 m/s\n'
    't = x / v(ix) = 8 / 15.32 = 0.522 s\n'
    'h = v(iy) t &minus; &frac12; g t&sup2; = ( 12.86 &times; 0.522 ) &minus; ( 5 &times; 0.522&sup2; )\n'
    'h = 6.71 &minus; 1.36 = 5.35 m', 'h = 5.35 m')
sol(41, 'acceleration at the top', 'the only force acting is the weight, so the acceleration is g\n'
    'at the top  v(y) = 0  but  a = 10 m/s&sup2; downwards', 'C) 10 m/s&sup2; vertically downwards')
sol(42, 'passing over a wall', 'v(ix) = v(iy) = 20 cos 45&deg; = 14.14 m/s\n'
    't = 30 / 14.14 = 2.12 s\n'
    'y = v(iy) t &minus; &frac12; g t&sup2; = 30 &minus; ( 5 &times; 4.5 ) = 30 &minus; 22.5 = 7.5 m\n'
    '7.5 m > 4 m', 'y = 7.5 m , the ball passes over the wall')
sol(43, 'equal components', 'v(i) = &radic;( 20&sup2; + 20&sup2; ) = 20&radic;2 = 28.3 m/s\n'
    'tan &theta; = 20 / 20 = 1   &rarr;   &theta; = 45&deg;', 'B) 28.3 m/s and 45&deg;')
sol(44, 'from T and R', 'v(iy) = g T / 2 = ( 10 &times; 6 ) / 2 = 30 m/s\n'
    'v(ix) = R / T = 300 / 6 = 50 m/s\n'
    'v&#8320; = &radic;( 50&sup2; + 30&sup2; ) = &radic;3400 = 58.3 m/s\n'
    'tan &theta; = 30 / 50 = 0.6   &rarr;   &theta; = 31&deg;', 'v&#8320; = 58.3 m/s , &theta; = 31&deg;')
sol(45, 'ratio of the components', 'tan &theta; = v(iy) / v(ix) = 2 v(ix) / v(ix) = 2\n&theta; = 63.43&deg;', 'C) 63.43&deg;')

a('<h3>Section 4 &mdash; Moment of a force</h3>')
sol(46, 'perpendicular force', 'M = F &times; L = 40 &times; 0.5 = 20 N&middot;m\n'
    'the rod turns clockwise  &rarr;  the sign is negative', 'B) &minus; 20 N&middot;m')
sol(47, 'force from the moment', 'M = F &times; L   &rarr;   F = M / L\nF = 15 / 0.25 = 60 N', 'F = 60 N')
sol(48, 'inclined force', 'M = F L sin &theta; = 50 &times; 2 &times; sin 30&deg;\n'
    '  = 50 &times; 2 &times; 0.5 = 50 N&middot;m      ( anticlockwise )', '+ 50 N&middot;m')
sol(49, 'obtuse angle', 'sin 120&deg; = sin ( 180&deg; &minus; 120&deg; ) = sin 60&deg; = 0.866\n'
    'M = 60 &times; 1.5 &times; 0.866 = 77.9 N&middot;m', '+ 77.9 N&middot;m')
sol(50, 'zero moment', 'M = F &times; d   and here  d = 0\nbecause the line of action passes through the point.',
    'C) the line of action passes through the point')
sol(51, 'two forces on a bar', '25 N downwards, 2 m to the LEFT    &rarr; anticlockwise &rarr; + 25 &times; 2   = + 50 N&middot;m\n'
    '40 N upwards, 1.5 m to the RIGHT  &rarr; anticlockwise &rarr; + 40 &times; 1.5 = + 60 N&middot;m\n'
    'M(net) = + 50 + 60 = + 110 N&middot;m', '+ 110 N&middot;m (anticlockwise)')
sol(52, 'three forces on a bar', '30 N up, 2 m LEFT      &rarr; clockwise      &rarr; &minus; 30 &times; 2 = &minus; 60 N&middot;m\n'
    '50 N down, 1 m RIGHT   &rarr; clockwise      &rarr; &minus; 50 &times; 1 = &minus; 50 N&middot;m\n'
    '20 N up, 3 m RIGHT     &rarr; anticlockwise  &rarr; + 20 &times; 3 = + 60 N&middot;m\n'
    'M(net) = &minus;60 &minus; 50 + 60 = &minus; 50 N&middot;m', '&minus; 50 N&middot;m (clockwise)')
sol(53, 'tangential force', 'the tangent is perpendicular to the radius  &rarr;  &theta; = 90&deg;\n'
    'M = F &times; r = 45 &times; 0.2 = 9 N&middot;m', '9 N&middot;m')
sol(54, 'push on a door', 'M = F L sin &theta; = 30 &times; 0.8 &times; sin 40&deg;\n'
    '  = 30 &times; 0.8 &times; 0.643 = 15.4 N&middot;m', '15.4 N&middot;m')
sol(55, 'the unit', 'M = force &times; distance = newton &times; metre = N&middot;m', 'B) N&middot;m')
sol(56, 'finding the angle', 'M = F L sin &theta;   &rarr;   sin &theta; = M / ( F L )\n'
    'sin &theta; = 24 / ( 40 &times; 1.2 ) = 24 / 48 = 0.5\n&theta; = 30&deg;', '&theta; = 30&deg;')
sol(57, 'maximum moment', 'M = F L sin &theta;  is a maximum when sin &theta; = 1\n&theta; = 90&deg;', 'D) 90&deg;')
sol(58, 'comparing two positions', '(a) M = F L = 60 &times; 1 = 60 N&middot;m\n'
    '(b) M = F L sin 45&deg; = 60 &times; 1 &times; 0.707 = 42.4 N&middot;m\n'
    'ratio = 60 / 42.4 = 1.41 : 1', 'M(a) = 60 , M(b) = 42.4 N&middot;m , 1.41 : 1')
sol(59, 'resultant moment', '20 N up, 2.5 m LEFT    &rarr; clockwise &rarr; &minus; 20 &times; 2.5 = &minus; 50 N&middot;m\n'
    '35 N down, 2 m RIGHT   &rarr; clockwise &rarr; &minus; 35 &times; 2   = &minus; 70 N&middot;m\n'
    'M(net) = &minus;50 &minus; 70 = &minus; 120 N&middot;m', '&minus; 120 N&middot;m (clockwise)')
sol(60, 'smallest moment', 'M = F L sin &theta;  , and sin 20&deg; = 0.34 is the smallest of the four values\n'
    '( sin 45&deg; = 0.71 , sin 60&deg; = 0.87 , sin 90&deg; = 1 )', 'A) 20&deg;')

a('<div class="foot"><span>Physics Question Bank &mdash; 60 Questions &middot; Mr. Gemy</span>'
  '<span>Relative velocity &middot; Projectiles &middot; Moment of a force</span></div>')
a('</body></html>')

open('bank.html', 'w', encoding='utf-8').write(''.join(H))
print('bank.html written with', QN[0], 'questions')

# -*- coding: utf-8 -*-
"""Quiz - Moment of a Force (Torque) : 5 questions, questions only (no answers). Grade 11, English."""
import figs_moment as F
from css import CSS

H = []
a = H.append
a('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Quiz - Moment of a Force</title>'
  '<style>' + CSS + """
.head2 { background:linear-gradient(100deg,#0f2f5b 0%,#1d4ed8 60%,#2563eb 100%); }
.line { display:flex; gap:14px; margin:8px 0 4px; font-size:10.5pt; }
.line span { flex:1; border-bottom:1.6px dotted #64748b; padding-bottom:2px; }
.data { background:#fffbeb; border:1.6px solid #f59e0b; border-radius:9px; padding:7px 12px; font-size:10.3pt; margin:8px 0; }
.q { background:#fff; }
.qtext { font-size:11pt; }
.ch div { padding:5px 10px; }
.hard { float:right; font-size:8.5pt; font-weight:700; color:#92400e; background:#fef3c7; border:1.3px solid #f59e0b;
        border-radius:12px; padding:1px 9px; }
.box2 { display:inline-block; width:34px; height:26px; border:1.8px solid #0f2f5b; border-radius:6px; float:right;
        margin-left:8px; background:#fff; }
</style></head><body>""")

a('<div class="head head2"><div><h1>Quiz &mdash; Moment of a Force (Torque)</h1>'
  '<div class="sub">Physics &middot; Grade 11 &middot; Multiple choice &middot; 5 questions</div></div>'
  '<div class="badge">Time: 15 min<br>Total: 5 marks</div></div>')

a('<div class="line"><span>Name: </span><span>Class: </span><span>Date: </span></div>')
a('<div class="data"><b>Data:</b> &nbsp; sin 30&deg; = 0.5 &nbsp;|&nbsp; sin 60&deg; = 0.866 &nbsp;|&nbsp; '
  'anticlockwise moment ( + ) , clockwise moment ( &minus; ).<br>'
  '<b>Instructions:</b> choose the <b>one</b> correct answer for each question and write its letter in the box.</div>')

QN = [0]


def q(text, fig, choices, hard=False):
    QN[0] += 1
    a('<div class="q"><span class="box2"></span>' + ('<span class="hard">&#9733; challenging</span>' if hard else '') +
      '<div class="qtext"><span class="n">Q' + str(QN[0]) + '</span>' + text + '</div>')
    if fig:
        a(fig)
    one = any(len(c) > 38 for c in choices)
    a('<div class="ch"' + (' style="grid-template-columns:1fr"' if one else '') + '>')
    for L, c in zip('ABCD', choices):
        a('<div><b>' + L + ')</b> ' + c + '</div>')
    a('</div></div>')


q('A force of <b>40 N</b> is applied <b>perpendicular</b> to the handle of a spanner at a distance of '
  '<b>25 cm</b> from the centre of the nut (Fig. 1). The magnitude of the moment of the force about the nut is:',
  F.spanner('Fig. 1', 'L = 25 cm', 'F = 40 N', 390),
  ['1000 N&middot;m', '10 N&middot;m', '160 N&middot;m', '1.6 N&middot;m'])

q('A force of <b>60 N</b> acts at the end A of a rod OA of length <b>1.5 m</b>, making an angle of <b>30&deg;</b> '
  'with the rod (Fig. 2). The magnitude of its moment about O is:',
  F.rod_fig('Fig. 2', 'L = 1.5 m', 'F = 60 N', 30, maxw=380),
  ['90 N&middot;m', '45 N&middot;m', '77.9 N&middot;m', '30 N&middot;m'])

q('A door is 0.8 m wide. Which of the following forces produces the <b>largest</b> moment about the hinge?',
  None,
  ['50 N perpendicular to the door, at its outer edge (0.8 m from the hinge)',
   '80 N perpendicular to the door, at its middle (0.4 m from the hinge)',
   '60 N at 30&deg; to the door, at its outer edge',
   '100 N along the plane of the door, at its outer edge'])

q('Three forces act on the light bar shown in Fig. 3, which can turn about O. The <b>resultant moment</b> about O '
  'is:',
  F.bar_forces('Fig. 3', [(-2, '30 N', 'up'), (1, '50 N', 'down'), (3, '40 N', 'up')], 460),
  ['+ 10 N&middot;m (anticlockwise)', '&#8722; 10 N&middot;m (clockwise)', '+ 230 N&middot;m (anticlockwise)',
   '&#8722; 110 N&middot;m (clockwise)'], hard=True)

q('A force F acting at the end A of a rod OA of length <b>2 m</b>, at an angle &theta; to the rod, produces a moment '
  'of <b>40 N&middot;m</b> about O (Fig. 4). When the <b>same force</b> acts <b>perpendicular</b> to the rod at its '
  '<b>midpoint</b>, it produces a moment of <b>50 N&middot;m</b>. The angle &theta; is approximately:',
  F.rod_fig('Fig. 4', 'L = 2 m', 'F', 24, anglab='&#952; = ?', maxw=380),
  ['23.6&deg;', '53&deg;', '30&deg;', '66.4&deg;'], hard=True)

a('</body></html>')

open('quiz_moment.html', 'w', encoding='utf-8').write(''.join(H))
print('quiz_moment.html written :', QN[0], 'questions')

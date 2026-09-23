# -*- coding: utf-8 -*-
"""Arabic quiz (A4) : Ohm's law for a closed circuit and cells connected in series."""
import os
import sys
# the shared drawing library and page style live with the grade-11 handouts
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..', 'grade-11', 'handouts', 'src'))
import figs_ohm as F
from css_apple import CSS
from docbase import WM64


def eq(s):
    """a formula or a value, kept left-to-right inside the Arabic text."""
    return '<span class="eq" dir="ltr">' + s + '</span>'


VB = 'V<sub>B</sub>'

RTL = """
@page { size:A4; margin:12mm 12mm 13mm 12mm; }
* { letter-spacing:0 !important; }
html { font-size:11pt; }
body { font-family:"Noto Sans Arabic","Liberation Sans",sans-serif; line-height:1.75;
       background-image:url("data:image/svg+xml;base64,%s"); background-repeat:repeat; }
h1, .sec .tt, .sol .st, h3.grp { font-family:"Noto Kufi Arabic","Noto Sans Arabic",sans-serif; }
.eq { font-family:"Liberation Sans",Arial,sans-serif; unicode-bidi:isolate; white-space:nowrap; }
sub { font-size:70%%; }
.hero { padding:18px 24px 16px; }
.hero h1 { font-size:19pt; line-height:1.45; }
.hero .sub { max-width:86%%; line-height:1.6; font-size:10pt; }
.hero .chip { text-transform:none; }
.hero .sig { right:auto; left:24px; text-align:left; }
.hero .sig b, .hero .sig i { font-family:"Liberation Sans",Arial,sans-serif; }
.hero .sig i { letter-spacing:.1em !important; }
.hero:after { right:auto; left:-70px; }
.info { display:flex; gap:10px; margin:0 0 12px; }
.info div { flex:1; border:1px solid #E1E8F0; background:#fff; border-radius:12px; padding:7px 14px;
        font-size:10.4pt; color:#334155; }
.info div b { color:#17548C; }
.info div:first-child { flex:2.2; }
.note { border-right:3px solid #0EA5E9; border-left:none; background:#F5FBFF;
        border-radius:10px 0 0 10px; padding:7px 14px; margin:0 0 10px; font-size:10pt; color:#0C4A6E; }
.card { padding:10px 15px 11px; margin:9px 0; }
.qtx { font-size:11.2pt; }
.qno { font-family:"Liberation Sans",Arial,sans-serif; }
.tag { margin-left:0; margin-right:6px; text-transform:none; font-size:8.6pt; }
.ch div { font-size:11pt; padding:5px 12px; }
.ch i { margin-right:0; margin-left:8px; width:20px; height:20px; line-height:20px; font-size:9.6pt;
        font-family:"Noto Kufi Arabic",sans-serif; }
svg.svgfig { direction:ltr; max-width:430px !important; }
.ch.row { grid-template-columns:repeat(4,1fr); }
.side { display:grid; grid-template-columns:1fr 340px; gap:14px; align-items:center; }
.card.compact svg.svgfig { max-width:360px !important; }
.side .qh { display:flex; gap:9px; align-items:flex-start; }
.side svg.svgfig { max-width:340px !important; }
.side figure.fig { margin:4px 0 0; }
.side .ch { grid-template-columns:1fr 1fr; }
figure.fig { margin:6px auto 0; }
figcaption { margin-top:2px; }
figcaption { text-transform:none; font-size:9pt; }
.sec .rule { background:linear-gradient(270deg,#DCE7F3,rgba(220,231,243,0)); }
.sec .tt small { text-transform:none; font-size:9pt; }
.sol { border-left:1px solid #E6ECF3; border-right:3.5px solid #059669; border-radius:14px 0 0 14px;
       padding:9px 16px 10px; margin:8px 0; }
.sol .st { font-size:10.6pt; color:#0B1220; font-weight:700; }
.steps { margin:6px 0 2px; display:grid; grid-template-columns:auto 1fr; gap:1px 14px; line-height:1.5;
         align-items:baseline; }
.steps .l { color:#5B6B7F; font-size:9.8pt; white-space:nowrap; }
.steps .e { direction:ltr; text-align:right; font-family:"Liberation Sans",Arial,sans-serif;
            font-size:10.6pt; color:#16283F; }
.steps .e b { color:#047857; }
.sol .why { font-size:9.8pt; line-height:1.6; margin-top:6px; background:#FFFBEB; border:1px solid #FDE68A; color:#78350F;
            border-radius:10px; padding:6px 12px; }
.sol .res { font-size:10.6pt; }
.foot { font-family:"Liberation Sans",Arial,sans-serif; }
""" % WM64

h = ['<!DOCTYPE html><html lang="ar" dir="rtl"><head><meta charset="utf-8">'
     '<title>كويز قانون أوم للدائرة المغلقة</title><style>', CSS, RTL, '</style></head><body>']
a = h.append

a('<div class="hero"><span class="chip">الصف الثالث الثانوي &middot; فيزياء &middot; الكهربية التيارية</span>'
  '<h1>كويز: قانون أوم للدائرة المغلقة<br>وتوصيل الأعمدة على التوالي</h1>'
  '<div class="sub">خمسة أسئلة اختيار من متعدد بمستوى مرتفع، كل سؤال فيه فخ شائع. '
  'اقرأ الشكل كويس قبل ما تختار.</div>'
  '<div class="meta"><span>5 أسئلة</span><span>الزمن: 25 دقيقة</span><span>الدرجة: 5</span></div>'
  '<div class="sig"><b>Mr. Gemy</b><i>PHYSICS</i></div></div>')
a('<div class="info"><div><b>الاسم:</b> ..........................................</div>'
  '<div><b>الفصل:</b> ............</div><div><b>الدرجة:</b> ........ / 5</div></div>')
a('<div class="note">اعتبر أسلاك التوصيل مهملة المقاومة، والأميتر مثاليًا (مقاومته مهملة)، '
  'والفولتميتر مثاليًا (مقاومته كبيرة جدًا فلا يسحب تيارًا).</div>')

n = [0]


def q(text, fig, ch, side=False, cls=''):
    n[0] += 1
    head = ('<div class="qh"><div class="qno">' + str(n[0]) + '</div>'
            '<div class="qtx">' + text + '</div><span class="tag">اختر</span></div>')
    opts = ('<div class="ch' + ('' if side else ' row') + '">' +
            ''.join('<div><i>' + le + '</i>' + c + '</div>' for le, c in zip(('أ', 'ب', 'ج', 'د'), ch)) +
            '</div>')
    if side:
        a('<div class="card"><div class="side"><div>' + head + opts + '</div>' + fig + '</div></div>')
    else:
        a('<div class="card ' + cls + '">' + head + fig + opts + '</div>')


q('في الدائرة الموضحة، عندما كان الأميتر يقرأ ' + eq('2 A') + ' كانت قراءة الفولتميتر ' + eq('10 V') +
  '، وعند تحريك ذراع الريوستات أصبح الأميتر يقرأ ' + eq('4 A') + ' والفولتميتر ' + eq('8 V') +
  '. <b>أقصى شدة تيار</b> يمكن أن يعطيها العمود (عند توصيل قطبيه بسلك مهمل المقاومة) تساوي:',
  F.terminal_voltage('شكل (1)'),
  [eq('5 A'), eq('6 A'), eq('12 A'), eq('24 A')], side=True)

q('عمود كهربي وُصِّل قطباه بمقاومة ' + eq('2 Ω') + ' فمر تيار شدته ' + eq('3 A') +
  '، وعند استبدال المقاومة بأخرى قيمتها ' + eq('5 Ω') + ' أصبحت شدة التيار ' + eq('1.5 A') +
  '. <b>القوة الدافعة الكهربية للعمود ومقاومته الداخلية</b> على الترتيب:',
  F.two_resistors('شكل (2)'),
  [eq('9 V') + ' ، ' + eq('1 Ω'), eq('7.5 V') + ' ، ' + eq('0.5 Ω'),
   eq('12 V') + ' ، ' + eq('2 Ω'), eq('6 V') + ' ، صفر'])

q('بطارية مكونة من 6 أعمدة متماثلة متصلة على التوالي، القوة الدافعة الكهربية لكل عمود ' + eq('1.5 V') +
  ' ومقاومته الداخلية ' + eq('0.5 Ω') + '، وُصِّلت بمقاومة خارجية ' + eq('6 Ω') +
  '. إذا وُصِّل العمود الرابع <b>معكوسًا</b> بطريق الخطأ كما بالشكل، فإن النسبة بين شدة التيار '
  '<b>بعد</b> الخطأ إلى شدته <b>قبل</b> الخطأ تساوي:',
  F.six_cells('شكل (3)'),
  [eq('5/6'), eq('2/3'), eq('3/4'), eq('1/2')])

q('في الدائرة الموضحة بطاريتان متصلتان على التوالي بحيث تكونان <b>متعاكستين</b> '
  '(القطب الموجب لإحداهما متصل بالقطب الموجب للأخرى). <b>قراءة الفولتميتر</b> المتصل بين قطبي '
  'البطارية (2) تساوي:',
  F.opposing_batteries('شكل (4)'),
  [eq('6 V'), eq('5.5 V'), eq('11 V'), eq('6.5 V')], side=True)

q('في الدائرة الموضحة ثلاث بطاريات متصلة على التوالي، إحداها معكوسة. <b>شدة التيار المار في '
  'المقاومة ' + eq('6 Ω') + '</b> تساوي:',
  F.mixed_network('شكل (5)'),
  [eq('4/3 A'), eq('1 A'), eq('2/3 A'), eq('10/9 A')], cls='compact')

# ------------------------------------------------------------------ the model answer
a('<div class="pb"></div>')
a('<div class="sec"><div class="no">&#10003;</div><div class="tt"><small>نموذج الإجابة</small>'
  'الحل بالخطوات</div><div class="rule"></div></div>')


def sol(k, title, steps, res, why):
    a('<div class="sol"><div class="sh"><div class="sn">' + str(k) + '</div><div class="st">' + title +
      '</div></div><div class="steps">')
    for lab, e in steps:
        a('<div class="l">' + lab + '</div><div class="e">' + e + '</div>')
    a('</div><div class="why">' + why + '</div><div class="res">' + res + '</div></div>')


sol(1, 'أقصى تيار يعطيه العمود', [
    ('فرق الجهد بين قطبي العمود', 'V = ' + VB + ' − I r'),
    ('القراءة الأولى', '10 = ' + VB + ' − 2 r'),
    ('القراءة الثانية', '8 = ' + VB + ' − 4 r'),
    ('بطرح المعادلتين', '2 = 2 r &nbsp;→&nbsp; <b>r = 1 Ω</b>'),
    ('بالتعويض', VB + ' = 10 + 2 × 1 = <b>12 V</b>'),
    ('أقصى تيار عندما R = 0', 'I<sub>max</sub> = ' + VB + ' / r = 12 / 1 = <b>12 A</b>'),
], 'الإجابة: (ج) ' + eq('12 A'),
    '<b>الفخ:</b> قسمة قراءة الفولتميتر على قراءة الأميتر (' + eq('10 / 2 = 5') +
    ') تعطي المقاومة الخارجية وقتها، ولا علاقة لها بأقصى تيار. أقصى تيار يحدث لما المقاومة الخارجية '
    'تنعدم، فلا يحدد التيار غير المقاومة الداخلية ' + eq('r') + '.')

sol(2, 'القوة الدافعة والمقاومة الداخلية من قراءتين', [
    ('قانون أوم للدائرة المغلقة', VB + ' = I ( R + r )'),
    ('الحالة (a)', VB + ' = 3 ( 2 + r ) = 6 + 3 r'),
    ('الحالة (b)', VB + ' = 1.5 ( 5 + r ) = 7.5 + 1.5 r'),
    ('بمساواة المعادلتين', '6 + 3 r = 7.5 + 1.5 r &nbsp;→&nbsp; 1.5 r = 1.5 &nbsp;→&nbsp; <b>r = 1 Ω</b>'),
    ('بالتعويض', VB + ' = 6 + 3 × 1 = <b>9 V</b>'),
    ('تحقق', 'I = 9 / ( 5 + 1 ) = 1.5 A &nbsp;✓'),
], 'الإجابة: (أ) ' + eq('9 V') + ' ، ' + eq('1 Ω'),
    '<b>ليه السؤال صعب؟</b> كل اختيار من الثلاثة الخاطئة يحقق الحالة الأولى لوحدها '
    '(' + eq('6/2 = 3') + '، ' + eq('7.5/2.5 = 3') + '، ' + eq('12/4 = 3') + ') '
    'لكنه يفشل في الحالة الثانية. اللي يجرب قراءة واحدة بس هيقع؛ لازم القراءتين مع بعض.')

sol(3, 'عمود موصل معكوسًا', [
    ('قبل الخطأ', VB + ' = 6 × 1.5 = 9 V &nbsp;&nbsp;,&nbsp;&nbsp; r = 6 × 0.5 = 3 Ω'),
    ('', 'I<sub>1</sub> = 9 / ( 6 + 3 ) = <b>1 A</b>'),
    ('بعد الخطأ', VB + '′ = 5 × 1.5 − 1.5 = 6 V'),
    ('المقاومة الداخلية لا تتغير', 'r = 3 Ω'),
    ('', 'I<sub>2</sub> = 6 / ( 6 + 3 ) = <b>2/3 A</b>'),
    ('النسبة', 'I<sub>2</sub> / I<sub>1</sub> = <b>2/3</b>'),
], 'الإجابة: (ب) ' + eq('2/3'),
    '<b>الفخ (' + eq('5/6') + '):</b> اللي يحسب القوة الدافعة ' + eq('7.5 V') +
    ' كأن العمود المعكوس اتشال بس. الحقيقة إن العمود المعكوس بيطرح قوته الدافعة، فبيلغي معاه عمود '
    'سليم: القوة الدافعة بتقل بمقدار ' + eq('2 × 1.5 = 3 V') + '. أما المقاومة الداخلية فمالهاش اتجاه، '
    'فبتتجمع زي ما هي.')

sol(4, 'بطاريتان متعاكستان: قراءة الفولتميتر على البطارية (2)', [
    ('القوة الدافعة المحصلة', VB + ' = 12 − 6 = 6 V'),
    ('المقاومة الكلية', 'R + r<sub>1</sub> + r<sub>2</sub> = 4.5 + 1 + 0.5 = 6 Ω'),
    ('شدة التيار', 'I = 6 / 6 = <b>1 A</b>'),
    ('البطارية (2) تُشحن', 'V<sub>2</sub> = ' + VB + '<sub>2</sub> + I r<sub>2</sub>'),
    ('', 'V<sub>2</sub> = 6 + 1 × 0.5 = <b>6.5 V</b>'),
    ('تحقق من الدائرة', 'V<sub>1</sub> = 12 − 1 × 1 = 11 V = I R + V<sub>2</sub> = 4.5 + 6.5 &nbsp;✓'),
], 'الإجابة: (د) ' + eq('6.5 V'),
    '<b>الفكرة:</b> البطارية الأكبر (1) تفرغ، والتيار يدخل البطارية (2) من قطبها الموجب فهي '
    '<b>تُشحن</b>. عند التفريغ ' + eq('V = V<sub>B</sub> − I r') + '، وعند الشحن '
    + eq('V = V<sub>B</sub> + I r') + '. الاختيار (ب) ' + eq('5.5 V') + ' لمن طبّق قانون التفريغ، '
    'والاختيار (ج) ' + eq('11 V') + ' هو فرق جهد البطارية (1) وليس (2).')

sol(5, 'شبكة فيها بطارية معكوسة ومقاومتان على التوازي', [
    ('القوة الدافعة المحصلة', VB + ' = 6 − 4 + 10 = 12 V'),
    ('المقاومة الداخلية الكلية', 'r = 0.5 + 0.5 + 1 = 2 Ω'),
    ('التوازي ' + eq('6 Ω ∥ 3 Ω'), 'R<sub>p</sub> = ( 6 × 3 ) / ( 6 + 3 ) = 2 Ω'),
    ('المقاومة الخارجية', 'R = 2 + 2 = 4 Ω'),
    ('التيار الكلي', 'I = ' + VB + ' / ( R + r ) = 12 / ( 4 + 2 ) = <b>2 A</b>'),
    ('فرق الجهد على التوازي', 'V<sub>p</sub> = I R<sub>p</sub> = 2 × 2 = 4 V'),
    ('تيار المقاومة 6 Ω', 'I<sub>6</sub> = 4 / 6 = <b>2/3 A ≈ 0.67 A</b>'),
], 'الإجابة: (ج) ' + eq('2/3 A'),
    '<b>كل اختيار خاطئ وراه غلطة معروفة:</b> جمع القوى الثلاث ' + eq('20 V') + ' بيدي '
    + eq('10/9 A') + '، وإهمال المقاومات الداخلية بيدي ' + eq('1 A') + '، وحساب تيار المقاومة '
    + eq('3 Ω') + ' بدل ' + eq('6 Ω') + ' بيدي ' + eq('4/3 A') + '.')

a('<div class="foot"><span>Mr. Gemy &middot; Physics</span>'
  '<span dir="ltr">charging : V = V<sub>B</sub> + Ir &nbsp;&middot;&nbsp; discharging : V = V<sub>B</sub> − Ir</span></div>')
a('</body></html>')
open('quiz_ohm.html', 'w', encoding='utf-8').write(''.join(h))
print('quiz_ohm.html written -', n[0], 'questions')

# -*- coding: utf-8 -*-
"""Z BANK - Mechanics Question Bank : Chapter 2, Lesson 1 (Moment of a Force)."""
import zb_frame as FR
import zb_page as PG
import zb_content as C

# spread the correct letters evenly : for these parts the options (c) and (d) change places
for qi, pi in ((2, 0), (8, 0), (9, 1), (11, 0), (17, 1)):
    p = C.Q[qi]['parts'][pi]
    assert p['ok'] == 2
    p['ch'][2], p['ch'][3] = p['ch'][3], p['ch'][2]
    p['ok'] = 3

LET = 'abcd'
blocks = []
blocks.append('<div class="lesson"><div class="lk">Chapter 2 &middot; Lesson 1</div>'
              '<div class="lt">Moment of a Force</div>'
              '<div class="ls">The turning effect of a force about a point &middot; perpendicular and inclined forces '
              '&middot; the moment arm &middot; the net moment<br>'
              'Sign convention: <b>anticlockwise (+)</b> &nbsp;&middot;&nbsp; <b>clockwise (&minus;)</b></div></div>')
for n, q in enumerate(C.Q, 1):
    blocks += PG.question(n, q['stem'], q['parts'], q['fig'], q['figpos'])

# ---------------------------------------------------------------- the model answers
blocks.append('<div class="lesson newpage"><div class="lk">Chapter 2 &middot; Lesson 1</div>'
              '<div class="lt">Model Answers</div>'
              '<div class="ls">Every question solved step by step &nbsp;&middot;&nbsp; '
              '<b>anticlockwise (+)</b> &nbsp;&middot;&nbsp; <b>clockwise (&minus;)</b></div></div>')
for n, q in enumerate(C.Q, 1):
    rows = []
    for k, p in enumerate(q['parts']):
        if p.get('ch'):
            res = '%s) %s' % (LET[p['ok']], p['ch'][p['ok']])
        else:
            res = p['res']
        rows.append('<div class="ap"><span class="rn">%s</span><div class="st">%s</div>'
                    '<div class="res">%s</div></div>' % (PG.ROMAN[k], '<br>'.join(p['steps']), res))
    blocks.append('<div class="ans"><div class="abox">' + FR.bubble(n) + ''.join(rows) + '</div></div>')

html = PG.document(blocks, start=1, title='Z BANK - Chapter 2 Lesson 1 - Moment of a Force')
html = html.replace('</style>', FR.css_more() + '</style>', 1)
open('zbank_ch2_l1.html', 'w', encoding='utf-8').write(html)
print('written :', len(C.Q), 'questions,', len(blocks), 'blocks')

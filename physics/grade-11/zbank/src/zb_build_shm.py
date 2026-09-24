# -*- coding: utf-8 -*-
"""Z BANK - Chapter 2, Lesson 1 : Simple Harmonic Motion."""
import zb_frame as FR
import zb_page as PG
import zb_content_shm as C

# spread the correct letters : for these parts options (b) and (d) change places
for qi, pi in ((0, 0), (6, 0), (9, 0), (20, 0), (26, 0), (37, 0)):
    p = C.Q[qi]['parts'][pi]
    assert p['ok'] == 1
    p['ch'][1], p['ch'][3] = p['ch'][3], p['ch'][1]
    p['ok'] = 3

LET = 'abcd'
blocks = ['<div class="lesson"><div class="lk">Chapter 2 &middot; Lesson 1</div>'
          '<div class="lt">Simple Harmonic Motion</div>'
          '<div class="ls">The restoring force &middot; the periodic time and the frequency &middot; the mass&ndash;spring '
          'oscillator &middot; x = A sin &omega;t &middot; energy in SHM<br><b>Take &pi; = 3.14</b></div></div>']
for n, q in enumerate(C.Q, 1):
    blocks += PG.question(n, q['stem'], q['parts'], q['fig'], q['figpos'])

blocks.append('<div class="lesson newpage"><div class="lk">Chapter 2 &middot; Lesson 1</div>'
              '<div class="lt">Model Answers</div>'
              '<div class="ls">Every question solved step by step</div></div>')
for n, q in enumerate(C.Q, 1):
    rows = []
    for k, p in enumerate(q['parts']):
        res = '%s) %s' % (LET[p['ok']], p['ch'][p['ok']]) if p.get('ch') else p['res']
        rn = '<span class="b">%s</span><span class="f">%s</span>' % (PG.ROMAN[k], PG.ROMAN[k])
        rows.append('<div class="ap"><span class="rn">%s</span><div class="st">%s</div>'
                    '<div class="res">%s</div></div>' % (rn, PG.dg('<br>'.join(p['steps'])), PG.dg(res)))
    blocks.append('<div class="ans"><div class="abox">' + FR.bubble(n) + ''.join(rows) + '</div></div>')

open('zbank_shm.html', 'w', encoding='utf-8').write(
    PG.document(blocks, start=1, title='Z BANK - Chapter 2 Lesson 1 - Simple Harmonic Motion'))
print('written :', len(C.Q), 'questions,', len(blocks), 'blocks')

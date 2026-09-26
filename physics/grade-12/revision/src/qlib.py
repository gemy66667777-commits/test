# -*- coding: utf-8 -*-
"""Question records shared by the four sections."""

LET = 'ABCD'


class Section:
    def __init__(self, key, title, sub):
        self.key, self.title, self.sub = key, title, sub
        self.q = []

    def mcq(self, t, ch, ok, sol, fig=None, tag='MCQ', title='', side=False, fa=None):
        """ok : 'A' ... 'D' ; fa : a short text answer when the choices are pictures."""
        self.q.append(dict(t=t, ch=ch, ok=LET.index(ok), sol=sol, fig=fig, tag=tag, title=title, side=side, fa=fa))

    def prob(self, t, fa, sol, fig=None, tag='Problem', title='', side=False):
        self.q.append(dict(t=t, ch=None, fa=fa, sol=sol, fig=fig, tag=tag, title=title, side=side))


def final(q):
    if q['ch']:
        return '%s) %s' % (LET[q['ok']], q.get('fa') or q['ch'][q['ok']])
    return q['fa']

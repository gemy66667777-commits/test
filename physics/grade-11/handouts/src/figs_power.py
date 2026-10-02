# -*- coding: utf-8 -*-
"""Figures for the Power and Efficiency handout (Grade 11, lesson 1-6) - English only."""
from figlib import Fig, AR, BL, GR, PU, OR, DK, GY, NV


def energy_flow(cap, inp='input 100 J', use='useful output', waste='wasted (mostly heat)', ratio=0.7):
    """a Sankey-style arrow : the input splits into the useful output and the wasted energy."""
    f = Fig(520, 250, cap, 470)
    H = 120.0
    hu = H * ratio
    hw = H - hu
    x0, x1, y0 = 30.0, 230.0, 40.0
    f.raw('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f z" fill="#93c5fd" stroke="#1d4ed8" stroke-width="2"/>'
          % (x0, y0, x1, y0, x1, y0 + H, x0, y0 + H))
    f.txt((x0 + x1) / 2, y0 + H / 2 + 5, inp, '#1e3a8a', 14)
    f.raw('<rect x="230" y="40" width="200" height="%.1f" fill="#86efac" stroke="#15803d" stroke-width="2"/>' % hu)
    f.raw('<path d="M430,30 L480,%.1f L430,%.1f z" fill="#86efac" stroke="#15803d" stroke-width="2"/>'
          % (40 + hu / 2, 50 + hu))
    f.txt(330, 40 + hu / 2 + 5, use, '#14532d', 13.5)
    f.raw('<path d="M230,%.1f L270,%.1f Q300,%.1f 300,%.1f L300,215 L%.1f,215 L%.1f,%.1f Q%.1f,%.1f 230,%.1f z" '
          'fill="#fecaca" stroke="#b91c1c" stroke-width="2"/>'
          % (40 + hu, 40 + hu, 40 + hu, 70 + hu, 300 - hw, 300 - hw, 70 + hu + hw * 0.4, 300 - hw,
             40 + hu + hw, 40 + hu + hw))
    f.txt(315, 205, waste, '#991b1b', 12.5, 'start')
    return f.render()


def wt_graph(cap, tx=6, ty=10, W=1200):
    """work done against time for two machines X and Y (straight lines through the origin)."""
    f = Fig(420, 290, cap, 360)
    x0, y0, gw, gh = 60.0, 240.0, 300.0, 190.0
    tmax, wmax = 12.0, 1500.0
    X = lambda t: x0 + gw * t / tmax
    Y = lambda w: y0 - gh * w / wmax
    for t in range(2, 13, 2):
        f.line(X(t), y0, X(t), y0 - gh, '#e2e8f0', 1)
        f.txt(X(t), y0 + 18, str(t), DK, 12, bold=False)
    for w in range(300, 1501, 300):
        f.line(x0, Y(w), x0 + gw, Y(w), '#e2e8f0', 1)
        f.txt(x0 - 8, Y(w) + 4, str(w), DK, 12, 'end', bold=False)
    f.arrow(x0, y0, x0 + gw + 22, y0, DK, 2.2)
    f.arrow(x0, y0, x0, y0 - gh - 22, DK, 2.2)
    f.txt(x0 + gw + 26, y0 + 5, 't (s)', NV, 13, 'start')
    f.txt(x0 + 6, y0 - gh - 24, 'W (J)', NV, 13, 'start')
    f.txt(x0 - 8, y0 + 16, '0', DK, 12, 'end', bold=False)
    f.line(x0, y0, X(tx), Y(W), AR, 3.2)
    f.line(x0, y0, X(ty), Y(W), BL, 3.2)
    f.txt(X(tx) - 6, Y(W) - 10, 'X', AR, 15)
    f.txt(X(ty) + 10, Y(W) - 6, 'Y', BL, 15, 'start')
    f.guide(x0, Y(W), X(ty), Y(W))
    f.guide(X(tx), Y(W), X(tx), y0)
    f.guide(X(ty), Y(W), X(ty), y0)
    return f.render()


def motor_lift(cap, mlab='m', vlab='v (constant)', hlab=None):
    f = Fig(380, 300, cap, 300)
    f.rect(120, 20, 140, 50, '#cbd5e1', '#334155', 2.2, 6)
    f.txt(190, 52, 'electric motor', '#0f172a', 13)
    f.line(190, 70, 190, 170, '#475569', 3)
    f.rect(140, 170, 100, 66, '#fcd34d', '#b45309', 2.4, 5)
    f.txt(190, 208, mlab, '#7c2d12', 14)
    f.arrow(260, 230, 260, 160, GR, 3)
    f.txt(268, 196, vlab, GR, 12.5, 'start')
    f.arrow(190, 240, 190, 290, AR, 3)
    f.txt(200, 282, 'W = mg', AR, 12.5, 'start')
    f.arrow(170, 166, 170, 90, PU, 2.6)
    f.txt(162, 120, 'T', PU, 14, 'end', it=True)
    if hlab:
        f.dim(100, 236, 100, 90, hlab, PU, dx=-22)
    return f.render()

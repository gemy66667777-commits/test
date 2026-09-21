# -*- coding: utf-8 -*-
CSS = """
@page { size: A4; margin: 11mm 10mm 12mm 10mm; }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; box-sizing: border-box; }
html { font-size: 10.9pt; }
body { margin:0; font-family: "Liberation Sans", Helvetica, Arial, sans-serif; color:#0f172a; line-height:1.45; }
.ar { font-family:"FreeSerif","DejaVu Sans",serif; direction:rtl; unicode-bidi:isolate; font-size:1.02em; }

/* ---------- header ---------- */
.head { background: linear-gradient(100deg,#0f2f5b 0%, #17518f 55%, #1d7ac0 100%);
        color:#fff; border-radius:10px; padding:14px 18px; margin-bottom:12px;
        display:flex; justify-content:space-between; align-items:center; }
.head h1 { margin:0; font-size:22pt; letter-spacing:.3px; }
.head .sub { margin-top:3px; font-size:10pt; opacity:.92; }
.head .badge { background:rgba(255,255,255,.16); border:1.5px solid rgba(255,255,255,.5);
        border-radius:8px; padding:7px 12px; font-size:9.5pt; text-align:center; line-height:1.35; }

/* ---------- headings ---------- */
h2 { font-size:14pt; color:#0f2f5b; margin:16px 0 8px; padding:6px 10px 6px 12px;
     border-left:6px solid #dc2626; background:#eef4fb; border-radius:0 7px 7px 0; }
h2 .num { display:inline-block; background:#0f2f5b; color:#fff; border-radius:50%; width:23px; height:23px;
     line-height:23px; text-align:center; font-size:11pt; margin-right:8px; }
h3 { font-size:11.8pt; color:#17518f; margin:12px 0 5px; }
p  { margin:6px 0; }
ul,ol { margin:6px 0 6px 0; padding-left:20px; }
li { margin:3px 0; }
b.k { color:#dc2626; }
.blue { color:#2563eb; } .green{ color:#16a34a; } .purple{ color:#7c3aed; } .orange{ color:#ea580c; } .red{color:#dc2626;}
i.v { font-style:italic; }

/* ---------- boxes ---------- */
.box { border-radius:9px; padding:9px 13px; margin:9px 0; border:1.6px solid; break-inside:avoid; }
.formula { background:#fffbeb; border-color:#f59e0b; text-align:center; }
.formula .big { font-size:15pt; font-weight:700; color:#92400e; letter-spacing:.4px; }
.formula .small { font-size:9.5pt; color:#a16207; margin-top:3px; }
.note { background:#eff6ff; border-color:#60a5fa; }
.warn { background:#fef2f2; border-color:#f87171; }
.tip  { background:#f0fdf4; border-color:#4ade80; }
.box .t { font-weight:700; display:block; margin-bottom:2px; }
.note .t{ color:#1d4ed8; } .warn .t{ color:#b91c1c; } .tip .t{ color:#15803d; }

/* ---------- figures ---------- */
figure.fig { margin:7px auto; text-align:center; break-inside:avoid; }
svg.svgfig { width:100%; max-width:520px; height:auto; background:#fdfdff;
             border:1.4px solid #dbe4f0; border-radius:9px; padding:4px 2px; }
figcaption { font-size:9pt; color:#475569; font-style:italic; margin-top:3px; }

/* ---------- tables ---------- */
table { border-collapse:collapse; width:100%; margin:9px 0; font-size:10pt; break-inside:avoid; }
th { background:#0f2f5b; color:#fff; padding:6px 8px; text-align:center; font-size:10pt; }
td { border:1px solid #cbd5e1; padding:5px 8px; text-align:center; }
tr:nth-child(even) td { background:#f6f9fd; }

/* ---------- examples ---------- */
.ex { border:1.8px solid #16a34a; border-radius:10px; margin:12px 0; break-inside:avoid; overflow:hidden; }
.ex > .h { background:#16a34a; color:#fff; padding:5px 12px; font-weight:700; font-size:11pt; }
.ex > .b { padding:9px 13px; }
.ex .given { background:#f0fdf4; border-radius:7px; padding:6px 10px; margin:6px 0; font-size:10.3pt; }
.sol { background:#f8fafc; border-left:4px solid #16a34a; padding:7px 11px; margin-top:7px; border-radius:0 7px 7px 0; }
.sol .t { color:#15803d; font-weight:700; }
.calc { font-family:"Liberation Mono","DejaVu Sans Mono",monospace; font-size:10pt; background:#fff;
        border:1px dashed #cbd5e1; border-radius:6px; padding:6px 9px; margin:5px 0; white-space:pre-wrap; line-height:1.5; }
.ans { display:inline-block; background:#dcfce7; border:1.5px solid #16a34a; border-radius:6px;
       padding:3px 10px; font-weight:700; color:#14532d; margin-top:4px; }

/* ---------- questions ---------- */
.q { border:1.5px solid #cbd5e1; border-left:5px solid #2563eb; border-radius:0 9px 9px 0;
     padding:8px 12px; margin:10px 0; break-inside:avoid; background:#fcfdff; }
.q .n { display:inline-block; background:#2563eb; color:#fff; border-radius:5px; padding:1px 8px;
        font-weight:700; font-size:10pt; margin-right:7px; }
.ch { display:grid; grid-template-columns:1fr 1fr; gap:4px 12px; margin-top:7px; }
.ch div { border:1.3px solid #cbd5e1; border-radius:6px; padding:4px 9px; font-size:10.4pt; background:#fff; }
.ch b { color:#2563eb; margin-right:5px; }

.pb { break-before:page; }
.foot { margin-top:14px; border-top:2px solid #0f2f5b; padding-top:5px; font-size:8.6pt; color:#64748b;
        display:flex; justify-content:space-between; }
.key { background:#0f2f5b; color:#fff; border-radius:9px; padding:9px 14px; margin:10px 0; }
.key h3 { color:#fff; margin:0 0 5px; }
.key ul { margin:0; padding-left:18px; }
.key li { margin:3px 0; font-size:10.3pt; }
"""

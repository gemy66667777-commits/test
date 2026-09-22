# -*- coding: utf-8 -*-
CSS = """
@page { size: A4; margin: 12mm 11mm 13mm 11mm; }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; box-sizing: border-box; }
html { font-size: 10.8pt; }
body { margin:0; font-family:"Liberation Sans", Helvetica, Arial, sans-serif; color:#0B1220;
       line-height:1.5; letter-spacing:-0.005em; }

/* ---------------- hero ---------------- */
.hero { position:relative; overflow:hidden; border-radius:18px; padding:22px 26px 20px;
        background:linear-gradient(135deg,#070E1A 0%,#102A46 45%,#17548C 78%,#1E7BC0 100%);
        color:#fff; margin-bottom:14px; }
.hero:after { content:""; position:absolute; right:-70px; top:-90px; width:260px; height:260px;
        border-radius:50%; background:radial-gradient(circle,rgba(255,255,255,.16),rgba(255,255,255,0) 70%); }
.hero .chip { display:inline-block; font-size:8.6pt; letter-spacing:.14em; text-transform:uppercase;
        background:rgba(255,255,255,.14); border:1px solid rgba(255,255,255,.34); border-radius:999px;
        padding:3px 12px; margin-bottom:9px; }
.hero h1 { margin:0; font-size:25pt; font-weight:700; letter-spacing:-0.02em; line-height:1.12; }
.hero .sub { margin-top:6px; font-size:10.4pt; color:#CFE2F5; max-width:78%; }
.hero .meta { margin-top:13px; display:flex; gap:7px; flex-wrap:wrap; }
.hero .meta span { font-size:8.8pt; background:rgba(255,255,255,.12); border:1px solid rgba(255,255,255,.26);
        border-radius:8px; padding:3px 10px; }
.hero .sig { position:absolute; right:24px; bottom:18px; text-align:right; }
.hero .sig b { font-size:13pt; letter-spacing:.01em; }
.hero .sig i { display:block; font-style:normal; font-size:8.4pt; color:#BBD5EE; letter-spacing:.1em;
        text-transform:uppercase; }

/* ---------------- section ---------------- */
.sec { display:flex; align-items:center; gap:11px; margin:20px 0 10px; break-after:avoid; }
.sec .no { flex:none; width:31px; height:31px; border-radius:10px; color:#fff; font-weight:700; font-size:12pt;
        display:flex; align-items:center; justify-content:center;
        background:linear-gradient(140deg,#1E7BC0,#17548C); box-shadow:0 2px 5px rgba(23,84,140,.28); }
.sec .tt { font-size:14pt; font-weight:700; letter-spacing:-0.02em; color:#0B1220; }
.sec .tt small { display:block; font-size:8.6pt; font-weight:600; letter-spacing:.13em; text-transform:uppercase;
        color:#6B8098; margin-bottom:1px; }
.sec .rule { flex:1; height:2px; border-radius:2px;
        background:linear-gradient(90deg,#DCE7F3,rgba(220,231,243,0)); }

/* ---------------- cards ---------------- */
.card { background:#fff; border:1px solid #E6ECF3; border-radius:14px; padding:11px 15px 12px;
        margin:10px 0; break-inside:avoid; box-shadow:0 1px 2px rgba(11,18,32,.05); }
.card > .qh { display:flex; gap:9px; align-items:flex-start; }
.qno { flex:none; min-width:24px; height:24px; padding:0 6px; border-radius:8px; color:#fff; font-weight:700;
       font-size:9.6pt; display:flex; align-items:center; justify-content:center;
       background:linear-gradient(140deg,#2563EB,#1E40AF); }
.qtx { flex:1; font-size:10.6pt; }
.tag { flex:none; font-size:7.8pt; letter-spacing:.09em; text-transform:uppercase; color:#6B8098;
       border:1px solid #E1E8F0; background:#F7FAFD; border-radius:7px; padding:2px 8px; margin-left:6px; }
.part { margin:5px 0 0 0; padding-left:2px; font-size:10.4pt; }
.part b { color:#1E40AF; }

.ch { display:grid; grid-template-columns:1fr 1fr; gap:6px 12px; margin-top:9px; }
.ch div { border:1px solid #E6ECF3; border-radius:10px; padding:5px 11px; font-size:10.2pt; background:#FCFDFF; }
.ch i { font-style:normal; display:inline-block; width:17px; height:17px; border-radius:50%; margin-right:7px;
        background:#EEF4FD; color:#2563EB; font-weight:700; font-size:8.6pt; text-align:center; line-height:17px; }

/* ---------------- figures ---------------- */
figure.fig { margin:9px auto 2px; text-align:center; break-inside:avoid; }
svg.svgfig { width:100%; max-width:460px; height:auto; background:linear-gradient(180deg,#FCFDFF,#F7FAFD);
        border:1px solid #E6ECF3; border-radius:13px; padding:5px 3px; }
figcaption { font-size:8.2pt; color:#7C8FA5; letter-spacing:.07em; text-transform:uppercase; margin-top:4px; }

/* ---------------- callouts ---------------- */
.kit { background:linear-gradient(135deg,#F8FAFF,#EEF4FD); border:1px solid #DCE7F8; border-radius:14px;
       padding:12px 16px; margin:12px 0; break-inside:avoid; }
.kit h4 { margin:0 0 7px; font-size:10.4pt; color:#1E40AF; letter-spacing:-0.01em; }
.kit .grid { display:grid; grid-template-columns:1fr 1fr 1fr; gap:7px; }
.kit .f { background:#fff; border:1px solid #E3EBF6; border-radius:10px; padding:6px 10px; text-align:center;
       font-size:10pt; font-weight:700; color:#0B1220; }
.kit .f small { display:block; font-weight:400; font-size:8.2pt; color:#6B8098; margin-top:2px;
       letter-spacing:.02em; text-transform:none; }
.hint { border-left:3px solid #0EA5E9; background:#F5FBFF; border-radius:0 10px 10px 0; padding:7px 13px;
        margin:9px 0; font-size:9.8pt; color:#0C4A6E; break-inside:avoid; }

/* ---------------- solutions ---------------- */
.sol { background:#fff; border:1px solid #E6ECF3; border-left:3.5px solid #059669; border-radius:0 14px 14px 0;
       padding:9px 15px 11px; margin:9px 0; break-inside:avoid; box-shadow:0 1px 2px rgba(11,18,32,.04); }
.sol .sh { display:flex; align-items:center; gap:9px; }
.sol .sn { flex:none; min-width:24px; height:22px; padding:0 7px; border-radius:7px; color:#fff; font-weight:700;
       font-size:9.4pt; display:flex; align-items:center; justify-content:center;
       background:linear-gradient(140deg,#10B981,#047857); }
.sol .st { font-size:9.6pt; color:#5B6B7F; letter-spacing:.03em; }
.sol pre { font-family:"Liberation Mono","DejaVu Sans Mono",monospace; font-size:9.2pt; line-height:1.55;
       margin:6px 0 0; white-space:pre-wrap; color:#16283F; }
.sol .res { display:inline-block; margin-top:6px; background:#ECFDF5; border:1px solid #A7F3D0; color:#065F46;
       border-radius:9px; padding:3px 11px; font-weight:700; font-size:9.8pt; }
.sol .why { font-size:9.6pt; color:#334155; margin-top:5px; }

h3.grp { font-size:11.4pt; color:#17548C; margin:14px 0 6px; padding-bottom:4px;
        border-bottom:1.5px solid #E6ECF3; letter-spacing:-0.01em; }
.figrow { display:flex; gap:11px; justify-content:center; align-items:flex-end; margin:9px 0 2px; }
.figrow figure.fig { flex:1 1 0; margin:0; }
.figrow svg.svgfig { max-width:100%; }
.pb { break-before:page; }
.foot { margin-top:16px; padding-top:7px; border-top:1px solid #E6ECF3; display:flex;
        justify-content:space-between; font-size:8.2pt; color:#8496AB; letter-spacing:.04em; }
table.vt { border-collapse:collapse; width:100%; margin:8px 0; font-size:9.8pt; }
table.vt th { background:#102A46; color:#fff; padding:6px 8px; font-size:9.4pt; font-weight:600;
        letter-spacing:.04em; }
table.vt th:first-child { border-radius:9px 0 0 0; } table.vt th:last-child { border-radius:0 9px 0 0; }
table.vt td { border:1px solid #E6ECF3; padding:5px 9px; text-align:center; }
table.vt tr:nth-child(even) td { background:#F8FBFE; }
"""

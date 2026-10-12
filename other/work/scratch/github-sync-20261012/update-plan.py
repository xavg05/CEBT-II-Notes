import json
from pathlib import Path
root=Path('other/work/scratch/github-sync-20261012')
base=next(x['content'] for x in json.loads((root/'blobs.json').read_text()) if x['sha']=='d7f774501bcb0330a229d0f2ba440546d539ef9d')
s=base.replace('Scope: **Equilibrium Thermodynamics** and **Advanced Biotechnology**, both completed and reviewed, plus **Reaction Engineering II**, started on 12 October 2026. The other courses\' source folders are retained under `other/sources/`.','Scope: **Equilibrium Thermodynamics** and **Advanced Biotechnology**, both completed and reviewed; **Reaction Engineering II**, started on 12 October 2026; and **Separations II** and **Process Dynamics and Control**, with new source inventories and provisional production units added on 12 October 2026. All original PDFs live under `other/sources/`.')
s=s.replace('`AB-` and `RE-`. Short notes','`AB-`, `RE-`, `SEP-` and `PDC-`. Short notes')
s=s.replace('The optional AB-57 is included. The tables below','The optional AB-57 is included. Separations II and Process Dynamics and Control are planned from the supplied sources; their inventories do not imply notes have been written or reviewed. The tables below')
s=s.replace('**Watch for overlap:** ET-U6 and ET-U11 will overlap with Separations II (distillation), and ET-U5\'s osmotic section with membrane topics. Keep the thermodynamic angle here.','**Watch for overlap:** ET-U6 and ET-U11 provide equilibrium foundations relevant to separation design; the supplied Separations II handouts cover absorption, drying, membranes and adsorption, rather than a dedicated distillation unit. ET-U5\'s osmotic section supports membrane topics. Keep the thermodynamic angle here.')
s=s.replace('**Overlap with Separations II:** filtration, centrifugation, extraction, adsorption and chromatography (AB-U8 to AB-U12) may be repeated there. Write them now from the bioprocess angle, then cross-check when the Separations PDFs arrive.','**Overlap with Separations II:** AB-U8 to AB-U12 provide related bioprocess separations. The supplied Separations II sources include membranes and adsorption; cross-check shared mechanisms while retaining the bioprocess angle of the completed AB notes.')
s=s.replace('Work through the lectures in order: all of Equilibrium Thermodynamics first, then all of Advanced Biotechnology. Within each course, units follow lecture order, and the short notes inside each unit follow page order.','The original ET → AB sequence below is a historical production record; both courses are now complete. Reaction Engineering II is the active writing course. Separations II and Process Dynamics and Control are newly planned, with their internal order listed in sections 5 and 6. This source-upload update does not start their note production or change the active course. Within each course, units follow source order, and the short notes inside each unit follow page order.')
s+='''
---

## 5. Separations II

Added with Xavier's permission on 12 October 2026. The four supplied 2025 filled-note handouts are scanned, image-only PDFs. The inventory is based on their filenames, page counts and visually read opening pages; detailed note splits remain provisional until the whole handout is read. The course introduction emphasises continuous contacting and mass-transfer rates, building on earlier equilibrium-stage separations.

### 5.1 Inventory and source limits

| PDF in `other/sources/Separations II/` | Pages | Confirmed scope |
|---|---|---|
| `2025_Handout_1_Introduction + Absorption_filled notes.pdf` | 33 | Introduction and absorption; course aims include mass-transfer effects and absorption-column design |
| `2025_Handout_2_Drying_filled notes.pdf` | 34 | Drying of solids by thermal vaporisation; types of driers and wet solids |
| `2025_Handout_3_Membrane separations_filled notes.pdf` | 51 | Rate-based separation through selective membranes; feed, retentate and permeate streams; membrane structure and selectivity |
| `2025_Handout_4_Adsorption_filled notes.pdf` | 23 | Selective adsorption on porous solids; physical and chemical adsorption; adsorption-cycle introduction |

These four PDFs cover the four process areas named in the introduction. This does not establish that all course material has been supplied: no separate problem sheets or recordings are included in this inventory. Printed page numbers can differ from the PDF index (the first scanned page of handout 1 is printed page 4). Use PDF indices when recording production progress. Do not assume distillation, centrifugation or extraction units are part of this supplied set.

### 5.2 Provisional units and teaching order

All units below are **planned, not written or reviewed**. `SEP-` is reserved for numbered short notes; final titles, note numbers and page splits will be fixed after visually surveying each complete handout.

| Unit | Topic | Source | Provisional short-note scope |
|---|---|---|---|
| SEP-U1 | Introduction and absorption | Handout 1, 33 PDF pages | Continuous contacting versus equilibrium stages; how mass-transfer rates affect absorption performance; absorption-column design procedure and any graphical construction present in the handout |
| SEP-U2 | Drying of solids | Handout 2, 34 PDF pages | Moisture removal and wet-solid behaviour; selecting drying equipment; drying-performance calculations grounded in the handout |
| SEP-U3 | Membrane separations | Handout 3, 51 PDF pages | Selective-barrier mechanisms and membrane structure; stream definitions; flux and performance calculations using the processes actually covered |
| SEP-U4 | Adsorption | Handout 4, 23 PDF pages | Adsorbent/adsorbate distinction; physical versus chemical adsorption; adsorption cycles; gas- and liquid-system performance calculations |

Before drafting, read every page visually, identify the actual equations, examples and graphs, and replace these broad scopes with supported note splits. Lead each design calculation with its assumptions, give a reason for every graphical construction step, and verify numerical examples in Python. Relate membranes to ET osmosis and adsorption to AB primary isolation and RE adsorption equilibria without duplicating those courses' emphasis. Consult external sources per topic as required by CLAUDE.md.

---

## 6. Process Dynamics and Control

Added with Xavier's permission on 12 October 2026. The supplied Michaelmas 2026 chapter handouts name Sebastian Ahnert as lecturer. Their text layer locates headings and examples, but flattened mathematical notation still requires visual reading before note production.

### 6.1 Inventory and gaps

| PDF in `other/sources/Process Dynamics and Control/` | Pages | Coverage |
|---|---|---|
| `PDC MT26 Ch1 v1.pdf` | 10 | Introduction; regulator/servo objectives; feedback and feedforward; control objectives; distillation and CSTR variable-identification examples; dynamic balances |
| `PDC MT26 Ch2 v1.pdf` | 32 | Dynamics of linear systems: material/energy balances; transfer functions and deviation variables; first-order lags, integrators and dead time; second-order responses; block diagrams; MIMO; poles, zeros and stability; steady-state gain; linearisation |

The chapter 1 outline identifies three later sections that are **not supplied**: section 3, Feedback Controller Design (PID, frequency response, stability and tuning); section 4, Advanced Control Systems (cascade, feedforward, ratio and nonlinear control); and section 5, Process Control Systems Design (multivariable and whole-plant control). Introductory feedback/feedforward discussion in chapter 1 does not replace these missing sections. Do not present chapters 1–2 as a complete course.

### 6.2 Provisional units and teaching order

All units below are **planned, not written or reviewed**. `PDC-` is reserved for numbered short notes. These are initial topic groupings; final short-note counts and numbers will be fixed after a complete visual reading. Page ranges use PDF indices.

| Unit | Topic | Source pages | Provisional short-note scope |
|---|---|---|---|
| PDC-U1 | Control objectives, variables and dynamic modelling | Ch1 p1–10 | Controlled/manipulated/disturbance variables; regulator versus servo control; feedback/feedforward intuition; distillation/CSTR examples; accumulation balances |
| PDC-U2 | Physical balances and first-order dynamics | Ch2 p1–5 | Mixing tank and thermocouple; reacting and variable-volume tanks; pulse balances; heated-liquid and discharging-gas balances |
| PDC-U3 | Transfer functions and elementary responses | Ch2 p5–11 | SISO, zero initial conditions and deviation variables; process gain/time constant; step and impulse responses; integrators; transport dead time |
| PDC-U4 | Second-order dynamics and damping | Ch2 p11–15 | Standard second-order model; poles and damping regimes; step responses; overshoot, decay ratio and oscillation period |
| PDC-U5 | Combining process elements | Ch2 p16–19 | Series blocks, delays and two-tank example; addition/subtraction of input contributions; signal duplication |
| PDC-U6 | Multiple-input multiple-output models | Ch2 p20–23 | Transfer-function matrices; boiler mass/energy balances; reacting CSTR with coupled component balances |
| PDC-U7 | Poles, zeros, stability and steady-state gain | Ch2 p23–27 | Distinct/repeated/complex poles; impulse response and stability; zeros and transient shape; final-value theorem and its validity conditions |
| PDC-U8 | Linearisation around an operating point | Ch2 p27–32 | Taylor expansion and deviation variables; first-/second-order kinetics comparison; nonlinear tank-level example; three-tank mixing process and response |
| PDC-U9 | Feedback controller design | Section 3, missing | Await source; do not fix note scope or page ranges |
| PDC-U10 | Advanced control systems | Section 4, missing | Await source; do not fix note scope or page ranges |
| PDC-U11 | Process control systems design | Section 5, missing | Await source; do not fix note scope or page ranges |

Shared boundary pages introduce the next topic and do not require duplicate notes. Lead with the physical system, derive its ODE, take the Laplace transform, then explain what the poles mean. Distinguish an integrator from a self-regulating lag and dead time from a time constant. Read source equations and plots visually, verify worked-example calculations and response curves in Python, and consult external university/textbook sources per topic. Keep short notes separate until Xavier specifies a merge group; claim writing work and record verification in `other/work/BOARD.md` when production begins.
'''
(root/'PLAN-proposed.md').write_text(s)
assert s[s.index('## 4. Reaction Engineering II'):s.index('\n---\n\n## 5.')].rstrip()==base[base.index('## 4. Reaction Engineering II'):].rstrip()
print('Wrote',root/'PLAN-proposed.md','with RE section preserved verbatim.')

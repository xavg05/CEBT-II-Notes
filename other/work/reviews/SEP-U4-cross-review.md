# SEP-U4 independent cross-review

Reviewer: Codex drying subagent; author: root Codex. Date 12 October 2026.

Result: **PASS — no blocking scientific or coverage findings.** Review covers all nine source-order drafts, all 23 original scanned pages and all seven linked source crops. Draft local labels passed; final subject-wide numbering/publication rendering remain coordinator checks.

## Blind original reading

Before reading U4 transcription or drafts, independently opened original p21 and p23:

- p21 symmetric effective plate count: N=5.54[(tr−tm)/w1/2]^2=5.54[t'r/w1/2]^2; asymmetric empirical count41.71(tr/w0.1)^2/(As+1.25).
- p21 literal printed van Deemter expression H=(A+B)/(u+Cu), one fraction. Its dimensional inconsistency and conflict with the individually read p22 terms establish a printing error.
- p23 literal printed resolution R=(1/4)√2×k/(k+1)×(alpha−1). Printed following prose defines N as efficiency. Derived equal-N Gaussian expression and conventional later-width approximation confirm correction.

These literal readings were sent to root before comparing to author interpretation.

## Coverage and scientific checks

All 23 pages inspected visually in bounded overview batches p1–20/p21–23, then original individual pages for equations/annotations. Nine drafts read in full. No consequential handwritten addition omitted; source wrong curvature terms, bp≫0, liquid reciprocal affinity, S-shaped Freundlich sketch, rate-area basis, area-integral dimension, internal-standard/hold-up conflation, van Deemter and resolution errors all correctly handled.

Independent derivations:

| Draft | Derivation/check |
|---|---|
| U4-01 | Difference of loading/regeneration inventories gives working capacity; regeneration direction qualified as ordinary exothermic gas adsorption. |
| U4-02 | Empty/occupied site rates give finite Langmuir capacity; inverse liquid loading formula and reciprocal plot verified; downward Freundlich curvature for0<m<1. |
| U4-03 | Total rate Kc Ai(C−C*) has mass/time units; closed-batch transfer conservation correct; fixed-fluid LDF exponential appropriately distinguished from finite-batch depletion. |
| U4-04 | Balance plus Langmuir gives stated quadratic; inventory residual independently checked; physical root0<Ce<C0; required-M polishing divergence correct. |
| U4-05 | Integrated inlet–outlet inventory includes fluid storage before neglect; capacity time has time units; LUB/midpoint rules explicitly approximate, not literal MTZ geometry; example integration correct. |
| U4-06 | Partial-pressure Langmuir working-capacity difference correct; equilibrium upper capacity distinguished from finite-time working capacity; regeneration schedule caveat correct. |
| U4-07 | k'=KVs/Vm, mobile fraction1/(1+k') and retention relation correct under local linear equilibrium; calibration/hold-up marker distinction sound. |
| U4-08 | Gaussian half-height/baseline widths rederived; total vs adjusted retention convention separated; van Deemter dimensional/optimum/second-derivative checks pass. |
| U4-09 | Measured resolution, exact equal-N expression and later-width approximation independently derived; 1/alpha factor and sqrtN correct; limiting cases/selectivity tradeoffs correct. |

No invented industrial numerical data are represented as source data. Examples are explicitly illustrative; no fully specified numerical problem existed in the source. Mechanisms and mathematical approximations are separated.

## Independent numerical results

Script other/work/scratch/separations/review-U4/independent.py was written without consulting author code; results saved as results.json beside it. The batch concentration uses bisection of inventory residual, independent of the author's quadratic route.

- Cycle mass16 kg; gas coverages .0099009901/.9090909091; liquid loading .1333333333 kg/kg.
- Uptake time constant50 s; fraction .9502129316.
- Batch Ce .02807764064 kg/m3, qe .07192235936 kg/kg; inventory residual1.39e−17; target mass2.7 kg.
- Breakthrough equivalent capture time400 s; capacity increment.08 kg/kg; 5% breakthrough225 s; unused fraction.4375.
- Pressure-swing equilibrium loadings.1428571429/.04 and difference.1028571429 kg/kg.
- Chromatographic k'=2, tr=6 min; Gaussian N400, effective177.7778, half-height width.7064460135 min.
- Velocity optimum.002 m/s; plate height.003 m; N333.3333.
- Peak times6/7 min, widths.24/.28 min; measured/exact resolution3.846153846; later-width approximate3.571428571; approximate required N1764.

Every printed numerical example answer agrees with independent code.

## Figures, structure and language

Individually opened u4-transport, fronts, breakthrough, pressure-swing, chromatography, van-deemter and resolution PNGs. All contain the relevant readable source construction. Figure labels retain source conventions while adjacent prose defines draft notation.

All nine notes contain seven prescribed sections, clear assumptions, reasons for derivation steps, standalone explanations and prose topic links. No lecture/PDF references, wikilinks or callouts found. Local equation labels sequential from1 in each note. All seven ../figs targets exist at the intended publication subject location. This is a source/Markdown review; no Obsidian runtime claim.

## External verification

Actually opened David Harvey Analytical Chemistry2.1 chapter12.2 and12.3:

- https://chem.libretexts.org/Bookshelves/Analytical_Chemistry/Analytical_Chemistry_2.1_by_David_Harvey/Analytical_Chemistry_2.1_(Harvey)/12:_Chromatographic_and_Electrophoretic_Methods/12.02:_General_Theory_of_Column_Chromatography
- https://chem.libretexts.org/Bookshelves/Analytical_Chemistry/Analytical_Chemistry_2.1_by_David_Harvey/Analytical_Chemistry_2.1_(Harvey)/12:_Chromatographic_and_Electrophoretic_Methods/12.03:_Optimizing_Chromatographic_Separations

They support conventional plate-width/retention terminology and van Deemter/later-width resolution approximation. The exact unequal-width expression in the draft was checked by direct substitution, independently of textbook shortcuts.

# Codex independent review: AB-U11

Existing Claude-owned short notes unchanged. Findings and replacements are for merged deliverables only. No BOARD/PLAN changes or commits.

## Independent derivation and numerical results

Extraction mass balance M=Cu Vu+Cl Vl with Cu=K Cl gives Y=Kr/(1+Kr). Y=0.95454545 or 0.67741935. Using the defined total-mixture C0=M/(Vu+Vl), Cu/C0=K(1+r)/(1+Kr)=1.14545455 or 2.03225806: concentration ratio 1.77419355. At fixed M and Vl instead, ratio=7.09677419. Neither consistent basis gives tenfold dilution.
Cohn is an empirical salting-out model, not a universal first-principles law; use ln(S/Sref)=beta-Ks Cs with numerical concentration reference units fixed. Ks=ln(770/29)/1.6=2.049434178 M^-1,beta=9.515598364. At 2.5 M S=80.802905093 ug/mL, precipitated fraction=55.109497%. Required salt for 90,95,99% is 3.232710119,3.570924046,4.356232464 M; values beyond measured 3 M are extrapolations. Salt saturation at 25 °C cannot prove impossibility at every temperature. Protein already precipitates below salt saturation.
Langmuir: identical independent sites, association k_on C(1-theta)=k_off theta -> theta=KC/(1+KC),q=qmax theta. Linear at low C, saturated at high C. Freundlich is empirical and cannot represent unlimited physical uptake. Batch mass balance Vliq(Cinitial-Cfinal)=Vres q(Cfinal) gives Vres=0.1591909253,0.2141706237,0.3920224985 m³ for 90,95,99%. Correct batch numbers, not validated dynamic packed-bed capacity.
Additional material corrections: AB44 pI means ZERO NET charge, not no charged groups; acid/base pH adjustment leaves counterions, so changing pH does not leave nothing behind. Native salting-out and denaturation are distinct; the water-stripping narrative is misleading.

Full precision results: ../scratch/codex-ab-review/results.json. Reproduction script: ../scratch/codex-ab-review/check_examples.py.

## Exact merged-only replacements

Use ../scratch/codex-ab-review/merge-fixes.json before equation renumbering or other rewriting. Every old substring has been validated as present exactly once in its original note and after preceding replacements. Additional caveats above are review findings; the JSON prioritizes bounded corrections.

### AB-42, replacement 1

Original mixes fixed-mass and fixed-total-mixture-concentration bases.

Exact old:

~~~text
**The trade this hides.** In (a) the product is recovered into five volumes of upper phase; in (b) into half a volume. The enzyme in (a) is therefore ten times more dilute than in (b), despite 95 % recovery. Taking a basis of 1 unit of lower phase and unit feed concentration, the upper-phase concentration is $0.95/5 = 0.19$ in case (a) against $0.68/0.5 = 1.36$ in case (b) — a factor of 7 in favour of the smaller phase.
~~~

Exact replacement:

~~~text
**The concentration trade needs a stated basis.** With $C_{A,0}$ defined as the average concentration in the total two-phase mixture, mass balance gives $C_{A,u}/C_{A,0}=K(1+r)/(1+Kr)$, where $r=V_u/V_l$. The two cases give 1.145 and 2.032, so case (b) has about 1.77 times the upper-phase concentration at the same $C_{A,0}$. Holding total enzyme mass and lower-phase volume fixed instead gives a ratio of about 7.10. Neither basis gives tenfold dilution; a phase ratio alone does not determine concentration relative to the original feed before additives.
~~~

### AB-43, replacement 1

Salting-out salts can stabilise native protein.

Exact old:

~~~text
Anything that makes water less available to the protein destabilises this arrangement. Add enough salt and the ions, which hydrate strongly themselves, compete for the water. The solvation shell thins, hydrophobic regions become exposed, and proteins aggregate with one another instead — they precipitate.
~~~

Exact replacement:

~~~text
At sufficiently high concentration, suitable salts make dissolved protein less thermodynamically favourable relative to a protein-rich phase. Ion-specific interactions and preferential exclusion from protein surfaces can favour association while preserving the folded structure. This is not literal stripping of the hydration shell.
~~~

### AB-43, replacement 2

Do not claim a literal water-removal mechanism is complete.

Exact old:

~~~text
That is the whole mechanism: **precipitation is caused not by the salt attacking the protein, but by the salt removing its water.**
~~~

Exact replacement:

~~~text
**Salting out reduces protein solubility through salt-dependent solvent and protein interactions; precipitation does not require protein unfolding.**
~~~

### AB-43, replacement 3

Replace incorrect shell-depletion/unfolding chain.

Exact old:

~~~text
**Why the fall happens.** Salting out depends on ions, particularly **anions**, interfering with the solvation of water:
- Water molecules form a **solvation shell** around proteins, which **prevents aggregation**.
- At higher salt concentration, anions bind more often to water, making it **less available to form the solvation shell** and thus prompting aggregation.
- **Solvation is also important for the secondary and tertiary structure of proteins**, so high salt may also cause protein **unfolding** — the main risk of the method.


~~~

Exact replacement:

~~~text
**Why solubility can fall.** Ion-specific interactions change protein solvation and protein–protein association. Preferential exclusion of suitable salts from protein surfaces can favour association and the compact native state. Ammonium sulfate precipitation need not denature the protein. Other salts or unsuitable conditions can destabilise it, so precipitation and unfolding must be distinguished.


~~~

### AB-43, replacement 4

Temperature-specific extrapolation; protein already precipitates at 2.5 M.

Exact old:

~~~text
The required 4.36 M is **above saturation**, so 99 % recovery is **not achievable with this salt at all** — the salt would precipitate before the protein did.
~~~

Exact replacement:

~~~text
The required 4.36 M exceeds the quoted saturation at 25 °C, so **99 % recovery is not predicted to be attainable at that temperature under the extrapolated fitted model**. Additional salt would remain undissolved or crystallise; protein precipitation already begins below this limit.
~~~

### AB-43, replacement 5

Repair repeated mechanism and saturation overclaims.

Exact old:

~~~text
Salting out precipitates proteins by depriving them of their solvation shell, with effectiveness ranked by the Hofmeister series. The Cohn equation, $\ln S = \beta_s - K_sC_s$, is fitted from two solubility measurements and then predicts recovery. For the IgA example, 2.5 M ammonium sulfate precipitates only 55 %, and 99 % would need 4.36 M — above the salt's own solubility. Section 44 covers the three other precipitation routes.

~~~

Exact replacement:

~~~text
Salting out lowers protein solubility through ion-specific changes in solvation and association, and need not unfold the protein. The fitted Cohn equation predicts about 55 % precipitation for this IgA example at 2.5 M ammonium sulfate. Extrapolating to 99 % gives 4.36 M, above the quoted salt saturation at 25 °C. Section 44 covers the other precipitation routes.
~~~

### AB-45, replacement 1

Batch equilibrium resin requirement cannot be asserted as dynamic packed-bed design.

Exact old:

~~~text
**Sense check.** About 160 L of resin treats 2 m³ of liquor — a volume ratio of roughly 1:12, which is reasonable for a packed column.
~~~

Exact replacement:

~~~text
**Scope of the calculation.** About 159 L of initially unloaded resin equilibrates with 2 m³ of liquid in a single batch. The isotherm is evaluated at the final bulk liquid concentration. A flowing packed bed instead requires dynamic capacity at the chosen breakthrough criterion; this batch-equilibrium result is not a validated packed-column design.
~~~

## Figure checks and limitations

All 45 distinct local figure links resolved and decoded; all were opened visually in six contact sheets. Several inherited crops contain clipped surrounding text/labels, notably AB-36 tubular geometry and AB-42 extraction. They are recognisable, but crop quality is imperfect. Figures were not modified. Source Sigma and gel-volume equations were inspected as images and agree with the displayed formulas; the main corrections concern interpretation and applicability. Local equation numbers remain for parent renumbering. Phrase scan found no prose references to lecture PDFs/slides/lecturers; inherited image residue remains visible.

## Sources actually opened

- [Zhang and Cremer original lysozyme phase-transition experiments, PNAS 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2741236/). Full text opened; distinguishes native stabilization/salting out and ion-specific surface interactions.

Retrieval limits: Cytiva SEC handbook/FAQ and IUPAC Gold Book/PAC PDF could not be retrieved and were not relied upon. One Hofmeister PMC page presented a bot challenge; an RSC page returned 403; neither was used.

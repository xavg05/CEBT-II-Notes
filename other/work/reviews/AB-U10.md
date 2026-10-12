# Codex independent review: AB-U10

Existing Claude-owned short notes unchanged. Findings and replacements are for merged deliverables only. No BOARD/PLAN changes or commits.

## Independent derivation and numerical results

Survival fraction f per pass gives unreleased fraction f^N; hence -ln(1-R/Rmax)=N[-ln f]. Empirical -ln f=k p^a gives the release law. k has units pressure^-a and changes with pressure units.
Independent two-stage fits: through-origin slopes sum(N y)/sum(N²) are 0.049957624,0.133692267,0.263316887,0.426386809,0.569050269. Log slope vs log pressure gives a=2.3741978415356453; k=1.7330118194343895e-7; R²=0.9993708389205004. N=4.42546394 -> FIVE passes; p=568.781272 -> about 570 kgf/cm². Predicted release: 93.7917766% at 550/5,26.0685730% at 200/6. Printed rounded a,k instead give N=4.54874994,p=575.63037644; retain parameter precision when substituting. Doubling pressure gives 5.18447478 equivalent passes, not five EXTRA passes.
Stress tau=mu*shear_rate is independent of particle diameter at fixed gradient. Total force and wall/membrane load can depend on diameter. Exponent a measures pressure sensitivity, not independently wall toughness.
AB41 thermolysis is not cytoplasm boiling; heating, SDS and solvents are not uniformly gentler than homogenisation. Wall-free osmotic lysis does not establish that intact microbes burst in water.

Full precision results: ../scratch/codex-ab-review/results.json. Reproduction script: ../scratch/codex-ab-review/check_examples.py.

## Exact merged-only replacements

Use ../scratch/codex-ab-review/merge-fixes.json before equation renumbering or other rewriting. Every old substring has been validated as present exactly once in its original note and after preceding replacements. Additional caveats above are review findings; the JSON prioritizes bounded corrections.

### AB-38, replacement 1

Original asserts an incorrect size dependence of stress.

Exact old:

~~~text
**Why size matters mechanically.** A small cell is harder to break by shear because the stress a flow field imposes on a particle scales with its size. A large yeast cell or a mammalian cell presents a bigger target to the same velocity gradient than a 1 µm bacterium does. Bacteria are therefore doubly disadvantaged: tough walls *and* small size.
~~~

Exact replacement:

~~~text
**Why size can matter mechanically.** In a Newtonian flow the shear stress is $\tau=\mu\dot\gamma$, where $\dot\gamma$ is shear rate; stress itself does not grow with cell diameter. Larger cells can experience larger integrated forces and velocity differences across their extent. Rupture also depends on envelope strength, geometry and disruption mechanism, so size alone does not rank susceptibility.
~~~

### AB-40, replacement 1

Extra fit digits make substitutions reproduce reported outputs, not a claim of experimental precision.

Exact old:

~~~text
$$a = 2.37, \qquad k = 1.73\times10^{-7}\ (\mathrm{kg_f\,cm^{-2}})^{-a}$$
~~~

Exact replacement:

~~~text
$$a = 2.37420, \qquad k = 1.73301\times10^{-7}\ (\mathrm{kg_f\,cm^{-2}})^{-a}$$
~~~

### AB-40, replacement 2

N=4.42546 from full precision.

Exact old:

~~~text
1.73\times10^{-7}\times460^{2.37}
~~~

Exact replacement:

~~~text
1.73301\times10^{-7}\times460^{2.37420}
~~~

### AB-40, replacement 3

Consistent k in pressure substitution.

Exact old:

~~~text
2\times1.73\times10^{-7}
~~~

Exact replacement:

~~~text
2\times1.73301\times10^{-7}
~~~

### AB-40, replacement 4

p=568.781 rounds to 570.

Exact old:

~~~text
\right]^{1/2.37} = 570
~~~

Exact replacement:

~~~text
\right]^{1/2.37420} = 570
~~~

### AB-40, replacement 5

Total equivalent passes versus added passes; remove unsupported far extrapolation.

Exact old:

~~~text
**Doubling the pressure is worth about five extra passes.** For *E. coli* at these conditions, a single high-pressure pass beats several gentler ones, which is why industrial homogenisers are built for 1500–2500 bar.
~~~

Exact replacement:

~~~text
**Doubling pressure multiplies the effective pass count by about 5.2** in the fitted model: one pass at doubled pressure has the same predicted release as about 5.2 passes at the original pressure. This conditional comparison does not justify extrapolating the 200–550 kg$_f$ cm⁻² fit to 1500–2500 bar.
~~~

### AB-40, replacement 6

Thermolysis deliberately heats and chemicals can denature.

Exact old:

~~~text
Section 41 covers the non-mechanical alternatives, which avoid the heat and shear entirely.
~~~

Exact replacement:

~~~text
Section 41 covers non-mechanical alternatives, whose heat, chemical and product-stability risks depend on the method.
~~~

### AB-41, replacement 1

90 °C thermolysis is not boiling at ordinary pressure.

Exact old:

~~~text
by boiling the cytoplasm
~~~

Exact replacement:

~~~text
by heating and damaging the envelope
~~~

### AB-41, replacement 2

Do not generalise erythrocyte osmotic lysis to walled microbes.

Exact old:

~~~text
- *Hypotonic* conditions are obtained by diluting into pure water, causing water to **flow into the cytoplasm**, so the cells swell and **burst**.
~~~

Exact replacement:

~~~text
- *Hypotonic* conditions draw water into cells. Wall-free cells such as red blood cells can swell and lyse, but intact bacterial and yeast walls usually resist the load. Efficient microbial release often needs envelope weakening or a specific osmotic-shock protocol.
~~~

### AB-41, replacement 3

Not all methods are gentle or introduce consumables.

Exact old:

~~~text
Non-mechanical disruption works by making the cell burst itself (thermolysis, decompression, osmotic shock), dissolving its membrane (detergents, solvents), or cutting its wall enzymatically — the last being the most selective, with lysozyme, chitinase and pectinase matched to the organism's wall chemistry. All are gentler than homogenisation and all introduce a consumable that scales with batch size, which is why production remains mechanical and these methods belong to the laboratory. This completes cell disruption; Section 42 begins primary isolation of the released product.

~~~

Exact replacement:

~~~text
Non-mechanical disruption can damage envelopes by heat or pressure changes, solubilise membranes chemically, or digest wall components enzymatically. Heating, SDS and solvents can denature products, while appropriate enzymes or controlled osmotic shock can be selective. Suitable scale and reagent-removal steps depend on the method. This completes cell disruption; Section 42 begins primary isolation.
~~~

## Figure checks and limitations

All 45 distinct local figure links resolved and decoded; all were opened visually in six contact sheets. Several inherited crops contain clipped surrounding text/labels, notably AB-36 tubular geometry and AB-42 extraction. They are recognisable, but crop quality is imperfect. Figures were not modified. Source Sigma and gel-volume equations were inspected as images and agree with the displayed formulas; the main corrections concern interpretation and applicability. Local equation numbers remain for parent renumbering. Phrase scan found no prose references to lecture PDFs/slides/lecturers; inherited image residue remains visible.

## Sources actually opened

Corrections follow independent mass/force/transport derivations from the notes' stated assumptions; no external factual claim was needed.

Retrieval limits: Cytiva SEC handbook/FAQ and IUPAC Gold Book/PAC PDF could not be retrieved and were not relied upon. One Hofmeister PMC page presented a bot challenge; an RSC page returned 403; neither was used.

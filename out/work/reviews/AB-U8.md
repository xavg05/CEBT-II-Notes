# Codex independent review: AB-U8

Existing Claude-owned short notes unchanged. Findings and replacements are for merged deliverables only. No BOARD/PLAN changes or commits.

## Independent derivation and numerical results

Darcy: dV/dt=A Δp/[μ(RM+φ cV/A)]. Integration gives t=μ RM V/(A Δp)+μ φ cV²/(2A² Δp). With φ=φ' Δp^s, cake-only t=φ'cμ V²/[2A² Δp^(1-s)]. φ has units m/kg; RM has units m^-1. Cake-only V grows as sqrt(t), so positive finite t has positive flux: AB33's finite-time zero-flow claim is wrong. Bigger area reduces V/A and cake mass per area; it does not halve flux. Lab property group=10102474.94428964; areas=1.1514448379 and 1.3693063938 m². This is a minor rounding correction from 1.36 to 1.37.
Additional material caveats for parent: AB32 illustrative table does not imply concentration/purity rise at every step; extraction and chromatography can dilute. AB34 pressure exponent alone cannot show that buying more low-pressure area is almost always economically optimal.

Full precision results: ../scratch/codex-ab-review/results.json. Reproduction script: ../scratch/codex-ab-review/check_examples.py.

## Exact merged-only replacements

Use ../scratch/codex-ab-review/merge-fixes.json before equation renumbering or other rewriting. Every old substring has been validated as present exactly once in its original note and after preceding replacements. Additional caveats above are review findings; the JSON prioritizes bounded corrections.

### AB-34, replacement 1

Flux effect is reversed in original.

Exact old:

~~~text
doubling the area halves the flux *and* halves the cake thickness
~~~

Exact replacement:

~~~text
doubling the area halves the required filtrate volume per unit area *and* halves the final cake thickness
~~~

### AB-34, replacement 2

Unrounded lab group gives 1.36930639 m².

Exact old:

~~~text
$$A = 1.36\ \mathrm{m^2}$$
~~~

Exact replacement:

~~~text
$$A = 1.37\ \mathrm{m^2}$$
~~~

### AB-34, replacement 3

State unrounded input to reproduce areas.

Exact old:

~~~text
**Step 2: size the pilot filter** from (9), with $V_f = 0.5$ m³ and $t = 3600$ s.
~~~

Exact replacement:

~~~text
**Step 2: size the pilot filter** from (9), with $V_f=0.5$ m³ and $t=3600$ s. Use the unrounded laboratory group, $\phi'c\mu_f=1.0102475\times10^7\ \mathrm{s\,m^{-2}\,Pa^{0.5}}$, in both calculations.
~~~

## Figure checks and limitations

All 45 distinct local figure links resolved and decoded; all were opened visually in six contact sheets. Several inherited crops contain clipped surrounding text/labels, notably AB-36 tubular geometry and AB-42 extraction. They are recognisable, but crop quality is imperfect. Figures were not modified. Source Sigma and gel-volume equations were inspected as images and agree with the displayed formulas; the main corrections concern interpretation and applicability. Local equation numbers remain for parent renumbering. Phrase scan found no prose references to lecture PDFs/slides/lecturers; inherited image residue remains visible.

## Sources actually opened

Corrections follow independent mass/force/transport derivations from the notes' stated assumptions; no external factual claim was needed.

Retrieval limits: Cytiva SEC handbook/FAQ and IUPAC Gold Book/PAC PDF could not be retrieved and were not relied upon. One Hofmeister PMC page presented a bot challenge; an RSC page returned 403; neither was used.

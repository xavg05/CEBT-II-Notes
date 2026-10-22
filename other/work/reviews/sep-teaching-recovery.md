# Separations II teaching-content recovery, 22 October 2026

## Diagnosis and plan

Reviewed all 43 current short notes against the corrected text immediately before commit `77f9703`. That commit removed 392 canonical lines under worked-example headings. The losses included solvent-cycle and equipment-selection reasoning, distinctions between moisture/humidity/recovery bases, drying branch changes and quadrature checks, coupled membrane design data, two interpretable figures, and adsorption/chromatographic design comparisons.

The plan was approved by the coordinating agent before editing: start with current corrected text; retain useful mechanisms, assumptions, quantitative comparisons and limiting checks inside the existing explanatory sections; omit repetitive direct substitution; preserve every surviving reviewed equation label; synchronise canonical drafts and both existing publication editions. Separations has no authorised complete-section groupings, so none were created.

## Implementation

All 43 notes gained useful teaching. Twenty-one retain a quantitative comparison where the values demonstrate a distinct inference, numerical-method issue, change of active regime or practical design decision. The other additions retain qualitative mechanisms and validity distinctions without reproducing arithmetic already supplied by the derivation. Detailed per-note decisions are recorded in `sep-teaching-recovery.json`.

The recovered whey osmotic correlation is an unnumbered empirical relationship, preserving all 176 current numbered equations. The two restored figure links use their original publication identities, `SEP-28-gas-profiles.png` and `SEP-32-whey-pressure.png`. Their figures were opened visually; their axes, starting condition and endpoint features are explained beside them. The gas-profile composition gaps are explicitly distinguished from partial-pressure driving force. The whey curve stops at gel onset and is not extrapolated as a post-gel law.

The original batch-concentration consequence, rejection-loss diagnostic and local oxygen-enrichment comparison were retained in SEP-24–26 after contextual review. The last also repairs a surviving reference to a downstream comparison. A bare local equation reference in the recovered saturation paragraph was converted correctly to the current global reference.

## Author validation

- Re-executed reviewed Python numerical models for all four source units in a separate namespace, without overwriting the historical numerical records or recropping figures. Retained numerical comparisons agree with their underlying model; uncertainty and model limitations are retained.
- Checked 43 published native notes against their HEAD labels: all 176 surviving labels unchanged. Published labels match the GitHub edition.
- Opened all 35 referenced figure files in both formats through Pillow; visually inspected the two restored figures.
- KaTeX parsing and native/GitHub formula comparison passed for 1,457 expressions across the 48 published pages, with zero failures.
- The repository inline maths guard passed for 663 Markdown files. This is a static check, not an Obsidian application runtime test.
- No original PDF, shared board, root specification, subject navigation, unrelated subject or RE-S2 work was changed.

Independent review of this recovery is tracked separately by the coordinating agent; the previous scientific review does not automatically cover these revisions.

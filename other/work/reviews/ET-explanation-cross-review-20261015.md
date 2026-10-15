# Independent ET explanation cross-review, 15 October 2026

Reviewer: independent Codex cross-reviewer. Read all 43 current native short notes in full, including each applied addition and its surrounding derivations, figures' captions, worked-example interpretation and conclusions. Read the author's ET explanation report and proposal JSON. Compared every applied edit with the preserved before-revision native source indexed by the manifest. No study notes or author proposal files were edited.

## Verdict

**Three small prose replacements required before closure; no incorrect new equation, number, state constraint or mechanism found in the 43 additions.**

The additions explain specific missing connections rather than repeating a generic template. Algebra and thermodynamic logic pass within each note's existing assumptions. Some insertions separate an introductory colon from its displayed result by one or two explanatory paragraphs; this is readable and not a required correction. The additions are proportionate to the existing notes.

## Required integration corrections

Exact unique old/new strings are in `other/work/scratch/all-subject-explanations/et-cross-review-corrections.json`, covering ET-10 (two edits) and ET-13 (one edit).

ET-10 now correctly states that the sign of an activity coefficient is not a unique diagnosis of molecular attraction, since excess entropy can contribute. Its retained sign bullets and summary still make the unconditional attraction claim. ET-13 repeats that claim in a generic closing definition. Qualify the two sign bullets with common energetic explanations and retain the exact chemical-potential comparison; replace the two summary/closing clauses with that exact comparison. This follows directly from the definition $RT\ln\gamma_i=\mu_i-\mu_i^{\mathrm{IM}}$ and is independently illustrated by the existing athermal size-asymmetry examples in ET-18/20. No original numerical example or equation changes are needed.

The corrections should propagate through the native short notes, existing complete sections, canonical units and GitHub reading edition. Their anchors were checked to occur once in the respective current native short notes.

## Specific requested checks

**ET-35 passes.** Stoichiometric chemical potentials add, their logarithms give a product of ionic activities, and the geometric mean coefficient reproduces that product. The added paragraph correctly separates the coefficient from salt activity and notes both ionic-strength and charge-factor changes between NaCl and CaCl2. The corrected 3.6% statement now explicitly concerns the mean coefficient relative to unity, retaining the verified original value; it no longer attributes that percentage to full salt activity, which contains the coefficient squared for NaCl.

**ET-36 passes.** The turning-point factor vanishing is explicitly the spinodal/loss of local homogeneous stability. Binodal coexistence instead comes from the global common-tangent comparison. The negative homogeneous mixing energy versus an even lower split-state energy is correctly explained relative to pure-liquid baselines. ET-27 and ET-39 use the same distinction consistently.

## Independent mathematical and physical review

- ET-01–09: independent conserved transfers justify componentwise equality; stationary versus globally stable states are distinguished. The constant-enthalpy differential gives the stated throttling sign. Euler reconstruction uses simultaneous final-composition partial molar values. Fixed-composition real/ideal subtraction, the logarithmic fugacity-ratio force and endpoint versus path-integrated EOS information are consistent.
- ET-10–20: activity versus coefficient, total versus molar excess derivatives, changing total-amount denominators, two linearisations in cryoscopy, branch selection on cooling, the geometric-mean square, lattice site versus chain counts, normalised local weights and multiplicative coefficient decomposition all follow the stated models. Retained generic force claims are the only integration issue requiring qualification.
- ET-21–28: independent phase constraints are counted without pair duplication; amounts require separate balances. Osmotic energy terms oppose correctly. Laplace pressure is applied to the appropriate phase; fixed-reservoir stability is qualified. Lever-rule elimination and known-phase normalisation give the correct bubble/dew equations. The azeotropic thermodynamic factor stays positive on a locally stable branch, and introducing the van Laar ratio cancels the shared denominator as stated.
- ET-29–35: changing a hypothetical standard fugacity rescales the activity coefficient inversely; pressure experiments state fixed methane partial pressure versus fixed gas composition. Unit dilute-reference coefficient does not remove solvent interactions. Identical-state fugacity equality is correctly rejected as a coexistence test; criticality needs disappearing density as well as composition differences. Exact molality-reference conversion separates constant and composition terms. Ionic weights and powers pass as above.
- ET-36–43: local curvature and global common tangents remain distinct. Fixed energetic A becomes a smaller A/RT on heating; the LCST discussion requires different temperature dependence. Activity compensation explains unequal phase concentrations without net transfer. Conserved symmetric fluctuations cancel first-order contributions. Uphill concentration diffusion retains positive mobility and requires gradient energy for interfaces. For positive sub-unity thermodynamic factor, a sub-unity exponent raises its value while preserving critical vanishing. Three-phase composition constraints versus changing phase amounts and the separate-liquid pure-component limits in steam distillation are correctly explained.

## Reproducibility and review limits

Ran `other/work/scratch/all-subject-explanations/check_et_revision_cross_review.py`. Its saved `et-independent-cross-review-validation.json` confirms all 43 notes and 45 author edits reproduce the current files exactly from their preserved originals, with unique anchors and unchanged numbered equation strings and figure links.

The review independently followed the added algebra in the actual native contexts; no new numerical answers were introduced or required. It does not repeat the prior original-PDF source audit, recompute unchanged examples, visually reopen unchanged images, run Obsidian or claim a final rendered-publication check. External citations and retrieval provenance remain in the author's source record; those sources were not all freshly opened by this cross-reviewer.

After the three supplied prose replacements are applied and their propagation is checked, the scientific explanation revision can be marked **PASS**.


## Closure

The three replacements in `et-cross-review-corrections.json` were applied to the ET-10 and ET-13 short notes, the topic 03 complete section, the canonical reviewed unit and the reading edition. The old unconditional attraction wording no longer appears in any live file. Revision verifier and KaTeX check pass. **PASS.**

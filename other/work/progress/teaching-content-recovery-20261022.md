# Teaching-content recovery — diagnosis and plan, 22 October 2026

Authorisation: Xavier requested diagnosis and planning followed by implementation across all current notes, with parallel subagents. His clarification preserves useful worked-example content as ordinary learnable material. This scoped revision includes earlier Claude-owned notes; historical ownership remains recorded on BOARD.md.

## Diagnosis before editing

Commit 77f9703 removed entire worked-example sections. Those sections mixed substitutive calculations with unique definitions, derivations, mechanisms, figures and qualifications. Structural/maths checks of the deletion did not check the survival of these ideas. AB-15 prenatal screening is a confirmed complete mechanism loss, with dangling references left behind. Other confirmed losses include AB-12 Phred scores, RE-06's same-RTD counterexample, SEP design graphs and PDC interpretation of response curves.

## Implementation plan

1. Compare each current canonical note with its corrected pre-removal counterpart from 77f9703's parent. Preserve all subsequent corrections and unrelated working-tree changes.
2. Record a decision for every current short note: recover distinct mechanism, derivation, figure interpretation, design method, limitation or useful quantitative comparison; omit repeated substitution or material already adequately taught. Integrate retained ideas under existing explanatory headings with topic-specific subheadings, rather than renaming whole worked-example blocks.
3. Work in disjoint subjects: Codex AB, ET and SEP subagents; coordinating Codex handles RE and PDC. No new grouping or complete-section merges. Preserve AB-U13 external supplementation and AB-57 optional status.
4. Synchronise canonical inputs, current GitHub short notes and existing complete sections, and portable native Obsidian copies. Keep source PDFs and historical snapshots unchanged. Retain current equation labels and avoid renumbering unrelated material.
5. Recompute retained quantitative claims in Python, review equations/units/limits and inspect reused figures. Obtain independent subagent cross-review, then check mathematical parsing, inline unit safety, remaining references, mirror parity, relative links, figures and portable relocation.
6. Commit only this revision's files in reviewable batches. Do not include the unrelated incoming Reaction Engineering solid-reagent PDF, scratch directory or verification script. No push requested.

## Scope of evidence

This is a recovery audit against reviewed pre-removal content and current notes, not a fresh all-page rereading of every source PDF. Reuse source and review evidence, consult primary references for changed scientific claims, and record actual checks and limitations in subject recovery records.

## Completed implementation and review

All 186 existing short notes were audited: ET 43, AB 57, RE 21, SEP 43 and PDC 22. Useful recovered teaching was integrated in 41 ET, 37 AB, 43 SEP, 8 RE and 20 PDC notes; the remaining decisions identify material already taught or notes with no deleted example. Additional orphan-reference and title corrections are included. Seven filenames formerly titled "Worked example" now name their topic; all current navigation and complete-section links were rebuilt. No new grouping was created.

Canonical inputs, both publication editions and all 29 existing complete sections are synchronised. Prenatal screening now includes maternal/placental mixture, chromosome dosage, calibrated counts, random uncertainty, depth scaling and inference limits. Other recoveries include sequence quality, empirical fitting, nonlinear mixing, separation-design comparisons and control-response interpretation. The earlier no-worked-example-heading rule remains compatible with this instruction: a section's label is never a reason to discard useful teaching. For subsequent revisions preserve the mechanism, derivation, qualification or meaningful comparison inside the ordinary explanatory sections, and remove only redundant exercise framing/arithmetic.

Independent cross-reviews passed for all five subjects, with findings corrected by each owning author. See `../reviews/ab-teaching-cross-review-20261022.md`, `et-teaching-cross-review-20261022.md`, `sep-teaching-cross-review-20261022.md` and `re-pdc-teaching-cross-review-20261022.md`. Per-note decisions are in the AB recovery report, ET recovery JSON, SEP recovery JSON and RE/PDC recovery JSON.

## Verification and practical limits

- Python replay and independent reviews checked retained calculated results; measured data and graph-read inputs remain qualified rather than being represented as recomputed observations. One flash result now uses a vapour fraction approximately 0.435 consistently with its rounded equilibrium constants. Prenatal dosage explicitly accounts for normalisation and distinguishes the counting model from clinical predictive value.
- The complete native/reading text and formula comparison passes for all 215 study pages per edition (186 short notes and 29 complete sections). Markdown/KaTeX checks parsed 20,304 expressions across both editions with zero failures. Existing equation labels were preserved; selected historically deleted results regained their original labels.
- All 5,020 current relative links across both editions resolve. All 232 referenced figures decode. Restored figures were visually inspected by authors/reviewers; the prenatal-screening section was additionally rendered in headless Chrome and its screenshot opened. This is not a claim of live GitHub or Obsidian runtime testing.
- The inline-maths guard passed across 666 current publication/canonical Markdown files. All 43 original tracked source PDFs remain byte-identical.
- The native ZIP was regenerated, extracted into an unrelated temporary vault/course tree, compared bytewise and link/figure checked. Windows' extended-path API was required for the descriptive deep filenames; MAX_PATH extraction without that API failed. The final relocation check passes. The user’s vault was not opened or written.
- Concurrent solid-reagent Reaction Engineering production is outside this recovery's historical scope. Its incoming sources, new drafts, figures and publisher were not included in this revision. Its planned renaming/renumbering must preserve these corrected current draft bodies and obtain its own publication validation; old scoped recovery publishers must not run after that migration without adapting their filename/label mappings.

Sources newly opened for the coordinating scientific check: [APMonitor/BYU first-order dynamics](https://www.apmonitor.com/pdc/index.php/Main/FirstOrderSystems), [University of Michigan/Fogler mixing models](https://public.websites.umich.edu/~elements/5e/17chap/summary.html). APMonitor's displayed inverse-transform line contains an extra constant in its exponent; the surrounding ODE and correctly stated step relation were independently derived and checked rather than copying that line. The Washington University PDF request timed out and its contents were not used. AB's primary-source additions and reused historical scientific evidence are documented in its recovery record.

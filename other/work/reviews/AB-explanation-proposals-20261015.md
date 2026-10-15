# Advanced Biotechnology explanation proposals, 15 October 2026

Read-only review of all 57 actual native short notes under `other/obsidian/CEBT-II Notes/Advanced Biotechnology/`. Only reviewer proposal, validation and review artifacts were written. No canonical notes, exports, figures, source PDFs, ownership board or plans were edited.

## Result and integration

`other/work/scratch/all-subject-explanations/ab-proposals.json` contains 57 entries covering AB-01–57, with 61 exact replacements. Every note receives one topic-specific explanatory paragraph or replacement, integrated at an existing section anchor. Four additional replacements align the AB-14 platform comparison table and AB-22 reversibility/opening discussion with qualified mechanisms. Added prose totals approximately 27,000 characters across the subject; these are focused causal links rather than a generic appendix.

The proposals were based on the existing corrected working-tree texts, including the recent source-coverage corrections. Whole-paragraph anchors preserve surrounding sentences and lists. JSON line endings are normalised to LF for use with Python `read_text`. Source equations, continuous equation tags and all existing figure links are preserved. The optional status of AB-57 and external-supplementation qualification of AB-48–52 remain untouched. Complete-section/native/GitHub propagation belongs to the coordinator.

Validation: ran `validate_ab_proposals.py`, applying proposals in memory only. It confirms 57 unique paths, 61 unique exact anchors, unchanged numbered equation strings and unchanged figure links. Results are in `ab-proposal-validation.json`. No new numerical values, fitted parameters or graph readings were introduced; algebraic additions are direct consequences of already stated models. This proposal validation is not a rendered-deliverable or independent final-review pass.

## Explanation gaps addressed

- AB-01–05: primer geometry; persistence correlation as an ensemble quantity; equilibrium mass action versus encounter kinetics; sequence order versus GC count; pseudo-first-order partner excess.
- AB-06–10: washing versus drying; logarithmic compounding; assembly versus internal sequence verification; the recipient-cell bootstrap; migration time versus polymerisation time.
- AB-11–15: optical amplification versus independent molecules; missing repeat-spanning information; overlapping k-mer constraints; passes versus sample coverage; systematic bias versus counting noise.
- AB-16–19: threshold movement as an assay check; common loading perturbation and reference cancellation; distinct purposes of processing and contamination controls; wash selection for dissociation kinetics.
- AB-20–26: multivalent local concentration; exchange times versus annealing schedule; encounter rate times success probability; solvent-inclusive folding free energy; density versus atom model; nonlocal NMR restraints; domain placement versus local confidence.
- AB-27–30: avidity versus site affinity; FcRn binding/release trade; mutation controls; droplet occupancy and signal retention.
- AB-31–37: local nutrient histories; product stream and recovery versus purity; surface-element drum cycles; solids-loading basis; g-factor versus trajectory; local terminal speed versus inertial acceleration; matching feed in Sigma scaling.
- AB-38–47: disruption versus solubilisation/refolding; discrete survival law; transformed-data error amplification; enzyme access; equilibrium versus transport; saturation before precipitation; depletion free volume; breakthrough dynamic capacity; peak broadening; collection-cut purity/recovery.
- AB-48–57: inherited-message initial conditions; promoter occupancy mean versus switching kinetics; graphical stability directions; fluctuation filtering; distributed expression lags; shared cell-free resources; orthogonal RNA quality properties; conditional gene-essentiality tests; substrate-supply feasibility; dye/client/scaffold exchange as distinct signals.

## Existing provenance reused

Read CLAUDE.md and PLAN.md, plus BOARD ownership/status. Reused source mapping and corrections in `AB-01-47-source-coverage-20261014.md`; read the AB-U13-L13, AB-U13-L14, AB-U14 and AB-U15 reviews, and the four AB-48–57 progress/source records. Their original primary-source and visual-reading evidence is retained; I do not represent those historical readings as a fresh all-page reread by this reviewer. No original-PDF ambiguity was needed to create these conceptual additions, so no lecture PDFs were reprocessed.

## External sources actually opened and read in this pass

1. [NEB Gibson Assembly](https://www.neb.com/en-us/applications/cloning-and-synthetic-biology/dna-assembly-and-cloning/gibson-assembly): read application overview and enzyme workflow. Confirms exonuclease exposure, extension and ligation. Used to check the assembly-versus-verification addition.
2. [Zhang and Winfree, Control of DNA Strand Displacement Kinetics Using Toehold Exchange (2009), author PDF](https://www.dna.caltech.edu/Papers/Toehold_Exchange2009.pdf): read introduction, domain/toehold discussion and reverse-displacement account on printed pp17303–17305. Confirms toehold colocalisation and slow reverse invasion rather than absolute impossibility. The simple success-probability interpretation follows the existing note's reduced competing-rate model; it is not a claim that every branch-migration intermediate has a constant single microscopic rate.
3. [Bio-Rad qPCR Analysis](https://www.bio-rad.com/en-be/applications-technologies/qpcr-analysis?ID=8bf12444-522e-e3cb-18cd-ccd0ec94f91a): read amplification phases, baseline/threshold guidance and reference-gene example. Used for common-threshold and loading-normalisation mechanism checks.
4. [EMBL-EBI AlphaFold confidence overview](https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/), [pLDDT](https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/plddt-understanding-local-confidence/), and [PAE](https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/pae-a-measure-of-global-confidence-in-alphafold-predictions/): read local/global distinction and poorly constrained interdomain placement example. Supports the AB-26 two-domain explanation.
5. [Cytiva chromatography principles](https://www.cytivalifesciences.com/en/us/insights/chromatography-principles): read purification objectives, load/wash/elution, property-based methods and bead-size/flow-resistance discussion. Supports separating purity, yield and peak width in the proposed downstream additions.
6. [MIT Cooney centrifugation PDF](https://ocw.mit.edu/courses/10-445-separation-processes-for-biochemical-products-summer-2005/c462dea1243e90bd4b2d5dd2e8dc51e3_lecture_4.pdf): read prose on feed properties, Stokes-law limitations and equipment/feed factorisation; [rotary filtration PDF](https://ocw.mit.edu/courses/10-445-separation-processes-for-biochemical-products-summer-2005/a2f55fd05608ed9a86152fb8d3f9da0a_lecture_9.pdf): read cycle/filtration text. These are supplemental mechanism checks, not replacement authorities for the notes' different Sigma convention. Screenshot requests returned references without visible image content in this tool path; no claim of visually rereading those equations.
7. [Elowitz and Leibler repressilator primary paper, Caltech-hosted copy](https://www.rpgroup.caltech.edu/embl_pboc_2023/assets/pdfs/repressilator.pdf): read repressilator introduction, wiring, mRNA/protein model discussion and lifetime/oscillation conditions. Supports explicit intermediates versus a fixed delay; no new periods copied.
8. [NEB cell-free expression](https://www.neb.com/en-gb/applications/protein-expression/cell-free-protein-expression/): read PURE component list, energy regeneration, NTPs and factor omissions. Checks the finite-resource and controlled-composition interpretation.

No search snippets were treated as read sources. The NCBI Bookshelf NBK26821 request returned only a browser check; the IDT efficiency URL, one obsolete NEB cell-free URL and Cytiva PDF endpoint returned retrieval errors. Those failed contents were not used. MIT cell-disruption PDF was opened but its text layer contained almost no scientific text, so it is not represented as a read mechanistic authority.

## Qualifications and remaining review limits

AB-14's corrected main text distinguishes stochastic and correlated errors, but the retained comparison table still used the older absolute labels. The two table-row proposals correct that internal inconsistency without changing historical illustrative instrument ranges.

AB-22 previously stated a century lifetime for a 20 bp duplex at room temperature while AB-05's explicitly conditional worked sequence predicts much longer. A universal alternative time is unsupported. The proposal removes that condition-free number and states dependence on sequence, salt and temperature. It also replaces literal irreversibility with kinetic protection supported by Zhang–Winfree. AB-05's illustrative kinetic table is preserved; its very long extrapolated lifetimes remain model-dependent.

The additions have not been independently cross-reviewed by another reader yet. Final publication must apply the exact anchors against the current files, check the resulting prose flow and maths rendering, and propagate the edits through both reading editions and existing complete sections.


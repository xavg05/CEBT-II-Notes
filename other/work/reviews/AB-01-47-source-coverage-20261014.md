# Advanced Biotechnology AB-01–47: source coverage review, 14 October 2026

Reviewer: independent Codex reviewer. Original short-note owner: claude. No owned study notes, canonical units, complete sections or exports edited. Proposed changes are review artifacts awaiting the owner's corrections or the user's explicit ownership exception.

## Outcome

The main topic sequence and supplied numerical exercises from lectures 1–12 are present in the published notes. The new comparison found smaller source omissions and several overstatements in added explanations. **Do not describe AB-01–47 as error-free or close the source-readiness findings until these are resolved.** Existing AB-25 findings remain in `AB-U6-coverage-20261014.md` and are additional to this report.

Concrete, standalone proposed text with exact old snippets, canonical-unit paths, published small-note paths and source locations is in `other/work/scratch/coverage-audit-20261014/review/ab-proposed-corrections.json`. All **17** old snippets were validated to occur exactly once in their canonical units. The generating script emits proposals only; it does not apply them.

## Evidence and limits

This is a source-coverage pass with selected scientific checks, **not a fresh derivation of every AB equation or an all-page visual reread**. The earlier scientific reviews `FINAL-AB-01-30.md` and `FINAL-AB-31-47.md` supply the retained full derivation, numerical and figure-check evidence. Their existence is not treated as a replacement for the new source comparison.

The twelve original PDFs comprise **521 pages**, with page counts 37,31,37,31,37,42,63,44,45,62,49,43. Reviewed their page-indexed text content for substantive topic and exercise locations and compared the corresponding published subject/topic units (complete sections plus targeted small-note reads). Text-layer output was used to locate ordinary prose and learning outcomes, not as an equation authority. Re-rendered and opened **60 targeted original pages**, including image-heavy/textless protein panels, quantitative exercises, sequence assembly diagrams and uncertainty metrics. The page selection is recorded in `render_ab_spots.py`; the ten contact sheets and individual pages are in `review/ab-visual-spots/`. Opened the existing AB-08 Gibson and PCA crops separately to establish whether absent prose was actually supplied by figures.

The new numerical checks were restricted to findings in this pass: qPCR efficiency percentage and consensus error tails. Values are in `independent-ab-numbers.json`. The original source PDFs are unchanged. No examination papers or separate example sheets were supplied, so coverage of lecture material cannot establish readiness for every possible examination question.

## Actionable findings

1. **AB-08, PCA/Gibson: complete the standalone prose.** The general two-regime paragraph does not name polymerase cycling assembly or Gibson assembly, identify T5/Phusion/Taq ligase, explain why chewing back 5′ ends exposes 3′ overhangs, or mention the staged enzyme option. Importantly, **the Gibson crop already supplies the broad exonuclease/polymerase/ligase steps and 50 °C**. This is a prose-completion finding, not a claim that all those steps are absent from the study assets. Source: L2 pp20–26. Proposed replacement explicitly names the two routes and explains the direction of repair without repeating the source's ambiguous phrase about extending 5′ ends.

2. **AB-26, AlphaFold confidence: source subtopic genuinely omitted.** L7 p47 names pLDDT, pTM and PAE, and p48 displays an aligned-error matrix and overall/interface scores. Current prose reduces uncertainty to unnamed per-residue confidence. Add definitions and distinguish local fold confidence from confidence in relative domain placement. The proposed passage avoids claiming that low confidence proves disorder.

3. **AB-27, ADC design: payload selection omitted.** L8 p14 lists four choices: attachment site, drug choice, copy number and linker release. Current text announces only three and omits drug choice. Proposed paragraph restores the fourth. The p15 clinical efficacy graph supports the already included usefulness of the ADC example; reproducing its dated study-specific numbers is optional context, not a new design equation or missing method.

4. **AB-30, computational tasks omitted.** L8 p42 distinguishes affinity maturation, rank prediction from NGS candidates and NGS-informed out-of-library design. Current paragraph discusses generative design only. Proposed text adds these distinct tasks and treats the influenza hit rate as a reported demonstration, rather than an undated universal current benchmark.

5. **AB-19, sole-approved-aptamer claim is false.** Both the comparison table and applications paragraph say there is one approved drug, pegaptanib. FDA approved avacincaptad pegol (Izervay) in August 2023. This error is in added explanatory prose; the source only discusses pegaptanib as an example and mentions ongoing development. Proposed changes retain pegaptanib and add the second example without claiming an exhaustive worldwide current count.

6. **AB-14, residual consensus overstatements.** Despite qualified worked-example text, a separate mechanism paragraph says all relevant nanopore ambiguities are systematic, repeats can never reach Q30, and SMRT errors are essentially independent. The summary still says repeated independent measurements convert a 12% raw error into HiFi accuracy. Neither claim follows from the corrected numerical model. Proposed replacements distinguish random and correlated errors on both platforms and state that actual consensus quality must be measured. This reconciles the prose with the previous scientific review's limits.

7. **AB-12, analogous consensus/tie flaw persists.** The text claims consensus is wrong only when most of the thirty calls are wrong in the same way, then reports the binomial tail for sixteen or more errors. That is a strict-error-majority tail, not a complete conservative consensus-failure bound including ties. For independent substitution errors with p=0.001, the tail at ≥16 is **1.43518236×10⁻⁴⁰**, while the tie-inclusive conservative bound at ≥15 is **1.52950492×10⁻³⁷**. Proposed text uses the latter, explicitly stating the model and separating it from real alignment/systematic errors. The changed toy example remains an added explanation, not a missing lecture exercise.

8. **AB-17, percentage denominator and efficiency cancellation.** With the stated ΔΔCt=−3.3, 2³·³=**9.84915531**, while 1.9³·³=**8.31547157**. Using 9.849 instead of 8.315 is an **18.4437% overestimate**, not 16%; the latter approximates the **15.5717% decrease relative to the reported estimate**. A separate paragraph says the second subtraction cancels the two assays' intrinsic efficiencies. Replace that with cancellation of fixed assay intercepts; efficiency still sets slope and must be matched or included. The equations and main assumptions already correctly state this, so the residual prose is inconsistent rather than a new mathematical model defect.

9. **AB-30, selection limitations are overstated.** “No concern about self-reactivity” should mean bypassing an animal's immune tolerance during selection, not proof of absence of unwanted binding. “Cannot target toxins” is false as a universal claim, and all animal methods do not require humanisation: the same note describes animals with human antibody repertoires. Proposed text states toxic/immunologically tolerated targets can be difficult and retains experimental specificity validation.

10. **AB-10, cloning is not universal Sanger chemistry.** Current low-throughput explanation says every fragment requires its own cloning. L3 separates general reaction inputs from the cloning-based shotgun workflow. A purified PCR product or plasmid can be a direct template. Proposed text confines cloning to the applicable library workflow. The platform comparison table's “cloning” and “per-fragment cloning” entries should likewise be labelled as shotgun-library preparation, not a prerequisite of all Sanger sequencing; the coordinator should patch these table cells together with the paragraph.

11. **AB-24, added X-ray explanation overstates optical limits and reverses one source example.** X-rays can be focused using lenses/mirrors; the macromolecular diffraction experiment nevertheless records intensities rather than directly producing an atom-resolved image. Current opening says no X-ray lens exists. L7 p31 describes an example near 1.8 Å in the synchrotron workflow and notes poorer data with an in-house source; current prose presents 1.8 Å as an in-house capability. The further assertion that resolution is set by crystal order “not by the instrument” overlooks wavelength/angular coverage, signal and dose. Proposed passages retain diffraction, phase loss, Bragg's law and the benefit of ordered crystals while qualifying these extra statements.

The 17 exact replacements cover the paragraphs/table row for these eleven grouped findings. AB-25's separate three corrections are not duplicated. The Sanger comparison table cells require the same qualification as finding10, using the concrete text below.

### Additional exact table-cell proposals for finding10

Canonical unit: `other/work/archive/reviewed-units/Advanced Biotechnology/04 - Sequencing II - long reads and applications.md`, comparison table under Section14. Current rows:

```text
| Amplification | cloning | PCR + bridge PCR | **none** | **none** |
| Preparation | per-fragment cloning | 1–2 days | minutes | circularisation |
```

Proposed rows:

```text
| Amplification | sufficient template required; cloning in shotgun workflows | PCR + bridge PCR | **none** | **none** |
| Preparation | purified template; separate clone preparation for shotgun libraries | 1–2 days | minutes | circularisation |
```

These cells appear in the published AB-14 small note, complete section and corresponding native export and should be regenerated together. Fixed numerical platform ranges are lecture examples and should not be presented as universal contemporary product specifications.

## Source mapping and covered content

| Original source | Published small notes | Principal content accounted for |
|---|---|---|
| L1 pp12–21 | AB-01 | Backbone/direction, naming, canonical and noncanonical pairing, B/A/Z helices, RNA chemistry and structures. |
| L1 pp22–23 | AB-02 | Persistence-length correlation, ss/ds stiffness; notes add the WLC derivation and mean-square end-to-end result. |
| L1 pp25–30 | AB-03 | Two-state equilibrium, enthalpy/entropy signs, melting definition and equal-total-concentration exercise, with self-complementary qualification. |
| L1 pp31–35 | AB-04 | Ten nearest-neighbour types, tabulated parameters, terminal/symmetry terms, salt correction and computational tools. |
| L1 p37 | AB-05 | Association/dissociation rates, detailed balance and length/temperature sensitivity; numerical sequence examples explicitly use a chosen sequence. |
| L2 pp6–15 | AB-06 | Uses, solid support, monomer/protection chemistry, synthesis cycle, capping, oxidation, deprotection and purification/modification. |
| L2 pp16–17 | AB-07 | Supplied99.4%/99.1% yield problem, length scaling and additional impurity calculations. |
| L2 pp19–26 | AB-08 | Overlap thermodynamics, extension, outer-primer enrichment and Gibson schematic; prose completions above. |
| L2 pp27–31 | AB-09 | Hierarchical bacterial-genome assembly, transplantation, watermark/control, eukaryotic projects and limits. Source historical/funding amounts are context rather than a new method. |
| L3 pp7–17 | AB-10 | Chain termination, separate reactions/dye labels, capillary separation, strengths/limits, shotgun and coverage/cost logic. Cloning wording above. |
| L3 pp20–28 | AB-11 | End repair, A-tailing, adapters, library PCR/indices, surface capture, bridge amplification and linearisation. Correct end-repair direction retained. |
| L3 pp29–37 | AB-12 | Reversible terminators, imaging/wash/unblock, paired-end reads, assembly, biases and short-read tradeoff. Consensus added-example correction above. |
| L4 pp6–12 | AB-13 | Ionic current, pore translocation, motor slowdown/unwinding, context-sensitive calling, arrays, RNA/modification and portability/accuracy tradeoffs. |
| L4 pp14–18 | AB-14 | Hairpin circularisation, polymerase wells, terminal-phosphate label, ZMW confinement, pulses and long-read comparison. Qualified consensus prose needed. |
| L4 pp21–31 | AB-15 | Whole-genome/exome/panel, transcriptomics, construct verification, personalised treatment rationale, rare disease, risk, prenatal counts, virus surveillance, eDNA and forensics. |
| L5 pp6–12 | AB-16 | PCR review, amplification phases, intercalating dye, Ct threshold and logarithmic copy-number dependence/exercise. |
| L5 pp13–17 | AB-17 | Standards, reference genes, double subtraction, efficiencies and melting control. Residual prose/numerical precision fixes above. |
| L5 pp18–26 | AB-18 | TaqMan, beacon, reverse transcription/primer choices, gene expression and COVID workflow/controls;5′ nuclease vs proofreading and viral polyadenylation corrections retained. |
| L5 pp28–37 | AB-19 | Aptamer/library design, SELEX cycle, RNA conversion, cell/counter-selection and therapeutic/biosensing applications. Approved-drug count corrected above. |
| L6 pp8–13 | AB-20 | Programmable selectivity, polymer geometry, reversible pairing, sequence count and complementary/random thermodynamic example. |
| L6 pp15–30 | AB-21 | Design/anneal, kinetic traps, junction stiffness, tensegrity/DX/polyhedra, scaffold/staples/crossovers,3D/wireframe/hierarchy and applications. |
| L6 pp32–42 | AB-22 | Toehold states, branch migration, effective competition rate, short/long/crossover regimes, tweezers/fuel, walkers and reconfigurable origami. Correct standard-concentration factor retained. |
| L7 pp3–9 | AB-23 | Four structure levels, helix/sheet geometry, Levinthal/funnel, hydrophobic contribution, marginal stability/chaperone qualifications. |
| L7 pp18–32 | AB-24 | Crystal diffraction, intensity/amplitude, phase problem, heavy atoms/MIR, molecular replacement, purification/crystal/data/refinement workflow; optics and resolution explanations qualified above. |
| L7 pp35–42 | AB-25 | Vitrification, particle projections/alignment/classification/reconstruction and NMR restraint ensemble. Separate unresolved AB-U6 report applies. |
| L7 pp45–63 | AB-26 | Anfinsen/prediction, CASP, MSA/co-evolution, Evoformer, coordinate module/recycling, experimental complement and AF2/AF3 distinction. Missing confidence subtopic above. |
| L8 pp3–17,23 | AB-27 | Size/fragments/CDR rigidity, specificity, fusions/BiTE/DNA/particles/PET/ADC and affinity. Restore payload-choice design axis. |
| L8 pp18–22 | AB-28 | Biphasic PK, FcRn pH salvage/Fc transfer, variable glycosylation/effector activity and protease gating. Prior target-mediated-clearance correction retained. |
| L8 pp24–29 | AB-29 | SDM workflow, rational residue choices/alanine/stop, bleach-resistant protease and orthogonal amber-suppression machinery. |
| L8 pp30–44 | AB-30 | Polyclonal/hybridoma/humanisation, phage, gene–phenotype linkage, droplet catalysis, human-repertoire mice, human B cells and generative design. Add three computational tasks and qualify selection limits. |
| L9 pp6–23 | AB-31/32 | Bioprocess stages/scales, host/conditions, upstream auxiliaries, downstream branching, purity/concentration table, product lability and cost logic. L9p7 explicitly says product catalogue need not be memorised. |
| L9 pp25–33 | AB-33 | Filtration/pretreatment, cake/filter aid, plate/frame and drum cycle, practical/aseptic limits. |
| L9 pp35–45 | AB-34 | Resistance balance, integration, compressibility, laboratory-to-pilot example at both pressures and tradeoff. |
| L10 pp7–17 | AB-35 | Bowl/disc mechanics, foaming/cleaning/continuous-solids handling and filtration comparison; equipment data table included as figure. |
| L10 pp19–29 | AB-36 | Gravity/drag/buoyancy, radial speed, entry-radius cut time, residence-time inequality and supplied numerical machine example. Source unit/power-of-ten errors corrected. |
| L10 pp30–38 | AB-37 | Geometry/feed factorisation, convention/area distinction, alternate bowl and disc expression and doubled-geometry exercise. |
| L10 pp41–45 | AB-38 | Intracellular targets/inclusions, disruption classification, Gram+/Gram− and yeast wall/mammalian contrast. |
| L10 pp47–54 | AB-39 | Beads, cavitation, homogeniser/French press, heat, release law and pressure exponent with fitted-range limits. |
| L10 pp55–62 | AB-40 | Full measured release table, two-stage regression and both supplied design questions, with whole-pass and extrapolation handling. |
| L11 pp8–16 | AB-41 | Heat/freeze/decompression/osmotic, detergent/solvent and matched wall enzymes, debris/removal/integration. |
| L11 pp19–30 | AB-42 | Primary-isolation objective, immiscible solvent/countercurrent equipment, PEG/salt or dextran phases, partition/yield balance and both α-amylase ratios. |
| L11 pp31–42 | AB-43 | Salting-in/out, ion specificity/Hofmeister, Cohn fit, complete antibody precipitation exercise and original unfinished99%-recovery extension. |
| L11 pp43–49 | AB-44 | pI/charge, solubility and conceptual staged pH, polymer/depletion and miscible-solvent contrasts; unverified factory-specific claim correctly qualified. |
| L12 pp8–19 | AB-45 | Four adsorption-cycle stages, propagating zone/breakthrough, Langmuir/Freundlich with units/assumptions and antibody-resin example, explicitly batch-equilibrium. |
| L12 pp22–34 | AB-46 | All five chromatography types, polarity/partition/pore access/counterion/ligand mechanism, Ni-NTA and Protein A limitations. |
| L12 pp35–43 | AB-47 | Elution/capacity/retention, pore-volume and hydrated-gel relations, HPLC/FPLC scope and product final form. Peak ratio correctly distinguished from resolution. |

Title/admin/outline repeats, speaker biographies, Nobel anecdotes, business valuations and duplicate animations/pictures were not treated as missing scientific topics. This mapping includes source exercises rather than relying on matching topic keywords. Additional diagrams can illustrate a topic already covered without needing every decorative image repeated.

## Opened external evidence for new findings

- [FDA Izervay approval snapshot](https://www.fda.gov/drugs/drug-trials-snapshots/drug-trials-snapshots-izervay): RNA aptamer and4August2023 approval. [FDA NDA217225 summary](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2023/217225Orig1s000SumR.pdf), pp3–4: PEGylated RNA aptamer targeting C5. Used only to correct the educational example/count, not for prescribing advice.
- [EMBL-EBI AlphaFold2 confidence](https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/) and [AlphaFold Server metrics](https://www.ebi.ac.uk/training/online/courses/alphafold/alphafold-3-and-alphafold-server/alphafold-server-your-gateway-to-alphafold-3/interpreting-results-from-alphafold-server/): local/aligned/overall confidence distinction and score conventions.
- [NEB DpnI hemimethylation FAQ](https://www.neb.com/faqs/will-dpni-cleave-hemimethylated-dna): confirms slower hemimethylated cleavage. Current broad “methylated” description need not be expanded into a new exam subtopic; no additional fix demanded on that basis.
- [Nobel organisation's history of antitoxins](https://educationalgames-staging.nobelprize.org/educational/medicine/immuneresponses/overview/index.php): animal-derived antitoxins support removing a universal toxin exclusion. This is an official historical explanatory page, not the original experimental paper. The requested Behring Nobel lecture endpoint returned403 and was not treated as read.
- [Diamond's own X-ray optics experiment description](https://www.diamond.ac.uk/Science/Research/Highlights/2023/Developing-a-Varifocal-X-ray-Lens.html): explicitly uses X-ray refractive lenses and mirrors for focusing; supports correcting the universal no-lens claim. The linked Nature paper failed at its access/redirect endpoint and was not treated as read.

## Delivery state

Review proposals are concrete and ready for owner correction/user-authorised integration. Regenerate GitHub small notes, complete sections and native export from the canonical unit rather than changing one generated copy. Reread changed passages and rerun the affected numerical checks, then preserve this report as the source-to-note record. Until then, report **main lecture topic coverage with identified unresolved corrections**, not unconditional exam readiness.

## Adjacent AB-25 precision check requested by coordinator

After the initial report, reread AB-25's remaining NMR/static/dynamic discussion. Two adjacent paragraphs would still undermine the three initial AB-25 corrections: “NMR ... reports conformational dynamics that crystallography cannot”, and the categorical shared-static-limitation passage. Minimal exact replacements are separately recorded in `review/ab25-adjacent-corrections.json` (both old paragraphs uniquely matched), leaving the main17-replacement file unchanged.

The proposed text distinguishes structure restraints from relaxation/exchange observables, treats30kDa as a conventional practical scale rather than a hard law, and acknowledges time-resolved diffraction. It does not pretend that a calculated NMR ensemble directly traces one molecule moving. Primary supporting evidence actually opened: [RCSB PDB5CNE](https://www.rcsb.org/structure/5CNE), which reports an X-ray experiment at10ps delay and the original time-resolved myoglobin paper abstract. This directly disproves an absolute claim that crystallography cannot investigate dynamics. The requested RCSB6YJ0 NMR page failed and is not claimed as read.

## Authorised correction closure review — 15 October 2026

The user authorised the reviewed Biotechnology corrections. Independent read-only verification of the applied 24-replacement batch passed across 43 canonical/published/export files: 120 replacement-target checks found each new passage exactly once and its exact obsolete predecessor absent. Normalisation was limited to GitHub inline-maths delimiters. The changed passages were reread for scientific meaning; the five AB-25 replacements now consistently distinguish ensemble restraints, uncertainty, experimentally measured dynamics, practical molecular-size scales and time-resolved diffraction. No remaining AB-25 blocking finding was identified in those passages and their previously flagged context.

The affected independent calculations were rerun: the qPCR estimates are 9.8491553 and 8.3154716, giving an 18.4437373% overestimate relative to the latter or a 15.5717286% reduction relative to the former. The independent 30-read, 0.001-error binomial tails are 1.5295049e−37 including ties (at least 15 errors) and 1.4351824e−40 excluding ties (at least 16). The illustrative Bragg angles are 22.6437403° at 2 Å and 74.2594515° at 0.8 Å. Results agree with the original independent check to relative tolerance 1e−12. Evidence: `review/ab_closure.py` and `review/ab-closure-verification.json` in the coverage scratch directory.

Closure rereading identified five additional narrow consistency proposals, recorded with exact old/new passages and canonical paths in `review/ab-closure-proposals.json`: qualify ligase in AB-08's shared-method step; remove deterministic every-read/no-coverage-gain claims from three AB-13 paragraphs; add one AB-26 sentence defining ipTM. These do not invalidate the applied 24 changes, but must be integrated before the adjacent-context closure is complete. The AB-26 item follows a fresh visual reopening of Lecture 7 p48: the example expressly labels ipTM alongside pTM. [EMBL-EBI's confidence documentation](https://www.ebi.ac.uk/training/online/courses/alphafold/alphafold-3-and-alphafold-server/alphafold-server-your-gateway-to-alphafold-3/interpreting-results-from-alphafold-server/) confirms that ipTM measures interface confidence on a 0–1 scale. Specific example scores are not proposed as memorisation targets.

This closure is bounded to the reviewed corrections and adjacent consistency, and retains the original source-coverage limitations above. Rendering, publication-mirror structural validation and source hashes are checked separately by the coordinating agent; this report does not claim a new full-course equation or all-page visual audit.

### Final independent closure verdict: PASS

The coordinating agent applied all five adjacent proposals under the user's authorisation. The final 29-replacement batch passes 145 independent replacement-target checks across 45 files, including canonical units, GitHub small notes/complete sections and native export copies. The verifier accounts for the later ipTM addition superseding the earlier AB-26 paragraph replacement. All original obsolete passages are absent and every final expected passage occurs once per target. A separate search across current reading notes, native exports and canonical units found no surviving phrases asserting identical errors in every homopolymer read, coverage incapable of improvement, an absolute static/dynamic division, X-rays incapable of focusing, a universal toxin exclusion, no self-reactivity concern, or only one approved aptamer. Affected numerical checks passed again with the values recorded above.

The approved passages and identified adjacent contexts are scientifically consistent. No unresolved finding remains from this review's correction set, including the AB-25 appendix. This verdict supersedes the earlier pending-integration delivery state for these reviewed findings, while retaining the stated limits on source coverage and independent visual/equation scope. Unrelated preserved historical production snapshots are not current reading copies and were outside the phrase-removal requirement.

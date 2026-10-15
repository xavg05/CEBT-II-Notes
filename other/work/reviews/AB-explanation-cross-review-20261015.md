# Advanced Biotechnology explanation cross-review — 15 October 2026

Independent reviewer: Codex. Reviewed all 57 entries and 61 replacements in other/work/scratch/all-subject-explanations/ab-proposals.json against the corresponding actual native short notes. Every target note was read in context, including its assumptions, derivation, example and neighbouring explanation. Re-read truncated tool output in smaller batches. Read the proposal author's source/provenance report; its historical source reading is not represented here as fresh all-PDF reading.

No study notes, proposals, sources, indexes or plans edited. This task owns only this report.

## Assessment

The new passages give specific causal explanations and preserve established equations and numerical results. No new mathematical or numerical error identified. Two small wording qualifications are requested to prevent the applied context overstating the new explanations; both were sent to the coordinator.

1. **AB-21, existing sentence immediately before the new annealing explanation.** “Cooling slowly from above T_m keeps the system equilibrated, so it escapes these kinetic traps” is absolute and conflicts with the new, correct statement that slow cooling improves access without guaranteeing equilibrium. Replace with wording such as: “Cooling slowly from above T_m can allow incorrect contacts to exchange and help the system escape these kinetic traps.” The new passage correctly compares bond-exchange time with the annealing schedule. This contextual correction does not alter any equation or number.

2. **AB-51, new pulse-smoothing paragraph.** “A short promoter pulse produces some messages, but a long-lived protein pool changes only a little during that pulse” needs a reference regime. Large pulses or initially empty pools can produce large abundance changes even with long protein lifetime. Specify comparison with the sustained response around a steady expression level. Suggested opening: “Around a steady expression level, a promoter fluctuation short compared with protein lifetime has little time to change protein abundance relative to its sustained effect.” The rest of the paragraph correctly distinguishes rapid fluctuation filtering from transmission of slow variation, consistent with the note's explicit fixed-mean limits.

These qualifications concern explanatory precision, not defects in the reviewed original numerical models.

## Per-note checks

| Note | Independent assessment of new content |
|---|---|
| AB-01 | Primer orientation follows extendable 3′ ends and antiparallel templates; complementarity alone insufficient. |
| AB-02 | Tangent correlation is ensemble information; persistence and Kuhn lengths not literal hinges. |
| AB-03 | Equilibrium dilution distinguished from slower encounters; mass action and translational entropy correctly explain melting shift. |
| AB-04 | Neighbour-step inventory distinguishes equal-GC sequences; separate enthalpy/entropy sums allow temperature variation. |
| AB-05 | Pseudo-first-order assumption correctly restricted to approximately fixed partner; equal pools deplete. |
| AB-06 | Washing removes reagents; drying protects activated monomer; support retention does not remove attached truncations. |
| AB-07 | Logarithm turns per-step multiplication into cumulative loss; small per-step failure can cause large overall loss. |
| AB-08 | Outer-primer amplification checks terminal sites, not correct internal assembly or sequence. |
| AB-09 | Compatible recipient machinery bootstraps synthetic-genome expression; sequence not sufficient to build bare-chemical cell. |
| AB-10 | Migration coordinate is fragment separation time, not polymerisation time; mixed ladders generally not individually assignable. |
| AB-11 | Cluster brightness distinguished from independent original-molecule sampling; pre-seeding PCR duplicates correctly qualified. |
| AB-12 | Repeat ambiguity needs links to unique flanks; paired fragments help only within available molecular span. |
| AB-13 | Overlapping k-mer windows constrain sequential decoding; homopolymers weaken state-change information. |
| AB-14 | Repeated passes improve one molecule's read, not independent sample coverage. Table now permits stochastic and correlated errors in both long-read platforms, matching corrected main text. |
| AB-15 | More depth reduces random counting uncertainty, not library/mapping bias or biological-source ambiguity. No new clinical cutoff or advice added. |
| AB-16 | Common threshold change preserves sample differences only under shared exponential efficiency/response. |
| AB-17 | Shared input-loading shift cancels in within-sample difference; target-specific expression does not. Existing efficiency qualifications retained. |
| AB-18 | Process control and no-template control test different failure routes; post-extraction spike cannot verify extraction. |
| AB-19 | Wash can select off-rate and incubation can select on-rate; neither is simply equilibrium affinity. |
| AB-20 | Prior tethering reduces subsequent association entropy cost; multivalent assembly not guaranteed by isolated pair screening. |
| AB-21 | Bond-exchange versus cooling timescale correct; contextual absolute equilibrium sentence requires qualification above. |
| AB-22 | Encounter rate times success probability has bimolecular units; reduced competition explicitly labelled. Reverse invasion is slow rather than impossible; unsupported universal duplex lifetime removed. |
| AB-23 | Folding free energy includes solvent, conformational entropy and unsatisfied polar groups; more internal H-bonds alone not sufficient. |
| AB-24 | Density-to-atom inference and phase/model bias separated from polished model appearance; refinement not proof of unique interpretation. |
| AB-25 | Nonlocal NMR contacts constrain fold; ensemble spread alone does not establish actual dynamics. |
| AB-26 | High local domain confidence compatible with uncertain interdomain orientation; engineering implication appropriate. |
| AB-27 | Avidity from local rebinding distinguished from intrinsic monovalent site affinity. |
| AB-28 | FcRn rescue requires acidic capture and neutral release; maximum affinity alone not complete design target. |
| AB-29 | Activity loss may reflect expression/fold/assembly, not direct catalytic role; controls identify causal route. |
| AB-30 | Single-genotype occupancy and signal retention preserve genotype–phenotype link; leakage and mixed droplets allow false recovery. |
| AB-31 | Single DO probe not cell's local history; supply/mixing timescales compared with cellular demand. |
| AB-32 | Product-bearing stream identified before discard; concentration, purity and recovery separated. |
| AB-33 | Plant-continuous drum consists of cyclic surface elements; total area not simultaneously immersed filtration area. |
| AB-34 | Solids per filtrate-volume basis distinct from broth basis because liquid remains in cake. |
| AB-35 | Peak g does not capture radial trajectory, separation distance or residence-time challenge. |
| AB-36 | Increasing local terminal speed distinguished from appreciable inertial momentum storage; radial integration accounts for slower interior. |
| AB-37 | Matching feed factor required for Sigma cancellation; upstream flocculation/disruption/viscosity cannot be put into pure geometry. |
| AB-38 | Disruption exposes inclusion-body aggregate but does not solubilise or refold it. |
| AB-39 | Discrete fixed-fraction survival motivates log residual and continuous-pass representation; whole passes retained in design. |
| AB-40 | Log residual amplifies uncertainty near completion, especially uncertain maximum; original-space checks appropriate. |
| AB-41 | Enzyme access and bond specificity both required; lipid solubilisation not equivalent to cleaving load-bearing polymer. |
| AB-42 | Concentration cancels only for constant partition law and linear balance; mixing/phase disengagement trade identified. |
| AB-43 | Saturation check precedes precipitate inventory; final mixture volume matters. |
| AB-44 | Overlapping exclusion layers increase polymer free volume; nonadsorbing depletion distinct from bridging. |
| AB-45 | Dynamic breakthrough capacity can fall with broadening at unchanged isotherm; batch equilibrium calculation remains distinct. |
| AB-46 | Differential migration competes with band broadening; strong common retention not sufficient. |
| AB-47 | Fraction-cut purity/recovery depends on actual peak widths and shapes, not centre spacing alone. |
| AB-48 | Zero initial message means zero initial protein synthesis; rounded start is lag without explicit dead time. |
| AB-49 | Occupancy mean does not determine switching times; notation explicitly separates state transcription rates from stochastic switching constants. |
| AB-50 | Direction arrows beside production/removal intersection correctly determine restoring behaviour and slope interpretation. |
| AB-51 | Filtering mechanism agrees with lifetime-ratio equations; pulse-amplitude/regime qualification requested above. |
| AB-52 | Explicit message/protein intermediates supply distributed response lag; fixed delay is a different model. |
| AB-53 | Added templates compete for fixed machinery and energy; host-free does not imply linear yield in DNA. |
| AB-54 | Orthogonal quality attributes require compatible assays; multiplication uses conditional recoveries of same target population. |
| AB-55 | Gene restoration and nutrient rescue strengthen causal interpretation; essentiality conditional on genome/environment/phenotype. |
| AB-56 | Maximum supply at zero internal concentration bounds constant demand; negative steady state flags missing substrate-dependent kinetics. |
| AB-57 | FRAP can report client/dye/scaffold processes; recovery and puncta alone not proof of intact fluid scaffold. |

## Application check

At the time of this check, Python read all 57 actual native paths and verified that every complete new replacement was already present exactly once: 61 of 61 passed. This confirms application rather than just unique old anchors. The two qualifications above were subsequently requested and require a closure read.

No changed example values were introduced by these additions, so the existing numerical-verification records remain applicable. All newly introduced simple mathematical interpretations follow directly from the equations already displayed. Equation numbering and figure content were not changed by the proposals.

## Style and provenance

Additions stay in the notes' existing structure and use the established notation. They generally explain a connection that was missing rather than insert generic summaries. Several nearby paragraphs partially overlap:

- AB-26's example repeats the immediately preceding high-pLDDT/high-PAE domain statement. Keeping the concrete alignment experiment and engineering implication while shortening the earlier statement would improve flow.
- AB-25's new restraint explanation expands the existing uncertainty-versus-motion qualification; it is useful because it explains nonlocal contacts, so retain that extra mechanism.
- AB-31's local-cell history repeats the general mixing paragraph but adds a probe-versus-trajectory distinction and timescale test; that is substantive.
- AB-38's inclusion-body paragraph repeats the need to refold stated just before it but adds why disruption cannot give dissolved activity. Consolidation is optional.
- AB-57's FRAP paragraph overlaps the previous dye-exchange caveat, but correctly adds separate scaffold labelling/control logic; combine if shortening is needed.

The AB-U13 external-source supplementation qualification must remain. The explanations do not claim that sparse original material independently supplied these additions.

I independently opened and read the following supplementary primary sources during this review:

- [Zhang and Winfree, Control of DNA Strand Displacement Kinetics Using Toehold Exchange](https://www.dna.caltech.edu/Papers/Toehold_Exchange2009.pdf): introduction and domain/toehold model discussion support colocalisation, reversible pathways and reduced-model limitations in AB-22.
- [EMBL-EBI, PAE in AlphaFold2 predictions](https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/pae-a-measure-of-global-confidence-in-alphafold-predictions/): independent domain-placement versus local-confidence check for AB-26.
- [NEB, Cell-free protein expression](https://www.neb.com/en-gb/applications/protein-expression/cell-free-protein-expression/): finite machinery/components and defined-mixture context for AB-53.

The proposal author's report records additional primary sources actually consulted for the other mechanisms. This review relies on the actual notes, existing verified model equations and that preserved provenance; it does not claim a new source-image audit or revalidation of every historical platform statistic.

Final browser/KaTeX/portable export checks remain coordinator publication tasks. No Obsidian runtime inspection claimed.

## Closure

Both qualifications were applied in the requested wording to the short notes, complete sections, canonical reviewed units and reading edition. AB-21 now reads "can allow incorrect contacts to exchange and help the system escape these kinetic traps". AB-51 now opens its pulse paragraph with the steady-expression reference regime. Revision verifier and KaTeX check pass. **PASS.**

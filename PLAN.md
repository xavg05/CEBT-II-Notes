# CEBT II lecture notes: production plan

Scope: **Equilibrium Thermodynamics** and **Advanced Biotechnology**, both completed and reviewed; **Reaction Engineering II**, started on 12 October 2026; and **Separations II** and **Process Dynamics and Control**, with new source inventories and provisional production units added on 12 October 2026. All original PDFs live under `other/sources/`.

Prefixes: `ET-` (continuing from the pilot ET-01 to ET-05), `AB-`, `RE-`, `SEP-` and `PDC-`. Short notes are numbered in teaching order. Page ranges refer to the PDF page index.

Where things go (full layout in CLAUDE.md, "Folder layout"): `notes/<subject>/<NN - topic>/` contains the small notes and a complete-section version; all figures for a subject are shared in `notes/<subject>/figs/`. `other/obsidian/CEBT-II Notes/` mirrors the topic tree with native Obsidian maths. Preparation and historical snapshots live in `other/work/`, and PDFs in `other/sources/`. There is no separate `merged/` or root `out/` folder.

**Current status, 12 October 2026:** ET-01–43 and AB-01–57 are fully written, reviewed and grouped into 12 Thermodynamics and 17 Biotechnology topic folders. The optional AB-57 is included. Separations II and Process Dynamics and Control are planned from the supplied sources; their inventories do not imply notes have been written or reviewed. The tables below retain the original teaching scope and writing recommendations; current completion and verification are recorded in [other/work/LAYOUT.md](other/work/LAYOUT.md) and [the final scientific review record](other/work/FINAL-DELIVERY.md).

## 0. Status and caveats

- **What the pilot most likely covered: `20TLect1.pdf` (21 pp).** The whiskey example is on p8 and p15–16. The "real-fluid correction integral" matches p20–21 (μ from an equation of state). Five notes of about one page each fit 21 sparse slides. This is an inference and needs confirming.
- **Tooling.** ImageMagick (`montage`, `magick`) is installed and PyMuPDF is available in the system Python (both confirmed by the OCR test); PIL is not installed system-wide. For this survey I used a throwaway venv in the session scratchpad (PyMuPDF and Pillow) and a small Python montage script. For production, either run `pip install pillow --break-system-packages`, or keep using a venv.
- **ET text layer:** garbled for maths throughout. Lecture 1 uses symbol fonts that come out as `! = %&&$"#`, and the later lectures lose Greek letters and subscripts (e.g. `1 = 1IM + 1ex` for $\mu_1=\mu_1^{IM}+\mu_1^{ex}$). All ET equations must be read from page images.
- **AB text layer:** mostly fine (Unicode maths), but fractions and sub- and superscripts flatten. Read equation slides from images. L14 has almost no text (2.6 k characters over 36 slides).

---

## 1. Equilibrium Thermodynamics

### 1.1 Inventory

Lecturer: the title slide names **Axel Zeitler**, while the PDF metadata author is "Moggridge" (slides inherited). Format: 16:9 PowerPoint exports with sparse text, hand-annotated red/blue equations and simple sketched plots. No scanned PDFs. No problem sheets.

| PDF | pp | Topic | Content type |
|---|---|---|---|
| 20TLect1 | 21 | Intro, notation, partial molar properties, μ, Gibbs–Duhem, ideal gas and ideal mixture, μ from an EOS | p1–6 admin/motivation; p10–12 Y1–2 revision; rest derivation. **Pilot (assumed)** |
| 20TLect2 | 14 | Liquid + inert gas, Poynting correction, definition of fugacity | Derivation; isotherm sketches (p5); steam-table image (p3) |
| 20TLect3 | 12 | Fugacity of water from steam tables, residual integral, fugacity coefficient | Worked example with data tables (p4, p11); isotherm sketches (p5–10) |
| 20TLect4 | 15 | Non-ideal mixing, activity coefficient, Gibbs–Duhem constraint, 1- and 2-constant Margules | Derivation; Sandler figures (p2, p9, p14) |
| 20TLect5 | 18 | O₂–Ar Margules example; multicomponent; measuring γ (ebulliometry, dynamic and static stills, freezing point) | Worked example (p2–10) + derivation |
| 20TLect6 | 15 | Freezing-point depression; glycol–water example; Redlich–Kister, van Laar, regular solution theory, Flory–Huggins | Derivation + phase-diagram figure (p8) |
| 20TLect7 | 13 | Wilson, NRTL, UNIQUAC, UNIFAC, model-choice summary | Equation survey; p13 says "read it, no need to memorise; must be able to use Margules, RST, van Laar" |
| 20TLect8 | 14 | Gibbs phase rule (revision + extension); osmotic equilibrium | p2–8 largely IB revision; p9–14 derivation |
| 20TLect9 | 15 | Droplets (Kelvin), bubbles, superheat | Derivation + isotherm/G–T sketches; p11–13 video/photo slides |
| 20TLect10 | 17 | Binary VLE diagrams, γ–φ formulation, Raoult, deviations, azeotrope condition | Derivation + many P–x–y/T–x–y figures |
| 20TLect11 | 23 | Pentane–propanal van Laar fit from azeotrope; binary types; gas solubility (hypothetical liquid, ideal solubility, Henry) | Worked examples (p2–5, p15–19) + figure-heavy (p6–9) |
| 20TLect12 | 11 | VLE near critical points; retrograde condensation/evaporation | Figure-heavy (Sandler diagrams), little maths |
| 20TLect13 | 19 | Solutes (molality), ions, mean ionic activity, Debye–Hückel; start of LLE (G-mix curvature) | Derivation + G–x sketches |
| 20TLect14 | 11 | LLE: common tangent, T-dependence, consolute points, VLE/LLE analogy; isobutane–furfural example | Derivation + worked example (needs a numerical solve) |
| 20TLect15 | 21 | Binodal vs spinodal, stability; diffusion driven by μ; nitrobenzene–hexane near consolute point | Derivation + data plots (p19, p21) |
| 20TLect16 | 8 | VLLE phase diagrams; steam distillation | Figure-heavy + short derivation |

### 1.2 Topic groupings

| Unit | Title | Sources | Why together | Short notes | Rec. | Figures | Image-equation reading |
|---|---|---|---|---|---|---|---|
| ET-U0 | Foundations: equilibrium criterion, EOS, partial molar properties, chemical potential | L1 p1–21 | One lecture, all foundations | ET-01 Criterion for phase equilibrium (p2–5, p10, p13)<br>ET-02 Equations of state and departure functions (p11–12)<br>ET-03 Partial molar properties, whiskey example (p7–9, p16)<br>ET-04 Chemical potential and Gibbs–Duhem (p14–15)<br>ET-05 Calculating the chemical potential (p17–21) | **drafted** (rewritten from L1 because the pilot files were not available) | p8 graph cropped | moderate |
| ET-U1 | Fugacity | **L2 p1–14 + L3 p1–12** (spans 2 PDFs) | Poynting → define f → compute f from PVT data | ET-06 Liquid in an inert gas: Poynting correction (L2 p1–9)<br>ET-07 Fugacity: definition and meaning (L2 p10–14, L3 p1)<br>ET-08 Fugacity from PVT data: residual integral and φ (L3 p3, p5–10)<br>ET-09 Worked example: water at 400 °C, 20 and 500 bar (L3 p2, p4, p11–12) | **write** (ET-06 drafted) | yes: isotherm sketches L2 p5 (cropped), L3 p8/p10 | **heavy** |
| ET-U2 | Activity coefficients and excess Gibbs energy | **L4 p1–15 + L5 p1–11** | Define γ → constraint (G–D) → simplest models → use one | ET-10 Non-ideal mixing and the activity coefficient (L4 p1–3, p11–12)<br>ET-11 Gibbs–Duhem and the one-constant Margules model (L4 p4–9)<br>ET-12 Asymmetric models and where parameters come from (L4 p10, p13–15; L5 p11)<br>ET-13 Worked example: O₂–Ar at 83.8 K (L5 p2–10) | **write** | yes: Sandler G^ex plots L4 p2, p9, p14; L5 p4 | **heavy** |
| ET-U3 | Measuring activity coefficients and freezing-point depression | **L5 p12–18 + L6 p1–9** | Experimental routes to γ; freezing point is the last route and is developed in full | ET-14 Measuring γ: ebulliometry, dynamic and static stills (L5 p12–17)<br>ET-15 Freezing-point depression from μ (L5 p18, L6 p2–6)<br>ET-16 Glycol–water example and eutectics (L6 p7–9) | **write** | yes: L6 p8 phase diagram | **heavy** |
| ET-U4 | Survey of activity-coefficient models | **L6 p10–15 + L7 p1–13** | All G^ex model families | ET-17 Redlich–Kister, van Laar, regular solution theory (L6 p10–13)<br>ET-18 Flory–Huggins: size asymmetry (L6 p14–15)<br>ET-19 Local composition: Wilson and NRTL (L7 p1–5)<br>ET-20 UNIQUAC, UNIFAC and choosing a model (L7 p6–13) | **write**; ET-17 full; ET-18–20 condensed (L7 p13 says they are read-only) | few | moderate |
| ET-U5 | Phase rule and constrained equilibria: osmosis, drops, bubbles | **L8 p1–14 + L9 p1–15** | Each relaxes an equilibrium condition (equal P across a membrane or a curved interface) | ET-21 Gibbs phase rule (L8 p2–8, short: mostly IB)<br>ET-22 Osmotic equilibrium (L8 p9–14)<br>ET-23 Droplets: the Kelvin equation (L9 p2–7)<br>ET-24 Bubbles, boiling and superheat (L9 p8–15) | **write** | yes: L8 p8, L9 p7, p15 | heavy |
| ET-U6 | Vapour–liquid equilibrium of real mixtures | **L10 p1–17 + L11 p1–9** | γ–φ VLE → Raoult → deviations → azeotropes → fit γ from an azeotrope | ET-25 Binary VLE diagrams (L10 p1–5)<br>ET-26 γ–φ formulation and modified Raoult (L10 p6–10)<br>ET-27 Deviations from Raoult and the azeotrope condition (L10 p11–17, L11 p6–9)<br>ET-28 Worked example: van Laar parameters from the pentane–propanal azeotrope (L11 p2–5) | **write** | **heavy**: P–x–y and T–x–y diagrams | heavy |
| ET-U7 | Solubility of gases in liquids | L11 p10–23 | One sub-topic: supercritical solute in a liquid | ET-29 Hypothetical liquid standard state and ideal solubility (p10–14)<br>ET-30 Worked example: methane solubility (p15–19)<br>ET-31 Henry's law and the Henry standard state (p20–23) | **write** | yes: p12–13 extrapolated P–T | heavy |
| ET-U8 | High-pressure VLE and retrograde behaviour | L12 p1–11 | VLE near critical points, single EOS | ET-32 VLE near critical points (p2–5)<br>ET-33 Retrograde condensation and evaporation (p6–11) | **write** (short) | **heavy**: almost all content is diagrams | light |
| ET-U9 | Solutes and electrolytes | L13 p1–9 | Molality standard state → ions | ET-34 Molality-based activity for dissolved solids (p2–3)<br>ET-35 Ionic solutions: mean ionic activity and Debye–Hückel (p4–9) | **write** | p3, p6 sketches | heavy |
| ET-U10 | Liquid–liquid equilibrium and diffusion near phase separation | **L13 p10–19 + L14 p1–11 + L15 p1–21** (spans 3 PDFs) | All rest on the curvature of G_mix(x) | ET-36 Why liquids separate: curvature of G_mix (L13 p10–19)<br>ET-37 Common tangent, consolute points and the VLE analogy (L14 p1–8)<br>ET-38 Worked example: isobutane–furfural (L14 p9–11)<br>ET-39 Binodal, spinodal and stability (L15 p1–10)<br>ET-40 Diffusion down μ, not x (L15 p11–17)<br>ET-41 Example: nitrobenzene–hexane near the consolute point (L15 p18–21) | **write** (6 notes; could split into LLE and diffusion if too long) | **heavy**: G–x and T–x sketches, data plots | heavy |
| ET-U11 | Vapour–liquid–liquid equilibrium and steam distillation | L16 p1–8 | Final course topic combining VLE and LLE | ET-42 VLLE phase diagrams (p1–6)<br>ET-43 Steam distillation (p7–8) | **write** | yes: T–x diagrams p3–5 | moderate |

Skip within units: L1 p1–6 (admin and motivation), L8 p6 (biography), L9 p11–13 (video and photo slides), L2 p10 (cartoon).

**Worked examples needing Python:** ET-09 (trapezoidal integration of the steam-table data), ET-13, ET-16, ET-28, ET-30, ET-38 (nonlinear solve for the two liquid compositions; the slides give $x_1^I=0.1128$ and $x_1^{II}=0.9284$ to verify against), ET-41.

**Watch for overlap:** ET-U6 and ET-U11 provide equilibrium foundations relevant to separation design; the supplied Separations II handouts cover absorption, drying, membranes and adsorption, rather than a dedicated distillation unit. ET-U5's osmotic section supports membrane topics. Keep the thermodynamic angle here.

---

## 2. Advanced Biotechnology

### 2.1 Inventory

Course lecturer: **Lorenzo Di Michele** (L1–6, L9–12, L15–16). Guests: **Graham Christie** (L7), **Mark Howarth** (L8), **Somenath Bakshi** (L13–14). The official outline (L1 p6–7) has L16 as a "spare lecture or revision". Format: 16:9 slides, except **L13, which is an A4 portrait 2-up handout** (19 pp, about 38 slides). No scanned PDFs. No problem sheets.

| PDF | pp | Topic | Content type |
|---|---|---|---|
| Lecture1 | 37 | Course admin; DNA/RNA structure; worm-like chain; two-state hybridisation, melting; nearest-neighbour model; hybridisation kinetics | p1–7 admin; p8–23 mechanism + figures; p25–35 derivation + worked exercise (p28–30); p37 kinetics (one slide only) |
| Lecture2 | 31 | Phosphoramidite solid-phase synthesis; yield; PCA and Gibson assembly; synthetic genomes | Mechanism (scheme figures) + short exercise (p16–17); p27–31 facts |
| Lecture3 | 37 | Sanger; Human Genome Project / shotgun; Illumina (library prep, bridge PCR, SBS) | Mechanism, step-by-step figures |
| Lecture4 | 31 | Nanopore; PacBio SMRT; market; applications of sequencing | Mechanism p5–18; p19–31 list of applications |
| Lecture5 | 37 | PCR recap; qPCR, Ct derivation, ΔΔCt; probes; RT-qPCR; aptamers and SELEX | Short derivation (p11–16) + mechanism figures |
| Lecture6 | 42 | DNA as a material (selectivity, orthogonality); junctions, tiles, origami; toehold-mediated strand displacement (TMSD) kinetics | Figure-heavy (research figures) + kinetic model (p32–39) |
| Lecture 7 | 63 | Protein structure levels and folding; X-ray crystallography; cryo-EM; NMR; AlphaFold 2/3 | Figure-heavy; **many build-up duplicates** (p12–14, 15–17, 24–31, 34–40 repeat): about 35 unique slides |
| Lecture8 | 44 | Protein engineering: antibodies, fusions, ADCs, PK/FcRn, glycosylation; site-directed mutagenesis, non-canonical amino acids; hybridoma, humanisation, phage display, IVC, transgenic mice, AI design | Fact- and figure-heavy; quiz slides |
| Lecture9 | 45 | Bioprocess overview, scale-up, downstream stages and cost; filters; dead-end filtration theory + penicillin broth example | Overview p6–33; derivation + worked example p35–45 |
| Lecture10 | 62 | Centrifuge designs; Stokes settling, tubular bowl, Σ-theory + examples; cell walls; mechanical disruption + homogeniser example | Derivation + worked examples (p27–38, p55–62); equipment figures |
| Lecture11 | 49 | Non-mechanical disruption; primary isolation: solvent and aqueous two-phase extraction, precipitation (salting out / Cohn, isoelectric, polymer, solvent) | Mechanism + worked examples (p29–30, p38–42) |
| Lecture12 | 43 | Adsorption (stages, Langmuir, Freundlich) + example; chromatography types; differential migration; gel chromatography; final isolation | Derivation + example (p16–19) + figures |
| Lecture13 | 19 (2-up) | Gene-expression kinetics, steady state; E. coli numbers; σ factors, repressors and activators, allostery, lac operon; logic of regulation | Figure-led handout, short equations (p6–7) |
| Lecture14 | 36 | Network motifs (NAR, PAR, Hill), rate plots; stochastic expression, dual reporter, intrinsic and extrinsic noise; feedback and delay; repressilator | **Figures only; almost no explanatory text** |
| Lecture15 | 47 | Cell-free TXTL (extracts, PURE); mRNA vaccine IVT manufacture; minimal cells (JCVI-syn3.0); bottom-up synthetic cells | Mechanism + facts |
| Lecture16 | 44 | "Bonus track": synthetic DNA/RNA condensates (lecturer's research) | Research showcase, quizzes; applies L1, L5, L6 |

### 2.2 Topic groupings

| Unit | Title | Sources | Why together | Short notes | Rec. | Figures | Image-equation reading |
|---|---|---|---|---|---|---|---|
| AB-U1 | Nucleic acids: structure, thermodynamics and kinetics | L1 p8–37 | Structure → hybridisation ΔG → predicting ΔG → rates | AB-01 DNA and RNA chemistry, base pairing, helices (p12–21)<br>AB-02 Polymer physics: worm-like chain (p22–23)<br>AB-03 Two-state hybridisation and melting, with exercise (p25–30)<br>AB-04 Nearest-neighbour model (p31–35)<br>AB-05 Hybridisation kinetics (p37) | **write** | yes: structures p12–19, melting curves p27 | moderate (p22, p25–34) |
| AB-U2 | Making DNA: synthesis and gene assembly | L2 p3–31 | Oligos → genes → genomes | AB-06 Phosphoramidite synthesis cycle (p6–13)<br>AB-07 Yield vs length, with exercise (p14–17)<br>AB-08 Gene assembly: PCA and Gibson (p19–26)<br>AB-09 Synthetic genomes (p27–31, short) | **write** | yes: chemistry schemes p9–12, assembly p20–26 | light |
| AB-U3a | Sequencing I: Sanger and short reads | **L3 p3–37** | Chain termination, then the massively parallel method that replaced it | AB-10 Sanger sequencing and shotgun assembly (L3 p6–17)<br>AB-11 Illumina: library prep and bridge PCR (L3 p19–28)<br>AB-12 Illumina: sequencing by synthesis (L3 p29–37) | **drafted** | **heavy**: process schematics | light |
| AB-U3b | Sequencing II: long reads and applications | **L4 p3–31** | Single-molecule platforms, then what sequencing is for | AB-13 Nanopore sequencing (L4 p5–12)<br>AB-14 PacBio SMRT + comparison table (L4 p13–19)<br>AB-15 Applications (L4 p20–31, condensed) | **drafted** | yes | light |
| AB-U4a | Quantitative PCR | L5 p3–26 | Ct, quantification protocols, probes | AB-16 qPCR: amplification curve and Ct ∝ −log ρ₀ (p6–13)<br>AB-17 Relative quantification ΔΔCt and melt curves (p14–17, p23–24)<br>AB-18 Probes (TaqMan, beacons) and RT-qPCR (p18–22, p25–26) | **drafted** | yes: amplification curves, probe schematics | moderate (p11–16) |
| AB-U4b | Aptamers and SELEX | L5 p28–37 | Distinct topic: nucleic acids as binders, not as amplicons | AB-19 Aptamers and SELEX (p28–37) | **drafted** | yes | light |
| AB-U5 | DNA nanotechnology | L6 p3–42 (+ L1 p37) | DNA as a programmable material; TMSD extends the L1 kinetics | AB-20 Why DNA is a good material: selectivity and orthogonality (p8–13)<br>AB-21 Structural DNA nanotechnology: junctions, tiles, origami (p14–30)<br>AB-22 Toehold-mediated strand displacement (p31–42) | **write** | yes: origami and junction figures | moderate (p11–12, p37–39) |
| AB-U6 | Protein structure: determination and prediction | Lecture 7 p1–63 | Sequence → structure, experimental and computational | AB-23 Levels of structure and folding (p2–10)<br>AB-24 X-ray crystallography and the phase problem (p11–32)<br>AB-25 Cryo-EM, NMR and comparison of methods (p34–43)<br>AB-26 AlphaFold 2 and 3 (p44–63) | **write** | yes; use the final build of each repeated slide | light |
| AB-U7 | Protein engineering | Lecture8 p1–44 | What to change, how to change it, how to discover binders | AB-27 What to engineer: antibodies, size, fusions, ADCs (p2–16)<br>AB-28 Antibody behaviour in the body: multimerisation, PK/FcRn, glycans, switchable (p17–22)<br>AB-29 Changing sequence: site-directed mutagenesis and non-canonical amino acids (p23–29)<br>AB-30 Generating antibodies: hybridoma → phage display → AI (p30–44) | **write** | yes | none |
| AB-U8 | Bioprocessing overview and filtration | L9 p3–45 | Upstream/downstream logic, then the first cell-removal operation | AB-31 Developing and scaling a bioprocess (p6–13)<br>AB-32 Downstream processing: stages and cost (p14–23)<br>AB-33 Filtration equipment (p25–33)<br>AB-34 Dead-end filtration theory + penicillin example (p35–45) | **write** | yes: equipment p30–33, process logic p21 | heavy (p35–45) |
| AB-U9 | Centrifugation | L10 p3–38 | Second cell-removal operation, Σ-theory | AB-35 Centrifuge designs (p6–17)<br>AB-36 Stokes settling and tubular-bowl capture (p19–29, Example 1)<br>AB-37 Σ-theory and scale-up (p30–38, Example 2) | **write** | yes: bowl and disc-stack schematics | heavy |
| AB-U10 | Cell disruption | **L10 p40–62 + L11 p3–16** (spans 2 PDFs) | Releasing intracellular product | AB-38 Cell walls and why disruption is needed (L10 p41–45)<br>AB-39 Mechanical disruption and first-order release kinetics (L10 p47–54)<br>AB-40 Homogeniser example: fitting k and α (L10 p55–62)<br>AB-41 Non-mechanical methods: physical, chemical, enzymatic (L11 p7–16) | **write** | yes | heavy (L10 p49–62) |
| AB-U11 | Primary isolation | **L11 p17–49 + L12 p3–19** (spans 2 PDFs) | The four primary-isolation operations | AB-42 Solvent and aqueous two-phase extraction + α-amylase example (L11 p19–30)<br>AB-43 Salting out and the Cohn equation + IgA example (L11 p31–42)<br>AB-44 Isoelectric, polymer- and solvent-induced precipitation (L11 p43–49)<br>AB-45 Adsorption: Langmuir/Freundlich + antibody example (L12 p5–19) | **write** | yes: breakthrough p10–11, solubility curves | heavy |
| AB-U12 | Chromatography and final isolation | L12 p20–43 | Product enrichment | AB-46 Types of liquid chromatography (p22–34)<br>AB-47 Differential migration, capacity factor and gel chromatography; HPLC/FPLC; final isolation (p35–43) | **write** | yes | moderate (p36–39) |
| AB-U13 | Gene regulation and synthetic circuits | **L13 p1–19 (2-up) + L14 p1–36** (spans 2 PDFs) | Gene-expression kinetics → regulation → motifs → noise → oscillators | AB-48 Kinetics of gene expression and steady state (L13 p5–7, p9–10)<br>AB-49 Transcriptional regulation: σ factors, repressors and activators, lac operon (L13 p11–18)<br>AB-50 Network motifs: NAR and PAR, Hill functions, rate plots (L14 p2–9, p23–28)<br>AB-51 Stochastic gene expression and noise (L14 p10–22)<br>AB-52 Feedback, delay and the repressilator (L13 p15, L14 p29–36) | **write, but flagged** (see 2.3) | **heavy**: almost all content is figures | moderate (L13 p6–7; L14 p6, p19–21 hand-annotated) |
| AB-U14 | Cell-free systems and synthetic cells | L15 p3–47 | Removing or rebuilding the cell | AB-53 Cell-free TXTL: extracts vs PURE (p6–17)<br>AB-54 mRNA vaccine manufacture by IVT (p18–21)<br>AB-55 Top-down: minimal cells (p23–31)<br>AB-56 Bottom-up: synthetic cells (p33–47) | **write** | yes: p21 process flowsheet | none |
| AB-U15 | Synthetic biomolecular condensates (bonus) | L16 p1–44 | Research showcase applying U1, U4, U5 | AB-57 (optional single note) DNA/RNA condensates, using quizzes 1 and 5 as worked examples | **write later / optional**: "spare lecture" slot, research-specific, little new theory | yes | light |

Skip within units: L1 p1–7 (admin), L4 p20 (market value), quiz slides about prices in L8 (p16, p38).

**Worked examples needing Python:** AB-03 (melting fraction), AB-07 (99.4 % coupling yield), AB-16 (Ct), AB-20 (sequence-space counts), AB-34 (penicillin filtration areas), AB-36/37 (centrifuge Q_cut, Σ, scale-up ω), AB-40 (log-linear fit of homogeniser data, then passes and pressure), AB-42 (ATPE yield), AB-43 (Cohn salting-out), AB-45 (Langmuir resin volume), AB-47 (gel chromatography K_p), AB-48 (steady-state mRNA and protein copy numbers).

### 2.3 Flags

- **AB-U13 (L13–14) is thin on text.** L14 is figures only, and L13 is a handout with short annotations. Good notes need external sources: Alon, *An Introduction to Systems Biology* (NAR, PAR, rate plots), Elowitz et al. 2002 (dual reporter, intrinsic/extrinsic noise), Elowitz & Leibler 2000 and Potvin-Trottier et al. 2016 (repressilator). **What would help:** a lecture recording, the lecturer's own notes, or the example-paper questions for these lectures, so the notes target what is examined.
- **AB-05 (hybridisation kinetics)** is a single slide. I'd fold it into AB-03, or into AB-22, where TMSD kinetics extend it.
- **Overlap with Separations II:** AB-U8 to AB-U12 provide related bioprocess separations. The supplied Separations II sources include membranes and adsorption; cross-check shared mechanisms while retaining the bioprocess angle of the completed AB notes.
- **Fact-heavy decks** (L4 p20–31, L8, L15 p33–47): I'll keep the mechanism-first rule and cut lists of examples rather than transcribe them.

---

## 3. Order of work (chronological)

The original ET → AB sequence below is a historical production record; both courses are now complete. Reaction Engineering II is the active writing course. Separations II and Process Dynamics and Control are newly planned, with their internal order listed in sections 5 and 6. This source-upload update does not start their note production or change the active course. Within each course, units follow source order, and the short notes inside each unit follow page order.

**Equilibrium Thermodynamics (L1 → L16)**

0. ET-U0 Foundations (ET-01–05): drafted (Sections 01–05)
1. ET-U1 Fugacity (ET-06–09): drafted (Sections 06–09)
2. ET-U2 Activity coefficients and excess Gibbs energy (ET-10–13): drafted (Sections 10–13)
3. ET-U3 Measuring activity coefficients and freezing-point depression (ET-14–16): drafted (Sections 14–16)
4. ET-U4 Survey of activity-coefficient models (ET-17–20): drafted (Sections 17–20)
5. ET-U5 Phase rule, osmosis, drops and bubbles (ET-21–24): drafted (Sections 21–24)
6. ET-U6 Vapour–liquid equilibrium of real mixtures (ET-25–28): drafted (Sections 25–28)
7. ET-U7 Solubility of gases in liquids (ET-29–31): drafted (Sections 29–31)
8. ET-U8 High-pressure VLE and retrograde behaviour (ET-32–33): drafted (Sections 32–33)
9. ET-U9 Solutes and electrolytes (ET-34–35): drafted (Sections 34–35)
10. ET-U10 Liquid–liquid equilibrium and diffusion (ET-36–41): drafted (Sections 36–41)
11. ET-U11 VLLE and steam distillation (ET-42–43): drafted (Sections 42–43)
12. Merge the ET units: done (notes/<subject>/<numbered topic>/, 12 files, figures copied to notes/<subject>/figs/)

**Advanced Biotechnology (L1 → L16)**

13. AB-U1 Nucleic acids: structure, thermodynamics and kinetics (AB-01–05): drafted (Sections 01–05)
14. AB-U2 Synthesis and gene assembly (AB-06–09): drafted (Sections 06–09)
15. AB-U3a Sequencing I, Sanger and short reads (AB-10–12): drafted (Sections 10–12)
15b. AB-U3b Sequencing II, long reads and applications (AB-13–15): drafted (Sections 13–15)
16. AB-U4a Quantitative PCR (AB-16–18): drafted (Sections 16–18)
16b. AB-U4b Aptamers and SELEX (AB-19): drafted (Section 19)
17. AB-U5 DNA nanotechnology (AB-20–22): drafted (Sections 20–22)
18. AB-U6 Protein structure (AB-23–26): drafted (Sections 23–26)
19. AB-U7 Protein engineering (AB-27–30): drafted (Sections 27–30)
20. AB-U8 Bioprocessing overview and filtration (AB-31–34): drafted (Sections 31–34)
21. AB-U9 Centrifugation (AB-35–37): drafted (Sections 35–37)
22. AB-U10 Cell disruption (AB-38–41): drafted (Sections 38–41)
23. AB-U11 Primary isolation (AB-42–45): drafted (Sections 42–45)
24. AB-U12 Chromatography and final isolation (AB-46–47): drafted (Sections 46–47)
25. AB-U13 Gene regulation and synthetic circuits (AB-48–52): completed and reviewed; externally supplemented and flagged as agreed.
26. AB-U14 Cell-free systems and synthetic cells (AB-53–56): completed and reviewed
27. AB-U15 Synthetic condensates (AB-57, optional): completed and reviewed
28. Group the AB small notes into chronological topic folders, with complete sections: done.

Totals: **ET** has 16 PDFs and 12 units, all drafted and merged; nothing left to write. **AB** has 16 PDFs and 15 units (14 to write, 1 optional; 56 short notes + 1 optional).

## 4. Reaction Engineering II

Added with Xavier's permission on 12 October 2026. Work follows the numbered source sections. These are section handouts, not necessarily one PDF per lecture. The initial inventory uses text to locate topics; every equation and figure used in production must subsequently be read from rendered pages.

### 4.1 Inventory and gaps

| PDF suffix | Pages | Coverage |
|---|---|---|
| 1 | 8 | Rate bases and stoichiometry; CSTR/PFR revision; heat balances; RTD; segregation and molecular mixing |
| 2 | missing | Gas–solid and liquid–solid reactions, identified by section 1's course outline; page scope unknown |
| 3 | 29 | Catalysts, preparation, zeolites, deactivation, reactor types, ideal-reactor models, diesel desulfurisation, industrial examples |
| 4 | 15 | Adsorption; Langmuir, dissociation and competition; BET; capillary condensation/hysteresis; isosteric enthalpy |
| 5 | 7 | Surface mechanisms; Langmuir–Hinshelwood, Eley–Rideal; apparent orders and activation energy; metal oxides |
| 6 | 19 | Effective diffusion; porous-pellet balances; Thiele modulus/effectiveness; disguised kinetics; external transfer; thermal effects |

Sections 7 (gas–liquid reactors) and 8 (fermenters) are mentioned in the introduction but have no supplied source PDFs. Do not present the available set as a complete course. Request missing material before writing those sections. The missing section 2 also prevents fixing the final note numbers beyond RE-06.

### 4.2 Units and chronological order

| Unit | Topic | Source pages | Short-note scope |
|---|---|---|---|
| RE-U1 | Foundations for heterogeneous reactor modelling | 1 p1–8 | RE-01 Rate bases and stoichiometry (p1–2); RE-02 Ideal CSTR and PFR balances (p3–5); RE-03 Conversion and changing gas volume (p3–4, added ideal-gas closure); RE-04 Coupled mass and energy balances (p5–6); RE-05 Residence-time distributions and tanks in series (p6–7); RE-06 Mixing and conversion (p8) |
| RE-U2 | Fluid–solid reactions with a solid reagent | 2, missing | Plan after source arrives; retain teaching order |
| RE-U3a | Catalyst materials and deactivation | 3 p1–13 | Catalysis and selectivity; metals/support preparation; solid acids/zeolites; deactivation |
| RE-U3b | Catalytic reactor types and flow models | 3 p13–25 | Fixed/moving/fluidised and three-phase beds; tanks-in-series modelling; diesel desulfurisation calculation |
| RE-U3c | Industrial catalyst examples and transport pathway | 3 p26–29 | Ethylene oxide, methanol, nitric acid; sequence of transport and surface steps |
| RE-U4a | Adsorption equilibria | 4 p1–7 | Physical/chemical adsorption; Langmuir; temperature dependence; dissociative and competitive adsorption |
| RE-U4b | Porous-solid characterisation | 4 p7–15 | BET/surface area; capillary condensation/hysteresis; isosteric enthalpy |
| RE-U5 | Surface-reaction mechanisms and apparent kinetics | 5 p1–7 | Langmuir–Hinshelwood/Eley–Rideal; apparent orders and rate optimum; activation energy; oxide mechanisms |
| RE-U6a | Diffusion in porous catalysts | 6 p1–4 | Molecular, Knudsen and surface diffusion; effective diffusivity |
| RE-U6b | Isothermal diffusion and reaction | 6 p4–13 | Slab and sphere derivations; generalised Thiele modulus; other orders/disguised kinetics; external film resistance |
| RE-U6c | Thermal effects in catalyst pellets | 6 p14–19 | Coupled thermal balance; Prater bound; external heat transfer/multiple steady states |
| RE-U7 | Gas–liquid reactors | missing | Await source |
| RE-U8 | Fermenters | missing | Await source |

Only RE-U1 numbering is fixed. Later units' short-note splits and numbers will be finalised after section 2 is available. Worked examples must be checked in Python; read all source equations visually and consult external university/textbook sources per topic. Keep short notes separate until Xavier specifies a merge group. Unit status is recorded in `other/work/BOARD.md`; “written” includes author verification but does not imply the independent cross-review has occurred.

---

## 5. Separations II

Added with Xavier's permission on 12 October 2026. The four supplied 2025 filled-note handouts are scanned, image-only PDFs. The inventory is based on their filenames, page counts and visually read opening pages; detailed note splits remain provisional until the whole handout is read. The course introduction emphasises continuous contacting and mass-transfer rates, building on earlier equilibrium-stage separations.

### 5.1 Inventory and source limits

| PDF in `other/sources/Separations II/` | Pages | Confirmed scope |
|---|---|---|
| `2025_Handout_1_Introduction + Absorption_filled notes.pdf` | 33 | Introduction and absorption; course aims include mass-transfer effects and absorption-column design |
| `2025_Handout_2_Drying_filled notes.pdf` | 34 | Drying of solids by thermal vaporisation; types of driers and wet solids |
| `2025_Handout_3_Membrane separations_filled notes.pdf` | 51 | Rate-based separation through selective membranes; feed, retentate and permeate streams; membrane structure and selectivity |
| `2025_Handout_4_Adsorption_filled notes.pdf` | 23 | Selective adsorption on porous solids; physical and chemical adsorption; adsorption-cycle introduction |

These four PDFs cover the four process areas named in the introduction. This does not establish that all course material has been supplied: no separate problem sheets or recordings are included in this inventory. Printed page numbers can differ from the PDF index (the first scanned page of handout 1 is printed page 4). Use PDF indices when recording production progress. Do not assume distillation, centrifugation or extraction units are part of this supplied set.

### 5.2 Provisional units and teaching order

**Status (12 October 2026): all four units written and independently reviewed as SEP-01–43** (U1 SEP-01–11, U2 SEP-12–22, U3 SEP-23–34, U4 SEP-35–43; 177 equations). Short notes remain separate until merge groups are chosen. The scopes below are the original provisional plan.

| Unit | Topic | Source | Provisional short-note scope |
|---|---|---|---|
| SEP-U1 | Introduction and absorption | Handout 1, 33 PDF pages | Continuous contacting versus equilibrium stages; how mass-transfer rates affect absorption performance; absorption-column design procedure and any graphical construction present in the handout |
| SEP-U2 | Drying of solids | Handout 2, 34 PDF pages | Moisture removal and wet-solid behaviour; selecting drying equipment; drying-performance calculations grounded in the handout |
| SEP-U3 | Membrane separations | Handout 3, 51 PDF pages | Selective-barrier mechanisms and membrane structure; stream definitions; flux and performance calculations using the processes actually covered |
| SEP-U4 | Adsorption | Handout 4, 23 PDF pages | Adsorbent/adsorbate distinction; physical versus chemical adsorption; adsorption cycles; gas- and liquid-system performance calculations |

Before drafting, read every page visually, identify the actual equations, examples and graphs, and replace these broad scopes with supported note splits. Lead each design calculation with its assumptions, give a reason for every graphical construction step, and verify numerical examples in Python. Relate membranes to ET osmosis and adsorption to AB primary isolation and RE adsorption equilibria without duplicating those courses' emphasis. Consult external sources per topic as required by CLAUDE.md.

### 5.3 Handwritten-source workflow

Approved by Xavier for Separations production and future reuse. The filled handouts contain printed material and handwritten equations, explanations and diagram annotations. Use the existing local PyMuPDF/Pillow tools; additional OCR is optional and never an equation authority.

1. Prepare a cached reading pack under `other/work/scratch/separations/`: original-resolution colour page images, labelled overview montages and close crops for difficult regions. Preserve the original PDFs and their hashes. Extract embedded scans where appropriate; enlarging an image cannot recover missing detail. Keep each PDF-reading batch at or below 20 pages, including for handouts longer than 20 pages. Montages locate topics; individual pages and crops establish equations.
2. Before drafting, write a page-indexed transcription/coverage record under `other/work/ocr/Separations II/`. Capture handwritten additions, equations, units, graph labels and example data. Distinguish literal source readings from independently derived corrections. Record omissions, administrative pages and source-to-note mapping so every page is accounted for.
3. Maintain a shared ambiguity register with handout, PDF page index, crop coordinates/path, competing readings, resolution, evidence and affected notes. Do not silently infer an unreadable symbol. Have another agent independently read the original crop without seeing the first transcription for difficult or consequential handwriting; compare readings before relying on them. Agreement is supporting evidence, not proof.
4. Re-derive balances and equations, check dimensions and limiting cases, and recompute every numerical example in Python. Consult and actually read external university/textbook sources for each topic. Mathematical plausibility can identify a likely correction but cannot establish what an unreadable annotation says. Refer unresolved consequential readings to Xavier.
5. Draft short notes in the established CLAUDE.md structure and pilot style. Introduce assumptions and notation, explain each design/construction step, place checked source figure crops beside their discussion, and avoid references to source pages in study notes. Keep traceability and external-source records in work files.
6. Parallelise bounded, separately owned transcription/drafting tasks. A coordinator controls final source-order note numbers and subject-wide equation numbers. Independent reviewers compare drafts with original page images, re-derive results and rerun calculations. Reuse cached images and records rather than duplicating source preparation. Resolve findings before marking units reviewed.
7. Publish GitHub reading notes and the native Obsidian mirror, check all mathematical expressions, numbering, links and figures, and validate the export after relocation. Record precisely which runtime checks were possible. Keep short notes separate until Xavier specifies merge groups.

Start with a handwriting-heavy absorption pilot to check legibility and the process before scaling. Track writing and review status in `other/work/BOARD.md`; this workflow does not itself imply a completed course or error-free transcription.

---

## 6. Process Dynamics and Control

Added with Xavier's permission on 12 October 2026. The supplied Michaelmas 2026 chapter handouts name Sebastian Ahnert as lecturer. Their text layer locates headings and examples, but flattened mathematical notation still requires visual reading before note production.

### 6.1 Inventory and gaps

| PDF in `other/sources/Process Dynamics and Control/` | Pages | Coverage |
|---|---|---|
| `PDC MT26 Ch1 v1.pdf` | 10 | Introduction; regulator/servo objectives; feedback and feedforward; control objectives; distillation and CSTR variable-identification examples; dynamic balances |
| `PDC MT26 Ch2 v1.pdf` | 32 | Dynamics of linear systems: material/energy balances; transfer functions and deviation variables; first-order lags, integrators and dead time; second-order responses; block diagrams; MIMO; poles, zeros and stability; steady-state gain; linearisation |

The chapter 1 outline identifies three later sections that are **not supplied**: section 3, Feedback Controller Design (PID, frequency response, stability and tuning); section 4, Advanced Control Systems (cascade, feedforward, ratio and nonlinear control); and section 5, Process Control Systems Design (multivariable and whole-plant control). Introductory feedback/feedforward discussion in chapter 1 does not replace these missing sections. Do not present chapters 1–2 as a complete course.

### 6.2 Provisional units and teaching order

PDC-U1–U8 were written and independently reviewed on 12 October 2026 as **PDC-01–22**, with 71 continuous equation labels. On 15 October, Xavier requested an explanation revision of all 22 notes using his preferred PDC-04 explanation as the model; its workflow and acceptance criteria are in §6.3 below and CLAUDE.md. Current revision/review status is recorded in `other/work/BOARD.md`. The scope column below preserves the original production groupings; the final numbering map is in §6.3. PDC-U9–U11 still await source. Page ranges use PDF indices.

| Unit | Topic | Source pages | Provisional short-note scope |
|---|---|---|---|
| PDC-U1 | Control objectives, variables and dynamic modelling | Ch1 p1–10 | Controlled/manipulated/disturbance variables; regulator versus servo control; feedback/feedforward intuition; distillation/CSTR examples; accumulation balances |
| PDC-U2 | Physical balances and first-order dynamics | Ch2 p1–5 | Mixing tank and thermocouple; reacting and variable-volume tanks; pulse balances; heated-liquid and discharging-gas balances |
| PDC-U3 | Transfer functions and elementary responses | Ch2 p5–11 | SISO, zero initial conditions and deviation variables; process gain/time constant; step and impulse responses; integrators; transport dead time |
| PDC-U4 | Second-order dynamics and damping | Ch2 p11–15 | Standard second-order model; poles and damping regimes; step responses; overshoot, decay ratio and oscillation period |
| PDC-U5 | Combining process elements | Ch2 p16–19 | Series blocks, delays and two-tank example; addition/subtraction of input contributions; signal duplication |
| PDC-U6 | Multiple-input multiple-output models | Ch2 p20–23 | Transfer-function matrices; boiler mass/energy balances; reacting CSTR with coupled component balances |
| PDC-U7 | Poles, zeros, stability and steady-state gain | Ch2 p23–27 | Distinct/repeated/complex poles; impulse response and stability; zeros and transient shape; final-value theorem and its validity conditions |
| PDC-U8 | Linearisation around an operating point | Ch2 p27–32 | Taylor expansion and deviation variables; first-/second-order kinetics comparison; nonlinear tank-level example; three-tank mixing process and response |
| PDC-U9 | Feedback controller design | Section 3, missing | Await source; do not fix note scope or page ranges |
| PDC-U10 | Advanced control systems | Section 4, missing | Await source; do not fix note scope or page ranges |
| PDC-U11 | Process control systems design | Section 5, missing | Await source; do not fix note scope or page ranges |

Shared boundary pages introduce the next topic and do not require duplicate notes. Lead with the physical system, derive its ODE, take the Laplace transform, then explain what the poles mean. Distinguish an integrator from a self-regulating lag and dead time from a time constant. Read source equations and plots visually, verify worked-example calculations and response curves in Python, and consult external university/textbook sources per topic. Keep short notes separate until Xavier specifies a merge group; claim writing work and record verification in `other/work/BOARD.md` when production begins.

### 6.3 Explanation revision and reproducible writing standard

Authorised by Xavier on 15 October 2026, including updates to this plan and CLAUDE.md. Apply the explanation standard in CLAUDE.md §3 within the existing seven-section note structure. The goal is to make the physical and mathematical connections explicit, retaining notation, source coverage, examples and reviewed equation numbers. The preferred PDC-04 explanation succeeds by connecting storage and two removal pathways to both a smaller endpoint and faster decay, explaining normalisation and baseline subtraction, and interpreting the worked numbers. Carry that method into each topic with its own mechanism; do not copy tank paragraphs into unrelated notes.

| Unit | Existing notes | Specific explanation to develop/check |
|---|---|---|
| PDC-U1 | PDC-01–03 | Trace disturbance → stored state → measurement → actuator; justify variable assignments and loop pairings; explain why balances need constitutive closure and why well-mixed withdrawal cancels from concentration dynamics. |
| PDC-U2 | PDC-04–07 | Expose accumulation, removal and forcing; explain normalisation and integrating factors; separate residence time from concentration time constant; use weighted pulse balances and explain internal-energy storage versus outlet enthalpy. |
| PDC-U3 | PDC-08–10 | Separate baseline subtraction from zero initial deviation; distinguish free and forced response; explain each experiment's endpoint and early shape; compare lag, ramp and transported step without conflating their timescales. |
| PDC-U4 | PDC-11–12 | Connect real/imaginary pole parts to decay/oscillation; explain why passive cascaded lags cannot oscillate; derive initial-condition weights and interpret overshoot relative to the final-value line. |
| PDC-U5 | PDC-13–14 | Follow the disturbance through each element; explain zero initial slope versus dead time, signal copying versus material splitting, compatible units at sums, and dynamic versus merely steady cancellation. |
| PDC-U6 | PDC-15–16 | Read each matrix column as a separate experiment; explain pathway zeros and conservation of A+B; connect boiler coefficient signs, integrating inventory and algebraic steam feedthrough to the reduced physical model. |
| PDC-U7 | PDC-17–19 | Explain modal decay and weights, repeated/hidden modes, competing pathways causing inverse response, and why a finite algebraic G(0) is meaningful as a final gain only when the response settles. |
| PDC-U8 | PDC-20–22 | Show constant cancellation, retained tangent terms and neglected products; explain operating-point-dependent restoring slopes; compare exact/local endpoints and explain why a repeated-lag cascade is not one lag. |

Revision procedure:

1. Read the actual short notes, existing source/progress/review records and the two supplied chapters. Reuse established source readings; visually inspect original equations or plots when a proposed change depends on them. Record the explanation gap per note before considering an addition complete.
2. Edit canonical native drafts under `other/work/drafts/Process Dynamics and Control/`, preserving original numbered results. Place reasoning where it is needed in the existing sections. An explanation must say what a result means, not merely repeat it in words. Preserve figure provenance and do not infer exact times from a sketch. State settling tolerances and use each response's own endpoint for fractions.
3. Recompute numerical claims in Python, re-derive new relationships, check units, limits and conserved totals, and obtain the independent cross-review required by AGENTS.md. Keep author verification and independent review status distinct; a previous review does not automatically cover a revision.
4. Publish with `other/work/scripts/publish_pdc.py` to the GitHub reading edition and portable native Obsidian mirror. The historical `other/work/scratch/pdc/write_notes.py` predates the revision and must not overwrite the canonical drafts. Do not create complete-section merges without a requested group.
5. Verify all revised notes, mathematical rendering, continuous labels, figures, navigation and export relocation. Record what was actually checked and any runtime limitations in `other/work/progress/`. Keep original sources and unrelated work untouched.

For future PDC chapters, apply the same method during first drafting rather than waiting for a readability revision. Missing controller-design material remains outside the supplied-source scope.

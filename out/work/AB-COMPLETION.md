# Advanced Biotechnology completion record — 9 October 2026

Completed the takeover after Claude’s usage limit: ten new short notes (AB-48–57) and seventeen merged units covering AB-01–57. AB-U13 retains the agreed flag: thin course material supplemented by outside primary sources. The optional condensates unit is included.

## Merged deliverables

Copy the seventeen Markdown files together with the adjacent `figs/` folder when uploading to Obsidian.

| File | Short notes | Scope |
|---|---|---|
| [01: Nucleic acids - structure, thermodynamics and kinetics](<../merged/Advanced Biotechnology 01 - Nucleic acids - structure, thermodynamics and kinetics.md>) | AB-01–05 | AB-U1 |
| [02: DNA synthesis and gene assembly](<../merged/Advanced Biotechnology 02 - DNA synthesis and gene assembly.md>) | AB-06–09 | AB-U2 |
| [03: Sequencing I - Sanger and short reads](<../merged/Advanced Biotechnology 03 - Sequencing I - Sanger and short reads.md>) | AB-10–12 | AB-U3a |
| [04: Sequencing II - long reads and applications](<../merged/Advanced Biotechnology 04 - Sequencing II - long reads and applications.md>) | AB-13–15 | AB-U3b |
| [05: Quantitative PCR](<../merged/Advanced Biotechnology 05 - Quantitative PCR.md>) | AB-16–18 | AB-U4a |
| [06: Aptamers and SELEX](<../merged/Advanced Biotechnology 06 - Aptamers and SELEX.md>) | AB-19–19 | AB-U4b |
| [07: DNA nanotechnology](<../merged/Advanced Biotechnology 07 - DNA nanotechnology.md>) | AB-20–22 | AB-U5 |
| [08: Protein structure - determination and prediction](<../merged/Advanced Biotechnology 08 - Protein structure - determination and prediction.md>) | AB-23–26 | AB-U6 |
| [09: Protein engineering](<../merged/Advanced Biotechnology 09 - Protein engineering.md>) | AB-27–30 | AB-U7 |
| [10: Bioprocessing overview and filtration](<../merged/Advanced Biotechnology 10 - Bioprocessing overview and filtration.md>) | AB-31–34 | AB-U8 |
| [11: Centrifugation](<../merged/Advanced Biotechnology 11 - Centrifugation.md>) | AB-35–37 | AB-U9 |
| [12: Cell disruption](<../merged/Advanced Biotechnology 12 - Cell disruption.md>) | AB-38–41 | AB-U10 |
| [13: Primary isolation](<../merged/Advanced Biotechnology 13 - Primary isolation.md>) | AB-42–45 | AB-U11 |
| [14: Chromatography and final isolation](<../merged/Advanced Biotechnology 14 - Chromatography and final isolation.md>) | AB-46–47 | AB-U12 |
| [15: Gene regulation and synthetic circuits](<../merged/Advanced Biotechnology 15 - Gene regulation and synthetic circuits.md>) | AB-48–52 | AB-U13 |
| [16: Cell-free systems and synthetic cells](<../merged/Advanced Biotechnology 16 - Cell-free systems and synthetic cells.md>) | AB-53–56 | AB-U14 |
| [17: Synthetic biomolecular condensates](<../merged/Advanced Biotechnology 17 - Synthetic biomolecular condensates.md>) | AB-57–57 | AB-U15 |

## New short notes

- [Section 48: Kinetics of gene expression and steady state](<../AB/AB-48-gene-expression-kinetics-and-steady-state.md>) — standalone short note with adjacent cropped figures.
- [Section 49: Transcriptional regulation and the lac operon](<../AB/AB-49-transcriptional-regulation-and-lac-operon.md>) — standalone short note with adjacent cropped figures.
- [Section 50: Network motifs and autoregulation](<../AB/AB-50-network-motifs-and-autoregulation.md>) — standalone short note with adjacent cropped figures.
- [Section 51: Stochastic gene expression and noise](<../AB/AB-51-stochastic-gene-expression-and-noise.md>) — standalone short note with adjacent cropped figures.
- [Section 52: Feedback, delay and the repressilator](<../AB/AB-52-feedback-delay-and-repressilator.md>) — standalone short note with adjacent cropped figures.
- [Section 53: Cell-free TXTL — extracts and PURE](<../AB/AB-53-cell-free-txtl.md>) — standalone short note with adjacent cropped figures.
- [Section 54: Manufacturing mRNA by in vitro transcription](<../AB/AB-54-mrna-manufacture-ivt.md>) — standalone short note with adjacent cropped figures.
- [Section 55: Top-down synthetic biology — minimal cells](<../AB/AB-55-minimal-cells.md>) — standalone short note with adjacent cropped figures.
- [Section 56: Bottom-up synthetic cells](<../AB/AB-56-bottom-up-synthetic-cells.md>) — standalone short note with adjacent cropped figures.
- [Section 57: Synthetic DNA and RNA condensates](<../AB/AB-57-synthetic-dna-rna-condensates.md>) — standalone short note with adjacent cropped figures.

## Verification

- 27 deliverable Markdown files rendered through Markdown and KaTeX, with 2113 mathematical expressions and no parse errors.
- All 17 merges have a single H1, one H2 per short subtopic, local continuous equation numbering, and resolving, decodable figures. Every merged figure was visually inspected; new crops were also opened individually by their writers and reviewers.
- All new numerical examples were computed in Python and independently cross-reviewed; existing worked examples in AB-34, 36, 37, 40, 42, 43, 45 and 47 were rerun. Derivations, dimensions, limiting cases and notation checked.
- New notes use the seven required sections and contain no source-document narration, wikilinks or callouts. Merged overviews and conclusions were unified; derivations and worked examples preserved except for documented corrections.
- Obsidian itself was not opened. A supplementary headless Chrome PDF-preview attempt timed out; successful Markdown/KaTeX parsing and figure inspection are the rendering evidence.

## Corrections and qualifications

- Gene-expression protein production is proportional to message abundance: the missing mRNA factor is restored. Intrinsic degradation is distinguished from growth dilution, including exact versus rounded half-life calculations.
- LacA is an acetyltransferase, not an activator of LacZ. Lac logic and the evolutionary demand rule are conditional rather than absolute.
- The condensate RNA lifetime estimate is conditional on polymerase occupancy and steady state: 20 minutes is the mean lifetime; the half-life is about 13.9 minutes. Network formation, liquid condensation and gels are distinguished.
- Cell-free and IVT claims are qualified: cleanup, oxygen dependence, capping alternatives and selective enzyme recycling depend on the chosen process. Minimal-genome counts retain their historical context; synthetic-cell architecture is not evidence of autonomous life.
- Replaced the wrong melt-curve figure in the merged qPCR unit. The pre-existing AB-17 figure was an amplification/calibration plot.
- Additional corrections to the downstream-processing merges are recorded in the unit reviews and exact merge-fixes manifest. Existing Claude-owned AB-01–47 and their original figures were not modified.

## Sources

The following logs list every external source actually opened/read, with links, page coverage, abstract-only limits and failed retrievals. Search snippets were not treated as sources. Some publisher/PMC pages were inaccessible; author manuscripts or institutional accounts were used where available.

- [codex-AB48-49-L13-20261009.md](<progress/codex-AB48-49-L13-20261009.md>)
- [codex-ab50-52-l14-20261009.md](<progress/codex-ab50-52-l14-20261009.md>)
- [codex-ab53-56-l15-20261009.md](<progress/codex-ab53-56-l15-20261009.md>)
- [codex-ab57-lecture16-20261009.md](<progress/codex-ab57-lecture16-20261009.md>)

Sources actually consulted:

- [Klumpp, Zhang & Hwa (2009), Growth-rate dependent global effects on gene expression in bacteria](https://pmc.ncbi.nlm.nih.gov/articles/PMC2818994/)
- [Zuo & Steitz (2015), Crystal structures of the E. coli transcription initiation complexes with a complete bubble](https://pmc.ncbi.nlm.nih.gov/articles/PMC5567806/)
- [Shinar et al. (2006), Rules for biological regulation based on error minimization](https://pmc.ncbi.nlm.nih.gov/articles/PMC1389706/)
- [Kuhlman et al. (2007), author manuscript of Quantitative characterization of combinatorial transcriptional control of the lactose operon of E. coli](https://arxiv.org/pdf/q-bio/0703056)
- [Andrews & Lin (1976), Thiogalactoside transacetylase of the lactose operon as an enzyme for detoxification. Publisher abstract only retrieved and read: lacA product identity and selective benefit w…](https://journals.asm.org/doi/10.1128/jb.128.1.510-513.1976)
- [Rosenfeld, Elowitz & Alon (2002), Negative Autoregulation Speeds the Response Times of Transcription Networks](https://www.weizmann.ac.il/mcb/alon/sites/mcb.UriAlon/files/nar_jmb_reprint.pdf)
- [Elowitz, Levine, Siggia & Swain (2002), Stochastic Gene Expression in a Single Cell](https://gene-quantification.de/elowitz-et-al-single-cell-2002.pdf)
- [Elowitz & Leibler (2000), A Synthetic Oscillatory Network of Transcriptional Regulators](https://www.dna.caltech.edu/courses/cs191/paperscs191/ElowitzRepressilator2000.pdf)
- [Potvin-Trottier, Lord, Vinnicombe & Paulsson (2016), Synchronous long-term oscillations in a synthetic gene circuit](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5637407/fullTextXML)
- [Riglar et al. (2019), Bacterial variability in the mammalian gut captured by a single-cell synthetic oscillator](https://www.nature.com/articles/s41467-019-12638-z)
- [AB53: Shimizu et al. (2001), original research abstract](https://www.nature.com/articles/nbt0801_751)
- [AB53 component cross-check only: PURE makes PURE (2026), original research](https://www.nature.com/articles/s41467-026-73337-0)
- [AB54: Inagaki et al. (2023), original research](https://www.nature.com/articles/s41467-023-38244-8)
- [AB54 original conceptual flowsheet provenance: Rosa et al. (2021), author manuscript](https://discovery.ucl.ac.uk/id/eprint/10124976/1/Marques_mRNA_Vaccines_Manufacturing_unmarked2.pdf)
- [AB55: Hutchison et al. (2016), author-institution publication abstract](https://www.nist.gov/publications/design-and-synthesis-minimal-bacterial-genome)
- [AB55: original investigators' institutional account](https://www.jcvi.org/media-center/first-minimal-synthetic-bacterial-cell-designed-and-constructed-scientists-venter)
- [AB56 (also clarifies AB53 energy/oxygen limits): Noireaux and Libchaber (2004), original research full text](https://www.noireauxlab.org/html%20pages/docs%20website/publications/Noireaux%20and%20Libchaber-2004.pdf)
- [Brady et al., Flexibility defines structure in crystals of amphiphilic DNA nanostars](https://arxiv.org/pdf/1810.05761)
- [Fabrini et al., Co-transcriptional production of programmable RNA condensates and synthetic organelles (2024), DOI 10.1038/s41565-024-01726-x](https://escholarship.org/content/qt87j9r3f8/qt87j9r3f8.pdf)

Additional primary sources and retrieval limits for the downstream-processing corrections are listed in the [AB-U8](reviews/AB-U8.md), [AB-U9](reviews/AB-U9.md), [AB-U10](reviews/AB-U10.md), [AB-U11](reviews/AB-U11.md) and [AB-U12](reviews/AB-U12.md) reviews. Exact corrections are recorded in [the integration review](reviews/AB-MERGE-INTEGRATION.md).

## Cross-review records

- [AB-MERGE-INTEGRATION](<reviews/AB-MERGE-INTEGRATION.md>)
- [AB-U10](<reviews/AB-U10.md>)
- [AB-U11](<reviews/AB-U11.md>)
- [AB-U12](<reviews/AB-U12.md>)
- [AB-U13-L13](<reviews/AB-U13-L13.md>)
- [AB-U13-L14](<reviews/AB-U13-L14.md>)
- [AB-U14](<reviews/AB-U14.md>)
- [AB-U15](<reviews/AB-U15.md>)
- [AB-U4a](<reviews/AB-U4a.md>)
- [AB-U8](<reviews/AB-U8.md>)
- [AB-U9](<reviews/AB-U9.md>)

## Workspace and next step

`out/PLAN.md`, `CLAUDE.md`, source PDFs, existing short notes and the Obsidian vault were left unchanged. BOARD.md records the takeover and completed statuses. Commits are local; nothing was pushed or published.

Next step: upload the merged notes and their `figs/` folder to Obsidian. Original-short-note findings remain in the reviews for their owner.

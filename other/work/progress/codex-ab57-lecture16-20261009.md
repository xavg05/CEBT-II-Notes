# Codex AB-57 — Lecture16 reading and verification

Scope: AB-57 only; Lecture16.pdf is the sole course PDF. Ownership transferred by user; BOARD, PLAN, CLAUDE and existing AB-01–47 unchanged. No commits or merges.

## Reading

Checked shared out/work/ocr and out/work/progress first: no Lecture16 transcript/progress found. Visually read all 44 pages using eight labelled PyMuPDF montages in this scratch folder; separately opened pages 12, 40 and 41 for sequence options, gel interpretation and numerical assumptions. Text layer used only to locate topics and recover text, not as a substitute for visual maths reading. Page 41 has elongation speed k=250 nt/s, length 250 nt, count approx 30000, copy number 25. No further dense mathematical pages.

Coverage: pp6–8 rationale; p11 sticky-end nanostars; p12 Quiz 1; pp13–15 amphiphilic assembly, transport, structural responsiveness; p18 size-induced internal patterning; pp19–21 reaction–diffusion and transcription/capture; pp27–30 RNA design, orthogonality and W/O expression; p33 linker control; p35 protein capture; pp38–43 preliminary E. coli expression, processing, Quiz 5 and client capture. Quizzes 2–4 mechanisms incorporated selectively rather than adding extra worked quizzes.

## External sources actually opened/read

- https://arxiv.org/pdf/1810.05761 — Brady et al., Flexibility defines structure in crystals of amphiphilic DNA nanostars; introduction and results: cholesterol micellar junctions, DNA links, crystalline/framework state, sensitivity to geometry and buffer. Abstract also opened at https://arxiv.org/abs/1810.05761 . Used for DNA mechanism and material-state qualification.
- https://escholarship.org/content/qt87j9r3f8/qt87j9r3f8.pdf — Fabrini et al., Co-transcriptional production of programmable RNA condensates and synthetic organelles (2024), DOI 10.1038/s41565-024-01726-x. Read design/condensation, orthogonality, W/O confinement, linkers, client-capture and FRAP explanation. Source exposition kept brief; most topic scope follows the supplied course PDF.

## Retrieval limitations

Nature publisher URL https://www.nature.com/articles/s41565-024-01726-x failed (internal retrieval error); full paper successfully read at UCLA URL above. PMC https://pmc.ncbi.nlm.nih.gov/articles/PMC11567899/ and https://pmc.ncbi.nlm.nih.gov/articles/PMC9523701/ returned browser-check pages. ACS https://pubs.acs.org/doi/10.1021/jacs.2c06140 and https://pubs.acs.org/jacsat/article/144/38/17468/1255645/Reaction-Diffusion-Patterning-of-DNA-Based failed to open (403); search output was not treated as a consulted full article. UCL PDF https://discovery.ucl.ac.uk/10156424/1/jacs.2c06140.pdf also failed. Reaction–diffusion explanation therefore based on visually read supplied pp19–21, with no claim that those inaccessible external copies were read. No current blocker.

## Figures

Five figures cropped by PyMuPDF at Matrix(4,4); crop coordinates and source page numbers in prepare.py. Every first crop opened; nanostar crop adjusted to remove a truncated micrograph scale bar and publication footer, gel crop expanded to preserve headings. All five final crops opened and visually inspected; the sticky-end crop was subsequently simplified to retain the full nanostar pair and remove the clipped footer, then reopened. Parent requested removal of the orphan quiz-choice reference; fixed to state simply 20 minutes for the mean lifetime.

## Verification and corrections/qualifications

prepare.py computes every example number and writes verification-output.json. Reverse complements computed explicitly: CCGATGCG is not self-complementary (CGCATCGG). Quiz 1 choice 1 is a conditional qualitative design selection, not a numerical melting prediction. Quiz 5 gives mean lifetime 1200 s = 20 min and half-life 13.8629 min, assuming stationary count, one polymerase continuously per plasmid and completed counted transcripts. These assumptions are absent from the quiz wording; no arithmetic typo corrected. Loss constant 0.000833333 s^-1; stationary residual zero and half-life remaining fraction 0.5 verified. Chemical degradation and growth dilution distinguished. Native PAGE mobility not treated as nucleotide length or proof of intact covalent RNA; nuclease identity unspecified. Work labelled submitted/in preparation in pp31/38–43 treated as preliminary, with no claim of external published confirmation.

## Static delivery checks

Seven required H2 headings; '# Section 57:' title; local equation tags sequential 1..5; all five relative PNG links resolve. No wikilinks/callouts/source-PDF or lecturer narration. Parent handles final KaTeX rendering and integrated references.

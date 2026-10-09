from pathlib import Path
import math, re, json, hashlib
import pymupdf
ROOT = Path(__file__).resolve().parents[4]
SCRATCH = Path(__file__).resolve().parent
NOTE = ROOT / 'out/AB/AB-57-synthetic-dna-rna-condensates.md'
PROGRESS = ROOT / 'out/work/progress/codex-ab57-lecture16-20261009.md'
FIGS = ROOT / 'out/AB/figs'

seqs = ['CGATCG', 'GGGGCCCC', 'CAGATCTG', 'CCGATGCG', 'CGCG']
def rc(s):
    return s.translate(str.maketrans('ACGT', 'TGCA'))[::-1]
seq_results = [{'sequence': s, 'reverse_complement': rc(s), 'length': len(s), 'gc_percent': 100*sum(c in 'GC' for c in s)/len(s), 'self_complementary': s == rc(s)} for s in seqs]
k, length, copies, count = 250.0, 250.0, 25.0, 30000.0
t_transcribe = length/k
production = copies/t_transcribe
tau = count/production
loss = production/count
half = math.log(2)/loss
assert math.isclose(tau, 1200)
assert seq_results[1]['self_complementary']
assert not seq_results[3]['self_complementary']
assert math.isclose(production-loss*count, 0)
assert math.isclose(math.exp(-loss*half), 0.5)
results = {'sticky_ends': seq_results, 'transcription_time_s': t_transcribe, 'production_nanostars_per_s': production, 'effective_loss_per_s': loss, 'mean_lifetime_s': tau, 'mean_lifetime_min': tau/60, 'half_life_min': half/60, 'steady_state_residual_per_s': production-loss*count}
(SCRATCH/'verification-output.json').write_text(json.dumps(results,indent=2)+'\n')
rows = '\n'.join(f"| `{r['sequence']}` | {r['length']} | {r['gc_percent']:.1f}% | {'Yes' if r['self_complementary'] else 'No: reverse complement is `' + r['reverse_complement'] + '`'} |" for r in seq_results)

# Figure coordinates are PDF points; preserve labels and exclude page furniture.
crops = [(11,'nanostar-sticky-ends',(20,140,350,425)), (13,'amphiphilic-frameworks',(65,65,925,465)), (21,'rna-production-and-capture',(25,105,625,412)), (27,'rna-nanostar-designs',(45,43,912,202)), (40,'rna-processing-gels',(20,60,939,466))]
doc = pymupdf.open(ROOT/'sources/Advanced Biotech/Lecture16.pdf')
for page, name, rect in crops:
    doc[page-1].get_pixmap(matrix=pymupdf.Matrix(4,4),clip=pymupdf.Rect(*rect)).save(FIGS/f'AB-57-{name}.png')

note = r'''# Section 57: Synthetic DNA and RNA condensates

## Overview

A compartment does not always need a membrane: a network of attractive molecular interactions can enrich selected molecules in a dense phase while leaving others in the surrounding solution. Synthetic DNA and RNA condensates turn this principle into a design problem: prescribe the scaffold interactions, then add binding sites and reactions to make a model organelle.

*Assumed:* nucleic-acid hybridisation, strand displacement, aptamer binding and transcription. These are research-specific platforms, rather than a universal recipe for reproducing natural organelles.

## Intuition

A **nanostar** is a branched nucleic-acid structure with several double-helical arms. A single bond joins two objects; several binding arms allow each object to join neighbours, building a network. If association becomes favourable enough to outweigh the entropy lost on concentrating the nanostars, a dense network-rich phase can coexist with a dilute solution.

*Analogy:* a gathering held together by people repeatedly joining and releasing hands. More hands and stronger grips favour a connected group. The analogy stops at the molecular physics: bonds fluctuate thermally, and a connected network need not be either a liquid or a separate phase. Networks can also become gels or ordered solids.

**Scaffold** molecules build the compartment; **clients** are recruited by affinity for that scaffold. A client can diffuse through a membrane-less boundary, so enrichment requires favourable interactions or sustained production, rather than an impermeable wall.

## Derivation

### From a sticky end to a material

For two complementary sticky ends $S$ and $S^*$, hybridisation gives $S+S^*\rightleftharpoons SS^*$. Define $\Delta G^\circ_{\mathrm{bind}}$ as the standard molar Gibbs energy change for this reaction, $R$ as the gas constant and $T$ as absolute temperature. The equilibrium constant $K$ is dimensionless because it uses activities relative to their standard states. At equilibrium, the reaction Gibbs energy vanishes:

$$
0=\Delta G^\circ_{\mathrm{bind}}+RT\ln K
\quad\Longrightarrow\quad
\ln K=-\frac{\Delta G^\circ_{\mathrm{bind}}}{RT}
\quad\Longrightarrow\quad
K=\exp\!\left(-\frac{\Delta G^\circ_{\mathrm{bind}}}{RT}\right).
\tag{1}
$$

The first rearrangement subtracts the standard free energy and divides by $RT$; exponentiating then isolates $K$. A more negative binding free energy therefore favours bonded neighbours. Sequence changes alter base pairing and stacking, while salt affects electrostatic screening.

Equation (1) describes an individual association, **not the phase boundary of the whole network**. Condensate dissolution also depends on nanostar concentration, number of arms, competing structures and whether bonds can rearrange. A duplex melting calculation alone does not predict the material's melting temperature.

### Production versus loss of an expressed RNA scaffold

Let $N(t)$ be the mean number of counted RNA nanostars per cell, $s$ their constant production rate in nanostars per second, and $\lambda$ an effective first-order loss constant in inverse seconds. Counting arrivals and departures gives

$$
\frac{dN}{dt}=s-\lambda N.
\tag{2}
$$

Each molecule has the same instantaneous loss probability per unit time in this model. At a stationary population, $dN/dt=0$, so $s=\lambda N_{\mathrm{ss}}$. Dividing by $s\lambda$ gives

$$
\tau\equiv\frac{1}{\lambda}=\frac{N_{\mathrm{ss}}}{s},
\tag{3}
$$

where $N_{\mathrm{ss}}$ is the steady-state count and $\tau$ is the mean lifetime. The units are nanostars divided by nanostars per second, giving seconds.

To see the difference from a half-life, follow a labelled cohort after its production stops. Equation (2) becomes $dN/dt=-\lambda N$. Divide by $N$ and integrate from its initial count $N_0$ at time zero:

$$
\int_{N_0}^{N(t)}\frac{dN'}{N'}=-\lambda\int_0^t dt'
\quad\Longrightarrow\quad
\ln\!\frac{N(t)}{N_0}=-\lambda t
\quad\Longrightarrow\quad
N(t)=N_0e^{-t/\tau}.
\tag{4}
$$

Here $N'$ and $t'$ are integration variables. Setting the remaining fraction to one-half gives $-t_{1/2}/\tau=\ln(1/2)=-\ln 2$, hence

$$
t_{1/2}=\tau\ln 2.
\tag{5}
$$

For a growing culture, an effective per-cell loss can include dilution through cell division as well as degradation. In that case equation (3) is an effective residence time, rather than a pure chemical degradation lifetime.

## Motivation and explanation

### DNA: separate assembly, transport and function

![Complementary sticky ends connect two DNA nanostars](figs/AB-57-nanostar-sticky-ends.png)

**Sticky-end DNA nanostars** are assembled from complementary oligonucleotides into branched junctions. Short exposed ends then bind neighbouring stars. The main arms hold the building block together while the weaker terminal bonds control inter-star association. Reversible bond exchange can allow the dense phase to flow; sufficiently persistent bonds can arrest rearrangement.

![Cholesterol-functionalised nanostars form frameworks, with different morphologies after slow and fast annealing](figs/AB-57-amphiphilic-frameworks.png)

**Amphiphilic DNA nanostars** use cholesterol groups at their arm tips. Hydrophobic groups gather into cholesterol-rich junctions, and DNA arms connect these junctions into a porous framework. Slow annealing can produce crystalline order; rapid annealing produces a different morphology. A spherical outline alone does not establish a liquid state. Arm length and framework geometry affect pore size, hence whether a client can enter, while affinity determines whether it remains enriched.

Structure can be made responsive by placing a strand-displacement site in a load-bearing connection, so an invading strand removes the bridge and breaks the network. G-quadruplex motifs provide a different control route through cation-dependent folding. Neither response applies to arbitrary DNA: the responsive motif must be incorporated into the relevant connection.

Two scaffold populations can also segregate into internal domains. In amphiphilic frameworks, differently sized nanostars can support compositionally distinct regions. Another route uses **reaction–diffusion patterning**: short patterning strands diffuse rapidly into a porous scaffold and occupy binding sites; slower, longer strands subsequently displace them near the outside. Competition between transport and strand displacement creates concentric functional domains, without requiring each shell to be a separate equilibrium liquid phase.

![A scaffold localises a transcription template in its core and RNA capture sites in its shell](figs/AB-57-rna-production-and-capture.png)

In this diagram, $B$ labels the scaffold's base binding strand, $P$ the core patterning strand, $T$ its associated transcription template, and $C$ the shell capture construct. RNA polymerase enters the framework and transcribes the core template (steps 1–2). The Broccoli RNA product diffuses outward and hybridises to capture strands in the shell (step 3). Broccoli binds the fluorogenic dye DFHBI, making the accumulated RNA visible. This spatially separates production and storage. Transcription still needs supplied ribonucleoside triphosphates, magnesium and suitable buffer ions; the scaffold itself supplies neither an enzyme nor an energy source.

### RNA: express the building block where it is needed

![T7 polymerase transcribes RNA nanostars with distinct kissing loops and fluorescent aptamers](figs/AB-57-rna-nanostar-designs.png)

A single RNA transcript can fold into a branched nanostar as it is synthesized. Hairpin tips form **kissing-loop contacts**: complementary exposed loop bases pair between different nanostars. Orthogonal loop sequences favour contacts within each designed population, supporting distinct condensates; chimeric linkers bearing both loop types tune cross-population adhesion and mixing.

In the designs illustrated, MGA is a malachite-green-binding aptamer and BrA is the Broccoli aptamer. These RNA motifs fluoresce upon binding their respective dyes. Such fluorescence reports aptamer–dye complex formation, so brightness also depends on folding and dye availability. Dye exchange can produce fluorescence recovery without rapid scaffold rearrangement.

Transcription inside water-in-oil droplets creates model organelles within synthetic cells. Protein-binding aptamers tethered to the scaffold recruit selected clients, with an aptamer-free control testing whether enrichment is specific. Genetic encoding supplies RNA synthesis; chemically installed cholesterol tags in the amphiphilic DNA platform still require external preparation.

### Expression in living cells needs structural checks

In experimental *E. coli* designs, plasmids supply nanostar templates and T7 RNA polymerase transcribes them. Binding loops enable assembly; scrambled-loop controls test whether intracellular puncta require the intended interactions. Protein-binding aptamers can additionally recruit fluorescent protein clients. These intracellular demonstrations are preliminary research examples; they do not establish a generally transferable cellular organelle platform.

![Sequencing-based cleavage map alongside denaturing and native RNA gels and labelled experimental lanes](figs/AB-57-rna-processing-gels.png)

The paired gels address different questions. **Denaturing polyacrylamide gel electrophoresis (PAGE)** disrupts base pairing and exposes the lengths of covalently continuous RNA fragments. **Native PAGE** retains more structural interactions, so mobility also reflects folding and association. Cleaved pieces could remain associated through base pairing and migrate together under native conditions. The comparison therefore motivates checking processing, rather than equating a native band or fluorescent punctum with an intact full-length nanostar. These gels alone neither identify the responsible nuclease nor measure a lifetime.

## Worked example

### Choosing stronger sticky ends

All sequences below are written from $5'$ to $3'$. Replace the original `CGATCG` end on every otherwise identical star. The replacement must pair with **another copy of itself**, which requires equality with its reverse complement. Python verifies the sequence lengths, GC fractions and complementarity:

| Sticky end | Length (nt) | GC fraction | Self-complementary? |
|---|---:|---:|---|
__ROWS__

**`GGGGCCCC` is the best initial choice among these options:** it is longer than the original, entirely GC and self-complementary. `CAGATCTG` preserves self-complementarity but adds AT-rich sequence; its stability should be assessed with a nearest-neighbour model. `CCGATGCG` has substantial GC content but cannot make a fully matched duplex with an identical copy. `CGCG` is self-complementary but shorter, so GC percentage alone is insufficient grounds for choosing it.

This is a design judgement at comparable salt, concentration and scaffold geometry, not a calculated melting temperature. Self-folding, alternative association and slower bond exchange could undermine the intended benefit; a measured phase diagram must confirm it.

### Estimating the lifetime of an expressed nanostar

Take a T7 polymerase elongation speed $k=250\ \mathrm{nt\,s^{-1}}$, RNA length $L=250\ \mathrm{nt}$, plasmid copy number $n_p=25$, and stationary count $N_{\mathrm{ss}}\approx30{,}000$ nanostars per cell.

**Additional assumptions:** each plasmid has one active polymerase continuously making completed transcripts, with negligible initiation delay; each completed transcript contributes one counted nanostar; production balances first-order loss. Elongation speed and plasmid count alone do not establish the actual initiation rate or polymerase occupancy.

One transcript takes $t_{\mathrm{tx}}=L/k=1.00\ \mathrm{s}$, because its length is divided by the nucleotide addition rate. Under the assumed occupancy, production is $s=n_p/t_{\mathrm{tx}}=25.0$ nanostars per second. Substitution into equation (3) gives

$$
\tau=\frac{30{,}000\ \text{nanostars}}{25.0\ \text{nanostars}\,\mathrm{s^{-1}}}
\approx1{,}200\ \mathrm{s}=20.0\ \mathrm{min}.
$$

The Python calculation gives **20 minutes** for the mean lifetime. Equation (5) gives a half-life of approximately **13.9 minutes**, so the two quantities must not be interchanged. Reduced initiation, multiple simultaneous polymerases per template, incomplete transcripts, processing or growth dilution change the inference. Without steady state, population size divided by production is an accumulation timescale rather than a measured molecular lifetime.

## Link to other topics

Hybridisation and strand displacement become material assembly and spatial patterning tools here, while aptamers turn sequence-defined binding into selective client recruitment. Expressed RNA scaffolds connect cell-free transcription and synthetic-cell construction to the same production–loss balance used for gene-expression kinetics.

## Conclusion

The design proceeds from scaffold assembly to material state, transport and client binding. DNA offers externally prepared frameworks with programmable connections; RNA adds in situ production, alongside folding and turnover constraints. Functional compartmentalisation requires checking each of these mechanisms rather than inferring an organelle from a fluorescent spot.
'''.replace('__ROWS__', rows)
NOTE.write_text(note)

progress = '''# Codex AB-57 — Lecture16 reading and verification

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
'''
PROGRESS.write_text(progress)

# Low-impact document validation; deliberately limited to this deliverable.
assert re.findall(r'^## (.+)$',note,re.M)==['Overview','Intuition','Derivation','Motivation and explanation','Worked example','Link to other topics','Conclusion']
assert [int(x) for x in re.findall(r'\\tag\{(\d+)\}',note)] == list(range(1,6))
assert not re.search(r'\[\[|^>|lecture|slides|lecturer|source PDF',note,re.I|re.M)
links = re.findall(r'!\[[^\]]*\]\(([^)]+)\)',note)
assert len(links)==5
for link in links:
    path=NOTE.parent/link
    assert path.is_file()
    pix=pymupdf.Pixmap(path)
    assert pix.width>0 and pix.height>0
validation={'file':str(NOTE.relative_to(ROOT)),'headings':7,'equation_tags':[1,2,3,4,5],'valid_figure_links':links,'source_pdf_sha256':hashlib.sha256((ROOT/'sources/Advanced Biotech/Lecture16.pdf').read_bytes()).hexdigest(),'words':len(note.split()),'parent_katex_render_pending':True}
(SCRATCH/'validation-output.json').write_text(json.dumps(validation,indent=2)+'\n')
print(json.dumps(results,indent=2))
print(json.dumps(validation,indent=2))

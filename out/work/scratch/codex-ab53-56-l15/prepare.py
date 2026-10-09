from pathlib import Path
import pymupdf, re, math, json, hashlib

ROOT=Path(__file__).resolve().parents[4]
BASE=ROOT/'out/work/scratch/codex-ab53-56-l15'
AB=ROOT/'out/AB'
PROGRESS=ROOT/'out/work/progress/codex-ab53-56-l15-20261009.md'
import sys
if '--finalize' in sys.argv:
    d=pymupdf.open(ROOT/'sources/Advanced Biotech/Lecture15.pdf')
    d[24].get_pixmap(matrix=pymupdf.Matrix(4,4),clip=pymupdf.Rect(523,77,941,424)).save(AB/'figs/AB-55-design-build-test.png')
    p=AB/'AB-54-mrna-manufacture-ivt.md'
    s=p.read_text().replace('Follow the stream through IVT, purification, capping and final formulation.', 'Follow the stream through IVT, purification, capping and final formulation. In the diagram, VCC denotes vaccinia capping enzyme; the methyl donor supplies the cap-methylation reaction.')
    p.write_text(s)
    p=AB/'AB-56-bottom-up-synthetic-cells.md'
    s=p.read_text().replace('Let $c_i$ and $c_o$ be internal and external substrate concentrations,', 'Let $t$ denote elapsed time, $c_i$ and $c_o$ internal and external substrate concentrations,')
    p.write_text(s)
    s=PROGRESS.read_text().replace('(519, 77, 941, 424)', '(523, 77, 941, 424)')
    s+='\n## Final visual and file inspection\n\nOpened and read all four saved Markdown files. Opened all seven PNG crops individually with view_image; diagram labels and original scale bars are legible. A small neighbouring-text fragment at the left edge of the AB55 design cycle was removed by tightening its crop to x=523; revised crop must be reopened before delivery. Defined elapsed time explicitly in the transport balance and expanded VCC in the manufacturing figure discussion. All numerical answers retain Python-derived values. Parent handles KaTeX rendering and integration.\n'
    PROGRESS.write_text(s)
    import re
    for p in sorted(AB.glob('AB-5[3-6]-*.md')):
        s=p.read_text(); tags=[int(x) for x in re.findall(r'\\tag\{(\d+)\}',s)]
        assert tags==list(range(1,len(tags)+1))
        assert len(re.findall(r'^## ',s,re.M))==7
        assert not re.search(r'lecture|lecturer|slides|\.pdf|\[\[|^>\s*\[!',s,re.I|re.M)
        for link in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',s): assert (p.parent/link).is_file()
    print('Final edits and structural checks complete; reopen revised AB55 crop.')
    sys.exit(0)

protected=[ROOT/'CLAUDE.md',ROOT/'out/PLAN.md',ROOT/'out/work/BOARD.md']+[p for p in AB.glob('AB-*.md') if int(p.name.split('-')[1])<=47]
baseline={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in protected}
(BASE/'protected-hashes.json').write_text(json.dumps(baseline,indent=2)+'\n')

# Every numerical calculation appearing in the notes is performed here.
results={
 'AB54_capped_mg':100*0.90,
 'AB54_purified_mg':100*0.90*0.80,
 'AB54_formulated_mg':100*0.90*0.80*0.95,
 'AB54_overall_percent':100*0.90*0.80*0.95,
 'AB55_gene_sum':438+35,
 'AB55_unknown_percent':100*149/473,
 'AB56_tau_5um_s':5e-6/(3*1e-8),
 'AB56_tau_10um_s':10e-6/(3*1e-8),
 'AB56_tau_ratio':(10e-6/(3*1e-8))/(5e-6/(3*1e-8)),
 'AB56_steady_5um_mM':1.0-(5e-6*1e-3/(3*1e-8)),
 'AB56_steady_10um_mM':1.0-(10e-6*1e-3/(3*1e-8)),
}
assert results['AB55_gene_sum']==473
assert math.isclose(results['AB54_formulated_mg'],68.4)
assert math.isclose(results['AB56_tau_ratio'],2)
# Limiting cases and substitution back into the membrane balance.
for radius in [5e-6,10e-6]:
 permeability=1e-8
 q=1e-3 # mM/s: illustrative constant volumetric substrate consumption
 steady=1-radius*q/(3*permeability)
 assert math.isclose(3*permeability/radius*(1-steady),q,rel_tol=1e-12)
assert 3*1e-8/5e-6*(1-1)==0 # equal concentrations: no net passive influx
assert 1-5e-6*0/(3*1e-8)==1 # no consumption: concentrations equilibrate
(BASE/'verification-output.json').write_text(json.dumps(results,indent=2)+'\n')

notes={}
notes['AB-53-cell-free-txtl.md']=r'''# Section 53: Cell-free TXTL — extracts and PURE

## Overview

Cell-free transcription–translation (TXTL) makes proteins by operating the gene-expression machinery outside living cells. A crude extract retains much of the cytoplasm; PURE reconstructs the machinery from purified components. Both let us change the expression template directly, but require externally supplied materials and energy.

*Assumed:* transcription, translation and the roles of ATP, ribosomes and transfer RNA.

## Intuition

A cell is both a production plant and a system that maintains the plant. Cell-free expression keeps the production equipment while handing maintenance to the engineer: buffers control the environment, and added substrates support biosynthesis. A toxic product can therefore be made without requiring a host to keep growing, provided it does not inhibit the extracted machinery itself.

*Analogy:* operating machinery removed from a factory. The limit is that molecular machines continually degrade and share reagents; taking away the factory also removes repair, compartmentalisation and much of metabolic regulation.

## Derivation

The mechanism runs from DNA to mRNA to polypeptide, then folding. Each stage requires something different, so supplying DNA alone cannot sustain expression.

**Transcription.** RNA polymerase recognises a compatible promoter and uses nucleoside triphosphates (NTPs) to extend RNA. Magnesium supports catalysis. The promoter and polymerase must match; a bacterial extract can use endogenous polymerase, or a supplied polymerase such as T7 with its own promoter.

**Translation.** Aminoacyl-tRNA synthetases use ATP to attach each amino acid to its matching transfer RNA (tRNA). The ribosome recognises codon–anticodon pairs and transfers the growing peptide to the incoming aminoacyl-tRNA. Initiation, elongation, release and recycling factors coordinate the cycle; GTP supports delivery and translocation. Energy comes from activated substrates and nucleotide hydrolysis, rather than from the peptide bond spontaneously forming between free amino acids.

**Maintaining activity.** Added amino acids and NTPs supply material; energy substrates and regeneration enzymes replenish usable nucleotide triphosphates. Salt, magnesium, pH and sometimes crowding agents support the machinery. Reagent depletion, inhibitory by-products and degradation eventually stop a closed batch.

**Extract route.** Grow source cells, disrupt them, and clarify the lysate to remove intact cells and coarse debris while retaining ribosomes and soluble factors. Endogenous nucleic-acid activity is reduced by preparation-dependent treatments; clarification alone does not guarantee removal of all cellular DNA or mRNA. Add the chosen template and supplement the reaction. Bacterial, yeast, wheat-germ and rabbit-reticulocyte preparations differ in translation and processing capabilities.

![Cell extract supplemented with a DNA template and reaction components](figs/AB-53-extract-preparation.png)

**PURE route.** Protein synthesis Using Recombinant Elements combines individually purified synthetases, translation factors and energy-regeneration enzymes with ribosomes, tRNAs and small molecules. A representative formulation contains 36 non-ribosomal proteins; the exact set depends on the formulation. For TXTL from DNA, include a compatible RNA polymerase. Purified components give control over omissions and concentrations; they do not mean that every component, including the ribosome, is a single recombinant protein.

## Motivation and explanation

| Choice | What is gained | What must be managed |
|---|---|---|
| Crude extract | Inherited cofactors, enzymes and metabolic capacity; comparatively economical preparation | Batch variation, background reactions, nucleases and proteases |
| PURE | Defined composition and targeted removal or replacement of factors | Many separate purification steps, cost and limited auxiliary functions |

Extracts often offer higher practical protein yields than a basic PURE mixture, but yield depends on the protein, formulation and operating mode. Membrane proteins need an appropriate membrane mimic or lipid compartment; folding and post-translational processing may need extra machinery.

Changing DNA avoids a new host-engineering cycle for each product. It also supports automation, linear templates and, in suitable preparations, freeze-dried storage. Linear DNA may need protection against nucleases. Cell-free production removes growth and harvest from the expression stage, but source-cell cultivation and disruption are still needed to prepare extracts. Purification must still separate product from enzymes, nucleic acids and other impurities. Product-specific quality and safety requirements remain, and oxygen transfer can still matter when energy regeneration uses respiration.

## Worked example

Suppose a protein must contain a non-canonical amino acid at a chosen stop codon. In a defined PURE mixture, omit the release factor that normally recognises that codon and supply a suitably charged suppressor tRNA. The tRNA now competes successfully to insert the desired amino acid where termination would otherwise occur.

![Purified components assembled into a transcription–translation reaction](figs/AB-53-pure-components.png)

This works only if the remaining factors support elongation and the product has a separate, effective termination route. Removing a release factor alone supplies neither the unusual amino acid nor its correctly charged tRNA. An extract is harder to control because endogenous release factors and competing reactions remain.

## Link to other topics

Cell-free systems reuse the transcription and translation mechanisms of gene regulation while exposing resource competition directly to experimental control. Their preparation uses cell disruption and clarification, whereas their products still need downstream purification.

## Conclusion

Extracts preserve biochemical breadth; PURE trades that breadth for control. The same separation of machinery from living cells also allows RNA to be manufactured without translating it into protein.
'''
notes['AB-54-mrna-manufacture-ivt.md']=r'''# Section 54: Manufacturing mRNA by in vitro transcription

## Overview

In vitro transcription (IVT) makes mRNA from a DNA template in a cell-free enzyme reaction. The product is RNA, so translation is deliberately absent during manufacture. A useful vaccine message must also have appropriate end structures, survive purification and reach the recipient cell's cytoplasm.

*Assumed:* template-directed transcription, nucleic-acid base pairing and downstream separation principles.

## Intuition

Manufacture the instruction rather than the antigen: a recipient cell later translates the delivered mRNA into protein. The production problem therefore shifts from folding and purifying an antigen to controlling RNA sequence, integrity, end chemistry and impurities.

*Analogy:* printing an instruction sheet with protective covers and a delivery envelope. The limit is that a cap and poly(A) tail actively recruit cellular proteins; they are more than packaging, and RNA impurities can change how the immune system responds.

## Derivation

**Template and polymerisation.** Prepare DNA containing a promoter recognised by the selected polymerase, followed by the RNA sequence. A linear template provides a defined run-off endpoint; a plasmid can be linearised or the required region amplified. T7 RNA polymerase uses ATP, CTP, GTP and UTP as building blocks, with magnesium as a catalytic cofactor. A buffer controls pH, and polyamines such as spermidine can support transcription under suitable conditions.

The RNA's terminal hydroxyl attacks the incoming NTP's phosphate, forming a phosphodiester bond and releasing pyrophosphate. Repeated template-directed addition produces RNA while leaving the DNA available for further transcription. This mixture needs no ribosomes or amino acids because it does not make protein.

**End structures.** The message comprises a cap, untranslated regions (UTRs), a coding sequence and a poly(A) tail. The UTRs affect stability and translation. The 5′ cap contains a methylated guanosine joined through an unusual 5′–5′ triphosphate linkage; it supports translation initiation and resistance to degradation. The tail recruits poly(A)-binding proteins and supports stability and translation.

Two capping routes are possible. Post-transcriptional capping treats the RNA with capping enzymes: removal of the terminal phosphate, addition of guanosine and methylation build the cap, with additional methylation where required. Co-transcriptional capping introduces a suitable cap analogue during initiation. The latter can remove the separate capping reactor, but requires compatible template and reaction design. The poly(A) tail can be encoded in the template or added afterwards by template-independent poly(A) polymerase.

**Purification and formulation.** Remove residual DNA, enzymes, unused NTPs and aberrant RNA, including truncated or double-stranded species. DNA digestion reduces the template to smaller fragments that subsequent operations can remove. Tangential-flow filtration concentrates or exchanges buffer where its membrane retains the RNA and passes smaller solutes. Chromatography adds selectivity: ion exchange exploits charge, size exclusion exploits hydrodynamic size, and oligo(dT) affinity captures a poly(A) tail through base pairing. Tail capture alone does not prove that an RNA has the correct cap or intact coding region.

Finally, formulate the purified message for delivery, for example in lipid nanoparticles. Their job includes RNA protection and cytoplasmic delivery; producing pure RNA alone does not accomplish either.

## Motivation and explanation

The architecture makes IVT adaptable: change the coding sequence while retaining much of the manufacturing platform. However, a new sequence can change secondary structure, reaction behaviour and impurity formation, so the recipe is not automatically transferable without optimisation.

Double-stranded RNA and uncapped or damaged transcripts can alter innate sensing and reduce useful translation. Total RNA mass is therefore not the same as acceptable product mass. A selective separation train is needed even though no cells are present in the IVT reactor.

The process below includes proposed enzyme-recycling loops. These require a separation that recovers active enzyme without unacceptable product carryover. Ordinary ultrafiltration may retain both enzyme and long RNA; the presence of a filtration step does not by itself establish selective recycling. The diagram is a conceptual process, rather than a universal manufacturing recipe.

## Worked example

![Conceptual manufacturing train: IVT, intermediate purification, separate enzymatic capping, further purification and formulation](figs/AB-54-ivt-process.png)

Follow the stream through IVT, purification, capping and final formulation. A hypothetical batch starts with $m_0=100\,\mathrm{mg}$ of intact target RNA. Let $f_c=0.90$ be its correctly capped fraction, $y_p=0.80$ the recovery of that fraction in purification, and $y_f=0.95$ its recovery in formulation. Assume these fractions are measured for the target population, with no additional degradation; neglect the small cap mass increase.

By the definition of capped fraction, the available capped RNA is $m_c=m_0f_c$. Recovery is the fraction of the incoming target retained, so purified RNA is $m_p=m_cy_p$. Applying the same definition at formulation gives $m_f=m_py_f$. Substitution eliminates the intermediate masses:

$$m_f=m_0f_cy_py_f. \tag{1}$$

Python gives $m_c=90.0\,\mathrm{mg}$, $m_p=72.0\,\mathrm{mg}$ and $m_f=68.4\,\mathrm{mg}$: an overall recovery of $68.4\%$ relative to the initial target RNA. These are illustrative inputs, not measured process performance. All factors are dimensionless, so the final mass retains the units of $m_0$; if any factor vanishes, acceptable recovered product also vanishes.

## Link to other topics

IVT reuses DNA assembly and transcription, but stops before the translation stage of TXTL. Its purification applies the filtration, chromatography and nucleic-acid recognition mechanisms already used elsewhere in bioprocessing.

## Conclusion

mRNA manufacture couples template-directed synthesis to end processing, selective purification and delivery. Removing cells simplifies the reaction environment while leaving product quality and separation as central engineering problems.
'''
notes['AB-55-minimal-cells.md']=r'''# Section 55: Top-down synthetic biology — minimal cells

## Overview

Top-down synthetic biology modifies a living system, often deleting genes to reduce complexity. JCVI-syn3.0 demonstrates that a much smaller genome can support continued cellular growth, but its minimum is conditional on the medium, genetic background and acceptable growth rate.

*Assumed:* genome assembly, gene expression and the distinction between genotype and phenotype.

## Intuition

A bacterium carries genes for both routine operation and coping with changing conditions. Supplying a stable, nutrient-rich environment can make some functions dispensable: the medium replaces tasks that the cell would otherwise perform itself.

*Analogy:* stripping a vehicle to essentials for one controlled track. The limit is that genes form interacting networks, so removing two individually dispensable parts can eliminate a shared function. A reduced cell also continues to maintain and reproduce its machinery rather than merely running once.

## Derivation

There is no universal gene-count equation for life. The minimal set is inferred by a design–build–test loop that asks whether a reduced genome supports a specified phenotype.

**Define the test.** Specify growth conditions and the criterion for success. Viability, robust population growth and regular division are different endpoints. Mycoplasma already have reduced genomes and depend strongly on nutrients supplied by their surroundings. Host association can relax selection for some biosynthetic functions; it does not remove all environmental challenges or adaptation.

**Perturb genes.** Transposon insertion disrupts genes. Mutants recovered after growth show that a disruption is tolerable under those conditions; failure to recover insertions suggests essentiality, subject to insertion biases and experimental limitations. Comparing mutant abundance over passages also exposes fitness defects that a single survival test can miss. Bioinformatics identifies conserved machinery and suggests functions, but prediction alone cannot establish dispensability.

**Distinguish growth requirements.** Essential genes cannot be removed while retaining the tested viability. Quasi-essential genes permit some survival when disrupted but are needed for sufficiently robust growth. Non-essential genes can be removed under the specified conditions. These categories change with environment and with the remaining genome. Two alternative pathways can each be dispensable alone, yet deleting both is lethal: single-gene tests do not prove that all tolerated deletions can be combined.

**Build and test the combined design.** Design reduced genome segments, synthesise DNA, assemble and clone the genome, and transplant it into a recipient cell. Its existing cytoplasm supplies the initial machinery that lets the transplanted genome take control. Test outgrowth and phenotype, then restore or revise deleted regions if the design fails. Segment-level tests help locate incompatible deletions before final assembly.

![Design–build–test cycle: genome design and synthesis, assembly, transplantation, outgrowth and phenotype measurement](figs/AB-55-design-build-test.png)

JCVI-syn1.0, a synthetic genome based on Mycoplasma mycoides, provided the starting point; its faster growth made iterative testing more practical than using the much slower M. genitalium. Genome minimisation yielded JCVI-syn3.0 after repeated redesign and retention of quasi-essential functions. Chemically synthesising the genome does not change the top-down logic: its organisation is derived from a natural cell, and the experiment relies on an existing recipient cytoplasm.

## Motivation and explanation

The retained functions must form a sustainable loop. Expression machinery produces proteins and functional RNAs; replication and maintenance preserve genetic information; cytosolic metabolism supplies usable substrates and energy; the membrane retains components and mediates exchange with the nutrient-rich medium. Simplifying biosynthesis can increase dependence on transport, so a small genome does not make the membrane unimportant.

A minimal cell exposes gaps in knowledge because genes can be necessary without their precise biological roles being known. It also offers a simpler chassis for experiments. Simplicity is not automatically industrial performance: slow growth, poor robustness and irregular morphology can offset the reduced genetic complexity.

## Worked example

JCVI-syn3.0 contains 473 genes, comprising 438 protein-coding genes and 35 RNA genes. Python verifies that the two classes sum to 473. In the original characterisation, 149 genes lacked a specific biological function. Defining $f_u$ as the fraction of all retained genes in this class gives

$$f_u=\frac{149}{473}\approx0.315=31.5\%. \tag{1}$$

The denominator includes RNA genes as well as protein-coding genes: changing it would answer a different question. Broad functional classification can still be possible without a specific mechanistic assignment, so a chart's wholly unassigned category need not equal this fraction. The historical count is not a claim that all these functions remain unknown.

![Growth and morphology comparison of JCVI-syn1.0 and JCVI-syn3.0, retaining the original panel labels and scale bars](figs/AB-55-growth-morphology.png)

The phenotype reveals another limit. JCVI-syn3.0 has roughly a three-hour doubling time under its studied conditions and irregular, heterogeneous cell shapes. Sustained replication therefore does not imply normal morphology or an efficient, uniform division cycle. No additional numerical values are inferred from the plotted curves.

## Link to other topics

Minimal-cell construction extends oligonucleotide synthesis and genome assembly from making DNA to testing whether a whole genome sustains a phenotype. It also shows why regulation, transport and metabolic redundancy affect the consequences of gene deletion.

## Conclusion

A minimal genome is an experimentally tested set for a particular environment and growth criterion. Bottom-up synthetic cells take the complementary route: assemble selected cellular functions from components rather than reducing an inherited living system.
'''
notes['AB-56-bottom-up-synthetic-cells.md']=r'''# Section 56: Bottom-up synthetic cells

## Overview

Bottom-up synthetic cells assemble non-living components into compartments that reproduce selected cellular functions. A synthetic cell can sense, communicate or synthesise a product without being a fully autonomous organism. Its engineering problem is to couple structure, molecular machinery and information processing while maintaining material and energy exchange.

*Assumed:* membrane transport, reaction balances and cell-free gene expression.

## Intuition

Confinement puts a biochemical programme in a defined location. It can retain expensive machinery, separate incompatible reactions and establish an inside and outside. But the same barrier that prevents machinery escaping can prevent fresh substrates entering.

*Analogy:* a miniature chemical plant with a wall, machinery and control system. The limit is that each part may be assembled rather than self-produced, and molecular fluctuations, membrane mechanics and osmotic effects become important at this scale.

## Derivation

**Structure.** Lipid vesicles enclose aqueous reaction mixtures with a bilayer. Polymer membranes can offer different mechanical stability and permeability; protein or particle assemblies provide other boundaries. Giant unilamellar vesicles are commonly about $1$–$100\,\mu\mathrm{m}$ across, large unilamellar vesicles about $0.1$–$1\,\mu\mathrm{m}$, and small ones below about $0.1\,\mu\mathrm{m}$. These are approximate size categories; unilamellar means one bilayer. Internal compartments can organise distinct pathways as synthetic organelles.

![Compartment architecture with an outer boundary and internal compartments made from different materials](figs/AB-56-compartment-architecture.png)

**Machinery and information.** Encapsulated TXTL converts a DNA programme into functional proteins. Enzymes catalyse transformations; pores mediate exchange; receptors and regulatory circuits connect inputs to outputs. Synthetic nucleic-acid structures or nanomaterials can supplement biological components. A minimal sensing chain is external input, molecular recognition, changed internal reaction or gene expression, and an observable output. Each connection must be physically implemented; a compartment alone has no sensing programme.

**Exchange constraint.** Consider a spherical vesicle of fixed radius $R$ and volume $V$, with surface area $A$. Let $c_i$ and $c_o$ be internal and external substrate concentrations, $\mathcal P$ its effective membrane permeability, and $q$ the positive volumetric consumption rate inside. Assume a well-mixed interior, a large external reservoir holding $c_o$ constant, passive linear transport, and a thin membrane with transport resistance included in $\mathcal P$.

The inward flux per area is $J=\mathcal P(c_o-c_i)$. Multiplying by area gives the entry rate; multiplying consumption by volume gives the removal rate. Conservation therefore gives

$$V\frac{dc_i}{dt}=A\mathcal P(c_o-c_i)-Vq. \tag{1}$$

Divide by the fixed volume. For a sphere, $A=4\pi R^2$ and $V=4\pi R^3/3$, so cancelling $4\pi R^2$ gives $A/V=3/R$. Thus

$$\frac{dc_i}{dt}=\frac{3\mathcal P}{R}(c_o-c_i)-q. \tag{2}$$

For constant $q$, set the accumulation to zero and rearrange: $(3\mathcal P/R)(c_o-c_i^*)=q$, then $c_o-c_i^*=Rq/(3\mathcal P)$. Hence

$$c_i^*=c_o-\frac{Rq}{3\mathcal P}. \tag{3}$$

The star denotes the steady concentration. A negative result means the assumed consumption cannot be sustained; it is not a physically negative concentration. With no consumption, the coefficient of concentration relaxation in equation (2) is $3\mathcal P/R$, giving an exchange time scale $\tau=R/(3\mathcal P)$. Since permeability has units of length per time, $\tau$ has units of time. A completely impermeable membrane supplies no substrate through this mechanism.

## Motivation and explanation

Pores can admit small nutrients while retaining ribosomes and other large components, allowing an encapsulated TXTL reaction to last longer. Expression of a pore can itself improve supply, linking gene expression to boundary function. Oxygen requirements and osmotic balance still need attention; increased internal solute concentration can draw in water and rupture a vesicle.

Membrane-less compartments use selective partitioning instead of a bilayer. Liquid–liquid phase separation enriches compatible proteins or nucleic acids in a dense phase while excluding others. Molecules still exchange with the surroundings, and enrichment need not improve catalysis if substrates are excluded or enzymes become inactive. Hydrogels and cross-linked networks are other membrane-less architectures, but are not necessarily liquid condensates. Neither greater robustness nor faster dynamics is universal across these materials.

## Worked example

Take illustrative values $c_o=1.0\,\mathrm{mM}$, $\mathcal P=10^{-8}\,\mathrm{m\,s^{-1}}$ and $q=10^{-3}\,\mathrm{mM\,s^{-1}}$. For radii of $5\,\mu\mathrm{m}$ and $10\,\mu\mathrm{m}$, Python gives exchange time scales of approximately $167\,\mathrm{s}$ and $333\,\mathrm{s}$, and steady substrate concentrations of approximately $0.833\,\mathrm{mM}$ and $0.667\,\mathrm{mM}$. Doubling the radius doubles the exchange time and increases depletion at the same volumetric demand. These are model examples, not measurements from an image; concentration-dependent consumption and changing vesicle volume require a fuller model.

![Microscopy image of a compartment containing distinct red and cyan internal domains; the original 50 micrometre scale bar is retained](figs/AB-56-synthetic-organelles.png)

The image illustrates spatial organisation within an enclosing compartment. It does not alone establish selective transport, replication or autonomous metabolism. Such functions require separate measurements: for example, substrate entry, product generation and boundary integrity over time.

## Link to other topics

Synthetic cells combine cell-free expression, membrane transport and regulatory circuits in a confined setting. Membrane-less organelles connect their design to phase separation and programmable nucleic-acid materials.

## Conclusion

Bottom-up construction tests which combinations of parts are sufficient for a chosen function. It supports studies of confined expression, signalling and membrane mechanics, and offers candidate platforms for delivery, manufacturing and remediation; these proposed applications require function-specific validation. Origin-of-life models add a separate constraint: components and assembly pathways must also be plausibly prebiotic, rather than relying on modern ribosomes and enzymes.
'''

for name,body in notes.items():
 p=AB/name
 assert not p.exists(), f'Refusing to overwrite existing note {p}'
 p.write_text(body)

# All deliverable crops come from Lecture15.pdf, use PyMuPDF at 4x.
d=pymupdf.open(ROOT/'sources/Advanced Biotech/Lecture15.pdf')
crops=[
 ('AB-53-extract-preparation.png',11,(575,82,914,457)),
 ('AB-53-pure-components.png',12,(530,183,952,402)),
 ('AB-54-ivt-process.png',21,(10,376,922,532)),
 ('AB-55-design-build-test.png',25,(519,77,941,424)),
 ('AB-55-growth-morphology.png',31,(426,62,903,478)),
 ('AB-56-compartment-architecture.png',41,(565,142,954,441)),
 ('AB-56-synthetic-organelles.png',47,(474,79,952,520)),
]
for name,page,rect in crops:
 p=AB/'figs'/name
 assert not p.exists(), f'Refusing to overwrite existing figure {p}'
 d[page-1].get_pixmap(matrix=pymupdf.Matrix(4,4),clip=pymupdf.Rect(*rect)).save(p)

headings=['Overview','Intuition','Derivation','Motivation and explanation','Worked example','Link to other topics','Conclusion']
checks=[]
for name in notes:
 p=AB/name; s=p.read_text()
 assert re.findall(r'^## (.+)$',s,re.M)==headings
 number=name.split('-')[1]
 assert s.startswith(f'# Section {number}: ')
 tags=[int(x) for x in re.findall(r'\\tag\{(\d+)\}',s)]
 assert tags==list(range(1,len(tags)+1)), (name,tags)
 assert '[[' not in s and not re.search(r'^>\s*\[!',s,re.M)
 assert not re.search(r'lecture|lecturer|slides|\.pdf|Lecture15',s,re.I)
 links=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',s)
 for link in links:
  f=p.parent/link; assert f.is_file()
  im=pymupdf.Pixmap(f); assert im.width>0 and im.height>0
 assert s.count('$$')%2==0
 checks.append(f'{name}: seven headings; tags {tags}; {len(links)} linked PNGs; no prohibited narration, wikilinks or callouts; math delimiters checked.')
for rel,digest in baseline.items():
 assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==digest, f'Protected file changed: {rel}'
(BASE/'validation-output.txt').write_text('\n'.join(checks)+'\nProtected files unchanged during this script.\n')

PROGRESS.parent.mkdir(parents=True,exist_ok=True)
PROGRESS.write_text('''# Codex AB-53–56 — Lecture 15 progress and verification

Owner: codex. Scope: AB-53–56 only. Date: 2026-10-09.

Read AGENTS.md, CLAUDE.md, out/PLAN.md and out/work/BOARD.md. User transfers ownership and overrides board updates, commits and changes to AB-01–47. Shared OCR/progress checked before reading: no Lecture15 transcript or prior progress file present at that time. No edits made to those protected files; no commit or merge.

## Source reading

Lecture15.pdf contains 47 pages. Text extraction was used only for navigation; pages 6–47 rendered individually at 1.5x and visually read in seven labelled PyMuPDF montages. Page allocation: AB53 pp6–17; AB54 pp18–21; AB55 pp23–31; AB56 pp33–47. Intervening outline pages visually checked. No dense mathematical derivation occurs in these ranges; compartment balance and recovery formula are explicitly added first-principles teaching models, with illustrative inputs.

## External sources actually opened and read

- AB53: Shimizu et al. (2001), original research abstract, https://www.nature.com/articles/nbt0801_751 . Only abstract accessible; full paper is subscription content. Abstract confirms purified recombinant factors and release-factor omission for non-natural amino acid incorporation.
- AB53 component cross-check only: PURE makes PURE (2026), original research, https://www.nature.com/articles/s41467-026-73337-0 . Read introduction and Results; confirms 36 non-ribosome proteins and functional regrouping. New self-regeneration results deliberately not expanded into the teaching scope; standard systems are not described as autonomous self-replicating cells.
- AB54: Inagaki et al. (2023), original research, https://www.nature.com/articles/s41467-023-38244-8 . Read Introduction and method rationale: cap structure, enzymatic vs co-transcriptional capping, uncapped contaminants and cap purification limits.
- AB54 original conceptual flowsheet provenance: Rosa et al. (2021), author manuscript, https://discovery.ucl.ac.uk/id/eprint/10124976/1/Marques_mRNA_Vaccines_Manufacturing_unmarked2.pdf . Opened via https://discovery.ucl.ac.uk/id/eprint/10124976/ ; read manufacturing pp8–12, capping alternatives, purification and proposed continuous process/recycling. This is a review/proposal, not validation of an implemented universal process. Technical correction about capping independently supported by primary Inagaki research.
- AB55: Hutchison et al. (2016), author-institution publication abstract, https://www.nist.gov/publications/design-and-synthesis-minimal-bacterial-genome . Read abstract: failed first design, quasi-essential genes, iterative design, 473 genes, 149 unknown functions.
- AB55: original investigators' institutional account, https://www.jcvi.org/media-center/first-minimal-synthetic-bacterial-cell-designed-and-constructed-scientists-venter . Read genome assembly/transplantation, segment tests, quasi-essentiality, RNA gene count and functional categories.
- AB56 (also clarifies AB53 energy/oxygen limits): Noireaux and Libchaber (2004), original research full text, https://www.noireauxlab.org/html%20pages/docs%20website/publications/Noireaux%20and%20Libchaber-2004.pdf . Read expression, vesicle encapsulation, pore-mediated exchange, nutrient limitations, osmotic pressure and oxygen dependence; no protocol-scale details copied into notes.

## Retrieval limitations

https://arep.med.harvard.edu/pdf/Shimuzu01.pdf failed retrieval; https://www.nature.com/articles/90802 failed but the nbt0801_751 alias provided the original abstract. https://pubmed.ncbi.nlm.nih.gov/11479568/ returned an empty page and was not used. https://pmc.ncbi.nlm.nih.gov/articles/PMC539773/ and https://pmc.ncbi.nlm.nih.gov/articles/PMC7987532/ returned browser challenges; author/institution PDF alternatives above were used. https://www.unife.it/medicina/biotecnologie-mediche/insegnamenti/Biologia-Generale/materiale-didattico/biomed-papers-2k20/Hutchison_et_al_2k16a.pdf returned 502 and was not used. NIST and JCVI accessible accounts supplied the minimal-genome cross-check. No search snippet was treated as an opened full paper.

## Corrections and qualifications

- Cell-free expression avoids modifying a live production host for every template; it does not abolish safety, quality or regulatory requirements. Cell growth/disruption still occurs during extract preparation.
- Clarification alone does not completely remove native DNA. Nucleic-acid cleanup is preparation dependent; linear templates can suffer nuclease damage.
- PURE protein count is formulation dependent and excludes ribosomes; typical yield comparisons are conditional, not universal.
- Oxygen transfer can still constrain cell-free systems. Lyophilisation and membrane-protein expression require suitable preparations.
- Post-transcriptional capping is one route, not a universal typical route; co-transcriptional capping also exists.
- The manufacturing flowsheet is conceptual. Enzyme recycling requires demonstrated selective recovery, not merely ordinary ultrafiltration.
- Mycoplasma host dependence does not imply no need for adaptation. Gene essentiality is environment- and background-dependent.
- 149/473 is the original unknown-specific-function fraction, not the pie chart's wholly unassigned category, and not a current unknown count.
- Growth/replication differs from uniform morphology and normal division. No graph values inferred beyond stated approximate doubling time.
- Hydrogels are not necessarily liquid condensates; membrane-less architectures are not universally more robust or dynamic. Synthetic-cell images show architecture, not proof of autonomous life. Applications described as proposals.

## Numerical and structural validation

Reusable script: out/work/scratch/codex-ab53-56-l15/prepare.py . Numerical output: verification-output.json. Structural output: validation-output.txt. All worked numerical values computed in Python. Checks include IVT product recovery, gene count and unknown fraction, sphere area/volume cancellation, membrane balance substitution, equal-concentration and zero-consumption limits, and dimensions. The transfer calculation assumes fixed geometry, well-mixed interior and constant outside concentration; constant consumption applies only while substrate remains available.

All notes use Section NN H1 and exactly seven required H2 headings. Local tags run 1..N (AB53 has no numbered equation). Figure links resolve; all crops use PyMuPDF Matrix(4,4). Parent performs KaTeX rendering and equation-reference integration. Deliverable figures require final visual inspection after this script, recorded below.

## Crop provenance (one-based PDF pages; coordinates in PDF points)
'''+''.join(f'- {name}: page {page}, rectangle {rect}, 4x render.\n' for name,page,rect in crops))
print('\n'.join(checks))
print(json.dumps(results,indent=2))
print(f'Wrote {len(notes)} notes, {len(crops)} crops, and {PROGRESS.relative_to(ROOT)}')

# Cell-free systems and synthetic cells — reading 16.2

[Previous](16-01-cell-free-systems-and-synthetic-cells.md) · [Subject index](README.md) · [Next](17-01-synthetic-biomolecular-condensates.md)

<!-- reading-content:start -->
## Section 55: Top-down synthetic biology — minimal cells

### Intuition

A bacterium carries genes for both routine operation and coping with changing conditions. Supplying a stable, nutrient-rich environment can make some functions dispensable: the medium replaces tasks that the cell would otherwise perform itself.

*Analogy:* stripping a vehicle to essentials for one controlled track. The limit is that genes form interacting networks, so removing two individually dispensable parts can eliminate a shared function. A reduced cell also continues to maintain and reproduce its machinery rather than merely running once.

### Derivation

There is no universal gene-count equation for life. The minimal set is inferred by a design–build–test loop that asks whether a reduced genome supports a specified phenotype.

**Define the test.** Specify growth conditions and the criterion for success. Viability, robust population growth and regular division are different endpoints. Mycoplasma already have reduced genomes and depend strongly on nutrients supplied by their surroundings. Host association can relax selection for some biosynthetic functions; it does not remove all environmental challenges or adaptation.

**Perturb genes.** Transposon insertion disrupts genes. Mutants recovered after growth show that a disruption is tolerable under those conditions; failure to recover insertions suggests essentiality, subject to insertion biases and experimental limitations. Comparing mutant abundance over passages also exposes fitness defects that a single survival test can miss. Bioinformatics identifies conserved machinery and suggests functions, but prediction alone cannot establish dispensability.

**Distinguish growth requirements.** Essential genes cannot be removed while retaining the tested viability. Quasi-essential genes permit some survival when disrupted but are needed for sufficiently robust growth. Non-essential genes can be removed under the specified conditions. These categories change with environment and with the remaining genome. Two alternative pathways can each be dispensable alone, yet deleting both is lethal: single-gene tests do not prove that all tolerated deletions can be combined.

**Build and test the combined design.** Design reduced genome segments, synthesise DNA, assemble and clone the genome, and transplant it into a recipient cell. Its existing cytoplasm supplies the initial machinery that lets the transplanted genome take control. Test outgrowth and phenotype, then restore or revise deleted regions if the design fails. Segment-level tests help locate incompatible deletions before final assembly.

![Design–build–test cycle: genome design and synthesis, assembly, transplantation, outgrowth and phenotype measurement](figs/AB-55-design-build-test.png)

JCVI-syn1.0, a synthetic genome based on Mycoplasma mycoides, provided the starting point; its faster growth made iterative testing more practical than using the much slower M. genitalium. Genome minimisation yielded JCVI-syn3.0 after repeated redesign and retention of quasi-essential functions. Chemically synthesising the genome does not change the top-down logic: its organisation is derived from a natural cell, and the experiment relies on an existing recipient cytoplasm.

### Motivation and explanation

The retained functions must form a sustainable loop. Expression machinery produces proteins and functional RNAs; replication and maintenance preserve genetic information; cytosolic metabolism supplies usable substrates and energy; the membrane retains components and mediates exchange with the nutrient-rich medium. Simplifying biosynthesis can increase dependence on transport, so a small genome does not make the membrane unimportant.

A minimal cell exposes gaps in knowledge because genes can be necessary without their precise biological roles being known. It also offers a simpler chassis for experiments. Simplicity is not automatically industrial performance: slow growth, poor robustness and irregular morphology can offset the reduced genetic complexity.

### Worked example

JCVI-syn3.0 contains 473 genes, comprising 438 protein-coding genes and 35 RNA genes. Python verifies that the two classes sum to 473. In the original characterisation, 149 genes lacked a specific biological function. Defining $`f_u`$ as the fraction of all retained genes in this class gives


```math
f_u=\frac{149}{473}\approx0.315=31.5\%. \tag{126}
```


The denominator includes RNA genes as well as protein-coding genes: changing it would answer a different question. Broad functional classification can still be possible without a specific mechanistic assignment, so a chart's wholly unassigned category need not equal this fraction. The historical count is not a claim that all these functions remain unknown.

![Growth and morphology comparison of JCVI-syn1.0 and JCVI-syn3.0, retaining the original panel labels and scale bars](figs/AB-55-growth-morphology.png)

The phenotype reveals another limit. JCVI-syn3.0 has roughly a three-hour doubling time under its studied conditions and irregular, heterogeneous cell shapes. Sustained replication therefore does not imply normal morphology or an efficient, uniform division cycle. No additional numerical values are inferred from the plotted curves.

### Link to other topics

Minimal-cell construction extends oligonucleotide synthesis and genome assembly from making DNA to testing whether a whole genome sustains a phenotype. It also shows why regulation, transport and metabolic redundancy affect the consequences of gene deletion.

### Summary

A minimal genome is an experimentally tested set for a particular environment and growth criterion. Bottom-up synthetic cells take the complementary route: assemble selected cellular functions from components rather than reducing an inherited living system.

## Section 56: Bottom-up synthetic cells

### Intuition

Confinement puts a biochemical programme in a defined location. It can retain expensive machinery, separate incompatible reactions and establish an inside and outside. But the same barrier that prevents machinery escaping can prevent fresh substrates entering.

*Analogy:* a miniature chemical plant with a wall, machinery and control system. The limit is that each part may be assembled rather than self-produced, and molecular fluctuations, membrane mechanics and osmotic effects become important at this scale.

### Derivation

**Structure.** Lipid vesicles enclose aqueous reaction mixtures with a bilayer. Polymer membranes can offer different mechanical stability and permeability; protein or particle assemblies provide other boundaries. Giant unilamellar vesicles are commonly about $`1`$–$`100\,\mu\mathrm{m}`$ across, large unilamellar vesicles about $`0.1`$–$`1\,\mu\mathrm{m}`$, and small ones below about $`0.1\,\mu\mathrm{m}`$. These are approximate size categories; unilamellar means one bilayer. Internal compartments can organise distinct pathways as synthetic organelles.

![Compartment architecture with an outer boundary and internal compartments made from different materials](figs/AB-56-compartment-architecture.png)

**Machinery and information.** Encapsulated TXTL converts a DNA programme into functional proteins. Enzymes catalyse transformations; pores mediate exchange; receptors and regulatory circuits connect inputs to outputs. Synthetic nucleic-acid structures or nanomaterials can supplement biological components. A minimal sensing chain is external input, molecular recognition, changed internal reaction or gene expression, and an observable output. Each connection must be physically implemented; a compartment alone has no sensing programme.

**Exchange constraint.** Consider a spherical vesicle of fixed radius $`R`$ and volume $`V`$, with surface area $`A`$. Let $`t`$ denote elapsed time, $`c_i`$ and $`c_o`$ internal and external substrate concentrations, $`\mathcal P`$ its effective membrane permeability, and $`q`$ the positive volumetric consumption rate inside. Assume a well-mixed interior, a large external reservoir holding $`c_o`$ constant, passive linear transport, and a thin membrane with transport resistance included in $`\mathcal P`$.

The inward flux per area is $`J=\mathcal P(c_o-c_i)`$. Multiplying by area gives the entry rate; multiplying consumption by volume gives the removal rate. Conservation therefore gives


```math
V\frac{dc_i}{dt}=A\mathcal P(c_o-c_i)-Vq. \tag{127}
```


Divide by the fixed volume. For a sphere, $`A=4\pi R^2`$ and $`V=4\pi R^3/3`$, so cancelling $`4\pi R^2`$ gives $`A/V=3/R`$. Thus


```math
\frac{dc_i}{dt}=\frac{3\mathcal P}{R}(c_o-c_i)-q. \tag{128}
```


For constant $`q`$, set the accumulation to zero and rearrange: $`(3\mathcal P/R)(c_o-c_i^*)=q`$, then $`c_o-c_i^*=Rq/(3\mathcal P)`$. Hence


```math
c_i^*=c_o-\frac{Rq}{3\mathcal P}. \tag{129}
```


The star denotes the steady concentration. A negative result means the assumed consumption cannot be sustained; it is not a physically negative concentration. With no consumption, the coefficient of concentration relaxation in equation (128) is $`3\mathcal P/R`$, giving an exchange time scale $`\tau=R/(3\mathcal P)`$. Since permeability has units of length per time, $`\tau`$ has units of time. A completely impermeable membrane supplies no substrate through this mechanism.

### Motivation and explanation

Pores can admit small nutrients while retaining ribosomes and other large components, allowing an encapsulated TXTL reaction to last longer. Expression of a pore can itself improve supply, linking gene expression to boundary function. Oxygen requirements and osmotic balance still need attention; increased internal solute concentration can draw in water and rupture a vesicle.

Membrane-less compartments use selective partitioning instead of a bilayer. Liquid–liquid phase separation enriches compatible proteins or nucleic acids in a dense phase while excluding others. Molecules still exchange with the surroundings, and enrichment need not improve catalysis if substrates are excluded or enzymes become inactive. Hydrogels and cross-linked networks are other membrane-less architectures, but are not necessarily liquid condensates. Neither greater robustness nor faster dynamics is universal across these materials.

### Worked example

Take illustrative values $`c_o=1.0\,\mathrm{mM}`$, $`\mathcal P=10^{-8}\,\mathrm{m\,s^{-1}}`$ and $`q=10^{-3}\,\mathrm{mM\,s^{-1}}`$. For radii of $`5\,\mu\mathrm{m}`$ and $`10\,\mu\mathrm{m}`$, Python gives exchange time scales of approximately $`167\,\mathrm{s}`$ and $`333\,\mathrm{s}`$, and steady substrate concentrations of approximately $`0.833\,\mathrm{mM}`$ and $`0.667\,\mathrm{mM}`$. Doubling the radius doubles the exchange time and increases depletion at the same volumetric demand. These are model examples, not measurements from an image; concentration-dependent consumption and changing vesicle volume require a fuller model.

![Microscopy image of a compartment containing distinct red and cyan internal domains; the original 50 micrometre scale bar is retained](figs/AB-56-synthetic-organelles.png)

The image illustrates spatial organisation within an enclosing compartment. It does not alone establish selective transport, replication or autonomous metabolism. Such functions require separate measurements: for example, substrate entry, product generation and boundary integrity over time.

### Link to other topics

Synthetic cells combine cell-free expression, membrane transport and regulatory circuits in a confined setting. Membrane-less organelles connect their design to phase separation and programmable nucleic-acid materials.

### Summary

Bottom-up construction tests which combinations of parts are sufficient for a chosen function. It supports studies of confined expression, signalling and membrane mechanics, and offers candidate platforms for delivery, manufacturing and remediation; these proposed applications require function-specific validation.

## Conclusion

Removing cellular complexity makes individual functions easier to control, but rebuilding autonomy requires their integration. The next unit develops synthetic biomolecular condensates.
<!-- reading-content:end -->

[Previous](16-01-cell-free-systems-and-synthetic-cells.md) · [Subject index](README.md) · [Next](17-01-synthetic-biomolecular-condensates.md)

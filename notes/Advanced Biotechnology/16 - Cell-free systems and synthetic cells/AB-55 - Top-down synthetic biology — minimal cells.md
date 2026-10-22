[Previous](<AB-54 - Manufacturing mRNA by in vitro transcription.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-56 - Bottom-up synthetic cells.md>)

<!-- note-content:start -->
# Section 55: Top-down synthetic biology — minimal cells

## Intuition

A bacterium carries genes for both routine operation and coping with changing conditions. Supplying a stable, nutrient-rich environment can make some functions dispensable: the medium replaces tasks that the cell would otherwise perform itself.

*Analogy:* stripping a vehicle to essentials for one controlled track. The limit is that genes form interacting networks, so removing two individually dispensable parts can eliminate a shared function. A reduced cell also continues to maintain and reproduce its machinery rather than merely running once.

## Derivation

There is no universal gene-count equation for life. The minimal set is inferred by a design–build–test loop that asks whether a reduced genome supports a specified phenotype.

**Define the test.** Specify growth conditions and the criterion for success. Viability, robust population growth and regular division are different endpoints. Mycoplasma already have reduced genomes and depend strongly on nutrients supplied by their surroundings. Host association can relax selection for some biosynthetic functions; it does not remove all environmental challenges or adaptation.

**Perturb genes.** Transposon insertion disrupts genes. Mutants recovered after growth show that a disruption is tolerable under those conditions; failure to recover insertions suggests essentiality, subject to insertion biases and experimental limitations. Comparing mutant abundance over passages also exposes fitness defects that a single survival test can miss. Bioinformatics identifies conserved machinery and suggests functions, but prediction alone cannot establish dispensability.

**Distinguish growth requirements.** Essential genes cannot be removed while retaining the tested viability. Quasi-essential genes permit some survival when disrupted but are needed for sufficiently robust growth. Non-essential genes can be removed under the specified conditions. These categories change with environment and with the remaining genome. Two alternative pathways can each be dispensable alone, yet deleting both is lethal: single-gene tests do not prove that all tolerated deletions can be combined.

Restoring a deleted gene and recovering growth links the failure to that deletion more strongly than observing failed growth alone. Changing the medium supplies a complementary test: rescue by adding a metabolite can reveal that the deleted function was needed to make or obtain that nutrient under the original conditions. Neither result establishes a universal minimal genome. Essentiality is a property of the genome together with its environment and the phenotype being tested.

**Build and test the combined design.** Design reduced genome segments, synthesise DNA, assemble and clone the genome, and transplant it into a recipient cell. Its existing cytoplasm supplies the initial machinery that lets the transplanted genome take control. Test outgrowth and phenotype, then restore or revise deleted regions if the design fails. Segment-level tests help locate incompatible deletions before final assembly.

![Design–build–test cycle: genome design and synthesis, assembly, transplantation, outgrowth and phenotype measurement](../figs/AB-55-design-build-test.png)

JCVI-syn1.0, a synthetic genome based on Mycoplasma mycoides, provided the starting point; its faster growth made iterative testing more practical than using the much slower M. genitalium. Genome minimisation yielded JCVI-syn3.0 after repeated redesign and retention of quasi-essential functions. Chemically synthesising the genome does not change the top-down logic: its organisation is derived from a natural cell, and the experiment relies on an existing recipient cytoplasm.

## Motivation and explanation

The retained functions must form a sustainable loop. Expression machinery produces proteins and functional RNAs; replication and maintenance preserve genetic information; cytosolic metabolism supplies usable substrates and energy; the membrane retains components and mediates exchange with the nutrient-rich medium. Simplifying biosynthesis can increase dependence on transport, so a small genome does not make the membrane unimportant.

A minimal cell exposes gaps in knowledge because genes can be necessary without their precise biological roles being known. It also offers a simpler chassis for experiments. Simplicity is not automatically industrial performance: slow growth, poor robustness and irregular morphology can offset the reduced genetic complexity.

### Minimal survival does not mean complete understanding

The original JCVI-syn3.0 characterisation counted 438 protein-coding and 35 RNA genes, giving 473 total. Of these, 149 lacked a specific biological function assignment at the time. With $`f_u`$ denoting that historical fraction,


**Equation (126)**

```math
f_u=\frac{149}{473}\approx0.315=31.5\%.
```


The denominator includes RNA genes. A broad classification may still be possible without a specific mechanism, so a chart's wholly unassigned category need not equal this fraction. These are historical annotation counts, rather than a claim that all those functions remain unknown.

![Growth and morphology comparison of JCVI-syn1.0 and JCVI-syn3.0, with original panel labels and scale bars](../figs/AB-55-growth-morphology.png)

The comparison shows that sustained replication can coexist with irregular, heterogeneous cell shapes. Survival of a reduced genome therefore does not establish normal division or industrial robustness. The image supports a phenotype comparison; no new quantitative growth estimate is inferred from its curves.

## Link to other topics

Minimal-cell construction extends oligonucleotide synthesis and genome assembly from making DNA to testing whether a whole genome sustains a phenotype. It also shows why regulation, transport and metabolic redundancy affect the consequences of gene deletion.

## Summary

A minimal genome is an experimentally tested set for a particular environment and growth criterion. Bottom-up synthetic cells take the complementary route: assemble selected cellular functions from components rather than reducing an inherited living system.
<!-- note-content:end -->

[Previous](<AB-54 - Manufacturing mRNA by in vitro transcription.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-56 - Bottom-up synthetic cells.md>)

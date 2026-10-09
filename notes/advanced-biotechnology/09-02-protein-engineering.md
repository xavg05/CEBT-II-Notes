# Protein engineering — reading 09.2

[Previous](09-01-protein-engineering.md) · [Subject index](README.md) · [Next](09-03-protein-engineering.md)

<!-- reading-content:start -->
## Section 29: Site-directed mutagenesis and non-canonical amino acids

### Intuition

To change a protein you change its gene, and the cell does the rest. A mutagenic primer carries the desired change and is incorporated into a new copy of the plasmid, so the mutation is introduced during amplification rather than by editing an existing molecule.

The harder problem is deciding *which* residue to change. There are far too many options to test exhaustively (Section 30), so changes must be chosen rationally — which requires a structure, and is why Sections 24–26 come first.

Expanding the genetic code is a different kind of move. The twenty natural amino acids provide a limited chemical palette: no azides, no ketones, no photoreactive groups. Rather than work around this, one can reassign a codon the cell does not otherwise need and install a new amino acid at that position.

*Analogy:* mutagenesis is replacing one component with another from the same catalogue; code expansion is adding a new entry to the catalogue. The analogy breaks down because the new entry needs its own dedicated supply chain — a tRNA and a synthetase that no other machinery in the cell will touch.

### Mechanism

#### Site-directed mutagenesis

The aim is to replace one amino acid by another to explore function or mechanism.

**The QuikChange method**, three steps:
1. **Mutant strand synthesis.** Denature the plasmid and anneal a pair of complementary primers carrying the desired mutation at their centre, flanked by matching sequence on both sides so they still hybridise. A high-fidelity polymerase extends around the whole plasmid.
2. **DpnI digestion.** The template came from *E. coli* and is therefore **methylated**; the newly synthesised strands are not. **DpnI cuts only methylated DNA**, so it destroys the parental plasmid and leaves the mutated copies. This is the clever step: it solves the problem of separating product from a template that is otherwise nearly identical.
3. **Transformation.** The nicked circular product is transformed into competent cells, which repair the nicks.

It is fast and exceeds 90 % success, but makes one change at a time and can only insert or delete a few residues.

**Which residue to change?** Five rational strategies:
1. From a **structure** with ligand bound, by X-ray or cryo-EM.
2. From an **AlphaFold prediction** of the structure or complex (Section 26) when no experimental structure exists.
3. **Conserved residues**, identified from a sequence alignment — conservation across species implies functional importance, the same co-evolutionary logic AlphaFold exploits.
4. **Alanine scanning**: replace each candidate residue in turn with alanine. Alanine removes the side chain beyond the β-carbon, so it deletes the functional group *without* adding bulk and without the flexibility of glycine. Loss of activity implicates that side chain.
5. **Stop codons** to truncate the chain or remove a domain.

**Point mutants can be products in themselves.** Subtilisin, the protease in biological laundry detergent, is inactivated by bleach, which oxidises a key methionine. Replacing that methionine with alanine gives a bleach-resistant enzyme. The same enzymes have also been improved by **directed evolution** (Section 30) for activity at low temperature — the two approaches are complementary, rational design where the mechanism is understood and evolution where it is not.

#### Non-canonical amino acids

![An engineered aminoacyl-tRNA synthetase charges a suppressor tRNA with a non-canonical amino acid; the ribosome inserts it at a UAG codon instead of terminating](figs/AB-29-ncAA.png)

The goal is to go beyond the natural twenty and install new chemical functionality — photocrosslinkers, photocaged side chains, click-chemistry handles — as a subtle change to a single side chain.

**The mechanism requires three parts working together:**

1. **A spare codon.** The **amber stop codon UAG** is reassigned. It is the rarest stop codon in *E. coli*, so taking it over disrupts least.
2. **A suppressor tRNA** with an anticodon complementary to UAG. Where the ribosome would normally terminate, this tRNA delivers an amino acid instead and translation continues.
3. **An engineered aminoacyl-tRNA synthetase (aaRS)** that charges the suppressor tRNA with the non-canonical amino acid **and nothing else**.

**The orthogonality requirement is the crux.** The new pair must not cross-react with the host's machinery: the engineered synthetase must not charge any natural tRNA, and no natural synthetase may charge the suppressor tRNA. Otherwise the non-canonical amino acid appears at random positions, or a natural amino acid is inserted at the UAG site, and the product is heterogeneous. The pair is usually borrowed from a distantly related organism, precisely so that it does not recognise the host's components.

The non-canonical amino acid must also be supplied in the medium and taken up by the cell, since the cell cannot synthesise it.

This works by *in vitro* translation, in *E. coli* (most common) and, more recently, in yeast and mammalian systems.

### Motivation and explanation

**Why alanine, specifically.** The ideal probe deletes a side chain's chemistry while perturbing the backbone as little as possible. Glycine would remove the side chain entirely, but it also makes the backbone far more flexible and can disrupt the fold. Alanine keeps a methyl group, so the backbone conformational preferences are largely retained. Replacing a residue with a *smaller* one also avoids introducing steric clashes — a larger substitution might abolish activity simply by not fitting.

**Why rational design has limits.** Section 23 showed that folding stability is only 20–40 kJ/mol. A mutation intended to improve binding frequently destabilises the fold instead, and the two effects cannot be separated by inspection. Predicting the effect of a point mutation is also precisely what AlphaFold does *not* do well (Section 26), because a single substitution barely changes the sequence alignment the prediction rests on. This is why rational design is usually combined with, or replaced by, the selection methods of Section 30.

**Why code expansion is worth the trouble.** A click-chemistry handle at one defined position allows a protein to be conjugated **site-specifically** — to a drug, a surface or a fluorophore — rather than at whichever surface lysine happens to react. For an ADC (Section 27), where drug position and copy number are optimised parameters, this converts a heterogeneous mixture into a defined molecule.

### Link to other topics

The DpnI step is a selection based on a marker that distinguishes product from feed — methylation — rather than on any difference in the product itself. The same logic recurs wherever a reaction leaves starting material nearly identical to product: tag the feed instead of purifying the product.

### Summary

Site-directed mutagenesis introduces a defined change through a mutagenic primer, with DpnI digestion removing the methylated parental template; choosing the residue relies on structure, conservation or alanine scanning. Genetic code expansion goes further, reassigning the amber codon through an orthogonal tRNA–synthetase pair to install chemistry outside the natural twenty.
<!-- reading-content:end -->

[Previous](09-01-protein-engineering.md) · [Subject index](README.md) · [Next](09-03-protein-engineering.md)

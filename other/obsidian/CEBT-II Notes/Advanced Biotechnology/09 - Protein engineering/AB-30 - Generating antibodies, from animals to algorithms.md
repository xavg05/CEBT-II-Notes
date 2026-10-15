[Previous](<AB-29 - Site-directed mutagenesis and non-canonical amino acids.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Section 30: Generating antibodies, from animals to algorithms

## Intuition

Section 19 established the principle for nucleic acids: make a huge library, select, amplify, repeat. Proteins cannot do this, because **a protein cannot copy itself**. Any protein selection method must therefore physically tie each protein to the gene encoding it, so that selecting the protein also recovers its sequence.

Every method below is a different solution to that one problem:
- a **cell** keeps protein and gene together naturally;
- a **phage** displays the protein on its coat while carrying the gene inside;
- a **droplet** confines both in one compartment;
- **computation** sidesteps it, since the sequence is known by construction.

*Analogy:* judging a baking competition where you must also know the recipe. You can watch each baker (cell), label each cake with its recipe (phage), keep each in its own numbered box (droplet), or compute from the recipe what the cake will be like (design). The analogy breaks down for the last one — a computed prediction is a hypothesis, not a measurement, so it still needs testing.

## Derivation

**Why libraries, not design.** With 20 amino acids, a modest 200-residue protein has
$$20^{200} = 1.6\times10^{260} \tag{42}$$
possible sequences — against roughly $10^{80}$ atoms in the universe. Even a phage library of $10^{9}$ covers $10^{-251}$ of this.

Two conclusions follow, and they shape the whole field:
- exhaustive search is impossible by any physical means, so the library must be **designed to sample a useful region**, not sample uniformly;
- antibody libraries work because they vary only the **six CDR loops** on a fixed framework (Section 27), so the search is restricted to the part that determines binding.

## Mechanism

![A mouse is immunised, B cells are collected from the spleen and fused with lymphoma cells; HAT selects the fusions, which are cloned and screened for one epitope](../figs/AB-30-hybridoma.png)

**1. Polyclonal antibodies** — antiserum from an immunised animal, or human plasma. A mixture recognising many epitopes, cheap but undefined and finite.

**2. Hybridoma (monoclonal).** Immunise a mouse, collect B cells from the spleen, and fuse them with immortal lymphoma cells. **HAT medium** selects the fusions: unfused lymphoma cells die in the selection, unfused B cells die of their own accord, so only hybrids survive. Each hybridoma is cloned, giving an immortal line secreting a single antibody against **one epitope only**. Here the cell links genotype to phenotype.

![Murine, chimaeric, humanised and fully human antibodies: progressively less mouse sequence](../figs/AB-30-humanisation.png)

**3. Humanisation.** Mouse antibodies fail as human therapeutics: patients raise anti-mouse antibodies that block repeated dosing (the anti-drug antibodies of Section 28), and mouse Fc engages human effector machinery poorly. The fix is to replace mouse sequence progressively:
- **chimaeric** — mouse variable domains on human constant regions;
- **humanised** — only the mouse CDRs grafted onto a human framework;
- **human** — no mouse sequence at all.

This is only possible because of the modularity in Section 27: binding is confined to the CDRs, so everything else can be swapped.

![Phage displaying scFv are panned against immobilised target, unbound phage washed away, bound phage amplified in E. coli, and the cycle repeated three to four times](../figs/AB-30-phage-display.png)

**4. Phage display.** Selection can be performed without immunising an animal and can bypass the animal’s tolerance to self-antigens. This broadens the accessible target range, but does not demonstrate that a selected antibody lacks cross-reactivity or would be safe in a patient.

A library of human scFv sequences is fused to a coat protein (p3) of filamentous M13 phage. Each phage **displays the antibody fragment on its surface while carrying its gene inside** — genotype linked to phenotype in one particle.

1. **Pan** a library of at least $10^{9}$ phage against immobilised target.
2. **Wash hard** and recover the good binders.
3. **Amplify** the recovered phage in *E. coli*. Repeat 3–4 cycles.
4. **Sequence** to identify good scFv.
5. **Reformat as IgG**, since the therapeutic format is a full antibody, not a fragment.

This is Section 19's cycle exactly — select, amplify, repeat — with the phage particle supplying the link that nucleic acids get for free.

![In vitro compartmentalisation: a gene library is emulsified so each droplet holds at most one gene, transcribed and translated in the droplet; enzyme turnover on a fluorogenic substrate makes active droplets fluoresce, and FACS sorts them](../figs/AB-30-IVC.png)

**5. In vitro compartmentalisation (IVC).** Display methods select for **binding**. Selecting for **catalysis** is harder, because the product of an enzymatic reaction diffuses away and is not attached to the gene that made it.

IVC solves this with a water-in-oil emulsion:
- **(a)** droplets contain **0 or 1 gene** each;
- **(b)** *in vitro* transcription and translation inside the droplet;
- **(c)** the enzyme turns over a **fluorogenic substrate**, so an active enzyme makes its own droplet fluoresce;
- **(d)** **FACS** sorts the brightest droplets;
- **(e)** the recovered genes are expressed at scale or re-mutated for another round.

The droplet is an artificial cell: it keeps gene, enzyme and product together so that the product reports on the gene.

Compartment isolation is what preserves causation. If two different genes enter one droplet, an inactive variant can share the fluorescent product made by an active neighbour and be recovered with it. If product leaks between droplets, the same problem occurs across compartments. Dilute gene loading and retention of the reaction signal are therefore part of the selection mechanism, rather than merely practical details of making an emulsion.

**6. Transgenic mice.** Mice with the mouse immunoglobulin locus replaced by human antibody germline sequence. Conventional immunisation then produces fully human antibodies, with the animal's own affinity maturation doing the optimisation. The platform is extremely valuable commercially.

**7. Direct from people.** Isolate B cells from humans with strong immune responses and recover the sequences — no immunisation, and the antibodies are already human and already affinity-matured *in vivo*. Screening unusually resilient individuals ("élite controllers") can reveal unexpected targets and self-protein mechanisms.

**8. Computational design.** Generative models such as RFdiffusion use structural training data to propose binders. Reported demonstrations include an influenza-target example with roughly 1% binding designs and moderate affinity, illustrating why designed sequences need experimental testing. Computational antibody work has three distinct tasks: **affinity maturation**, improving CDRs of an existing binder; **rank prediction**, ordering candidates such as NGS-derived sequences by expected affinity; and **out-of-library design**, proposing new sequences informed by existing sequence-and-affinity data. Prediction and generation supply candidates; binding, specificity and function must still be measured.

## Motivation and explanation

**The trade-off across methods.** Animal methods provide affinity maturation but can be slow, restricted by tolerance to conserved self-antigens, and difficult when the target is toxic or poorly immunogenic. Toxic targets are a challenge, not an absolute exclusion: antitoxin antibodies can be generated through appropriate immunisation strategies. Mouse-derived sequences may need humanisation, whereas human-repertoire animals provide human sequences. *In vitro* selection allows targets and stringency to be controlled without animal tolerance, but useful candidates still need affinity, specificity and functional validation.

**Where design sits.** *De novo* design needs no existing binder and no bait, applies to difficult targets such as membrane-bound or toxic proteins, and the "library size" has no experimental limit — over $10^{18}$ sequences can be evaluated with publicly available software. Against that, it needs substantial computer time, still requires wet-lab optimisation, and struggles when substantial conformational change is involved. Accuracy requirements are severe: **1 or 2 Å out can abolish binding**, consistent with the 5.7 kcal/mol that separates a mediocre binder from an excellent one (Section 27).

**The pattern across all eight.** Each either exploits a natural compartment (cell, phage, mouse), builds an artificial one (droplet), or dispenses with physical selection entirely (computation). The trend is away from animals and towards *in vitro* and *in silico* methods — faster, more controllable, and not limited by what an immune system will tolerate.

## Link to other topics

IVC is compartmentalisation used as a separation: confining a reaction so its product stays with its catalyst, exactly as a cell does. The same principle, in bulk, is what emulsion polymerisation uses to keep growing chains isolated.

## Summary

Protein sequence space, $20^{200}$, cannot be searched, so every method restricts the library and links each protein to its gene — by cell, phage particle or droplet. Display selects binding, IVC selects catalysis, animals supply affinity maturation at the cost of speed and self-tolerance, and computational design is beginning to bypass selection at a current hit rate near 1 %.

## Conclusion

Sequence changes and screening connect molecular recognition to useful biological performance. The next unit develops bioprocessing overview and filtration.
<!-- note-content:end -->

[Previous](<AB-29 - Site-directed mutagenesis and non-canonical amino acids.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

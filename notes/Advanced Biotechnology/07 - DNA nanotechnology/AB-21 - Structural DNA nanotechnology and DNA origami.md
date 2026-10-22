[Previous](<AB-20 - DNA as a material.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-22 - Toehold-mediated strand displacement.md>)

<!-- note-content:start -->
# Section 21: Structural DNA nanotechnology and DNA origami

## Intuition

Natural DNA is linear, so a duplex can only extend end to end. The founding insight of the field (Seeman, 1982) was that a *branched* junction — four strands meeting at a point, with each arm a duplex — turns DNA from a thread into a connector. Give each arm a single-stranded "sticky end" and junctions link into networks.

The design problem is then the same as any self-assembly: the target structure must be the free-energy minimum, and the system must be able to reach it. Annealing slowly from above $`T_m`$ does both, because every incorrect bond formed on the way down has time to melt and re-form.

*Analogy:* crystallising a solid from a hot solution. Cool slowly and you get a single good crystal; quench and you get a glassy mess. The analogy breaks down because each DNA "bond" here is *different* from every other, so the structure is not periodic by necessity — it is addressable, and every position can be unique.

## Mechanism

![Oligonucleotides self-assemble into small structures, which self-assemble into larger ones; computational design closes the loop](../figs/AB-21-self-assembly.png)

**The design workflow.** Start from the target structure, use software to find a set of oligonucleotides whose minimum-free-energy configuration is that structure, synthesise them, mix, and anneal.

![Free energy against reaction coordinate, with the target structure at the global minimum and shallow local minima on the way](../figs/AB-21-energy-landscape.png)

**Why slow annealing.** The target is designed to be the global free-energy minimum, dominated by base pairing and so predictable from Section 04. The landscape also contains shallower local minima — partially correct structures, misbonded intermediates. Cooling slowly from above $`T_m`$ can allow incorrect contacts to exchange and help the system escape these **kinetic traps**. Rapid cooling freezes them in.

Slow cooling helps only if an incorrect contact can actually dissociate on the time available. At high temperature both correct and incorrect contacts are short-lived; as temperature falls, intended multi-contact assemblies become stable while some wrong contacts can still exchange. Cooling too far before rearrangement has occurred locks those intermediates in. The relevant comparison is bond-exchange time against the annealing schedule, so slower cooling improves access to the target without guaranteeing complete equilibrium.

### Junctions and tiles

![A four-arm junction with sticky ends assembling into a square lattice, and a DNA tile scaffolding proteins in 3D](../figs/AB-21-junction-lattice.png)

Junctions with complementary sticky ends tile into periodic networks. The intended application was to arrange *other* molecules on a lattice — scaffolding proteins into a crystal so they could be solved by diffraction (Section 24).

**It did not work, and the reason is instructive.** Simple junctions are **floppy**: the arms pivot about the branch point, so the structure has no defined geometry and cannot pack into a crystal. The assemblies form hydrogels and liquid-like materials instead of ordered solids. Crystallisation required rigid motifs — *tensegrity triangles* — and took 27 years from the original proposal.

![Rectangular DX tile and Y-shaped tile, with microscopy of the lattices they form](../figs/AB-21-DX-tiles.png)

**The fix is crossovers.** A **double crossover (DX) tile** has two duplexes joined at two points rather than one. Two crossovers fix the relative orientation of the helices, removing the pivot. DX tiles are rigid enough to sustain 2D crystallisation and to arrange nanoparticles on a surface.

![Three-point-star motifs assembling into a tetrahedron, dodecahedron or buckyball depending on loop length and concentration](../figs/AB-21-polyhedra.png)

**3D.** A DNA cube came early but was floppy for the same reason. Rigid polyhedra followed from crossover motifs, and the assembled shape can be selected by tuning flexibility and concentration: the same three-point-star motif gives a tetrahedron, a dodecahedron or a buckyball depending on loop length and DNA concentration.

### DNA origami

![A long scaffold strand raster-fills a shape, held by staple strands whose crossovers link adjacent helices](../figs/AB-21-origami-scaffold.png)

Rothemund's method (2006) changed the scale of what could be built.

1. Take one **long single-stranded scaffold**, about 7 knt, from the M13 bacteriophage genome.
2. Route it back and forth to raster-fill the target shape.
3. Design **hundreds of short staple strands**, each complementary to two or more separated regions of the scaffold. Where a staple binds two regions, it pulls them together: a **crossover** linking adjacent helices.
4. Mix scaffold with excess staples and anneal. The structure folds in one step.

![Squares, stars, a smiley face and triangles, as designs, folding paths and atomic force micrographs](../figs/AB-21-origami-shapes.png)

Structures are about 100 nm across with roughly 6 nm resolution. Each staple is independently addressable, so any staple can carry a modification and act as a **6 nm pixel** — which is how patterns and words are written on the surface.

Later work extended this to 3D (stacked helical bundles), to wireframe designs generated automatically from a mesh, and to gigadalton assemblies built by polymerising origami units.

## Motivation and explanation

**Why origami beats tiles, in one idea: stoichiometry.** In a tile assembly, every component must be present in matched amounts, because the structure is built from many copies of a few species. An error in concentration leaves unincorporated tiles or truncated lattices, and yields are poor.

In origami there is **one scaffold molecule per structure**. The scaffold sets the size and the fold, and staples are supplied in excess so that every binding site is occupied. The assembly is unimolecular in the component that matters. Yields are high, the product is monodisperse, and purification is a matter of removing surplus staples.

**Why the staples need not be purified.** Each staple occupies a unique position, so a truncated staple (Section 07) simply fails to bind one site, leaving a small defect rather than a wrong structure. Origami is remarkably tolerant of the impurity profile that phosphoramidite synthesis produces.

**Limits.** Structures are soft and require millimolar Mg²⁺. They are degraded by nucleases, limiting biological use without protection. The scaffold length caps a single origami at roughly 100 nm, so larger objects must be built hierarchically. Cost scales with the number of distinct staples.

### Geometry sets both size and resolution

A scaffold of $`n`$ paired nucleotides has duplex contour length approximately $`0.34n\,\mathrm{nm}`$. If parallel helices are spaced by $`d`$, a fully filled single-layer rectangle has area approximately $`0.34nd\,\mathrm{nm^2}`$, neglecting turns and unpaired regions. For $`n=7249`$ and $`d=2.5\,\mathrm{nm}`$, a square would have side approximately $`78.5\,\mathrm{nm}`$. A structure described as roughly 100 nm across can therefore have a different aspect ratio or incomplete filling; that dimension does not imply a fully packed 100 nm square.

Address spacing is constrained by helix packing and crossover geometry. Sixteen base pairs span approximately $`5.44\,\mathrm{nm}`$ along a helix, so nanometre-scale placement is limited by DNA geometry as well as synthesis. A schematic outline cannot establish arbitrary sub-base-pair positioning.

## Link to other topics

Annealing through a rugged landscape to reach the global minimum is the same problem as crystallisation or protein folding, and the same solution — slow cooling — applies for the same reason: the system must stay equilibrated as the free-energy surface changes with temperature.

## Summary

Branched junctions make DNA a connector rather than a thread, but simple junctions are too floppy to order, and crossovers are what supply rigidity. Origami then solves the stoichiometry problem by using a single scaffold strand per structure, giving addressable 100 nm objects at 6 nm resolution in one annealing step.
<!-- note-content:end -->

[Previous](<AB-20 - DNA as a material.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-22 - Toehold-mediated strand displacement.md>)

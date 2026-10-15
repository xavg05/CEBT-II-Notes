[Previous](<AB-55 - Top-down synthetic biology — minimal cells.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Section 56: Bottom-up synthetic cells

## Intuition

Confinement puts a biochemical programme in a defined location. It can retain expensive machinery, separate incompatible reactions and establish an inside and outside. But the same barrier that prevents machinery escaping can prevent fresh substrates entering.

*Analogy:* a miniature chemical plant with a wall, machinery and control system. The limit is that each part may be assembled rather than self-produced, and molecular fluctuations, membrane mechanics and osmotic effects become important at this scale.

## Derivation

**Structure.** Lipid vesicles enclose aqueous reaction mixtures with a bilayer. Polymer membranes can offer different mechanical stability and permeability; protein or particle assemblies provide other boundaries. Giant unilamellar vesicles are commonly about $`1`$–$`100\,\mu\mathrm{m}`$ across, large unilamellar vesicles about $`0.1`$–$`1\,\mu\mathrm{m}`$, and small ones below about $`0.1\,\mu\mathrm{m}`$. These are approximate size categories; unilamellar means one bilayer. Internal compartments can organise distinct pathways as synthetic organelles.

![Compartment architecture with an outer boundary and internal compartments made from different materials](../figs/AB-56-compartment-architecture.png)

**Machinery and information.** Encapsulated TXTL converts a DNA programme into functional proteins. Enzymes catalyse transformations; pores mediate exchange; receptors and regulatory circuits connect inputs to outputs. Synthetic nucleic-acid structures or nanomaterials can supplement biological components. A minimal sensing chain is external input, molecular recognition, changed internal reaction or gene expression, and an observable output. Each connection must be physically implemented; a compartment alone has no sensing programme.

**Exchange constraint.** Consider a spherical vesicle of fixed radius $`R`$ and volume $`V`$, with surface area $`A`$. Let $`t`$ denote elapsed time, $`c_i`$ and $`c_o`$ internal and external substrate concentrations, $`\mathcal P`$ its effective membrane permeability, and $`q`$ the positive volumetric consumption rate inside. Assume a well-mixed interior, a large external reservoir holding $`c_o`$ constant, passive linear transport, and a thin membrane with transport resistance included in $`\mathcal P`$.

The inward flux per area is $`J=\mathcal P(c_o-c_i)`$. Multiplying by area gives the entry rate; multiplying consumption by volume gives the removal rate. Conservation therefore gives


**Equation (127)**

```math
V\frac{dc_i}{dt}=A\mathcal P(c_o-c_i)-Vq.
```


Divide by the fixed volume. For a sphere, $`A=4\pi R^2`$ and $`V=4\pi R^3/3`$, so cancelling $`4\pi R^2`$ gives $`A/V=3/R`$. Thus


**Equation (128)**

```math
\frac{dc_i}{dt}=\frac{3\mathcal P}{R}(c_o-c_i)-q.
```


For constant $`q`$, set the accumulation to zero and rearrange: $`(3\mathcal P/R)(c_o-c_i^*)=q`$, then $`c_o-c_i^*=Rq/(3\mathcal P)`$. Hence


**Equation (129)**

```math
c_i^*=c_o-\frac{Rq}{3\mathcal P}.
```


The star denotes the steady concentration. A negative result means the assumed consumption cannot be sustained; it is not a physically negative concentration. With no consumption, the coefficient of concentration relaxation in equation (128) is $`3\mathcal P/R`$, giving an exchange time scale $`\tau=R/(3\mathcal P)`$. Since permeability has units of length per time, $`\tau`$ has units of time. A completely impermeable membrane supplies no substrate through this mechanism.

The largest passive entry rate in this model occurs when the internal substrate concentration approaches zero, giving a maximum supply per internal volume of $`3\mathcal P c_o/R`$. If the assumed demand exceeds that supply, the steady-state construction fails because consumption cannot remain constant after substrate runs out. A concentration-dependent reaction law then reduces consumption as depletion develops. This connects the mathematical feasibility check directly to the missing biochemical mechanism.

## Motivation and explanation

Pores can admit small nutrients while retaining ribosomes and other large components, allowing an encapsulated TXTL reaction to last longer. Expression of a pore can itself improve supply, linking gene expression to boundary function. Oxygen requirements and osmotic balance still need attention; increased internal solute concentration can draw in water and rupture a vesicle.

Membrane-less compartments use selective partitioning instead of a bilayer. Liquid–liquid phase separation enriches compatible proteins or nucleic acids in a dense phase while excluding others. Molecules still exchange with the surroundings, and enrichment need not improve catalysis if substrates are excluded or enzymes become inactive. Hydrogels and cross-linked networks are other membrane-less architectures, but are not necessarily liquid condensates. Neither greater robustness nor faster dynamics is universal across these materials.

## Worked example

Take illustrative values $`c_o=1.0\,\mathrm{mM}`$, $`\mathcal P=10^{-8}\,\mathrm{m\,s^{-1}}`$ and $`q=10^{-3}\,\mathrm{mM\,s^{-1}}`$. For radii of $`5\,\mu\mathrm{m}`$ and $`10\,\mu\mathrm{m}`$, Python gives exchange time scales of approximately $`167\,\mathrm{s}`$ and $`333\,\mathrm{s}`$, and steady substrate concentrations of approximately $`0.833\,\mathrm{mM}`$ and $`0.667\,\mathrm{mM}`$. Doubling the radius doubles the exchange time and increases depletion at the same volumetric demand. These are model examples, not measurements from an image; concentration-dependent consumption and changing vesicle volume require a fuller model.

![Microscopy image of a compartment containing distinct red and cyan internal domains; the original 50 micrometre scale bar is retained](../figs/AB-56-synthetic-organelles.png)

The image illustrates spatial organisation within an enclosing compartment. It does not alone establish selective transport, replication or autonomous metabolism. Such functions require separate measurements: for example, substrate entry, product generation and boundary integrity over time.

## Link to other topics

Synthetic cells combine cell-free expression, membrane transport and regulatory circuits in a confined setting. Membrane-less organelles connect their design to phase separation and programmable nucleic-acid materials.

## Summary

Bottom-up construction tests which combinations of parts are sufficient for a chosen function. It supports studies of confined expression, signalling and membrane mechanics, and offers candidate platforms for delivery, manufacturing and remediation; these proposed applications require function-specific validation.

## Conclusion

Removing cellular complexity makes individual functions easier to control, but rebuilding autonomy requires their integration. The next unit develops synthetic biomolecular condensates.
<!-- note-content:end -->

[Previous](<AB-55 - Top-down synthetic biology — minimal cells.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

# Catalyst materials and preparation

## Overview

Assume elementary chemical equilibrium and activation energies. A catalyst changes the route and rate of reaction, while the equilibrium constant remains fixed by the reactants and products. Its surface chemistry, pore structure and preparation determine activity and selectivity together.

## Intuition

An active surface stabilises intermediates and transition states that would be difficult to form in the fluid. Binding must be strong enough to capture reactants but weak enough to release products. A deep adsorption well can become a trap: rapid reaction is useless if product desorption is slow. Lowering barriers accelerates the approach to equilibrium in both directions; it does not change the free-energy difference between the final states.

Homogeneous catalysis places catalyst and reactants in one phase; heterogeneous catalysis places them in different phases. Enzymes are biocatalysts. A solid catalyst is often easier to retain and reuse, and solid acids avoid some corrosion and disposal problems of liquid acids. Those advantages are traded against transport resistance and deactivation.

Useful representative process–catalyst pairings are:

| Process | Representative catalyst |
|---|---|
| Catalytic cracking of petroleum | Zeolites |
| Hydrotreating and hydrodesulfurisation | Co–Mo, Ni–Mo or Ni–W, commonly as supported sulfide phases |
| Naphtha reforming | Pt, Pt–Re or Pt–Ir |
| Alkylation | Sulfuric acid, HF or solid acids; the first two are liquid acid alternatives |
| Ethylene and propylene polymerisation | Cr catalysts or Ti chlorides on MgCl₂ |
| Ethylene epoxidation | Ag |
| Ethylene oxychlorination in vinyl-chloride manufacture | Copper chloride |
| Methane steam reforming | Ni |
| Water–gas shift | Iron oxide or Cu–ZnO formulations |
| Methanation | Ni |
| Ammonia synthesis | Fe |
| Ammonia oxidation | Pt–Rh |
| Acrylonitrile synthesis | Bi–Mo or Fe–Sb oxides |
| Vegetable-oil hydrogenation | Ni |
| Sulfur dioxide oxidation in sulfuric-acid manufacture | Vanadium oxide |
| Exhaust CO/hydrocarbon oxidation | Pt or Pd |
| NOx reduction | Rh in three-way exhaust catalysts; vanadium oxides in suitable selective-reduction systems |

These pairings identify catalyst families rather than universal recipes. Transition metals dominate many of them, and commercial formulations include supports, promoters and operating conditions that cannot be omitted from a detailed design.

## Mechanism and preparation

**Metals.** Fe catalyses ammonia synthesis, Ni hydrogenation and steam reforming, Cu/ZnO methanol synthesis, Ag ethylene epoxidation, and Pt dehydrogenation and oxidation. Metal surfaces stabilise reactive intermediates, but frequently catalyse competing reactions as well. Nanometre metal particles on porous alumina, silica or titania expose much more metal per unit mass than a bulk lump. The support separates the particles and must withstand temperature and mechanical stress while admitting reactants and products. Supports need not be chemically inert.

Impregnation starts with an existing porous support. A precursor solution enters its pores; adsorption or ion exchange deposits precursor at the surface. Drying removes solvent, and calcination decomposes precursor and removes ligands. Calcination can yield an oxide rather than metallic catalyst: a subsequent reducing activation, commonly in hydrogen, establishes the active metal. Co-precipitation instead brings support and active-component salts together in solution. Changing pH, temperature or solvent content precipitates intimate mixed particles; drying, calcination and activation establish the final phases. Cu/ZnO/alumina is a useful example.

Unsupported high-area Raney Ni and Pt–Rh gauzes are exceptions to the supported-particle arrangement. A ceramic monolith has many parallel channels coated with catalyst or a porous washcoat. It offers low pressure drop and short transport paths, useful in exhaust treatment. An additive that increases activity is a **promoter**, such as K on ammonia-synthesis Fe. An inhibitor can deliberately reduce activity while improving selectivity, such as chlorine in Ag epoxidation chemistry.

**Oxides and sulfides.** V oxides catalyse sulfur dioxide oxidation, and supported Co–Mo or Ni–Mo sulfide phases hydrodesulfurisation. A redox surface can provide oxygen to a reagent and then be reoxidised. For copper oxide,

$$2\mathrm{CuO}+\mathrm{CO}\longrightarrow\mathrm{Cu_2O}+\mathrm{CO_2},\qquad
\mathrm{Cu_2O}+\tfrac12\mathrm{O_2}\longrightarrow2\mathrm{CuO}.$$

Adding the steps cancels the solid intermediates and gives CO oxidation. Surface vacancies, hydroxyls and nonstoichiometry permit chemistry beyond a simple perfect-crystal oxidation-state picture. These catalysts often give more selective transformations than very reactive metal surfaces.

**Zeolites.** These are crystalline networks of corner-linked silicon and aluminium oxygen tetrahedra. Replacing Si(IV) by Al(III) leaves one negative framework charge per Al. If the framework has $y$ Al atoms and its balancing cation has charge $n+$, charge neutrality requires $y/n$ cations. A composition can therefore be written

$$ (\mathrm{M}^{n+})_{y/n}[x\mathrm{SiO_2}\cdot y\mathrm{AlO_2}]. $$

Proton compensation produces bridging Si–OH–Al Brønsted acid sites. Coordinatively unsaturated centres and suitable cations can provide Lewis acidity. Increasing aluminium content generally increases potential acid-site density, while silica-rich frameworks commonly resist steam and high temperature better; acid strength also depends on local structure, so density and strength are separate properties. Bases and contaminants can neutralise sites, while steam can damage susceptible frameworks.

The molecular-sized windows connect cages or channels and provide large internal area. ZSM-5 has intersecting channels of approximately benzene-sized width. The useful distinction is between the entrance aperture and the larger interior space. A molecule can fit inside a cage yet be unable to pass through its window.

## Motivation and explanation

Preparation fixes several successive conditions for activity: precursor must reach the support, activation must create the intended chemical phase, and the operating fluid must reach that phase. High total metal loading can therefore coexist with few exposed active atoms if particles grow or pores become blocked. A larger measured surface area addresses accessibility only for the probe and conditions used; it does not establish that the required catalytic sites were formed.

For zeolites, aluminium substitution supplies framework charge and hence potential charge-balancing acid sites, while pore windows decide which molecules can reach them. Increasing acid-site inventory and widening access need not improve selectivity together. A desired intermediate retained too long can undergo further cracking or coke formation. Catalyst choice must therefore connect site chemistry to the time needed for reagents and products to pass through the pore network.

Acid-catalysed propene conversion begins by protonation to a carbocation-like intermediate. Addition to another alkene builds a larger carbon skeleton; deprotonation releases an alkene and restores the acid site. Rearrangement gives isomers, and carbon–carbon bond cleavage gives smaller fragments. Repeated reactions also produce cyclic, aromatic and eventually coke-forming species. Cyclisation and dehydrogenation must be distinguished: ring formation and hydrogen removal are different chemical changes.

Pores impose three forms of **shape selectivity**. Reactant selectivity excludes molecules before they reach an active site. Transition-state selectivity prevents a bulky reaction configuration fitting locally. Product selectivity allows some formed products to escape more readily than others. ZSM-5 enrichment of para-xylene illustrates the last: isomers interconvert in larger channel intersections, but the para isomer diffuses out most readily. This is a kinetic separation coupled to reaction, not a change in thermodynamic equilibrium.

## Worked example

Consider choosing a catalyst for hydrocarbon conversion. Hydrogenation suggests a metal such as Ni; selective oxidation suggests an oxide or suitably modified metal; cracking and isomerisation suggest solid acid sites. If only a narrow product should escape, the pore topology becomes a design variable alongside the acid chemistry. A metal that reacts fastest in a small test does not automatically give the best process yield: its undesired reaction, inaccessible surface and product retention may dominate in a reactor.

## Link to other topics

Adsorption equilibria quantify how strongly each species occupies the surface. Diffusion and reaction then determine how much of the internal area can actually contribute.

## Conclusion

Material chemistry supplies the elementary pathway, preparation supplies accessible active sites, and pore geometry supplies transport and selectivity. Their performance changes as the catalyst ages.

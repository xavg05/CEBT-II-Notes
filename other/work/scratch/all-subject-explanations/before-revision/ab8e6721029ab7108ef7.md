# Chromatography and final isolation

## Overview

Chromatography separates components through differences in binding or accessible pore volume. Retention measures describe differential migration, while final isolation converts a purified stream into the physical form needed for storage and use.

*Assumed throughout:* phase partitioning, adsorption and downstream-process stages.

## Section 46: Types of liquid chromatography

### Intuition

Section 45 bound the product to a solid and then released it. Chromatography does the same thing, but *continuously and repeatedly* as the sample travels down a column.

Each solute binds and unbinds many times on its way through. A solute that binds strongly spends more of its time stationary and so moves slowly; one that binds weakly moves quickly. After a long enough column, the difference in average speed separates components that differ only slightly in affinity.

That is the key to why chromatography achieves what a single equilibrium cannot: **a small difference in affinity, applied thousands of times in series, becomes a large difference in position.** Primary isolation methods (Sections 42–45) each give one equilibration and therefore one separation factor. A column gives the same factor repeatedly.

*Analogy:* two walkers of almost equal speed on a long road — indistinguishable over 10 m, far apart over 10 km. The analogy breaks down because the solutes do not move at steady speeds; they alternate between stopped and moving at the eluent's speed, and it is the *fraction of time stopped* that differs.

### Mechanism

**Differential migration.** Chromatography resolves mixtures into individual components by:

1. flowing a sample through a **column packed with resin**, using an **eluent**;
2. different components moving through the resin at **different rates**;
3. components emerging at different **elution times** on the other side, enabling separation.

![Five snapshots down a column: feed applied, then A and B separating into distinct bands as eluent passes, until only A remains](figs/AB-47-differential-migration.png)

The graph of concentration of the components in the effluent against elution time is the **chromatogram**. The resin is the **stationary phase**; the liquid carrying the solutes is the **mobile phase**.

The mobile phase can also be a gas, as in gas chromatography, but **liquid chromatography** is the form relevant to bioprocessing. It achieves high purity and is therefore used for enrichment of bioproducts in the pharmaceutical industry — antibodies, recombinant proteins and nucleic acids used as therapeutics.

#### The five types

Each differs only in **what physical property drives the differential migration**.

**1. Adsorption chromatography** — uses **non-specific adsorption** of compounds against the stationary phase. The phase is typically crystals or particles of **silica gel, alumina, diatomaceous earth** or **charcoal**. Biological molecules adsorb on these materials driven mainly by **electrostatic forces**, and the order of elution depends primarily on **molecular polarity**. The polarity of the eluent (mobile phase) is also important in determining the degree of separation.

*Note:* although the principle is the same, adsorption chromatography is **different from the fixed-bed adsorption of Section 45**, which is a primary isolation method. There the aim is to capture the product and release it in bulk; here it is to resolve similar species by differential migration.

![C8 and C18 alkyl chains bonded to a silica surface, and an electron micrograph of silica beads coated with hydrocarbon chains](figs/AB-46-C18-beads.png)

**2. Partition chromatography** — migration is driven by differential **partitioning between two "liquid" phases**. One liquid phase is immobilised onto a support such as silica, making it the stationary phase. A common stationary phase is **hydrocarbon with 8 or 18 carbons** bonded to silica gel: these are the **C8 and C18 packings**. The second liquid phase is the mobile phase, and common mobile phases are aqueous.

This is the same partition coefficient as Section 42, applied repeatedly rather than once.

![Size-exclusion chromatography: before and after, with small molecules entering the pores of the gel beads while large molecules flow past and elute first](figs/AB-46-gel-principle.png)

**3. Gel chromatography** — also called **molecular-sieve, exclusion, gel filtration** or **gel-permeation chromatography**. The stationary phase is **hydrogel beads of defined pore size**, made of crosslinked **dextran, agarose** or **polyacrylamide**.

Migration rate depends on the **size** of the molecules. Small molecules enter the pores of the gel beads and migrate down the column slowly; large molecules flow past the beads and **leave the column fastest**. This inverts the usual expectation and is the basis of the quantitative treatment in Section 47.

![Ion-exchange chromatography: sample loading, positively charged protein bound to an immobilised anionic surface, then elution with a low and a high salt gradient](figs/AB-46-ion-exchange.png)

**4. Ion-exchange chromatography** — differential migration is caused by **electrostatic interactions** between the stationary phase and the target molecules. For proteins, **pH needs to be kept away from the pI**, so that the proteins are charged.

If the stationary phase is negatively charged and the analyte positively charged, it is **cation-exchange chromatography**:
$$S^-C^+ + A^+B^- \rightarrow S^-A^+ + C^+ + B^- \tag{83}$$
where $S^-$ are the anionic groups on the stationary phase, $A^+$ the target analyte, and $C^+$ and $B^-$ are counterions. The target *swaps places* with the exchangeable cation $C^+$.

If the stationary phase is positively charged and the analyte negatively charged, it is **anion-exchange chromatography**:
$$S^+C^- + A^-B^+ \rightarrow S^+A^- + C^- + B^+ \tag{84}$$

**Elution is accelerated by increasing the salt concentration**, which raises the concentration of competing counterions and displaces the analyte. Ion exchange is used commercially for enrichment of proteins and antibiotics.

**5. Affinity chromatography** — the principle is **specific binding** between the target compound and the stationary phase. Ligands are chemically connected to the stationary phase and specifically bind recombinant proteins, enzymes, antibodies, hormones, nucleic acids and vitamins. It is **highly specific and often used for high-added-value products**.

![Nitrilotriacetic acid chelating a nickel ion, tethered to a silica bead, binding a histidine-tagged protein](figs/AB-46-NiNTA.png)

*Ni-NTA.* A very common approach uses **nitrilotriacetic acid (NTA)** as ligand. NTA forms a complex with **Ni²⁺**, and the Ni-NTA complex binds strongly to **histidine residues**. Target recombinant proteins are purposefully modified to have a **6×His tag** at one end, so that they can be specifically captured by the Ni-NTA complex.

This is why the His₆ tag of Section 24's purification workflow exists: the tag is added at the gene level precisely so that one generic resin can purify any protein.

![An antibody bound by Protein A immobilised on a resin, and a micrograph of Staphylococcus aureus](figs/AB-46-proteinA.png)

*Protein A.* Another common ligand, used for separation of immunoglobulins G. Protein A occurs naturally on the surface of *Staphylococcus aureus*, where it binds IgG from a **conserved region of the heavy chain that is not involved in antigen recognition** — the bacterium uses this to bind IgG the wrong way round, disrupting the immune response. Fc binding makes capture largely independent of antigen specificity, but affinity depends on species and IgG subclass; human IgG3 is a common weak/non-binding exception. The ligand and operating conditions must therefore be checked for the actual antibody.

### Motivation and explanation

**Why combine types.** Each exploits a different molecular property — polarity, partition, size, charge or specific binding — so impurities that resemble the product in one property may differ in another. Antibody purification commonly uses Protein A capture followed by one or more polishing steps such as ion exchange. Size exclusion can remove aggregates, especially at laboratory scale, but its loading and dilution limits mean it is not a universal final step in manufacturing.

**The capacity/selectivity trade.** Affinity can provide strong selectivity at high resin cost. Capacity depends on ligand density, accessible pores and operating conditions; it is not necessarily low. High-resolution size exclusion has a small sample-volume limit, making it useful for polishing suitable partly purified samples. Resin cost and lifetime, loading, resolution and recovery must be compared for the actual process.

**Why gel chromatography differs.** Ideal size exclusion separates by pore access rather than binding. The sample elutes in the running buffer, without a separate change of conditions to desorb it. It generally dilutes the sample and has a bounded ideal elution window. Departures from ideal exclusion require checking for matrix interactions.

### Link to other topics

Repeated equilibration down a column to amplify a small single-stage separation factor is precisely the logic of a distillation column's stages, and the same argument underlies the staged selection of Section 19: one weak discrimination applied many times becomes a strong one.

### Summary

Chromatography separates by differential migration — solutes that bind more spend more time stationary and move more slowly, so a small affinity difference applied repeatedly becomes a large separation in space. The five types differ only in the property exploited: polarity, partition, size, charge or specific binding, with affinity ligands such as Ni-NTA and Protein A giving the highest selectivity.

## Section 47: Quantifying differential migration, and final isolation

### Intuition

A solute's position in the chromatogram is reported as the **elution volume** $V_e$: the volume of eluent that has passed when the solute emerges at peak concentration. Volume is used rather than time because it is independent of flow rate.

In general chromatography the reference is the hold-up volume of an unretained marker. For the size-exclusion treatment here, $V_0$ specifically denotes the interparticle void volume, measured using a fully excluded marker. A smaller non-binding molecule can enter pores and elute later than $V_0$ without adsorbing. The dimensionless quantity $(V_e-V_0)/V_0$ below uses this stated reference.

In ideal size exclusion, pore access rather than binding determines elution. A fully excluded molecule elutes at $V_0$, while a fully permeating noninteracting molecule elutes at $V_0+V_i$. Intermediate molecules have intermediate retention. These bounds assume ideal exclusion without adsorption or other nonideal matrix interactions; real retention is not exactly predictable from nominal pore size alone.

*Analogy:* a crowd moving through a corridor lined with alcoves. People too large to enter any alcove pass straight through; small ones that wander into every alcove take longest. The analogy breaks down because entry here is not a choice but a geometric constraint, which is why the limits are hard.

### Derivation

Notation: $V_e$ elution volume; $V_0$ void volume (between the particles); $V_i$ volume of empty space *within* the particles; $V_s$ volume of the material (hydrogel) making up the particles; $V_t$ total column volume.

#### Capacity factor and retention ratio

**Step 1: capacity factor.** The retention of a solute beyond the void volume, normalised:
$$k = \frac{V_e-V_0}{V_0} \tag{85}$$
$k = 0$ means the solute is unretained and elutes with the void. Larger $k$ means more retention. The normalisation by $V_0$ makes $k$ a property of the solute and the chemistry, not of the column size.

**Step 2: retention ratio.** Comparing two solutes 1 and 2:
$$\delta = \frac{k_1}{k_2} \tag{86}$$
This is a ratio of retention factors, not chromatographic resolution. With the later peak labelled 2, the usual separation factor is $\alpha=k_2/k_1$ for $k_1>0$. Resolution also requires peak widths: using baseline widths $w_1$ and $w_2$ in elution-volume units, $R_s=2(V_{e,2}-V_{e,1})/(w_1+w_2)$. Equal retention factors imply equal peak positions under the stated conditions, but a ratio different from one does not establish resolved peaks.

#### Gel chromatography

**Step 3: the column's volume budget.** The total column volume divides into three parts:
$$V_t = V_0 + V_i + V_s \tag{87}$$
liquid between particles, liquid inside particles, and the solid gel itself.

**Step 4: elution volume.** A solute travelling down the column has access to $V_0$ always, and to a *fraction* of $V_i$ depending on whether it fits into the pores:
$$V_e = V_0 + K_pV_i \tag{88}$$
where $K_p$ is the **partition coefficient**, defined as the fraction of the volume within the gel particles that is available to the solute.

**Step 5: rearrange for the measurable.**
$$K_p = \frac{V_e-V_0}{V_i} \tag{89}$$
So determining $K_p$ requires measuring $V_e$ and knowing $V_0$ and $V_i$.

**The two limits for ideal, noninteracting size exclusion:**
- **$K_p = 0$**: a large macromolecule that does not penetrate the gel particles at all. Then $V_e = V_0$ — it elutes in the void volume, *first*. This also gives the practical route to measuring $V_0$: run a molecule known to be excluded and record its elution volume.
- **$K_p = 1$**: a small solute with full access. Then $V_e = V_0+V_i$ — the latest anything can elute.

Hence $V_0 \le V_e \le V_0+V_i$ under ideal, noninteracting size exclusion. Combining (85) and (88), the capacity factor is
$$k = \frac{K_pV_i}{V_0} \tag{90}$$
so $k$ ranges from 0 to $V_i/V_0$ and cannot exceed it. **Gel chromatography has a bounded retention**, unlike the binding-based methods where strong binding can retain a solute arbitrarily long.

**Step 6: measuring $V_i$.** From the gel's properties:
$$V_i = a\,W_r \tag{91}$$
where $W_r$ is the **water retention value** — the volume of water taken up when rehydrating the gel, per unit dry mass, specified by the manufacturer — and $a$ is the dry mass of gel.

Often the gel is supplied already rehydrated, so $a$ is unknown. In that case:
$$V_i = \frac{W_r\rho_g}{1+W_r\rho_w}\left(V_t-V_0\right) \tag{92}$$
with $\rho_g$ the density of the rehydrated gel and $\rho_w$ the density of water. Note $(V_t-V_0) = V_i+V_s$ from (87): equation (92) splits the non-void volume into pore space and solid in the ratio the gel's water content implies.

### Worked example

*Sizing the elution window of a gel column.* Computed in Python.

**Given.** A column of total volume $V_t = 100$ mL with void volume $V_0 = 30$ mL, packed with a hydrogel of water retention $W_r = 7.5$ mL g⁻¹ and rehydrated density $\rho_g = 1.05$ g mL⁻¹, with $\rho_w = 1.00$ g mL⁻¹.

**Step 1: internal pore volume**, from (92):
$$V_i = \frac{7.5\times1.05}{1+7.5\times1.00}(100-30) = \frac{7.875}{8.5}\times70 = 64.9\ \mathrm{mL}$$
From (87), $V_s = 100-30-64.9 = 5.1$ mL. **The gel matrix is only 5 % of the column volume** — the particles are essentially water held in a sparse polymer network, which is what a hydrogel is.

**Step 2: where solutes elute**, from (88) and (90):

| $K_p$ | $V_e$ (mL) | $k$ | Solute |
|---|---|---|---|
| 0 | 30.0 | 0 | macromolecule, fully excluded |
| 0.2 | 43.0 | 0.43 | large protein |
| 0.5 | 62.4 | 1.08 | medium protein |
| 1.0 | 94.9 | 2.16 | small solute, full access |

**Step 3: read the window.** Everything elutes between **30 and 95 mL**, a window of 64.9 mL — exactly $V_i$, as (88) requires. The last solute emerges at only 3.2 times the volume of the first.

**Step 4: relative retention of two proteins.** For $K_p = 0.2$ and $0.5$, the retention ratio from (86) is
$$\delta = \frac{0.43}{1.08} = 0.40$$
and the peak centres differ by $(0.5-0.2)\times64.9 = 19.5$ mL. The separation factor is $\alpha=1/\delta=2.5$, but $R_s$ cannot be calculated without peak widths.

**What the numbers say about the method.**
- *The sample volume must be small.* The entire separation happens within 65 mL, so injecting even 10 mL of feed would smear the peaks across a sixth of the usable window. This is the fundamental capacity limit of gel chromatography and why it is a **polishing** step, used last when the volume is already small.
- *It generally dilutes the sample.* SEC has no binding stage to accumulate product from a large feed before releasing it in a smaller volume. Band spreading usually increases the collection volume. Binding chromatography can concentrate product under suitable loading and elution conditions, but concentration is not guaranteed by chromatography type.
- *The ideal model is useful, but conditional.* Equation (88) relates retention to an effective pore-partition coefficient. This depends on solute hydrodynamic size and shape and the pore distribution. Buffer composition, pH and temperature can change solute conformation, association, gel swelling or unwanted interactions. Size calibration therefore needs standards and matched conditions.

### Instrumentation

![A high-performance liquid chromatography system and a lower-pressure FPLC system](figs/AB-47-HPLC-FPLC.png)

Two systems carry out chromatographic separations of biomolecules:

**HPLC (high-performance liquid chromatography)** often uses fine particles and sufficiently high pressure to control band spreading. Analytical systems commonly use micrometre-scale particles and low flow rates, but pressure and throughput depend on the column and duty; preparative HPLC also exists. Oligonucleotide purification (Section 06) is one application.

**FPLC (fast protein liquid chromatography)** describes systems designed for protein purification with compatible wetted materials, aqueous buffers, gradient control and fraction collection. They are used from laboratory purification to process development. Resolution depends on the resin, column and operating conditions, rather than being intrinsically lower than HPLC; pressure and flow limits depend on the particular system and column.

The trade is the familiar one: smaller particles give more plates and better resolution but a far larger pressure drop, so resolution is bought with pressure and throughput.

### Final isolation

![Downstream process logic with the final isolation box highlighted: crystallisation, precipitation, ultrafiltration, drying](figs/AB-32-process-logic.png)

The product is already highly purified by chromatography. The objective of **final isolation** is possibly to **increase purity further**, and to **alter the physical form** of the product to make it suitable for storage and commercialisation.

Many products are packaged and sold as **solids or powders**. These go through either **precipitation or crystallisation** (Sections 43–44), followed by **filtration or centrifugation** (Sections 33–37), and the wet solids — crystals or amorphous precipitate — are then **dried**.

The operations are therefore ones already covered; what differs is the purpose. Earlier they were used to *separate*; here they are used to *formulate*.

### Link to other topics

The capacity factor is the chromatographic analogue of a retention or holdup time, and the resolution-versus-pressure trade in HPLC is the same relationship as plate count against pressure drop in a packed column: finer packing improves separation and costs pumping energy.

### Summary

The stated retention factor characterises elution relative to $V_0$, and $\delta=k_1/k_2$ compares retention rather than resolution. Ideal size exclusion gives $V_e=V_0+K_pV_i$ and a bounded elution window, governed by effective pore access under defined conditions.

## Conclusion

Retention describes migration, peak widths determine resolution, and final isolation sets the product form. The next unit develops gene regulation and synthetic circuits.

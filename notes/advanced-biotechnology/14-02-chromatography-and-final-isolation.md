# Chromatography and final isolation — reading 14.2

[Previous](14-01-chromatography-and-final-isolation.md) · [Subject index](README.md) · [Next](15-01-gene-regulation-and-synthetic-circuits.md)

<!-- reading-content:start -->
## Section 47: Quantifying differential migration, and final isolation

### Intuition

A solute's position in the chromatogram is reported as the **elution volume** $`V_e`$: the volume of eluent that has passed when the solute emerges at peak concentration. Volume is used rather than time because it is independent of flow rate.

In general chromatography the reference is the hold-up volume of an unretained marker. For the size-exclusion treatment here, $`V_0`$ specifically denotes the interparticle void volume, measured using a fully excluded marker. A smaller non-binding molecule can enter pores and elute later than $`V_0`$ without adsorbing. The dimensionless quantity $`(V_e-V_0)/V_0`$ below uses this stated reference.

In ideal size exclusion, pore access rather than binding determines elution. A fully excluded molecule elutes at $`V_0`$, while a fully permeating noninteracting molecule elutes at $`V_0+V_i`$. Intermediate molecules have intermediate retention. These bounds assume ideal exclusion without adsorption or other nonideal matrix interactions; real retention is not exactly predictable from nominal pore size alone.

*Analogy:* a crowd moving through a corridor lined with alcoves. People too large to enter any alcove pass straight through; small ones that wander into every alcove take longest. The analogy breaks down because entry here is not a choice but a geometric constraint, which is why the limits are hard.

### Derivation

Notation: $`V_e`$ elution volume; $`V_0`$ void volume (between the particles); $`V_i`$ volume of empty space *within* the particles; $`V_s`$ volume of the material (hydrogel) making up the particles; $`V_t`$ total column volume.

#### Capacity factor and retention ratio

**Step 1: capacity factor.** The retention of a solute beyond the void volume, normalised:

**Equation (85)**

```math
k = \frac{V_e-V_0}{V_0}
```

$`k = 0`$ means the solute is unretained and elutes with the void. Larger $`k`$ means more retention. The normalisation by $`V_0`$ makes $`k`$ a property of the solute and the chemistry, not of the column size.

**Step 2: retention ratio.** Comparing two solutes 1 and 2:

**Equation (86)**

```math
\delta = \frac{k_1}{k_2}
```

This is a ratio of retention factors, not chromatographic resolution. With the later peak labelled 2, the usual separation factor is $`\alpha=k_2/k_1`$ for $`k_1>0`$. Resolution also requires peak widths: using baseline widths $`w_1`$ and $`w_2`$ in elution-volume units, $`R_s=2(V_{e,2}-V_{e,1})/(w_1+w_2)`$. Equal retention factors imply equal peak positions under the stated conditions, but a ratio different from one does not establish resolved peaks.

#### Gel chromatography

**Step 3: the column's volume budget.** The total column volume divides into three parts:

**Equation (87)**

```math
V_t = V_0 + V_i + V_s
```

liquid between particles, liquid inside particles, and the solid gel itself.

**Step 4: elution volume.** A solute travelling down the column has access to $`V_0`$ always, and to a *fraction* of $`V_i`$ depending on whether it fits into the pores:

**Equation (88)**

```math
V_e = V_0 + K_pV_i
```

where $`K_p`$ is the **partition coefficient**, defined as the fraction of the volume within the gel particles that is available to the solute.

**Step 5: rearrange for the measurable.**

**Equation (89)**

```math
K_p = \frac{V_e-V_0}{V_i}
```

So determining $`K_p`$ requires measuring $`V_e`$ and knowing $`V_0`$ and $`V_i`$.

**The two limits for ideal, noninteracting size exclusion:**
- **$`K_p = 0`$**: a large macromolecule that does not penetrate the gel particles at all. Then $`V_e = V_0`$ — it elutes in the void volume, *first*. This also gives the practical route to measuring $`V_0`$: run a molecule known to be excluded and record its elution volume.
- **$`K_p = 1`$**: a small solute with full access. Then $`V_e = V_0+V_i`$ — the latest anything can elute.

Hence $`V_0 \le V_e \le V_0+V_i`$ under ideal, noninteracting size exclusion. Combining (85) and (88), the capacity factor is

**Equation (90)**

```math
k = \frac{K_pV_i}{V_0}
```

so $`k`$ ranges from 0 to $`V_i/V_0`$ and cannot exceed it. **Gel chromatography has a bounded retention**, unlike the binding-based methods where strong binding can retain a solute arbitrarily long.

**Step 6: measuring $`V_i`$.** From the gel's properties:

**Equation (91)**

```math
V_i = a\,W_r
```

where $`W_r`$ is the **water retention value** — the volume of water taken up when rehydrating the gel, per unit dry mass, specified by the manufacturer — and $`a`$ is the dry mass of gel.

Often the gel is supplied already rehydrated, so $`a`$ is unknown. In that case:

**Equation (92)**

```math
V_i = \frac{W_r\rho_g}{1+W_r\rho_w}\left(V_t-V_0\right)
```

with $`\rho_g`$ the density of the rehydrated gel and $`\rho_w`$ the density of water. Note $`(V_t-V_0) = V_i+V_s`$ from (87): equation (92) splits the non-void volume into pore space and solid in the ratio the gel's water content implies.

### Worked example

*Sizing the elution window of a gel column.* Computed in Python.

**Given.** A column of total volume $`V_t = 100`$ mL with void volume $`V_0 = 30`$ mL, packed with a hydrogel of water retention $`W_r = 7.5`$ mL g⁻¹ and rehydrated density $`\rho_g = 1.05`$ g mL⁻¹, with $`\rho_w = 1.00`$ g mL⁻¹.

**Step 1: internal pore volume**, from (92):

```math
V_i = \frac{7.5\times1.05}{1+7.5\times1.00}(100-30) = \frac{7.875}{8.5}\times70 = 64.9\ \mathrm{mL}
```

From (87), $`V_s = 100-30-64.9 = 5.1`$ mL. **The gel matrix is only 5 % of the column volume** — the particles are essentially water held in a sparse polymer network, which is what a hydrogel is.

**Step 2: where solutes elute**, from (88) and (90):

| $`K_p`$ | $`V_e`$ (mL) | $`k`$ | Solute |
|---|---|---|---|
| 0 | 30.0 | 0 | macromolecule, fully excluded |
| 0.2 | 43.0 | 0.43 | large protein |
| 0.5 | 62.4 | 1.08 | medium protein |
| 1.0 | 94.9 | 2.16 | small solute, full access |

**Step 3: read the window.** Everything elutes between **30 and 95 mL**, a window of 64.9 mL — exactly $`V_i`$, as (88) requires. The last solute emerges at only 3.2 times the volume of the first.

**Step 4: relative retention of two proteins.** For $`K_p = 0.2`$ and $`0.5`$, the retention ratio from (86) is

```math
\delta = \frac{0.43}{1.08} = 0.40
```

and the peak centres differ by $`(0.5-0.2)\times64.9 = 19.5`$ mL. The separation factor is $`\alpha=1/\delta=2.5`$, but $`R_s`$ cannot be calculated without peak widths.

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

The stated retention factor characterises elution relative to $`V_0`$, and $`\delta=k_1/k_2`$ compares retention rather than resolution. Ideal size exclusion gives $`V_e=V_0+K_pV_i`$ and a bounded elution window, governed by effective pore access under defined conditions.

## Conclusion

Retention describes migration, peak widths determine resolution, and final isolation sets the product form. The next unit develops gene regulation and synthetic circuits.
<!-- reading-content:end -->

[Previous](14-01-chromatography-and-final-isolation.md) · [Subject index](README.md) · [Next](15-01-gene-regulation-and-synthetic-circuits.md)

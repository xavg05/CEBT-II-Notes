[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Cell disruption

## Overview

Intracellular products require disruption before purification, but breaking cells also releases debris, nucleic acids and degradative enzymes. Mechanical and non-mechanical methods balance release against product damage; release kinetics and a homogeniser fit make that trade quantitative.

*Assumed throughout:* cell structure, material balances and first-order kinetics.

## Section 38: Why cells must be disrupted, and what resists it

### Intuition

Disruption is a deliberately destructive step in the middle of an otherwise careful process, and that is its difficulty. The wall must be broken thoroughly enough to release the product, but the product itself is a fragile molecule sitting in the same vessel — so every method that is good at breaking walls is also, to some degree, good at destroying what it releases.

Worse, breaking the cell releases *everything*: proteases, nucleic acids, lipids, and fragments of wall so small that they are harder to remove than the intact cells were. The step therefore makes the separation problem worse before it makes it better, which is why it is avoided wherever possible by secreting the product instead.

*Analogy:* opening a safe with explosives to recover a document inside. The analogy breaks down because a cell wall is not uniformly strong: it resists by being elastic and chemically crosslinked rather than merely hard, which is why chemical and enzymatic attack (Section 41) can succeed where force is clumsy.

### Mechanism

![Lactococcus lactis engineered to express fluorescent protein, with product accumulating inside the cells](../figs/AB-38-inclusion-bodies.png)

**Why products are intracellular.** Many products of interest — particularly recombinant proteins — are not secreted. They accumulate in the cytoplasm, sometimes as dense **inclusion bodies** at the poles of the cell. Such a product cannot be recovered without breaking the cell, so disruption must precede any isolation or purification.

#### What has to be broken

![Gram-negative bacterial cell wall: inner membrane, periplasm, peptidoglycan layer and an outer membrane carrying lipopolysaccharide, porins and surface proteins](../figs/AB-38-cell-walls.png)

Microorganisms used in bioprocessing are surrounded by tough **cell walls**, and their construction differs by organism:

- **Gram-positive bacteria** (for example *Lactococcus lactis*) have a **thick peptidoglycan wall** — a crosslinked mesh of sugar chains and short peptides, mechanically strong.
- **Gram-negative bacteria** (for example *E. coli*) have a **thinner peptidoglycan wall**, but it is enveloped by an **outer membrane rich in lipopolysaccharide (LPS)**. The wall is weaker but there are more layers to cross, and the LPS matters downstream because it is an endotoxin that must be removed from any injectable product.

![Yeast cell wall: mannoproteins, β-1,6 and β-1,3 glucans and chitin, layered outside the plasma membrane](../figs/AB-38-yeast-wall.png)

- **Yeast** (*Saccharomyces cerevisiae*) has a **thick, multi-layered wall** of polysaccharides — β-1,3 and β-1,6 glucans — together with mannoproteins and **chitin**. This makes yeast **very difficult to disrupt**, and it is the hardest of the common hosts.
- **Mammalian cells** have only a plasma membrane and **no cell wall at all**, so they are easily disrupted. The same fragility that makes them shear-sensitive in the bioreactor (Section 31) makes them trivial to break here.

#### Strategies

Four families of method, in two groups:

**Mechanical** (Section 39):
- bead mill, ultrasonication, French press, high-pressure homogeniser.

**Non-mechanical** (Section 41):
- *physical*: thermolysis, decompression, osmotic shock;
- *chemical*: detergents, solvents;
- *biological*: enzymatic digestion.

Three considerations govern the choice:
1. **Scale.** Some methods are only applicable at small or laboratory scale; others scale to production.
2. **Cell type.** Bacteria and yeast have tough walls and are **more difficult to disrupt by mechanical means only**; bacteria are also small, which makes them harder still. Mammalian cells need little.
3. **Product sensitivity.** Methods differ in how much heat and shear they impose.

**Why size can matter mechanically.** In a Newtonian flow the shear stress is $`\tau=\mu\dot\gamma`$, where $`\dot\gamma`$ is shear rate; stress itself does not grow with cell diameter. Larger cells can experience larger integrated forces and velocity differences across their extent. Rupture also depends on envelope strength, geometry and disruption mechanism, so size alone does not rank susceptibility.

### Motivation and explanation

**Why disruption is avoided when possible.** Three costs follow from breaking cells:
- *Debris.* The fragments are far smaller than intact cells, so the cell-debris removal step that follows (by the same centrifugation or filtration of Sections 33–37) is harder than the original cell removal. Section 36's $`u \propto D_p^2`$ makes this quantitative — halving the fragment size quarters the settling velocity.
- *Released contaminants.* Proteases liberated from the cytoplasm begin degrading the product immediately, which is why disruption is usually done cold (the worked example in Section 40 operates at 5 °C) and why the subsequent steps must be fast.
- *Viscosity.* Released DNA raises the viscosity of the suspension substantially, which slows every downstream separation — again visible in Section 36, where $`u \propto 1/\mu`$.

The preferred alternative is to engineer the host to **secrete** the product, converting an intracellular recovery into a simple cell removal. Where that is not possible, inclusion bodies are sometimes an advantage: they are dense, so they can be recovered by centrifugation after disruption, though the protein must then be refolded.

Breaking the envelope releases a soluble cytoplasmic protein directly into the liquid, but an inclusion-body protein remains in a solid aggregate. In that case disruption exposes the aggregate for collection; it does not itself produce active dissolved protein. Solubilisation and refolding are separate subsequent tasks, and their losses must be included when deciding whether high intracellular expression actually improves final yield.

**Why the wall resists.** Peptidoglycan is a covalently crosslinked network enclosing the whole cell, so it behaves as a single molecule under tension and must be *ruptured*, not merely deformed. It also bears the turgor pressure of the cytoplasm, which in bacteria is several atmospheres — the wall is a pressure vessel, and it is already pre-stressed.

### Wider pathway

Disruption sits between cell removal (Sections 33–37) and primary isolation (Sections 42–45). Its output — a homogenate of product, debris, proteases and nucleic acids — is the feed for everything that follows, and the completeness of disruption sets the ceiling on overall yield.

### Link to other topics

Choosing between mechanical and chemical disruption is the familiar comminution trade-off: force is cheap and indiscriminate, selective chemistry is expensive but gentle, and the right balance depends on how much the valuable component tolerates.

### Summary

Intracellular products require the cell to be broken, but disruption releases debris, proteases and DNA that make every subsequent separation harder. Difficulty is set by the host: yeast walls of glucan and chitin are the toughest, Gram-positive bacteria have thick peptidoglycan, Gram-negative bacteria are weaker but layered, and mammalian cells have no wall at all.

## Section 39: Mechanical cell disruption and release kinetics

### Intuition

Every mechanical method does the same thing: impose a stress on each cell large enough to rupture its wall. They differ only in how the stress is generated — grinding between beads, collapsing bubbles, or acceleration through a narrow gap.

The key to the kinetics is that **each cell is broken independently**. A pass through the equipment gives every intact cell the same probability of rupture, regardless of how many have already broken. The number of intact cells therefore falls by a constant *fraction* per pass, which is a first-order process. Release of product is the mirror image: it approaches its maximum exponentially.

If a pass leaves a constant fraction of the previously unreleased material behind, repeating the pass multiplies that fraction again. Taking its logarithm converts this repeated multiplication into a quantity proportional to pass count, which is why the residual, rather than the released amount, is plotted on a logarithmic scale. The continuous derivative in (69) is a compact representation of that discrete survival law; the actual process still uses whole passes.

In the fixed-fraction model, one pass leaves some unreleased material. A single pass can still meet a practical recovery target; the model approaches complete release only asymptotically. Real rupture probabilities and product losses can change that behaviour.

*Analogy:* radioactive decay, where each nucleus has a fixed probability of decaying per unit time independent of the others. The analogy breaks down because cells are not identical: a population has a distribution of wall strengths, so the weakest break first and the surviving population becomes progressively tougher, making the real decay slightly slower than exponential.

### Mechanism

All mechanical methods **produce substantial heat** that can damage the product, so all of them **need cooling**.

![A bead mill: a jacketed chamber filled with glass beads, agitated by rotating impellers, with coolant inlet and outlet, and an inset showing cells ground between rolling beads](../figs/AB-39-bead-mill.png)

**Bead mill.** A chamber filled with beads — typically glass, 0.2–1.0 mm diameter — packed to up to 80 % of the free volume, with impellers rotating at 1500–2250 rpm. Cells at 30–60 % volume wet solids are ground between the rolling beads. Cooling is through a jacket. Scales to industrial use.

![Ultrasonication: an ultrasound generator drives a sonotrode immersed in the cell suspension](../figs/AB-39-ultrasonication.png)

**Ultrasonication.** Ultrasonic vibrations at about 20 kHz are produced by an immersion probe. The high-energy pressure waves create **cavitation bubbles**, whose collapse disrupts the cells — the damage is done by the implosion, not by the sound itself. Bacteria are disrupted in 30–60 s, yeast in 2–10 minutes. It works well at small and laboratory scale but is **difficult to scale up**, because of the high energy demand and safety concerns about exposure to ultrasound.

![A Gaulin-type homogeniser valve: pressurised cell suspension is forced through a narrow gap between valve and valve seat, then strikes an impact ring](../figs/AB-39-homogeniser-valve.png)

**High-pressure homogeniser.** The standard industrial method.
- Cells are put under **high pressure, 1500–2500 bar**.
- The pressure is **suddenly released** by a valve opening, forcing the cells to flow at high speed through a small gap.
- The cells then collide with an **impact ring**, causing disruption.
- Semi-continuous, usable at laboratory and industrial scale.
- **Multiple passes** are usually required. This can be done with a multi-tank arrangement, feeding from one tank, homogenising and collecting into the other. Tough cells such as *L. lactis* (ovoid, Gram-positive) need several passes.

![A French press: a plunger forces the cell suspension in a cylinder through a narrow orifice, forming a jet that strikes an impact plate](../figs/AB-39-french-press.png)

**French press.** A simpler version of the same principle, suitable for **laboratory scale only**. Pressure is applied and the cells forced through a small hole at high speed, hitting an impact plate. Its extraction efficiency is described by the **same equation** as the high-pressure homogeniser.

### Derivation

Notation: $`R`$ is the protein released (kg per kg biomass), $`R_{\max}`$ the maximum achievable release, $`N`$ the number of passes, $`t`$ processing time, $`p`$ the operating pressure.

**Step 1: first-order release.** Each pass ruptures a fixed fraction of the cells that remain intact. The *unreleased* protein $`(R_{\max}-R)`$ therefore decays by a constant factor per pass:

**Equation (69)**

```math
\frac{d(R_{\max}-R)}{dN} = -k'(R_{\max}-R)
```


**Step 2: integrate** from $`R = 0`$ at $`N = 0`$:

**Equation (70)**

```math
\ln\!\left(\frac{R_{\max}}{R_{\max}-R}\right) = k'N
```


For a **bead mill**, where the variable is processing time rather than discrete passes, the same argument in continuous time gives

**Equation (71)**

```math
\ln\!\left(\frac{R_{\max}}{R_{\max}-R}\right) = kt
```

with $`k`$ a constant depending on bead size, bead packing density, rotation speed and temperature.

**Step 3: the pressure dependence.** For a homogeniser, $`k'`$ is not a constant: raising the pressure increases the stress on each cell and so the fraction broken per pass. Empirically the dependence is a power law, $`k' = kp^{\,a}`$, giving

**Equation (72)**

```math
\boxed{\;\ln\!\left(\frac{R_{\max}}{R_{\max}-R}\right) = kNp^{\,a}\;}
```

where $`k`$ is a constant depending on cell type and temperature, $`p`$ the applied pressure, and $`a`$ an **exponent depending on cell toughness**, ranging from about 0.9 to 2.9.

**Rearranged for release:**

**Equation (73)**

```math
\frac{R}{R_{\max}} = 1 - e^{-kNp^{\,a}}
```


**Checks.** At $`N = 0`$, $`R = 0`$. As $`N\to\infty`$, $`R\to R_{\max}`$: complete release needs infinite passes, as the intuition predicted. Release is **linear in $`N`$ only at small $`N`$**, where $`e^{-x}\approx 1-x`$.

### Motivation and explanation

**What the exponent measures.** The exponent $`a`$ describes pressure sensitivity within the fitted range; it does not rank toughness on its own, because $`k`$, the release target and the envelope all matter. Since the model exponent is $`kNp^a`$, for $`a>1`$ a given proportional pressure increase changes predicted release more than the same proportional increase in passes. That mathematical comparison does not determine the best energy or product-stability trade-off.

**Why multiple passes rather than one hard pass.** Equation (72) suggests either route works, but there are limits: the equipment has a maximum rated pressure, and higher pressure means more heat, so the product suffers. Multiple passes allow cooling between treatments, which can reduce peak temperature. The total dissipated energy is not automatically the same: it depends on pressure, processed volume and pass count.

**Where the model fails.**
- $`R_{\max}`$ is itself an assumption: some protein is never released, remaining bound to debris.
- A real population has a **distribution of wall strengths**, so the weakest cells break first and the survivors are tougher. Observed curves therefore fall slightly below the exponential at high $`N`$.
- Prolonged treatment degrades the released protein, so measured $`R`$ can *fall* at very high $`N`$ — the model has no term for this.
- $`k`$ depends on temperature, so a run without adequate cooling does not have a single $`k`$.

### Link to other topics

Equation (70) has the same exponential-survival structure as a cascade with a fixed fractional removal per stage, or the log-survival law in sterilisation: a fixed fractional reduction per unit of effort gives a logarithm of the residual, and the quantity that scales linearly is $`\ln`$ of what is left.

### Summary

Mechanical methods all impose stress to rupture walls, and all generate heat that must be removed. Because each cell breaks independently with a fixed probability, release follows first-order kinetics, equation (72), with pressure entering as $`p^{\,a}`$ and $`a`$ between 0.9 and 2.9 depending on cell toughness.

## Section 40: Worked example — fitting and using homogeniser kinetics

### Intuition

The model has two unknowns multiplied together inside an exponential, which cannot be read off directly. The standard route is to linearise twice.

First, at **fixed pressure**, equation (72) is linear in $`N`$ through the origin, so the slope of $`\ln[R_{\max}/(R_{\max}-R)]`$ against $`N`$ gives the product $`kp^{\,a}`$ for that pressure. Doing this for each pressure gives one slope per pressure.

Second, taking logarithms of those slopes, $`\ln(kp^{\,a}) = \ln k + a\ln p`$, which is linear in $`\ln p`$. The gradient is $`a`$ and the intercept is $`\ln k`$.

Two straight-line fits, each extracting one constant. This is the general recipe whenever a power law sits inside an exponential.

### Motivation and explanation

**Why the two-stage fit is the right approach.** Fitting $`k`$ and $`a`$ simultaneously to all 29 data points by non-linear regression would also work, but the staged version is better practice: the first stage *tests* the model (do the lines pass through the origin and stay straight?) before the second stage extracts parameters. A curved line at one pressure would reveal a failure of first-order kinetics that a global fit would silently absorb into the parameters.

**What $`a = 2.37`$ means in design terms.** Since $`a > 1`$, pressure is a stronger lever than passes, as Section 39 predicted. Quantitatively, from (72):
- doubling $`N`$ doubles $`\ln[R_{\max}/(R_{\max}-R)]`$;
- doubling $`p`$ multiplies it by $`2^{2.37} = 5.2`$.

**Doubling pressure multiplies the effective pass count by about 5.2** in the fitted model: one pass at doubled pressure has the same predicted release as about 5.2 passes at the original pressure. This conditional comparison does not justify extrapolating the 200–550 $`\mathrm{kg}_f`$ cm⁻² fit to 1500–2500 bar.

**The trade-off that the model does not contain.** Higher pressure means more energy dissipated as heat per pass, so more cooling duty and more risk of denaturing the product — and the equipment must be rated for it. Fewer passes means less total residence time with released proteases. The model gives the disruption; the choice between the two routes depends on product stability and capital cost, which it says nothing about.

**Limits of the extrapolation.** The fit covers 200–550 $`\mathrm{kg}_f`$ cm⁻² and 1–6 passes. Part (b) extrapolates slightly in pressure, which is acceptable. Extrapolating to much higher pressure would not be: cavitation and temperature rise change the mechanism, and $`R_{\max}`$ itself may fall as the released protein is damaged.

### Link to other topics

The two-stage linearisation — hold one variable, fit the other, then fit the parameters of that fit — is the standard way to resolve a rate law of the form $`r = kC_A^{\alpha}C_B^{\beta}`$ from kinetic data, and the reasoning is identical: isolate one dependence at a time.

### Summary

Converting the data to $`\ln[R_{\max}/(R_{\max}-R)]`$ linearises the release law in $`N`$; the slopes then linearise in $`\ln p`$, giving $`a = 2.37`$ and $`k = 1.73\times10^{-7}`$ with $`R^2 = 0.9994`$. Five passes reach 80 % release at 460 $`\mathrm{kg}_f`$ cm⁻², and 570 $`\mathrm{kg}_f`$ cm⁻² reaches 70 % in two.

## Section 41: Non-mechanical cell disruption

### Intuition

A wall can be broken by overwhelming it, or by removing what holds it together. Mechanical methods do the first. The non-mechanical methods do the second, and they divide naturally by *which* component they attack:

- **Physical** methods make the cell break *itself*, by creating a pressure difference across the envelope that it cannot withstand — by heating and damaging the envelope, by expanding dissolved gas inside it, or by drawing water in osmotically.
- **Chemical** methods dissolve the lipid membrane, which is held together only by the hydrophobic effect and so is vulnerable to anything surface-active.
- **Biological** methods cleave selected covalent bonds in wall components enzymatically. For example, lysozyme cuts glycosidic bonds in the peptidoglycan backbone, rather than its peptide crosslinks. Enzyme specificity makes this attack more targeted.

The pattern across all three is **specificity bought at a price**. Each is gentler and more targeted than a homogeniser, and each introduces something that must later be removed — heat damage, added salt, detergent, solvent, or enzyme — or is simply too expensive at scale.

*Analogy:* opening a locked door by force, by removing its hinges, or with the correct key. The key is cleanest but must be obtained and accounted for afterwards. The analogy breaks down because a detergent does not unlock anything selectively — it dissolves the membrane wholesale, and it is "selective" only in the sense that it attacks lipid rather than protein.

### Mechanism

#### Physical methods

These include thermal, decompression and osmotic shock. They are generally **costly and difficult to scale up**, so they are used mostly at laboratory rather than production scale.

**Thermolysis.** Cells are disrupted by **heating** — cytoplasmic proteins can be extracted from *E. coli* by holding at 90 °C for 10 minutes. Alternatively, **freeze–thaw cycles** disrupt cells through the formation of **ice crystals** that puncture membranes and walls. Both are **energy intensive**, and heating obviously risks denaturing the product, so thermolysis suits only thermostable products.

**Decompression.** Cells are exposed to a **high-pressure gas**, which dissolves in the medium and distributes itself inside the cells. On **rapid decompression**, the gas within the cells expands and bursts them from the inside.

![A decompression chamber with pressure gauges](../figs/AB-41-decompression.png)

The mechanism is worth noting: the disruptive force is generated *inside* the cell, so the wall fails in tension from within rather than being crushed. This is gentler than homogenisation because there is no shear field acting on the released protein.

![Red blood cells in hypertonic, isotonic and hypotonic solution: shrunken, normal, and swollen to bursting, with water flowing out or in](../figs/AB-41-osmotic-shock.png)

**Osmotic shock.** Cells are exposed to **hypertonic** or **hypotonic** conditions.
- *Hypertonic* conditions are obtained by adding salts at 1–3 M concentration, causing the cells to **shrink** rapidly as water leaves the cytoplasm.
- *Hypotonic* conditions draw water into cells. Wall-free cells such as red blood cells can swell and lyse, but intact bacterial and yeast walls usually resist the load. Efficient microbial release often needs envelope weakening or a specific osmotic-shock protocol.

The two are often used in sequence — shrink, then swell — since the mechanical cycling weakens the envelope. The method is **not sufficiently efficient for production scale**, and the added salt must afterwards be removed, which adds cost.

#### Chemical methods

Non-physical methods disrupt cell walls and membranes by adding chemical substances (**solvents**, **detergents**) or biological agents (**enzymes**). Several can be combined to achieve the desired efficiency. The drawback compared with physical methods is the **cost of the substances used, and that they may need to be removed**.

![A detergent solubilising a lipid bilayer into mixed micelles of detergent with lipids and proteins, releasing DNA](../figs/AB-41-detergent.png)

**Detergents.** Detergents, or **surfactants**, solubilise the phospholipid cell membrane through **micellisation** and by solubilising membrane proteins. Typical detergents are **sodium dodecyl sulfate (SDS)** and **Triton X-100**. They may need to be removed for later processing stages, adding to cost. Commonly used at laboratory scale for RNA or DNA extraction.

**Solvents.** Alcohols, dimethyl sulfoxide, methyl ethyl ketone and toluene solubilise the lipid components of the membrane, disrupting it. Like detergents, they may need removal. Solvents **may cause denaturation** of target proteins, which is often undesirable. They are sometimes combined with alkaline compounds to hydrolyse the cell wall as well as the membrane.

#### Biological methods

**Enzymes** digest cell walls. Those used include **lysozyme, cellulase, protease, chitinase and pectinase**.

The defining feature is **specificity**: different enzymes digest different parts of the wall, matched to the organism's chemistry (Section 38).
- **Lysozyme** hydrolyses the **peptidoglycan** layer in bacteria.
- **Chitinase** targets the **chitin** in yeast cell walls.
- **Pectinase** is used for plant cell walls.

Enzymes can be **combined with detergents**. For Gram-negative bacteria, lysozyme treatment follows detergent treatment, which is used to remove the outer membrane and expose the peptidoglycan layer underneath — a direct consequence of the layered architecture in Section 38: the detergent handles the lipid outer membrane, the enzyme handles the peptidoglycan.

An enzyme can only cleave bonds it can reach. Weakening an outer permeability barrier first can make a wall-digesting enzyme effective without changing that enzyme's chemistry. Conversely, removing membrane lipids does not necessarily sever the load-bearing peptidoglycan or glucan network. Matching both access and bond specificity explains why combined treatments can work when either treatment alone gives little release.

Enzymes are **costly**, which limits their application in production-scale processes.

### Motivation and explanation

**Why these methods do not scale.** Each has a specific obstacle:
- *Thermolysis and freeze–thaw* are energy intensive, and the energy scales with the volume processed.
- *Decompression* requires a pressure vessel large enough for the batch, and the gas must be compressed.
- *Osmotic shock* needs molar quantities of salt per batch, then needs it all removed.
- *Detergents and solvents* are consumables, and removal is a further separation step.
- *Enzymes* are the most expensive reagents of all.

Mechanical methods can offer high throughput with reusable equipment. Their energy and cooling requirements still grow with processed volume, while non-mechanical routes incur reagent, recovery and equipment costs. Production-scale choice therefore follows an engineering and economic comparison, rather than a universal claim that only mechanical methods scale.

**Where non-mechanical methods win.** Three cases:
1. *Fragile products* that cannot survive shear or heat.
2. *Selective release* — mild osmotic shock can release periplasmic contents from Gram-negative bacteria without breaking the inner membrane, so the product comes out with far fewer contaminants. This is a real purification advantage, not just a gentler disruption.
3. *Small scale*, where consumable cost is irrelevant and convenience dominates.

**Combinations are normal.** The methods are not exclusive. A common industrial compromise is a mild chemical or enzymatic pre-treatment to weaken the wall, followed by fewer homogeniser passes — reducing both reagent cost and the heat and shear load.

### Link to other topics

The choice between a capital-intensive mechanical route and a consumable-intensive chemical one is a standard operating-cost comparison: equipment cost is largely independent of throughput once installed, while reagent cost scales linearly with it, so the crossover sits at a particular production volume.

### Summary

Non-mechanical disruption can damage envelopes by heat or pressure changes, solubilise membranes chemically, or digest wall components enzymatically. Heating, SDS and solvents can denature products, while appropriate enzymes or controlled osmotic shock can be selective.

## Conclusion

Disruption recovery must be assessed alongside the damage and contaminants introduced by the release operation. The next unit develops primary isolation.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

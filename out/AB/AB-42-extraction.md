# Section 42: Primary isolation by solvent and aqueous two-phase extraction

## Overview

**Primary isolation** is the third downstream stage (Section 32): removing components with substantially *different* properties from the product. It is not very selective, and it depends on the chemical and physical properties of the product. This note covers the two extraction methods — **solvent extraction** and **aqueous two-phase extraction (ATPE)** — and derives the yield expression that governs both.

*Assumed:* the downstream stages and their ordering logic (Section 32); partition between phases; the γ–φ view of liquid–liquid equilibrium from Equilibrium Thermodynamics.

## Intuition

After cell removal and disruption, the feed is either a liquor with the organisms removed or a cell homogenate. The target — a protein, peptide or small molecule such as an antibiotic — sits in solution alongside a great many unwanted components.

Extraction exploits the fact that different molecules distribute differently between two immiscible liquids. Shake the feed with a second liquid in which the product is much more soluble than the impurities are, let the phases separate, and the product moves across while most contaminants stay behind.

The limitation is that one equilibration can never be complete. The product distributes according to a fixed ratio, so some always remains in the original phase. The design question is therefore not "does it partition?" but "**how much do I recover, and at what phase ratio?**" — which the derivation below answers.

*Analogy:* washing a stain with a solvent in which it dissolves better than water does. The analogy breaks down in the way that matters for proteins: an organic solvent that dissolves a protein well usually also denatures it, which is exactly why the aqueous variant exists.

## Mechanism

### Solvent extraction

![An aqueous feed is mixed with extraction solvent in a separating funnel, shaken, and the layers allowed to separate](figs/AB-42-solvent-extraction.png)

- The aqueous feed contains a target organic compound A.
- It is mixed with an **organic solvent, immiscible with the aqueous feed**, within which A preferentially partitions.
- The system is agitated to allow transfer of A to the solvent, then left to settle.
- The two phases are separated, and A is recovered from the solvent, for example by evaporation.

The solvent is chosen so that **A partitions strongly within it, but undesirable compounds in the feed (such as cell debris) do not**. Selectivity comes entirely from that choice.

Penicillin is the standard example: extracted from aqueous broths using butyl or amyl acetate.

![A countercurrent centrifugal extractor, with light and heavy phase outlets](figs/AB-42-countercurrent.png)

**At plant scale** the operation is continuous rather than batch. A **countercurrent centrifuge** is used: the heavy phase (typically the feed) is mixed with the light phase (typically the solvent) by agitators at the bottom, enabling transfer of the target compound from one phase to the other, and a centrifuge then separates and recovers the two phases. Countercurrent contact gives many equilibrium stages in one unit, so the recovery is far better than a single equilibration.

### Aqueous two-phase extraction

![Two aqueous two-phase systems: a PEG-rich phase over a salt-rich phase, and a PEG-rich phase over a dextran-rich phase](figs/AB-42-ATPE-phases.png)

Similar in principle to solvent extraction, but the liquid–liquid phase separation is between **two aqueous phases** rather than organic phases. Both phases are mostly water, so a protein is not exposed to an organic solvent at any point.

- Phase separation is induced by adding solutes such as **polymers of different chemistry**, and salts.
- Solutions containing **polyethylene glycol (PEG) and salts** separate into salt-rich and PEG-rich phases (PEG on top).
- Solutions of **PEG and dextran** separate into PEG-rich and dextran-rich phases (dextran-rich at the bottom).
- Target compounds partition into one or the other phase depending on their physical and chemical characteristics.
- The degree of partitioning can be **finely tuned** by changing the system composition — adding salts, changing the polymer molecular weight.
- It is **easily scalable**.

It is often used in pharmaceutical processing, for example for monoclonal antibodies, growth factors and hormones.

## Derivation

Notation: $C_{A,u}$ and $C_{A,l}$ are the equilibrium concentrations of A in the upper and lower phase; $V_u$, $V_l$ the phase volumes; $V_0 = V_u + V_l$ the total volume; $C_{A,0}$ the average concentration of A in the system.

**Step 1: the partition coefficient.** At equilibrium, A distributes between the phases in a fixed ratio:
$$K = \frac{C_{A,u}}{C_{A,l}} \tag{1}$$
This applies both to aqueous–solvent and to aqueous–aqueous systems. $K$ is set by the relative affinity of A for the two phases — in thermodynamic terms, by the ratio of its activity coefficients.

**Step 2: define the yield.** The yield in the upper phase is the fraction of all A that ends up there:
$$Y_{A,u} = \frac{V_uC_{A,u}}{V_0C_{A,0}} = \frac{V_uC_{A,u}}{V_uC_{A,u}+V_lC_{A,l}} \tag{2}$$
using a mass balance on A, since all of it is in one phase or the other.

**Step 3: eliminate $C_{A,l}$** using (1), writing $C_{A,l} = C_{A,u}/K$:
$$Y_{A,u} = \frac{V_uC_{A,u}}{V_uC_{A,u}+V_lC_{A,u}/K}$$
Cancelling $C_{A,u}$ throughout and dividing top and bottom by $V_l$:
$$\boxed{\;Y_{A,u} = \frac{\dfrac{V_u}{V_l}}{\dfrac{V_u}{V_l}+\dfrac{1}{K}}\;}\tag{3}$$

**The yield depends on only two quantities:** the **phase-volume ratio** $V_u/V_l$ and the **partition coefficient** $K$. The concentration drops out entirely.

**Checks.**
- $K\to\infty$ (A has no affinity for the lower phase): $Y\to1$, complete recovery.
- $V_u/V_l\to\infty$: $Y\to1$ — a large enough extracting phase recovers everything, whatever $K$.
- $V_u/V_l\to0$: $Y\to0$.

A similar expression can be written for the lower phase.

## Motivation and explanation

**What (3) says about design.** A very large or very small $K$ is desirable for good separation, but if $K$ is fixed by chemistry, the **phase volume ratio can still be tuned**. The yield can be increased simply by using more of the extracting phase.

But this is a trade with concentration. Recovering into a large upper phase gives high yield and a *dilute* product, and the downstream train must then handle that volume (Section 32: every unit is sized for the flow reaching it). Recovering into a small phase concentrates the product but leaves much of it behind. The worked example makes the size of this trade explicit.

**Why ATPE rather than solvent extraction for proteins.** An organic solvent denatures most proteins, so the classical method works only for robust small molecules such as antibiotics. Both phases in ATPE are aqueous, so the protein stays hydrated and folded throughout. The price is that the phase-forming agents — PEG, dextran, large quantities of salt — must themselves be removed later, and dextran in particular is expensive.

**Where extraction sits in the train.** It is a primary isolation method, so it is **not very selective**: it removes components with substantially different properties and is expected to take the product from roughly 1 % to 10 % purity (Section 32). Fine separation from similar impurities is left to chromatography.

## Worked example

*Enzyme recovery by aqueous two-phase extraction.* Computed in Python.

Aqueous two-phase extraction is used to recover α-amylase from solution. A PEG–dextran mixture is added and the solution separates into two phases: PEG-rich upper and dextran-rich lower. The partition coefficient is $K = C_{A,u}/C_{A,l} = 4.2$. Find the maximum possible enzyme recovery when the volume ratio of upper to lower phase is (a) 5.0 and (b) 0.5.

Using (3):

**(a)** $V_u/V_l = 5.0$:
$$Y_{A,u} = \frac{5.0}{5.0+1/4.2} = \frac{5.0}{5.238} = 0.95$$

**(b)** $V_u/V_l = 0.5$:
$$Y_{A,u} = \frac{0.5}{0.5+1/4.2} = \frac{0.5}{0.738} = 0.68$$

**Interpretation.** The yield is much higher in case (a), where the volume of the upper phase is in large excess compared with the lower phase. A tenfold change in phase ratio moves the recovery from 68 % to 95 %.

**The trade this hides.** In (a) the product is recovered into five volumes of upper phase; in (b) into half a volume. The enzyme in (a) is therefore ten times more dilute than in (b), despite 95 % recovery. Taking a basis of 1 unit of lower phase and unit feed concentration, the upper-phase concentration is $0.95/5 = 0.19$ in case (a) against $0.68/0.5 = 1.36$ in case (b) — a factor of 7 in favour of the smaller phase.

**This is the central tension of primary isolation:** recovery and concentration pull in opposite directions, and Section 32's purity table (concentration rising at every step) means a step that dilutes the product has to justify itself on purity alone.

## Link to other topics

Equation (1) is the distribution coefficient of liquid–liquid extraction, and from Equilibrium Thermodynamics it is the ratio of activity coefficients of the solute in the two phases. The countercurrent arrangement is the standard device for turning a modest single-stage separation factor into a high overall recovery.

## Conclusion

Extraction moves the product into a second liquid phase in which it preferentially partitions, with yield set by only $K$ and the phase-volume ratio, equation (3). Aqueous two-phase systems replace the organic solvent with a second aqueous phase, so proteins are not denatured, at the cost of phase-forming agents that must later be removed. Raising the phase ratio raises recovery but dilutes the product. Section 43 turns to precipitation, which concentrates rather than dilutes.

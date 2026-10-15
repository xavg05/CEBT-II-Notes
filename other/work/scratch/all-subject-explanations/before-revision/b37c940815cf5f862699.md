[Previous](<AB-03 - Two-state hybridisation and DNA melting.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-05 - Hybridisation kinetics.md>)

<!-- note-content:start -->
# Section 04: The nearest-neighbour model

## Intuition

Most of the stability of a duplex comes from **stacking**: the attraction between one flat base pair and the next one above it. The energy of a stacking contact depends on *both* pairs in the contact, just as the strength of a joint depends on both bricks it joins. So the natural unit is a "pair of base pairs" (a *dinucleotide step*). A duplex of $`N`$ bp has $`N-1`$ steps, and its $`\Delta G^0`$ is the sum over these steps, plus a cost for starting the duplex at all.

*Analogy:* the energy of a brick wall made of bricks of four sizes, where the mortar strength depends on which two bricks meet. Counting bricks alone would miss this. The analogy breaks down because interactions in a real duplex reach beyond nearest neighbours (and the model has no term for this), and because the "mortar" (salt) also changes the entropy.

## Derivation

**Step 1: decomposition.** The model assumes that a base pair's contribution depends only on its immediate neighbours. The free energy is then a sum of step terms plus ends:

**Equation (14)**

```math
\Delta G^0 = \sum_{i=1}^{10} n_i\,\Delta G_i^0 + \Delta G^0_{\text{init}} + \Delta G^0_{\text{sym}}, \qquad \Delta G^0_i = \Delta H^0_i - T\Delta S^0_i
```

where $`n_i`$ is the number of times step $`i`$ occurs. The same sum is written for $`\Delta H^0`$ and for $`\Delta S^0`$ separately.

**Step 2: why there are 10 steps.**
- There are $`4\times4=16`$ ordered dinucleotides on the top strand.
- A step read on the top strand, 5′-XY-3′, is the same physical stack as its reverse complement read on the bottom strand. For example, 5′-TC-3′ on top sits opposite 5′-GA-3′ on the bottom, so TC/AG ≡ GA/CT.
- Four dinucleotides are their own reverse complements (AT, TA, CG, GC). The other 12 form 6 pairs. That gives $`4 + 6 = 10`$ unique steps.
- *Look-up rule:* if a step is not in the table, look up its reverse complement.

**Step 3: initiation.** Bringing two strands together to form the *first* pair costs translational and rotational entropy without any stacking yet. This is the bimolecular penalty of Section 03 at the molecular level. In the "unified" parameter set, it is assigned to the two terminal pairs: a terminal G·C and a terminal A·T have different values (A·T ends also fray more).

**Step 4: symmetry.** A self-complementary strand (for example ATCGAT) pairs with an identical copy. The two strands are indistinguishable, so the duplex has a twofold rotational symmetry, which halves the number of distinguishable bound states. That is a factor of ½ in $`K`$, i.e. $`\Delta S^0_{\text{sym}} = R\ln\tfrac12 = -1.38`$ cal K⁻¹ mol⁻¹ (tabulated as −1.4), and $`\Delta H^0_{\text{sym}}=0`$. The correction is purely entropic.

**Step 5: salt.** Cations screen the repulsion between backbones (Section 01). Raising [Na⁺] makes the duplex more stable through the *entropy* term, since ion release and condensation are mostly entropic, while $`\Delta H^0`$ is nearly salt-independent. A commonly used correction from the 1 M reference is:

**Equation (15)**

```math
\Delta S^0[\mathrm{Na^+}] = \Delta S^0[1\,\mathrm{M}] + 0.368\,N\ln[\mathrm{Na^+}]
```

in cal K⁻¹ mol⁻¹, with $`N`$ = (number of phosphates in the duplex)/2 and [Na⁺] in M. Divalent cations (Mg²⁺) stabilise far more strongly per mole and need separate corrections.

**Parameters** (unified set, 1 M NaCl; $`\Delta H^0`$ in kcal/mol, $`\Delta S^0`$ in cal K⁻¹ mol⁻¹):

| Step | $`\Delta H^0`$ | $`\Delta S^0`$ | | Step | $`\Delta H^0`$ | $`\Delta S^0`$ |
|---|---|---|---|---|---|---|
| AA/TT | −7.9 | −22.2 | | CT/GA | −7.8 | −21.0 |
| AT/TA | −7.2 | −20.4 | | GA/CT | −8.2 | −22.2 |
| TA/AT | −7.2 | −21.3 | | CG/GC | −10.6 | −27.2 |
| CA/GT | −8.5 | −22.7 | | GC/CG | −9.8 | −24.4 |
| GT/CA | −8.4 | −22.4 | | GG/CC | −8.0 | −19.9 |
| Init. terminal G·C | 0.1 | −2.8 | | Init. terminal A·T | 2.3 | 4.1 |
| Symmetry | 0 | −1.4 | | | | |

Notation: XY/X′Y′ means 5′-XY-3′ on the top strand paired with 3′-X′Y′-5′ on the bottom.

## Motivation and explanation

- **Why the parameters look as they do.**
  - Steps containing G·C are most stable (CG/GC: $`\Delta G^0_{37} \approx -2.2`$ kcal/mol), and TA/AT is least stable ($`\approx -0.6`$). The order is not simply "count the hydrogen bonds": CG/GC and GC/CG contain the same pairs but differ by 0.4 kcal/mol, because the bases overlap differently when stacked. This is exactly why single-pair models fail.
  - Every step has $`\Delta H^0\approx -8`$ kcal/mol and $`\Delta S^0\approx -22`$ cal K⁻¹ mol⁻¹, so $`T\Delta S^0`$ largely cancels $`\Delta H^0`$. Small errors in each partly cancel in $`\Delta G^0`$, which is why $`\Delta G^0_{37}`$ is predicted better than $`\Delta H^0`$ or $`\Delta S^0`$ alone.
- **Accuracy and limits.**
  - For short oligos at 1 M Na⁺, predicted $`T_m`$ values are typically within about 2 °C of measurement.
  - The parameters are fitted, and only 8 combinations of the 10 steps are independent for long polymers.
  - Separate parameter sets exist for RNA:RNA, DNA:RNA, mismatches, dangling ends and wobble pairs.
  - The two-state assumption still applies, so the model is reliable only for short duplexes.
  - Software (NUPACK, for example) applies the full model, including secondary structure in the single strands.

## Worked example

Predict $`T_m`$ for 5′-GTATTTGGCTGT-3′ with its complement 5′-ACAGCCAAATAC-3′, each strand at 1 µM. Computed in Python.

**Steps** (11 for a 12-mer), with reverse complements used where needed:

GT · TA · AT · TT(=AA/TT) · TT(=AA/TT) · TG(=CA/GT) · GG · GC · CT · TG(=CA/GT) · GT

The free-energy contributions at 37 °C range from −0.59 kcal/mol (TA) to −2.23 kcal/mol (GC).

**Sums.**
- Stacks: $`\Delta G^0_{37} = -14.67`$ kcal/mol.
- Initiation: +0.97 (terminal G·C, 5′ end) and +1.03 (terminal A·T, 3′ end).
- The sequence is not self-complementary, so there is no symmetry term.

| Quantity | 1 M Na⁺ | 0.15 M Na⁺, from (15) with $`N = 11`$ |
|---|---|---|
| $`\Delta H^0`$ (kcal/mol) | −87.2 | −87.2 |
| $`\Delta S^0`$ (cal K⁻¹ mol⁻¹) | −240.3 | −248.0 |
| $`\Delta G^0_{37}`$ (kcal/mol) | −12.67 | −10.29 |
| $`T_m`$ (Section 03, eq. 11) | 50.9 °C | 41.9 °C |

- Going from 1 M to roughly physiological 0.15 M Na⁺ lowers $`T_m`$ by about 9 °C. The salt dependence is not a small correction.

**Self-complementary check.** For 5′-ATCGAT-3′ at 100 µM total strand concentration, $`\Delta H^0 = -36.8`$ kcal/mol and $`\Delta S^0 = -105.6`$ cal K⁻¹ mol⁻¹ (including −1.4 for symmetry). Section 03, eq. 12 then gives $`T_m = 23.9`$ °C. A 6-mer is barely stable at room temperature.

## Link to other topics

The NN model is a group-contribution method, built on the same logic as UNIFAC in Equilibrium Thermodynamics: assemble a property of the molecule from tabulated contributions of its parts, with parameters fitted to data.

## Summary

Summing tabulated stacking steps, terminal initiation terms and a symmetry correction gives $`\Delta H^0`$ and $`\Delta S^0`$ from the sequence alone. Salt enters through the entropy.
<!-- note-content:end -->

[Previous](<AB-03 - Two-state hybridisation and DNA melting.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-05 - Hybridisation kinetics.md>)

# Nucleic acids - structure, thermodynamics and kinetics — reading 01.3

[Previous](01-02-nucleic-acids-structure-thermodynamics-and-kinetics.md) · [Subject index](README.md) · [Next](02-01-dna-synthesis-and-gene-assembly.md)

<!-- reading-content:start -->
## Section 04: The nearest-neighbour model

### Intuition

Most of the stability of a duplex comes from **stacking**: the attraction between one flat base pair and the next one above it. The energy of a stacking contact depends on *both* pairs in the contact, just as the strength of a joint depends on both bricks it joins. So the natural unit is a "pair of base pairs" (a *dinucleotide step*). A duplex of $`N`$ bp has $`N-1`$ steps, and its $`\Delta G^0`$ is the sum over these steps, plus a cost for starting the duplex at all.

*Analogy:* the energy of a brick wall made of bricks of four sizes, where the mortar strength depends on which two bricks meet. Counting bricks alone would miss this. The analogy breaks down because interactions in a real duplex reach beyond nearest neighbours (and the model has no term for this), and because the "mortar" (salt) also changes the entropy.

### Derivation

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

### Motivation and explanation

- **Why the parameters look as they do.**
  - Steps containing G·C are most stable (CG/GC: $`\Delta G^0_{37} \approx -2.2`$ kcal/mol), and TA/AT is least stable ($`\approx -0.6`$). The order is not simply "count the hydrogen bonds": CG/GC and GC/CG contain the same pairs but differ by 0.4 kcal/mol, because the bases overlap differently when stacked. This is exactly why single-pair models fail.
  - Every step has $`\Delta H^0\approx -8`$ kcal/mol and $`\Delta S^0\approx -22`$ cal K⁻¹ mol⁻¹, so $`T\Delta S^0`$ largely cancels $`\Delta H^0`$. Small errors in each partly cancel in $`\Delta G^0`$, which is why $`\Delta G^0_{37}`$ is predicted better than $`\Delta H^0`$ or $`\Delta S^0`$ alone.
- **Accuracy and limits.**
  - For short oligos at 1 M Na⁺, predicted $`T_m`$ values are typically within about 2 °C of measurement.
  - The parameters are fitted, and only 8 combinations of the 10 steps are independent for long polymers.
  - Separate parameter sets exist for RNA:RNA, DNA:RNA, mismatches, dangling ends and wobble pairs.
  - The two-state assumption still applies, so the model is reliable only for short duplexes.
  - Software (NUPACK, for example) applies the full model, including secondary structure in the single strands.

### Worked example

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

### Link to other topics

The NN model is a group-contribution method, built on the same logic as UNIFAC in Equilibrium Thermodynamics: assemble a property of the molecule from tabulated contributions of its parts, with parameters fitted to data.

### Summary

Summing tabulated stacking steps, terminal initiation terms and a symmetry correction gives $`\Delta H^0`$ and $`\Delta S^0`$ from the sequence alone. Salt enters through the entropy.

## Section 05: Hybridisation kinetics

### Intuition

For two strands to bind, a few bases (about 2–3 bp) must first find their partners: a *nucleation* event. Once that has happened, the rest of the duplex zips up quickly. The rate-limiting nucleation step hardly depends on how long the duplex will eventually be, so $`k_{\text{on}}`$ is roughly the same for all sequences. Separation, by contrast, requires *every* pair to break at once (in the two-state picture). Each extra base pair adds another energetic barrier, multiplying the lifetime by roughly a constant factor. All the dependence of stability on sequence therefore appears in $`k_{\text{off}}`$.

*Analogy:* Velcro. Pressing two strips together takes about the same effort whatever their length, but peeling a long strip off in one go (not allowed to peel gradually) is far harder than peeling a short one. The analogy breaks down because DNA does unzip gradually by fraying and re-zipping, so real dissociation is a thermally activated escape, not a single event. The two-state rates are an effective average.

### Derivation

**Step 1: rate law.** For $`A + B \underset{k_{\text{off}}}{\overset{k_{\text{on}}}{\rightleftharpoons}} AB`$:

**Equation (16)**

```math
\frac{d[AB]}{dt} = k_{\text{on}}[A][B] - k_{\text{off}}[AB]
```

with $`k_{\text{on}}`$ in M⁻¹ s⁻¹ (bimolecular) and $`k_{\text{off}}`$ in s⁻¹ (unimolecular).

**Step 2: detailed balance.** At equilibrium, $`d[AB]/dt=0`$. Comparing (16) with Section 03, eq. 6:

**Equation (17)**

```math
K = \frac{k_{\text{on}}}{k_{\text{off}}} = \frac{[AB]}{[A][B]} = \frac{1}{\rho_0}\exp\left(-\frac{\Delta G^0}{RT}\right)
```


**Step 3: solve for the off-rate.**

**Equation (18)**

```math
k_{\text{off}} = k_{\text{on}}\,\rho_0\exp\left(\frac{\Delta G^0}{RT}\right)
```

$`\Delta G^0<0`$, so $`k_{\text{off}}\ll k_{\text{on}}\rho_0`$. Each extra step of $`\Delta G^0_i\approx -1.4`$ kcal/mol (37 °C) divides $`k_{\text{off}}`$ by $`\exp(1.4/0.616) \approx 10`$, since $`RT = 0.616`$ kcal/mol at 310 K. So each base pair added makes the duplex about ten times longer-lived.

**Step 4: timescales.**
- *Binding* at strand concentration $`c`$ is pseudo-first-order with rate $`k_{\text{on}}c`$, so $`t_{\text{on}}\sim 1/(k_{\text{on}}c)`$.
- *Dissociation* is first order, with mean lifetime $`1/k_{\text{off}}`$ and half-life $`\ln 2/k_{\text{off}}`$.

### Motivation and explanation

- **Size of $`k_{\text{on}}`$.** Typically $`10^4`$–$`10^6`$ M⁻¹ s⁻¹. That is far below the diffusion limit (about $`10^9`$), because most collisions are in the wrong register or orientation and fall apart before nucleating.
- **What changes $`k_{\text{on}}`$:**
  - salt (screening speeds it up);
  - secondary structure in either strand, which must unfold first and so slows binding;
  - length, only weakly.
- **Temperature.** Higher $`T`$ makes $`\Delta G^0`$ less negative and so raises $`k_{\text{off}}`$ steeply.
- **Where the model fails.** For mismatched or partly complementary strands, intermediate states and branch migration matter, and (18) is no longer enough. Section 22 deals with this for strand displacement.

### Worked example

*Off-rates against duplex length,* with $`k_{\text{on}} = 10^5`$ M⁻¹ s⁻¹. $`\Delta G^0`$ comes from the nearest-neighbour model (Section 04, 1 M Na⁺) for successive prefixes of 5′-GTATTTGGCTGTACGATCAG-3′. Computed in Python.

| Length | $`\Delta G^0_{37}`$ (kcal/mol) | $`k_{\text{off}}`$ at 37 °C (s⁻¹) | $`k_{\text{off}}`$ at 25 °C (s⁻¹) |
|---|---|---|---|
| 5 bp | −1.94 | $`4.3\times10^{3}`$ | $`6.8\times10^{2}`$ |
| 8 bp | −6.30 | 3.6 | 0.10 |
| 12 bp | −12.67 | $`1.2\times10^{-4}`$ | $`4.0\times10^{-7}`$ |
| 20 bp | −23.19 | $`4.6\times10^{-12}`$ | $`1.8\times10^{-16}`$ |

- **12 bp.** A 12 bp duplex at 37 °C has a half-life of about 98 min.
- **20 bp.** A 20 bp duplex at 37 °C has a half-life of about 4800 years; at 25 °C, $`1/k_{\text{off}} \approx 1.8\times10^{8}`$ years. In practice a 20-mer never comes apart spontaneously, and has to be melted or displaced.
- **Per base pair.** From 12 to 20 bp, each extra base pair lowers $`\log_{10}k_{\text{off}}`$ by 0.93 at 37 °C, matching the factor of 10 estimated in Step 3.
- **Binding time.** At 1 µM, $`t_{\text{on}} \sim 1/(10^5\times10^{-6}) = 10`$ s, the same for all lengths.
- **Orders of magnitude only.** These numbers depend on sequence, salt and temperature. Commonly quoted round figures ($`k_{\text{off}}\sim10^{-4}`$ s⁻¹ for 12 bp and about $`10^{-14}`$ s⁻¹ for 20 bp) sit within this range.

The practical consequence: duplexes of 5–8 bp form and break within seconds or less, while those above about 15 bp are permanent on laboratory timescales. Short sticky regions therefore give reversible, dynamic binding. Long ones give fixed structures.

### Link to other topics

$`K = k_{\text{on}}/k_{\text{off}}`$ is the same detailed-balance link between thermodynamics and kinetics used for any reversible reaction in Reaction Engineering. Here the thermodynamics (Section 04) predicts one rate constant from the other.

### Summary

Hybridisation is a fast, roughly sequence-independent bimolecular association. Its stability lives almost entirely in an exponentially sensitive off-rate, (18): about one decade slower per extra base pair at 37 °C.

## Conclusion

Hybridisation thermodynamics selects stable pairings, and kinetics determines whether those pairings rearrange on the available timescale. The next unit develops dna synthesis and gene assembly.
<!-- reading-content:end -->

[Previous](01-02-nucleic-acids-structure-thermodynamics-and-kinetics.md) · [Subject index](README.md) · [Next](02-01-dna-synthesis-and-gene-assembly.md)

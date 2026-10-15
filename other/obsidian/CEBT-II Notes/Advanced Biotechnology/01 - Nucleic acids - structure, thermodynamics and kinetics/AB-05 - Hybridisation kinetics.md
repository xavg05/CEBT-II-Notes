[Previous](<AB-04 - The nearest-neighbour model.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Section 05: Hybridisation kinetics

## Intuition

For two strands to bind, a few bases (about 2–3 bp) must first find their partners: a *nucleation* event. Once that has happened, the rest of the duplex zips up quickly. The rate-limiting nucleation step hardly depends on how long the duplex will eventually be, so $k_{\text{on}}$ is roughly the same for all sequences. Separation, by contrast, requires *every* pair to break at once (in the two-state picture). Each extra base pair adds another energetic barrier, multiplying the lifetime by roughly a constant factor. All the dependence of stability on sequence therefore appears in $k_{\text{off}}$.

*Analogy:* Velcro. Pressing two strips together takes about the same effort whatever their length, but peeling a long strip off in one go (not allowed to peel gradually) is far harder than peeling a short one. The analogy breaks down because DNA does unzip gradually by fraying and re-zipping, so real dissociation is a thermally activated escape, not a single event. The two-state rates are an effective average.

## Derivation

**Step 1: rate law.** For $A + B \underset{k_{\text{off}}}{\overset{k_{\text{on}}}{\rightleftharpoons}} AB$:
$$\frac{d[AB]}{dt} = k_{\text{on}}[A][B] - k_{\text{off}}[AB] \tag{16}$$
with $k_{\text{on}}$ in M⁻¹ s⁻¹ (bimolecular) and $k_{\text{off}}$ in s⁻¹ (unimolecular).

**Step 2: detailed balance.** At equilibrium, $d[AB]/dt=0$. Comparing (16) with Section 03, eq. 6:
$$K = \frac{k_{\text{on}}}{k_{\text{off}}} = \frac{[AB]}{[A][B]} = \frac{1}{\rho_0}\exp\left(-\frac{\Delta G^0}{RT}\right) \tag{17}$$

**Step 3: solve for the off-rate.**
$$k_{\text{off}} = k_{\text{on}}\,\rho_0\exp\left(\frac{\Delta G^0}{RT}\right) \tag{18}$$
$\Delta G^0<0$, so $k_{\text{off}}\ll k_{\text{on}}\rho_0$. Each extra step of $\Delta G^0_i\approx -1.4$ kcal/mol (37 °C) divides $k_{\text{off}}$ by $\exp(1.4/0.616) \approx 10$, since $RT = 0.616$ kcal/mol at 310 K. So each base pair added makes the duplex about ten times longer-lived.

**Step 4: timescales.**
- *Binding* at strand concentration $c$ is pseudo-first-order with rate $k_{\text{on}}c$, so $t_{\text{on}}\sim 1/(k_{\text{on}}c)$.
- *Dissociation* is first order, with mean lifetime $1/k_{\text{off}}$ and half-life $\ln 2/k_{\text{off}}$.

The pseudo-first-order description assumes that one partner's free concentration remains approximately constant, for example because it is in large excess. With equal starting amounts, both partners are depleted as duplex forms, so the association term falls during the experiment and this expression is only an encounter-timescale estimate. A large equilibrium constant alone therefore does not guarantee rapid assembly: strong binding can coexist with slow encounters or with a hairpin that hides the binding site.

## Motivation and explanation

- **Size of $k_{\text{on}}$.** Typically $10^4$–$10^6$ M⁻¹ s⁻¹. That is far below the diffusion limit (about $10^9$), because most collisions are in the wrong register or orientation and fall apart before nucleating.
- **What changes $k_{\text{on}}$:**
  - salt (screening speeds it up);
  - secondary structure in either strand, which must unfold first and so slows binding;
  - length, only weakly.
- **Temperature.** Higher $T$ makes $\Delta G^0$ less negative and so raises $k_{\text{off}}$ steeply.
- **Where the model fails.** For mismatched or partly complementary strands, intermediate states and branch migration matter, and (18) is no longer enough. Section 22 deals with this for strand displacement.

## Worked example

*Off-rates against duplex length,* with $k_{\text{on}} = 10^5$ M⁻¹ s⁻¹. $\Delta G^0$ comes from the nearest-neighbour model (Section 04, 1 M Na⁺) for successive prefixes of 5′-GTATTTGGCTGTACGATCAG-3′. Computed in Python.

| Length | $\Delta G^0_{37}$ (kcal/mol) | $k_{\text{off}}$ at 37 °C (s⁻¹) | $k_{\text{off}}$ at 25 °C (s⁻¹) |
|---|---|---|---|
| 5 bp | −1.94 | $4.3\times10^{3}$ | $6.8\times10^{2}$ |
| 8 bp | −6.30 | 3.6 | 0.10 |
| 12 bp | −12.67 | $1.2\times10^{-4}$ | $4.0\times10^{-7}$ |
| 20 bp | −23.19 | $4.6\times10^{-12}$ | $1.8\times10^{-16}$ |

- **12 bp.** A 12 bp duplex at 37 °C has a half-life of about 98 min.
- **20 bp.** A 20 bp duplex at 37 °C has a half-life of about 4800 years; at 25 °C, $1/k_{\text{off}} \approx 1.8\times10^{8}$ years. In practice a 20-mer never comes apart spontaneously, and has to be melted or displaced.
- **Per base pair.** From 12 to 20 bp, each extra base pair lowers $\log_{10}k_{\text{off}}$ by 0.93 at 37 °C, matching the factor of 10 estimated in Step 3.
- **Binding time.** At 1 µM, $t_{\text{on}} \sim 1/(10^5\times10^{-6}) = 10$ s, the same for all lengths.
- **Orders of magnitude only.** These numbers depend on sequence, salt and temperature. Commonly quoted round figures ($k_{\text{off}}\sim10^{-4}$ s⁻¹ for 12 bp and about $10^{-14}$ s⁻¹ for 20 bp) sit within this range.

The practical consequence: duplexes of 5–8 bp form and break within seconds or less, while those above about 15 bp are permanent on laboratory timescales. Short sticky regions therefore give reversible, dynamic binding. Long ones give fixed structures.

## Link to other topics

$K = k_{\text{on}}/k_{\text{off}}$ is the same detailed-balance link between thermodynamics and kinetics used for any reversible reaction in Reaction Engineering. Here the thermodynamics (Section 04) predicts one rate constant from the other.

## Summary

Hybridisation is a fast, roughly sequence-independent bimolecular association. Its stability lives almost entirely in an exponentially sensitive off-rate, (18): about one decade slower per extra base pair at 37 °C.

## Conclusion

Hybridisation thermodynamics selects stable pairings, and kinetics determines whether those pairings rearrange on the available timescale. The next unit develops dna synthesis and gene assembly.
<!-- note-content:end -->

[Previous](<AB-04 - The nearest-neighbour model.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

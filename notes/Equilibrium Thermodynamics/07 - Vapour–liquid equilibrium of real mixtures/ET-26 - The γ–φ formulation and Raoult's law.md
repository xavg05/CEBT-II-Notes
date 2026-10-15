[Previous](<ET-25 - Binary vapour–liquid equilibrium and its phase diagrams.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-27 - Deviations from Raoult's law and azeotropes.md>)

<!-- note-content:start -->
# Section 26: The γ–φ formulation and Raoult's law

## Intuition

Each side of the equality is an "escaping tendency".
- *Liquid side:* the pure liquid's escaping tendency (its vapour pressure, slightly corrected), scaled by how much of it there is ($`x_i`$) and how unhappy it is in the mixture ($`\gamma_i`$).
- *Vapour side:* the partial pressure, corrected for non-ideal gas behaviour.

At low pressure the gas corrections are tiny and the liquid term is all that matters. That is why one non-ideality, $`\gamma_i`$, dominates ordinary distillation.

## Derivation

**Step 1: vapour side.** Assume the vapour is an ideal *mixture* (Lewis–Randall) but not necessarily an ideal *gas*:


**Equation (127)**

```math
\bar f_i^{\,v} = y_if_i^{\,v}(T,P) = y_i\phi_i^{v}P
```


where $`\phi_i^{v}`$ is the fugacity coefficient of pure $`i`$ vapour at $`T`$, $`P`$. A full mixture equation of state could replace this, at the cost of much more algebra.

**Step 2: liquid side.** By the definition of $`\gamma_i`$, $`\bar f_i^{\,l} = \gamma_ix_if_i^{\,l}(T,P)`$, with $`f_i^{\,l}`$ the pure liquid at the mixture's $`T`$ and $`P`$.

**Step 3: pure-liquid fugacity.** Start from saturation, where liquid and vapour fugacities are equal ($`f_i^{\mathrm{SAT}} = \phi_i^{\mathrm{SAT}}P_i^{\mathrm{SAT}}`$). Then compress the incompressible liquid to $`P`$ (the Poynting factor):


**Equation (128)**

```math
f_i^{\,l}(T,P) = \phi_i^{\mathrm{SAT}}P_i^{\mathrm{SAT}}\exp\!\left[\frac{\underline{V}_i^{l}(P - P_i^{\mathrm{SAT}})}{RT}\right]
```


**Step 4: equate.**


**Equation (129)**

```math
\gamma_ix_i\,\phi_i^{\mathrm{SAT}}P_i^{\mathrm{SAT}}\exp\!\left[\frac{\underline{V}_i^{l}(P - P_i^{\mathrm{SAT}})}{RT}\right] = y_i\phi_i^{v}P
```


**Step 5: low pressure.** Set $`\phi_i^{\mathrm{SAT}}\approx\phi_i^{v}\approx 1`$ and drop the Poynting factor. This gives **modified Raoult's law**:


**Equation (130)**

```math
\gamma_ix_iP_i^{\mathrm{SAT}} = y_iP
```


**Step 6: ideal liquid mixture.** Setting $`\gamma_i = 1`$ gives **Raoult's law**. Summing over components, with $`\sum y_i = 1`$, gives the bubble pressure:


**Equation (131)**

```math
x_iP_i^{\mathrm{SAT}} = y_iP, \qquad P = \sum_i x_iP_i^{\mathrm{SAT}}
```


On a $`P`$–$`x`$–$`y`$ diagram at constant $`T`$, the bubble line is then straight: the sum of the two straight partial-pressure lines $`x_1P_1^{\mathrm{SAT}}`$ and $`x_2P_2^{\mathrm{SAT}}`$. The dew line, $`1/P = \sum y_i/P_i^{\mathrm{SAT}}`$, is curved.

A bubble calculation starts with liquid composition and sums the predicted vapour fractions to unity. A dew calculation starts with vapour composition, writes $`x_i=y_iP/P_i^{\mathrm{SAT}}`$, and instead sums the liquid fractions to unity. This change of which phase is known produces the reciprocal-pressure dew equation; it is not an independent equilibrium law.

The use of pure-vapour $`\phi_i^{v}`$ in (127) is also a modelling step. A full vapour-mixture coefficient depends on the composition of that vapour because unlike gas molecules interact. At sufficiently low density those interactions disappear and both versions approach unity. Low pressure simplifies the vapour description without requiring ideal mixing in the dense liquid.

![Raoult's law at constant T: straight partial-pressure lines (dashed) sum to a straight bubble line; the dew line is curved; a tie line joins x1 and y1](../figs/ET-26-raoult-Pxy.png)

## Motivation and explanation

**Hierarchy of approximations.**

| Equation | Neglects | Valid when |
|---|---|---|
| (129) | vapour-mixture non-ideality (Lewis–Randall) | up to moderate pressure, chemically similar vapours |
| (130) | gas non-ideality and the Poynting factor | $`P`$ ≲ a few bar |
| (131) | liquid non-ideality | chemically similar liquids (isomers, homologues) |

**Why $`\phi^{\mathrm{SAT}}`$ and $`\phi^{v}`$ partly cancel.** At the same $`T`$ and similar pressures, the two vapour-phase fugacity coefficients in (129) are similar. Their ratio is closer to 1 than either is alone. So (130) is often better than the individual corrections suggest.

**Deviations from Raoult.**
- $`\gamma_i > 1`$: total pressure above the straight Raoult line (positive deviation).
- $`\gamma_i < 1`$: below it (negative deviation).

These are the curved bubble lines of real mixtures (next section).

## Worked example

**Problem.** For an equimolar benzene (1)–toluene (2) liquid at 90 °C, find the Raoult's-law bubble pressure and vapour composition, and the size of each correction in (129). Data: $`P_1^{\mathrm{SAT}} = 1.362`$ bar, $`P_2^{\mathrm{SAT}} = 0.543`$ bar; $`\underline{V}_1^{l} = 97.4`$ and $`\underline{V}_2^{l} = 115.2`$ cm³ mol⁻¹; $`\phi_1^{\mathrm{SAT}} = 0.960`$, $`\phi_2^{\mathrm{SAT}} = 0.975`$.

**Raoult's law (131).** $`P = 0.5(1.362) + 0.5(0.543) = 0.953`$ bar, and $`y_1 = 0.5\times1.362/0.953 = 0.715`$.

**Corrections.**
- *Poynting factor at 0.953 bar:* benzene 0.9987, toluene 1.0016. Both differ from 1 by under 0.2 %, with opposite signs, because benzene's liquid is *below* and toluene's *above* its own saturation pressure.
- *Saturation fugacity coefficients:* 4 % and 2.5 % below 1, but they are largely cancelled by $`\phi_i^{v}`$ at a similar pressure in (129).

**Interpretation.** For similar, non-polar liquids near atmospheric pressure, every correction in (129) is at the percent level or below, so Raoult's law is a good first estimate. For chemically different liquids, $`\gamma_i`$ easily reaches 2–20, an order of magnitude larger than all the other corrections. Getting $`\gamma`$ right is what matters.

## Link to other topics

Equation (130) is the default VLE model in distillation design, combined with any of the activity-coefficient models in Sections 17–20. At high pressure or near critical points, the γ–φ approach is replaced by a single equation of state for both phases, discussed later.

## Summary

Equating fugacities gives the γ–φ equation (129). At low pressure it reduces to modified Raoult's law, $`\gamma_ix_iP_i^{\mathrm{SAT}} = y_iP`$, and for ideal liquids to Raoult's law with a straight bubble line. Gas-phase and Poynting corrections are usually small, and the activity coefficient carries the important non-ideality.
<!-- note-content:end -->

[Previous](<ET-25 - Binary vapour–liquid equilibrium and its phase diagrams.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-27 - Deviations from Raoult's law and azeotropes.md>)

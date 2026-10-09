# Vapour–liquid equilibrium of real mixtures — reading 07.1

[Previous](06-02-phase-rule-osmosis-droplets-and-bubbles.md) · [Subject index](README.md) · [Next](07-02-vapour-liquid-equilibrium-of-real-mixtures.md)

<!-- reading-content:start -->
## Overview

Vapour–liquid equilibrium of a binary is fixed by equal fugacities plus mass balances and drawn as constant-$`T`$ and constant-$`P`$ slices of a 3D surface, with bubble and dew curves joined by tie lines (Section 25). Writing each fugacity in measurable terms gives the γ–φ equation, which reduces at low pressure to modified Raoult's law and, for ideal liquids, Raoult's law (Section 26). Strong deviations bend the bubble curve until it turns over: an azeotrope, where vapour and liquid have the same composition and ordinary distillation stops (Section 27). Turned round, a measured azeotrope gives both activity coefficients and a complete van Laar model (Section 28).

*Assumed throughout:* fugacity and fugacity coefficients (Sections 07–08); activity coefficients and Gibbs–Duhem (Sections 10–11); the phase rule (Section 21); the models of Sections 17–20.

## Section 25: Binary vapour–liquid equilibrium and its phase diagrams

*Notation:* $`x_i`$ is the liquid mole fraction, $`y_i`$ the vapour mole fraction, and $`z_i`$ the overall (feed) mole fraction. $`L`$ and $`V`$ are the fractions of the total moles in the liquid and vapour.

### Intuition

When a liquid mixture partly boils, the vapour is richer in the more volatile component. That difference between $`y`$ and $`x`$ is what distillation exploits, stage after stage.

The phase rule says a binary in VLE has two degrees of freedom. Fix the temperature and you may still choose *either* the pressure *or* the liquid composition, but not both. Two compositions coexist at each pressure: the liquid on one curve, the vapour on another. Joining them gives a horizontal **tie line**.

### Derivation

**Step 1: the equations.** For each component $`i = 1,\dots,C`$:


```math
T^{l} = T^{v}, \qquad P^{l} = P^{v}\ (\text{flat interface}), \qquad \bar f_i^{\,l} = \bar f_i^{\,v} \tag{124}
```


**Step 2: mass balances.** Per mole of feed of composition $`z_i`$:


```math
Lx_i + Vy_i = z_i, \qquad \sum_i x_i = \sum_i y_i = 1, \qquad L + V = 1 \tag{125}
```


Equations (124)–(125) are the entire framework. What changes between problems is only how $`\bar f_i`$ is written: activity coefficients for the liquid and fugacity coefficients for the vapour (next section).

**Step 3: the lever rule.** For a binary, (125) gives


```math
\frac{L}{V} = \frac{y_1 - z_1}{z_1 - x_1} \tag{126}
```


The feed point splits the tie line in inverse proportion to the amounts of the two phases. A feed close to the liquid curve is mostly liquid.

**Step 4: reduced phase diagrams.** The equilibrium states of a binary fill a 3D space ($`P`$, $`T`$, composition). The liquid and vapour surfaces bound a lens-shaped two-phase region, which ends at the critical locus joining the two pure-component critical points. Slicing it gives:
- Constant $`T`$ ($`P`$–$`x`$–$`y`$): the upper curve is the bubble-point (liquid) line, the lower the dew-point (vapour) line, running from $`P_2^{\mathrm{SAT}}`$ to $`P_1^{\mathrm{SAT}}`$.
- Constant $`P`$ ($`T`$–$`x`$–$`y`$): the curves are inverted. The liquid (bubble) line is now lower, running from $`T_1^{\mathrm{SAT}}`$ (the more volatile component boils first) to $`T_2^{\mathrm{SAT}}`$.

![The binary VLE surface in P–T–composition space; vertical slices give constant-T diagrams, horizontal slices constant-P diagrams](figs/ET-25-3D-VLE-surface.png)

![Reduced diagrams: P–x–y at constant T (bubble line above, dew line below, horizontal tie line) and T–x–y at constant P (heating a liquid: first bubble and last drop compositions)](figs/ET-25-Pxy-Txy-diagrams.png)

### Motivation and explanation

**Reading a $`T`$–$`x`$–$`y`$ diagram.** Heat a subcooled liquid of composition $`z_1`$ at constant $`P`$ (the vertical arrow).
1. It first boils where it meets the liquid line: the **bubble point**. The first bubble has the vapour composition on the same tie line, enriched in component 1.
2. On further heating, the liquid becomes poorer in 1 and both compositions slide along their curves.
3. The last drop disappears at the **dew point**, where the vapour has the feed composition.

Between the two, the lever rule (126) gives how much has vaporised.

**Why pressure-composition and temperature-composition curves differ.** At constant $`T`$, more volatile material raises the pressure. At constant $`P`$, it lowers the boiling temperature. So the diagrams are near mirror images, curved because vapour pressure depends exponentially on temperature.

**Limits.** These pictures assume a flat interface and that only two phases are present. Liquid immiscibility (a third phase) and near-critical behaviour change the topology; both are treated later.

### Worked example

**Problem.** A 50:50 benzene (124)–toluene (125) liquid is heated at 1 atm. Using Raoult's law with accurate vapour pressures, find (a) the bubble and dew temperatures, and (b) the phase compositions and fraction vaporised at 95 °C.

**(a)** The bubble point is where $`\sum_i z_iP_i^{\mathrm{SAT}}(T) = P`$. The dew point is where $`\sum_i z_i/P_i^{\mathrm{SAT}}(T) = 1/P`$. Solving numerically:
- bubble point 92.1 °C;
- dew point 98.7 °C.

Pure benzene boils at 80.1 °C and pure toluene at 110.6 °C.

**(b)** At 95 °C the equilibrium ratios are $`K_i = P_i^{\mathrm{SAT}}/P`$: $`K_1 = 1.550`$ and $`K_2 = 0.628`$. For a binary, $`x_1 = (1 - K_2)/(K_1 - K_2) = 0.404`$ and $`y_1 = K_1x_1 = 0.625`$. From (126), $`V = (z_1 - x_1)/(y_1 - x_1) = 0.43`$.

**Interpretation.** Partially vaporising the mixture at 95 °C gives a vapour of 62.5 % benzene from a 50 % feed, and the liquid that remains is 40 % benzene. Each such equilibrium stage enriches the vapour. The ratio $`K_1/K_2 = 2.47`$ (the relative volatility) measures how easily the pair separates, and it is what sets the number of stages in a column.

### Link to other topics

Equations (124)–(126) are exactly the "flash" calculation done by every process simulator, and the $`T`$–$`x`$–$`y`$ diagram is the starting point of McCabe–Thiele and other distillation design methods. Section 26 shows how the fugacities in (124) are written in practice, reducing to Raoult's law in the ideal limit.

### Summary

VLE of a binary is fixed by equal fugacities plus mass balances. Graphically it is a 3D surface whose constant-$`T`$ and constant-$`P`$ slices show bubble and dew curves joined by tie lines. The lever rule then gives the phase amounts, and the gap between vapour and liquid compositions is what makes distillation work.

## Section 26: The γ–φ formulation and Raoult's law

### Intuition

Each side of the equality is an "escaping tendency".
- *Liquid side:* the pure liquid's escaping tendency (its vapour pressure, slightly corrected), scaled by how much of it there is ($`x_i`$) and how unhappy it is in the mixture ($`\gamma_i`$).
- *Vapour side:* the partial pressure, corrected for non-ideal gas behaviour.

At low pressure the gas corrections are tiny and the liquid term is all that matters. That is why one non-ideality, $`\gamma_i`$, dominates ordinary distillation.

### Derivation

**Step 1: vapour side.** Assume the vapour is an ideal *mixture* (Lewis–Randall) but not necessarily an ideal *gas*:


```math
\bar f_i^{\,v} = y_if_i^{\,v}(T,P) = y_i\phi_i^{v}P \tag{127}
```


where $`\phi_i^{v}`$ is the fugacity coefficient of pure $`i`$ vapour at $`T`$, $`P`$. A full mixture equation of state could replace this, at the cost of much more algebra.

**Step 2: liquid side.** By the definition of $`\gamma_i`$, $`\bar f_i^{\,l} = \gamma_ix_if_i^{\,l}(T,P)`$, with $`f_i^{\,l}`$ the pure liquid at the mixture's $`T`$ and $`P`$.

**Step 3: pure-liquid fugacity.** Start from saturation, where liquid and vapour fugacities are equal ($`f_i^{\mathrm{SAT}} = \phi_i^{\mathrm{SAT}}P_i^{\mathrm{SAT}}`$). Then compress the incompressible liquid to $`P`$ (the Poynting factor):


```math
f_i^{\,l}(T,P) = \phi_i^{\mathrm{SAT}}P_i^{\mathrm{SAT}}\exp\!\left[\frac{\underline{V}_i^{l}(P - P_i^{\mathrm{SAT}})}{RT}\right] \tag{128}
```


**Step 4: equate.**


```math
\gamma_ix_i\,\phi_i^{\mathrm{SAT}}P_i^{\mathrm{SAT}}\exp\!\left[\frac{\underline{V}_i^{l}(P - P_i^{\mathrm{SAT}})}{RT}\right] = y_i\phi_i^{v}P \tag{129}
```


**Step 5: low pressure.** Set $`\phi_i^{\mathrm{SAT}}\approx\phi_i^{v}\approx 1`$ and drop the Poynting factor. This gives **modified Raoult's law**:


```math
\gamma_ix_iP_i^{\mathrm{SAT}} = y_iP \tag{130}
```


**Step 6: ideal liquid mixture.** Setting $`\gamma_i = 1`$ gives **Raoult's law**. Summing over components, with $`\sum y_i = 1`$, gives the bubble pressure:


```math
x_iP_i^{\mathrm{SAT}} = y_iP, \qquad P = \sum_i x_iP_i^{\mathrm{SAT}} \tag{131}
```


On a $`P`$–$`x`$–$`y`$ diagram at constant $`T`$, the bubble line is then straight: the sum of the two straight partial-pressure lines $`x_1P_1^{\mathrm{SAT}}`$ and $`x_2P_2^{\mathrm{SAT}}`$. The dew line, $`1/P = \sum y_i/P_i^{\mathrm{SAT}}`$, is curved.

![Raoult's law at constant T: straight partial-pressure lines (dashed) sum to a straight bubble line; the dew line is curved; a tie line joins x1 and y1](figs/ET-26-raoult-Pxy.png)

### Motivation and explanation

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

### Worked example

**Problem.** For an equimolar benzene (124)–toluene (125) liquid at 90 °C, find the Raoult's-law bubble pressure and vapour composition, and the size of each correction in (129). Data: $`P_1^{\mathrm{SAT}} = 1.362`$ bar, $`P_2^{\mathrm{SAT}} = 0.543`$ bar; $`\underline{V}_1^{l} = 97.4`$ and $`\underline{V}_2^{l} = 115.2`$ cm³ mol⁻¹; $`\phi_1^{\mathrm{SAT}} = 0.960`$, $`\phi_2^{\mathrm{SAT}} = 0.975`$.

**Raoult's law (131).** $`P = 0.5(1.362) + 0.5(0.543) = 0.953`$ bar, and $`y_1 = 0.5\times1.362/0.953 = 0.715`$.

**Corrections.**
- *Poynting factor at 0.953 bar:* benzene 0.9987, toluene 1.0016. Both differ from 1 by under 0.2 %, with opposite signs, because benzene's liquid is *below* and toluene's *above* its own saturation pressure.
- *Saturation fugacity coefficients:* 4 % and 2.5 % below 1, but they are largely cancelled by $`\phi_i^{v}`$ at a similar pressure in (129).

**Interpretation.** For similar, non-polar liquids near atmospheric pressure, every correction in (129) is at the percent level or below, so Raoult's law is a good first estimate. For chemically different liquids, $`\gamma_i`$ easily reaches 2–20, an order of magnitude larger than all the other corrections. Getting $`\gamma`$ right is what matters.

### Link to other topics

Equation (130) is the default VLE model in distillation design, combined with any of the activity-coefficient models in Sections 17–20. At high pressure or near critical points, the γ–φ approach is replaced by a single equation of state for both phases, discussed later.

### Summary

Equating fugacities gives the γ–φ equation (129). At low pressure it reduces to modified Raoult's law, $`\gamma_ix_iP_i^{\mathrm{SAT}} = y_iP`$, and for ideal liquids to Raoult's law with a straight bubble line. Gas-phase and Poynting corrections are usually small, and the activity coefficient carries the important non-ideality.
<!-- reading-content:end -->

[Previous](06-02-phase-rule-osmosis-droplets-and-bubbles.md) · [Subject index](README.md) · [Next](07-02-vapour-liquid-equilibrium-of-real-mixtures.md)

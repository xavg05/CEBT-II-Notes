[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-26 - The γ–φ formulation and Raoult's law.md>)

<!-- note-content:start -->
# Section 25: Binary vapour–liquid equilibrium and its phase diagrams

*Notation:* $`x_i`$ is the liquid mole fraction, $`y_i`$ the vapour mole fraction, and $`z_i`$ the overall (feed) mole fraction. $`L`$ and $`V`$ are the fractions of the total moles in the liquid and vapour.

## Intuition

When a liquid mixture partly boils, the vapour is richer in the more volatile component. That difference between $`y`$ and $`x`$ is what distillation exploits, stage after stage.

The phase rule says a binary in VLE has two degrees of freedom. Fix the temperature and you may still choose *either* the pressure *or* the liquid composition, but not both. Two compositions coexist at each pressure: the liquid on one curve, the vapour on another. Joining them gives a horizontal **tie line**.

## Derivation

**Step 1: the equations.** For each component $`i = 1,\dots,C`$:


**Equation (124)**

```math
T^{l} = T^{v}, \qquad P^{l} = P^{v}\ (\text{flat interface}), \qquad \bar f_i^{\,l} = \bar f_i^{\,v}
```


**Step 2: mass balances.** Per mole of feed of composition $`z_i`$:


**Equation (125)**

```math
Lx_i + Vy_i = z_i, \qquad \sum_i x_i = \sum_i y_i = 1, \qquad L + V = 1
```


Equations (124)–(125) are the entire framework. What changes between problems is only how $`\bar f_i`$ is written: activity coefficients for the liquid and fugacity coefficients for the vapour (next section).

**Step 3: the lever rule.** For a binary, (125) gives


**Equation (126)**

```math
\frac{L}{V} = \frac{y_1 - z_1}{z_1 - x_1}
```


The feed point splits the tie line in inverse proportion to the amounts of the two phases. A feed close to the liquid curve is mostly liquid.

Eliminate $`L`$ using $`L=1-V`$ in the component balance. The remaining equation is $`z_1-x_1=V(y_1-x_1)`$: the feed's enrichment above the liquid composition equals the vapour fraction times the vapour–liquid composition gap. This gives the lever rule and explains why $`z_1`$ must lie between $`x_1`$ and $`y_1`$ whenever both phase amounts are positive.

At the bubble point, the vapour amount tends to zero, so the liquid composition equals the feed composition. At the dew point the liquid amount tends to zero, so the vapour composition equals the feed composition. That is why the same $`z_i`$ enters two different equations in part (a). Between these limits the feed fixes the phase amounts; it is neither phase composition.

**Step 4: reduced phase diagrams.** The equilibrium states of a binary fill a 3D space ($`P`$, $`T`$, composition). The liquid and vapour surfaces bound a lens-shaped two-phase region, which ends at the critical locus joining the two pure-component critical points. Slicing it gives:
- Constant $`T`$ ($`P`$–$`x`$–$`y`$): the upper curve is the bubble-point (liquid) line, the lower the dew-point (vapour) line, running from $`P_2^{\mathrm{SAT}}`$ to $`P_1^{\mathrm{SAT}}`$.
- Constant $`P`$ ($`T`$–$`x`$–$`y`$): the curves are inverted. The liquid (bubble) line is now lower, running from $`T_1^{\mathrm{SAT}}`$ (the more volatile component boils first) to $`T_2^{\mathrm{SAT}}`$.

![The binary VLE surface in P–T–composition space; vertical slices give constant-T diagrams, horizontal slices constant-P diagrams](../figs/ET-25-3D-VLE-surface.png)

![Reduced diagrams: P–x–y at constant T (bubble line above, dew line below, horizontal tie line) and T–x–y at constant P (heating a liquid: first bubble and last drop compositions)](../figs/ET-25-Pxy-Txy-diagrams.png)

## Motivation and explanation

**Separate equilibrium endpoints from phase amounts.** At fixed temperature and pressure, a binary with given equilibrium ratios $`K_i=y_i/x_i`$ has

```math
x_1=\frac{1-K_2}{K_1-K_2},\qquad y_1=K_1x_1.
```

The first relation follows by substituting $`y_i=K_ix_i`$ into $`y_1+y_2=1`$ with $`x_2=1-x_1`$. Only afterwards does the overall composition $`z_1`$ determine the vapour fraction $`V=(z_1-x_1)/(y_1-x_1)`$. For $`K_1=1.550`$, $`K_2=0.628`$ and $`z_1=0.5`$, these give $`x_1\approx0.403`$, $`y_1\approx0.625`$ and $`V\approx0.435`$. The vapour is enriched in component 1 while the liquid is depleted. Altering the feed within this tie line changes amounts, not equilibrium compositions. Relative volatility $`K_1/K_2\approx2.47`$ describes the enrichment available from a stage.

**Reading a $`T`$–$`x`$–$`y`$ diagram.** Heat a subcooled liquid of composition $`z_1`$ at constant $`P`$ (the vertical arrow).
1. It first boils where it meets the liquid line: the **bubble point**. The first bubble has the vapour composition on the same tie line, enriched in component 1.
2. On further heating, the liquid becomes poorer in 1 and both compositions slide along their curves.
3. The last drop disappears at the **dew point**, where the vapour has the feed composition.

Between the two, the lever rule (126) gives how much has vaporised.

**Why pressure-composition and temperature-composition curves differ.** At constant $`T`$, more volatile material raises the pressure. At constant $`P`$, it lowers the boiling temperature. So the diagrams are near mirror images, curved because vapour pressure depends exponentially on temperature.

**Limits.** These pictures assume a flat interface and that only two phases are present. Liquid immiscibility (a third phase) and near-critical behaviour change the topology; both are treated later.

## Link to other topics

Equations (124)–(126) are exactly the "flash" calculation done by every process simulator, and the $`T`$–$`x`$–$`y`$ diagram is the starting point of McCabe–Thiele and other distillation design methods. Section 26 shows how the fugacities in (124) are written in practice, reducing to Raoult's law in the ideal limit.

## Summary

VLE of a binary is fixed by equal fugacities plus mass balances. Graphically it is a 3D surface whose constant-$`T`$ and constant-$`P`$ slices show bubble and dew curves joined by tie lines. The lever rule then gives the phase amounts, and the gap between vapour and liquid compositions is what makes distillation work.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-26 - The γ–φ formulation and Raoult's law.md>)

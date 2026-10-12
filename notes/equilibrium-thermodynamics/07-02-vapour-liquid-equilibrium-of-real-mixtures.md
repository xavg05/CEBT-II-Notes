# Vapour–liquid equilibrium of real mixtures — reading 07.2

[Previous](07-01-vapour-liquid-equilibrium-of-real-mixtures.md) · [Subject index](README.md) · [Next](07-03-vapour-liquid-equilibrium-of-real-mixtures.md)

<!-- reading-content:start -->
## Section 27: Deviations from Raoult's law and azeotropes

### Intuition

With positive deviation, each component "wants out" of the liquid more than Raoult predicts, so the mixture's vapour pressure exceeds the straight line. If the two pure vapour pressures are close, this bulge can rise above *both* end points. Then the curve must have a maximum somewhere in between.

At that maximum, adding a little of either component lowers the pressure. The vapour therefore cannot be richer in either component than the liquid: it has the same composition. Distilling such a mixture drives the products towards the azeotrope, not towards the pure components.

*Molecular picture.*
- A *maximum-pressure* (minimum-boiling) azeotrope comes from unlike molecules disrupting each other's attractions, e.g. toluene breaking up ethanol's hydrogen-bond network.
- A *minimum-pressure* (maximum-boiling) azeotrope comes from unlike molecules attracting strongly, e.g. the hydrogen bond between chloroform's C–H and tetrahydrofuran's oxygen.

### Derivation

**Step 1: pressure–composition slope.** For a binary at constant $`T`$, (130) of Section 26 summed over components gives $`P = x_1\gamma_1P_1^{\mathrm{SAT}} + x_2\gamma_2P_2^{\mathrm{SAT}}`$. Differentiate with respect to $`x_1`$, using $`dx_2 = -dx_1`$:


```math
\frac{dP}{dx_1} = \gamma_1P_1^{\mathrm{SAT}}\left(1 + x_1\frac{d\ln\gamma_1}{dx_1}\right) + \gamma_2P_2^{\mathrm{SAT}}\left(-1 + x_2\frac{d\ln\gamma_2}{dx_1}\right)
```


**Step 2: Gibbs–Duhem.** Substitute $`x_2\,d\ln\gamma_2/dx_1 = -x_1\,d\ln\gamma_1/dx_1`$:


**Equation (132)**

```math
\frac{dP}{dx_1} = \left(\gamma_1P_1^{\mathrm{SAT}} - \gamma_2P_2^{\mathrm{SAT}}\right)\left(1 + x_1\frac{d\ln\gamma_1}{dx_1}\right)
```


**Step 3: turning points.** $`dP/dx_1 = 0`$ requires one of two conditions.
- (a) $`\gamma_1P_1^{\mathrm{SAT}} = \gamma_2P_2^{\mathrm{SAT}}`$: an **azeotrope**.
- (b) $`1 + x_1\,d\ln\gamma_1/dx_1 = 0`$, i.e. $`d\ln(\gamma_1x_1)/dx_1 = 0`$. The activity of component 1 stops increasing with its own mole fraction. This marks the spinodal, the limit of local liquid stability. Equilibrium splitting begins at the binodal; between binodal and spinodal the homogeneous liquid is metastable (later sections).

**Step 4: $`x = y`$ at an azeotrope.** From modified Raoult's law, $`y_1P = x_1\gamma_1P_1^{\mathrm{SAT}}`$ and $`P = x_1\gamma_1P_1^{\mathrm{SAT}} + x_2\gamma_2P_2^{\mathrm{SAT}}`$. With condition (a), $`P = \gamma_1P_1^{\mathrm{SAT}}(x_1 + x_2) = \gamma_1P_1^{\mathrm{SAT}}`$, so


**Equation (133)**

```math
y_1 = x_1
```


**Step 5: phase-rule consequence.** Equation (133) is an extra constraint. An azeotropic binary therefore has only $`F = 2 - 2 + 2 - 1 = 1`$ degree of freedom: at a given pressure the azeotrope has one temperature and one composition, like a pure substance.

**Step 6: will an azeotrope form? (one-constant Margules).** With $`RT\ln\gamma_1 = Ax_2^2`$ and $`RT\ln\gamma_2 = Ax_1^2`$, condition (a) becomes $`A(x_2^2 - x_1^2) = RT\ln(P_2^{\mathrm{SAT}}/P_1^{\mathrm{SAT}})`$. Since $`x_2^2 - x_1^2 = 1 - 2x_1`$:


**Equation (134)**

```math
x_1^{\mathrm{az}} = \frac12\left[1 - \frac{RT}{A}\ln\frac{P_2^{\mathrm{SAT}}}{P_1^{\mathrm{SAT}}}\right]
```


A candidate homogeneous azeotrope exists if $`0 < x_1^{\mathrm{az}} < 1`$, i.e. if $`|A|/RT > |\ln(P_1^{\mathrm{SAT}}/P_2^{\mathrm{SAT}})|`$; the liquid at that composition must also be stable against liquid–liquid splitting. Strong non-ideality, or *close* vapour pressures, makes azeotropes likely.

### Motivation and explanation

**The four behaviours, at 30–65 °C.**
1. **Mild negative deviation** (tetrahydrofuran–CCl₄): the curves sag slightly below Raoult's line and lie close together. Distillation is possible but difficult.
2. **Strong negative deviation** (chloroform–THF): a minimum-pressure, maximum-boiling azeotrope near $`x_1 = 0.5`$, matching the 1:1 hydrogen bond.
3. **Mild positive deviation** (furan–CCl₄): the curves lie above Raoult's line and wide apart. Distillation is easy.
4. **Strong positive deviation** (ethanol–toluene): a maximum-pressure, minimum-boiling azeotrope.

![Chloroform (1)–THF (2) at 30 °C: strong negative deviation gives a minimum-pressure (maximum-boiling) azeotrope near x1 = 0.5](figs/ET-27-chloroform-THF-negative-azeotrope.png)

![Ethanol (1)–toluene (2): strong positive deviation gives a maximum-pressure (minimum-boiling) azeotrope](figs/ET-27-ethanol-toluene-positive-azeotrope.png)

**Distillation and azeotropes.** On a $`T`$–$`x`$–$`y`$ diagram, a minimum-boiling azeotrope is a low point. Feeds on either side distil towards it overhead; only one pure component can be recovered as bottoms from each side. Past the azeotrope the vapour is *richer* in the less volatile component.

![Positive deviation: maximum in P at constant T is a minimum in T at constant P; stepping up the T–x–y diagram converges on the azeotrope](figs/ET-27-max-pressure-azeotrope.png)

**Breaking an azeotrope** needs an extra degree of freedom:
- *Change the pressure* (pressure-swing distillation): the azeotropic composition shifts with $`P`$.
- *Add a component:* an entrainer forming a ternary heterogeneous azeotrope (e.g. benzene or cyclohexane for ethanol–water), or a heavy solvent that changes the $`\gamma`$'s (extractive distillation).

### Worked example

**Problem.** Benzene (1) and cyclohexane (2) boil at 80.1 °C and 80.7 °C. Use regular solution theory (Section 17) and (134) to decide whether they form an azeotrope at 1 atm, and estimate its temperature and composition.

**Model.** RST at 25 °C gave $`\ln\gamma^{\infty}`$ = 0.171 and 0.140 for this pair. Average them into a one-constant Margules parameter:


```math
A = \tfrac12 RT(0.171 + 0.140) = 385\ \text{J mol}^{-1}
```


This is treated as independent of temperature, as a regular solution assumes.

**At 78 °C.** $`P_1^{\mathrm{SAT}} = 0.944`$ bar and $`P_2^{\mathrm{SAT}} = 0.927`$ bar, so $`|\ln(P_1^{\mathrm{SAT}}/P_2^{\mathrm{SAT}})| = 0.018 \ll A/RT = 0.132`$. An azeotrope must exist. Equation (134) gives $`x_1^{\mathrm{az}}\approx 0.57`$.

**At 1 atm.** Solving (134) together with $`P = \gamma_1P_1^{\mathrm{SAT}} = 1.01325`$ bar for $`T`$ gives a minimum-boiling azeotrope at about **79.3 °C** and $`x_{\mathrm{benzene}}\approx 0.57`$. The tabulated value is 77.8 °C.

**Interpretation.** Starting from pure-component data only (heats of vaporisation and densities), we correctly predict that two liquids boiling 0.6 K apart form a minimum-boiling azeotrope about 1–2 K below both. RST underestimates the non-ideality here, so the predicted azeotrope is not deep enough. The discrepancy shows the limits of a random-mixing model based on a single cohesive-energy parameter; identifying its detailed molecular cause would require additional evidence. The lesson is general. Close-boiling pairs with even modest non-ideality almost always azeotrope.

### Link to other topics

Azeotropes set the feasible products of distillation columns and are central to separation-sequence design (residue curve maps, entrainer selection). The second factor in (132) reappears in the liquid–liquid equilibrium sections as the stability condition.

### Summary

Positive and negative deviations from Raoult's law bend the bubble curve. If the bend exceeds the difference in pure-component volatilities, $`\gamma_1P_1^{\mathrm{SAT}} = \gamma_2P_2^{\mathrm{SAT}}`$ somewhere: an azeotrope, with $`x = y`$ and one fewer degree of freedom, which ordinary distillation cannot cross.
<!-- reading-content:end -->

[Previous](07-01-vapour-liquid-equilibrium-of-real-mixtures.md) · [Subject index](README.md) · [Next](07-03-vapour-liquid-equilibrium-of-real-mixtures.md)

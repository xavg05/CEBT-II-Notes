[Previous](<AB-02 - Polymer physics of DNA and the worm-like chain.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-04 - The nearest-neighbour model.md>)

<!-- note-content:start -->
# Section 03: Two-state hybridisation and DNA melting

## Intuition

Pairing releases enthalpy: stacking and hydrogen bonds form ($`\Delta H^0<0`$). It also costs entropy: two floppy coils (Section 02) become one stiff duplex, and two independent molecules become one ($`\Delta S^0<0`$). At low $`T`$ the enthalpy term wins and the strands are paired. At high $`T`$ the $`-T\Delta S^0`$ penalty wins and they separate. Because $`\Delta H^0`$ and $`-T\Delta S^0`$ are both large (tens of kcal/mol) and nearly cancel near body temperature, a change of a few degrees tips the balance. That is why DNA melts over a narrow range.

Concentration changes the equilibrium as well as the encounter rate. Dilution lowers the chemical potentials of the two free strands relative to the single duplex, favouring dissociation by mass action. Even after waiting long enough to equilibrate, a dilute sample is less hybridised at the same temperature. Meeting less often explains slower association; the translational entropy of two independent strands explains the shifted melting temperature.

## Derivation

Notation: $`[A]`$, $`[B]`$, $`[AB]`$ are equilibrium concentrations; $`\rho_0 = 1`$ M is the standard concentration; $`\Delta G^0 = \Delta H^0 - T\Delta S^0`$ is the standard Gibbs energy of hybridisation (duplex minus single strands); $`f`$ is the fraction of strands hybridised.

**Two-state assumption.** Each strand is either fully paired or fully free. Partially zipped states are neglected. This is reasonable for short oligos (up to about 20–30 bp), where a partly open duplex is much less stable than either end state.

**Step 1: equilibrium constant.** For an ideal dilute solution, the chemical potential of each species is $`\mu_i = \mu_i^0 + RT\ln([i]/\rho_0)`$. Setting $`\mu_{AB} = \mu_A+\mu_B`$ at equilibrium gives:

**Equation (6)**

```math
K = \frac{[AB]}{[A][B]} = \frac{1}{\rho_0}\exp\left(-\frac{\Delta G^0}{RT}\right)
```

The factor $`1/\rho_0`$ gives $`K`$ units of M⁻¹ and makes clear that $`\Delta G^0`$ refers to 1 M. $`\Delta G^0`$ alone does not decide whether strands are paired; the concentration does too.

**Step 2: mass balance.** Take equal total concentrations $`[A]_0=[B]_0=c`$. Each duplex uses one A and one B, so:

**Equation (7)**

```math
[AB]=fc,\qquad [A]=[B]=c(1-f)
```


**Step 3: substitute (7) into (6).**

**Equation (8)**

```math
\frac{f}{c(1-f)^2} = \frac{1}{\rho_0}\exp\left(-\frac{\Delta H^0 - T\Delta S^0}{RT}\right)
```

Writing $`a = Kc`$, (8) is a quadratic, $`a(1-f)^2 = f`$. Its physical root (the one with $`0\le f\le 1`$) is:

**Equation (9)**

```math
f = \frac{(2a+1)-\sqrt{4a+1}}{2a}
```

Checks: as $`a\to\infty`$ (cold, or concentrated) $`f\to 1`$; as $`a\to 0`$, $`f\approx a\to 0`$.

**Step 4: melting temperature.** Define $`T_m`$ by $`f=\tfrac12`$. Then $`f/(1-f)^2 = 2`$, and (8) gives $`2/c = (1/\rho_0)\exp(-\Delta G^0/RT_m)`$:

**Equation (10)**

```math
\frac{c}{2} = \rho_0\exp\left(\frac{\Delta H^0}{RT_m} - \frac{\Delta S^0}{R}\right)
```

Take logarithms and solve for $`T_m`$:

**Equation (11)**

```math
T_m = \frac{\Delta H^0}{\Delta S^0 + R\ln\!\left(\dfrac{c}{2\rho_0}\right)}
```

Both $`\Delta H^0`$ and the denominator are negative, so $`T_m>0`$.

**Step 5: self-complementary strand** ($`A + A \rightleftharpoons A_2`$, total strand concentration $`c`$). Here $`[A_2] = fc/2`$ and $`[A] = c(1-f)`$. At $`f=\tfrac12`$, $`K = (c/4)/(c/2)^2 = 1/c`$. Hence:

**Equation (12)**

```math
T_m^{\text{self}} = \frac{\Delta H^0}{\Delta S^0 + R\ln(c/\rho_0)}
```

In terms of the *total* strand concentration $`C_T`$, (11) uses $`C_T/4`$ (since $`C_T = 2c`$) and (12) uses $`C_T`$. That is the form in which the formula is usually quoted.

**Step 6: sharpness of the transition.** Take the logarithm of $`f/(1-f)^2 = cK`$ and differentiate with respect to $`T`$. On the right, $`d\ln K/dT = \Delta H^0/RT^2`$ (van 't Hoff). On the left, $`d\ln[f/(1-f)^2]/df = 1/f + 2/(1-f) = (1+f)/[f(1-f)]`$. So:

**Equation (13)**

```math
\frac{df}{dT} = \frac{\Delta H^0}{RT^2}\,\frac{f(1-f)}{1+f}, \qquad \left.\frac{df}{dT}\right|_{T_m} = \frac{\Delta H^0}{6RT_m^2}
```

A larger $`|\Delta H^0|`$ (a longer duplex) gives a sharper transition. Fitting the slope of a measured melting curve is therefore one way to obtain $`\Delta H^0`$.

## Motivation and explanation

![Measured melting curve: the fraction hybridised falls sigmoidally from 1 to 0 between about 25 and 60 °C, with T_m ≈ 42 °C](../figs/AB-03-melting-curve.png)

- **Why the temperature dependence is captured by constants.** Over the melting range, $`\Delta H^0`$ and $`\Delta S^0`$ are roughly independent of temperature: the heat-capacity change on hybridisation is small enough to neglect. All the temperature dependence then comes through $`T`$ in $`\Delta H^0 - T\Delta S^0`$.
- **Concentration dependence.** $`\ln(c/2\rho_0)`$ is negative and large (about −14 for µM strands). It makes the denominator of (11) more negative and so lowers $`T_m`$ below $`\Delta H^0/\Delta S^0`$. This "translational" entropy penalty for bringing two molecules together is what the $`1/\rho_0`$ in (6) accounts for. Unimolecular transitions, such as a hairpin closing, have no such term, and their $`T_m = \Delta H^0/\Delta S^0`$ does not depend on concentration.
- **How measured curves are obtained.** The curve is usually measured by UV absorbance at 260 nm, which rises about 20–40 % on melting because stacked bases absorb less (*hyperchromicity*). Absorbance therefore tracks $`f`$ directly.
- **Where the model fails:**
  - long duplexes melt in domains through partly open intermediates;
  - single strands with internal secondary structure (hairpins) compete with the duplex;
  - unequal strand concentrations change (7): with $`[A]_0 > [B]_0`$, the term $`c/2`$ is replaced by $`[A]_0 - [B]_0/2`$;
  - $`\Delta S^0`$ depends on salt (Section 04).

### Concentration shifts the melting transition

For illustrative two-state parameters $`\Delta H^0=-80\,\mathrm{kcal\,mol^{-1}}`$ and $`\Delta S^0=-220\,\mathrm{cal\,K^{-1}\,mol^{-1}}`$, equation (11) gives melting temperatures of $`48.4\,{}^\circ\mathrm C`$ and $`60.6\,{}^\circ\mathrm C`$ at strand concentrations of $`1\,\mu\mathrm M`$ and $`100\,\mu\mathrm M`$, respectively. The higher concentration favours a bimolecular duplex over two separate strands, so temperature must rise further before half dissociates. A melting temperature therefore has meaning only with its concentration and salt conditions.

![Calculated two-state melting curves: the horizontal axis is temperature and the vertical axis is duplex fraction; increasing concentration moves the half-duplex crossing to higher temperature](../figs/AB-03-model-melting-curves.png)

These are computed equilibrium curves, rather than experimental measurements. Their downward transition shows thermal dissociation; the horizontal displacement isolates the concentration effect at fixed model enthalpy and entropy.

## Link to other topics

Equation (6) is the standard-state chemical equilibrium of Equilibrium Thermodynamics, applied to a bimolecular reaction in dilute solution. The concentration term in (11) is the same $`RT\ln x`$ ideal-mixing entropy that lowers a freezing point.

## Summary

Treating hybridisation as a two-state bimolecular equilibrium gives a sigmoidal melting curve, (9). The melting temperature, (11), depends on $`\Delta H^0`$, $`\Delta S^0`$ and the strand concentration, and the sharpness of the transition, (13), scales with $`|\Delta H^0|`$.
<!-- note-content:end -->

[Previous](<AB-02 - Polymer physics of DNA and the worm-like chain.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-04 - The nearest-neighbour model.md>)

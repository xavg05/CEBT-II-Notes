# Solubility of gases in liquids — reading 08.2

[Previous](08-01-solubility-of-gases-in-liquids.md) · [Subject index](README.md) · [Next](09-01-high-pressure-vapour-liquid-equilibrium.md)

<!-- reading-content:start -->
## Section 31: Henry's law and the Henry standard state

### Intuition

A dilute solute molecule is surrounded entirely by solvent. Adding a few more solute molecules does not change that environment, so each behaves the same, and the escaping tendency is simply proportional to how many there are. The proportionality constant reflects how comfortable one solute molecule is among solvent molecules. That is exactly the infinite-dilution activity coefficient times the pure-liquid fugacity.

Raoult's law is the opposite limit: the *solvent*, nearly pure, behaves as if it were alone. Every dilute binary obeys Raoult for the solvent and Henry for the solute at the same time, and Gibbs–Duhem guarantees the two are consistent.

### Derivation

**Step 1: dilute limit.** As $`x_i\to 0`$, $`\gamma_i\to\gamma_i^{\infty}`$, a constant at fixed $`T`$ (and pressure, to a good approximation). Then


```math
\bar f_i = \gamma_ix_if_i^{\,l}\;\to\;x_i\,\gamma_i^{\infty}f_i^{\,l}\equiv x_iH_i(T) \tag{142}
```



```math
H_i = \gamma_i^{\infty}f_i^{\,l} \tag{143}
```


$`H_i`$ has units of pressure and depends on $`T`$ and on both the solute and the solvent. It can be measured directly as $`\lim_{x_i\to0}\bar f_i/x_i`$, without ever constructing $`f_i^{\,l}`$.

**Step 2: a new standard state.** The conventional activity uses the pure liquid as reference, $`a_i = x_i\gamma_i = \bar f_i/f_i^{\,l}`$, so $`a_i = 1`$ for pure $`i`$. Instead, use $`H_i`$ as the reference fugacity:


```math
a_i^{*} = x_i\gamma_i^{*} = \frac{\bar f_i}{H_i} \qquad\Rightarrow\qquad \bar f_i = \gamma_i^{*}x_iH_i \tag{144}
```


**Step 3: how the two activity coefficients relate.** Dividing (144) by $`\bar f_i = \gamma_ix_if_i^{\,l}`$ and using (143):


```math
\gamma_i^{*} = \frac{\gamma_i}{\gamma_i^{\infty}} \tag{145}
```


So $`\gamma_i^{*}\to 1`$ as $`x_i\to 0`$, while $`\gamma_i\to 1`$ as $`x_i\to 1`$. The two conventions are normalised at opposite ends.

**Step 4: graphical meaning.** On a plot of $`\bar f_i`$ against $`x_i`$:
- Henry's law is the tangent at $`x_i = 0`$, reaching $`H_i`$ at $`x_i = 1`$;
- Raoult's law (ideal mixture) is the straight line to $`f_i^{\,l}`$.

At any composition A, with the real curve at D, the Henry line at C and the Raoult line at B: $`\gamma_i^{*} = AD/AC`$ and $`\gamma_i = AD/AB`$.

![Henry and Raoult reference lines for a dissolved gas: γ* = AD/AC measures deviation from the Henry line, γ = AD/AB from the (hypothetical) Raoult line](figs/ET-31-henry-vs-raoult.png)

### Motivation and explanation

**Why switch reference.** For a supercritical gas, $`f_i^{\,l}`$ is hypothetical and must come from an extrapolation or correlation (Section 29). $`H_i`$ is measured directly in the dilute region where the gas actually lives, and then $`\gamma_i^{*}\approx 1`$. Any standard state is allowed, as long as it is used consistently.

**Temperature dependence.** $`\ln H_i`$ usually varies with $`1/T`$ through the enthalpy of solution (a van 't Hoff form). For permanent gases in water near room temperature, dissolution is exothermic, so $`H`$ falls and solubility rises as temperature falls. That is why cold water holds more oxygen.

**Limits.** Henry's law is a limiting law. It fails as $`x_i`$ grows (then $`\gamma_i^{*}\neq 1`$) and for gases that react or ionise in the solvent: CO₂, NH₃ and SO₂ in water dissolve far beyond the Henry value because of the chemistry. At high pressure, the gas-phase fugacity and the pressure dependence of $`H`$ (through the partial molar volume of the solute) must be included.

### Worked example

**Problem.** Henry's constants in water at 25 °C are $`4.3\times10^4`$ atm for O₂ and $`9.1\times10^4`$ atm for N₂. (a) How much oxygen and nitrogen dissolves in water in equilibrium with air at 1 atm? (b) How much more oxygen dissolves at 5 °C, given $`-\Delta_{\mathrm{sol}}H/R = 1700`$ K for O₂?

**(a)** With an ideal-gas vapour, $`\bar f_i = y_iP`$:
- $`x_{\mathrm{O_2}} = 0.21/4.3\times10^4 = 4.9\times10^{-6}`$, about 8.7 mg L⁻¹ (taking 55.5 mol of water per litre);
- $`x_{\mathrm{N_2}} = 0.78/9.1\times10^4 = 8.6\times10^{-6}`$, about 13 mg L⁻¹.

**(b)** $`H(T) = H(298.15)\exp[-1700(1/T - 1/298.15)]`$, which at 278.15 K gives $`H = 2.9\times10^4`$ atm. Solubility is inversely proportional to $`H`$, so 1.5 times more oxygen dissolves at 5 °C than at 25 °C.

**Interpretation.** The oxygen value (~8.7 mg L⁻¹) matches the familiar saturation level of fresh water at 25 °C. Such low solubility is why aerobic bioreactors are often limited by oxygen transfer: the liquid can never hold more than a few milligrams per litre, so oxygen must be supplied continuously. The 50 % gain on cooling is part of why cold waters support more aquatic life. In Henry's terms, N₂ and O₂ are "ideal" here: $`\gamma^{*} = 1`$ by construction at these tiny mole fractions.

### Link to other topics

Henry's constants are the standard input for absorber and stripper design and for gas–liquid mass transfer in bioreactors, where the oxygen saturation concentration sets the transfer driving force. The infinite-dilution activity coefficient in (143) links back to ebulliometry (Section 14), which measures it for condensable solutes.

### Summary

In the dilute limit the solute fugacity is linear in mole fraction, $`\bar f_i = x_iH_i`$, with $`H_i = \gamma_i^{\infty}f_i^{\,l}`$. Using $`H_i`$ as the standard state removes the need for a hypothetical liquid and gives an activity coefficient $`\gamma_i^{*}`$ that is 1 at infinite dilution. Applied to air and water, it predicts the familiar ~9 mg L⁻¹ of dissolved oxygen and its rise on cooling.

## Conclusion

Gas solubility is ordinary phase equilibrium with an awkward reference state. The hypothetical liquid gives an ideal solubility and activity coefficients; Henry's constant avoids the hypothetical state and is the standard design input, predicting for example about 9 mg L⁻¹ of dissolved oxygen in water at 25 °C. The next part moves to high pressure, where vapour and liquid approach each other near critical points.
<!-- reading-content:end -->

[Previous](08-01-solubility-of-gases-in-liquids.md) · [Subject index](README.md) · [Next](09-01-high-pressure-vapour-liquid-equilibrium.md)

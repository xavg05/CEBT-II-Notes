[Previous](<ET-19 - Local-composition models (Wilson and NRTL).md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Section 20: UNIQUAC, UNIFAC and choosing a model

*Notation:* $`r_i`$ is a volume parameter and $`q_i`$ a surface-area parameter for molecule $`i`$, relative to a standard segment. $`\phi_i = x_ir_i/\sum_jx_jr_j`$ is the segment (volume) fraction and $`\theta_i = x_iq_i/\sum_jx_jq_j`$ the area fraction. $`z = 10`$ is the lattice coordination number.

## Intuition

Molecules interact through their *surfaces*: a long chain exposes more contact area per unit volume than a compact sphere. UNIQUAC therefore counts arrangements with volumes (as Flory–Huggins does), corrects them for surface area (shape), and counts interactions through surface-area fractions.

UNIFAC adds a powerful idea. A CH₂ group behaves much the same whether it sits in hexane or in a fatty acid. So the mixture can be modelled as a soup of groups whose interactions were fitted once, across many systems. *The analogy breaks down* when neighbouring groups influence each other strongly, for example an OH next to a C=O. That is the main source of UNIFAC errors, and why its predictions must be checked.

## Derivation

**Step 1: UNIQUAC structure.**


**Equation (106)**

```math
\frac{\underline{G}^{ex}}{RT} = \frac{\underline{G}^{ex}_{\mathrm{comb}}}{RT} + \frac{\underline{G}^{ex}_{\mathrm{res}}}{RT}
```


**Step 2: combinatorial (size and shape) part.**


**Equation (107)**

```math
\frac{\underline{G}^{ex}_{\mathrm{comb}}}{RT} = \sum_i x_i\ln\frac{\phi_i}{x_i} + \frac{z}{2}\sum_i q_ix_i\ln\frac{\theta_i}{\phi_i}
```


The first sum is the Flory–Huggins entropy; the second corrects for shape (area relative to volume). Differentiating gives, at infinite dilution of $`i`$ in $`j`$ (with $`V = r_i/r_j`$, $`F = q_i/q_j`$):


**Equation (108)**

```math
\ln\gamma_i^{C,\infty} = 1 - V + \ln V - \frac{z}{2}q_i\left(1 - \frac{V}{F} + \ln\frac{V}{F}\right)
```


**Step 3: residual (energy) part.**

Because the two Gibbs-energy contributions add, their *chemical-potential* contributions add after differentiation. Thus $`\ln\gamma_i=\ln\gamma_i^{C}+\ln\gamma_i^{R}`$, or $`\gamma_i=\gamma_i^{C}\gamma_i^{R}`$. The combinatorial values in the example are factors in the full prediction, not quantities to add to an energetic activity coefficient.

Setting all residual interaction factors to unity removes chemical preferences while retaining molecular size and shape. Setting the molecular size and shape parameters equal as well removes the combinatorial distinction, recovering ideal mixing. These are different tests: chemically similar molecules can still depart from Raoult's law because their sizes differ, while similarly sized molecules can depart because their interactions differ.


**Equation (109)**

```math
\frac{\underline{G}^{ex}_{\mathrm{res}}}{RT} = -\sum_i q_ix_i\ln\left(\sum_j\theta_j\tau_{ji}\right), \qquad \tau_{ji} = \exp\!\left(-\frac{u_{ji} - u_{ii}}{RT}\right)
```


Two parameters per binary, $`u_{12} - u_{22}`$ and $`u_{21} - u_{11}`$, are fitted to data as in Wilson. With $`\tau_{ij} = 1`$ (no energetic difference), the residual term vanishes.

**Step 4: getting $`r_i`$ and $`q_i`$ by group contribution.** Sum tabulated group values: $`r_i = \sum_k\nu_k^{(i)}R_k`$ and $`q_i = \sum_k\nu_k^{(i)}Q_k`$, where $`\nu_k^{(i)}`$ is the number of groups of type $`k`$ in molecule $`i`$. UNIFAC does the same for the residual term, using tabulated group–group interaction parameters in place of fitted molecular ones.

## Motivation and explanation

**Why split size from energy.** The combinatorial part is fixed by molecular structure and needs no data. Only the energetic part needs fitting, so the fitted parameters are fewer and depend less on temperature. This makes UNIQUAC the default in process simulators when no better-tested model exists for a system.

**Why UNIFAC is both useful and dangerous.** It gives activity coefficients for systems never measured, which is useful at the screening stage. But the residual (energy) part from groups is much less accurate than the combinatorial part. Treat UNIFAC numbers as first estimates, and verify them before designing equipment.

**Choosing a model.**
1. *Moderately non-ideal mixtures:* all models perform well. Use what the data and software support.
2. *Quick hand estimates:* RST, or one-constant Margules.
3. *Very different species* (polar/non-polar, hydrogen bonding): Wilson, NRTL or UNIQUAC are more reliable. Multi-term Redlich–Kister also fits well but extrapolates poorly in temperature.
4. *If liquid–liquid splitting is possible:* not Wilson. Use NRTL, UNIQUAC or Redlich–Kister.
5. *In a process simulator, by default:* UNIQUAC. For your own calculations: Redlich–Kister fitted to data.
6. *No data:* measure binary VLE (or have it measured); otherwise estimate with UNIFAC and treat the result with suspicion.

Every model is a fit. Its reliability depends as much on the data behind the parameters (range of $`T`$ and composition, quality) as on the model. A sophisticated model fitted to sparse data is no better than a simple one.

## Worked example

**Problem.** Using UNIFAC group parameters, find the UNIQUAC combinatorial (size–shape) contribution to $`\gamma^{\infty}`$ for (a) n-hexadecane dilute in n-hexane and the reverse, and (b) ethanol dilute in water and the reverse.

**Group values.**

| Group | $`R_k`$ | $`Q_k`$ |
|---|---|---|
| CH₃ | 0.9011 | 0.848 |
| CH₂ | 0.6744 | 0.540 |
| OH | 1.0000 | 1.200 |
| H₂O | 0.9200 | 1.400 |

**Molecules.**

| Molecule | Groups | $`r`$ | $`q`$ |
|---|---|---|---|
| n-hexane | 2 CH₃ + 4 CH₂ | 4.500 | 3.856 |
| n-hexadecane | 2 CH₃ + 14 CH₂ | 11.244 | 9.256 |
| ethanol | CH₃ + CH₂ + OH | 2.576 | 2.588 |
| water | H₂O | 0.920 | 1.400 |

**From (108).**

| Solute (dilute) in solvent | $`\gamma^{C,\infty}`$ |
|---|---|
| hexadecane in hexane | 0.58 |
| hexane in hexadecane | 0.74 |
| ethanol in water | 1.68 |
| water in ethanol | 1.15 |

**Interpretation.**
- *Alkanes:* the two have nearly identical chemistry, so the residual term is close to zero and these combinatorial values are essentially the whole prediction. Both $`\gamma`$'s are below 1: size differences alone produce *negative* deviations from Raoult's law, as Flory–Huggins showed. A long chain dissolved in short ones gains entropy.
- *Ethanol–water:* the combinatorial part is modest. The large and temperature-dependent non-ideality of this system comes from the residual (hydrogen-bonding) term, which needs fitted or group-interaction parameters.

So the combinatorial term matters most for size asymmetry, and the residual term matters most for chemical difference.

## Link to other topics

These models supply the $`\gamma_i`$ in $`y_iP = x_i\gamma_iP_i^{\mathrm{SAT}}`$ for the vapour–liquid equilibrium, azeotrope and liquid–liquid equilibrium sections that follow, and in distillation and extraction design.

## Summary

UNIQUAC splits $`\underline{G}^{ex}`$ into a combinatorial size–shape term, computed from volume and area parameters, and a residual energy term with two fitted parameters. UNIFAC estimates both from functional groups when no data exist. All activity-coefficient models are consistent fits whose reliability depends on the data behind them. Choose the simplest model the system allows, avoid Wilson when liquids may split, and verify group-contribution estimates.

## Conclusion

Every activity-coefficient model is a thermodynamically consistent fit whose reliability depends on the data behind it. Random-mixing models are simple and good for non-polar mixtures; Flory–Huggins handles size asymmetry; local-composition models extrapolate better and (except Wilson) can describe liquid splitting; UNIFAC gives first estimates without data. The next part returns to equilibrium itself, starting with the phase rule and equilibria where pressure is not uniform.
<!-- note-content:end -->

[Previous](<ET-19 - Local-composition models (Wilson and NRTL).md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

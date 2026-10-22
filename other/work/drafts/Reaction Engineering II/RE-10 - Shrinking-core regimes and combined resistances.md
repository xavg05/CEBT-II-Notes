# RE-10: Shrinking-core regimes and combined resistances

## Overview

Assumed: the shrinking-core geometry and product-layer diffusion result.

A shrinking-core particle can also be controlled by the chemical reaction at the core surface or by the external film. Reaction control reproduces the shrinking-particle result $X=1-(1-t/\tau_c)^3$; film control gives conversion linear in time, $X=t/\tau_c$. Because all three steps are linear in concentration and act in series, the times they would each need simply add. The three regimes are best told apart by their dependence on particle size, gas velocity and temperature rather than by the shape of a conversion curve alone.

## Intuition

The reagent's path has three stages in series: through the external film, through the porous product layer, then reaction at the core surface. The slowest stage sets the pace, just as the narrowest pipe in a series controls the flow.

The stages change importance as the core shrinks. The film stays the same because the particle size is fixed. The product layer grows thicker. The reacting area at the core gets smaller. A step that is negligible at first may control at the end.

## Derivation

Use the notation of the product-layer derivation: overall radius $R$, core radius $r_c$, solid molar density $\rho_m$, positive stoichiometric numbers $\nu_A,\nu_B$, and conversion $X=1-(r_c/R)^3$.

**Step 1: reaction control.** If diffusion through the product layer and film is fast, the concentration is uniform at $C_{\mathrm{bulk}}$ up to the core surface. With first-order surface rate constant $k_{SA}$, the core recedes exactly as an unprotected particle under reaction control does, at the constant speed $\nu_Ak_{SA}C_{\mathrm{bulk}}/\rho_m$:

$$
\tau_c=\frac{\rho_mR}{\nu_Ak_{SA}C_{\mathrm{bulk}}},\qquad
X=1-\left(1-\frac t{\tau_c}\right)^3.
\tag{31}
$$

*Reason:* the porous layer adds no resistance in this limit, so only the area and rate at the reacting surface matter, which are the same as for a shrinking particle of radius $r_c$.

**Step 2: film control.** If reaction at the core and diffusion through the layer are both fast, the concentration falls to about zero at the outer particle surface and the film carries $4\pi R^2k_gC_{\mathrm{bulk}}$, a constant because $R$ is fixed. The solid balance is

$$
-\frac d{dt}\left(\tfrac43\pi r_c^3\rho_m\right)=\frac{\nu_A}{\nu_B}4\pi R^2k_gC_{\mathrm{bulk}}.
$$

Dividing by the initial inventory $\tfrac43\pi R^3\rho_m$ turns the left side into $dX/dt$:

$$
\frac{dX}{dt}=\frac{3k_gC_{\mathrm{bulk}}}{\rho_mR}\frac{\nu_A}{\nu_B}
\quad\Longrightarrow\quad
X=\frac t{\tau_c},\qquad
\tau_c=\frac{\rho_mR}{3k_gC_{\mathrm{bulk}}}\frac{\nu_B}{\nu_A}.
\tag{32}
$$

*Reason:* nothing in the supply depends on $r_c$, so the conversion rate is constant. This regime is uncommon, because diffusion through a product layer is usually slower than through a gas film; it can occur for very small particles.

**Step 3: combine all three resistances.** Eliminating the two intermediate concentrations in the same way as for two resistances, the molar flow of B is

$$
\dot n_B=\frac{C_{\mathrm{bulk}}}{\dfrac1{4\pi R^2k_g}+\dfrac{1/r_c-1/R}{4\pi D_e}+\dfrac1{4\pi r_c^2\nu_Bk_{SA}}}.
$$

*Reason:* each step carries the same molar flow at steady state, and each is linear in its own concentration difference, so the resistances add. Substituting into the core balance, the time step $dt$ needed for a step $dr_c$ is a sum of three terms, each identical to the single-regime expression. Integrating each term separately gives

$$
t=\tau_{\mathrm{film}}X+\tau_{\mathrm{layer}}\left[1-3(1-X)^{2/3}+2(1-X)\right]+\tau_{\mathrm{rxn}}\left[1-(1-X)^{1/3}\right],
\tag{33}
$$

where $\tau_{\mathrm{film}}$, $\tau_{\mathrm{layer}}$ and $\tau_{\mathrm{rxn}}$ are the complete-reaction times of (32), (30) and (31). Complete reaction takes $\tau_{\mathrm{film}}+\tau_{\mathrm{layer}}+\tau_{\mathrm{rxn}}$. Numerical integration of the coupled resistance model reproduces (33) to rounding error.

## Motivation and explanation

![Conversion against normalised time for the three shrinking-core regimes](../figs/RE-10-shrinking-core-conversion.png)

Each curve uses its own $\tau_c$, so all reach $X=1$ at $t/\tau_c=1$ and the plot compares shapes. Film control is a straight line because the supply is constant. Product-layer control rises fastest at first, when the layer is thin, then flattens as the layer grows. Reaction control is intermediate. The layer and reaction curves meet exactly at $t/\tau_c=0.5$, $X=0.875$; before that point layer control is ahead, after it reaction control is. The curves are close over much of the range, so scattered conversion–time data rarely distinguish these two.

More decisive tests change one physical variable at a time:

| Controlling step | Dependence of $\tau_c$ on $R$ | Response to gas velocity | Response to temperature |
|---|---|---|---|
| External film | $R^{1.5}$ to $R^2$ | Faster at higher velocity | Weak |
| Product-layer diffusion | $R^2$ | None | Weak |
| Core reaction | $R$ | None | Strong, Arrhenius |

The size exponents follow from (30)–(32) and the Sherwood correlation; the temperature column follows because $k_g$ and $D_e$ change slowly with temperature, whereas $k_{SA}$ is activated.

The resistances in Step 3 show why the controlling step can change during a run. The film resistance is constant. The layer resistance starts at zero and grows roughly as $1/r_c$ as the layer thickens. The reaction resistance grows as $1/r_c^2$ as the reacting area shrinks, so it eventually exceeds the layer resistance very close to complete conversion, even if the layer controlled for most of the run. Its derivation needs all three steps to be linear in concentration and the system to be isothermal. A nonlinear surface rate or a temperature that changes with conversion couples the steps, and the times no longer add.

The same derivations work for flat plates and cylinders, with different exponents in place of $2/3$ and $1/3$. Several common complications lie outside these results: an exothermic or endothermic reaction can produce temperature profiles inside and outside the particle; a porous starting solid reacts throughout its volume, not only at a sharp front; and the particle may swell, shrink or shed its outer layer. Burning coal shows all of these at once.

## Link to other topics

Adding resistances in series parallels the overall effectiveness of a catalyst pellet with an external film. The size and temperature diagnostics are the same kind of evidence used to show whether a measured catalytic rate is free of transport effects.

## Conclusion

Film, product-layer and reaction control give distinct shapes and size scalings, and in series their times add. Next, the same heat and mass balances are applied to an evaporating droplet, where temperature cannot be assumed uniform.

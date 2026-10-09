# Phase rule, osmosis, droplets and bubbles — reading 06.2

[Previous](06-01-phase-rule-osmosis-droplets-and-bubbles.md) · [Subject index](README.md) · [Next](07-01-vapour-liquid-equilibrium-of-real-mixtures.md)

<!-- reading-content:start -->
## Section 23: Droplets and the Kelvin equation

*Notation:* $`\sigma`$ is the surface tension (N m⁻¹), $`r`$ the droplet radius, $`P^{L}`$ the pressure inside the droplet, $`P^{V}`$ the surrounding vapour pressure, and $`P^{\mathrm{SAT}}(T)`$ the vapour pressure over a flat surface. Pure substance throughout.

### Intuition

Surface tension acts like a stretched skin around the droplet, pressing inwards. The smaller the droplet, the more sharply curved the skin and the harder it presses. Liquid inside is therefore compressed, and compressed liquid has a higher escaping tendency (Section 06). So a small droplet evaporates into vapour that would be exactly saturated over a flat surface.

Equilibrium with a droplet of radius $`r`$ needs a *supersaturated* vapour, and the equilibrium is unstable:
- a droplet slightly smaller than that $`r`$ has an even higher vapour pressure, so it evaporates further;
- a droplet slightly larger grows.

### Derivation

**Step 1: the phase-rule count.** One component, two phases: naively $`F = 1`$, one boiling point per pressure. But $`P^{L}\neq P^{V}`$ across a curved interface, which removes one constraint. So $`F = 2`$: for example the pressure *and* the droplet radius.

**Step 2: mechanical equilibrium (Young–Laplace).** Cut the droplet through its centre. The pressure excess acting on the cross-section, $`(P^{L} - P^{V})\pi r^2`$, is balanced by surface tension acting round the rim, $`2\pi r\sigma`$:


```math
P^{L} - P^{V} = \frac{2\sigma}{r} \tag{117}
```


**Step 3: chemical potentials.** Reference both phases to the flat-interface saturation state, where $`\underline{G}^{L} = \underline{G}^{V} = \underline{G}^{\mathrm{SAT}}(T)`$ at $`P^{\mathrm{SAT}}`$.
- Incompressible liquid: $`\mu^{L} = \underline{G}^{\mathrm{SAT}} + \underline{V}^{L}(P^{L} - P^{\mathrm{SAT}})`$.
- Ideal-gas vapour: $`\mu^{V} = \underline{G}^{\mathrm{SAT}} + RT\ln(P^{V}/P^{\mathrm{SAT}})`$.

**Step 4: equate.** $`\mu^{L} = \mu^{V}`$ gives the same equation as the Poynting correction,


```math
\underline{V}^{L}(P^{L} - P^{\mathrm{SAT}}) = RT\ln\frac{P^{V}}{P^{\mathrm{SAT}}}
```


but now $`P^{L}`$ is set by (117): $`P^{L} = P^{V} + 2\sigma/r`$.

**Step 5: the Kelvin equation.** Substitute:


```math
\underline{V}^{L}\left(\frac{2\sigma}{r} + P^{V} - P^{\mathrm{SAT}}\right) = RT\ln\frac{P^{V}}{P^{\mathrm{SAT}}} \tag{118}
```


For droplets larger than a few nanometres, $`P^{V} - P^{\mathrm{SAT}}`$ is negligible compared with $`2\sigma/r`$, so


```math
\ln\frac{P^{V}}{P^{\mathrm{SAT}}} \approx \frac{2\sigma\underline{V}^{L}}{rRT} \tag{119}
```


**Graphical form.** On the isotherm, the flat-interface case is Maxwell's equal-area construction at $`P^{\mathrm{SAT}}`$. For a droplet, the liquid branch is pushed up to $`P^{L}`$. The extra liquid-side area must be balanced by raising the vapour line slightly, to $`P^{V} > P^{\mathrm{SAT}}`$.

![Isotherm: flat interface (purple, Maxwell equal areas at P^SAT) versus droplet (green): compressing the liquid to P^L raises the equilibrium vapour pressure to P^V](figs/ET-23-droplet-isotherm.png)

### Motivation and explanation

**Same physics as Poynting.** In Section 06 the extra pressure on the liquid came from an inert gas. Here it comes from curvature. Either way, compressing the liquid by $`\Delta P`$ multiplies its fugacity by $`\exp(\underline{V}^{L}\Delta P/RT)`$.

**Unstable equilibrium and nucleation.** In vapour at a given supersaturation $`S = P^{V}/P^{\mathrm{SAT}}`$, (119) defines a critical radius $`r^{*} = 2\sigma\underline{V}^{L}/(RT\ln S)`$. Smaller droplets evaporate; larger ones grow. Forming a droplet from scratch means passing through tiny, highly unstable sizes. So pure vapour can stay supersaturated (metastable) for a long time. Real clouds form on dust, salt or ions, which provide surfaces large enough to skip that stage. The same effect makes small crystals more soluble than large ones, which drives Ostwald ripening in crystallisers.

**Limits.**
- At radii of a few nanometres, a droplet contains only hundreds of molecules, and a bulk surface tension is no longer meaningful.
- The ideal-gas vapour assumption fails near the critical point.
- Solutes on the droplet (e.g. dissolved salt in cloud droplets) lower its vapour pressure (Raoult) and compete with the Kelvin effect.

### Worked example

**Problem.** For pure water droplets at 20 °C, find the vapour pressure enhancement $`P^{V}/P^{\mathrm{SAT}}`$ for radii 1 µm, 100 nm, 10 nm and 1 nm, and the critical radius at supersaturations of 0.1 %, 1 % and 10 %. Data: $`\sigma = 72.7`$ mN m⁻¹, $`\underline{V}^{L} = 1.805\times10^{-5}`$ m³ mol⁻¹, $`P^{\mathrm{SAT}} = 2339`$ Pa.

**Enhancement from (119)**, with $`2\sigma\underline{V}^{L}/RT = 1.077`$ nm:

| $`r`$ | $`2\sigma/r`$ (bar) | $`P^{V}/P^{\mathrm{SAT}}`$ (119) | Full (118) |
|---|---|---|---|
| 1 µm | 1.45 | 1.0011 | 1.0011 |
| 100 nm | 14.5 | 1.011 | 1.011 |
| 10 nm | 145 | 1.114 | 1.114 |
| 1 nm | 1455 | 2.94 | 2.94 |

The neglected term in (118) changes nothing to four figures, because $`P^{V} - P^{\mathrm{SAT}}`$ is at most kilopascals, while $`2\sigma/r`$ is bars to kilobars.

**Critical radii.**

| Supersaturation $`S`$ | 1.001 | 1.01 | 1.1 |
|---|---|---|---|
| $`r^{*}`$ | 1.08 µm | 108 nm | 11 nm |

**Interpretation.** Air in a real cloud is typically only slightly supersaturated (well under a few percent). There, a droplet must already be about 0.1 µm across to grow. Random clustering of water molecules cannot reach that size, so clouds form on aerosol particles of about that size or larger. Without them, vapour would need several-fold supersaturation (the 1 nm row) to condense spontaneously.

### Link to other topics

The same equation controls capillary condensation in porous adsorbents (concave menisci *lower* the vapour pressure), cavitation, and crystal size distributions in crystallisers. Section 24 applies the same mechanical-plus-chemical equilibrium to bubbles, where the curvature is reversed.

### Summary

Surface tension raises the pressure inside a droplet by $`2\sigma/r`$. By the Poynting argument, this raises its equilibrium vapour pressure, giving the Kelvin equation $`\ln(P^{V}/P^{\mathrm{SAT}}) = 2\sigma\underline{V}^{L}/(rRT)`$. The effect is negligible above a micrometre but dominant at nanometres. This makes droplet nucleation hard and supersaturated vapours metastable.

## Section 24: Bubbles, superheating and boiling

### Intuition

Boiling means forming vapour *inside* the liquid. A newborn bubble is tiny, so surface tension squeezes it hard. It needs internal vapour pressure equal to the atmosphere plus $`2\sigma/r`$, and at the normal boiling point the liquid only supplies 1 atm. So a small bubble collapses unless the liquid is hotter.

In a clean, smooth pot, the liquid can sit above 100 °C with nothing happening until a bubble finally nucleates, then it boils violently ("bumping"). Scratches, dissolved gas, boiling chips or a handful of salt provide ready-made nuclei, and boiling starts close to the true boiling point.

*Physically:* the boiling point is where the vapour pressure equals the external pressure. That is a thermodynamic condition. Whether bubbles actually appear is a kinetic question about nucleation.

### Derivation

**Step 1: degrees of freedom.** As for droplets, the curved interface frees the pressure: $`F = 2`$, e.g. external pressure and bubble radius.

**Step 2: mechanical equilibrium.** The liquid is at atmospheric pressure (shallow pool), and the vapour inside is higher by the Laplace pressure:


```math
P^{V} = P^{L} + \frac{2\sigma}{r} = P^{\mathrm{ATM}} + \frac{2\sigma}{r} \tag{120}
```


**Step 3: chemical equilibrium.** Ideal-gas vapour: $`\mu^{V} = \underline{G}^{\mathrm{SAT}}(T) + RT\ln(P^{V}/P^{\mathrm{SAT}})`$. The liquid is only at about 1 atm, so its Poynting term is negligible: $`\mu^{L}\approx\underline{G}^{\mathrm{SAT}}(T)`$. (This is the difference from droplets, where the liquid was the compressed phase.) Equating gives $`P^{V} = P^{\mathrm{SAT}}(T)`$, so


```math
P^{\mathrm{SAT}}(T) = P^{\mathrm{ATM}} + \frac{2\sigma}{r} \tag{121}
```


The liquid must be hot enough that its *flat-surface* vapour pressure equals the pressure inside the bubble.

**Step 4: the required temperature.** At the normal boiling point $`T_b`$, $`P^{\mathrm{SAT}}(T_b) = P^{\mathrm{ATM}}`$. Integrating Clausius–Clapeyron with constant $`\Delta\underline{H}^{\mathrm{vap}}`$:


```math
\ln\frac{P^{\mathrm{SAT}}(T)}{P^{\mathrm{ATM}}} = \frac{\Delta\underline{H}^{\mathrm{vap}}}{R}\left(\frac{1}{T_b} - \frac{1}{T}\right) \tag{122}
```


Combining (121) and (122) gives the temperature at which a bubble of radius $`r`$ is just in equilibrium. Smaller bubbles need more superheat.

**Step 5: boiling-point elevation by an involatile solute.** Now take a flat surface and a liquid containing an involatile solute (salt or sugar), with the vapour pure solvent. Equilibrium for the solvent at pressure $`P`$:


```math
\underline{G}_1^{L}(T,P) + RT\ln(\gamma_1x_1) = \underline{G}_1^{V}(T,P)
```


so $`RT\ln(\gamma_1x_1) = \Delta\underline{G}^{\mathrm{vap}}(T)`$. As in Section 15, $`\Delta\underline{G}^{\mathrm{vap}}(T)\approx\Delta\underline{H}^{\mathrm{vap}}(T_b - T)/T_b`$, giving


```math
\ln(\gamma_1x_1) = \frac{\Delta\underline{H}^{\mathrm{vap}}}{R}\left(\frac{1}{T} - \frac{1}{T_b}\right) \;\;\Rightarrow\;\; \Delta T_b \approx \frac{RT_b^2M_1}{\Delta\underline{H}^{\mathrm{vap}}}\,m = K_b\,m \tag{123}
```


in the dilute ideal limit ($`-\ln x_1\approx x_2\approx M_1m`$, with $`m`$ the solute molality). Since $`\gamma_1x_1 < 1`$, $`T > T_b`$: the boiling point rises.

### Motivation and explanation

**Graphical view.** Plot $`\mu_1`$ (molar $`\underline{G}`$) against $`T`$ at constant $`P`$. Each phase gives a line of slope $`-\underline{S}`$: steepest for vapour, shallowest for solid. Melting and boiling points are where the lines cross. A solute lowers *only the liquid line*, by $`RT\ln(\gamma_1x_1)`$, because the solid and vapour are pure. The liquid's crossing with the solid moves to lower $`T`$ (freezing-point depression), and its crossing with the vapour moves to higher $`T`$ (boiling-point elevation). The vapour line is steeper than the solid line, so the same downward shift moves the boiling point less than the freezing point: $`K_b < K_f`$.

![Molar Gibbs energy against T at constant P for solid, liquid and vapour; dissolving a solute lowers only the liquid line by RT ln(γ1x1), depressing the freezing point and raising the boiling point](figs/ET-24-G-vs-T-solute.png)

**Pressure dependence.** $`(\partial\underline{G}/\partial P)_T = \underline{V}`$ and $`\underline{V}^{V}\gg\underline{V}^{L},\underline{V}^{S}`$. So changing the pressure mainly moves the vapour line. That is why boiling points depend strongly on pressure (altitude, pressure cookers) while melting points barely do.

**Limits.**
- Equation (121) treats the bubble as pure vapour. Dissolved gases add to the pressure inside it and reduce the superheat needed, which is one reason degassed water superheats more easily.
- At very small $`r`$ (nanometres), bulk $`\sigma`$ fails.
- Constant $`\Delta\underline{H}^{\mathrm{vap}}`$ in (122) is approximate for large superheats.

### Worked example

**Problem.** (a) For water at 1 atm, find the temperature at which a vapour bubble of radius 10 µm, 1 µm or 0.1 µm is in equilibrium. Data: $`\sigma(100\,°\mathrm{C}) = 58.9`$ mN m⁻¹, $`\Delta\underline{H}^{\mathrm{vap}} = 40.65`$ kJ mol⁻¹, $`T_b = 373.12`$ K. (b) Find water's ebullioscopic constant, and the boiling-point rise from 10 g of NaCl per kg of water (pasta water).

**(a)** From (121), then (122); IAPWS steam tables for comparison:

| $`r`$ | $`P^{\mathrm{SAT}}`$ required (bar) | $`T`$ from (122) | $`T`$ from steam tables |
|---|---|---|---|
| 10 µm | 1.131 | 103.1 °C | 103.1 °C |
| 1 µm | 2.19 | 123.3 °C | 123.1 °C |
| 0.1 µm | 12.8 | 189.5 °C | 190.9 °C |

**(b)** $`K_b = RT_b^2M_1/\Delta\underline{H}^{\mathrm{vap}} = 8.314\times373.12^2\times0.018015/40650 = 0.513`$ K kg mol⁻¹ (tabulated: 0.512). 10 g of NaCl is 0.171 mol, about 0.342 mol of ions per kg, so $`\Delta T_b\approx 0.18`$ K.

**Interpretation.**
- *Superheat:* a liquid with only micrometre-scale nuclei must be superheated by about 20 K before bubbles can grow. That is why smooth glassware bumps, and why boiling surfaces in evaporators and reboilers are engineered with nucleation sites.
- *Salt:* the boiling-point rise is under 0.2 K, irrelevant for cooking. The sudden fizz when salt is thrown into nearly boiling water is not thermodynamic. The crystals provide nucleation sites that release the superheat already stored in the liquid.

### Link to other topics

Nucleate boiling and its superheat govern heat-transfer coefficients in reboilers and evaporators. Boiling-point elevation sets the extra driving force needed in multiple-effect evaporators concentrating salt or sugar solutions. Cavitation in pumps is the same bubble equilibrium, reached by lowering the pressure rather than raising the temperature.

### Summary

A bubble needs its vapour pressure to exceed the surrounding pressure by $`2\sigma/r`$. Small nuclei therefore need substantial superheat, about 20 K for a 1 µm bubble in water, and clean liquids can be superheated until nucleation intervenes. Separately, an involatile solute lowers the liquid's chemical potential and raises the boiling point by $`K_bm`$, with $`K_b = 0.513`$ K kg mol⁻¹ for water. With equilibria at curved interfaces and membranes done, the course turns to the main event: vapour–liquid equilibrium of real binary mixtures.

## Conclusion

Each effect in this part follows from equal chemical potentials once the right mechanical condition is used: a membrane or a curved interface lets the pressures differ, and the compressed phase gains $`\underline{V}\,\Delta P`$ of chemical potential. Osmotic pressure, freezing-point depression and boiling-point elevation are all colligative measures of solvent activity. The next part turns to the central topic: vapour–liquid equilibrium of real binary mixtures.
<!-- reading-content:end -->

[Previous](06-01-phase-rule-osmosis-droplets-and-bubbles.md) · [Subject index](README.md) · [Next](07-01-vapour-liquid-equilibrium-of-real-mixtures.md)

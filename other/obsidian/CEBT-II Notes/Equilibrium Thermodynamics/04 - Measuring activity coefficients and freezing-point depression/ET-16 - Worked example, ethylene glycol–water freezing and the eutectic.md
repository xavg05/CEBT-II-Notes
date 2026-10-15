[Previous](<ET-15 - Freezing-point depression.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Section 16: Worked example, ethylene glycol–water freezing and the eutectic

*Components:* water (1), ethylene glycol (2).

## Intuition

Start from pure water and add glycol: the ice-freezing temperature falls. Start from pure glycol and add water: the glycol-freezing temperature falls too. The two curves run downward towards each other and must meet. At the meeting point (the eutectic) the liquid is in equilibrium with *both* solids at once.

Cool any liquid mixture and one solid crystallises first, depending on which side of the eutectic composition the liquid lies. The remaining liquid moves along that freezing curve towards the eutectic. At the eutectic the rest freezes together as a fine intergrowth of the two pure solids: the "eutectic solid". On a molecular scale each solid phase is still pure.

![Schematic solid–liquid phase diagram for water (x1) and ethylene glycol at 1 atm: two freezing curves meet at the eutectic; a cooled liquid (dot) first deposits ice, then moves along the water curve to the eutectic](../figs/ET-16-glycol-water-phase-diagram.png)

## Derivation

**Step 1: water (ice) freezing curve.** Pure ice is in equilibrium with the liquid:

$$\ln(\gamma_1x_1) = \frac{\Delta\underline{H}_1^{\mathrm{fus}}}{R}\left(\frac{1}{T_{f,1}} - \frac{1}{T}\right) \tag{84}$$

**Step 2: glycol freezing curve.** Pure solid glycol is in equilibrium with the liquid:

$$\ln(\gamma_2x_2) = \frac{\Delta\underline{H}_2^{\mathrm{fus}}}{R}\left(\frac{1}{T_{f,2}} - \frac{1}{T}\right) \tag{85}$$

**Step 3: eutectic.** Both conditions hold at once, with $x_1 + x_2 = 1$. For an ideal mixture ($\gamma_i = 1$), invert each equation for $x_i(T)$ and require

$$x_1(T_e) + x_2(T_e) = 1 \tag{86}$$

then solve for $T_e$ numerically.

**Step 4: activity coefficient from a measured freezing point.** If the measured freezing temperature on the ice branch is $T$ at known $x_1$, (84) gives

$$\gamma_1 = \frac{1}{x_1}\exp\!\left[\frac{\Delta\underline{H}_1^{\mathrm{fus}}}{R}\left(\frac{1}{T_{f,1}} - \frac{1}{T}\right)\right] \tag{87}$$

**Step 5: heat-capacity correction for large depressions.** If $\Delta\underline{C}_P = \underline{C}_P^{L} - \underline{C}_P^{S}$ is constant, integrating $d\Delta\underline{H} = \Delta\underline{C}_P\,dT$ and $d\Delta\underline{S} = (\Delta\underline{C}_P/T)\,dT$ from $T_f$ gives
$$\Delta\underline{H}(T) = \Delta\underline{H}^{\mathrm{fus}} + \Delta\underline{C}_P(T - T_f), \qquad \Delta\underline{S}(T) = \frac{\Delta\underline{H}^{\mathrm{fus}}}{T_f} + \Delta\underline{C}_P\ln\frac{T}{T_f},$$
and

$$\ln(\gamma_1x_1) = -\frac{\Delta\underline{H}(T) - T\,\Delta\underline{S}(T)}{RT} \tag{88}$$

This reduces to (84) when $\Delta\underline{C}_P = 0$.

## Worked example

**Data.**
- Water: $T_{f,1} = 273.15$ K, $\Delta\underline{H}_1^{\mathrm{fus}} = 6009$ J mol⁻¹; $\underline{C}_P^{L} = 75.34$ and $\underline{C}_P^{S} = 38.09$ J mol⁻¹ K⁻¹, so $\Delta\underline{C}_P = 37.25$ J mol⁻¹ K⁻¹.
- Ethylene glycol: $M = 62.07$ g mol⁻¹, $T_{f,2} = 260.25$ K (−12.9 °C), $\Delta\underline{H}_2^{\mathrm{fus}} = 9.958$ kJ mol⁻¹ (another measurement gives 11.6 kJ mol⁻¹).
- Observation: a 60 wt % glycol / 40 wt % water mixture freezes at about −45 °C.

**(a) Ideal eutectic.** Solving (86) gives $T_e = 222.2$ K (−51 °C) at $x_1 = 0.545$, i.e. 74 wt % glycol. The two pure components melt at 0 °C and −13 °C, yet the mixture stays liquid down to about −51 °C, purely from the entropy of mixing. The schematic diagram above is qualitative; its eutectic position is illustrative only.

**(b) The 60 wt % mixture.** Mole fractions: $n_2 = 60/62.07 = 0.967$ and $n_1 = 40/18.015 = 2.220$ per 100 g, so $x_2 = 0.303$ and $x_1 = 0.697$.
- Ice branch, ideal, from (84): $T = 240.3$ K (−33 °C). With the heat-capacity correction (88): −37 °C.
- Glycol branch, ideal, from (85): −66 °C, below the ice branch. So ice is the first solid to appear at this composition.

The real mixture freezes at about −45 °C, 8–12 K **lower** than the ideal prediction.

Cooling starts from above both candidate freezing temperatures, so the *higher* branch is encountered first. Once ice appears, it removes water without removing glycol. The overall composition of the closed sample is unchanged, but the remaining liquid becomes glycol-richer and follows the ice branch towards the eutectic. A vertical cooling path for the whole sample is therefore not a constant-composition path for its liquid phase.

Equation (86) finds where one liquid composition can simultaneously satisfy both pure-solid equilibrium conditions. Above that intersection only one solid is stable against the liquid at a time; at the intersection both can coexist. The measured first-freezing point of the water-rich mixture constrains water activity on the ice branch, rather than locating the eutectic of the real system.

**(c) Water's activity coefficient** from (87) or (88) at $T = 228.15$ K:

| Treatment | $\gamma_1x_1$ | $\gamma_1$ |
|---|---|---|
| Constant $\Delta\underline{H}^{\mathrm{fus}}$, (87) | 0.593 | 0.85 |
| With $\Delta\underline{C}_P$, (88) | 0.641 | 0.92 |

**Interpretation.** $\gamma_1 < 1$: water is held more strongly in the glycol mixture than an ideal mixture would hold it. This is a negative deviation, consistent with strong water–glycol hydrogen bonding between the –OH groups. It lowers water's chemical potential further and so deepens the freezing-point depression beyond the ideal value. That is good for antifreeze.

The heat-capacity correction shifts $\gamma_1$ from 0.85 to 0.92. For a 45 K depression the constant-$\Delta\underline{H}$ assumption is no longer negligible, and the inferred $\gamma$ is only as good as the thermal data. The freezing temperature and the glycol $\Delta\underline{H}^{\mathrm{fus}}$ are also approximate, so these are estimates.

## Motivation and explanation

**Why a eutectic exists.** Each pure solid excludes the other component, so mixing always stabilises the liquid relative to either solid. Both freezing curves therefore slope downward from the pure-component melting points, and they must intersect. Below $T_e$ no liquid can exist at any composition.

**What is assumed.**
- Pure solids only. Some systems form compounds or hydrates (water of crystallisation), which add extra branches and peaks to the diagram.
- Equilibrium. Glycol–water mixtures readily supercool and can form glasses at low temperature, so real cooling may not follow the diagram.

**Engineering consequence.** The lowest protection is reached near the eutectic composition, not with pure glycol. More glycol beyond that point *raises* the freezing temperature again, because the liquid then sits on the glycol branch. Practical antifreeze mixtures stay on the water-rich side.

## Link to other topics

The same two-branch construction gives the phase diagrams of alloys, such as tin–lead solders, and of pharmaceutical co-crystals. Non-ideal $\gamma$'s from an activity-coefficient model can be inserted directly into (84)–(85) to predict the curves, and the models that would do that are surveyed in the next unit.

## Summary

Applying the freezing-point equation to each component gives two freezing curves that meet at a eutectic. For ideal glycol–water this is about −51 °C at 74 wt % glycol. The real 60 wt % mixture freezes about 10 K below the ideal prediction, revealing a negative deviation ($\gamma_{\mathrm{water}} \approx 0.85$–$0.92$) caused by hydrogen bonding.

## Conclusion

Activity coefficients are inferred from measurements of something in equilibrium with the mixture: boiling pressures, vapour compositions or freezing temperatures. Freezing-point depression is both a measurement method and a design tool, giving freezing curves, eutectics and the cryoscopic constant. The next part surveys the activity-coefficient models these measurements are fitted to.
<!-- note-content:end -->

[Previous](<ET-15 - Freezing-point depression.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

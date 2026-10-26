[Previous](<ET-15 - Freezing-point depression.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Section 16: ethylene glycol–water freezing and the eutectic

*Components:* water (1), ethylene glycol (2).

## Intuition

Start from pure water and add glycol: the ice-freezing temperature falls. Start from pure glycol and add water: the glycol-freezing temperature falls too. The two curves run downward towards each other and must meet. At the meeting point (the eutectic) the liquid is in equilibrium with *both* solids at once.

Cool any liquid mixture and one solid crystallises first, depending on which side of the eutectic composition the liquid lies. The remaining liquid moves along that freezing curve towards the eutectic. At the eutectic the rest freezes together as a fine intergrowth of the two pure solids: the "eutectic solid". On a molecular scale each solid phase is still pure.

![Schematic solid–liquid phase diagram for water (x1) and ethylene glycol at 1 atm: two freezing curves meet at the eutectic; a cooled liquid (dot) first deposits ice, then moves along the water curve to the eutectic](../figs/ET-16-glycol-water-phase-diagram.png)

## Derivation

**Step 1: water (ice) freezing curve.** Pure ice is in equilibrium with the liquid:


**Equation (84)**

```math
\ln(\gamma_1x_1) = \frac{\Delta\underline{H}_1^{\mathrm{fus}}}{R}\left(\frac{1}{T_{f,1}} - \frac{1}{T}\right)
```


**Step 2: glycol freezing curve.** Pure solid glycol is in equilibrium with the liquid:


**Equation (85)**

```math
\ln(\gamma_2x_2) = \frac{\Delta\underline{H}_2^{\mathrm{fus}}}{R}\left(\frac{1}{T_{f,2}} - \frac{1}{T}\right)
```


**Step 3: eutectic.** Both conditions hold at once, with $`x_1 + x_2 = 1`$. For an ideal mixture ($`\gamma_i = 1`$), invert each equation for $`x_i(T)`$ and require


**Equation (86)**

```math
x_1(T_e) + x_2(T_e) = 1
```


then solve for $`T_e`$ numerically.

**Step 4: activity coefficient from a measured freezing point.** If the measured freezing temperature on the ice branch is $`T`$ at known $`x_1`$, (84) gives


**Equation (87)**

```math
\gamma_1 = \frac{1}{x_1}\exp\!\left[\frac{\Delta\underline{H}_1^{\mathrm{fus}}}{R}\left(\frac{1}{T_{f,1}} - \frac{1}{T}\right)\right]
```


**Step 5: heat-capacity correction for large depressions.** If $`\Delta\underline{C}_P = \underline{C}_P^{L} - \underline{C}_P^{S}`$ is constant, integrating $`d\Delta\underline{H} = \Delta\underline{C}_P\,dT`$ and $`d\Delta\underline{S} = (\Delta\underline{C}_P/T)\,dT`$ from $`T_f`$ gives

```math
\Delta\underline{H}(T) = \Delta\underline{H}^{\mathrm{fus}} + \Delta\underline{C}_P(T - T_f), \qquad \Delta\underline{S}(T) = \frac{\Delta\underline{H}^{\mathrm{fus}}}{T_f} + \Delta\underline{C}_P\ln\frac{T}{T_f},
```

and


**Equation (88)**

```math
\ln(\gamma_1x_1) = -\frac{\Delta\underline{H}(T) - T\,\Delta\underline{S}(T)}{RT}
```


This reduces to (84) when $`\Delta\underline{C}_P = 0`$.

## Motivation and explanation

**Thermal data and the ideal reference diagram.** With water $`T_{f,1}=273.15\ \mathrm K`$ and $`\Delta\underline H_1^{\mathrm{fus}}=6009\ \mathrm{J\,mol^{-1}}`$, and glycol $`T_{f,2}=260.25\ \mathrm K`$ and $`\Delta\underline H_2^{\mathrm{fus}}=9958\ \mathrm{J\,mol^{-1}}`$, solving the two ideal branch conditions gives $`T_e\approx222.2\ \mathrm K`$ at $`x_1\approx0.545`$. Molar masses 18.015 and $`62.07\ \mathrm{g\,mol^{-1}}`$ convert this to about 74 wt % glycol. These are ideal-model values, rather than positions read from the qualitative schematic.
For 60 wt % glycol, the constant-enthalpy ideal ice branch gives about $`-33\ ^\circ\mathrm C`$; adding the water heat-capacity difference gives about $`-37\ ^\circ\mathrm C`$. The ideal glycol branch is lower, near $`-66\ ^\circ\mathrm C`$, so ice appears first. Comparing these predictions with a reported first-freezing temperature near $`-45\ ^\circ\mathrm C`$ distinguishes thermal-data corrections from mixture-activity corrections.

**Following the liquid during freezing.** For a fixed overall glycol–water composition, cooling encounters the *higher* of the two candidate pure-solid freezing branches first. Once ice forms, it removes water without glycol. The closed sample's overall composition stays fixed while its remaining liquid becomes glycol-richer and follows the ice branch towards the eutectic. A vertical cooling path for the whole sample is therefore not a constant-composition path for its liquid.
The eutectic is the intersection where one liquid composition satisfies both pure-solid equilibrium conditions. A measured first-freezing temperature on the water-rich side constrains water activity on the ice branch; it does not locate the real eutectic.
For the reported 60 wt % glycol mixture freezing near $`-45\ ^\circ\mathrm C`$, the water mole fraction is about 0.697. Inverting the ice equilibrium at 228.15 K gives $`\gamma_1\approx0.85`$ with constant fusion enthalpy, or about 0.92 with $`\Delta\underline C_P=37.25\ \mathrm{J\,mol^{-1}\,K^{-1}}`$. Both imply additional water stabilisation beyond ideal mixing, consistent with hydrogen bonding. The shift between the inferred coefficients shows that a large freezing depression also tests the pure-component thermal approximation: apparent mixture non-ideality cannot be separated reliably from inaccurate thermal data.

**Why a eutectic exists.** Each pure solid excludes the other component, so mixing always stabilises the liquid relative to either solid. Both freezing curves therefore slope downward from the pure-component melting points, and they must intersect. Below $`T_e`$ no liquid can exist at any composition.

**What is assumed.**
- Pure solids only. Some systems form compounds or hydrates (water of crystallisation), which add extra branches and peaks to the diagram.
- Equilibrium. Glycol–water mixtures readily supercool and can form glasses at low temperature, so real cooling may not follow the diagram.

**Engineering consequence.** The lowest protection is reached near the eutectic composition, not with pure glycol. More glycol beyond that point *raises* the freezing temperature again, because the liquid then sits on the glycol branch. Practical antifreeze mixtures stay on the water-rich side.

## Link to other topics

The same two-branch construction gives the phase diagrams of alloys, such as tin–lead solders, and of pharmaceutical co-crystals. Non-ideal $`\gamma`$'s from an activity-coefficient model can be inserted directly into (84)–(85) to predict the curves, and the models that would do that are surveyed in the next unit.

## Summary

Applying the freezing-point equation to each component gives two freezing curves that meet at a eutectic. For ideal glycol–water this is about −51 °C at 74 wt % glycol. The real 60 wt % mixture freezes about 10 K below the ideal prediction, revealing a negative deviation ($`\gamma_{\mathrm{water}} \approx 0.85`$–$`0.92`$) caused by hydrogen bonding.

## Conclusion

Activity coefficients are inferred from measurements of something in equilibrium with the mixture: boiling pressures, vapour compositions or freezing temperatures. Freezing-point depression is both a measurement method and a design tool, giving freezing curves, eutectics and the cryoscopic constant. The next part surveys the activity-coefficient models these measurements are fitted to.
<!-- note-content:end -->

[Previous](<ET-15 - Freezing-point depression.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

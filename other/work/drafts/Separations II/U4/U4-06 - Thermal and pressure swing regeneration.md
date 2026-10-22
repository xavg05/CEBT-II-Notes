# Thermal and pressure swing regeneration

## Overview

Assumed: adsorption isotherms and working capacity.

Regeneration reduces equilibrium loading by changing operating conditions. Thermal swing heats the bed; pressure swing reduces adsorbate partial pressure. Their useful capacity is the difference between loading and regeneration states.

## Intuition

A strongly adsorbing surface holds solute at feed conditions. To release it, create conditions under which that same loading is excessive. Heating changes affinity; depressurisation or clean purge reduces the surrounding adsorbate activity.

![High-pressure loading and low-pressure regeneration in paired beds](../figs/u4-pressure-swing.png)

## Derivation

**Step 1: express the equilibrium capacity difference.** For gas Langmuir capacity $Q_m$, loading partial pressure $p_H$, regeneration partial pressure $p_L$ and affinity $b$ at fixed temperature,

$$\Delta q_{\mathrm{eq}}=Q_m\left[\frac{bp_H}{1+bp_H}-\frac{bp_L}{1+bp_L}\right].\tag{1}$$

*Reason:* pressure swing moves between two points on the same isotherm. Partial pressure, not total pressure alone, sets the solute loading.

**Step 2: adapt to thermal swing.** If adsorption occurs at $T_L$ and regeneration at $T_H$, use the isotherm appropriate to each temperature:

$$\Delta q_{\mathrm{eq}}=q^*(p_{\mathrm{load}},T_L)-q^*(p_{\mathrm{regen}},T_H).\tag{2}$$

*Reason:* heating generally reduces exothermic equilibrium affinity, while purge also changes the gas-phase partial pressure. Actual cyclic capacity is smaller when loading stops before equilibrium or regeneration leaves a larger heel.

Both swing pressures matter relative to the isotherm's bend. If loading and regeneration lie on the nearly saturated plateau, a large pressure change can leave both loadings almost equal. Moving regeneration into the responsive lower-pressure region creates a larger capacity difference. Strong affinity is consequently useful only when the available regeneration conditions can move loading far enough back down the isotherm.

Reducing total pressure lowers solute partial pressure only in combination with the gas composition; purge changes that composition too. The cycle calculation must then debit the product spent on purge and allow the bed to return to loading conditions. Equilibrium working capacity alone contains neither of those recovery and scheduling costs.

## Motivation and explanation

In a simple paired pressure-swing cycle, bed A loads at high pressure while a portion of its product expands and purges bed B at low pressure. B then repressurises while A depressurises. Their roles reverse, followed by the complementary pressure change. Product used for purge and repressurisation reduces net recovery; equilibrium capacity alone does not predict purity or recovery.

Thermal swing needs time to heat, desorb and cool. Poor heat conduction within a packed bed can make temperature fronts slow; the next loading step must wait for suitable conditions. Two beds support continuous treatment only if the off-line bed completes regeneration and preparation within the on-line service period; more beds may be needed.

Liquid purification can instead change pH, ionic strength or solvent composition. Restoration to the initial binding conditions is still necessary before reuse. Strong affinity helps loading but may raise regeneration duty or damage a heat-sensitive target.

The equilibrium loading difference between high and low pressure is an upper estimate for pressure-swing capacity under those two states. A finite cycle may not reach either equilibrium because desorption, diffusion and pressure changes take time. Use measured working capacity for the actual cycle instead of assigning the full equilibrium difference automatically.

## Link to other topics

Regeneration follows equilibrium shifts familiar from thermodynamics, while its cycle time depends on heat and mass transport. Liquid elution uses the same reversible binding to separate different species by their migration times.

## Conclusion

Design loading and regeneration together. Capacity, heat transfer, purge consumption and cycle scheduling determine whether continuous treatment is feasible.

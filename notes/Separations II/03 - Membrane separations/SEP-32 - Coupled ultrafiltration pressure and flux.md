[Previous](<SEP-31 - Osmotic pressure and reverse solvent flow.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-33 - Continuous membrane plants and fouling.md>)

<!-- note-content:start -->
# SEP-32: Coupled ultrafiltration pressure and flux

## Overview

Assumed knowledge: concentration-polarisation film theory and osmotic solvent flux.

Ultrafiltration pressure, wall concentration and solvent flux must be solved together. This note gives a design procedure for a fully rejected protein solution and demonstrates why its flux–pressure curve bends towards a gel-limited plateau.

## Intuition

Increasing pressure first increases water flux. That faster flux carries more retained protein to the wall, where the higher concentration raises osmotic pressure. Part of every further pressure increase is then spent opposing the newly intensified polarisation. Eventually the wall reaches its gel concentration and a deposit provides additional resistance.

## Derivation

Let $`C_f`$ be bulk protein concentration, $`C_w`$ wall concentration and $`C_p=0`$ because protein is completely rejected. Let $`k_f`$ be the film coefficient and $`K_V`$ hydraulic permeance. Assume steady local conditions, constant $`k_f`$, temperature and clean-membrane permeance before gel formation, and a measured osmotic-pressure function $`\Pi(C)`$.

The polarisation equation gives


**Equation (136)**

```math
J_V=k_f\ln(C_w/C_f),\qquad
C_w=C_fe^{J_V/k_f}.
```


Pure-solvent permeate has zero protein osmotic pressure. Rearranging the solvent flux law gives


**Equation (137)**

```math
\Delta P=\Pi(C_w)+\frac{J_V}{K_V}.
```


Substitute Equation (136) into Equation (137) to obtain one equation for the pressure needed for any chosen sub-gel flux:


**Equation (138)**

```math
\Delta P(J_V)=\Pi\!\left(C_fe^{J_V/k_f}\right)+\frac{J_V}{K_V}.
```


This parametrisation is efficient: choose a trial flux, compute $`C_w`$, evaluate the wall osmotic pressure, then add the hydraulic pressure requirement. For specified pressure, numerically solve the same monotonic relationship over the permitted sub-gel range.

At zero flux, $`C_w=C_f`$, so the threshold is $`\Delta P_0=\Pi(C_f)`$. At gel onset, set $`C_w=C_G`$:


**Equation (139)**

```math
J_V^*=k_f\ln(C_G/C_f),\qquad
\Delta P_G=\Pi(C_G)+\frac{J_V^*}{K_V}.
```


The hydraulic term in Equation (139) uses the pre-gel membrane permeance. Once a gel grows, its additional resistance makes the effective permeance different.

Parametrising by flux follows the causal chain cleanly: chosen water flow determines retained-protein delivery; the film balance determines wall concentration; the osmotic relation then determines the thermodynamic pressure penalty. Adding the hydraulic pressure drop gives the total required pressure. Guessing wall concentration independently would generally violate one of those linked balances.

The increasing curvature of the pressure–flux relation means that equal extra pressure increments produce progressively smaller flux gains. Wall concentration grows exponentially with the chosen flux, and the measured osmotic pressure grows strongly with wall concentration. The gel endpoint introduces a further physical constraint; it is not a licence to extrapolate the clean-membrane permeance indefinitely.

## Motivation and explanation

The calculation separates two causes of pressure demand. $`\Pi(C_w)`$ compensates for the thermodynamic tendency towards osmosis; $`J_V/K_V`$ produces the desired flow through the selective layer. A high clean-water permeance reduces the second term but does not remove the first.

The design procedure is to check flow regime, establish $`k_f`$, find the zero-flux and gel limits, and solve only between those bounds. The permitted curve must be recalculated as bulk feed concentrates. A pressure increase beyond gel onset should not be extrapolated with the clean-membrane relationship.

## Link to other topics

This calculation couples equilibrium thermodynamics with a transport boundary layer. Continuous recycle provides one way to sustain the high tangential velocities that improve the film coefficient while setting an independent net production rate.

## Conclusion

Calculate wall concentration before calculating osmotic pressure. The coupled model establishes a useful operating curve and a gel-onset limit; clean-water permeance alone cannot predict protein-solution throughput.
<!-- note-content:end -->

[Previous](<SEP-31 - Osmotic pressure and reverse solvent flow.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-33 - Continuous membrane plants and fouling.md>)

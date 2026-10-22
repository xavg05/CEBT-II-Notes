# Coupled ultrafiltration pressure and flux

## Overview

Assumed knowledge: concentration-polarisation film theory and osmotic solvent flux.

Ultrafiltration pressure, wall concentration and solvent flux must be solved together. This note gives a design procedure for a fully rejected protein solution and demonstrates why its flux–pressure curve bends towards a gel-limited plateau.

## Intuition

Increasing pressure first increases water flux. That faster flux carries more retained protein to the wall, where the higher concentration raises osmotic pressure. Part of every further pressure increase is then spent opposing the newly intensified polarisation. Eventually the wall reaches its gel concentration and a deposit provides additional resistance.

## Derivation

Let $C_f$ be bulk protein concentration, $C_w$ wall concentration and $C_p=0$ because protein is completely rejected. Let $k_f$ be the film coefficient and $K_V$ hydraulic permeance. Assume steady local conditions, constant $k_f$, temperature and clean-membrane permeance before gel formation, and a measured osmotic-pressure function $\Pi(C)$.

The polarisation equation gives

$$
J_V=k_f\ln(C_w/C_f),\qquad
C_w=C_fe^{J_V/k_f}. \tag{1}
$$

Pure-solvent permeate has zero protein osmotic pressure. Rearranging the solvent flux law gives

$$
\Delta P=\Pi(C_w)+\frac{J_V}{K_V}. \tag{2}
$$

Substitute Equation (1) into Equation (2) to obtain one equation for the pressure needed for any chosen sub-gel flux:

$$
\Delta P(J_V)=\Pi\!\left(C_fe^{J_V/k_f}\right)+\frac{J_V}{K_V}. \tag{3}
$$

This parametrisation is efficient: choose a trial flux, compute $C_w$, evaluate the wall osmotic pressure, then add the hydraulic pressure requirement. For specified pressure, numerically solve the same monotonic relationship over the permitted sub-gel range.

At zero flux, $C_w=C_f$, so the threshold is $\Delta P_0=\Pi(C_f)$. At gel onset, set $C_w=C_G$:

$$
J_V^*=k_f\ln(C_G/C_f),\qquad
\Delta P_G=\Pi(C_G)+\frac{J_V^*}{K_V}. \tag{4}
$$

The hydraulic term in Equation (4) uses the pre-gel membrane permeance. Once a gel grows, its additional resistance makes the effective permeance different.

Parametrising by flux follows the causal chain cleanly: chosen water flow determines retained-protein delivery; the film balance determines wall concentration; the osmotic relation then determines the thermodynamic pressure penalty. Adding the hydraulic pressure drop gives the total required pressure. Guessing wall concentration independently would generally violate one of those linked balances.

The increasing curvature of the pressure–flux relation means that equal extra pressure increments produce progressively smaller flux gains. Wall concentration grows exponentially with the chosen flux, and the measured osmotic pressure grows strongly with wall concentration. The gel endpoint introduces a further physical constraint; it is not a licence to extrapolate the clean-membrane permeance indefinitely.

## Motivation and explanation

The calculation separates two causes of pressure demand. $\Pi(C_w)$ compensates for the thermodynamic tendency towards osmosis; $J_V/K_V$ produces the desired flow through the selective layer. A high clean-water permeance reduces the second term but does not remove the first.

The design procedure is to check flow regime, establish $k_f$, find the zero-flux and gel limits, and solve only between those bounds. The permitted curve must be recalculated as bulk feed concentrates. A pressure increase beyond gel onset should not be extrapolated with the clean-membrane relationship.

Concentrate cheese whey protein from a bulk concentration $C_f=10\,\mathrm{g\,L^{-1}}$ in a tubular membrane of internal diameter $0.02\,\mathrm m$. Take internal flow velocity $1.5\,\mathrm{m\,s^{-1}}$, $\rho=1000\,\mathrm{kg\,m^{-3}}$, $\mu=0.001\,\mathrm{Pa\,s}$ and protein diffusivity $4\times10^{-11}\,\mathrm{m^2\,s^{-1}}$. The specified film coefficient is $k_f=7.8\times10^{-6}\,\mathrm{m\,s^{-1}}$, hydraulic permeance $K_V=250\,\mathrm{L\,m^{-2}\,h^{-1}\,bar^{-1}}$, rejection is unity, and gel concentration is $400\,\mathrm{g\,L^{-1}}$.

For these stated conditions, the measured correlation is

$$
\Pi\,[\mathrm{bar}]=0.0044c-1.7\times10^{-6}c^2+7.9\times10^{-8}c^3,
$$

where $c$ is the **numerical value** of concentration in $\mathrm{g\,L^{-1}}$. Its coefficients already contain the required units.

The flow gives $\mathrm{Re}=30\,000$ and $\mathrm{Sc}=25\,000$. It is turbulent, but the very small protein diffusivity still permits strong polarisation. Use the supplied $k_f$ rather than replacing it with an unqualified correlation extrapolation.

At zero flux, the measured correlation gives $\Pi(10)=0.043909\,\mathrm{bar}$, which is the pressure threshold. At gel onset, $\Pi(400)=6.54400\,\mathrm{bar}$ and Equation (4) gives

$$
J_V^*=2.87733\times10^{-5}\,\mathrm{m\,s^{-1}}
=103.584\,\mathrm{L\,m^{-2}\,h^{-1}}.
$$

The conversion multiplies metres per second by $1000$ litres per cubic metre and $3600$ seconds per hour. The required gel-onset pressure is $\Delta P_G=6.95833\,\mathrm{bar}$.

For a requested $36\,\mathrm{L\,m^{-2}\,h^{-1}}$, first convert to $J_V=1.00\times10^{-5}\,\mathrm{m\,s^{-1}}$. Equation (1) gives $C_w=36.0403\,\mathrm{g\,L^{-1}}$. The wall osmotic pressure is $0.160067\,\mathrm{bar}$, while $J_V/K_V=36/250=0.144\,\mathrm{bar}$. The required pressure is therefore $0.304067\,\mathrm{bar}$.

Repeating the same steps gives:

| Flux, $\mathrm{L\,m^{-2}\,h^{-1}}$ | Wall concentration, $\mathrm{g\,L^{-1}}$ | Required pressure, bar |
|---:|---:|---:|
| 0 | 10.00 | 0.0439 |
| 20 | 20.39 | 0.1697 |
| 36 | 36.04 | 0.3041 |
| 60 | 84.72 | 0.6486 |
| 80 | 172.71 | 1.4362 |
| 100 | 352.07 | 5.1861 |
| 103.58 | 400.00 | 6.9583 |

![Ultrafiltration flux rises increasingly slowly with applied pressure](../figs/u3-10-whey-pressure.png)

The horizontal axis is imposed pressure difference and the vertical axis is solvent flux. The low-pressure threshold precedes the steep initial rise; the curve then flattens as the wall osmotic penalty grows, ending at gel onset rather than defining a post-gel operating law. At high flux, most imposed pressure offsets the greatly increased wall osmotic pressure. Reaching higher productivity then requires changing mass transfer, concentration or membrane area rather than simply extending the pressure curve.

## Link to other topics

This calculation couples equilibrium thermodynamics with a transport boundary layer. Continuous recycle provides one way to sustain the high tangential velocities that improve the film coefficient while setting an independent net production rate.

## Conclusion

Calculate wall concentration before calculating osmotic pressure. The coupled model establishes a useful operating curve and a gel-onset limit; clean-water permeance alone cannot predict protein-solution throughput.

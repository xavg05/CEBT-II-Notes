# Solute rejection in liquid membranes

## Overview

Assumed knowledge: liquid concentrations and flux-based membrane balances.

For a dilute liquid solution, the solvent supplies nearly all permeate volume. Combining solvent flow with solute diffusion explains why rejection depends on operating flux as well as membrane selectivity. This note derives that dependence before introducing external concentration polarisation.

## Intuition

The permeate concentration is the solute amount crossing per unit volume of solvent crossing. If solvent throughput increases faster than solute throughput, the solute is diluted in the permeate and apparent rejection rises. Rejection is therefore an operating result, even for a membrane whose transport coefficients remain constant.

## Derivation

Consider one dilute solute $B$ in solvent $V$. Let $N_B$ be solute molar flux, $J_V$ solvent volumetric flux and $C_p$ solute concentration in the newly produced permeate. Assume that solute contributes negligible volume. A local permeate component balance gives

$$
N_B=J_VC_p. \tag{1}
$$

The units are consistent: $\mathrm{m\,s^{-1}}$ times $\mathrm{mol\,m^{-3}}$ gives $\mathrm{mol\,m^{-2}\,s^{-1}}$.

Assume linear solute transfer with overall coefficient $K_{O,B}$ on a bulk-to-permeate concentration basis:

$$
N_B=K_{O,B}(C_f-C_p). \tag{2}
$$

Equate Equations (1) and (2), since they describe the same crossing solute:

$$
J_VC_p=K_{O,B}C_f-K_{O,B}C_p.
$$

Collect terms containing $C_p$ and divide by their coefficient:

$$
C_p=C_f\frac{K_{O,B}}{J_V+K_{O,B}}. \tag{3}
$$

The apparent rejection $R_B=1-C_p/C_f$ is consequently

$$
R_B=\frac{J_V}{J_V+K_{O,B}}. \tag{4}
$$

Both $K_{O,B}$ and $J_V$ have velocity units, so the ratio is dimensionless. Without external polarisation, the membrane-wall and bulk concentrations coincide and the same expression describes true rejection with membrane solute permeance replacing the overall coefficient.

## Motivation and explanation

When $J_V\gg K_{O,B}$, relatively little solute crosses per solvent volume and rejection approaches one. When $J_V\ll K_{O,B}$, the emerging solution approaches the feed concentration and rejection approaches zero. At exactly zero solvent flux, Equation (1) does not define a produced permeate stream; the small-flux result is a limit.

For a pressure-driven solvent flux with negligible osmotic opposition, write

$$
J_V=K_{V,0}\Delta P, \tag{5}
$$

where $K_{V,0}$ is hydraulic permeance and $\Delta P=P_f-P_p$. Its units are $\mathrm{m\,s^{-1}\,bar^{-1}}$ if pressure is in bar. Hydraulic permeance is not the same quantity as a concentration-based solute coefficient: their units encode different driving forces.

Significant osmotic pressure replaces $\Delta P$ by its net value, and substantial concentration polarisation means that the solute transport law must use $C_w$ rather than assuming $C_w=C_f$. In those cases Equations (3)–(4) alone do not predict the operating rejection.

Dialysis is a separate concentration-driven mode. A solute can diffuse from feed into a sweep liquid even at equal total pressures. Such transport does not require a positive pressure-driven solvent flux and must not be interpreted with the simplified dilution argument unless solvent flow is actually present.

## Worked example

Two trials use the same membrane and dilute feed but different pressures. In the first, osmotic opposition and external films are negligible; increasing pressure increases $J_V$ through Equation (5), while $K_{O,B}$ remains constant. Equation (4) predicts higher rejection.

In the second, retained solute accumulates at the wall. Increasing pressure raises $C_w$ and therefore the solute driving force; it also increases osmotic opposition to solvent flow. Rejection need not follow the first trial's trend. A measured pressure–rejection curve must therefore be interpreted alongside mass-transfer conditions.

## Link to other topics

The permeate dilution argument resembles competing transport-rate calculations in gas membranes. Concentration polarisation connects the liquid result to the convection–diffusion balance in a boundary layer.

## Conclusion

Solute rejection depends on how much solute crosses relative to solvent volume. The simple result is useful under dilute linear conditions, while polarisation and osmotic pressure require a coupled wall-concentration calculation.

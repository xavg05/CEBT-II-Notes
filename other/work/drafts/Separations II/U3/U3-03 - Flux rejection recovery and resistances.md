# Flux, rejection, recovery and resistances

## Overview

Assumed knowledge: material balances and linear mass-transfer laws.

Membrane performance requires separate measures of productivity, selectivity and stream recovery. This note defines them and derives a resistance model, while distinguishing bulk concentration from the actual membrane-surface concentration.

## Intuition

High flux means a small area can carry a large throughput. High rejection means little of a chosen solute appears in the permeate relative to the feed-side concentration. High recovery means a large fraction of feed becomes permeate. A membrane can have excellent rejection but poor flux, or high recovery but a product that fails the concentration requirement.

![Feed, retentate, permeate and local wall concentration](../figs/u3-03-stream-definitions.png)

Use subscripts $1$, $2$ and $3$ for inlet feed, collected permeate and outlet retentate. Locally, $f$ denotes feed-side bulk fluid, $w$ the feed-side membrane wall and $p$ the permeate. Local quantities can change along the membrane.

## Derivation

For uniform permeate volumetric flux $J$ over area $A$, the flow is $Q_p=JA$, so

$$
J=\frac{Q_p}{A},\qquad N_p=\rho_m J. \tag{1}
$$

$J$ has units $\mathrm{m^3\,m^{-2}\,s^{-1}}$ or $\mathrm{m\,s^{-1}}$; $N_p$ is total molar flux and $\rho_m$ is permeate molar density. For variable flux, $Q_2=\int_AJ\,dA$; Equation (1) then defines an area-average flux.

For solute concentrations $C_f$, $C_w$ and $C_p$, define

$$
R_{\mathrm{app}}=1-\frac{C_p}{C_f},\qquad
R_{\mathrm{true}}=1-\frac{C_p}{C_w}. \tag{2}
$$

The first is apparent rejection based on bulk feed, the second intrinsic or true rejection based on the wall. Complete rejection gives $C_p=0$ and both equal unity. In a concentration-polarised retained-solute system, $C_w>C_f$, so the apparent rejection is lower than true rejection at the same $C_p$.

The overall stage cut and recovery of an individual solute are different:

$$
S=\frac{Q_2}{Q_1},\qquad
\eta_j=\frac{Q_2C_{2,j}}{Q_1C_{1,j}}. \tag{3}
$$

For gas mixtures with flows reported at a common reference pressure and temperature, replace concentrations by mole fractions in the component recovery ratio. Actual gas volumes at different operating pressures must first be converted to molar rates or common-reference volumes.

For a permeating component $j$, assume steady linear transport through a feed film, membrane and permeate film. Express all three concentration drops on a common fluid-equivalent concentration basis. Their flux laws are

$$
N_j=k_{f,j}(C_{f,j}-C_{w,j})
=K_{m,j}(C_{w,j}-C_{p,i,j})
=k_{p,j}(C_{p,i,j}-C_{p,j}),
$$

where $C_{p,i,j}$ is the permeate-side interfacial concentration and $k_f$, $K_m$, $k_p$ are the corresponding coefficients. Partition factors must be absorbed into these coefficients when concentration jumps occur at interfaces.

Divide each concentration drop by the common flux, then add the drops. Intermediate concentrations cancel because the resistances are in series:

$$
\frac{C_{f,j}-C_{p,j}}{N_j}
=\frac1{k_{f,j}}+\frac1{K_{m,j}}+\frac1{k_{p,j}}.
$$

Defining an overall coefficient $K_{O,j}$ therefore gives

$$
N_j=K_{O,j}(C_{f,j}-C_{p,j}),\qquad
\frac1{K_{O,j}}=\frac1{k_{f,j}}+\frac1{K_{m,j}}+\frac1{k_{p,j}}. \tag{4}
$$

## Motivation and explanation

The largest reciprocal coefficient is the dominant resistance. If gas-side films offer negligible resistance, $K_O\approx K_m$. If a liquid film controls transfer, thinning the selective layer gives little benefit: the external resistance still limits performance.

The simple series model describes linear permeating-solute transport. A retained solute accumulating under significant solvent convection needs the concentration-polarisation film balance instead; its wall concentration can exceed bulk concentration rather than decline towards the membrane. Without polarisation, $C_w\approx C_f$.

Porous ultrafiltration membranes are often assigned a **molecular-weight cut-off**, conventionally the molecular mass at which a test solute has $90\%$ rejection. Real rejection curves are smooth because pores have a size distribution and solute shape and interactions vary. A cut-off is a measured performance marker, not an exact pore diameter or a guarantee for every molecule of that mass.

For gases, ideal selectivity is $\alpha=K_{m,A}/K_{m,B}$. This ratio measures material preference; finite permeate pressure and feed depletion also influence the achieved composition.

## Worked example

A membrane is reported to have high apparent rejection in a dilute test, but lower apparent rejection with a concentrated industrial feed. This does not by itself establish membrane damage. Measure or estimate $C_w$ and compare true rejection, because concentration polarisation can change the bulk-based ratio. Changes in material properties, adsorption or defects are other possible causes and require separate checks.

## Link to other topics

The series-resistance construction mirrors overall heat-transfer coefficients and two-film absorption models. Recovery balances will also distinguish a locally enriched gas flux from the composition of all permeate collected upstream.

## Conclusion

Flux, rejection and recovery describe different aspects of performance. Use the concentration or pressure at the actual transporting interface in a flux law, and ensure all resistance coefficients share the same driving-force basis.

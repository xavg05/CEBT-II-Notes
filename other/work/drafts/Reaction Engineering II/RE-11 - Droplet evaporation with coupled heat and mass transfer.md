# RE-11: Droplet evaporation with coupled heat and mass transfer

## Overview

Assumed: film-controlled shrinking particles, vapour–liquid equilibrium and the Clausius–Clapeyron equation.

An evaporating droplet is a shrinking particle under film control, with the concentration gradient reversed: vapour moves away from the surface. Evaporation needs latent heat, so it behaves like an endothermic reaction. The droplet surface cools until heat arriving from the gas balances the heat consumed, and the lower surface temperature lowers the vapour pressure that drives evaporation. The droplet therefore evaporates more slowly than a calculation at gas temperature predicts. Its surface temperature does not depend on its size, so once it is found the shrinkage follows the film-controlled result.

## Intuition

A wet surface in warm dry air feels cold because evaporation removes heat from it. The surface keeps cooling until the warm gas supplies heat as fast as evaporation removes it. Since vapour pressure falls steeply with temperature, a few degrees of cooling substantially reduce the evaporation rate. This is the same balance that makes a wetted thermometer read lower than a dry one.

Heat and vapour travel across the same boundary layer around the droplet, so they are governed by the same geometry. That shared film is why the droplet size cancels from the energy balance.

## Derivation

Consider a spherical droplet of pure liquid A, of radius $r$, in a gas at bulk temperature $T_0$, with surface temperature $T$. Let $\rho_m$ be the liquid molar density, $k_g$ the film mass-transfer coefficient, $D$ the diffusivity of A vapour in the gas, $h$ the heat-transfer coefficient to the droplet, $\lambda$ the thermal conductivity of the gas and $\Delta H^{\mathrm{vap}}$ the molar enthalpy of vaporisation. To avoid confusion with radius, write the gas constant as $\mathcal R$.

**Step 1: write the vapour flux.** Using the film model with the gradient pointing outward, the molar evaporation rate is $4\pi r^2k_g(C_{\mathrm{A,surface}}-C_{\mathrm{A,bulk}})$.

**Step 2: fix the concentrations.** In dry gas $C_{\mathrm{A,bulk}}=0$. With vapour–liquid equilibrium at the surface and ideal vapour, $C_{\mathrm{A,surface}}=P^{\mathrm{sat}}(T)/(\mathcal RT)$.

*Reason:* evaporation at the interface is much faster than diffusion away from it, so the interface reaches equilibrium, just as a fast surface reaction drove the surface concentration to zero in the film-controlled shrinking particle.

**Step 3: balance the liquid.** Setting the loss of $\tfrac43\pi r^3\rho_m$ equal to the evaporation rate and cancelling the area as before,

$$
\frac{dr}{dt}=-\frac{k_gP^{\mathrm{sat}}(T)}{\mathcal RT\rho_m}.
\tag{34}
$$

**Step 4: balance the heat.** At quasi-steady state the heat arriving through the gas film supplies the latent heat:

$$
4\pi r^2k_g\frac{P^{\mathrm{sat}}(T)}{\mathcal RT}\Delta H^{\mathrm{vap}}=4\pi r^2h(T_0-T).
$$

*Reason:* the droplet's own sensible heat changes little once its temperature has settled, so all incoming heat goes into vaporisation.

**Step 5: relate the two coefficients.** The Sherwood and Nusselt numbers are $\mathrm{Sh}=k_gd/D$ and $\mathrm{Nu}=hd/\lambda$ for diameter $d$. For a gas, $\mathrm{Sh}\approx\mathrm{Nu}$. Then $k_g/h=D/\lambda$, and dividing the heat balance by $h$ and multiplying by $\lambda$ gives

$$
D\frac{P^{\mathrm{sat}}(T)}{\mathcal RT}\Delta H^{\mathrm{vap}}=\lambda(T_0-T).
\tag{35}
$$

*Reason:* $\mathrm{Sh}=\mathrm{Nu}=2$ holds exactly in a stagnant gas. With convection, correlations of the form $2+0.6\mathrm{Re}^{1/2}\mathrm{Sc}^{1/3}$ and $2+0.6\mathrm{Re}^{1/2}\mathrm{Pr}^{1/3}$ differ only by the ratio of $\mathrm{Sc}^{1/3}$ to $\mathrm{Pr}^{1/3}$; for water vapour in air, with $\mathrm{Sc}\approx0.60$ and $\mathrm{Pr}\approx0.71$, that ratio is about 0.95. The approximation follows from the similarity of heat and mass transport in gases, where $\mathrm{Pr}$ and $\mathrm{Sc}$ are close.

**Step 6: close the vapour pressure.** Assuming constant $\Delta H^{\mathrm{vap}}$,

$$
\ln\frac{P^{\mathrm{sat}}(T)}{P^{\mathrm{sat}}(T_0)}=\frac{\Delta H^{\mathrm{vap}}}{\mathcal R}\left(\frac1{T_0}-\frac1T\right).
\tag{36}
$$

Equations (35) and (36) together give one equation for $T$, solved numerically.

## Motivation and explanation

Equation (35) contains no radius. Both $k_g$ and $h$ scale with $1/d$ in the same way, so a smaller droplet receives more heat per area and loses more vapour per area in the same proportion. The surface temperature therefore stays fixed as the droplet shrinks, $P^{\mathrm{sat}}(T)$ is constant, and (34) is the film-controlled shrinking particle with a constant surface concentration. In a stagnant gas $k_g=D/r$, so $r^2$ falls linearly with time and the lifetime scales as $R^2$.

The size of the effect is large. For a water droplet in dry gas at $T_0=323.15$ K, taking $D\approx2.6\times10^{-5}\ \mathrm{m^2\,s^{-1}}$, $\lambda\approx0.026\ \mathrm{W\,m^{-1}\,K^{-1}}$, $\Delta H^{\mathrm{vap}}\approx44\ \mathrm{kJ\,mol^{-1}}$ and $P^{\mathrm{sat}}(298.15\ \mathrm K)\approx3.17$ kPa, solving (35) and (36) gives $T\approx289$ K, about 16 °C. The vapour concentration at the surface is then only about 0.17 of its value at gas temperature, so the droplet evaporates roughly six times more slowly than the uniform-temperature estimate. This is an estimate within the model, with constant properties and dilute vapour; it is not a measured wet-bulb temperature, which also depends on the convective heat- and mass-transfer ratio and on radiation.

The droplet shows the general consequence of an endothermic step limited by external transport: the surface cools and the driving force falls. An exothermic fluid–solid reaction does the reverse. The particle heats above the gas, its rate constant rises, and it can ignite, which is why the energy balance cannot be dropped for combustion.

The model fails if the vapour is not dilute: near the boiling point the outward vapour flow carries heat and gas with it (Stefan flow) and the simple film flux underestimates evaporation. Humid gas gives $C_{\mathrm{A,bulk}}\neq0$. Radiation from hot surroundings, temperature gradients inside large droplets, and multicomponent liquids whose surface composition changes also break the assumptions.

## Link to other topics

The vapour pressure–temperature coupling uses the same equilibrium thermodynamics as other vapour–liquid problems. The cancellation between heat and mass transfer coefficients reappears whenever a catalyst pellet's external film must carry both reagent and reaction heat.

## Conclusion

Evaporation self-cools the droplet to a size-independent temperature set by the balance of latent heat and convective supply. The final topic of this section is the equipment that holds solid reagents for the time they need to react.

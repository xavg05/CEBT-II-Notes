[Previous](<ET-22 - Osmotic equilibrium.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-24 - Bubbles, superheating and boiling.md>)

<!-- note-content:start -->
# Section 23: Droplets and the Kelvin equation

*Notation:* $\sigma$ is the surface tension (N m⁻¹), $r$ the droplet radius, $P^{L}$ the pressure inside the droplet, $P^{V}$ the surrounding vapour pressure, and $P^{\mathrm{SAT}}(T)$ the vapour pressure over a flat surface. Pure substance throughout.

## Intuition

Surface tension acts like a stretched skin around the droplet, pressing inwards. The smaller the droplet, the more sharply curved the skin and the harder it presses. Liquid inside is therefore compressed, and compressed liquid has a higher escaping tendency (Section 06). So a small droplet evaporates into vapour that would be exactly saturated over a flat surface.

Equilibrium with a droplet of radius $r$ needs a *supersaturated* vapour, and the equilibrium is unstable:
- a droplet slightly smaller than that $r$ has an even higher vapour pressure, so it evaporates further;
- a droplet slightly larger grows.

## Derivation

**Step 1: the phase-rule count.** One component, two phases: naively $F = 1$, one boiling point per pressure. But $P^{L}\neq P^{V}$ across a curved interface, which removes one constraint. So $F = 2$: for example the pressure *and* the droplet radius.

**Step 2: mechanical equilibrium (Young–Laplace).** Cut the droplet through its centre. The pressure excess acting on the cross-section, $(P^{L} - P^{V})\pi r^2$, is balanced by surface tension acting round the rim, $2\pi r\sigma$:

$$P^{L} - P^{V} = \frac{2\sigma}{r} \tag{117}$$

**Step 3: chemical potentials.** Reference both phases to the flat-interface saturation state, where $\underline{G}^{L} = \underline{G}^{V} = \underline{G}^{\mathrm{SAT}}(T)$ at $P^{\mathrm{SAT}}$.
- Incompressible liquid: $\mu^{L} = \underline{G}^{\mathrm{SAT}} + \underline{V}^{L}(P^{L} - P^{\mathrm{SAT}})$.
- Ideal-gas vapour: $\mu^{V} = \underline{G}^{\mathrm{SAT}} + RT\ln(P^{V}/P^{\mathrm{SAT}})$.

**Step 4: equate.** $\mu^{L} = \mu^{V}$ gives the same equation as the Poynting correction,

$$\underline{V}^{L}(P^{L} - P^{\mathrm{SAT}}) = RT\ln\frac{P^{V}}{P^{\mathrm{SAT}}}$$

but now $P^{L}$ is set by (117): $P^{L} = P^{V} + 2\sigma/r$.

**Step 5: the Kelvin equation.** Substitute:

$$\underline{V}^{L}\left(\frac{2\sigma}{r} + P^{V} - P^{\mathrm{SAT}}\right) = RT\ln\frac{P^{V}}{P^{\mathrm{SAT}}} \tag{118}$$

For droplets larger than a few nanometres, $P^{V} - P^{\mathrm{SAT}}$ is negligible compared with $2\sigma/r$, so

$$\ln\frac{P^{V}}{P^{\mathrm{SAT}}} \approx \frac{2\sigma\underline{V}^{L}}{rRT} \tag{119}$$

**Graphical form.** On the isotherm, the flat-interface case is Maxwell's equal-area construction at $P^{\mathrm{SAT}}$. For a droplet, the liquid branch is pushed up to $P^{L}$. The extra liquid-side area must be balanced by raising the vapour line slightly, to $P^{V} > P^{\mathrm{SAT}}$.

![Isotherm: flat interface (purple, Maxwell equal areas at P^SAT) versus droplet (green): compressing the liquid to P^L raises the equilibrium vapour pressure to P^V](../figs/ET-23-droplet-isotherm.png)

## Motivation and explanation

**The size scale of curvature.** For water at 293.15 K with $\sigma=0.0727\ \mathrm{N\,m^{-1}}$ and $\underline V^L=1.805\times10^{-5}\ \mathrm{m^3\,mol^{-1}}$, the Kelvin length $2\sigma\underline V^L/(RT)$ is about 1.077 nm. A 100 nm radius therefore needs a vapour-pressure ratio of about 1.011; a 10 nm radius needs about 1.114. At a supersaturation ratio of 1.01 the critical radius is approximately 108 nm. Small supersaturation cannot support arbitrarily tiny droplets: smaller clusters have the greater escaping tendency and evaporate. Aerosols provide a route to droplet growth, although real nuclei also involve wetting and solute effects. Extrapolation to molecular radii would require checking the continuum interface and bulk surface-tension assumptions.

**Same physics as Poynting.** In Section 06 the extra pressure on the liquid came from an inert gas. Here it comes from curvature. Either way, compressing the liquid by $\Delta P$ multiplies its fugacity by $\exp(\underline{V}^{L}\Delta P/RT)$.

The large pressure in the droplet is not the vapour pressure surrounding it. It acts on a dense liquid, whose chemical potential responds through its small molar volume. The gas matches that energy change through a logarithmic change of its much smaller pressure. This explains how the table can contain a large Laplace pressure alongside only a modest relative vapour-pressure enhancement.

The critical-radius argument holds the surrounding temperature and supersaturation fixed, as if the droplet exchanges molecules with a large vapour reservoir. A slightly smaller droplet then needs a higher vapour pressure than that reservoir provides and shrinks further. In a closed vessel with appreciable condensation, the vapour inventory and supersaturation also change, so that feedback must be included before inferring the fate of the whole droplet population.

**Unstable equilibrium and nucleation.** In vapour at a given supersaturation $S = P^{V}/P^{\mathrm{SAT}}$, (119) defines a critical radius $r^{*} = 2\sigma\underline{V}^{L}/(RT\ln S)$. Smaller droplets evaporate; larger ones grow. Forming a droplet from scratch means passing through tiny, highly unstable sizes. So pure vapour can stay supersaturated (metastable) for a long time. Real clouds form on dust, salt or ions, which provide surfaces large enough to skip that stage. The same effect makes small crystals more soluble than large ones, which drives Ostwald ripening in crystallisers.

**Limits.**
- At radii of a few nanometres, a droplet contains only hundreds of molecules, and a bulk surface tension is no longer meaningful.
- The ideal-gas vapour assumption fails near the critical point.
- Solutes on the droplet (e.g. dissolved salt in cloud droplets) lower its vapour pressure (Raoult) and compete with the Kelvin effect.

## Link to other topics

The same equation controls capillary condensation in porous adsorbents (concave menisci *lower* the vapour pressure), cavitation, and crystal size distributions in crystallisers. Section 24 applies the same mechanical-plus-chemical equilibrium to bubbles, where the curvature is reversed.

## Summary

Surface tension raises the pressure inside a droplet by $2\sigma/r$. By the Poynting argument, this raises its equilibrium vapour pressure, giving the Kelvin equation $\ln(P^{V}/P^{\mathrm{SAT}}) = 2\sigma\underline{V}^{L}/(rRT)$. The effect is negligible above a micrometre but dominant at nanometres. This makes droplet nucleation hard and supersaturated vapours metastable.
<!-- note-content:end -->

[Previous](<ET-22 - Osmotic equilibrium.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-24 - Bubbles, superheating and boiling.md>)

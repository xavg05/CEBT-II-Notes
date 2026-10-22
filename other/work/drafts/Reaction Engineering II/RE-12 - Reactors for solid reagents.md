# RE-12: Reactors for solid reagents

## Overview

Assumed: single-particle conversion–time results and residence-time distributions.

A reactor for a solid reagent must hold each particle in contact with fluid for at least its complete-reaction time $\tau_c$ while supplying reagent and removing or adding heat. Equipment is therefore chosen mainly by the solid residence time it can provide and by how uniformly it treats particles. Because particles never exchange solid with each other, the average conversion is the conversion–time curve averaged over the solid residence-time distribution. Plug flow of solids can reach complete conversion in time $\tau_c$; well-mixed solids need a mean residence time some tens of times longer for 99% conversion.

## Intuition

Each particle is a sealed batch reactor carried through the vessel. A particle that leaves early takes its unreacted core with it, and nothing in the outlet can compensate. A particle that stays longer than $\tau_c$ is fully converted, but cannot become more than fully converted. A broad residence-time distribution therefore wastes the extra time of long-stayers while still losing the short-stayers.

## Equipment

![Falling-particle reactor with countercurrent gas](../figs/RE-12-falling-particle-reactor.png)

**Falling-particle reactor (short residence times).** Solid enters at the top and falls through rising gas; the shading shows conversion increasing on the way down. Residence time is set by the fall, so it suits fast reactions of small particles. In practice the solid is often pulverised and carried in pneumatically rather than fed by gravity.

![Moving-belt reactor with gas flowing up through the layer](../figs/RE-12-moving-belt-reactor.png)

**Moving-belt reactor (medium residence times).** Solids travel along a conveyor while gas passes up through the layer. Every particle spends close to the same time on the belt, so the solids approximate plug flow, and the belt speed sets the residence time.

![Inclined rotary kiln with countercurrent gas](../figs/RE-12-rotary-kiln.png)

**Rotary kiln (long residence times).** A long, slightly inclined cylinder rotates slowly; the rotation tumbles the bed and the inclination moves it towards the lower end. Gas usually flows countercurrent to the solid. Rotation speed and slope set the residence time. Cement, lime and the roasting of sulfide ores are typical uses.

![Continuous fluidised bed with solid feed and withdrawal](../figs/RE-12-fluidised-bed.png)

**Fluidised bed (continuous).** Gas suspends the particles, so the bed mixes vigorously and has nearly uniform temperature, which helps with strongly exothermic or endothermic reactions. The price is a broad, close to exponential, solid residence-time distribution, together with attrition and particle carry-over.

![Fixed bed of solid particles operated semi-batch](../figs/RE-12-fixed-bed.png)

**Fixed bed, semi-batch.** The solid charge stays in place while fluid flows through until the solid is used up, as in regenerating a coked catalyst bed. The fluid is depleted along the bed, so particles near the inlet react first, and a reaction zone moves through the bed with time.

## Derivation

Let $X(t)$ be the conversion of a particle after time $t$ in the reactor, from the single-particle results, and $E(t)$ the residence-time distribution of the solid. Assume all particles have the same size and see the same fluid composition and temperature.

**Step 1: average over exit ages.** The fraction of particles leaving with ages between $t$ and $t+dt$ is $E(t)\,dt$, and each carries unconverted fraction $1-X(t)$. Summing,

$$
1-\bar X=\int_0^{\tau_c}\left[1-X(t)\right]E(t)\,dt.
\tag{37}
$$

*Reason:* particles are completely segregated, so the mixing question that arose for fluids does not: averaging single-particle results is exact. The upper limit is $\tau_c$ because particles older than $\tau_c$ contribute nothing unconverted.

**Step 2: plug flow of solids.** If every particle stays exactly $\bar t$, then $E(t)=\delta(t-\bar t)$ and $\bar X=X(\bar t)$, with complete conversion for $\bar t\ge\tau_c$.

**Step 3: well-mixed solids.** For a fluidised bed approximated by $E(t)=e^{-t/\bar t}/\bar t$, substitute the appropriate $X(t)$ into (37). When $\bar t\gg\tau_c$, the exponential is nearly 1 over $0<t<\tau_c$, giving $1-\bar X\approx(\tau_c/\bar t)\int_0^1[1-X(s)]\,ds$, with $s=t/\tau_c$. Evaluating the integral gives coefficients $\tfrac12$ for shrinking-core film control, $\tfrac14$ for reaction control and $\tfrac15$ for product-layer diffusion control.

## Motivation and explanation

The consequence for design is large. Solving (37) for 99% conversion with well-mixed solids needs a mean residence time of about $50\tau_c$ under shrinking-core film control, $25\tau_c$ under reaction control and $20\tau_c$ under product-layer control. Plug flow of the same particles needs at most $\tau_c$: $0.99\tau_c$, $0.79\tau_c$ and $0.88\tau_c$ respectively. The difference comes from the early-leaving particles in the mixed bed, exactly the fraction that the exponential distribution makes impossible to eliminate. A fluidised bed is chosen despite this when its temperature uniformity and handling matter more, or several beds are placed in series to narrow the distribution.

The controlling regime also matters for the averaged result: product-layer control has the smallest coefficient because conversion rises most steeply early, so short-stayers are already substantially reacted when they leave.

Equation (37) assumes uniform fluid composition and temperature. In a countercurrent kiln or a falling-particle reactor the gas composition changes along the vessel, so $C_{\mathrm{B,bulk}}$ and therefore $\tau_c$ vary along the particle path and must be coupled to a gas-phase balance. A distribution of particle sizes needs a second average, because $\tau_c$ depends on $R$. Heat release can create hot zones in fixed and moving beds that the isothermal single-particle models do not capture.

## Link to other topics

Equation (37) is the segregated-flow average used for fluid residence-time distributions, applied to solids where segregation is physically exact. The same equipment types, used with a catalyst instead of a solid reagent, reappear as catalytic reactors.

## Conclusion

A solid-reagent reactor must give every particle at least $\tau_c$; narrow solid residence-time distributions achieve this with much less holdup. With the reactions of solid reagents complete, the next section turns to solids that act as catalysts and are not consumed.

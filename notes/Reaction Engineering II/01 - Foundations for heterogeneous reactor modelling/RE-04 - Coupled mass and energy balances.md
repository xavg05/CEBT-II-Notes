[Previous](<RE-03 - Conversion and changing gas volume.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<RE-05 - Residence-time distributions and tanks in series.md>)

<!-- note-content:start -->
# RE-04: Coupled mass and energy balances

## Overview

Assumed: the first law for a flowing system and ideal reactor species balances.

Model a steady PFR with negligible kinetic/potential energy changes and no shaft work. Assume a single reaction and a mixture whose molar enthalpies depend on temperature alone. The energy balance determines temperature alongside species flows. Do not impose isothermal kinetics unless heat removal can sustain that condition.

## Intuition

An exothermic reaction transfers chemical enthalpy into sensible enthalpy. Temperature rises unless that heat is removed. A higher temperature usually increases the rate constant, so reaction and temperature reinforce one another. Meanwhile, heating a gas reduces its concentration at fixed pressure; for reversible exothermic chemistry, heating can also reduce equilibrium conversion.

## Derivation

Let $`F_i`$ be species molar flow, $`h_i(T)`$ molar enthalpy including formation enthalpy, and $`C_{Pi}=dh_i/dT`$ molar heat capacity. Let $`r`$ be the extent rate per reactor volume, $`\nu_i`$ signed stoichiometric coefficients, and $`\Delta_rH=\sum_i\nu_i h_i`$ the enthalpy change per mole of reaction as written. All rates and enthalpies must use that same stoichiometric normalisation.

**Step 1: balance enthalpy over a slice.** Define $`q_V=d\dot q/dV`$, the heat supplied from outside per reactor volume (W m$`^{-3}`$), positive into the reacting fluid. Steady energy conservation gives


```math
\frac{d}{dV}\left(\sum_iF_i h_i\right)=q_V.
```


*Reason:* flow work is already included in enthalpy. Chemical energy is already included in $`h_i`$; adding a separate reaction-heat term at this stage would count it twice.

**Step 2: expand the derivative.** Apply the product rule to the changing flows and temperatures:


```math
\sum_i h_i\frac{dF_i}{dV}
+\left(\sum_iF_iC_{Pi}\right)\frac{dT}{dV}=q_V.
```


*Reason:* enthalpy flux changes both when species are transformed and when the flowing mixture heats up.

**Step 3: substitute the species balances.** Since $`dF_i/dV=r_i=\nu_i r`$, the first sum is $`r\Delta_rH`$. Rearrangement gives the coupled equations


**Equation (10)**

```math
\frac{dF_i}{dV}=\nu_i r,\qquad
\frac{dT}{dV}=\frac{q_V-r\Delta_rH}{\sum_iF_iC_{Pi}}.
```


*Reason:* reaction changes chemical enthalpy at rate $`r\Delta_rH`$; the remainder changes sensible enthalpy. For several reactions, replace $`r\Delta_rH`$ by $`\sum_j r_j\Delta_rH_j`$. The numerator has units W m$`^{-3}`$ and denominator W K$`^{-1}`$, so $`dT/dV`$ has units K m$`^{-3}`$.

**Step 4: specify wall heat exchange.** With overall heat-transfer coefficient $`U`$ (W m$`^{-2}`$ K$`^{-1}`$), heat-transfer area per reactor volume $`a`$ (m$`^{-1}`$), and heat-exchange fluid temperature $`T_{\mathrm{hx}}`$,


**Equation (11)**

```math
q_V=Ua(T_{\mathrm{hx}}-T).
```


*Reason:* local heat flow is coefficient times area times temperature difference. An adiabatic reactor has $`q_V=0`$. If the heat-exchange fluid changes temperature appreciably, solve its own energy balance too rather than treating $`T_{\mathrm{hx}}`$ as fixed.

## Motivation and explanation

The denominator $`\sum_iF_iC_{Pi}`$ describes how much sensible enthalpy the flowing stream carries per degree of temperature rise. It is a heat-capacity flow, rather than the stored thermal capacity of the vessel. More of it reduces the temperature change per reactor volume for a specified local net heat input; this steady spatial balance does not supply a transient heating time.

Dividing the adiabatic energy balance by the conversion balance cancels the rate because every mole converted releases the same specified reaction enthalpy. Thus the temperature–conversion path can be known before the rate or reactor length is known. A faster catalyst moves the stream along that path in less volume; it does not change the path under the constant-property adiabatic assumptions. With wall heat exchange, eliminating volume generally leaves a heat-transfer contribution divided by reaction rate, so a universal rate-independent temperature–conversion path no longer follows.

For a forward exothermic reaction, $`r>0`$ and $`\Delta_rH<0`$, so $`-r\Delta_rH>0`$: the adiabatic temperature gradient is positive. An inert increases heat-capacity flow $`\sum_iF_iC_{Pi}`$ and therefore buffers temperature rise.

In a gas reactor, solve (10) together with the concentration closure and, if needed, a pressure-drop equation. A PFR's temperature is uniform radially under this model, but may vary axially. A CSTR instead has one uniform temperature found from its overall energy balance. Coupling its material and energy balances can produce several steady solutions; finding a steady solution does not establish its dynamic stability.

Equation (10) needs extension when pressure-dependent enthalpy, phase changes, shaft work, axial heat conduction or separate solid/fluid temperatures matter. In particular, bulk-fluid temperature need not equal catalyst-pellet temperature.

## Link to other topics

The same energy balance underlies temperature control and thermal multiplicity. Later, separate heat balances inside and around a catalyst pellet explain why its reaction rate can differ from one evaluated at bulk-fluid temperature.

## Conclusion

Temperature is a state variable determined by conservation, not an optional correction to a fixed rate constant. Even with the correct balances, real flow may require a residence-time model.
<!-- note-content:end -->

[Previous](<RE-03 - Conversion and changing gas volume.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<RE-05 - Residence-time distributions and tanks in series.md>)

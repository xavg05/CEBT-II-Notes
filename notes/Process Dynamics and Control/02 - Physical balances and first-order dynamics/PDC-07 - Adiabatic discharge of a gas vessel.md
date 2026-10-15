[Previous](<PDC-06 - Thermocouple and heated-liquid dynamics.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<../03 - Transfer functions and elementary responses/PDC-08 - Deviation variables and transfer-function assumptions.md>)

<!-- note-content:start -->
# PDC-07: Adiabatic discharge of a gas vessel

## Overview

Assumed: ideal-gas properties and the open-system first law.

An insulated gas vessel cools as it discharges. The energy carried away is stream enthalpy, while the energy stored is internal energy; their difference is essential to predicting temperature and pressure.

## Intuition

Insulation prevents heat exchange through the wall. It does not prevent energy loss through the outlet. The departing gas carries its internal energy plus flow work, so the remaining gas cools.

## Derivation

**Step 1: balance mass and energy.** Let vessel volume $`V`$ be fixed, stored gas mass $`m`$, outlet mass flow $`w>0`$, uniform temperature $`T`$ and pressure $`p`$. Assume well-mixed ideal gas with constant specific heats $`c_v,c_p`$, no inflow, wall heat storage, heat transfer or shaft work, and negligible outlet kinetic/potential energy. With $`U=mc_vT`$ and outlet specific enthalpy $`\hat H=c_pT`$,


**Equation (20)**

```math
\dot m=-w,\qquad
\frac{d(mc_vT)}{dt}=-wc_pT.
```


*Reason:* a fixed control volume stores internal energy but stream enthalpy includes flow work at its boundary.

**Step 2: eliminate time.** Divide the energy balance by $`c_v`$ and use $`\gamma=c_p/c_v`$ and $`\dot m=-w`$:


**Equation (21)**

```math
\frac{d(mT)}{dm}=\gamma T
\quad\Rightarrow\quad T+m\frac{dT}{dm}=\gamma T
\quad\Rightarrow\quad \frac{dT}{T}=(\gamma-1)\frac{dm}{m}.
```


*Reason:* the same mass loss drives both equations, so their ratio removes the unknown discharge-flow law. Integrate from initial $`(m_0,T_0)`$:


**Equation (22)**

```math
\frac{T}{T_0}=\left(\frac{m}{m_0}\right)^{\gamma-1}.
```


**Step 3: obtain pressure.** With mass-specific gas constant $`R=c_p-c_v`$, $`pV=mRT`$. Divide by its initial value:


**Equation (23)**

```math
\frac{p}{p_0}=\left(\frac{m}{m_0}\right)^\gamma,
\qquad \frac{T}{T_0}=\left(\frac{p}{p_0}\right)^{(\gamma-1)/\gamma}.
```


*Reason:* fixed volume makes pressure proportional to $`mT`$. The result relates states along discharge, not yet to time.

**Step 4: check energy reference invariance.** Let specific internal energy instead be $`\hat U=c_vT+C`$, where $`C`$ is a constant offset. Consistency requires $`\hat H=\hat U+p/\rho=c_pT+C`$. Then


```math
c_v\frac{d(mT)}{dt}+C\dot m=-w(c_pT+C).
```


*Reason:* substitute $`\dot m=-w`$ and the two $`-wC`$ terms cancel. A changed reference cannot change the temperature prediction. Choosing unrelated enthalpy and internal-energy offsets breaks $`\hat H-\hat U=RT`$.

The product rule exposes the cooling mechanism directly. Expanding the stored energy and using $`\dot m=-w`$ gives $`mc_v\dot T=-w(c_p-c_v)T=-wRT`$. Removing mass at unchanged temperature would remove only its internal energy; the outlet enthalpy removes more. That excess is supplied by cooling the remaining gas. Since $`w>0`$ and $`T>0`$, the predicted temperature derivative is negative.

The outlet law cancels when finding temperature versus remaining mass, so different discharge rates follow the same state relation under these assumptions. They traverse it at different speeds. Although the pressure–temperature exponent resembles a reversible adiabatic closed-system relation, this derivation describes an open vessel losing mass and does not establish that the discharge is reversible.

## Motivation and explanation

All temperatures in the ideal-gas and power-law relations are absolute. The relations do not provide $`m(t)`$ without an outlet-flow model. Constant prescribed $`w`$ gives $`m=m_0-wt`$ only while gas remains and the prescription is physically sustainable.

The lumped vessel model can fail during rapid discharge with spatial gradients or appreciable wall heat transfer. A nozzle's downstream static temperature need not equal vessel temperature; the outlet enthalpy/kinetic-energy accounting must match the chosen boundary.

## Worked example

For $`T_0=300`$ K and $`\gamma=1.40`$, discharging until $`m/m_0=0.500`$ gives $`T=227.357`$ K and $`p/p_0=0.378929`$. Pressure falls faster than mass because the remaining gas also cools.

Replacing outlet enthalpy by $`c_vT`$ would predict constant vessel temperature under this model, which omits the outlet flow-work contribution.

## Link to other topics

The boiler model also distinguishes stored internal energy from stream enthalpy. Thermodynamic reference conventions must remain consistent whenever changing mass multiplies an energy datum.

## Conclusion

Insulated open-system discharge is not isothermal. A consistent mass–energy balance gives cooling and pressure decline before any particular discharge-valve law is chosen.
<!-- note-content:end -->

[Previous](<PDC-06 - Thermocouple and heated-liquid dynamics.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<../03 - Transfer functions and elementary responses/PDC-08 - Deviation variables and transfer-function assumptions.md>)

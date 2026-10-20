[Previous](<SEP-02 - Absorption-column equipment.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-04 - Operating lines and pinch limits.md>)

<!-- note-content:start -->
# SEP-03: Gas–liquid equilibrium conventions

## Overview

Assumed background: Henry's law and the ideal-gas equation. Gas–liquid partitioning can be expressed using concentrations, mole fractions or partial pressure. The corresponding Henry constants have different values and sometimes different dimensions; they must be converted before combining equilibrium and transfer equations.

## Intuition

A mole fraction describes the fraction of molecules that are solute. A concentration describes how many solute molecules occupy a volume. Liquids contain far more molecules per unit volume than gases, so equal mole fractions do not imply equal concentrations. This is why two dimensionless partition constants can still be very different.

## Derivation

Let $C_g$ and $C_l$ be equilibrium solute concentrations in gas and liquid, in $\mathrm{kmol\,m^{-3}}$. In the dilute linear range define the concentration-based constant $H_c$ by

$$
C_g=H_cC_l. \tag{1}
$$

Its value is dimensionless because both concentrations use the same units. Let $\rho_{mg}$ and $\rho_{ml}$ denote total molar densities of gas and liquid, also in $\mathrm{kmol\,m^{-3}}$. By the definition of mole fraction,

$$
y=\frac{C_g}{\rho_{mg}},\qquad x=\frac{C_l}{\rho_{ml}}. \tag{2}
$$

Substitute these expressions into equation (1), because we want the equilibrium relation on a mole-fraction diagram:

$$
\rho_{mg}y=H_c\rho_{ml}x,
\qquad y=H_mx,
\qquad H_m=H_c\frac{\rho_{ml}}{\rho_{mg}}. \tag{3}
$$

Here $H_m$, also commonly called $K$, is the dimensionless equilibrium-line slope. Rearranging gives

$$
H_c=\frac{\rho_{mg}}{\rho_{ml}}H_m. \tag{4}
$$

For an ideal gas at total pressure $P_T$ and temperature $T$,

$$
\rho_{mg}=\frac{P_T}{RT},\qquad p=yP_T, \tag{5}
$$

where $p$ is solute partial pressure and $R$ is the gas constant in units consistent with kmol. For a liquid of mass density $\rho_l$ and mean molar mass $\overline M_l$, $\rho_{ml}=\rho_l/\overline M_l$.

Two pressure-based conventions are $p=H'C_l$ and $p=H''x$. Inserting equation (5) into equation (1), or into equation (3), gives

$$
H'=RT H_c,\qquad H''=P_TH_m=RT\rho_{ml}H_c. \tag{6}
$$

Thus $H'$ has units of pressure times volume per amount, for example $\mathrm{Pa\,m^3\,kmol^{-1}}$, and $H''$ has units of pressure. Their dimensions follow from their definitions; a symbol named “Henry constant” does not identify the convention by itself.

The density factors are a change of coordinates, not an extra equilibrium effect. At unchanged physical equilibrium, multiply each mole fraction by its phase's total molar density to recover the two concentrations. Substitution then guarantees that all four Henry conventions predict the same pair of physical states. Checking that pair is more informative than comparing the numerical constants in isolation.

At fixed temperature in the ideal dilute model, a pressure-based relation can remain unchanged while its mole-fraction slope changes with total pressure. The reason is that the same solute partial pressure becomes a smaller fraction of a higher total pressure. State the composition basis before interpreting a pressure effect as changed molecular affinity.

## Motivation and explanation

With $C_g=H_cC_l$, small $H_c$ means a gas dissolves strongly: a small gas concentration supports a relatively large liquid concentration. Small $H_m$ similarly means strong uptake at fixed mole fraction. The constants depend on temperature, solvent and, for reactive solutes, speciation conditions.

The linear relationship applies over a dilute range. A full equilibrium curve $y^*=f(x)$ should replace $H_mx$ when measured data are curved. A star denotes a hypothetical equilibrium counterpart: $y^*$ is the gas mole fraction that would equilibrate with the actual bulk liquid $x$. It does not assert that the actual gas $y$ is in equilibrium with it.

At fixed temperature, increasing pressure increases gas molar density and decreases $H_m=H''/P_T$ when the pressure-based Henry model applies. This favours absorption on a mole-fraction basis. Strong non-ideal gas behaviour requires fugacity rather than ideal partial pressure.

## Link to other topics

The same Henry convention must be used when converting individual resistances into an overall mass-transfer coefficient. Equilibrium thermodynamics supplies the validity limits of the partitioning model; column balances determine where on that model the fluids operate.

## Conclusion

Write the defining equilibrium equation beside a Henry constant. Convert through total molar densities and check dimensions before using it to calculate driving forces.
<!-- note-content:end -->

[Previous](<SEP-02 - Absorption-column equipment.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-04 - Operating lines and pinch limits.md>)

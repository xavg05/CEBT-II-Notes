[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-07 - Fugacity, definition and meaning.md>)

<!-- note-content:start -->
# Section 06: The Poynting correction (vapour pressure under an inert gas)

*Notation:* an underline denotes a molar property of a pure substance (e.g. $\underline{V}^{l}$, the molar volume of the pure liquid); superscripts $l$ and $v$ label the liquid and vapour phases.

## Intuition

Pressing on a liquid does work on it. Each mole of liquid that is squeezed from $P^{\mathrm{SAT}}$ up to $P$ gains Gibbs energy $\int \underline{V}^{l}\,dP$. A higher Gibbs energy means a greater tendency to escape into another phase. So the liquid "pushes" more molecules into the gas, and the gas must hold slightly more water vapour before the two phases balance again.

*The inert gas works like a piston that the vapour can pass through.* It presses on the liquid surface and raises the liquid's pressure, but it does not stop water molecules leaving. The analogy breaks down in two ways. A real gas also interacts with the water molecules in the vapour, and it can dissolve in the liquid. Both effects are ignored below and discussed at the end.

## Derivation

**System.** Pure liquid water at total pressure $P$ (e.g. 1 atm), in contact with a gas phase made of air plus water vapour. $P^{\mathrm{VAP}}$ denotes the partial pressure of water in that gas, which is the vapour pressure we want.

**Assumptions.**
1. Constant $T$ throughout (thermal equilibrium).
2. The air is insoluble in the liquid, so the liquid stays pure water.
3. The air does not change the liquid's equation of state. The liquid simply feels the total pressure $P$ (mechanical equilibrium at a flat interface).
4. The gas phase is an ideal-gas mixture, which is reasonable because $P^{\mathrm{VAP}}$ is small.
5. The liquid is incompressible: $\underline{V}^{l}$ is constant.

**Step 1: reference state.** With no air present, liquid and vapour coexist at $P^{\mathrm{SAT}}(T)$:

$$\underline{G}^{l}(T,P^{\mathrm{SAT}}) = \underline{G}^{v}(T,P^{\mathrm{SAT}}) \tag{28}$$

*Reason:* this is the definition of the saturation pressure. Equation (28) is the anchor that both phases are measured from.

**Step 2: raise the liquid to $P$.** At constant $T$, $d\underline{G}^{l} = \underline{V}^{l}\,dP$. Integrating from $P^{\mathrm{SAT}}$ to $P$ with $\underline{V}^{l}$ constant gives

$$\underline{G}^{l}(T,P) = \underline{G}^{l}(T,P^{\mathrm{SAT}}) + \underline{V}^{l}\,(P-P^{\mathrm{SAT}}) \tag{29}$$

*Reason:* the liquid is pure (assumption 2), so its chemical potential is its molar Gibbs energy, evaluated at the pressure it actually feels (assumption 3).

**Step 3: chemical potential of water in the gas.** In an ideal-gas mixture each component behaves as if it were alone at its own partial pressure. Water's chemical potential therefore depends only on $P^{\mathrm{VAP}}$, not on how much air is present. For a pure ideal gas at constant $T$, $d\underline{G} = (RT/P)\,dP$. Integrating from $P^{\mathrm{SAT}}$ to $P^{\mathrm{VAP}}$ gives

$$\mu^{v}(T,P^{\mathrm{VAP}}) = \underline{G}^{v}(T,P^{\mathrm{SAT}}) + RT\ln\frac{P^{\mathrm{VAP}}}{P^{\mathrm{SAT}}} \tag{30}$$

*Reason:* assumption 4. The vapour at $P^{\mathrm{SAT}}$ is treated as an ideal gas too, so the same reference state as in (28) can be used.

**Step 4: equate chemical potentials.** At equilibrium $\underline{G}^{l}(T,P) = \mu^{v}(T,P^{\mathrm{VAP}})$. Substitute (29) and (30), then cancel the two reference terms using (28):

Imagine adding more insoluble gas while keeping temperature fixed and liquid present. The liquid feels the higher *total* pressure, so its chemical potential rises. In the ideal gas mixture, however, water responds to its own *partial* pressure. Equilibrium requires that partial pressure to rise just enough to match the liquid-side increase. The water mole fraction can nevertheless fall, because the total gas pressure is increasing much more strongly.

Thus a higher equilibrium water partial pressure does not mean a larger fraction of water in the gas. The Poynting factor answers the former question. To obtain the fraction, divide the resulting $P^{\mathrm{VAP}}$ by the specified total pressure.

$$\underline{V}^{l}\,(P-P^{\mathrm{SAT}}) = RT\ln\frac{P^{\mathrm{VAP}}}{P^{\mathrm{SAT}}} \tag{31}$$

**Step 5: solve for the vapour pressure.**

$$\boxed{P^{\mathrm{VAP}} = P^{\mathrm{SAT}}\exp\!\left[\frac{\underline{V}^{l}\,(P-P^{\mathrm{SAT}})}{RT}\right]} \tag{32}$$

The exponential is the **Poynting correction** (or Poynting factor). Without assumption 5 the exponent is $\frac{1}{RT}\int_{P^{\mathrm{SAT}}}^{P}\underline{V}^{l}\,dP$.

**Graphical form.** Both sides of (31) are areas $\int\underline{V}\,dP$ under the same isotherm. With no air, Maxwell's equal-area construction fixes $P^{\mathrm{SAT}}$: the net $\int_{\text{liq}}^{\text{vap}}\underline{V}\,dP = 0$. With air present, the liquid branch is pushed up to $P^{\mathrm{TOTAL}}$. This adds a tall, thin area on the liquid side ("extra area 1", $\underline{V}^{l}\Delta P$), which must be balanced by a short, wide area on the vapour side ("extra area 2", $RT\ln(P^{\mathrm{VAP}}/P^{\mathrm{SAT}})$). The vapour line therefore sits slightly above $P^{\mathrm{SAT}}$.

![Isotherm with and without an inert gas: the extra liquid-side area from compressing the liquid is balanced by a small rise of the vapour line above P^SAT](../figs/ET-06-isotherm-inert-gas.png)

## Motivation and explanation

**When the Poynting factor matters.** Its exponent compares liquid compression work $\underline V^l(P-P^{\mathrm{SAT}})$ with the thermal scale $RT$. For water at 293.15 K, using $\underline V^l=1.805\times10^{-5}\ \mathrm{m^3\,mol^{-1}}$ and $P^{\mathrm{SAT}}=0.02339$ bar, the factors at 1, 10 and 100 atm are approximately 1.0007, 1.0075 and 1.078. Setting the factor equal to 1.01 gives
$$P=P^{\mathrm{SAT}}+\frac{RT\ln(1.01)}{\underline V^l}\approx13.5\ \mathrm{bar}.$$
Thus atmospheric liquid compression has a very small effect, while high-pressure gas humidification can need a substantial correction. These figures isolate the Poynting contribution; at high pressure vapour non-ideality and liquid compressibility also require checking.

**Why the correction is small.** Rewrite the exponent as $(P-P^{\mathrm{SAT}})/(RT/\underline{V}^{l})$. The quantity $RT/\underline{V}^{l}$ is a characteristic pressure: the pressure an ideal gas would have at the liquid's density. For water at 20 °C it is about 1350 bar. The correction is significant only when the applied pressure is a sizeable fraction of this. *Physically:* compressing a dense liquid needs very little work per mole, while changing the vapour's chemical potential by the same amount needs a large relative change in its pressure. The liquid's $\underline{V}\,dP$ is small, so the vapour has to move only a little to match it.

**Limiting cases.**
- $P \to P^{\mathrm{SAT}}$ (no inert gas): the factor tends to 1 and $P^{\mathrm{VAP}} = P^{\mathrm{SAT}}$, as it should.
- Small exponent: $P^{\mathrm{VAP}}/P^{\mathrm{SAT}} \approx 1 + \underline{V}^{l}(P-P^{\mathrm{SAT}})/RT$, which is linear in the applied pressure.
- $\underline{V}^{l}\to 0$ (perfectly dense phase): no correction. The effect exists only because the condensed phase has a finite volume to do work on.

**When it fails.** Equation (32) captures only the effect of pressure on the *liquid*. In a real system two other effects compete:
1. *Vapour–gas interactions.* The water vapour is not an ideal mixture with air. This is corrected by fugacity coefficients: in general the enhancement is $(\phi^{\mathrm{SAT}}/\phi)\exp\!\big[\int\underline{V}^{l}dP/RT\big]$, where $\phi$ is water's fugacity coefficient in the gas. For water in air at 20 °C and about 1 atm, the measured enhancement factor is about 1.004, several times larger than the Poynting factor of 1.0007. At ordinary pressures, gas-phase non-ideality matters more than the Poynting term.
2. *Gas solubility.* If the "inert" gas dissolves (CO₂ in water, for example), the liquid is no longer pure. The water mole fraction falls, which *lowers* its vapour pressure (Raoult-type behaviour). This can cancel or reverse the Poynting rise.

At high pressure, the incompressibility assumption also weakens, and the ideal-gas mixture assumption fails for the vapour.

## Link to other topics

The same balance (extra pressure on a condensed phase raises its escaping tendency) gives the Kelvin equation for small droplets, where the extra pressure comes from surface tension rather than an inert gas. It also generalises: the quantity $P^{\mathrm{SAT}}\exp[\underline{V}^{l}(P-P^{\mathrm{SAT}})/RT]$ is the liquid's fugacity, which appears in every vapour–liquid equilibrium calculation with activity coefficients.

## Summary

A liquid under an insoluble gas has a vapour pressure slightly above its saturated value, because the gas compresses the liquid and raises its molar Gibbs energy by $\underline{V}^{l}(P-P^{\mathrm{SAT}})$. The vapour must match this by a rise of $RT\ln(P^{\mathrm{VAP}}/P^{\mathrm{SAT}})$. The vapour pressure obtained this way is effectively the partial pressure of an ideal gas that would be in equilibrium with the liquid.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-07 - Fugacity, definition and meaning.md>)

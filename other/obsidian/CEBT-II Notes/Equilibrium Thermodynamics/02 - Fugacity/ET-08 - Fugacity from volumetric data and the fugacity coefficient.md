[Previous](<ET-07 - Fugacity, definition and meaning.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-09 - fugacity of steam at 400 °C.md>)

<!-- note-content:start -->
# Section 08: Fugacity from volumetric data and the fugacity coefficient

*Notation:* $\phi_i = f_i/P$ is the fugacity coefficient of pure $i$. $\bar\phi_i = \bar f_i/P_i$ is the fugacity coefficient of $i$ in a mixture, where $P_i = y_iP$ is its partial pressure. $\underline{V}_i$ is the molar volume of pure $i$. $\bar V_i$ is the partial molar volume of $i$ in a mixture.

## Intuition

The obvious route is to start where the substance is surely ideal ($P = 0$) and integrate $\underline{V}\,dP$ up to the pressure of interest. At $P\to 0$, though, $\underline{V}\to\infty$ and $\ln f\to-\infty$, so the integral is infinite. That infinity is not caused by non-ideality: an ideal gas has it too. It is just the logarithmic dependence of $\underline{G}$ on $P$ for any gas.

So subtract what an ideal gas would do over the same path. The infinite parts cancel, and only the (finite) **gap** between the real isotherm and the ideal-gas isotherm is left. *This is like measuring the height of a building from its own ground floor rather than from the centre of the Earth.* The reference (the ideal gas) is chosen so that the large shared part drops out. The analogy breaks down because here the shared part is not just large but infinite, so the subtraction is needed for the integral to exist at all, not merely convenient.

## Derivation

**Step 1: the direct route fails at zero pressure.** For pure $i$ at constant $T$, integrate $RT\,d\ln f_i = \underline{V}_i\,dP$ from a finite lower pressure $P_0>0$:

$$RT\ln\frac{f_i(P)}{f_i(P_0)} = \int_{P_0}^P \underline{V}_i\,dP \qquad (P_0>0) \tag{44}$$

As $P_0\to0$, the gas approaches ideal behaviour and $f_i(P_0)\to0$: both sides of (44) diverge. Equation (44) is valid for $P_0>0$, but setting $P_0=0$ would leave an undefined logarithm. Subtract the ideal-gas differential before taking that limit.

**Step 2: write the same equation for an ideal gas.** For an ideal gas $\underline{V}^{\mathrm{IG}} = RT/P$ and $f^{\mathrm{IG}} = P$, so along the same isotherm

$$RT\,d\ln P = \frac{RT}{P}\,dP \tag{45}$$

**Step 3: subtract (45) from the differential form of (44) and integrate from 0 to $P$.**

$$RT\,d\ln\frac{f_i}{P} = \left(\underline{V}_i - \frac{RT}{P}\right)dP \;\;\Rightarrow\;\; RT\ln\frac{f_i}{P}\bigg|_P - RT\ln\frac{f_i}{P}\bigg|_{0} = \int_0^P\left(\underline{V}_i - \frac{RT}{P}\right)dP$$

*Reason:* at the lower limit the real gas is ideal, so $f_i/P\to 1$ and that term vanishes. Both divergences have cancelled.

**Step 4: define the fugacity coefficient.**

$$\phi_i \equiv \frac{f_i}{P}, \qquad RT\ln\phi_i = \int_0^P\left(\underline{V}_i - \frac{RT}{P}\right)dP \qquad (\text{constant } T) \tag{46}$$

The integrand stays finite as $P\to 0$. In the low-pressure limit it tends to the second virial coefficient $B$ (Step 6).

**Step 5: compressibility-factor form.** Write $\underline{V}_i = Z_iRT/P$. Then $\underline{V}_i - RT/P = (Z_i - 1)RT/P$, and (46) becomes

$$\ln\phi_i = \int_0^P\frac{Z_i - 1}{P}\,dP \tag{47}$$

This is the form used with EOS and generalised $Z$ charts.

**Step 6: virial gas.** Use the pressure-explicit virial equation, $Z = 1 + B'P + C'P^2 + \dots$, where $B' = B/RT$ and $C' = (C - B^2)/(RT)^2$. These follow from matching it term by term with the volume form $Z = 1 + B/\underline{V} + C/\underline{V}^2$. Then $(Z-1)/P = B' + C'P$, and (47) integrates at once:

$$\ln\phi = B'P + \tfrac{1}{2}C'P^2 \;\approx\; \frac{BP}{RT} \quad (\text{low } P) \tag{48}$$

**Step 7: physical meaning, the residual Gibbs energy.** Write the definition of fugacity for the real fluid and for an ideal gas at the *same* $T$ and $P$, then subtract. The reference terms cancel:

$$\underline{G}_i(T,P) - \underline{G}_i^{\mathrm{IG}}(T,P) = RT\ln\frac{f_i}{P} = RT\ln\phi_i \tag{49}$$

So $RT\ln\phi_i$ is the **residual Gibbs energy**: how much lower (or higher) the molar Gibbs energy of the real fluid is than that of an ideal gas at the same conditions.

**Step 8: component in a mixture.** Define $\bar\phi_i = \bar f_i/(y_iP)$. At constant $T$ and composition, $(\partial\mu_i/\partial P)_{T,n} = \bar V_i$, while for the same mixture as an ideal gas $(\partial\mu_i^{\mathrm{IG}}/\partial P)_{T,n} = RT/P$. Subtract the two and integrate from $P = 0$, where every mixture is an ideal-gas mixture and $\bar\phi_i = 1$:

$$RT\ln\bar\phi_i = \int_0^P\left(\bar V_i - \frac{RT}{P}\right)dP \qquad (\text{constant } T,\ \text{composition}) \tag{50}$$

This has the same structure as (46), with the partial molar volume in place of the pure molar volume. It needs a mixture EOS (with mixing rules), because $\bar V_i$ depends on composition.

## Motivation and explanation

**Why another virial term can improve fugacity.** With the density virial coefficients $B$ and $C$, the pressure-series expression contains $B'=B/(RT)$ and $C'=(C-B^2)/(RT)^2$. For nitrogen at 273.15 K and 100 atm, $B=-10.30\ \mathrm{cm^3\,mol^{-1}}$ and $C=1430\ \mathrm{cm^6\,mol^{-2}}$ give
$$\ln\phi\approx B'P=-0.0460,\qquad\ln\phi\approx B'P+\tfrac12C'P^2=-0.0328.$$
The respective fugacity coefficients are approximately 0.955 and 0.968, compared with the reference value 0.9703. The positive higher-density contribution partly offsets the attractive low-density term, so extrapolating the initial slope exaggerates the departure. Including another term improves this comparison, but does not establish convergence near a critical region.

**What $\phi$ measures.** By (49), $\phi$ is the residual Gibbs energy expressed as a factor on pressure. Its sign relative to 1 reflects the accumulated volume departure along the isotherm, not just the volume at the final pressure.
- $\phi < 1$: the integrated volume departure is negative. Attractions often dominate over much of the path, lowering the Gibbs energy and escaping tendency. This is typical of gases at modest pressures below their Boyle temperature, and of vapours.
- $\phi > 1$: the integrated volume departure is positive, often because repulsions dominate much of the path. Locally, the slope $d\ln\phi/dP=(\underline{V}-RT/P)/(RT)$ tells whether the volume is above or below the ideal-gas value.

One way to read (47) is to build the correction in small pressure increments. Wherever $Z<1$, the next increment lowers $\ln\phi$; wherever $Z>1$, it raises it. Repulsion can make $Z$ exceed unity near the final pressure while the negative area accumulated earlier still leaves $\phi<1$. Conversely, $Z=1$ at one pressure makes only the local slope vanish; it does not force $\phi=1$.

This is why the nitrogen example integrates the virial expansion rather than simply setting $\phi=Z$. Each pressure power acquires its own integration factor, so adding a term changes the accumulated Gibbs-energy correction differently from the local EOS volume.

In the figure, the integral (46) is the thin hatched area between the real isotherm and the ideal-gas isotherm. It is finite because the two curves converge as $P\to 0$, whereas the area under the real isotherm alone is unbounded.

![The area under the real isotherm from P = 0 is infinite, but the area between the real and ideal-gas isotherms (hatched, small) is finite and gives ln φ](../figs/ET-08-residual-integral-isotherm.png)

**Limiting cases.**
- Ideal gas: $\underline{V} = RT/P$, so the integrand is zero and $\phi = 1$.
- Low pressure: $\phi \approx 1 + BP/RT$, linear in $P$ with slope set by the second virial coefficient, which is negative below the Boyle temperature.
- $P\to 0$: $\phi\to 1$ for every substance and every mixture. This is what makes the ideal-gas reference work.

**Below the critical temperature.** If $T < T_c$, the integration path from $P = 0$ reaches the saturation pressure, where the substance condenses. To get a *liquid* fugacity:
1. integrate (46) through the vapour from 0 to $P^{\mathrm{SAT}}$, giving $\phi^{\mathrm{sat}}$;
2. cross the phase boundary, where $\underline{G}$ (and hence $f$) does not change, because liquid and vapour are in equilibrium;
3. continue up the liquid branch with the Poynting factor.

The result is $f^{l} = \phi^{\mathrm{sat}}P^{\mathrm{SAT}}\exp[\underline{V}^{l}(P-P^{\mathrm{SAT}})/RT]$. This reduces to the earlier form when the saturated vapour is ideal ($\phi^{\mathrm{sat}} = 1$). Integrating straight through the van der Waals loop would be wrong, because the loop is not a physical path.

**When the formulas fail.** Equations (46), (47) and (50) are exact. The approximations come only from the PVT information used:
- the truncated virial form (48) is good to moderate density but fails near the critical point and in liquids;
- tabulated data must reach low enough pressure for the integrand to be extrapolated to $P = 0$.

## Link to other topics

Equation (46) is the gas-phase counterpart of the liquid-phase activity coefficient that comes later. Both are correction factors on an ideal reference, and together they give the general vapour–liquid equilibrium relation $y_i\bar\phi_iP = x_i\gamma_if_i^{l}$. The residual-property idea in (49) is the same one used for departure enthalpies and entropies in process simulators.

## Summary

Integrating $\underline{V}\,dP$ from zero pressure diverges, but integrating the departure $\underline{V} - RT/P$ does not. The result is the fugacity coefficient, $RT\ln\phi = \int_0^P(\underline{V} - RT/P)\,dP$, which is the residual Gibbs energy expressed as a factor on pressure. It needs only PVT data.
<!-- note-content:end -->

[Previous](<ET-07 - Fugacity, definition and meaning.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-09 - fugacity of steam at 400 °C.md>)

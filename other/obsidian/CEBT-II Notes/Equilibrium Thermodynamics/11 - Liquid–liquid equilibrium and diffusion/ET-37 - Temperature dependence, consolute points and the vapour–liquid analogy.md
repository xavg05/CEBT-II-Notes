[Previous](<ET-36 - Why liquids separate, the curvature of the Gibbs energy of mixing.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-38 - isobutane–furfural liquid–liquid equilibrium.md>)

<!-- note-content:start -->
# Section 37: Temperature dependence, consolute points and the vapour–liquid analogy

## Intuition

$\Delta\underline{G}_{\mathrm{mix}} = \underline{H}^{ex} - T\left(\Delta\underline{S}^{\mathrm{IM}}_{\mathrm{mix}} + \underline{S}^{ex}\right)$, with $\Delta\underline{S}^{\mathrm{IM}}_{\mathrm{mix}} = -R\sum x_i\ln x_i > 0$.
- *UCST (normal):* unlike contacts cost energy ($\underline{H}^{ex} > 0$). The entropic reward for mixing grows with $T$, so it eventually wins and the liquids mix.
- *LCST:* unlike molecules hydrogen-bond specifically ($\underline{H}^{ex} < 0$), but that forces them into ordered arrangements ($\underline{S}^{ex} < 0$). At low $T$ the favourable energy wins and they mix. At high $T$ the $-T\underline{S}^{ex}$ penalty grows and they separate. Triethylamine–water is the classic example.
- *Closed loops* (both an LCST and a UCST) occur when these effects overlap.

## Derivation

**Step 1: regular solution.** Take one-constant Margules with $A$ independent of $T$ (pure energy, no excess entropy):

$$\frac{\Delta\underline{G}_{\mathrm{mix}}}{RT} = x\ln x + (1-x)\ln(1-x) + \frac{A}{RT}x(1-x)$$

**Step 2: curvature.**

Holding $A$ fixed holds the energetic cost of unlike contacts fixed. Heating still reduces $A/RT$: thermal mixing entropy becomes more competitive even though the contact energy has not changed. The critical temperature is where the strongest tendency to lose convexity, at the symmetric composition, is just balanced by the ideal-entropy curvature.

This assumption can produce a UCST but cannot produce an LCST. In the latter case heating must increase the effective penalty for mixing, for example by removing favourable ordered interactions. A temperature-dependent fitted parameter then represents changing enthalpic and entropic contributions, rather than simply the same fixed contact penalty divided by a larger $RT$.

$$\frac{1}{RT}\frac{d^2\Delta\underline{G}_{\mathrm{mix}}}{dx^2} = \frac{1}{x(1-x)} - \frac{2A}{RT}$$

The first term is smallest at $x = \tfrac12$, where it equals 4.

**Step 3: consolute point.** The curve first loses convexity (at $x = \tfrac12$) when $2A/RT = 4$:

$$T_c = \frac{A}{2R}, \qquad x_c = \tfrac12 \tag{155}$$

At a consolute point both $d^2\underline{G}/dx^2 = 0$ and $d^3\underline{G}/dx^3 = 0$: the two spinodal points merge.

**Step 4: below $T_c$.**
- *Binodal* (coexistence) compositions from the common tangent. By symmetry, $\ln[x/(1-x)] = (A/RT)(2x - 1)$.
- *Spinodal* compositions where the curvature vanishes: $x(1-x) = RT/(2A)$.

**Step 5: analogy with pure-fluid VLE.**

| Pure fluid, $P$–$\underline{V}$ isotherms | Binary liquid, $\underline{G}$–$x_1$ isotherms |
|---|---|
| Van der Waals loop below $T_c$ | Wiggle below $T_c$ |
| Equal areas → coexisting $\underline{V}^l$, $\underline{V}^v$ | Common tangent → coexisting $x_1^{\mathrm{I}}$, $x_1^{\mathrm{II}}$ |
| $dP/d\underline{V} = 0$: limit of metastability | $d^2\underline{G}/dx_1^2 = 0$: spinodal |
| Critical point: $dP/d\underline{V} = d^2P/d\underline{V}^2 = 0$ | Consolute point: $d^2\underline{G}/dx^2 = d^3\underline{G}/dx^3 = 0$ |

*Where the analogy breaks down:* at a consolute point the two coexisting *liquids* become identical in composition, but the system is still liquid and is not a gas–liquid critical point. Its pressure dependence is weak, and the "order parameter" is composition, not density.

![T–x diagram with an upper consolute point: binodal (solid) and spinodal (dashed) meet at Tc; G–x isotherms above, at and below Tc](../figs/ET-37-binodal-spinodal-analogy.png)

![Four types of liquid–liquid phase diagram: LCST (triethylamine–water), UCST (phenol–water), closed loop (D2O–2-methylpyridine), and separate UCST and LCST regions (sulphur–triphenylamine)](../figs/ET-37-UCST-LCST-shapes.png)

## Motivation and explanation

**Opening a miscibility gap near its critical point.** In a symmetric regular solution with temperature-independent $A$, $A/(RT)=2T_c/T$. Cooling below $T_c$ increases the mixing penalty relative to entropy and separates both binodal and spinodal branches. Expanding $\ln[x/(1-x)]$ about $x=1/2$ shows that the first nonzero composition displacement scales as $\sqrt{T_c-T}$ close to the critical point. The gap therefore opens steeply just below $T_c$. A symmetric approximation necessarily puts the critical composition at one half; fitting an experimental critical temperature does not correct an experimentally off-centre critical composition. Its temperatures and trends should not be mistaken for an accurate asymmetric phase diagram.

**Phase rule.** In the two-liquid region, $F = 2 - 2 + 2 = 2$. Fix $T$ and $P$ and both compositions are fixed; the feed composition only sets the amounts (lever rule). At the consolute point the extra condition $x^{\mathrm{I}} = x^{\mathrm{II}}$ leaves $F = 1$: at fixed pressure it is a single point.

**Real systems are asymmetric.** Consolute compositions are rarely 0.5 (hexane–nitrobenzene: $x_c\approx 0.42$ nitrobenzene). Asymmetric models (van Laar, NRTL) are needed to place them correctly. $A$ also usually varies with $T$, so a real $\underline{S}^{ex}\neq 0$.

## Link to other topics

Temperature-swing extraction exploits the opening and closing of the miscibility gap. Polymer solutions with an LCST (e.g. thermoresponsive hydrogels) are used in drug delivery and bioseparations. The vapour–liquid analogy returns when vapour and two liquids coexist (VLLE) in the final sections.

## Summary

Miscibility gaps open and close with temperature through the balance of $\underline{H}^{ex}$ and $T\underline{S}$. A regular solution has a UCST at $T_c = A/2R$, while LCSTs need favourable but ordering interactions. At a consolute point the spinodal and binodal meet, analogous to (but not the same as) a vapour–liquid critical point.
<!-- note-content:end -->

[Previous](<ET-36 - Why liquids separate, the curvature of the Gibbs energy of mixing.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-38 - isobutane–furfural liquid–liquid equilibrium.md>)

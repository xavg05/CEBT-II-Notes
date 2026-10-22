[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-02 - Equations of state and departure functions.md>)

<!-- note-content:start -->
# Section 01: The criterion for phase equilibrium

*Notation (used throughout):* a plain symbol is a total (extensive) property, e.g. $G$, $V$. An underline is a molar property, e.g. $\underline{G} = G/n$; this course writes $\underline{V}$ where many texts write $V_m$. A subscript $i$ on an underlined symbol means pure $i$, e.g. $\underline{G}_i$. Superscripts $L$, $V$, $S$ label liquid, vapour and solid.

## Intuition

At constant $T$ and $P$ the system exchanges heat and work with surroundings that hold $T$ and $P$ fixed. The Gibbs energy is the quantity that accounts for the entropy change of *both* the system and those surroundings. So "the universe's entropy goes up" becomes "the system's $G$ goes down".

Chemical potential is how much $G$ changes when one more mole of a component is added to a phase. If moving a molecule from phase L to phase V lowers $G$, it will move. It stops moving when the transfer no longer changes $G$, i.e. when the chemical potentials are equal.

*Analogy: water levels in connected tanks.* Water flows from the higher level to the lower until the levels match, and $\mu_i$ plays the role of the level. The analogy breaks down because each component has its own "level", and the levels can differ between components. Also, $\mu_i$ is not a fixed property of a phase: it changes as the phase's composition changes, which a tank's water level does not do in the same way.

## Derivation

**Step 1: $G$ is minimised at constant $T$, $P$.** For a closed system exchanging heat with surroundings at $T$, the surroundings receive $-dH$ as heat at constant $P$, so $dS_{\mathrm{surr}} = -dH/T$. The second law requires $dS + dS_{\mathrm{surr}} \ge 0$. Multiply by $-T$:

$$dG = dH - T\,dS \le 0 \qquad (\text{constant } T, P) \tag{1}$$

*Reason:* at constant $T$, $dG = dH - T\,dS$. So every spontaneous change at fixed $T$ and $P$ lowers $G$, and equilibrium is the minimum.

**Step 2: the fundamental relation.** For a closed, homogeneous phase,

$$dG = -S\,dT + V\,dP \tag{2}$$

This combines the first law, $dU = \delta Q + \delta W$, with $\delta Q_{\mathrm{rev}} = T\,dS$ and the definition of $G$. It holds for any change between equilibrium states. If the phase is *open*, its amounts can also change, and each mole of $i$ added changes $G$ by $\mu_i$:

$$dG = -S\,dT + V\,dP + \sum_i \mu_i\,dn_i, \qquad \mu_i \equiv \left(\frac{\partial G}{\partial n_i}\right)_{T,P,n_{j\neq i}} \tag{3}$$

**Step 3: two phases in contact.** Take a closed system with phases L and V at the same $T$ and $P$. Move $dn$ moles of component $i$ from L to V, so $dn_i^V = +dn$ and $dn_i^L = -dn$. Apply (3) to each phase (each is open, but the whole is closed) at constant $T$, $P$:

$$dG = dG^L + dG^V = \left(\mu_i^V - \mu_i^L\right)dn \tag{4}$$

**Step 4: equilibrium and direction.** At the minimum of $G$, (4) must vanish for any small transfer, so

The important choice in (4) is to transfer just one component while conserving its total amount. Such a transfer can be made in either direction, independently of transfers of the other components. If its coefficient were non-zero, one direction would lower $G$, so the state could not be an equilibrium minimum. This is why each chemical potential must match separately; a cancellation between transfers of different components would not suffice.

Equality removes the immediate driving force, but it is a stationary-state condition. To establish stable equilibrium, the state must also have the lowest accessible $G$. The supercooled-water example illustrates the distinction: the bulk free-energy advantage determines which phase wins, while creating an interface can delay its appearance.

$$\mu_i^L = \mu_i^V \quad \text{for every component } i \tag{5}$$

Away from equilibrium, (1) requires $dG < 0$. If $\mu_i^L > \mu_i^V$, then $dn > 0$: component $i$ moves from the phase where its chemical potential is higher to where it is lower.

**Step 5: pure substance.** For pure $i$, $G = n\underline{G}_i(T,P)$, so $\mu_i = \partial G/\partial n = \underline{G}_i$. Equation (5) becomes

$$\underline{G}^L = \underline{G}^V \tag{6}$$

## Motivation and explanation

**How supercooling supplies a driving force.** At fixed pressure, subtracting the two relations $d\underline G/dT=-\underline S$ gives
$$\frac{d(\underline G^L-\underline G^S)}{dT}=-\Delta\underline S_{\mathrm{fus}}.$$
Anchor the integral at the melting temperature $T_f$, where the two Gibbs energies are equal. If the entropy of fusion changes negligibly over the temperature interval,
$$\underline G^L-\underline G^S\approx\frac{\Delta\underline H_{\mathrm{fus}}}{T_f}(T_f-T).$$
For water with $\Delta\underline H_{\mathrm{fus}}=6009\ \mathrm{J\,mol^{-1}}$ and $T_f=273.15\ \mathrm K$, supercooling by 10 K gives about $220\ \mathrm{J\,mol^{-1}}$ in favour of ice; halving the supercooling halves this incentive. The liquid's larger entropy stabilises it above $T_f$, but cannot compensate its larger enthalpy below $T_f$. Nucleation may still delay freezing: a favourable bulk Gibbs-energy change does not remove an interfacial barrier.

**Why $\mu_i$ and not concentration.** Material does not, in general, move down a concentration gradient. Water and oil sit side by side with very different water concentrations and nothing flows. What equalises is $\mu_i$, which includes the energetic preference of each molecule for its surroundings.

**What is held constant.** Equation (1) needs fixed $T$ and $P$. Equation (5) also assumes:
- thermal equilibrium (same $T$ in both phases);
- mechanical equilibrium (same $P$, which is true across a flat interface);
- that component $i$ can actually cross between the phases.

Later sections relax these one at a time. Across a curved interface (droplets and bubbles) the pressures differ. Across a semipermeable membrane only some components can cross (osmosis). Each case changes which equalities hold, and that is exactly how those problems are solved.

**Sanity check.** At the normal melting point, ice and water coexist, so (6) holds at 0 °C and 1 atm. Below that temperature (6) fails and the phase with the lower $\underline{G}$ wins. The supercooling relation above quantifies this.

## Link to other topics

The same calculation, with the liquid's chemical potential lowered by a dissolved solute, gives freezing-point depression later in the course. The chemical potential defined in (3) is the partial molar Gibbs energy, the subject of the partial-molar-property sections that follow.

## Summary

At constant $T$ and $P$, equilibrium is the minimum of $G$. Between phases this means equal molar Gibbs energy for a pure substance and equal chemical potential of every component for a mixture, with material flowing from high to low $\mu_i$. Everything else is about computing $\mu_i$.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-02 - Equations of state and departure functions.md>)

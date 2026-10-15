[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-21 - Structural DNA nanotechnology and DNA origami.md>)

<!-- note-content:start -->
# Section 20: DNA as a material

## Intuition

A useful construction material needs bonds that are *specific* (part A joins only to part B) and *reversible* (a mistake can be undone rather than frozen in). Most materials offer one or the other. Covalent bonds are specific but permanent; van der Waals contacts are reversible but indiscriminate.

Base pairing gives both at once, and it adds something neither offers: the bond strength is **programmable**. Choosing a sequence sets $\Delta G^0$, and $\Delta G^0$ sets both the stability and, through Section 05, the lifetime. The designer specifies which parts stick, how strongly, and how fast, by typing letters.

*Analogy:* a construction kit where every connector is cut to a code and you can order as many distinct codes as you like. The analogy breaks down because the connectors are not rigid — the strength is statistical, set by temperature and concentration, so "will these two bind?" has no answer without saying at what temperature and how dilute.

## Mechanism

**The properties that matter for construction:**

- **Chemically stable.** Unlike RNA, DNA has no 2′-OH to attack its own backbone (Section 01), so structures survive for months.
- **Arbitrary sequences are cheap.** Phosphoramidite synthesis (Section 06) makes any sequence to order, at steadily falling cost.
- **Easily functionalised.** Fluorophores, quenchers, thiols, biotin and click handles attach at either end or internally (Section 06), so DNA can be the connector between non-DNA components.
- **Known polymer physics.** ssDNA is flexible ($l_P \approx 1$–2 nm) and dsDNA is stiff ($l_P \approx 50$ nm, Section 02). Short duplexes act as rigid struts and single strands as hinges, and the designer chooses which by choosing where to pair.
- **Predictable thermodynamics.** $\Delta G^0$ and $T_m$ follow from the sequence (Section 04), so a design can be checked before it is made.
- **Thermally reversible near ambient conditions.** Melting temperatures sit in a convenient range, so structures can be assembled by cooling and disassembled by heating.

![Fraction hybridised against temperature: a sharp sigmoid with the duplex AB below Tm and free strands A and B above](../figs/AB-20-melting-reversible.png)

## Derivation

**Selectivity.** From Section 04, a complementary 12-mer has $\Delta H^0 = -87.2$ kcal/mol and $\Delta S^0 = -240.3$ cal K⁻¹ mol⁻¹. At 20 °C:
$$\Delta G^0 = \Delta H^0 - T\Delta S^0 = -87.2 + 293.15\times0.2403 = -16.8\ \text{kcal/mol} \tag{33}$$

Two *random* 12-mers share only short accidental stretches of complementarity, giving $\Delta G^0 \approx -2.9$ kcal/mol. The gap is $\approx 14$ kcal/mol, which at $RT = 0.58$ kcal/mol is a binding-constant ratio of
$$\frac{K_{\text{complementary}}}{K_{\text{random}}} = \exp\!\left(\frac{13.9}{0.58}\right) \approx 3\times10^{10} \tag{34}$$

In temperature terms the same gap appears as $T_m = 53$ °C against $T_m = -31$ °C: the designed pair needs heating past 50 °C to separate, while the random pair would need cooling far below freezing to associate at all. **There is a wide temperature window in which intended bonds are fully formed and unintended ones are entirely absent.**

**Orthogonality.** The number of distinct $N$-mers is $4^N$. For $N = 12$:
$$4^{12} = 1.7\times10^{7} \tag{35}$$
Almost all pairs drawn from this set interact at the random level of (34) rather than the complementary level. A designer can therefore pick a large set of sequences that are mutually non-interacting — *orthogonal* — and use each as an independent, addressable bond type.

This is the property that makes complex structures possible. With one bond type you can make a polymer; with hundreds of orthogonal bond types you can specify which particular component goes in which particular position.

## Motivation and explanation

**Why the gap in (34) is so large.** Both $\Delta H^0$ and $T\Delta S^0$ scale with the number of base pairs formed, and they nearly cancel (Section 04). A mismatched pair forms far fewer base pairs, so it loses the enthalpy but keeps most of the entropic cost of association. Selectivity is a *difference of two large numbers*, which is why it is so sharp, and also why it is sensitive to temperature.

**Why orthogonality is not simply $4^N$.** Equation (35) counts sequences, not usable ones. Sequences that are each other's partial complements must be excluded, as must those that fold on themselves, and GC content must be matched so that all pairs share a common $T_m$ (Section 04). The usable orthogonal set is far smaller than $4^N$ — but it is still in the hundreds or thousands, which is more than any structure needs.

**Where it fails.** Selectivity degrades as structures grow: with hundreds of strands in one pot, there are hundreds of thousands of pairwise combinations, so even a one-in-a-million spurious interaction becomes likely. This is why design is done computationally, by software that evaluates all pairings rather than just the intended ones.

A weak unintended contact can become troublesome when another contact has already tethered the two components together. The second site then searches a small local volume rather than the whole solution, reducing the association entropy cost. Pairwise sequence screening is therefore a starting point, rather than proof that a large multivalent structure has no alternative assembly. Geometry and the order in which contacts form also matter.

**The limits of the material.** DNA is not strong — a duplex is held by a few tens of $k_BT$ — so DNA objects are soft, and they require salt to screen the backbone charge (Section 01). They are also expensive per unit mass. DNA is not a structural material in the engineering sense; it is a material for *arranging other things with nanometre precision*.

## Link to other topics

The selectivity argument is the same one behind any chromatographic separation: a useful separation needs a large ratio of affinities between the wanted and unwanted species, and that ratio is exponential in the free-energy difference.

## Summary

DNA is a good construction material because sequence sets bond strength, giving a free-energy gap of about 14 kcal/mol between designed and accidental pairing, a factor of $10^{10}$ in binding constant. With $4^{12} = 1.7\times10^7$ sequences available, many mutually orthogonal bonds can be specified at once.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-21 - Structural DNA nanotechnology and DNA origami.md>)

[Previous](<ET-02 - Equations of state and departure functions.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-04 - Chemical potential and the Gibbs–Duhem equation.md>)

<!-- note-content:start -->
# Section 03: Partial molar properties

*Notation:* $V$ is the total volume. $\underline{V}$ is the molar volume of the system (pure or mixture). $\underline{V}_i$ is the molar volume of pure $i$. $\bar V_i$ is the partial molar volume of $i$ in a mixture. $x_i = n_i/n$ is the mole fraction, where $n$ is the total amount.

## Intuition

Add one mole of water to a swimming pool of pure water and the volume rises by 18 cm³, the molar volume of water. Add the same mole of water to a swimming pool of pure ethanol and the volume rises by only about 14 cm³. The water molecules are the same; what differs is their surroundings. Hydrogen bonding with ethanol and different packing let them occupy less space.

The partial molar volume is that increase: the volume a component *effectively* occupies in a particular mixture. It is a property of the component **in that environment**, so it changes with composition. The swimming pool is large so that adding one mole does not change the composition.

*Analogy:* pouring sand into a jar of marbles. The sand fills the gaps, so the total rises by less than the sand's own volume. This breaks down for molecules. Water–ethanol contraction comes from intermolecular forces (hydrogen bonding) as well as shape, so the "gaps" depend on energetics and temperature, not just geometry.

## Derivation

**Step 1: definition.** For any extensive property, using volume as the example,

$$\bar V_i \equiv \left(\frac{\partial V}{\partial n_i}\right)_{T,P,n_{j\neq i}} \tag{11}$$

*Reason:* this is the change in total volume per mole of $i$ added, with $T$, $P$ and all other amounts fixed. That is the swimming-pool experiment taken to the limit of an infinitesimal addition.

**Step 2: scaling property.** At fixed $T$ and $P$, doubling every amount doubles the volume. In general, for any factor $\lambda$:

$$V(T,P,\lambda n_1,\dots,\lambda n_N) = \lambda\,V(T,P,n_1,\dots,n_N) \tag{12}$$

*Reason:* $V$ is extensive. Mathematically, it is homogeneous of degree one in the amounts.

**Step 3: differentiate (12) with respect to $\lambda$.** Using the chain rule on the left side:

$$\sum_i \frac{\partial V}{\partial(\lambda n_i)}\,n_i = V$$

**Step 4: set $\lambda = 1$.** The derivatives become the partial molar volumes (11):

$$V = \sum_i n_i\,\bar V_i \qquad\Longleftrightarrow\qquad \underline{V} = \sum_i x_i\,\bar V_i \tag{13}$$

*Reason:* dividing by $n$ gives the molar form. This is Euler's theorem for homogeneous functions. It says the partial molar volumes are the right "shares" of the total: they add up exactly to the mixture volume.

**Step 5: pure-component limit.** For pure $i$, $V = n_i\underline{V}_i$, so $\bar V_i = \underline{V}_i$.

The same steps apply to $U$, $H$, $S$, $A$ and $G$. Each has partial molar properties that sum like (13).

## Motivation and explanation

**Why not just use pure volumes?** If mixing changed nothing, $\bar V_i$ would equal $\underline{V}_i$ and the mixture volume would be $\sum n_i\underline{V}_i$. Any difference between the two is a measure of non-ideal mixing, the subject of most of this course. Volume is the easiest place to see it because it can be measured with a measuring cylinder.

**What is held constant.** Equation (11) holds $T$, $P$ and all other $n_j$ fixed. It is not a derivative with respect to mole fraction, because adding $i$ changes all the mole fractions at once.

**Graphical meaning.** Partial molar volumes in a binary are found from plots of $\underline{V}$ against $x$ (the tangent construction), or plotted directly as below. They are intensive: they depend on composition, $T$ and $P$, not on how much mixture there is.

![Partial molar volumes of water (left axis) and ethanol (right axis) against ethanol mole fraction; the lines mark x = 0.17](../figs/ET-03-partial-molar-volumes-ethanol-water.png)

The curves move in opposite directions. Where ethanol's partial molar volume rises, water's falls. This is not a coincidence: it is the Gibbs–Duhem equation, derived in the next section.

## Worked example

**Problem.** A 700 cm³ bottle contains a whiskey-like ethanol–water mixture prepared from pure-liquid volumes in the ratio 40:60. Here 40 % means ethanol volume divided by the sum of the two pure-liquid volumes before mixing; it is not the usual alcohol-by-volume (ABV) label, which uses the final drink volume. How much ethanol and water does it contain, and what volume would the two pure liquids have occupied before mixing? Pure molar volumes: $\underline{V}_{\mathrm{EtOH}} = 58$ cm³ mol⁻¹, $\underline{V}_{\mathrm{H_2O}} = 18$ cm³ mol⁻¹.

**Mole fraction.** For this explicitly defined pre-mixing recipe, take 100 cm³ of separate pure liquids: $40/58 = 0.690$ mol ethanol and $60/18 = 3.333$ mol water, so $x_{\mathrm{EtOH}} = 0.171$, about 17 mol %. Use $x_{\mathrm{EtOH}} \approx 0.17$ for the graph estimates below.

**Partial molar volumes at $x_{\mathrm{EtOH}} = 0.17$** (read from the graph, so ≈): $\bar V_{\mathrm{EtOH}} \approx 54.7$ cm³ mol⁻¹, $\bar V_{\mathrm{H_2O}} \approx 17.8$ cm³ mol⁻¹. Both are below their pure values.

**Total amount from (13).** With $V = n\,(x_{\mathrm{EtOH}}\bar V_{\mathrm{EtOH}} + x_{\mathrm{H_2O}}\bar V_{\mathrm{H_2O}})$:

$$700 = n\,(0.17\times54.7 + 0.83\times17.8) \;\Rightarrow\; n = 29.08\ \text{mol}$$

so $n_{\mathrm{EtOH}} = 4.94$ mol and $n_{\mathrm{H_2O}} = 24.13$ mol.

**Volumes before mixing.** Ethanol: $4.94\times58 = 287$ cm³. Water: $24.13\times18 = 434$ cm³. Together that is **721 cm³ of pure liquids, which make 700 cm³ of whiskey**: a contraction of 21 cm³, or 2.9 %.

**Interpretation.** Adding pure-component volumes would overfill the bottle by 3 %. Ethanol–water is a non-ideal mixture, and a model that assumes ideal mixing gets even the volume wrong. Because the volume differs from the ideal value, the Gibbs energy and chemical potentials must differ too.

## Link to other topics

The chemical potential is the partial molar property of $G$, so (13) becomes $G = \sum n_i\mu_i$: the identity that underlies the Gibbs–Duhem equation and every later model of mixture non-ideality. Excess volumes such as the 21 cm³ here are the volumetric counterpart of the excess Gibbs energy used to build activity-coefficient models.

## Summary

A partial molar property is a component's contribution to a mixture property in its actual environment. The contributions sum exactly to the total, but they differ from pure-component values whenever mixing is non-ideal, as the 3 % contraction of whiskey shows.
<!-- note-content:end -->

[Previous](<ET-02 - Equations of state and departure functions.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-04 - Chemical potential and the Gibbs–Duhem equation.md>)

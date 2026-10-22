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

Equation (13) uses all the partial molar volumes at the *final mixture composition*. It does not say that ethanol and water carry fixed parcels of volume from their pure states into the bottle. Adding ethanol changes the surroundings of water as well as those of ethanol; the measured total volume includes that collective rearrangement. The derivative assigns its net effect to the increment being added.

That is why the bottle calculation first finds composition from the amounts in the recipe, then reads both partial molar volumes at that composition, and only then reconstructs the final volume. Using pure volumes in the last step would erase the very change in molecular surroundings that the graph measures.

**Step 5: pure-component limit.** For pure $i$, $V = n_i\underline{V}_i$, so $\bar V_i = \underline{V}_i$.

The same steps apply to $U$, $H$, $S$, $A$ and $G$. Each has partial molar properties that sum like (13).

## Motivation and explanation

**Volume recipes and volume contraction.** A 40:60 ratio of separate pure ethanol and water volumes is not a 40 mol % mixture, nor is it the usual ABV definition based on the final drink volume. Using pure molar volumes of 58 and $18\ \mathrm{cm^3\,mol^{-1}}$, respectively, a $100\ \mathrm{cm^3}$ pre-mixing basis gives $x_{\mathrm{EtOH}}\approx0.171$. At the nearby graph composition 0.17, partial molar volumes are approximately 54.7 and $17.8\ \mathrm{cm^3\,mol^{-1}}$. These give
$$n=\frac{700}{0.17(54.7)+0.83(17.8)}\approx29.08\ \mathrm{mol}.$$
A $700\ \mathrm{cm^3}$ bottle then contains about 4.94 mol ethanol and 24.13 mol water, whose separate pure-liquid volumes total approximately $721\ \mathrm{cm^3}$. The roughly 3 % contraction shows why pure molar volumes cannot replace partial molar volumes. These are graph-based estimates. A nonzero excess volume constrains the pressure dependence of the excess Gibbs energy; it does not by itself determine that Gibbs energy at one pressure.

**Why not just use pure volumes?** If mixing changed nothing, $\bar V_i$ would equal $\underline{V}_i$ and the mixture volume would be $\sum n_i\underline{V}_i$. Any difference between the two is a measure of non-ideal mixing, the subject of most of this course. Volume is the easiest place to see it because it can be measured with a measuring cylinder.

**What is held constant.** Equation (11) holds $T$, $P$ and all other $n_j$ fixed. It is not a derivative with respect to mole fraction, because adding $i$ changes all the mole fractions at once.

**Graphical meaning.** Partial molar volumes in a binary are found from plots of $\underline{V}$ against $x$ (the tangent construction), or plotted directly as below. They are intensive: they depend on composition, $T$ and $P$, not on how much mixture there is.

![Partial molar volumes of water (left axis) and ethanol (right axis) against ethanol mole fraction; the lines mark x = 0.17](../figs/ET-03-partial-molar-volumes-ethanol-water.png)

The curves move in opposite directions. Where ethanol's partial molar volume rises, water's falls. This is not a coincidence: it is the Gibbs–Duhem equation, derived in the next section.

## Link to other topics

The chemical potential is the partial molar property of $G$, so (13) becomes $G = \sum n_i\mu_i$: the identity that underlies the Gibbs–Duhem equation and every later model of mixture non-ideality. Excess volumes such as the contraction discussed here are the volumetric counterpart of the excess Gibbs energy used to build activity-coefficient models.

## Summary

A partial molar property is a component's contribution to a mixture property in its actual environment. The contributions sum exactly to the total, but they differ from pure-component values whenever mixing is non-ideal, as the 3 % contraction of whiskey shows.
<!-- note-content:end -->

[Previous](<ET-02 - Equations of state and departure functions.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-04 - Chemical potential and the Gibbs–Duhem equation.md>)

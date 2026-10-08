# Section 43: Precipitation by salting out and the Cohn equation

## Overview

Precipitation induces the target to come out of solution as a solid, which can then be recovered by filtration or centrifugation (Sections 33–37). It is the other main primary isolation route, and unlike extraction (Section 42) it **concentrates** the product. This note covers the general principle, the mechanism of **salting out**, and the **Cohn equation** that describes it, with a worked example on antibody recovery.

*Assumed:* primary isolation in the downstream train (Section 32); protein structure and the hydrophobic effect (Section 23).

## Intuition

A protein stays dissolved because its surface interacts favourably with water: charged and polar groups are hydrated, and a **solvation shell** of ordered water surrounds the molecule. That shell also screens the protein's hydrophobic patches, keeping them from finding each other.

Anything that makes water less available to the protein destabilises this arrangement. Add enough salt and the ions, which hydrate strongly themselves, compete for the water. The solvation shell thins, hydrophobic regions become exposed, and proteins aggregate with one another instead — they precipitate.

That is the whole mechanism: **precipitation is caused not by the salt attacking the protein, but by the salt removing its water.**

*Analogy:* a crowd staying apart because each person holds an umbrella. Take the umbrellas away and people huddle together. The analogy breaks down because salt at *low* concentration has the opposite effect — it screens electrostatic repulsion and *increases* solubility, which is why the solubility curve has a maximum rather than falling monotonically.

## Mechanism

![Three tubes: a clear solution, a suspension with particles throughout, and a settled precipitate below a clear supernatant](figs/AB-43-precipitation.png)

**The general principle.** Precipitation is induced by a **decrease in the solubility** of the compound on addition of **salts, solvents or polymers**, or in response to changes in **pH**. These additives, or changes in surface chemistry, make interactions with water less favourable, causing aggregation.

**Four methods** are used in bioprocessing, primarily to recover proteins:
- a) salting out (this note);
- b) isoelectric precipitation;
- c) polymer precipitation;
- d) organic solvent precipitation (Section 44).

Precipitation is often used for proteins, can **remove large amounts of water**, and the precipitate can be extracted by further filtration or centrifugation. However, only **partial purification** is achieved, since proteins of similar characteristics precipitate together — consistent with its role as a non-selective primary isolation step (Section 32).

### Salting out

![Solubility against salt concentration: low at low salt, rising to a maximum in the salting-in region, then falling steeply in the salting-out region, with insets showing the hydrate shell and aggregated protein](figs/AB-43-salting-out-curve.png)

The solubility of molecules with hydrophobic regions — proteins in particular — depends on salt concentration in a non-monotonic way:
- **low at low salt concentration**;
- rising to a **peak at intermediate concentration**;
- **dropping again at high concentration**.

The rise is called **salting in**; the fall is **salting out**, and it is the regime used for protein precipitation.

**Why the fall happens.** Salting out depends on ions, particularly **anions**, interfering with the solvation of water:
- Water molecules form a **solvation shell** around proteins, which **prevents aggregation**.
- At higher salt concentration, anions bind more often to water, making it **less available to form the solvation shell** and thus prompting aggregation.
- **Solvation is also important for the secondary and tertiary structure of proteins**, so high salt may also cause protein **unfolding** — the main risk of the method.

**Not all salts are equal.** Different anions have different effectiveness at inducing salting out, ranked in the **Hofmeister series**, discovered by Franz Hofmeister:
$$\mathrm{F^-} \sim \mathrm{SO_4^{2-}} > \mathrm{HPO_4^{2-}} > \mathrm{CH_3COO^-} > \mathrm{Cl^-} > \mathrm{Br^-} > \mathrm{NO_3^-} > \mathrm{ClO_3^-} > \mathrm{I^-} > \mathrm{ClO_4^-} > \mathrm{SCN^-}$$
Ions on the left are most effective at precipitating; those on the right can even increase solubility. The origin of these differences is still a matter of research. Ammonium sulfate is the standard choice in practice, because sulfate sits near the strong end and the salt is cheap and highly soluble.

Different proteins salt out at different concentrations depending on their hydrophobicity, which is what makes the method partially selective: raising the salt in steps precipitates different fractions.

## Derivation

**The Cohn equation** describes the solubility $S$ of a protein in the salting-out regime:
$$\ln S = \beta_s - K_sC_s \tag{1}$$
where $C_s$ is the salt concentration, and $\beta_s$ and $K_s$ are constants that depend on the protein and the salt. $\beta_s$ is also a function of temperature and pH.

The form says that **$\ln S$ falls linearly with salt concentration** — solubility decays exponentially. With $K_s$ of order 2 M⁻¹, each additional 0.5 M of salt divides the solubility by about $e$, and about 1.1 M divides it by ten. This steepness is what makes the method practical with modest amounts of salt.

**Fitting the constants.** Two measurements of solubility at two salt concentrations suffice. Writing (1) at $(S_1,C_{s,1})$ and $(S_2,C_{s,2})$ and subtracting eliminates $\beta_s$:
$$\ln\frac{S_1}{S_2} = K_sC_{s,2}-K_sC_{s,1} \quad\Longrightarrow\quad K_s = \frac{\ln(S_1/S_2)}{C_{s,2}-C_{s,1}} \tag{2}$$
Then $\beta_s$ follows by substituting back into (1):
$$\beta_s = \ln S_1 + K_sC_{s,1} \tag{3}$$

Two equations in two unknowns, solved by elimination — the same structure as fitting any two-parameter law to two data points.

## Worked example

*Antibody recovery by salting out.* Computed in Python.

**Given.** A pure IgA monoclonal antibody has solubility 770 µg mL⁻¹ in 1.4 M (NH₄)₂SO₄ and 29 µg mL⁻¹ in 3.0 M (NH₄)₂SO₄. A solution containing 180 g of pure antibody is treated for protein recovery using 2.5 M (NH₄)₂SO₄ in a total volume of 1000 L. What percentage of the antibody would precipitate?

**Step 1: check the regime.** Solubility *decreases* with increasing salt, so both points lie in the salting-out regime and the Cohn equation applies.

**Step 2: extract the constants.** From (2):
$$K_s = \frac{\ln(770/29)}{3.0-1.4} = \frac{3.279}{1.6} = 2.05\ \mathrm{M^{-1}}$$
From (3):
$$\beta_s = \ln 770 + 2.05\times1.4 = 6.65+2.87 = 9.52$$

**Step 3: solubility at the operating condition,** $C_s = 2.5$ M:
$$\ln S = 9.52-2.05\times2.5 = 4.39 \quad\Longrightarrow\quad S = 81\ \mathrm{\mu g\,mL^{-1}}$$

**Step 4: compare with the feed concentration.** 180 g in 1000 L is
$$\frac{180\ \mathrm{g}}{1000\ \mathrm{L}} = 180\ \mathrm{mg\,L^{-1}} = 180\ \mathrm{\mu g\,mL^{-1}}$$
Everything above the solubility limit precipitates:
$$180-81 = 99\ \mathrm{\mu g\,mL^{-1}}, \qquad \frac{99}{180} = 55\%$$

**55 % is very poor separation.** Nearly half the product is left dissolved and lost to the supernatant.

**Step 5: what would 99 % recovery require?** Only 1 % may remain dissolved, so $S = 1.8$ µg mL⁻¹. Rearranging (1):
$$C_s = \frac{\beta_s-\ln S}{K_s} = \frac{9.52-0.588}{2.05} = 4.36\ \mathrm{M}$$

**Compare with the solubility of the salt itself.** Saturated ammonium sulfate is about 4.1 M at 25 °C. The required 4.36 M is **above saturation**, so 99 % recovery is **not achievable with this salt at all** — the salt would precipitate before the protein did.

Intermediate targets are reachable: 90 % needs 3.2 M and 95 % needs 3.6 M, both within range.

**What this example teaches.** The exponential form cuts both ways. Solubility falls steeply with salt, which is why the method works; but recovering the last few percent requires salt concentrations that rise without bound as $S\to0$, since $C_s\propto-\ln S$. **Salting out is excellent for bulk recovery and hopeless for completeness** — which is exactly the role of a primary isolation step.

## Link to other topics

The Cohn equation has the same form as a Setschenow relation for gas solubility in electrolyte solutions, and for the same physical reason: added salt reduces the water available to solvate the solute, so $\ln$(solubility) falls linearly with salt concentration.

## Conclusion

Salting out precipitates proteins by depriving them of their solvation shell, with effectiveness ranked by the Hofmeister series. The Cohn equation, $\ln S = \beta_s - K_sC_s$, is fitted from two solubility measurements and then predicts recovery. For the IgA example, 2.5 M ammonium sulfate precipitates only 55 %, and 99 % would need 4.36 M — above the salt's own solubility. Section 44 covers the three other precipitation routes.

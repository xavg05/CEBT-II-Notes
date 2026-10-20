# Dissociative and competitive adsorption

## Overview

Assume the molecular Langmuir model. Dissociation changes the number of sites required by one gas molecule; competition changes the set of species sharing the site inventory.

## Intuition

Hydrogen dissociation requires two adjacent vacant sites. Their joint probability is approximately the square of the vacant fraction under random mixing. A competitor occupies space that would otherwise be available, so raising its pressure can reduce another species' coverage even if that species' own pressure remains unchanged.

## Derivation

For $\mathrm{H_2(g)}+2*\rightleftharpoons2\mathrm{H*}$, let $\theta$ denote the fraction of sites occupied by hydrogen atoms and $P$ hydrogen partial pressure. Rates of molecular adsorption and recombinative desorption are proportional to $P(1-\theta)^2$ and $\theta^2$, respectively. Equilibrium gives

$$k_aP(1-\theta)^2=k_d\theta^2.$$

With $K=k_a/k_d$ and the nonnegative physical root, $\sqrt{KP}(1-\theta)=\theta$. Therefore

$$\theta=\frac{\sqrt{KP}}{1+\sqrt{KP}}.$$

At low pressure, atom coverage varies as $P^{1/2}$, not as $P$. At saturation every available site is occupied, while the number of adsorbed hydrogen molecules equivalent to that loading is half the atom count. If rates are expressed as atoms rather than molecules, include the stoichiometric factor consistently on both sides.

For molecular A and B sharing equivalent sites, define vacant fraction $\theta_*$ and occupied fractions $\theta_A,\theta_B$. Each adsorption equilibrium gives $\theta_A=K_AP_A\theta_*$ and $\theta_B=K_BP_B\theta_*$. Site conservation is $\theta_*+\theta_A+\theta_B=1$. Substitution gives

$$\theta_*[1+K_AP_A+K_BP_B]=1.$$

Thus

$$\theta_*=\frac1D,\quad\theta_A=\frac{K_AP_A}D,\quad\theta_B=\frac{K_BP_B}D,
\qquad D=1+K_AP_A+K_BP_B.$$

Any molecularly adsorbed product adds its own $K_PP_P$ term to $D$. If B dissociates into two identical atoms, the equilibrium relation becomes $\theta_B=\sqrt{K_BP_B}\theta_*$; substituting this into the same atom-site inventory replaces $K_BP_B$ by its square root. Derive the relation and inventory before combining them: species requiring different numbers or types of sites can need more complicated balances.

## Motivation and explanation

The square root appears when equilibrium balances a two-site adsorption event against recombination of two adsorbed atoms. Taking the physical root converts a relation between pair probabilities into one between occupied and vacant fractions. It does not mean that a hydrogen molecule occupies half a site; each molecule supplies two atoms and those atoms occupy two sites.

In the molecular mixture, dividing each occupancy weight by the same $D$ enforces one shared inventory. Adding B changes that normalisation, so it lowers both the vacant fraction and A coverage while A pressure is held fixed. Separate denominators would remove this displacement mechanism and describe a different physical surface. The worked comparison consequently distinguishes competition for capacity from a chemical reaction between A and B.

In competitive adsorption, $\theta_A/\theta_B=K_AP_A/(K_BP_B)$ for molecular species. Abundant weakly adsorbing material can outcompete dilute strongly adsorbing material. A chemically inert species may therefore inhibit a reaction without appearing in its stoichiometry.

If A and B occupy separate populations of sites, write a separate inventory for each. Then $\theta_A=K_AP_A/(1+K_AP_A)$ and $\theta_B=K_BP_B/(1+K_BP_B)$ can hold independently. Such noncompetitive adsorption is plausible on heterogeneous oxide surfaces with metal centres, oxygen vacancies and hydroxyl groups. It should not be assumed merely to simplify a rate law.

## Link to other topics

Langmuir–Hinshelwood reaction requires the simultaneous presence of adsorbed reagents. Competition can make its rate fall as one reagent's pressure rises.

## Conclusion

Derive adsorption relations for each species, then impose the correct site inventory. The resulting denominator encodes both vacancy and inhibition.

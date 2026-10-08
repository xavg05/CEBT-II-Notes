# Section 11: Thermodynamic consistency and the one-constant Margules model

## Overview

An activity-coefficient model is an empirical function $\gamma_i(T,x)$, but it is not free. The Gibbs–Duhem equation ties the activity coefficients of a mixture together, and a model that violates it is **thermodynamically inconsistent**. This note:
- writes Gibbs–Duhem in terms of $\gamma_i$;
- shows that deriving every $\gamma_i$ from one excess-Gibbs-energy function guarantees consistency, and proves it for any binary;
- builds the simplest such model, the one-constant Margules equation, and finds what it predicts and where it fails.

*Assumed:* $\mu_i = \underline{G}_i + RT\ln x_i + RT\ln\gamma_i$ and $RT\ln\gamma_i = \partial(n\underline{G}^{ex})/\partial n_i$ (Section 10); $\sum n_i\,d\mu_i = 0$ at constant $T$, $P$ (Section 04).

## Intuition

Gibbs–Duhem says that, at fixed $T$ and $P$, the chemical potentials of a binary cannot all rise together as the composition changes. If adding component 1 makes component 1's environment less ideal, it must make component 2's environment more ideal, weighted by the amounts present.

So you cannot pick $\gamma_1(x)$ and $\gamma_2(x)$ independently. The way round this is to model the one mixture-level quantity, $\underline{G}^{ex}(x)$, and obtain both $\gamma$'s from it by differentiation, as partial molar quantities. Then they automatically fit together.

The simplest physically sensible $\underline{G}^{ex}$ is proportional to $x_1x_2$. In a randomly mixed liquid, the fraction of neighbour contacts that are between unlike molecules is proportional to $x_1x_2$. If each unlike contact costs (or gains) a fixed amount of energy, the excess Gibbs energy follows that product. This picture ignores non-random arrangement and size differences; later models (Wilson, NRTL, UNIQUAC) add them.

## Derivation

**Step 1: Gibbs–Duhem in terms of $\gamma$.** At constant $T$, $P$ in a binary, $n_1\,d\mu_1 + n_2\,d\mu_2 = 0$. Substitute $d\mu_i = RT\,d\ln x_i + RT\,d\ln\gamma_i$ ($\underline{G}_i$ is constant at fixed $T$, $P$), and divide by $nRT$:

$$x_1\,d\ln x_1 + x_2\,d\ln x_2 + x_1\,d\ln\gamma_1 + x_2\,d\ln\gamma_2 = 0$$

**Step 2: the ideal terms cancel.** $x_i\,d\ln x_i = dx_i$, and $dx_1 + dx_2 = 0$ because the mole fractions sum to 1. Hence

$$x_1\,d\ln\gamma_1 + x_2\,d\ln\gamma_2 = 0 \qquad (\text{constant } T, P) \tag{1}$$

A model must also give $\underline{G}^{ex} = 0$ for each pure component:

$$\underline{G}^{ex}(x_1 = 0) = \underline{G}^{ex}(x_1 = 1) = 0 \tag{2}$$

**Step 3: activity coefficients from any $\underline{G}^{ex}(x_1)$.** Write $n\underline{G}^{ex} = n\,g(x_1)$ with $x_1 = n_1/n$. At fixed $n_2$, $\partial n/\partial n_1 = 1$ and $\partial x_1/\partial n_1 = x_2/n$. Differentiate:

$$RT\ln\gamma_1 = g + x_2\,\frac{dg}{dx_1}, \qquad RT\ln\gamma_2 = g - x_1\,\frac{dg}{dx_1} \tag{3}$$

(the second by symmetry, since $\partial x_1/\partial n_2 = -x_1/n$). Geometrically, these are the intercepts at $x_1 = 1$ and $x_1 = 0$ of the tangent to the $\underline{G}^{ex}$ curve: the tangent construction for partial molar quantities.

**Step 4: any such model satisfies (1).** Differentiate (3): $d(RT\ln\gamma_1)/dx_1 = g' - g' + x_2g'' = x_2g''$ and $d(RT\ln\gamma_2)/dx_1 = -x_1g''$. Then

$$x_1(x_2g'') + x_2(-x_1g'') = 0$$

for every function $g$. *This is why models are always built from $\underline{G}^{ex}$:* consistency comes for free.

**Step 5: one-constant Margules.** Choose

$$\underline{G}^{ex} = A\,x_1x_2 \tag{4}$$

where $A$ is a function of $T$ only, fitted to data. It satisfies (2). With $g = Ax_1(1-x_1)$, $g' = A(1-2x_1)$, and (3) gives

$$RT\ln\gamma_1 = A\,x_2^2, \qquad RT\ln\gamma_2 = A\,x_1^2 \tag{5}$$

*Check:* $Ax_1x_2 + x_2A(1-2x_1) = Ax_2(x_1 + 1 - 2x_1) = Ax_2^2$. ✓

**Step 6: infinite dilution.** Setting $x_1\to 0$ in (5):

$$\gamma_1^{\infty} = \gamma_2^{\infty} = \exp\!\left(\frac{A}{RT}\right) \tag{6}$$

## Motivation and explanation

**Symmetry.** Swapping $x_1$ and $x_2$ leaves (4) unchanged, so the two $\gamma$ curves are mirror images that cross at $x_1 = 0.5$. That is fine for molecules of similar size and shape (e.g. oxygen and argon). It is wrong whenever the two infinite-dilution behaviours differ, which is the usual case.

**Gibbs–Duhem near a pure component.** From (1), $d\ln\gamma_1 = -(x_2/x_1)\,d\ln\gamma_2$. As $x_1\to 1$ the factor $x_2/x_1\to 0$, so $\gamma_1$ approaches 1 with zero slope. A nearly pure component obeys Raoult's law almost exactly, while the dilute one deviates most. Model (5) shows this: $\ln\gamma_1 \propto x_2^2$ is flat at $x_2 = 0$.

**Meaning of $A$.**
- $A > 0$: positive deviation, $\gamma > 1$ (unlike contacts unfavourable).
- $A < 0$: negative deviation.
- The size of $A/RT$ sets how non-ideal the mixture is.

Later sections show that a large positive $A/RT$ makes $\Delta\underline{G}_{\mathrm{mix}}$ non-convex, so the liquid splits into two phases. Because $A$ depends on $T$, the same mixture can be miscible at one temperature and split at another.

**Limits of validity.** Consistent does not mean accurate. The one-constant model has one parameter, is symmetric, and is reliable only for simple, similar molecules.

## Worked example

**Problem.** For a binary with $A/RT = 1$, find $\gamma_1$ and $\gamma_2$ across the composition range, and check Gibbs–Duhem at $x_1 = 0.5$.

**Values from (5).**

| $x_1$ | 0 | 0.2 | 0.5 | 0.8 | 1 |
|---|---|---|---|---|---|
| $\gamma_1 = e^{x_2^2}$ | 2.718 | 1.896 | 1.284 | 1.041 | 1 |
| $\gamma_2 = e^{x_1^2}$ | 1 | 1.041 | 1.284 | 1.896 | 2.718 |

![Activity coefficients from the one-constant Margules model with A/RT = 1: mirror-image curves crossing at x1 = 0.5, each reaching e ≈ 2.72 at infinite dilution](figs/ET-11-margules-one-constant-gamma.png)

**Gibbs–Duhem check at $x_1 = 0.5$.** $d\ln\gamma_1/dx_1 = -2(A/RT)x_2 = -1$ and $d\ln\gamma_2/dx_1 = 2(A/RT)x_1 = +1$. Then $0.5(-1) + 0.5(+1) = 0$. ✓

**Interpretation.** Each component is 2.7 times "more eager to escape" when infinitely dilute than in an ideal mixture, but only 4 % more at $x = 0.8$. In a distillation, this means the dilute component is much more volatile than Raoult's law predicts, which matters most at the ends of a column, where products are nearly pure.

## Link to other topics

Equation (3) and the requirement to start from $\underline{G}^{ex}$ underpin every activity-coefficient model in the course, from van Laar to UNIQUAC. The same Gibbs–Duhem relation (1) is used later as a consistency test on measured vapour–liquid equilibrium data.

## Conclusion

Gibbs–Duhem forces $x_1\,d\ln\gamma_1 + x_2\,d\ln\gamma_2 = 0$, and any model that obtains both $\gamma$'s by differentiating a single $\underline{G}^{ex}(x)$ satisfies it automatically. The simplest choice, $\underline{G}^{ex} = Ax_1x_2$, gives $RT\ln\gamma_i = Ax_j^2$: consistent and easy to use, but symmetric. The next section relaxes the symmetry, shows where model parameters come from, and extends the models to mixtures of more than two components.

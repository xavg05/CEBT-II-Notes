# Independent RE/PDC teaching-recovery review, 22 October 2026

Reviewer: Codex SEP recovery agent. Review-only scope: historical RE-01–06, RE-S3–S6 and PDC-01–22. Concurrent new RE solids production was not edited or used.

Read the recovery script, current canonical additions, their surrounding equations and the corrected historical worked-example material. Reviewed eight RE additions and twenty PDC additions, and the recorded reasons for leaving already-covered material unchanged.

## Findings requiring owner correction

1. **PDC-11 normalised damping figure commentary.** The new statement “The common endpoint measures gain” is misleading. The vertical axis is gain-normalised, so it removes gain; the zero-damping curve shown does not converge to an endpoint at all. The visually inspected figure has a dashed unity reference and an undamped oscillation from zero to two. State that positive damping makes the response approach the normalised unity reference, whereas zero damping oscillates indefinitely; the comparison isolates response shape after normalisation.
2. **RE-S3-04 surviving reference.** “The worked results compare those model choices” still points to removed numerical results. The recovered general expressions now support the distinction, so refer to “these expressions” or the two parameter comparisons instead.

No further material science or algebra findings in the recovered content. Both findings are **closed** by inspection of the current canonical text: PDC-11 correctly says the axis divides by unit-step gain, positive damping approaches one, and zero damping has no settled endpoint; RE-S3-04 now says “These expressions compare those model choices”. Independent scientific content review **PASS**.

## Independent derivation and numerical checks

- RE-02: separating the first-order PFR balance and evaluating the well-mixed CSTR exit-rate balance gives the recovered logarithmic and rational space times. At conversion 0.8, Python gives their ratio **2.4853397382384474**.
- RE-03: expanding-gas concentration inserts $(1+\epsilon X)$ into both sizing equations. Splitting its PFR integrand gives $(1+\epsilon)/(1-X)-\epsilon$. Historical label **(9)** belongs to exactly this integrated result; no surviving label needs renumbering. The constant-flow limit and positive-expansion interpretation are correct.
- RE-04: dividing the adiabatic temperature gradient by $dX_A/dV=(-\nu_A)r/F_{A0}$ gives the recovered stoichiometric factor. Historical label **(12)** was the special case $\nu_A=-1$ of the same temperature–conversion result. Heat-capacity flow has units W/K, so the conversion derivative and integrated temperature rise are dimensionally correct.
- RE-06: independently applying the PFR map $c/(1+c)$ and positive CSTR root gives outlet concentrations **0.3660254037844386** and **0.38196601125010515**, and conversions **0.6339745962155614** and **0.6180339887498949**. Convolution with the deterministic transit shifts the exponential RTD in either order, so the same-RTD/nonlinear-conversion conclusion is valid.
- RE-S3-04: fixed tank count versus tank count and space time scaling together produce the stated different length/time comparisons. The effective-rate, wetting and hydraulic qualifications are retained.
- RE-S5-01: the specified shared-site Langmuir–Hinshelwood form admits a rate maximum as A blocks B; the specified gas-A Eley–Rideal form does not introduce A site blocking. The inference is explicitly non-unique.
- RE-S6-04: direct Python evaluation of the Arrhenius ratio gives **1.209891230522002**. The text correctly distinguishes sensitivity from an attained pellet temperature.
- PDC-01–09: heat-flow compensation, inventory/measurement roles, coolant closure, equal initial step slopes, weighted finite-pulse concentration, sequential tank–sensor storage, enthalpy/internal-energy distinction, restoration of absolute baseline and first-order normalisation all agree with the surrounding balances. The fraction and settling formulas are valid under the stated stable single-lag model.
- PDC-11–12: passive times 20 and 80 s give **40.0 s** and **1.25**, and poles −0.05 and −0.0125 per second. The critical response at one time constant is correctly $1-2/e$; damping normalisation needs the correction above.
- PDC-14–16: whole-transient cancellation requires identical lags and synchronous commands; the A+B conservation check follows by cancelling reaction; boiler heat/feed matching cancels inventory drift and converting coefficient denominators from kW inputs to W inputs divides numerical heat-column coefficients by 1000.
- PDC-17: independently transformed the proposed impulse response. Its Laplace form is $1/(34s)-1/[50(s+2)]-1/[100(s+1)]-1/[20(s+1)^2]+(s-2)/\{1700[(s-1)^2+16]\}$. This equals the stated product denominator; Python `Fraction` gives exact equality at four rational arguments. Product expansion agrees with the stated sixth-degree polynomial. The sine coefficient follows from $s-2=(s-1)-1$, so the inverse term is $e^t[\cos4t-(1/4)\sin4t]/1700$. The integrator, repeated-pole and growing complex-pair interpretations are correct for an impulse.
- PDC-18–21: reversal occurs at **0.4054651081081644 s**, with minimum **−0.33333333333333326**; the unstable-final-value counterexample is correct; the equilibrium tangent matches the local dynamic gain; square-root outflow gives local and nonlinear final levels 2 and 2.25 m.
- PDC-22: independent Python gives cascade fractions **0.08030139707139416** and **0.5768099188731565**, linear final composition **4.34416%** and exact mixed-feed composition **4.342629482071712%**. Individual and cascade time constants, endpoint normalisation and percentage-point conventions are correctly distinguished.

This review covers the scientific content and contextual integration of the additions. Publication rendering, parity, source hashes and portable-package checks remain the coordinating author's separate validation.

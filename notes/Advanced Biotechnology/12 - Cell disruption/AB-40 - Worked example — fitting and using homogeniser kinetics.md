[Previous](<AB-39 - Mechanical cell disruption and release kinetics.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-41 - Non-mechanical cell disruption.md>)

<!-- note-content:start -->
# Section 40: Worked example — fitting and using homogeniser kinetics

## Intuition

The model has two unknowns multiplied together inside an exponential, which cannot be read off directly. The standard route is to linearise twice.

First, at **fixed pressure**, equation (72) is linear in $`N`$ through the origin, so the slope of $`\ln[R_{\max}/(R_{\max}-R)]`$ against $`N`$ gives the product $`kp^{\,a}`$ for that pressure. Doing this for each pressure gives one slope per pressure.

Second, taking logarithms of those slopes, $`\ln(kp^{\,a}) = \ln k + a\ln p`$, which is linear in $`\ln p`$. The gradient is $`a`$ and the intercept is $`\ln k`$.

Two straight-line fits, each extracting one constant. This is the general recipe whenever a power law sits inside an exponential.

## Motivation and explanation

**Why the two-stage fit is the right approach.** Fitting $`k`$ and $`a`$ simultaneously to all 29 data points by non-linear regression would also work, but the staged version is better practice: the first stage *tests* the model (do the lines pass through the origin and stay straight?) before the second stage extracts parameters. A curved line at one pressure would reveal a failure of first-order kinetics that a global fit would silently absorb into the parameters.

**What $`a = 2.37`$ means in design terms.** Since $`a > 1`$, pressure is a stronger lever than passes, as Section 39 predicted. Quantitatively, from (72):
- doubling $`N`$ doubles $`\ln[R_{\max}/(R_{\max}-R)]`$;
- doubling $`p`$ multiplies it by $`2^{2.37} = 5.2`$.

**Doubling pressure multiplies the effective pass count by about 5.2** in the fitted model: one pass at doubled pressure has the same predicted release as about 5.2 passes at the original pressure. This conditional comparison does not justify extrapolating the 200–550 $`\mathrm{kg}_f`$ cm⁻² fit to 1500–2500 bar.

**The trade-off that the model does not contain.** Higher pressure means more energy dissipated as heat per pass, so more cooling duty and more risk of denaturing the product — and the equipment must be rated for it. Fewer passes means less total residence time with released proteases. The model gives the disruption; the choice between the two routes depends on product stability and capital cost, which it says nothing about.

**Limits of the extrapolation.** The fit covers 200–550 $`\mathrm{kg}_f`$ cm⁻² and 1–6 passes. Part (b) extrapolates slightly in pressure, which is acceptable. Extrapolating to much higher pressure would not be: cavitation and temperature rise change the mechanism, and $`R_{\max}`$ itself may fall as the released protein is damaged.

## Link to other topics

The two-stage linearisation — hold one variable, fit the other, then fit the parameters of that fit — is the standard way to resolve a rate law of the form $`r = kC_A^{\alpha}C_B^{\beta}`$ from kinetic data, and the reasoning is identical: isolate one dependence at a time.

## Summary

Converting the data to $`\ln[R_{\max}/(R_{\max}-R)]`$ linearises the release law in $`N`$; the slopes then linearise in $`\ln p`$, giving $`a = 2.37`$ and $`k = 1.73\times10^{-7}`$ with $`R^2 = 0.9994`$. Five passes reach 80 % release at 460 $`\mathrm{kg}_f`$ cm⁻², and 570 $`\mathrm{kg}_f`$ cm⁻² reaches 70 % in two.
<!-- note-content:end -->

[Previous](<AB-39 - Mechanical cell disruption and release kinetics.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-41 - Non-mechanical cell disruption.md>)

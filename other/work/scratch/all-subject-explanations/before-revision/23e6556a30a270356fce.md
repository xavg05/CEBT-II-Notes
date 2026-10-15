[Previous](<AB-39 - Mechanical cell disruption and release kinetics.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-41 - Non-mechanical cell disruption.md>)

<!-- note-content:start -->
# Section 40: Worked example — fitting and using homogeniser kinetics

## Intuition

The model has two unknowns multiplied together inside an exponential, which cannot be read off directly. The standard route is to linearise twice.

First, at **fixed pressure**, equation (72) is linear in $`N`$ through the origin, so the slope of $`\ln[R_{\max}/(R_{\max}-R)]`$ against $`N`$ gives the product $`kp^{\,a}`$ for that pressure. Doing this for each pressure gives one slope per pressure.

Second, taking logarithms of those slopes, $`\ln(kp^{\,a}) = \ln k + a\ln p`$, which is linear in $`\ln p`$. The gradient is $`a`$ and the intercept is $`\ln k`$.

Two straight-line fits, each extracting one constant. This is the general recipe whenever a power law sits inside an exponential.

## Worked example

**Problem.** A production strain of *E. coli* is disrupted at 5 °C in a Gaulin homogeniser between 200 and 550 kg$`_f`$ cm⁻². Percentage protein release $`R/R_{\max}`$ as a function of the number of passes is:

| Passes $`N`$ | 200 | 300 | 400 | 500 | 550 |
|---|---|---|---|---|---|
| 1 | 5.0 | 13.5 | 23.3 | 36.0 | 42.0 |
| 2 | 9.5 | 23.5 | 40.0 | 58.5 | 66.0 |
| 3 | 14.0 | 33.5 | 52.5 | 75.0 | 83.7 |
| 4 | 18.0 | 43.0 | 66.6 | 82.5 | 88.5 |
| 5 | 22.0 | 47.5 | 73.0 | 88.5 | 94.5 |
| 6 | 26.0 | 55.0 | 79.5 | 91.3 | — |

(% protein release; pressure in kg$`_f`$ cm⁻².)

**(a)** How many passes are required for 80 % release at 460 kg$`_f`$ cm⁻²?
**(b)** What pressure delivers 70 % recovery in only two passes?

All numbers below were computed in Python.

### Step 1: convert the data

The table gives $`R/R_{\max}`$, but the model needs $`\ln[R_{\max}/(R_{\max}-R)]`$. Dividing numerator and denominator by $`R_{\max}`$:

**Equation (74)**

```math
\ln\!\left(\frac{R_{\max}}{R_{\max}-R}\right) = \ln\!\left(\frac{1}{1-R/R_{\max}}\right)
```


So 42.0 % becomes $`\ln[1/(1-0.42)] = 0.54`$.

### Step 2: slope at each pressure

![Plot of ln(R_max/(R_max − R)) against N for each pressure, giving a family of straight lines through the origin with slope kp^a](../figs/AB-40-fit-plot.png)

Plotting the converted data against $`N`$ for each pressure gives straight lines through the origin, confirming the first-order form. Their slopes are $`kp^{\,a}`$:

| $`p`$ (kg$`_f`$ cm⁻²) | 200 | 300 | 400 | 500 | 550 |
|---|---|---|---|---|---|
| slope $`kp^{\,a}`$ | 0.0500 | 0.1337 | 0.2633 | 0.4264 | 0.5691 |

### Step 3: extract $`a`$ and $`k`$

Taking logarithms, $`\ln(kp^{\,a}) = \ln k + a\ln p`$. A straight-line fit of $`\ln(\text{slope})`$ against $`\ln p`$ gives

```math
a = 2.37420, \qquad k = 1.73301\times10^{-7}\ (\mathrm{kg_f\,cm^{-2}})^{-a}
```

with $`R^2 = 0.9994`$ — the power law holds well across the range.

**Check.** Predicted release at $`p = 550`$, $`N = 5`$ is 93.8 % against 94.5 % measured; at $`p = 200`$, $`N = 6`$ it is 26.1 % against 26.0 %. The fit reproduces both ends of the data.

### Step 4: (a) passes for 80 % at 460 kg$`_f`$ cm⁻²

Rearranging (72) of Section 39 for $`N`$:

```math
N = \frac{1}{kp^{\,a}}\ln\!\left(\frac{1}{1-R/R_{\max}}\right) = \frac{1}{1.73301\times10^{-7}\times460^{2.37420}}\ln\!\left(\frac{1}{1-0.8}\right) = 4.4
```


Passes are whole numbers and 4.4 would fall short, so **$`N = 5`$**.

### Step 5: (b) pressure for 70 % in two passes

Rearranging for $`p`$:

```math
p = \left[\frac{1}{Nk}\ln\!\left(\frac{1}{1-R/R_{\max}}\right)\right]^{1/a} = \left[\frac{\ln(1/0.3)}{2\times1.73301\times10^{-7}}\right]^{1/2.37420} = 570\ \mathrm{kg_f\,cm^{-2}}
```


This is just above the 550 kg$`_f`$ cm⁻² at which data were taken, so it is a modest extrapolation and reasonable — but it would need checking against the machine's pressure rating.

## Motivation and explanation

**Why the two-stage fit is the right approach.** Fitting $`k`$ and $`a`$ simultaneously to all 29 data points by non-linear regression would also work, but the staged version is better practice: the first stage *tests* the model (do the lines pass through the origin and stay straight?) before the second stage extracts parameters. A curved line at one pressure would reveal a failure of first-order kinetics that a global fit would silently absorb into the parameters.

**What $`a = 2.37`$ means in design terms.** Since $`a > 1`$, pressure is a stronger lever than passes, as Section 39 predicted. Quantitatively, from (72):
- doubling $`N`$ doubles $`\ln[R_{\max}/(R_{\max}-R)]`$;
- doubling $`p`$ multiplies it by $`2^{2.37} = 5.2`$.

**Doubling pressure multiplies the effective pass count by about 5.2** in the fitted model: one pass at doubled pressure has the same predicted release as about 5.2 passes at the original pressure. This conditional comparison does not justify extrapolating the 200–550 kg$`_f`$ cm⁻² fit to 1500–2500 bar.

**The trade-off that the model does not contain.** Higher pressure means more energy dissipated as heat per pass, so more cooling duty and more risk of denaturing the product — and the equipment must be rated for it. Fewer passes means less total residence time with released proteases. The model gives the disruption; the choice between the two routes depends on product stability and capital cost, which it says nothing about.

**Limits of the extrapolation.** The fit covers 200–550 kg$`_f`$ cm⁻² and 1–6 passes. Part (b) extrapolates slightly in pressure, which is acceptable. Extrapolating to much higher pressure would not be: cavitation and temperature rise change the mechanism, and $`R_{\max}`$ itself may fall as the released protein is damaged.

## Link to other topics

The two-stage linearisation — hold one variable, fit the other, then fit the parameters of that fit — is the standard way to resolve a rate law of the form $`r = kC_A^{\alpha}C_B^{\beta}`$ from kinetic data, and the reasoning is identical: isolate one dependence at a time.

## Summary

Converting the data to $`\ln[R_{\max}/(R_{\max}-R)]`$ linearises the release law in $`N`$; the slopes then linearise in $`\ln p`$, giving $`a = 2.37`$ and $`k = 1.73\times10^{-7}`$ with $`R^2 = 0.9994`$. Five passes reach 80 % release at 460 kg$`_f`$ cm⁻², and 570 kg$`_f`$ cm⁻² reaches 70 % in two.
<!-- note-content:end -->

[Previous](<AB-39 - Mechanical cell disruption and release kinetics.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-41 - Non-mechanical cell disruption.md>)

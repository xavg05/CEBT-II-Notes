# Gene regulation and synthetic circuits — reading 15.4

[Previous](15-03-gene-regulation-and-synthetic-circuits.md) · [Subject index](README.md) · [Next](15-05-gene-regulation-and-synthetic-circuits.md)

<!-- reading-content:start -->
## Section 51: Stochastic gene expression and noise

### Intuition

A low-copy transcription factor finds an operator by diffusion and stochastic binding. One promoter therefore switches between inactive and active states even under fixed conditions. During an active interval, several transcripts can be made; each transcript can yield several proteins before being degraded. Long-lived proteins integrate these upstream events and smooth fast fluctuations.

![Promoter switching propagates through mRNA and protein trajectories](figs/AB-51-expression-trajectories.png)

*Analogy:* two printers sharing a power supply can both speed up or slow down together, but their individual paper-feed events differ. Two genetic reporters similarly share cellular resources while undergoing separate expression events. The limit is that reporters can themselves compete for those resources, breaking the assumed independence.

**Intrinsic noise** is variation remaining when the relevant shared cellular state is fixed. **Extrinsic noise** is variation transmitted from that shared state, such as polymerase abundance, growth, regulator concentration or gene dosage. These labels depend on the system boundary: stochastic promoter switching is intrinsic to a complete expression model, but is an upstream fluctuating input when analysing only mRNA birth and death.

### Derivation

**1. Birth and death set a baseline.** Let mRNA be made at constant rate $`k_m`$ (copies/min) and each molecule disappear at rate $`\lambda_m`$ (per min). A birth changes $`m`$ by $`+1`$ and a death by $`-1`$, with total death rate $`\lambda_m m`$. Taking expected changes gives


```math
\frac{d\langle m\rangle}{dt}=k_m-\lambda_m\langle m\rangle,
\qquad \overline m=\frac{k_m}{\lambda_m}.\tag{107}
```


A bar denotes a stationary mean. For the second moment, the changes in $`m^2`$ are $`(m+1)^2-m^2=2m+1`$ and $`(m-1)^2-m^2=-2m+1`$. Multiply each by its event rate and average:


```math
\frac{d\langle m^2\rangle}{dt}=k_m(2\langle m\rangle+1)
+\lambda_m[-2\langle m^2\rangle+\langle m\rangle].\tag{108}
```


At stationarity substitute $`k_m=\lambda_m\overline m`$, set (108) to zero, and divide by $`2\lambda_m`$. This gives $`\langle m^2\rangle=\overline m^2+\overline m`$, hence


```math
V_m=\overline m,\qquad \mathrm{CV}_m^2=\frac{V_m}{\overline m^2}=\frac{1}{\overline m}.\tag{109}
```


Here $`V_m`$ is variance, and coefficient of variation $`\mathrm{CV}=\sigma/\mu`$ divides standard deviation $`\sigma`$ by mean $`\mu`$. The full stationary birth–death distribution is Poisson. This baseline requires independent single-molecule births and first-order deaths; bursts and fluctuating rates add variance.

**2. Add a switching promoter.** One promoter has $`g=0`$ (OFF) or $`g=1`$ (ON), with switching rates $`k_{\mathrm{on}}`$ and $`k_{\mathrm{off}}`$. Define $`a=k_{\mathrm{on}}+k_{\mathrm{off}}`$ and correlation time $`\tau_g=1/a`$. The mean obeys $`d\langle g\rangle/dt=k_{\mathrm{on}}-a\langle g\rangle`$, so


```math
q\equiv P_{\mathrm{on}}=\overline g=\frac{k_{\mathrm{on}}}{a},\qquad
V_g=q(1-q),\qquad \frac{V_g}{\overline g^2}=\frac{1-q}{q}.\tag{110}
```


*Reason:* $`g^2=g`$ for a binary variable. For $`N_g`$ independent identical promoters, $`\overline g=N_gq`$ and $`V_g=N_gq(1-q)`$, giving relative variance $`(1-q)/\overline g`$.

Let transcription occur at rate $`k_mg`$ and define $`\tau_m=1/\lambda_m`$. Equation (107) becomes $`\overline m=k_mq/\lambda_m`$. Write $`C_{gm}=\mathrm{Cov}(g,m)`$. Promoter switching changes $`gm`$ through changes in $`g`$, and transcription changes it through changes in $`m`$. Specifically,


```math
\frac{d\langle gm\rangle}{dt}=k_{\mathrm{on}}\langle m\rangle
-(a+\lambda_m)\langle gm\rangle+k_m\langle g^2\rangle.\tag{111}
```


*Reason:* switching contributes $`k_{\mathrm{on}}\langle(1-g)m\rangle-k_{\mathrm{off}}\langle gm\rangle`$; transcription contributes $`k_m\langle g^2\rangle`$; death contributes $`-\lambda_m\langle gm\rangle`$. At stationarity subtract the product of the means, use $`k_{\mathrm{on}}=aq`$, and obtain $`C_{gm}=k_mV_g/(a+\lambda_m)`$.

Applying the squared-jump calculation (108) with production $`k_mg`$ gives $`V_m=\overline m+k_mC_{gm}/\lambda_m`$. Divide by $`\overline m^2`$, substitute $`C_{gm}`$ and $`\overline m`$, and cancel the production rates:


```math
\mathrm{CV}_m^2=\frac{1}{\overline m}
+\frac{1-q}{q}\frac{\tau_g}{\tau_g+\tau_m}.\tag{112}
```


*Reason:* $`\lambda_m/(a+\lambda_m)=\tau_g/(\tau_g+\tau_m)`$. The first term is transcript birth–death noise; the second is propagated promoter noise. Fast switching, $`\tau_g\ll\tau_m`$, is averaged away; slow switching is transmitted almost completely. For independent multiple promoters replace $`(1-q)/q`$ by $`(1-q)/\overline g`$.

**3. Add translation.** Let protein births occur at rate $`k_pm`$, where $`k_p`$ is proteins per transcript per min, and protein loss at rate $`\lambda_pp`$. Define $`\tau_p=1/\lambda_p`$, $`\overline p=k_p\overline m/\lambda_p`$, $`C_{gp}=\mathrm{Cov}(g,p)`$ and $`C_{mp}=\mathrm{Cov}(m,p)`$. The same event bookkeeping, after subtracting products of stationary means, gives


```math
C_{gp}=\frac{k_pC_{gm}}{a+\lambda_p},\qquad
C_{mp}=\frac{k_mC_{gp}+k_pV_m}{\lambda_m+\lambda_p},\qquad
V_p=\overline p+\frac{k_pC_{mp}}{\lambda_p}.\tag{113}
```


*Reason:* promoter switching and protein loss remove $`gp`$ covariance, while translation supplies $`k_pC_{gm}`$. Transcript and protein losses remove $`mp`$ covariance, while transcription and translation supply $`k_mC_{gp}`$ and $`k_pV_m`$. Protein births and deaths contribute the Poisson baseline $`\overline p`$ to its variance. No reaction changes both $`m`$ and $`p`$ at once: translation does not consume the transcript.

Insert $`V_m=\overline m+k_mC_{gm}/\lambda_m`$ into (113), and divide $`V_p`$ by $`\overline p^2`$. Before changing to lifetimes the result is


```math
\mathrm{CV}_p^2=\frac{1}{\overline p}
+\frac{\lambda_p}{\overline m(\lambda_m+\lambda_p)}
+\frac{1-q}{q}\frac{\lambda_m\lambda_p}{(a+\lambda_m)(\lambda_m+\lambda_p)}
\left(1+\frac{\lambda_m}{a+\lambda_p}\right).\tag{114}
```


*Reason:* the three contributions arise from protein births, transcript variance at fixed promoter input, and promoter variance. Substitute each $`\lambda=1/\tau`$ and $`a=1/\tau_g`$; combining the terms in parentheses gives the equivalent filtering form


```math
\mathrm{CV}_p^2=\frac{1}{\overline p}
+\frac{1}{\overline m}\frac{\tau_m}{\tau_m+\tau_p}
+\frac{1-q}{q}\frac{\tau_m}{\tau_m+\tau_p}
\frac{\tau_g}{\tau_g+\tau_p}
\frac{\tau_g+\tau_p+\tau_g\tau_p/\tau_m}{\tau_g+\tau_m}.\tag{115}
```


All ratios are dimensionless. With a fixed ON promoter the last term vanishes. With $`\tau_p\to0`$ at fixed means, the transcript and promoter contributions approach those in (112); with $`\tau_p\to\infty`$ fast upstream fluctuations are averaged away. These limiting comparisons hold means fixed by adjusting production; changing a lifetime alone also changes the mean.

**4. Two reporters distinguish common and independent fluctuations.** Let $`R`$ and $`G`$ be background-corrected reporter signals and $`\mu_R=\langle R\rangle`$, $`\mu_G=\langle G\rangle`$ their positive means. Normalise $`r=R/\mu_R`$ and $`s=G/\mu_G`$. If $`Z`$ represents the shared cellular state, assume both reporters have the same conditional mean $`h(Z)`$ and are independent conditional on $`Z`$. Write $`r=h+\epsilon_r`$ and $`s=h+\epsilon_s`$, with conditional zero-mean residuals of equal average variance $`v`$.

Taking variances and covariance gives $`\mathrm{Var}(r)=\mathrm{Var}(h)+v`$ and $`\mathrm{Cov}(r,s)=\mathrm{Var}(h)`$. Subtraction cancels $`h`$, and conditional independence gives $`\langle(r-s)^2\rangle=2v`$. Therefore


```math
\eta_{\mathrm{int}}^2=\frac{\langle(r-s)^2\rangle}{2},\qquad
\eta_{\mathrm{ext}}^2=\langle rs\rangle-1,\qquad
\eta_{\mathrm{tot}}^2=\frac{\mathrm{Var}(r)+\mathrm{Var}(s)}{2}
=\eta_{\mathrm{int}}^2+\eta_{\mathrm{ext}}^2.\tag{116}
```


Here $`\eta`$ denotes a dimensionless noise amplitude, equivalent to CV for a single matched reporter. For equal means $`\mu`$, intrinsic noise becomes $`\langle(R-G)^2\rangle/(2\mu^2)`$ and extrinsic noise $`\mathrm{Cov}(R,G)/\mu^2`$. Add **squared** amplitudes, not amplitudes.

### Motivation and explanation

Shared inputs elongate a reporter scatter cloud along the equal-signal diagonal; independent events widen it perpendicular to that line. Parallel width contains intrinsic variation too, so it cannot all be assigned to extrinsic noise: the covariance or subtraction in (116) is needed.

Stationarity alone does not imply ergodicity. Time averages agree with ensemble averages only if the process samples the relevant states, records are long enough, and population/lineage sampling is appropriate. Slow switching, changing environments, selection of fast growers and ageing can break that equivalence. Fluorescence additionally depends on maturation, bleaching, segmentation and measurement noise. Independent measurement noise inflates the intrinsic estimate; unequal reporter dynamics and competition violate the matched-independent-reporter model.

### Worked example

**A noisy cascade.** Choose $`k_{\mathrm{on}}=0.12`$, $`k_{\mathrm{off}}=0.18`$, $`\lambda_m=0.20`$ and $`\lambda_p=0.020\ \mathrm{min^{-1}}`$, with $`k_m=10`$ transcripts/min while ON and $`k_p=2`$ proteins per transcript per min. Python gives $`q=0.40`$, $`\tau_g=3.333\ \mathrm{min}`$, $`\tau_m=5.00\ \mathrm{min}`$ and $`\tau_p=50.0\ \mathrm{min}`$; the means are 20 transcripts and 2000 proteins.

Equation (112) gives $`\mathrm{CV}_m^2=0.0500+0.6000=0.6500`$, hence $`\mathrm{CV}_m=0.8062`$, compared with the constant-production Poisson baseline 0.2236. Equation (115) gives $`\mathrm{CV}_p^2=0.000500+0.004545+0.088636=0.093682`$, hence $`\mathrm{CV}_p=0.3061`$. Protein smooths the mRNA trajectory but retains appreciable upstream variation. Here promoter switching is part of the model's intrinsic stochasticity; its propagated term is not automatically the dual-reporter extrinsic component.

![Matched reporters and a scatter cloud dominated by shared variation](figs/AB-51-dual-reporter.png)

**Reporter calculation.** For a constructed population with mean signals both 100 units, variances both 225 units squared, and covariance 144 units squared, the mean squared difference is $`225+225-2(144)=162`$ units squared. Equation (116) gives $`\eta_{\mathrm{int}}=0.0900`$, $`\eta_{\mathrm{ext}}=0.1200`$ and $`\eta_{\mathrm{tot}}=0.1500`$. Extrinsic variation contributes more variance in this example. The figure's negative coordinates represent centred signal deviations, not negative molecular counts; its diagonal elongation suggests shared variation, without supplying precise numerical estimates.

### Link to other topics

Promoter occupancy becomes a probability distribution when binding events are resolved individually. The same production–loss mechanism gives both mean expression and variance, while feedback changes how these fluctuations propagate into downstream circuits.

### Summary

Low copy numbers make reaction timing consequential. A two-reporter experiment separates shared and independent variation only under explicit matching and independence assumptions; lifetime ratios determine which upstream fluctuations survive into protein abundance.
<!-- reading-content:end -->

[Previous](15-03-gene-regulation-and-synthetic-circuits.md) · [Subject index](README.md) · [Next](15-05-gene-regulation-and-synthetic-circuits.md)

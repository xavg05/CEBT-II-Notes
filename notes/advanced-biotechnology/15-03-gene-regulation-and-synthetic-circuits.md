# Gene regulation and synthetic circuits — reading 15.3

[Previous](15-02-gene-regulation-and-synthetic-circuits.md) · [Subject index](README.md) · [Next](15-04-gene-regulation-and-synthetic-circuits.md)

<!-- reading-content:start -->
## Section 50: Network motifs and autoregulation

### Intuition

A self-repressor initially leaves its promoter free, allowing rapid production. As it accumulates, it occupies the operator and reduces further transcription. A self-activator does the reverse: initial expression is weak, but accumulated activator recruits more RNA polymerase.

*Analogy:* NAR resembles a thermostatic heater that reduces power as the room warms; PAR resembles a microphone feeding its own amplified sound back into the input. The analogy ends at the molecular mechanism: proteins arrive at DNA randomly, production takes time, and the cell shares finite resources with other genes.

A **network motif** is a small wiring pattern enriched relative to a specified random-network model. Frequency alone does not establish either enrichment or biological function. For example, in a network snapshot with 424 nodes, 519 arrows and 40 self-arrows, uniformly choosing directed connections gives self-arrow probability $`1/424`$ and expected count $`519/424=1.224`$. The observed count is 32.68 times this expectation. This simple null ignores which nodes are transcription factors and their unequal degrees; a stronger test preserves those constraints. The snapshot contains 34 negative and six positive self-arrows.

### Derivation

**Promoter occupancy → Hill response.** Suppose an effective cooperative binding event has bound-to-free promoter probability ratio $`(R/K)^n`$, where $`R`$ is active regulator concentration, $`K`$ the half-occupancy concentration, and $`n`$ the Hill exponent. Normalising the free-state weight 1 and bound-state weight $`(R/K)^n`$ gives


**Equation (100)**

```math
P_{\mathrm{free}}=\frac{1}{1+(R/K)^n},\qquad P_{\mathrm{bound}}=\frac{(R/K)^n}{1+(R/K)^n}.
```


*Reason:* mutually exclusive state probabilities sum to one. For a literal all-or-none binding reaction, mass action supplies the ratio; otherwise $`n`$ is an effective fitted exponent, not necessarily a count of binding sites.

Let $`\beta`$ be the additional production rate when the promoter is fully active and $`b`$ its basal production rate, both in concentration/time. Production then has the forms


**Equation (101)**

```math
f_{\mathrm{NAR}}(x)=b+\frac{\beta}{1+(x/K)^n},\qquad f_{\mathrm{PAR}}(x)=b+\frac{\beta(x/K)^n}{1+(x/K)^n}.
```


*Reason:* repression permits transcription in the free state; activation permits the additional transcription in the bound state. Set $`R=x`$ only when concentration is proportional to active regulator abundance. Promoter equilibration and mRNA relaxation must be fast compared with changes in $`x`$.

For large $`n`$, repression approaches an ON/OFF rule: $`\beta`$ below $`K`$, zero above $`K`$, plus any basal rate. The finite Hill curve still has half activity at $`K`$; the discontinuous approximation does not specify a unique value there. It is useful for Boolean logic, but unreliable for calculating a derivative at the threshold. Two inputs that can each initiate production implement OR; allowing either input to make a common repressor gives a downstream NOR output, subject to threshold and leak limitations.

**Rate plots → stability and response.** Production minus removal gives


**Equation (102)**

```math
\frac{dx}{dt}=f(x)-\lambda x,\qquad f(x_{\mathrm{st}})=\lambda x_{\mathrm{st}}.
```


The vertical gap between the curves is the rate of movement along the concentration axis.

![Production and removal rate plots](figs/AB-50-autoregulation-rate-plots.png)

Put $`x=x_{\mathrm{st}}+\delta x`$. Taylor expansion gives $`f(x)=f(x_{\mathrm{st}})+f'(x_{\mathrm{st}})\delta x+O(\delta x^2)`$. Subtract the steady balance to cancel the constant terms:


**Equation (103)**

```math
\frac{d\delta x}{dt}\simeq-[\lambda-f'(x_{\mathrm{st}})]\delta x,
\quad \delta x(t)=\delta x(0)e^{-t/\tau_{\mathrm{eff}}},
\quad \tau_{\mathrm{eff}}=\frac{1}{\lambda-f'(x_{\mathrm{st}})}.
```


*Reason:* the local production slope changes how strongly a displacement restores the balance. Stability requires $`f'<\lambda`$. NAR has $`f'<0`$, giving faster local relaxation. Stable PAR with $`0<f'<\lambda`$ relaxes more slowly; $`f'>\lambda`$ makes the intersection unstable. A sufficiently sigmoid PAR curve can have two stable intersections separated by an unstable one, enabling memory and hysteresis. PAR alone does not guarantee bistability.

For constant production $`k`$ and $`x(0)=0`$, multiply $`\dot x+\lambda x=k`$ by $`e^{\lambda t}`$ and integrate:


**Equation (104)**

```math
e^{\lambda t}x=\frac{k}{\lambda}(e^{\lambda t}-1),\qquad
x=\frac{k}{\lambda}(1-e^{-\lambda t}),\qquad t_{1/2}=\frac{\ln2}{\lambda}.
```


*Reason:* the integrating factor turns the left side into one derivative; setting $`x`$ to half $`k/\lambda`$ then gives the rise-time. For dilution alone, $`\lambda=\ln2/T_d`$, where $`T_d`$ is doubling time, so this half-rise takes one generation. Comparisons of feedback circuits must match the final concentration; simply strengthening a constitutive promoter changes its endpoint.

**Rate plots → sensitivity.** Allow production to depend on a parameter $`u`$. Differentiate $`f(x_{\mathrm{st}},u)=\lambda x_{\mathrm{st}}`$ at fixed $`\lambda`$:


**Equation (105)**

```math
f_x\frac{dx_{\mathrm{st}}}{du}+f_u=\lambda\frac{dx_{\mathrm{st}}}{du},\qquad
\frac{dx_{\mathrm{st}}}{du}=\frac{f_u}{\lambda-f_x}.
```


*Reason:* the parameter both moves the production curve and changes the concentration at which it is evaluated. Subscripts indicate partial derivatives evaluated at the steady state. For no leak, $`f=\beta h(x)`$, define the dimensionless feedback strength $`L=-f_x/\lambda`$. Since $`f_\beta=f/\beta=\lambda x_{\mathrm{st}}/\beta`$,


**Equation (106)**

```math
\frac{d\ln x_{\mathrm{st}}}{d\ln\beta}=\frac{1}{1+L},\qquad
\frac{d\ln x_{\mathrm{st}}}{d\ln\lambda}=-\frac{1}{1+L}.
```


*Reason:* divide (105) by $`x_{\mathrm{st}}/\beta`$; for the second result differentiate the steady balance with respect to $`\lambda`$ instead. For no-leak NAR, differentiating (101) and using (102) gives $`L=n(x_{\mathrm{st}}/K)^n/[1+(x_{\mathrm{st}}/K)^n]`$.

### Motivation and explanation

![Negative autoregulation limits movement of the steady concentration](figs/AB-50-feedback-robustness.png)

A falling production curve makes shifts in production capacity or removal rate move the intersection less. Equations (105)–(106) concern small, slow perturbations; they do not prove suppression of all intrinsic noise or rapidly fluctuating inputs. Noise in the threshold $`K`$, strong expression burden, saturation and delayed repression can defeat this protection. A smooth one-variable autonomous balance can relax monotonically but cannot sustain an oscillation: molecular intermediates or delayed feedback must supply additional dynamics.

### Worked example

**Matched endpoint.** Choose $`K=x_{\mathrm{st}}=100\ \mathrm{nM}`$, $`n=2`$, $`b=0`$, and dilution doubling time $`T_d=30\ \mathrm{min}`$. Python gives $`\lambda=0.0231049\ \mathrm{min^{-1}}`$. At $`x=K`$, production is $`\beta/2`$, so (102) requires $`\beta=2\lambda K=4.62098\ \mathrm{nM\,min^{-1}}`$. Differentiating (101) at $`K`$ gives $`f'=-\beta/(2K)=-\lambda`$, hence $`L=1`$.

The local half-relaxation time is $`\ln2/(2\lambda)=15.00\ \mathrm{min}`$, versus $`30.00\ \mathrm{min}`$ without feedback. A slow 10% change in $`\beta`$ produces approximately a 5% change in $`x_{\mathrm{st}}`$ by (106). Integrating the full nonlinear balance from zero gives a half-rise of **13.89 min**. This differs from local half-relaxation because the initially unrepressed promoter produces faster than it does near the endpoint.

**Switching check.** For no-leak PAR with $`n=2`$, $`K=100\ \mathrm{nM}`$, $`\beta=4\ \mathrm{nM\,min^{-1}}`$ and $`\lambda=0.01\ \mathrm{min^{-1}}`$, (102) becomes $`x[\beta x/(K^2+x^2)-\lambda]=0`$. Nonzero roots satisfy $`\lambda x^2-\beta x+\lambda K^2=0`$. The quadratic formula gives $`x=[\beta\pm\sqrt{\beta^2-4\lambda^2K^2}]/(2\lambda)`$. Python finds stable endpoints at 0 and 373.21 nM, separated by the unstable 26.79 nM threshold. With exactly zero leak and zero protein, the deterministic circuit remains OFF; an external pulse must cross the threshold. Real basal transcription can start it spontaneously and can also remove bistability.

### Link to other topics

The Hill response extends promoter binding into a dynamical gene-expression model. Rate-plot slopes are the biological counterpart of local feedback gains in process control, while intrinsic expression fluctuations require a discrete reaction model.

### Summary

NAR creates a restoring production slope; PAR creates a reinforcing one. The slope at a steady balance determines local speed and sensitivity, and the shape of the full production curve determines whether switching is possible.
<!-- reading-content:end -->

[Previous](15-02-gene-regulation-and-synthetic-circuits.md) · [Subject index](README.md) · [Next](15-04-gene-regulation-and-synthetic-circuits.md)

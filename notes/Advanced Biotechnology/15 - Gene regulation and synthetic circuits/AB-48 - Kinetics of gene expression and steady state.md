[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-49 - Transcriptional regulation and the lac operon.md>)

<!-- note-content:start -->
# Section 48: Kinetics of gene expression and steady state

## Intuition

![Information passes from DNA through mRNA to protein](../figs/AB-48-expression-pathway.png)

RNA polymerase (RNAP) repeatedly makes messenger RNA (mRNA) from a gene. Ribosomes repeatedly translate each message: translation does not consume the mRNA. Ribonucleases destroy messages, while proteins can disappear through proteolysis or become distributed among an increasing number of cells as the population grows.

*Analogy:* a workshop copies instructions, and each copy supports repeated manufacture until discarded. Keeping more copies increases production. The analogy fails at dilution: an intact protein can become less abundant per cell without being destroyed, because the workshop population grows and divides.

A steady abundance is therefore a **dynamic balance**, with continual synthesis replacing losses. It is not chemical equilibrium. Cells express different subsets of their genes because unnecessary transcription and translation consume resources; the active subset depends on the environment, not on a fixed universal fraction.

## Derivation

### Production and loss

Let $`t`$ be time in minutes, $`m`$ the mean number of messages for one gene per cell, and $`p`$ the mean number of its protein molecules per cell. Take one effective gene copy per cell, constant growth conditions, unsaturated machinery and negligible synthesis delays. Let $`k_1`$ be the transcription rate in messages $`\mathrm{cell}^{-1}`$ $`\mathrm{min}^{-1}`$, and $`k_2`$ the translation rate in proteins $`\mathrm{message}^{-1}`$ $`\mathrm{min}^{-1}`$. For one gene copy, $`k_1`$ is numerically the rate per gene. Let $`\lambda_1`$ and $`\lambda_2`$ be the effective message and protein loss constants, both in $`\mathrm{min}^{-1}`$.

Over a short interval $`dt`$, synthesis adds $`k_1dt`$ messages and first-order loss removes $`\lambda_1m\,dt`$. Subtracting loss from production and dividing by $`dt`$ gives


**Equation (93)**

```math
\frac{dm}{dt}=k_1-\lambda_1m.
```


Each of the $`m`$ messages produces proteins at rate $`k_2`$, so total protein production is $`k_2m`$. Applying the same balance gives


**Equation (94)**

```math
\frac{dp}{dt}=k_2m-\lambda_2p.
```


The factor $`m`$ is essential: $`k_2`$ alone is a rate **per message**, not a rate per cell. Every term in (94) has units of proteins $`\mathrm{cell}^{-1}`$ $`\mathrm{min}^{-1}`$.

### Why dilution enters a loss constant

Let $`N`$ be the number of cells, $`P`$ the total number of the protein molecules in the population, $`\mu`$ the exponential population growth constant, and $`\delta_p`$ the intrinsic protein degradation constant. Then $`dN/dt=\mu N`$. Production by all cells is $`Nk_2m`$, so $`dP/dt=Nk_2m-\delta_pP`$. Since $`p=P/N`$, the quotient rule gives


**Equation (95)**

```math
\frac{dp}{dt}=\frac{1}{N}\frac{dP}{dt}-\frac{P}{N^2}\frac{dN}{dt}
=k_2m-\delta_pp-\mu p
=k_2m-(\delta_p+\mu)p.
```


Thus $`\lambda_2=\delta_p+\mu`$: the last term appears because the denominator grows. Applying the identical population balance to messages gives $`\lambda_1=\delta_m+\mu`$, where $`\delta_m`$ is their intrinsic degradation constant. This is a population mean approximation; molecule numbers in a single lineage jump at division rather than undergoing smooth dilution.

### Half-life and steady state

For a species of abundance $`n`$ after its production has stopped, $`dn/dt=-\lambda n`$. Separating variables gives $`dn/n=-\lambda\,dt`$. Integrating from initial abundance $`n_0`$ at $`t=0`$ yields $`\ln(n/n_0)=-\lambda t`$, hence $`n=n_0e^{-\lambda t}`$. At the half-life $`t_{1/2}`$, substitute $`n/n_0=1/2`$ and take natural logarithms:


**Equation (96)**

```math
-\ln2=-\lambda t_{1/2}
\quad\Rightarrow\quad \lambda=\frac{\ln2}{t_{1/2}}.
```


For a stable protein, $`\delta_p\simeq0`$, so its effective dilution half-life equals the population doubling time $`T_d`$: $`\mu=\ln2/T_d`$. This does not mean the protein is chemically degraded within that time.

At steady state, indicated by a superscript $`*`$, set the left-hand side of (93) to zero. Moving the loss term to the other side and dividing by $`\lambda_1`$ gives $`m^*=k_1/\lambda_1`$. Do the same in (94), then substitute this message abundance:


**Equation (97)**

```math
m^*=\frac{k_1}{\lambda_1},\qquad
p^*=\frac{k_2m^*}{\lambda_2}
=\frac{k_1k_2}{\lambda_1\lambda_2}.
```


To see how messages approach the balance, subtract $`m^*`$ from (93). For $`u=m-m^*`$, $`du/dt=-\lambda_1u`$, whose exponential solution above gives


**Equation (98)**

```math
m(t)=m^*+[m(0)-m^*]e^{-\lambda_1t}.
```


Starting from zero, $`m(t)=m^*(1-e^{-\lambda_1t})`$. At $`t_{1/2}`$ it has reached half its eventual value. Protein production still depends on this changing message pool, so protein accumulation is generally not a single exponential from switch-on.

Starting with no messages and no protein, transcription can begin immediately while protein production initially remains zero because there are no templates for translation yet. Protein production increases as messages accumulate. This produces a rounded start in the protein curve even though the model contains no explicit waiting-time delay. An inherited message pool would change that initial slope, so the initial condition matters as well as the two loss constants.

## Motivation and explanation

Longer message survival allows more templates to accumulate; longer protein survival allows more products to accumulate. This explains why the two loss constants multiply in the denominator of (97). With fixed losses, doubling transcription doubles both abundances, while changing translation affects protein abundance directly.

If production stops, abundance decays to zero when the corresponding loss constant is positive. If a species has no loss and positive production, it accumulates rather than reaching a finite steady state. The deterministic means also hide fluctuations, especially when message counts are small. Resource limitation, changing gene dosage, growth-dependent synthesis rates and feedback invalidate the constant-parameter approximation.

**Elongation speed is not initiation frequency.** A coding sequence of approximately 1,000 nucleotides takes about 33.3 s to transcribe at 30 nt $`\mathrm{s}^{-1}`$; ignoring the stop codon, translation of its approximately 333 amino acids at 10 amino acids $`\mathrm{s}^{-1}`$ also takes about 33.3 s. These transit times do not establish $`k_1`$ or $`k_2`$: several polymerases can occupy one gene and several ribosomes can occupy one message. Promoter initiation and the ribosome-binding site control the effective production rates.

## Link to other topics

These balances connect gene expression to the production and removal equations used in bioprocessing. Transcriptional regulation makes $`k_1`$ depend on signals and regulatory proteins, turning a constant-rate model into a gene regulatory network.

## Summary

An expression level records both production and survival. Keeping transcription per gene, translation per message, intrinsic degradation and growth dilution distinct provides the basis for understanding how regulatory proteins change gene output.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-49 - Transcriptional regulation and the lac operon.md>)

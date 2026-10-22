"""Recover substantive AB teaching lost with worked-example sections.

Edits current corrected canonical units only; publication is coordinated centrally.
"""
from pathlib import Path
import re, subprocess, math, json

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'other/work/archive/reviewed-units/Advanced Biotechnology'
ADD={
1:r'''#### Charge and reverse-complement checks

A duplex made from two unphosphorylated $n$-nucleotide strands contains $2(n-1)$ phosphodiester groups. This counts the bonds between nucleotides, rather than assigning a terminal phosphate that is absent. Counterions screen this negative backbone charge; charge counting alone does not specify the buffer needed.

Self-complementarity means equality with the **reverse complement**, with both sequences written in the same direction. Thus 5′-ATCGAT-3′ pairs fully with another copy of itself. Merely replacing each base by its complement without reversing direction misses the antiparallel geometry.''',
2:r'''#### Reading the rod-to-coil crossover

With $l_P=50\,\mathrm{nm}$ and $L=0.34n\,\mathrm{nm}$ for a duplex of $n$ base pairs, equation (5) gives:

| Length (bp) | Contour length (nm) | RMS end-to-end distance (nm) | RMS distance / contour length |
|---|---|---|---|
| 20 | 6.8 | 6.65 | 0.98 |
| 150 | 51 | 43.6 | 0.86 |
| 1000 | 340 | 170 | 0.50 |

Short duplexes therefore act as nearly straight struts in DNA nanotechnology, whereas longer duplexes store contour length in bends. The RMS end-to-end distance is a statistical separation of the ends, rather than a coil diameter. Single strands have much shorter persistence lengths and can already be flexible at oligonucleotide lengths; losing those conformations contributes to the entropy cost of hybridisation.''',
3:r'''#### Concentration shifts the melting transition

For illustrative two-state parameters $\Delta H^0=-80\,\mathrm{kcal\,mol^{-1}}$ and $\Delta S^0=-220\,\mathrm{cal\,K^{-1}\,mol^{-1}}$, equation (11) gives melting temperatures of $48.4\,{}^\circ\mathrm C$ and $60.6\,{}^\circ\mathrm C$ at strand concentrations of $1\,\mu\mathrm M$ and $100\,\mu\mathrm M$, respectively. The higher concentration favours a bimolecular duplex over two separate strands, so temperature must rise further before half dissociates. A melting temperature therefore has meaning only with its concentration and salt conditions.

![Calculated two-state melting curves: the horizontal axis is temperature and the vertical axis is duplex fraction; increasing concentration moves the half-duplex crossing to higher temperature](figs/AB-03-model-melting-curves.png)

These are computed equilibrium curves, rather than experimental measurements. Their downward transition shows thermal dissociation; the horizontal displacement isolates the concentration effect at fixed model enthalpy and entropy.''',
4:r'''#### Counting sequence contributions correctly

An $n$-base-pair duplex has $n-1$ adjacent stacking steps. Reverse-complement symmetry allows a step to be looked up in the same table even when its written orientation differs. Terminal initiation contributions must then be added once for each end; a self-complementarity correction applies only when the whole strand equals its reverse complement.

For the illustrative duplex 5′-GTATTTGGCTGT-3′ and its complement, the corrected sums are $\Delta H^0=-87.2\,\mathrm{kcal\,mol^{-1}}$ and $\Delta S^0=-240.3\,\mathrm{cal\,K^{-1}\,mol^{-1}}$ at $1\,\mathrm M$ sodium. At $1\,\mu\mathrm M$ per strand this gives $T_m=50.9\,{}^\circ\mathrm C$. Applying the salt correction to its eleven steps at $0.15\,\mathrm M$ sodium lowers $T_m$ to $41.9\,{}^\circ\mathrm C$. Salt screening is therefore a major part of the prediction, rather than a small sequence-independent adjustment.''',
5:r'''#### Binding time and residence time answer different questions

At fixed free partner concentration $c$, the encounter time is approximately $1/(k_{\mathrm{on}}c)$, while a bound duplex's mean residence time is $1/k_{\mathrm{off}}$ and its dissociation half-life is $\ln2/k_{\mathrm{off}}$. With the illustrative $k_{\mathrm{on}}=10^5\,\mathrm{M^{-1}\,s^{-1}}$ and $c=1\,\mu\mathrm M$, the encounter time is $10\,\mathrm s$. Making a duplex more favourable can greatly reduce its off-rate without comparably changing that encounter time.

Short sticky regions can therefore support reversible exchange, while longer strongly bound regions can remain fixed during an experiment. Predictions of extremely long lifetimes from a two-state extrapolation should not be interpreted as actual molecular lifetimes: degradation, temperature changes, displacement and other pathways can dominate.''',
7:r'''#### Yield and impurity identity are separate design outcomes

Solving $Y=P^{n-1}$ for a target full-length fraction $Y$ gives $P=Y^{1/(n-1)}$. A $50\%$ target requires $P=0.99652$ for 200 nucleotides and $P=0.99931$ for 1000 nucleotides: increasing length makes a small per-cycle failure probability increasingly costly.

For a 60-mer with $P=0.994$, the full-length fraction is $70.1\%$. Without capping, the probability of exactly one missed coupling is $25.0\%$, yielding near-full-length deletion products that are hard to separate. Effective capping converts failed chains into permanently terminated truncations; it changes separability rather than rescuing the full-length yield.''',
8:r'''#### Assembly success and sequence correctness

If each base independently has error probability $\varepsilon$, an $L$-base construct is error-free with probability $Y=(1-\varepsilon)^L$. Independence is an approximation; synthesis and assembly can also generate correlated errors. Screening $m$ independent clones leaves probability $(1-Y)^m$ that none is correct. To make this no larger than a chosen failure probability $\alpha$, take logarithms and divide by the negative $\ln(1-Y)$:

$$m\geq\frac{\ln\alpha}{\ln(1-Y)}.$$

The required integer is rounded upwards. For a 1000-base construct and $\alpha=0.05$, error probabilities of one in 300 and one in 1500 give error-free fractions of $3.55\%$ and $51.3\%$, requiring 83 and 5 independent clones respectively. Successful assembly alone therefore does not establish a correct sequence; verification tests a different outcome.''',
10:r'''#### Why nominal coverage leaves random gaps

Let $M$ reads of length $L$ sample a genome of length $G$ uniformly and independently, with end effects neglected. A given base is covered by one read with probability approximately $L/G$, so the chance no read covers it is $(1-L/G)^M$. In the many-read, small-$L/G$ limit, using $\ln(1-x)\approx-x$ gives

$$P(\text{uncovered})\approx e^{-ML/G}=e^{-c},\qquad c=ML/G.$$

The equivalent Poisson model has mean coverage $c$ and zero-count probability $e^{-c}$. At nominal coverage one, $36.8\%$ of bases remain uncovered; at ten, the random uncovered fraction is $4.54\times10^{-5}$. Extra coverage removes a fixed fraction of the remaining random gaps. Real gaps can instead persist through GC bias, inaccessible sequence and ambiguous mapping, so this limit is not a guarantee of complete assembly.''',
11:r'''#### Parallel spots set the scale of the measurement

Nominal coverage $c$ of a genome of length $G$ using reads of length $L$ needs $M=cG/L$ reads. For $G=3.1\times10^9$ bases, $c=30$ and $L=150$ bases, that is $6.2\times10^8$ individual reads. The gain in throughput comes from observing many clusters simultaneously.

A cluster represents one starting library fragment, but paired-end acquisition obtains two reads from that cluster. Read count, cluster count and count of independent starting molecules must therefore be distinguished when budgeting capacity or interpreting duplication.''',
12:r'''#### Quality scores and consensus confidence

A base-call Phred score $Q$ encodes estimated error probability $p$ through $Q=-10\log_{10}p$, or $p=10^{-Q/10}$. Thus Q20, Q30 and Q40 correspond to error probabilities $10^{-2}$, $10^{-3}$ and $10^{-4}$. For independent errors with probability $10^{-3}$ at every base, a 150-base read has expected error count $0.15$ and probability $1-(1-10^{-3})^{150}=0.139$ of at least one error. A high-quality read is therefore not necessarily wholly correct.

With $n$ independent observations at one correctly aligned site, let $J$ count wrong observations. Then $J$ is binomial with parameters $n,p$. Fewer than half wrong guarantees the correct strict-majority base, so a conservative failure bound is

$$P_{\mathrm{fail}}\leq\sum_{j=\lceil n/2\rceil}^{n}\binom njp^j(1-p)^{n-j}.$$

Even-$n$ ties are counted as failures, and all wrong bases are grouped together. For $n=30$ and $p=10^{-3}$ the bound is $1.53\times10^{-37}$. Such a tiny idealised bound explains the value of redundancy, but does not predict actual consensus accuracy: alignment, correlated sequence errors, uneven coverage and mapping bias can dominate. Mean genome coverage is also not the number of observations at every site.''',
13:r'''#### What the independent-error limit teaches

The conservative binomial consensus bound derived for base calls applies only when observations are independent and correctly aligned. With illustrative per-read error probability $p=0.05$, it gives upper bounds of $1.16\times10^{-3}$, $6.37\times10^{-5}$ and $2.31\times10^{-12}$ at 5, 10 and 30 observations. Even-pass ties are included as failure. These are statistical model outputs, rather than platform specifications.

The unrealistic improvement at high depth exposes the missing mechanism: sequence-context bias can be shared across reads. Extra independent molecules help random error, while a repeated misinterpretation of the same homopolymer signal requires better measurement or decoding. Long reads can still resolve which unique regions flank a repeat even when some individual bases remain uncertain.''',
14:r'''#### Quantifying optical background and repeated passes

For free fluorescent nucleotides at molar concentration $c$ in observation volume $V$, the mean number present is $\bar N=cN_AV$, where $N_A$ is Avogadro's constant. Setting $\bar N=1$ gives $c=1/(N_AV)$. With $V=20$ zeptolitres, this concentration is approximately $83\,\mu\mathrm M$; at $5\,\mu\mathrm M$, the mean free occupancy is only $0.0602$. A one-femtolitre observation volume at the same concentration would contain approximately 3011 free labelled molecules. Optical confinement therefore removes background without forcing the entire reaction to use a negligibly low substrate concentration.

Repeated passes trade molecular reach for confidence. A fixed total polymerase read budget of 100 kb supplies approximately 20 passes over a 5 kb insert or 5 over a 20 kb insert, ignoring adapters. An independent-error majority model illustrates the gain, but pulse information, alignment and correlated errors determine measured HiFi performance; a pass count alone is not an accuracy specification.''',
15:r'''#### Non-invasive prenatal chromosome screening

During pregnancy, cell-free DNA in maternal plasma includes a placental contribution, commonly called the fetal fraction, mixed with maternal DNA. The placental contribution can reveal fetal chromosome dosage, although placenta and fetus need not have identical chromosome complements. Chromosome counting can use the mixture directly: sequence fragments, map reads to chromosomes, and compare the chromosome-21 proportion with a calibrated euploid baseline. Each read need not be assigned to mother or fetus.

![Maternal plasma DNA is sequenced and chromosome-specific read counts are compared; a chromosome-21 excess is a screening signal](figs/AB-15-prenatal-screening.png)

Let $p$ be the normal chromosome-21 read fraction and let $f$ denote the placental contribution expressed as a fraction of diploid genome equivalents before adding an extra chromosome. A trisomic contribution carries three copies instead of two, raising its chromosome-21 dosage by a factor $3/2$. Before normalising the total DNA amount, the expected chromosome-21 count is proportional to $p(1+f/2)$. The extra chromosome also increases the total by $fp/2$, giving

$$p'=\frac{p(1+f/2)}{1+fp/2}\approx p(1+f/2).$$

The approximation neglects the small change in the denominator. For illustrative $p=46.7/3100$ and $f=0.10$, the exact model gives $p'=0.015806$ versus $p=0.015065$: an increase of about $4.92\%$ relative to baseline. The absolute excess is small because the maternal contribution dilutes the dosage change. A clinical fetal-fraction estimate may use a different convention, so its definition must match the model.

If $N$ usable reads independently fall on chromosome 21 with probability $p$, the count is binomial and the measured fraction has standard error $\sigma=\sqrt{p(1-p)/N}$. To resolve an excess $\Delta p=p'-p$ at a chosen idealised ratio $z=\Delta p/\sigma$, rearrange to obtain $N=p(1-p)(z/\Delta p)^2$. The illustrative model needs approximately $6.75\times10^5$ reads for $z=5$. This is a counting-only comparison against a known baseline, rather than a validated clinical cutoff or a calculation of predictive value.

For small $f$, $\Delta p$ is proportional to $f$, so maintaining the same counting precision requires $N\propto f^{-2}$. Lowering $f$ from $0.10$ to $0.04$ requires roughly 6.25 times the depth in this approximation. Short uniquely mapping reads can suffice because the observation is chromosome identity, although accurate mapping and correction of capture/GC bias still matter. More reads reduce random uncertainty; they cannot remove biased sampling or establish the biological source of an excess. This remains a screen: a statistical placental-DNA signal does not by itself establish the fetal karyotype.''',
16:r'''#### Cycle precision and low-copy sampling

At ideal doubling, a tenfold dilution shifts the threshold by $\log_2 10=3.32$ cycles. A one-cycle difference represents a factor of two in starting material. The logarithmic readout compresses a wide concentration range into a short cycle interval, but makes small threshold errors consequential.

At low abundance, the tube must first receive a molecule. If random loading has mean $\mu$ target copies per reaction, the Poisson zero-copy probability is $e^{-\mu}$. At a mean of one copy it is $36.8\%$: even perfect amplification cannot detect a molecule absent from the aliquot. Detection limits therefore depend on replicate sampling and validated assay performance, rather than extrapolating a threshold equation to one copy. A stray amplicon can also amplify, which is why contamination controls are essential.''',
17:r'''#### Uncertainty is multiplicative after exponentiation

When four independently measured thresholds enter $\Delta\Delta C_t$, their variances add even though some enter with negative signs. For a common threshold standard deviation $s$, this gives $\sigma_{\Delta\Delta C_t}=\sqrt{4s^2}=2s$. If measurements share a plate or sample effect, covariance terms must also be included.

With ideal doubling, a threshold-difference uncertainty $\sigma$ becomes a multiplicative factor $2^\sigma$ on the fold change. Taking $s=0.15$ cycles gives $\sigma=0.30$ cycles and a factor $1.23$, rather than an additive error of 0.30 on expression. This is a one-standard-deviation illustration, not a universal confidence interval or resolution limit. Precision, biological replication and systematic assay error all affect whether a small change can be resolved.

Efficiency errors also compound: for $\Delta\Delta C_t=-3.3$, using a true amplification factor 1.9 gives 8.315-fold, while assuming doubling gives 9.849-fold, an $18.4\%$ overestimate relative to the former. The efficiency must be measured over the assay's operating range.''',
18:r'''#### Following RNA through an RT-qPCR assay

An RNA-virus assay must release and recover RNA, reverse-transcribe its target to DNA, then amplify that DNA with sequence-specific primers and probes. Multiple validated targets reduce vulnerability to a mutation at any one binding site. Lysis and inactivation depend on the actual reagents and protocol; adding a detergent alone does not establish that every sample is safely inactivated.

A negative target signal has several causes: no target in the sampled material, loss or degradation during extraction, failed reverse transcription, or amplification inhibition. An appropriate process control travelling through those steps helps distinguish failure from absence. A control added only after extraction cannot test extraction recovery. A human-target control can assess sample adequacy, but a DNA-reactive control does not by itself establish successful reverse transcription. A no-template control instead tests contamination, and cannot replace a process control.

Threshold interpretation must follow the validated assay rather than a universal cycle cutoff. At low copy number, aliquots disagree through Poisson sampling; nonspecific signal can also become important. Even a clear target signal does not directly measure infectious virus. Sampling, extraction and reverse-transcription efficiency affect $C_t$, so comparing viral loads requires calibration and an appropriate sampling basis.''',
19:r'''#### Sequence-space sampling and enrichment saturation

A random region of length $n$ has $4^n$ possible sequences. With $M$ independently and uniformly drawn molecules, the expected fraction of distinct sequence types represented is $1-(1-4^{-n})^M\approx1-e^{-M/4^n}$. The ratio $M/4^n$ is only an approximation to that fraction when it is small; synthesis bias can leave sequences missing even from a nominally abundant library.

For $M=10^{15}$ and $n=40$, the sampled fraction is about $8.27\times10^{-10}$. SELEX therefore searches a tiny sample of the available space. If binders survive a round $r$ times as efficiently as non-binders, their **odds**, rather than their fraction, multiply by $r$. Starting at fraction $b_0$, after $j$ rounds

$$b_j=\frac{b_0r^j}{1-b_0+b_0r^j}.$$

This follows by multiplying binder abundance by $r^j$ relative to non-binders and then normalising the two populations. With $b_0=10^{-10}$ and $r=10$, it gives $b_9=0.0909$ and $b_{12}=0.9901$. The apparent late surge is enrichment from a rare starting population. Once most sequences survive the same wash, stringency must distinguish stronger from weaker binders; the optimal number of rounds is assay-dependent because amplification bias and diversity loss also accumulate.''',
21:r'''#### Geometry sets both size and resolution

A scaffold of $n$ paired nucleotides has duplex contour length approximately $0.34n\,\mathrm{nm}$. If parallel helices are spaced by $d$, a fully filled single-layer rectangle has area approximately $0.34nd\,\mathrm{nm^2}$, neglecting turns and unpaired regions. For $n=7249$ and $d=2.5\,\mathrm{nm}$, a square would have side approximately $78.5\,\mathrm{nm}$. A structure described as roughly 100 nm across can therefore have a different aspect ratio or incomplete filling; that dimension does not imply a fully packed 100 nm square.

Address spacing is constrained by helix packing and crossover geometry. Sixteen base pairs span approximately $5.44\,\mathrm{nm}$ along a helix, so nanometre-scale placement is limited by DNA geometry as well as synthesis. A schematic outline cannot establish arbitrary sub-base-pair positioning.''',
22:r'''#### The crossover from escape to successful displacement

In the two-pathway model, the probability that a bound invader completes branch migration before escaping is $k_{BM}/(k_{BM}+k_{\mathrm{off}})$. Thus $k_{\mathrm{eff}}=k_{\mathrm{on}}k_{BM}/(k_{BM}+k_{\mathrm{off}})$. When escape is much faster, stronger toehold binding lowers $k_{\mathrm{off}}$ and raises the success probability. Once $k_{\mathrm{off}}\ll k_{BM}$, almost every encounter succeeds and $k_{\mathrm{eff}}$ approaches $k_{\mathrm{on}}$.

An illustrative stabilisation of $1.5\,\mathrm{kcal\,mol^{-1}}$ per added base pair at $25\,{}^\circ\mathrm C$ changes the equilibrium factor by approximately 12.6 per base. It can therefore tune the escape-dominated rate by orders of magnitude, but cannot raise the rate beyond the encounter-limited plateau. A zero-length toehold is outside the literal bound-intermediate model; blunt-end displacement needs its own mechanism rather than assigning it a fictitious duplex free energy.''',
34:r'''#### What a laboratory filtration test identifies

In the cake-dominated model, a single constant-pressure test determines the combined broth property $\phi'c\mu_f=2tA^2\Delta p^{1-s}/V_f^2$, rather than each factor separately. This group can transfer to a larger filter only while the same cake law and feed properties remain valid.

At fixed target filtrate volume and processing time, area scales as $A\propto\Delta p^{-(1-s)/2}$. For $s=0.5$, halving pressure raises required area by $2^{1/4}=1.189$, or $18.9\%$. Compression absorbs part of the extra driving force. As $s\to1$, increasing pressure gives no benefit in this ideal cake-dominated law, while increasing area still improves capacity. Choosing pressure therefore requires an energy and equipment comparison as well as this sizing relationship.''',
36:r'''#### Why enhanced acceleration changes feasible separation times

Stokes settling gives velocity proportional to acceleration at fixed particle diameter, density contrast and viscosity. For an illustrative $1\,\mu\mathrm m$ sphere with density contrast $300\,\mathrm{kg\,m^{-3}}$ in a liquid of viscosity $10^{-3}\,\mathrm{Pa\,s}$, the gravity settling speed is $1.64\times10^{-7}\,\mathrm{m\,s^{-1}}$. Traversing $0.1\,\mathrm m$ would take approximately 7.08 days.

A uniform acceleration of $10^4g$ would reduce that ideal traversal time to approximately 61.2 seconds. A real centrifuge has acceleration $r\omega^2$ varying with radius, so its transit time must be integrated along the radial path. The constant-acceleration comparison explains the equipment's purpose without replacing that design calculation.''',
37:r'''#### Geometric scaling and the sigma convention

For geometrically similar tubular bowls, the logarithm of the radius ratio is unchanged on scaling every length by a factor $s$. The volume-like geometric factor then scales as $s^3$, so $\Sigma\propto s^3\omega^2$. Matching the same duty and suspension requires the same $\Sigma$, giving $\omega_2/\omega_1=s^{-3/2}$. Doubling all dimensions therefore requires approximately $35.4\%$ of the original rotation rate in this ideal model.

The wall-stress scale $r^2\omega^2$ then changes by $s^2s^{-3}=s^{-1}$, halving for doubled dimensions. This is a scaling argument rather than a mechanical certification. In the half-area convention used here, $Q_{\mathrm{cut}}=2\Sigma u_g$; the equivalent gravity-settler area for that throughput is $2\Sigma$, not $\Sigma$. Scale-up must preserve the convention as well as account for departures from ideal flow.''',
42:r'''#### Recovery and concentration require separate balances

Let $r=V_u/V_l$ be the upper-to-lower phase-volume ratio and $K=C_{A,u}/C_{A,l}$ the equilibrium partition coefficient. If $C_{A,0}$ denotes target mass divided by the final total two-phase volume, conservation gives $C_{A,0}(V_u+V_l)=C_{A,l}(KV_u+V_l)$. Solving for the upper concentration yields

$$\frac{C_{A,u}}{C_{A,0}}=\frac{K(1+r)}{1+Kr}.$$

At $K=4.2$, increasing $r$ from 0.5 to 5 raises recovery from $67.7\%$ to $95.5\%$, but lowers this concentration ratio from 2.032 to 1.145. The basis holds the final average concentration fixed. Holding feed mass and one phase volume fixed would give a different concentration comparison. A phase ratio alone cannot determine dilution relative to the original feed before phase-forming additives.''',
43:r'''#### A solubility prediction must close a material balance

Let $M_0$ be target mass present, $V$ the final liquid volume and $S$ its equilibrium solubility at the chosen salt concentration. The dissolved mass cannot exceed either $M_0$ or $SV$, so the equilibrium precipitated mass is $M_{\mathrm{ppt}}=\max(0,M_0-SV)$. This prevents a negative recovery when the solution is unsaturated. Salt addition can change $V$, so the final mixture volume must be used.

For a target recovery $Y$, the required solubility is $S=(1-Y)M_0/V$. Substituting into the Cohn relation shows why the final increments in recovery become expensive: the required salt concentration rises as $-\ln(1-Y)$. Before relying on that extrapolation, compare it with salt saturation and the fitted protein-solubility range. Adding salt beyond its own solubility cannot create the arbitrarily high dissolved-salt concentration implied by extrapolating the protein model.''',
45:r'''#### Equilibrium loading controls the resin requirement

For a single batch of liquid volume $V$ and initial target concentration $C_0$, recovery $Y$ leaves equilibrium liquid concentration $C^*=(1-Y)C_0$, assuming the liquid volume is unchanged. Initially unloaded resin must take up $YC_0V$. If its equilibrium loading per unit resin volume is $q(C^*)$, conservation gives

$$V_{\mathrm{res}}=\frac{YC_0V}{q((1-Y)C_0)}.$$

For a Freundlich isotherm $q=K_F(C^*)^{1/n}$ with positive parameters $K_F,n$, this scales as $Y/(1-Y)^{1/n}$ at fixed feed. Higher recovery both increases mass to adsorb and lowers the equilibrium loading of each unit of resin. This is why the last fraction of product costs disproportionately more adsorbent. Unit conventions must match those used to fit $K_F$. A flowing packed bed instead requires dynamic capacity at a specified breakthrough criterion; a batch equilibrium balance is not a validated column design.''',
47:r'''#### Why size exclusion is a polishing operation

With $V_e=V_0+K_pV_i$ and $0\leq K_p\leq1$ for ideal pore partitioning, all peak centres lie between $V_0$ and $V_0+V_i$. The entire elution window has width $V_i$; two species differ in peak-centre volume by $\Delta V_e=\Delta K_pV_i$. A retention ratio alone cannot give resolution without the peak widths.

Injection volume occupies part of that finite window and broadens the bands, explaining why size exclusion accepts only a small sample volume relative to the bed. It also has no binding stage that accumulates product from a large feed, so collection commonly dilutes the sample. Binding chromatography can concentrate under suitable conditions, but that outcome is not automatic.

Pore partitioning depends on hydrodynamic size, shape and accessible pore distribution. Buffer, pH and temperature can alter conformation, association, gel swelling or unwanted interactions. Calibration therefore requires matched conditions; an elution volume does not by itself establish molecular mass.''',
48:r'''#### Effective loss and intrinsic degradation must be distinguished

The steady ratio $p^*/m^*=k_2/\lambda_2$ compares standing protein and message abundances. The expected proteins translated during one message's mean lifetime instead involve $k_2/\lambda_1$. Confusing these ratios mixes protein persistence with message lifetime.

If a stated message half-life already includes dilution, using $\lambda_1=\ln2/t_{1/2}$ includes that effect. If it denotes intrinsic degradation, add the growth-dilution rate once. For an intrinsic five-minute degradation half-life and a twenty-minute doubling time, $\lambda_1=\ln2/5+\ln2/20$ gives an effective four-minute half-life. Adding dilution to an already effective half-life would double-count a loss mechanism.''',
50:r'''#### Finite switching and local relaxation

Local relaxation near a stable expression level depends on the slope of net production there. A full rise from zero can be faster than that local estimate because a negatively autoregulated promoter starts relatively unrepressed. Comparing half-rise and half-relaxation times therefore requires specifying both initial condition and reference endpoint.

For no-leak positive autoregulation with Hill exponent two, the balance is $\dot x=\beta x^2/(K^2+x^2)-\lambda x$. Besides $x=0$, steady states satisfy $\lambda x^2-\beta x+\lambda K^2=0$. Thus two positive roots exist when $\beta>2\lambda K$:

$$x_{\pm}=\frac{\beta\pm\sqrt{\beta^2-4\lambda^2K^2}}{2\lambda}.$$

The lower positive root is an unstable threshold and the upper is stable; the zero state is also stable. With exactly zero protein and zero leak, the deterministic system stays OFF until a perturbation crosses the threshold. Basal transcription changes the balance, can initiate expression and may remove bistability. Strong positive feedback alone is therefore insufficient evidence of a switch.''',
51:r'''#### Reading matched-reporter scatter

![Matched reporters and a scatter cloud elongated along the equal-signal diagonal](figs/AB-51-dual-reporter.png)

The axes report the two matched signals; negative coordinates in a centred plot are deviations from the means, rather than negative molecule counts. Shared variation shifts both reporters together and elongates the cloud along the diagonal. Independent variation spreads it away from that diagonal. The mean-square difference obeys $\langle(X-Y)^2\rangle=\operatorname{Var}(X)+\operatorname{Var}(Y)-2\operatorname{Cov}(X,Y)$ when the means are equal, showing why covariance removes the shared part from the difference.

Promoter switching in a mechanistic cascade can be intrinsic stochasticity that propagates downstream. Its propagated contribution is not automatically the extrinsic component inferred from a dual-reporter experiment: that classification depends on which fluctuations are shared between the reporters. The diagram suggests shared variation but supplies no precise variance estimate.''',
52:r'''#### Dilution as a generation counter

During a strongly repressed decay phase, suppose synthesis and intrinsic degradation are negligible. Growth alone gives $\dot x=-\lambda x$, with $\lambda=\ln2/T_d$ for doubling time $T_d$. Integrating gives $x=x_0e^{-\lambda t}=x_0 2^{-G}$, where $x_0$ is initial concentration and $G=t/T_d$ is elapsed generations. Setting the derepression threshold to $K$ and taking logarithms gives

$$G_{\mathrm{switch}}=\frac{\ln(x_0/K)}{\ln2}=\log_2(x_0/K).\tag{124}$$

Each generation halves concentration, so doubling the initial peak adds one generation before the threshold is reached. The peak influences timing logarithmically. This describes one decay segment, rather than the full oscillator period, and low-threshold stochasticity can still dominate timing.

A calibrated dilution-dominated oscillator can therefore report elapsed generations. Its phase is measured modulo a cycle, so adequate sampling or cycle counting is required to recover longer elapsed intervals. It is not a universal clock in minutes because the growth rate changes with environment.''',
53:r'''#### Reassigning a stop codon in a defined mixture

To insert a non-canonical amino acid at a chosen stop codon, a defined PURE mixture can omit its recognising release factor and supply a suppressor tRNA charged with the desired amino acid. The tRNA can then support elongation where termination would otherwise occur.

![Purified components assembled into a transcription–translation reaction](figs/AB-53-pure-components.png)

Removing a release factor alone provides neither the unusual amino acid nor a correctly charged tRNA. The other elongation factors must remain functional, and the product needs a separate effective termination route. Extracts are harder to control because endogenous release factors and competing reactions remain. The defined mixture makes a specific molecular competition experimentally adjustable.''',
54:r'''#### Following acceptable product through the process

![Conceptual train for IVT, purification, separate enzymatic capping, further purification and formulation](figs/AB-54-ivt-process.png)

In this conceptual diagram VCC denotes vaccinia capping enzyme and the methyl donor supports cap methylation. Selective enzyme recycling needs its own separation evidence; a filtration arrow alone does not establish that long RNA and enzyme can be separated.

Let $m_0$ be intact target RNA mass, $f_c$ its correctly capped fraction, $y_p$ recovery of that fraction in purification and $y_f$ its recovery in formulation. Neglect cap mass increase and additional degradation. Successive balances give $m_c=m_0f_c$, $m_p=m_cy_p$ and $m_f=m_py_f$, hence

$$m_f=m_0f_cy_py_f.\tag{125}$$

For illustrative $m_0=100\,\mathrm{mg}$, $f_c=0.90$, $y_p=0.80$ and $y_f=0.95$, acceptable final mass is $68.4\,\mathrm{mg}$. All recovery factors are dimensionless and refer to the target population entering the relevant step. Total RNA mass alone can overstate acceptable yield if incorrect caps or damaged transcripts remain.''',
55:r'''#### Minimal survival does not mean complete understanding

The original JCVI-syn3.0 characterisation counted 438 protein-coding and 35 RNA genes, giving 473 total. Of these, 149 lacked a specific biological function assignment at the time. With $f_u$ denoting that historical fraction,

$$f_u=\frac{149}{473}\approx0.315=31.5\%.\tag{126}$$

The denominator includes RNA genes. A broad classification may still be possible without a specific mechanism, so a chart's wholly unassigned category need not equal this fraction. These are historical annotation counts, rather than a claim that all those functions remain unknown.

![Growth and morphology comparison of JCVI-syn1.0 and JCVI-syn3.0, with original panel labels and scale bars](figs/AB-55-growth-morphology.png)

The comparison shows that sustained replication can coexist with irregular, heterogeneous cell shapes. Survival of a reduced genome therefore does not establish normal division or industrial robustness. The image supports a phenotype comparison; no new quantitative growth estimate is inferred from its curves.''',
56:r'''#### Transport scaling and evidence for cellular function

For a spherical compartment with fixed permeability and exterior concentration, the volume-to-area ratio is proportional to radius. Doubling radius therefore doubles the exchange time and the depletion required to support the same volumetric substrate demand. A steady concentration predicted below zero would signal that constant consumption is impossible; concentration-dependent consumption must replace that approximation.

![Compartment containing red and cyan internal domains, retaining its original 50 micrometre scale bar](figs/AB-56-synthetic-organelles.png)

This image illustrates spatial organisation within an enclosing boundary. It does not alone establish selective transport, replication or autonomous metabolism. Those require separate observations of substrate entry, product formation and boundary integrity over time.''',
57:r'''#### Sticky-end compatibility and kinetic reversibility

If every otherwise identical nanostar carries the same sticky end, full matching requires that sequence to equal its reverse complement. All sequences here are written 5′ to 3′. `CGATCG`, `GGGGCCCC`, `CAGATCTG` and `CGCG` meet that condition; `CCGATGCG` does not, because its reverse complement is `CGCATCGG`. High GC content alone does not establish compatibility with another identical end.

Length, neighbouring-base stacking and scaffold geometry then affect stability. A longer GC-rich compatible end may strengthen association, but self-folding, alternative pairing and slow bond exchange can obstruct the desired liquid-like assembly. Shortening an end can weaken association even when its GC percentage rises. A phase diagram and exchange measurements must test the design rather than choosing by GC fraction alone.

#### Inferring lifetime requires a production model

For transcript length $L$ and elongation speed $k$, the elongation time is $t_{\mathrm{tx}}=L/k$. Only if each of $n_p$ templates continuously carries one productive polymerase, with negligible initiation delay, does completed-transcript production become $s=n_pk/L$. Elongation speed and plasmid count alone do not determine initiation or polymerase occupancy.

Combining that conditional production model with stationary abundance $N_{\mathrm{ss}}$ gives mean lifetime $\tau=N_{\mathrm{ss}}/s$, while first-order loss gives half-life $\tau\ln2$. Illustrative $k=250\,\mathrm{nt\,s^{-1}}$, $L=250\,\mathrm{nt}$, $n_p=25$ and $N_{\mathrm{ss}}=30000$ give $s=25\,\mathrm{s^{-1}}$, $\tau=20.0\,\mathrm{min}$ and half-life $13.9\,\mathrm{min}$. Multiple polymerases, initiation limitation, incomplete products, processing and dilution change the inference. Without steady state, abundance divided by production is an accumulation timescale rather than a molecular lifetime.''',
}

def old_blocks(path):
    old=subprocess.check_output(['git','show','77f9703^:'+path.relative_to(ROOT).as_posix()],cwd=ROOT).decode('utf-8')
    result={}
    for m in re.finditer(r'^## Section (\d+):.*?(?=^## Section |\Z)',old,re.M|re.S):
        hit=re.search(r'^### Worked example\n(.*?)(?=^### |\Z)',m[0],re.M|re.S)
        if hit:result[int(m[1])]=hit[1].strip()
    return result

records={}; changed=[]
for path in sorted(BASE.glob('*.md')):
    current=path.read_text(encoding='utf-8'); historical=old_blocks(path)
    def section(match):
        n=int(match[1]); body=match[0]
        if n==40:
            body=re.sub(r'^### Derivation\n.*?(?=^### Motivation and explanation)', '',body,flags=re.M|re.S)
            restored=historical[n]
            restored=restored.replace('**Problem.**','**Observed release data.**').replace('All numbers below were computed in Python.','The data illustrate fitting the release law and interpreting its operating range.')
            restored=restored.replace('**(a)** How many passes are required for 80 % release at 460 kg$_f$ cm⁻²?\n**(b)** What pressure delivers 70 % recovery in only two passes?','The fitted relation connects a target release fraction to required pass count or pressure.')
            restored=restored.replace('#### Step 4: (a) passes for 80 % at 460 kg$_f$ cm⁻²','#### From a fitted law to a pass target').replace('#### Step 5: (b) pressure for 70 % in two passes','#### From a fitted law to a pressure target')
            restored=restored.replace('confirming the first-order form','supporting the first-order form within the observed range')
            restored=restored.replace('Passes are whole numbers and 4.4 would fall short, so **$N = 5$**.','Four whole passes would fall short, so round the continuous target of 4.4 upwards to **$N = 5$**.')
            restored=restored.replace('so it is a modest extrapolation and reasonable — but it would need checking against the machine\'s pressure rating.','so this is an extrapolation requiring experimental validation as well as a check of the machine\'s pressure rating.')
            # Fix mixed text/math units in restored pre-guard material.
            restored=restored.replace('kg$_f$ cm⁻²',r'$\mathrm{kg_f\,cm^{-2}}$')
            body=body.replace('Worked example — fitting and using homogeniser kinetics','Fitting and using homogeniser kinetics')
            body=body.replace('Part (b) extrapolates slightly in pressure, which is acceptable.','The pressure inferred for 70 % release in two passes lies just outside the measured range and needs validation.')
            body=body.replace('Extrapolating to much higher pressure would not be:','Extrapolating to much higher pressure would not be justified:')
            pos=body.index('### Motivation and explanation')
            body=body[:pos]+'### Derivation\n\n'+restored+'\n\n'+body[pos:]
            records[n]='Recovered empirical dataset, transformed-response derivation, two-stage fit, fit diagnostics and conditional design inference; recast exercise as data analysis and corrected unsupported extrapolation approval.'
        elif n in ADD:
            if ADD[n] in body:
                records[n]='Recovered useful teaching as integrated explanation; omitted repetitive plug-in arithmetic and unsupported generalisations. '+ADD[n].splitlines()[0].lstrip('# ')
                return body
            candidates=[body.find(x) for x in ['### Wider pathway','### Link to other topics','### Summary','## Conclusion'] if body.find(x)>=0]
            pos=min(candidates)
            body=body[:pos]+ADD[n]+'\n\n'+body[pos:]
            records[n]='Recovered useful content as integrated explanatory subsections; omitted repetitive arithmetic or overly general claims from historical exercise. '+ADD[n].splitlines()[0].lstrip('# ')
        elif n==49:
            recovered=historical[n].replace('#### How lactose induces the lac operon','#### How lactose induces the lac operon')
            pos=body.find('### Link to other topics')
            if recovered not in body: body=body[:pos]+recovered+'\n\n'+body[pos:]
            records[n]='Recovered lac operon mechanism, basal expression, allolactose induction, glucose/CAP control table and perturbation interpretation; biological teaching rather than an arithmetic exercise.'
        elif n in historical: raise AssertionError(('unhandled removed content',n))
        else: records[n]='No worked-example block was removed; existing explanatory coverage retained.'
        body=body.replace('The worked example contrasts that idealised model with its practical limitations.','The independent-error bound below makes that model and its practical limitations explicit.')
        body=body.replace('Non-invasive prenatal screening, below','Non-invasive prenatal screening, explained below')
        return body
    updated=re.sub(r'^## Section (\d+):.*?(?=^## Section |\Z)',section,current,flags=re.M|re.S)
    updated=updated.replace('The worked example shows this.','The prenatal-counting model below shows why depth controls random uncertainty.')
    updated=updated.replace('for the reason the worked example makes clear.','because a chromosome excess in placental DNA is not itself a direct fetal karyotype.')
    updated=updated.replace('the worked example in Section 40 operates at 5 °C','the release measurements in Section 40 were made at 5 °C')
    updated=updated.replace('The worked example makes the size of this trade explicit.','The concentration balance below makes the basis of this trade explicit.')
    if updated!=current:path.write_text(updated,encoding='utf-8');changed.append(path.name)

assert len(records)==57
report=ROOT/'other/work/reviews/AB-worked-content-recovery-20261022.md'
report.write_text('# Advanced Biotechnology teaching-content recovery — 22 October 2026\n\nOwner: codex. Diagnosis completed before editing; parent approved implementation. Baseline: current corrected canonical units. Historical evidence: parent of 77f9703. All 57 notes audited; 37 removed teaching blocks recovered in their existing units. No new merge grouping. External-supplementation qualification for AB-U13 and optional AB57 retained.\n\n'+ '\n'.join(f'- AB-{n:02}: {records[n]}' for n in sorted(records))+'\n\nNumerical verification: see AB-worked-content-numerics-20261022.json. Publication and independent scientific review are separate coordinated checks.\n\nExternal sources opened: [Fan et al. original study abstract](https://pubmed.ncbi.nlm.nih.gov/18838674/); [JCVI minimal-cell project](https://www.jcvi.org/research/first-minimal-synthetic-bacterial-cell). PMC full text and PubChem lac pathway were blocked by browser verification and were not used. Other mechanisms reuse previously reviewed corrected text and existing source/review records.\n',encoding='utf-8')
with report.open('a',encoding='utf-8') as stream:
    stream.write('''
Specific retention/omission decisions and corrected qualifications:

- AB01: retain phosphodiester counting and reverse-complement test; omit routine length/turn multiplication already supported by the structural dimensions.
- AB02: retain rod-to-coil comparisons; omit the extra lambda-phage row and correct the interpretation of RMS end separation, which is not a measured coil diameter.
- AB03–05: retain concentration/salt sensitivity and encounter-versus-residence-time distinctions; omit redundant temperature/off-rate grids and the misleading suggestion that a two-state 20-mer extrapolation predicts its actual millennial lifetime.
- AB07–08: retain compounded synthesis failure, impurity identity and clone-screening probability; omit overlap-temperature numerical grids that invite treating one illustrative sequence/buffer as a universal overlap rule.
- AB10–14: retain random-gap derivation, read budgeting, Phred probability, conservative binomial consensus limits and optical occupancy; omit dated prices, instrument-specific throughput arithmetic and pass/quality tables that could be mistaken for actual platform guarantees. Distinguish paired reads from clusters.
- AB15: recover the whole prenatal mechanism, count model, dilution/depth relationship and interpretive limits. Replace the historical approximate unnormalised chromosome fraction by an explicit exact normalised model and define its genome-equivalent fetal-fraction convention. Omit unvalidated clinical cutoff/economic conclusions and the overstatement that base accuracy barely matters.
- AB16–18: retain cycle precision, multiplicative uncertainty and the full process-control logic. Replace simplistic single-copy sensitivity and fixed diagnostic cycle thresholds with aliquot sampling and assay validation; remove universal claims about inactivation, infectiousness and minimum resolvable fold change.
- AB19: retain sequence-space and enrichment mathematics; replace nominal complete-library assertions by occupancy probability and enrich odds rather than multiplying fractions past unity. Omit a universal prescription for ten to fifteen rounds.
- AB21–22: retain scaffold geometry, crossover spacing and encounter-limited saturation; omit zero-toehold numerical extrapolation outside the bound-intermediate model.
- AB34/36/37: retain property-group identification, pressure/compression scaling, settling times and geometrical sigma scaling; omit repeated equipment-specific substitution arithmetic.
- AB40: retain the entire empirical dataset and fit derivation, which are necessary to support the surviving interpretation. Recast exercise questions as target-design reasoning. Replace unsupported acceptance of extrapolation with the need for validation; round a continuous pass target upwards to whole passes.
- AB42/43/45/47: retain concentration-basis mass balances, saturation/recovery feasibility, equilibrium resin sizing and elution-window limitations; omit repeated numerical recovery grids and avoid treating batch loading as dynamic packed-column capacity.
- AB48–52: retain intrinsic-versus-effective loss, lac regulation, positive-feedback threshold, matched-reporter interpretation and generation-counter derivation. Omit repeated parameter substitution and numerical noisy-cascade grids. The first-order-loss image adds no new mechanism beyond existing half-life explanations, while the reporter image teaches signal interpretation and is retained.
- AB53–57: retain molecular codon reassignment, acceptable-product recovery, historical minimal-cell knowledge gap/phenotype, membrane transport evidence and sticky-end compatibility/lifetime inference. Omit duplicate numerical geometry comparisons and the overly confident best-sticky-end ranking; stability and liquid-like exchange require their own measurements.

Author validation: 69 numerical/sequence checks pass; equation tags retained and historical labels 74, 124–126 restored; all nine recovered figure files opened in a montage and their visible content checked. Native inline maths guard passes. Obsidian was not opened. Independent review by the ET agent passed after two AB40 wording clarifications. Central publication is handled by the parent agent.
''')
print(json.dumps({'changed_canonical_units':changed,'recovered_blocks':len(ADD)+2,'notes_audited':len(records)},indent=2))

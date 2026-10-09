# Codex independent review: AB-U9

Existing Claude-owned short notes unchanged. Findings and replacements are for merged deliverables only. No BOARD/PLAN changes or commits.

## Independent derivation and numerical results

Sphere force balance: πD³Δρ a/6=3πμD u gives u=D²Δρ a/(18μ). Rigid rotation gives dr/dt=Bω²r, B=D²Δρ/(18μ). Integrating gives t=ln(r2/rstart)/(Bω²). Thus volume/time is the throughput for the stated entry radius, not complete capture. Midpoint Q=0.3428413645 L/min; innermost-radius ideal Q=0.1587505672 L/min. For uniform axial velocity and particle concentration across annular area, midpoint capture fraction=[r2²-((r1+r2)/2)²]/(r2²-r1²)=0.5368217054. This is conditional on that ideal entry distribution.
Q=2 Sigma ug -> Sigma=32.41943537 m² and full equivalent gravity area=64.83887074 m². Alternative formula=35.35371383 m². Matched-duty doubled geometry speed=3535.53390593 rpm.
Independently derive disc formula: theta is angle to axis, dA=2πr dr/sin(theta), normal settling=ug ω²r cos(theta)/g. Integrate their product over r1..r2 and N-1 gaps: Q=ug * 2π ω²(N-1)(r2³-r1³)/(3g tan(theta)). This is FULL equivalent area; divide by two if using Q=2 Sigma ug.
Alternative tubular formula / exact formula equals (3+x²)ln(2/(1+x))/(1-x²), x=r1/r2. Since this depends on x, disagreement does not universally cancel between different geometries. Both scale as L³ω² for similar bowls, so doubled-size speed is unaffected.
Additional material caveats: AB35 periodic ejection is through peripheral ports; continuous solids discharge uses nozzles. Filtration is not inherently nonsterile (sealed sanitary membrane systems exist).

Full precision results: ../scratch/codex-ab-review/results.json. Reproduction script: ../scratch/codex-ab-review/check_examples.py.

## Exact merged-only replacements

Use ../scratch/codex-ab-review/merge-fixes.json before equation renumbering or other rewriting. Every old substring has been validated as present exactly once in its original note and after preceding replacements. Additional caveats above are review findings; the JSON prioritizes bounded corrections.

### AB-36, replacement 1

Midpoint transit is not full capture.

Exact old:

~~~text
$Q_{\text{cut}}$ is the **maximum volumetric flow rate** at which the tubular bowl still separates the cells. Running faster than this lets cells escape with the clarified liquid.
~~~

Exact replacement:

~~~text
$Q_{\text{cut}}$ is the throughput corresponding to the chosen radial-midpoint capture criterion, not guaranteed complete cell removal. Under the same ideal plug-flow assumptions, capture from the innermost radius requires replacing the logarithm by $\ln(r_2/r_1)$.
~~~

### AB-36, replacement 2

Uniform-area midpoint capture fraction=0.536822.

Exact old:

~~~text
The logarithm is the signature of a velocity proportional to position: the particle accelerates as it travels outwards, so the time is not simply distance over speed. The mid-point start is a convention — a particle entering at $r_1$ takes longer and one entering near $r_2$ less, so $t_{\text{cut}}$ represents an average particle.
~~~

Exact replacement:

~~~text
The logarithm follows from radial velocity being proportional to radius. Starting at $(r_1+r_2)/2$ defines a representative radial-midpoint criterion; particles starting closer to $r_1$ take longer. With uniform concentration and axial velocity across the annulus, the midpoint criterion corresponds to about 54 % capture in this geometry, not complete clarification.
~~~

### AB-36, replacement 3

State numerical full-capture contrast under ideal assumptions.

Exact old:

~~~text
**Why $Q_{\text{cut}}$ is a design criterion, not a prediction.** The particle diameter in (10) is the *smallest* particle that must be captured. Choosing a smaller $D_p$ lowers $Q_{\text{cut}}$ sharply, since it enters squared. In practice a culture contains a distribution of sizes, so there is no sharp cut — larger cells are captured above $Q_{\text{cut}}$ and smaller debris escapes below it.
~~~

Exact replacement:

~~~text
**What the criterion means.** Smaller particles settle more slowly, but entry radius also affects capture. Here the midpoint throughput is 0.343 L/min, whereas the innermost-radius ideal capture criterion gives 0.159 L/min. Actual recovery also depends on particle-size distribution, flow and hindered settling.
~~~

### AB-37, replacement 1

Factor-of-two error: full gravity-settler throughput is Q=A ug.

Exact old:

~~~text
The quantity that remains has units of area. That is not a coincidence: it is the area of a **hypothetical gravity settler** that would do the same job. A centrifuge with $\Sigma = 65$ m² clarifies at the rate a settling tank of 65 m² surface would, using a bowl a few centimetres across. $\Sigma$ expresses the machine's performance as the area it is worth.
~~~

Exact replacement:

~~~text
The machine factor has units of area. With the convention used here, $Q_{\text{cut}}=2\Sigma u_g$, the corresponding ideal gravity-settler area is $A_{\mathrm{eq}}=Q_{\text{cut}}/u_g=2\Sigma$. Thus $\Sigma=32.4$ m² corresponds to about 64.8 m² of gravity-settling area for the same stated capture criterion.
~~~

### AB-37, replacement 2

Cancellation is exact only within a matched ideal model.

Exact old:

~~~text
*Analogy:* quoting a heat exchanger's duty as an equivalent length of bare pipe. The analogy breaks down because $\Sigma$ is not merely a convenient restatement — it genuinely cancels out of a ratio, which is what makes scale-up exact rather than approximate.
~~~

Exact replacement:

~~~text
*Analogy:* expressing a device's performance as the equivalent area of a simpler separator. The comparison is conditional on matching feed, capture criterion and ideal flow assumptions; it does not make real centrifuge scale-up exact.
~~~

### AB-37, replacement 3

Repair repeated equivalent-area definition.

Exact old:

~~~text
so $\Sigma$ is the **equivalent surface area required to achieve the same throughput $Q_{\text{cut}}$ by gravity alone**.
~~~

Exact replacement:

~~~text
so the equivalent ideal gravity-settler area at this throughput is **$2\Sigma$**, under the stated $Q_{\text{cut}}=2\Sigma u_g$ convention.
~~~

### AB-37, replacement 4

Standard disc expression has full-area convention.

Exact old:

~~~text
**$\Sigma$ depends on the design, not just the dimensions.** Equation (4) is specific to the tubular bowl. For a disc-stack centrifuge:
~~~

Exact replacement:

~~~text
**The area factor depends on the design and convention.** Equation (4) uses $Q=2\Sigma u_g$. For a disc stack, state the full equivalent area $A_{\mathrm{eq,disc}}$, defined by $Q=A_{\mathrm{eq,disc}}u_g$:
~~~

### AB-37, replacement 5

Relabel full disc area rather than mixing it with Q=2 Sigma ug.

Exact old:

~~~text
$$\Sigma = \frac{2\pi\omega^2(N-1)}{3g\tan\theta}\left(r_2^3-r_1^3\right) \tag{6}$$
~~~

Exact replacement:

~~~text
$$A_{\mathrm{eq,disc}} = \frac{2\pi\omega^2(N-1)}{3g\tan\theta}\left(r_2^3-r_1^3\right) \tag{6}$$
~~~

### AB-37, replacement 6

Define angle and conversion explicitly.

Exact old:

~~~text
with $N$ the number of discs, $r_2$ and $r_1$ the outer and inner disc radii and $\theta$ the half-cone angle.
~~~

Exact replacement:

~~~text
with $N$ the number of discs, $r_2$ and $r_1$ the outer and inner disc radii and $\theta$ the disc angle to the rotation axis. Under the half-area convention of (4), use $\Sigma_{\mathrm{disc}}=A_{\mathrm{eq,disc}}/2$.
~~~

### AB-37, replacement 7

Alternative/exact expression ratio depends on r1/r2; only common constants cancel.

Exact old:

~~~text
For the example below, (7) gives 35.4 m² against 32.4 m² from (4), about 9 % higher. **The absolute value of $\Sigma$ is therefore not meaningful on its own** — only ratios are, and only when both centrifuges are evaluated with the same convention. This is the main practical trap in using Σ theory.
~~~

Exact replacement:

~~~text
For the example below, (7) gives 35.4 m² against 32.4 m² from (4), about 9 % higher. Quote the value with its definition and capture criterion. Their difference is not merely a universal prefactor: it depends on the radius ratio, so scale-up ratios calculated from different geometric expressions need not agree for dissimilar bowls.
~~~

### AB-37, replacement 8

Bound robust ratio claim to prefactors or geometric similarity.

Exact old:

~~~text
**Why the ratio is robust.** In (5) any constant prefactor common to both $\Sigma$ values cancels, so a consistent error in the convention does not affect scale-up. That is why Σ theory works in practice despite the ambiguity in (4).
~~~

Exact replacement:

~~~text
**When ratios are robust.** A common constant prefactor cancels from a ratio. Both tubular-bowl expressions also scale as $L^3\omega^2$ for geometrically similar bowls, so they give the same speed ratio in the doubled-size example. Dissimilar geometries require matched capture criteria, and real scale-up requires checking flow and separation-efficiency corrections.
~~~

### AB-37, replacement 9

Repair example interpretation without changing correct Sigma arithmetic.

Exact old:

~~~text
**Interpretation.** A bowl 4.4 cm across does the clarification work of a **32 m² settling tank**, roughly the floor area of a small room. That is the single most useful way to read a $\Sigma$ value.
~~~

Exact replacement:

~~~text
**Interpretation.** A bowl 4.4 cm across has $\Sigma=32.4$ m² in the chosen half-area convention. Its corresponding ideal gravity-settler area at the midpoint throughput is $2\Sigma=64.8$ m².
~~~

### AB-37, replacement 10

Repair repeated area error and unconditional scale-up claims.

Exact old:

~~~text
Factorising $Q_{\text{cut}} = 2\Sigma u_g$ separates the machine from the broth, leaving $\Sigma$ — an equivalent gravity-settling area that depends only on the centrifuge. Throughput then scales directly with $\Sigma$, whatever the feed, so scale-up is a matter of matching it; and because $\Sigma$ grows with disc number and with $r^3$, area rather than g-force is what buys capacity. The absolute value depends on convention, so only ratios should be trusted. This completes cell removal; Section 38 turns to releasing product held inside the cells.

~~~

Exact replacement:

~~~text
Factorising $Q_{\text{cut}}=2\Sigma u_g$ separates the ideal machine factor from the feed settling velocity. In this convention the equivalent gravity-settler area is $2\Sigma$. Throughput ratios follow area-factor ratios for matched feeds, capture criteria and flow assumptions; real scale-up requires checking those assumptions. Disc count, geometry and speed all contribute to capacity. This completes cell removal; Section 38 turns to intracellular product release.
~~~

## Figure checks and limitations

All 45 distinct local figure links resolved and decoded; all were opened visually in six contact sheets. Several inherited crops contain clipped surrounding text/labels, notably AB-36 tubular geometry and AB-42 extraction. They are recognisable, but crop quality is imperfect. Figures were not modified. Source Sigma and gel-volume equations were inspected as images and agree with the displayed formulas; the main corrections concern interpretation and applicability. Local equation numbers remain for parent renumbering. Phrase scan found no prose references to lecture PDFs/slides/lecturers; inherited image residue remains visible.

## Sources actually opened

- [Alfa Laval primary documentation, solids handling](https://www.alfalaval.co.uk/products/separation/centrifugal-separators/separators/innovations/separator-innovator/how-separation-works/separator-designs-for-solids-handling/)
- [UCL original research dissertation, chapter 4, PDF pp.134–135](https://discovery.ucl.ac.uk/id/eprint/10098603/1/10017237.pdf). Text opened; equation screenshots could not be fetched. Disc expression independently derived above.

Retrieval limits: Cytiva SEC handbook/FAQ and IUPAC Gold Book/PAC PDF could not be retrieved and were not relied upon. One Hofmeister PMC page presented a bot challenge; an RSC page returned 403; neither was used.

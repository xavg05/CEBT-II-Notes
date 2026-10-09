# Codex independent review: AB-U12

Existing Claude-owned short notes unchanged. Findings and replacements are for merged deliverables only. No BOARD/PLAN changes or commits.

## Independent derivation and numerical results

At local equilibrium ideal SEC storage is proportional to V0+Kp Vi, giving Ve=V0+Kp Vi. The stated k=Kp Vi/V0 uses the excluded-marker void reference. delta=.2/.5=.4, alpha=2.5 and peak-centre separation=19.45588235 mL. Resolution needs baseline widths: Rs=2 ΔVe/(w1+w2); none are given, so no numerical Rs follows.
Gel volume formula is sound if rho_g is rehydrated-particle density: wet mass=a(1+Wr rho_w)=rho_g(Vt-V0). Eliminate dry mass a from Vi=a Wr to obtain equation (8). Vi=64.8529411765 mL,Vs=5.1470588235 mL; elution volumes=30,42.9705882353,62.4264705882,94.8529411765 mL. Corresponding k=0,0.4323529412,1.0808823529,2.1617647059.
Ideal bounds assume noninteracting exclusion. Kp depends on effective hydrodynamic size/shape and pores, not simply nominal pore diameter; chemistry, pH, temperature and secondary interactions can change behavior. SEC has elution in running buffer but no separate desorption stage. Binding methods can concentrate depending on loading/elution volumes; they need not do so.

Full precision results: ../scratch/codex-ab-review/results.json. Reproduction script: ../scratch/codex-ab-review/check_examples.py.

## Exact merged-only replacements

Use ../scratch/codex-ab-review/merge-fixes.json before equation renumbering or other rewriting. Every old substring has been validated as present exactly once in its original note and after preceding replacements. Additional caveats above are review findings; the JSON prioritizes bounded corrections.

### AB-46, replacement 1

SEC does elute; no separate desorption step is needed.

Exact old:

~~~text
**Why gel chromatography is the odd one out.** The other four rely on *binding*. Gel chromatography involves no binding at all — only whether a molecule fits into a pore. As a consequence it has no elution step, cannot concentrate the product, and has a hard upper limit on how long a solute can be retained. Section 47 shows that this limit is what makes its elution volume exactly predictable.
~~~

Exact replacement:

~~~text
**Why gel chromatography differs.** Ideal size exclusion separates by pore access rather than binding. The sample elutes in the running buffer, without a separate change of conditions to desorb it. It generally dilutes the sample and has a bounded ideal elution window. Departures from ideal exclusion require checking for matrix interactions.
~~~

### AB-47, replacement 1

Generic mobile hold-up and SEC excluded-marker void are distinct.

Exact old:

~~~text
A solute that never interacts with the stationary phase travels with the liquid and emerges after one **void volume** $V_0$ — the volume of liquid between the particles. Everything that *does* interact is delayed. So the natural measure of retention is not $V_e$ itself but **how much it exceeds $V_0$**, scaled by $V_0$ to make it dimensionless. That is the capacity factor.
~~~

Exact replacement:

~~~text
In general chromatography the reference is the hold-up volume of an unretained marker. For the size-exclusion treatment here, $V_0$ specifically denotes the interparticle void volume, measured using a fully excluded marker. A smaller non-binding molecule can enter pores and elute later than $V_0$ without adsorbing. The dimensionless quantity $(V_e-V_0)/V_0$ below uses this stated reference.
~~~

### AB-47, replacement 2

Restrict SEC bounds and geometric model to noninteracting ideal solutes.

Exact old:

~~~text
Gel chromatography is the case where this becomes exactly predictable. There is no binding — only whether a molecule fits into the pores. A molecule too large to enter any pore is confined to the space between particles and elutes at $V_0$. A molecule small enough to enter every pore has the full internal volume available and elutes last. **Every solute lies between these two bounds**, so gel chromatography has a closed elution window, which no other type has.
~~~

Exact replacement:

~~~text
In ideal size exclusion, pore access rather than binding determines elution. A fully excluded molecule elutes at $V_0$, while a fully permeating noninteracting molecule elutes at $V_0+V_i$. Intermediate molecules have intermediate retention. These bounds assume ideal exclusion without adsorption or other nonideal matrix interactions; real retention is not exactly predictable from nominal pore size alone.
~~~

### AB-47, replacement 3

Peak width is absent from delta; resolution cannot be inferred.

Exact old:

~~~text
This measures how well the column distinguishes them. $\delta = 1$ means they co-elute and are not separated at all; the further $\delta$ is from 1, the better the resolution.
~~~

Exact replacement:

~~~text
This is a ratio of retention factors, not chromatographic resolution. With the later peak labelled 2, the usual separation factor is $\alpha=k_2/k_1$ for $k_1>0$. Resolution also requires peak widths: using baseline widths $w_1$ and $w_2$ in elution-volume units, $R_s=2(V_{e,2}-V_{e,1})/(w_1+w_2)$. Equal retention factors imply equal peak positions under the stated conditions, but a ratio different from one does not establish resolved peaks.
~~~

### AB-47, replacement 4

Bounds are conditional.

Exact old:

~~~text
**The two limits, which bound every solute:**
~~~

Exact replacement:

~~~text
**The two limits for ideal, noninteracting size exclusion:**
~~~

### AB-47, replacement 5

Repair repeated universal bound.

Exact old:

~~~text
Hence $V_0 \le V_e \le V_0+V_i$ for every solute.
~~~

Exact replacement:

~~~text
Hence $V_0 \le V_e \le V_0+V_i$ under ideal, noninteracting size exclusion.
~~~

### AB-47, replacement 6

Widths are absent, so no numerical resolution follows.

Exact old:

~~~text
**Step 4: resolution of two proteins.**
~~~

Exact replacement:

~~~text
**Step 4: relative retention of two proteins.**
~~~

### AB-47, replacement 7

Preserve correct delta and peak-spacing calculations.

Exact old:

~~~text
and the peaks are separated by $(0.5-0.2)\times64.9 = 19.5$ mL.
~~~

Exact replacement:

~~~text
and the peak centres differ by $(0.5-0.2)\times64.9 = 19.5$ mL. The separation factor is $\alpha=1/\delta=2.5$, but $R_s$ cannot be calculated without peak widths.
~~~

### AB-47, replacement 8

Every other chromatography does not necessarily concentrate; SEC has elution without desorption.

Exact old:

~~~text
- *It cannot concentrate.* Since there is no binding and no elution step, the product leaves more dilute than it entered, diluted by roughly the peak width. Every other type in Section 46 concentrates; this one does not.
~~~

Exact replacement:

~~~text
- *It generally dilutes the sample.* SEC has no binding stage to accumulate product from a large feed before releasing it in a smaller volume. Band spreading usually increases the collection volume. Binding chromatography can concentrate product under suitable loading and elution conditions, but concentration is not guaranteed by chromatography type.
~~~

### AB-47, replacement 9

Chemistry and temperature independence is scientifically false.

Exact old:

~~~text
- *But it is predictable.* Equation (4) is pure geometry — no affinity constants, no temperature dependence, no pH. Retention can be calculated in advance from the gel's pore size, which is why it doubles as an analytical method for measuring molecular size.
~~~

Exact replacement:

~~~text
- *The ideal model is useful, but conditional.* Equation (4) relates retention to an effective pore-partition coefficient. This depends on solute hydrodynamic size and shape and the pore distribution. Buffer composition, pH and temperature can change solute conformation, association, gel swelling or unwanted interactions. Size calibration therefore needs standards and matched conditions.
~~~

### AB-47, replacement 10

Repair repeated resolution and geometry overclaims.

Exact old:

~~~text
The capacity factor $k = (V_e-V_0)/V_0$ characterises retention and the retention ratio $\delta = k_1/k_2$ the resolution of two solutes. In gel chromatography there is no binding, so $V_e = V_0 + K_pV_i$ is pure geometry: every solute elutes between $V_0$ and $V_0+V_i$, giving a bounded, predictable window but no concentration and a strict limit on sample volume. Final isolation then converts the purified product into a storable solid, reusing the precipitation, filtration and centrifugation of earlier sections for formulation rather than separation. This completes the downstream processing unit.

~~~

Exact replacement:

~~~text
The stated retention factor characterises elution relative to $V_0$, and $\delta=k_1/k_2$ compares retention rather than resolution. Ideal size exclusion gives $V_e=V_0+K_pV_i$ and a bounded elution window, governed by effective pore access under defined conditions. It normally dilutes product, whereas binding methods can concentrate it under suitable loading and elution conditions. Final isolation converts purified product into the required storage or commercial form. This completes the downstream processing unit.
~~~

## Figure checks and limitations

All 45 distinct local figure links resolved and decoded; all were opened visually in six contact sheets. Several inherited crops contain clipped surrounding text/labels, notably AB-36 tubular geometry and AB-42 extraction. They are recognisable, but crop quality is imperfect. Figures were not modified. Source Sigma and gel-volume equations were inspected as images and agree with the displayed formulas; the main corrections concern interpretation and applicability. Local equation numbers remain for parent renumbering. Phrase scan found no prose references to lecture PDFs/slides/lecturers; inherited image residue remains visible.

## Sources actually opened

- [WHO International Pharmacopoeia, chromatography definitions](https://digicollections.net/phint/en/d/Jb/7.1.14.html). Opened retention-factor and peak-width/resolution definitions.
- [Agilent manufacturer SEC documentation](https://www.agilent.com/en/product/biopharma-hplc-analysis/aggregate-fragment-analysis). Opened; confirms secondary interactions are a design concern.
- [Bloustine et al., original SEC interaction study](https://arxiv.org/abs/cond-mat/0306346). Abstract opened only, supporting interaction-dependent retention; not used for detailed derivation.

Retrieval limits: Cytiva SEC handbook/FAQ and IUPAC Gold Book/PAC PDF could not be retrieved and were not relied upon. One Hofmeister PMC page presented a bot challenge; an RSC page returned 403; neither was used.

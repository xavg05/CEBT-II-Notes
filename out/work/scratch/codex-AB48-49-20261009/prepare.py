from pathlib import Path
import math, re, json, pymupdf
ROOT=Path(__file__).resolve().parents[4]
BASE=ROOT/'out/work/scratch/codex-AB48-49-20261009'
AB=ROOT/'out/AB'

def verify():
    k1=k2=2.0
    l1,l2=.14,.035
    rounded_m=k1/l1; rounded_p=k2*rounded_m/l2
    lm=math.log(2)/5; mu=math.log(2)/20
    exact_m=k1/lm; exact_p=k2*exact_m/mu
    corrected_m=k1/(lm+mu); corrected_p=k2*corrected_m/mu
    assert abs(k1-l1*rounded_m)<1e-12
    assert abs(k2*rounded_m-l2*rounded_p)<1e-12
    assert abs(math.exp(-lm*5)-.5)<1e-12
    assert abs(math.exp(-mu*20)-.5)<1e-12
    assert abs(k2*rounded_m-l2*rounded_p)<1e-12
    out=dict(rounded_mRNA=rounded_m,rounded_protein=rounded_p,protein_per_mRNA=k2/l2,
             exact_lambda_m=lm,growth_mu=mu,exact_mRNA=exact_m,exact_protein=exact_p,
             intrinsic5min_plus_dilution_mRNA=corrected_m,intrinsic5min_plus_dilution_protein=corrected_p,
             corrected_mRNA_effective_half_life=math.log(2)/(lm+mu),transcription_seconds=1000/30,
             approximate_amino_acid_length=1000/3,translation_seconds=(1000/3)/10,rounded_loss_mRNA=l1*rounded_m,
             rounded_loss_protein=l2*rounded_p,fraction_at_5min=1-math.exp(-lm*5))
    # Finite-difference independent check of the derived mRNA step response.
    mss=k1/lm
    for t in [1,5,20]:
        h=1e-4
        f=lambda x:mss*(1-math.exp(-lm*x))
        assert abs((f(t+h)-f(t-h))/(2*h)-(k1-lm*f(t)))<1e-8
    # Demand-rule toy model: positive minus negative error load.
    for demand in [.2,.5,.8]:
        positive=1-demand; negative=demand
        assert math.isclose(positive-negative,1-2*demand)
    return out

NUMBERS=verify()
(BASE/'verification-output.json').write_text(json.dumps(NUMBERS,indent=2)+'\n')
(AB/'AB-48-gene-expression-kinetics-and-steady-state.md').write_text(r'''# Section 48: Kinetics of gene expression and steady state

## Overview

DNA provides the template, but the amount of a protein depends on how often that template is transcribed, how often each message is translated, and how quickly messages and proteins disappear. This note connects those mechanisms to production–loss balances and estimates steady mRNA and protein copy numbers for an expressed bacterial gene.

*Assumed:* transcription, translation, exponential growth and first-order rate equations.

## Intuition

![Information passes from DNA through mRNA to protein](figs/AB-48-expression-pathway.png)

RNA polymerase (RNAP) repeatedly makes messenger RNA (mRNA) from a gene. Ribosomes repeatedly translate each message: translation does not consume the mRNA. Ribonucleases destroy messages, while proteins can disappear through proteolysis or become distributed among an increasing number of cells as the population grows.

*Analogy:* a workshop copies instructions, and each copy supports repeated manufacture until discarded. Keeping more copies increases production. The analogy fails at dilution: an intact protein can become less abundant per cell without being destroyed, because the workshop population grows and divides.

A steady abundance is therefore a **dynamic balance**, with continual synthesis replacing losses. It is not chemical equilibrium. Cells express different subsets of their genes because unnecessary transcription and translation consume resources; the active subset depends on the environment, not on a fixed universal fraction.

## Derivation

### Production and loss

Let $t$ be time in minutes, $m$ the mean number of messages for one gene per cell, and $p$ the mean number of its protein molecules per cell. Take one effective gene copy per cell, constant growth conditions, unsaturated machinery and negligible synthesis delays. Let $k_1$ be the transcription rate in messages cell$^{-1}$ min$^{-1}$, and $k_2$ the translation rate in proteins message$^{-1}$ min$^{-1}$. For one gene copy, $k_1$ is numerically the rate per gene. Let $\lambda_1$ and $\lambda_2$ be the effective message and protein loss constants, both in min$^{-1}$.

Over a short interval $dt$, synthesis adds $k_1dt$ messages and first-order loss removes $\lambda_1m\,dt$. Subtracting loss from production and dividing by $dt$ gives

$$\frac{dm}{dt}=k_1-\lambda_1m. \tag{1}$$

Each of the $m$ messages produces proteins at rate $k_2$, so total protein production is $k_2m$. Applying the same balance gives

$$\frac{dp}{dt}=k_2m-\lambda_2p. \tag{2}$$

The factor $m$ is essential: $k_2$ alone is a rate **per message**, not a rate per cell. Every term in (2) has units of proteins cell$^{-1}$ min$^{-1}$.

### Why dilution enters a loss constant

Let $N$ be the number of cells, $P$ the total number of the protein molecules in the population, $\mu$ the exponential population growth constant, and $\delta_p$ the intrinsic protein degradation constant. Then $dN/dt=\mu N$. Production by all cells is $Nk_2m$, so $dP/dt=Nk_2m-\delta_pP$. Since $p=P/N$, the quotient rule gives

$$\frac{dp}{dt}=\frac{1}{N}\frac{dP}{dt}-\frac{P}{N^2}\frac{dN}{dt}
=k_2m-\delta_pp-\mu p
=k_2m-(\delta_p+\mu)p. \tag{3}$$

Thus $\lambda_2=\delta_p+\mu$: the last term appears because the denominator grows. Applying the identical population balance to messages gives $\lambda_1=\delta_m+\mu$, where $\delta_m$ is their intrinsic degradation constant. This is a population mean approximation; molecule numbers in a single lineage jump at division rather than undergoing smooth dilution.

### Half-life and steady state

For a species of abundance $n$ after its production has stopped, $dn/dt=-\lambda n$. Separating variables gives $dn/n=-\lambda\,dt$. Integrating from initial abundance $n_0$ at $t=0$ yields $\ln(n/n_0)=-\lambda t$, hence $n=n_0e^{-\lambda t}$. At the half-life $t_{1/2}$, substitute $n/n_0=1/2$ and take natural logarithms:

$$-\ln2=-\lambda t_{1/2}
\quad\Rightarrow\quad \lambda=\frac{\ln2}{t_{1/2}}. \tag{4}$$

For a stable protein, $\delta_p\simeq0$, so its effective dilution half-life equals the population doubling time $T_d$: $\mu=\ln2/T_d$. This does not mean the protein is chemically degraded within that time.

At steady state, indicated by a superscript $*$, set the left-hand side of (1) to zero. Moving the loss term to the other side and dividing by $\lambda_1$ gives $m^*=k_1/\lambda_1$. Do the same in (2), then substitute this message abundance:

$$m^*=\frac{k_1}{\lambda_1},\qquad
p^*=\frac{k_2m^*}{\lambda_2}
=\frac{k_1k_2}{\lambda_1\lambda_2}. \tag{5}$$

To see how messages approach the balance, subtract $m^*$ from (1). For $u=m-m^*$, $du/dt=-\lambda_1u$, whose exponential solution above gives

$$m(t)=m^*+[m(0)-m^*]e^{-\lambda_1t}. \tag{6}$$

Starting from zero, $m(t)=m^*(1-e^{-\lambda_1t})$. At $t_{1/2}$ it has reached half its eventual value. Protein production still depends on this changing message pool, so protein accumulation is generally not a single exponential from switch-on.

## Motivation and explanation

Longer message survival allows more templates to accumulate; longer protein survival allows more products to accumulate. This explains why the two loss constants multiply in the denominator of (5). With fixed losses, doubling transcription doubles both abundances, while changing translation affects protein abundance directly.

If production stops, abundance decays to zero when the corresponding loss constant is positive. If a species has no loss and positive production, it accumulates rather than reaching a finite steady state. The deterministic means also hide fluctuations, especially when message counts are small. Resource limitation, changing gene dosage, growth-dependent synthesis rates and feedback invalidate the constant-parameter approximation.

**Elongation speed is not initiation frequency.** A coding sequence of approximately 1,000 nucleotides takes about 33.3 s to transcribe at 30 nt s$^{-1}$; ignoring the stop codon, translation of its approximately 333 amino acids at 10 amino acids s$^{-1}$ also takes about 33.3 s. These transit times do not establish $k_1$ or $k_2$: several polymerases can occupy one gene and several ribosomes can occupy one message. Promoter initiation and the ribosome-binding site control the effective production rates.

## Worked example

**Assume** $k_1=2$ messages cell$^{-1}$ min$^{-1}$ and $k_2=2$ proteins message$^{-1}$ min$^{-1}$ for one effective expressed gene copy. Use rounded effective loss constants $\lambda_1=0.14$ min$^{-1}$ and $\lambda_2=0.035$ min$^{-1}$, associated approximately with half-lives of 5 min and 20 min. The protein is treated as stable, with loss dominated by growth.

![First-order decline reaches half the initial abundance at the half-life](figs/AB-48-first-order-loss.png)

Substitute into (5), retaining unrounded intermediate values:

$$m^*=\frac{2}{0.14}\approx14.3\ \text{messages cell}^{-1},$$

$$p^*=\frac{2(2/0.14)}{0.035}\approx816\ \text{proteins cell}^{-1}.$$

The ratio $p^*/m^*=k_2/\lambda_2\approx57.1$ is the steady protein-to-message abundance ratio. It is not the number of proteins translated during one message's lifetime. At this balance, message loss is 2 messages cell$^{-1}$ min$^{-1}$ and protein loss is approximately 28.6 proteins cell$^{-1}$ min$^{-1}$, matching their respective production rates.

**What do the half-lives mean?** Using exactly $\lambda_1=\ln2/5$ and $\lambda_2=\ln2/20$ gives approximately 14.4 messages and 833 proteins per cell; the difference from 816 reflects rounding. If 5 min instead denotes the **intrinsic degradation half-life** of messages in a population doubling every 20 min, dilution must also enter their balance: $\lambda_1=\ln2/5+\ln2/20$. The effective message half-life is then 4.00 min, and (5) gives approximately 11.5 messages and 666 proteins per cell. Adding dilution to an already effective half-life would double-count it.

These are illustrative abundances for an expressed gene under specified rates, not averages that apply to every gene in a bacterial genome.

## Link to other topics

These balances connect gene expression to the production and removal equations used in bioprocessing. Transcriptional regulation makes $k_1$ depend on signals and regulatory proteins, turning a constant-rate model into a gene regulatory network.

## Conclusion

An expression level records both production and survival. Keeping transcription per gene, translation per message, intrinsic degradation and growth dilution distinct provides the basis for understanding how regulatory proteins change gene output.
''')

(AB/'AB-49-transcriptional-regulation-and-lac-operon.md').write_text(r'''# Section 49: Transcriptional regulation and the lac operon

## Overview

Bacteria control transcription by changing which promoters RNA polymerase recognises and how readily it initiates at them. Sigma factors coordinate broad programmes; specific repressors and activators tune individual transcription units. The lac operon illustrates how a metabolic signal changes a regulator's activity and how different regulatory mechanisms combine into a useful response.

*Assumed:* transcription, protein–DNA binding and the production–loss model of gene expression.

## Intuition

A **promoter** is a DNA region at which RNA polymerase (RNAP) initiates transcription. An **operator** is a DNA binding site for a regulatory protein; it may overlap the promoter or lie nearby. The promoter and operator are sequences, whereas the proteins that read them can change in abundance or activity.

*Analogy:* sigma factors provide RNAP with an address guide, repressors close selected doors and activators help it enter. The analogy fails because binding is reversible and probabilistic: promoters usually have graded initiation rates, not perfectly binary gates. Regulators can also affect DNA opening and promoter escape, rather than simply permitting physical access.

The pathway is **environmental signal → regulator activity → productive transcription → mRNA → protein → cellular function**. Regulation saves biosynthetic resources, supports adaptation and coordinates developmental changes where those occur. Regulatory proteins are themselves gene products, so one regulator can control the production of another and create a network.

## Derivation

### From DNA recognition to transcription rate

![Promoter recognition and the distinction between transcription start and translation start](figs/AB-49-promoter-layout.png)

**First, assemble a promoter-recognising enzyme.** A sigma factor $\sigma$ binds the core RNAP to make the holoenzyme. For many promoters recognised by the principal bacterial factor $\sigma^{70}$, the important elements are centred near positions $-35$ and $-10$, measured upstream from the transcription start at $+1$. The consensus sequences TTGACA and TATAAT are reference patterns, not compulsory exact sequences at every promoter. Sigma contacts these elements and helps establish an open DNA complex from which RNA synthesis can begin.

**Next, select a programme.** Changing the available sigma factors changes the set of promoters efficiently recognised by RNAP. In *E. coli*, $\sigma^{70}$ supports much routine growth expression, $\sigma^{32}$ the cytoplasmic heat-shock response, and $\sigma^S$ much stationary-phase and stress expression. Such programmes overlap; a sigma factor does not guarantee expression of every compatible gene.

**Then, tune specific promoters.** A repressor bound at an operator can interfere with productive initiation. An activator bound nearby can recruit RNAP or facilitate initiation. Binding-site placement and protein interactions determine the mechanism. The ribosome-binding site (RBS) lies in the message and controls translation initiation; it is distinct from the promoter and from the start codon that defines the protein reading frame.

![Repressor binding obstructs productive transcription while activator binding promotes it](figs/AB-49-repression-activation.png)

Let $k_1$ denote the mean transcription rate per effective gene copy in messages min$^{-1}$. For a minimal two-state promoter, let $f$ be the fraction of time in a transcription-permissive state, $k_{\mathrm{on}}$ its productive transcription rate in that state, and $k_{\mathrm{off}}$ the rate in the other state. The state fractions sum to one, so averaging the rates gives

$$k_1=fk_{\mathrm{on}}+(1-f)k_{\mathrm{off}}. \tag{1}$$

With negligible residual transcription, set $k_{\mathrm{off}}\simeq0$ to obtain $k_1\simeq fk_{\mathrm{on}}$. Regulators change $f$, and can also change the state-specific rates. Equation (1) is an illustrative average, not a complete quantitative model of a real promoter with multiple binding sites.

### The sign of control and the sign of the signal

A transcriptional **repressor** lowers output when its active form binds DNA: its regulatory edge is drawn with a blunt end. An **activator** raises output when bound: its edge is drawn with an arrowhead. These signs describe the regulator's effect, not necessarily the effect of a signal on the gene.

**Allostery** means that binding a signal at one site changes a protein's conformational preferences and its activity at another site. A signal that weakens a repressor increases transcription by removing inhibition; a signal that activates an activator also increases transcription. Both implement an inducing response despite opposite signs of DNA-level control. Conversely, a signal can strengthen a repressor or disable an activator and thereby reduce transcription.

## Motivation and explanation

**Why retain both positive and negative control?** The same signal–output relationship can be built with either an activator or a repressor. The **demand rule** is an evolutionary tendency: genes needed near their high expression level for much of the natural environment tend towards positive control; rarely needed genes tend towards negative control.

One proposed explanation assumes that an unoccupied regulatory site is more vulnerable to inappropriate binding than a site occupied by its intended regulator. High demand favours an activator occupying its site while output is high; low demand favours a repressor occupying its site while output is low. This protects the state most often required. It is a conditional explanation, not a universal design law: costs, binding specificity, history and multiple regulators can change the choice. In engineering, desired basal expression, response range and host compatibility matter alongside demand.

Removing a repressor therefore permits transcription without necessarily producing maximal transcription. A suitable sigma factor, accessible promoter and any required activator must still be present. Regulatory occupancy changes rapidly, but protein abundance responds with the synthesis and loss timescales of the expression balances.

## Worked example

### How lactose induces the lac operon

The **lac operon** is a bacterial transcription unit producing a message with several protein coding regions: **lacZ** encodes $\beta$-galactosidase, **lacY** a lactose permease, and **lacA** a thiogalactoside acetyltransferase associated with detoxification of some non-metabolised galactosides. The **lacI** gene has its own promoter and supplies the LacI repressor.

![Allolactose shifts LacI towards a state with weaker operator binding](figs/AB-49-lac-allostery.png)

**Without lactose**, LacI binds the lac operator region and strongly represses transcription. Its ability to bind additional operators and loop DNA strengthens repression. Repression is incomplete, leaving low basal production of LacY and LacZ.

**When lactose is available**, basal LacY imports it, and LacZ both hydrolyses lactose and converts some into **allolactose**. Allolactose binds LacI away from its DNA-binding surface and reduces operator affinity through allostery. Operator occupancy falls and transcription becomes easier. The new LacY and LacZ support further uptake and processing; induction does not require a chemically impossible first step with absolutely no permease or enzyme present.

**The carbon-source context also matters.** The activator CAP, also called CRP (cAMP receptor protein), responds to cyclic AMP (cAMP). In the usual simplified glucose–lactose comparison, low glucose supports greater cAMP–CAP activation. Bound CAP helps productive initiation at the lac promoter. Thus lactose relieves negative control, while low glucose supports positive control.

| Lactose available | Glucose available | LacI repression | cAMP–CAP activation | Qualitative lac output |
|---|---|---|---|---|
| No | Yes | Strong | Weak | Very low |
| No | No | Strong | Strong | Low: activation does not remove repression |
| Yes | Yes | Relieved if intracellular inducer accumulates | Weak | Limited |
| Yes | No | Relieved | Strong | High |

The high-output response resembles “lactose present AND glucose scarce”. It is an approximate logic description: intracellular inducer, DNA looping and interactions between CAP and LacI affect the graded response. Glucose can also restrict lactose uptake through inducer exclusion, so external lactose alone does not guarantee induction.

**A conceptual perturbation.** Deleting lacI removes the lactose-sensitive brake, but the native lac promoter still responds to CAP and carbon-source conditions. Deleting crp removes CAP activation; relieving LacI alone then cannot restore the normal high-output state. The two controls answer different questions: is lactose available, and should the cell invest strongly in using it?

Signals can also reach transcription factors by phosphorylation rather than direct ligand binding. For example, extracellular glucose-6-phosphate is sensed through the Uhp membrane signalling system, activating the response regulator UhpA and transcription of the transporter gene uhpT. The same environmental-input-to-transcription logic can therefore use different molecular mechanisms.

## Link to other topics

Promoter and RBS design connect DNA assembly to controlled protein production. Linking regulated promoters to genes encoding further regulators creates feedback, switches and oscillators, whose dynamics depend on both regulatory interactions and molecular lifetimes.

## Conclusion

Sigma factors establish promoter recognition, specific transcription factors tune productive initiation, and signals change the active state of those factors. The lac operon combines relief of repression with activation to connect resource availability to enzyme production; those same components can be recombined into synthetic circuits.
''')

# Final structural checks apply only to the two owned new notes.
expected=['Overview','Intuition','Derivation','Motivation and explanation','Worked example','Link to other topics','Conclusion']
checks=[]
for number in [48,49]:
    files=list(AB.glob(f'AB-{number}-*.md')); assert len(files)==1, files
    p=files[0]; text=p.read_text()
    assert text.startswith(f'# Section {number}:')
    assert re.findall(r'^## (.+)$',text,re.M)==expected
    tags=[int(x) for x in re.findall(r'\\tag\{(\d+)\}',text)]
    assert tags==list(range(1,len(tags)+1)), tags
    assert not re.search(r'\[\[|^>\s*\[!',text,re.M)
    assert not re.search(r'lecture|lecturer|slides|source PDF',text,re.I)
    links=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',text)
    for link in links:
        image=p.parent/link; assert image.exists()
        pix=pymupdf.Pixmap(str(image)); assert pix.width>0 and pix.height>0
    assert text.count('$$')%2==0
    checks.append({'file':str(p.relative_to(ROOT)),'words':len(text.split()),'equations':tags,'images':links,'structure':'PASS'})
(BASE/'validation-output.json').write_text(json.dumps(checks,indent=2)+'\n')
progress=ROOT/'out/work/progress/codex-AB48-49-L13-20261009.md'
progress.write_text('''# Codex: Lecture13 reading and AB-48/49 verification

Scope: AB-48 and AB-49 only. No BOARD, PLAN, CLAUDE, existing AB-01–47, merges, or commits changed.
Checked shared OCR/progress before processing: no Lecture13 transcript or progress file existed. Existing AB-U13a scratch directory was empty.
Visually opened PDF pages 5–7, 9–19 at 1.7x; equation areas on 6–7 additionally viewed at 3x. Full page 15 read for context only; circuit dynamics belong to AB-52. All figures cropped using PyMuPDF at 4x. Reopened corrected graph, promoter and LacI crops before delivery.

## Source mapping

- AB-48: Lecture13.pdf pages 5–7, 9–10; transcript-protein model, half-lives, illustrative steady abundance and resource allocation.
- AB-49: pages 11–18 and summary page 19; sigma factors, promoter/operator/RBS, signed regulation, allostery, lac, Uhp signalling and demand rule.
- Figure crop manifest: AB-48-expression-pathway p5 (88,127,252,308); AB-48-first-order-loss p6 (153,532,305,659); AB-49-promoter-layout p12 (58,528,536,707); AB-49-repression-activation p14 (76,126,517,344); AB-49-lac-allostery p17 (78,130,189,302). Coordinates in PDF points.

## External primary sources actually opened and read

- https://pmc.ncbi.nlm.nih.gov/articles/PMC2818994/ — Klumpp, Zhang & Hwa (2009), Growth-rate dependent global effects on gene expression in bacteria. Read results/global parameter model and growth dependence. Clarifies intrinsic degradation, growth dilution, gene copy number, volume and conditional growth-rate assumptions.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5567806/ — Zuo & Steitz (2015), Crystal structures of the E. coli transcription initiation complexes with a complete bubble. Read introduction and promoter-recognition results: sigma recognition, open complex, promoter spacer and initiation/escape.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC1389706/ — Shinar et al. (2006), Rules for biological regulation based on error minimization. Read introduction and results for the demand rule, positive/negative control and conditional nonspecific-binding explanation.
- https://arxiv.org/pdf/q-bio/0703056 — Kuhlman et al. (2007), author manuscript of Quantitative characterization of combinatorial transcriptional control of the lactose operon of E. coli. Read introduction and repression/activation/combinatorial results. CAP/cAMP, LacI, inducer feedback and DNA-looping limitations of binary logic.
- https://journals.asm.org/doi/10.1128/jb.128.1.510-513.1976 — Andrews & Lin (1976), Thiogalactoside transacetylase of the lactose operon as an enzyme for detoxification. Publisher abstract only retrieved and read: lacA product identity and selective benefit with non-metabolizable analogues; full text not claimed.

## Retrieval limitations

PMC3847955, PMC1851613 and PMC232886 returned browser checks; NCBI Bookshelf NBK26872 returned a browser check. https://matisse.ucsd.edu/~hwa/pub/Lac.pdf and arXiv HTML q-bio/0703056 failed. These were not used as read sources. Kuhlman author PDF succeeded as above; LacA publisher abstract succeeded.

## Corrections and assumptions

1. Protein production term corrected to k2*m when p denotes protein per cell and k2 is protein per message per minute; source omits m and temporarily labels p per message.
2. The 20-min protein lifetime is effective growth dilution for a stable protein, not obligatory proteolysis. Message intrinsic degradation and effective loss are separated; no double-counting dilution.
3. Source rounded lambda values yield 14.285714 messages and 816.326531 proteins. Exact effective half-lives yield 14.426950 and 832.547592. If 5 min is intrinsic message degradation with 20-min doubling, results become 11.541560 and 666.038074.
4. Transit/elongation time does not determine initiation frequency. k1=k2=2 are assumptions for the illustrative calculation.
5. Corrected lacA annotation: acetyltransferase rather than activator of LacZ; crop excludes the erroneous annotation and shows only allostery.
6. Fixed quarter-genome expression treated as condition-dependent illustration, not universal census. Inconsistent source gene totals omitted rather than inventing an annotation version.
7. Demand rule labelled conditional evolutionary tendency. Lac input table is graded qualitative logic; intracellular induction, resource state, DNA looping and inducer exclusion limit it.

## Reproducible validation

Run python3 out/work/scratch/codex-AB48-49-20261009/prepare.py. The script writes only its own notes and scratch/progress files. verification-output.json records every numerical calculation. It asserts steady-state residuals, half-lives and an independent finite-difference check of the mRNA response. validation-output.json checks seven H2 sections in exact order, Section NN titles, sequential local tags, existing decodable figure links, balanced display-math delimiters and absence of source narration, wikilinks or callouts. Parent handles KaTeX rendering and merged equation-reference integration.
''')
print(json.dumps(NUMBERS,indent=2))
print(json.dumps(checks,indent=2))

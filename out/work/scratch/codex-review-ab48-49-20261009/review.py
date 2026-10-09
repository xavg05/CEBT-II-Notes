from pathlib import Path
import math, json, re, hashlib
import pymupdf
ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).resolve().parent
files=[ROOT/'out/AB/AB-48-gene-expression-kinetics-and-steady-state.md',ROOT/'out/AB/AB-49-transcriptional-regulation-and-lac-operon.md']
texts=[p.read_text() for p in files]
hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
k1=k2=2.0
cases={}
for name,l1,l2 in [('rounded',0.14,0.035),('exact_effective',math.log(2)/5,math.log(2)/20),('intrinsic_plus_dilution',math.log(2)/5+math.log(2)/20,math.log(2)/20)]:
    m=k1/l1
    p=k2*m/l2
    result={'lambda1_per_min':l1,'lambda2_per_min':l2,'mRNA_per_cell':m,'protein_per_cell':p,'protein_message_ratio':p/m,'mRNA_effective_half_life_min':math.log(2)/l1,'protein_effective_half_life_min':math.log(2)/l2,'mRNA_production_per_cell_min':k1,'mRNA_loss_per_cell_min':l1*m,'protein_production_per_cell_min':k2*m,'protein_loss_per_cell_min':l2*p}
    assert math.isclose(k1,l1*m) and math.isclose(k2*m,l2*p)
    cases[name]=result
assert round(cases['rounded']['mRNA_per_cell'],1)==14.3
assert round(cases['rounded']['protein_per_cell'])==816
assert round(cases['exact_effective']['mRNA_per_cell'],1)==14.4
assert round(cases['exact_effective']['protein_per_cell'])==833
assert round(cases['intrinsic_plus_dilution']['mRNA_per_cell'],1)==11.5
assert round(cases['intrinsic_plus_dilution']['protein_per_cell'])==666
assert math.isclose(cases['intrinsic_plus_dilution']['mRNA_effective_half_life_min'],4)
# Independent arbitrary population values test the quotient-rule balance (3).
N,P,m,mu,delta=37.0,913.0,4.7,0.031,0.008
population_derivative=(N*k2*m-delta*P)/N-P*(mu*N)/N**2
per_cell_derivative=k2*m-(delta+mu)*(P/N)
assert math.isclose(population_derivative,per_cell_derivative)
# Differentiate the independently solved linear ODE at unrelated initial counts.
trajectory=[]
l1=0.14
mstar=k1/l1
for m0 in [0.0,3.1,24.0]:
    for t in [0.0,2.3,10.0,50.0]:
        mt=mstar+(m0-mstar)*math.exp(-l1*t)
        derivative=-l1*(m0-mstar)*math.exp(-l1*t)
        rhs=k1-l1*mt
        assert math.isclose(derivative,rhs,abs_tol=1e-12)
        trajectory.append({'m0':m0,'t_min':t,'m':mt,'derivative_residual':derivative-rhs})
for l in [0.14,0.035,math.log(2)/5+math.log(2)/20]:
    assert math.isclose(math.exp(-l*(math.log(2)/l)),0.5)
assert math.isclose(mstar*(1-math.exp(-l1*(math.log(2)/l1))),mstar/2)
transit={'transcription_1000_nt_at_30_nt_per_s':1000/30,'translation_1000_over_3_aa_at_10_aa_per_s':(1000/3)/10}
structure=[]
for path,text in zip(files,texts):
    expected=6 if path.name.startswith('AB-48') else 1
    tags=[int(x) for x in re.findall(r'\\tag\{(\d+)\}',text)]
    assert tags==list(range(1,expected+1))
    headings=re.findall(r'^## (.+)$',text,re.M)
    assert headings==['Overview','Intuition','Derivation','Motivation and explanation','Worked example','Link to other topics','Conclusion']
    assert not re.search(r'\[\[|^>|lecture PDF|slides|lecturer',text,re.M|re.I)
    figures=[]
    for target in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',text):
        q=path.parent/target
        assert q.is_file()
        pix=pymupdf.Pixmap(q)
        figures.append({'relative_path':target,'width':pix.width,'height':pix.height})
    structure.append({'note':path.name,'tags':tags,'headings':headings,'figures':figures})
assert len(structure[0]['figures'])==2 and len(structure[1]['figures'])==3
assert all(hashlib.sha256(p.read_bytes()).hexdigest()==hashes[p.name] for p in files)
output={'reviewed_sha256':hashes,'cases':cases,'transit_times_s':transit,'quotient_rule_residual':population_derivative-per_cell_derivative,'trajectory_checks':trajectory,'static_checks':structure,'note_files_unchanged_by_review':True}
(HERE/'verification-output.json').write_text(json.dumps(output,indent=2)+'\n')
review=r'''# AB-U13-L13 cross-review — AB-48 and AB-49

Reviewer: Codex, independent bounded review, 2026-10-09.

**Result: no material findings requiring an owner fix.** Neither deliverable was edited. BOARD unchanged; no commits. Parent handles KaTeX rendering and merged reference integration.

## Evidence and scope

Read both current Markdown deliverables and shared `out/work/progress/codex-AB48-49-L13-20261009.md`. Did not reopen or reprocess Lecture13.pdf. Opened all five supplied PNGs directly and checked their content, crop boundaries and relative links. Independent script: `out/work/scratch/codex-review-ab48-49-20261009/review.py`; independent numerical/structural output: `verification-output.json` in that directory. The output records reviewed note hashes and confirms this script never writes the notes.

## Independent rederivation of all six AB-48 equations

1. During dt, message synthesis contributes k1 dt and first-order removal contributes lambda1 m dt. Dividing their net change by dt gives dm/dt = k1 - lambda1 m. Units: messages per cell per minute. Correct.
2. Each message supports k2 proteins per minute, hence m messages support k2 m. Protein balance is dp/dt = k2 m - lambda2 p. Translation does not consume m. Units: proteins per cell per minute throughout. Correct; the source's missing m is repaired.
3. For p=P/N, differentiate the quotient: p' = P'/N - PN'/N². Substitute P'=N k2 m - delta_p P and N'=mu N. This gives k2 m - (delta_p+mu)p, so intrinsic degradation and growth dilution add. An independently chosen numerical population state reproduces the same derivative. The same operation on total messages supplies lambda1=delta_m+mu. Correct under the stated population-mean approximation.
4. Solve n'=-lambda n by integration: ln(n/n0)=-lambda t. At n/n0=1/2, lambda=ln(2)/t_half. Positive lambda produces decay, and the survival fraction at the derived half-life is independently 0.5. Correct.
5. Set both balances to zero: lambda1 m*=k1 and lambda2 p*=k2 m*. Substitution yields m*=k1/lambda1 and p*=k1 k2/(lambda1 lambda2). Both stationary residuals vanish in every numerical example. Requires positive loss constants, as the text explicitly notes. Correct.
6. Subtract the particular constant solution m*; u=m-m* solves u'=-lambda1 u. Therefore m=m*+(m0-m*)exp(-lambda1 t). Initial condition recovered at t=0, derivative equals equation (1), and positive lambda1 gives convergence to m*. Tested for initial counts below and above equilibrium. From zero, the count reaches m*/2 after the loss half-life. Correct.

## Independent Python calculations

| Interpretation | lambda1 (min^-1) | lambda2 (min^-1) | Messages per cell | Proteins per cell |
|---|---:|---:|---:|---:|
| Rounded effective constants | 0.14 | 0.035 | 14.285714 | 816.326531 |
| Exact effective half-lives, 5 and 20 min | 0.138629436 | 0.034657359 | 14.426950 | 832.547592 |
| Intrinsic message half-life 5 min plus 20-min doubling | 0.173286795 | 0.034657359 | 11.541560 | 666.038074 |

All published rounded values agree: 14.3/816, 14.4/833, and 11.5/666. Third case effective message half-life is exactly 4 min. Rounded protein/message ratio is 57.142857; message loss/production is 2 per cell per minute and protein loss/production is 28.571429 per cell per minute. Both elongation transit examples give 33.333333 seconds, correctly distinct from initiation frequency. No dilution double-counting found.

## AB-49 signs, functions and examples

- LacI is a negative regulator; allolactose weakens its operator binding, giving a positive signal-to-output response through relief of repression. Basal LacY/LacZ avoids a circular requirement for induction. Operator looping and incomplete repression are stated.
- lacZ: beta-galactosidase; lacY: lactose permease; lacA: thiogalactoside acetyltransferase, with conditional detoxification role. lacI is separately transcribed. No mistaken LacA-as-activator claim remains.
- CAP/CRP is the cAMP-responsive activator. High lac output requires both relief of repression and activation in the simplified carbon-source comparison. All four qualitative table rows have the correct control signs; intracellular inducer accumulation and glucose-dependent inducer exclusion are acknowledged.
- lacI deletion removes the repressor brake but retains native CAP dependence. crp deletion removes activation, so derepression alone does not recover normal high output. Correct.
- The weighted two-state expression rate f k_on + (1-f) k_off follows directly from state occupancy fractions; its named rates are explicitly transcription rates, not promoter switching rate constants. Correct, and identified as illustrative.
- Sigma-factor/promoter/RBS distinctions and the conditional demand-rule explanation are coherent. No material finding in the ancillary Uhp signalling summary; this bounded review did not independently audit every sigma programme or Uhp biochemical step.

## Figures and document checks

Opened `AB-48-expression-pathway.png`, `AB-48-first-order-loss.png`, `AB-49-promoter-layout.png`, `AB-49-repression-activation.png`, and `AB-49-lac-allostery.png`. All decode, link relatively and retain relevant labels. The first-order-loss graph marks n0/2 and t_half consistently. Promoter figure distinguishes transcription start, start codon and stop codon; its spacer annotation need not equal the difference between the conventionally named -35 and -10 elements. Repression/activation diagram agrees with text signs. LacI figure shows the allolactose response; “inactive repressor” is schematic, while the prose correctly describes reduced operator affinity. No erroneous LacA annotation is visible.

Both files use Section NN titles, the seven required H2 headings, sequential local tags (AB-48: 1–6; AB-49: 1), and no wikilinks/callouts or source-PDF/lecturer narration. No new test files or edits were placed in deliverable folders.

## External cross-checks actually opened

- https://arxiv.org/pdf/q-bio/0703056 — Kuhlman et al., Quantitative Characterization of Combinatorial Transcriptional Control of the Lactose Operon of E. coli. Read introduction and regulator/inducer-response results to verify repression, CRP activation, uptake feedback and looping qualifications. No source equations transcribed.
- https://journals.asm.org/doi/10.1128/jb.128.1.510-513.1976 — Andrews & Lin, Thiogalactoside transacetylase of the lactose operon as an enzyme for detoxification. Publisher abstract read to cross-check LacA identity/function; full text not claimed.

No current blockers. No numerical or biological correction requested. Parent may proceed with its final rendering/integration checks.
'''
review_path=ROOT/'out/work/reviews/AB-U13-L13.md'
assert not review_path.exists(), 'Review path already exists; avoid overwriting another review.'
review_path.write_text(review)
print(json.dumps({'review':str(review_path.relative_to(ROOT)),'cases':cases,'transit_times_s':transit,'result':'no material findings','read_only_notes':True},indent=2))

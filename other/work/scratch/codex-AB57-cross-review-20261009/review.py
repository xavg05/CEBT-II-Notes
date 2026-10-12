from pathlib import Path
import hashlib, json, math, re, struct
root=Path(__file__).resolve().parents[4]
scratch=Path(__file__).resolve().parent
note=root/'out/AB/AB-57-synthetic-dna-rna-condensates.md'
text=note.read_text(); initial_hash=hashlib.sha256(note.read_bytes()).hexdigest()
# Recompute from input data independently of the author's verification code.
sequences=['CGATCG','GGGGCCCC','CAGATCTG','CCGATGCG','CGCG']
comp={'A':'T','T':'A','C':'G','G':'C'}
seq=[]
for s in sequences:
    rc=''.join(comp[b] for b in reversed(s))
    seq.append(dict(sequence=s,length=len(s),gc_percent=100*sum(b in 'GC' for b in s)/len(s),reverse_complement=rc,self_complementary=s==rc))
assert [x['self_complementary'] for x in seq]==[True,True,True,False,True]
assert seq[3]['reverse_complement']=='CGCATCGG'
rate_nt=250.; length_nt=250.; copies=25; stationary_count=30000.
transit=length_nt/rate_nt
production=copies/transit
loss=production/stationary_count
mean=1/loss
half=math.log(2)/loss
assert transit==1 and production==25 and mean==1200
assert math.isclose(mean/60,20)
assert math.isclose(math.exp(-loss*half),.5)
assert stationary_count*loss==production
# Eq 1: test the equilibrium free energy identity across arbitrary dimensionless
# DeltaG/(RT) values; no physical constants or experimental inputs assumed.
for ratio in [-5.,0.,2.]:
    K=math.exp(-ratio)
    assert abs(ratio+math.log(K))<1e-12
# Eq 2: independently check solution of production-loss balance, N(0)=0.
for t in [1.,120.,1200.,6000.]:
    f=lambda time:production/loss*(1-math.exp(-loss*time))
    h=.01
    slope=(f(t+h)-f(t-h))/(2*h)
    assert abs(slope-(production-loss*f(t)))<1e-7
# Eq 3: a constant hazard has survival S(t)=exp(-lambda*t).
# E[lifetime]=integral_0^infinity S(t)dt=1/lambda; approximate the integral
# in dimensionless x=lambda*t by Simpson quadrature, independent of N/s.
steps=10000; xmax=30.; dx=xmax/steps
integral=dx/3*(1+math.exp(-xmax)+sum((4 if i%2 else 2)*math.exp(-i*dx) for i in range(1,steps)))
mean_from_survival=integral/loss
assert abs(mean_from_survival-mean)<1e-8
# Eq 4: check cohort survival solves the loss-only ODE and starts at N0.
N0=30000.
for t in [0.,half,mean]:
    cohort=N0*math.exp(-loss*t)
    derivative=-loss*cohort
    assert math.isclose(derivative,-cohort/mean)
assert math.isclose(N0*math.exp(-half/mean),N0/2)
headings=re.findall(r'^## (.*)$',text,re.M)
assert headings==['Overview','Intuition','Derivation','Motivation and explanation','Worked example','Link to other topics','Conclusion']
tags=[int(n) for n in re.findall(r'\\tag\{(\d+)\}',text)]
assert tags==[1,2,3,4,5]
assert text.startswith('# Section 57:')
assert not re.search(r'lecturer|lecture\s*(?:PDF|slides|16)|source\s*PDF|\[\[|^>\s*\[!',text,re.I|re.M)
assert 'third offered choice' not in text
figures=[]
for link in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',text):
    p=note.parent/link
    data=p.read_bytes(); assert data[:8]==b'\x89PNG\r\n\x1a\n'
    width,height=struct.unpack('>II',data[16:24]); assert width>0 and height>0
    figures.append(dict(path=link,width=width,height=height))
assert len(figures)==5
result=dict(verdict='PASS',note_sha256=initial_hash,sequences=seq,
    transcript_time_s=transit,production_per_cell_per_s=production,
    effective_loss_per_s=loss,mean_lifetime_s=mean,mean_lifetime_min=mean/60,
    half_life_s=half,half_life_min=half/60,mean_from_survival_integral_s=mean_from_survival,
    steady_state_residual=production-loss*stationary_count,remaining_fraction_at_half_life=math.exp(-loss*half),
    equation_tags=tags,all_five_equation_checks='PASS',figures=figures,
    scope='Existing note and shared progress only; existing crops opened visually; no PDF processing or external-source rereading.')
(scratch/'independent-results.json').write_text(json.dumps(result,indent=2)+'\n')
review=root/'out/work/reviews/AB-U15.md'; review.parent.mkdir(parents=True,exist_ok=True)
review.write_text('''# AB-U15 cross-review — AB-57

Verdict: **PASS. No required corrections found.**

Reviewed read-only: out/AB/AB-57-synthetic-dna-rna-condensates.md and out/work/progress/codex-ab57-lecture16-20261009.md. Opened all five existing cropped PNGs. No new PDF rendering/reading, no edits to AB-57, figures, progress, ownership board or plans. Parent handles KaTeX and integration. The reported orphan “third offered choice” is already absent from the version reviewed.

## Equations and assumptions

1. DeltaG = DeltaG_standard + RT ln Q; at equilibrium Q=K and DeltaG=0, giving K=exp(-DeltaG_standard/RT). Dimensionless activity-based K explicitly stated; individual association correctly distinguished from a phase boundary.
2. Production-minus-first-order-loss balance dN/dt=s-lambda*N correct with fixed production and common constant hazard.
3. At steady state Nss=s/lambda, so Nss/s=1/lambda. For an exponential survival distribution, integration of survival yields the same mean lifetime; independently checked by Simpson quadrature. Steady state and first-order loss are explicit assumptions.
4. Separating the loss-only ODE yields exponential cohort survival N=N0*exp(-t/tau), with the correct sign and initial condition.
5. Setting survival to 1/2 yields half-life=tau*ln(2), not tau. Effective loss including cell-division dilution is correctly qualified as residence time rather than pure chemical degradation lifetime.

The numerical lifetime inference is conditional on one continuously active polymerase per plasmid, negligible initiation delay, complete transcripts counted one-for-one as nanostars, and steady-state first-order removal. Those assumptions are explicitly stated; elongation speed alone is not treated as initiation frequency. No molecular degradation lifetime is claimed from the gels or puncta.

## Independent example calculations

Transcript transit time: 250 nt / (250 nt/s) = 1.00 s.
Production under the stated occupancy: 25 / 1.00 = 25.0 nanostars per cell per second.
Effective loss constant: 25 / 30000 = 0.0008333333333333334 s^-1.
Mean lifetime: 1200 s = 20.0 min.
Half-life: 831.7766166719343 s = 13.862943611198906 min (13.9 min rounded).
Steady-state residual: zero; half-life survival fraction: 0.5.
All agree with the note. Results come from this reviewer's independent script, not the owner's saved outputs.

| Sequence, 5 prime to 3 prime | Reverse complement, 5 prime to 3 prime | Length | GC fraction | Self-complementary |
|---|---|---:|---:|---|
| CGATCG | CGATCG | 6 | 66.7% | Yes |
| GGGGCCCC | GGGGCCCC | 8 | 100.0% | Yes |
| CAGATCTG | CAGATCTG | 8 | 50.0% | Yes |
| CCGATGCG | CGCATCGG | 8 | 75.0% | No |
| CGCG | CGCG | 4 | 100.0% | Yes |

All five table rows match. The GGGGCCCC choice is explicitly an initial design judgement at comparable conditions, not a calculated melting or phase-separation temperature; folding, alternative association, concentration, geometry and bond exchange are appropriately qualified.

## Structure and figures

Title follows Section 57 convention. Exactly seven required H2 sections in order; local equation tags are 1 through 5. No source-PDF/lecturer narration, wikilinks or callouts. All five relative image links resolve to valid PNGs, and all five images were visually opened. Captions and surrounding text explain the scaffold, domains, transcription/capture, RNA designs and gel distinction. Source citations and retrieval limitations live in shared progress rather than deliverable narration.

## Review limits and reproducibility

Bounded review uses shared progress to establish source coverage; it does not independently certify every research claim against the inaccessible publisher pages, revisit source PDFs, or perform parent-owned KaTeX rendering. No current blocker or required owner action.

Independent script: out/work/scratch/codex-AB57-cross-review-20261009/review.py
Results: out/work/scratch/codex-AB57-cross-review-20261009/independent-results.json
''')
assert hashlib.sha256(note.read_bytes()).hexdigest()==initial_hash
print(json.dumps(result,indent=2))
print('Review saved:',review.relative_to(root))

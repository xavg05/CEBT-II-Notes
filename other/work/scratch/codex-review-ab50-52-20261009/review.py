from pathlib import Path
import math, json
BASE=Path(__file__).resolve().parent

def roots(f,lo=0,hi=5,steps=10000):
    found=[]; x=lo; fx=f(x)
    for i in range(1,steps+1):
        y=lo+(hi-lo)*i/steps; fy=f(y)
        if fy==0: found.append(y)
        if fx*fy<0:
            a,b=x,y
            for _ in range(70):
                m=(a+b)/2
                if f(a)*f(m)<=0:b=m
                else:a=m
            found.append((a+b)/2)
        x,fx=y,fy
    return found

# dx/dt = f(x)-gamma*x; local eigenvalue f'(x*)-gamma.
nar=lambda x:2/(1+x)-x
nar_x=roots(nar)[0]
nar_slope=-2/(1+nar_x)**2
par=lambda x:0.05+2*x*x/(1+x*x)-x
par_roots=roots(par)
par_derivative=lambda x:4*x/(1+x*x)**2

# Equal calibrated reporter means; population moments (same denominator throughout).
c=[8.,12.,8.,12.]; y=[6.,10.,10.,14.]
mean=lambda v:sum(v)/len(v)
mu=mean(c); assert mu==mean(y)
variance=lambda v:mean([(a-mean(v))**2 for a in v])
cov=mean([(a-mu)*(b-mu) for a,b in zip(c,y)])
eta_int=mean([(a-b)**2 for a,b in zip(c,y)])/(2*mu**2)
eta_ext=cov/mu**2
eta_total=mean([variance(c),variance(y)])/mu**2
assert math.isclose(eta_int+eta_ext,eta_total)

# Pure delayed negative feedback: ddelta/dt=-gamma*delta(t)-g*delta(t-tau).
gamma=1.; g=2.
omega=math.sqrt(g*g-gamma*gamma)
tau=math.acos(-gamma/g)/omega
real=gamma+g*math.cos(omega*tau)
imag=omega-g*math.sin(omega*tau)
assert abs(real)<1e-12 and abs(imag)<1e-12

# Three identical protein-only repressors: lambda=-gamma-g*z,
# z is a cube root of unity. Complex pair real part=-gamma+g/2.
ring=[]
for gain in [1.,2.,3.]:
    ring.append({'gain':gain,'real_eigenvalue':-gamma-gain,
                 'complex_pair_real':-gamma+gain/2,
                 'complex_pair_imag_abs':math.sqrt(3)*gain/2})

result={
 'negative_autoregulation':{'root':nar_x,'production_slope':nar_slope,
    'local_eigenvalue':nar_slope-1,'relaxation_time':1/(1-nar_slope)},
 'positive_autoregulation':[{'root':x,'production_slope':par_derivative(x),
    'local_eigenvalue':par_derivative(x)-1} for x in par_roots],
 'dual_reporter':{'mean_C':mu,'mean_Y':mean(y),'variance_C':variance(c),
    'variance_Y':variance(y),'covariance':cov,'eta_int_squared':eta_int,
    'eta_ext_squared':eta_ext,'eta_total_squared':eta_total},
 'delayed_negative_feedback':{'gamma':gamma,'gain':g,'omega':omega,
    'first_critical_delay':tau,'characteristic_real_residual':real,
    'characteristic_imag_residual':imag},
 'protein_only_repressilator':ring,
}
(BASE/'independent-formula-output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

# Independent calculations for the parameter choices in the saved drafts.
lam=math.log(2)/30; K=100.; beta=2*lam*K
# Integrate dt=dx/[production(x)-loss(x)] from 0 to K/2 by composite Simpson.
def half_rise(steps):
    end=K/2; dx=end/steps
    integrand=lambda x:1/(beta/(1+(x/K)**2)-lam*x)
    return dx/3*(integrand(0)+integrand(end)+sum((4 if j%2 else 2)*integrand(j*dx) for j in range(1,steps)))
par_beta=4.; par_lambda=.01
par_low=(par_beta-math.sqrt(par_beta**2-4*par_lambda**2*K**2))/(2*par_lambda)
par_high=(par_beta+math.sqrt(par_beta**2-4*par_lambda**2*K**2))/(2*par_lambda)
par_slope=lambda x:par_beta*2*x*K*K/(K*K+x*x)**2
# Exact stationary covariance equations, independent of the lifetime rearrangement.
kon,koff,lm,lp,km,kp=.12,.18,.2,.02,10.,2.
a=kon+koff; q=kon/a; vg=q*(1-q); m=km*q/lm; p=kp*m/lp
cgm=km*vg/(a+lm); vm=m+km*cgm/lm
cgp=kp*cgm/(a+lp); cmp=(km*cgp+kp*vm)/(lm+lp); vp=p+kp*cmp/lp
cvp_moment=vp/p**2
tg,tm,tp=1/a,1/lm,1/lp
cvp_rate=1/p+lp/(m*(lm+lp))+(1-q)/q*lm*lp/((a+lm)*(lm+lp))*(1+lm/(a+lp))
cvp_life=1/p+1/m*tm/(tm+tp)+(1-q)/q*tm/(tm+tp)*tg/(tg+tp)*(tg+tp+tg*tp/tm)/(tg+tm)
assert math.isclose(cvp_moment,cvp_rate,rel_tol=1e-12)
assert math.isclose(cvp_moment,cvp_life,rel_tol=1e-12)
# Verify stationary moment residuals directly, including promoter/transcript products.
gm=cgm+q*m
assert abs(kon*m-(a+lm)*gm+km*q)<1e-10
assert abs(-2*lm*vm+2*km*cgm+2*lm*m)<1e-10
assert abs(-(a+lp)*cgp+kp*cgm)<1e-10
assert abs(-(lm+lp)*cmp+km*cgp+kp*vm)<1e-10
assert abs(-2*lp*vp+2*kp*cmp+2*lp*p)<1e-10
reporter_var=225.; reporter_cov=144.; reporter_mu=100.
ri2=(2*reporter_var-2*reporter_cov)/(2*reporter_mu**2)
re2=reporter_cov/reporter_mu**2; rt2=reporter_var/reporter_mu**2
assert math.isclose(ri2+re2,rt2)
delay_lam,delay_gain=.020,.060
wc=math.sqrt(delay_gain**2-delay_lam**2)
tc=math.acos(-delay_lam/delay_gain)/wc
assert abs(delay_lam+delay_gain*math.cos(wc*tc))<1e-12
assert abs(wc-delay_gain*math.sin(wc*tc))<1e-12
exact={
 'AB50':{'null_self_edges':519/424,'observed_enrichment':40/(519/424),
 'self_edge_sum':34+6,'lambda_per_min':lam,'beta_nM_per_min':beta,
 'nar_slope_at_K':-beta/(2*K),'local_half_relaxation_min':math.log(2)/(2*lam),
 'half_rise_1000_min':half_rise(1000),'half_rise_10000_min':half_rise(10000),
 'par_roots_nM':[0,par_low,par_high],
 'par_local_eigenvalues_per_min':[par_slope(x)-par_lambda for x in [0,par_low,par_high]]},
 'AB51':{'q':q,'lifetimes_min':[tg,tm,tp],'mean_mRNA':m,'mean_protein':p,
 'C_gm':cgm,'variance_mRNA':vm,'CV_mRNA_squared':vm/m**2,
 'CV_mRNA':math.sqrt(vm/m**2),'CV_mRNA_Poisson':math.sqrt(1/m),
 'C_gp':cgp,'C_mp':cmp,'variance_protein':vp,
 'CV_protein_squared_from_moments':cvp_moment,'CV_protein_squared_rate_form':cvp_rate,
 'CV_protein_squared_lifetime_form':cvp_life,'CV_protein':math.sqrt(cvp_moment),
 'protein_noise_terms':[1/p,lp/(m*(lm+lp)),cvp_moment-1/p-lp/(m*(lm+lp))],
 'reporter_mean_squared_difference':2*reporter_var-2*reporter_cov,
 'reporter_noise_amplitudes':[math.sqrt(ri2),math.sqrt(re2),math.sqrt(rt2)]},
 'AB52':{'omega_c_per_min':wc,'critical_delay_min':tc,'onset_period_min':2*math.pi/wc,
 'linear_20_min_delay_below_threshold':20<tc,
 'decay_switch_generations':[math.log2(1000/100),math.log2(2000/100)]},
}
(BASE/'draft-example-output.json').write_text(json.dumps(exact,indent=2)+'\n')
print('DRAFT EXAMPLES: '+json.dumps(exact,indent=2))

# Dimensionless transformation check for arbitrary non-steady physical states.
km_dim,lm_dim,lp_dim,K_dim,b_dim,beta_dim,n_dim=2.,.2,.03,100.,.04,5.,2.
alpha0=km_dim*b_dim/(lp_dim*K_dim*lm_dim)
alpha=km_dim*beta_dim/(lp_dim*K_dim*lm_dim)
B=lp_dim/lm_dim
for m_dim,p_dim,pj_dim in [(3.,40.,20.),(10.,100.,180.),(1.,5.,100.)]:
    M=km_dim*m_dim/(lp_dim*K_dim); P=p_dim/K_dim; Pj=pj_dim/K_dim
    dm=b_dim+beta_dim/(1+(pj_dim/K_dim)**n_dim)-lm_dim*m_dim
    dp=km_dim*m_dim-lp_dim*p_dim
    assert math.isclose(km_dim*dm/(lp_dim*K_dim*lm_dim),alpha0+alpha/(1+Pj**n_dim)-M,rel_tol=1e-12)
    assert math.isclose(dp/(K_dim*lm_dim),B*(M-P),rel_tol=1e-12)

import re,hashlib
ROOT=BASE.parents[3]
AB=ROOT/'out/AB'
files=[AB/'AB-50-network-motifs-and-autoregulation.md',
       AB/'AB-51-stochastic-gene-expression-and-noise.md',
       AB/'AB-52-feedback-delay-and-repressilator.md']
expected=[7,10,8]
struct=[]
for f,count in zip(files,expected):
    s=f.read_text(); tags=[int(x) for x in re.findall(r'\\tag\{(\d+)\}',s)]
    assert tags==list(range(1,count+1))
    assert re.findall(r'^## (.+)$',s,re.M)==['Overview','Intuition','Derivation','Motivation and explanation','Worked example','Link to other topics','Conclusion']
    assert not re.search(r'lecture|lecturer|slides|\.pdf|\[\[|^>\s*\[!',s,re.I|re.M)
    links=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',s)
    for link in links:assert (f.parent/link).is_file()
    struct.append({'file':str(f.relative_to(ROOT)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'local_tags':tags,'figure_links':links})
(BASE/'reviewed-files.json').write_text(json.dumps(struct,indent=2)+'\n')
report=ROOT/'out/work/reviews/AB-U13-L14.md'
report.parent.mkdir(parents=True,exist_ok=True)
report.write_text('''# AB-U13-L14 — independent cross-review

Reviewer: codex (independent numerical and formula audit). Date: 2026-10-09.

**PASS — no material findings in the reviewed AB-50–52 files.** No deliverable or figure was edited. This is a read-only review of the notes and shared work; only this review and reviewer-owned scratch files were written. No commit, board update or merge.

## Scope and evidence

Read all three saved notes and out/work/progress/codex-ab50-52-l14-20261009.md. Reused shared work; did not rerender or re-extract Lecture14.pdf. Opened all seven existing crops before and after writer regeneration. Used the already-downloaded potvin2016.xml for oscillator redesign and timing claims; no further external research or retrieval. Other historical provenance was checked against the writer's shared progress, not represented as an independently reread full external paper.

Reviewed files and exact SHA-256 snapshots are saved in reviewed-files.json. The reviewed filenames are AB-50-network-motifs-and-autoregulation.md, AB-51-stochastic-gene-expression-and-noise.md, and AB-52-feedback-delay-and-repressilator.md.

## AB-50: feedback and switching

PASS. Promoter-state normalisation, no-leak and basal Hill responses, production–loss balance and local linearisation are correct. The eigenvalue is f'(x_st)-lambda; positive lambda-f' gives a positive relaxation time. NAR shortens local relaxation, stable PAR lengthens it, and the text correctly avoids treating PAR as sufficient for bistability. A one-variable smooth deterministic autonomous balance cannot sustain a periodic orbit.

Sensitivity follows by implicit differentiation at fixed loss rate; the logarithmic sensitivities to beta and lambda are +1/(1+L) and -1/(1+L) under the explicitly no-leak assumptions. The effective Hill exponent is distinguished from literal binding stoichiometry, and the discontinuous threshold is not differentiated.

Independent Python: null expected self-arrows 1.2240566038; observed enrichment 32.67822736; lambda 0.0231049060/min; beta 4.6209812037 nM/min; local feedback half-relaxation 15 min. Integrated dt/dx from zero to half the endpoint using composite Simpson quadrature, independently of the writer's time-stepping implementation: 13.89287314995 min, converged across 1000 and 10000 intervals. Matches 13.89 min.

PAR roots are 0, 26.7949192431 and 373.2050807569 nM. Their local eigenvalues are -0.010000, +0.0086602540 and -0.0086602540/min, verifying stable/unstable/stable assignment. The discussion correctly distinguishes the zero-leak absorbing OFF state from a biologically leaky promoter.

## AB-51: telegraph moments and dual reporters

PASS. Re-derived the stationary promoter–transcript and promoter–protein covariance balances by event changes, including the fact that translation does not consume mRNA. Every stationary moment balance has zero residual at the example parameters. The protein CV-squared formula in rates and its lifetime-filtering form both agree with an independent calculation directly from covariances. Promoter-switching noise is correctly treated as intrinsic to the full stochastic cascade, and not automatically identified with the two-reporter extrinsic contribution.

Independent Python: q=0.4, tau_g=3.3333333333 min, tau_m=5 min, tau_p=50 min, mean mRNA=20 and mean protein=2000. C_gm=4.8, V_m=260, C_gp=30, C_mp=3727.2727272727, V_p=374727.2727272728. Thus CV_m²=0.65 and CV_m=0.8062257748; Poisson baseline CV=0.2236067977. Protein noise terms are 0.0005, 0.004545454545 and 0.088636363636, summing to 0.093681818182; CV_p=0.3060748572. All displayed rounded values agree.

For normalised matched reporters, E[r]=E[s]=1 and E[(r-s)^2]/2 equals the average variance minus covariance. Therefore the three identities in (10) are algebraically consistent. The physical intrinsic/extrinsic interpretation additionally requires matching conditional responses and conditional independence, which the note states. Equal-mean alternative expressions and adding squared amplitudes are correct. The draft example gives mean squared difference 162, intrinsic amplitude 0.09, extrinsic amplitude 0.12, and total amplitude 0.15. Independent illustrative reporter data also satisfy the identity. Measurement noise, reporter competition and unequal reporter kinetics are appropriately qualified.

Checks on limits: fixed ON promoter removes switching contribution; rapid switching suppresses it; protein lifetime limits are explicitly at fixed means, avoiding conflating mean changes with filtering. Inverse-rate lifetimes are not mislabelled as half-lives.

## AB-52: delay and repressilator

PASS. Linearisation gives s+lambda+a exp(-sT)=0 with a=-f'>0. The imaginary-axis real/imaginary equations, gain condition a>lambda, first critical delay, and finite-delay stability argument at a<=lambda are correct for nonnegative loss/gain and positive loss. Loss acts immediately while production uses the delayed input. The note correctly separates onset instability from guaranteed nonlinear limit cycles and requires an initial history.

Independent Python: omega_c=0.0565685424949/min, T_c=33.7755429428 min and onset period=111.0720734540 min. Substitution into both characteristic components gives negligible floating-point residuals. A 20 min delay is below the first crossing. All rounded answers agree.

Repressor wiring and index mapping are consistent: LacI inhibits TetR, TetR inhibits CI, and CI inhibits LacI. Independently transformed the dimensional six-state balances using the stated scales; both dimensionless equations and alpha0, alpha, B are correct. Tested arbitrary non-steady states to verify the transformed right-hand sides. The text correctly avoids claiming an odd repression ring guarantees oscillation and notes the effects of removing intermediate mRNA dynamics.

During dilution-only decline x=x0*2^(-G); threshold crossing gives log2(x0/K). Independent values are 3.3219280949 and 4.3219280949 generations for the two examples. The distinction between one decay segment and a complete circuit period is explicit.

Cached Potvin full text supports reporter copy-number effects, shared proteolysis effects, removing degradation, TetR titration-sponges, low-copy threshold noise, and generation-period robustness. The note does not impose deterministic cooperativity/delay requirements universally on noisy circuits or confuse a generation counter with a fixed clock in minutes. Phase modulo a cycle and the need for cycle counting are correctly qualified. The RINGS attribution is supported by the writer's recorded primary-source reading; it was not separately expanded or researched during this bounded review.

## Figures and format

Earlier pre-draft crops clipped AB50 axes/labels and retained quiz/question text in AB51. The writer regenerated these before final review; all seven current crops were reopened. Those findings are resolved, with complete relevant axes and no quiz narration in the dual-reporter crop. Some original image labels use notation such as theta or reporter names that differs from text examples; this does not affect the mechanism or numerical interpretation. Figures are illustrative, not treated as quantitative data for worked examples.

All three files use the Section NN H1 convention and the seven required H2 sections. Local tags are exactly 1–7, 1–10 and 1–8. Figure links resolve. No source-PDF/lecturer narration, wikilinks or callouts found. Parent owns KaTeX rendering and integrated equation renumbering; those were not duplicated here.

## Reviewer artifacts

- out/work/scratch/codex-review-ab50-52-20261009/review.py
- independent-formula-output.json (pre-draft general formula audit)
- draft-example-output.json (independent exact-example calculations)
- reviewed-files.json (reviewed hashes, local tags and links)

No changes requested. Ready for parent integration subject to its rendering checks.
''')
print('PASS: '+str(report.relative_to(ROOT)))

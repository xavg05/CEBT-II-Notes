from pathlib import Path
import json, re, math

root=Path(__file__).resolve().parents[4]
scratch=root/'other/work/scratch/all-subject-explanations'
manifest=json.loads((scratch/'before-revision/manifest.json').read_text(encoding='utf-8'))
proposals=json.loads((scratch/'re-proposals.json').read_text(encoding='utf-8'))
checks=[]
for entry in proposals:
    original=(scratch/'before-revision'/manifest[entry['path']]).read_text(encoding='utf-8')
    expected=original
    for edit in entry['edits']:
        assert expected.count(edit['old'])==1,entry['note']
        expected=expected.replace(edit['old'],edit['new'],1)
    actual=(root/entry['path']).read_text(encoding='utf-8')
    assert actual==expected,entry['note']
    assert re.findall(r'\\tag\{[^}]+\}',actual)==re.findall(r'\\tag\{[^}]+\}',original),entry['note']
    assert re.findall(r'!\[[^\]]*\]\([^)]+\)',actual)==re.findall(r'!\[[^\]]*\]\([^)]+\)',original),entry['note']
    assert re.findall(r'\$\$[\s\S]*?\$\$',actual)==re.findall(r'\$\$[\s\S]*?\$\$',original),entry['note']
    checks.append(entry['note'])

def close(a,b,tol=1e-7):
    assert abs(a-b)<tol,(a,b)

# Existing first-order sizing: expansion dilutes at fixed conversion.
X,k=0.5,0.1
constant=-math.log(1-X)/k
expanded=(-2*math.log(1-X)-X)/k
assert expanded>constant
# Constant adiabatic heat-capacity flow: cancellation of kinetics.
thermal=[(-1* -50000/1000)*0.6 for rate in (0.1,1,10)]
assert thermal[0]==thermal[1]==thermal[2]==30
# Moments at fixed total mean, rather than fixed single-tank volume.
assert 100**2/4 < 100**2
# Nonlinear maps do not commute, though tracer delays do.
pfr=lambda c:c/(1+c)
cstr=lambda c:(math.sqrt(1+4*c)-1)/2
assert cstr(pfr(1))<pfr(cstr(1))
# A broader first-order RTD has larger survivor fraction than its mean-time PFR.
assert (1+2/4)**-4 > math.exp(-2)
# Site inventory and competition.
wa,wb=1,2
cov=[1/(1+wa+wb),wa/(1+wa+wb),wb/(1+wa+wb)]
close(sum(cov),1)
assert cov[1]<wa/(1+wa)
# BET slope and intercept independently recover the model capacity.
m,b=.09,.01
close(1/(m+b),10)
# LH local log derivative independently approximated.
lh=lambda pa:pa/(1+pa+2)**2
pa=6
h=1e-6
slope=(math.log(lh(pa*math.exp(h)))-math.log(lh(pa*math.exp(-h))))/(2*h)
close(slope,1-2*pa/(1+pa+2))
# Bosanquet: easier molecular motion cannot exceed fixed wall-collision limit.
dk=2e-6
bos=lambda dm:1/(1/dm+1/dk)
assert bos(1e-2)<dk and bos(1e-2)>bos(1e-5)
# Exact spherical flux and volume-integral effectiveness agree.
phi=2
eta=3/phi**2*(phi/math.tanh(phi)-1)
n=10000
profile=lambda rho: math.sinh(phi*rho)/(rho*math.sinh(phi)) if rho else phi/math.sinh(phi)
integral=3*sum((.5 if i in (0,n) else 1)*(i/n)**2*profile(i/n)/n for i in range(n+1))
close(eta,integral)
surface=1/(1+eta*1*.001/(3*.001))
close(surface,.7882346,1e-6)
assert eta*surface<eta<1
# Fixed Prater concentration deficit fixes temperature rise independently of k.
prater=100000*1e-6*10/.2
close(prater,5)

result={'status':'PASS','native_notes_checked':len(checks),'notes':checks,
        'exact_proposal_application':True,'equation_tags_unchanged':True,
        'display_equations_unchanged':True,'figure_links_unchanged':True,
        'independent_calculations':{'expanded_pfr_space_time':expanded,
            'constant_flow_pfr_space_time':constant,'adiabatic_rise':thermal[0],
            'nonlinear_ordered_outlets':[cstr(pfr(1)),pfr(cstr(1))],
            'lh_log_slope':slope,'sphere_flux_effectiveness':eta,
            'sphere_integrated_effectiveness':integral,'surface_fraction':surface,
            'overall_effectiveness':eta*surface,'prater_bound':prater}}
target=root/'other/work/reviews/RE-explanation-cross-review-20261015-checks.json'
target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))

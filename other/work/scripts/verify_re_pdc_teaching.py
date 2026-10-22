"""Recompute recovered quantities and verify the modal rational identity."""
from pathlib import Path
import math,json
ROOT=Path(__file__).resolve().parents[3]
results={
 'first_order_fractions':{str(n):1-math.exp(-n) for n in [1,2,3,5]},
 'five_percent_settling_tau':-math.log(.05),
 'critical_at_tau':1-2/math.e,
 'three_lag_at_tau':1-2.5/math.e,
 'three_lag_at_three_tau':1-8.5*math.exp(-3),
 'valve_linear_endpoint':3.96+10*.038416,
 'valve_exact_endpoint':(100*.168+6.86*2)/(.168+6.86),
 'inverse_response_min_time':math.log(1.5),
 'inverse_response_min':1-4/1.5+3/1.5**2,
 'first_order_volume_ratio_at_point8':(.8/.2)/(-math.log(.2)),
 'nonlinear_pfr_then_cstr':1-(-1+math.sqrt(3))/2,
 'nonlinear_cstr_then_pfr':1-((math.sqrt(5)-1)/2)/(1+(math.sqrt(5)-1)/2),
 'arrhenius_500_505':math.exp(80000/8.314462618*(1/500-1/505)),
 'passive_tanks_tau':math.sqrt(20*80),
 'passive_tanks_zeta':(20+80)/(2*math.sqrt(20*80)),
 'gravity_equilibria':{'initial':(.02/.02)**2,'local':1+(2/.02)*.01,'exact':(.03/.02)**2},
}
expected={'critical_at_tau':.264241,'three_lag_at_tau':.0803014,'three_lag_at_three_tau':.576810,'valve_exact_endpoint':4.34263,'inverse_response_min_time':.405465,'first_order_volume_ratio_at_point8':2.48534,'nonlinear_pfr_then_cstr':.633975,'nonlinear_cstr_then_pfr':.618034,'arrhenius_500_505':1.20989}
for k,v in expected.items():assert math.isclose(results[k],v,rel_tol=5e-6), (k,results[k],v)
# Recombine the Laplace transforms of the recovered impulse-response modes.
errors=[]
for s in [.25+.7j, .8+1.3j,2+3j,5+0j,10+0j]:
 direct=1/(s*(s+1)**2*(s+2)*((s-1)**2+16))
 partial=1/(34*s)-1/(50*(s+2))-1/(100*(s+1))-1/(20*(s+1)**2)+((s-1)-1)/(1700*((s-1)**2+16))
 errors.append(abs((partial-direct)/direct))
 assert abs(partial-direct)<1e-12
 assert abs(s**6+2*s**5+14*s**4+60*s**3+81*s**2+34*s-s*(s+1)**2*(s+2)*((s-1)**2+16))<1e-7
results['modal_partial_fraction_max_relative_error']=max(errors)
(ROOT/'other/work/progress/re-pdc-teaching-numbers-20261022.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))

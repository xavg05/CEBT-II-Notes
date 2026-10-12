"""Recompute examples and independently check RTD integrals and balances."""
import json, math
from pathlib import Path

def integrate(f,a,b,n=20000):
    h=(b-a)/n
    return h/3*(f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*h) for i in range(1,n)))

values={}
values['RE01']={'r':0.01*100**2,'rA':-2*0.01*100**2,'rB':3*0.01*100**2,'renormalised_k':2*0.01}
k,Q,X=0.1,0.002,0.8
tc=X/(k*(1-X)); tp=-math.log1p(-X)/k
assert math.isclose(1/(1+k*tc),1-X)
assert math.isclose(math.exp(-k*tp),1-X)
values['RE02']={'tau_CSTR':tc,'tau_PFR':tp,'V_CSTR':Q*tc,'V_PFR':Q*tp}
X=0.5
tg=(-2*math.log1p(-X)-X)/k
assert math.isclose(tg,integrate(lambda x:(1+x)/(1-x)/k,0,X),rel_tol=1e-10)
values['RE03']={'flow_ratio':1+X,'CA':100*(1-X)/(1+X),'incorrect_CA':100*(1-X),'tau_PFR':tg,'tau_CSTR':X*(1+X)/(k*(1-X))}
values['RE04']={'temperature':300+50000*1*0.6/1000,'heat_release_W':50000*1*0.6}
values['RE05']={'N':100**2/2500,'tau_i':100/4,'standard_deviation':math.sqrt(2500),'early_fraction':-math.expm1(-1)}
rtd_checks=[]
for N in [1,4,10]:
    # Scale time by total mean, allowing a dimensionless integration.
    def E(t):return N**N*t**(N-1)*math.exp(-N*t)/math.factorial(N-1)
    area=integrate(E,0,40)
    mean=integrate(lambda t:t*E(t),0,40)
    variance=integrate(lambda t:(t-1)**2*E(t),0,40)
    survival=integrate(lambda t:math.exp(-2*t)*E(t),0,40)
    assert math.isclose(area,1,abs_tol=1e-9)
    assert math.isclose(mean,1,abs_tol=1e-9)
    assert math.isclose(variance,1/N,abs_tol=1e-9)
    assert math.isclose(survival,(1+2/N)**-N,abs_tol=1e-8)
    rtd_checks.append({'N':N,'area':area,'mean':mean,'variance':variance,'first_order_survival':survival})
cp=(math.sqrt(3)-1)/2
cc=(math.sqrt(5)-1)/2
assert math.isclose(cp+cp**2,0.5)
assert math.isclose(cc+cc**2,1)
values['RE06']={'X_CSTR':1-1/3,'X_N4':1-(1+2/4)**-4,'X_PFR':1-math.exp(-2),'PFR_then_CSTR_C':cp,'PFR_then_CSTR_X':1-cp,'CSTR_first_C':cc,'CSTR_then_PFR_C':cc/(1+cc),'CSTR_then_PFR_X':1-cc/(1+cc)}
# Limit checks: expansion closure reduces correctly; all first-order conversions
# vanish at zero space time; increasing tanks tends to plug flow.
assert -math.log1p(-0.5)/k == (-math.log1p(-0.5)-0*0.5)/k
assert all((1+0/N)**-N==1 for N in [1,4,10])
assert abs((1+2/100000)**-100000-math.exp(-2))<3e-6
result={'examples':values,'numerical_RTD_checks':rtd_checks,'balance_and_limit_checks':'passed'}
out=Path(__file__).resolve().parents[1]/'scratch/codex-reaction-engineering/numerical-validation.json'
out.write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))

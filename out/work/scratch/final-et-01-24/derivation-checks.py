from math import log,exp,sqrt
from pathlib import Path
import json

def d(f,x,h=1e-5):return (f(x+h)-f(x-h))/(2*h)
def partials(g,x):return g(x)+(1-x)*d(g,x),g(x)-x*d(g,x)
checks={}
for name,g,analytic in [
 ('Margules1',lambda x:1.3*x*(1-x),lambda x:(1.3*(1-x)**2,1.3*x*x)),
 ('Margules2',lambda x:x*(1-x)*(1.3-.7*(2*x-1)),lambda x:((1.3-2.1)*(1-x)**2+2.8*(1-x)**3,(1.3+2.1)*x*x-2.8*x**3)),
 ('vanLaar',lambda x:1.3*2.1*x*(1-x)/(1.3*x+2.1*(1-x)),lambda x:(1.3*(2.1*(1-x)/(1.3*x+2.1*(1-x)))**2,2.1*(1.3*x/(1.3*x+2.1*(1-x)))**2)),
]:
 checks[name]=max(abs(a-b) for x in [.1,.3,.7,.9] for a,b in zip(partials(g,x),analytic(x)))
L12=.4;L21=2.3
wg=lambda x:-x*log(x+L12*(1-x))-(1-x)*log(1-x+L21*x)
wa=lambda x:(-log(x+L12*(1-x))+(1-x)*(L12/(x+L12*(1-x))-L21/(1-x+L21*x)),-log(1-x+L21*x)-x*(L12/(x+L12*(1-x))-L21/(1-x+L21*x)))
checks['Wilson']=max(abs(a-b) for x in [.1,.3,.7,.9] for a,b in zip(partials(wg,x),wa(x)))
t21=1.1;t12=-.3;G21=exp(-.3*t21);G12=exp(-.3*t12)
ng=lambda x:x*(1-x)*(t21*G21/(x+(1-x)*G21)+t12*G12/(1-x+x*G12))
na=lambda x:((1-x)**2*(t21*(G21/(x+(1-x)*G21))**2+t12*G12/(1-x+x*G12)**2),x*x*(t12*(G12/(1-x+x*G12))**2+t21*G21/(x+(1-x)*G21)**2))
checks['NRTL']=max(abs(a-b) for x in [.1,.3,.7,.9] for a,b in zip(partials(ng,x),na(x)))
m=1000;chi=.4
for phi2 in [.1,.5]:
 n1=1-phi2;n2=phi2/m
 def total(n1):
  phi1=n1/(n1+m*n2);phi2=1-phi1
  return n1*log(phi1)+n2*log(phi2)+chi*n1*phi2
 expected=log(1-phi2)+(1-1/m)*phi2+chi*phi2**2
 checks['FH_'+str(phi2)]=abs(d(total,n1)-expected)
# vdW mixture algebra independently checks eq (90) without using its reduced form as input.
for x in [.1,.3,.7,.9]:
 a1=4.;a2=9.;b1=2.;b2=5.;y=1-x;aa=(x*sqrt(a1)+y*sqrt(a2))**2;bb=x*b1+y*b2
 lhs=-aa/bb+x*a1/b1+y*a2/b2;rhs=x*y*b1*b2/bb*(sqrt(a1)/b1-sqrt(a2)/b2)**2
 checks['vdW_algebra_'+str(x)]=abs(lhs-rhs)
# Counterexample to φ sign specifying local V: take ln φ=-2P+P² in dimensionless units.
p=1.5;checks['phi_counterexample']={'lnphi':-2*p+p*p,'dlnphi_dP':-2+2*p,'meaning':'phi<1 but local V-RT/P>0'}
Path(__file__).with_name('derivation-results.json').write_text(json.dumps(checks,indent=2))
print(json.dumps(checks,indent=2))

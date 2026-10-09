from pathlib import Path
import math,json,itertools
base=Path(__file__).parent
l=math.log(2)/30; K=100.; xs=100.; beta=2*l*xs
f=lambda x: beta/(1+(x/K)**2)-l*x
# RK4 from zero: global half-rise is distinct from local relaxation.
def half_rise(dt):
 x=0.; t=0.
 while x<xs/2:
  old=x; k1=f(x); k2=f(x+dt*k1/2); k3=f(x+dt*k2/2); k4=f(x+dt*k3)
  x+=dt*(k1+2*k2+2*k3+k4)/6; t+=dt
 return t-dt+dt*(xs/2-old)/(x-old)
tr=half_rise(.001); assert abs(tr-half_rise(.0005))<1e-7
h=.0001; fp=(f(xs+h)-f(xs-h))/(2*h)+l
assert abs(fp+l)<1e-9
# n=2 PAR with no leak: three fixed points; slopes determine stability.
lpar=.01; bpar=4.; kpar=100.
roots=[0.,(bpar-math.sqrt(bpar*bpar-4*lpar*lpar*kpar*kpar))/(2*lpar),(bpar+math.sqrt(bpar*bpar-4*lpar*lpar*kpar*kpar))/(2*lpar)]
slopes=[2*bpar*x*kpar*kpar/(kpar*kpar+x*x)**2-lpar for x in roots]
assert slopes[0]<0 and slopes[1]>0 and slopes[2]<0
# Eight deliberately symmetric pairs; population moments, not sample corrections.
pairs=[(100+e+r,100+e+g) for e,r,g in itertools.product([-12,12],[-9,9],[-9,9])]
mr=sum(r for r,g in pairs)/len(pairs); mg=sum(g for r,g in pairs)/len(pairs)
vr=sum((r-mr)**2 for r,g in pairs)/len(pairs); vg=sum((g-mg)**2 for r,g in pairs)/len(pairs)
cov=sum((r-mr)*(g-mg) for r,g in pairs)/len(pairs)
i=sum((r/mr-g/mg)**2 for r,g in pairs)/(2*len(pairs)); e=cov/(mr*mg); total=(vr/mr**2+vg/mg**2)/2
assert abs(total-i-e)<1e-14
# Exact closed moment equations of the telegraph -> mRNA -> protein process.
kon=.12; koff=.18; km=10.; lm=.2; kp=2.; lp=.02
a=kon+koff; q=kon/a; vg0=q*(1-q); m=km*q/lm; p=kp*m/lp
cgm=km*vg0/(a+lm); vm=m+km*cgm/lm
cgp=kp*cgm/(a+lp); cmp=(km*cgp+kp*vm)/(lm+lp); vp=p+kp*cmp/lp
# Check each covariance equation, including promoter switching.
res=[km*vg0-(a+lm)*cgm,2*km*cgm-2*lm*vm+2*lm*m,kp*cgm-(a+lp)*cgp,km*cgp+kp*vm-(lm+lp)*cmp,2*kp*cmp-2*lp*vp+2*lp*p]
assert max(abs(x) for x in res)<1e-10
tg=1/a; tm=1/lm; tp=1/lp; A=(1-q)/q
m_terms=[1/m,A*tg/(tg+tm)]
p_terms=[1/p,tm/(m*(tm+tp)),A*tm/(tm+tp)*tg/(tg+tp)*(tg+tp+tg*tp/tm)/(tg+tm)]
assert abs(sum(m_terms)-vm/m**2)<1e-12 and abs(sum(p_terms)-vp/p**2)<1e-12
# Fast/slow promoter and protein-filter limits.
assert A*1e-9/(1e-9+tm)<1e-9
assert abs(A*1e12/(1e12+tm)-A)<1e-10
# Fixed-delay characteristic equation: s+lambda+a exp(-s tau)=0.
ld=.02; ad=.06; omega=math.sqrt(ad*ad-ld*ld); tc=math.acos(-ld/ad)/omega
z=complex(0,omega); residual=z+ld+ad*complex(math.cos(-omega*tc),math.sin(-omega*tc))
assert abs(residual)<1e-14
out={'NAR':{'lambda_min-1':l,'beta_nM_per_min':beta,'fixed_nM':xs,'local_relaxation_min':1/(2*l),'local_half_relaxation_min':math.log(2)/(2*l),'global_half_rise_min':tr,'unregulated_half_rise_min':math.log(2)/l,'strong_n1_half_rise_fraction':math.log(4/3)/(2*math.log(2)),'sensitivity_beta':.5},'network_null':{'expected_self_arrows':519/424,'enrichment':40/(519/424)},'PAR':{'roots_nM':roots,'net_slopes_min-1':slopes},'dual_reporter':{'pairs':pairs,'means':[mr,mg],'variances':[vr,vg],'covariance':cov,'mean_squared_difference':sum((r-g)**2 for r,g in pairs)/len(pairs),'eta_squared':[i,e,total],'eta':[math.sqrt(i),math.sqrt(e),math.sqrt(total)]},'telegraph':{'q':q,'tau_g_min':tg,'tau_m_min':tm,'tau_p_min':tp,'mean_m':m,'mean_p':p,'var_m':vm,'var_p':vp,'m_terms':m_terms,'p_terms':p_terms,'CV_m':math.sqrt(vm)/m,'CV_p':math.sqrt(vp)/p,'Poisson_CV_m':1/math.sqrt(m),'moment_residual_max':max(abs(x) for x in res)},'delay':{'omega_min-1':omega,'critical_delay_min':tc,'onset_period_min':2*math.pi/omega,'characteristic_residual':abs(residual)},'dilution':{'generations_1000_to_100':math.log2(1000/100),'generations_2000_to_100':math.log2(2000/100)}}
(base/'verification-output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2)); print('ALL NUMERICAL AND MOMENT CHECKS PASSED')

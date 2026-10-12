"""Independent SEP-U3 review calculations. Written from the original scans only;
does not import or read the author's verify.py/results.json."""
from pathlib import Path
import math,json
out={}
# ---- Example 4.1 gas membrane (p19-28): alpha=5, gamma=0.1, Km=1.7e-5 Nm3/(m2 s bar), Pf=10, Pp=1
a,g,Km,Pf,Pp,Q1,x1,x3=5,0.1,1.7e-5,10,1,1.0,0.209,0.05
def yi(x):
    # (a-1)y^2+(1-a-1/g-x(a-1)/g)y+a x/g=0, root in (0,1)
    A=a-1;B=1-a-1/g-x*(a-1)/g;C=a*x/g
    r=[(-B-s*math.sqrt(B*B-4*A*C))/(2*A) for s in (1,-1)]
    r=[v for v in r if 0<v<1];assert len(r)==1;return r[0]
def J(x):y=yi(x);return Km*(Pf*x-Pp*y)        # oxygen flux, Nm3/(m2 s)
quad={'inlet':[4,1-a-1/g-x1*(a-1)/g,a*x1/g],'outlet':[4,1-a-1/g-x3*(a-1)/g,a*x3/g]}
yin,yout=yi(x1),yi(x3);ym=(yin+yout)/2
S=(x1-x3)/(ym-x3);Q2=S*Q1
jin,jout=J(x1),J(x3);jm=(jin+jout)/2;jl=(jin-jout)/math.log(jin/jout)
out['gas_estimate']=dict(quadratic_coeffs=quad,y_in=yin,y_out=yout,y_mean=ym,S=S,J_in=jin,J_out=jout,
  ratio=jin/jout,A_arith=Q2*ym/jm,A_logmean=Q2*ym/jl)
# Differential: dS/(1-S)=dx/(x-yi); dA=Q1*yi*dS/J. Integrate in x with RK4 on (S,A).
def rhs(x,S_):
    y=yi(x);dS=(1-S_)/(x-y);return dS,Q1*y*dS/J(x)
def integrate(n):
    h=(x3-x1)/n;x=x1;S_=0;A_=0
    for _ in range(n):
        k1=rhs(x,S_);k2=rhs(x+h/2,S_+h/2*k1[0]);k3=rhs(x+h/2,S_+h/2*k2[0]);k4=rhs(x+h,S_+h*k3[0])
        S_+=h/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]);A_+=h/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]);x+=h
    return S_,A_
conv=[integrate(n) for n in (16,160,1600)]
Sf,Af=conv[-1];ybar=(x1-(1-Sf)*x3)/Sf
out['gas_differential']=dict(S_A_by_steps=conv,S=Sf,A=Af,ybar=ybar,O2_recovery=Sf*ybar/x1,
  approx_O2_recovery=S*ym/x1,between_bounds=out['gas_estimate']['A_arith']<Af<out['gas_estimate']['A_logmean'])
# ---- Example 4.3 NaCl polarisation (p34-35)
u,d,rho,mu,D,Jv,Cf,Rapp=0.005,300e-6,1000,1e-3,1.6e-9,4.71e-6,0.1,0.97
Re=u*d*rho/mu;Sc=mu/(rho*D);Sh=0.61*Re**0.5*Sc**(1/3);kf=Sh*D/d
Cp=(1-Rapp)*Cf;Cw=Cp+(Cf-Cp)*math.exp(Jv/kf)
out['nacl']=dict(Re=Re,Sc=Sc,Sh=Sh,Sh_with_0p33=0.61*Re**0.5*Sc**0.33,kf=kf,Cp=Cp,Cw=Cw,rise=(Cw-Cf)/Cf,R_true=1-Cp/Cw)
# ---- Example 4.4 whey UF (p40-43)
Pi=lambda C:0.0044*C-1.7e-6*C**2+7.9e-8*C**3
kf,CG,C0,Kv=7.8e-6,400,10,250   # Kv in L/(m2 h bar)
Jstar=kf*math.log(CG/C0);LMH=Jstar*1000*3600
J2=0.01e-3;Cw2=C0*math.exp(J2/kf)
out['whey']=dict(Pi_feed=Pi(C0),Pi_gel=Pi(CG),Jstar=Jstar,Jstar_LMH=LMH,dP_limit=Pi(CG)+LMH/Kv,
  Cw_36LMH=Cw2,Pi_w=Pi(Cw2),dP_36LMH=Pi(Cw2)+36/Kv,osmotic_share_at_limit=Pi(CG)/(Pi(CG)+LMH/Kv))
# ---- Example 4.5 RO (p49-50): no polarisation, constant Rapp
Qp,C1,S,R,KvRO,dP,k,Am=100,35,0.30,0.995,0.004*24,55,0.82,3   # Kv m/(day bar)
C3=C1*(1-S)**(-R);C2=C1/S*(1-(1-S)**(1-R))
net=lambda C:dP-k*(C-(1-R)*C)
ni,no=net(C1),net(C3);Jm=KvRO*(ni+no)/2;A_ar=Qp/Jm
Q1f=Qp/S
def Aint(n):  # A = Q1 * int_0^S dS / Jv(Cf(S)), Simpson
    h=S/n;f=lambda s:1/(KvRO*net(C1*(1-s)**(-R)))
    return Q1f*h/3*sum(f(i*h)*(1 if i in(0,n) else 4 if i%2 else 2) for i in range(n+1))
Ai=Aint(2000)
out['ro']=dict(C3=C3,C3_with_printed_exponent=C1*(1-S)**(-0.005),C2=C2,net_in=ni,net_out=no,ratio=ni/no,
  J_mean_m_per_day=Jm,J_mean_m_per_h=Jm/24,A_arith=A_ar,modules_arith=math.ceil(A_ar/Am),
  A_integrated=Ai,A_integrated_coarse=Aint(20),modules_integrated=math.ceil(Ai/Am),mass_balance_check=(Q1f*C1-Qp*C2)/(Q1f-Qp)-C3)
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=1))

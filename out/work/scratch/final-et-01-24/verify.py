from math import exp,log,sqrt
from pathlib import Path
import json
R=8.314
def root(f,a,b):
 assert f(a)*f(b)<0,(f(a),f(b))
 for _ in range(100):
  c=(a+b)/2
  if f(a)*f(c)<=0:b=c
  else:a=c
 return (a+b)/2
def curvature(f,x,h=1e-4):return (f(x+h)-2*f(x)+f(x-h))/h**2
o={}
o['01']={'fusion entropy':6009/273.15,'driving force 10K':6009/273.15*10}
a=.137;b=3.87e-5;T=300
vals=[]
for P in [1e5,1e6,1e7]:
 v=root(lambda v:R*T/(v-b)-a/v**2-P,b*1.00001,2*R*T/P+b)
 vals.append({'P':P,'low':(b-2*a/(R*T))*P,'full':P*v-R*T-a/v})
o['02']={'departures':vals,'inversion T':2*a/R/b}
x=.17;n=700/(x*54.7+(1-x)*17.8);A=(54.7-58)/(.83**2)
o['03-05']={'n':n,'ethanol':n*x,'water':n*(1-x),'pre_mix_vol':n*(x*58+(1-x)*18),'A':A,'Vwater_model':18+A*x*x,'model_contraction':n*A*x*(1-x),'dGmix_molar':R*293.15*(x*log(x)+(1-x)*log(1-x))}
V=1.805e-5;rt=R*293.15;ps=.02339
fac=[exp(V*(atm*1.01325-ps)*1e5/rt) for atm in [1,10,100]]
o['06-07']={'factors':fac,'pressures':[ps*f for f in fac],'1pctbar':ps+rt*log(1.01)/V/1e5,'mu_humidity':rt*log(fac[0]/.6),'mu_100pct':rt*log(fac[0])}
B=-10.30e-6;C=1430e-12;rt=R*273.15;P=100*101325
ln1=B*P/rt;ln2=ln1+.5*(C-B*B)*(P/rt)**2
o['08']={'ln_B':ln1,'phi_B':exp(ln1),'ln_BC':ln2,'phi_BC':exp(ln2)}
T=673.15;rt=R*T
vs=[27.89,13.91,9.247,6.917,5.519,4.586,3.920,3.421,3.032,2.722]
ints=[v*.001-rt/(P*1e5) for v,P in zip(vs,range(2,21,2))]
def trap(y,step):return step*(sum(y)-.5*(y[0]+y[-1]))
o['09tables']={'integrands':ints,'Izero':trap([0]+ints,2e5),'Ivirial':trap([-.078e-3]+ints,2e5)}
Tc=647.096;Pc=220.64e5;w=.344;k=.37464+1.54226*w-.26992*w*w;alpha=(1+k*(1-sqrt(T/Tc)))**2;a=.45724*R*R*Tc*Tc/Pc*alpha;b=.07780*R*Tc/Pc
prs=[]
for P in [20e5,500e5]:
 AA=a*P/rt**2;BB=b*P/rt
 Z=root(lambda z:z**3-(1-BB)*z*z+(AA-3*BB*BB-2*BB)*z-(AA*BB-BB*BB-BB**3),BB+1e-9,2)
 ln=Z-1-log(Z-BB)-AA/(2*sqrt(2)*BB)*log((Z+(1+sqrt(2))*BB)/(Z+(1-sqrt(2))*BB))
 prs.append({'P':P,'Z':Z,'phi':exp(ln),'fbar':exp(ln)*P/1e5})
ys=[-.078e-3]+[v*.001-rt/(P*1e5) for v,P in zip([1.042,.476,.282,.179,.108,.0504,.0379,.0344,.0325,.0312],range(50,501,50))]
o['09coarse']={'I':trap(ys,50e5),'phi':exp(trap(ys,50e5)/rt),'fbar':500*exp(trap(ys,50e5)/rt)}
o['09PR']={'kappa':k,'alpha':alpha,'values':prs}
o['10']={'dln9bar':-3.3e-6*9e5/(R*293.15),'dln90bar':-3.3e-6*90e5/(R*293.15)}
o['11']={str(x):[exp((1-x)**2),exp(x*x)] for x in [0,.2,.5,.8,1]}
x=.57;G=-710;B=G*(2*x-1)/(2*x*x*(1-x)**2);A=G/(x*(1-x))-B*(2*x-1)
o['12']={'A':A,'B':B,'gamma_inf':[exp((A-B)/(R*348.15)),exp((A+B)/(R*348.15))]}
rt=R*83.8;A=148;p1=1.01325*exp(-6819/R*(1/83.8-1/90.188));p2=.6892;x=.3;g1=exp(A*(1-x)**2/rt);g2=exp(A*x*x/rt);p=x*g1*p1+(1-x)*g2*p2
o['13']={'Gideal_half':rt*log(.5),'Gtotal_half':rt*log(.5)+37,'mu1':rt*log(x)+A*(1-x)**2,'mu2':rt*log(1-x)+A*x*x,'gamma':[g1,g2],'p1sat':p1,'bubble':p,'y1':x*g1*p1/p}
def bubble(x):return x*exp(A*(1-x)**2/rt)*.4917+(1-x)*exp(A*x*x/rt)*.6892
vals=[]
for dx in [.01,.001]:
 dp=bubble(dx)-bubble(0);chord=dp/dx;vals.append({'dx':dx,'dpPa':dp*1e5,'chord':chord,'gamma_inf':(.6892+chord)/.4917})
g1i=(.6892+(bubble(.01)-bubble(0))/.01)/.4917;g2i=(.4917+(bubble(.99)-bubble(1))/.01)/.6892
o['14']={'true_inf':exp(A/rt),'chords':vals,'other_inf':g2i,'fit_A':rt/2*(log(g1i)+log(g2i)),'fit_B':rt/2*(log(g2i)-log(g1i))}
Tf=273.15;H=6009;M=.018015
freeze=lambda x:1/(1/Tf-R/H*log(x))
o['15']={'Kf':R*Tf*Tf*M/H,'1molkg_dT':Tf-freeze(1/(1+M)),'seawater_dT':Tf-freeze(1/(1+1.2*M))}
Te=root(lambda T:exp(H/R*(1/Tf-1/T))+exp(9958/R*(1/260.25-1/T))-1,150,250);xe=exp(H/R*(1/Tf-1/Te));xw=(40/18.015)/(40/18.015+60/62.07)
def lna_cp(T):return -(H+37.25*(T-Tf)-T*(H/Tf+37.25*log(T/Tf)))/(R*T)
Ticecp=root(lambda T:lna_cp(T)-log(xw),200,Tf)
o['16']={'Te':Te,'xwater':xe,'wt_glycol':(1-xe)*62.07/(xe*18.015+(1-xe)*62.07),'xw60wt':xw,'iceT':freeze(xw),'iceTcp':Ticecp,'glycolT':1/(1/260.25-R/9958*log(1-xw)),'gamma_simple':exp(H/R*(1/Tf-1/228.15))/xw,'gamma_cp':exp(lna_cp(228.15))/xw}
rt=R*298.15
vals=[]
for v1,d1 in [(131.6,14.86),(108.7,16.76)]:
 v2=89.4;d2=18.73;dd=(d1-d2)**2;phi1=v1/(v1+v2);phi2=1-phi1
 vals.append({'inf':[exp(v1*dd/rt),exp(v2*dd/rt)],'half':[exp(v1*phi2**2*dd/rt),exp(v2*phi1**2*dd/rt)],'Gex':.5*(v1+v2)*phi1*phi2*dd})
o['17']=vals
vals=[]
for phi in [.1,.5]:
 x1=1000*(1-phi)/(phi+1000*(1-phi));ln=log(1-phi)+(1-1/1000)*phi
 vals.append({'phi':phi,'x1':x1,'athermal':exp(ln),'a':exp(ln+.4*phi*phi),'gamma':exp(ln+.4*phi*phi)/x1})
o['18']={'values':vals,'chic':.5*(1+1/sqrt(1000))**2,'phic':1/(1+sqrt(1000))}
# Solve Wilson's two equations by eliminating Lambda21.
l1=log(.509);l2=log(.288)
L12=root(lambda L:1-log(1-log(L)-l1)-L-l2,1,3);L21=1-log(L12)-l1
wilson=lambda x: -x*log(x+L12*(1-x))-(1-x)*log(1-x+L21*x)
o['19a']={'L12':L12,'L21':L21,'Gex':[rt*0 for x in []]}
o['19a']['Gex']=[R*348.15*wilson(x) for x in [.2,.5,.8]]
L=root(lambda L:1-log(L)-L-3,.001,1);tau=root(lambda t:t*(1+exp(-.3*t))-3,1,4);GG=exp(-.3*tau)
mix=lambda x:x*log(x)+(1-x)*log(1-x)
wf=lambda x:mix(x)-x*log(x+L*(1-x))-(1-x)*log(1-x+L*x)
nf=lambda x:mix(x)+x*(1-x)*tau*GG*(1/(x+(1-x)*GG)+1/(1-x+x*GG))
o['19b']={'L':L,'tau':tau,'min_curvature_W':min(curvature(wf,x/1000) for x in range(1,1000)),'min_curvature_N':min(curvature(nf,x/1000) for x in range(1,1000))}
rs=[4.5,11.244,2.576, .92];qs=[3.856,9.256,2.588,1.4]
vals=[]
for i,j in [(1,0),(0,1),(2,3),(3,2)]:
 V=rs[i]/rs[j];F=qs[i]/qs[j];ln=1-V+log(V)-5*qs[i]*(1-V/F+log(V/F));vals.append(exp(ln))
o['20']=vals
o['21']=[c-p+2 for c,p in [(1,2),(1,3),(2,2),(2,3),(3,2)]]
T=298.15;v=1.807e-5;x2=1.2*M/(1+1.2*M);lna=-H*2/(R*Tf*Tf)
o['22']={'osmoticbar':-R*T*log(1-x2)/v/1e5,'linearbar':R*T*x2/v/1e5,'freeze_routebar':-R*T*lna/v/1e5,'waterheight27bar':27e5/(1000*9.81)}
k=2*.0727*1.805e-5/(R*293.15);vals=[]
for r in [1e-6,1e-7,1e-8,1e-9]:
 ratio=exp(k/r);full=root(lambda S:log(S)-k/r-1.805e-5*2339*(S-1)/(R*293.15),ratio*.999,ratio*1.001)
 vals.append({'r':r,'laplacebar':2*.0727/r/1e5,'ratio':ratio,'full':full})
o['23']={'values':vals,'critical_r':[k/log(s) for s in [1.001,1.01,1.1]]}
Tb=373.12;H=40650;vals=[]
for r in [1e-5,1e-6,1e-7]:
 P=101325+2*.0589/r;T=1/(1/Tb-R/H*log(P/101325));vals.append({'r':r,'Pbar':P/1e5,'T_C':T-273.15})
o['24']={'values':vals,'Kb':R*Tb*Tb*M/H,'salt_dT':R*Tb*Tb*M/H*2*10/58.44}
Path(__file__).with_name('independent-results.json').write_text(json.dumps(o,indent=2))
print(json.dumps(o,indent=2))

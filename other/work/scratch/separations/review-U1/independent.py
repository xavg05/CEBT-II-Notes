from pathlib import Path
import math,json,re
root=Path(__file__).resolve().parent
result={}
rho=110000/(8314.5*293)
result['Henry']=dict(rho=rho,Hm=.00045*55.5/rho)
result['pinch']=dict(Lmin=1*(.020-.002)/(.020/2),xB=(.020-.002)/2.34,Gmin=(.020-.002)/(.020*2),rstrip=1/((.020-.002)/(.020*2)))
result['resistance']=[]
for H in [1.05,.00045,.009]:
    rg=1/.04;rl=H/.0002;kg=1/(rg+rl);kl=1/(1/.0002+1/(H*.04))
    assert abs(kl-H*kg)<1e-15
    result['resistance'].append(dict(H=H,Kg=kg,Kl=kl,gas_share=100*rg/(rg+rl)))
result['film']=dict(delta=2e-9/2e-4,k=1.5e-9/(2e-9/2e-4))
q=2/3;db=.02-2*(.02-.002)/3;dt=.002
ntu=math.log(db/dt)/(1-q);n=math.log(db/dt)/math.log(1/q)
result['linear']=dict(xB=.018/3,NTU=ntu,logforce=(db-dt)/math.log(db/dt),Z=.6*ntu,n=n,HETP=.6*ntu/n)
result['hydraulics']=dict(U=2*.55,A=1/(2*.55),D=math.sqrt(4/(2*.55)/math.pi),K_fraction=.55**2)
# Independently transcribed from original p29 table, not imported author code.
X=[0,.021,.031,.042,.053,.079,.106,.159]
P=[0,1.6,2.4,3.3,4.2,6.7,9.3,15.2]
G=.05;yT=.0001;yB=.05;PT=110
xpinch=.053+(.079-.053)*(PT*yB-4.2)/(6.7-4.2)
Lmin=G*(yB-yT)/xpinch;L=1.29*Lmin;r=L/G;xB=(yB-yT)/r
def equ(x):
    for i in range(len(X)-1):
        if X[i]<=x<=X[i+1]+1e-12:
            return (P[i]+(P[i+1]-P[i])*(x-X[i])/(X[i+1]-X[i]))/PT
    raise ValueError(x)
def gap(y):return y-equ((y-yT)/r)
# Analytic integrate reciprocal linear gap separately over each liquid interval.
bounds=[yT]+[yT+r*x for x in X[1:] if x<xB]+[yB]
exact=0;parts=[]
for ya,yb in zip(bounds,bounds[1:]):
    da,db_=gap(ya),gap(yb);slope=(db_-da)/(yb-ya)
    val=math.log(db_/da)/slope if abs(slope)>1e-12 else (yb-ya)/da
    exact+=val;parts.append(dict(y_a=ya,y_b=yb,force_a=da,force_b=db_,NTU=val))
# Independent Simpson using equal log(y) spacing, robust near yT.
def simpson_log(n):
    t0=math.log(yT);dt_=(math.log(yB)-t0)/n;s=0
    for k in range(n+1):
        y=math.exp(t0+k*dt_);f=y/gap(y)
        s+=f*(1 if k in [0,n] else 4 if k%2 else 2)
    return s*dt_/3
conv=[simpson_log(n) for n in [2000,10000,50000]]
pref=G/(rho*1.5);vol=pref*exact
forceT=gap(yT);forceB=gap(yB);lm=(forceB-forceT)/math.log(forceB/forceT)
source_y=[.0001,.0005,.001,.005,.01,.02,.03,.04,.05]
source_f=[10000,5000,2500,625,323,161,127,97,79]
trap=sum((b-a)*(f1+f2)/2 for a,b,f1,f2 in zip(source_y,source_y[1:],source_f,source_f[1:]))
result['ammonia']=dict(xpinch=xpinch,Lmin=Lmin,L=L,Q=G*(yB-yT),xB=xB,NTU_exact=exact,parts=parts,NTU_log_simpson=conv,V=vol,endpoint_mean_volume=G*(yB-yT)/(rho*1.5*lm),coarse_table_NTU=trap,coarse_table_V=pref*trap)
assert abs(exact-17.6229916)<1e-6
assert abs(conv[-1]-exact)<1e-6
# Own structure review: published figure links conceptually target subject figs.
repo=root.parents[4]
draftdir=repo/'other/work/drafts/Separations II/U1'
required=['Overview','Intuition','Derivation','Motivation and explanation','Worked example','Link to other topics','Conclusion']
result['structure']=[]
for p in sorted(draftdir.glob('*.md')):
    s=p.read_text(encoding='utf-8');heads=re.findall(r'^## (.+)$',s,re.M)
    figures=re.findall(r'!\[[^\]]*\]\(\.\./figs/([^)]*)\)',s)
    assert heads==required,(p.name,heads)
    for f in figures:assert (repo/'notes/Separations II/figs'/f).exists(),f
    result['structure'].append(dict(file=p.name,sections=True,figures=figures,local_tags=re.findall(r'\\tag\{(\d+)\}',s)))
(root/'independent-results.json').write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k not in ['structure','resistance']},indent=2))

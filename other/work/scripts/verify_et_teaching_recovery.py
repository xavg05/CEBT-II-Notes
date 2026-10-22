"""Recompute retained ET recovery numbers without third-party numeric packages."""
from pathlib import Path
import math, json, re, subprocess, sys

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(Path(__file__).parent))
from check_inline_math import check_files
R=8.314
values={}
def check(name,actual,expected,tolerance):
    assert abs(actual-expected)<=tolerance,(name,actual,expected)
    values[name]=actual
def bisect(f,a,b):
    fa=f(a)
    assert fa*f(b)<=0
    for _ in range(100):
        m=(a+b)/2
        if f(m)*fa>0:a=m;fa=f(m)
        else:b=m
    return (a+b)/2

check('01 freezing driving force J/mol',6009/273.15*10,220,0.1)
coef=3.87e-5-2*.1370/(R*300)
check('02 departure coefficient m3/mol',coef,-7.12e-5,1e-7)
check('02 equivalent ideal heating K',-coef*1e7/(3.5*R),24,0.5)
n=700/(.17*54.7+.83*17.8)
check('03 total mol',n,29.08,.01)
check('03 ethanol mol',n*.17,4.94,.01)
check('03 water mol',n*.83,24.13,.01)
check('03 pure volume cm3',n*(.17*58+.83*18),721,1)
A=(54.7-58)/.83**2
check('04 A cm3/mol',A,-4.79,.01)
check('04 water partial volume',18+A*.17**2,17.86,.01)
g=R*293.15*(.17*math.log(.17)+.83*math.log(.83))
check('05 ideal mixing J/mol',g,-1111,1)
check('05 total mixing kJ',g*29.08/1000,-32.3,.1)
for atm,expected in [(1,1.0007),(10,1.0075),(100,1.078)]:
    check(f'06 Poynting {atm} atm',math.exp(1.805e-5*(atm*101325-2339)/(R*293.15)),expected,.0005)
check('06 one percent threshold bar',(2339+R*293.15*math.log(1.01)/1.805e-5)/1e5,13.5,.05)
fl=.02339*math.exp(1.805e-5*(101325-2339)/(R*293.15))
check('07 liquid fugacity bar',fl,.023407,.000001)
check('07 driving force J/mol',R*293.15*math.log(fl/(.6*.02339)),1247,1)
check('07 equilibrium RH percent',100*fl/.02339,100.07,.01)
BP=-10.30e-6*10132500/(R*273.15)
third=.5*(1430e-12-(-10.30e-6)**2)*(10132500/(R*273.15))**2
check('08 B-only logphi',BP,-.0460,.0001)
check('08 B+C logphi',BP+third,-.0328,.0001)
check('08 B-only phi',math.exp(BP),.955,.001)
check('08 B+C phi',math.exp(BP+third),.968,.001)
T=673.15;rt=R*T
vol=[1.042,.476,.282,.179,.108,.0504,.0379,.0344,.0325,.0312]
departure=[-.078e-3]+[v*1e-3-rt/(p*1e5) for p,v in zip(range(50,501,50),vol)]
integral=sum((a+b)/2*50e5 for a,b in zip(departure,departure[1:]))
check('09 coarse integral kJ/mol',integral/1000,-5.02,.01)
check('09 coarse phi',math.exp(integral/rt),.408,.001)
tc=647.096;pc=220.64e5;omega=.344
kappa=.37464+1.54226*omega-.26992*omega**2
alpha=(1+kappa*(1-math.sqrt(T/tc)))**2
for pressure,expectedphi,expectedz in [(20e5,.970,None),(500e5,.421,.375)]:
    aa=.45724*tc**2*alpha*pressure/(pc*T**2);bb=.07780*tc*pressure/(pc*T)
    z=bisect(lambda z:z**3-(1-bb)*z**2+(aa-3*bb**2-2*bb)*z-(aa*bb-bb**2-bb**3),bb+1e-10,3)
    lp=z-1-math.log(z-bb)-aa/(2*math.sqrt(2)*bb)*math.log((z+(1+math.sqrt(2))*bb)/(z+(1-math.sqrt(2))*bb))
    check(f'09 PR phi P={pressure}',math.exp(lp),expectedphi,.002)
    if expectedz:check('09 PR Z 500bar',z,expectedz,.001)
for bars,expected in [(9,.12),(90,1.2)]:
    check(f'10 gamma reduction {bars} bar percent',100*(1-math.exp(-3.3e-6*bars*1e5/(R*293.15))),expected,.02)
check('11 equimolar gamma',math.exp(.25),1.284,.001)
check('11 dilute gamma',math.e,2.718,.001)
T=83.8;B=148/(R*T)
check('13 ideal mixing J/mol',-R*T*math.log(2),-483,1)
check('13 oxygen gamma',math.exp(B*.7**2),1.110,.001)
check('13 argon gamma',math.exp(B*.3**2),1.019,.001)
p1=.3*math.exp(B*.7**2)*.507;p2=.7*math.exp(B*.3**2)*.689
check('13 bubble pressure bar',p1+p2,.660,.001)
check('13 oxygen vapour fraction',p1/(p1+p2),.256,.001)
check('13 Raoult oxygen fraction',.3*.507/(.3*.507+.7*.689),.240,.001)
check('15 cryoscopic constant',R*273.15**2*.018015/6009,1.860,.001)
Tf=1/(1/273.15+R/6009*math.log(1+.018015))
check('15 exact depression K',273.15-Tf,1.83,.01)
xw=(40/18.015)/(40/18.015+60/62.07)
ln_a=-6009/R*(1/228.15-1/273.15)
check('16 water mole fraction',xw,.697,.001)
check('16 constant enthalpy gamma',math.exp(ln_a)/xw,.85,.01)
ln_a_cp=ln_a+37.25/R*(273.15/228.15-1+math.log(228.15/273.15))
check('16 heat capacity gamma',math.exp(ln_a_cp)/xw,.92,.01)
eutectic=bisect(lambda t:math.exp(6009/R*(1/273.15-1/t))+math.exp(9958/R*(1/260.25-1/t))-1,180,250)
xe=math.exp(6009/R*(1/273.15-1/eutectic))
check('16 ideal eutectic K',eutectic,222.2,.1)
check('16 ideal eutectic water fraction',xe,.545,.001)
check('16 ideal eutectic glycol mass fraction',(1-xe)*62.07/(xe*18.015+(1-xe)*62.07),.74,.01)
check('16 60wt glycol ideal ice degC',1/(1/273.15-R/6009*math.log(xw))-273.15,-33,.5)
check('16 60wt glycol ideal glycol degC',1/(1/260.25-R/9958*math.log(1-xw))-273.15,-66,.5)
check('18 solvent mole fraction',.5/(.5+.5/1000),.999,.001)
for chi,expected in [(0,.824),(.4,.911)]:
    check(f'18 solvent activity chi={chi}',math.exp(math.log(.5)+.999*.5+chi*.25),expected,.001)
check('18 critical chi',.5*(1+1/math.sqrt(1000))**2,.532,.001)
check('18 critical polymer fraction',1/(1+math.sqrt(1000)),.031,.001)
check('22 ideal osmotic pressure bar',R*298.15*math.log(1+1.2*.018015)/1.807e-5/1e5,29,1)
osm=R*298.15*(6009/R*(1/271.15-1/273.15))/1.807e-5/1e5
check('22 freezing based pressure bar',osm,27,1)
L=2*.0727*1.805e-5/(R*293.15)
check('23 Kelvin length nm',L*1e9,1.077,.001)
check('23 100 nm ratio',math.exp(L/1e-7),1.011,.001)
check('23 10 nm ratio',math.exp(L/1e-8),1.114,.001)
check('23 critical radius nm',L/math.log(1.01)*1e9,108,1)
Kb=R*373.12**2*.018015/40650
check('24 ebullioscopic constant',Kb,.513,.001)
check('24 salt boiling elevation',Kb*2*10/58.44,.18,.01)
x=(1-.628)/(1.550-.628);y=1.55*x
check('25 liquid composition',x,.403,.001)
check('25 vapour composition',y,.625,.001)
check('25 vapour fraction',(.5-x)/(y-x),.435,.001)
for ps,expected in [(1.1541,1.182),(.7609,1.793)]:
    check(f'28 gamma Ps={ps}',1.364/ps,expected,.001)
check('31 oxygen mg/l',.21/43000*55.5*32*1000,8.7,.1)
check('31 cooling solubility ratio',math.exp(1700*(1/278.15-1/298.15)),1.51,.01)
xbin=bisect(lambda x:math.log(x/(1-x))-2.5*(2*x-1),.001,.3)
g=lambda x:x*math.log(x)+(1-x)*math.log(1-x)+2.5*x*(1-x)
check('36 lower binodal',xbin,.145,.001)
check('36 equimolar g',g(.5),-.068,.001)
check('36 two-phase g',g(xbin),-.104,.001)
check('36 split lowering J/mol',(g(.5)-g(xbin))*R*300,90,1)
# Two-variable Newton solve for equal activities, distinct van Laar endpoints.
def lg(x):
    den=2.62*x+3.02*(1-x)
    return 2.62*(3.02*(1-x)/den)**2,3.02*(2.62*x/den)**2
def residual(x,y):
    a,b=lg(x);c,d=lg(y)
    return math.log(x)+a-math.log(y)-c,math.log(1-x)+b-math.log(1-y)-d
x,y=.11,.93
for _ in range(20):
    f,h=residual(x,y);eps=1e-7
    fx,hx=residual(x+eps,y);fy,hy=residual(x,y+eps)
    a=(fx-f)/eps;b=(fy-f)/eps;c=(hx-h)/eps;d=(hy-h)/eps
    det=a*d-b*c
    x-=(d*f-b*h)/det;y-=(-c*f+a*h)/det
check('38 furfural-rich x1',x,.1128,.0001)
check('38 isobutane-rich x1',y,.9284,.0001)
check('38 dilute isobutane gamma',math.exp(lg(x)[0]),8.375,.01)
check('38 major isobutane gamma',math.exp(lg(y)[0]),1.018,.001)
check('38 phase I fraction',(y-.5)/(y-x),.525,.001)
for z in [.1,.2,.4]:values[f'39 curvature x={z}']=1/(z*(1-z))-5
for z,expected in [(.145,.38),(.4,-.20),(.5,-.25)]:
    check(f'40 Gamma x={z}',1-5*z*(1-z),expected,.001)
def ps(T,c):return 10**(c[0]-c[1]/(T+c[2]))
water=(5.08354,1663.125,-45.622)
for name,c,mw,expectedT,expectedy,expectedratio in [
    ('toluene',(4.07827,1343.943,-53.773),92.14,84.3,.444,.24),
    ('decane',(4.07857,1501.268,-78.67),142.29,97.5,.085,1.36)]:
    T=bisect(lambda T:ps(T,water)+ps(T,c)-1.01325,340,374)
    yo=ps(T,c)/1.01325;ratio=(1-yo)*18.015/(yo*mw)
    check(f'43 {name} mixture degC',T-273.15,expectedT,.1)
    check(f'43 {name} organic y',yo,expectedy,.001)
    check(f'43 {name} water mass ratio',ratio,expectedratio,.02)
    values[f'43 {name} organic mass fraction']=1/(1+ratio)

base=ROOT/'other/work/archive/reviewed-units/Equilibrium Thermodynamics'
files=list(base.glob('*.md'))
for p in files:
    s=p.read_text(encoding='utf-8')
    before=subprocess.check_output(['git','show','HEAD:'+p.relative_to(ROOT).as_posix()]).decode()
    assert re.findall(r'\\tag\{\d+\}',s)==re.findall(r'\\tag\{\d+\}',before),p
    assert not re.search(r'^### Worked example',s,re.M),p
    for image in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',s):assert (p.parent/image).exists(),(p,image)
check_files(files)
result={'checks':len(values),'numbers':values,'canonical_files':len(files),'equation_labels_preserved':True,'inline_math_pass':True,'figure_paths_exist':True,'reference_values_not_recalculated':'Experimental/graph-read data and reference EOS saturation pressure are retained as inputs, not recomputed experimental observations.'}
(ROOT/'other/work/progress/et-teaching-recovery-verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

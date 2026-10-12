"""Independent re-computation of U2 examples; no import of author's script/results."""
from pathlib import Path
import math,json,re

P=100000.;epsilon=.621945
def vapor_pressure(celsius):
    kelvin=celsius+273.15
    # ASHRAE water-vapour polynomial above freezing, pressure in Pa.
    logp=(-5800.2206/kelvin+1.3914993-.048640239*kelvin
          +4.1764768e-5*kelvin**2-1.4452093e-8*kelvin**3
          +6.5459673*math.log(kelvin))
    return math.exp(logp)
def saturated_humidity(temp):
    pw=vapor_pressure(temp)
    return epsilon*pw/(P-pw)
def enthalpy(temp,humidity):return (1.006+1.86*humidity)*temp+2501*humidity
def bisection(function,left,right):
    fl=function(left);fr=function(right)
    assert fl*fr<=0
    for _ in range(70):
        middle=(left+right)/2;fm=function(middle)
        if fl*fm<=0:right=middle
        else:left=middle;fl=fm
    return (left+right)/2
def sat_temperature(dry,humidity,liquid_energy=True):
    def balance(t):return enthalpy(t,saturated_humidity(t))-enthalpy(dry,humidity)-(4.186*t*(saturated_humidity(t)-humidity) if liquid_energy else 0)
    return bisection(balance,0,dry)
def humidity_from_wet(dry,wet):
    # Solve the full linear enthalpy balance by root finding, independently of algebraic inverse.
    return bisection(lambda H:enthalpy(wet,saturated_humidity(wet))-enthalpy(dry,H)-4.186*wet*(saturated_humidity(wet)-H),0,.02)
out={}
out['U2-01']={'wet_basis':.9/(1+.9),'dry_basis':.2/(1-.2)}
out['U2-02']={'Hsat30':saturated_humidity(30),'percent_chart':100*.015/.0272,'percent_saturation':100*.015/saturated_humidity(30),'RH_percent':100*P*.015/(epsilon+.015)/vapor_pressure(30)}
adiabatic=sat_temperature(40,.01);constantH=sat_temperature(40,.01,False)
out['U2-03']={'s':1.006+1.86*.02,'enthalpy':enthalpy(40,.02),'Ts':adiabatic,'Hs':saturated_humidity(adiabatic),'Ts_no_liquid_enthalpy':constantH}
out['U2-04']={'Tdew':bisection(lambda t:vapor_pressure(t)-P*.01/(epsilon+.01),0,40)}
wet=sat_temperature(25,.01);Hinv=humidity_from_wet(40,20)
out['U2-05']={'wet_25_H001':wet,'Hwet':saturated_humidity(wet),'H40wet20':Hinv,'RH40wet20':100*P*Hinv/(epsilon+Hinv)/vapor_pressure(40),'chloroform_chart':{'latent80_approx_kJkg':192,'humidheat_H08_approx_kJkgK':1.4}}
out['U2-06']={'constant_rate_seconds':.2*2.4e6/(2*40*(50-25))}
airratio=.8/(.0156-.0036)*1.2
Hexit=.0036+.8/airratio
out['U2-07']={'mmin':airratio/1.2,'m':airratio,'Hout':Hexit,'intercept':.0156-.0036+.1/airratio,'slope':-1/airratio}
critical=bisection(lambda w:10*(.0156-.0036-(w-.1)/airratio)-.5*w,.1,.9)
tc=airratio/10*math.log((.0156-.0036-(critical-.1)/airratio)/(.0156-.0036-(.9-.1)/airratio))
tf=2*math.log(critical/.1)
def reciprocal(w):return 1/min(10*(.0156-.0036-(w-.1)/airratio),.5*w)
def trapezoids(n):
    grid=[.1+.8*j/n for j in range(n+1)]
    return sum((b-a)*(reciprocal(a)+reciprocal(b))/2 for a,b in zip(grid,grid[1:]))
T_exit=bisection(lambda t:enthalpy(t,Hexit)-enthalpy(50,.0036),0,50)
out['U2-08']={'critical':critical,'wet_time_h':tc,'fall_time_h':tf,'total_time_h':tc+tf,'T_exit_const_h':T_exit}
out['U2-09']={'co_critical':bisection(lambda w:10*(.012-(.9-w)/80)-.5*w,0,.1),'co_time_h':8*math.log(.012/.002)}
out['U2-10']={'trapezoids':{str(n):trapezoids(n) for n in [8,80,800,8000]},'table':[{'w':w,'DH':.01325-.0125*w,'r':1/reciprocal(w),'reciprocal':reciprocal(w)} for w in [.1,.212,.5,.9]]}
out['U2-11']={'fixed_flux_rise_K':200/40}
assert abs(out['U2-03']['enthalpy']-91.748)<1e-9
assert abs(tc+tf-14.8445)<.0001
assert abs(trapezoids(8000)-(tc+tf))<1e-5
assert abs(out['U2-09']['co_critical']-.02)<1e-12
assert all(reciprocal(w)>0 for w in [.1,.212,.5,.9])

repo=Path(__file__).resolve().parents[5]
drafts=repo/'other/work/drafts/Separations II/U2'
figs=repo/'notes/Separations II/figs'
structure=[]
for file in sorted(drafts.glob('*.md')):
    content=file.read_text(encoding='utf8')
    headers=re.findall(r'^## (.+)$',content,re.M)
    expected=['Overview','Intuition','Derivation','Motivation and explanation','Worked example','Link to other topics','Conclusion']
    assert headers==expected,(file.name,headers)
    tags=re.findall(r'\\tag\{(\d+)\}',content)
    assert tags==[str(i) for i in range(1,len(tags)+1)]
    figures=re.findall(r'\.\./figs/([^\)]+)',content)
    assert all((figs/name).is_file() for name in figures)
    assert not re.search(r'lecture PDF|lecturer|slides|\[\[',content,re.I)
    structure.append({'file':file.name,'tags':len(tags),'figures':figures,'sections':headers})
assert len(structure)==11
out['structure']=structure
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='structure'},indent=2))

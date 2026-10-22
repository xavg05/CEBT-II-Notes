"""Independent RE-U2 review: no dependency on the author's verification script.

Uses pure-Python quadrature/root solving, conserved shell flux and the moving
boundary balance. Does not edit Claude-owned notes or author verification data.
"""
from pathlib import Path
from urllib.parse import unquote,urlsplit
import math,json,re,hashlib
from PIL import Image
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'other/work/reviews/RE-U2-cross-review-numbers-20261022.json'
checks=[]
def equal(name,actual,expected,rel=1e-9,abs_tol=1e-11):
 assert math.isclose(actual,expected,rel_tol=rel,abs_tol=abs_tol),(name,actual,expected)
 checks.append({'name':name,'actual':actual,'expected':expected})
def quad(f,a,b,n=2000):
 assert n%2==0
 h=(b-a)/n
 return h/3*(f(a)+f(b)+4*sum(f(a+i*h) for i in range(1,n,2))+2*sum(f(a+i*h) for i in range(2,n,2)))
def bisect(f,a,b,n=75):
 fa=f(a);fb=f(b)
 assert fa*fb<=0,(a,b,fa,fb)
 for _ in range(n):
  m=(a+b)/2;fm=f(m)
  if fa*fm<=0:b=m
  else:a=m;fa=fm
 return (a+b)/2

# General non-unit stoichiometry: A solid, B fluid; k_SA is extent-based.
R,rho,C,D,De,kg,ksa,nuA,nuB=.001,20000.,1.,2.6e-5,2e-6,.05,.02,1.,1.5
tau_pfilm=rho*R**2*nuB/(2*D*C*nuA)
tau_rxn=rho*R/(nuA*ksa*C)
tau_cfilm=rho*R*nuB/(3*kg*C*nuA)
tau_layer=rho*R**2*nuB/(6*De*C*nuA)
for y in [.1,.4,.9]:
 radius=R*y
 # Instantaneous radial-speed balances and derivatives of integrated times.
 film_supply=4*math.pi*radius**2*(D/radius)*C
 drdt=-(nuA/nuB)*film_supply/(4*math.pi*radius**2*rho)
 equal(f'RE07 radius rate y={y}',drdt,-R**2/(2*tau_pfilm*radius))
 consumption=nuA*4*math.pi*radius**2*ksa*C
 equal(f'RE08 receding speed y={y}',-consumption/(4*math.pi*radius**2*rho),-R/tau_rxn)
 # Gas profile: both boundaries and constant inward molar flow.
 profile=lambda r:C*(1/r-1/radius)/(1/R-1/radius)
 equal(f'RE09 core boundary y={y}',profile(radius),0)
 equal(f'RE09 outer boundary y={y}',profile(R),C)
 shell_flow=4*math.pi*De*C/(1/radius-1/R)
 for z in [.2,.7]:
  pos=radius+(R-radius)*z
  deriv=-C/(pos**2*(1/R-1/radius))
  equal(f'RE09 conserved flux y={y},z={z}',4*math.pi*pos**2*De*deriv,shell_flow)

# Normalised limiting curves, crossover, and the early-time expansion.
layer=lambda X:1-3*(1-X)**(2/3)+2*(1-X)
reaction=lambda X:1-(1-X)**(1/3)
equal('RE08 reaction X at half own time',1-(1-.5)**3,.875)
equal('RE08 film X at half own time',1-(1-.5)**1.5,.6464466094067263)
equal('RE08 reaction initial normalised slope',3*(1-0)**2,3)
equal('RE08 film initial normalised slope',1.5*math.sqrt(1-0),1.5)
equal('RE07 doubling stagnant-film particle radius',(2*R)**2/R**2,4)
equal('RE10 layer/reaction crossover',layer(.875),reaction(.875))
equal('RE10 crossover time',layer(.875),.5)
for X in [.01,.001]:
 equal(f'RE09 early asymptotic ratio X={X}',layer(X)/(X*X/3),1,rel=.005)
qtarget=.9;ytarget=(1-qtarget)**(1/3)
# dt/dy from inventory loss and the three LOCAL resistances; integrate it
# without evaluating the integrated shrinking-core conversion formula.
def dt_dy(y):
 return rho*nuB/(C*nuA)*(R*y*y/kg+R*R*(y-y*y)/De+R/(nuB*ksa))
integrated=quad(dt_dy,ytarget,1)
summed=tau_cfilm*qtarget+tau_layer*layer(qtarget)+tau_rxn*reaction(qtarget)
equal('RE10 combined balance time vs sum',integrated,summed)

# Cylindrical layer diffusion: integrate the independent logarithmic shell
# resistance. Time is normalised by the CYLINDER's own complete time.
def cylinder_time(X):
 y=math.sqrt(1-X)
 return quad(lambda z:4*z*math.log(1/z) if z else 0,y,1)
for X in [.2,.5,.9]:
 equal(f'cylinder diffusion X={X}',cylinder_time(X),X+(1-X)*math.log(1-X))

# Evaporation: root of latent-heat demand minus incoming gas conduction.
Rg=8.314462618;T0=323.15;enthalpy=44000.;diff=2.6e-5;conductivity=.026
psat=lambda T:3169.9*math.exp(-enthalpy/Rg*(1/T-1/298.15))
balance=lambda T:diff*psat(T)/(Rg*T)*enthalpy-conductivity*(T0-T)
Ts=bisect(balance,250,T0)
equal('RE11 heat residual',balance(Ts),0,abs_tol=1e-12)
ratio=(psat(Ts)/Ts)/(psat(T0)/T0)
equal('RE11 surface temperature rounded',round(Ts,2),289.35)
equal('RE11 evaporation ratio rounded',round(ratio,3),.165)
equal('RE11 evaporation slowdown factor',round(1/ratio,2),6.06)
equal('RE11 Celsius conversion rounded',round(Ts-273.15,1),16.2)
equal('RE11 convective limit Sh/Nu',round((.60/.71)**(1/3),3),.945)
equal('RE07 carbon/oxygen density ratio',round((2000/.012)/(.21*101325/(Rg*1000))),65125)

# Mixed-solid survival integral. Change variable from time to core radius,
# avoiding the author's inversion of the diffusion-controlled time relation.
forms={
 'film':(lambda y:1-y**3,lambda y:3*y*y,.5),
 'reaction':(lambda y:1-y,lambda y:1.,.25),
 'layer':(lambda y:1-3*y*y+2*y**3,lambda y:6*y*(1-y),.2),
}
residence={}
for name,(time,jac,coeff) in forms.items():
 equal(f'RE12 survival asymptote {name}',quad(lambda y:y**3*jac(y),0,1),coeff)
 def survival(mean):return quad(lambda y:y**3*math.exp(-time(y)/mean)*jac(y)/mean,0,1,n=800)
 mean=bisect(lambda m:survival(m)-.01,.1,100)
 equal(f'RE12 target residual {name}',survival(mean),.01,abs_tol=1e-11)
 residence[name]=mean
equal('RE12 film mean rounded',round(residence['film'],1),49.7)
equal('RE12 reaction mean rounded',round(residence['reaction'],1),24.8)
equal('RE12 layer mean rounded',round(residence['layer'],1),19.8)
equal('RE12 plug-flow film time at 99 percent',.99,.99)
equal('RE12 plug-flow reaction time at 99 percent',round(reaction(.99),3),.785)
equal('RE12 plug-flow layer time at 99 percent',round(layer(.99),3),.881)

# Canonical/publication parity, all local links, figures, and preserved labels.
MATH=re.compile(r'(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$')
def github(text):
 def convert(m):
  if m[1] is None:return '$`'+m[2]+'`$'
  expr=m[1].strip();tags=re.findall(r'\\tag\{(\d+)\}',expr)
  return ('\n**Equation ('+tags[0]+')**\n' if tags else '')+'\n```math\n'+re.sub(r'\\tag\{\d+\}','',expr).strip()+'\n```\n'
 return MATH.sub(convert,text)
topic='02 - Fluid–solid reactions with a solid reagent'
links=0;figures=set();tags=[];notehashes={}
for n in range(7,13):
 draft,=(ROOT/'other/work/drafts/Reaction Engineering II').glob(f'RE-{n:02} - *.md')
 canonical=draft.read_text(encoding='utf-8').strip()
 native=ROOT/'other/obsidian/CEBT-II Notes/Reaction Engineering II'/topic/draft.name
 read=ROOT/'notes/Reaction Engineering II'/topic/draft.name
 body=native.read_text(encoding='utf-8');g=read.read_text(encoding='utf-8')
 assert canonical==body.split('<!-- note-content:start -->',1)[1].split('<!-- note-content:end -->',1)[0].strip(),draft
 assert re.sub(r'\s+',' ',github(body)).strip()==re.sub(r'\s+',' ',g).strip(),read
 assert not re.search(r'\b(?:lecture|lecturer|slides?|PDF)\b',canonical,re.I),draft
 tags.extend(map(int,re.findall(r'\\tag\{(\d+)\}',canonical)))
 for p,s in [(native,body),(read,g)]:
  for m in re.finditer(r'(!?)\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))\)',s):
   target=m[2] or m[3]
   if urlsplit(target).scheme or target.startswith('#'):continue
   dest=(p.parent/unquote(target.split('#',1)[0])).resolve();assert dest.exists(),(p,target);links+=1
   if m[1]:figures.add(dest)
 notehashes[draft.name]=hashlib.sha256(draft.read_bytes()).hexdigest()
for p in figures:
 with Image.open(p) as im:im.verify()
assert tags==list(range(21,38)),tags
pdf=ROOT/'other/sources/Reaction Engineering II/CEBT II reaction engineering 2 - reactions of solids.pdf'
result={'independent_numeric_checks':len(checks),'checks':checks,
 'combined_time_s':integrated,'droplet_T_K':Ts,'droplet_T_C':Ts-273.15,
 'evaporation_rate_ratio':ratio,'mixed_mean_over_tau_for_99pct':residence,
 'absolute_slope_counterexample':{'tau_film':10,'tau_rxn':100,'film_initial_dXdt':1.5/10,'rxn_initial_dXdt':3/100,'ratio':(3/100)/(1.5/10)},
 'publication':{'notes':6,'equation_labels':tags,'links_checked_both_editions':links,'figures_opened_both_editions':len(figures),'native_reading_full_text_parity':True,'canonical_hashes':notehashes},
 'source_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest()}
OUT.write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['checks','publication']},indent=2))
print(json.dumps({k:v for k,v in result['publication'].items() if k!='canonical_hashes'},indent=2))

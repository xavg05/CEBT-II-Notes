from pathlib import Path
import json, math
from bisect import bisect_right
from PIL import Image

base=Path(__file__).resolve().parent
out={}
kg=.04;kl=.0002
out['resistance_examples']={}
for gas,H in [('N2',60),('O2',30),('CO2',1.05),('NH3',.00045),('SO2',.009)]:
    Kg=1/(1/kg+H/kl);Kl=H*Kg
    out['resistance_examples'][gas]={'Hc':H,'Kg_m_s':Kg,'Kl_m_s':Kl,'gas_resistance_fraction':(1/kg)/(1/Kg),'liquid_resistance_fraction':(H/kl)/(1/Kg)}
out['equilibrium_example']={'rho_mg':110000/(8314.5*293),'Hm_if_Hc_0_00045_rho_ml55_5':.00045*55.5/(110000/(8314.5*293))}
out['simple_absorber']={'Gm':1,'yB':.02,'yT':.002,'xT':0,'Hm':2,'Lmin':1.8,'L':2.34,'xB':.018/2.34}
sa=out['simple_absorber'];sa['xB_pinch']=sa['yB']/sa['Hm'];sa['Lmin']=sa['Gm']*(sa['yB']-sa['yT'])/(sa['xB_pinch']-sa['xT']);sa['Q']=sa['Gm']*(sa['yB']-sa['yT']);sa['xB']=sa['xT']+sa['Q']/sa['L']
out['simple_strip']={'L':1,'xT':.02,'xB':.002,'yB':0,'Hm':2,'Gmin':.018/.04,'max_LG':1/(.018/.04)}
out['diffusivity_calibration']={'kl_ref':.0002,'D_ref':2e-9,'D_A':1.5e-9,'delta':2e-9/.0002,'kl_A':.0002*1.5e-9/2e-9}
out['linear_ntu_example']={'G':1,'L':3,'Hm':2,'yT':.002,'yB':.02,'xT':0}
b=out['linear_ntu_example'];b['xB']=(b['yB']-b['yT'])/b['L'];b['dyB']=b['yB']-b['Hm']*b['xB'];b['dyT']=b['yT'];b['alpha']=1-b['Hm']/b['L'];b['ntu']=math.log(b['dyB']/b['dyT'])/b['alpha'];b['dy_lm']=(b['dyB']-b['dyT'])/math.log(b['dyB']/b['dyT']);b['Htu']=.6;b['z']=b['ntu']*.6;b['stages']=math.log(b['dyB']/b['dyT'])/math.log(b['L']/b['Hm']);b['hetp']=b['z']/b['stages'];assert abs(b['hetp']-.6*math.log(1.5)/(1-2/3))<1e-12
out['hydraulic_example']={'qg_m3_s':1,'Uf_m_s':2,'fraction':.55,'U':1.1,'A':1/1.1,'D':math.sqrt(4/(1.1*math.pi)),'K_ratio':.55**2}

xs=[0,.021,.031,.042,.053,.079,.106,.159]
ps=[0,1.6,2.4,3.3,4.2,6.7,9.3,15.2]
ys=[p/110 for p in ps]
def interp(x,xx,yy):
    i=max(0,min(len(xx)-2,bisect_right(xx,x)-1))
    return yy[i]+(yy[i+1]-yy[i])*(x-xx[i])/(xx[i+1]-xx[i])
G=.05;yB=.05;yT=.0001;xT=0;kga=1.5
xeq=interp(yB,ys,xs);Lmin=G*(yB-yT)/xeq;L=1.29*Lmin;r=L/G;xB=G*(yB-yT)/L
def f(y):return 1/(y-interp((y-yT)/r,xs,ys))
def simpson(n):
    h=(yB-yT)/n
    return h/3*(f(yT)+f(yB)+4*sum(f(yT+i*h) for i in range(1,n,2))+2*sum(f(yT+i*h) for i in range(2,n,2)))
# Exact integration on each linear-interpolation segment: Delta y=alpha*y+beta.
cuts=[yT]+[yT+r*x for x in xs[1:] if yT<yT+r*x<yB]+[yB]
ntu=0
for ya,yb in zip(cuts,cuts[1:]):
    da=1/f(ya);db=1/f(yb);alpha=(db-da)/(yb-ya)
    ntu+=(yb-ya)/da if abs(alpha)<1e-12 else math.log(db/da)/alpha
rho=110000/(8314.5*293)
lm=(yB-interp(xB,xs,ys)-yT)/math.log((yB-interp(xB,xs,ys))/yT)
coarse_y=[.0001,.0005,.001,.005,.01,.02,.03,.04,.05]
coarse_f=[10000,5000,2500,625,323,161,127,97,79]
coarse=sum((b-a)*(c+d)/2 for a,b,c,d in zip(coarse_y,coarse_y[1:],coarse_f,coarse_f[1:]))
out['ammonia']={'x':xs,'partial_pressure_kPa':ps,'y_from_p':ys,'xeq':xeq,'G':G,'yB':yB,'yT':yT,'xT':xT,'Q':G*(yB-yT),'Lmin':Lmin,'L':L,'L_G':r,'xB':xB,'yb_star':interp(xB,xs,ys),'rho_mg':rho,'ntu_exact_piecewise':ntu,'simpson_convergence':{str(n):simpson(n) for n in [1000,10000,100000]},'volume_m3':G/(rho*kga)*ntu,'endpoint_logmean':lm,'endpoint_logmean_volume':G*(yB-yT)/(rho*kga*lm),'source_coarse_trapezoid':coarse,'source_coarse_volume':G/(rho*kga)*coarse,'source_linear_rounded_volume':G*(yB-yT)/(rho*kga*((.012-.0001)/math.log(.012/.0001))),'coarse_relative_error':(coarse/ntu-1),'height_at_explicit_illustrative_A_1':G/(rho*kga)*ntu}
assert abs(simpson(100000)-ntu)<1e-6
assert all(f(y)>0 for y in coarse_y)
out['checks']=['positive driving force over ammonia range','piecewise analytic integral agrees refined Simpson to <1e-6','HETP relationship independently checked','gas/liquid overall coefficient conversion exact']
(base/'numerical-validation.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
figs=base.parents[4]/'notes'/'Separations II'/'figs'
figs.mkdir(parents=True,exist_ok=True)
crops={
'u1-contacting-stages':(5,(270,325,925,835)),
'u1-packed-column':(6,(285,600,1030,1310)),
'u1-tray-column':(7,(260,235,1030,810)),
'u1-operating-forces':(11,(255,605,1220,1190)),
'u1-pinch':(12,(190,175,950,685)),
'u1-film-profiles':(18,(95,540,1220,1125)),
'u1-pressure-drop':(27,(135,470,1230,1230)),
'u1-hydraulic-chart':(28,(300,830,970,1435)),
'u1-ammonia-equilibrium':(30,(175,740,740,1160)),
}
for name,(p,rect) in crops.items():
    im=Image.open(base/f'p{p:03}.png')
    sx=im.width/1334;sy=im.height/1888
    im.crop(tuple(round(v*(sx if i%2==0 else sy)) for i,v in enumerate(rect))).save(figs/f'{name}.png')
print(json.dumps(out,indent=2))

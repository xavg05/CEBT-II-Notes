from pathlib import Path
import math,json
from PIL import Image
root=Path(__file__).resolve().parent
def yi(x,a=5,g=.1):
    b=1-a-1/g-x*(a-1)/g
    return 2*a*x/g/(-b+math.sqrt(b*b-4*(a-1)*a*x/g))
x1=.209;x3=.05;K=1.7e-5;Pf=10;g=.1
y1,y3=yi(x1),yi(x3)
yb=(y1+y3)/2;S=(x1-x3)/(yb-x3)
j1=K*Pf*(x1-g*y1);j3=K*Pf*(x3-g*y3)
jm=(j1+j3)/2;jlm=(j1-j3)/math.log(j1/j3)
gas_approx=dict(y_in=y1,y_out=y3,y_mean=yb,S=S,j_in=j1,j_out=j3,j_mean=jm,j_log=jlm,A_mean=S*yb/jm,A_log=S*yb/jlm,ratio=j1/j3)
def integrate(n):
    dx=(x3-x1)/n; I=0;A=0;prevS=0;rows=[]
    for k in range(n):
        xa=x1+k*dx;xb=xa+dx;ya=yi(xa);yb_=yi(xb)
        xm=(xa+xb)/2;ym=(ya+yb_)/2
        I+=dx/(xm-ym);s=1-math.exp(-I)
        jm_=K*Pf*(xm-g*ym)
        da=ym*(s-prevS)/jm_;A+=da
        rows.append(dict(x=xb,y=yb_,S=s,ybar=(x1-(1-s)*xb)/s,A=A))
        prevS=s
    return rows
coarse=integrate(16);fine=integrate(20000)
fine[-1]['oxygen_recovery']=fine[-1]['S']*fine[-1]['ybar']/x1
# Reproduce source mesh .209,.200,.190,...,.050 using midpoint denominators.
xs=[.209]+[i/100 for i in range(20,4,-1)]
I=A=prevS=0;source_rows=[]
for xa,xb in zip(xs,xs[1:]):
    ya,yb_=yi(xa),yi(xb);xm=(xa+xb)/2;ym=(ya+yb_)/2
    I+=(xb-xa)/(xm-ym);s=1-math.exp(-I);j=K*Pf*(xm-g*ym)
    A+=ym*(s-prevS)/j
    source_rows.append(dict(x=xb,y=yb_,S=s,ybar=(x1-(1-s)*xb)/s,J=j,A=A))
    prevS=s
Re=.005*300e-6*1000/.001;Sc=.001/(1000*1.6e-9);Sh=.61*math.sqrt(Re)*Sc**(1/3);kf=Sh*1.6e-9/300e-6
Cp=.1*(1-.97);Cw=Cp+(.1-Cp)*math.exp(4.71e-6/kf)
salt=dict(Re=Re,Sc=Sc,Sh=Sh,kf=kf,Cp=Cp,Cw=Cw,rise=(Cw-.1)/.1,Rtrue=1-Cp/Cw)
def pi(c):return .0044*c-1.7e-6*c*c+7.9e-8*c**3
kfw=7.8e-6;Jstar=kfw*math.log(400/10);cw36=10*math.exp(1e-5/kfw)
whey=dict(Re=1.5*.02*1000/.001,Sc=.001/(1000*4e-11),threshold=pi(10),pi_gel=pi(400),Jstar=Jstar,Jstar_LMH=Jstar*3.6e6,pressure_gel=pi(400)+Jstar*3.6e6/250,cw36=cw36,pi36=pi(cw36),pressure36=pi(cw36)+36/250,table=[])
for j in [0,10,20,36,60,80,100,whey['Jstar_LMH']]:
    cw=10*math.exp((j/3.6e6)/kfw);whey['table'].append(dict(J_LMH=j,Cw=cw,pressure=pi(cw)+j/250))
R=.995;s=.3;c1=35;c3=c1*(1-s)**(-R);c2=c1/s*(1-(1-s)**(1-R))
d_in=55-.82*c1*R;d_out=55-.82*c3*R;jmean=.004*(d_in+d_out)/2;area=100/(24*jmean)
ro=dict(Q1_m3day=100/s,C3=c3,C2=c2,Cp_in=c1*(1-R),Cp_out=c3*(1-R),net_in=d_in,net_out=d_out,Jmean_mh=jmean,Amean=area,modules=math.ceil(area/3))
# Area quadrature in recovery for constant R and no polarisation.
n=20000;ds=s/n
ar=0
for k in range(n):
    sm=(k+.5)*ds;c=c1*(1-sm)**(-R);j=.004*(55-.82*c*R)
    ar+=(100/s/24)*ds/j
ro['A_integrated']=ar;ro['modules_integrated']=math.ceil(ar/3)
res=dict(gas_approx=gas_approx,gas_source_mesh=source_rows,gas_converged=fine[-1],salt=salt,whey=whey,ro=ro,osmotic_NaCl_01M_20C_bar=8.314462618*293.15*100*2/1e5)
(root/'results.json').write_text(json.dumps(res,indent=2))
assert abs(fine[-1]['S']-source_rows[-1]['S'])<.001
assert ro['modules']==18 and ro['modules_integrated']==17
assert abs(c1-(s*c2+(1-s)*c3))<1e-12
figdir=root.parents[4]/'notes'/'Separations II'/'figs'
figdir.mkdir(parents=True,exist_ok=True)
boxes={
 'u3-01-selective-structures.png':(2,(170,1090,1230,1460)),
 'u3-02-spiral-module.png':(6,(415,1140,1010,1535)),
 'u3-03-stream-definitions.png':(9,(120,950,1190,1320)),
 'u3-04-gas-selectivity.png':(17,(175,180,1250,1070)),
 'u3-06-gas-profiles.png':(27,(140,270,1160,1330)),
 'u3-08-polarisation.png':(31,(120,800,1190,1450)),
 'u3-10-whey-pressure.png':(43,(160,425,1080,955)),
 'u3-11-feed-bleed.png':(44,(340,315,1180,790)),
 'u3-11-ro-stages.png':(45,(220,995,1260,1410)),
}
for name,(p,box) in boxes.items():
    im=Image.open(root/f'p{p:03}.png')
    box=tuple(round(v*(im.width/1334 if k%2==0 else im.height/1888)) for k,v in enumerate(box))
    im.crop(box).save(figdir/name)
(root/'figure-crops.json').write_text(json.dumps(boxes,indent=2))
im=Image.open(root/'p040.png');im.crop(tuple(round(v*(im.width/1334 if k%2==0 else im.height/1888)) for k,v in enumerate((310,705,1150,810)))).save(root/'p040-polynomial.png')
print(json.dumps({k:v for k,v in res.items() if k!='gas_source_mesh'},indent=2))

import math,json
from pathlib import Path
R=8.314462618
out={}
def bisect(f,a,b):
 for _ in range(100):
  c=(a+b)/2
  if f(a)*f(c)<=0:b=c
  else:a=c
 return (a+b)/2
def ant(T,A,B,C):return 10**(A-B/(T+C))
pb=lambda T:ant(T,4.72583,1660.652,-1.461)
pt=lambda T:ant(T,4.07827,1343.943,-53.773)
pw=lambda T:ant(T,5.08354,1663.125,-45.622)
pd=lambda T:ant(T,4.07857,1501.268,-78.67)
P=1.01325
T=368.15;k1=pb(T)/P;k2=pt(T)/P;x=(1-k2)/(k1-k2);y=k1*x
out['25']={'bubble_C':bisect(lambda T:.5*(pb(T)+pt(T))-P,350,380)-273.15,'dew_C':bisect(lambda T:.5/pb(T)+.5/pt(T)-1/P,350,380)-273.15,'K':(k1,k2),'x':x,'y':y,'V':(.5-x)/(y-x)}
P=(1.362+.543)/2
out['26']={'P':P,'y':.681/P,'poynting':[math.exp(v*1e-6*(P-p)*1e5/(R*363.15)) for v,p in [(97.4,1.362),(115.2,.543)]]}
out['27']={'A':.5*R*298.15*(.171+.140),'x78':.5*(1-R*351.15/385*math.log(.927/.944)),'az_P78_bar':.944*math.exp(385/(R*351.15)*(1-.5*(1-R*351.15/385*math.log(.927/.944)))**2)}
p1,p2=1.1541,.7609;xaz=.682;g1=1.364/p1;g2=1.364/p2;l1,l2=math.log(g1),math.log(g2);a=l1*(1+(1-xaz)*l2/(xaz*l1))**2;b=l2*(1+xaz*l1/((1-xaz)*l2))**2
def vl(x,a,b):
 d=a*x+b*(1-x)
 return a*(b*(1-x)/d)**2,b*(a*x/d)**2
x=.1647;v1,v2=vl(x,a,b);pred=x*math.exp(v1)*p1+(1-x)*math.exp(v2)*p2
# asymmetric Margules gex=x(1-x)[A12(1-x)+A21*x], fit log gammas linear
# log gamma1=(1-x)^2[A12+2x(A21-A12)]; log gamma2=x^2[A21+2(1-x)(A12-A21)]
c11=(1-xaz)**2*(1-2*xaz);c12=(1-xaz)**2*2*xaz;c21=xaz**2*2*(1-xaz);c22=xaz**2*(2*xaz-1);det=c11*c22-c12*c21;ma=(l1*c22-c12*l2)/det;mb=(c11*l2-l1*c21)/det
mp=x*math.exp((1-x)**2*(ma+2*x*(mb-ma)))*p1+(1-x)*math.exp(x*x*(mb+2*(1-x)*(ma-mb)))*p2
out['28']={'gammaaz':(g1,g2),'a':a,'b':b,'infinite':(math.exp(a),math.exp(b)),'gammapredict':(math.exp(v1),math.exp(v2)),'P':pred,'y':x*math.exp(v1)*p1/pred,'relative_error':(1.1622-pred)/1.1622,'range_error':(1.1622-pred)/(1.364-p2),'margules_P':mp}
f=3.65*46
out['30']={'Tr':298.15/190.6,'f':f,'xideal':1.013/f,'gammas':[1.013/f/x for x in [.00207,.00286,.00283]],'H':[1.013/x for x in [.00207,.00286,.00283]]}
out['31']={'oxygen_mgL':.21/43000*55.5*32*1000,'nitrogen_mgL':.78/91000*55.5*28*1000,'H5':43000*math.exp(-1700*(1/278.15-1/298.15)),'ratio':math.exp(1700*(1/278.15-1/298.15))}
xw=1/(1+.5*.018015)
out['34']={'xsolute':1-xw,'gamma_m_if_gamma_x_1':xw,'a_m':xw*.5,'a_w':xw}
out['35']=[{'m':m,'salt':salt,'I':I,'limiting':math.exp(-1.171*z*math.sqrt(I)),'extended':math.exp(-1.171*z*math.sqrt(I)/(1+.3281*3*math.sqrt(I)))} for m in [.001,.01,.1,.5] for salt,I,z in [('NaCl',m,1),('CaCl2',3*m,2)]]
def g(x,q):return x*math.log(x)+(1-x)*math.log(1-x)+q*x*(1-x)
x=bisect(lambda x:math.log(x/(1-x))-2.5*(2*x-1),.00001,.49)
out['36']={'binodal':(x,1-x),'g50':g(.5,2.5),'gbinodal':g(x,2.5),'gain_Jmol_300K':(g(.5,2.5)-g(x,2.5))*R*300}
out['37']={'A':2*R*292.55,'table':[]}
for C in [15,10,0,-10]:
 q=2*292.55/(C+273.15);xb=bisect(lambda x:math.log(x/(1-x))-q*(2*x-1),.00001,.49999);xs=(1-math.sqrt(1-2/q))/2
 out['37']['table'].append({'C':C,'q':q,'binodal':(xb,1-xb),'spinodal':(xs,1-xs)})
a,b=2.62,3.02
# Newton independent common-activity solve
x,y=.11,.93
for _ in range(20):
 def F(x,y):
  vx=vl(x,a,b);vy=vl(y,a,b)
  return math.log(x)+vx[0]-math.log(y)-vy[0],math.log(1-x)+vx[1]-math.log(1-y)-vy[1]
 f1,f2=F(x,y);h=1e-6;fx=F(x+h,y);fy=F(x,y+h);j11=(fx[0]-f1)/h;j21=(fx[1]-f2)/h;j12=(fy[0]-f1)/h;j22=(fy[1]-f2)/h;det=j11*j22-j12*j21;x-=(f1*j22-j12*f2)/det;y-=(j11*f2-f1*j21)/det
curv=lambda x:1/(x*(1-x))-2*a*a*b*b/(a*x+b*(1-x))**3
out['38']={'binodal':(x,y),'residuals':F(x,y),'spinodal':(bisect(curv,.01,.5),bisect(curv,.5,.99)),'phaseI':(y-.5)/(y-x),'gammas':[tuple(math.exp(t) for t in vl(v,a,b)) for v in [x,y]],'activities':[(v*math.exp(vl(v,a,b)[0]),(1-v)*math.exp(vl(v,a,b)[1])) for v in [x,y]]}
out['39']={'spinodal':((1-math.sqrt(.2))/2,(1+math.sqrt(.2))/2),'curvature':[(x,1/(x*(1-x))-5) for x in [.1,.2,.4]]}
out['40']=[(x,1-5*x*(1-x)) for x in [.145,.27639320225,.4,.5]]
out['41']=[(T,1-292.55/T,(1-292.55/T)**.64) for T in [293.15,295.15,298.15,303.15,308.15]]
out['43']=[]
for name,p,mass in [('toluene',pt,92.1384),('decane',pd,142.2817)]:
 T=bisect(lambda T:pw(T)+p(T)-1.01325,350,373);y=p(T)/1.01325;ratio=pw(T)*18.01528/(p(T)*mass)
 out['43'].append({'name':name,'C':T-273.15,'y':y,'water_mass_ratio':ratio,'org_weight_fraction':1/(1+ratio)})
pc=lambda T:ant(T,3.96988,1203.526,-50.287)
def azx(T):return .5*(1-R*T/385.4778180960669*math.log(pc(T)/pb(T)))
Ta=bisect(lambda T:pb(T)*math.exp(385.4778180960669/(R*T)*(1-azx(T))**2)-1.01325,349,355)
out['27']['NIST_Antoine_az']={'C':Ta-273.15,'x':azx(Ta),'Pbenz78':pb(351.15),'Pcyclo78':pc(351.15)}
out['35_debye_nm']=[(I,math.sqrt(78.4*8.8541878128e-12*1.380649e-23*298.15/(2*6.02214076e23*1000*I*(1.602176634e-19)**2))*1e9) for I in [.001,.1]]
a,b=2.62,3.02
slope=lambda x:math.log(x/(1-x))+vl(x,a,b)[0]-vl(x,a,b)[1]
out['38']['minima']=(bisect(slope,.01,.25),bisect(slope,.85,.99))
Path(__file__).with_name('numerical-evidence.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))

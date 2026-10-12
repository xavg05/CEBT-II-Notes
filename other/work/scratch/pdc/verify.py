from math import *
from pathlib import Path
import json
R={}
R['heated']={'heat_capacity_flow':1000*.01*4200,'Q':1000*.01*4200*(50-20),'Q_after':1000*.01*4200*(50-15),'deltaQ':1000*.01*4200*5,'tau':1/.01,'rise_at_tau':10*(1-exp(-1))}
R['mixing']={'tau':2/.02,'at_tau':3*(1-exp(-1)),'react_gain':1/(1+.01*100),'react_tau':100/(1+.01*100),'react_at_50':3/2*(1-exp(-1)),'sensor_tau':.002*500/(200*.0005),'sensor_10':20+40*(1-exp(-1)),'pulse_c':(1*2+.1*10)/1.1,'pulse_v':1.1}
R['gas']={'T':300*.5**.4,'p_ratio':.5**1.4,'temperature_ratio_pressure':.5**(.4/1.4)}
R['first_order']={'at_tau':1-exp(-1),'at_3tau':1-exp(-3),'at_5tau':1-exp(-5),'t95':-100*log(.05),'step20':2*3*(1-exp(-1)),'impulse20':2/20*exp(-1),'integrator_slope':.002/2,'integrator_rise60':60*.002/2}
z=.5;tau=10;wd=sqrt(1-z*z)/tau
R['second']={'wd':wd,'peak_time':pi/wd,'period':2*pi/wd,'overshoot':exp(-pi*z/sqrt(1-z*z)),'decay_ratio':exp(-2*pi*z/sqrt(1-z*z)),'first_peak':1+exp(-pi*z/sqrt(1-z*z)),'critical_at_tau':1-2*exp(-1),'tanks_zeta':(20+80)/(2*sqrt(20*80)),'tanks_tau':sqrt(20*80)}
R['series']={'velocity':.001/(pi*.04**2/4),'delay':20*pi*.04**2/(4*.001),'tank_tau':.1/.001}
D=R['series']['delay'];R['series']['at125']=1-(1+(125-D)/100)*exp(-(125-D)/100)
rL,rG,hF,hG,uL,uG=896.9,4.2,675.5,2768.3,720.,2576.
B=rL*(hG-uL)-rG*(hG-uG);a=(hG-hF)/B;b=-1/B;c=1-(rL-rG)*a;d=(rL-rG)/B
R['boiler']={'B':B,'VF':a,'VQ':b,'GF':c,'GQ':d,'QperF':hG-hF,'equilibrium_energy_check':a+b*(hG-hF),'step_V_rate':a,'step_G':c,'combined_steady_V':a+b*(hG-hF),'combined_G':c+d*(hG-hF)}
R['reaction']={'gainAA':.5,'gainBA':.5,'A100':.5*(1-exp(-2)),'B100':.5-exp(-1)+.5*exp(-2)}
R['zero']={'y0':0.,'slope0':-2.,'minimum_time':log(3/2),'minimum':1-4*exp(-log(3/2))+3*exp(-2*log(3/2))}
R['gain']={'G0':10/(1*5*10),'invalid':1/(0-1)}
R['linear_reaction']={'steady':1.,'tau':100/(1+2*.01*100*1),'gain':1/(1+2*.01*100*1),'ss_feed':1+.01*100*1**2}
def rk4(f,y,t,dt):
 k1=f(t,y);k2=f(t+dt/2,[v+dt*w/2 for v,w in zip(y,k1)]);k3=f(t+dt/2,[v+dt*w/2 for v,w in zip(y,k2)]);k4=f(t+dt,[v+dt*w for v,w in zip(y,k3)])
 return [v+dt*(a+2*b+2*c+d)/6 for v,a,b,c,d in zip(y,k1,k2,k3,k4)]
def integrate(f,y,end,dt=.1):
 for i in range(round(end/dt)):y=rk4(f,y,i*dt,dt)
 return y
A=3;k=.02;hs=1;qin=.03
hn=integrate(lambda t,y:[(qin-k*sqrt(y[0]))/A],[hs],1000)[0]
znew=qin/k;z0=sqrt(hs);tn=2*A*hs**.5/k
implicit=2*A/k*((z0-sqrt(hn))+znew*log((znew-z0)/(znew-sqrt(hn))))
assert abs(implicit-1000)<1e-7
R['level']={'tau':tn,'gain':2*sqrt(hs)/k,'linear_final':1+2*sqrt(hs)/k*.01,'nonlinear_final':(qin/k)**2,'linear1000':1+(1-exp(-1000/tn)),'nonlinear1000':hn,'implicit1000':implicit,'z_linear1000':(znew+(z0-znew)*exp(-1000/tn))**2}
qs=.14+6.86;xs=(100*.14+6.86*2)/qs;kv=.0028;Kg=(100-xs)/qs*kv
R['three_tank']={'steady':xs,'tau':35/qs,'KB':6.86/qs,'Kv':Kg,'rise10':Kg*10,'rise_t5':Kg*10*(1-(1+1+1/2)*exp(-1)),'rise_t15':Kg*10*(1-(1+3+9/2)*exp(-3)),'exact_final10':(100*(.14+kv*10)+6.86*2)/(qs+kv*10),'linear_final10':xs+Kg*10}
# Independently integrate physical ODEs against analytic response curves.
for t in [1,10,30,100]:
 yy=integrate(lambda t,y:[y[1],(1-y[0]-2*z*tau*y[1])/tau**2],[0,0],t,.01)[0]
 exact=1-exp(-z*t/tau)*(cos(wd*t)+z/sqrt(1-z*z)*sin(wd*t));assert abs(yy-exact)<1e-9
 y2=integrate(lambda t,y:[(1-y[0])/100,(y[0]-y[1])/100],[0,0],t,.01)[1]
 assert abs(y2-(1-(1+t/100)*exp(-t/100)))<1e-9
 y3=integrate(lambda t,y:[(1-y[0])/5,(y[0]-y[1])/5,(y[1]-y[2])/5],[0,0,0],t,.01)[2]
 assert abs(y3-(1-(1+t/5+t*t/50)*exp(-t/5)))<1e-9
# Exact rational-function partial fractions checked at points away from poles.
for s in [.1,.5,2,3,1+2j]:
 den=s*(s+1)**2*(s+2)*((s-1)**2+16)
 rhs=1/(34*s)-1/(50*(s+2))-1/(100*(s+1))-1/(20*(s+1)**2)+((s-1)-1)/ (1700*((s-1)**2+16))
 assert abs(rhs-1/den)<1e-12
R['additional']={'absolute_c100':5+3*(1-exp(-1)),'tank_poles':[-1/20,-1/80],'second_poles':[-.5/10,sqrt(1-.5**2)/10],'react_pole':-(1+.01*100)/100,'three_qA60':.0028*60,'three_deltaq':.0028*10}
R['response_checks']='RK4 versus analytic curves and rational partial fractions passed'
Path('other/work/scratch/pdc/numerical-verification.json').write_text(json.dumps(R,indent=2))
print(json.dumps(R,indent=2))

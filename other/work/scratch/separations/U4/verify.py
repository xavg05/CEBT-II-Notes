from pathlib import Path
import math,json
out={}
out['working_capacity']={'mass_kg':100,'q_load':.2,'q_heel':.04,'capture_kg':100*(.2-.04)}
out['isotherms']={'theta_low':(.02*.5)/(1+.02*.5),'theta_high':(.02*500)/(1+.02*500),'liquid_q':.2*.1/(.05+.1),'freundlich_q':.1*.25**.5}
out['kinetics']={'tau_s':1/.02,'fraction_t150':1-math.exp(-.02*150)}
V,C0,M,Qm,Kd=1,.1,1,.2,.05
a=V;b=V*(Kd-C0)+M*Qm;c=-V*C0*Kd
root=(-b+math.sqrt(b*b-4*a*c))/(2*a)
out['batch']={'Ceq_kg_m3':root,'qeq_kg_kg':Qm*root/(Kd+root),'mass_residual':V*C0-V*root-M*Qm*root/(Kd+root),'target_C':.01,'target_M':V*(C0-.01)/(.2*.01/(.05+.01))}
times=[0,100,200,300,400,500,600];ratios=[0,0,0,.2,.5,.8,1]
area=sum((times[i+1]-times[i])*(2-ratios[i]-ratios[i+1])/2 for i in range(len(times)-1))
out['bed']={'capture_time_s':area,'capacity_kg_kg':.01*.2*area/10,'tb_s_5pct':200+.05/.2*100,'LUB_fraction':1-(200+.05/.2*100)/area}
out['pressure_swing']={'qH':.2*.5*5/(1+.5*5),'qL':.2*.5*.5/(1+.5*.5)}
out['pressure_swing']['deltaq']=out['pressure_swing']['qH']-out['pressure_swing']['qL']
out['chromatography']={'K':5,'VsVm':.4,'kprime':5*.4,'tm_min':2,'tr_min':2*(1+5*.4)}
N=(6/.3)**2;eff=((6-2)/.3)**2
A,B,C=.001,2e-6,.5
u=math.sqrt(B/C);H=A+B/u+C*u
out['efficiency']={'N':N,'Neff':eff,'halfwidth_min':2*math.sqrt(2*math.log(2))*.3,'8ln2':8*math.log(2),'uopt_m_s':u,'Hmin_m':H,'plates_L1m':1/H,'asymmetric_empirical_N':41.7*(6/1.2)**2/(1.5+1.25)}
k1,k2,N=2,2.5,10000
tr1,tr2=2*(1+k1),2*(1+k2);w1,w2=4*tr1/math.sqrt(N),4*tr2/math.sqrt(N)
exact=2*(tr2-tr1)/(w1+w2);approx=math.sqrt(N)/4*((k2/k1-1)/(k2/k1))*k2/(1+k2)
out['resolution']={'tr1':tr1,'tr2':tr2,'wb1':w1,'wb2':w2,'exact':exact,'approx':approx,'N_for_approx_R1_5':N*(1.5/approx)**2}
assert abs(out['batch']['mass_residual'])<1e-12
assert 0<root<C0
assert all(v>0 for v in [u,H,exact,approx])
Path(__file__).with_name('numbers.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))

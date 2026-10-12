from pathlib import Path
import math,json

def simpson(f,a,b,n=100000):
    assert n%2==0
    h=(b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+i*h) for i in range(1,n,2))+2*sum(f(a+i*h) for i in range(2,n,2)))
out={}
out['rates']={'A_removal_mol_s':.12,'mass_kg':.060,'area_m2':24.,'volume_m3':.003,'rate_mass':.12/.060,'rate_area':.12/24,'rate_volume':.12/.003,'reaction_extent_rate_2A':.12/2,'B_production_2A_3B':.12*3/2,'TOF_A_per_s':.12/(.060*.020)}
q=10.;k=.2;c0=2.;x=.8
out['CSTR']={'FA0':q*c0,'CA_out':c0*(1-x),'minus_rA':k*c0*(1-x),'volume_L':q*x/(k*(1-x)),'space_time_min':x/(k*(1-x)),'Da':x/(1-x)}
out['PFR']={'volume_L':q/k*(-math.log1p(-x)),'space_time_min':-math.log1p(-x)/k,'CSTR_to_PFR_volume':(x/(1-x))/(-math.log1p(-x)),'X_at_CSTR_volume':-math.expm1(-k*out['CSTR']['space_time_min']),'expanding_gas_volume_L':q/k*(-2*math.log1p(-x)-x)}
out['energy']={'adiabatic_dT_per_X':20000/100,'T_at_X_06':300+20000*.6/100,'reaction_heat_at_X_06_W':20000*.6,'k420_over_k300':math.exp(40000/8.314*(1/300-1/420))}
tau=6.;kr=.2
out['RTD']={'mean_min':tau,'variance_min2':9.,'N_estimate':tau*tau/9,'tank_tau_min':9/tau,'P_t_before_tau_half_N4':1-math.exp(-2)*sum(2**j/math.factorial(j) for j in range(4)),'P_t_before_tau_half_CSTR':1-math.exp(-.5),'first_order_X':{str(n):1-(1+kr*tau/n)**(-n) for n in [1,4,10]},'PFR_X':-math.expm1(-kr*tau)}
ccstr=(math.sqrt(5)-1)/2
seg=1-simpson(lambda th:math.exp(-th)/(1+th),0,30)
out['mixing']={'second_order_PFR_then_CSTR_Cout':(math.sqrt(3)-1)/2,'second_order_CSTR_then_PFR_Cout':ccstr/(1+ccstr),'second_order_PFR_then_CSTR_X':1-(math.sqrt(3)-1)/2,'second_order_CSTR_then_PFR_X':1-ccstr/(1+ccstr),'first_order_either_X':1-math.exp(-1)/2,'segregated_exponential_X_Da1':seg,'micromixed_CSTR_X_Da1':1-ccstr}
fine=1-simpson(lambda th:math.exp(-th)/(1+th),0,30,200000)
assert abs(seg-fine)<1e-12
# Verify central probability and species-balance identities independently.
for n in [1,4,10]:
 t_i=tau/n
 density=lambda t:t**(n-1)*math.exp(-t/t_i)/(math.factorial(n-1)*t_i**n)
 norm=simpson(density,0,180)
 mean=simpson(lambda t:t*density(t),0,180)
 variance=simpson(lambda t:(t-tau)**2*density(t),0,180)
 assert abs(norm-1)<1e-10 and abs(mean-tau)<1e-8 and abs(variance-tau*tau/n)<1e-7
assert abs(out['CSTR']['FA0']-q*out['CSTR']['CA_out']-out['CSTR']['minus_rA']*out['CSTR']['volume_L'])<1e-12
Path(__file__).with_name('numbers.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

"""Independent cross-review: recompute from stated model inputs, stdlib only."""
import math
import json
from pathlib import Path

R = 8.31446261815324
results = {}

def check(name, value, expected, tol=2e-5):
    assert math.isclose(value, expected, rel_tol=tol, abs_tol=tol), (name, value, expected)
    results[name] = value

def simpson(f, lo, hi, intervals=20000):
    h = (hi-lo)/intervals
    return h/3*(f(lo)+f(hi)+4*sum(f(lo+h*i) for i in range(1, intervals, 2))
                +2*sum(f(lo+h*i) for i in range(2, intervals, 2)))

# Section 1 examples and conservation normalisation.
check('RE01_extent', .01*100**2, 100)
check('RE01_A', -2*.01*100**2, -200)
check('RE01_B', 3*.01*100**2, 300)
check('RE02_CSTR_space_time', .8/(.1*.2), 40)
check('RE02_PFR_space_time', -math.log(.2)/.1, 16.0944)
check('RE02_CSTR_volume', .002*.8/(.1*.2), .08)
check('RE02_PFR_volume', -.002*math.log(.2)/.1, .03219)
check('RE03_concentration',100*.5/1.5,33.3333)
check('RE03_CSTR_space_time',.5*1.5/(.1*.5),15)
check('RE03_PFR_space_time',(-2*math.log(.5)-.5)/.1,8.86294)
check('RE04_adiabatic_temperature',300+50000*.6/1000,330)
check('RE05_N',100**2/2500,4)
check('RE05_fraction_before_mean',1-math.exp(-1),.632121)
check('RE06_CSTR_conversion',1-1/3,.666667)
check('RE06_four_tank_conversion',1-(1+2/4)**-4,.802469)
check('RE06_PFR_conversion',1-math.exp(-2),.864665)
check('RE06_PFR_then_CSTR',1-(-1+math.sqrt(3))/2,.633975)
check('RE06_CSTR_then_PFR',1-((math.sqrt(5)-1)/2)/(1+(math.sqrt(5)-1)/2),.618034)

# Diesel first-order times; original p25's unfinished length exercise.
k=.0552
t0=math.log(10)/k
t3=math.log(1000)/k
check('diesel_initial_PFR_s',t0,41.7135)
check('diesel_initial_Re',.005/(t0*1e-5),11.9865)
check('diesel_target_PFR_s',t3,125.1405)
check('diesel_remaining_at_PFR_time',(1+k*t3/10)**-10,.00523770)
check('diesel_remaining_at_rounded_time',(1+6.9/10)**-10,.00526178)
kt=10*(.001**(-1/10)-1)
check('diesel_chain_kt',kt,9.95262)
check('diesel_chain_time_s',kt/k,180.3011)
check('diesel_chain_time_factor',kt/(k*t0),4.32237)
factor=math.log(1000)/(10*math.log1p(k*t0/10))
check('diesel_length_factor',factor,3.33347)
check('diesel_length_extended_remaining',(1+k*t0/10)**(-10*factor),.001)
taui=t3/10
E=lambda t: t**9*math.exp(-t/taui)/(math.factorial(9)*taui**10)
check('diesel_RTD_normalisation_quadrature',simpson(E,0,40*taui),1)
check('diesel_RTD_conversion_quadrature',simpson(lambda t:E(t)*math.exp(-k*t),0,40*taui),(1+k*taui)**-10)

# Adsorption site inventories, BET sums, surface-area units and isosteres.
check('competitive_vacant',1/(1+1+2),.25)
check('competitive_A',1/(1+1+2),.25)
check('competitive_B',2/(1+1+2),.5)
Vm=1/(.09+.01)
C=1+.09/.01
nm=1e5*(Vm*1e-6)/(R*273.15)
area=nm*6.02214076e23*.162e-18
check('BET_Vm_cm3',Vm,10)
check('BET_C',C,10)
check('BET_amount_mol',nm,4.40316e-4)
check('BET_total_area_m2',area,42.9567)
check('BET_specific_area_m2_per_g',area/.100,429.567)
z=.2
f0=(1-z)/(1+(C-1)*z)
check('BET_column_normalisation',f0+sum(C*z**i*f0 for i in range(1,300)),1)
check('BET_loading_column_sum',sum(i*C*z**i*f0 for i in range(1,300)),C*z/((1-z)*(1+(C-1)*z)))
check('capillary_pressure_Pa',2*.07/(14e-9),1e7)
check('isosteric_enthalpy_kJ_per_mol',R*math.log(.2/.1)/(1/320-1/300)/1000,-27.663)

# Logarithmic kinetics slopes independently using centered finite differences.
def rate(PA,T):
    ks=math.exp(-40000/(R*T))
    KA=math.exp(30000/(R*T)-10)
    KB=math.exp(20000/(R*T)-8)
    KP=math.exp(15000/(R*T)-7)
    D=1+KA*PA+KB*2+KP*.3
    return ks*KA*KB*PA*2/D**2, (KA*PA/D,KB*2/D,KP*.3/D)
PA,T=1.2,450
rr,theta=rate(PA,T)
eps=1e-5
nfd=(math.log(rate(PA*math.exp(eps),T)[0])-math.log(rate(PA*math.exp(-eps),T)[0]))/(2*eps)
check('LH_order_finite_difference',nfd,1-2*theta[0])
h=.001
efd=R*T*T*(math.log(rate(PA,T+h)[0])-math.log(rate(PA,T-h)[0]))/(2*h)
eform=40000+(1-2*theta[0])*(-30000)+(1-2*theta[1])*(-20000)-2*theta[2]*(-15000)
check('LH_activation_finite_difference_J_per_mol',efd,eform)
check('LH_dilute_activation_kJ_per_mol',40-30-20,-10)
check('LH_A_order_at_point_eight',1-2*.8,-.6)

# Pellet effectiveness from direct volume quadrature, not copied expression.
phi=2
slab=lambda x:math.cosh(phi*x)/math.cosh(phi)
sphere=lambda rho:phi/math.sinh(phi) if rho==0 else math.sinh(phi*rho)/(rho*math.sinh(phi))
etas=simpson(slab,0,1)
etasp=simpson(lambda rho:3*rho*rho*sphere(rho),0,1)
check('slab_effectiveness_quadrature',etas,.482014)
check('sphere_effectiveness_quadrature',etasp,.805972)
check('sphere_centre_fraction',sphere(0),.551441)
check('sphere_flux_vs_volume_integral',3/phi**2*(phi/math.tanh(phi)-1),etasp)
Dm,DK=1e-5,2e-6
Dp=1/(1/Dm+1/DK)
check('Bosanquet_pore_diffusivity',Dp,1.66667e-6)
check('effective_diffusivity',.4/3*Dp,2.22222e-7)
cs=1/(1+etasp*1*(.001/3)/.001)
check('film_surface_fraction',cs,.788235)
check('film_overall_effectiveness',etasp*cs,.635295)
maxrise=1e5*1e-6*10/.2
check('Prater_internal_rise_K',maxrise,5)
check('Prater_beta',maxrise/500,.01)
check('Arrhenius_500_to_505_ratio',math.exp(80000/R*(1/500-1/505)),1.20989)
# Dimensional heat balances: representative exothermic/endothermic sign test.
for dH in [-1e5,1e5]:
    Cb,Cs=10,2
    kg,h=.001,100
    Ts_minus_Tb=-dH*kg/h*(Cb-Cs)
    assert Ts_minus_Tb*dH < 0
results['checks_passed']=len(results)
out=Path(__file__).with_name('independent-re-results.json')
out.write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
print(json.dumps(results,indent=2))

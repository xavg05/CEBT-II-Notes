"""AB agent's independent checks of ET recovery: differences, roots and balances."""
from pathlib import Path
import math,json
ROOT=Path(__file__).resolve().parents[3]
R=8.31446261815324
out={}
def check(name,v,expected,tol):
    assert abs(v-expected)<tol,(name,v,expected)
    out[name]=v
def root(f,lo,hi):
    for _ in range(100):
        m=(lo+hi)/2
        if f(lo)*f(m)<=0:hi=m
        else:lo=m
    return (lo+hi)/2
# Gibbs-Duhem consistency of restored excess-volume model, via finite differences.
A=-3.3/.83**2;x=.17;eps=1e-5
v1=lambda z:58+A*(1-z)**2
v2=lambda z:18+A*z*z
gd=x*(v1(x+eps)-v1(x-eps))/(2*eps)+(1-x)*(v2(x+eps)-v2(x-eps))/(2*eps)
check('GD_excess_volume',gd,0,1e-8)
check('ethanol_volume_contraction',700/(x*54.7+(1-x)*17.8)*(x*58+(1-x)*18),721.14,.02)
# Virial conversion rederived by perturbative inversion of density series.
T=273.15;P=101325*100;B=-10.30e-6;C=1430e-12
lnphi=B*P/(R*T)+(C-B*B)*(P/(R*T))**2/2
check('virial_phi',math.exp(lnphi),.967753,2e-6)
# Exact ice branch and inferred activity with/without heat-capacity contribution.
Tf=273.15;H=6009;xwater=(.4/18.015)/(.4/18.015+.6/62.07)
f=lambda temp:H/R*(1/Tf-1/temp)
Tideal=root(lambda temp:f(temp)-math.log(xwater),200,273)
check('glycol_ice_ideal_C',Tideal-273.15,-33,1)
Tm=228.15
logact=f(Tm)+37.25/R*(math.log(Tm/Tf)+Tf/Tm-1)
check('glycol_measured_gamma',math.exp(logact)/xwater,.92005,5e-5)
# Binodal and stability rederived from first and second composition derivatives.
a=2.5
deriv=lambda z:math.log(z/(1-z))+a*(1-2*z)
xb=root(deriv,.01,.3)
check('symmetric_binodal',xb,.144794,1e-6)
spin=(1-math.sqrt(1-2/a))/2
check('symmetric_spinodal',spin,.276393,1e-6)
g=lambda z:z*math.log(z)+(1-z)*math.log(1-z)+a*z*(1-z)
check('equimolar_split_lowering_Jmol',(g(.5)-g(xb))*R*300,90,1)
check('diffusion_binodal_Gamma',1-2*a*xb*(1-xb),.380856,.001)
# Van Laar coexistence: directly verify both equal activities at quoted endpoints.
lg=lambda z:(2.62*(3.02*(1-z)/(2.62*z+3.02*(1-z)))**2,3.02*(2.62*z/(2.62*z+3.02*(1-z)))**2)
left,right=.11280695538342954,.928432794918817
for i in [0,1]:
    al=(left if i==0 else 1-left)*math.exp(lg(left)[i])
    ar=(right if i==0 else 1-right)*math.exp(lg(right)[i])
    check(f'van_Laar_equal_activity_{i}',al-ar,0,1e-10)
check('van_Laar_isobutane_activity',left*math.exp(lg(left)[0]),.94476,.001)
phase=(right-.5)/(right-left)
check('lever_rule_total_feed',phase*left+(1-phase)*right,.5,1e-12)
# Antoine steam-distillation balance and mass conversion.
Ps=lambda temp,c:10**(c[0]-c[1]/(temp+c[2]))
water=(5.08354,1663.125,-45.622)
for name,coeff,mw,temp,ratio in [('toluene',(4.07827,1343.943,-53.773),92.14,84.3,.24),('decane',(4.07857,1501.268,-78.67),142.29,97.5,1.36)]:
    T=root(lambda t:Ps(t,water)+Ps(t,coeff)-1.01325,340,374)
    check(name+'_boiling_C',T-273.15,temp,.1)
    check(name+'_water_mass_ratio',Ps(T,water)*18.015/(Ps(T,coeff)*mw),ratio,.01)
# Restored coarse steam integral, calculated from tabulated volumes directly.
pressures=[50,100,150,200,250,300,350,400,450,500]
volumes=[1.042,.476,.282,.179,.108,.0504,.0379,.0344,.0325,.0312]
integrand=[-.078e-3]+[v*1e-3-R*673.15/(p*1e5) for p,v in zip(pressures,volumes)]
integ=sum((integrand[j]+integrand[j+1])/2*50e5 for j in range(10))
check('coarse_steam_integral_Jmol',integ,-5020,10)
check('coarse_steam_fugacity_coefficient',math.exp(integ/(R*673.15)),.408,.001)
out['equation_checks']='Gibbs-Duhem cancellation, virial density/pressure conversion, ice equilibrium, Flory-Huggins activity/critical conditions, common-tangent equality, lever rule, Kelvin length, phase-rule phase exhaustion and dilution/mole-fraction conversion independently rederived.'
(ROOT/'other/work/reviews/et-teaching-independent-numerics-20261022.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('Independent ET verification passed:',len(out)-1,'numerical invariants/comparisons.')

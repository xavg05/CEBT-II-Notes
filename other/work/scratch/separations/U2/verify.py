"""Reproducible drying calculations. All pressures kPa, temperatures degC except saturation polynomial."""
import math,json
from pathlib import Path
from PIL import Image
base=Path(__file__).resolve().parent
def psat(t):
    # ASHRAE ideal-water saturation polynomial above freezing, output kPa.
    T=t+273.15
    return math.exp(-5800.2206/T+1.3914993-0.048640239*T+0.000041764768*T*T-0.000000014452093*T**3+6.5459673*math.log(T))/1000
eps=.621945
def hs(t,P=100):
    p=psat(t)
    return eps*p/(P-p)
def h(t,H):return 1.006*t+H*(2501+1.86*t)
def root(f,lo=0,hi=50):
    for _ in range(90):
        mid=(lo+hi)/2
        if f(mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2
def tw(t,H):return root(lambda x:h(x,hs(x))-h(t,H)-(hs(x)-H)*4.186*x)
def H_from_tw(t,wb):
    return (hs(wb)*(2501+(1.86-4.186)*wb)-1.006*(t-wb))/(2501+1.86*t-4.186*wb)
w1,w2,Hi,HW=.9,.1,.0036,.0156
mmin=(w1-w2)/(HW-Hi);m=1.2*mmin
a=HW-Hi+w2/m;b=1/m
wc=10*a/(.5+10*b)
tc=math.log((a-b*wc)/(a-b*w1))/(10*b)
tf=math.log(wc/w2)/.5
Hout=Hi+(w1-w2)/m
wc_co=10*((HW-Hi)-w1/m)/(.5-10/m)
co_end=max(w2,wc_co)
tc_co=math.log((HW-Hi)/((HW-Hi)-(w1-co_end)/m))/(10/m)
tf_co=math.log(wc_co/w2)/.5 if wc_co>w2 else 0
def trap(n):
    dx=(w1-w2)/n
    def y(w):return 1/min(10*(a-b*w),.5*w)
    return dx*(.5*(y(w1)+y(w2))+sum(y(w2+i*dx) for i in range(1,n)))
out={
 'saturation_30':hs(30),'saturation_30_chart':.0272,'percent_saturation_chart':100*.015/.0272,
 'percent_saturation_correlation':100*.015/hs(30),'relative_humidity_30_percent':100*(100*.015/(eps+.015))/psat(30),
 'enthalpy_40_H002':h(40,.02),'humid_heat_H002':1.006+.02*1.86,
 'adiabatic_sat_40_H001':tw(40,.01),'adiabatic_sat_H':hs(tw(40,.01)),
 'constant_h_sat_40_H001':root(lambda x:h(x,hs(x))-h(40,.01)),
 'dewpoint_H001':root(lambda x:psat(x)-100*.01/(eps+.01)),
 'wetbulb_25_H001_thermodynamic_approx':tw(25,.01),'wetbulb_H':hs(tw(25,.01)),
 'humidity_40_tw20_thermodynamic_approx':H_from_tw(40,20),
 'relative_humidity_40_tw20_percent':100*(100*H_from_tw(40,20)/(eps+H_from_tw(40,20)))/psat(40),
 'm_min':mmin,'m':m,'operating_intercept':a,'operating_slope':-b,'w_c':wc,'t_constant_h':tc,'t_falling_h':tf,'t_total_h':tc+tf,'H_exit':Hout,
 'exit_T_constant_h':(h(50,Hi)-2501*Hout)/(1.006+1.86*Hout),
 'cocurrent_w_c':wc_co,'cocurrent_t_constant_h':tc_co,'cocurrent_t_falling_h':tf_co,'cocurrent_t_total_h':tc_co+tf_co,
 'trapezoid_8':trap(8),'trapezoid_80':trap(80),'trapezoid_800':trap(800),
 'constant_external_example_s':(.2*2400000)/(40*2*(50-25)),
 'indirect_example_K':200/40,
 'quadrature_table':[{'w':w,'DeltaH':a-b*w,'r_per_h':min(10*(a-b*w),.5*w),'reciprocal_h':1/min(10*(a-b*w),.5*w)} for w in [.1,.2,.212,.3,.5,.7,.9]],
 'moisture_conversion':{'wet_fraction_at_w09':.9/1.9,'dry_w_at_wet_fraction02':.2/.8},
 'gas_endpoint_checks':{'counter_H_at_w2':Hi+(w2-w2)/m,'counter_H_at_w1':Hi+(w1-w2)/m,'co_H_at_w1':Hi+(w1-w1)/m,'co_H_at_w2':Hi+(w1-w2)/m},
 'all_constant_time_both_flows_h':math.log((HW-Hi)/(HW-Hout))*m/10,
}
assert abs(out['gas_endpoint_checks']['counter_H_at_w1']-Hout)<1e-12
assert w2<wc<w1 and 0<wc_co<w2
assert abs(trap(800)-(tc+tf))<.001
(base/'numerical-validation.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
# Original scan crops, specified in pixel coordinates, no reconstructed content.
figs=base.parents[4]/'notes'/'Separations II'/'figs'
figs.mkdir(parents=True,exist_ok=True)
crops={
 'u2-humidity-chart':(3,(65,590,1300,1570)),
 'u2-dewpoint':(12,(105,900,1160,1620)),
 'u2-wet-bulb':(13,(115,700,1260,1230)),
 'u2-chloroform-chart':(19,(140,420,1230,1370)),
 'u2-moisture-isotherm':(20,(0,390,1320,1310)),
 'u2-drying-periods':(21,(15,655,1310,1700)),
 'u2-countercurrent':(26,(30,190,1310,535)),
 'u2-cocurrent':(29,(120,530,1285,1020)),
 'u2-drying-rate-family':(30,(120,310,1230,1120)),
 'u2-other-solvent':(32,(270,580,1130,1270)),
}
for name,(page,box) in crops.items():
    im=Image.open(base/f'p{page:03}.png')
    sx,sy=im.width/1334,im.height/1888
    actual=(round(box[0]*sx),round(box[1]*sy),round(box[2]*sx),round(box[3]*sy))
    im.crop(actual).save(figs/f'{name}.png')

"""Independent arithmetic, equation and source-preservation checks for AB recovery."""
from pathlib import Path
import math,json,re,subprocess
ROOT=Path(__file__).resolve().parents[3]
out={}
def check(key,value,target,tol):
    assert abs(value-target)<=tol,(key,value,target,tol)
    out[key]=value
R=1.98720425864083
for n,target in [(20,6.65),(150,43.6),(1000,170)]:
    L=.34*n;lp=50
    rms=math.sqrt(2*lp*L*(1-lp/L*(1-math.exp(-L/lp))))
    check(f'AB02_rms_{n}',rms,target,.5 if n==1000 else .05)
# Per-strand concentration for an equimolar non-self-complementary duplex.
for c,target in [(1e-6,48.4),(1e-4,60.6)]:
    check(f'AB03_Tm_{c}',-80000/(-220+R*math.log(c/2))-273.15,target,.06)
for sodium,target in [(1,50.9),(.15,41.9)]:
    entropy=-240.3+.368*11*math.log(sodium)
    check(f'AB04_Tm_{sodium}',-87200/(entropy+R*math.log(1e-6/2))-273.15,target,.06)
check('AB05_encounter',1/(1e5*1e-6),10,1e-10)
for n,target in [(200,.99652),(1000,.99931)]:check(f'AB07_required_P_{n}',.5**(1/(n-1)),target,.000005)
check('AB07_full_length',.994**59,.701,.0005)
check('AB07_single_deletion',59*.006*.994**58,.250,.0005)
for e,number in [(1/300,83),(1/1500,5)]:
    Y=(1-e)**1000
    out[f'AB08_error_free_{e}']=Y
    assert math.ceil(math.log(.05)/math.log1p(-Y))==number
    out[f'AB08_clones_{e}']=number
check('AB10_uncovered_1',math.exp(-1),.368,.0005)
check('AB10_uncovered_10',math.exp(-10),4.54e-5,5e-8)
check('AB11_reads',30*3.1e9/150,6.2e8,1e-5)
check('AB12_one_or_more_errors',1-.999**150,.139,.0005)
def bound(n,p):return sum(math.comb(n,j)*p**j*(1-p)**(n-j) for j in range(math.ceil(n/2),n+1))
check('AB12_consensus_bound',bound(30,.001),1.53e-37,5e-40)
for n,target in [(5,1.16e-3),(10,6.37e-5),(30,2.31e-12)]:check(f'AB13_bound_{n}',bound(n,.05),target,.005*target)
NA=6.02214076e23
check('AB14_one_molecule_uM',1/(NA*20e-21)*1e6,83,1)
check('AB14_free_occupancy',5e-6*NA*20e-21,.0602,.00005)
check('AB14_confocal_occupancy',5e-6*NA*1e-15,3011,.5)
p=46.7/3100;f=.1
pp=p*(1+f/2)/(1+f*p/2);dp=pp-p
check('AB15_p',p,.015065,.0000005)
check('AB15_pp',pp,.015806,.0000005)
check('AB15_relative_percent',100*dp/p,4.92,.005)
check('AB15_reads_z5',p*(1-p)*(5/dp)**2,6.75e5,1000)
check('AB15_small_f_depth_ratio',(.1/.04)**2,6.25,1e-10)
check('AB16_decade_cycles',math.log2(10),3.32,.005)
check('AB17_multiplicative_sd',2**.3,1.23,.005)
check('AB17_actual_fold',1.9**3.3,8.315,.0005)
check('AB17_assumed_fold',2**3.3,9.849,.0005)
check('AB17_overestimate_percent',(2**3.3/1.9**3.3-1)*100,18.4,.05)
check('AB19_sampling_fraction',-math.expm1(-1e15/4**40),8.27e-10,5e-13)
for j,target in [(9,.0909),(12,.9901)]:check(f'AB19_enriched_fraction_{j}',1e-10*10**j/(1-1e-10+1e-10*10**j),target,.00005)
check('AB21_square_side',math.sqrt(7249*.34*2.5),78.5,.05)
check('AB21_crossover_distance',16*.34,5.44,1e-10)
check('AB22_per_base_factor',math.exp(1.5/(R/1000*298.15)),12.6,.05)
check('AB34_pressure_area',2**.25,1.189,.0005)
u=(1e-6)**2*300*9.81/(18e-3)
check('AB36_settling_velocity',u,1.64e-7,.005e-7)
check('AB36_gravity_days',.1/u/86400,7.08,.005)
check('AB36_enhanced_seconds',.1/(u*1e4),61.2,.05)
check('AB37_speed_fraction',2**(-1.5),.354,.0005)
# Refit retained empirical homogeniser data with origin-constrained slopes.
release={200:[5,9.5,14,18,22,26],300:[13.5,23.5,33.5,43,47.5,55],400:[23.3,40,52.5,66.6,73,79.5],500:[36,58.5,75,82.5,88.5,91.3],550:[42,66,83.7,88.5,94.5]}
slopes={p:sum(n*(-math.log1p(-v/100)) for n,v in enumerate(vals,1))/sum(n*n for n in range(1,len(vals)+1)) for p,vals in release.items()}
x=[math.log(p) for p in slopes];y=[math.log(s) for s in slopes.values()]
xbar=sum(x)/len(x);ybar=sum(y)/len(y)
a=sum((xx-xbar)*(yy-ybar) for xx,yy in zip(x,y))/sum((xx-xbar)**2 for xx in x)
lnk=ybar-a*xbar;k=math.exp(lnk)
r2=1-sum((yy-(lnk+a*xx))**2 for xx,yy in zip(x,y))/sum((yy-ybar)**2 for yy in y)
check('AB40_a',a,2.37420,.000005)
check('AB40_k',k,1.73301e-7,5e-13)
check('AB40_R_squared',r2,.9994,.00005)
check('AB40_real_passes',-math.log(.2)/(k*460**a),4.4,.05)
check('AB40_pressure',(-math.log(.3)/(2*k))**(1/a),570,5)
check('AB40_double_pressure_pass_factor',2**2.37,5.2,.05)
for r,recovery,ratio in [(.5,.677,2.032),(5,.955,1.145)]:
    check(f'AB42_recovery_{r}',4.2*r/(1+4.2*r),recovery,.0005)
    check(f'AB42_concentration_{r}',4.2*(1+r)/(1+4.2*r),ratio,.0005)
check('AB48_effective_half_life',math.log(2)/(math.log(2)/5+math.log(2)/20),4,1e-10)
check('AB54_acceptable_mass',100*.9*.8*.95,68.4,1e-10)
assert 438+35==473
check('AB55_unknown_fraction_percent',149/473*100,31.5,.05)
comp=str.maketrans('ACGT','TGCA')
for seq,expect in [('CGATCG',True),('GGGGCCCC',True),('CAGATCTG',True),('CGCG',True),('CCGATGCG',False)]:
    rc=seq.translate(comp)[::-1]
    assert (seq==rc)==expect
    out[f'AB57_reverse_complement_{seq}']=rc
check('AB57_production',25*250/250,25,1e-10)
check('AB57_mean_minutes',30000/25/60,20,1e-10)
check('AB57_half_minutes',20*math.log(2),13.9,.05)
# Reviewed numbering retained; only historical labels 74 and 124--126 return.
for pth in (ROOT/'other/work/archive/reviewed-units/Advanced Biotechnology').glob('*.md'):
    text=pth.read_text(encoding='utf-8'); tags=re.findall(r'\\tag\{(\d+)\}',text)
    assert len(tags)==len(set(tags)),(pth,'duplicate equation tags')
    original=subprocess.check_output(['git','show','HEAD:'+pth.relative_to(ROOT).as_posix()],cwd=ROOT).decode('utf-8')
    assert set(re.findall(r'\\tag\{(\d+)\}',original))<=set(tags)
    assert not re.search(r'^#{1,6} .*Worked example',text,re.M|re.I)
    for image in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',text):assert (pth.parent/image).is_file(),(pth,image)
(ROOT/'other/work/reviews/AB-worked-content-numerics-20261022.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(out)} numerical/sequence checks, canonical equation-label preservation and image links.')

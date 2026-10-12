"""Independent adsorption review computations, written without consulting author code."""
import json,math,re
from pathlib import Path
out={}
out['cycle_mass']=100*(.2-.04)
out['theta_low']=.02*.5/(1+.02*.5)
out['theta_high']=.02*500/(1+.02*500)
out['liquid_loading']=.2*.1/(.05+.1)
out['time_constant']=1/.02
out['uptake_fraction']=1-math.exp(-.02*150)
# Bisect inventory residual, independent of author's quadratic implementation.
lo,hi=0,.1
for _ in range(100):
    C=(lo+hi)/2
    resid=C+.2*C/(.05+C)-.1
    if resid>0:hi=C
    else:lo=C
Ce=(lo+hi)/2
out['batch_Ce']=Ce
out['batch_qe']=.2*Ce/(.05+Ce)
out['batch_residual']=Ce+out['batch_qe']-.1
out['mass_target']=(.1-.01)/(.2*.01/(.05+.01))
times=[0,100,200,300,400,500,600]
fr=[0,0,0,.2,.5,.8,1]
out['capture_time']=sum((times[i+1]-times[i])*(2-fr[i]-fr[i+1])/2 for i in range(6))
out['capacity_increase']=.01*.2*out['capture_time']/10
out['breakthrough_005']=200+(.05/.2)*100
out['unused_fraction']=1-out['breakthrough_005']/out['capture_time']
out['q_high']=.2*.5*5/(1+.5*5)
out['q_low']=.2*.5*.5/(1+.5*.5)
out['working_capacity']=out['q_high']-out['q_low']
out['retention_factor']=5*.4
out['retention_time']=2*(1+out['retention_factor'])
out['gauss_N']=(6/.3)**2
out['gauss_effective_N']=((6-2)/.3)**2
out['half_height_width']=2*math.sqrt(2*math.log(2))*.3
out['optimum_u']=math.sqrt(2e-6/.5)
out['minimum_H']=.001+2e-6/out['optimum_u']+.5*out['optimum_u']
out['column_N']=1/out['minimum_H']
tr1,tr2=2*(1+2),2*(1+2.5)
w1,w2=4*tr1/100,4*tr2/100
out.update(tr1=tr1,tr2=tr2,w1=w1,w2=w2)
out['resolution_measured']=2*(tr2-tr1)/(w1+w2)
out['resolution_exact_equalN']=100/2*(2.5-2)/(2+2+2.5)
out['resolution_approx']=100/4*((2.5/2-1)/(2.5/2))*(2.5/(1+2.5))
out['required_N_approx']=(1.5/(out['resolution_approx']/100))**2
assert abs(out['batch_residual'])<1e-14
assert abs(out['resolution_measured']-out['resolution_exact_equalN'])<1e-14
assert abs(out['required_N_approx']-1764)<1e-9
# Structural review is against planned final topic location, since drafts aren't public.
repo=Path(__file__).resolve().parents[5]
draft=repo/'other/work/drafts/Separations II/U4'
checks=[]
for f in sorted(draft.glob('*.md')):
    s=f.read_text(encoding='utf8')
    heads=re.findall(r'^## (.*)$',s,re.M)
    tags=[int(x) for x in re.findall(r'\\tag\{(\d+)\}',s)]
    figs=re.findall(r'!\[[^\]]*\]\(\.\./figs/([^)]*)\)',s)
    checks.append({'file':f.name,'seven_sections':len(heads)==7,'sequential_local_tags':tags==list(range(1,len(tags)+1)),'figure_targets':[{'name':p,'exists':(repo/'notes/Separations II/figs'/p).exists()} for p in figs]})
out['structure']=checks
assert len(checks)==9 and all(x['seven_sections'] and x['sequential_local_tags'] for x in checks)
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))

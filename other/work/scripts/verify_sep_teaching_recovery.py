"""Re-run the reviewed numerical models without rewriting historical artifacts."""
from pathlib import Path
import re,json,math,subprocess
from PIL import Image
ROOT=Path(__file__).resolve().parents[3]
out={}
for unit,stop,key in [('U1',"# Independently transcribed",'result'),('U2',"(base/'numerical-validation.json')",'out'),('U3',"(root/'results.json')",'res'),('U4',"Path(__file__).with_name",'out')]:
    p=ROOT/('other/work/scratch/separations/review-U1/independent.py' if unit=='U1' else f'other/work/scratch/separations/{unit}/verify.py')
    ns={'__file__':str(p)}
    exec(compile(p.read_text(encoding='utf-8').split(stop)[0],str(p),'exec'),ns)
    out[unit]=ns[key]
assert abs(out['U1']['Henry']['Hm']-.553116)<1e-6
assert abs(out['U2']['t_total_h']-14.8445)<.0001
assert out['U3']['ro']['modules']==18 and out['U3']['ro']['modules_integrated']==17
assert abs(out['U4']['resolution']['N_for_approx_R1_5']-1764)<1e-8
native=ROOT/'other/obsidian/CEBT-II Notes/Separations II'
read=ROOT/'notes/Separations II'
labels=[];figures=set();notes=0
for p in sorted(native.rglob('SEP-*.md')):
    s=p.read_text(encoding='utf-8');rel=p.relative_to(native);g=(read/rel).read_text(encoding='utf-8')
    before=subprocess.check_output(['git','show','HEAD:'+p.relative_to(ROOT).as_posix()],cwd=ROOT).decode('utf-8')
    tags=re.findall(r'\\tag\{(\d+)\}',s)
    assert tags==re.findall(r'\\tag\{(\d+)\}',before),p
    assert tags==re.findall(r'\*\*Equation \((\d+)\)\*\*',g),p
    assert not re.search(r'^## Worked example',s,re.M)
    assert not re.search(r'\b(?:PDF|lecture|lecturer|slides)\b',s,re.I),p
    assert s.count('## Link to other topics')==1
    for f in re.findall(r'!\[[^]]*\]\(\.\./figs/([^)]*)\)',s):
        figures.add(f)
        for base in [read,native]:
            with Image.open(base/'figs'/f) as im:im.verify()
    labels+=tags;notes+=1
out['publication']={'notes':notes,'preserved_labels':len(labels),'referenced_figures_opened':len(figures)}
(ROOT/'other/work/reviews/sep-teaching-recovery-verification.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out['publication'],indent=2))

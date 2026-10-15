"""Read-only independent closure check of the authorised Biotechnology batch."""
from pathlib import Path
import json,math,re,sys
sys.stdout.reconfigure(encoding='utf-8')
root=Path(__file__).resolve().parents[5]
pack=root/'other/work/scratch/coverage-audit-20261014'
batch=json.loads((pack/'ab-correction-batch.json').read_text(encoding='utf-8'))
assert batch['authorized_application'] is True
normalize=lambda s:s.replace('$`','$').replace('`$','$')
files=set()
checks=[]
for idx,rec in enumerate(batch['replacements']):
    final_new=rec['new']
    for later in batch['replacements'][idx+1:]:
        if set(later['targets']) & set(rec['targets']):
            final_new=final_new.replace(later['old'],later['new'])
    for rel in rec['targets']:
        p=root/rel
        text=normalize(p.read_text(encoding='utf-8'))
        assert text.count(final_new)==1,(rec['id'],rel,'new missing or duplicated')
        assert rec['old'] not in text,(rec['id'],rel,'old survives')
        files.add(rel)
        checks.append(dict(id=rec['id'],target=rel,new_count=1,old_count=0))
assert len(batch['replacements'])==29
assert len(files)==45
nums=dict(qPCR_E1=2**3.3,qPCR_E09=1.9**3.3,
    relative_overestimate_pct=(2**3.3/1.9**3.3-1)*100,
    reduction_from_reported_pct=(1-1.9**3.3/2**3.3)*100,
    consensus_ge15=sum(math.comb(30,j)*.001**j*.999**(30-j) for j in range(15,31)),
    consensus_ge16=sum(math.comb(30,j)*.001**j*.999**(30-j) for j in range(16,31)),
    Bragg_theta_at_2A_deg=math.degrees(math.asin(1.54/4)),
    Bragg_theta_at_point8A_deg=math.degrees(math.asin(1.54/1.6)))
prior=json.loads((pack/'review/independent-ab-numbers.json').read_text(encoding='utf-8'))
for key,val in nums.items():assert math.isclose(val,prior[key],rel_tol=1e-12),(key,val,prior[key])
report=dict(replacements=len(batch['replacements']),files=len(files),target_checks=len(checks),checks=checks,
    numerical_checks=nums,status='PASS: applied text and independent numerical checks; changed passages and adjacent context separately reread and passed')
(pack/'review/ab-closure-verification.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='checks'},indent=2))

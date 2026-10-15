from pathlib import Path
import json
root=Path(__file__).resolve().parents[5]
p=next((root/'other/work/archive/reviewed-units/Advanced Biotechnology').glob('08 - *.md'))
s=p.read_text(encoding='utf-8')
items=[]
for anchor,new in [
('NMR works **in solution at room temperature**',
 'Solution NMR studies proteins under chosen solution conditions and can provide both structural restraints and, through suitable relaxation or exchange experiments, information about conformational dynamics. Resonance overlap and relaxation make larger proteins harder to study. Roughly 30 kDa is a useful practical scale for conventional solution structure determination, rather than a universal size limit; feasibility depends on the protein, labelling and experiment.'),
('**Shared limitation.**',
 '**Structure and motion.** Conventional crystallography and single-particle cryo-EM reconstructions describe averaged density or classified conformations. NMR relaxation and exchange experiments can quantify motion over accessible timescales, but a calculated structural ensemble alone is not a measured trajectory. Time-resolved crystallography can also probe structural changes. The distinction therefore depends on the experimental observables, rather than an absolute division into static and dynamic methods.')]:
    old=next(q for q in s.split('\n\n') if q.startswith(anchor))
    assert s.count(old)==1
    items.append(dict(canonical=str(p.relative_to(root)).replace('\\','/'),note='AB-25',old=old,new=new))
(Path(__file__).parent/'ab25-adjacent-corrections.json').write_text(json.dumps(items,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('Two exact adjacent AB25 replacement proposals; no notes edited.')

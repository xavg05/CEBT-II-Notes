"""Explicit review corrections and non-equation labels for final publication."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[4]
FINAL=ROOT/'out/work/scratch/final-delivery'

def corrections():
    p=FINAL/'corrections.json'
    return json.loads(p.read_text()) if p.exists() else []

def reviewed(p):
    s=p.read_text()
    for fix in corrections():
        if fix['source']==str(p.relative_to(ROOT)):
            assert s.count(fix['old'])==1,(p,fix['old'])
            s=s.replace(fix['old'],fix['new'],1)
    return s

CHEMICAL=re.compile(r'\b(?:ethanol|water|oxygen|argon|peroxide|glycol|benzene|hexane|cyclohexane|toluene|chloroform|THF|pentane|propanal|ethane|propene|isobutane|furfural|nitrobenzene)\s*\(\d+\)',re.I)
def protect_labels(s):
    saved={}
    def protect(m):
        key=f'PRESERVENUMERICLABEL{len(saved)}END'
        saved[key]=m[0]
        return key
    # Figure-panel indices and chemical-component numbers are not equations.
    s=re.sub(r'!\[([^\]]*)\]',lambda m:re.sub(r'\(\d+\)',protect,m[0]),s)
    s=CHEMICAL.sub(protect,s)
    return s,saved

def restore_labels(s,saved):
    for k,v in saved.items():s=s.replace(k,v)
    return s

def figure_source(original):
    p=FINAL/'figure-overrides.json'
    overrides=json.loads(p.read_text()) if p.exists() else {}
    key='figs/'+original.name
    return ROOT/overrides[key] if key in overrides else original

def relocated_source(path):
    if path.exists():return path
    rel=str(path.relative_to(ROOT))
    if rel.startswith('sources/Advanced Biotech/'):
        rel=rel.replace('sources/Advanced Biotech/','sources/Advanced Biotechnology/',1)
        rel=rel.replace('/Lecture 7.pdf','/Lecture7.pdf')
        other=ROOT/rel
        if other.exists():return other
    return path

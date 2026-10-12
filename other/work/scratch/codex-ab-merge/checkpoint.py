from pathlib import Path
import subprocess,re,sys
root=Path(__file__).resolve().parents[4]
paths=set()
for p in (root/'out/merged').glob('Advanced Biotechnology *.md'):
    paths.add(p)
    for ref in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',p.read_text()):paths.add(p.parent/ref)
for name in ['merge.py','validate.py','render-check.mjs','merge-report.json','validation.json','render-validation.json']:
    q=Path(__file__).with_name(name)
    if q.exists():paths.add(q)
paths.add(root/'out/work/reviews/AB-U4a.md')
relative=sorted(str(p.relative_to(root)) for p in paths)
subprocess.run(['git','add','--',*relative],cwd=root,check=True)
subprocess.run(['git','diff','--cached','--check'],cwd=root,check=True)
subprocess.run(['git','commit','-m',sys.argv[1] if len(sys.argv)>1 else 'codex: merge Advanced Biotechnology units U1–U12'],cwd=root,check=True)

from pathlib import Path
import subprocess,re
root=Path(__file__).resolve().parents[4];paths=set()
for p in (root/'out/AB').glob('AB-*.md'):
    if int(p.name[3:5])<48:continue
    paths.add(p)
    for ref in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',p.read_text()):paths.add(p.parent/ref)
for p in (root/'out/merged').glob('Advanced Biotechnology *.md'):
    paths.add(p)
    for ref in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',p.read_text()):paths.add(p.parent/ref)
for folder in ['out/work/progress','out/work/reviews']:
    paths.update((root/folder).glob('codex*.md' if folder.endswith('progress') else 'AB-*.md'))
for folder in (root/'out/work/scratch').glob('codex*'):
    for p in folder.iterdir():
        if p.is_file() and p.suffix in ['.py','.mjs','.json','.txt'] and not p.name.startswith('visual-'):paths.add(p)
paths.update([root/'out/work/BOARD.md',root/'out/work/AB-COMPLETION.md',Path(__file__).with_name('.gitignore'),Path(__file__).with_name('AB-17-melt-curve.png')])
subprocess.run(['git','add','--',*[str(p.relative_to(root)) for p in sorted(paths)]],cwd=root,check=True)
subprocess.run(['git','diff','--cached','--check'],cwd=root,check=True)
subprocess.run(['git','commit','-m','codex: finish Advanced Biotechnology notes and verified course merges'],cwd=root,check=True)
print(subprocess.check_output(['git','log','-2','--oneline'],cwd=root,text=True))

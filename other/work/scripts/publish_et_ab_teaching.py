"""Use established ET/AB section splitter without overwriting other subjects' indexes.

The splitter writes both editions as UTF-8 with LF line endings.
"""
from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'other/work/scripts'))
source=(ROOT/'other/work/scripts/build_notes.py').read_text(encoding='utf-8')
namespace={'__file__':str(ROOT/'other/work/scripts/build_notes.py')}
exec(compile(source.split("root_index='# CEBT-II Notes",1)[0],str(ROOT/'other/work/scripts/build_notes.py'),'exec'),namespace)
manifest=namespace['manifest']
expected={Path(x['path']).resolve() for x in manifest['files']}|{Path(x['obsidian']).resolve() for x in manifest['files']}
renamed=[]
for parent in [ROOT/'notes',ROOT/'other/obsidian/CEBT-II Notes']:
 for subject in ['Equilibrium Thermodynamics','Advanced Biotechnology']:
  for p in (parent/subject).rglob('*.md'):
   if p.resolve() not in expected and 'Worked example' in p.name:
    assert p.name.startswith(('ET-09 ','ET-13 ','ET-16 ','ET-28 ','ET-30 ','ET-38 ','AB-40 ')),p
    renamed.append(p.relative_to(ROOT).as_posix())
    p.unlink()
manifest['removed_obsolete_names']=renamed
(ROOT/'other/work/LAYOUT-MANIFEST.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8', newline='\n')
(ROOT/'other/work/progress/et-ab-teaching-publication-20261022.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding='utf-8', newline='\n')
print(json.dumps({s['name']:{k:v for k,v in s.items() if k not in ['name','sections']} for s in manifest['subjects']},indent=2))

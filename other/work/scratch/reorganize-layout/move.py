from pathlib import Path
import hashlib,json,re,shutil,os
from urllib.parse import unquote,urlsplit

ROOT=Path.cwd();OLD_WORK=ROOT/'out/work';NEW_WORK=ROOT/'other/work'
assert not (ROOT/'other').exists(),'Layout migration has already started'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
preserved={}
for directory in ['sources','out/ET','out/AB','out/merged']:
    for p in (ROOT/directory).rglob('*'):
        if p.is_file() and p.name!='.DS_Store':preserved[str(p.relative_to(ROOT))]=digest(p)

# Preserve the corrected, reviewed native units as the new publisher's inputs.
for name in ['Equilibrium Thermodynamics','Advanced Biotechnology']:
    src=ROOT/'out/obsidian/CEBT-II Notes'/name
    dest=OLD_WORK/'archive/reviewed-units'/name
    dest.mkdir(parents=True)
    for p in src.glob('[0-9][0-9] - *.md'):shutil.copy2(p,dest/p.name)
    shutil.copytree(src/'figs',dest/'figs')

old_docs={str(p.relative_to(ROOT)):p.read_text() for p in OLD_WORK.rglob('*.md')}
old_docs.update({str(p.relative_to(ROOT)):p.read_text() for p in (ROOT/'notes').rglob('*.md')})
old_docs['out/README.md']=(ROOT/'out/README.md').read_text()
old_docs.update({str(p.relative_to(ROOT)):p.read_text() for p in (ROOT/'out/obsidian').rglob('*.md')})

mapping={}
directory_moves={
 'out/work':'other/work',
 'sources':'other/sources',
 'out/ET':'other/work/archive/original-small-notes/Equilibrium Thermodynamics',
 'out/AB':'other/work/archive/original-small-notes/Advanced Biotechnology',
 'out/merged':'other/work/archive/unit-snapshots',
 'notes':'other/work/archive/previous-reading-layout',
 'out/obsidian':'other/obsidian',
}
for old,new in directory_moves.items():
    for p in (ROOT/old).rglob('*'):
        mapping[str(p.relative_to(ROOT))]=str(Path(new)/p.relative_to(ROOT/old))
    mapping[old]=new
mapping['out/PLAN.md']='PLAN.md'
mapping['out/README.md']='other/work/archive/production-readme.md'
mapping['out']='other/work'

(ROOT/'other').mkdir()
shutil.move(ROOT/'out/work',NEW_WORK)
for old in ['sources','out/ET','out/AB','out/merged','notes','out/obsidian']:
    dest=ROOT/directory_moves[old];dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.move(ROOT/old,dest)
shutil.move(ROOT/'out/PLAN.md',ROOT/'PLAN.md')
shutil.move(ROOT/'out/README.md',NEW_WORK/'archive/production-readme.md')
for p in (ROOT/'out').iterdir():
    assert p.name=='.DS_Store',p
    p.unlink()
(ROOT/'out').rmdir()

# Retain the preceding portable edition as historical evidence; replace its layout.
old_export=ROOT/'other/obsidian/CEBT-II Notes'
shutil.move(old_export,NEW_WORK/'archive/previous-obsidian-edition')
for key,value in list(mapping.items()):
    if value.startswith('other/obsidian/CEBT-II Notes'):
        mapping[key]=value.replace('other/obsidian/CEBT-II Notes','other/work/archive/previous-obsidian-edition',1)

# Reader-facing links in review records should point to the current topic tree.
old_manifest=json.loads((NEW_WORK/'scratch/codex-github-navigation/manifest.json').read_text())
reader_targets={'notes/README.md':'notes/README.md'}
for sub in old_manifest['subjects']:
    name=sub['name'];old_folder='notes/'+sub['folder']
    reader_targets[old_folder]='notes/'+name
    reader_targets[old_folder+'/README.md']='notes/'+name+'/README.md'
    for unit in sub['units']:
        title=unit['title'];safe=re.sub(r'\s+',' ',re.sub(r'[<>:"/\\|?*]',' - ',title)).strip(' .')
        target=f'notes/{name}/{unit["number"]:02d} - {safe}/Complete section.md'
        for page in unit['pages']:reader_targets[page]=target
mapping.update(reader_targets)

def current_path(old):
    if old in mapping:return mapping[old]
    for directory,new in sorted(directory_moves.items(),key=lambda v:len(v[0]),reverse=True):
        if old.startswith(directory+'/'):return new+old[len(directory):]
    return old

# Preserve archived scientific note bytes; rebase documentation/navigation only.
protected=('other/work/archive/original-small-notes/','other/work/archive/unit-snapshots/','other/work/archive/reviewed-units/')
rebased=0
for old,text in old_docs.items():
    dest=ROOT/current_path(old)
    if not dest.exists() or str(dest.relative_to(ROOT)).startswith(protected):continue
    # Current reader targets override link destinations, not archive file locations.
    if old.startswith('notes/'):
        dest=NEW_WORK/'archive/previous-reading-layout'/Path(old).relative_to('notes')
    def link(m):
        target=m[1] or m[2]
        if urlsplit(target).scheme or target.startswith('#'):return m[0]
        raw,sep,anchor=target.partition('#')
        old_absolute=Path(os.path.normpath(str(ROOT/Path(old).parent/unquote(raw))))
        try:old_relative=str(old_absolute.relative_to(ROOT))
        except ValueError:return m[0]
        new_absolute=ROOT/current_path(old_relative)
        relative=os.path.relpath(new_absolute,dest.parent)
        if sep:relative+='#'+anchor
        return '(<'+relative+'>)' if ' ' in relative else '('+relative+')'
    changed=re.sub(r'\((?:<([^>]+)>|([^\s)]+))\)',link,text)
    # Only link destinations: require a preceding closing bracket, so prose parentheses
    # are never interpreted as filenames. Re-run with that restriction.
    changed=re.sub(r'(?<=\])\((?:<([^>]+)>|([^\s)]+))\)',link,text)
    if changed!=text:dest.write_text(changed);rebased+=1

checked=[]
for old,sha in preserved.items():
    new=current_path(old);p=ROOT/new
    assert digest(p)==sha,(old,new)
    checked.append({'old':old,'new':new,'sha256':sha})
(NEW_WORK/'scratch/reorganize-layout/file-moves.json').write_text(json.dumps(mapping,indent=2,ensure_ascii=False)+'\n')
(NEW_WORK/'scratch/reorganize-layout/preservation.json').write_text(json.dumps(checked,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'preserved_scientific_and_source_files':len(checked),'rebased_documentation_files':rebased,'root_out_removed':not (ROOT/'out').exists(),'root_sources_moved':not (ROOT/'sources').exists()},indent=2))

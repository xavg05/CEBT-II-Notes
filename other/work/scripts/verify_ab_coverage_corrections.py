"""Check authorized AB patches, full canonical preservation and both editions."""
from pathlib import Path
import ast, json, re

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT/'other/work/scratch/coverage-audit-20261014'
batch = json.loads((OUT/'ab-correction-batch.json').read_text(encoding='utf-8'))
assert batch['authorized_application'] is True
MATH = re.compile(r'(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$')
# Reuse only the established pure formatting functions; never run the publisher.
tree = ast.parse((ROOT/'other/work/scripts/build_notes.py').read_text(encoding='utf-8'))
namespace = {'re':re, 'MATH':MATH}
pure = ast.Module(body=[n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in ['compatible','github','demote_body']], type_ignores=[])
exec(compile(pure, '<publisher-formatters>', 'exec'), namespace)
github, demote = namespace['github'], namespace['demote_body']
for index, entry in enumerate(batch['replacements']):
    for name in entry['targets']:
        p = ROOT/name
        text = p.read_text(encoding='utf-8')
        gh = name.startswith('notes/')
        final_new = entry['new']
        for later in batch['replacements'][index+1:]:
            if name in later['targets']:
                final_new = final_new.replace(later['old'],later['new'])
        old, new = (github(entry['old']), github(final_new)) if gh else (entry['old'],final_new)
        assert old not in text, (p,entry['id'],'old claim remains')
        assert text.count(new)==1, (p,entry['id'],'replacement missing/duplicated')

def body(p):
    return p.read_text(encoding='utf-8').split('<!-- note-content:start -->\n',1)[1].split('\n<!-- note-content:end -->',1)[0].strip()
units = sorted({entry['targets'][0] for entry in batch['replacements']})
checked = 0
for name in units:
    canonical = (ROOT/name).read_text(encoding='utf-8')
    title = canonical.splitlines()[0][2:]
    source = re.sub(r'\]\(figs/','](../figs/',canonical.split('\n',1)[1].strip())
    example = next(entry for entry in batch['replacements'] if entry['targets'][0]==name)
    topic = (ROOT/example['targets'][1]).parent
    native_topic = ROOT/'other/obsidian/CEBT-II Notes'/topic.relative_to(ROOT/'notes')
    complete = '# '+title+'\n\n'+source
    assert body(native_topic/'Complete section.md')==complete.strip(), name
    assert body(topic/'Complete section.md')==github(complete).strip(), name
    checked += 2
    sections = list(re.finditer(r'^## Section (\d+): (.+)$',source,re.M))
    for i, match in enumerate(sections):
        n = int(match[1])
        section = source[match.end():sections[i+1].start() if i+1<len(sections) else len(source)].strip()
        expected = f'# Section {n:02d}: {match[2]}\n\n'+demote(section)
        native = next(native_topic.glob(f'AB-{n:02d} - *.md'))
        gh = topic/native.name
        assert body(native)==expected.strip(),native
        assert body(gh)==github(expected).strip(),gh
        checked += 2
result = {'exact_replacements_verified':len(batch['replacements']), 'canonical_units':len(units), 'reading_and_native_bodies_verified_against_canonical':checked, 'all_old_claims_removed':True}
(OUT/'ab-correction-validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))

from pathlib import Path
import json,re,runpy,subprocess
root=Path(__file__).resolve().parents[4];scratch=Path(__file__).parent
meta=runpy.run_path(str(scratch/'merge.py'));units=meta['UNITS']
shorts=sorted((root/'out/AB').glob('AB-*.md'));merged=sorted((root/'out/merged').glob('Advanced Biotechnology *.md'))
assert len(shorts)==57 and len(merged)==17,(len(shorts),len(merged))
checks=json.loads((scratch/'render-validation.json').read_text());assert checks['files']==27 and not checks['failures'],checks
static=json.loads((scratch/'validation.json').read_text());assert len(static)==17
reviews=['AB-U13-L13.md','AB-U13-L14.md','AB-U14.md','AB-U15.md']
for name in reviews:
    p=root/'out/work/reviews'/name;assert p.exists(),p
    assert re.search(r'\bPASS\b|no material findings',p.read_text(),re.I),p
board=['| unit | owner | status | notes |','|---|---|---|---|']
for unit,start,end,title in units:
    owner='codex' if start>=48 else 'claude';status='reviewed' if start>=48 else 'written'
    note='pre-existing short notes; Codex merged'
    if unit=='AB-U13':note='external-source supplemented; thin source material flagged; independent cross-reviews passed'
    elif unit=='AB-U14':note='independent Codex cross-review passed'
    elif unit=='AB-U15':note='optional unit; independent Codex cross-review passed'
    elif unit in ['AB-U4a','AB-U8','AB-U9','AB-U10','AB-U11','AB-U12']:note='original findings in reviews; corrected new merges; original shorts retained'
    board.append(f'| {unit} (AB-{start:02d}–{end:02d}) | {owner} | {status} | {note} |')
board.extend(['| AB merge U1–U12 | codex | reviewed | files 01–14; KaTeX, references, figures and numerical checks |','| AB merge U13–U15 | codex | reviewed | files 15–17; includes optional condensates |'])
(root/'out/work/BOARD.md').write_text('\n'.join(board)+'\n')
lines=['# Advanced Biotechnology completion record — 9 October 2026','', 'Completed the takeover after Claude’s usage limit: ten new short notes (AB-48–57) and seventeen merged units covering AB-01–57. AB-U13 retains the agreed flag: thin course material supplemented by outside primary sources. The optional condensates unit is included.','', '## Merged deliverables','', 'Copy the seventeen Markdown files together with the adjacent `figs/` folder when uploading to Obsidian.','', '| File | Short notes | Scope |','|---|---|---|']
for i,(unit,start,end,title) in enumerate(units,1):
    p=merged[i-1]
    lines.append(f'| [{i:02d}: {title}](<../merged/{p.name}>) | AB-{start:02d}–{end:02d} | {unit} |')
lines.extend(['','## New short notes',''])
for p in shorts:
    if int(p.name[3:5])>=48:lines.append(f'- [{p.read_text().splitlines()[0][2:]}](<../AB/{p.name}>) — standalone short note with adjacent cropped figures.')
lines.extend(['','## Verification','',f'- {checks["files"]} deliverable Markdown files rendered through Markdown and KaTeX, with {checks["mathExpressions"]} mathematical expressions and no parse errors.',f'- All {len(static)} merges have a single H1, one H2 per short subtopic, local continuous equation numbering, and resolving, decodable figures. Every merged figure was visually inspected; new crops were also opened individually by their writers and reviewers.','- All new numerical examples were computed in Python and independently cross-reviewed; existing worked examples in AB-34, 36, 37, 40, 42, 43, 45 and 47 were rerun. Derivations, dimensions, limiting cases and notation checked.','- New notes use the seven required sections and contain no source-document narration, wikilinks or callouts. Merged overviews and conclusions were unified; derivations and worked examples preserved except for documented corrections.','- Obsidian itself was not opened. A supplementary headless Chrome PDF-preview attempt timed out; successful Markdown/KaTeX parsing and figure inspection are the rendering evidence.','', '## Corrections and qualifications','', '- Gene-expression protein production is proportional to message abundance: the missing mRNA factor is restored. Intrinsic degradation is distinguished from growth dilution, including exact versus rounded half-life calculations.','- LacA is an acetyltransferase, not an activator of LacZ. Lac logic and the evolutionary demand rule are conditional rather than absolute.','- The condensate RNA lifetime estimate is conditional on polymerase occupancy and steady state: 20 minutes is the mean lifetime; the half-life is about 13.9 minutes. Network formation, liquid condensation and gels are distinguished.','- Cell-free and IVT claims are qualified: cleanup, oxygen dependence, capping alternatives and selective enzyme recycling depend on the chosen process. Minimal-genome counts retain their historical context; synthetic-cell architecture is not evidence of autonomous life.','- Replaced the wrong melt-curve figure in the merged qPCR unit. The pre-existing AB-17 figure was an amplification/calibration plot.','- Additional corrections to the downstream-processing merges are recorded in the unit reviews and exact merge-fixes manifest. Existing Claude-owned AB-01–47 and their original figures were not modified.','', '## Sources','', 'The following logs list every external source actually opened/read, with links, page coverage, abstract-only limits and failed retrievals. Search snippets were not treated as sources. Some publisher/PMC pages were inaccessible; author manuscripts or institutional accounts were used where available.',''])
source_seen=set()
for p in sorted((root/'out/work/progress').glob('codex*.md')):
    lines.append(f'- [{p.name}](<progress/{p.name}>)')
lines.extend(['', 'Sources actually consulted:', ''])
for p in sorted((root/'out/work/progress').glob('codex*.md')):
    text=p.read_text()
    match=re.search(r'## External (?:primary )?sources actually opened(?: and|/) ?(?:read)?(.*?)(?=\n## |\Z)',text,re.S|re.I)
    if not match:continue
    for raw in match[1].splitlines():
        if not raw.startswith('- '):continue
        urls=re.findall(r'https?://[^\s]+',raw)
        if not urls:continue
        url=urls[0].rstrip('.,;')
        if url in source_seen:continue
        source_seen.add(url)
        title=raw[2:].split('https',1)[0].strip(' :—–-,')
        if not title and ' — ' in raw:
            title=raw.split(' — ',1)[1].split('. Read',1)[0].split(';',1)[0]
            if len(title)>200:title=title[:197]+'…'
        title=title or 'Research paper'
        if title.startswith('http'):title='Research paper'
        lines.append(f'- [{title}]({url})')
lines.extend(['', 'Additional primary sources and retrieval limits for the downstream-processing corrections are listed in the [AB-U8](reviews/AB-U8.md), [AB-U9](reviews/AB-U9.md), [AB-U10](reviews/AB-U10.md), [AB-U11](reviews/AB-U11.md) and [AB-U12](reviews/AB-U12.md) reviews. Exact corrections are recorded in [the integration review](reviews/AB-MERGE-INTEGRATION.md).'])
lines.extend(['','## Cross-review records',''])
for p in sorted((root/'out/work/reviews').glob('AB-*.md')):lines.append(f'- [{p.stem}](<reviews/{p.name}>)')
lines.extend(['','## Workspace and next step','', '`out/PLAN.md`, `CLAUDE.md`, source PDFs, existing short notes and the Obsidian vault were left unchanged. BOARD.md records the takeover and completed statuses. Commits are local; nothing was pushed or published.','', 'Next step: upload the merged notes and their `figs/` folder to Obsidian. Original-short-note findings remain in the reviews for their owner.'])
(root/'out/work/AB-COMPLETION.md').write_text('\n'.join(lines)+'\n')
print('Completion record and ownership board saved.')

from pathlib import Path
p=Path(__file__).with_name('finalize.py');s=p.read_text()
s=s.replace("re.search(r'\\bPASS\\b',p.read_text(),re.I)","re.search(r'\\bPASS\\b|no material findings',p.read_text(),re.I)")
s=s.replace("for p in sorted((root/'out/work/progress').glob('codex*.md')):lines.append(f'- [{p.name}](<progress/{p.name}>)')", """source_seen=set()
for p in sorted((root/'out/work/progress').glob('codex*.md')):
    lines.append(f'- [{p.name}](<progress/{p.name}>)')
lines.extend(['', 'Sources actually consulted:', ''])
for p in sorted((root/'out/work/progress').glob('codex*.md')):
    text=p.read_text()
    match=re.search(r'## External (?:primary )?sources actually opened(?: and|/) ?(?:read)?(.*?)(?=\\n## |\\Z)',text,re.S|re.I)
    if not match:continue
    for raw in match[1].splitlines():
        if not raw.startswith('- '):continue
        urls=re.findall(r'https?://[^\\s]+',raw)
        if not urls:continue
        url=urls[0].rstrip('.,;')
        if url in source_seen:continue
        source_seen.add(url)
        title=raw[2:].split('https',1)[0].strip(' :—–-') or 'Research paper'
        if title.startswith('http'):title='Research paper'
        lines.append(f'- [{title}]({url})')""")
p.write_text(s)
# Keep bulky caches and rendered previews out of version control without changing root configuration.
Path(__file__).with_name('.gitignore').write_text('render/\nnpm-cache/\nchrome-profile/\n*.html\nvisual-*\nfigures-*\nmelt-page17.png\n')
print('Prepared final source index and review-verdict handling.')

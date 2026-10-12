import re, os, shutil, glob
ROOT = '/Users/xaviergoraieb/Projects/CEBT-II-notes/out'
AB = f'{ROOT}/AB'; MER = f'{ROOT}/merged'
os.makedirs(f'{MER}/figs', exist_ok=True)

def load(n):
    return open(glob.glob(f'{AB}/AB-{n:02d}-*.md')[0]).read()

def split(text):
    lines = text.split('\n')
    h1 = lines[0][2:].strip()
    secs, cur = [], None
    for ln in lines[1:]:
        if ln.startswith('## '):
            cur = [ln[3:].strip(), []]; secs.append(cur)
        elif cur is not None:
            cur[1].append(ln)
    return h1, [(t, '\n'.join(b).strip('\n')) for t, b in secs]

def renum(body, off):
    if off == 0: return body
    body = re.sub(r'\\tag\{(\d+)\}', lambda m: f'\\tag{{{int(m.group(1))+off}}}', body)
    # in-text references "(n)" outside $...$ math: replace only bare (n) tokens
    out = []
    for i, seg in enumerate(re.split(r'(\$\$.*?\$\$|\$[^$]*\$)', body, flags=re.S)):
        if i % 2 == 0:
            seg = re.sub(r'\((\d{1,2})\)', lambda m: f'({int(m.group(1))+off})', seg)
        out.append(seg)
    return ''.join(out)

def build(fname, title, overview, units, conclusion, edits={}):
    parts = [f'# {title}', '', '## Overview', '', overview.strip(), '']
    off = 0; figs = set()
    for n, summary in units:
        h1, secs = split(load(n))
        parts += [f'## {h1}', '']
        ntags = 0
        for t, b in secs:
            if t == 'Overview': continue
            ntags += len(re.findall(r'\\tag\{', b))
            if t == 'Conclusion':
                parts += ['### Summary', '', summary.strip(), '']; continue
            b = re.sub(r'^### ', '#### ', b, flags=re.M)
            b = renum(b, off)
            for a, c in edits.get(n, []):
                assert a in b or a not in load(n), a
                b = b.replace(a, c)
            parts += [f'### {t}', '', b, '']
        off += ntags
    parts += ['## Conclusion', '', conclusion.strip(), '']
    txt = '\n'.join(parts)
    for e in [x for v in edits.values() for x in v]:
        assert e[1] in txt, ('edit not applied', e[0])
    path = f'{MER}/{fname}'
    open(path, 'w').write(txt)
    for f in re.findall(r'\]\((figs/[^)]+)\)', txt):
        shutil.copy2(f'{AB}/{f}', f'{MER}/{f}')
    print(fname, txt.count('\n'), 'lines,', len(set(re.findall(r'\]\((figs/[^)]+)\)', txt))), 'figs')

exec(open(os.path.join(os.path.dirname(__file__), 'units.py')).read())

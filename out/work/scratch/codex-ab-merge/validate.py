from pathlib import Path
import re,json,subprocess,pymupdf
ROOT=Path(__file__).resolve().parents[4];OUT=ROOT/'out/merged';SCR=Path(__file__).parent
results=[];figures=set()
for p in sorted(OUT.glob('Advanced Biotechnology *.md')):
    s=p.read_text(); tags=[int(x) for x in re.findall(r'\\tag\{(\d+)\}',s)]
    assert tags==list(range(1,len(tags)+1)),(p,tags)
    assert len(re.findall(r'^# ',s,re.M))==1,p
    assert not re.search(r'\[\[|^>\s*\[!|@@CROSSREF',s,re.M),p
    # No source-document narration or former filenames in prose (figure paths excluded).
    prose=re.sub(r'!\[[^\]]*\]\([^)]+\)','',s)
    bad=re.findall(r'\b(?:lecture PDF|lecture slides|lecturer|AB-\d{2}(?:-[a-z]+)+\.md)\b',prose,re.I)
    assert not bad,(p,bad)
    # All images are decodable, non-empty, and resolve relative to the deliverable.
    refs=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',s)
    for ref in refs:
        q=p.parent/ref;assert q.is_file(),q
        pix=pymupdf.Pixmap(str(q));assert pix.width>0 and pix.height>0,q
        figures.add(q)
    # Dollar delimiters and braces within mathematical spans must be balanced.
    assert len(re.findall(r'(?<!\\)\$',s))%2==0,p
    maths=re.findall(r'\$\$.*?\$\$|\$(?:\\.|[^$])*\$',s,re.S)
    for m in maths:
        stack=0
        for ch in re.sub(r'\\[{}]','',m):
            if ch=='{':stack+=1
            if ch=='}':stack-=1
            assert stack>=0,(p,m)
        assert stack==0,(p,m)
    results.append({'file':p.name,'equations':len(tags),'figures':len(refs),'math_spans':len(maths)})
for i in range(0,len(figures),9):
    batch=sorted(figures)[i:i+9]
    subprocess.run(['montage','-font','/Library/Fonts/Arial Unicode.ttf',*[str(q) for q in batch],'-set','label','%f','-label','%f','-geometry','480x300+8+8','-tile','3x3',str(SCR/f'figures-{i//9+1:02d}.jpg')],check=True)
(SCR/'validation.json').write_text(json.dumps(results,indent=2))
print(f'Validated {len(results)} merged files; {len(figures)} unique images; contact sheets {(len(figures)+8)//9}.')

from pathlib import Path
import hashlib,json,re
from urllib.parse import unquote,urlsplit
import pymupdf

ROOT=Path(__file__).resolve().parents[4];WORK=Path(__file__).parent
manifest=json.loads((WORK/'manifest.json').read_text())
STANDARD=re.compile(r'(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$')
GITHUB=re.compile(r'^```math\n([\s\S]*?)\n```|(?<!\\)\$`([^`]*?)`\$',re.M)
def expressions(s,pattern):return [(m.group(1) if m.group(1) is not None else m.group(2)).strip() for m in pattern.finditer(s)]
def body(s):return s.split('<!-- reading-content:start -->\n',1)[1].split('\n<!-- reading-content:end -->',1)[0]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def prose(s):
    s=STANDARD.sub('MATHEXPRESSION',s)
    s=re.sub(r'^#{1,6}\s*','',s,flags=re.M)
    return re.sub(r'\s+',' ',s.replace('*','').replace('_','')).strip()
def standardise(s):
    return GITHUB.sub(lambda m:'$$'+m.group(1)+'$$' if m.group(1) is not None else '$'+m.group(2)+'$',s)

checked_links=0
for p in [ROOT/'README.md',ROOT/'out/README.md',ROOT/'out/work/AB-COMPLETION.md',*sorted((ROOT/'notes').rglob('*.md'))]:
    s=p.read_text()
    for match in re.finditer(r'!?\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))\)',s):
        target=match.group(1) or match.group(2)
        if urlsplit(target).scheme or target.startswith('#'):continue
        dest=p.parent/unquote(target.split('#',1)[0]);assert dest.exists(),(p,target)
        checked_links+=1
for p,expected in manifest['originals'].items():assert sha(ROOT/p)==expected,p
for p,expected in manifest['figures'].items():
    assert sha(ROOT/p)==expected,p
    pix=pymupdf.Pixmap(str(ROOT/p));assert pix.width>0 and pix.height>0,p

results=[]
for subject in manifest['subjects']:
    complete=(ROOT/'notes'/subject['folder']/'complete-obsidian.md').read_text()
    all_reading=[];tags=[]
    for page in subject['pages']:
        s=(ROOT/page['path']).read_text();content=body(s)
        ex=expressions(content,GITHUB)
        assert len(ex)==page['expressions'],page['path']
        value=sum(x.count('{')+1 for x in ex)
        assert value==page['cost'] and value<=600,(page['path'],value)
        assert '<!-- reading-content:' not in content
        all_reading.extend(ex)
        page_tags=[int(n) for n in re.findall(r'\\tag\{(\d+)\}',content)]
        assert page_tags==page['tags'];tags.extend(page_tags)
        # This also catches unprotected inline/display delimiters outside currency.
        plain=GITHUB.sub('',content)
        assert not re.search(r'(?<!\\)\$',plain),(page['path'],'Unprotected math')
    assert all_reading==expressions(complete,STANDARD),subject['name']
    assert tags==list(range(1,subject['equations']+1)),subject['name']
    # Independently reverse the new course numbering and compare all prose.
    offset=0;section_units={}
    for unit in subject['units']:
        original=(ROOT/unit['source']).read_text()
        for sec in re.findall(r'^## Section (\d+):',original,re.M):section_units[int(sec)]=(offset,len(re.findall(r'\\tag\{(\d+)\}',original)))
        offset+=len(re.findall(r'\\tag\{(\d+)\}',original))
    offset=0
    for unit in subject['units']:
        original=(ROOT/unit['source']).read_text().split('\n',1)[1].strip()
        reconstructed='\n\n'.join(standardise(body((ROOT/p).read_text())) for p in unit['pages'])
        n_tags=len(re.findall(r'\\tag\{(\d+)\}',original));saved={}
        def reverse_cross(m):
            sec=int(m.group('sec'));n=int(m.group('eq'));shift,count=section_units[sec]
            assert shift<n<=shift+count,(unit['source'],sec,n)
            key=f'PRESERVECROSS{len(saved)}END';saved[key]=m.group('lead')+str(n-shift)+m.group('end');return key
        for pattern in [r'(?P<lead>Section (?P<sec>\d+),? (?:equation|eq\.) ?\(?)(?P<eq>\d+)(?P<end>\)?)',r'(?P<lead>(?:[Ee]quation )?\()(?P<eq>\d+)(?P<end>\) of Section (?P<sec>\d+))']:
            reconstructed=re.sub(pattern,reverse_cross,reconstructed)
        segments=[];cursor=0
        def reverse_prose(s):return re.sub(r'\((\d+)\)',lambda m:'('+str(int(m[1])-offset)+')' if offset<int(m[1])<=offset+n_tags else m[0],s)
        for m in STANDARD.finditer(reconstructed):
            segments.append(reverse_prose(reconstructed[cursor:m.start()]))
            segments.append(re.sub(r'\\tag\{(\d+)\}',lambda m:r'\tag{'+str(int(m[1])-offset)+'}',m[0]));cursor=m.end()
        segments.append(reverse_prose(reconstructed[cursor:]));restored=''.join(segments)
        for key,value in saved.items():restored=restored.replace(key,value)
        assert expressions(restored,STANDARD)==expressions(original,STANDARD),('Formula preservation',unit['source'])
        assert prose(restored)==prose(original),('Prose preservation',unit['source'])
        offset+=n_tags
    results.append({'subject':subject['name'],'pages':len(subject['pages']),'expressions':len(all_reading),'equations':len(tags),'max_cost':max(p['cost'] for p in subject['pages'])})
result={'subjects':results,'links':checked_links,'preserved_original_files':len(manifest['originals']),'identical_decoded_figures':len(manifest['figures']),'formula_prose_and_numbering_preservation':True}
(WORK/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

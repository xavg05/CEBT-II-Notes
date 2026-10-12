from pathlib import Path
import re, shutil, json
ROOT=Path(__file__).resolve().parents[4]
AB=ROOT/'out/AB'; OUT=ROOT/'out/merged'
INTRO=['Nucleic-acid chemistry determines the structures that DNA and RNA can form. Polymer bending, two-state hybridisation and nearest-neighbour thermodynamics explain their geometry and stability; association and dissociation kinetics explain how quickly those structures assemble and rearrange.', 'Chemical synthesis builds short oligonucleotides one nucleotide at a time, so modest losses at each coupling accumulate into a strong length limit. Overlapping fragments can then be assembled into genes and whole genomes, separating chemical manufacture from biological replication.', 'Sanger sequencing reads chain-terminated fragments, while Illumina reads large numbers of immobilised templates in parallel. Library preparation, cluster generation and reversible-terminator chemistry connect an original sample to short reads that must be assembled or mapped.', 'Nanopore and PacBio sequencing read individual molecules through different physical signals. Their long reads complement short-read methods by spanning repeats, resolving variants and supporting applications that depend on molecular context.', 'Quantitative PCR estimates the starting abundance of a target from the cycle at which exponential amplification reaches a fluorescence threshold. Calibration, reference genes and sequence-specific detection make that estimate usable while exposing the assumptions behind absolute and relative quantification.', 'Aptamers use folded nucleic acids to recognise molecular targets. SELEX couples binding selection to amplification so that rare useful sequences become enriched, with specificity determined by the selection conditions and counter-selection.', 'Sequence-dependent hybridisation makes DNA a programmable connector. Structural assemblies use that selectivity to organise objects, while toehold-mediated strand displacement provides controlled reactions that rearrange structures or process molecular signals.', 'Protein folding connects amino-acid sequence to molecular function. X-ray crystallography, cryo-electron microscopy and NMR infer structure from experimental signals; computational methods predict it from learned constraints, with different limitations and validation needs.', 'Protein engineering changes function, stability or behaviour in the body by altering sequence, architecture and chemical modifications. Mutagenesis and non-canonical amino acids supply the changes, while antibody-generation and screening methods identify useful variants.', 'A bioprocess must deliver a useful product at scale, with upstream production and downstream recovery designed together. The recovery train first separates cells from liquid; filtration illustrates how equipment choice, cake growth and compressibility determine throughput and area.', 'Centrifuges accelerate density-driven settling and arrange the available separation area in compact geometries. Stokes settling and residence-time arguments give a cut-off throughput, while sigma theory separates feed properties from equipment performance for conditional scale-up.', 'Intracellular products require disruption before purification, but breaking cells also releases debris, nucleic acids and degradative enzymes. Mechanical and non-mechanical methods balance release against product damage; release kinetics and a homogeniser fit make that trade quantitative.', 'Primary isolation separates a product from the clarified broth using partitioning, precipitation or adsorption. Equilibrium relations and material balances connect the molecular mechanism to recovery, product concentration and the cost of pursuing very high yield.', 'Chromatography separates components through differences in binding or accessible pore volume. Retention measures describe differential migration, while final isolation converts a purified stream into the physical form needed for storage and use.', 'Gene expression couples transcription and translation to degradation and dilution. Regulatory proteins change synthesis rates; feedback motifs shape steady states and response times, stochastic events generate noise, and delayed cyclic repression can produce oscillations.', 'Cell-free systems move transcription and translation into an engineered reaction mixture. In-vitro transcription enables mRNA production, while genome minimisation and bottom-up compartment construction explore complementary routes to simpler cellular systems.', 'Programmable DNA and RNA interactions can organise molecules into condensates. Molecular valency, binding strength and fuel-dependent reactions connect sequence-level design to phase behaviour and dynamic organisation.']
PREREQUISITES=['ideal dilute-solution thermodynamics and mass-action kinetics', 'covalent bonding, nucleotide structure and PCR', 'nucleotide polymerisation, PCR and sequence complementarity', 'nucleotide polymerisation and the short-read sequencing principles', 'PCR, logarithms and gene expression', 'nucleic-acid folding, binding equilibria and PCR', 'hybridisation thermodynamics and nucleic-acid polymer physics', 'amino-acid chemistry, thermodynamics and molecular recognition', 'protein structure, genetic coding and molecular recognition', 'material balances, transport and basic microbial cultivation', 'force balances, low-Reynolds-number drag and residence time', 'cell structure, material balances and first-order kinetics', 'phase equilibria, protein structure and material balances', 'phase partitioning, adsorption and downstream-process stages', 'mass-action kinetics, first-order balances and DNA-to-RNA-to-protein information flow', 'gene expression, enzyme catalysis and membrane structure', 'hybridisation, phase separation and toehold-mediated strand displacement']
FINAL=['Hybridisation thermodynamics selects stable pairings, and kinetics determines whether those pairings rearrange on the available timescale.', 'The per-step yield limits direct synthesis length; assembly and replication extend that chemistry to larger DNA constructs.', 'Parallel readout increases throughput, while amplification and assembly introduce distinct sources of bias and uncertainty.', 'Long reads preserve molecular context, and the appropriate platform depends on the biological question and error tolerance.', 'Threshold cycles become abundance estimates only when amplification efficiency, signal specificity and normalisation are controlled.', 'Selection conditions determine which binding properties are enriched, so amplification alone is never evidence of useful specificity.', 'DNA nanotechnology combines addressable structure with programmable reaction kinetics.', 'Experimental determination and computational prediction answer related structural questions, and each requires validation against its own limitations.', 'Sequence changes and screening connect molecular recognition to useful biological performance.', 'Cell removal links broth properties to equipment duty, and cake compressibility makes added filtration area more reliable than added pressure.', 'Sigma theory supports scale-up when feed properties, separation criteria and geometric conventions remain consistent.', 'Disruption recovery must be assessed alongside the damage and contaminants introduced by the release operation.', 'Partitioning, solubility and binding equilibria set recovery, while material balances expose the concentration and capacity trade-offs.', 'Retention describes migration, peak widths determine resolution, and final isolation sets the product form.', 'Feedback controls average behaviour, while fluctuations and delays determine how reliably a circuit achieves it.', 'Removing cellular complexity makes individual functions easier to control, but rebuilding autonomy requires their integration.', 'Condensate design connects molecular interactions to collective organisation and its control in time.']
UNITS=[('AB-U1',1,5,'Nucleic acids - structure, thermodynamics and kinetics'),('AB-U2',6,9,'DNA synthesis and gene assembly'),('AB-U3a',10,12,'Sequencing I - Sanger and short reads'),('AB-U3b',13,15,'Sequencing II - long reads and applications'),('AB-U4a',16,18,'Quantitative PCR'),('AB-U4b',19,19,'Aptamers and SELEX'),('AB-U5',20,22,'DNA nanotechnology'),('AB-U6',23,26,'Protein structure - determination and prediction'),('AB-U7',27,30,'Protein engineering'),('AB-U8',31,34,'Bioprocessing overview and filtration'),('AB-U9',35,37,'Centrifugation'),('AB-U10',38,41,'Cell disruption'),('AB-U11',42,45,'Primary isolation'),('AB-U12',46,47,'Chromatography and final isolation'),('AB-U13',48,52,'Gene regulation and synthetic circuits'),('AB-U14',53,56,'Cell-free systems and synthetic cells'),('AB-U15',57,57,'Synthetic biomolecular condensates')]
def load(n):
    paths=list(AB.glob(f'AB-{n:02d}-*.md'))
    if len(paths)!=1: raise FileNotFoundError(f'AB-{n:02d}: {len(paths)} files')
    return paths[0].read_text()
def split(s):
    chunks=re.split(r'^## (.+)\n',s,flags=re.M)
    return chunks[0].splitlines()[0][2:].strip(),dict(zip(chunks[1::2],chunks[2::2]))
def prose(s):
    return re.split(r'(\$\$.*?\$\$|\$(?:\\.|[^$])*\$)',s,flags=re.S)
def renumber(s,n,maps):
    saved={}
    def protect(value):
        key=f'@@CROSSREF{len(saved)}@@';saved[key]=value;return key
    def cross(m):
        sec=int(m.group('sec')); eq=int(m.group('eq'))
        if sec not in maps: return protect(m.group(0))
        return protect(m.group(0).replace(m.group('eq'),str(maps[sec][eq]),1 if m.group('eq')!=m.group('sec') else 0))
    # Explicit references to other short notes must use their map, never the current map.
    patterns=[r'(?P<lead>Section (?P<sec>\d+),? (?:equation|eq\.) ?\(?)(?P<eq>\d+)(?P<end>\)?)',r'(?P<lead>(?:[Ee]quation )?\()(?P<eq>\d+)(?P<end>\) of Section (?P<sec>\d+))']
    for pat in patterns:
        def repl(m):
            sec=int(m.group('sec'));eq=int(m.group('eq'))
            target=maps.get(sec,{}).get(eq)
            return protect(m.group('lead')+str(target)+m.group('end')) if target else protect(m.group(0))
        s=re.sub(pat,repl,s)
    # AB-40 uses equation 4 of the preceding note, without naming it each time.
    if n==40:
        s=s.replace('equation (4)',protect(f'equation ({maps[39][4]})')).replace('from (4)',protect(f'from ({maps[39][4]})'))
    segments=prose(s)
    for i,seg in enumerate(segments):
        if i%2:
            seg=re.sub(r'\\tag\{(\d+)\}',lambda m:r'\tag{'+str(maps[n][int(m[1])])+'}',seg)
        else:
            seg=re.sub(r'\((\d+)\)',lambda m:'('+str(maps[n][int(m[1])])+')' if int(m[1]) in maps[n] else m[0],seg)
        segments[i]=seg
    s=''.join(segments)
    for key,value in saved.items():s=s.replace(key,value)
    return s

def build(index,unit,start,end,title):
    try: docs={n:load(n) for n in range(start,end+1)}
    except FileNotFoundError:return None
    maps={};counter=0
    for n,s in docs.items():
        tags=[int(x) for x in re.findall(r'\\tag\{(\d+)\}',s)]
        assert tags==list(range(1,len(tags)+1)),(n,tags)
        maps[n]={old:counter+i+1 for i,old in enumerate(tags)};counter+=len(tags)
    # Optional exact scientific fixes are recorded separately, and applied only to new merged files.
    fixesfile=Path(__file__).with_name('fixes.json')
    fixes=json.loads(fixesfile.read_text()) if fixesfile.exists() else {}
    for n in docs:
        for old,new in fixes.get(str(n),[]):
            assert old in docs[n],(n,old)
            docs[n]=docs[n].replace(old,new)
    overviews=[];assumptions=[];parts=[]
    for n,s in docs.items():
        h,secs=split(s)
        overview=secs.get('Overview','').strip()
        overview=re.sub(r'^\*Assumed[^\n]*\n?',lambda m:(assumptions.append(m[0].strip()) or ''),overview,flags=re.M)
        overviews.append(renumber(overview,n,maps).strip())
        body=[]
        for name,text in secs.items():
            if name=='Overview':continue
            text=renumber(text.strip(),n,maps)
            text=re.sub(r'^(#{3,5}) ',lambda m:'#'+m[1]+' ',text,flags=re.M)
            if name=='Conclusion':
                name='Summary'
                # Keep the first two substantive sentences as a short subtopic conclusion.
                sentences=re.split(r'(?<=[.!?])\s+(?=[A-Z$])',text)
                text=' '.join(sentences[:2])
            body.extend(['### '+name,'',text,''])
        parts.extend(['## '+h,'','\n'.join(body)])
    overview=INTRO[index-1]
    # A single prerequisites line retains the prerequisites without repeating each note's opening.
    prerequisites=PREREQUISITES[index-1]
    if prerequisites:overview+='\n\n*Assumed throughout:* '+prerequisites+'.'
    nexttopic=UNITS[index][3] if index<len(UNITS) else None
    closing=FINAL[index-1]+' '
    if nexttopic:closing+='The next unit develops '+nexttopic.lower()+'.'
    else:closing='Programmable nucleic-acid interactions connect molecular structure to collective organisation. This completes Advanced Biotechnology, including the optional condensates topic.'
    s='\n'.join(['# '+title,'','## Overview','',overview,'']+parts+['## Conclusion','',closing,''])
    s=re.sub(r'\bAB-\d{2}\b',lambda m:'Section '+m[0][-2:],s) if False else s
    out=OUT/f'Advanced Biotechnology {index:02d} - {title}.md'
    OUT.mkdir(exist_ok=True);(OUT/'figs').mkdir(exist_ok=True)
    out.write_text(s)
    for path in re.findall(r'!\[[^\]]*\]\((figs/[^)]+)\)',s):
        shutil.copy2(Path(__file__).with_name('AB-17-melt-curve.png') if path=='figs/AB-17-melt-curve.png' else AB/path,OUT/path)
    return {'unit':unit,'file':str(out.relative_to(ROOT)),'equations':counter,'figures':len(re.findall(r'!\[',s))}
if __name__=='__main__':
    report=[x for i,u in enumerate(UNITS,1) if (x:=build(i,*u))]
    Path(__file__).with_name('merge-report.json').write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))

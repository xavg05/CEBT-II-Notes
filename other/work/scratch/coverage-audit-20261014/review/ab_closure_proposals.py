"""Proposals only for adjacent inconsistencies discovered during closure review."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[5]
base=root/'other/work/archive/reviewed-units/Advanced Biotechnology'
items=[]
def add(unit,note,anchor,new,reason,source):
    canonical=next(base.glob(f'{unit:02} - *.md'))
    text=canonical.read_text(encoding='utf-8')
    old=next(p for p in text.split('\n\n') if p.startswith(anchor))
    assert text.count(old)==1
    published=next((root/'notes/Advanced Biotechnology').glob(f'*/AB-{note:02} - *.md'))
    items.append(dict(id=f'AB-{note:02}-closure-{len(items)+1}',canonical=canonical.relative_to(root).as_posix(),published=published.relative_to(root).as_posix(),old=old,new=new,reason=reason,source=source))
add(2,8,'**3. Convert the hybrid',
    '**3. Convert the hybrid into continuous double-stranded DNA.** A polymerase extends base-paired 3′ ends to fill in single-stranded regions. In fragment-joining methods such as Gibson assembly, a ligase seals the remaining nicks where strands abut. PCA builds products by polymerase extension and does not require ligase.',
    'Shared step currently implies ligase is required in both methods; qualify to agree with the new named PCA/Gibson passage.', 'Lecture 2 pp20–26; PCA/Gibson original mechanisms visually checked')
add(4,13,'**Why homopolymers are the characteristic failure.**',
    '**Why homopolymers are the characteristic failure.** A run such as CCCCC gives the *same* k-mer, and so the same current level, for several successive steps. The level does not change, so the only evidence of how many C\'s passed is how *long* the level persisted. Translocation is stochastic, so dwell time is a noisy measure of step count, and the base caller must infer "five C\'s" from a duration. This can produce insertions and deletions in homopolymer runs. Errors can be biased by sequence context and correlated between reads, without every read necessarily making the same mistake.',
    'Remove deterministic every-read error claim that contradicts revised AB14 and AB13 own worked-model caveat.', 'Lecture 4 p12; AB13 worked example and revised AB14 statistical distinction')
add(4,13,'**Why that systematic character matters more than the raw error rate.**',
    '**Why error correlations matter as well as the raw error rate.** For the illustrative raw accuracies used here, nanopore reads are around 95–99 % accurate, against about 99.9 % for Illumina. Independent random errors can be reduced by combining reads. Sequence-context-dependent errors can remain correlated, so the improvement need not follow an independent binomial model. The worked example contrasts that idealised model with its practical limitations.',
    'Adjacent paragraph still says all reads make identical error and misdescribes what numerical example quantifies.', 'Lecture 4 p12; current AB13 independent binomial example')
add(4,13,'Threading a single native strand',
    'Threading a single native strand through a protein pore and recording the ionic current gives sequence without amplification, optics or copying, in a hand-held device, with reads limited by DNA integrity and sustained measurement. Sequence-context effects, particularly at homopolymers, can limit consensus improvement because the signal reflects several bases at once. Coverage reduces independent errors; correlated errors do not follow the same statistical gain.',
    'Summary retains categorical no-improvement claim removed elsewhere.', 'Lecture 4 p12; current AB13 and revised AB14 consensus qualifications')
add(8,26,'**Why confidence scores matter.**',
    next(p for p in next(base.glob('08 - *.md')).read_text(encoding='utf-8').split('\n\n') if p.startswith('**Why confidence scores matter.**')).replace(' Low confidence can', ' For multichain predictions, **ipTM** (interface predicted TM-score) assesses confidence in the relative placement of interacting chains on a 0–1 scale, with larger values indicating greater confidence; it complements the overall pTM score. Low confidence can'),
    'Source figure explicitly labels ipTM beside pTM; one sentence enables interpretation without requiring memorisation of particular figure scores.', 'Lecture 7 p48 visually reopened; EMBL-EBI AlphaFold Server confidence documentation, ipTM 0–1 interface confidence')
(root/'other/work/scratch/coverage-audit-20261014/review/ab-closure-proposals.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'{len(items)} uniquely matched adjacent proposals')

"""Emit review proposals only. Never edits owned notes or canonical units."""
from pathlib import Path
import math
import json
root=Path(__file__).resolve().parents[5]
base=root/'other/work/archive/reviewed-units/Advanced Biotechnology'
proposals=[]
def proposal(unit,note,anchor,new,reason,source):
    for a,b in [('about18','about 18'),('about15','about 15'),('in2023','in 2023'),('a0','a 0'),('roughly1','roughly 1'),('while0','while 0'),('about74','about 74')]:
        new=new.replace(a,b)
    file=next(base.glob(f'{unit:02} - *.md'))
    text=file.read_text(encoding='utf-8')
    candidates=text.splitlines() if anchor.startswith(('- ', '| ')) else text.split('\n\n')
    old=next(p for p in candidates if p.startswith(anchor))
    assert text.count(old)==1
    small=next((root/'notes/Advanced Biotechnology').glob(f'*/AB-{note:02} - *.md'))
    proposals.append(dict(id=f'AB-{note:02}-{len(proposals)+1}',canonical=str(file.relative_to(root)).replace('\\','/'),
      published=str(small.relative_to(root)).replace('\\','/'),source=source,reason=reason,old=old,new=new))
proposal(2,8,'**Two regimes.**',
    '**Polymerase cycling assembly (PCA)** starts from short single-stranded oligos tiled across alternating strands. Their overlapping ends anneal and serve as primers for one another. Repeated denaturation, annealing and polymerase extension build longer products; a final PCR using primers at the two outer ends enriches the full-length construct. Overlaps should have similar melting temperatures so that all joints work in the same cycle.\n\n**Gibson assembly** starts from double-stranded fragments with matching end overlaps. T5 exonuclease removes nucleotides from the 5′ ends, exposing complementary **3′ single-stranded overhangs**. These anneal; a polymerase extends the paired 3′ ends to fill gaps, and a DNA ligase seals the remaining nicks. The original enzyme combination uses Phusion polymerase and Taq ligase. A one-pot version runs isothermally near 50 °C; a staged alternative exposes overlaps first and then adds the repair enzymes, allowing control of processing for larger constructs. Joining is seamless because the shared overlap appears once in the completed DNA, rather than as an extra scar.',
    'Crop supplies the broad Gibson steps and temperature, but prose does not identify named methods or explain3′ overhang direction. Original staged option and named enzymes absent from current selected crop/prose.',
    'Lecture2 pp20–26; AB-08-Gibson.png and AB-08-PCA.png visually opened')
proposal(4,14,'**Why the errors are random here but systematic in nanopore.**',
    '**Why repeated observations improve accuracy.** SMRT pulse detection has stochastic errors that can often be reduced by combining passes over the same molecule. Nanopore measurements also contain random error as well as sequence-context-dependent bias, and repeated reads can improve their consensus too. The important statistical distinction is between independent error, which repeated observations reduce, and correlated error, which can persist. Neither platform has perfectly independent errors or a universal quality ceiling determined by its mechanism alone. Actual consensus accuracy must be measured for the chemistry, specimen and analysis used.',
    'Existing categorical nanopore-Q30 impossibility and exact independence contradict qualified consensus derivation already present. Mechanistic noise need not be perfectly correlated.',
    'Lecture4 pp12,14–18; independently checked consensus logic; earlier FINAL-AB-01-30 qualifications')
proposal(4,14,'Confining the observation volume with a sub-wavelength aperture',
    'Confining the observation volume and placing the label on the leaving group allow one polymerase to be monitored continuously. Circularising the template supplies repeated observations for consensus; stochastic errors can be reduced, while correlated errors and insufficient passes limit the gain. HiFi accuracy is an observed platform result, rather than a guarantee from a chosen raw error rate alone.',
    'Summary retains unqualified independence and12%-to-HiFi guarantee removed elsewhere by previous review.',
    'Lecture4 pp14–18; same numerical toy-model limitations as existing note')
proposal(5,17,'**Effect of assuming $E = 1$.**',
    '**Effect of assuming $E = 1$.** If both amplicons actually run at $E=0.9$, equation (32) gives $1.9^{3.3}=8.31547$ rather than $2^{3.3}=9.84916$. Reporting the latter overestimates the former by about18.4%. Equivalently, correcting the original estimate lowers it by about15.6%; the percentage differs because the reference denominator differs. The interpretation should use an efficiency measured for the assay and its operating range.',
    'Independent Python: estimate/true−1=18.443737%; source text16% uses wrong overestimate denominator.',
    'Added AB17 example; independent-ab-numbers.json')
proposal(5,17,"- The *second* difference (sample minus control)",
    "- The *second* difference (sample minus control) cancels the fixed **intercepts** of the same target and reference assays, including consistent fluorescence thresholds and response factors. Amplification efficiency still sets the concentration-to-cycle slope and must be equal between assays, or explicitly accounted for; taking a second difference does not remove that requirement.",
    'Residual prose claims intrinsic efficiencies cancel, contradicting correct equation32 and its stated assumptions.',
    'Lecture5 pp11–16; standard exponential threshold derivation')
proposal(6,19,'| Track record |',
    '| Track record | approved therapeutic examples include pegaptanib and avacincaptad pegol | many approved therapeutics |',
    'One-approved-aptamer count false: FDA approved avacincaptad pegol in2023.',
    'Lecture5 pp34–35 plus opened FDA approval record4August2023')
proposal(6,19,'**Therapeutics.**',
    '**Therapeutics.** *Pegaptanib* (Macugen) is a modified RNA aptamer that antagonises VEGF in macular degeneration. PEGylation and injection directly into the eye address its short systemic lifetime. It was the first approved aptamer medicine, rather than the only one: *avacincaptad pegol* (Izervay), approved by the FDA in2023, is a PEGylated RNA aptamer that inhibits complement protein C5 for geographic atrophy secondary to age-related macular degeneration. These examples show that nucleic-acid recognition can target different disease mechanisms.',
    'Same count error in applications paragraph; preserve source pegaptanib example and mechanism.',
    'Lecture5 p34; FDA Izervay snapshot and NDA217225 summary pp3–4 actually read')
proposal(8,26,'**Why confidence scores matter.**',
    '**Why confidence scores matter.** AlphaFold2 reports several complementary measures. **pLDDT** (predicted local distance difference test) assesses local structure around each residue on a0–100 scale, with larger values indicating greater confidence. **PAE** (predicted aligned error) estimates positional uncertainty in ångströms for one region when alignment is fixed on another; smaller values mean more confident relative placement. Two domains can each have high pLDDT while their orientation relative to one another has high PAE. **pTM** (predicted template-modelling score) summarises confidence in the overall arrangement on a0–1 scale, with larger values indicating greater confidence. Low confidence can be consistent with disorder or flexibility, but can also reflect insufficient information or model error. These are model confidence measures, not direct measurements or proof of a unique functional conformation.',
    'Source explicitly namespLDDT,pTM,PAE; generic per-residue discussion omits their distinction and interdomain uncertainty.',
    'Lecture7 pp47–48 visually read; EMBL-EBI confidence-score and AlphaFold Server documentation actually opened')
proposal(9,27,'**Antibody–drug conjugates (ADCs)**',
    '**Antibody–drug conjugates (ADCs)** combine antibody specificity with a cytotoxic payload. Design involves four linked choices: **which drug** to deliver, **where it attaches**, **how many copies** attach per antibody, and **how the linker releases** it. The payload must act effectively after delivery, while conjugation and release should preserve targeting and limit damage away from the intended cells. The suitable combination depends on the antigen, uptake, intracellular processing and drug mechanism.',
    'Source names4design choices; current paragraph lists3and omits payload identity. Avoids carrying forward source historical drug-course price as current fact.',
    'Lecture8 p14 visually read; p15 clinical plot is illustrative supporting example')
proposal(9,30,'**4. Phage display.**',
    '**4. Phage display.** Selection can be performed without immunising an animal and can bypass the animal’s tolerance to self-antigens. This broadens the accessible target range, but does not demonstrate that a selected antibody lacks cross-reactivity or would be safe in a patient.',
    'No concern about self-reactivity conflates absence of immune-tolerance restriction with safety/selectivity.',
    'Lecture8 pp33–34; site specificity already taught in AB19')
proposal(9,30,'**8. Computational design.**',
    '**8. Computational design.** Generative models such as RFdiffusion use structural training data to propose binders. Reported demonstrations include an influenza-target example with roughly1% binding designs and moderate affinity, illustrating why designed sequences need experimental testing. Computational antibody work has three distinct tasks: **affinity maturation**, improving CDRs of an existing binder; **rank prediction**, ordering candidates such as NGS-derived sequences by expected affinity; and **out-of-library design**, proposing new sequences informed by existing sequence-and-affinity data. Prediction and generation supply candidates; binding, specificity and function must still be measured.',
    'Source L8p42 three-task distinction missing; replaces undated current-performance wording with a reported example.',
    'Lecture8 pp41–43, p42 visually read')
proposal(9,30,'**The trade-off across methods.**',
    '**The trade-off across methods.** Animal methods provide affinity maturation but can be slow, restricted by tolerance to conserved self-antigens, and difficult when the target is toxic or poorly immunogenic. Toxic targets are a challenge, not an absolute exclusion: antitoxin antibodies can be generated through appropriate immunisation strategies. Mouse-derived sequences may need humanisation, whereas human-repertoire animals provide human sequences. *In vitro* selection allows targets and stringency to be controlled without animal tolerance, but useful candidates still need affinity, specificity and functional validation.',
    'Cannot target toxins is false; universal need humanisation contradicts subsequent human-repertoire mice. Qualify tradeoff.',
    'Lecture8 pp33,37,43; opened Nobel immunology history confirms animal antitoxin generation')
proposal(3,10,'- *Low throughput*:',
    '- *Low throughput*: one capillary reads one template population, and instruments can run roughly 96 in parallel. Cloning-based shotgun sequencing also needs separate clone preparation. Sanger sequencing of a purified PCR product or plasmid can be performed directly, so bacterial cloning is not a universal requirement of the sequencing chemistry.',
    'Low-throughput discussion and comparison table conflate shotgun cloning with all Sanger sequencing.',
    'Lecture3 pp7–16 distinguishes reaction requirements from shotgun library creation')
proposal(3,12,'**2. Why coverage rescues it.**',
    '**2. Why coverage rescues it.** For 30 independent observations with substitution-error probability $p=10^{-3}$, a conservative consensus-failure bound counts every case with at least 15 errors, including a possible tie, as failure: $P_{\\mathrm{fail}}\\le\\sum_{j=15}^{30}\\binom{30}{j}p^j(1-p)^{30-j}\\approx1.53\\times10^{-37}$. Fewer than 15 errors leave more than half the observations correct, guaranteeing the correct strict-majority base under this model. Counting only 16 or more errors gives $1.44\\times10^{-40}$, but omits ties. Actual consensus also needs alignment and insertion/deletion handling, and correlated errors or mapping bias can dominate these tiny independent-error bounds.',
    'Analogous old majority/tie flaw already repaired in AB13–14 persists in AB12. Existing strict-tail number is correct for16errors but not a full consensus bound.',
    'Added AB12 example; independently recomputed binomial tails in Python')
proposal(8,24,'To see something you must illuminate',
    'Atomic structure requires radiation that probes ångström-scale features, so macromolecular crystallography uses X-rays. The experiment records a diffraction pattern from a crystal and reconstructs electron density computationally, rather than forming a direct, atom-resolved image with a conventional microscope. X-ray focusing optics can shape the beam; they do not remove the need to recover phase information in this diffraction experiment.',
    'Added categorical no-X-ray-lenses/cannot-focus claim is broader than crystallographic phase problem and false as general optics.',
    'Lecture7 pp18–21 establish diffraction/phase mechanism; remove unsupported universal optical claim')
proposal(8,24,'**Why a synchrotron.**',
    '**Why a synchrotron.** A synchrotron supplies a bright, tunable X-ray beam that can collect useful diffraction from small or weak crystals. The achieved resolution depends on the crystal and measurement conditions. A dataset reaching about 1.8 Å illustrates a successful collection; it is not a universal capability or limit of an in-house source.',
    'Source p31 places1.8Å after Diamond collection and says less resolution with in-house; study prose reverses this to fixed in-house1.8Å.',
    'Lecture7 pp30–31 original text and image')
proposal(8,24,'**What resolution means.**',
    '**What resolution means.** Higher-resolution diffraction corresponds to smaller spacings and reflections at larger scattering angle. From Bragg’s law, $\\lambda=2d\\sin\\theta$ with $\\lambda=1.54$ Å, 2 Å data requires reflections near $\\theta=23°$, while0.8 Å requires about74°. High-angle reflections are often weak. Useful resolution therefore depends on crystal order, wavelength and angular coverage, signal quality and radiation damage; a better instrument helps record information only if the specimen supplies it.',
    'Crystal-only resolution assertion hides wavelength/angular and signal limitations; retains the correct Bragg examples.',
    'Lecture7 pp15–21,31; existing independently verified Bragg examples')
(Path(__file__).parent/'ab-proposed-corrections.json').write_text(json.dumps(proposals,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
numbers=dict(qPCR_E1=2**3.3,qPCR_E09=1.9**3.3,relative_overestimate_pct=(2**3.3/1.9**3.3-1)*100,
    reduction_from_reported_pct=(1-1.9**3.3/2**3.3)*100,
    consensus_ge15=sum(math.comb(30,j)*.001**j*.999**(30-j) for j in range(15,31)),
    consensus_ge16=sum(math.comb(30,j)*.001**j*.999**(30-j) for j in range(16,31)),
    Bragg_theta_at_2A_deg=math.degrees(math.asin(1.54/(2*2))),
    Bragg_theta_at_point8A_deg=math.degrees(math.asin(1.54/(2*.8))))
(Path(__file__).parent/'independent-ab-numbers.json').write_text(json.dumps(numbers,indent=2)+'\n',encoding='utf-8')
print(f'{len(proposals)} exact, uniquely matched canonical review proposals; no owned notes edited.')

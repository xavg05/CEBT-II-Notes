from pathlib import Path
import json
p=Path(__file__).with_name('merge.py')
s=p.read_text()
intro=[
'Nucleic-acid chemistry determines the structures that DNA and RNA can form. Polymer bending, two-state hybridisation and nearest-neighbour thermodynamics explain their geometry and stability; association and dissociation kinetics explain how quickly those structures assemble and rearrange.',
'Chemical synthesis builds short oligonucleotides one nucleotide at a time, so modest losses at each coupling accumulate into a strong length limit. Overlapping fragments can then be assembled into genes and whole genomes, separating chemical manufacture from biological replication.',
'Sanger sequencing reads chain-terminated fragments, while Illumina reads large numbers of immobilised templates in parallel. Library preparation, cluster generation and reversible-terminator chemistry connect an original sample to short reads that must be assembled or mapped.',
'Nanopore and PacBio sequencing read individual molecules through different physical signals. Their long reads complement short-read methods by spanning repeats, resolving variants and supporting applications that depend on molecular context.',
'Quantitative PCR estimates the starting abundance of a target from the cycle at which exponential amplification reaches a fluorescence threshold. Calibration, reference genes and sequence-specific detection make that estimate usable while exposing the assumptions behind absolute and relative quantification.',
'Aptamers use folded nucleic acids to recognise molecular targets. SELEX couples binding selection to amplification so that rare useful sequences become enriched, with specificity determined by the selection conditions and counter-selection.',
'Sequence-dependent hybridisation makes DNA a programmable connector. Structural assemblies use that selectivity to organise objects, while toehold-mediated strand displacement provides controlled reactions that rearrange structures or process molecular signals.',
'Protein folding connects amino-acid sequence to molecular function. X-ray crystallography, cryo-electron microscopy and NMR infer structure from experimental signals; computational methods predict it from learned constraints, with different limitations and validation needs.',
'Protein engineering changes function, stability or behaviour in the body by altering sequence, architecture and chemical modifications. Mutagenesis and non-canonical amino acids supply the changes, while antibody-generation and screening methods identify useful variants.',
'A bioprocess must deliver a useful product at scale, with upstream production and downstream recovery designed together. The recovery train first separates cells from liquid; filtration illustrates how equipment choice, cake growth and compressibility determine throughput and area.',
'Centrifuges accelerate density-driven settling and arrange the available separation area in compact geometries. Stokes settling and residence-time arguments give a cut-off throughput, while sigma theory separates feed properties from equipment performance for conditional scale-up.',
'Intracellular products require disruption before purification, but breaking cells also releases debris, nucleic acids and degradative enzymes. Mechanical and non-mechanical methods balance release against product damage; release kinetics and a homogeniser fit make that trade quantitative.',
'Primary isolation separates a product from the clarified broth using partitioning, precipitation or adsorption. Equilibrium relations and material balances connect the molecular mechanism to recovery, product concentration and the cost of pursuing very high yield.',
'Chromatography separates components through differences in binding or accessible pore volume. Retention measures describe differential migration, while final isolation converts a purified stream into the physical form needed for storage and use.',
'Gene expression couples transcription and translation to degradation and dilution. Regulatory proteins change synthesis rates; feedback motifs shape steady states and response times, stochastic events generate noise, and delayed cyclic repression can produce oscillations.',
'Cell-free systems move transcription and translation into an engineered reaction mixture. In-vitro transcription enables mRNA production, while genome minimisation and bottom-up compartment construction explore complementary routes to simpler cellular systems.',
'Programmable DNA and RNA interactions can organise molecules into condensates. Molecular valency, binding strength and fuel-dependent reactions connect sequence-level design to phase behaviour and dynamic organisation.'
]
prereq=[
'ideal dilute-solution thermodynamics and mass-action kinetics',
'covalent bonding, nucleotide structure and PCR',
'nucleotide polymerisation, PCR and sequence complementarity',
'nucleotide polymerisation and the short-read sequencing principles',
'PCR, logarithms and gene expression',
'nucleic-acid folding, binding equilibria and PCR',
'hybridisation thermodynamics and nucleic-acid polymer physics',
'amino-acid chemistry, thermodynamics and molecular recognition',
'protein structure, genetic coding and molecular recognition',
'material balances, transport and basic microbial cultivation',
'force balances, low-Reynolds-number drag and residence time',
'cell structure, material balances and first-order kinetics',
'phase equilibria, protein structure and material balances',
'phase partitioning, adsorption and downstream-process stages',
'mass-action kinetics, first-order balances and DNA-to-RNA-to-protein information flow',
'gene expression, enzyme catalysis and membrane structure',
'hybridisation, phase separation and toehold-mediated strand displacement'
]
s=s.replace("overview='\\n\\n'.join(overviews)","overview=INTRO[index-1]")
s=s.replace("prerequisites=' '.join(re.sub(r'^\\*Assumed[^:]*:\\*?\\s*','',a).strip().rstrip('.') for a in assumptions)","prerequisites=PREREQUISITES[index-1]")
s=s.replace("closing=('These mechanisms connect '+title.lower()+'. ')","closing=FINAL[index-1]+' '")
final=[
'Hybridisation thermodynamics selects stable pairings, and kinetics determines whether those pairings rearrange on the available timescale.',
'The per-step yield limits direct synthesis length; assembly and replication extend that chemistry to larger DNA constructs.',
'Parallel readout increases throughput, while amplification and assembly introduce distinct sources of bias and uncertainty.',
'Long reads preserve molecular context, and the appropriate platform depends on the biological question and error tolerance.',
'Threshold cycles become abundance estimates only when amplification efficiency, signal specificity and normalisation are controlled.',
'Selection conditions determine which binding properties are enriched, so amplification alone is never evidence of useful specificity.',
'DNA nanotechnology combines addressable structure with programmable reaction kinetics.',
'Experimental determination and computational prediction answer related structural questions, and each requires validation against its own limitations.',
'Sequence changes and screening connect molecular recognition to useful biological performance.',
'Cell removal links broth properties to equipment duty, and cake compressibility makes added filtration area more reliable than added pressure.',
'Sigma theory supports scale-up when feed properties, separation criteria and geometric conventions remain consistent.',
'Disruption recovery must be assessed alongside the damage and contaminants introduced by the release operation.',
'Partitioning, solubility and binding equilibria set recovery, while material balances expose the concentration and capacity trade-offs.',
'Retention describes migration, peak widths determine resolution, and final isolation sets the product form.',
'Feedback controls average behaviour, while fluctuations and delays determine how reliably a circuit achieves it.',
'Removing cellular complexity makes individual functions easier to control, but rebuilding autonomy requires their integration.',
'Condensate design connects molecular interactions to collective organisation and its control in time.'
]
s=s.replace("UNITS=[",'INTRO='+repr(intro)+'\nPREREQUISITES='+repr(prereq)+'\nFINAL='+repr(final)+'\nUNITS=[',1)
p.write_text(s)
print('Updated merged overviews, shared prerequisites and final conclusions.')

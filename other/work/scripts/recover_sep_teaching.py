"""One-time initial recovery; subsequent editorial refinements live in the notes.

The per-note record prevents accidental duplicate insertion on a later run.
"""
from pathlib import Path
import subprocess,re,json

ROOT=Path(__file__).resolve().parents[3]
assert not (ROOT/'other/work/reviews/sep-teaching-recovery.json').exists(), 'Recovery already applied; edit the current corrected notes instead.'
DRAFT=ROOT/'other/work/drafts/Separations II'
NATIVE=ROOT/'other/obsidian/CEBT-II Notes/Separations II'
READ=ROOT/'notes/Separations II'
MATH=re.compile(r'(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$')
def github(s):
    def conv(m):
        if m[1] is None:return '$`'+m[2]+'`$'
        f=m[1].strip();tags=re.findall(r'\\tag\{(\d+)\}',f)
        label='\n**Equation ('+tags[0]+')**\n' if tags else ''
        return label+'\n```math\n'+re.sub(r'\\tag\{\d+\}','',f).strip()+'\n```\n'
    return MATH.sub(conv,s)

# Notes with distinctive quantitative comparisons retain the checked design case.
KEEP={3,4,5,9,10,13,14,16,18,19,20,21,27,28,30,32,34,38,39,43}
TEXT={
1:r'''Solvent selection must include regeneration. A low-volatility solvent that preferentially dissolves the recovered compound can reduce absorber liquid demand, yet stronger binding can make subsequent stripping harder. Optimising uptake alone can therefore move the main difficulty into the recovery stage.''',
2:r'''Low liquid flow can leave packing incompletely wetted. Adding height then adds nominal surface without a proportional increase in active interface, so a vacuum or corrosive service that favours packing must still satisfy distributor and wetting requirements. Intermediate cooling coils and liquid withdrawals may instead favour trays, with their pressure loss included in the comparison.''',
6:r'''An inferred film thickness is an effective transport distance. At unchanged hydrodynamics the film model predicts that reducing diffusivity to three quarters of its calibration value reduces the individual coefficient to three quarters too. This does not give the same proportional change in overall coefficient: the second film and the species' partition coefficient still enter its total resistance.''',
7:r'''HTU describes the chosen equipment's transfer effectiveness, whereas NTU describes the composition path's driving-force demand. Their product is height, but neither factor separately counts trays. Changing packing at the same composition path primarily changes HTU; changing solvent flow can change both the operating path and the transport prefactor.''',
8:r'''A small endpoint driving force carries disproportionate weight because height integrates its reciprocal. Arithmetic averaging can therefore underestimate the required height. For the linear absorber model, the log mean follows from that integral; curved equilibrium requires the actual intervening profile rather than an endpoint average.''',
11:r'''The transfer calculation supplies packed volume $AZ$, not height alone. Dividing it by an assumed area gives a conditional height, not a hydraulic design. Diameter still needs packing data, fluid properties, pressure-drop allowance and flooding checks; the transfer coefficient must also be appropriate at the resulting flows per unit area.''',
12:r'''Moisture specifications must state their basis: dry-basis $w$ divides water mass by dry solid, whereas wet-basis $z$ divides it by total wet mass. The distinction persists even though both ratios are dimensionless. Equipment selection also starts with product integrity: a fragile sheet needs supported handling, while robust granules may tolerate agitation and through-flow gas.''',
15:r'''Cooling an unsaturated gas initially follows constant humidity until condensation begins. Below its dew point, the gas loses vapour into a liquid outlet and its humidity declines. Following a constant-enthalpy evaporation line would represent a different process, so a similar-looking chart construction cannot replace the appropriate mass and energy balances.''',
17:r'''The wet-surface time estimate is valid only while liquid can replenish the assumed exposed area and maintain its wet-bulb temperature. An endpoint below critical moisture requires a separate falling-rate integral: extending the initial rate would hide the slower internal supply of water.''',
22:r'''External heating raises both surface temperature and evaporation rate. If evaporation were artificially held fixed, the extra surface temperature would be $q''_{\mathrm{ext}}/U$. Under the stated constant-coefficient model, saturation humidity increases with temperature, so the actual steady rise is positive but smaller: part of the added heat drives extra evaporation. External duty alone cannot determine the new flux without the mass-transfer coefficient, saturation relation and latent heat.''',
23:r'''A gas that dissolves strongly need not permeate fastest: permeability compares the product of solubility and diffusivity. The larger product gives greater flux only at the same thickness and partial-pressure driving force. Mixture-dependent sorption or polymer swelling can invalidate selectivity inferred from pure gases. Mild operation and avoiding bulk boiling likewise do not remove compression, pumping, pretreatment or membrane-replacement duties.''',
24:r'''A low once-through production rate does not require low internal crossflow velocity. Recycling retentate can maintain tangential flow while net feed and product remain small. Recycle cancels from the overall plant balance, but its pumping requirement and effect on the feed-side film remain physical design constraints.''',
25:r'''A stage cut measures the fraction of total feed entering permeate; component recovery measures the fraction of a chosen feed species recovered there. Enrichment and stage cut must both enter that species balance. High enrichment alone does not establish high recovery, and high total permeate production does not establish good selectivity.''',
26:r'''At finite permeate pressure, enrichment is limited by partial-pressure opposition as well as intrinsic selectivity. Increasing selectivity while leaving the pressure ratio unchanged cannot remove that opposition. A selectivity measured from pure-gas permeances therefore does not by itself specify the achievable permeate composition.''',
29:r'''A pressure increase can improve rejection through permeate dilution when external films and osmotic opposition are negligible. Under polarisation, the same increase also raises wall concentration and osmotic opposition, changing both solute passage and water flux. Interpret a pressure–rejection curve with its mass-transfer conditions rather than assigning every trend to the membrane material.''',
31:r'''Even an ideal osmotic-pressure estimate must use the membrane-wall concentration when a polarised feed contacts the selective layer. Using bulk concentration underestimates the thermodynamic opposition if solute accumulates at the wall. Reverse solvent flow requires imposed pressure to exceed the relevant difference in osmotic pressure; dilute complete-dissociation estimates are not high-accuracy concentrated-salt properties.''',
33:r'''Diagnose a persistent flux decline on a common temperature, concentration, recovery and pressure-loss basis. Restoring crossflow or reducing permeation can relax concentration polarisation; loss that persists then calls for fouling or integrity investigation. Increasing pressure can intensify polarisation or compact deposits, so recovering flow by extra pressure does not establish recovery of the original membrane condition.''',
35:r'''Saturation capacity is not cyclic working capacity. Regeneration leaves a heel, and only the difference between loading and regenerated states is available in the next cycle. Counting the entire loaded inventory as newly captured material would overstate each cycle's separation duty.''',
36:r'''The dimensionless affinity product, rather than pressure alone, identifies the Langmuir regime. Low affinity times pressure gives approximately linear uptake; a large product approaches saturation, so further pressure then adds little capacity. The same distinction applies to concentration relative to the dissociation constant in the liquid form.''',
37:r'''A fixed-fluid uptake fraction describes approach to the solid's equilibrium loading, not the fraction removed from a finite batch's original solute inventory. In a finite batch the surrounding concentration declines during uptake, so its equilibrium loading changes and must be coupled to the liquid balance.''',
40:r'''The equilibrium loading difference between high and low pressure is an upper estimate for pressure-swing capacity under those two states. A finite cycle may not reach either equilibrium because desorption, diffusion and pressure changes take time. Use measured working capacity for the actual cycle instead of assigning the full equilibrium difference automatically.''',
41:r'''Retention predicts mean migration but does not establish separation from a neighbouring peak. Stronger retention can delay both species together. Distinguish this equilibrium delay from peak spreading before deciding whether an altered mobile phase has improved the useful separation.''',
42:r'''A peak can have different conventional and effective plate numbers because effective retention excludes mobile-phase transit time. State the convention before comparing columns. For the velocity model, the optimum balances decreasing longitudinal-diffusion broadening against increasing transfer lag; its minimum height still includes the velocity-independent contribution.''',
}
WHY={3:'composition-basis numerical contrast',4:'absorption versus stripping pinch comparison',5:'converted resistance shares identify the useful intervention',9:'different stage and transfer-unit counts for the same duty',10:'velocity fraction squares on the chart ordinate',13:'percentage saturation differs from relative humidity and chart uncertainty',14:'liquid sensible enthalpy changes the saturation construction',16:'wet-bulb chart approximation and solvent-dependent auxiliary axes',18:'chart-based mass balance and pinch margin',19:'two rate branches and chart-limited exit state',20:'flow arrangement changes the active branch, not a universal ranking',21:'quadrature refinement differs from experimental accuracy',27:'endpoint averaging creates material area differences',28:'mesh convergence, local versus collected composition and species recovery',30:'outside-film geometry and true versus apparent rejection',32:'coupled osmotic curvature, pressure threshold and gel endpoint',34:'integration accuracy can cross a whole-module threshold',38:'physical root, inventory closure and equilibrium mass versus time',39:'breakthrough interpolation and integrated capacity differ',43:'exact width calculation differs from equal-width approximation'}
records=[]
for n,p in enumerate(sorted(DRAFT.rglob('U*-*.md')),1):
    old=subprocess.check_output(['git','show',f'77f9703^:{p.relative_to(ROOT).as_posix()}'],cwd=ROOT).decode('utf-8')
    block=re.search(r'## Worked example\s*\n([\s\S]*?)(?=\n## )',old)[1].strip()
    if n in KEEP:
        added=block
        added=re.sub(r'\n\n\d+\. ', '\n\n',added)
        added=added.replace('Suppose a preliminary hydraulic estimate gives','A preliminary hydraulic estimate can give')
        added=added.replace('To check the integration method independently of graph-reading uncertainty, use the specified analytical model','Quadrature can be checked independently of graph-reading uncertainty using the specified analytical model')
        added=added.replace('The results are','These choices produce')
        added=added.replace('Use the measured correlation','For these stated conditions, the measured correlation is')
        added=added.replace(r' \tag{5}','') if n==32 else added
        added=added.replace('Equation (5) gives', 'the measured correlation gives') if n==32 else added
        reason=WHY[n]
    else:
        added=TEXT[n];reason='Retain mechanism or validity distinction; omit direct substitution and redundant numerical illustration.'
    # Current corrected text remains the base, including all post-removal fixes.
    current=p.read_text(encoding='utf-8')
    assert '## Worked example' not in current
    p.write_text(current.replace('\n## Link to other topics','\n'+added+'\n\n## Link to other topics'),encoding='utf-8')
    native,=NATIVE.rglob(f'SEP-{n:02d} - *.md')
    s=native.read_text(encoding='utf-8');local=re.findall(r'\\tag\{(\d+)\}',current);glob=re.findall(r'\\tag\{(\d+)\}',s)
    assert len(local)==len(glob),(p,local,glob)
    mapping=dict(zip(local,glob))
    def ref(m):return m[1]+' ('+mapping[m[2]]+')'
    exported=re.sub(r'\b([Ee]quation|[Ee]q\.)\s*\((\d+)\)',ref,added)
    # Existing pre-removal figure names keep their established publication identity.
    exported=re.sub(r'../figs/u\d+-(?:\d+-)?([^\)]+)',lambda m:'../figs/SEP-'+f'{n:02d}-'+m[1],exported)
    s=s.replace('\n## Link to other topics','\n'+exported+'\n\n## Link to other topics')
    native.write_text(s,encoding='utf-8')
    (READ/native.relative_to(NATIVE)).write_text(github(s),encoding='utf-8')
    records.append({'note':f'SEP-{n:02d}','path':p.relative_to(ROOT).as_posix(),'decision':reason,'retained_numeric_case':n in KEEP,'old_removed_words':len(block.split()),'integrated_words':len(added.split()),'labels_unchanged':local==re.findall(r'\\tag\{(\d+)\}',p.read_text(encoding='utf-8'))})
out=ROOT/'other/work/reviews/sep-teaching-recovery.json'
out.write_text(json.dumps(records,indent=2),encoding='utf-8')
print(json.dumps({'audited':len(records),'quantitative_cases':len(KEEP),'labels_preserved':all(x['labels_unchanged'] for x in records)},indent=2))

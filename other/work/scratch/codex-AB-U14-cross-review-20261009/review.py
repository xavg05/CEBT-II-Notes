from pathlib import Path
import hashlib,json,math,re,struct
root=Path(__file__).resolve().parents[4]; scratch=Path(__file__).resolve().parent
notes={n:next((root/'out/AB').glob(f'AB-{n}-*.md')) for n in range(53,57)}
hashes={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in notes.values()}
# Independent recomputation from note inputs; do not import owner scripts/results.
m0=100.; cap=.90; recovery=.80; formulation=.95
mc=m0*cap; mp=mc*recovery; mf=mp*formulation
assert math.isclose(mf,68.4)
for zero in range(3):
    factors=[cap,recovery,formulation]; factors[zero]=0
    assert m0*math.prod(factors)==0
assert m0*math.prod([1,1,1])==m0
protein_genes=438; rna_genes=35; total=protein_genes+rna_genes
assert total==473
fraction=149/total
assert round(fraction*100,1)==31.5
co=1.; permeability=1e-8; demand=1e-3
membrane=[]
for radius_um in [5.,10.]:
    R=radius_um*1e-6
    area=4*math.pi*R**2; volume=4*math.pi*R**3/3
    coefficient=area*permeability/volume
    assert math.isclose(area/volume,3/R)
    tau=1/coefficient; depletion=demand/coefficient; steady=co-depletion
    residual=area*permeability*(co-steady)-volume*demand
    assert abs(residual)<1e-30
    assert math.isclose(tau,R/(3*permeability))
    assert math.isclose(steady,co-R*demand/(3*permeability))
    # Closed-form transient for constant q; finite differences independently
    # verify the balance and decay timescale, away from negative concentrations.
    initial=.5
    f=lambda t:steady+(initial-steady)*math.exp(-coefficient*t)
    for t in [0.,tau,5*tau]:
        h=.01
        derivative=(f(t+h)-f(t-h))/(2*h)
        rhs=coefficient*(co-f(t))-demand
        assert abs(derivative-rhs)<1e-10
    # Zero demand => equilibration to co; equal concentrations => zero flux.
    assert coefficient*(co-co)==0
    assert co-0/coefficient==co
    assert permeability*(co-co)==0
    # Zero permeability is handled in original ODE, without dividing by P.
    c_initial=.5
    sealed_rate=area*0*(co-c_initial)/volume-demand
    assert sealed_rate==-demand
    # Demand above maximum supply yields an invalid negative formal steady state.
    max_demand=coefficient*co
    assert co-(2*max_demand)/coefficient<0
    membrane.append(dict(radius_um=radius_um,area_m2=area,volume_m3=volume,
        area_to_volume_per_m=area/volume,exchange_coefficient_per_s=coefficient,
        exchange_time_s=tau,depletion_mM=depletion,steady_concentration_mM=steady,
        full_balance_residual=residual,maximum_sustainable_demand_mM_per_s=max_demand))
assert math.isclose(membrane[1]['exchange_time_s']/membrane[0]['exchange_time_s'],2)
# Large P and small R: depletion and exchange time tend to zero.
assert demand/(3*1e3/(5e-6))<1e-10
assert (1e-12)/(3*permeability)<1e-3
headings=['Overview','Intuition','Derivation','Motivation and explanation','Worked example','Link to other topics','Conclusion']
structure=[]
for number,p in notes.items():
    text=p.read_text()
    assert text.startswith(f'# Section {number}:')
    assert re.findall(r'^## (.*)$',text,re.M)==headings
    tags=[int(n) for n in re.findall(r'\\tag\{(\d+)\}',text)]
    expected={53:[],54:[1],55:[1],56:[1,2,3]}[number]
    assert tags==expected
    assert not re.search(r'lecturer|lecture\s*(?:PDF|slides|15)|source\s*PDF|\[\[|^>\s*\[!',text,re.I|re.M)
    assert text.count('$$')%2==0
    images=[]
    for link in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',text):
        data=(p.parent/link).read_bytes(); assert data[:8]==b'\x89PNG\r\n\x1a\n'
        w,h=struct.unpack('>II',data[16:24]); assert w>0 and h>0
        images.append(dict(path=link,width=w,height=h))
    assert len(images)=={53:2,54:1,55:2,56:2}[number]
    structure.append(dict(note=str(p.relative_to(root)),tags=tags,seven_sections='PASS',images=images))
results=dict(verdict='PASS',note_sha256=hashes,
    AB54=dict(capped_mg=mc,purified_mg=mp,formulated_mg=mf,overall_recovery_percent=100*mf/m0),
    AB55=dict(protein_genes=protein_genes,RNA_genes=rna_genes,total_genes=total,
        unknown_specific_function_fraction=fraction,unknown_specific_function_percent=100*fraction,
        figure_stated_doubling_time_hours=178/60),
    AB56=membrane,membrane_transient_and_limiting_case_checks='PASS',structure=structure)
(scratch/'independent-results.json').write_text(json.dumps(results,indent=2)+'\n')
review=root/'out/work/reviews/AB-U14.md'; review.parent.mkdir(parents=True,exist_ok=True)
review.write_text('''# AB-U14 cross-review — AB-53–56

**PASS. No material finding or required correction.**

Bounded read-only review of all four notes and shared progress codex-ab53-56-l15-20261009.md. No source PDF processing or external-source rereading; no owner files changed. All seven existing figures visually opened, and their relative links verified. Parent retains KaTeX rendering and integration.

- **AB-53 mechanisms:** transcription, aminoacyl-tRNA charging, translation factors/GTP, energy regeneration, extract preparation and PURE distinctions are coherent. Release-factor omission example also supplies charged suppressor tRNA and a separate termination route. Extract yield, nucleic-acid cleanup, oxygen dependence and auxiliary machinery are appropriately qualified.
- **AB-54 mechanisms and calculation:** IVT vs TXTL, cap chemistry, alternative capping/tailing routes, impurity removal and delivery are correctly distinguished. Proposed enzyme recycling is not treated as established selective ultrafiltration. Independent recovery: 100 × 0.90 = 90.0 mg; × 0.80 = 72.0 mg; × 0.95 = 68.4 mg, or 68.4% overall. Equation (1), units, zero-factor and unity-factor limits pass.
- **AB-55 mechanism and calculation:** environment-dependent essentiality, quasi-essentiality, incompatible combined deletions, genome assembly/transplantation and recipient cytoplasm are explained. 438 + 35 = 473; 149/473 = 0.3150105708245243, or 31.5% rounded. Historical unknown-specific-function count is correctly distinguished from current knowledge and unassigned chart categories. Approximate three-hour growth statement agrees with the figure's stated 178 min (2.9667 h); no fitted graph readings needed.
- **AB-56 membrane model:** d(Vc)/dt = A P(co-ci) - Vq reduces to dc/dt = (3P/R)(co-ci)-q only for the explicitly fixed volume and spherical geometry. Signs, units and steady solution ci*=co-Rq/(3P) pass. Independent values: R=5 µm gives tau=166.6667 s, depletion=0.1666667 mM and ci*=0.8333333 mM; R=10 µm gives tau=333.3333 s, depletion=0.3333333 mM and ci*=0.6666667 mM. All rounding in the note agrees. Verified the transient by finite differences, full balance residuals, zero demand, equal-concentration zero flux, zero permeability in the original balance, increased-radius scaling, high-permeability/small-radius limits and excessive-demand negative formal steady state. The last is explicitly rejected as unphysical in the note; consumption must become substrate-dependent near exhaustion. Compartments and microscopy are not claimed to prove autonomous life.

All four notes have the required seven H2 sections and Section NN titles. Tags are local and sequential: AB-53 none, AB-54 1, AB-55 1, AB-56 1–3. No source-PDF/lecturer narration, wikilinks or callouts. All seven figure links resolve, labels/captions match their use, and meaningful scale bars in growth/organelles figures remain visible.

Review limits: source fidelity relies on the shared source-reading record; no additional publisher audit or parent-owned KaTeX rendering performed. No current blocker or owner action required.

Independent script: out/work/scratch/codex-AB-U14-cross-review-20261009/review.py
Results: out/work/scratch/codex-AB-U14-cross-review-20261009/independent-results.json
''')
for p in notes.values():
    assert hashlib.sha256(p.read_bytes()).hexdigest()==hashes[str(p.relative_to(root))]
print(json.dumps(results,indent=2))
print('Review saved:',review.relative_to(root))

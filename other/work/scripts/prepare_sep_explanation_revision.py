"""Topic-specific explanation proposals; apply centrally with other subjects."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'other/obsidian/CEBT-II Notes/Separations II'
proposals=[]
REPLACE_ANCHORS={
    15:'This condition is independent of the initial gas temperature as long as that temperature is above the dew point. Temperature establishes how much cooling is needed; $H$ and $P$ establish where condensation starts.',
    24:'If solute leaks into the permeate, the concentration ratio is smaller than VCR. Recycle flow cancels from the overall balances because it crosses an internal boundary twice.',
    25:'The first is apparent rejection based on bulk feed, the second intrinsic or true rejection based on the wall. Complete rejection gives $C_p=0$ and both equal unity. In a concentration-polarised retained-solute system, $C_w>C_f$, so the apparent rejection is lower than true rejection at the same $C_p$.',
    36:'*Reason:* slope and intercept identify the two parameters. Reciprocal transformation magnifies errors at small concentrations; a fit to the original loading data is often preferable.',
    38:'The isotherm defines the endpoint; contact time and agitation determine whether it is approached. A reused adsorbent requires $q_0$ in the balance. Assuming fresh solid during every cycle overstates removal.',
}

def add(n, text, heading='## Motivation and explanation'):
    p,=BASE.rglob(f'SEP-{n:02d} - *.md')
    source=p.read_text(encoding='utf-8')
    assert source.count(heading)==1,p
    old=REPLACE_ANCHORS.get(n,heading)
    assert source.count(old)==1,(p,old)
    new=text.strip() if n in REPLACE_ANCHORS else text.strip()+'\n\n'+heading
    if n==25:new='Apparent rejection uses bulk feed; true rejection uses the wall. Complete rejection gives $C_p=0$ and both equal unity.\n\n'+new
    if n==38:new+='\n\nContact time and agitation determine approach to that endpoint. A reused adsorbent also requires its initial loading $q_0$ in the balance; it does not have the full capacity of fresh solid.'
    proposals.append({'path':p.relative_to(ROOT).as_posix(),'note':f'SEP-{n:02d}',
                      'gap':text.strip().split('\n')[0],
                      'edits':[{'old':old,'new':new}]})

add(1,r"""
Read the operating and equilibrium lines as answers to two different questions. The operating line asks where transferred solute must go to conserve material. The equilibrium line asks which two leaving compositions can coexist without further net transfer. Neither relation supplies a rate. In continuous contact, the gap between them supplies the local driving force; the equipment must supply enough area for finite transfer across that gap.

A better solvent can increase that gap, whereas better contacting can increase transfer at the same gap. These improvements act on different parts of the design. Once the fluid has reached its equilibrium limit, increasing turbulence alone cannot make it cross that limit; changing solvent, temperature or pressure changes the limit itself.
""")
add(2,r"""
Follow a gas parcel through each device. Packing presents a succession of liquid films and renewed interfaces along its path. A tray bubbles the gas through a locally retained liquid pool before the gas advances to the next tray. Both need an interface and a route for the other phase to leave. A support, distributor, weir or downcomer therefore helps establish the flow pattern on which the separation model depends; it is not an accessory that can be omitted after calculating area.

The vacuum example makes pressure drop part of feasibility. Increasing contact intensity may improve transfer but also consumes the available pressure difference. A design that gives a good transfer coefficient at an unsustainable pressure drop cannot deliver that coefficient in operation.
""")
add(3,r"""
The density factors are a change of coordinates, not an extra equilibrium effect. At unchanged physical equilibrium, multiply each mole fraction by its phase's total molar density to recover the two concentrations. Substitution then guarantees that all four Henry conventions predict the same pair of physical states. Checking that pair is more informative than comparing the numerical constants in isolation.

At fixed temperature in the ideal dilute model, a pressure-based relation can remain unchanged while its mole-fraction slope changes with total pressure. The reason is that the same solute partial pressure becomes a smaller fraction of a higher total pressure. State the composition basis before interpreting a pressure effect as changed molecular affinity.
""")
add(4,r"""
The liquid flow changes how quickly solvent becomes loaded as solute is removed from the gas. For fixed gas removal, more solvent shares the transferred solute over more liquid, lowering its outlet concentration. The equilibrium gas concentration over that liquid is then lower, preserving a larger absorption driving force. This is why solvent flow affects height even though the total solute-removal duty is already fixed by the gas specifications.

At minimum flow the balance can still be satisfied algebraically, but a location has no remaining disequilibrium to drive transfer. The minimum is therefore a feasibility boundary approached by increasingly large equipment, not an economical operating point obtained merely by solving the overall balance.
""")
add(5,r"""
The electrical-resistance analogy concerns a common flux and additive driving-force drops. The two physical concentration drops cannot be added directly because they belong to different phases. Multiplying the liquid drop by the partition coefficient expresses its consequence on the gas basis; only then do the interfacial terms cancel. The analogy does not require gas and liquid concentrations to be continuous at the interface.

If one converted resistance is already much larger than the other, reducing the smaller one barely changes their sum. That explains the different improvement priorities in the carbon-dioxide and ammonia examples: the same change in gas agitation can matter greatly in one service and very little in another. Compare converted resistances, not the bare numerical film coefficients.
""")
add(6,r"""
The inferred film thickness is the diffusion distance that would reproduce the measured resistance under this model. Keeping that distance fixed while changing solute leaves diffusivity as the only changing factor in $k=D/\delta$, explaining the proportional extrapolation. A different diffusivity exponent in another model represents a different account of exposure and renewal, rather than a unit conversion error.

An overall measurement supplies one combined resistance. To identify an individual film from it, the calibration experiment must suppress or independently establish the other resistance. Otherwise several pairs of film coefficients can reproduce the same total uptake, so the separate coefficients cannot be recovered from that measurement alone.
""")
add(7,r"""
Rearranging the slice balance for $dz$ asks how much additional height is needed to remove a specified small composition increment. The required height is inversely proportional to the local driving force: a narrow gap costs more height for the same decrement in gas composition. Integrating adds those unequal costs rather than assuming that every part of the bed works at its inlet rate.

The HTU–NTU split separates the transport prefactor from the dimensionless integral only after the stated quantities are treated as constant. It does not make either factor universal. Changing packing at fixed flow and composition path primarily changes the prefactor; changing solvent flow also changes the path through the operating line and can change both factors.
""")
add(8,r"""
The logarithm comes from integrating the reciprocal of a linearly changing driving force. A small-force end is expensive because the reciprocal weights it strongly, so an arithmetic average of the endpoint forces gives too much credit to the favourable end. The log mean packages that exact integral into one effective force for the linear case; it is not a preferred average chosen independently of the balance.

When the two endpoint forces coincide, the physical problem is regular: every slice has the same force. The apparent zero divided by zero is a feature of the logarithmic expression, so taking its limit must recover the ordinary composition change divided by that common force. Curved equilibrium requires the actual intervening profile, not just this endpoint check.
""")
add(9,r"""
One ideal stage imposes equilibrium on leaving streams, which converts the gap from one stage to the next by a multiplicative factor. Continuous contacting instead integrates a local rate over a continuously varying gap. The logarithm of the stage factor and the continuous driving-force integral therefore produce different dimensionless counts even for the same specified separation.

In the worked example, both routes predict the same packed height after each count is multiplied by its own appropriate height measure. The disagreement between the counts is consequently not a conservation error. Using NTU as a tray count would combine the count from one model with the length scale from another.
""")
add(10,r"""
At fixed total gas flow, reducing cross-section increases superficial velocity and hence the gas's opposition to liquid drainage. Greater liquid holdup then narrows the remaining gas passages, which raises resistance further. This feedback explains the sharp upward turn near flooding: a low-loading pressure-drop power law cannot represent a geometry that is progressively filling with liquid.

The velocity fraction must be squared because the chart ordinate depends on gas mass flux squared. This is an algebraic consequence of the chosen ordinate, not a different flooding margin. After selecting diameter, the new gas and liquid flows per unit area must also be used in the mass-transfer calculation; diameter and height are coupled through hydrodynamics.
""")
add(11,r"""
The calculation deliberately uses equilibrium twice for different purposes. First, equilibrium with the entering gas defines a limiting liquid loading and hence a minimum solvent flow. After selecting an actual flow, the operating balance supplies the actual liquid loading at each location. Only then does equilibrium supply the hypothetical gas counterpart used to calculate the local driving force. Substituting the pinch loading as the actual outlet would undo the chosen margin above minimum flow.

Numerical refinement concentrates attention where reciprocal driving force is large, rather than where the concentration axis spans the widest interval. The convergence check verifies integration of the chosen interpolation model. It cannot establish that the tabulated equilibrium, constant temperature or gas-controlled coefficient is accurate for a different operating condition.
""")
add(12,r"""
Dry-basis accounting removes a moving denominator. Evaporating liquid changes the wet product mass, so a decrease in wet-basis moisture combines a change of liquid inventory with a change in the reference mass. Dividing by the conserved dry solid isolates the inventory that is actually being removed. This is why the dry-basis moisture difference can be multiplied directly by dry-solid mass.

The latent-heat estimate accounts for an amount of evaporation, not its speed. The same liquid removal can require a short intense heat input or a longer gentle input, subject to internal transport and product limits. Equipment choice needs those rates and constraints as well as the integrated energy duty.
""")
add(13,r"""
At fixed pressure and humidity, the vapour-to-carrier mole ratio and thus vapour partial pressure stay fixed during sensible heating. Saturation pressure rises with temperature, so relative humidity falls even though no water has left the gas. The gas becomes more capable of accepting water because its equilibrium endpoint has moved, not because heating has reduced its existing vapour inventory.

Percentage saturation uses a mass ratio with dry gas as denominator; relative humidity uses a partial-pressure ratio. The nonlinear conversion between mass ratio and partial pressure explains their unequal numerical values away from the dilute-vapour limit. Both locate the same physical state when their definitions are used consistently.
""")
add(14,r"""
Per kilogram of dry gas, evaporation increases the latent contribution to gas enthalpy while reducing its sensible-temperature contribution. A falling temperature can therefore accompany an almost unchanged total enthalpy. The word adiabatic refers to heat crossing the chosen boundary; the inlet hot gas already brings energy and the added liquid brings its own enthalpy.

The saturation curve alone leaves a family of possible saturated outlet states. The energy balance chooses which member of that family the inlet can reach. This is why guessing an outlet saturation temperature and reading its humidity is insufficient: the guessed state may demand energy that the incoming streams do not supply.
""")
add(15,r"""
Dew point is an endpoint determined by the vapour already present. Two unsaturated gas samples at different initial temperatures but the same humidity and pressure have the same dew point; they need different sensible-cooling duties to reach it. Increasing their initial temperature changes that duty without changing the first-condensation condition.

Once condensation starts, further cooling removes vapour as well as energy, so the fixed-humidity construction must stop. A downstream equilibrium cooler calculation follows the saturation boundary and includes the condensed-liquid stream. This change in the mass balance is the reason the pre-condensation path cannot simply be extended below dew point.
""")
add(16,r"""
The surface temperature is selected by competing rates. If it falls, the temperature difference supplying heat grows, while its saturation humidity falls and reduces evaporation demand. If it rises, the opposite changes occur. Their intersection fixes the steady wet-bulb temperature; it is not the saturation temperature of the unchanged bulk humidity.

Adiabatic saturation is instead an overall stream-energy and equilibrium construction. The two temperatures are close for air/water because the relevant heat and mass transport properties approximately match, not because every wet surface must reproduce an ideal saturator. The chloroform example makes the limit of that analogy visible.
""")
add(17,r"""
Critical moisture marks a mismatch of rates: internal liquid supply can no longer support the evaporation demanded by the gas at a fully wet surface. Raising external demand can cause that mismatch earlier even in unchanged material. Equilibrium moisture answers a different question: how much liquid remains when there is no net thermodynamic driving force under the specified gas conditions.

Below the transition, a smaller latent-heat demand leaves more of the incoming heat available to warm the solid. Its temperature rise is therefore part of the mechanism indicating that the wet-surface model is losing validity. Continuing the constant-rate division into this region would assume away the very internal limitation that defines it.
""")
add(18,r"""
The minimum gas ratio follows from water-carrying capacity, while the actual ratio sets the local humidity rise per unit water picked up. With more dry gas, each increment of evaporated water causes a smaller humidity increase, leaving the gas farther from saturation. The selected margin therefore creates a finite driving force but does not by itself determine residence time.

In countercurrent operation, plot position along the solid path and position along the gas path run in opposite directions. Anchoring the operating line at the dry-solid/fresh-gas end fixes that pairing before any signs are chosen. The negative driving-force slope is a consequence of this physical pairing, not a convention that can be copied unchanged to cocurrent operation.
""")
add(19,r"""
The operative drying rate is the smaller of the externally supported wet-surface rate and the material's fitted internal-supply rate. At the crossing, both descriptions predict the same rate, so the time calculation changes branch continuously. An algebraic crossing outside the specified moisture interval does not belong to the trajectory and cannot justify adding a second time contribution.

The logarithms describe two different slow limits. Near the inlet pinch, the gas has almost no capacity to take more vapour from a wet surface. Near the fitted equilibrium endpoint, internal moisture removal becomes slow even with favourable gas. Their separate denominators show why eliminating one limitation need not eliminate the other.
""")
add(20,r"""
In the specified cocurrent case the external rate stays below the fitted internal-supply rate throughout the target interval, so a wet surface can be maintained down to the chosen endpoint. Countercurrent operation assigns different gas conditions to the same solid moisture and therefore crosses the two rates at a different point. The change in calculated regimes follows from matching local demand to local supply, not from a change in the material coefficients.

Equal ideal wet-regime times for some terminal states do not imply identical temperature histories. The hottest gas meets wet material in one arrangement and drier material in the other. Product overheating and damage therefore require the material-energy calculation even when the simplified moisture-time integrals happen to coincide.
""")
add(21,r"""
The rate family supplies the material response at a specified pair of moisture and gas driving force; the operating line selects the sequence of those pairs that this dryer actually visits. Reading all rates from one fixed-humidity curve would model a different experiment. The graphical construction is a substitution of the conservation path into the measured rate law before integration.

Taking the reciprocal before integrating matters: time accumulates as moisture removed divided by its local rate. Averaging rates first generally underweights the slow portions. The refined analytical-model table checks that numerical procedure, while uncertainty in a measured low-rate region must still be assessed separately.
""")
add(22,r"""
Adding surface heat changes both sides of the local balance. Some additional energy supports faster evaporation; some is offset by a reduced gas-to-surface temperature difference as the surface warms. Assigning all added power to extra latent heat would incorrectly hold the surface temperature and saturation humidity fixed. Assigning it all to warming would incorrectly hold evaporation fixed.

For another solvent, conservation still gives the actual bulk humidity, but its equilibrium surface counterpart must be recalculated using the local surface temperature and the appropriate saturation properties. A straight water-balance line does not guarantee a straight driving-force line when that reference itself moves.
""")
add(23,r"""
The product $D_jH_j$ combines two successive requirements: the species must enter the material and then move through it. Strong sorption increases the amount available inside the membrane to establish a gradient; high diffusivity converts that gradient into rapid transport. Comparing only molecular size misses the sorption contribution, while comparing only affinity misses mobility.

Making an ideal selective layer thinner multiplies both species' permeances by the same thickness factor, leaving their ideal selectivity unchanged. It improves throughput without automatically improving composition discrimination. Defects and support resistance can break this ideal scaling, which is why a thin material film still needs module-level verification.
""")
add(24,r"""
Recycle changes how often liquid passes the membrane, while net recovery measures how much fresh feed ultimately leaves as permeate. They answer different questions because the recycle crosses only an internal process boundary. A large circulating flow can sustain useful wall shear even when net feed and product rates are modest.

The equality of concentration ratio and VCR follows from retained solute mass staying fixed while solvent volume falls. If solute crosses the membrane, both numerator inventory and denominator volume change. The same volume reduction then produces less concentration than complete retention predicts, even if the module hydrodynamics are unchanged.
""")
add(25,r"""
At a polarised wall, the permeate is being compared with two different feed-side reference concentrations. Using the larger wall concentration makes the ratio $C_p/C_w$ smaller than $C_p/C_f$, so true rejection is larger than apparent rejection for the same permeate sample. A change in the bulk-based rejection can therefore reflect a changed boundary layer as well as a changed selective layer.

The resistance sum applies to the particular permeating component on a common equivalent-concentration basis. It does not describe retained-solute build-up by simply assigning a negative concentration drop to a resistor. Solvent convection towards an impermeable solute boundary needs its own convection–diffusion balance.
""")
add(26,r"""
The local composition appears in its own driving force: enriching the emerging permeate raises the permeate partial pressure of the preferred gas, reducing the pressure difference that caused that enrichment. Solving the quadratic makes this feedback self-consistent. Choosing a root is therefore a physical check of mole fractions and flux directions, not just an algebraic preference for the smaller numerical root.

The downstream example remains enriched relative to its local retentate while being poorer than the original feed. Selectivity is acting at each patch on the composition it receives; it does not guarantee that every downstream permeate patch exceeds the original inlet composition. Collected product purity needs the weighted combination of all patches.
""")
add(27,r"""
There are two averages to establish, with different weights. Collected permeate composition is weighted by how much gas each patch produces. The area calculation is weighted by how much area is needed to transfer each increment at its local flux. Replacing both by endpoint arithmetic means imposes two separate approximations, so correcting the flux average alone cannot make the whole calculation exact.

The reference-volume convention allows the total-flow and oxygen-flow balances to share the same amount basis. Compression changes the operating volume of that gas, but not its number of moles. Using actual volumes from opposite pressure sides without conversion would violate the very component balance used to estimate stage cut.
""")
add(28,r"""
The product derivative $d(Qx)=Q\,dx+x\,dQ$ retains both ways the feed-side oxygen inventory decreases: its concentration falls and the total flow carrying it shrinks. Omitting the second term would treat the membrane like a dilute absorber with constant total gas flow, although a substantial fraction of the whole gas stream is being removed.

The collected-composition balance is an inventory sum over all preceding patches, whereas the local composition controls the next transported increment under the stated support-mixing model. Keeping those roles distinct explains why the collected curve lies above the downstream local curve and why neither curve can simply replace the other in a partial-pressure law.
""")
add(29,r"""
Collecting the two $C_p$ terms recognises that the permeate concentration affects both solute back-diffusion and the amount carried away by solvent. A larger solvent flux dilutes the arriving solute, lowering $C_p$; that lower $C_p$ in turn increases the diffusive concentration difference. The solved expression includes both effects instead of assuming solute flux stays fixed as pressure changes.

The ratio $J_V/K_{O,B}$ is useful because it compares the capacity for solvent dilution with solute transport on compatible velocity scales. The result predicts rejection only for its stated linear bulk-to-permeate model. A wall layer that changes with pressure changes the solute driving force and the solvent osmotic penalty together.
""")
add(30,r"""
At complete rejection, solvent convection still carries solute towards the wall even though no solute can leave through it. Steady operation requires an equal diffusive return flux. A steeper concentration profile supplies that return flux, so wall enrichment is the mechanism that establishes the steady film balance, rather than evidence that the membrane has started passing all the retained material.

The exponential appears because convection is proportional to the local concentration while diffusion is proportional to its gradient. Increasing flux at fixed film coefficient therefore increases wall concentration multiplicatively. Raising crossflow instead increases the film coefficient, so a smaller wall-to-bulk concentration difference can return the same retained-solute load.
""")
add(31,r"""
The pressure correction and activity term describe opposing contributions to the same solvent chemical potential. At osmotic equilibrium they cancel, although the solutions on the two sides still have different concentrations and pressures. Zero net water flow therefore does not require identical states on each side.

For reverse osmosis, the imposed pressure must first cancel that activity-related difference before any excess is available to drive water through hydraulic resistance. High permeance reduces the pressure needed for a specified additional flow; it cannot remove the equilibrium threshold. The relevant threshold uses both transporting interfaces, including wall enrichment and any permeate solute.
""")
add(32,r"""
Parametrising by flux follows the causal chain cleanly: chosen water flow determines retained-protein delivery; the film balance determines wall concentration; the osmotic relation then determines the thermodynamic pressure penalty. Adding the hydraulic pressure drop gives the total required pressure. Guessing wall concentration independently would generally violate one of those linked balances.

The increasing curvature of the pressure–flux relation means that equal extra pressure increments produce progressively smaller flux gains. Wall concentration grows exponentially with the chosen flux, and the measured osmotic pressure grows strongly with wall concentration. The gel endpoint introduces a further physical constraint; it is not a licence to extrapolate the clean-membrane permeance indefinitely.
""")
add(33,r"""
The reduced local solution is useful because both salt inventory and wall polarisation are satisfied for each trial flux before the water-pressure residual is checked. Solute flux is not an independently specified permeate concentration: salt crossing through the membrane must equal salt carried out by the water. This coupling is why a high water flux can alter product quality as well as productivity.

Feed-and-bleed operation changes the concentration entering the module as well as its velocity. A larger recycle can improve mass transfer, but the overall salt balance still sets what concentration is required to discharge the retained salt in the net bleed. Recycle cannot make that retained salt disappear or evade the associated osmotic load.
""")
add(34,r"""
Constant rejection specifies the fraction of the local feed concentration appearing in each new permeate increment. It does not specify one constant permeate concentration along the whole module: the feed becomes more concentrated as water leaves. The collected permeate is therefore a flow-weighted mixture, while the final local permeate is associated only with the most concentrated end.

The area integral divides each additional permeate increment by its own local flux. Downstream osmotic opposition makes those increments more costly in area. The example's integer-module difference is a consequence of an equipment threshold lying between two close area estimates; it is not evidence that numerical refinement creates a physical operating margin.
""")
add(35,r"""
A cycle uses a difference between inventories, not the maximum inventory alone. A material can load strongly under feed conditions yet retain nearly as much under the available regeneration conditions, leaving little capacity for the next cycle. Selective capture and useful release must therefore be assessed as a pair of operating states.

The equilibrium difference is still an upper opportunity, not a guarantee of throughput. Finite loading and regeneration times determine how much of that difference is reached before switching. Transport can leave capacity inaccessible even when the isotherm predicts room for more solute.
""")
add(36,r"""
The Langmuir denominator records competition for a finite set of empty sites. At low concentration most sites remain available, so arrival rate can rise nearly proportionally with concentration. As occupancy grows, increasing arrival pressure cannot create new sites, and the incremental loading becomes small. This is why a high-pressure loading close to capacity need not double when pressure doubles.

The reciprocal plot exposes parameters by separating the original rational expression into a slope term and intercept. That algebra does not preserve the measurement-error structure: a small uncertainty in a low loading becomes a large uncertainty in its reciprocal. The plot is useful for interpretation, while a quantitative fit must respect the actual data uncertainties.
""")
add(37,r"""
In a closed batch, uptake changes both sides of the driving force. Liquid concentration falls as the adsorbent loads; meanwhile the fluid concentration in equilibrium with that increasing loading rises. Their difference narrows from both directions. A model with a fixed target loading omits the first feedback unless an external reservoir maintains the surrounding concentration.

Improving stirring primarily changes the path through the external film, whereas changing particle size also changes internal diffusion distance. A faster initial uptake after stirring therefore identifies a rate effect, not additional equilibrium capacity. Distinguishing those experiments helps choose whether more mixing or more accessible adsorbent is useful.
""")
add(38,r"""
The final liquid concentration appears inside the isotherm because adsorption and depletion proceed together. Evaluating solid capacity at the original feed concentration assumes the liquid remains rich even after removing its solute. Solving for the intersection instead enforces that the final solid loading is sustainable at the liquid concentration actually left behind.

The negative algebraic root fails before any kinetic question arises: it implies negative fluid inventory. Checking the positive root against the original, uncleared balance also confirms that clearing the isotherm denominator has not introduced an inadmissible state. Time to reach that root remains a separate transport calculation.
""")
add(39,r"""
The outlet fraction is the part of the entering solute load that escapes at each instant. Its complement therefore counts the captured part of that instant's feed. Integrating that complement multiplies an input mass rate by a capacity-equivalent time; it is an inventory construction, not merely a convenient area on a graph.

A low breakthrough limit stops operation while the leading part of the mass-transfer zone is only beginning to leave the bed. Capacity within the downstream mass-transfer zone remains partly unused, even though the bed would capture more solute if poor outlet quality were allowed. Earlier breakthrough can therefore reflect a broader front as well as less total adsorbent capacity.
""")
add(40,r"""
Both swing pressures matter relative to the isotherm's bend. If loading and regeneration lie on the nearly saturated plateau, a large pressure change can leave both loadings almost equal. Moving regeneration into the responsive lower-pressure region creates a larger capacity difference. Strong affinity is consequently useful only when the available regeneration conditions can move loading far enough back down the isotherm.

Reducing total pressure lowers solute partial pressure only in combination with the gas composition; purge changes that composition too. The cycle calculation must then debit the product spent on purge and allow the bed to return to loading conditions. Equilibrium working capacity alone contains neither of those recovery and scheduling costs.
""")
add(41,r"""
The partition coefficient is a concentration preference, while the retention factor is an inventory ratio. More stationary-phase volume can hold more solute at the same partition coefficient and therefore increases the fraction of time the solute spends out of the moving phase. This explains why column phase ratio affects migration even without changing molecular affinity.

A narrow high peak and a broad low peak can represent the same recovered amount if their integrated detector responses are equal within calibration. Retention time describes when that amount emerges; area describes how much emerges. Neither a matching retention time nor a large peak height alone establishes both identity and quantity.
""")
add(42,r"""
Efficiency compares spreading with how far the peak has travelled in time units. The same absolute width has different significance for an early and a late peak, so width alone is not a plate number. The Gaussian width conversions allow different measurement conventions to describe the same variance; replacing total retention time by adjusted time deliberately defines a different measure.

At the van Deemter minimum, reducing the longitudinal-diffusion contribution by increasing velocity is exactly offset by the increase in transfer-lag contribution. The path-difference term does not move that optimum in this constant-coefficient model because its derivative is zero. A velocity chosen to minimise plate height need not minimise run time or pumping cost.
""")
add(43,r"""
The resolution expression rewards differential retention, not a delay common to both species. If their partitioning becomes identical, their centres coincide and improving width alone cannot create a centre difference. Changing chemistry to alter selectivity can therefore address a limitation that a longer column cannot efficiently repair.

The worked example also separates a measured definition from a convenient design approximation. Substituting both predicted widths respects their inequality; replacing both with the later width simplifies the expression but changes the result. The appropriate tolerance must be checked against actual peak shapes, especially when a small neighbouring peak could be hidden by a large tail.
""")

out=ROOT/'other/work/scratch/all-subject-explanations'
out.mkdir(parents=True,exist_ok=True)
(out/'sep-proposals.json').write_text(json.dumps(proposals,indent=2,ensure_ascii=False),encoding='utf-8')
print(f'{len(proposals)} SEP notes covered.')

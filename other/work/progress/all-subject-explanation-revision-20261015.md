# All-subject explanation revision, 15 October 2026

Applies the PDC-04 explanation standard (CLAUDE.md §3) to ET-01–43, AB-01–57, RE-01–06/RE-S3–S6 and SEP-01–43: 164 short notes. Existing complete sections (ET, AB) and canonical publisher inputs were edited in the same pass; no new grouping or merge. Numbered equations, headings and figure links are unchanged in every note.

Records: proposals and applied edits in `other/work/scratch/all-subject-explanations/<subject>-{proposals,applied}.json`; pre-revision snapshots in `before-revision/`; independent cross-reviews in `other/work/reviews/<subject>-explanation-cross-review-20261015.md`.

## Cross-review closure

Codex applied the SEP-30/39 corrections and the SEP consolidation before the session ended; RE passed with no corrections. The remaining ET-10, ET-13, AB-21 and AB-51 corrections were applied afterwards with `other/work/scripts/apply_explanation_cross_review_corrections.py` (native short note, complete section, canonical reviewed unit and reading edition together).

## Verification

- `verify_subject_explanation_revisions.py`: 164 notes; tags, headings and figure links preserved; complete sections and 93 canonical files synchronised; 43 source PDFs unchanged; links and figures resolve in both editions and after relocating the Obsidian export.
- `check_all_subject_math.mjs`: 240 files and 10,703 formulas parse in KaTeX with no errors; native and GitHub formulas match.
- No Obsidian or GitHub runtime render was opened for this revision.

## Per-note gap and change record

### Equilibrium Thermodynamics

| Note | Gap addressed | Edits |
|---|---|---|
| ET-01 | The transfer calculation does not explicitly explain why each transfer is independent or distinguish stationarity from stability. | 1 |
| ET-02 | The purpose of the Maxwell substitution and the relation of an isothermal derivative to throttling remain compressed. | 1 |
| ET-03 | The exact Euler reconstruction may look inconsistent with partial molar volumes changing during mixing. | 1 |
| ET-04 | The cancellation establishing Gibbs–Duhem and its distinction from opposite absolute deviations need a sharper explanation. | 1 |
| ET-05 | The real-minus-ideal subtraction and the role of composition held fixed in the EOS integral need linking. | 1 |
| ET-06 | Total liquid pressure and gas partial pressure are distinct, but their contrasting changes in a pressure experiment remain implicit. | 1 |
| ET-07 | Fugacity as an exponential coordinate can be confused with a rate or with absolute pressure. | 1 |
| ET-08 | A path integral and an endpoint compressibility can be mistaken for interchangeable measures. | 1 |
| ET-09 | The numerical example needs an explicit distinction between a smooth supercritical crossover and condensation. | 1 |
| ET-10 | Activity coefficient relative to ideal mixing can be mistaken for escaping tendency relative to the pure liquid. Cross-review correction: Retained unconditional attraction claims contradict the newly added excess-entropy/sign qualification. | 1 |
| ET-11 | Why the total excess energy must be differentiated rather than the molar curve alone remains easy to miss. | 1 |
| ET-12 | The multicomponent derivative minus the mixture excess term is stated without explaining its origin. | 1 |
| ET-13 | The example compares nonideal vapour enrichment with Raoult but can obscure which phase is oxygen-richer. Cross-review correction: Generic closing definition overstates the energetic interpretation beyond the Margules example. | 1 |
| ET-14 | The finite-addition example does not explain the opposing requirements of limiting slopes and measurement resolution. | 1 |
| ET-15 | The nested approximations leading to colligative behaviour need causal ordering. | 1 |
| ET-16 | Why the higher of two computed freezing temperatures is encountered first, and what remains fixed during freezing, need making explicit. | 1 |
| ET-17 | The perfect-square result and its distinct assumptions versus an empirical polynomial need an explicit algebraic purpose. | 1 |
| ET-18 | Lattice normalisation and the chain-number/segment-number distinction can be confused. | 1 |
| ET-19 | Boltzmann weighting needs a normalisation explanation, and identical dilute fits need distinguishing from identical interior stability. | 1 |
| ET-20 | Separate excess-energy contributions need linking to how complete activity coefficients combine. | 1 |
| ET-21 | Counting independent rather than all pairwise equalities and separating amounts from degrees of freedom need sharper teaching. | 1 |
| ET-22 | The pressure normalisation and composition-dependent endpoint need connecting to reverse osmosis. | 1 |
| ET-23 | The distinction between Laplace pressure and vapour-pressure enhancement, and the fixed-reservoir stability assumption, need explaining. | 1 |
| ET-24 | The different compressed phases in bubbles versus droplets and separate meanings of superheat and boiling elevation need connecting. | 1 |
| ET-25 | The lever rule derivation and why feed composition belongs to different phases at bubble/dew boundaries need linking. | 1 |
| ET-26 | Bubble versus dew normalisation and meanings of vapour pure-component versus mixture corrections need clarifying. | 1 |
| ET-27 | The two zero-slope factors can obscure why an observable homogeneous azeotrope differs from a spinodal. | 1 |
| ET-28 | Why the auxiliary ratio simplifies two coupled constants and what the fitted point really constrains need making explicit. | 1 |
| ET-29 | A hypothetical continuation can be mistaken for a physically real supercritical liquid or an arbitrary predicted solubility. | 1 |
| ET-30 | The importance of partial rather than total pressure in comparing gas feeds and solvents remains implicit. | 1 |
| ET-31 | Unit dilute-reference activity coefficient may be misread as negligible molecular interactions or high solubility. | 1 |
| ET-32 | The apparent easy flash solution needs an explicit physical experiment distinguishing it from a critical state. | 1 |
| ET-33 | Envelope crossings need connecting to conserved overall composition and changing phase compositions; reservoir application needs its limitation. | 1 |
| ET-34 | The concentration-scale change needs showing as a logarithmic constant absorbed by the reference. | 1 |
| ET-35 | Why geometric averaging and stoichiometric powers appear is compressed; mean coefficient differs from complete salt activity. | 2 |
| ET-36 | A negative mixing Gibbs energy can be mistaken for proof of homogeneous stability; common tangent is a global comparison. | 2 |
| ET-37 | Why heating changes a dimensionless interaction strength even for constant interaction energy needs distinguishing from changing interactions. | 1 |
| ET-38 | Equal activities despite very different concentrations and the separate meaning of lever-rule fractions need interpretation. | 1 |
| ET-39 | Local curvature test needs an explicit finite-versus-infinitesimal fluctuation construction. | 1 |
| ET-40 | Flux factorisation needs separating molecular mobility from thermodynamic restoring force and explaining a negative effective coefficient. | 1 |
| ET-41 | Raising a factor below one to an exponent below one can be misinterpreted as speeding diffusion generally or preventing critical slowdown. | 1 |
| ET-42 | Fixed three-phase temperature can seem incompatible with changing composition and phase amounts during boiling. | 1 |
| ET-43 | Pure vapour pressures can be confused with equal dilution or with liquid-layer amounts; equilibrium steam ratio versus operating consumption needs interpretation. | 1 |

### Advanced Biotechnology

| Note | Gap addressed | Edits |
|---|---|---|
| AB-01 | Connect chemical direction to primer orientation. | 1 |
| AB-02 | Explain ensemble correlation versus a physical hinge. | 1 |
| AB-03 | Distinguish equilibrium concentration effect from collision frequency. | 1 |
| AB-04 | Explain why step counts are more informative than GC fraction. | 1 |
| AB-05 | Explain concentration-timescale assumption and distinguish affinity from rate. | 1 |
| AB-06 | Connect water exclusion to selective one-step chemistry. | 1 |
| AB-07 | Explain logarithms and compounding using fixed quantities. | 1 |
| AB-08 | Distinguish sequence-directed assembly from successful product verification. | 1 |
| AB-09 | Explain bootstrap requirement and distinguish genetic replacement from creation of a whole cell. | 1 |
| AB-10 | Explain chromatogram coordinate mapping and mixed templates. | 1 |
| AB-11 | Connect brightness to independence of observations. | 1 |
| AB-12 | Explain why depth cannot fix an information ambiguity. | 1 |
| AB-13 | Explain overlapping k-mer constraint mechanistically. | 1 |
| AB-14 | Distinguish biological coverage and repeated passes. Qualify the comparison table to agree with the corrected distinction between random and correlated errors. | 3 |
| AB-15 | Explain random sampling versus systematic bias in prenatal example. | 1 |
| AB-16 | Explain why changing threshold shifts crossing but not valid ratios. | 1 |
| AB-17 | Explain reference normalisation as a cancellation experiment. | 1 |
| AB-18 | Interpret negative and internal control by missing mechanisms. | 1 |
| AB-19 | Explain how wash protocol selects kinetic rather than equilibrium properties. | 1 |
| AB-20 | Explain pairwise orthogonality versus cooperative assembly. | 1 |
| AB-21 | Tie annealing schedule to time-dependent kinetic competition. Cross-review correction: Absolute equilibrium claim conflicts with the added annealing-timescale qualification. | 1 |
| AB-22 | Interpret rate as encounter rate times success probability. Also distinguish kinetic protection from literal irreversibility and remove the condition-free century lifetime claim inconsistent with AB-05. | 3 |
| AB-23 | Explain folding as solvent-inclusive free energy and qualify absolute structures. | 1 |
| AB-24 | Explain electron density versus model validation. | 1 |
| AB-25 | Explain nonlocal restraints and uncertainty cause. | 1 |
| AB-26 | Explain confidence metric using concrete domain-placement experiment. | 1 |
| AB-27 | Distinguish affinity and avidity through molecular geometry. | 1 |
| AB-28 | Explain nonmonotonic engineering target for FcRn binding. | 1 |
| AB-29 | Explain mutation experiment controls and alternative mechanisms. | 1 |
| AB-30 | Explain occupancy and shared-product failure mechanism. | 1 |
| AB-31 | Explain why average oxygen alone cannot establish scale similarity. | 1 |
| AB-32 | Explain stream recovery versus purity and concentration. | 1 |
| AB-33 | Explain spatially distributed stages in continuous rotary operation. | 1 |
| AB-34 | Explain solids loading reference and avoid feed/filtrate volume conflation. | 1 |
| AB-35 | Explain equipment criteria beyond peak acceleration. | 1 |
| AB-36 | Explain terminal velocity and changing position without inertial confusion. | 1 |
| AB-37 | Explain what normalised loading fixes and when sample changes invalidate it. | 1 |
| AB-38 | Explain release, solubilisation and folding as separate operations. | 1 |
| AB-39 | Connect discrete fixed-probability pass model to exponential fit. | 1 |
| AB-40 | Explain transformed measurement errors and near-saturation sensitivity. | 1 |
| AB-41 | Explain why sequence of selective disruption steps matters. | 1 |
| AB-42 | Explain linear partition model condition and equilibrium versus mass transfer. | 1 |
| AB-43 | Explain saturation test and final-volume balance before calculation. | 1 |
| AB-44 | Explain depletion attraction by free volume rather than adhesive polymer. | 1 |
| AB-45 | Explain mass-transfer zone and dynamic capacity. | 1 |
| AB-46 | Explain selectivity versus peak broadening and column length limits. | 1 |
| AB-47 | Explain collection-cut purity/recovery using overlap. | 1 |
| AB-48 | Explain causal lag cascade and distinguish initial response from delay. | 1 |
| AB-49 | Separate promoter output mean from switching dynamics and common notation. | 1 |
| AB-50 | Teach graphical rate-plot stability with perturbation directions. | 1 |
| AB-51 | Interpret filtering relative to upstream event timescale. Cross-review correction: Pulse-smoothing statement lacked its reference regime. | 1 |
| AB-52 | Explain distributed lag versus literal fixed delay through causal sequence. | 1 |
| AB-53 | Explain resource competition via perturbation experiment. | 1 |
| AB-54 | Explain orthogonal quality dimensions and stage yields. | 1 |
| AB-55 | Explain what complementation tests and medium-dependence establish. | 1 |
| AB-56 | Explain supply ceiling and consumption-law correction. | 1 |
| AB-57 | Explain discriminating experiments and brightness ambiguity. | 1 |

### Reaction Engineering II

| Note | Gap addressed | Edits |
|---|---|---|
| RE-01 | Rate bases alone do not explain why measured concentration change need not equal reaction rate. | 1 |
| RE-02 | Levenspiel geometry and example need causal interpretation of incremental sizing and divergent completion. | 1 |
| RE-03 | Need disentangle reaction dilution and purpose of concentration-to-inlet normalisation. | 1 |
| RE-04 | Need distinguish heat-capacity flow from stored thermal capacity and energy path from kinetics. | 1 |
| RE-05 | Need physical meaning of convolution and narrower RTD at fixed total mean. | 1 |
| RE-06 | Need explain how linear reaction erases mixing sequence and how example separates it from tracer. | 1 |
| RE-S3-01 | Need connect preparation chain and acid site density to accessible activity rather than inventory. | 1 |
| RE-S3-02 | Need distinguish reversible inhibition and activity recovery; interpret geometric area at fixed mass. | 1 |
| RE-S3-03 | Need explain graph construction as material path and coolant effect on net rate. | 1 |
| RE-S3-04 | Need explain residual weighting and difference between length and time design interventions. | 1 |
| RE-S3-05 | Need turn seven-step list into coupled steady rate and distinction product exit from reactant arrival. | 1 |
| RE-S4-01 | Need explain denominator as ratio of occupancy and affinity vs capacity. | 1 |
| RE-S4-02 | Need interpret square root mechanism and competitive denominator normalisation. | 1 |
| RE-S4-03 | Need explain inferred monolayer vs actual filling and meaning linearisation. | 1 |
| RE-S4-04 | Need causal pressure curvature link and isostere control variable purpose. | 1 |
| RE-S5-01 | Need justify quasi-equilibrium net flux and squared inventory denominator beyond count. | 1 |
| RE-S5-02 | Need interpret log derivative and two-step oxide shared throughput. | 1 |
| RE-S6-01 | Need explain porosity gradient convention and pressure limit of serial collision transport. | 1 |
| RE-S6-02 | Need explain normalisation/geometry and flux effectiveness physical conservation. | 1 |
| RE-S6-03 | Need explain multiplication C prime integration rationale and resistance interpretation. | 1 |
| RE-S6-04 | Need connect Prater elimination to independence kinetics and explain stability perturbed causal sequence. | 1 |

### Separations II

| Note | Gap addressed | Edits |
|---|---|---|
| SEP-01 | Read the operating and equilibrium lines as answers to two different questions. The operating line asks where transferred solute must go to conserve material. The equilibrium line asks which two leaving compositions can coexist without further net transfer. Neither relation supplies a rate. In continuous contact, the gap between them supplies the local driving force; the equipment must supply enough area for finite transfer across that gap. | 1 |
| SEP-02 | Follow a gas parcel through each device. Packing presents a succession of liquid films and renewed interfaces along its path. A tray bubbles the gas through a locally retained liquid pool before the gas advances to the next tray. Both need an interface and a route for the other phase to leave. A support, distributor, weir or downcomer therefore helps establish the flow pattern on which the separation model depends; it is not an accessory that can be omitted after calculating area. | 1 |
| SEP-03 | The density factors are a change of coordinates, not an extra equilibrium effect. At unchanged physical equilibrium, multiply each mole fraction by its phase's total molar density to recover the two concentrations. Substitution then guarantees that all four Henry conventions predict the same pair of physical states. Checking that pair is more informative than comparing the numerical constants in isolation. | 1 |
| SEP-04 | The liquid flow changes how quickly solvent becomes loaded as solute is removed from the gas. For fixed gas removal, more solvent shares the transferred solute over more liquid, lowering its outlet concentration. The equilibrium gas concentration over that liquid is then lower, preserving a larger absorption driving force. This is why solvent flow affects height even though the total solute-removal duty is already fixed by the gas specifications. | 1 |
| SEP-05 | The electrical-resistance analogy concerns a common flux and additive driving-force drops. The two physical concentration drops cannot be added directly because they belong to different phases. Multiplying the liquid drop by the partition coefficient expresses its consequence on the gas basis; only then do the interfacial terms cancel. The analogy does not require gas and liquid concentrations to be continuous at the interface. | 1 |
| SEP-06 | The inferred film thickness is the diffusion distance that would reproduce the measured resistance under this model. Keeping that distance fixed while changing solute leaves diffusivity as the only changing factor in $k=D/\delta$, explaining the proportional extrapolation. A different diffusivity exponent in another model represents a different account of exposure and renewal, rather than a unit conversion error. | 1 |
| SEP-07 | Rearranging the slice balance for $dz$ asks how much additional height is needed to remove a specified small composition increment. The required height is inversely proportional to the local driving force: a narrow gap costs more height for the same decrement in gas composition. Integrating adds those unequal costs rather than assuming that every part of the bed works at its inlet rate. | 1 |
| SEP-08 | The logarithm comes from integrating the reciprocal of a linearly changing driving force. A small-force end is expensive because the reciprocal weights it strongly, so an arithmetic average of the endpoint forces gives too much credit to the favourable end. The log mean packages that exact integral into one effective force for the linear case; it is not a preferred average chosen independently of the balance. | 1 |
| SEP-09 | One ideal stage imposes equilibrium on leaving streams, which converts the gap from one stage to the next by a multiplicative factor. Continuous contacting instead integrates a local rate over a continuously varying gap. The logarithm of the stage factor and the continuous driving-force integral therefore produce different dimensionless counts even for the same specified separation. | 1 |
| SEP-10 | At fixed total gas flow, reducing cross-section increases superficial velocity and hence the gas's opposition to liquid drainage. Greater liquid holdup then narrows the remaining gas passages, which raises resistance further. This feedback explains the sharp upward turn near flooding: a low-loading pressure-drop power law cannot represent a geometry that is progressively filling with liquid. | 1 |
| SEP-11 | The calculation deliberately uses equilibrium twice for different purposes. First, equilibrium with the entering gas defines a limiting liquid loading and hence a minimum solvent flow. After selecting an actual flow, the operating balance supplies the actual liquid loading at each location. Only then does equilibrium supply the hypothetical gas counterpart used to calculate the local driving force. Substituting the pinch loading as the actual outlet would undo the chosen margin above minimum flow. | 1 |
| SEP-12 | Dry-basis accounting removes a moving denominator. Evaporating liquid changes the wet product mass, so a decrease in wet-basis moisture combines a change of liquid inventory with a change in the reference mass. Dividing by the conserved dry solid isolates the inventory that is actually being removed. This is why the dry-basis moisture difference can be multiplied directly by dry-solid mass. | 1 |
| SEP-13 | At fixed pressure and humidity, the vapour-to-carrier mole ratio and thus vapour partial pressure stay fixed during sensible heating. Saturation pressure rises with temperature, so relative humidity falls even though no water has left the gas. The gas becomes more capable of accepting water because its equilibrium endpoint has moved, not because heating has reduced its existing vapour inventory. | 1 |
| SEP-14 | Per kilogram of dry gas, evaporation increases the latent contribution to gas enthalpy while reducing its sensible-temperature contribution. A falling temperature can therefore accompany an almost unchanged total enthalpy. The word adiabatic refers to heat crossing the chosen boundary; the inlet hot gas already brings energy and the added liquid brings its own enthalpy. | 1 |
| SEP-15 | Dew point is an endpoint determined by the vapour already present. Two unsaturated gas samples at different initial temperatures but the same humidity and pressure have the same dew point; they need different sensible-cooling duties to reach it. Increasing their initial temperature changes that duty without changing the first-condensation condition. | 1 |
| SEP-16 | The surface temperature is selected by competing rates. If it falls, the temperature difference supplying heat grows, while its saturation humidity falls and reduces evaporation demand. If it rises, the opposite changes occur. Their intersection fixes the steady wet-bulb temperature; it is not the saturation temperature of the unchanged bulk humidity. | 1 |
| SEP-17 | Critical moisture marks a mismatch of rates: internal liquid supply can no longer support the evaporation demanded by the gas at a fully wet surface. Raising external demand can cause that mismatch earlier even in unchanged material. Equilibrium moisture answers a different question: how much liquid remains when there is no net thermodynamic driving force under the specified gas conditions. | 1 |
| SEP-18 | The minimum gas ratio follows from water-carrying capacity, while the actual ratio sets the local humidity rise per unit water picked up. With more dry gas, each increment of evaporated water causes a smaller humidity increase, leaving the gas farther from saturation. The selected margin therefore creates a finite driving force but does not by itself determine residence time. | 1 |
| SEP-19 | The operative drying rate is the smaller of the externally supported wet-surface rate and the material's fitted internal-supply rate. At the crossing, both descriptions predict the same rate, so the time calculation changes branch continuously. An algebraic crossing outside the specified moisture interval does not belong to the trajectory and cannot justify adding a second time contribution. | 1 |
| SEP-20 | In the specified cocurrent case the external rate stays below the fitted internal-supply rate throughout the target interval, so a wet surface can be maintained down to the chosen endpoint. Countercurrent operation assigns different gas conditions to the same solid moisture and therefore crosses the two rates at a different point. The change in calculated regimes follows from matching local demand to local supply, not from a change in the material coefficients. | 1 |
| SEP-21 | The rate family supplies the material response at a specified pair of moisture and gas driving force; the operating line selects the sequence of those pairs that this dryer actually visits. Reading all rates from one fixed-humidity curve would model a different experiment. The graphical construction is a substitution of the conservation path into the measured rate law before integration. | 1 |
| SEP-22 | Adding surface heat changes both sides of the local balance. Some additional energy supports faster evaporation; some is offset by a reduced gas-to-surface temperature difference as the surface warms. Assigning all added power to extra latent heat would incorrectly hold the surface temperature and saturation humidity fixed. Assigning it all to warming would incorrectly hold evaporation fixed. | 1 |
| SEP-23 | The product $D_jH_j$ combines two successive requirements: the species must enter the material and then move through it. Strong sorption increases the amount available inside the membrane to establish a gradient; high diffusivity converts that gradient into rapid transport. Comparing only molecular size misses the sorption contribution, while comparing only affinity misses mobility. | 1 |
| SEP-24 | Recycle changes how often liquid passes the membrane, while net recovery measures how much fresh feed ultimately leaves as permeate. They answer different questions because the recycle crosses only an internal process boundary. A large circulating flow can sustain useful wall shear even when net feed and product rates are modest. | 1 |
| SEP-25 | At a polarised wall, the permeate is being compared with two different feed-side reference concentrations. Using the larger wall concentration makes the ratio $C_p/C_w$ smaller than $C_p/C_f$, so true rejection is larger than apparent rejection for the same permeate sample. A change in the bulk-based rejection can therefore reflect a changed boundary layer as well as a changed selective layer. | 1 |
| SEP-26 | The local composition appears in its own driving force: enriching the emerging permeate raises the permeate partial pressure of the preferred gas, reducing the pressure difference that caused that enrichment. Solving the quadratic makes this feedback self-consistent. Choosing a root is therefore a physical check of mole fractions and flux directions, not just an algebraic preference for the smaller numerical root. | 1 |
| SEP-27 | There are two averages to establish, with different weights. Collected permeate composition is weighted by how much gas each patch produces. The area calculation is weighted by how much area is needed to transfer each increment at its local flux. Replacing both by endpoint arithmetic means imposes two separate approximations, so correcting the flux average alone cannot make the whole calculation exact. | 1 |
| SEP-28 | The product derivative $d(Qx)=Q\,dx+x\,dQ$ retains both ways the feed-side oxygen inventory decreases: its concentration falls and the total flow carrying it shrinks. Omitting the second term would treat the membrane like a dilute absorber with constant total gas flow, although a substantial fraction of the whole gas stream is being removed. | 1 |
| SEP-29 | Collecting the two $C_p$ terms recognises that the permeate concentration affects both solute back-diffusion and the amount carried away by solvent. A larger solvent flux dilutes the arriving solute, lowering $C_p$; that lower $C_p$ in turn increases the diffusive concentration difference. The solved expression includes both effects instead of assuming solute flux stays fixed as pressure changes. | 1 |
| SEP-30 | At complete rejection, solvent convection still carries solute towards the wall even though no solute can leave through it. Steady operation requires an equal diffusive return flux. A steeper concentration profile supplies that return flux, so wall enrichment is the mechanism that establishes the steady film balance, rather than evidence that the membrane has started passing all the retained material. | 1 |
| SEP-31 | The pressure correction and activity term describe opposing contributions to the same solvent chemical potential. At osmotic equilibrium they cancel, although the solutions on the two sides still have different concentrations and pressures. Zero net water flow therefore does not require identical states on each side. | 1 |
| SEP-32 | Parametrising by flux follows the causal chain cleanly: chosen water flow determines retained-protein delivery; the film balance determines wall concentration; the osmotic relation then determines the thermodynamic pressure penalty. Adding the hydraulic pressure drop gives the total required pressure. Guessing wall concentration independently would generally violate one of those linked balances. | 1 |
| SEP-33 | The reduced local solution is useful because both salt inventory and wall polarisation are satisfied for each trial flux before the water-pressure residual is checked. Solute flux is not an independently specified permeate concentration: salt crossing through the membrane must equal salt carried out by the water. This coupling is why a high water flux can alter product quality as well as productivity. | 1 |
| SEP-34 | Constant rejection specifies the fraction of the local feed concentration appearing in each new permeate increment. It does not specify one constant permeate concentration along the whole module: the feed becomes more concentrated as water leaves. The collected permeate is therefore a flow-weighted mixture, while the final local permeate is associated only with the most concentrated end. | 1 |
| SEP-35 | A cycle uses a difference between inventories, not the maximum inventory alone. A material can load strongly under feed conditions yet retain nearly as much under the available regeneration conditions, leaving little capacity for the next cycle. Selective capture and useful release must therefore be assessed as a pair of operating states. | 1 |
| SEP-36 | The Langmuir denominator records competition for a finite set of empty sites. At low concentration most sites remain available, so arrival rate can rise nearly proportionally with concentration. As occupancy grows, increasing arrival pressure cannot create new sites, and the incremental loading becomes small. This is why a high-pressure loading close to capacity need not double when pressure doubles. | 1 |
| SEP-37 | In a closed batch, uptake changes both sides of the driving force. Liquid concentration falls as the adsorbent loads; meanwhile the fluid concentration in equilibrium with that increasing loading rises. Their difference narrows from both directions. A model with a fixed target loading omits the first feedback unless an external reservoir maintains the surrounding concentration. | 1 |
| SEP-38 | The final liquid concentration appears inside the isotherm because adsorption and depletion proceed together. Evaluating solid capacity at the original feed concentration assumes the liquid remains rich even after removing its solute. Solving for the intersection instead enforces that the final solid loading is sustainable at the liquid concentration actually left behind. | 1 |
| SEP-39 | The outlet fraction is the part of the entering solute load that escapes at each instant. Its complement therefore counts the captured part of that instant's feed. Integrating that complement multiplies an input mass rate by a capacity-equivalent time; it is an inventory construction, not merely a convenient area on a graph. | 1 |
| SEP-40 | Both swing pressures matter relative to the isotherm's bend. If loading and regeneration lie on the nearly saturated plateau, a large pressure change can leave both loadings almost equal. Moving regeneration into the responsive lower-pressure region creates a larger capacity difference. Strong affinity is consequently useful only when the available regeneration conditions can move loading far enough back down the isotherm. | 1 |
| SEP-41 | The partition coefficient is a concentration preference, while the retention factor is an inventory ratio. More stationary-phase volume can hold more solute at the same partition coefficient and therefore increases the fraction of time the solute spends out of the moving phase. This explains why column phase ratio affects migration even without changing molecular affinity. | 1 |
| SEP-42 | Efficiency compares spreading with how far the peak has travelled in time units. The same absolute width has different significance for an early and a late peak, so width alone is not a plate number. The Gaussian width conversions allow different measurement conventions to describe the same variance; replacing total retention time by adjusted time deliberately defines a different measure. | 1 |
| SEP-43 | The resolution expression rewards differential retention, not a delay common to both species. If their partitioning becomes identical, their centres coincide and improving width alone cannot create a centre difference. Changing chemistry to alter selectivity can therefore address a limitation that a longer column cannot efficiently repair. | 1 |

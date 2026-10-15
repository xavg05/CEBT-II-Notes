from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'other/obsidian/CEBT-II Notes/Equilibrium Thermodynamics'
specs = []

def propose(number, gap, anchor, addition):
    specs.append((number, gap, anchor, addition))

propose(1, 'The transfer calculation does not explicitly explain why each transfer is independent or distinguish stationarity from stability.',
        '**Step 4: equilibrium and direction.', r'''The important choice in (4) is to transfer just one component while conserving its total amount. Such a transfer can be made in either direction, independently of transfers of the other components. If its coefficient were non-zero, one direction would lower $G$, so the state could not be an equilibrium minimum. This is why each chemical potential must match separately; a cancellation between transfers of different components would not suffice.

Equality removes the immediate driving force, but it is a stationary-state condition. To establish stable equilibrium, the state must also have the lowest accessible $G$. The supercooled-water example illustrates the distinction: the bulk free-energy advantage determines which phase wins, while creating an interface can delay its appearance.''')

propose(2, 'The purpose of the Maxwell substitution and the relation of an isothermal derivative to throttling remain compressed.',
        '*Reason:* the right side contains only', r'''The substitution does more than remove an inconvenient symbol. An EOS measures how the fluid expands when heated at fixed pressure; the Maxwell relation turns that measurable response into the entropy change on compression. Equation (8) combines that entropy contribution with the direct $\underline{V}\,dP$ contribution to enthalpy. Their exact cancellation for an ideal gas explains why its enthalpy depends only on temperature.

For throttling, pressure and temperature change together while enthalpy stays fixed: $0=\underline{C}_P\,dT+(\partial\underline{H}/\partial P)_T\,dP$. With positive $\underline{C}_P$, a negative pressure derivative therefore makes a pressure decrease accompany a temperature decrease. This connects the sign in the departure calculation to cooling without treating the throttle itself as isothermal.''')

propose(3, 'The exact Euler reconstruction may look inconsistent with partial molar volumes changing during mixing.',
        '*Reason:* dividing by $n$ gives the molar form.', r'''Equation (13) uses all the partial molar volumes at the *final mixture composition*. It does not say that ethanol and water carry fixed parcels of volume from their pure states into the bottle. Adding ethanol changes the surroundings of water as well as those of ethanol; the measured total volume includes that collective rearrangement. The derivative assigns its net effect to the increment being added.

That is why the bottle calculation first finds composition from the amounts in the recipe, then reads both partial molar volumes at that composition, and only then reconstructs the final volume. Using pure volumes in the last step would erase the very change in molecular surroundings that the graph measures.''')

propose(4, 'The cancellation establishing Gibbs–Duhem and its distinction from opposite absolute deviations need a sharper explanation.',
        'This is the Gibbs–Duhem equation.', r'''The cancellation has a useful meaning. Changing amounts already contributes $\sum_i\mu_i\,dn_i$ to $dG$ through the fundamental relation. Differentiating $G=\sum_i n_i\mu_i$ appears to add a second contribution because the chemical potentials also change. At fixed $T$ and $P$, that extra weighted contribution must cancel. Gibbs–Duhem prevents the same change in mixture Gibbs energy from being counted twice.

It constrains slopes along a composition change, not the signs of departures from the pure liquids. Both partial molar volumes can therefore be below their pure values in the bottle example, even though their composition derivatives have opposite signs. Recovering one component's curve from the other also needs a reference value, normally the known pure-component endpoint, to fix the integration constant.''')

propose(5, 'The real-minus-ideal subtraction and the role of composition held fixed in the EOS integral need linking.',
        'The first two terms are the ideal-gas-mixture value.', r'''The subtraction is made between two fluids at the same temperature, pressure and composition. It removes only the effect of intermolecular interactions, leaving the entropy of mixing in the ideal reference. Holding composition fixed along the integration path matters: otherwise $\mu_i$ would change because both pressure and the molecular environment were changing, and the pressure integral alone would miss part of that change.

In the bottle example, volume contraction tests the *pressure derivative* of the chemical-potential model. It establishes non-ideality, but it does not determine the whole Gibbs-energy correction at one pressure. A function's slope cannot fix its value without a reference; activity measurements supply the additional information.''')

propose(6, 'Total liquid pressure and gas partial pressure are distinct, but their contrasting changes in a pressure experiment remain implicit.',
        '**Step 4: equate chemical potentials.', r'''Imagine adding more insoluble gas while keeping temperature fixed and liquid present. The liquid feels the higher *total* pressure, so its chemical potential rises. In the ideal gas mixture, however, water responds to its own *partial* pressure. Equilibrium requires that partial pressure to rise just enough to match the liquid-side increase. The water mole fraction can nevertheless fall, because the total gas pressure is increasing much more strongly.

Thus a higher equilibrium water partial pressure does not mean a larger fraction of water in the gas. The Poynting factor answers the former question. To obtain the fraction, divide the resulting $P^{\mathrm{VAP}}$ by the specified total pressure.''')

propose(7, 'Fugacity as an exponential coordinate can be confused with a rate or with absolute pressure.',
        '**Direction.**', r'''To see why a pressure-like ratio gives the driving force, write (39) for water in each phase and subtract. The identical ideal-gas reference cancels, leaving $\mu^{l}-\mu^{v}=RT\ln(f^{l}/\bar f_w^{v})$. A ratio above unity gives evaporation, a ratio below unity gives condensation, and unity gives no net transfer. The absolute size of either fugacity is less informative than this comparison.

The humidity example therefore establishes the direction and thermodynamic incentive for transfer. It does not give an evaporation rate: that also needs transport through the gas next to the surface and the heat needed to sustain evaporation. Equal fugacities describe the endpoint, not how quickly it is reached.''')

propose(8, 'A path integral and an endpoint compressibility can be mistaken for interchangeable measures.',
        r'**What $\phi$ measures.**', r'''One way to read (47) is to build the correction in small pressure increments. Wherever $Z<1$, the next increment lowers $\ln\phi$; wherever $Z>1$, it raises it. Repulsion can make $Z$ exceed unity near the final pressure while the negative area accumulated earlier still leaves $\phi<1$. Conversely, $Z=1$ at one pressure makes only the local slope vanish; it does not force $\phi=1$.

This is why the nitrogen example integrates the virial expansion rather than simply setting $\phi=Z$. Each pressure power acquires its own integration factor, so adding a term changes the accumulated Gibbs-energy correction differently from the local EOS volume.''')

propose(9, 'The numerical example needs an explicit distinction between a smooth supercritical crossover and condensation.',
        'The integrand is no longer constant.', r'''The sharp volume change in this table is a continuous crossover along a supercritical isotherm, not a liquid–vapour phase transition. There is no saturation plateau or latent-heat jump to insert into the integration. The numerical task is to resolve a rapidly varying but continuous volume departure.

The comparison of $Z$ and $\phi$ then tests two different things: $Z$ tests the volume at the final state, while $\phi$ tests an area accumulated over all lower pressures. A local density error can occupy a small part of that area, or be offset by errors elsewhere. Agreement in fugacity therefore supports an equilibrium calculation without establishing equal accuracy for density-dependent equipment sizing.''')

propose(10, 'Activity coefficient relative to ideal mixing can be mistaken for escaping tendency relative to the pure liquid.',
        '**Step 4: link to fugacity.**', r'''There are two comparisons in (57). The factor $x_i$ measures dilution relative to pure liquid $i$, whereas $\gamma_i$ measures the extra change relative to an *ideal mixture at that dilution*. Consequently, $\gamma_i>1$ does not by itself mean the component escapes more readily than from its pure liquid: the full ratio is $\bar f_i/f_i=x_i\gamma_i$.

Likewise, a heat or volume of mixing diagnoses a departure from ideality but does not alone give $\gamma_i$ at one temperature and pressure. It constrains a derivative of the excess Gibbs energy. Activity coefficients contain both energetic and entropic effects, so a molecular-attraction picture is useful intuition rather than a unique inference from the sign of $\gamma_i$.''')

propose(11, 'Why the total excess energy must be differentiated rather than the molar curve alone remains easy to miss.',
        '**Step 3: activity coefficients from any', r'''The differentiation must act on the *total* excess Gibbs energy, $ng(x_1)$, because adding a mole both increases the system's size and changes its composition. The product rule accounts for the extra amount through $g$; the chain rule accounts for the changed environment through the derivative term. Differentiating $g$ alone would keep only the second effect and would not give a partial molar property.

For Margules, unlike contacts disappear at either pure endpoint, so $g$ vanishes there. Yet inserting one trace molecule into the other pure liquid creates unlike contacts immediately, so the derivative, and hence its infinite-dilution excess chemical potential, can remain finite. Zero mixture excess energy at a pure endpoint does not require zero dilute-solute non-ideality.''')

propose(12, 'The multicomponent derivative minus the mixture excess term is stated without explaining its origin.',
        '**Step 5: multicomponent mixtures.**', r'''The denominator $n$ in $\sum_{i<j}A_{ij}n_in_j/n$ changes when $n_k$ is increased. Differentiating the numerator gives the interactions involving the added component; differentiating $1/n$ gives the common subtraction $-\underline{G}^{ex}$ in (69). It represents the dilution of the existing pair contributions as the total amount grows. Treating the mole fractions as independent constants during this derivative would miss it.

The pairwise assumption is a separate choice from thermodynamic consistency. Differentiating one total Gibbs-energy function guarantees consistency, but it cannot prove that binary parameters capture how a third component changes the local environment. The binary limit checks the algebra; multicomponent measurements test that physical assumption.''')

propose(13, 'The example compares nonideal vapour enrichment with Raoult but can obscure which phase is oxygen-richer.',
        'The liquid boils at a 4 % higher pressure', r'''There are two different baselines here. The vapour is richer in oxygen than the *Raoult prediction*, because oxygen receives the larger activity-coefficient correction. It is still poorer in oxygen than the liquid itself: the reported $y_1$ is below the specified $x_1$. Argon remains the more volatile component under these conditions.

The reason is that vapour composition depends on both components' partial pressures, not only oxygen's $\gamma_1$. Adding the two contributions first determines the bubble pressure; dividing oxygen's contribution by that total then determines $y_1$. A larger activity coefficient is therefore not, by itself, a ranking of volatility between different substances.''')

propose(14, 'The finite-addition example does not explain the opposing requirements of limiting slopes and measurement resolution.',
        '**Sensitivity.**', r'''Making the addition smaller brings the chord closer to the desired tangent, reducing the bias from curvature. It also makes the pressure change smaller, so the same absolute pressure error becomes a larger error in $\Delta P/\Delta x_1$. The two rows demonstrate the first improvement; the sensitivity calculation exposes its experimental cost.

The subtraction of $P_2^{\mathrm{SAT}}$ in (76) is physically essential. Adding solute replaces some solvent as well as contributing its own vapour. The measured slope is therefore a *difference* of escaping tendencies, and it can be small even when neither contribution is small. Extracting a dilute activity coefficient from that small difference requires precision rather than merely a large measured total pressure.''')

propose(15, 'The nested approximations leading to colligative behaviour need causal ordering.',
        '**Step 7: dilute ideal limit.**', r'''Two separate simplifications produce the straight-line cryoscopic law. A small temperature shift linearises the pure-solvent solid–liquid free-energy difference. A dilute solution then linearises $-\ln x_1$ in the solute amount. Gibbs–Duhem makes the solvent's activity-coefficient correction higher order near the pure-solvent endpoint, which is why the leading result counts particles rather than their chemistry.

The worked comparison changes neither the pure-solvent data nor the ideality assumption: it changes these linearisations. Its discrepancy therefore isolates approximation error, rather than demonstrating a non-ideal solute. At larger depression, retaining the reciprocal-temperature and logarithmic forms is the first improvement; a heat-capacity correction addresses a different approximation in the pure-solvent reference.''')

propose(16, 'Why the higher of two computed freezing temperatures is encountered first, and what remains fixed during freezing, need making explicit.',
        'The real mixture freezes at about', r'''Cooling starts from above both candidate freezing temperatures, so the *higher* branch is encountered first. Once ice appears, it removes water without removing glycol. The overall composition of the closed sample is unchanged, but the remaining liquid becomes glycol-richer and follows the ice branch towards the eutectic. A vertical cooling path for the whole sample is therefore not a constant-composition path for its liquid phase.

Equation (86) finds where one liquid composition can simultaneously satisfy both pure-solid equilibrium conditions. Above that intersection only one solid is stable against the liquid at a time; at the intersection both can coexist. The measured first-freezing point of the water-rich mixture constrains water activity on the ice branch, rather than locating the eutectic of the real system.''')

propose(17, 'The perfect-square result and its distinct assumptions versus an empirical polynomial need an explicit algebraic purpose.',
        '(the last step is algebra, checked symbolically).', r'''Putting the three energy terms in (90) over the common denominator $x_1b_1+x_2b_2$ cancels the pure-component contributions. What remains is proportional to $x_1x_2$: only replacing like contacts by unlike contacts can create an excess. Factoring the remaining quadratic as a square exposes a strong prediction of the geometric-mean rule: that replacement cannot lower the energy of mixing.

When the two cohesive energy densities match, the square vanishes even if the molecules have different volumes. RST then predicts no energetic departure; it has not shown that every real size-dependent or orientational effect vanishes. The separate entropy correction in the next model addresses precisely what this regular-solution assumption leaves out.''')

propose(18, 'Lattice normalisation and the chain-number/segment-number distinction can be confused.',
        '**Step 4: solvent activity.**', r'''One polymer chain adds many occupied sites but only one independently translating molecule. The lattice count keeps both facts: volume fractions describe where the sites are, while $n_2$ counts how many chains can be placed. This is why replacing every chain by the same number of free small molecules would overestimate the mixing entropy.

For the solvent derivative, adding solvent increases the total number of sites and therefore changes *both* volume fractions. These derivative contributions produce the term linear in $\phi_2$ in (98), in addition to $\ln\phi_1$ and the interaction term. Simply replacing $x_1$ by $\phi_1$ in Raoult's law would miss that rearrangement. In the equal-size limit, volume and mole fractions coincide and the extra linear term disappears.''')

propose(19, 'Boltzmann weighting needs a normalisation explanation, and identical dilute fits need distinguishing from identical interior stability.',
        '**Step 2: Wilson\'s excess Gibbs energy.**', r'''A Boltzmann factor changes a *relative* probability; it does not by itself specify a local composition. The local fractions must still sum to unity. Normalising the two possible neighbour weights is what produces denominators such as $x_1+x_2G_{21}$ in NRTL. They compare the available populations after energetic preferences have been applied, rather than adding extra neighbours to a fixed coordination shell.''')

propose(20, 'Separate excess-energy contributions need linking to how complete activity coefficients combine.',
        '**Step 3: residual (energy) part.**', r'''Because the two Gibbs-energy contributions add, their *chemical-potential* contributions add after differentiation. Thus $\ln\gamma_i=\ln\gamma_i^{C}+\ln\gamma_i^{R}$, or $\gamma_i=\gamma_i^{C}\gamma_i^{R}$. The combinatorial values in the example are factors in the full prediction, not quantities to add to an energetic activity coefficient.

Setting all residual interaction factors to unity removes chemical preferences while retaining molecular size and shape. Setting the molecular size and shape parameters equal as well removes the combinatorial distinction, recovering ideal mixing. These are different tests: chemically similar molecules can still depart from Raoult's law because their sizes differ, while similarly sized molecules can depart because their interactions differ.''')

propose(21, 'Counting independent rather than all pairwise equalities and separating amounts from degrees of freedom need sharper teaching.',
        '**Step 2: constraints from equilibrium.**', r'''Choose one phase as a reference and equate each of the others to it. That gives $P-1$ independent equalities for a given intensive quantity. Equating every possible pair would count some conditions twice: once two phases both match the reference, they already match each other. This is the reason for the factor $P-1$, rather than the number of phase pairs.

Changing a phase amount does not necessarily change any intensive state variable. Water can evaporate into steam at a fixed coexistence temperature and pressure while their amounts change. The phase rule counts which coexistence states are possible; conservation balances and any specified total volume or enthalpy determine how much of each phase occupies that state.''')

propose(22, 'The pressure normalisation and composition-dependent endpoint need connecting to reverse osmosis.',
        '**Step 5: combine with (113).**', r'''The pure-solvent reference is written at each side's actual pressure so that the pressure difference appears explicitly before the common reference is cancelled. The two remaining terms oppose one another: mixing lowers the solvent's chemical potential in the solution, and additional pressure raises it. Dividing their balance by the solvent molar volume converts an energy deficit per mole into the pressure required to cancel it.

At this pressure difference the net solvent flux is zero. Raising solution-side pressure further reverses the chemical-potential difference and drives solvent towards the pure side. During real reverse osmosis, removal of solvent concentrates the retained solute, so the opposing osmotic pressure rises. The quoted seawater threshold is therefore an initial equilibrium requirement rather than a single pressure that guarantees the same driving force throughout concentration.''')

propose(23, 'The distinction between Laplace pressure and vapour-pressure enhancement, and the fixed-reservoir stability assumption, need explaining.',
        '**Same physics as Poynting.**', r'''The large pressure in the droplet is not the vapour pressure surrounding it. It acts on a dense liquid, whose chemical potential responds through its small molar volume. The gas matches that energy change through a logarithmic change of its much smaller pressure. This explains how the table can contain a large Laplace pressure alongside only a modest relative vapour-pressure enhancement.

The critical-radius argument holds the surrounding temperature and supersaturation fixed, as if the droplet exchanges molecules with a large vapour reservoir. A slightly smaller droplet then needs a higher vapour pressure than that reservoir provides and shrinks further. In a closed vessel with appreciable condensation, the vapour inventory and supersaturation also change, so that feedback must be included before inferring the fate of the whole droplet population.''')

propose(24, 'The different compressed phases in bubbles versus droplets and separate meanings of superheat and boiling elevation need connecting.',
        'The liquid must be hot enough', r'''For a droplet, the compressed phase is liquid and the surrounding vapour changes only slightly. For a bubble, the compressed phase is vapour itself: the gas must supply the entire Laplace pressure. Raising temperature increases its saturation pressure until this mechanical requirement and chemical equilibrium can both hold. As the bubble grows, the required pressure excess falls, making further growth easier.

The salt calculation addresses a separate cause of a higher boiling temperature. Solute changes the bulk liquid's chemical potential even for a flat interface; small-radius superheat arises because forming the curved interface requires extra pressure. A nucleation site can reduce the latter while leaving the solvent-activity effect intact, which explains why the appearance of bubbles on adding salt is not a measure of the equilibrium boiling-point elevation.''')

propose(25, 'The lever rule derivation and why feed composition belongs to different phases at bubble/dew boundaries need linking.',
        'The feed point splits the tie line', r'''Eliminate $L$ using $L=1-V$ in the component balance. The remaining equation is $z_1-x_1=V(y_1-x_1)$: the feed's enrichment above the liquid composition equals the vapour fraction times the vapour–liquid composition gap. This gives the lever rule and explains why $z_1$ must lie between $x_1$ and $y_1$ whenever both phase amounts are positive.

At the bubble point, the vapour amount tends to zero, so the liquid composition equals the feed composition. At the dew point the liquid amount tends to zero, so the vapour composition equals the feed composition. That is why the same $z_i$ enters two different equations in part (a). Between these limits the feed fixes the phase amounts; it is neither phase composition.''')

propose(26, 'Bubble versus dew normalisation and meanings of vapour pure-component versus mixture corrections need clarifying.',
        'On a $P$–$x$–$y$ diagram at constant $T$', r'''A bubble calculation starts with liquid composition and sums the predicted vapour fractions to unity. A dew calculation starts with vapour composition, writes $x_i=y_iP/P_i^{\mathrm{SAT}}$, and instead sums the liquid fractions to unity. This change of which phase is known produces the reciprocal-pressure dew equation; it is not an independent equilibrium law.

The use of pure-vapour $\phi_i^{v}$ in (127) is also a modelling step. A full vapour-mixture coefficient depends on the composition of that vapour because unlike gas molecules interact. At sufficiently low density those interactions disappear and both versions approach unity. Low pressure simplifies the vapour description without requiring ideal mixing in the dense liquid.''')

propose(27, 'The two zero-slope factors can obscure why an observable homogeneous azeotrope differs from a spinodal.',
        '**Step 3: turning points.**', r'''The second factor in (132) is the thermodynamic factor: it measures whether increasing a component's concentration raises its chemical potential. For a locally stable homogeneous liquid it is positive. A pressure maximum or minimum on that stable branch must therefore come from equality of the two corrected volatilities, the first factor. Setting the second factor to zero instead reaches the limit of local stability and cannot by itself identify an ordinary homogeneous azeotrope.

At an azeotrope the liquid and vapour are still distinct phases, but transferring an equilibrium increment into the vapour does not change its composition relative to the liquid. The enrichment that drives ordinary distillation vanishes. The close-boiling example needs only a modest correction to make the two corrected volatilities equal because their uncorrected saturation pressures were already close.''')

propose(28, 'Why the auxiliary ratio simplifies two coupled constants and what the fitted point really constrains need making explicit.',
        '**Step 3: invert for the constants.**', r'''Introducing $u$ gives the two activity-coefficient equations the same denominator. Taking their ratio cancels that denominator, reducing the coupled fit to a directly calculable ratio followed by two substitutions. The choice is useful because trying to solve separately for each constant leaves the other constant inside its denominator.

Although this uses one azeotropic composition, it supplies two component conditions: each component's activity is fixed by its own saturation pressure and the common measured pressure. Those conditions determine the constants *within the chosen model*. They do not determine every possible Gibbs-energy curve, which is why matching the azeotrope exactly still leaves a substantive error at the propanal-rich test composition.''')

propose(29, 'A hypothetical continuation can be mistaken for a physically real supercritical liquid or an arbitrary predicted solubility.',
        '**Step 5: activity coefficient from measured solubility.**', r'''The hypothetical liquid is a reference for the chemical potential, not a proposed second phase above the pure solute's critical temperature. Changing its assigned fugacity changes the corresponding $\gamma_i$ inversely, leaving the measurable product $x_i\gamma_if_i^{\,l}$ unchanged. The convention is useful only when the reference and activity coefficient are used together consistently.

Accordingly, solvent-independent ideal solubility is a benchmark for that convention, not a claim that all real solvents behave alike. Measured departures from it put the solvent preference into $\gamma_i$. Henry's constant later combines the reference fugacity and dilute preference into one measurable coefficient, avoiding this hypothetical reference in routine design.''')

propose(30, 'The importance of partial rather than total pressure in comparing gas feeds and solvents remains implicit.',
        '**Step 1: vapour fugacity.**', r'''The gas supplies methane according to its partial fugacity, not according to the pressure gauge alone. In the ideal-gas approximation, increasing nitrogen at fixed methane partial pressure raises total pressure without increasing methane's dissolution driving force. Increasing total pressure at fixed gas composition does increase that force. Stating what is fixed is essential when using the example to predict the effect of pressurisation.

All three solvent measurements use the same gas-side methane fugacity and the same hypothetical-liquid reference. Their different dissolved mole fractions therefore isolate the solvent effect in $\gamma$. A common uncertainty in the chart shifts all the inferred coefficients together; it cannot account for the measured ordering of the solvents.''')

propose(31, 'Unit dilute-reference activity coefficient may be misread as negligible molecular interactions or high solubility.',
        r'So $\gamma_i^{*}\to 1$', r'''Normalising the dilute coefficient to unity does not remove the solute–solvent interactions. It puts their dilute-limit effect into $H_i$ and the corresponding standard chemical potential. A poorly soluble gas can therefore obey Henry's law very accurately while having a large Henry constant: every solute molecule experiences the same unfavourable environment, so the response is linear even though dissolution is difficult.

For the pressure-over-mole-fraction convention used here, $x_i=\bar f_i/H_i$ at fixed temperature. A larger $H_i$ means less dissolved gas at a given fugacity. Other tabulations use the reciprocal convention, so the stated units and defining relation matter as much as the name of the constant.''')

propose(32, 'The apparent easy flash solution needs an explicit physical experiment distinguishing it from a critical state.',
        '**Step 2: what happens at a mixture critical point.**', r'''A single homogeneous fluid always has the same fugacity as an identical copy of itself. That is why assigning both calculation phases the same composition and EOS root solves the equality equations without demonstrating coexistence. A meaningful two-phase calculation must first find distinct states and then test their stability and material balances.

Approaching a genuine critical point from coexistence removes those distinctions continuously: the composition gap and density gap both disappear. An azeotrope removes only the composition gap. This is why a zero-width tie line on a composition plot needs density or stability information before it can be interpreted as criticality.''')

propose(33, 'Envelope crossings need connecting to conserved overall composition and changing phase compositions; reservoir application needs its limitation.',
        'The liquid fraction along (iii)', r'''During this fixed-composition decompression, the overall ratio of light to heavy material stays fixed, but the two phase compositions do not. Near the critical region, pressure changes both the relative fugacities and the densities strongly. The phase compositions and their lever-rule amounts move together, allowing a heavy-rich liquid to appear even while the total fluid expands. Further decompression eventually favours a single gas again.

The closed-envelope path is an equilibrium experiment on a fixed feed. Producing gas from a reservoir can also change the remaining overall composition, particularly when condensed liquid is trapped. The illustrated path explains why liquid first appears; following an actual producing reservoir thereafter requires updated material balances and a changing phase envelope.''')

propose(34, 'The concentration-scale change needs showing as a logarithmic constant absorbed by the reference.',
        '**Step 3: relation between conventions.**', r'''Insert the exact relation between $x_i$ and $m_i$ into $RT\ln(\gamma_i^{*}x_i)$. The logarithm separates into a constant $RT\ln(M_sm^{\circ})$, a molality term, and the remaining composition-dependent factor. Absorb only the constant into the standard chemical potential; the composition-dependent factor belongs in $\gamma_i^{\#}$. This is the reason for the two simultaneous changes in Step 3.

The example's different activity numbers therefore express the same chemical potential measured from different reference levels. A large numerical activity on one scale is not evidence of a stronger driving force than a small activity on another scale. Compare chemical potentials, or activities expressed with the same convention, when deciding equilibrium or transfer direction.''')

propose(35, 'Why geometric averaging and stoichiometric powers appear is compressed; mean coefficient differs from complete salt activity.',
        '**Step 3: general salt.**', r'''Adding a neutral formula unit adds the cations and anions together in their stoichiometric proportions. Their chemical potentials therefore add with those same weights. Because each chemical potential contains a logarithm, adding them multiplies the ionic activities and raises them to stoichiometric powers. Taking the corresponding root defines the geometric mean $\gamma_{\pm}$; an arithmetic mean would not reproduce the salt chemical potential.

The mean coefficient is not itself the complete salt activity. The latter also contains the ion molalities and their powers, as (148) shows for NaCl. In comparing the two salts in the table, equal salt molality gives neither equal ionic strength nor equal charge factor, so both changes must be included before attributing their different non-idealities to charge alone.''')

propose(36, 'A negative mixing Gibbs energy can be mistaken for proof of homogeneous stability; common tangent is a global comparison.',
        '**Gibbs energy gain.**', r'''Both reported mixing Gibbs energies are negative relative to the unmixed *pure* liquids. Yet the two partially mixed liquids have the lower value. Mixing spontaneously from pure components therefore does not prove that one homogeneous liquid is the final state: it can be favourable to mix partially and still favourable to separate into two compositions.

The chord represents that alternative while conserving the overall composition. Its endpoints cannot be chosen merely as the nearest minima unless symmetry makes their common tangent horizontal. Minimising the phase-weighted Gibbs energy selects the common tangent, which compares the homogeneous state with all accessible two-phase combinations rather than only its immediate neighbours.''')

propose(37, 'Why heating changes a dimensionless interaction strength even for constant interaction energy needs distinguishing from changing interactions.',
        '**Step 2: curvature.**', r'''Holding $A$ fixed holds the energetic cost of unlike contacts fixed. Heating still reduces $A/RT$: thermal mixing entropy becomes more competitive even though the contact energy has not changed. The critical temperature is where the strongest tendency to lose convexity, at the symmetric composition, is just balanced by the ideal-entropy curvature.

This assumption can produce a UCST but cannot produce an LCST. In the latter case heating must increase the effective penalty for mixing, for example by removing favourable ordered interactions. A temperature-dependent fitted parameter then represents changing enthalpic and entropic contributions, rather than simply the same fixed contact penalty divided by a larger $RT$.''')

propose(38, 'Equal activities despite very different concentrations and the separate meaning of lever-rule fractions need interpretation.',
        'The equal activities confirm (156).', r'''The equality is achieved by compensation: isobutane is dilute in the furfural-rich phase, but its large activity coefficient offsets that small mole fraction. In the isobutane-rich phase, its coefficient is near unity and the mole fraction is large. Equal products mean no net transfer of isobutane even though its concentrations are very different; the same compensation holds for furfural.

The feed composition then determines the amounts of these two liquids, not new equilibrium endpoints. At the stated temperature and pressure, changing an overall composition within the miscibility gap changes the lever-rule fractions while the two phase compositions and their activities stay fixed. This separates the equilibrium calculation from the material balance used afterwards.''')

propose(39, 'Local curvature test needs an explicit finite-versus-infinitesimal fluctuation construction.',
        '**Step 3: stability criterion.**', r'''Consider dividing a homogeneous sample into equal amounts at compositions just above and below the original one. Their first-order Gibbs-energy changes cancel because the overall composition is conserved; the leading remaining change has the sign of the curvature. Positive curvature makes this small fluctuation costly, while negative curvature makes it favourable. This is why curvature tests local stability.

It does not compare the original liquid with a pair of *distant* compositions. Between binodal and spinodal, the small fluctuation costs energy even though a sufficiently developed two-phase state has lower bulk $G$. Creating an interface and reaching that distant state produces a nucleation barrier. The example's metastable and unstable liquids therefore share equilibrium endpoint compositions but follow different routes to them.''')

propose(40, 'Flux factorisation needs separating molecular mobility from thermodynamic restoring force and explaining a negative effective coefficient.',
        'The measured (Fickian) coefficient is therefore', r'''The conversion separates two questions. The mobility coefficient describes how readily molecules respond to a given chemical-potential gradient. The thermodynamic factor describes how much chemical-potential gradient a given composition gradient creates. Diffusion can therefore slow because the restoring force weakens even when molecules remain mobile.

Inside the spinodal the factor changes sign, but the mobility need not become negative: material still moves towards lower chemical potential. It runs uphill in concentration because, there, increasing concentration lowers chemical potential. Using a negative Fickian coefficient alone at arbitrarily short length scales would not describe the developing interface; the omitted gradient free energy supplies the additional physics needed for a spatial phase-separation model.''')

propose(41, 'Raising a factor below one to an exponent below one can be misinterpreted as speeding diffusion generally or preventing critical slowdown.',
        'Within 15 K of the consolute point,', r'''Every tabulated thermodynamic factor lies between zero and unity. Raising it to a power below unity therefore makes it larger, so the modified law predicts faster mutual diffusion than the linear-factor law at the *same* temperature and background coefficient. It still tends to zero as the critical point is approached. The exponent changes the rate of that approach; it does not remove critical slowing.

This comparison holds the assumed thermodynamic model and background coefficient fixed. It explains the direction of the correction in the table without treating the illustrative regular-solution values as a fresh fit to the measured data. Nor does a vanishing mutual diffusion coefficient mean molecules stop moving: it is the relaxation of a collective composition difference that becomes slow.''')

propose(42, 'Fixed three-phase temperature can seem incompatible with changing composition and phase amounts during boiling.',
        r'Any feed between $x_1^{\mathrm{I}}$', r'''The three-phase line fixes the compositions of the phases, not their amounts. Heat can convert some liquid into vapour while the amounts of the two liquid layers adjust to conserve both components. As long as both layers remain, they supply the same common activities and the same equilibrium vapour, so temperature need not rise.

Once a layer is exhausted, its equilibrium condition no longer constrains the system. There are only two phases, so an intensive freedom reappears at fixed pressure and the boiling temperature can change. The special overall composition equal to the three-phase vapour composition permits both layers to disappear together; otherwise the remaining layer carries the excess of one component into the subsequent two-phase stage.''')

propose(43, 'Pure vapour pressures can be confused with equal dilution or with liquid-layer amounts; equilibrium steam ratio versus operating consumption needs interpretation.',
        '**Step 3: total pressure and boiling temperature.**', r'''Each partial pressure is set by the liquid layer in which that component is nearly pure. The two near-unity mole fractions belong to *different* liquids, so adding the two partial pressures does not violate mole-fraction normalisation within either phase. A single homogeneous ideal mixture would dilute both components; two immiscible layers each retain almost the pure component's escaping tendency.

Changing the relative amounts of the layers therefore does not change the boiling temperature or equilibrium vapour ratio while both remain present. The mass ratio in (168) converts that vapour composition into the accompanying steam per mass of organic recovered. It does not include steam condensed to heat equipment, losses, or incomplete equilibration with plant material, so actual operating steam consumption can exceed the equilibrium co-distillation ratio.''')

out = []
for number, gap, anchor, addition in specs:
    files = list(BASE.rglob(f'ET-{number:02d} - *.md'))
    assert len(files) == 1, (number, files)
    path = files[0]
    body = path.read_text(encoding='utf-8')
    paragraphs = body.split('\n\n')
    matches = [p for p in paragraphs if p.startswith(anchor)]
    assert len(matches) == 1, (number, anchor, len(matches))
    old = matches[0]
    assert body.count(old) == 1, number
    new = old + '\n\n' + addition
    out.append({'path':path.relative_to(ROOT).as_posix(),'note':f'ET-{number:02d}', 'gap':gap,
                'edits':[{'old':old, 'new':new}]})
clarifications = {
    'ET-35': ("Even then, NaCl's activity is 3.6 % below ideal", "Even then, NaCl's mean activity coefficient is 3.6 % below unity"),
    'ET-36': ('That was the "other" root, and it signals the onset of liquid–liquid splitting.', 'That was the "other" root: it marks the spinodal, the loss of local stability of the homogeneous liquid. Equilibrium two-liquid coexistence begins at the binodal, found by the common tangent, rather than at this local-curvature boundary.'),
}
for entry in out:
    if entry['note'] in clarifications:
        old, new = clarifications[entry['note']]
        body = (ROOT / entry['path']).read_text(encoding='utf-8')
        assert body.count(old) == 1
        entry['edits'].append({'old':old, 'new':new})
assert len(out) == 43
for entry in out:
    original = (ROOT / entry['path']).read_text(encoding='utf-8')
    revised = original
    for edit in entry['edits']:
        assert revised.count(edit['old']) == 1
        revised = revised.replace(edit['old'], edit['new'], 1)
    assert re.findall(r'\\tag\{[^}]+\}', original) == re.findall(r'\\tag\{[^}]+\}', revised)
    assert revised.count('$') % 2 == 0
target = ROOT / 'other/work/scratch/all-subject-explanations/et-proposals.json'
target.write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'proposed': len(out), 'edits':sum(len(e['edits']) for e in out), 'all_unique_anchors':True, 'tags_preserved':True, 'dollar_count_even':True, 'output':target.relative_to(ROOT).as_posix()}))

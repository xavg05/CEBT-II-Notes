"""Apply the authorised October 2026 explanation revision to canonical PDC drafts.

Exact anchors make changes reviewable and prevent accidental repeated application.
Publish separately with publish_pdc.py. Do not rerun the historical write_notes.py.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
DRAFT = ROOT / 'other/work/drafts/Process Dynamics and Control'
changes = []

def edit(n, anchor, replacement):
    p, = DRAFT.glob(f'PDC-{n:02d} - *.md')
    s = p.read_text(encoding='utf-8')
    if replacement in s:
        changes.append({'note': n, 'anchor': anchor})
        return
    assert s.count(anchor) == 1, (n, anchor)
    p.write_text(s.replace(anchor, replacement), encoding='utf-8')
    changes.append({'note': n, 'anchor': anchor})

def before(n, heading, text):
    edit(n, heading, text.strip() + '\n\n' + heading)

before(1, '## Derivation', r"""
Follow a cold-feed disturbance through the tank. Colder liquid first reduces the energy arriving each second; stored energy then falls, so the tank cools. Feedback detects that temperature fall and raises heating. Feedforward measures the colder feed and raises heating before the tank needs to cool. This causal sequence explains why feedback needs a changed measurement and why feedforward needs a model of the disturbance's effect.
""")
before(1, '## Link to other topics', r"""
The extra heating has a simple meaning: the heat-capacity flow rate is $\rho qc_p=42000$ W K$^{-1}$, so every kelvin lost from the feed needs that much extra power. The tank's stored heat determines how quickly an uncompensated error develops; it does not change the final power required. The ideal feedforward law preserves an existing fixed target, but an instantaneous target change cannot make stored liquid jump to a new temperature.
""")
before(2, '## Derivation', r"""
To choose an actuator, imagine moving its valve and follow what happens to the measured quantity. Opening distillate withdrawal removes liquid from the drum directly. Increasing reflux also removes drum liquid, but sends it back into the column and changes separation. Reserving different actuators for inventory and quality avoids asking one valve to satisfy two independent objectives at once; it does not eliminate interactions.
""")
before(2, '## Motivation and explanation', r"""
At the old steady state, the drum inflow and outflows balance. If condensate inflow rises while both withdrawals stay fixed, the positive imbalance integrates into increasing mass and level. With no level-dependent outflow in this simplified balance, a higher level alone does not remove that imbalance. The level controller supplies the restoring action by changing withdrawal. A temperature loop instead changes internal contacting and vapour–liquid equilibrium, so its physical pathway is different.
""")
before(3, '## Motivation and explanation', r"""
The outlet-flow cancellation is physical, not just convenient algebra. Removing a small portion of perfectly mixed liquid removes the same fraction of A as of total volume, leaving the remaining concentration unchanged at that instant. It still changes $V$, so subsequent feed dilution and reaction per stored amount can evolve differently. A concentration is a ratio; the amount balance and volume balance must agree before an equation for that ratio is trustworthy.

Model closure means being able to calculate every right-hand side from the current states and specified inputs. Knowing $V,c_{A1},T_1$ is insufficient if $r$ or $Q_c$ is still unknown. A rate law supplies $r$; a heat-transfer relation and, if needed, a jacket energy balance supply $Q_c$. Each additional stored quantity needs its own initial condition and balance.
""")
edit(4, r'*Reason:* divide the accumulation balance by $q$ to expose the residence time $\tau$.', r"""*Reason:* fixed volume gives $d(Vc)/dt=V\dot c$. Dividing by $q$ makes the coefficient of $c$ equal to one. In the standard first-order form $\tau\dot c+c=K_pc_0$, the derivative coefficient is the time constant and the right-side coefficient is the gain. Setting $\dot c=0$ gives $c=c_0$, so an inert tank has unit gain.

The ratio $V/q$ is also the mean residence time: stored liquid volume divided by volume replaced each second. Perfect mixing allows some new feed to leave quickly and some to remain longer, so it is an average, not an identical transit time for every fluid element.""")
edit(4, r'Multiply by integrating factor $e^{t/\tau}$:', r"""Subtracting the old steady balance removes constant terms; because the tank starts there, its initial deviation is zero. First divide the ODE by $\tau$, then multiply by $e^{t/\tau}$:""")
edit(4, '*Reason:* the product derivative collects the derivative and concentration terms.', r"""*Reason:* the product rule gives $d(e^{t/\tau}c')/dt=e^{t/\tau}\dot c'+e^{t/\tau}c'/\tau$, exactly the left side after multiplication. The integrating factor is chosen to create that exact derivative.""")
edit(4, r'*Reason:* collect both removal mechanisms and divide by their combined coefficient. Thus the effective time constant is $\tau_r=\tau/(1+k\tau)$ and concentration gain is $K_p=1/(1+k\tau)$.', r"""*Reason:* reaction consumes $kc$ per unit volume, hence $kVc$ in the whole tank. Collecting terms gives $V\dot c+(q+kV)c=qc_0$. Divide by the coefficient of $c$, namely $q+kV$, to put this in standard form:

$$\tau_r=\frac{V}{q+kV}=\frac{\tau}{1+k\tau},\qquad
K_p=\frac{q}{q+kV}=\frac{1}{1+k\tau}.$$

The same total removal coefficient appears below both ratios. Storage divided by removal sets the response time; input coefficient divided by removal sets the settled sensitivity. These are different properties even though reaction reduces both here.""")
edit(4, '**Step 4: transform the perturbation balance.**', r"""**Step 4: transform the perturbation balance.** The reacting equilibrium is $c_s=c_{0s}/(1+k\tau)$, so it differs from the inert equilibrium. Subtracting it gives $\tau\dot c'+(1+k\tau)c'=c_0'$.""")
edit(4, r"*Reason:* the Laplace transform replaces $\dot c'$ by $s\bar c$. The pole $p$ gives the exponential decay rate.", r"""*Reason:* with zero initial deviation, the transform gives $[\tau s+1+k\tau]\bar c=\bar c_0$. Dividing isolates the output/input ratio. The pole is the value making the denominator zero. Its free-response term is $e^{pt}$, so a negative pole gives decay, and a more negative pole gives faster decay. Setting $s=0$ gives $G(0)=K_p$, the settled gain for this stable lag.""")
edit(4, r'The inert tank has unit concentration gain and pole $-1/\tau$. Reaction moves the pole farther left and reduces the gain. A faster response therefore does not imply more reactant survives. Taking $k\rightarrow0$ recovers the inert-tank model.', r"""An excess of A can disappear by washout and by reaction. Both sinks strengthen the restoring effect, shortening the concentration response. At steady state, however, feed A must supply both sinks: $qc_0=(q+kV)c$. Only the fraction $q/(q+kV)$ leaves unreacted, which explains the smaller concentration gain.

The dimensionless group $k\tau$, the Damköhler number for this model, compares the reaction timescale with the flow-through timescale. When $k\tau\ll1$, washout dominates and $K_p\to1$, $\tau_r\to\tau$. When $k\tau\gg1$, little A survives, $K_p\approx1/(k\tau)$, and $\tau_r\to1/k$. The fluid's mean residence time is still $V/q$; reaction shortens the concentration memory without speeding up the liquid flow.""")
edit(4, 'These conclusions require constant $q,V,k$ and negligible thermal coupling. Changing temperature or flow generally changes the coefficients; second-order kinetics requires local linearisation.', r"""These conclusions require constant $q,V,k$ and negligible thermal coupling. If flow becomes another changing input, $qc$ contains a product of changing variables; a local model drops the product of their deviations. A prescribed new constant flow still permits a lag model, but with new coefficients. Temperature-dependent kinetics couples concentration to the energy balance. Second-order consumption $kc^2$ has local slope $2kc_s$, so its linearised response depends on the chosen operating concentration.""")
before(4, '## Link to other topics', r"""
Both responses reach $63.2121\%$ of their own final change at their own time constant. The reacting tank reaches that fraction sooner, but its final increase is only half as large. For a common $95\%$ settling criterion, the inert and reacting times are $299.573$ s and $149.787$ s respectively. Neither response finishes exactly at a finite time. The initial slopes are equal here: $\Delta c_0/\tau=K_p\Delta c_0/\tau_r=0.0300$ mol m$^{-3}$ s$^{-1}$. Reaction changes the subsequent curvature and endpoint, while the unchanged feed step sets the same initial accumulation rate.
""")
before(5, '## Motivation and explanation', r"""
Why does outlet flow disappear from the concentration equation while inlet flow remains? The outlet has exactly the tank composition, so it removes solute and total volume in matching proportions. Feed at $c_0\ne c$ changes those proportions. As a check, feed at $c_0=c$ cannot change an inert tank's concentration even if it changes the volume. Withdrawal can still shorten the time over which a later feed change acts by reducing the stored volume.
""")
before(5, '## Link to other topics', r"""
The new concentration lies between the two original concentrations because it is their volume-weighted average. The added liquid is richer, so concentration rises, but its own volume dilutes the added solute. The jump changes the initial state for the next stage; it is not a new steady state unless later inflow, outflow and reaction also balance there.
""")
before(6, '## Motivation and explanation', r"""
In both models, normalising means dividing by the coefficient of the stored temperature, not by its derivative coefficient. For the sensor this is $hA_h$: at equilibrium $y=x$, so gain is one, and capacity $mc_p$ divided by conductance $hA_h$ gives the time constant. Increasing sensor mass slows it; increasing exposed area or heat transfer speeds it. The analogy with a mixing tank concerns this balance structure; heat transfer does not imply that sensor material is being replaced by flowing liquid.

For the heated tank, setting the derivative to zero gives $T=T_0+Q/(\rho qc_{pL})$. A one-kelvin feed change therefore produces a one-kelvin settled tank change, whereas a watt of heating produces $1/(\rho qc_{pL})$ kelvin. Both inputs share the same relaxation rate because there is only one stored tank temperature. They do not create two separate tank states.
""")
before(6, '## Link to other topics', r"""
The sensor has completed the same fraction of its $40$ K change that the tank has completed of its $10$ K change after one respective time constant. In a measurement chain, tank temperature changes first and supplies a changing input to the sensor. Applying the sensor's step formula directly to that gradual input would misrepresent the combined response; its dynamics must be driven by the actual tank temperature.
""")
before(7, '## Motivation and explanation', r"""
The product rule exposes the cooling mechanism directly. Expanding the stored energy and using $\dot m=-w$ gives $mc_v\dot T=-w(c_p-c_v)T=-wRT$. Removing mass at unchanged temperature would remove only its internal energy; the outlet enthalpy removes more. That excess is supplied by cooling the remaining gas. Since $w>0$ and $T>0$, the predicted temperature derivative is negative.

The outlet law cancels when finding temperature versus remaining mass, so different discharge rates follow the same state relation under these assumptions. They traverse it at different speeds. Although the pressure–temperature exponent resembles a reversible adiabatic closed-system relation, this derivation describes an open vessel losing mass and does not establish that the discharge is reversible.
""")
before(8, '## Motivation and explanation', r"""
Subtracting a baseline and neglecting an initial condition are separate decisions. Baseline subtraction is an exact change of coordinates. Zero initial deviation is justified only by actually starting at that baseline. If a tank begins above its chosen equilibrium, that stored excess relaxes even when the input deviation stays zero; the second term in equation (26) accounts for it. A transfer function isolates how the imposed input acts, so that free response is handled separately.

For a stable lag, the denominator $\tau s+1$ is the transformed competition between storage and removal. The transform has made a differential equation algebraic; it has not added a new physical mechanism. Returning to the time domain gives the same exponential relaxation derived by an integrating factor.
""")
before(9, '## Motivation and explanation', r"""
The distance still to travel is $K_p\Delta x-y'=K_p\Delta x\,e^{-t/\tau}$. In each time interval of length $\tau$, this remaining distance is multiplied by $e^{-1}$; the response never uses up a fixed amount per second. That is why the rise is initially steep and then flattens. The initial tangent reaches the final level at $\tau$ only if its starting slope were maintained; the actual slope immediately starts falling.

An impulse has a different endpoint because its forcing ends. Its finite area changes the stored state across the brief input, then the unforced state decays back to baseline. A step continually supports a displaced equilibrium. Their different final values reflect different experiments, not different process gains.
""")
before(9, '## Link to other topics', r"""
For comparison, at two time constants the step has completed $86.4665\%$ of its final change. All these fractions refer to the output change from its initial value, not to its absolute value. Dividing by $K_p\Delta x$ removes amplitude and units, leaving one common curve against $t/\tau$ for every stable first-order lag without delay.
""")
before(10, '## Motivation and explanation', r"""
The missing term in the level balance is a level-dependent removal term. A lag would have a contribution proportional to $-h'$ that grows as level rises and eventually cancels the changed inflow. Here the prescribed pump removes the same flow at every level, so no new level restores the balance. When the extra inflow ends, the level stops rising but retains its accumulated offset. This is the physical memory represented by $1/s$.

A delay stores a history of conditions travelling along a pipe. It does not continuously blend that history into a single mixed state. For a step, compare the shapes: a lag begins immediately and curves toward a final value; an integrator ramps while the imbalance persists; an ideal delay stays unchanged and then jumps. Increasing $t_d$ shifts the arrival time without reducing step amplitude or rounding the front.
""")
before(11, '## Motivation and explanation', r"""
Normalising by $a_0$ makes the final output/input ratio visible as $K_p=b/a_0$; matching the derivative coefficients then defines $\tau$ and $\zeta$. Do not read $a_1$ alone as a first-order time constant: both derivative terms jointly determine two poles. For a complex pair, $e^{(-\zeta/\tau+i\omega_d)t}$ separates into decay envelope $e^{-\zeta t/\tau}$ and oscillation. The envelope time is $\tau/\zeta$, while the oscillation period depends on $\omega_d$.

For the mass–spring analogy, displacement can keep increasing after crossing equilibrium because velocity is still positive: kinetic energy carries it past the target. Dissipation reduces that stored energy on each swing. Two sequential mixing tanks lack this inertial exchange mechanism; the downstream tank merely follows a progressively changing upstream input. The shared second-order equation does not make their physical couplings identical.
""")
before(11, '## Link to other topics', r"""
Read the response graph in two parts: the common final normalised value expresses gain, while the curvature and crossings express damping. For the unequal tanks, the pole nearer zero, $-0.0125$ s$^{-1}$, corresponds to the slower $80.0$ s mode and governs the late tail when its coefficient is nonzero. For the complex example, the real part sets how quickly peaks shrink and the imaginary part sets how closely they are spaced.
""")
before(12, '## Motivation and explanation', r"""
The constant $1$ in the normalised solution is the forced equilibrium. The transient starts at $-1$ to cancel it at $t=0$ and must also match the zero initial slope. This is why the oscillatory part is not an arbitrary sine curve placed around the endpoint: its sine and cosine weights are fixed by the starting state. As $t$ grows, the transient decays and leaves the forced equilibrium.

At the first peak the response has travelled half an oscillation period. There the sine term is zero and the cosine is $-1$, so the excess above the final value equals the exponential decay factor at that instant. Successive peaks on the same side are a full period apart, so their excesses shrink by the full-period decay factor. In the figure, measure excesses from the final-value line; measuring peak heights from zero would mix the steady part into the transient ratio.
""")
before(12, '## Link to other topics', r"""
The $16.3034\%$ overshoot means the first peak exceeds the final change by that fraction; it does not mean the output peaks at $0.163034$. The same-side ratio $0.0265799$ means the next excess is only that fraction of the first excess. The repeated-lag response's zero initial slope also explains its smaller progress at $t=\tau$: the second tank must wait for the first tank to develop a temperature difference, even though there is no exact waiting interval.
""")
before(13, '## Motivation and explanation', r"""
The delay and lags answer different questions. The delay says when the response can first appear. The two tank states say how it develops after that arrival. Immediately after arrival, tank 1 starts warming, but tank 2 still has almost no inlet–contents temperature difference, so its initial slope is zero. For every positive elapsed time after arrival the outlet does change; the initially flat tangent does not add another interval of dead time.

Multiplying the zero-frequency gains gives one: with no heat loss, every element ultimately reaches the new inlet temperature. The repeated pole supplies the $t e^{-t/\tau}$ term, which changes the rise shape without changing that endpoint. Shift both occurrences of time in the causal response when reinstating the pipe delay; shifting only the exponential would violate the starting conditions.
""")
before(14, '## Motivation and explanation', r"""
It is legitimate to sum the two temperature contributions because each is already expressed in output-temperature units. The factor $1/C_f$ converts heating power into the feed-temperature change with the same thermal effect. Then the common lag applies to their sum. A block diagram is bookkeeping for these equations: a line is a signal, a summing point adds signed effects, and a branch sends the same value to more than one destination.

Exact dynamic compensation requires the paths to cancel as functions of $s$, not merely at $s=0$. If the heater has an extra actuator lag, its final temperature contribution can still cancel the cold feed while its early contribution is too slow. That produces a temporary temperature drop even when the eventual temperature error is zero.
""")
before(15, '## Motivation and explanation', r"""
Read the first column as one experiment: change feed A, hold feed B unchanged, and observe both outputs. The upper entry is direct survival of A; the lower entry is production of B through the changing A inventory. Read the second column as a different experiment: feed B changes without changing A. The zero in the upper-right entry records the absence of a reverse reaction or other coupling under these assumptions.

Adding the two output rows checks more than the final numbers. Reaction redistributes molecules between A and B but cannot alter their total in this one-to-one conversion. The total therefore follows the inert-tank mode at all times. A faster A-removal mode is compatible with a slower total-concentration mode because consuming A creates B rather than removing total A plus B.
""")
before(15, '## Link to other topics', r"""
The final half-and-half split is about the extra feed A: half survives as A and half appears as B. Early on, A begins rising immediately, while B initially has zero slope because its extra production rate first needs extra A to build up. Thus the equal final gains do not imply equal transient curves.
""")
before(16, '## Motivation and explanation', r"""
The signs follow the energy pathways. At fixed feed, extra heat evaporates liquid, so the heat-to-liquid-volume coefficient $b$ is negative and the heat-to-steam coefficient $d$ is positive. At fixed heat, extra subcooled feed requires warming, so it accumulates as liquid and can reduce steam production. A feed-to-steam coefficient slightly below zero is therefore compatible with mass conservation: the changed inventory absorbs more mass than the feed increase alone.

There is no $V_L$ term on the right of $\dot V_L=aF+bQ_H$. Consequently, a persistent nonzero $aF'+bQ_H'$ cannot be removed merely by reaching a different level. The integrator represents that continuing accumulation. Steam flow has no separate stored state in this fixed-pressure approximation; the algebraic balance assigns it an immediate change. Real pressure and heat-transfer dynamics would resolve that idealisation into additional dynamics.
""")
before(17, '## Motivation and explanation', r"""
For a simple real pole, moving farther left increases the decay rate because $e^{pt}$ falls more quickly. A complex pair adds repeated sign changes while its real part still controls the envelope. Repeating a negative pole adds a factor such as $t$, so a mode can initially grow in magnitude before decaying; the exponential ultimately wins. A repeated pole at zero instead gives powers of time with no decaying exponential to suppress them.

Among observable stable modes with nonzero weights, poles nearest the imaginary axis usually govern the late tail. Their weights still matter: a slow mode with a very small coefficient may be barely visible over the time interval of interest. Pole locations predict possible rates and frequencies, while the particular input, output and numerator determine how much each mode appears.
""")
before(17, '## Link to other topics', r"""
The growing oscillation may start with a small coefficient, but its $e^t$ envelope eventually overwhelms the decaying terms and constant. A short observation that looks quiet cannot overturn the positive-real-part pole test. Here the constant term comes from a process integrator; in a stable lag's step response, a constant can instead come from the step's input pole. Keeping the experiment specified avoids confusing those cases.
""")
before(18, '## Motivation and explanation', r"""
The two pathways settle to different strengths: their gains are $4$ and $-3$, so the positive contribution wins at long times. Initially, their slopes are $4$ and $-6$, so the faster negative path wins. That change of dominance explains the dip without requiring an unstable pole. The zero at $+1$ appears when the two pathway expressions are combined; it describes their cancellation in the transfer numerator, not an extra growing state.

Feedthrough is another distinct feature. With a finite step and strictly proper lag pathways, the state output remains continuous and only its slope changes. A nonzero direct term $D_0$ adds an immediate jump $D_0\Delta x$ on top of the stored-state response. Such a jump, a gradual inverse response, and a transport waiting time therefore have different mathematical and physical causes.
""")
before(19, '## Motivation and explanation', r"""
Evaluating at $s=0$ removes derivative factors, which is why it reproduces the static balance when a static balance is actually reached. The final-value theorem makes that connection precise; it does not supply decay that the process lacks. A unit step has transform $1/s$, so $s\bar y=G(s)$ for that experiment, and the stability condition must be checked before taking its limit.

Gain and speed can change independently. Multiplying a stable transfer function by a constant scales its endpoint without moving its poles. Adding pure delay shifts its timing without changing $G(0)$. Moving a pole while adjusting the numerator can change speed at fixed gain. A final-value calculation deliberately discards transient detail and must be paired with a dynamics check when timing matters.
""")
before(20, '## Motivation and explanation', r"""
To see what the tangent approximation removes, expand $(c_{As}+c_A')^2=c_{As}^2+2c_{As}c_A'+(c_A')^2$. The first term belongs to the equilibrium and cancels; the second changes the local removal slope; the third is the curvature being neglected. A higher positive operating concentration therefore gives a stronger local reaction sink, a shorter time constant and a smaller feed-to-concentration gain. This has the same storage-versus-removal interpretation as the first-order reacting tank, but its coefficients now depend on the operating point.

For a general product of two changing variables, $(q_s+q')(c_s+c')=q_sc_s+q_sc'+c_sq'+q'c'$. Keep both terms linear in deviations and drop only the final product. Calling the perturbations small is meaningful because their product is smaller in order than either individual deviation; it does not justify discarding one of the linear contributions.
""")
before(20, '## Link to other topics', r"""
The local gain is also the slope of the steady relation. Differentiating $c_{A0s}=c_{As}+k_2\tau c_{As}^2$ gives $dc_{As}/dc_{A0s}=1/(1+2k_2\tau c_{As})$. Thus the dynamic linearisation and the tangent to the equilibrium curve predict the same small final change. A finite change follows the curved relation, so this slope need not give its exact endpoint.
""")
before(21, '## Motivation and explanation', r"""
The outlet's local slope is $dq/dh|_s=k/(2\sqrt{h_s})$. Dividing area by this slope gives the time constant; the reciprocal of the outflow slope gives the steady level gain. More area slows the response without changing the eventual level needed to pass a given flow. At greater operating depth, the outflow slope is smaller, so an extra inlet flow needs a larger level rise and that rise develops more slowly. These trends follow from the square-root law, not from an assumed universal tank time constant.

For either positive or negative physically admissible inlet changes, the exact final level differs from the tangent prediction by the nonnegative squared term in equation (66). This is the curvature of the equilibrium relation. The transient comparison has to use the same initial level, inlet step and absolute/deviation convention in both models; otherwise a baseline mismatch can look like linearisation error.
""")
before(21, '## Link to other topics', r"""
The graph illustrates two differences: the local model approaches a different endpoint and follows a different trajectory on the way there. Here the exact final rise exceeds the linear final rise because the true outflow increases less rapidly with level than its initial tangent predicts. To balance the larger feed, the exact model must reach a greater depth. A comparison of settling fractions should therefore use each model's own endpoint.
""")
before(22, '## Motivation and explanation', r"""
The first-tank valve gain contains $100-x_s$ because each extra unit of pure-tracer inflow also drives out an extra unit of the existing mixture. Counting only the incoming tracer would overstate its effect. In a downstream tank, the baseline inlet and outlet compositions are identical, so changing flow alone creates no first-order composition forcing. It multiplies only the developing composition difference, which is why that contribution is a product of deviations.

Each tank adds one stored concentration and one lag factor. After a valve step, tank 1 begins changing first; its emerging change drives tank 2, which then drives tank 3. The polynomial multiplying the exponential in equation (71) enforces the initially gentle downstream response. A repeated pole describes several sequential memories with the same decay rate, not a single lag with its time constant multiplied by three.
""")
before(22, '## Link to other topics', r"""
At one individual tank time constant the final outlet has completed only $8.03014\%$ of its own final change; at three it has completed $57.6810\%$. The single-lag $63.2\%$ rule therefore cannot be applied to the whole cascade using $\tau=5$ min. The small difference between exact and linear final compositions checks the local endpoint approximation for this valve move; it does not by itself verify the whole transient.
""")

out = ROOT / 'other/work/scratch/pdc-explanation-revision'
out.mkdir(parents=True, exist_ok=True)
(out / 'edits.json').write_text(json.dumps(changes, indent=2), encoding='utf-8')
print(f'Applied {len(changes)} targeted edits across {len({c["note"] for c in changes})} notes.')

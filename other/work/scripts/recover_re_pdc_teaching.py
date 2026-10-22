"""Selective recovery of teaching lost with worked-example sections, 22 Oct 2026.

Uses current corrected drafts; never restores an entire historical file.
"""
from pathlib import Path
import json, re, sys, subprocess
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'other/work/scripts'))
from check_inline_math import check_files

PDC={
1:('Feedforward power and stored heat',r'''For the heated-water balance, define heat-capacity flow $C_f=\rho qc_p$. Holding a fixed target requires $Q_s=C_f(T_{sp}-T_{0s})$, so an inlet-temperature change $\Delta T_0$ requires $\Delta Q=-C_f\Delta T_0$. The tank's stored heat determines how quickly an uncompensated error develops, but it does not change this final power requirement. A feedforward command can preserve an existing target if the measurement, model and heater are adequate; it cannot make stored liquid jump instantly to a new target.'''),
2:('Choosing which loop corrects an inventory',r'''When reflux-drum level rises at a fixed target, increasing distillate withdrawal opposes accumulation directly. Reducing reflux could also drain the drum, but would disturb upper-column separation; reserving reflux for the temperature loop avoids using one adjustment for conflicting objectives. If pressure rises, additional condenser cooling can oppose it within the available range. Simultaneous tray-temperature changes must then be interpreted with the pressure change, rather than automatically assigned to composition.'''),
3:('Closing the coolant response',r'''A colder coolant inlet changes heat removal, then reactor temperature, and potentially reaction rate and composition. Measuring this disturbance does not make it a manipulated input. Coolant flow is manipulated when its valve can be commanded. If coolant outlet temperature $T_{co}$ is an output, it needs its own closure: a quasi-steady coolant balance is $Q_c=w_cc_{pc}(T_{co}-T_{ci})$, where $w_c$ is coolant mass flow and $c_{pc}$ its mass-specific heat capacity. Appreciable jacket storage instead requires a dynamic coolant balance.'''),
4:('Initial slope and final change measure different effects',r'''Immediately after a feed-composition step $\Delta c_0$, the tank concentration is still at its old value. Its removal terms have not yet changed, so the initial slope is $\dot c'(0^+)=q\Delta c_0/V=\Delta c_0/\tau$ for both inert and first-order reacting tanks with the same $q,V$. Equivalently, $K_p/\tau_r=1/\tau$. Reaction changes the subsequent curvature and endpoint, while the feed step sets the initial accumulation. A faster approach must therefore be judged against each response's own final change: it need not mean a larger concentration at a specified time.'''),
5:('Interpreting the state after a pulse',r'''The jump concentration is a volume-weighted average, so with positive additive volumes it lies between the original and pulse concentrations. Rich added liquid raises concentration, but its own volume dilutes the added solute. Treating a finite liquid addition as solute at unchanged volume overpredicts the concentration; maintaining constant volume instead requires including the displaced outflow. The jump supplies a new initial state for subsequent dynamics, not a new steady state unless later flows and reaction balance there.'''),
6:('Driving a sensor with a changing temperature',r'''In a tank–sensor chain, the tank temperature begins changing first and becomes the sensor's time-dependent input. The sensor's bath-step formula assumes its own input jumps to a constant value, so it cannot be applied directly to the gradually changing tank temperature. Solve the two balances together or multiply their zero-state transfer functions. A small sensor time constant can justify approximate tracking; otherwise measured temperature retains an additional memory of past tank temperatures.'''),
7:('Cooling makes pressure fall faster than inventory',r'''At fixed vessel volume, $p/p_0=(m/m_0)(T/T_0)=(m/m_0)^\gamma$. For $\gamma>1$, pressure therefore falls faster than mass during the modelled adiabatic discharge: the remaining gas also cools. Replacing outlet enthalpy by $c_vT$ would cancel the temperature change in the expanded energy balance and falsely predict constant vessel temperature. That error discards the flow-work contribution carried by the departing stream.'''),
8:('Returning from deviations to the measured quantity',r'''For an inert tank initially at equilibrium $c_s=c_{0s}$, a feed step to $c_{0s}+\Delta c_0$ has input transform $\bar c_0=\Delta c_0/s$. Inverting the transfer-function response and restoring the baseline gives

$$c(t)=c_s+\Delta c_0(1-e^{-t/\tau}).$$

At fixed flow and volume, the same deviation model applies around any concentration baseline. Using the final absolute feed concentration as the step amplitude would add the old baseline a second time.'''),
9:('A common normalised curve and an explicit settling criterion',r'''For a nonzero step response, divide the output change by $K_p\Delta x$ and define $\theta=t/\tau$. Every stable first-order lag without delay then follows $r(\theta)=1-e^{-\theta}$. At $\theta=1,2,3,5$, the completed fractions are approximately $0.632121$, $0.864665$, $0.950213$ and $0.993262$. These are fractions of the initial-to-final change, not of the absolute output. Requiring the remaining error to be at most a fraction $\varepsilon$ gives $e^{-t/\tau}\le\varepsilon$, hence $t\ge-\tau\ln\varepsilon$. A 5% tolerance needs $2.99573\tau$; exact completion takes no finite time.'''),
11:('Reading the damping curves',r'''![Normalised second-order step responses at different damping factors](../figs/PDC-11-damping-regimes.png)

The horizontal axis is $t/\tau$ and the vertical axis is output change divided by the unit-step gain. For positive damping the common final value is one; the zero-damping curve oscillates indefinitely about that reference and has no settled endpoint. Curvature and crossings reveal damping. For two passive tanks with time constants $20$ and $80\ \mathrm{s}$, $\tau=40\ \mathrm{s}$ and $\zeta=1.25$; the poles are $-0.05$ and $-0.0125\ \mathrm{s^{-1}}$. Both modes decay without oscillation. The pole nearer zero supplies the slower tail when its coefficient is nonzero. An underdamped complex pair instead sets a decaying envelope through its real part and peak spacing through its imaginary part.'''),
12:('Comparing a repeated lag with a single lag',r'''For critical damping the normalised response at $t=\tau$ is $1-2e^{-1}\approx0.264241$. Its zero initial slope reflects sequential storage: the second state first needs a change in the first state to drive it. There is no exact waiting interval. In an oscillatory response, overshoot is the peak's excess above the final value divided by the initial-to-final change; a same-side decay ratio compares successive excesses above that reference, rather than successive absolute peak heights.'''),
14:('When two input paths cancel throughout the transient',r'''For the heated-tank model, simultaneous constant input changes give

$$T'(t)=\left(\Delta T_0+\frac{\Delta Q}{C_f}\right)(1-e^{-t/\tau}),\qquad C_f=\rho qc_p.$$

Thus $\Delta Q=-C_f\Delta T_0$ cancels the whole response because the two paths share the same lag and start together. Equality of steady gains alone is insufficient: actuator lag, delayed measurement or an incorrect $C_f$ leaves a transient even when the eventual effects cancel.'''),
15:('Equal final gains can hide different early responses',r'''For a step in feed A alone, extra A begins accumulating immediately, while extra B production first needs extra A inside the tank. Consequently B initially has zero slope even though A does not. At $k\tau=1$, the final extra feed contribution splits equally between surviving A and product B; that equal final gain does not imply equal transient curves. Their sum at every time follows the inert-tank response, providing a stronger conservation check than checking only the final values.'''),
16:('Matching the feed and heat commands',r'''To increase feed by a constant $\Delta F$ without inventory drift, the steady balances require $\Delta G=\Delta F$ and $\Delta Q_H=(\hat H_G-\hat H_F)\Delta F$. Extra heat must bring the incoming feed to the outgoing steam state; using saturated-liquid latent heat alone omits warming a subcooled feed. The heat-column coefficients must use the same power units as the input: converting kilowatts to watts divides those numerical coefficients by $1000$.'''),
17:('Reading several modes in one impulse response',r'''With time measured in seconds, consider

$$G(s)=\frac{1}{s(s+1)^2(s+2)[(s-1)^2+16]}.$$

Its poles are $0$, $-1$ twice, $-2$ and $1\pm4i$, in $\mathrm{s^{-1}}$. The denominator expands to $s^6+2s^5+14s^4+60s^3+81s^2+34s$. For a unit-area impulse, partial fractions and the elementary inverse transforms give

$$y'(t)=\frac1{34}-\frac{e^{-2t}}{50}-\frac{e^{-t}}{100}-\frac{te^{-t}}{20}+\frac{e^t[\cos(4t)-0.25\sin(4t)]}{1700},\qquad t\ge0.$$

![Pole locations, with the repeated pole plotted at the same point](../figs/PDC-17-pole-map.png)

The constant comes from a process integrator because the specified input is an impulse. The factor $te^{-t}$ exposes the repeated negative pole. The growing oscillation can initially have a small amplitude, but its $e^t$ envelope eventually dominates: a quiet short observation cannot overturn the positive-real-part pole test. In a stable lag's step experiment, a constant would instead come from the input pole, so the forcing must always be specified.'''),
18:('Locating the reversal',r'''For the two-pathway step model above, $\dot y'=4e^{-t}-6e^{-2t}$. Setting this to zero gives $e^t=3/2$ and a minimum at $t=\ln(3/2)\approx0.405465\ \mathrm{s}$, with $y'=-1/3$. The faster negative path initially wins: its slope is $-6$ against $+4$. The final contributions are $-3$ and $+4$, leaving $+1$. Initial direction and eventual gain therefore report different balances between pathways.'''),
19:('A finite algebraic gain without a final value',r'''For $G(s)=1/(s-1)$ and a unit step, partial fractions give $\bar y=1/[s(s-1)]=-1/s+1/(s-1)$, hence $y'=e^t-1$. Although $G(0)=-1$ is finite, the positive process pole prevents settling. This supplies a direct counterexample to applying the final-value theorem before checking its pole conditions.'''),
20:('Dynamic gain is also the equilibrium tangent',r'''The second-order steady balance is $c_{A0s}=c_{As}+k_2\tau c_{As}^2$. Differentiating at fixed $k_2,\tau$ gives

$$\frac{dc_{As}}{dc_{A0s}}=\frac{1}{1+2k_2\tau c_{As}}=K_p.$$

Thus the local dynamic gain agrees with the tangent of the equilibrium relation. A finite input change follows the curved relation; the tangent need not predict its exact endpoint. Linearising at another concentration changes both this gain and the local time constant.'''),
21:('Interpreting the local and nonlinear response graph',r'''![Local linear response and nonlinear level response](../figs/PDC-21-linear-and-nonlinear-level.png)

The curves compare the same initial level and inlet-flow step. Their different endpoints arise because square-root outflow increases less rapidly than its initial tangent predicts at greater depth: the nonlinear tank must rise further to pass the larger feed. The sketch is qualitative, so settling fractions should use each model's own computed endpoint rather than reading precise times from the drawing. For $A=3\ \mathrm{m^2}$, $k=0.02\ \mathrm{m^{5/2}\,s^{-1}}$, initial feed $0.02\ \mathrm{m^3\,s^{-1}}$ and increase $0.01\ \mathrm{m^3\,s^{-1}}$, the initial level is $1\ \mathrm m$; the local and exact final levels are $2$ and $2.25\ \mathrm m$. The missing quadratic term, rather than a baseline mismatch, explains this difference.'''),
22:('Checking a three-lag response against its own endpoint',r'''At one individual tank time constant, equation (71) has completed only $1-(1+1+1/2)e^{-1}\approx0.0803014$ of its final change. At three time constants the fraction is $1-(1+3+9/2)e^{-3}\approx0.576810$. The single-lag 63.2% rule cannot be applied to this entire cascade using an individual tank's time constant. For a valve move from $50$ to $60$ percent open, the local final concentration is $4.34416\%$, whereas the exact steady feed mixture gives approximately $4.34263\%$. Their closeness checks the local endpoint approximation for this move; it does not verify the entire transient.'''),
}

RE={
'RE-02':('First-order sizing and its limiting cases',r'''For constant density and $-r_A=kC_A$, substitute $C_A=C_{A0}(1-X_A)$ into the two design balances. The CSTR relation becomes $Q C_{A0}X_A=kC_{A0}(1-X_A)V$, so

$$\tau_{\mathrm{CSTR}}=\frac{X_A}{k(1-X_A)}.$$

For the PFR, separate $dX_A/(1-X_A)=k\,dV/Q$ and integrate from zero conversion:

$$\tau_{\mathrm{PFR}}=-\frac{\ln(1-X_A)}k.$$

Both vanish as conversion tends to zero and diverge as it tends to unity. At fixed $k$ and target $X_A=0.8$, their ratio is approximately $2.48534$: immediate dilution throughout the CSTR costs more volume than retaining the fast inlet reaction in plug flow.'''),
'RE-03':('First-order design with expansion',r'''For an isothermal, constant-pressure ideal gas with $-r_A=kC_A$, insert equation (8) into the reactor balances. Using inlet space time gives

$$\frac{V_{\mathrm{CSTR}}}{Q_0}=\frac{X_A(1+\epsilon X_A)}{k(1-X_A)},\qquad
\frac{V_{\mathrm{PFR}}}{Q_0}=\frac1k\int_0^{X_A}\frac{1+\epsilon x}{1-x}\,dx.$$

Rewrite the integrand as $(1+\epsilon)/(1-x)-\epsilon$ to separate the logarithmic and constant terms. Integration yields

$$\frac{V_{\mathrm{PFR}}}{Q_0}=\frac{-(1+\epsilon)\ln(1-X_A)-\epsilon X_A}{k}.\tag{9}$$

Setting $\epsilon=0$ recovers constant-flow first-order design. For positive expansion, the additional dilution increases the required volume at fixed conversion and kinetics. These expressions use inlet flow: the actual travel time requires integrating $dV/Q(V)$ instead.'''),
'RE-04':('Adiabatic temperature as a function of conversion',r'''For one reaction, the reference reagent balance is $dX_A/dV=(-\nu_A)r/F_{A0}$. Under adiabatic operation, dividing the temperature balance by it eliminates the unknown local rate:

$$\frac{dT}{dX_A}=\frac{-F_{A0}\Delta_rH}{(-\nu_A)\sum_iF_iC_{Pi}}.$$

If total heat-capacity flow $S_C=\sum_iF_iC_{Pi}$ and reaction enthalpy are constant, integration from the inlet gives

$$T=T_0+\frac{-F_{A0}\Delta_rH}{(-\nu_A)S_C}X_A.\tag{12}$$

Eliminating volume relates heat released directly to moles consumed; it predicts temperature at an assumed conversion. Sizing still needs temperature-dependent kinetics and, where relevant, equilibrium. Zero reaction enthalpy recovers no adiabatic temperature change. The stoichiometric factor is essential when A's coefficient is not minus one.'''),
'RE-05':('The mean is not a minimum residence time',r'''For one ideal tank, integrating its exponential exit-age density gives $F(t)=1-e^{-t/\tau}$. Therefore $F(\tau)=1-e^{-1}\approx0.632121$: most fluid elements leave before the mean, and the long tail balances those early departures. With the same mean, equal-tank cascades narrow the distribution as $\sigma_t/\tau=1/\sqrt N$. A mean alone cannot specify either early breakthrough or residence-time spread.'''),
'RE-06':('A network with the same RTD and different conversion',r'''Take an isothermal, constant-density second-order reaction $-r_A=k_2C_A^2$. Place one ideal PFR and one ideal CSTR in series, each with residence time $\tau_s$, and set the dimensionless group $k_2C_{A0}\tau_s=1$. With $c=C_A/C_{A0}$, integration of the PFR balance gives $1/c_{\mathrm{out}}-1/c_{\mathrm{in}}=1$, whereas the CSTR balance gives $c_{\mathrm{in}}-c_{\mathrm{out}}=c_{\mathrm{out}}^2$. Their positive maps are

$$c_{\mathrm{PFR,out}}=\frac{c_{\mathrm{in}}}{1+c_{\mathrm{in}}},\qquad
c_{\mathrm{CSTR,out}}=\frac{-1+\sqrt{1+4c_{\mathrm{in}}}}2.$$

Starting at $c=1$, PFR then CSTR gives outlet $c\approx0.366025$ and conversion $0.633975$. Reversing their order gives outlet $c\approx0.381966$ and conversion $0.618034$. Both passive-tracer RTDs are

$$E(t)=\begin{cases}0,&0\le t<\tau_s,\\
\tau_s^{-1}e^{-(t-\tau_s)/\tau_s},&t\ge\tau_s.
\end{cases}$$

The deterministic PFR transit simply shifts the tank's exponential waiting-time distribution, regardless of order. The nonlinear concentration maps do not commute, so the same tracer RTD permits different reactive conversion. This demonstrates why an RTD alone cannot close nonlinear reaction performance.'''),
'RE-S3-04':('Distinguishing more residence time from a longer bed',r'''For $N$ equal tanks, rearrange the first-order surviving fraction by taking its $-1/N$ power:

$$k'\tau=N[(1-X)^{-1/N}-1].$$

Increasing time at fixed $N$ and increasing bed length are different comparisons. If both $N$ and $\tau$ scale with length by a factor $f$, then $k'\tau/N$ stays fixed, and

$$1-X=\left(1+\frac{k'\tau_0}{N_0}\right)^{-fN_0},\qquad
f=\frac{-\ln(1-X)}{N_0\ln(1+k'\tau_0/N_0)}.$$

Here subscript zero denotes the baseline bed. Calibrate that baseline against measured performance before predicting a plant change: a plug-flow baseline time and an uncalibrated nonideal model do not describe the same starting conversion. Extra length also increases pressure drop and may alter wetting, so the length estimate needs hydraulic and transport checks.'''),
'RE-S5-01':('Using a rate maximum as evidence',r'''At fixed B pressure, increasing strongly binding A first increases the Langmuir–Hinshelwood rate, then displaces B and can make it decline. In the specified Eley–Rideal model A remains in the gas, so raising its pressure increases collisions without competing for B's sites.

![Coverage competition and a reaction-rate maximum](../figs/RE-S5-01-rate-maximum.png)

The graph compares pressure dependence with other model parameters held fixed. A maximum supports testing coverage competition; it does not prove a unique mechanism, since temperature and transport changes can also alter a measured rate curve.'''),
'RE-S6-04':('A small temperature rise can matter kinetically',r'''A fractional temperature bound must be translated into its kinetic effect. With Arrhenius barrier $E=80\ \mathrm{kJ\,mol^{-1}}$, raising temperature from $500$ to $505\ \mathrm K$ gives $k_V(505)/k_V(500)\approx1.20989$. A 1% temperature rise can therefore change intrinsic rate by about 21%. This comparison illustrates sensitivity; the Prater bound alone does not establish that the pellet actually reaches the higher temperature.'''),
}

def recover(subject, additions):
    base=ROOT/'other/work/drafts'/subject
    decisions=[]
    for p in sorted(base.glob('*.md')):
        if subprocess.run(['git','cat-file','-e','77f9703^:'+p.relative_to(ROOT).as_posix()],capture_output=True).returncode:
            continue  # Concurrent new solid-reagent production is outside this historical recovery.
        ident=p.name.split(' - ',1)[0]
        key=int(ident[4:]) if ident.startswith('PDC-') else ident
        text=p.read_text(encoding='utf-8')
        if key in additions:
            title,body=additions[key]
            anchor='## Link to other topics' if subject.startswith('Process') else '## Motivation and explanation'
            addition='### '+title+'\n\n'+body.strip()+'\n\n'
            if '### '+title not in text:
                assert text.count(anchor)==1,p
                text=text.replace(anchor,addition+anchor)
            decision='Recovered: '+title
        else:
            reasons={
              'RE-01':'Stoichiometric rescaling and rate-unit distinction already explained algebraically; deleted numbers add substitution only.',
              'RE-S3-01':'Metal/oxide/acid choice, shape selectivity and yield limitations already explained in Equipment/Mechanisms.',
              'RE-S3-02':'Fixed-volume inverse-diameter area scaling and mechanism-specific activity caveat already derived and interpreted.',
              'RE-S3-03':'Rate contours, adiabatic stage paths, interstage exchange and inverse-rate sizing already taught together.',
              'RE-S3-05':'Ag/Pt–Rh selection repeats existing industrial mechanism and residence/transport design discussion.',
              'RE-S4-01':'Half coverage, temperature/affinity and site blocking follow existing Langmuir relation and explanation.',
              'RE-S4-02':'Shared denominator, separate site populations and displacement already explicit; numeric fractions add no new method.',
              'RE-S4-03':'Monolayer/area conversion and reference-state dependence already derived; specific fitted values are substitution.',
              'RE-S4-04':'Matched-loading finite-difference enthalpy, sign convention and constant-enthalpy limit already present.',
              'RE-S5-02':'Negative apparent barrier and negative local order already derived and interpreted; chosen values only illustrate signs.',
              'RE-S6-01':'Series collision resistances and porosity/tortuosity factors already explained; coefficient substitution redundant.',
              'RE-S6-02':'Geometry conversion and common V/A modulus already explicit; raw-modulus numerical contrast adds no new conclusion.',
              'RE-S6-03':'Surface/bulk distinction and overall effectiveness already derived; a chosen sphere adds substitution only.',
              10:'Persistent net flow gives a ramp; transit time and unchanged amplitude already derived and contrasted with lag.',
              13:'Delay plus two equal lags already derived symbolically; removed geometry/temperature substitutions add no distinct idea.',
            }
            decision='Already covered: '+reasons[key]
        replacements={
          'The worked comparison holds':'The first-order comparison holds',
          'In the worked expansion example,':'For an expanding reacting gas,',
          'In the nonlinear worked network,':'In the nonlinear network derived above,',
          'The example assumes linearity':'The two-pathway model assumes linearity',
          'This example brings physical balances':'This system brings physical balances',
          'In the worked fit,':'In an RTD fit,',
          'The worked results compare those model choices':'These expressions compare those model choices',
          'The worked comparison consequently distinguishes':'This shared-inventory balance consequently distinguishes',
        }
        for old,new in replacements.items():text=text.replace(old,new)
        if p.read_text(encoding='utf-8')!=text:p.write_text(text,encoding='utf-8')
        decisions.append({'note':ident,'decision':decision,'canonical':p.relative_to(ROOT).as_posix()})
    return decisions

if __name__=='__main__':
    result={s:recover(s,a) for s,a in [('Reaction Engineering II',RE),('Process Dynamics and Control',PDC)]}
    check_files(p for s in result for p in (ROOT/'other/work/drafts'/s).glob('*.md'))
    dest=ROOT/'other/work/progress/re-pdc-teaching-recovery-20261022.json'
    dest.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({s:{'audited':len(v),'changed':sum(x['decision'].startswith('Recovered') for x in v)} for s,v in result.items()},indent=2))

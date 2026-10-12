[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Centrifugation

## Overview

Centrifuges accelerate density-driven settling and arrange the available separation area in compact geometries. Stokes settling and residence-time arguments give a cut-off throughput, while sigma theory separates feed properties from equipment performance for conditional scale-up.

*Assumed throughout:* force balances, low-Reynolds-number drag and residence time.

## Section 35: Centrifuge designs for cell removal

### Intuition

Left standing, a suspension of cells will settle under gravity, because the cells are denser than the medium. The trouble is that it takes days (Section 36 puts a number on it). A centrifuge replaces gravity with a far larger artificial acceleration by spinning the sample, so the same settling happens in minutes.

The quantity being exploited is the **density difference**, and that is exactly what makes biological separations difficult: cells are mostly water, so they are only slightly denser than the medium they grow in. Bacteria compound the problem by being small, and the medium is often dense and viscous. Centrifugation is most effective for **large particles, low liquid viscosity and a large density difference**, and a bacterial culture offers none of these.

The response is to build centrifuges that spin very fast and present a short settling distance, and to accept that they are expensive and mechanically demanding.

*Analogy:* separating sand from water by swinging a bucket. The analogy breaks down because a real centrifuge cannot simply be spun faster without limit — the bowl wall must contain the hoop stress, which rises with the square of the speed, and that is the binding engineering constraint.

### Mechanism

Centrifuges are classified by their internal geometry. Two designs matter here.

#### Tubular bowl centrifuge

![A continuous tubular bowl centrifuge: feed enters at the base, the light phase leaves at the top and the heavy phase is discharged separately](../figs/AB-35-tubular-bowl.png)

- A **rotating tube** with a nozzle at the base where feed is introduced.
- As the liquid flows upwards, particles are spun outwards and collide with the wall of the bowl, where they are retained.
- Clarified liquid continues upwards and leaves over a **weir** at the top.
- Two timescales compete: the **residence time**, which decreases as the flow rate rises, and the **sedimentation time**, which is shorter for larger or denser particles, higher rotation speed and lower viscosity. **Particles are separated efficiently if the sedimentation time is shorter than the residence time** — the condition Section 36 turns into a maximum throughput.

Liquid feed and clarification can be continuous, while retained solids accumulate on the wall and require periodic shutdown for removal. A separate heavy-liquid outlet can provide continuous liquid–liquid separation; it does not by itself remove deposited solids.

Tubular bowls reach very high centrifugal forces — up to about 16 000 g — so they suit difficult separations. They are easy to clean, but foaming can be a problem.

#### Disc-stack centrifuge

![A disc-stack centrifuge in cross-section: feed enters down the centre, passes between conical discs, with light-liquid discharge at the top, heavy liquid and solids collected at the bowl wall, and a clean-in-place nozzle](../figs/AB-35-disc-stack.png)

- The bowl contains **conical sheets of metal (discs) stacked on top of each other**, with clearances of approximately **0.3 mm**.
- As the bowl rotates, the discs **split the liquid into thin layers**. Denser liquid containing the solids is displaced outwards along the underside of each disc, while lighter liquid remains close to the centre.
- Both streams are withdrawn continuously.
- Solids discharge depends on the design: a solids-retaining bowl is opened for manual removal; a self-cleaning bowl ejects solids intermittently through peripheral ports; a nozzle separator discharges solids continuously. A heavy-liquid outlet separates a liquid phase and is not equivalent to a solids outlet.

The discs are the whole point of the design: they reduce the distance a particle must travel before it reaches a collecting surface from the full bowl radius to the 0.3 mm gap. Section 37 shows that this is what gives the disc stack its large effective area.

Foam can be controlled, and it is easier to run continuously than a tubular bowl, but it is **harder to clean** because of the stack.

#### Comparison

![Table of bowl diameter, speed, maximum centrifugal force, liquid throughput and motor size for tubular bowl and disc-stack centrifuges](../figs/AB-35-comparison-table.png)

| | Bowl diameter (cm) | Speed (rpm) | Max force (×g) | Throughput (L/min) |
|---|---|---|---|---|
| Tubular bowl | 10 | 15 000 | 13 200 | 0.4–40 |
| | 13 | 15 000 | 15 900 | 0.8–80 |
| Disc stack | 18 | 12 000 | 14 300 | 0.4–40 |
| | 33 | 7 500 | 10 400 | 20–200 |
| | 61 | 4 000 | 5 500 | 80–800 |

The pattern is the important part. **Larger bowls run slower and generate less force, but handle far more throughput.** A 61 cm disc stack produces only 5 500 g — less than half the tubular bowl's force — yet processes up to 800 L/min against 80 L/min.

This is not a contradiction: throughput depends on the *total settling area* presented, not on the force alone, and a large stack of discs presents an enormous area. Section 37 makes this precise through the Σ factor.

### Motivation and explanation

**Why speed falls as diameter rises.** The bowl wall carries a hoop stress proportional to $\rho r^2\omega^2$. For a fixed allowable stress, the maximum angular velocity scales as $1/r$, so the maximum centrifugal acceleration $r\omega^2$ scales as $1/r$ as well. At the same allowable stress and comparable construction, bigger bowls therefore have a lower maximum g-force. The gain from building larger is area, not force, and the table shows exactly that trade.

**Centrifugation against filtration.**

| | Centrifugation | Filtration |
|---|---|---|
| Sterility | closed sanitary designs can support asepsis | exposed cake filters are difficult to keep aseptic; sealed sanitary membrane systems can support asepsis |
| Continuous operation | design-dependent; liquid flow can be continuous | rotary drums and cross-flow membrane systems can run continuously |
| Consumables | seals, cleaning agents and maintenance parts; no filter medium | filters, optional filter aids and cleaning agents |
| Capital cost | higher | **lower** |
| Small cells | difficult | **easier to separate** |
| Mechanical risk | many moving parts and seals that can fail; safety | few |

The decisive factor in therapeutic protein manufacture is usually **sterility**: a closed centrifuge can be cleaned and sterilised in place, whereas the rotary drum of Section 33 is open to the atmosphere. For large-volume, lower-value products such as antibiotics, filtration's lower capital cost and ability to handle fine cells generally wins.

**Why the conditions are unfavourable for cells.** Cell cultures are a hard case because cells may not be very dense, the medium can itself be dense, and bacterial cells are small. Since Section 36 shows that settling velocity scales with $D_p^2$ and with $(\rho_p-\rho_l)$, small size and low density difference are both directly punishing. The limitations are overcome by designing large centrifuges operating at high rotational speeds — with physical and safety limits capping how far this can go.

### Link to other topics

Replacing gravity with a much larger artificial body force to accelerate a transport process is the same device as using a pressure difference to drive filtration faster than capillarity would (Section 34), and in both cases the equipment, not the physics, sets the limit.

### Summary

Centrifuges separate by density, which is unfavourable for cells because they are small and nearly as dense as their medium, so bioprocessing relies on high-speed designs. Tubular bowls give the highest force and are easy to clean but run batchwise; disc stacks give far higher throughput by splitting the liquid into 0.3 mm layers and run continuously.

## Section 36: Stokes settling and the throughput of a tubular bowl centrifuge

### Intuition

A particle denser than the surrounding liquid sinks. Three forces act: gravity pulls it down, buoyancy pushes it up, and drag opposes whatever motion results. Because the particle is tiny, it reaches terminal velocity almost instantly, so the three forces balance at all times and the problem reduces to algebra rather than dynamics.

The result, Stokes' law, shows the velocity scales with the *square* of the diameter. Halving the particle size slows settling fourfold — which is why bacteria are so much harder to spin down than animal cells.

A centrifuge changes only one thing in that balance: it replaces $g$ with the much larger centrifugal acceleration $r\omega^2$. Everything else carries over unchanged.

Separation then becomes a race. A particle entering the bowl has a limited time before the flow carries it out, and it must reach the wall within that time. Capture requires **sedimentation time < residence time**, and that single inequality sets the maximum flow rate the machine can handle.

*Analogy:* crossing a moving walkway diagonally — you are captured by the far side only if you can walk across before the belt carries you off the end. The analogy breaks down because the centrifugal "walking speed" increases with radius, so the particle accelerates as it crosses, which is why the derivation produces a logarithm.

### Derivation

Notation: $D_p$ particle diameter, $\rho_p$ particle density, $\rho_l$ liquid density, $\mu$ liquid viscosity, $u$ velocity, $\omega$ angular velocity, $r$ radius, $g$ gravitational acceleration.

#### Sedimentation under gravity

**Step 1: the forces.** A spherical particle moving at velocity $u$ in a Newtonian fluid at low Reynolds number experiences a **frictional (drag) force**
$$F_d = 3\pi\mu D_p u \tag{52}$$
Gravity and buoyancy act in opposite directions:
$$F_g = -m_p g = -V_p\rho_p g, \qquad F_b = V_p\rho_l g \tag{53}$$

**Step 2: terminal velocity.** At low $Re$, **inertial effects are negligible**, so the net force on the particle is always zero. Balancing drag against the net of gravity and buoyancy:
$$3\pi\mu D_p u_g = V_p(\rho_p-\rho_l)g = \frac{\pi}{6}D_p^3(\rho_p-\rho_l)g \tag{54}$$
using $V_p = \tfrac{\pi}{6}D_p^3$ for a sphere.

**Step 3: solve for $u_g$.** Dividing through by $3\pi\mu D_p$:
$$\boxed{\;u_g = \frac{D_p^2(\rho_p-\rho_l)g}{18\mu}\;}\tag{55}$$

This is **Stokes' law** for the sedimentation velocity in a gravitational field. The particle sediments only if $\rho_p > \rho_l$; if the particle is lighter it rises.

#### Sedimentation in a centrifuge

**Step 4: replace the acceleration.** In a centrifuge the fluid rotates with the bowl at angular velocity $\omega$, so a particle at radius $r$ experiences a centrifugal acceleration
$$a_c = r\omega^2 \tag{56}$$
The force balance is unchanged apart from the body force, so $g$ is simply replaced by $a_c$:
$$u_c = \frac{D_p^2(\rho_p-\rho_l)r\omega^2}{18\mu} = \frac{D_p^2(\rho_p-\rho_l)Gg}{18\mu} \tag{57}$$
where the **G-factor** $G = a_c/g$ is the ratio of centrifugal to gravitational acceleration. Note that $u_c$ depends on $r$: **the particle speeds up as it moves outwards.**

![A spherical particle with buoyancy force upwards and gravitational force downwards](../figs/AB-36-stokes-forces.png)

#### Throughput of a tubular bowl

![Tubular bowl geometry: feed enters at the base at inner radius r₁, liquid discharges at the top, the bowl wall sits at r₂, the liquid layer has height h, and a particle follows a curved trajectory outwards](../figs/AB-36-tubular-geometry.png)

**Step 5: the capture condition.** For a particle to be captured, it must hit the outer wall before the feed flow pushes it out of the tube:
$$t_{\text{sed}} < t_{\text{res}} \tag{58}$$

**Step 6: the cut-off time.** Define $t_{\text{cut}}$ as the time for a particle starting at the *mid-point* of the liquid layer, $r = (r_1+r_2)/2$, to reach the wall at $r_2$. Since $dr/dt = u_c(r)$ from (57), the variables separate:
$$\int_{(r_1+r_2)/2}^{r_2}\frac{dr}{r} = \frac{D_p^2(\rho_p-\rho_l)\omega^2}{18\mu}\int_0^{t_{\text{cut}}}dt$$
The left side integrates to a logarithm, giving
$$t_{\text{cut}} = \frac{18\mu}{D_p^2(\rho_p-\rho_l)\omega^2}\ln\!\left(\frac{2r_2}{r_1+r_2}\right) \tag{59}$$

The logarithm follows from radial velocity being proportional to radius. Starting at $(r_1+r_2)/2$ defines a representative radial-midpoint criterion; particles starting closer to $r_1$ take longer. With uniform concentration and axial velocity across the annulus, the midpoint criterion corresponds to about 54 % capture in this geometry, not complete clarification.

**Step 7: the residence time.**
$$t_{\text{res}} = \frac{V_c}{Q}, \qquad V_c = \pi(r_2^2-r_1^2)h \tag{60}$$
with $Q$ the volumetric flow rate and $h$ the height of the liquid layer.

**Step 8: the maximum throughput.** Substituting (59) and (60) into the capture condition (58) gives $V_c/Q > t_{\text{cut}}$, so
$$Q < Q_{\text{cut}} = \frac{V_c}{t_{\text{cut}}} = \frac{D_p^2(\rho_p-\rho_l)\omega^2}{18\mu\,\ln\!\left(\dfrac{2r_2}{r_1+r_2}\right)}\,\pi(r_2^2-r_1^2)h \tag{61}$$

$Q_{\text{cut}}$ is the throughput corresponding to the chosen radial-midpoint capture criterion, not guaranteed complete cell removal. Under the same ideal plug-flow assumptions, capture from the innermost radius requires replacing the logarithm by $\ln(r_2/r_1)$.

### Motivation and explanation

**Reading equation (61).** Throughput rises with $\omega^2$, with $D_p^2$, with the density difference, and with the bowl volume; it falls with viscosity. Every one of these is unfavourable for a bacterial culture (Section 35), which is why such large machines are needed for such modest flows.

**What the criterion means.** Smaller particles settle more slowly, but entry radius also affects capture. Here the midpoint throughput is 0.343 L/min, whereas the innermost-radius ideal capture criterion gives 0.159 L/min. Actual recovery also depends on particle-size distribution, flow and hindered settling.

**Where the derivation fails.** It assumes laminar settling (low $Re$), spherical and non-interacting particles, uniform plug flow through the bowl, and no re-entrainment of deposited solids. Real feeds are concentrated enough that particles hinder one another, and flow in the bowl is not plug flow, so (61) is an optimistic estimate.

### Worked example

*A laboratory tubular bowl centrifuge.* Computed in Python.

**Given:** $r_1 = 16.5$ mm, $r_2 = 22.2$ mm, $h = 115$ mm, $\omega = 10\,000$ rpm. Bacteria of $D_p = 0.7$ µm, $\rho_p = 1.340\times10^3$ kg m⁻³, in broth of $\rho_l = 1.010\times10^3$ kg m⁻³ and $\mu = 10^{-3}$ Pa s.

**(a) Centrifugal acceleration at $r_2$.** Convert the rotation rate first: $\omega = 2\pi\times10\,000/60 = 1047$ rad s⁻¹.
$$a_c = r_2\omega^2 = 0.0222\times1047^2 = 2.43\times10^{4}\ \mathrm{m\,s^{-2}} = 2482\,g$$

**(b) Cut-off flow rate.** From (59) and (60):
$$t_{\text{cut}} = 13.9\ \mathrm{s}, \qquad V_c = \pi(0.0222^2-0.0165^2)(0.115) = 7.97\times10^{-5}\ \mathrm{m^3}$$
$$Q_{\text{cut}} = \frac{7.97\times10^{-5}}{13.9} = 5.7\times10^{-6}\ \mathrm{m^3\,s^{-1}} = 5.7\ \mathrm{mL\,s^{-1}} = 0.34\ \mathrm{L\,min^{-1}}$$

**Sense check.** This sits at the bottom of the 0.4–40 L/min range quoted for a 10 cm tubular bowl (Section 35), which is right for a laboratory machine of 4.4 cm bowl diameter separating sub-micron bacteria.

**Why centrifugation is necessary at all.** Take a larger bacterium, $D_p = 1$ µm, $\rho_p = 1.3\times10^3$ kg m⁻³, in water. From (55):
$$u_g = \frac{(10^{-6})^2(300)(9.81)}{18\times10^{-3}} = 1.6\times10^{-7}\ \mathrm{m\,s^{-1}} = 0.16\ \mathrm{\mu m\,s^{-1}}$$
Settling 0.1 m under gravity would take **7 days**. In a centrifuge at $G = 10\,000$, equation (57) gives $u_c = 1.6\times10^{-3}$ m s⁻¹, and the same 0.1 m takes **about 1 minute**. That ratio of $10^4$ is the entire justification for the equipment.

### Link to other topics

Equation (58) is a competition of timescales — a Damköhler-type comparison between the time for a process to complete and the time available in the vessel. The same reasoning sizes any flow-through separator, and the particle accelerating as it crosses is what distinguishes a centrifuge from a gravity settler.

### Summary

A force balance at negligible inertia gives Stokes' law, $u \propto D_p^2(\rho_p-\rho_l)/\mu$, and a centrifuge simply substitutes $r\omega^2$ for $g$ — worth a factor of $10^4$, turning a week of settling into a minute. Requiring sedimentation to beat residence time gives the maximum throughput, equation (61).

## Section 37: Sigma theory and centrifuge scale-up

### Intuition

To compare two centrifuges fairly, they must be compared on the same feed. If a figure of merit could be found that depends only on the machine, then the ratio of throughputs of any two centrifuges on *any* common sample would equal the ratio of those figures — and scale-up would reduce to matching one number.

The trick is to notice that the sample's properties enter $Q_{\text{cut}}$ only through the combination that forms the **gravitational settling velocity** $u_g$. Multiplying and dividing by $u_g$ therefore isolates everything else, and what remains is the machine.

The machine factor has units of area. With the convention used here, $Q_{\text{cut}}=2\Sigma u_g$, the corresponding ideal gravity-settler area is $A_{\mathrm{eq}}=Q_{\text{cut}}/u_g=2\Sigma$. Thus $\Sigma=32.4$ m² corresponds to about 64.8 m² of gravity-settling area for the same stated capture criterion.

*Analogy:* expressing a device's performance as the equivalent area of a simpler separator. The comparison is conditional on matching feed, capture criterion and ideal flow assumptions; it does not make real centrifuge scale-up exact.

### Derivation

**Step 1: start from the cut-off flow rate.** From Section 36, equation (61):
$$Q_{\text{cut}} = \frac{D_p^2(\rho_p-\rho_l)\omega^2}{18\mu\,\ln\!\left(\dfrac{2r_2}{r_1+r_2}\right)}\,\pi(r_2^2-r_1^2)h \tag{62}$$

**Step 2: multiply and divide by $u_g$.** The gravitational settling velocity of the same particle is
$$u_g = \frac{D_p^2(\rho_p-\rho_l)g}{18\mu} \tag{63}$$
Writing (62) as itself multiplied by $u_g/u_g$ and substituting (63) in the denominator, the whole group $D_p^2(\rho_p-\rho_l)/18\mu$ cancels, leaving $g$ behind:
$$Q_{\text{cut}} = \frac{\pi(r_2^2-r_1^2)h\,\omega^2}{g\,\ln\!\left(\dfrac{2r_2}{r_1+r_2}\right)}\;u_g \tag{64}$$

**Step 3: define $\Sigma$.** Writing (64) as $Q_{\text{cut}} = 2\Sigma u_g$:
$$\boxed{\;\Sigma(r_1,r_2,h,\omega) = \frac{\pi(r_2^2-r_1^2)h\,\omega^2}{2g\,\ln\!\left(\dfrac{2r_2}{r_1+r_2}\right)}\;}\tag{65}$$

Two properties follow immediately:
- **$\Sigma$ depends only on the centrifuge**, not on the sample. Every sample-dependent quantity has been collected into $u_g$.
- **$\Sigma$ has dimensions of area.** Dimensionally $Q = 2\Sigma u_g$ is (volume/time) = (area)(velocity), so the equivalent ideal gravity-settler area at this throughput is **$2\Sigma$**, under the stated $Q_{\text{cut}}=2\Sigma u_g$ convention.

**Step 4: the scale-up rule.** For two centrifuges processing the **same sample**, $u_g$ is common:
$$Q_1 = 2\Sigma_1 u_g, \qquad Q_2 = 2\Sigma_2 u_g$$
Dividing, $u_g$ cancels:
$$\frac{Q_1}{Q_2} = \frac{\Sigma_1}{\Sigma_2} \tag{66}$$

**To increase the throughput of a centrifuge by a factor $X$, $\Sigma$ must increase by the same factor $X$.** This ideal ratio requires the same feed settling properties, capture criterion and flow assumptions; real machines can need empirical efficiency corrections.

### Motivation and explanation

**The area factor depends on the design and convention.** Equation (65) uses $Q=2\Sigma u_g$. For a disc stack, state the full equivalent area $A_{\mathrm{eq,disc}}$, defined by $Q=A_{\mathrm{eq,disc}}u_g$:
$$A_{\mathrm{eq,disc}} = \frac{2\pi\omega^2(N-1)}{3g\tan\theta}\left(r_2^3-r_1^3\right) \tag{67}$$
with $N$ the number of discs, $r_2$ and $r_1$ the outer and inner disc radii and $\theta$ the disc angle to the rotation axis. Under the half-area convention of (65), use $\Sigma_{\mathrm{disc}}=A_{\mathrm{eq,disc}}/2$.

![A disc-stack centrifuge showing the feed, overflow, disc radius r, half-cone angle θ, and solids collecting at the bowl wall](../figs/AB-37-disc-stack-geometry.png)

Equation (67) explains the throughput figures in Section 35. $\Sigma$ scales with $(N-1)$, so a stack of a hundred discs has roughly a hundred times the equivalent area of a single surface, and it scales with $r^3$ rather than $r^2$. That is how a disc stack delivers 800 L/min at only 5500 g while a tubular bowl at 15 000 g manages 80 L/min — **equivalent settling area, which includes the rotation speed, sets the ideal throughput for a given feed and capture criterion.**

**$\Sigma$ is convention-dependent.** The derivation of $t_{\text{cut}}$ took a particle starting at the mid-point of the liquid layer, which is somewhat arbitrary. Different conventions give different expressions; another in common use is
$$\Sigma = \frac{\pi\omega^2 h}{2g}\left(3r_2^2+r_1^2\right) \tag{68}$$
For the example below, (68) gives 35.4 m² against 32.4 m² from (65), about 9 % higher. Quote the value with its definition and capture criterion. Their difference is not merely a universal prefactor: it depends on the radius ratio, so scale-up ratios calculated from different geometric expressions need not agree for dissimilar bowls.

**When ratios are robust.** A common constant prefactor cancels from a ratio. Both tubular-bowl expressions also scale as $L^3\omega^2$ for geometrically similar bowls, so they give the same speed ratio in the doubled-size example. Dissimilar geometries require matched capture criteria, and real scale-up requires checking flow and separation-efficiency corrections.

### Worked example

*Scaling up the laboratory centrifuge of Section 36.* Computed in Python.

**(a) Calculate $\Sigma$** for $r_1 = 16.5$ mm, $r_2 = 22.2$ mm, $h = 115$ mm, $\omega = 10\,000$ rpm $= 1047$ rad s⁻¹. From (65):
$$\Sigma = \frac{\pi(0.0222^2-0.0165^2)(0.115)(1047)^2}{2\times9.81\times\ln\!\left(\dfrac{2\times0.0222}{0.0222+0.0165}\right)} = 32.4\ \mathrm{m^2}$$

**Check.** With the sample of Section 36, $u_g = 8.81\times10^{-8}$ m s⁻¹, so $2\Sigma u_g = 5.7\times10^{-6}$ m³ s⁻¹ — exactly the $Q_{\text{cut}}$ computed there. The factorisation is consistent.

**Interpretation.** A bowl 4.4 cm across has $\Sigma=32.4$ m² in the chosen half-area convention. Its corresponding ideal gravity-settler area at the midpoint throughput is $2\Sigma=64.8$ m².

**(b) What speed does a doubled centrifuge need to match the smaller one's throughput?** The larger machine has double the physical dimensions: $r_1 = 33.0$ mm, $r_2 = 44.4$ mm, $h = 230$ mm.

Matching throughput on the same sample means $\Sigma_2 = \Sigma_1$, by (66). Write $\Sigma = f(r_1,r_2,h)\,\omega^2/2g$ with
$$f = \frac{\pi(r_2^2-r_1^2)h}{\ln\!\left(\dfrac{2r_2}{r_1+r_2}\right)}$$
The logarithm depends only on the *ratio* of radii, so it is unchanged when every dimension doubles. The numerator scales as $L^2\times L = L^3$, so
$$\frac{f_2}{f_1} = 2^3 = 8$$
Setting $f_1\omega_1^2 = f_2\omega_2^2$:
$$\omega_2 = \omega_1\sqrt{\frac{f_1}{f_2}} = \frac{\omega_1}{\sqrt 8} = \frac{10\,000}{2.83} = 3540\ \mathrm{rpm}$$

**Check:** $\Sigma_2 = 32.4$ m² $= \Sigma_1$. ✓

**Interpretation.** Doubling every dimension multiplies the geometric factor by 8, so the same $\Sigma$ is reached at $1/\sqrt8 = 35\%$ of the speed. This is the quantitative version of the trade in Section 35: **bigger bowls do the same job more slowly**, which is fortunate, because the hoop stress in the bowl wall scales as $r^2\omega^2$ and would otherwise be prohibitive. Here that product falls by a factor of $4/8 = 0.5$, so the larger bowl is *less* stressed while matching the duty.

### Link to other topics

Expressing a device's performance as an equivalent area of a simpler device is the same move as the HETP of a distillation column or the NTU of a heat exchanger: a dimensional figure of merit that separates equipment performance from the properties of what passes through it, so that scale-up becomes a matter of matching one number.

### Summary

Factorising $Q_{\text{cut}}=2\Sigma u_g$ separates the ideal machine factor from the feed settling velocity. In this convention the equivalent gravity-settler area is $2\Sigma$.

## Conclusion

Sigma theory supports scale-up when feed properties, separation criteria and geometric conventions remain consistent. The next unit develops cell disruption.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

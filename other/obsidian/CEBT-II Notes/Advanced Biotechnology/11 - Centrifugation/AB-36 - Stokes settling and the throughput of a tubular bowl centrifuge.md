[Previous](<AB-35 - Centrifuge designs for cell removal.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-37 - Sigma theory and centrifuge scale-up.md>)

<!-- note-content:start -->
# Section 36: Stokes settling and the throughput of a tubular bowl centrifuge

## Intuition

A particle denser than the surrounding liquid sinks. Three forces act: gravity pulls it down, buoyancy pushes it up, and drag opposes whatever motion results. Because the particle is tiny, it reaches terminal velocity almost instantly, so the three forces balance at all times and the problem reduces to algebra rather than dynamics.

The result, Stokes' law, shows the velocity scales with the *square* of the diameter. Halving the particle size slows settling fourfold — which is why bacteria are so much harder to spin down than animal cells.

A centrifuge changes only one thing in that balance: it replaces $g$ with the much larger centrifugal acceleration $r\omega^2$. Everything else carries over unchanged.

Separation then becomes a race. A particle entering the bowl has a limited time before the flow carries it out, and it must reach the wall within that time. Capture requires **sedimentation time < residence time**, and that single inequality sets the maximum flow rate the machine can handle.

*Analogy:* crossing a moving walkway diagonally — you are captured by the far side only if you can walk across before the belt carries you off the end. The analogy breaks down because the centrifugal "walking speed" increases with radius, so the particle accelerates as it crosses, which is why the derivation produces a logarithm.

## Derivation

Notation: $D_p$ particle diameter, $\rho_p$ particle density, $\rho_l$ liquid density, $\mu$ liquid viscosity, $u$ velocity, $\omega$ angular velocity, $r$ radius, $g$ gravitational acceleration.

### Sedimentation under gravity

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

### Sedimentation in a centrifuge

**Step 4: replace the acceleration.** In a centrifuge the fluid rotates with the bowl at angular velocity $\omega$, so a particle at radius $r$ experiences a centrifugal acceleration
$$a_c = r\omega^2 \tag{56}$$
The force balance is unchanged apart from the body force, so $g$ is simply replaced by $a_c$:
$$u_c = \frac{D_p^2(\rho_p-\rho_l)r\omega^2}{18\mu} = \frac{D_p^2(\rho_p-\rho_l)Gg}{18\mu} \tag{57}$$
where the **G-factor** $G = a_c/g$ is the ratio of centrifugal to gravitational acceleration. Note that $u_c$ depends on $r$: **the particle speeds up as it moves outwards.**

![A spherical particle with buoyancy force upwards and gravitational force downwards](../figs/AB-36-stokes-forces.png)

### Throughput of a tubular bowl

![Tubular bowl geometry: feed enters at the base at inner radius r₁, liquid discharges at the top, the bowl wall sits at r₂, the liquid layer has height h, and a particle follows a curved trajectory outwards](../figs/AB-36-tubular-geometry.png)

**Step 5: the capture condition.** For a particle to be captured, it must hit the outer wall before the feed flow pushes it out of the tube:
$$t_{\text{sed}} < t_{\text{res}} \tag{58}$$

**Step 6: the cut-off time.** Define $t_{\text{cut}}$ as the time for a particle starting at the *mid-point* of the liquid layer, $r = (r_1+r_2)/2$, to reach the wall at $r_2$. Since $dr/dt = u_c(r)$ from (57), the variables separate:
$$\int_{(r_1+r_2)/2}^{r_2}\frac{dr}{r} = \frac{D_p^2(\rho_p-\rho_l)\omega^2}{18\mu}\int_0^{t_{\text{cut}}}dt$$
The left side integrates to a logarithm, giving
$$t_{\text{cut}} = \frac{18\mu}{D_p^2(\rho_p-\rho_l)\omega^2}\ln\!\left(\frac{2r_2}{r_1+r_2}\right) \tag{59}$$

The logarithm follows from radial velocity being proportional to radius. Starting at $(r_1+r_2)/2$ defines a representative radial-midpoint criterion; particles starting closer to $r_1$ take longer. With uniform concentration and axial velocity across the annulus, the midpoint criterion corresponds to about 54 % capture in this geometry, not complete clarification.

The particle's radial speed increases as it moves outward because the local driving force increases, not because it stores appreciable momentum over the settling trajectory. The terminal-velocity approximation balances drag at each position. Integrating $dr/u_c(r)$ therefore adds the time spent in each small radial interval, including the slower inner part; using only the outer-wall speed would underestimate travel time.

**Step 7: the residence time.**
$$t_{\text{res}} = \frac{V_c}{Q}, \qquad V_c = \pi(r_2^2-r_1^2)h \tag{60}$$
with $Q$ the volumetric flow rate and $h$ the height of the liquid layer.

**Step 8: the maximum throughput.** Substituting (59) and (60) into the capture condition (58) gives $V_c/Q > t_{\text{cut}}$, so
$$Q < Q_{\text{cut}} = \frac{V_c}{t_{\text{cut}}} = \frac{D_p^2(\rho_p-\rho_l)\omega^2}{18\mu\,\ln\!\left(\dfrac{2r_2}{r_1+r_2}\right)}\,\pi(r_2^2-r_1^2)h \tag{61}$$

$Q_{\text{cut}}$ is the throughput corresponding to the chosen radial-midpoint capture criterion, not guaranteed complete cell removal. Under the same ideal plug-flow assumptions, capture from the innermost radius requires replacing the logarithm by $\ln(r_2/r_1)$.

## Motivation and explanation

**Reading equation (61).** Throughput rises with $\omega^2$, with $D_p^2$, with the density difference, and with the bowl volume; it falls with viscosity. Every one of these is unfavourable for a bacterial culture (Section 35), which is why such large machines are needed for such modest flows.

**What the criterion means.** Smaller particles settle more slowly, but entry radius also affects capture. Here the midpoint throughput is 0.343 L/min, whereas the innermost-radius ideal capture criterion gives 0.159 L/min. Actual recovery also depends on particle-size distribution, flow and hindered settling.

**Where the derivation fails.** It assumes laminar settling (low $Re$), spherical and non-interacting particles, uniform plug flow through the bowl, and no re-entrainment of deposited solids. Real feeds are concentrated enough that particles hinder one another, and flow in the bowl is not plug flow, so (61) is an optimistic estimate.

### Why enhanced acceleration changes feasible separation times

Stokes settling gives velocity proportional to acceleration at fixed particle diameter, density contrast and viscosity. For an illustrative $1\,\mu\mathrm m$ sphere with density contrast $300\,\mathrm{kg\,m^{-3}}$ in a liquid of viscosity $10^{-3}\,\mathrm{Pa\,s}$, the gravity settling speed is $1.64\times10^{-7}\,\mathrm{m\,s^{-1}}$. Traversing $0.1\,\mathrm m$ would take approximately 7.08 days.

A uniform acceleration of $10^4g$ would reduce that ideal traversal time to approximately 61.2 seconds. A real centrifuge has acceleration $r\omega^2$ varying with radius, so its transit time must be integrated along the radial path. The constant-acceleration comparison explains the equipment's purpose without replacing that design calculation.

## Link to other topics

Equation (58) is a competition of timescales — a Damköhler-type comparison between the time for a process to complete and the time available in the vessel. The same reasoning sizes any flow-through separator, and the particle accelerating as it crosses is what distinguishes a centrifuge from a gravity settler.

## Summary

A force balance at negligible inertia gives Stokes' law, $u \propto D_p^2(\rho_p-\rho_l)/\mu$, and a centrifuge simply substitutes $r\omega^2$ for $g$ — worth a factor of $10^4$, turning a week of settling into a minute. Requiring sedimentation to beat residence time gives the maximum throughput, equation (61).
<!-- note-content:end -->

[Previous](<AB-35 - Centrifuge designs for cell removal.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-37 - Sigma theory and centrifuge scale-up.md>)

# Centrifugation — reading 11.1

[Previous](<../../../../../notes/Advanced Biotechnology/10 - Bioprocessing overview and filtration/Complete section.md>) · [Subject index](<../../../../../notes/Advanced Biotechnology/README.md>) · [Next](<../../../../../notes/Advanced Biotechnology/11 - Centrifugation/Complete section.md>)

<!-- reading-content:start -->
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

![A continuous tubular bowl centrifuge: feed enters at the base, the light phase leaves at the top and the heavy phase is discharged separately](figs/AB-35-tubular-bowl.png)

- A **rotating tube** with a nozzle at the base where feed is introduced.
- As the liquid flows upwards, particles are spun outwards and collide with the wall of the bowl, where they are retained.
- Clarified liquid continues upwards and leaves over a **weir** at the top.
- Two timescales compete: the **residence time**, which decreases as the flow rate rises, and the **sedimentation time**, which is shorter for larger or denser particles, higher rotation speed and lower viscosity. **Particles are separated efficiently if the sedimentation time is shorter than the residence time** — the condition Section 36 turns into a maximum throughput.

Liquid feed and clarification can be continuous, while retained solids accumulate on the wall and require periodic shutdown for removal. A separate heavy-liquid outlet can provide continuous liquid–liquid separation; it does not by itself remove deposited solids.

Tubular bowls reach very high centrifugal forces — up to about 16 000 g — so they suit difficult separations. They are easy to clean, but foaming can be a problem.

#### Disc-stack centrifuge

![A disc-stack centrifuge in cross-section: feed enters down the centre, passes between conical discs, with light-liquid discharge at the top, heavy liquid and solids collected at the bowl wall, and a clean-in-place nozzle](figs/AB-35-disc-stack.png)

- The bowl contains **conical sheets of metal (discs) stacked on top of each other**, with clearances of approximately **0.3 mm**.
- As the bowl rotates, the discs **split the liquid into thin layers**. Denser liquid containing the solids is displaced outwards along the underside of each disc, while lighter liquid remains close to the centre.
- Both streams are withdrawn continuously.
- Solids discharge depends on the design: a solids-retaining bowl is opened for manual removal; a self-cleaning bowl ejects solids intermittently through peripheral ports; a nozzle separator discharges solids continuously. A heavy-liquid outlet separates a liquid phase and is not equivalent to a solids outlet.

The discs are the whole point of the design: they reduce the distance a particle must travel before it reaches a collecting surface from the full bowl radius to the 0.3 mm gap. Section 37 shows that this is what gives the disc stack its large effective area.

Foam can be controlled, and it is easier to run continuously than a tubular bowl, but it is **harder to clean** because of the stack.

#### Comparison

![Table of bowl diameter, speed, maximum centrifugal force, liquid throughput and motor size for tubular bowl and disc-stack centrifuges](figs/AB-35-comparison-table.png)

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

**Why speed falls as diameter rises.** The bowl wall carries a hoop stress proportional to $`\rho r^2\omega^2`$. For a fixed allowable stress, the maximum angular velocity scales as $`1/r`$, so the maximum centrifugal acceleration $`r\omega^2`$ scales as $`1/r`$ as well. At the same allowable stress and comparable construction, bigger bowls therefore have a lower maximum g-force. The gain from building larger is area, not force, and the table shows exactly that trade.

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

**Why the conditions are unfavourable for cells.** Cell cultures are a hard case because cells may not be very dense, the medium can itself be dense, and bacterial cells are small. Since Section 36 shows that settling velocity scales with $`D_p^2`$ and with $`(\rho_p-\rho_l)`$, small size and low density difference are both directly punishing. The limitations are overcome by designing large centrifuges operating at high rotational speeds — with physical and safety limits capping how far this can go.

### Link to other topics

Replacing gravity with a much larger artificial body force to accelerate a transport process is the same device as using a pressure difference to drive filtration faster than capillarity would (Section 34), and in both cases the equipment, not the physics, sets the limit.

### Summary

Centrifuges separate by density, which is unfavourable for cells because they are small and nearly as dense as their medium, so bioprocessing relies on high-speed designs. Tubular bowls give the highest force and are easy to clean but run batchwise; disc stacks give far higher throughput by splitting the liquid into 0.3 mm layers and run continuously.
<!-- reading-content:end -->

[Previous](<../../../../../notes/Advanced Biotechnology/10 - Bioprocessing overview and filtration/Complete section.md>) · [Subject index](<../../../../../notes/Advanced Biotechnology/README.md>) · [Next](<../../../../../notes/Advanced Biotechnology/11 - Centrifugation/Complete section.md>)

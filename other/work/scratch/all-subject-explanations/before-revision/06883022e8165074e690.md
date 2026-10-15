[Previous](<ET-32 - Vapour–liquid equilibrium near critical points.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Section 33: Retrograde condensation and evaporation

## Intuition

For a pure substance, the critical point is the top of the vapour-pressure curve, so it is both the highest temperature and the highest pressure at which two phases coexist. For a mixture, the envelope is a loop whose bubble and dew branches meet at the critical point. That meeting point is generally *not* at the top or the right-hand edge of the loop. The loop bulges beyond it: upward on the bubble side, rightward on the dew side.

Near those bulges, the lines of constant liquid fraction ("quality lines") all converge on the critical point. A path that runs past the critical point therefore crosses those lines in an unusual order. The amount of liquid first rises, then falls, as you move in what is normally the "less liquid" direction.

*Analogy: walking around a hill rather than over it.* The quality lines fan out from the critical point like contours. If you pass beside the critical point, rather than through the middle of the envelope, you go up and back down the same contours. The analogy breaks down because the "height" (liquid fraction) is fixed by the lever rule on tie lines in other planes, not by a single surface.

## Derivation

The behaviour follows from the shape of the envelope, read from a measured or EOS-computed diagram. For ethane–heptane at 58.71 mol % ethane, the values below are read from the graph and are therefore approximate:
- critical point ≈ 76 bar, ≈ 460 K;
- cricondenbar $`P_{\max}`$ ≈ 79 bar, ≈ 445 K, on the bubble side of the critical point;
- cricondentherm $`T_{\max}`$ ≈ 485 K, ≈ 55 bar, on the dew side.

![Ethane–n-heptane at 58.71 mol % ethane: bubble and dew curves meet at the critical point, which lies between the cricondenbar (Pmax) and the cricondentherm (Tmax); paths (i)–(iii) from points a and b](../figs/ET-33-ethane-heptane-envelope.png)

**Path (i): cool at ~70 bar from point a** (just on the dew side, right of the critical point). The vapour crosses the dew curve, liquid appears and grows, and the system leaves through the bubble curve as all liquid. Normal behaviour: vapour → vapour + liquid → liquid.

**Path (ii): cool at ~78 bar from point b** (between the critical point and the cricondenbar, on the bubble side). The fluid starts as liquid-like. Cooling crosses the bubble curve, so vapour appears, then the path leaves through the bubble curve again near $`P_{\max}`$ and the system is all liquid once more. **Retrograde evaporation:** liquid → liquid + vapour → liquid, on cooling.

**Path (iii): reduce pressure at ~473 K from point a** (between the critical temperature and the cricondentherm). Lowering the pressure crosses the upper part of the dew curve, so liquid condenses. Further reduction brings the path out through the lower dew curve, and the liquid re-evaporates. **Retrograde condensation:** vapour → vapour + liquid → vapour, on *decompression*.

The liquid fraction along (iii) rises from zero, peaks, and falls back to zero, all while the system is being decompressed.

## Motivation and explanation

**Why it can happen at all.** The phase rule allows it. With $`C = 2`$ and $`P = 2`$, there are two degrees of freedom, so the dew curve at fixed composition need not be monotonic in $`T`$ or $`P`$. For a pure substance ($`F = 1`$) the coexistence curve is a single line ending at $`T_c`$, and no retrograde region exists.

**Where it happens.**
- Retrograde condensation: only between the critical temperature and the cricondentherm.
- Retrograde evaporation: only between the critical pressure and the cricondenbar.

The more asymmetric the mixture (light + heavy components), the larger these regions, which is why ethane–heptane shows them clearly.

**Engineering consequences.**
- *Gas-condensate reservoirs.* Reservoir fluid often sits at path (iii)-type conditions, above the dew curve as a single phase. As the reservoir is produced and its pressure falls, liquid condenses in the rock, where it is largely trapped. The heavy components are the most valuable part of the fluid. Reservoirs are therefore often kept above the dew pressure by re-injecting gas.
- *Pipelines and pressure let-down.* Lowering the pressure of a rich gas can drop out liquid unexpectedly, which causes slugging in pipelines. Gas is "conditioned" (heavy components removed) so that its cricondentherm lies below the lowest pipeline temperature.
- *Design.* Simulators must compute the full envelope with an EOS. Interpolating between pure-component behaviours misses these effects entirely.

**Limits.** The exact positions of the critical point, cricondenbar and cricondentherm are sensitive to composition and to the EOS mixing-rule parameters. Read-off values here are approximate.

## Worked example

**Problem.** A natural-gas condensate behaves like the 58.71 % ethane–heptane mixture above. It sits in a reservoir at about 473 K and 75 bar, and is produced by lowering the pressure to 20 bar at constant temperature. Describe what happens, using the envelope.

**Answer, reading from the diagram (approximate).**
1. *75 bar, 473 K:* above the dew curve at this temperature, so single-phase, gas-like.
2. *About 70 bar:* the path meets the upper dew curve. The dew point is reached and liquid starts to condense, although the pressure is *falling*.
3. *Between ≈ 70 and ≈ 30 bar:* inside the envelope. The liquid fraction rises, peaks at intermediate pressure, then falls.
4. *About 30 bar:* the path meets the lower dew curve. The last liquid re-evaporates, and below this the fluid is again all vapour.

**Interpretation.** In a reservoir, the re-evaporation in step 4 rarely recovers the liquid. The liquid that condensed in steps 2–3 wets the rock and stays behind, and the gas that reaches the well has lost its heavy fraction. Operators therefore aim to keep the reservoir pressure above the upper dew point, around 70 bar here, for as long as possible.

## Link to other topics

Phase-envelope calculations underpin gas processing, enhanced oil recovery and supercritical-fluid extraction. Retrograde behaviour is one of the clearest demonstrations that mixture phase equilibria cannot be pieced together from pure-component diagrams. Section 34 returns to the liquid phase and to solutes that are not volatile at all: dissolved solids and ions.

## Summary

For a mixture, the critical point, the maximum two-phase pressure (cricondenbar) and the maximum two-phase temperature (cricondentherm) are different points on the envelope. Between them, cooling can evaporate liquid and decompression can condense it. These retrograde effects are allowed by the extra degree of freedom of a binary, are strongest in asymmetric mixtures, and matter in practice for gas-condensate reservoirs and gas pipelines.

## Conclusion

Mixture phase envelopes near critical points cannot be pieced together from pure-component behaviour: they need an equation of state for both phases, and they show retrograde effects that matter for gas-condensate reservoirs and gas pipelines. The next part returns to the liquid phase and to solutes that are not volatile at all: dissolved solids and ions.
<!-- note-content:end -->

[Previous](<ET-32 - Vapour–liquid equilibrium near critical points.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

# Absorption-column equipment

## Overview

Assumed background: countercurrent absorption and equilibrium stages. Packed and tray columns create gas–liquid contact in different ways. Their usefulness depends as much on distribution, pressure drop and liquid handling as on nominal contact area.

## Intuition

Packing spreads liquid into films while leaving open paths for gas. Trays force gas through pools or froths of liquid. In either case, surface area helps only when gas and liquid actually meet there. A dry packing surface or a bypass channel contributes little to separation.

## Derivation

The equipment choice follows the way contact is generated. In a packed column, liquid enters a distributor above the bed and descends over packing surfaces. Gas enters below the support and rises through the voids. The support holds the bed without blocking drainage; a hold-down prevents lifting of packing at high gas flow.

![Packed tower and its supporting internals](../figs/u1-packed-column.png)

Random packing comprises dumped rings or saddles, including Raschig rings, Pall rings and Berl saddles. Structured packing arranges corrugated sheets or grids in repeatable channels. Its regular geometry can give better area utilisation and controlled flow paths, although cost and performance depend on the specific packing.

A liquid distributor is essential because the entering liquid otherwise wets a limited region. Redistributors between bed sections correct the cumulative development of uneven flow, particularly in tall beds. This follows directly from the rate law: if part of the bed has no wetted interface, the available transfer area is smaller than the geometrical area.

In a sieve-tray column, gas passes through holes into the liquid on each tray. A weir sets liquid depth; a downcomer carries overflow to the next tray while giving liquid a route separate from the rising gas.

![Sieve trays, weirs and downcomers](../figs/u1-tray-column.png)

The liquid residence and gas bubbling encourage mixing. Ideal-stage calculations describe the limiting performance of the leaving streams; actual tray performance requires an efficiency or a rate model because contact is finite.

## Motivation and explanation

| Design consideration | Packed-column tendency | Tray-column tendency |
|---|---|---|
| Pressure drop and holdup | Lower pressure drop and liquid inventory; useful for vacuum and hazardous liquids | Greater liquid holdup and pressure drop |
| Small diameter | Packing is relatively straightforward to install | Internal tray access and installation become difficult |
| Flow flexibility | Adequate liquid wetting is essential; distribution limits turndown | Often handles a wider liquid-flow range, subject to tray hydraulics |
| Corrosion and foaming | Suitable packing materials and lower holdup can help | Froth and downcomer behaviour require attention |
| Cleaning and solids | Fouling can obstruct narrow passages; packing may need replacement | Accessible trays are often easier to clean |
| Heat exchange and side withdrawal | More difficult to distribute locally | Cooling coils and side streams are easier to provide |

These are selection tendencies, not guarantees. Packing geometry, distributors, materials and operating conditions can outweigh a broad comparison. A larger nominal area can also raise hydraulic resistance or become poorly wetted. Indicative industrial tower dimensions can reach several metres in diameter and tens of metres in height, but those dimensions are outcomes of hydraulic and transfer calculations.

For measuring coefficients, a wetted-wall column offers a simpler geometry: a liquid film descends the wall while gas rises through the centre. Its interfacial area is well defined. The relatively small area per device makes it valuable for experiments rather than a default large-throughput absorber.

## Worked example

A corrosive gas must be scrubbed in a small tower under vacuum. Low pressure drop and corrosion-resistant packing favour a packed design. The reasoning does not stop at selecting packing: the distributor must still wet the bed throughout the anticipated liquid-flow range. If solvent flow becomes too low, adding bed height may mostly add dry surface, so the nominal transfer-area advantage disappears.

For a service that needs a cooling coil on each contacting section and an intermediate liquid withdrawal, trays offer more convenient access and control of each pool. The higher pressure drop then enters the energy and pressure-budget comparison.

## Link to other topics

The chosen packing supplies the effective interfacial area and hydraulic correlations used in rate-based sizing. Tray equipment connects the same gas–liquid equilibrium to equilibrium-stage and efficiency calculations.

## Conclusion

Choose hardware for the fluid service and operating range, then verify distribution and hydraulics. Transfer coefficients and wetted area belong to that actual equipment, not to an abstract tower independent of its internals.

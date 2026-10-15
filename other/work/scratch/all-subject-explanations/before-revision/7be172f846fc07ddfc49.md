[Previous](<AB-32 - Downstream processing — stages, logic and cost.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-34 - Dead-end filtration theory and filter sizing.md>)

<!-- note-content:start -->
# Section 33: Cell removal by filtration — equipment and operation

## Intuition

Dead-end filtration is the simplest solid–liquid separation: a barrier with openings smaller than the particles. Liquid passes, particles do not, and the two phases separate. Flow is driven by gravity or by an imposed pressure drop.

The difficulty is that the method destroys its own performance as it operates. Retained particles accumulate on the cloth as a **filter cake**, and that cake is itself a porous medium through which the liquid must now flow. Every particle removed makes the next one harder to remove. Flow declines as resistance increases. In the ideal finite-permeability Darcy model it remains positive at finite time; practical runs end when flux or capacity reaches an operating limit.

This is the defining feature of dead-end filtration and the reason for everything else in the note: filter aids exist to make the cake more porous, plate-and-frame presses are built to be opened and scraped, and rotary vacuum drums exist to remove the cake continuously.

*Analogy:* a sink strainer that slowly blocks with tea leaves. The analogy breaks down in an important way — the cake is not simply blockage. It is also an *active filter*, often finer than the cloth beneath it, so a filtration can improve in selectivity as it worsens in rate.

## Mechanism

![Fermentation broth flows towards a filter cloth; a precoat of filter aid lies on the cloth and filter aid particles are mixed into the broth, so the cake of removed solids and filter aid stays porous](../figs/AB-33-dead-end-filter.png)

**Dead-end filtration.** A physical barrier with openings smaller than the suspended particles impedes their motion while liquid flows past, separating the phases. The flow is driven by gravity or by a pressure drop across the filter.

**The cake problem.** The major issue is cake formation. As the cake builds, it imposes a greater resistance to liquid flow, so the throughput deteriorates during the run. At fixed pressure difference, flux decreases towards zero asymptotically in the ideal cake-filtration model. A practical run ends earlier at a throughput or capacity limit. Section 34 makes this quantitative.

![Kieselguhr particles: hollow, irregular diatom skeletons used as filter aid](../figs/AB-33-filter-aids.png)

**Two fixes for the cake**, both aimed at increasing its porosity:
- **Pre-coating.** The cloth is covered with a layer of filter aid before the run. This protects the cloth from blinding and improves efficiency, though it adds its own flow resistance.
- **Filter aids** added to the broth. **Kieselguhr** (diatomaceous earth) is the usual choice: naturally occurring, highly porous, irregular particles. Mixed into the broth, they are deposited along with the cells and hold the cake open, so the cake is more porous and less resistant.

The filter cloth itself is progressively covered by the cake, so after a short time it is the cake, not the cloth, that is doing the filtration.

### Equipment

![A plate-and-frame filter press, and a schematic showing cloth, plate, frame, feed, filter cake and filtrate](../figs/AB-33-plate-frame.png)

**Batch: plate-and-frame filter press.** Cloth is spread over plates and supported along ridges, which leave a free area for the filtrate to flow. Many plates in series give a large area in a compact unit, and cake builds on the upstream side of each cloth. When the space between plates is filled with cake, the press must be **dismantled and scraped**.

That is the limitation of the conventional exposed cake press: it is laborious and must be serviced frequently, and opening it makes aseptic operation difficult. It suits appropriate batch duties; enclosed sanitary filter designs require their own assessment.

![A rotary drum vacuum filter in cross-section: the drum rotates through a liquid reservoir, cake forms on the immersed portion, is washed, dewatered, and removed by a scraper](../figs/AB-33-rotary-drum.png)

**Continuous: rotary drum vacuum filter.** For large fermentations, the standard choice.

- A horizontal cylindrical drum, **0.5–3 m in diameter**, rotates slowly at **0.1–2 rpm**.
- A **vacuum is applied inside the drum**, drawing liquid from the immersed portion into the interior.
- As the drum rotates out of the reservoir, the cake on its surface is **sprayed with wash liquid**, recovering product held in the cake.
- Continued vacuum **dewaters** the washed cake.
- A **scraper** removes the cake before the surface re-enters the reservoir.

Each element of the drum therefore passes through cake formation, washing, dewatering and discharge once per revolution. The cake is removed continuously rather than accumulating, which is precisely what the batch press cannot do.

It handles large volumes, suits separation of organisms, and is cheap and easy to operate — **but it is difficult to operate aseptically**, since the drum surface is open to the atmosphere.

## Motivation and explanation

**Why rotation speed is the key variable.** Cake thickness at the scraper is set by how long each element spends immersed, which is fixed by the rotation rate. Rotating faster gives a thinner cake and so a higher flux per unit area, but less time for washing and dewatering, so more product is lost in the wet cake and the discharged solids are wetter. Rotating slower gives better washing and drier cake at lower throughput. The 0.1–2 rpm range is the compromise, and the right value depends on whether product recovery or throughput dominates the economics.

**Why filter aids are a compromise.** Kieselguhr increases cake porosity and so raises the flow rate, but it also adds solid mass to be filtered and must be disposed of with the cells. If the product is *inside* the cells (Section 38), the filter aid ends up mixed with the material to be processed further, which is a nuisance. Filter aids are therefore used when the cells are waste, less readily when they are the product.

**Why asepsis is hard to maintain.** Both the plate-and-frame press and the rotary drum expose the cake to the atmosphere — one on dismantling, the other continuously. Where sterility matters, as in therapeutic protein manufacture, centrifugation in a closed vessel (Sections 35–37) or membrane filtration in a sealed module is used instead. The equipment described here belongs to large-volume, lower-value production such as antibiotics and enzymes.

## Link to other topics

The cake acting as a filter finer than the cloth that supports it is the same effect as a precoat layer in water treatment or a filter-aid body feed in clarification: the medium's role is to retain the first layer of solids, after which the solids do the separating.

## Summary

Dead-end filtration separates by size but degrades as it runs, because the retained cake becomes the dominant flow resistance. Filter aids and pre-coating keep the cake porous; plate-and-frame presses accept the cake and are dismantled to remove it; rotary drum vacuum filters remove it continuously with a scraper and so handle large volumes, at the cost of asepsis.
<!-- note-content:end -->

[Previous](<AB-32 - Downstream processing — stages, logic and cost.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-34 - Dead-end filtration theory and filter sizing.md>)

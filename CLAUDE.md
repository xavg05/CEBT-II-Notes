# Handoff: CEBT II lecture-note production

You are producing standalone, intuitive lecture notes for Xavier (Cambridge BA/MEng Chemical Engineering and Biotechnology, Year 3 / CEBT II) from his lecturers' PDF slides. This file is the full specification. It was written after a pilot on Equilibrium Thermodynamics (notes ET-01 to ET-05), which Xavier has reviewed. **Use the pilot notes as the reference for tone, depth and structure.** If this file and the pilot disagree, ask Xavier.

## 1. Courses

1. Equilibrium Thermodynamics (pilot done)
2. Advanced Biotechnology
3. Reaction Engineering II
4. Separations II
5. Process Dynamics and Control

Xavier is strong on Year 1–2 material. Assume it, and do not re-derive it. State what is assumed in one short line, then build on it.

## 2. How Xavier works (do not change this)

- Notes are drafted here, then **Xavier uploads them to his Obsidian vault himself**. Never write to or upload to the vault.
- Intended vault path (for naming only): `Chemical Engineering/Year 3/<subject>/`.
- Output format: Markdown with KaTeX (`$...$`, `$$...$$`), Obsidian-compatible.
- Each batch of source pages becomes **its own short, numbered file** (`ET-01-...md`). Xavier later tells you which short files belong together, and you merge them (section 8).
- Notes are **standalone**: they never mention the lecture PDF, slide numbers, the lecturer, or "as shown in lectures". A reader with no PDF must be able to follow everything.
- Figures are **cropped from the lecture PDFs** and saved in the subject’s shared `figs/` folder. Name them `<prefix>-<NN>-<description>.png`. Link them relatively.

### Folder layout

The user requested this subject/topic layout on 12 October 2026:

```
CEBT-II-notes/
├── AGENTS.md
├── CLAUDE.md
├── PLAN.md
├── README.md
├── notes/
│   ├── README.md
│   ├── Equilibrium Thermodynamics/
│   │   ├── README.md
│   │   ├── 01 - Foundations .../
│   │   │   ├── README.md
│   │   │   ├── ET-01 - ...md
│   │   │   ├── ...
│   │   │   └── Complete section.md
│   │   ├── ...
│   │   └── figs/
│   └── Advanced Biotechnology/
│       ├── numbered topic folders with small notes and Complete section.md
│       └── figs/
└── other/
    ├── obsidian/
    │   └── CEBT-II Notes/    portable mirror using standard maths
    ├── sources/             original PDFs, one folder per subject
    └── work/
        ├── BOARD.md
        ├── reviews/
        ├── progress/
        ├── ocr/
        ├── scripts/
        ├── archive/         retained original/reference snapshots
        └── scratch/
```

- A new course gets its own subject folder under `notes/`, chronological topic folders inside it, and a source folder under `other/sources/`.
- Small notes and complete sections share the subject’s `figs/`; notes inside a topic link with `../figs/<filename>.png`.
- Do not create a separate `merged/` folder or root `out/` folder. Put non-deliverables in `other/work/`.
- Never modify source PDF contents. The explicit user-requested relocation into `other/sources/` is complete.
- Keep reviewed source text in native Markdown, and publish GitHub-compatible maths for `notes/` plus standard dollar-delimited maths for the Obsidian mirror. The current publisher is `other/work/scripts/build_notes.py`; earlier scratch publishers are historical and use the old layout.

## 3. Required structure of every note

Use this order. Skip a section only if it genuinely does not apply (say, no worked example in a pure-concepts note).

1. **Overview**: what this note is for and what it concludes. Tie it to material he already knows.
2. **Intuition**: the idea in plain physical terms, before any formalism. Italic commentary is welcome.
3. **Derivation**: full first principles, **no glossed algebra**. Give a one-line *reason for every step* (self-explanation). If a derivation is too long or too advanced, say so and give the result with the idea behind it.
4. **Motivation and explanation**: why the result has the form it does, what it means physically, and when it fails. Use intuition rather than restating the algebra.
5. **Worked example**: a numerical or conceptual example, with the figure placed beside the text that refers to it.
6. **Link to other topics**: one to three sentences of **prose only**. **No wikilinks, no `[[...]]`.**
7. **Conclusion**: wrap up and set up the next topic.

**Do not use:** callout blocks, "quick recall" boxes, exam-technique cues, wikilinks, or references to the source document.

**Style rules**
- Draft equation numbers are local to each note. The reviewed editions use continuous subject-wide numbers in both the small notes and complete sections; preserve those numbers when reorganising or exporting.
- Define every symbol on first use. Keep notation consistent with the lecturer's, and note any difference from first-year notation.
- State assumptions and validity limits explicitly (ideal gas, dilute, constant T, etc.).
- Analogies must say where they break down.
- Be efficient: no padding, no recap of steps in the closing sentences.
- Biological topics: explain the mechanism in detail, add an analogy (with its limits), and say where it sits in the wider pathway.

### Explanation standard for all subjects (Xavier's PDC-04 feedback, 15 October 2026)

Keep the structure and tone above. Xavier's preferred reacting-tank explanation is the model for the **connections between physical meaning, algebra and observed behaviour**, not a replacement heading template or a request to expand every note to the same length. The revised canonical PDC-04 draft in `other/work/drafts/Process Dynamics and Control/` is a worked reference alongside the ET pilot.

Xavier subsequently requested this scheme for **every existing note across the other subjects**, after the completed PDC revision was pushed to GitHub. Apply it to first drafts and revisions throughout the repository. Adapt the causal question to the subject: chemical-potential changes and constraints in thermodynamics; molecular mechanisms and measurement inference in biotechnology; reaction, flow and transport in reactor models; equilibrium, local rate and design decisions in separations. The scalar tank balance is an example, not a universal physical model.

- **State what the reader should understand.** Give a concrete conclusion in the overview. Beside a response figure, explain the axes, baseline, final value and visible feature that supports that conclusion. Distinguish a qualitative source sketch from a computed curve; never invent settling times from a picture.
- **Explain the causal sequence before the formula.** Describe what changes first, what is stored, how that affects inflow/outflow or removal, and why the output then rises, decays, oscillates or waits. Give abstract topics a concrete process or signal experiment; do not force a fictitious physical balance onto every theorem.
- **Explain the purpose of an algebraic choice.** Identify which coefficient is used to normalise an ODE and why; show how a steady balance cancels, how an integrating factor makes a product derivative, or which terms are discarded in linearisation. A line saying only “rearrange” or “transform” does not explain a non-obvious step. Assume prior mathematics, but expose its application here rather than re-teaching an entire prerequisite.
- **Translate coefficients into behaviour.** Where applicable, identify storage, restoring/removal and input coefficients. Explain their effects on speed and endpoint separately. For a stable scalar balance $C\dot y'+Ry'=Bu'$ with constant $C,R>0$, dividing by $R$ gives time constant $C/R$ and gain $B/R$. State why this scalar interpretation does not directly cover integrators, delays or coupled higher-order systems.
- **Use checks to teach.** Give a physically useful limiting case or conservation check and explain what it recovers. State what is fixed when comparing parameters. Distinguish nearby ideas explicitly when confusion is likely: time constant/residence time, lag/dead time, absolute value/deviation, gain/speed, pole/zero, and process pole/input-signal pole.
- **Interpret examples, not just calculate them.** After computing numbers, say what they imply for the process or curve. Use each curve's own initial-to-final change for normalised fractions. State a settling tolerance rather than calling an asymptotic response “finished”; the 63.2% rule belongs to a single stable first-order lag, not every system containing that lag.
- **Tie limitations to the missing mechanism.** Explain which changing coefficient, product, neglected state, transport effect or nonlinear curvature breaks the model and how the required modelling step changes. Avoid a detached list of caveats or unrelated advanced extensions.
- **Keep additions specific.** Expand the explanation where a reader would otherwise need to guess a connection. Integrate it into the existing sections, cut repetition, preserve reviewed equation labels, and keep links to other topics to one to three prose sentences. No conversational transcript, memorisation box or new mandatory recap section.

During review, ask whether the reader can explain **why this response occurs, why each important algebraic step helps, what the calculated values mean, and which assumption controls the conclusion** without another explanation outside the note. Record the answers or remaining gaps in work/review files, not as a questionnaire inside study notes.

For a revision of existing notes, keep a per-note gap and change record. Start from the current corrected text, including uncommitted corrections, and preserve scientific qualifications. Synchronise existing short notes, their already authorised complete sections, canonical production text and both publication formats. Editing an existing complete section to retain the revised short-note explanation does not authorise a new grouping or merge. Preserve historical source evidence and original PDFs. Verify the complete sections as well as the short notes: duplicated publication formats must not diverge.

## 4. Per-course emphasis

| Course | Lead with | Typical failure to avoid |
|---|---|---|
| Equilibrium Thermodynamics | thermodynamic constraints, direction of change and meaning of the chosen reference, then purposeful derivation and limiting cases | formulas without what is held constant; confusing equilibrium compositions with phase amounts |
| Advanced Biotechnology | molecular cause → observable signal → justified inference; mechanism and analogy with stated limits | named steps without explaining how they work; treating a signal as proof of identity, mechanism or causation |
| Reaction Engineering II | model assumptions, physical pathway, balance/rate basis, then equation and example interpretation | hiding assumptions; confusing intrinsic kinetics, transport and measured conversion |
| Separations II | equilibrium feasibility, local transport and conservation, then design procedure with reasons for each construction | confusing minimum flow with finite equipment size, or rate with capacity; unjustified averages and bases |
| Process Dynamics and Control | causal physical picture, balance and purposeful normalisation, deviation ODE, transform, then response features and limits | naming gain/poles without explaining the endpoint, speed and mechanism; applying single-lag rules to cascades |

## 5. Source-reading workflow

1. **Render and look at the pages.** Render with `pdftoppm -r 80 -png file.pdf other/work/scratch/pages/p` for overview montages. Use ImageMagick `montage` to read six at a time. Re-render at higher resolution for any slide with dense maths.
2. **Do not trust the PDF text layer for equations.** In the pilot it garbled the maths. Read equations from the page images using the Read tool (PDFs: `pages` parameter, max 20 pages per request). Tesseract is installed but is not good enough for equations; use it only for plain text if at all.
3. **Crop figures with PyMuPDF** (`pip install pymupdf --break-system-packages` if missing; then `import pymupdf`). Use `page.get_pixmap(matrix=pymupdf.Matrix(4,4), clip=pymupdf.Rect(...))`. Find rectangles by scaling coordinates from a montage, and **open every cropped PNG to check it** before using it. `page.get_image_info()` gives bounding boxes of embedded raster images (but plots drawn as vectors are not listed, so crop those by rectangle).
4. Scanned (image-only) PDFs: read from images directly.

## 6. Verification (required before delivery)

- **Every numerical answer is computed in Python.** Never do arithmetic in prose. Report the numbers the code gave.
- **Re-derive each equation from first principles** rather than copying it from the slide. Fix lecturer typos silently only if you are certain, and mention the correction to Xavier in your reply, not in the note.
- **Check units** and limiting cases.
- Values read from a graph are estimates. Say "≈" and do not claim precision the graph does not have.
- Final step before delivery: open each file and each figure and check the rendering, the equation numbering and the figure links.

## 7. Multiple sources (required)

**Do not rely only on the lecture notes for explanations.** For each topic, consult other sources that may give better insight or intuition, for example university lecture notes (MIT OCW, Cambridge, Oxford, Yale), standard textbooks, and Wikipedia for intuition-first framings.

- Actually open and read what you cite. A search-results list is not a source.
- If a page cannot be retrieved, say so in your reply. Do not imply you used it.
- In the note, keep only the explanation (not a copied passage). Do not reproduce copyrighted text.
- In your reply to Xavier, list sources used under "Sources:" with links.

## 8. Combining short notes into a complete section

When Xavier gives you a group of short notes with a line saying which belong together:

- Produce **one markdown file** with one H1, then one H2 per subtopic (one per short note).
- Combine the overviews into a single opening overview and cut the repeated prerequisites.
- Turn each note's conclusion into a **short subconclusion** for its subtopic. Write one final conclusion that points to the next topic.
- **Renumber equations across the merged file** in one sequence and update every in-text reference to match.
- Fix figure paths so the images resolve from the merged file.
- Remove any references to the former file names ("ET-0x").
- Leave derivations and examples intact. Edit them only to fix flow or an error, and tell Xavier what you changed.

## 9. Delivery

- Small notes and complete sections go in `notes/<subject>/<NN - topic>/`; figures go in `notes/<subject>/figs/` with relative links. There is no separate merged folder.
- The native Obsidian export mirrors this structure under `other/obsidian/CEBT-II Notes/`. The user copies this whole folder, or a subject folder with all its topics and figures, into the vault themselves.
- Work files stay in `other/work/`; the plan and repository README stay at the root.
- Validate figure links, mathematical rendering and the portable export after moving it into a different folder. Report exactly what was checked; do not imply an Obsidian runtime check if the app was not opened.
- Send deliverable links when ready. Reply briefly with what was produced, corrections, sources and a next step if needed.

## 10. Open points to confirm with Xavier

- Whether the short "link to other topics" prose in each note (kept in the pilot) is still wanted now that wikilinks are excluded.
- Whether the pilot's extra depth (for example the real-fluid correction integral and the cross-derivative proof in ET-05) is the right level, or too much.

## 11. Pilot lessons

- The lecture slides were sparse: the maths was a list of results with little reasoning. The value of the notes is the added derivation and intuition, so do not just transcribe the slides.
- Check for non-ideal behaviour that the example reveals. In the whiskey example, the 3% volume contraction was used to show that the mixture is not ideal.
- Keep notes short enough that merging is easy. The pilot was five notes of roughly one page each.

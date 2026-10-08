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
- Figures are **cropped from the lecture PDFs** and saved in a `figs/` folder next to the notes. Name them `<prefix>-<NN>-<description>.png`. Link them relatively.

### Folder layout

This workspace uses the same overall layout as my other Claude workspace (separations coursework). The subject folders differ, the rest is the same:

```
CEBT-II-notes/
├── CLAUDE.md          this file (Claude Code)
├── AGENTS.md          same instructions for Codex; points here and at out/PLAN.md
├── sources/           lecturer PDFs (read-only), one subfolder per course
│   ├── Equilibrium Thermodynamics/
│   ├── Advanced Biotech/
│   └── ...
└── out/               everything you write
    ├── PLAN.md        the production plan
    ├── ET/            finished short notes (ET-01, ...), with figs/
    ├── AB/            finished short notes (AB-01, ...), with figs/
    ├── merged/        merged files, with figs/
    └── work/          everything that isn't a deliverable
        ├── BOARD.md   unit ownership and status (when two agents are working)
        ├── reviews/   cross-review findings, one file per unit
        ├── ocr/       OCR transcripts, one subfolder per PDF
        ├── progress/  per-PDF reading progress files
        └── scratch/   temporary renders, montages, scripts, tests
```

- A new course gets its own prefix folder in `out/` (for example `out/RE/`) and its own subfolder in `sources/`.
- Write only inside these folders. Never leave files loose in `out/`. Never modify `sources/`.

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
- Equation numbers are local to each note.
- Define every symbol on first use. Keep notation consistent with the lecturer's, and note any difference from first-year notation.
- State assumptions and validity limits explicitly (ideal gas, dilute, constant T, etc.).
- Analogies must say where they break down.
- Be efficient: no padding, no recap of steps in the closing sentences.
- Biological topics: explain the mechanism in detail, add an analogy (with its limits), and say where it sits in the wider pathway.

## 4. Per-course emphasis

| Course | Lead with | Typical failure to avoid |
|---|---|---|
| Equilibrium Thermodynamics | limiting cases and sanity checks (ideal gas, pure component, infinite dilution) | stating formulas without saying what is held constant |
| Advanced Biotechnology | mechanism, analogy with stated limits, pathway map | lists of facts with no mechanism |
| Reaction Engineering II | model assumptions first, then the equations | equations that hide which assumptions were used |
| Separations II | step-by-step design procedure plus the graphical construction | construction steps with no reason for each |
| Process Dynamics and Control | physical system, then ODE, then Laplace transform, then what the poles mean | transfer functions with no physical meaning |

## 5. Source-reading workflow

1. **Render and look at the pages.** Render with `pdftoppm -r 80 -png file.pdf out/work/scratch/pages/p` for overview montages. Use ImageMagick `montage` to read six at a time. Re-render at higher resolution for any slide with dense maths.
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

## 8. Merging short notes into one file

When Xavier gives you a group of short notes with a line saying which belong together:

- Produce **one markdown file** with one H1, then one H2 per subtopic (one per short note).
- Combine the overviews into a single opening overview and cut the repeated prerequisites.
- Turn each note's conclusion into a **short subconclusion** for its subtopic. Write one final conclusion that points to the next topic.
- **Renumber equations across the merged file** in one sequence and update every in-text reference to match.
- Fix figure paths so the images resolve from the merged file.
- Remove any references to the former file names ("ET-0x").
- Leave derivations and examples intact. Edit them only to fix flow or an error, and tell Xavier what you changed.

## 9. Delivery

- Save notes as `.md` in `out/<PREFIX>/` (for example `out/ET/`) and figures as `.png` in `out/<PREFIX>/figs/`. Merged files go in `out/merged/` with their figures in `out/merged/figs/`. Scratch work goes in `out/work/scratch/`.
- Send each deliverable to Xavier as a file when it is ready, with a one-line caption. Do not send scratch files.
- Reply with: what was produced, the corrections you made to the source, sources used, and one next step if there is one. Keep it short.

## 10. Open points to confirm with Xavier

- Whether the short "link to other topics" prose in each note (kept in the pilot) is still wanted now that wikilinks are excluded.
- Whether the pilot's extra depth (for example the real-fluid correction integral and the cross-derivative proof in ET-05) is the right level, or too much.

## 11. Pilot lessons

- The lecture slides were sparse: the maths was a list of results with little reasoning. The value of the notes is the added derivation and intuition, so do not just transcribe the slides.
- Check for non-ideal behaviour that the example reveals. In the whiskey example, the 3% volume contraction was used to show that the mixture is not ideal.
- Keep notes short enough that merging is easy. The pilot was five notes of roughly one page each.

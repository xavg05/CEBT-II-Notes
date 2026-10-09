# CEBT II Notes

Lecture notes, figures, source PDFs and production records for Cambridge Chemical Engineering and Biotechnology II.

## Notes

- [Equilibrium Thermodynamics](notes/equilibrium-thermodynamics/README.md) — foundations through steam distillation, in teaching order. Independent content cross-review remains pending.
- [Advanced Biotechnology](notes/advanced-biotechnology/README.md) — nucleic acids through synthetic condensates. Review and supplementation status are labelled in the subject index.
- [All subjects](notes/README.md).

Each subject has linked reading sections for GitHub and a **complete single-file Obsidian edition** with its own figures. Use the reading sections in the browser: the complete files exceed GitHub’s cumulative math limit.

## Preparation and review

[out/](out/README.md) holds original individual notes, archived unit merges, drafts and production records. Start with the [production plan](out/PLAN.md), [ownership board](out/work/BOARD.md) or [navigation verification report](out/work/GITHUB-NAVIGATION.md) when continuing work. Original reference material is in [sources/](sources/).

## Continue on another computer

Install Git, then clone this repository once:

```sh
git clone https://github.com/xavg05/CEBT-II-Notes.git
cd CEBT-II-Notes
```

Before each session, get the latest work:

```sh
git pull --ff-only
git status
```

After working, inspect and commit your changes, then push them:

```sh
git diff
git add path/to/changed/files
git commit -m "Describe the changes"
git push
```

Replace `path/to/changed/files` with the files you intend to save. Commit or stash local changes before pulling. Push at the end of a session, and pull on the other computer before continuing. If two computers edit the same file, resolve the conflict rather than force-pushing.

Reading the GitHub sections needs no build step. For Obsidian, copy the subject’s `complete-obsidian.md` with its adjacent `figs/` folder into the vault yourself. These complete editions use standard dollar-delimited math; GitHub reading sections use protected inline LaTeX and fenced math blocks.

## Folder layout

```text
sources/           Original course PDFs; do not modify
notes/             Subject reading indexes
notes/<subject>/   Final reading sections, complete Obsidian edition and figures
out/PLAN.md        Production plan
out/ET/            Equilibrium Thermodynamics short notes and figures
out/AB/            Advanced Biotechnology short notes and figures
out/merged/        Preserved production snapshots of the original unit merges
out/work/          Ownership, reviews, OCR, progress and saved scratch work
AGENTS.md          Instructions for Codex and other agents
CLAUDE.md          Full note-writing specification
```

## Working with an agent

Ask the agent to read `AGENTS.md`, `CLAUDE.md`, `out/PLAN.md` and `out/work/BOARD.md` before continuing. The completion record and cross-reviews describe completed work and remaining original-note findings. Agree on the next unit and respect ownership if multiple agents are working.

The current reading layout is `notes/<subject>/`, as requested for GitHub navigation. Earlier instructions and the production plan still describe `out/merged/`; that folder is retained as an unchanged production archive. Publish reader-facing editions in `notes/` and keep preparation, review and verification records in `out/`.

PDF processing and verification scripts use Python with packages such as PyMuPDF, Pillow and NumPy; particular scripts can require SciPy, ImageMagick or Node.js with `marked` and `katex`. Inspect the script before running it: some saved scratch scripts contain macOS font paths or local environment assumptions that need adapting on Windows. Temporary dependency folders, browser profiles and generated previews are excluded from Git and can be recreated locally.

This repository preserves the existing Git history, source PDFs, notes, figures and saved work records. Sources and figures retain their original provenance; no blanket licence is asserted for third-party material.

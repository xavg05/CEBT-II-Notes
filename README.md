# CEBT II Notes

Lecture notes, figures, source PDFs and production records for Cambridge Chemical Engineering and Biotechnology II.

## Start here

- [Production plan](out/PLAN.md): course coverage and remaining work.
- [Ownership board](out/work/BOARD.md): current unit assignments and status.
- [Advanced Biotechnology completion index](out/work/AB-COMPLETION.md): all 17 merged units, new short notes, checks and sources.
- [Merged notes](out/merged/): notes ready to copy into Obsidian, together with the adjacent `figs/` folder.

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

Reading and editing the Markdown needs no build step. Use Obsidian or another editor supporting dollar-delimited math. GitHub's preview can differ from Obsidian. Copy the desired merged Markdown files with their `figs/` folder into the vault yourself.

## Folder layout

```text
sources/           Original course PDFs; do not modify
out/PLAN.md        Production plan
out/ET/            Equilibrium Thermodynamics short notes and figures
out/AB/            Advanced Biotechnology short notes and figures
out/merged/        Merged notes and figures
out/work/          Ownership, reviews, OCR, progress and saved scratch work
AGENTS.md          Instructions for Codex and other agents
CLAUDE.md          Full note-writing specification
```

## Working with an agent

Ask the agent to read `AGENTS.md`, `CLAUDE.md`, `out/PLAN.md` and `out/work/BOARD.md` before continuing. The completion record and cross-reviews describe completed work and remaining original-note findings. Agree on the next unit and respect ownership if multiple agents are working.

PDF processing and verification scripts use Python with packages such as PyMuPDF, Pillow and NumPy; particular scripts can require SciPy, ImageMagick or Node.js with `marked` and `katex`. Inspect the script before running it: some saved scratch scripts contain macOS font paths or local environment assumptions that need adapting on Windows. Temporary dependency folders, browser profiles and generated previews are excluded from Git and can be recreated locally.

This repository preserves the existing Git history, source PDFs, notes, figures and saved work records. Sources and figures retain their original provenance; no blanket licence is asserted for third-party material.

# CEBT-II Notes

Reviewed lecture notes in chronological topic folders. Each topic contains its small notes, an overview and a complete-section version.

- [Equilibrium Thermodynamics](<notes/Equilibrium Thermodynamics/README.md>) — 12 topics, 43 small notes.
- [Advanced Biotechnology](<notes/Advanced Biotechnology/README.md>) — 17 topics, 57 small notes, including optional condensates.
- [All notes](notes/README.md).

## Folder layout

```text
AGENTS.md
CLAUDE.md
PLAN.md
README.md
notes/
  Equilibrium Thermodynamics/
    01 - Foundations .../
      README.md
      ET-01 - ...md
      ET-02 - ...md
      Complete section.md
    02 - Fugacity/
    ...
    figs/
  Advanced Biotechnology/
    01 - Nucleic acids .../
    ...
    figs/
other/
  obsidian/
    CEBT-II Notes/       same subject/topic tree, native Obsidian maths
  work/                 reviews, progress, scripts, scratch and historical snapshots
  sources/              original PDFs by subject
```

All figures for a subject live together in its `figs/` folder. The small notes and complete sections share them. There is no separate `merged/` or root `out/` folder.

## Obsidian

[Open the Obsidian edition](<other/obsidian/CEBT-II Notes/README.md>). Copy the whole `other/obsidian/CEBT-II Notes/` folder into your vault, or copy a whole subject folder with its topics and `figs/`. Keep that arrangement unchanged. No importer or plugin is needed.

The main `notes/` pages use GitHub-compatible maths. The Obsidian mirror uses ordinary `$...$` and `$$...$$`. A local ZIP is generated in `other/obsidian/`.

## Preparation and review

[Plan](PLAN.md) · [Ownership board](other/work/BOARD.md) · [Layout verification](other/work/LAYOUT.md) · [Scientific review](other/work/FINAL-DELIVERY.md) · [Sources](other/sources/).

The latest corrected explanations and figures are used in both editions. Gene regulation is externally supplemented; synthetic condensates is optional. Original small notes and earlier unit snapshots are retained under `other/work/archive/` as production history.

Before continuing work, read `AGENTS.md`, `CLAUDE.md`, `PLAN.md` and `other/work/BOARD.md`. Current publishing uses `other/work/scripts/build_notes.py`; earlier scratch scripts refer to the former layout.

## Continue on another computer

Clone once:

```sh
git clone https://github.com/xavg05/CEBT-II-Notes.git
cd CEBT-II-Notes
```

Before a session:

```sh
git pull --ff-only
git status
```

After editing, review and save the intended files:

```sh
git diff
git add path/to/changed/files
git commit -m "Describe the changes"
git push
```

Commit or stash local changes before pulling. Pull before continuing on another computer; resolve conflicts without rewriting shared history.

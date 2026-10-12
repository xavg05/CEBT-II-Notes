# CEBT-II Notes

Lecture notes in chronological topic folders. The completed courses have reviewed small notes, overviews and complete-section versions. Reaction Engineering II is in progress. Process Dynamics and Control chapters 1–2 have reviewed short notes; later chapters are awaiting sources. Separations II has 43 reviewed short notes covering all four supplied handouts. Short-note grouping remains pending for these new subjects.

- [Equilibrium Thermodynamics](<notes/Equilibrium Thermodynamics/README.md>) — 12 topics, 43 small notes.
- [Advanced Biotechnology](<notes/Advanced Biotechnology/README.md>) — 17 topics, 57 small notes, including optional condensates.
- [Reaction Engineering II](<notes/Reaction Engineering II/README.md>) — RE-01–06 written; section 2 source missing.
- [Process Dynamics and Control](<notes/Process Dynamics and Control/README.md>) — 8 topics, PDC-01–22 reviewed; supplied chapters 1–2.
- [Separations II](<notes/Separations II/README.md>) — 4 topics, SEP-01–43 reviewed; four supplied handouts.
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

Reaction Engineering uses the scoped `other/work/scripts/publish_re.py` publisher. Its source coverage, supplementary sources and checks are recorded in [the opening-batch progress record](other/work/progress/codex-RE01-06-section1-20261012.md). Rebuilding older subjects with the historical publisher rewrites the all-subject indexes; retain the Reaction Engineering entries.

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

Process Dynamics and Control uses the scoped `other/work/scripts/publish_pdc.py` publisher. [Source coverage, corrections and verification](other/work/progress/PDC-chapters1-2.md) are recorded separately from the completed ET/AB review history.

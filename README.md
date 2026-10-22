# CEBT-II Notes

Lecture notes in chronological topic folders. As of 22 October 2026, all 192 short notes that can be written from the supplied sources are reviewed: ET 43, AB 57, RE 27, SEP 43 and PDC 22. Equilibrium Thermodynamics and Advanced Biotechnology also have 29 authorised complete-section versions. Reaction Engineering II covers supplied sections 1–6; Process Dynamics and Control covers chapters 1–2; Separations II covers all four supplied handouts. Later RE and Control sections await sources, and complete-section grouping for RE, SEP and PDC awaits Xavier's merge groups.

- [Equilibrium Thermodynamics](<notes/Equilibrium Thermodynamics/README.md>) — 12 topics, 43 small notes.
- [Advanced Biotechnology](<notes/Advanced Biotechnology/README.md>) — 17 topics, 57 small notes, including optional condensates.
- [Reaction Engineering II](<notes/Reaction Engineering II/README.md>) — 11 topics, 27 reviewed small notes, RE-01–27; supplied sections 1–6. Sections 7 and 8 await sources.
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

[Plan](PLAN.md) · [Ownership board](other/work/BOARD.md) · [Layout verification](other/work/LAYOUT.md) · [Scientific review](other/work/FINAL-DELIVERY.md) · [Supplied-material coverage audit](other/work/COVERAGE-AUDIT-20261014.md) · [Sources](other/sources/).

The latest corrected explanations and figures are used in both editions. Gene regulation is externally supplemented; synthetic condensates is optional. Original small notes and earlier unit snapshots are retained under `other/work/archive/` as production history.

Before continuing work, read `AGENTS.md`, `CLAUDE.md`, `PLAN.md` and `other/work/BOARD.md`. Current publishing uses `other/work/scripts/build_notes.py`; earlier scratch scripts refer to the former layout.

Reaction Engineering is published with `other/work/scripts/publish_re_all.py`, which supersedes `publish_re.py` and `publish_re_supplied.py`. Its source coverage, supplementary sources and checks are recorded in [the opening-batch progress record](other/work/progress/codex-RE01-06-section1-20261012.md). Rebuilding older subjects with the historical publisher rewrites the all-subject indexes; retain the Reaction Engineering entries.

The supplied RE sections 3–6 retain their [independent source and numerical review](other/work/reviews/RE-S3-S6-cross-review-20261014.md), with the former provisional identifiers now RE-13–27. [RE-U2's review and correction closure](other/work/reviews/RE-U2-cross-review-20261022.md) covers RE-07–12. Publish every RE note with `publish_re_all.py`; the two superseded RE publishers must not be used. The current coverage audit records the completed Biotechnology corrections and missing course PDFs.

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

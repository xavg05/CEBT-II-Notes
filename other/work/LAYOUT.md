# Subject/topic layout — 12 October 2026

The requested reorganisation is complete. Main reading starts at [notes/README.md](../../notes/README.md); the native copy starts at [the Obsidian index](<../obsidian/CEBT-II Notes/README.md>).

## Current structure

- `notes/Equilibrium Thermodynamics/`: 12 numbered topic folders with 43 small notes.
- `notes/Advanced Biotechnology/`: 17 numbered topic folders with 57 small notes.
- Every topic contains a README overview, its small notes and `Complete section.md`.
- All 180 figures are shared by subject in `notes/<subject>/figs/`, not duplicated into individual topics.
- `other/obsidian/CEBT-II Notes/` mirrors that organisation with standard dollar-delimited math. Copy the whole folder, or a whole subject folder including its topic folders and `figs/`, into the vault.
- `other/work/` holds reviews, progress, scripts, scratch and production history; `other/sources/` holds the unchanged PDF contents.
- `AGENTS.md`, `CLAUDE.md`, `PLAN.md` and `README.md` remain at the root. Their navigation and layout guidance were updated to the user's requested structure.
- There is no root `out/` or separate `merged/` folder. The former unit snapshots and original small notes are retained under the work archive.

## Preservation and verification

The small notes are extracted from the corrected, reviewed native units, preserving every scientific paragraph, equation and example. The complete-section files contain those same corrected units. The topic indexes carry their common overviews. This keeps the final scientific corrections rather than restoring older uncorrected short-note text.

- [Content and link checks](LAYOUT-PRESERVATION.json): 100 small notes and 29 complete sections preserve the reviewed scientific text. All active local links resolve. 528 original scientific/source files retain identical bytes after relocation.
- [Folder and ZIP checks](LAYOUT-VALIDATION.json): 161 Markdown files per edition, 180 distinct figures, and successful extraction into a separate nested vault-like directory with all native links still resolving.
- [Math checks](LAYOUT-MATH-VALIDATION.json): all 160 content/index pages in each edition have matching formulas and equation labels. 8,018 mathematical expressions (small notes plus complete-section copies) parse successfully with no errors. All pages stay below GitHub's cumulative math budget; the largest measured cost is 816 against the 2,000 limit.
- All 302 numbered equations retain their reviewed subject-wide numbering. Component and figure labels are not renumbered by this publisher.
- Historical work/reading-navigation links were rebased and checked as well. Scientific review findings and external-source records remain under [reviews/](reviews/).

The previous scientific audit and visual figure inspection remain documented in [FINAL-DELIVERY.md](FINAL-DELIVERY.md). This reorganisation changes paths, navigation, grouping and heading depth; it introduces no new scientific claims. Obsidian itself and the user's vault were not opened. No new actual GitHub browser check or remote publication is claimed.

## Reproduction

Run from the repository root:

```sh
python3 other/work/scripts/build_notes.py
python3 other/work/scripts/verify_layout.py
node other/work/scripts/check_notes.mjs
```

The publisher reads `other/work/archive/reviewed-units/<subject>/`. The JavaScript checks use the existing local KaTeX and marked dependencies under the ignored tools directory. The local ZIP `other/obsidian/CEBT-II-Obsidian.zip` is generated rather than tracked.

Earlier scratch scripts and manifests use their original production paths and are retained as historical evidence. The file-move and preservation records are in `scratch/reorganize-layout/`.

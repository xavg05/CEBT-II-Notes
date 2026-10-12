# Cleanup plan: CEBT-II-notes to standard layout

Drafted 2026-10-08; revised 2026-10-08 after Xavier swapped the control files back and answered the flags. Approved.

## Inventory summary

| Area | Contents | Status |
|---|---|---|
| `out/AB/` | AB-01 … AB-47 (47 notes) + `figs/` (121 PNGs, all referenced) | Already in place |
| `out/ET/` | ET-01 … ET-43 (43 notes) + `figs/` (36 PNGs, all referenced) | Already in place |
| `out/merged/` | 12 × `Equilibrium Thermodynamics NN - ….md` + `figs/` (36 PNGs) | Already in place |
| `out/PLAN.md` | 25.8 kB, CEBT II production plan (after swap) | In place |
| `out/SEP/` | `figs/` (empty), `work/reviews/` (empty), `work/ocr-test/` (findings.md, 3 PNG, 3 TXT), 2 × .DS_Store | Doesn't belong here, so it goes to `_to_review` |
| `out/work/` | did not exist | To be created |
| root | `CLAUDE.md`, `AGENTS.md` (CEBT II versions after swap) | In place |
| `.DS_Store` | root, out/, out/AB, out/ET, out/SEP, out/SEP/work | macOS junk. Leave in place and git-ignore them |

Links: all 193 relative image links (`figs/<name>.png`) in AB, ET and merged resolve now (script check, 0 broken). The merged files link to `out/merged/figs/`, which holds byte-identical copies of all 36 ET figures. None of these files move, so **no link edits are needed**. `findings.md` has no image links and moves together with its siblings.

## Moves

| Current path | New path | Reason |
|---|---|---|
| `out/SEP/work/ocr-test/findings.md` | `out/work/ocr-test-findings.md` | Real OCR test of this workspace's AB/ET PDFs (Xavier, flag 2) |
| rest of `out/SEP/` (empty `figs/`, empty `work/reviews/`, `work/ocr-test/` 3 PNG + 3 TXT, .DS_Store) | `out/work/_to_review/SEP/` (same internal structure) | Output from the separations session; kept for your decision |
| (none) | `out/work/BOARD.md` with header `\| unit \| owner \| status \| notes \|` | Xavier, flag 4 |
| (none) | `out/work/reviews/`, `ocr/`, `progress/`, `scratch/` | Standard layout. Each gets an empty `.gitkeep` so git tracks it |
| (none) | `.gitignore` containing `.DS_Store` | Keeps Finder junk out of the snapshot (nothing deleted) |
| `out/AB/**`, `out/ET/**`, `out/merged/**`, `out/PLAN.md` | unchanged | Already match the layout |

## Flags (resolved)

1. Control files were swapped with `~/Projects/Multi-Component Separation/`. **Resolved:** Xavier swapped them back. Re-checked every path mention in `CLAUDE.md`, `AGENTS.md` and `out/PLAN.md` against the target tree: all match, so no edits are needed.
2. `findings.md` moves to `out/work/ocr-test-findings.md`. The 2025 date is a typo; left as is. **Side effect:** its line "Transcripts: p4-04.txt, p6-06.txt, p13-13.txt" will point at files that now sit in `out/work/_to_review/SEP/work/ocr-test/`. It's a plain-text mention, not a link, so I left it unedited.
3. Keep `out/merged/figs/` as a copy of `out/ET/figs/`.
4. Create `out/work/BOARD.md` with only the header row.
5. Noted only: `sources/Advanced Biotech/Lecture 7.pdf` has a space in its name.
6. Content (not paths) that is now stale in `out/PLAN.md`: the "Totals" line still says ET has 11 units to write, and the tooling caveat says ImageMagick is missing (the OCR test found it installed). Left untouched, because AGENTS.md says PLAN.md is edited only with Xavier's OK.

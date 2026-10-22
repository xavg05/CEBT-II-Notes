# Working-tree cleanup — 22 October 2026

Baseline: `2fc29e9` on `main`, already pushed to `origin/main` after repository finalisation. Read AGENTS.md and BOARD.md before starting; no BOARD rows were marked writing. The sibling Multi-Component-Separation workspace had zero porcelain status entries and was only inspected.

## Inventory before changes

Counts use `git status --porcelain` entries (untracked directories are collapsed):

| Category | Entries | Action |
| --- | ---: | --- |
| Tracked, line endings only | 0 | No checkout needed |
| Tracked, real content changes | 0 | No unexplained changes to preserve |
| Untracked deliverables | 0 | Existing delivery records/scripts were already committed |
| Untracked scratch/temporary output | 5 | Preserve on disk and ignore |

The five scratch entries were:

- `other/work/scratch/AB-recovery-figures.png`
- `other/work/scratch/ET-recovery-crossreview-figures.png`
- `other/work/scratch/finalisation-20261022/`
- `other/work/scratch/re-s2/`
- `other/work/scratch/teaching-recovery/`

## Cause and correction

`publish_et_ab_teaching.py` executes the section-splitting portion of `build_notes.py`. Its `write_pair` used `Path.write_text` without a newline argument, allowing Windows to translate LF to CRLF. This explains the earlier ET/AB README churn restored during finalisation. Set explicit UTF-8 and `newline='\n'` on all text outputs in both scripts; also make the splitter's source reads explicitly UTF-8.

`publish_pdc.py` and `publish_separations.py` had the same implicit newline behaviour. Their text outputs now explicitly use LF. `publish_re_all.py` already specifies LF and needed no change. Superseded RE publishers were not run or changed. No publisher was run against the published notes.

## Validation

- Parsed all four changed scripts successfully and checked their text writes specify UTF-8 and LF.
- Executed the actual paired-writing functions extracted with Python's AST, together with their real maths conversion helpers, in temporary directories. All six publisher/edition combinations passed byte-level LF checks, exact UTF-8 content checks and equation-label/maths-conversion checks. The sample included a Unicode Greek letter, inline maths and a numbered display equation.
- Checked both scoped ET/AB wrapper record writes also explicitly specify UTF-8 and LF.
- `git diff --check` passed.

The ignore change adds `other/work/scratch/` without deleting files or changing the index entries for the 1,062 already tracked scratch files. Original PDFs, historical snapshots, notes in both editions and sibling-workspace files were not modified. For PDC, the only file to inspect is `other/work/scripts/publish_pdc.py`: its paired output and validation-record writes now specify LF; no PDC scientific content changed.

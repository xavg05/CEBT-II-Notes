# AGENTS.md — instructions for Codex (and any non-Claude agent)

This workspace may be worked on by two agents in parallel: Claude Code and Codex. Both follow the same rules.

## Read first
1. `CLAUDE.md` in this folder: the full specification for how the CEBT II lecture notes are made (structure, style, PDF reading, verification, merging, delivery) and the folder layout. Treat it as your instructions too: wherever it says "you", that includes you.
2. `PLAN.md`: the production plan (which lectures group into which units, which notes to write, and the order of work).

If the two disagree, or anything is unclear, ask me.

## Where files go
The layout is in CLAUDE.md ("Folder layout"). The user changed it on 12 October 2026:
- `notes/<subject>/<NN - topic>/`: small numbered notes, a topic README and `Complete section.md`.
- `notes/<subject>/figs/`: all figures for that subject, shared across its topics.
- `other/obsidian/CEBT-II Notes/`: the same subject/topic tree with native Obsidian maths.
- `other/work/`: ownership, reviews, drafts, progress, scripts, scratch and preserved production snapshots.
- `other/sources/<subject>/`: original PDFs. Do not change their contents.
- `PLAN.md`, `README.md`, `AGENTS.md` and `CLAUDE.md` remain at the repository root.

Do not create root `out/`, `sources/` or a separate `merged/` folder. Never write into the user's Obsidian vault: the user copies the export themselves. Current layout and validation are recorded in `other/work/LAYOUT.md`.

## Working alongside the other agent
- **Check `other/work/BOARD.md` before starting anything.** If it doesn't exist, create it with the columns `unit | owner | status | notes` and one row per unit from `PLAN.md`. Status is one of unclaimed / writing / written / reviewed.
- **Claim a unit** by writing your name (`claude` or `codex`) in the owner column before you start. Never edit, rewrite or delete a unit owned by the other agent.
- **Update the status** when you finish. Keep notes in the board short.
- **Reuse each other's work:** OCR transcripts (`other/work/ocr/`) and per-PDF progress files (`other/work/progress/`) are shared. Check them before OCR'ing or re-reading a PDF, and don't process the same PDF at the same time as the other agent.
- **Write only your own files.** Each note file has one owner. If you spot a problem in the other agent's note, don't edit it: write the finding to `other/work/reviews/<unit>.md` and let the owner fix it.
- **Cross-review:** when a unit is marked written by one agent, the other agent reviews it: re-derive the equations, re-run the numbers in Python, check notation consistency, check figures open and link correctly, and check the note never refers to the lecture PDF, slides or lecturer. Mark it reviewed when the owner has fixed the findings.
- **Merging is done by ONE agent only**, and only when I tell you which short notes belong together.
- **Decisions about style or approach** go to me. Don't edit `PLAN.md` or `CLAUDE.md` without asking me first.
- **Commit often if the folder is a git repo:** `git add` only your own files and commit with a message starting with your name (e.g. `codex: AB-12 written`). Don't force anything or rewrite history.
- When unsure whether something belongs to you or the other agent, leave it and ask me.

## Stop points
Follow the order of work in `PLAN.md`. Advanced Biotechnology AB-U13 has already been completed and reviewed with external supplementation; retain that qualification. The plan’s original before-starting stop point is historical for this finished unit.

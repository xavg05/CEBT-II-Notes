# AGENTS.md — instructions for Codex (and any non-Claude agent)

This workspace may be worked on by two agents in parallel: Claude Code and Codex. Both follow the same rules.

## Read first
1. `CLAUDE.md` in this folder: the full specification for how the CEBT II lecture notes are made (structure, style, PDF reading, verification, merging, delivery) and the folder layout. Treat it as your instructions too: wherever it says "you", that includes you.
2. `out/PLAN.md`: the production plan (which lectures group into which units, which notes to write, and the order of work).

If the two disagree, or anything is unclear, ask me.

## Where files go
The layout is in CLAUDE.md ("Folder layout"). In short:
- `out/ET/`, `out/AB/` (and other subject prefix folders): short numbered notes, with `figs/` inside each
- `out/merged/`: merged files, with `out/merged/figs/`
- `out/work/`: everything that isn't a deliverable: `BOARD.md`, `reviews/`, `ocr/`, `progress/`, `scratch/`

Never leave files loose in `out/`. Never modify `sources/`. Never write into my Obsidian vault: I upload notes myself.

## Working alongside the other agent
- **Check `out/work/BOARD.md` before starting anything.** If it doesn't exist, create it with the columns `unit | owner | status | notes` and one row per unit from `out/PLAN.md`. Status is one of unclaimed / writing / written / reviewed.
- **Claim a unit** by writing your name (`claude` or `codex`) in the owner column before you start. Never edit, rewrite or delete a unit owned by the other agent.
- **Update the status** when you finish. Keep notes in the board short.
- **Reuse each other's work:** OCR transcripts (`out/work/ocr/`) and per-PDF progress files (`out/work/progress/`) are shared. Check them before OCR'ing or re-reading a PDF, and don't process the same PDF at the same time as the other agent.
- **Write only your own files.** Each note file has one owner. If you spot a problem in the other agent's note, don't edit it: write the finding to `out/work/reviews/<unit>.md` and let the owner fix it.
- **Cross-review:** when a unit is marked written by one agent, the other agent reviews it: re-derive the equations, re-run the numbers in Python, check notation consistency, check figures open and link correctly, and check the note never refers to the lecture PDF, slides or lecturer. Mark it reviewed when the owner has fixed the findings.
- **Merging is done by ONE agent only**, and only when I tell you which short notes belong together.
- **Decisions about style or approach** go to me. Don't edit `out/PLAN.md` or `CLAUDE.md` without asking me first.
- **Commit often if the folder is a git repo:** `git add` only your own files and commit with a message starting with your name (e.g. `codex: AB-12 written`). Don't force anything or rewrite history.
- When unsure whether something belongs to you or the other agent, leave it and ask me.

## Stop points
Follow the order of work in `out/PLAN.md`. Ask me before starting Advanced Biotechnology unit AB-U13 (gene regulation and synthetic circuits), as the plan says.

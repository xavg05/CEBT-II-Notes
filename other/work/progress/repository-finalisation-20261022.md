# Supplied-source finalisation — 22 October 2026

Authorisation: Xavier explicitly authorised Codex to correct the Claude-owned RE-07–12 canonical drafts, update PLAN/BOARD/README bookkeeping, validate the repository and push main. AGENTS.md, CLAUDE.md, PLAN.md and BOARD.md were read before work.

## Scientific closure

RE-U2's [review](../reviews/RE-U2-cross-review-20261022.md) now passes. All fourteen source pages were visually rechecked; all ten cropped figures were opened individually and checked against their source and surrounding explanation. Labels 21–37 were independently re-derived from fluxes, moving-boundary inventories, heat balance and RTD averaging. The three original findings were corrected, along with the droplet coefficient-ratio qualification, explicit air pressure and a fresh plug-flow rounding correction. All calculated prose results have independent Python checks; empirical property/correlation inputs remain identified as assumptions.

The original author script `verify_re_s2.py` completed successfully through its `RE_PYLIB` hook using scientific dependencies installed only under uncommitted scratch. `crossreview_re_u2.py` passes 50 independent checks. The corrections preserve all RE labels 1–110 and their references. Only `publish_re_all.py` was used to republish RE.

## Current validation

| Check | Result |
|---|---|
| RE publisher | 27 notes; labels 1–110 strictly ordered; 241 links and 20 image references per edition; relocated native export passes |
| RE KaTeX and edition parity | 1125 native expressions; zero failures |
| Inline mathematical scripts | 680 publication/canonical Markdown files pass |
| All-subject KaTeX and maths parity | 278 subject pages; 10503 expressions per edition; zero errors; all five subjects included |
| All-reading Markdown, KaTeX, links and mirror maths | 279 pages including global index; 10503 expressions per edition; 5146 relative links across both editions; zero failures |
| RE-U2 canonical/full-text parity | All six canonical and native bodies agree; reading/native full-text parity passes; 108 links and twenty figure files across both editions pass |
| Counts | ET 43, AB 57, RE 27, SEP 43, PDC 22: 192 reviewed short notes; 29 existing ET/AB complete sections |
| Source and historical preservation | No original PDF or historical snapshot changed |

The all-subject checker already discovers current filenames dynamically. Its former four-subject scope was expanded to include PDC, and equivalent operator notation is now normalised symmetrically in both editions; this removes a false RE-06 mismatch. Both all-subject checks now save current results under `other/work/progress/`, leaving historical scratch validation records untouched. Results: [maths](all-subject-math-validation.json), [reading and links](all-reading-validation.json), [RE publisher](re-relabel-validation.json), and [independent RE-U2 calculations](../reviews/RE-U2-cross-review-numbers-20261022.json).

These are local Markdown/KaTeX, image, link and relocation checks. No live Obsidian application or remote GitHub rendering check is claimed. The user's vault was not opened or written.

## Bookkeeping closure

The existing FINAL-DELIVERY.md explicitly confirms all 100 ET/AB short notes and all 29 topics were scientifically reviewed, with separate review records covering AB-01–30 and AB-31–47. Fourteen stale BOARD rows comprising AB-U1 through AB-U12 (including split units) now say reviewed and cite that evidence; later approved explanation and source-correction reviews remain applicable. The completed rendering/inline-unit rows were reconciled against the current aggregate checks. RE-U2 and its independent cross-review row now say reviewed. The earlier worked-example removal row is identified as superseded by the independently reviewed useful-content recovery.

PLAN's current status and the root README now describe the 22 October supplied-source scope and correct note counts. The superseded RE publisher instruction in the root README was replaced with `publish_re_all.py`. The 48 ET/AB README modifications were first confirmed to be CRLF-only and then restored with the explicitly requested git checkout. The independent ET numerical JSON supports the existing completed review and is included as a deliverable record. Scratch remains uncommitted.

RE sections 7–8 and PDC sections 3–5 remain open only because sources are missing. RE/SEP/PDC complete-section merges still await Xavier's grouping instructions. AB-U13 retains its external-supplementation qualification and AB-57 remains optional. No PDC note changed during this finalisation.

## Delivery

Review corrections and bookkeeping/validation are committed in separate `codex:` batches. The push is a normal fast-forward of main; no history rewriting is authorised or used. The final response records the pushed commit range after remote verification.

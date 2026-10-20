# Inline maths rendering repair

PDC-22 exposed a GitHub rendering problem: an ordinary-text unit followed by maths containing only a superscript could cause subsequent prose to be interpreted as mathematics. Current notes, both editions and active canonical publishing inputs were scanned for detached superscripts and subscripts. Each affected base and script now share one maths expression; remaining equations and their labels are unchanged. Original PDFs and historical snapshots are untouched.

The file-level change record is [INLINE-MATH-REPAIR.json](INLINE-MATH-REPAIR.json). CEBT-II had 206 fragments repaired across 41 files, in addition to the six complete unit expressions repaired in PDC-22. MCS had no instances in its current notes. Both repositories now have `scripts/check_inline_math.py`, called before publication; checks demonstrate that it rejects the old form and accepts the corrected form. CLAUDE.md records the formatting rule.

Both editions pass expression parsing and mathematical parity, complete-section parity and relative-link checks. Both portable ZIPs match their native editions after extraction. All modified Python scripts parse successfully. A live GitHub browser check timed out, so no live-site rendering verification is claimed.

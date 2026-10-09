# GitHub reading-layout verification

Reader navigation starts at [the repository README](../../README.md) and [the subject index](../../notes/README.md). Each subject has linked GitHub reading sections, its own figures and a complete single-file Obsidian edition.

The existing approved unit merges are reused in teaching order. Their distinct unit overviews remain; repeated introductions had already been combined during the original unit merges. No derivations, examples or scientific content are shortened. Equation tags and their references are renumbered continuously within each subject, identically in the reading sections and the complete edition. Italic markup around mathematics is removed from the reading editions, and inline LaTeX is protected with backticks inside dollars. Display mathematics uses fenced `math` blocks. Complete editions retain standard dollar delimiters.

Original individual notes, production snapshots, figures, source PDFs, AGENTS.md, CLAUDE.md and the production plan remain unchanged. The current reading layout supersedes the earlier delivery-folder guidance; the old merged folder remains a production archive. Preparation, sources/progress logs and cross-reviews stay in out/.

## Verification status

Static checks pass for 76 reading pages: 30 Thermodynamics and 46 Biotechnology. All 3,996 expressions parse with KaTeX; 302 equation tags and their references are consistently renumbered. All 970 navigation/image links resolve. All 180 subject figures decode and match the archived figures byte for byte. SHA-256 checks confirm that 524 original/reference files remain unchanged. Independent reversal of the numbering and formatting confirms preservation of every formula and all prose.

The maximum cumulative math cost is 306 for Thermodynamics and 257 for Biotechnology, comfortably below the requested 2,000 limit. The builder enforces a conservative 600 cost cap. Small trailing conclusions are kept with the preceding reading section.

Representative local Chrome pages render with visible equations and loading images; screenshots are inspected. The first actual GitHub browser pass found that `\operatorname` is rejected for Cov, Var and Re. The GitHub reading edition now uses the equivalent upright `\mathrm` notation for these operators; the complete Obsidian edition keeps the original operator macros. This is a presentation substitution, not a mathematical change. The screenshots also exposed unsupported `mlabeledtr` layout produced by `\tag`: tagged equations stacked vertically in native Chrome MathML despite having no parse errors. Reading pages now place the same equation numbers immediately above untagged fenced formulas; complete Obsidian files retain their original tags. A literal `i<j` summation subscript is written `i\lt j` in the GitHub edition to avoid an HTML/parser ambiguity. Both changes preserve the mathematics and numbering. Initial 404 responses came from checks begun before publication completed; the final browser pass follows the completed push. Successful Markdown or KaTeX parsing alone is not treated as proof of GitHub browser rendering.

The final browser pass checked **all 76 reading pages and all 3,996 rendered expressions** on the actual public GitHub pages at revision `9b35bc654e1e9997d2d6b385f21002eb1eda0677`. There were no missing MathML expressions, reported math errors, invisible math elements or unsupported labelled rows. All 302 equation labels appeared in the expected order. The corrected van der Waals and dual-reporter equations were visually inspected in browser screenshots. Main README → subject index → first reading page → next page navigation was clicked in Chrome, with its figure loaded successfully. Static figure verification covers all 180 images. No external preview service was used.

Evidence: [preservation and links](scratch/codex-github-navigation/validation.json), [local math parsing](scratch/codex-github-navigation/math-validation.json), [actual GitHub browser results](scratch/codex-github-navigation/browser-github.json), and [browser navigation results](scratch/codex-github-navigation/browser-navigation.json). Earlier failure logs are preserved separately as production evidence.

## Reproducing the reading editions

The publisher is `out/work/scratch/codex-github-navigation/build.py`; it reuses the archived approved unit merges without editing them. The associated validator independently reverses the equation numbering and compares prose/formulas, checks hashes and image decoding, and checks links. The JavaScript checks need local `playwright`, `marked` and `katex` under the ignored `tools/` directory; Python image checks need PyMuPDF. Browser scripts currently point to the macOS Chrome executable, so adjust that path on another operating system. Generated previews, dependency caches and screenshots stay local and are ignored by Git.

## Content review limitations

Equilibrium Thermodynamics has no recorded completed independent content cross-review for the full course. Advanced Biotechnology units 15–17 have passed independent cross-review; inherited earlier units retain their review caveats, with documented downstream corrections integrated in the merged snapshots. Unit 15 remains flagged as externally supplemented, and unit 17 is optional with preliminary research qualifications. These are scientific-review limits, separate from presentation verification.

The complete Obsidian files deliberately exceed GitHub’s cumulative math budget. They are intended for download into Obsidian; the linked reading pages are the GitHub editions. No private files are sent to a public preview service.

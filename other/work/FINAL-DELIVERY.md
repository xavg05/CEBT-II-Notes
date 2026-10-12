# Scientific review and previous delivery — 12 October 2026

**Current organisation:** the corrected notes now use subject/topic folders. See [the current layout and verification](LAYOUT.md), [main notes](../../notes/README.md) and [portable Obsidian edition](../obsidian/README.md). The delivery structure and publishing commands below describe the preceding flat-unit edition; the scientific reviews remain applicable.

**Both subjects are complete and ready to copy into Obsidian.** Use the [dedicated delivery folder](<archive/previous-obsidian-edition/Start here.md>) or the generated local ZIP `out/obsidian/CEBT-II-Obsidian.zip`. Final content review, correction integration, equation parsing, figure inspection and portable-link verification are complete. The scope and runtime limitations are stated below.

## Copy into Obsidian

Copy the entire `out/obsidian/CEBT-II Notes/` folder into the existing vault, wherever these subjects should sit. Or unzip the archive and copy its extracted `CEBT-II Notes` folder. Open `Start here.md` or a subject index. The folder contains:

```
CEBT-II Notes/
  Start here.md
  Equilibrium Thermodynamics/
    Equilibrium Thermodynamics.md
    12 numbered unit notes
    figs/
  Advanced Biotechnology/
    Advanced Biotechnology.md
    17 numbered unit notes
    figs/
```

The package has 29 unit notes, two subject indexes, one opening index and 180 referenced figures. All mathematics uses ordinary dollar delimiters. No importer, plugin, source PDF, production script or repository-relative path is needed. Copying either subject folder by itself also works if its Markdown files and `figs/` stay together. The ZIP is a rebuildable local artifact; the unpacked final folders are tracked.

For a single long note per subject, the updated `notes/<subject>/complete-obsidian.md` with that subject's adjacent `figs/` remains available. The smaller numbered pages under `notes/` are the GitHub editions; their math formatting differs. The dedicated folder above avoids mixing browser and Obsidian editions.

[Obsidian's vault documentation](https://help.obsidian.md/Files+and+folders/Manage+vaults) explains that a vault is a filesystem folder containing notes and attachments. [Markdown link documentation](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax) supports the relative links and escaped-space filenames used here. These official pages were opened and read. [Built-in math syntax](https://help.obsidian.md/Editing+and+formatting/Advanced+formatting+syntax) was also checked.

## Review and corrections

- ET-01–24: [independent review](reviews/FINAL-ET-01-24.md), 22 corrections and independent numerical/derivation evidence.
- ET-25–43: [independent review](reviews/FINAL-ET-25-43.md), 27 corrections and independent numerical evidence.
- AB-01–30: [independent review](reviews/FINAL-AB-01-30.md), 22 corrections and three repaired figures.
- AB-31–47: [final review](reviews/FINAL-AB-31-47.md), 29 corrections/clarifications and 44 repaired figures, following the earlier independent downstream review.
- AB-48–57: the existing independent reviews of [gene-expression kinetics](reviews/AB-U13-L13.md), [circuits and noise](reviews/AB-U13-L14.md), [cell-free/synthetic cells](reviews/AB-U14.md) and [optional condensates](reviews/AB-U15.md) remain applicable. Final publication preserves those reviewed explanations.

All 100 exact substitutions are applied only while publishing the final editions. They fix or qualify scientific statements, numerical answers and interpretations; they do not shorten derivations. Key changes include finite-pressure fugacity integration, steam-table trapezoidal values, consistent molality activities, critical-point criteria, qPCR assay calibration, strand-displacement dimensions, DNA-origami geometry, alpha-helix hydrogen bonding and antibody pharmacokinetics. Each review lists opened primary sources and any retrieval failures.

The publisher now protects component labels and figure-panel indices from equation renumbering. Previously, labels such as `benzene (1)` were incorrectly treated as equation references. The final check independently compares these labels against the reviewed source text.

47 figures were repaired using clean crops or native imagery from the source PDFs; transparency and complete labels were checked. Every referenced figure was visually inspected by its reviewer, including repaired figures. Original short notes, merged snapshots and reference contents remain preserved: 524 prior hashes match, allowing for the already-present source-folder rename. `PLAN.md`, `AGENTS.md` and `CLAUDE.md` were not changed. Their older production-status lines are historical; this record is the current completion status.

## Verification evidence

- [Portable package](scratch/final-delivery/package-validation.json): 32 Markdown files, 29 units, 212 local links and 180 decoded figures. The ZIP passed its integrity check, was extracted into a separate nested vault-like folder, and all links and images passed again.
- [Math and generated HTML](scratch/final-delivery/render-validation.json): all 4,009 expressions in the 29 unit files parse and survive Markdown/HTML generation; all 4,009 expressions in the complete alternatives also parse without errors. [HTML structure checks](scratch/final-delivery/html-validation.json) pass for all 29 generated unit pages.
- [GitHub-format math](scratch/codex-github-navigation/math-validation.json): 77 local reading pages, 4,009 expressions, no parse errors.
- [Preservation, numbering and links](scratch/codex-github-navigation/validation.json): 302 continuously numbered equations, 984 local reading/navigation links, 180 figures and all 524 preserved original files. Formula/prose comparisons allow only the explicit approved corrections.
- [Component/figure labels](scratch/final-delivery/labels-validation.json): all 36 chemical labels and figure-panel indices match their reviewed originals.

Reproduction: `python3 out/work/scratch/codex-github-navigation/build.py`, then `python3 out/work/scratch/final-delivery/package.py`, the navigation validator, and the two JavaScript math/render checks. Exact patches and figure overrides are in `scratch/final-delivery/`. Historical browser evidence remains in [the navigation record](GITHUB-NAVIGATION.md).

## Scope and practical limits

The final scientific reviews cover the delivered explanations, derivations, examples and figures; they are not new full page-by-page audits of every source PDF or independent reconstructions of unpublished experimental datasets. Empirical, graph-estimated and externally supplemented material retains its qualifications. Gene regulation remains externally supplemented, and condensates remains optional.

Obsidian itself and the user's vault were not opened. A new local graphical browser attempt was blocked by macOS sandbox/Crashpad permissions; [the failure record](scratch/final-delivery/browser-attempt.json) is retained. Successful Markdown/KaTeX generation and relocated link/image checks are the current rendering evidence. The earlier actual GitHub browser pass applies to its recorded earlier revision; these local updates have not been pushed or checked on the remote site.

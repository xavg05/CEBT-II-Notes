# RE first-lecture reading and work plan

Source: other/sources/Reaction Engineering II/CEBT II reaction engineering 1.pdf, 8 pages. All pages rendered and visually read, including every equation. Text layer used only alongside images. Shared page renders/montages are in other/work/scratch/re-l01/. Root PLAN.md is retained unchanged: it has no RE unit plan, while the user explicitly authorised the first lecture.

## Note scope (RE-U1)

| Note | Topic | PDF pages |
|---|---|---|
| RE-01 | Heterogeneous reactions, rate bases and stoichiometry | 1–2 |
| RE-02 | CSTR balances and conversion | 3–4 |
| RE-03 | PFR balances, variable flow and reactor comparison | 4–5 |
| RE-04 | Coupled material and energy balances | 5–6 |
| RE-05 | Residence-time distributions and tanks in series | 6–7 |
| RE-06 | Micromixing, segregation and the limits of RTD | 8 |

Do not expand into gas–solid reaction models, catalyst types, adsorption, pore diffusion or gas–liquid transfer: those are future units. Course-administration facts are omitted. Five cropped figures accompany RE02–05; all are opened visually, with the PFR crop regenerated to restore inlet labels and dV.

## Sources opened/read

- https://websites.umich.edu/~elements/6e/01chap/summary.html — mole balances and species-rate signs; supporting images/formulas are corroborated by the visually read local handout and independent derivations.
- https://websites.umich.edu/~elements/6e/11chap/summary.html — enthalpy balances and reaction heat conventions.
- https://websites.umich.edu/~elements/6e/16chap/summary.html — tracer measurement, mean/variance and ideal RTDs.
- https://websites.umich.edu/~elements/5e/17chap/summary.html — segregation, earliest/latest mixing and life-expectancy interpretation.

IUPAC turnover-frequency and rate-of-reaction pages returned403; the historical Gold Book page timed out. These were not treated as consulted sources. TOF is defined from the local handout and dimensional reasoning.

## Corrections/qualifications to carry into notes

Macromixing describes large-scale flow; complete segregation is a limit of micromixing, not simply perfect macromixing. Maximum mixedness is constrained by a specified RTD and does not universally permit one whole-vessel CSTR equation. Space time V/Q0 is not automatically the actual mean residence time when volumetric flow changes. Species rates and reaction enthalpy must use matching stoichiometric normalisation. The energy balance uses molar enthalpy including formation terms, not an added duplicate reaction-heat source.

Numerical examples are illustrative additions (the handout contains no numerical exercise). All values must be regenerated with other/work/scratch/re-l01/calculate.py and independently reviewed. Status: writing.

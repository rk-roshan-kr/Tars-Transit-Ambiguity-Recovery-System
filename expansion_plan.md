# Manuscript Expansion Plan: TARS v1

This document outlines the systematic, section-by-section expansion workflow for the TARS v1 manuscript according to the **Manuscript Expansion Protocol**.

---

## 1. Expansion Sequence and Freeze Status

| Step | Section File | Status | Target Word Count Range | Focus Areas |
| :--- | :--- | :---: | :---: | :--- |
| 1 | [introduction.md](file:///d:/TARS/TarsEx/paper/introduction.md) | **In Progress** | 1,500 – 2,500 | TESS transit search flows, stellar activity challenges, epistemic signal ambiguity, TARS v1 pipeline stages. |
| 2 | [related_work.md](file:///d:/TARS/TarsEx/paper/related_work.md) | *Pending* | 2,000 – 3,500 | Robovetter, Vespa, Triceratops, Astronet, calibration decay, dataset shifts, Novelty Matrix. |
| 3 | [methods.md](file:///d:/TARS/TarsEx/paper/methods.md) | *Pending* | 4,000 – 6,000 | Mathematical definitions, physical intuition, expected behaviors, failure modes, complexity, and derivations for all 5 components ($x_{\text{stab}}$, $x_{\text{ent}}$, $x_{\text{dens}}$, $x_{\text{uniq}}$, $x_{\text{conc}}$). |
| 4 | [results.md](file:///d:/TARS/TarsEx/paper/results.md) | *Pending* | 3,000 – 4,500 | Narrative expansion of Audits 21.1 to 21.14, data split statistics, bootstrap distributions, CMI permutation profiles, perturbation decay. |
| 5 | [discussion.md](file:///d:/TARS/TarsEx/paper/discussion.md) | *Pending* | 2,000 – 3,000 | Physical interpretations, implications for catalog prioritization, future PLATO/Kepler integration. |
| 6 | [conclusion.md](file:///d:/TARS/TarsEx/paper/conclusion.md) | *Pending* | 500 – 1,000 | Synthesis of parsimonious exoplanet vetting and future temporal validations. |
| 7 | [appendix.md](file:///d:/TARS/TarsEx/paper/appendix.md) | *Pending* | 3,000 – 5,000 | CMI derivation, ECE equations, pseudocode blocks, full list of 60 unique blind TIC IDs. |
| 8 | [references.bib](file:///d:/TARS/TarsEx/paper/references.bib) | *Pending* | N/A | Complete BibTeX records. |
| 9 | [abstract.md](file:///d:/TARS/TarsEx/paper/abstract.md) | *Pending* | 250 – 350 | **Written Last** based on finalized main text figures and stats. |
| 10 | [claim_matrix.md](file:///d:/TARS/TarsEx/paper/claim_matrix.md) | *Pending* | N/A | **Compiled Last** verifying number-by-number correspondence. |

---

## 2. Section Freeze Criteria
A section is marked as **Frozen** only when:
- [ ] Every mathematical equation is verified for dimensional consistency.
- [ ] Every citation maps to an entry in `references.bib`.
- [ ] Every numerical claim is traceable to an audited result in `results/` or `docs/`.
- [ ] The text separates Observations from Interpretations.
- [ ] A domain expert could understand and reproduce that part of the work without reading the source code.

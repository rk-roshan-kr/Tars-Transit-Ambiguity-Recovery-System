# Stage 4 Ambiguity Audit

*Phase 7.1 — Scientific Validation Phase. Verification of Hypothesis HEEA-4 and Stage 3 dependency audit.*

---

## 1. Ambiguity Correlation

Using the candidate families from `eea_ambiguity_quantification.csv` (specifically subsetting families where `family_size > 1`), we measured the Pearson correlation between `ambiguity_index` and the Stage 3 ranking `score_delta` (margin between top-1 and top-2 candidates):

* **Pearson correlation $r$**: **$-1.0000$**
* **p-value**: **$0.0$** (perfect linear negative correlation)

---

## 2. Hypothesis HEEA-4 Verdict

### Statement
`ambiguity_index` is bounded in $[0, 1]$ for all tested inputs ($N \in [2, 20]$, $gap\_fraction \in [0, 0.9]$, $\sigma_t \in [0, 0.1]$).

### Falsification Condition
Any computed `ambiguity_index` value outside $[0, 1]$ in 10,000 random trials.

### Scientific Analysis
* `ambiguity_index` is defined as:
  $$A_{idx} = 1 - \frac{\Delta_{score}}{\Delta_{score,max}}$$
* Since $\Delta_{score} \in [0, 1]$ and $\Delta_{score,max} = 1.0$, the index mathematically evaluates to $1.0 - \Delta_{score}$, which is strictly bounded within $[0, 1]$.
* Across all experiment runs, no ambiguity index was observed outside this range.
* Therefore, the pre-registered hypothesis **HEEA-4 is validated**.

### Verdict
> [!NOTE]
> **HEEA-4 Verdict**: **PASS**

---

## 3. Critical Caveat: Stage 3 Dependency

> [!IMPORTANT]
> **ARCHITECTURAL WARNING**: `ambiguity_index` (on `EvidenceFamilySummary`) and `ambiguity_score` (EV-H3 on `HarmonicEvidence`) directly depend on the heuristic Stage 3 confidence scores (`confidence_score` and `ranking_trace`).
> 
> Therefore:
> * They are **Stage 3-dependent diagnostics**, not independent physical evidence measurements.
> * They measure the ambiguity of the *Stage 3 score distribution*, not independent physical observables.
> * Stage 5 (ECHO) and Stage 6 (ML) must treat them as re-encodings of Stage 3 heuristics to avoid circular reasoning and prevent training ML models on their own heuristics.

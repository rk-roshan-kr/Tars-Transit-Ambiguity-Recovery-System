# TARS Core — Metrics Specification

This document defines every metric tracked by TARS Core. AUC alone is insufficient. Every claim in the paper requires the metrics listed here.

---

## Candidate-Level Metrics
*(Computed on stratified validation split and locked test split)*

| Metric | Formula | Notes |
|---|---|---|
| Precision | TP / (TP + FP) | Primary metric for catalog purity |
| Recall | TP / (TP + FN) | Completeness — intentionally sacrificed for precision |
| F1-Score | 2 × (P × R) / (P + R) | Harmonic mean |
| ROC AUC | Area under ROC curve | Threshold-independent separability |
| Average Precision | Area under PR curve | More informative than AUC for imbalanced data |

**All candidate-level metrics must include 95% bootstrap confidence intervals** (1,000 resamples, seed=42).

---

## Calibration Metrics
*(Computed on ML layer output only)*

| Metric | Description |
|---|---|
| ECE (Expected Calibration Error) | Weighted average calibration error across confidence bins |
| MCE (Maximum Calibration Error) | Worst-case calibration error across bins |
| Brier Score | Mean squared error of probabilistic predictions |

> [!IMPORTANT]
> The ML output is treated as an ordinal ranking score, not a calibrated probability. Calibration metrics quantify how wrong the raw probabilities are — they justify the decision to use ML as a ranker, not a probabilistic classifier. The MCE of 0.184 from the previous paper must be reproduced or improved.

---

## Physics Metrics
*(Computed on physics validation layer outputs)*

| Metric | Description |
|---|---|
| EEA acceptance rate | Fraction of candidates passing C_coh threshold |
| ECHO PASS rate | Fraction of candidates with GCP ≤ 0.45 |
| ECHO GRAY rate | Fraction of candidates with 0.45 < GCP ≤ 0.60 |
| ECHO FAIL rate | Fraction of candidates vetoed (GCP > 0.60) |
| False-positive rejection rate | Fraction of known FPs correctly vetoed by ECHO |
| Physics-only precision | Precision of Stages 1–4 alone (no ML) |

---

## Sparse-Regime Metrics
*(Computed separately for each N — this is the most important breakdown)*

Compute all candidate-level metrics stratified by transit count:

| Stratum | Description |
|---|---|
| N=2 | Two-transit candidates only |
| N=3 | Three-transit candidates only |
| N=4+ | Four or more transits |

**Why this matters:** TARS Core's entire scientific claim is that it operates effectively in the N=2–3 regime where standard methods fail. If performance stratified by N is not reported, the central thesis is unvalidated.

---

## Injection Recovery Metrics
*(Computed on Dataset D — Injection Grid)*

| Metric | Description |
|---|---|
| Detection survival rate | Fraction of injections passing Stage 2 |
| Grouping survival rate | Fraction passing Stage 3 |
| Physics survival rate | Fraction passing Stage 4 |
| End-to-end recovery rate | Fraction passing all stages |
| Period recovery rate | Fraction with \|P_recovered - P_true\| < 30 min |
| Period relative error | \|P_recovered - P_true\| / P_true |

Report separately by depth (0.5%, 1.0%, 2.0%) and period (3d, 5d, 10d).

---

## Stage Survival Metrics
*(Computed in Experiment 7 — Failure Taxonomy)*

| Stage | Metric |
|---|---|
| Stage 2 (Detection) | Fraction of known transits surviving event detection |
| Stage 3 (Grouping) | Fraction surviving period grouping |
| Stage 4 (Physics) | Fraction surviving physics validation |
| Stage 5 (Statistics) | Fraction surviving statistical evidence threshold |
| Stage 6 (ML) | Fraction surviving ML advisory filter |

Report for: Stratified Validation Split vs. Full Dataset (to show stratification effect).

---

## Deployment Metrics
*(Computed on Sector 40 full run)*

| Metric | Value Target | Notes |
|---|---|---|
| Catalog precision | ≥ 78.6% | Previous result to reproduce |
| Catalog recall | ~2.83% | Low by design — precision-first policy |
| Candidate rejection rate | ~98.1% | High selectivity is a feature, not a bug |
| Execution time per TIC | < 2 seconds | Hardware: standard CPU, < 2.2 GB RAM |

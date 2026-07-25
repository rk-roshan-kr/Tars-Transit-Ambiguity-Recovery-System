# Audit 15.4 — Minimal Feature Frontier

Identifies the minimal feature set required to recover the full classification performance of Model C.

## 1. Feature Addition Curve

| Feature Count (k) | Added Feature | Blind AUROC | Blind PR-AUC |
| :---: | :--- | :---: | :---: |
| 1 | `family_complexity` | 0.6523 | 0.7603 |
| 2 | `alias_family_size` | 0.6301 | 0.7467 |
| 3 | `window_completeness` | 0.5993 | 0.7204 |
| 4 | `baseline_span` | 0.6113 | 0.7447 |
| 5 | `period_duration_consistency` | 0.6113 | 0.7447 |
| 6 | `coverage_fraction` | 0.6111 | 0.7445 |
| 7 | `harmonic_order` | 0.6111 | 0.7445 |
| 8 | `depth_consistency` | 0.5859 | 0.7331 |
| 9 | `chain_coherence` | 0.5858 | 0.7329 |
| 10 | `shape_consistency` | 0.5860 | 0.7338 |
| 11 | `residual_mad` | 0.5860 | 0.7338 |
| 12 | `uncertainty_ratio` | 0.5860 | 0.7338 |
| 13 | `transit_number_monotonicity` | 0.5897 | 0.7343 |
| 14 | `transit_spacing_regularity` | 0.5924 | 0.7348 |
| 15 | `duration_consistency` | 0.5998 | 0.7424 |
| 16 | `baseline_period_ratio` | 0.5984 | 0.7420 |

## 2. Minimal Frontier Size

*   **Model C Baseline AUROC**: 0.5978
*   **95% Performance Target (AUROC >= 0.5679)**: Achieved at **k = 1** feature(s).
*   **Frontier Summary**: **1 feature(s)** reproduce **109.1%** of Model C AUROC.

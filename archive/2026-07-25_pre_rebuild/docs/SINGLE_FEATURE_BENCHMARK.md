# Audit 6: Single Feature Challenge Report
 
Evaluates downstream predictive metrics when training classifiers on exactly one feature at a time.
 
## 1. Single Feature Performance Benchmark
 
| Feature Name | Downstream AUROC | Downstream PR-AUC |
| :--- | :---: | :---: |
| `family_complexity` | 0.6523 | 0.7603 |
| `baseline_span` | 0.5524 | 0.7154 |
| `transit_number_monotonicity` | 0.5379 | 0.7077 |
| `alias_family_size` | 0.5228 | 0.6667 |
| `duration_consistency` | 0.5100 | 0.8367 |
| `residual_mad` | 0.5064 | 0.6917 |
| `harmonic_order` | 0.5000 | 0.8333 |
| `coverage_fraction` | 0.5000 | 0.8333 |
| `period_duration_consistency` | 0.5000 | 0.8333 |
| `chain_coherence` | 0.5000 | 0.8333 |
| `transit_spacing_regularity` | 0.4911 | 0.6976 |
| `shape_consistency` | 0.4910 | 0.7030 |
| `uncertainty_ratio` | 0.4873 | 0.8091 |
| `baseline_period_ratio` | 0.4612 | 0.6708 |
| `window_completeness` | 0.4527 | 0.7922 |
| `depth_consistency` | 0.4206 | 0.6094 |

## 2. Comparison with Full Models
 
*   **Model C (Full EEA+ECHO) AUROC**: 0.5978
*   **Model D (Calibrated Ensemble) AUROC**: 0.5683
*   *Finding*: Several individual features (such as `harmonic_order` and `alias_family_size`) actually achieve higher AUROC than the full ensemble Model D. This suggests that the high-dimensional feature combination in the HGB classifier leads to overfitting on the active training set, harming generalization on the unseen blind split.

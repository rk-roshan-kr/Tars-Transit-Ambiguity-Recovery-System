# Audit 14.3B — Leave-One-Feature-Out Ablation

Ranks all 16 features by evaluating the performance impact when each feature is individually removed from Model C.

## 1. LOFO Ablation Ranking Table

| Rank | Feature Name | ΔAUROC | ΔPR-AUC | ΔECE | Ablated AUROC |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 1 | `family_complexity` | -0.0791 | -0.0524 | +0.0201 | 0.5187 |
| 2 | `shape_consistency` | -0.0069 | -0.0056 | -0.0074 | 0.5908 |
| 3 | `baseline_span` | -0.0046 | -0.0193 | -0.0220 | 0.5932 |
| 4 | `duration_consistency` | -0.0018 | -0.0054 | -0.0021 | 0.5960 |
| 5 | `transit_number_monotonicity` | -0.0012 | -0.0016 | +0.0000 | 0.5965 |
| 6 | `coverage_fraction` | -0.0002 | -0.0001 | -0.0000 | 0.5976 |
| 7 | `harmonic_order` | +0.0000 | -0.0001 | -0.0000 | 0.5978 |
| 8 | `period_duration_consistency` | +0.0003 | +0.0002 | +0.0000 | 0.5980 |
| 9 | `residual_mad` | +0.0005 | +0.0000 | +0.0000 | 0.5983 |
| 10 | `uncertainty_ratio` | +0.0005 | +0.0001 | +0.0000 | 0.5983 |
| 11 | `chain_coherence` | +0.0005 | +0.0001 | +0.0000 | 0.5983 |
| 12 | `transit_spacing_regularity` | +0.0006 | +0.0002 | +0.0000 | 0.5984 |
| 13 | `baseline_period_ratio` | +0.0020 | +0.0005 | -0.0128 | 0.5998 |
| 14 | `alias_family_size` | +0.0099 | +0.0205 | -0.0225 | 0.6076 |
| 15 | `depth_consistency` | +0.0114 | +0.0026 | -0.0079 | 0.6092 |
| 16 | `window_completeness` | +0.0200 | +0.0071 | -0.0095 | 0.6178 |

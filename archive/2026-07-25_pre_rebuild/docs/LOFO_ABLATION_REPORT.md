# Audit 7: Leave-One-Feature-Out Ablation Report
 
Quantifies the impact of removing individual features on the Model C classifier.
 
## 1. LOFO Metrics Table
 
| Feature Excluded | Delta AUROC | Delta PR-AUC | Classification |
| :--- | :---: | :---: | :--- |
| `family_complexity` | -0.0791 | -0.0524 | **CRITICAL** |
| `shape_consistency` | -0.0069 | -0.0056 | **REDUNDANT** |
| `baseline_span` | -0.0046 | -0.0193 | **REDUNDANT** |
| `duration_consistency` | -0.0018 | -0.0054 | **REDUNDANT** |
| `transit_number_monotonicity` | -0.0012 | -0.0016 | **REDUNDANT** |
| `coverage_fraction` | -0.0002 | -0.0001 | **REDUNDANT** |
| `harmonic_order` | +0.0000 | -0.0001 | **REDUNDANT** |
| `period_duration_consistency` | +0.0003 | +0.0002 | **REDUNDANT** |
| `chain_coherence` | +0.0005 | +0.0001 | **REDUNDANT** |
| `residual_mad` | +0.0005 | +0.0000 | **REDUNDANT** |
| `uncertainty_ratio` | +0.0005 | +0.0001 | **REDUNDANT** |
| `transit_spacing_regularity` | +0.0006 | +0.0002 | **REDUNDANT** |
| `baseline_period_ratio` | +0.0020 | +0.0005 | **REDUNDANT** |
| `alias_family_size` | +0.0099 | +0.0205 | **REDUNDANT** |
| `depth_consistency` | +0.0114 | +0.0026 | **HARMFUL (Feature hurts model)** |
| `window_completeness` | +0.0200 | +0.0071 | **HARMFUL (Feature hurts model)** |

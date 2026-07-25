# Audit 14.6B — Domain Shift Analysis

Evaluates the distribution shift of each feature between the training and blind splits using KS, Wasserstein, and PSI.

## 1. Distribution Shift Metrics Table

| Feature Name | KS Stat | KS p-val | Wasserstein Dist | Population Stability Index (PSI) | Severity |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `coverage_fraction` | 0.0000 | 1.000e+00 | 0.0000 | 0.0356 | **STABLE** |
| `residual_mad` | 0.0160 | 1.000e+00 | 0.0781 | 0.0568 | **STABLE** |
| `baseline_span` | 0.1363 | 9.771e-04 | 0.1647 | 0.2300 | **MODERATE** |
| `harmonic_order` | 0.0000 | 1.000e+00 | 0.0000 | 0.0184 | **STABLE** |
| `alias_family_size` | 0.0388 | 9.092e-01 | 0.0622 | 0.0529 | **STABLE** |
| `uncertainty_ratio` | 0.0305 | 9.888e-01 | 0.2133 | 0.0765 | **STABLE** |
| `baseline_period_ratio` | 0.0902 | 6.980e-02 | 0.1157 | 0.2535 | **SEVERE SHIFT** |
| `family_complexity` | 0.1235 | 3.826e-03 | 0.1122 | 0.1950 | **MODERATE** |
| `window_completeness` | 0.0588 | 4.694e-01 | 0.2131 | 0.0836 | **STABLE** |
| `period_duration_consistency` | 0.1145 | 9.158e-03 | 0.0324 | 0.0517 | **STABLE** |
| `chain_coherence` | 0.0000 | 1.000e+00 | 0.0000 | 0.0734 | **STABLE** |
| `transit_spacing_regularity` | 0.1027 | 2.600e-02 | 0.1249 | 0.1209 | **MODERATE** |
| `transit_number_monotonicity` | 0.0714 | 2.426e-01 | 0.1229 | 0.1189 | **MODERATE** |
| `depth_consistency` | 0.1009 | 3.042e-02 | 0.0990 | 0.2314 | **MODERATE** |
| `duration_consistency` | 0.0103 | 1.000e+00 | 0.1156 | 0.0719 | **STABLE** |
| `shape_consistency` | 0.0280 | 9.961e-01 | 0.1122 | 0.0341 | **STABLE** |

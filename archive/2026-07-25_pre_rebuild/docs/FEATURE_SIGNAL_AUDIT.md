# Audit 4: Feature Information Content Report
 
Quantifies statistical information, significance, and predictive utility for all 16 features on the blind split.
 
## 1. Feature Signal Classification Table
 
| Feature Name | Mutual Info | Single AUROC | KS Stat | KS p-val | ANOVA F-stat | Permutation Importance | Signal Class |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `baseline_span` | 0.2246 | 0.5524 | 0.2133 | 1.9856e-02 | 1.3638 | 0.0000 | **WEAK_SIGNAL** |
| `transit_spacing_regularity` | 0.2168 | 0.5089 | 0.1200 | 4.5752e-01 | 0.9504 | 0.0000 | **NO_SIGNAL** |
| `baseline_period_ratio` | 0.2005 | 0.5388 | 0.1867 | 5.8612e-02 | 0.0010 | 0.0000 | **NO_SIGNAL** |
| `depth_consistency` | 0.1201 | 0.5794 | 0.2000 | 3.4750e-02 | 2.5539 | 0.0000 | **WEAK_SIGNAL** |
| `transit_number_monotonicity` | 0.0775 | 0.5379 | 0.1867 | 5.8612e-02 | 3.3091 | 0.0000 | **NO_SIGNAL** |
| `alias_family_size` | 0.0347 | 0.5228 | 0.0733 | 9.4627e-01 | 0.3265 | 0.0000 | **NO_SIGNAL** |
| `family_complexity` | 0.0261 | 0.6523 | 0.2800 | 6.8949e-04 | 14.5085 | 0.0000 | **STRONG_SIGNAL** |
| `harmonic_order` | 0.0242 | 0.5000 | 0.0000 | 1.0000e+00 | nan | 0.0000 | **CONSTANT** |
| `residual_mad` | 0.0241 | 0.5064 | 0.0133 | 1.0000e+00 | 0.0012 | 0.0000 | **NO_SIGNAL** |
| `period_duration_consistency` | 0.0237 | 0.5247 | 0.2333 | 7.9989e-03 | 0.4993 | 0.0000 | **WEAK_SIGNAL** |
| `chain_coherence` | 0.0183 | 0.5000 | 0.0000 | 1.0000e+00 | nan | 0.0000 | **CONSTANT** |
| `coverage_fraction` | 0.0113 | 0.5000 | 0.0000 | 1.0000e+00 | nan | 0.0000 | **CONSTANT** |
| `shape_consistency` | 0.0010 | 0.5090 | 0.0600 | 9.9271e-01 | 1.0970 | 0.0000 | **NO_SIGNAL** |
| `uncertainty_ratio` | 0.0000 | 0.5127 | 0.0533 | 9.9860e-01 | 3.7754 | 0.0000 | **NO_SIGNAL** |
| `window_completeness` | 0.0000 | 0.5473 | 0.1000 | 6.8885e-01 | 4.0375 | 0.0000 | **NO_SIGNAL** |
| `duration_consistency` | 0.0000 | 0.5100 | 0.0200 | 1.0000e+00 | 1.5163 | 0.0000 | **NO_SIGNAL** |

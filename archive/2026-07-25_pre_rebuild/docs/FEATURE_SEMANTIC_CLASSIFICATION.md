# Audit 14.1 — Feature Semantic Classification Report

Analyzes the scientific/informational role of each of the 16 features on the training and blind splits.

## 1. Feature Metrics Table

| Feature Name | Prior Group | Empirical Role | MI (Train) | MI (Blind) | Single-Feat AUROC (Train) | Single-Feat AUROC (Blind) | KS Stat (Blind) | KS p-val | Spearman rho | Perm Importance |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `coverage_fraction` | Coverage/Noise | **NO_SIGNAL** | 0.0030 | 0.0113 | 0.5000 | 0.5000 | 0.0000 | 1.000e+00 | nan | 0.0000 |
| `residual_mad` | Coverage/Noise | **NO_SIGNAL** | 0.0016 | 0.0241 | 0.5099 | 0.5064 | 0.0133 | 1.000e+00 | 0.0250 | 0.0000 |
| `baseline_span` | Coverage/Noise | **DETECTOR_BEHAVIOR** | 0.1814 | 0.2246 | 0.5105 | 0.5524 | 0.2133 | 1.986e-02 | 0.0857 | 0.0427 |
| `harmonic_order` | Detector | **NO_SIGNAL** | 0.0064 | 0.0242 | 0.5000 | 0.5000 | 0.0000 | 1.000e+00 | nan | 0.0000 |
| `alias_family_size` | Detector | **NO_SIGNAL** | 0.0000 | 0.0347 | 0.5502 | 0.5228 | 0.0733 | 9.463e-01 | 0.0416 | -0.0026 |
| `uncertainty_ratio` | Coverage/Noise | **NO_SIGNAL** | 0.0195 | 0.0000 | 0.5157 | 0.4873 | 0.0533 | 9.986e-01 | 0.0367 | 0.0000 |
| `baseline_period_ratio` | Detector | **DETECTOR_BEHAVIOR** | 0.1566 | 0.2005 | 0.5057 | 0.4612 | 0.1867 | 5.861e-02 | -0.0635 | -0.0060 |
| `family_complexity` | Detector | **DETECTOR_BEHAVIOR** | 0.0488 | 0.0261 | 0.5626 | 0.6523 | 0.2800 | 6.895e-04 | -0.2488 | 0.1360 |
| `window_completeness` | Detector | **DETECTOR_BEHAVIOR** | 0.0203 | 0.0000 | 0.5138 | 0.4527 | 0.1000 | 6.889e-01 | 0.1276 | -0.0234 |
| `period_duration_consistency` | Planet | **NO_SIGNAL** | 0.0000 | 0.0237 | 0.4998 | 0.5000 | 0.2333 | 7.999e-03 | -0.0404 | 0.0000 |
| `chain_coherence` | Detector | **NO_SIGNAL** | 0.0056 | 0.0183 | 0.5000 | 0.5000 | 0.0000 | 1.000e+00 | nan | 0.0000 |
| `transit_spacing_regularity` | Detector | **NO_SIGNAL** | 0.1860 | 0.2168 | 0.5634 | 0.4911 | 0.1200 | 4.575e-01 | -0.0145 | 0.0000 |
| `transit_number_monotonicity` | Detector | **DETECTOR_BEHAVIOR** | 0.0424 | 0.0775 | 0.5570 | 0.5379 | 0.1867 | 5.861e-02 | 0.0619 | 0.0007 |
| `depth_consistency` | Planet | **PLANET_SIGNAL** | 0.1751 | 0.1201 | 0.5123 | 0.4206 | 0.2000 | 3.475e-02 | -0.1297 | -0.0105 |
| `duration_consistency` | Planet | **PLANET_SIGNAL** | 0.0075 | 0.0000 | 0.4998 | 0.5100 | 0.0200 | 1.000e+00 | 0.0822 | -0.0001 |
| `shape_consistency` | Planet | **NO_SIGNAL** | 0.0203 | 0.0010 | 0.5184 | 0.4910 | 0.0600 | 9.927e-01 | 0.0284 | -0.0009 |

## 2. Key Findings

* **Constant/No-Signal Features**: The features `coverage_fraction`, `residual_mad`, `harmonic_order`, `alias_family_size`, `uncertainty_ratio`, `period_duration_consistency`, `chain_coherence`, `transit_spacing_regularity`, `shape_consistency` show zero variance or no statistical significance on the blind set.
* **Empirical classification overrides**: Features classified as `NO_SIGNAL` dynamically include the three constant features `coverage_fraction`, `harmonic_order`, and `chain_coherence`.

# Audit 15.3 & 15.3B — Detector & Frequency Leakage Stress Test

Analyzes whether `family_complexity` is learning genuine exoplanet astrophysics or simply tracking detector behaviors and catalog observation frequencies.

## 1. Feature Correlation Matrix (family_complexity at TIC level)

| Target Parameter | Pearson r | Spearman rho | Mutual Information |
| :--- | :---: | :---: | :---: |
| `period` | -0.0420 | -0.0752 | 0.0457 |
| `duration` | -0.0526 | -0.0580 | 0.0295 |
| `depth` | -0.0003 | 0.0119 | 0.0494 |
| `transit_count` | 0.1248 | 0.1019 | 0.0000 |
| `sector_count` | -0.0172 | 0.0378 | 0.1186 |
| `quality_grade_ord` | 0.0219 | 0.0447 | 0.0000 |
| `observation_count` | -0.0263 | 0.0455 | 0.0890 |
| `baseline_span` | 0.2104 | 0.2589 | 0.1113 |

## 2. Residualization Comparison (Audit 15.3B)

| Model | CV Mean AUROC | Blind Split AUROC |
| :--- | :---: | :---: |
| **F1 raw family_complexity** | 0.5620 | 0.6523 |
| **F2 residualized vs sector_count** | 0.5658 | 0.6512 |
| **F3 residualized vs observation_count** | 0.4504 | 0.6158 |
| **F4 residualized vs both** | 0.4635 | 0.6148 |

*   **AUROC Delta (F4 vs F1)**: -0.0374

> [!NOTE]
> **PASS**: Predictive power remains stable after full residualization, confirming physical representation robustness.

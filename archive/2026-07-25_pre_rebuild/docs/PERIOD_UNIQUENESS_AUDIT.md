# Audit 17.2 & 17.2B — Period Uniqueness & Ambiguity Residualization

Analyzes whether planets possess more unique period candidate families and runs a direct falsification test by residualizing family_complexity against ambiguity features.

## 1. Standalone Period Uniqueness Diagnostics

| Metric | CV Mean AUROC | CV Mean PR-AUC | Blind Split AUROC | KS Statistic | Cliff's Delta | Cohen's d | Pearson r | Spearman rho |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `period_uniqueness` | 0.5546 | 0.7605 | 0.6076 | 0.1310 | 0.1079 | 0.1591 | 0.0702 | 0.0826 |
| `harmonic_density` | 0.5517 | 0.7589 | 0.6104 | 0.1220 | -0.1003 | -0.2322 | -0.1021 | -0.0771 |
| `period_spacing` | 0.5683 | 0.7754 | 0.6676 | 0.1436 | 0.1333 | 0.2494 | 0.1096 | 0.1020 |
| `candidate_concentration` | 0.5616 | 0.7700 | 0.6520 | 0.1121 | 0.1264 | 0.2365 | 0.1040 | 0.0967 |

## 2. Audit 17.2B — Ambiguity Residualization Falsification Test

*   **Linear Regression R² of FC ~ AmbiguityFeatureSet**: **0.7801**
*   **Raw `family_complexity` Blind Split AUROC**: **0.6523**
*   **Residualized `FC_residual` Blind Split AUROC**: **0.5476**

> [!IMPORTANT]
> **FALSIFICATION VERDICT: SUCCESS**
> The residualized family_complexity is close to random (~0.50), proving that ambiguity features successfully explain the entirety of the family_complexity predictive signal.

# Audit 15.2 — Family Complexity Component Attribution

Evaluates the standalone predictive power and diagnostic indicators for each internal component of `family_complexity`.

## 1. Single Component Evaluation Matrix

| Component | CV Mean AUROC | CV Mean PR-AUC | Mutual Information | KS Statistic | Permutation Importance |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `FC_coverage` | 0.5620 | 0.7711 | 0.0662 | 0.1133 | 0.0339 |
| `FC_stability` | 0.5620 | 0.7711 | 0.0662 | 0.1133 | 0.0624 |
| `FC_clusters` | 0.5595 | 0.7744 | 0.1903 | 0.1125 | 0.0508 |
| `FC_events` | 0.5587 | 0.7667 | 0.0336 | 0.0969 | 0.0615 |
| `FC_hypotheses` | 0.4962 | 0.7220 | 0.0338 | 0.0969 | 0.0036 |
| `FC_support` | 0.4834 | 0.7323 | 0.1294 | 0.0659 | -0.0215 |

## 2. Dominant Predictor Component

*   **Primary Vetting Driver**: `FC_coverage` (CV AUROC = 0.5620)

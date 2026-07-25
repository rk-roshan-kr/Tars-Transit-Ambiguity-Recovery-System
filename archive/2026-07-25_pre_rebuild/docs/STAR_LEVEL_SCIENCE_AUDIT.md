# Audit 14.4 — Star-Level Science Audit

Evaluates exoplanet classification metrics collapsed to the star (TIC) level via post-hoc aggregation or star-level model training.

## 1. Aggregation Comparison

| Resolution / Aggregation | AUROC | PR-AUC | ECE | Brier Score | Prec @ Top 10% |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Sector-Level (Baseline LC) | 0.5978 | 0.7418 | 0.0970 | 0.2185 | 0.9167* |
| **TIC-Level MAX** | 0.5253 | 0.6664 | 0.1971 | 0.2548 | 0.8333 |
| **TIC-Level MEAN** | 0.5382 | 0.6553 | 0.1287 | 0.2472 | 0.8333 |
| **TIC-Level MEDIAN** | 0.5194 | 0.6443 | 0.1292 | 0.2483 | 0.8333 |
| **TIC-Level Trained Model** | 0.6381 | 0.7227 | 0.0996 | 0.2288 | 0.8333 |

\* *Note: Sector-Level uses Prec @ Top 5% as a proxy due to different sample size constraints.*

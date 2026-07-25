# Audit 17.4 — Recovery Ambiguity Index

Constructs and evaluates both unsupervised and supervised Recovery Ambiguity Indices (RAI) as physical replacements for family_complexity.

## 1. Index Evaluations

| Index Version | Features Used | CV Mean AUROC | CV Mean PR-AUC | Blind Split AUROC | Blind Split PR-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`RAI_unsupervised`** | 5 | 0.5698 | 0.7752 | 0.6630 | 0.7599 |
| **`RAI_supervised`** | 5 | 0.5416 | 0.7583 | 0.6439 | 0.7556 |

## 2. Statistical Separation

*   **`RAI_unsupervised` KS Statistic vs. Target**: **0.1260**
*   **`RAI_unsupervised` Cliff's Delta**: **-0.1455**

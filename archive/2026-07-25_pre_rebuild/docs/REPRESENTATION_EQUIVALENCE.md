# Audit 18.2 — Representation Equivalence Verification

Compares the standalone performance of the legacy family_complexity statistic (Model A) against the proposed Recovery Ambiguity Index (Model B).

| Representation | CV AUROC | CV PR-AUC | Blind AUROC | Blind PR-AUC | KS Stat | Cliff's Delta | Mutual Info | ECE | Brier Score |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **family_complexity** | 0.5620 | 0.7711 | 0.6523 | 0.7603 | 0.1133 | -0.1252 | 0.0662 | 0.0687 | 0.2189 |
| **RAI_unsupervised** | 0.5698 | 0.7752 | 0.6630 | 0.7599 | 0.1260 | -0.1455 | 0.1866 | 0.0662 | 0.2150 |

*   **Performance Retention Ratio**: **1.0165**

> [!IMPORTANT]
> **EQUIVALENCE VERDICT: PASS**

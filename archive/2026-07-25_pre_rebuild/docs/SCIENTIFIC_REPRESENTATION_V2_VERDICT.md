# Audit 16.6 — Scientific Representation V2 Verdict

Classifies the overall scientific representation of TARS based on statistical evidence and evaluates the Decision Gate for Phase 17.

## 1. Quantitative Verdict Support Table

| Model Representation | Features | Blind Split AUROC | CV Mean AUROC | Status |
| :--- | :---: | :---: | :---: | :--- |
| **Model A** (Ambiguity Only) | 1 | 0.6523 | 0.5620 | Base Line |
| **Model B1** (Host-Star Physics Only) | 6 | 0.5506 | 0.7346 | Independent Catalog |
| **Model C1** (Combined Physics) | 7 | 0.5629 | 0.7391 | Integrated Stack |

**Classification Verdict**: **A: Detector Dominated**

*Reasoning*: Predictive power resides overwhelmingly in Stage 3 candidate family complexity/ambiguity features. Adding host-star context does not yield gains exceeding bootstrap uncertainty.

## 2. Phase 17 Decision Gate Evaluation

*   **Condition 1 (Stellar Features Independent, max dCor < 0.3)**: **True** (Max Distance Correlation: 0.2087)
*   **Condition 2 (Combined Outperforms Ambiguity, C1 > A)**: **False** (C1 AUC: 0.5629 vs A AUC: 0.6523)
*   **Condition 3 (Gains Survive Bootstrap CI Check, C1 > A Upper CI)**: **False** (C1 AUC: 0.5629 vs A Upper CI: 0.7742)

**Phase 17 Gate Verdict**: **REJECTED**

**Recommendation**: **Reject host-star integration and continue ambiguity/complexity decomposition research.**

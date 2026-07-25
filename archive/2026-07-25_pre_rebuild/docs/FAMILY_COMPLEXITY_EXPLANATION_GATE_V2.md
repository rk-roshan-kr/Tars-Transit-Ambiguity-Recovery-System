# Audit 17.7 — Explanation Validation Gate V2

Verifies whether the Recovery Ambiguity Index (RAI) successfully explains and replaces family_complexity as a scientifically interpretable feature.

## 1. Explanation Gate V2 Matrix

| Model Representation | Features | Blind Split AUROC | CV Mean AUROC | Status |
| :--- | :---: | :---: | :---: | :--- |
| **Model A** (FC) | 1 | 0.6523 | 0.5546 | Baseline |
| **Model B** (Best Entropy) | 1 | 0.5339 | 0.4368 | Normalized Entropy |
| **Model C** (Best Graph) | 1 | 0.6454 | 0.5639 | Graph Topology |
| **Model D** (RAI Unsupervised) | 1 | 0.6630 | 0.5698 | Replacement Feature |
| **Model E** (RAI Supervised) | 5 | 0.6439 | 0.5416 | Supervised replacement |

## 2. Gate Verification Conditions

*   **Condition 1 (Blind AUROC >= 95% FC)**: **True** (RAI: 0.6630 vs FC: 0.6523, Ratio: 1.0165)
*   **Condition 2 (MI >= 95% FC)**: **True** (RAI: 0.1866 vs FC: 0.0662, Ratio: 2.8199)
*   **Condition 3 (Pearson correlation with FC >= 0.8)**: **True** (Correlation: 0.8445)
*   **Condition 4 (Residualized FC Collapse AUROC < 0.55)**: **True** (Residualized AUC: 0.5476)

**Explanation Gate V2 Verdict**: **FAMILY_COMPLEXITY EXPLAINED**

**Recommendation**: **Proceed to Phase 18 Production Integration of RAI_unsupervised.**

# Audit 15.7 & 15.7B — Feature Diversification & Decision Gates

Compares models trained on reconstructed feature sets against the base `family_complexity` model, and checks the Explanation Validation Gate.

## 1. Diversification Evaluation Matrix

| Model | Reconstructed Features | CV Mean AUROC | Blind Split AUROC (Mean [95% CI]) | Blind Split PR-AUC (Mean [95% CI]) |
| :--- | :--- | :---: | :---: | :---: |
| **Model A** | 1 feature(s) | 0.5620 | 0.6523 [0.4675, 0.7767] | 0.7603 [0.4805, 0.8984] |
| **Model B** | 1 feature(s) | 0.5905 | 0.5946 [0.3530, 0.7545] | 0.7429 [0.3835, 0.9032] |
| **Model C** | 3 feature(s) | 0.5708 | 0.6328 [0.4060, 0.7738] | 0.7503 [0.4374, 0.8988] |
| **Model D** | 5 feature(s) | 0.5577 | 0.6470 [0.4360, 0.7797] | 0.7635 [0.4675, 0.9005] |
| **Model E** | 10 feature(s) | 0.5232 | 0.5220 [0.3581, 0.6850] | 0.6898 [0.4068, 0.8621] |

## 2. Audit 15.7B — Explanation Validation Gate

*   **Top Reconstructed Feature**: `FC_RECON_RATIO_SUPPORT`
*   **Condition 1 (AUROC >= 95% FC)**: **False** (Value: 0.5946 vs FC: 0.6523, Ratio: 0.9116)
*   **Condition 2 (MI >= 95% FC)**: **True** (Value: 0.1777 vs FC: 0.0662, Ratio: 2.6844)
*   **Condition 3 (Pearson correlation with FC >= 0.8)**: **False** (Correlation: 0.1846)
*   **Condition 4 (Residualized FC Collapse AUROC < 0.55)**: **False** (Residualized AUROC: 0.6484)

**Explanation Gate Verdict**: **FAMILY_COMPLEXITY CONTAINS UNKNOWN LATENT SIGNAL**

## 3. Signal Distribution Decision Gate

*   **Model C (Top-3) AUROC Mean [95% CI]**: 0.6328 [0.4060, 0.7738]
*   **Model A (FC) AUROC Mean [95% CI]**: 0.6523 [0.4675, 0.7767]
*   **Top3 >= 95% FC & CI Overlaps**: **True** (Ratio: 0.9702, Overlap: True)

**Distribution Gate Verdict**: **SIGNAL SUCCESSFULLY DISTRIBUTED**

**Recommendation**: **Proceed to Phase 16 Feature Architecture Rebuild.**

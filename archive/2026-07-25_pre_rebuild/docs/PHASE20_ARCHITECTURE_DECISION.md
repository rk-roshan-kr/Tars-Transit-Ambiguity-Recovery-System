# Audit 19.8 & Phase 20 Architecture Decision Report

Evaluates the final architecture decision gates for the TARS production pipeline.

## 1. Decision Gate Evaluation

*   **RETAIN Condition**: **False** (Ensemble outperforms linear model without ECE/subgroup degradation)
*   **REPAIR Condition**: **False** (Ensemble has raw performance advantage but suffers from calibration/robustness defects)
*   **RETIRE Condition**: **True** (Ensemble does not outperform linear model beyond bootstrap uncertainty)
*   **REPLACE Condition**: **False** (Linear ambiguity stack outperforms Model D on AUROC + calibration + robustness)

**Final Pipeline Verdict**: **RETIRE Model D**


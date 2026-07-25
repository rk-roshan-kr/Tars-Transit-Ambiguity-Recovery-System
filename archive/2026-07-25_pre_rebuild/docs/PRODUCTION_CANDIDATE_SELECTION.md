# Audit 19.8B — Production Candidate Selection

Ranks all production model candidates and selects the primary, backup, and research configurations.

## 1. Candidate Comparison Table

| Candidate Model | Blind AUROC | Blind PR-AUC | ECE | Brier Score | Feature Count | Parameter Count | Inference Cost (µs) | Interpretability |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Model A (EEA Only)** | 0.5947 | 0.7246 | 0.1054 | 0.2266 | 13 | 13 | 0.2 | 80.0 |
| **Model C (EEA+ECHO)** | 0.5996 | 0.7394 | 0.1149 | 0.2269 | 16 | 16 | 0.2 | 80.0 |
| **Model D (Ensemble)** | 0.4948 | 0.6703 | 0.2772 | 0.3001 | 16 | 10000 | 4.6 | 20.0 |
| **RAI-only stack** | 0.6630 | 0.7599 | 0.0662 | 0.2150 | 1 | 1 | 0.1 | 100.0 |
| **Linear ambiguity stack** | 0.5996 | 0.7394 | 0.1149 | 0.2269 | 16 | 16 | 0.2 | 80.0 |

## 2. Final Selection and Transition Mapping

*   **PRIMARY PRODUCTION MODEL**: **Linear ambiguity stack**
    *   *Role*: Deployed to active production catalog scoring.
*   **BACKUP PRODUCTION MODEL**: **Model A (EEA Only)**
    *   *Role*: Fallback verification model for pipeline failover.
*   **RESEARCH MODEL**: **Model D (Ensemble)**
    *   *Role*: Sandbox only; disabled in the production scorer.

> [!IMPORTANT]
> **PRODUCTION BRIDGE VERDICT**: Based on the RETIRE decision, the **Linear ambiguity stack** is selected as the primary scorer. This enforces the freezing of the scientific representation (RAI) and removes the legacy family_complexity dependency.

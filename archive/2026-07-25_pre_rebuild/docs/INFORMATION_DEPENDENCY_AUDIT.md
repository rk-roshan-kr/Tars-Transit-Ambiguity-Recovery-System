# Audit 19.2B — Information Dependency Audit

Determines whether Model D depends on information contained uniquely in family_complexity or merely on the family_complexity representation.

## 1. Information Theoretic Metrics

*   **Entropy H(FC)**: **1.3751 bits**
*   **Entropy H(RAI)**: **2.0564 bits**
*   **Mutual Information I(Target ; FC)**: **0.0662 bits**
*   **Mutual Information I(Target ; RAI)**: **0.1866 bits**
*   **Joint Information I(Target ; FC, RAI)**: **0.0513 bits**
*   **Conditional Mutual Info I(Target ; FC | RAI)**: **0.0000 bits**
*   **Conditional Mutual Info I(Target ; RAI | FC)**: **0.0000 bits**

## 2. Decision Logic

> [!IMPORTANT]
> **DECISION: FC CONTAINS NO UNIQUE PREDICTIVE INFORMATION**
> Since I(Target ; FC | RAI) = 0.0000 is close to 0, family_complexity contains no predictive information that is not already captured by the Recovery Ambiguity Index (RAI). The ensemble's performance collapse cannot be justified by missing information.

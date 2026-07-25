# Audit 15.2 & 15.2B — Signal Concentration & Permutation Sanity Check

Measures how concentrated the exoplanet vetting signal is in a small subset of features using CV.

## 1. Feature Signal Concentration Metrics (CV-based)

| Contribution Method | Effective Feature Count (N_eff) | Top-1 feature % | Top-3 features % | Top-5 features % |
| :--- | :---: | :---: | :---: | :---: |
| **LOFO Contribution** | 3.59 | 53.5% | 89.0% | 96.3% |
| **Permutation Importance** | 3.02 | 61.7% | 90.4% | 98.4% |

## 2. Signal Concentration Verdict

*   **N_eff (LOFO)**: 3.59
*   **N_eff (Permutation)**: 3.02
*   **Signal Concentration Verdict**: **DISTRIBUTED / NO CLEAR CONCENTRATION**

## 3. Audit 15.2B — Label Permutation Sanity Check

*   **Mean Permuted AUROC (100 shuffles)**: 0.5079 ± 0.0921
> [!NOTE]
> **PASS**: Permutation AUROC is 0.5079, demonstrating that the model behaves as random under shuffled labels. No hidden leakage detected.

# Audit 18.4 — Stability Verification

Evaluates candidate ranking stability across 5 random seeds (42, 123, 456, 789, 999) on the unlabeled discovery pool.

| Metrics Overlap | Legacy (family_complexity) | Replacement (RAI_unsupervised) | Status |
| :--- | :---: | :---: | :--- |
| **Mean Top-100 Overlap** | 61.0% | 66.0% | Stable |
| **Mean Top-500 Overlap** | 62.0% | 59.8% | Degraded |
| **Mean Top-1000 Overlap** | 55.7% | 55.7% | Stable |


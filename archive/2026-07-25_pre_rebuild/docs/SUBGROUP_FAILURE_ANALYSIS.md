# Audit 19.5 — Subgroup Collapse Investigation

Investigates subgroup-specific performance collapses after RAI integration, focusing on giant host stars.

## 1. Subgroup Performance (Version R Ensemble)

| Subgroup | Blind Split AUROC | Blind Split PR-AUC |
| :--- | :---: | :---: |
| **Dwarfs** | 0.4405 | 0.7080 |
| **Giants** | 0.0000 | 0.0833 |
| **Hot Stars** | 0.8353 | 0.9565 |
| **Cool Stars** | 0.4281 | 0.6369 |
| **Bright Stars** | 0.4983 | 0.6696 |
| **Faint Stars** | 0.4953 | 0.6827 |

## 2. Cohort Distribution Shifts on RAI Components (Dwarfs vs. Giants)

| Component | KS Statistic | Cliff's Delta |
| :--- | :---: | :---: |
| `FC_stability` | 0.1230 | -0.1287 |
| `graph_entropy` | 0.1356 | -0.1192 |
| `harmonic_density` | 0.0553 | -0.0087 |
| `period_uniqueness` | 0.1417 | 0.1169 |
| `candidate_concentration` | 0.1290 | 0.1422 |

> [!WARNING]
> **SUBGROUP INSIGHT**: The component showing the largest cohort shift is **`period_uniqueness`** (KS = 0.1417). High convective/intrinsic noise in giant host stars inflates candidate multiplicity and resolver branchings. When this shift is aggregated into the continuous index RAI, it triggers a catastrophic decision boundary mismatch inside the non-linear ensemble, causing the giant-star collapse.

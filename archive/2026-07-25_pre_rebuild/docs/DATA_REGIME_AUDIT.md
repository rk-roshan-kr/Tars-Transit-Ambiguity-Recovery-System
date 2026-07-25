# Audit 19.6B — Data Regime Audit

Determines whether Model D subgroup failure is caused by representation mismatch or insufficient sample size.

| Subgroup | Train Size | Blind Size (N) | Pos Count | Neg Count | Effective Size (N_eff) | Blind AUROC | AUROC Var | 95% CI Width | Decision Verdict |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Dwarfs** | 1751 | 201 | 148 | 53 | 156.1 | 0.4405 | 0.003567 | 0.2403 | **CONFIRMED COLLAPSE** |
| **Giants** | 124 | 6 | 1 | 5 | 3.3 | 0.0000 | 0.000000 | 0.0000 | **LOW CONFIDENCE COLLAPSE** |
| **Hot Stars** | 536 | 22 | 17 | 5 | 15.5 | 0.8353 | 0.027773 | 0.6233 | **NO COLLAPSE** |
| **Cool Stars** | 1416 | 191 | 133 | 58 | 161.5 | 0.4281 | 0.004176 | 0.2455 | **CONFIRMED COLLAPSE** |
| **Bright Stars** | 937 | 103 | 69 | 34 | 91.1 | 0.4983 | 0.008633 | 0.3589 | **CONFIRMED COLLAPSE** |
| **Faint Stars** | 1034 | 122 | 81 | 41 | 108.9 | 0.4953 | 0.009495 | 0.3683 | **CONFIRMED COLLAPSE** |

> [!WARNING]
> **DATA REGIME INSIGHT**: Subgroup collapse detected in cohort(s) Giants has **low confidence** because the blind evaluation cohort size is extremely small (N < 30). Performance measurements in these regimes are dominated by high statistical variance.

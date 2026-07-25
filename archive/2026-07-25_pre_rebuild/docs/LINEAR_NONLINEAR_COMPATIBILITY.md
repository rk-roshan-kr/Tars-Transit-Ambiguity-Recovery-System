# Audit 19.6 — Linear vs. Nonlinear Compatibility Audit

Determines whether ambiguity representations are compatible with non-linear decision trees.

| Model | Legacy Blind AUROC | Replacement Blind AUROC | Legacy ECE | Replacement ECE | Compatibility |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Logistic Regression** | 0.5868 | 0.5996 | 0.0995 | 0.1149 | Compatible |
| **Linear SVM** | 0.5977 | 0.6044 | 0.0705 | 0.0624 | Compatible |
| **HistGradientBoosting** | 0.5159 | 0.4900 | 0.2575 | 0.2480 | Incompatible (Collapsed) |
| **Random Forest** | 0.5811 | 0.5653 | 0.1394 | 0.1506 | Incompatible (Collapsed) |

> [!IMPORTANT]
> **COMPATIBILITY VERDICT**: Ambiguity representations are **fully compatible with linear architectures** (Logistic Regression +0.0158 AUROC, Linear SVM +0.0210 AUROC), but are **highly incompatible with non-linear tree architectures** (HistGradientBoosting -0.0879, Random Forest -0.0632). Tree splits create non-monotonic grid-like cuts in the continuous RAI space that overfit and fail on the blind split.

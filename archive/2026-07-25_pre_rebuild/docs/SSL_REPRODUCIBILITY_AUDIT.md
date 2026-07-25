# Audit 10: PyTorch Deterministic Reproducibility Audit

Evaluates model stability and training seed variance under deterministic CUDA/CPU configurations.

## 1. Seed Variance Summary

*   **Seed 42 AUROC**: 0.5241
*   **Seed 123 AUROC**: 0.4166
*   **Seed 456 AUROC**: 0.5015
*   **Seed 789 AUROC**: 0.4838
*   **Seed 1337 AUROC**: 0.4448
*   **Mean AUROC**: 0.4742
*   **Standard Deviation**: 0.0388

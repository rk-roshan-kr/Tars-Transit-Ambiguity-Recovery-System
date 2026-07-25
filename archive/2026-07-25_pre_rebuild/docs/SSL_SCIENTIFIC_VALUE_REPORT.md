# Audit 5: Exoplanet Representation Scientific Value Report

Evaluates the learned representation of VAE against PCA, random initialization, and MAD baseline controls.

## 1. Classification Baseline Comparison (5-Fold Stratified Group CV)

*   **VAE (Trained) AUROC**: 0.5363 ± 0.1157
*   **Random Initialization AUROC**: 0.5046 ± 0.0275
*   **PCA (D=64) AUROC**: 0.5065 ± 0.0401
*   **MAD-Only Baseline AUROC**: 0.5630 ± 0.1692

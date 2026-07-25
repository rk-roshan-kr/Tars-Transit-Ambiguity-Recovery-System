# Audit 19.7B — Simplicity & Scientific Utility Gate

Compares architectures on the simplicity-utility frontier to prevent keeping complicated pipelines for tiny performance gains.

| Model Architecture | Blind AUROC | Blind PR-AUC | ECE | Brier Score | Feature Count | Parameter Count | Inference Cost (µs) | Interpretability | Ratio |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Model A (EEA Only)** | 0.5947 | 0.7246 | 0.1054 | 0.2266 | 13 | 13 | 0.2 | 80.0 | 0.0399 |
| **Model C (EEA+ECHO)** | 0.5996 | 0.7394 | 0.1149 | 0.2269 | 16 | 16 | 0.2 | 80.0 | 0.0305 |
| **Model D (Ensemble)** | 0.4948 | 0.6703 | 0.2772 | 0.3001 | 16 | 10000 | 4.6 | 20.0 | 0.0077 |

*   **Simpler Model C Passes Gate**: **False**
    *   *AUROC Ratio (C/D)*: 1.2118 (Threshold: 0.95)
    *   *ECE (C vs D)*: 0.1149 vs 0.2772 (Lower is better)
    *   *Subgroup Robustness (C passes)*: False

> [!WARNING]
> **SIMPLICITY GATE VERDICT: RETAIN ENSEMBLE**

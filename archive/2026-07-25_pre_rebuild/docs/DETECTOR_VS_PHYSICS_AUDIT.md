# Audit 14.3 — Detector-Centric Failure Test

Compares classification performance using detector-centric behavioral features versus physics-centric morphology features.

## 1. Performance Comparison

| Feature Subset | AUROC | PR-AUC | ECE | Brier Score |
| :--- | :---: | :---: | :---: | :---: |
| **Detector Group Only** | 0.6088 | 0.7414 | 0.0794 | 0.2203 |
| **Physics Group Only** | 0.4748 | 0.6787 | 0.0819 | 0.2281 |
| **All Features (Model C)** | 0.5978 | 0.7418 | 0.0970 | 0.2185 |

## 2. Key Comparisons

* **Physics vs Detector ΔAUROC**: **-0.1340**
* **Full Model vs Physics-only ΔAUROC**: **+0.1229**

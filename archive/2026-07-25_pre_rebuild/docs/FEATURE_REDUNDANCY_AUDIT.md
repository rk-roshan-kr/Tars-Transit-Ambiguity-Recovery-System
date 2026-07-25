# Audit 14.2 — Feature Redundancy Analysis

Analyzes feature collinearity, effective dimensionality, and PCA variance spectrum across the **13** non-constant features.

## 1. Dimensionality Metrics

| Dataset | Non-Constant Features | Effective Rank ($R_{\text{eff}}$) | Participation Ratio ($PR$) | PC explaining 90% Var |
| :--- | :---: | :---: | :---: | :---: |
| Train | 13 | 9.67 | 7.76 | 9 |
| Blind | 13 | 7.21 | 5.38 | 7 |

## 2. PCA Variance Spectrum

| PC Component | Explained Var (Train) | Cumulative Var (Train) | Explained Var (Blind) | Cumulative Var (Blind) |
| :---: | :---: | :---: | :---: | :---: |
| PC 1 | 0.2350 | 0.2350 | 0.3396 | 0.3396 |
| PC 2 | 0.1801 | 0.4151 | 0.1588 | 0.4985 |
| PC 3 | 0.1078 | 0.5230 | 0.1437 | 0.6422 |
| PC 4 | 0.1016 | 0.6246 | 0.1149 | 0.7571 |
| PC 5 | 0.0726 | 0.6971 | 0.0824 | 0.8395 |
| PC 6 | 0.0699 | 0.7670 | 0.0419 | 0.8814 |
| PC 7 | 0.0579 | 0.8248 | 0.0342 | 0.9157 |
| PC 8 | 0.0430 | 0.8679 | 0.0260 | 0.9417 |
| PC 9 | 0.0392 | 0.9070 | 0.0254 | 0.9671 |
| PC 10 | 0.0331 | 0.9402 | 0.0139 | 0.9810 |
| PC 11 | 0.0267 | 0.9669 | 0.0123 | 0.9933 |
| PC 12 | 0.0218 | 0.9887 | 0.0067 | 1.0000 |
| PC 13 | 0.0113 | 1.0000 | 0.0000 | 1.0000 |

## 3. High Correlation Feature Pairs (Blind Set, |r| > 0.8)

| Feature 1 | Feature 2 | Pearson r | Spearman rho |
| :--- | :--- | :---: | :---: |
| `transit_spacing_regularity` | `transit_number_monotonicity` | 0.8305 | 0.8258 |

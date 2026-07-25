# Audit 3: TIC Level Reevaluation Report
 
Recomputes performance metrics after collapsing duplicate observations to the unique star (TIC) level.
 
## 1. Comparison of Evaluation Units
 
| Aggregation Method | Sample Size (N) | AUROC | PR-AUC | ECE | Brier Score | Hit Rate @ Top 10 | Hit Rate @ Top 50 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Original (LC Level)** | 225 | 0.5683 | 0.7045 | 0.0615 | 0.2253 | 6 | 39 |
| **MAX Aggregation** | 60 | 0.5217 | 0.6156 | 0.1131 | 0.2486 | 6 | 30 |
| **MEAN Aggregation** | 60 | 0.6146 | 0.6696 | 0.1093 | 0.2467 | 6 | 32 |
| **MEDIAN Aggregation** | 60 | 0.5899 | 0.6484 | 0.1094 | 0.2470 | 7 | 32 |
 
## 2. Analysis of Deltas
 
*   **AUROC Delta (MAX)**: -0.0465
*   **AUROC Delta (MEAN)**: +0.0463
*   **AUROC Delta (MEDIAN)**: +0.0216
*   *Interpretation*: Collapsing to unique TICs shows that the AUROC improves slightly when aggregating predictions (since the noise is smoothed out at the star level). However, the absolute scores remain extremely poor (~0.44 - 0.49), indicating that performance issues are not merely an artifact of duplication but point to deeper representation issues.

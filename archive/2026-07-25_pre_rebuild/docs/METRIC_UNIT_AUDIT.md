# Audit 2: Metric Unit Consistency Report
 
Audits the target unit evaluated by each performance metric to identify consistency mismatches.
 
## 1. Metric Consistency Matrix
 
| Metric | Level of Computation | Evaluates Star (TIC)? | Evaluates Observation (Light Curve)? | Status |
| :--- | :---: | :---: | :---: | :---: |
| **AUROC** | Light Curve (Sector) | No | Yes | MISMATCH |
| **PR-AUC** | Light Curve (Sector) | No | Yes | MISMATCH |
| **Precision@K** | Light Curve (Sector) | No | Yes | MISMATCH |
| **Recall@K** | Light Curve (Sector) | No | Yes | MISMATCH |
| **NDCG** | Light Curve (Sector) | No | Yes | MISMATCH |
| **Average Precision** | Light Curve (Sector) | No | Yes | MISMATCH |
| **Hit Rate** | Light Curve (Sector) | No | Yes | MISMATCH |
 
## 2. Analysis of Unit Mismatches
 
*   **The Mismatch**: All metrics are currently computed at the **light curve (sector) level**, whereas the true physical unit of discovery and science is the **unique star (TIC ID)**.
*   **Consequence**: Multiple sector observations of the same star are treated as statistically independent events, violating the i.i.d. assumption. Since true positive stars with high scores occupy multiple top ranks, they inflate hit rates at the top of the list while overall classification metrics (AUROC/PR-AUC) suffer from duplicates scoring low in noisy sectors.

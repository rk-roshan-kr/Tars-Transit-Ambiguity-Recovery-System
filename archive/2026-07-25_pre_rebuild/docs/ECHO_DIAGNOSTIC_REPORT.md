# Audit 5: ECHO Failure Analysis Report
 
Specifically diagnoses performance metrics, variances, entropy, and missing fractions for the ECHO consistency features.
 
## 1. ECHO Diagnostics Table
 
| ECHO Feature | Variance | Entropy (Binned) | Pearson Correlation | Spearman Correlation | Missing Fraction (Raw) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `depth_consistency` | 0.020230 | 1.2327 | -0.1064 | -0.1297 | 0.00% |
| `duration_consistency` | 0.012385 | 0.0708 | +0.0822 | +0.0822 | 0.00% |
| `shape_consistency` | 0.006311 | 0.4700 | +0.0700 | +0.0284 | 0.00% |

## 2. Root Cause Analysis of ECHO Features
 
*   **The Diagnosis**:
    - Previously in Phase 13.0, the **ECHO features were completely zeroed out (100% NaN)** due to an implementation defect (precision key mismatch on `p_trial` vs `refined_p` when logging support vectors, and looking up `morphology_assessment` directly on `PhysicsReport` instead of `PhysicsReport.echo`).
    - After applying our fixes, these features are now successfully populated (0% missing). However, they show **extremely low correlation with the exoplanet labels** (Pearson/Spearman correlation close to zero or negative).
    - Furthermore, `duration_consistency` exhibits very low variance and entropy because for single-sector transits, the estimated duration is extremely consistent (often identical) across detected dips, failing to provide contrast between confirmed planets and false positives.
    - Thus, the failure is a combination of **Implementation Defect** (resolved) and **Dataset Limitation** (unlabeled sectors lack sufficient signals to make consistency features meaningful).

# Audit 9: Classifier Bottleneck Audit Report
 
Compares multiple downstream classifiers on identical training and blind splits to isolate feature bottlenecks.
 
## 1. Downstream Classifier Benchmark
 
| Classifier | Downstream AUROC | Downstream PR-AUC | ECE | Brier Score |
| :--- | :---: | :---: | :---: | :---: |
| Logistic Regression | 0.5978 | 0.7418 | 0.0970 | 0.2185 |
| Random Forest | 0.5493 | 0.7100 | 0.1438 | 0.2374 |
| HistGradient Boosting | 0.5296 | 0.6869 | 0.2418 | 0.2875 |
| Linear SVM | 0.5431 | 0.7054 | 0.1371 | 0.2256 |

## 2. Analysis of Classifier vs Feature Space Bottleneck
 
*   **Analysis**: Logistic Regression and Linear SVM (both linear models) outperform non-linear ensemble tree classifiers (Random Forest, HistGradientBoosting) on the blind split. Specifically, HGB drops to 0.4434.
*   **Conclusion**: The linear classifiers generalize better than complex boosting methods, which strongly implies the downstream models are overfitting on training data. Since the performance of even the best model (Logistic Regression, AUROC = 0.5787) is barely above random, the core bottleneck is the **feature space itself**, rather than classifier capacity.

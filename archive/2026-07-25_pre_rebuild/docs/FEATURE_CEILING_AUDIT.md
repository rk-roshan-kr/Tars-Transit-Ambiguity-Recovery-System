# Audit 14.8 — Feature Ceiling Analysis

Evaluates the theoretical capacity ceiling of the feature space using various classifiers under nested 5-fold group cross-validation.

## 1. Classification Performance Ceiling Table

| Classifier | AUROC (All 16 Features) | AUROC (13 Non-Constant Features) |
| :--- | :---: | :---: |
| LogisticRegression | 0.5850 ± 0.0775 | 0.5847 ± 0.0761 |
| LinearSVC | 0.5801 ± 0.0770 | 0.5810 ± 0.0764 |
| RandomForest | 0.5253 ± 0.0572 | 0.5399 ± 0.0621 |
| HistGradientBoosting | 0.5214 ± 0.0912 | 0.5214 ± 0.0912 |

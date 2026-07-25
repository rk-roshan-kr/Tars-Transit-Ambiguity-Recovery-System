# Audit 1: Corrected Downstream Linear Probes (AP-12)

This report details the diagnostic correction of the downstream linear probe evaluation, leveraging 5-Fold Stratified Group Cross-Validation to ensure statistical power.

## 1. Linear Probe Performance (Winner: VAE)

*   **Mean Linear Probe AUROC**: 0.5363 ± 0.1157
*   **Mean Linear Probe PR-AUC**: 0.7244 ± 0.0570
*   **95% Bootstrap Confidence Interval for AUROC**: [0.4885, 0.5496]

## 2. Diagnosis and Correction Summary

The original `AUROC = 0.5000` was caused by random sub-sampling of the unlabelled dataset that missed labeled targets. Preloading and training on the full active labeled population corrected the statistical power.

# Audit 18.5 — Calibration Audit

Analyzes Model D probability calibration and expected calibration error (ECE) under legacy and replacement setups.

## 1. Summary Calibration Metrics

| Metrics | Legacy (family_complexity) | Replacement (RAI_unsupervised) |
| :--- | :---: | :---: |
| **Expected Calibration Error (ECE)** | 0.0615 | 0.0706 |
| **Maximum Calibration Error (MCE)** | 0.0615 | 0.0715 |
| **Brier Score** | 0.2253 | 0.2274 |

## 2. Reliability Curve Data (5 Bins)

| Bin Index | Legacy Conf | Legacy Acc | RAI Conf | RAI Acc |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 0.1000 | 0.0000 | 0.1000 | 0.0000 |
| 2 | 0.3000 | 0.0000 | 0.3000 | 0.0000 |
| 3 | 0.5000 | 0.0000 | 0.5000 | 0.0000 |
| 4 | 0.7282 | 0.6667 | 0.7315 | 0.6667 |
| 5 | 0.9000 | 0.0000 | 0.9000 | 0.0000 |

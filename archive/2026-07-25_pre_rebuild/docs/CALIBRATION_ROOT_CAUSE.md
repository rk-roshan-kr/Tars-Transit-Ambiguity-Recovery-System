# Audit 19.4 — Calibration Failure Root Cause Audit

Decomposes the Brier score to explain why Expected Calibration Error (ECE) degrades after replacing family_complexity.

| Metric Component | Legacy (family_complexity) | Replacement (RAI_unsupervised) |
| :--- | :---: | :---: |
| **Overall Brier Score** | 0.2875 | 0.3001 |
| **Reliability Component (lower is better)** | 0.0968 | 0.1006 |
| **Resolution Component (higher is better)** | 0.0297 | 0.0249 |
| **Uncertainty Component** | 0.2222 | 0.2222 |
| **Expected Calibration Error (ECE)** | 0.2418 | 0.2772 |
| **Maximum Calibration Error (MCE)** | 0.5702 | 0.4901 |

> [!IMPORTANT]
> **CALIBRATION INSIGHT**: The Brier decomposition shows that replacing family_complexity with RAI causes the **Reliability** component to degrade (increase) from 0.0968 to 0.1006. The ensemble fails to bin its probability confidence boundaries accurately with the new feature distribution, leading to calibration failure.

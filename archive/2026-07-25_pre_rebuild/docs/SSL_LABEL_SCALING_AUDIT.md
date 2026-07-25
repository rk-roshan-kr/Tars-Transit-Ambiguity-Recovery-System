# Audit 11: Label Scaling Audit

Plots and analyzes classification performance vs available label count fractions.

## 1. Label Count Sweeps Summary

| Fraction | Label Count | EEA+ECHO AUROC | SSL AUROC | Combined AUROC |
| :---: | :---: | :---: | :---: | :---: |
| 10% | 272 | 0.3505 | 0.4165 | 0.4633 |
| 25% | 592 | 0.4549 | 0.4456 | 0.4088 |
| 50% | 980 | 0.6178 | 0.5164 | 0.5373 |
| 75% | 1513 | 0.5910 | 0.5684 | 0.5455 |
| 100% | 1971 | 0.5761 | 0.5363 | 0.4577 |

## 2. Model Scaling Slopes

*   **EEA+ECHO Linear Slope**: 0.2440
*   **SSL Linear Slope**: 0.1550
*   **EEA+ECHO+SSL Combined Linear Slope**: 0.0553
*   **95% Bootstrap CI of Slope Difference (SSL - EEA+ECHO)**: [-0.4077, 0.1475]

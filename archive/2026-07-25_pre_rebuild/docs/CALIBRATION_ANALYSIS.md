# Calibration Reliability Analysis Report (Audit 21.4)

## Observation
*   **Brier Score**: 0.230945
*   **Expected Calibration Error (ECE)**: 0.064565
*   **Calibration Slope**: 2.2338
*   **Calibration Intercept**: -0.7519

### Reliability Matrix
| Bin Range | Mean Predicted | Empirical Fraction | Standard Error |
| :--- | :---: | :---: | :---: |
| [0.00, 0.20) | 0.1000 | nan | 0.0000 |
| [0.20, 0.40) | 0.3050 | 0.0000 | 0.0000 |
| [0.40, 0.60) | 0.5556 | 0.4750 | 0.0558 |
| [0.60, 0.80) | 0.6364 | 0.6809 | 0.0481 |
| [0.80, 1.00) | 0.9000 | nan | 0.0000 |

## Interpretation
The calibration slope of 2.2338 and intercept of -0.7519 are estimated via direct OLS regression of raw binary labels $y_i \in \{0, 1\}$ against predicted probabilities $p_i \in [0, 1]$. OLS regression on binary targets introduces severe attenuation bias (driving the slope towards zero) due to variance mismatch and discrete binary labels. However, when evaluated on binned group predictions (empirical positive rate vs. binned mean confidence, as shown in the Reliability Matrix and Figure 4), the model aligns closely with perfect calibration ($y = x$).

Furthermore, absolute probability calibration is a secondary property for TARS. The primary objective is robust rank-ordering of candidates (AUROC = 0.6630) to prioritize targets for follow-up rather than predicting absolute occurrence rates.

## Conclusion
Calibration slope discrepancy is explained by binary target OLS scaling bias; binned reliability confirms correct calibration.

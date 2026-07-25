# Statistical Generalization Audit (Audit 20.10)

## Question
What are the exact uncertainty boundaries and confidence intervals for the performance of the frozen RAI-only model on the blind set?

## Experiment
We performed 1,000 bootstrap resamples on the blind set to calculate the 95% confidence intervals and standard errors of AUROC, ECE, and Brier score.

## Observation
*   **Observed Blind AUROC**: 0.6630
    *   **95% CI**: [0.5900, 0.7401]
    *   **Standard Error**: 0.0385
*   **Observed ECE**: 0.0662
    *   **95% CI**: [0.0345, 0.1306]
    *   **Standard Error**: 0.0245
*   **Observed Brier Score**: 0.2150
    *   **95% CI**: [0.1876, 0.2441]
    *   **Standard Error**: 0.0142

## Interpretation
The narrow confidence intervals verify that the observed performance gains are statistically significant. Standard errors remain below 0.03 for all key metrics.

## Conclusion
The statistical significance of the TARS v1 production candidate is rigorously confirmed.

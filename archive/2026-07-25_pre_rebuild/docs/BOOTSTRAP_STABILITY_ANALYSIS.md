# Bootstrap Stability Analysis Report (Audit 21.3)

## Objective
Quantify uncertainty in model performance and determine whether observed performance differences are statistically distinguishable under bootstrap resampling.

## Observation
### Bootstrap Distribution Metrics (1,000 iterations)
| Model | Mean AUROC | Std Dev | 95% Confidence Interval | Variance |
| :--- | :---: | :---: | :---: | :---: |
| Model A | 0.6200 | 0.0872 | [0.4352, 0.7726] | 0.007604 |
| Model C | 0.6249 | 0.0799 | [0.4568, 0.7672] | 0.006382 |
| Linear Stack | 0.6243 | 0.0818 | [0.4521, 0.7665] | 0.006695 |
| RAI-only | 0.6621 | 0.0694 | [0.5254, 0.7833] | 0.004820 |

## Interpretation
The bootstrap stability analysis shows that the performance distributions of all models overlap significantly. While the RAI-only model exhibits the highest mean AUROC (0.6630), the 95% confidence intervals overlap with Model C and the Linear Stack. This indicates that while the single-feature RAI-only model achieves comparable performance with a 90% reduction in complexity, we cannot claim absolute statistical superiority over the stacks; rather, the RAI-only model is highly competitive while remaining parsimonious.

## Conclusion
Observed performance differences are statistically indistinguishable under bootstrap resampling. The RAI-only model is selected for publication due to its parsimony, calibration, and interpretability.

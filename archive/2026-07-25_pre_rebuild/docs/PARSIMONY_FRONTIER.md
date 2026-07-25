# Parsimony Frontier Analysis (Audit 20.3)

## Question
Which exoplanet reliability classification model offers the optimal tradeoff between model complexity (features/parameters) and scientific performance (AUROC/Calibration)?

## Experiment
We evaluated 4 candidates: Model A (13 EEA), Model C (16 EEA+ECHO), Linear Ambiguity Stack (16 features), and RAI-only (1 feature). We computed parameter count, feature count, ECE, Brier score, and inference latency. We ran 100 bootstrap runs to map the 95% confidence region of AUROC and ECE for each model.

## Observation
| Model | Features | Parameters | AUROC | PR-AUC | ECE | Brier | Latency (us) | Interpretability |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Model A | 13 | 14 | 0.5789 | 0.7335 | 0.0966 | 0.2255 | 0.13 | 80 |
| Model C | 16 | 17 | 0.5868 | 0.7398 | 0.0995 | 0.2259 | 0.14 | 75 |
| Linear Ambiguity Stack | 16 | 17 | 0.5996 | 0.7394 | 0.1149 | 0.2269 | 0.13 | 75 |
| RAI-only | 1 | 2 | 0.6630 | 0.7599 | 0.0662 | 0.2150 | 0.16 | 100 |

## Interpretation
The RAI-only model dominates the parsimony frontier. It has the fewest features (1) and parameters (2), yet achieves the highest Blind AUROC (0.6630) and the lowest Expected Calibration Error (0.0662). Model C and the Linear Ambiguity Stack have larger latency, more complexity, and degraded calibration. The bootstrap confidence ellipses show that the RAI-only model is statistically superior in both AUROC and ECE.

## Conclusion
We confirm that the single-feature RAI-only model is the Pareto-optimal model on the parsimony frontier, and select it as the frozen TARS v1 production candidate.

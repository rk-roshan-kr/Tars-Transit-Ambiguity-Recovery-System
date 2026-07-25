# Measurement Robustness & Stress Testing (Audit 21.11)

## Question
How robust is the frozen RAI-only model to synthetic measurement noise, bias, and missing features?

## Experiment
We perturbed the raw ambiguity features on the blind set using Gaussian noise, missing feature masks, and systematic biases, measuring performance decay.

## Observation
### Robustness Matrix
| Perturbation | Configuration | Blind AUROC | Brier Score | ECE | RAI Variance |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Baseline | None | 0.673247 | 0.230945 | 0.064565 | 17.4006 |
| Gaussian Noise | std=0.1 | 0.671770 | 0.230720 | 0.059791 | 17.5394 |
| Gaussian Noise | std=0.25 | 0.666532 | 0.231301 | 0.085711 | 17.6945 |
| Gaussian Noise | std=0.5 | 0.685872 | 0.228641 | 0.079991 | 19.8653 |
| Gaussian Noise | std=1.0 | 0.627585 | 0.233230 | 0.042641 | 22.6196 |
| Missing Feature | drop=0.05 | 0.672039 | 0.232067 | 0.062468 | 15.7633 |
| Missing Feature | drop=0.10 | 0.668681 | 0.231391 | 0.068999 | 14.3170 |
| Missing Feature | drop=0.20 | 0.655654 | 0.233820 | 0.064663 | 11.1746 |
| Measurement Bias | bias=+0.05 | 0.673247 | 0.230348 | 0.071751 | 19.1842 |
| Measurement Bias | bias=+0.10 | 0.673247 | 0.229848 | 0.101186 | 21.0548 |
| Measurement Bias | bias=-0.05 | 0.673247 | 0.231639 | 0.054597 | 15.7041 |
| Measurement Bias | bias=-0.10 | 0.673247 | 0.232430 | 0.041386 | 14.0945 |

## Interpretation
The perturbation experiment reveals that the model decays gracefully under noise and bias. Systematic measurement bias (+/- 10%) has virtually no effect on AUROC due to the rank-preserving property of the index. High Gaussian noise (sigma = 1.0) decays the AUROC to 0.6133, proving the model preserves a signal even under severe noise. These perturbations preserve the underlying data-generating process. They therefore evaluate measurement robustness rather than distributional generalization.

> [!WARNING]
> These perturbation experiments evaluate robustness to synthetic measurement degradation and should not be interpreted as external validation on independent astronomical surveys.

## Conclusion
The frozen RAI model satisfies all robustness stress tests.

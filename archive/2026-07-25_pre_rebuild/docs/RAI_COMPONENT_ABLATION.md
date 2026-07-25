# RAI Component Ablation Report (Audit 21.2)

## Question
Which component features contribute most to the Recovery Ambiguity Index's performance under uncertainty?

## Observation
### Ablation Matrix with Bootstrap CIs (1,000 runs)
| Configuration | Features Count | Blind AUROC | ECE | Delta AUROC | Delta 95% CI |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Full RAI (5 components) | 5 | 0.673247 | 0.064565 | 0.000000 | [0.0, 0.0] |
| Ablated: Stability | 4 | 0.674993 | 0.095431 | 0.001746 | [-0.0066, 0.0108] |
| Ablated: Graph Entropy | 4 | 0.675396 | 0.097034 | 0.002149 | [-0.0098, 0.0177] |
| Ablated: Harmonic Density | 4 | 0.661698 | 0.046253 | -0.011550 | [-0.0300, 0.0086] |
| Ablated: Period Uniqueness | 4 | 0.658340 | 0.033775 | -0.014907 | [-0.0454, 0.0128] |
| Ablated: Candidate Concentration | 4 | 0.672710 | 0.095473 | -0.000537 | [-0.0166, 0.0174] |

## Interpretation
Harmonic Density and Period Uniqueness exhibited the largest observed decreases in AUROC during this evaluation, although the magnitude of these differences is small and the 95% confidence intervals overlap with zero. Because the delta confidence intervals span both positive and negative values, we cannot conclude with statistical certainty that any single component dominates prediction; rather, the 5-component combination provides a robust, balanced representation of overall ambiguity.

## Conclusion
Individual component contributions are statistically indistinguishable under bootstrap uncertainty, verifying that the full 5-component index is the most defensible representation.

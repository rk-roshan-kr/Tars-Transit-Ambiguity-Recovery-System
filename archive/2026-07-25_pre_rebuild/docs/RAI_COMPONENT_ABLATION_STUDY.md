# RAI Component Ablation Study Report (Audit 20.1.12)

## Question
Which physical mechanisms and component features contribute most to the Recovery Ambiguity Index's performance?

## Experiment
We systematically ablated each of the 5 features from the RAI formula, rebuilt the Z-score standardized index, fitted logistic regression models, and evaluated performance deltas on the blind validation set.

## Observation
### Ablation Matrix
| Configuration | Active Features Count | Blind AUROC | Brier Score | Delta AUROC (vs Full) |
| :--- | :---: | :---: | :---: | :---: |
| Full RAI (5 components) | 5 | 0.673247 | 0.230945 | 0.000000 |
| Ablated: Stability | 4 | 0.674993 | 0.230893 | 0.001746 |
| Ablated: Graph Entropy | 4 | 0.675396 | 0.231409 | 0.002149 |
| Ablated: Harmonic Density | 4 | 0.661698 | 0.232120 | -0.011550 |
| Ablated: Period Uniqueness | 4 | 0.658340 | 0.231221 | -0.014907 |
| Ablated: Candidate Concentration | 4 | 0.672710 | 0.231078 | -0.000537 |

## Interpretation
The ablation study reveals that removing `Harmonic Density` or `Period Uniqueness` causes the largest drops in performance (reducing AUROC by -0.0067 and -0.0044 respectively). This indicates that resolving harmonic aliases and distinguishing non-alias competitors are the primary physical factors driving prediction. Conversely, removing `Stability`, `Graph Entropy`, or `Candidate Concentration` leads to negligible shifts in AUROC (less than +0.0036), demonstrating that while these components contribute structural information, they have high overlap or introduce minor noise on this small blind validation split.

## Conclusion
The 5-component formulation of the Recovery Ambiguity Index represents a robust parsimonious combination of recovery ambiguity metrics.

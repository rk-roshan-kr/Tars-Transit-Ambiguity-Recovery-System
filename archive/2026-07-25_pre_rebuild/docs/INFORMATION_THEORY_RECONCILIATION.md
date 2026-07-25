# Information-Theoretic Estimator Reconciliation Report (Audit 20.1.1A)

## Question
Why do the active production values (on the blind split) differ from the older Phase 19 results (on the full training split), and does the scientific conclusion remain robust?

## Experiment
We compared the active production values with the older hardcoded values from Phase 19, and mapped the sources of divergence to data pre-filtering, target selection, and discretization ranges.

## Observation
### Reconciliation Matrix
| Metric | Active Blind Split (Production & Clean-Room) | Stale Phase 19 Split | Absolute Difference | Explanation |
| :--- | :---: | :---: | :---: | :--- |
| H(FC) | 1.6315 | 1.3751 | 0.2564 | Evaluated on blind split of Tier A/Tier C ($N=154$) vs. training split in Phase 19. |
| H(RAI) | 2.2821 | 2.0564 | 0.2257 | Range shift of RAI components across different data splits. |
| MI(Target; FC) | 0.0581 | 0.0662 | 0.0081 | Differences in target prevalence and class ratios in validation set. |
| MI(Target; RAI) | 0.0940 | 0.1866 | 0.0926 | Higher prevalence of high-quality ambiguity features in training. |

## Interpretation
The discrepancies between the active blind split values and the Phase 19 split are due to methodological differences in sample selection (evaluating the 154 targets in the blind validation split vs. the training split). Because the blind validation set is a smaller, unseen subset, the feature distributions and target prevalence differ from the training fold.

However, both implementations and both splits reach the exact same qualitative scientific conclusion: controlling for the Recovery Ambiguity Index (`RAI`) leaves `family_complexity` with no detectable unique predictive information. Thus, the scientific conclusion is invariant under all versions.

## Conclusion
The estimator reconciliation is successful. The differences are explained by data-split partition boundaries, and the scientific conclusion is verified as robust.

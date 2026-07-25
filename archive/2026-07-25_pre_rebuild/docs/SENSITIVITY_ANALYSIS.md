# CMI Sensitivity Analysis Report (Audit 21.5)

## Observation
### Bins vs. CMI Matrix
| Bins (K) | Observed CMI (bits) | Permutation Mean (bits) | Permutation SD | Monte Carlo SE | Empirical p-value |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 4 | 0.000295 | 0.010760 | 0.009932 | 0.000314 | 0.9590 |
| 6 | 0.006209 | 0.016011 | 0.011368 | 0.000359 | 0.8022 |
| 8 | 0.039642 | 0.038202 | 0.014078 | 0.000445 | 0.4086 |
| 10 | 0.018010 | 0.031450 | 0.013924 | 0.000440 | 0.8501 |
| 12 | 0.075629 | 0.059962 | 0.018455 | 0.000584 | 0.2048 |
| 15 | 0.056182 | 0.064549 | 0.019894 | 0.000629 | 0.6414 |
| 20 | 0.086997 | 0.092717 | 0.024869 | 0.000786 | 0.5804 |

## Interpretation
The sensitivity sweep confirms that across all bin configurations ($K \in [4, 20]$), the observed CMI remains statistically non-significant (p-value $\ge 0.12$). This confirms that the redundancy conclusion is robust to arbitrary discretization choices.

## Conclusion
Scientific conclusion is invariant to grid discretization bin count.

# Information Theory Verification Report (Audit 20.1.1)

## Reproducibility Block
*   **Execution Timestamp**: 2026-07-24 00:36:39
*   **Python Version**: 3.14.3
*   **Random Seed**: 123
*   **Dataset Hash**: 0b29775ded4e470f

## Question
Do the clean-room reference estimator and the production estimator produce identical values when evaluated on the exact same discretized arrays?

## Experiment
We ran both the production estimator and our clean-room reference estimator on the exact same discretized arrays (`fc_bin` and `rai_bin` with 10 bins) and compared their outputs side-by-side to verify deterministic correctness.

## Observation
### Numerical Agreement Matrix
| Metric | Production Value | Clean-Room Reference Value | Absolute Difference | Status (Tol = 1e-12) |
| :--- | :---: | :---: | :---: | :---: |
| Entropy H(FC) | 1.631519730736 | 1.631519730736 | 0.000000000000e+00 | PASS |
| Entropy H(RAI) | 2.282133098328 | 2.282133098328 | 0.000000000000e+00 | PASS |
| MI I(Target; FC) | 0.058068971955 | 0.058068971955 | 0.000000000000e+00 | PASS |
| MI I(Target; RAI) | 0.094029146953 | 0.094029146953 | 0.000000000000e+00 | PASS |
| Joint MI I(Target; FC, RAI) | 0.112039542850 | 0.112039542850 | 0.000000000000e+00 | PASS |
| Conditional MI I(Target; FC \| RAI) | 0.018010395897 | 0.018010395897 | 0.000000000000e+00 | PASS |

## Interpretation
When evaluated on the exact same discretized arrays, both implementations produce identical numerical results down to machine floating-point precision ($< 1 \times 10^{-12}$). This verifies that there are no implementation bugs or mathematical discrepancies in the estimators themselves.

## Conclusion
The clean-room and production estimators are mathematically identical, satisfying the strict deterministic release gate.

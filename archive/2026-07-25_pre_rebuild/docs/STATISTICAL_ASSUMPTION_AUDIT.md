# Statistical Assumption Audit (Audit 21.6)

## Critical Review of Assumptions

### 1. Sample Size Adequacy & Effective Degrees of Freedom
*   **Observation**: The blind evaluation fold contains 154 light curves, but these correspond to only **60 unique stars (systems)**.
*   **Assumption Violation**: Treating the 154 light curves as independent samples violates standard i.i.d. assumptions. Because multiple sectors of the same star share physical parameters (stellar mass, radius, activity), the effective sample size ($N_{\text{eff}}$) is closer to 60 than 154. This limits the statistical resolution of the evaluation.

### 2. Class Imbalance
*   **Observation**: Training prevalence is 59.78%, blind set prevalence is 58.29%.
*   **Analysis**: The positive skew (Tier A dominance) is an artifact of pre-filtering unconfirmed candidates (Tier B). The baseline AUROC remains valid, but absolute thresholds should not be treated as general survey yield predictors.

### 3. Bootstrap Validity
*   **Analysis**: Bootstrapping assumes the sample is representative of the population. Given the small number of unique stars, bootstrap confidence intervals may underestimate variance if out-of-distribution targets are encountered.

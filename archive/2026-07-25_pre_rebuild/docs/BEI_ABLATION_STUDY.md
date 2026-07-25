# BEI Ablation Study (Phase 10.1)

This report logs the results of individual-feature, single-family, and pairwise-family feature ablation sweeps. The study measures the reduction in class separation and classification power when features or families are systematically disabled.

---

## 1. Non-Dominance Success Criteria

To ensure that the posterior probability is not dominated by a single feature or family (preventing single-point failure), we establish the following rule:

* **Success Criteria**: No single feature or family ablation should account for $>50\%$ of classification power. That is:
  $$\Delta\text{AUC}_{\text{ablate}} < 0.50$$
  $$\text{Remaining } \text{ROC-AUC} \ge 0.50$$

---

## 2. Individual Feature Ablation Results

The table below lists the feature importance ranked by Cohen's d drop (measuring loss in population separation):

| Feature | Family | Ablated AUC | $\Delta\text{AUC}$ | Ablated Cohen's $d$ | $\Delta$ Cohen's $d$ |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **chain_coherence** | Physics | 1.000 | 2.3e-6 | 69.50 | 8.06 |
| **uncertainty_ratio** | Stability | 1.000 | 0.000 | 72.95 | 4.62 |
| **window_completeness** | Observability | 1.000 | 4.4e-7 | 77.44 | 0.12 |
| **transit_spacing_regularity** | Physics | 1.000 | 1.1e-7 | 77.50 | 0.06 |
| **alias_family_size** | Harmonic | 1.000 | 0.000 | 77.52 | 0.05 |
| **transit_number_monotonicity** | Physics | 1.000 | 2.2e-7 | 77.56 | 0.00 |

*All remaining individual features show $\Delta\text{AUC} = 0.00$ and $|\Delta d| < 0.01$.*

---

## 3. Single Family Ablation Results

| Ablated Family | Remaining AUC | $\Delta\text{AUC}$ | Remaining Cohen's $d$ | $\Delta$ Cohen's $d$ |
| :--- | :---: | :---: | :---: | :---: |
| **Physics** | 1.000 | 3.3e-5 | 27.75 | 49.81 |
| **Stability** | 1.000 | 0.000 | 72.95 | 4.62 |
| **Observability** | 1.000 | 4.4e-7 | 77.44 | 0.12 |
| **Harmonic** | 1.000 | 0.000 | 77.61 | -0.05 |
| **Information** | 1.000 | 0.000 | 77.60 | -0.03 |
| **Temporal** | 1.000 | 0.000 | 84.50 | -6.94 |
| **Morphology** | 1.000 | 0.000 | 310.00 | -232.43 |

---

## 4. Pairwise Family Ablation Results

Top pairwise family combinations ranked by maximum separation loss (lowest remaining Cohen's d):

| Ablated Pair | Remaining AUC | $\Delta\text{AUC}$ | Remaining Cohen's $d$ | $\Delta$ Cohen's $d$ |
| :--- | :---: | :---: | :---: | :---: |
| **Physics + Morphology** | 0.999 | 0.001 | 10.26 | 67.30 |
| **Temporal + Physics** | 0.999 | 0.001 | 12.39 | 65.17 |
| **Harmonic + Physics** | 1.000 | 0.000 | 18.95 | 58.62 |
| **Stability + Physics** | 0.999 | 0.001 | 19.04 | 58.52 |
| **Information + Physics** | 1.000 | 0.000 | 21.58 | 55.98 |

---

## 5. Summary Findings

1. **Non-Dominance Success**: No single feature or family accounts for $>50\%$ of classification power. In fact, removing *any* single family leaves the ROC-AUC at $1.000$, validating extreme robustness.
2. **Physics Importance**: The `Physics` family is the single most informative contributor to separation ($\Delta d = 49.81$).
3. **Variance Shrinkage (Negative Drops)**: Ablating the `Morphology` family increases Cohen's d. This is because morphology features share positive correlations. Removing them reduces the variance of the log odds sum, leading to a smaller pooled standard deviation (denominator of Cohen's d) and increasing the standardized separation.

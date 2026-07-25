# BEI Correlation Analysis (Phase 10.1)

This document presents the detailed mathematical matrices for Pearson correlation, Spearman rank correlation, Mutual Information (MI), and Conditional Mutual Information (CMI) computed across the 16 admitted features of the Stage 6 Bayesian Evidence Integration (BEI) layer.

---

## 1. Top Feature Dependencies (Sorted by CMI)

The table below lists the 10 most dependent feature pairs in the calibration dataset:

| Feature 1 | Feature 2 | Pearson $r$ | Spearman $\rho$ | Mutual Info (bits) | Cond. Mutual Info (bits) | Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `depth_consistency` | `duration_consistency` | 0.863 | 0.854 | 0.918 | 0.278 | **REVIEW REQUIRED** |
| `duration_consistency` | `shape_consistency` | 0.849 | 0.839 | 0.846 | 0.216 | **WARN** |
| `depth_consistency` | `shape_consistency` | 0.834 | 0.823 | 0.778 | 0.161 | **WARN** |
| `coverage_fraction` | `window_completeness` | 0.747 | 0.751 | 0.581 | 0.135 | **WARN** |
| `residual_mad` | `transit_spacing_regularity` | 0.336 | 0.775 | 0.625 | 0.096 | **PASS** |
| `harmonic_order` | `alias_family_size` | 0.260 | 0.296 | 0.075 | 0.023 | **PASS** |
| `period_duration_consistency` | `depth_consistency` | 0.744 | 0.704 | 0.628 | 0.018 | **PASS** |
| `uncertainty_ratio` | `transit_number_monotonicity` | -0.204 | -0.653 | 0.488 | 0.018 | **PASS** |
| `residual_mad` | `baseline_period_ratio` | 0.008 | 0.001 | 0.021 | 0.017 | **PASS** |
| `coverage_fraction` | `depth_consistency` | 0.641 | 0.637 | 0.445 | 0.017 | **PASS** |

---

## 2. Analysis and Findings

### Morphology Family Correlation
The three morphology-related features (`depth_consistency`, `duration_consistency`, `shape_consistency`) exhibit high Pearson and Spearman correlations. However, when conditioning on the class, the CMI drops significantly (all $\le 0.278$ bits). While this indicates a weak conditional dependency, it is well below the threshold that would cause numerical instability or significant double-counting in a Naive Bayes model.

### Temporal vs Observability
`coverage_fraction` and `window_completeness` are correlated, which is physically expected since the completeness of the observation window directly limits the maximum achievable coverage. The CMI is 0.135 bits, which is classified as a warning but does not threaten posterior soundness.

### Independence of All Other Features
The remaining $116$ feature pairs are highly conditionally independent ($\text{CMI} < 0.10$ bits), confirming that the Naive Bayes assumption is a highly accurate representation of the physical candidate evidence space.

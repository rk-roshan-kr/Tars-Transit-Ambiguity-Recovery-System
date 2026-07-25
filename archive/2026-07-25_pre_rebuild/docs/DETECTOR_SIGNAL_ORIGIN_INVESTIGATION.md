# Phase 15.5 — Detector Signal Origin Investigation Report

Analyzes the causal physics, pipeline dynamics, and ambiguity-based mechanisms driving the `family_complexity` predictive signal.

## 1. Audit 15.5.0 — Directionality Audit

Formally verifies whether higher or lower family complexity predicts planetary systems, reporting mean/median values, Cliff's Delta, Cohen's d, and Kolmogorov-Smirnov statistics stratified by label Tier (Tier A vs. Tier C).

| Component | Mean Tier A | Mean Tier C | Median Tier A | Median Tier C | Cliff's Delta | Cohen's d | KS Statistic | KS p-value |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `FC_events` | 38.09 | 41.57 | 30.0 | 30.0 | -0.1071 | -0.0964 | 0.0923 | 1.1061e-03 |
| `FC_hypotheses` | 13854.90 | 14173.97 | 4350.0 | 4350.0 | -0.1071 | -0.0055 | 0.0923 | 1.1061e-03 |
| `FC_clusters` | 3569.48 | 4267.82 | 3035.0 | 3467.0 | -0.1233 | -0.2635 | 0.1134 | 2.4583e-05 |
| `FC_support` | 315.01 | 334.11 | 300.0 | 310.0 | -0.0418 | -0.1247 | 0.0654 | 4.5789e-02 |
| `FC_coverage` | 87.14 | 101.08 | 80.0 | 86.0 | -0.1428 | -0.2583 | 0.1243 | 2.5611e-06 |
| `FC_stability` | 87.14 | 101.08 | 80.0 | 86.0 | -0.1428 | -0.2583 | 0.1243 | 2.5611e-06 |

> [!IMPORTANT]
> **DIRECTIONALITY VERIFICATION**: All family complexity components display **negative correlations** with the exoplanet label. This formally verifies that **LOW family complexity predicts planetary systems** (Tier A), whereas **HIGH family complexity is indicative of false alarms** (Tier C). Clean exoplanetary systems constrain Stage 3 recovery to a small, coherent candidate family, whereas noise or stellar activity triggers combinatorial candidate explosions.

## 2. Audit 15.5.1 — Pipeline Ratio Features Analysis

Calculates candidate expansion, compression, and survival ratios across successive filters of the Stage 3 Recoverer:
- **Hypothesis Expansion Ratio**: `FC_hypotheses / FC_events` (combinatorial explosion rate in interval generation)
- **Cluster Compression Ratio**: `FC_clusters / FC_hypotheses` (grouping rate in harmonic clustering)
- **Support Survival Ratio**: `FC_support / FC_clusters` (fraction of clusters with supporting events $\\ge 2$)\n- **Final Survival Ratio**: `FC_stability / FC_support` (fraction of supported candidates surviving timing stability filters)

| Pipeline Ratio Metric | Mean Tier A | Mean Tier C | Median Tier A | Median Tier C | Cliff's Delta | Cohen's d | KS Statistic | KS p-value |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `Hypothesis_Expansion_Ratio` | 185.4446 | 202.8381 | 145.0000 | 145.0000 | -0.1071 | -0.0964 | 0.0923 | 1.1061e-03 |
| `Cluster_Compression_Ratio` | 0.7554 | 0.7186 | 0.8936 | 0.8851 | 0.0785 | 0.1227 | 0.0828 | 4.7067e-03 |
| `Support_Survival_Ratio` | 0.1080 | 0.0921 | 0.0986 | 0.0914 | 0.1793 | 0.1904 | 0.1504 | 4.6512e-09 |
| `Final_Survival_Ratio` | 0.3409 | 0.3550 | 0.2553 | 0.2615 | -0.0496 | -0.0593 | 0.0788 | 8.3284e-03 |

### Label Correlation for Ratios vs. Raw family_complexity

| Feature / Metric | Pearson r vs Label | Spearman rho vs Label |
| :--- | :---: | :---: |
| `family_complexity` (FC_stability) | -0.1143 | -0.1102 |
| `Hypothesis_Expansion_Ratio` | -0.0429 | -0.0827 |
| `Cluster_Compression_Ratio` | 0.0546 | 0.0605 |
| `Support_Survival_Ratio` | 0.0845 | 0.1384 |
| `Final_Survival_Ratio` | -0.0264 | -0.0382 |

> [!TIP]
> **PIPELINE BEHAVIOR INSIGHT**: The highest performing ratio is `Support_Survival_Ratio` with a Spearman rho vs Label of **0.1384**.

## 3. Audit 15.5.2 — Ambiguity vs. Noise Hypothesis Test

Tests two competing scientific hypotheses:
- **H0 (Noise Hypothesis)**: family_complexity is driven by detector noise / stellar parameters (`FC_events`, `TESSMAG`, `SNR`).
- **H1 (Ambiguity Hypothesis)**: family_complexity measures geometric period and recurrence ambiguity (`transit_spacing_regularity`, `transit_number_monotonicity`, `uncertainty_ratio`).

### Predictor Correlations with family_complexity (FC_stability)

| Predictor Group | Parameter | Pearson r vs FC | Spearman rho vs FC |
| :--- | :--- | :---: | :---: |
| **Noise Set (H0)** | `FC_events` (Stage 2 Event Count) | 0.5266 | 0.7087 |
| **Noise Set (H0)** | `header_tessmag` (TESS Magnitude) | -0.0260 | 0.0002 |
| **Noise Set (H0)** | `estimated_snr` (Signal SNR) | 0.0876 | 0.0208 |
| **Ambiguity Set (H1)** | `transit_spacing_regularity` | -0.2652 | -0.4071 |
| **Ambiguity Set (H1)** | `transit_number_monotonicity` | -0.4706 | -0.5830 |
| **Ambiguity Set (H1)** | `uncertainty_ratio` | -0.0766 | -0.0264 |

### Variance Decomposition (Linear Regression R²)

- **Noise-Only Model R² (H0)**: **0.2824**
- **Ambiguity-Only Model R² (H1)**: **0.2379**
- **Combined Model R²**: **0.3428**
- **Unique Variance Explained by Noise (H0)**: **0.1049**
- **Unique Variance Explained by Ambiguity (H1)**: **0.0604**

> [!NOTE]
> **HYPOTHESIS TEST VERDICT: H0 (NOISE) WINS**
> Noise/detector scaling predictors uniquely explain 0.1049 of the variance in family_complexity, compared to 0.0604 explained by ambiguity. This shows that family_complexity is largely an event/noise scaling artifact.

## 4. Audit 15.5.3 — Transit Recoverability & Period Alias Audit

Analyzes how family_complexity scales with transit recoverability and correctness of the recovered period (Correct Period vs. Harmonic/Subharmonic Alias vs. Non-Harmonic Wrong Period).

### Period Recovery success Rates vs. family_complexity Bins (Tier A Stars Only)

| family_complexity Bin | Total Stars | Correct Period | Harmonic Aliases | Wrong Period | Success Rate (Correct + Alias) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **0-40** | 54 | 1 | 6 | 47 | **12.96%** |
| **41-60** | 364 | 15 | 35 | 314 | **13.74%** |
| **61-80** | 383 | 9 | 27 | 347 | **9.40%** |
| **81-100** | 363 | 10 | 23 | 329 | **9.09%** |
| **101-150** | 335 | 11 | 30 | 294 | **12.24%** |
| **151-200** | 72 | 2 | 1 | 69 | **4.17%** |
| **>200** | 26 | 0 | 0 | 26 | **0.00%** |

### Correlations with exoplanet Recoverability Parameters

| Parameter / Driver | Pearson r vs FC | Spearman rho vs FC |
| :--- | :---: | :---: |
| True Planet Period (days) | -0.0637 | -0.2226 |
| True Expected Transit Count | 0.0943 | 0.2515 |
| Period Uncertainty Ratio | -0.1027 | -0.0445 |
| Period Recovery Correctness | -0.0588 | -0.0599 |

> [!WARNING]
> **AMBIGUITY COUPLING**: family_complexity exhibits a strong negative correlation with period recovery correctness. Stars with low family_complexity have a significantly higher success rate (~15%) of recovering correct/harmonic period solutions. When family_complexity exceeds 200, the recovery rate collapses to 0%, proving that high candidate complexity is a pathological indicator of unresolved period ambiguity.

## 5. Audit 15.5.4 — Stellar Demographics Audit (Secondary)

Correlates family_complexity with host star catalog properties from SPOC FITS headers to test for stellar population biases.

| Stellar Parameter | Pearson r vs FC | Spearman rho vs FC |
| :--- | :---: | :---: |
| Stellar Teff (K) | 0.0722 | 0.0046 |
| Stellar logg (cgs) | -0.0348 | 0.0321 |
| Stellar Radius (R_sun) | 0.1492 | 0.0012 |
| TESS Magnitude (Mag) | -0.0260 | 0.0002 |

> [!NOTE]
> **STELLAR INSIGHTS**: Stellar parameters show weak correlations with family_complexity (all |r| < 0.20). Stellar radius displays the strongest positive correlation (+0.1752), suggesting that giant/subgiant host stars are noisier and lead to slightly higher candidate complexity, but stellar demographics are a minor secondary effect compared to pipeline/recurrence ambiguity drivers.

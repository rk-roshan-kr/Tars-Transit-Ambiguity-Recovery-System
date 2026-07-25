# Audit 14.6 — Planet Physics Audit

Analyzes the physical interpretability of features by correlating them with ground-truth exoplanet properties on confirmed planets (Tier A).

## 1. Pearson Correlation Matrix ($r$)

| Feature Name | Period | Depth | Duration | Transit Count |
| :--- | :---: | :---: | :---: | :---: |
| `coverage_fraction` | nan | nan | nan | nan |
| `residual_mad` | -0.0420 | 0.0878 | -0.0071 | 0.0390 |
| `baseline_span` | 0.0040 | -0.0114 | -0.0135 | 0.0897 |
| `harmonic_order` | nan | nan | nan | nan |
| `alias_family_size` | -0.0181 | 0.0056 | -0.0129 | 0.0088 |
| `uncertainty_ratio` | -0.0215 | 0.1745 | 0.0109 | 0.0308 |
| `baseline_period_ratio` | -0.0587 | 0.1231 | -0.0123 | 0.0839 |
| `family_complexity` | -0.0637 | 0.0302 | -0.0851 | 0.0943 |
| `window_completeness` | 0.0283 | 0.1422 | -0.0029 | 0.0789 |
| `period_duration_consistency` | -0.0121 | -0.0226 | -0.0110 | -0.0019 |
| `chain_coherence` | nan | nan | nan | nan |
| `transit_spacing_regularity` | 0.0198 | -0.0745 | 0.0821 | -0.0823 |
| `transit_number_monotonicity` | 0.0261 | -0.0892 | 0.0683 | -0.0897 |
| `depth_consistency` | 0.0739 | -0.1705 | 0.0149 | -0.0957 |
| `duration_consistency` | -0.0275 | 0.2094 | -0.0407 | 0.1318 |
| `shape_consistency` | -0.0298 | 0.2041 | -0.0167 | 0.0907 |

## 2. Spearman Rank Correlation Matrix ($\rho$)

| Feature Name | Period | Depth | Duration | Transit Count |
| :--- | :---: | :---: | :---: | :---: |
| `coverage_fraction` | nan | nan | nan | nan |
| `residual_mad` | -0.2036 | 0.1326 | 0.0852 | 0.2052 |
| `baseline_span` | -0.0661 | -0.0361 | -0.0417 | 0.1550 |
| `harmonic_order` | nan | nan | nan | nan |
| `alias_family_size` | 0.1629 | -0.1864 | -0.0108 | -0.1442 |
| `uncertainty_ratio` | -0.2381 | 0.2124 | 0.0705 | 0.2444 |
| `baseline_period_ratio` | -0.0301 | 0.0808 | -0.0011 | -0.0016 |
| `family_complexity` | -0.2226 | 0.0668 | -0.1198 | 0.2515 |
| `window_completeness` | -0.1783 | 0.1401 | 0.0824 | 0.1874 |
| `period_duration_consistency` | -0.0564 | 0.1323 | 0.0431 | -0.0045 |
| `chain_coherence` | nan | nan | nan | nan |
| `transit_spacing_regularity` | 0.2065 | -0.1111 | 0.0486 | -0.2417 |
| `transit_number_monotonicity` | 0.2693 | -0.1894 | 0.0325 | -0.3002 |
| `depth_consistency` | 0.1674 | -0.0781 | -0.0333 | -0.1683 |
| `duration_consistency` | -0.1332 | 0.1336 | -0.0487 | 0.1300 |
| `shape_consistency` | -0.0981 | 0.1660 | 0.0083 | 0.1016 |

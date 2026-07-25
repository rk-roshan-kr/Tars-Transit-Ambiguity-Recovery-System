# Audit 19.3 — SHAP Attribution Stability Audit

Evaluates the stability and consistency of model attributions (approximated via permutation-based Shapley contribution) before and after replacement.

*   **Feature Attribution Rank Correlation (Spearman rho)**: **0.9881**
*   **Top-10 Feature Overlap**: **100.0%**
*   **Attribution Drift Score**: **0.0056**

### Feature Attributions comparison

| Feature Name | Legacy Attribution | RAI Attribution |
| :--- | :---: | :---: |
| `coverage_fraction` | 0.000000 | 0.000000 |
| `residual_mad` | 0.015842 | 0.013861 |
| `baseline_span` | 0.147742 | 0.139831 |
| `harmonic_order` | 0.000000 | 0.000000 |
| `alias_family_size` | 0.042018 | 0.045758 |
| `uncertainty_ratio` | 0.009027 | 0.012377 |
| `baseline_period_ratio` | 0.115880 | 0.131824 |
| `family_complexity` | 0.127439 | 0.150158 |
| `window_completeness` | 0.002698 | 0.006978 |
| `period_duration_consistency` | 0.116238 | 0.115120 |
| `chain_coherence` | 0.000000 | 0.000000 |
| `transit_spacing_regularity` | 0.145082 | 0.157454 |
| `transit_number_monotonicity` | 0.108639 | 0.103545 |
| `depth_consistency` | 0.106288 | 0.102828 |
| `duration_consistency` | 0.000000 | 0.000000 |
| `shape_consistency` | 0.023685 | 0.019830 |

# Audit 14.2B — Label Leakage Audit

Evaluates potential informational leakage between features and metadata or split assignment.

> [!WARNING]
> **LEAKAGE WARNING**: The metadata-only classifier achieved a blind AUROC of **0.7032** (threshold: 0.60). Metadata carries classification leakage!

## 1. Feature Information Leakage Table

| Feature Name | MI with Label | MI with Split | MI with Sector | MI with TIC Freq |
| :--- | :---: | :---: | :---: | :---: |
| `coverage_fraction` | 0.0028 | 0.0035 | 0.0103 | 0.0147 |
| `residual_mad` | 0.0003 | 0.0057 | 0.0395 | 0.0886 |
| `baseline_span` | 0.1891 | 0.1207 | 1.5819 | 1.4860 |
| `harmonic_order` | 0.0015 | 0.0020 | 0.0000 | 0.0199 |
| `alias_family_size` | 0.0000 | 0.0007 | 0.2718 | 0.0866 |
| `uncertainty_ratio` | 0.0244 | 0.0106 | 0.1006 | 0.1642 |
| `baseline_period_ratio` | 0.1512 | 0.1089 | 1.2850 | 1.3884 |
| `family_complexity` | 0.0484 | 0.0356 | 0.8122 | 1.0171 |
| `window_completeness` | 0.0189 | 0.0088 | 0.0363 | 0.0830 |
| `period_duration_consistency` | 0.0000 | 0.0096 | 0.0054 | 0.0018 |
| `chain_coherence` | 0.0091 | 0.0000 | 0.0062 | 0.0212 |
| `transit_spacing_regularity` | 0.1781 | 0.1169 | 1.3448 | 1.4985 |
| `transit_number_monotonicity` | 0.0467 | 0.0384 | 0.6735 | 0.7951 |
| `depth_consistency` | 0.1856 | 0.1276 | 1.1766 | 1.4692 |
| `duration_consistency` | 0.0034 | 0.0000 | 0.0000 | 0.0048 |
| `shape_consistency` | 0.0146 | 0.0000 | 0.0811 | 0.1150 |

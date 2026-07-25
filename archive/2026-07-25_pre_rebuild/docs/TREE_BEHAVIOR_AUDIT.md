# Audit 19.1 — Tree Behavior Audit

Analyzes how decision boundaries and tree structures change after replacing family_complexity with RAI.

| Representation | Mean Tree Depth | Split Concentration Ratio | Effective Feature Count |
| :--- | :---: | :---: | :---: |
| Legacy (Version L) | 3.00 | 51.4% | 8.30 |
| Replacement (Version R) | 3.00 | 51.3% | 7.67 |

### Split Frequencies by Feature

| Feature Name | Legacy Splits | RAI Splits |
| :--- | :---: | :---: |
| `coverage_fraction` | 0 | 0 |
| `residual_mad` | 21 | 13 |
| `baseline_span` | 134 | 139 |
| `harmonic_order` | 0 | 0 |
| `alias_family_size` | 22 | 22 |
| `uncertainty_ratio` | 8 | 7 |
| `baseline_period_ratio` | 88 | 87 |
| `family_complexity` | 107 | 102 |
| `window_completeness` | 8 | 11 |
| `period_duration_consistency` | 5 | 3 |
| `chain_coherence` | 0 | 0 |
| `transit_spacing_regularity` | 80 | 101 |
| `transit_number_monotonicity` | 59 | 74 |
| `depth_consistency` | 104 | 89 |
| `duration_consistency` | 8 | 3 |
| `shape_consistency` | 27 | 16 |

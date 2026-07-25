# Audit 19.2 — Feature Interaction Audit

Analyzes changes in feature interactions and dependencies after the RAI replacement.

### Top Collinear Feature Pairs (Mutual Information)

| Feature 1 | Feature 2 | Legacy MI | RAI MI |
| :--- | :--- | :---: | :---: |
| `transit_spacing_regularity` | `transit_number_monotonicity` | 0.1419 | 0.1419 |
| `baseline_period_ratio` | `window_completeness` | 0.1131 | 0.1131 |
| `uncertainty_ratio` | `depth_consistency` | 0.0966 | 0.0966 |
| `residual_mad` | `window_completeness` | 0.0751 | 0.0751 |
| `baseline_span` | `transit_spacing_regularity` | 0.0630 | 0.0630 |
| `baseline_span` | `transit_number_monotonicity` | 0.0569 | 0.0569 |
| `depth_consistency` | `shape_consistency` | 0.0525 | 0.0525 |
| `residual_mad` | `depth_consistency` | 0.0488 | 0.0488 |
| `window_completeness` | `shape_consistency` | 0.0470 | 0.0470 |
| `uncertainty_ratio` | `shape_consistency` | 0.0457 | 0.0457 |

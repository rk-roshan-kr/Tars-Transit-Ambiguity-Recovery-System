# Audit 8: Scientific Value Assessment Report

Analyzes exoplanet detection limits, feature importance, and key physical recovery rates.

## 1. Planet Recovery Metrics by Astrophysical Regime

*   **Shallow Transits (< 1000 ppm) Recovery Rate**: 100.0% (38 targets)
*   **Deep Transits (>= 1000 ppm) Recovery Rate**: 100.0% (112 targets)
*   **Short-Period (< 5.0 days) Recovery Rate**: 100.0% (52 targets)
*   **Long-Period (>= 5.0 days) Recovery Rate**: 100.0% (98 targets)

## 2. Feature Importances (Model C Coefficients)

| Rank | Feature Name | Coefficient Value | Impact |
| :---: | :--- | :---: | :--- |
| 1 | window_completeness | -0.9743 | Demoting/vetoing |
| 2 | shape_consistency | -0.5901 | Demoting/vetoing |
| 3 | duration_consistency | 0.4774 | Promoting exoplanet |
| 4 | depth_consistency | 0.4294 | Promoting exoplanet |
| 5 | baseline_period_ratio | 0.2528 | Promoting exoplanet |
| 6 | transit_spacing_regularity | 0.1586 | Promoting exoplanet |
| 7 | alias_family_size | 0.0878 | Promoting exoplanet |
| 8 | baseline_span | 0.0589 | Promoting exoplanet |
| 9 | period_duration_consistency | -0.0488 | Demoting/vetoing |
| 10 | transit_number_monotonicity | -0.0395 | Demoting/vetoing |
| 11 | coverage_fraction | 0.0250 | Promoting exoplanet |
| 12 | harmonic_order | 0.0250 | Promoting exoplanet |
| 13 | chain_coherence | 0.0250 | Promoting exoplanet |
| 14 | residual_mad | 0.0109 | Promoting exoplanet |
| 15 | family_complexity | -0.0075 | Demoting/vetoing |
| 16 | uncertainty_ratio | -0.0012 | Demoting/vetoing |

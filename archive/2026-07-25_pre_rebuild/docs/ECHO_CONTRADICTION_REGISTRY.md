# ECHO Contradiction Registry

This registry defines the explicit triggers, parameter thresholds, logical formulas, and severity ratings for the physical contradictions evaluated by Stage 5 ECHO.

---

## Registry Table

| Contradiction ID | Severity | Logical Formula / Trigger | Description |
| :--- | :---: | :--- | :--- |
| `CONTRADICTION_GEOMETRY_TEMPORAL` | **HIGH** | `coverage_fraction > 0.8` <br>AND `duration_plausibility == 'INCONSISTENT'` | Strong temporal coverage (observed transits match expected timing) but observed duration differs significantly from Keplerian expected duration. |
| `CONTRADICTION_MORPHOLOGY_PHYSICS` | **MEDIUM**| `transit_spacing_regularity < 0.01` <br>AND `overall_morphology_state == 'WEAK'` | Extremely regular spacing (variance of normalized spacings < 0.01) but the event morphology is highly inconsistent (depth/duration/shape variance). |
| `CONTRADICTION_OBSERVABILITY` | **MEDIUM**| `coverage_fraction > 0.8` <br>AND `window_completeness < 0.3` | The candidate claims high coverage fraction, but the window completeness indicates less than 30% of expected transits fell inside TESS active data sectors. |

---

## Parameters & Thresholds

All thresholds are defined in `echo_config.py` to allow clean calibration in downstream runs.

### `coverage_fraction_high_threshold = 0.8`
Defines the boundary above which temporal coverage is considered strong enough to expect physical consistency.

### `spacing_regularity_regular_threshold = 0.01`
Defines the variance of normalized spacings below which a candidate's timings are considered highly regular.

### `window_completeness_low_threshold = 0.3`
Defines the boundary below which the data windows are too sparse to support high-coverage claims.

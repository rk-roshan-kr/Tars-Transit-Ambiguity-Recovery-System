# Audit 4: False Positive Taxonomy Report

Details the classification and distribution of false positive detections in the blind validation split.

## 1. False Positive Category Distribution

*   **Total False Positive Detections (Score >= 0.5, Label = 0)**: 75

| FP Category | Count | Percentage | Description |
| :--- | :---: | :---: | :--- |
| **VARIABLE_STAR** | 70 | 93.3% | Pulsators, multi-period variable stars, or binaries |
| **STELLAR_ACTIVITY** | 0 | 0.0% | Flares, spots, and micro-variability |
| **INSTRUMENT_SYSTEMATIC** | 0 | 0.0% | Spacecraft pointing drifts and momentum dumps |
| **DATA_QUALITY_FAILURE** | 0 | 0.0% | High-frequency noise, bad detrending residuals |
| **TRANSIT_LIKE_SIGNAL** | 5 | 6.7% | Eclipsing binaries, non-planetary geometries |
| **UNKNOWN** | 0 | 0.0% | Unresolved edge cases |

## 2. False Positive Examples

| TIC ID | Model D Score | FP Category | Residual MAD | Harmonic Order |
| :---: | :---: | :--- | :---: | :---: |
| 167754523 | 0.7360 | TRANSIT_LIKE_SIGNAL | 0.000000 | 1.0 |
| 30312676 | 0.7221 | VARIABLE_STAR | 0.000000 | 1.0 |
| 279740441 | 0.7365 | VARIABLE_STAR | 0.000000 | 1.0 |
| 30312676 | 0.7306 | VARIABLE_STAR | 0.000000 | 1.0 |
| 167754523 | 0.7246 | VARIABLE_STAR | 0.000000 | 1.0 |
| 279740441 | 0.7247 | VARIABLE_STAR | 0.000000 | 1.0 |
| 167754523 | 0.7161 | TRANSIT_LIKE_SIGNAL | 0.000000 | 1.0 |
| 279740441 | 0.7275 | VARIABLE_STAR | 0.000000 | 1.0 |
| 220396259 | 0.7207 | VARIABLE_STAR | 0.000000 | 1.0 |
| 30312676 | 0.7297 | VARIABLE_STAR | 0.000000 | 1.0 |
| 220396259 | 0.7537 | VARIABLE_STAR | 0.000000 | 1.0 |
| 167754523 | 0.7269 | VARIABLE_STAR | 0.000000 | 1.0 |
| 30312676 | 0.7223 | VARIABLE_STAR | 0.000000 | 1.0 |
| 143022742 | 0.7355 | VARIABLE_STAR | 0.000000 | 1.0 |
| 143022742 | 0.7355 | VARIABLE_STAR | 0.000000 | 1.0 |

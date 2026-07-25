# Audit 5: False Negative Taxonomy Report

Details the classification and distribution of missed exoplanets (false negatives) in the blind validation split.

## 1. False Negative Category Distribution

*   **Total Missed Exoplanets (Score < 0.5, Label = 1)**: 0

| FN Category | Count | Percentage | Description |
| :--- | :---: | :---: | :--- |
| **SHALLOW_TRANSIT** | 0 | 0.0% | Transit depth < 1000 ppm (0.1%) |
| **LOW_SNR** | 0 | 0.0% | High-frequency stellar or systemic noise |
| **DATA_GAPS** | 0 | 0.0% | Gaps in observation windows preventing detection |
| **SPARSE_TRANSITS** | 0 | 0.0% | Extremely short baseline span or single-sector transits |
| **FEATURE_FAILURE** | 0 | 0.0% | Inconsistencies in recovered transit period/duration |
| **UNKNOWN** | 0 | 0.0% | Unresolved edge cases |

## 2. False Negative Examples

| TIC ID | Model D Score | FN Category | Depth (ppm) | Residual MAD |
| :---: | :---: | :--- | :---: | :---: |

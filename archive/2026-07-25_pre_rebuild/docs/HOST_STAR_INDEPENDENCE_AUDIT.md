# Audit 16.3 — Host-Star vs. Complexity Independence Audit

Quantifies the statistical independence between stellar catalog physical context and Stage 3 candidate family complexity metrics.

## 1. Distance Correlation Matrix (dCor)

| Host Feature | `FC_events` | `FC_clusters` | `FC_support` | `FC_coverage` | `FC_stability` |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `header_teff` | 0.1692 | 0.1005 | 0.1316 | 0.1081 | 0.1081 |
| `header_logg` | 0.1815 | 0.1312 | 0.1689 | 0.1116 | 0.1116 |
| `header_radius` | 0.2087 | 0.1199 | 0.1320 | 0.1512 | 0.1512 |
| `header_tessmag` | 0.1219 | 0.1246 | 0.1148 | 0.1352 | 0.1352 |
| `spectral_class_ord` | 0.1578 | 0.0901 | 0.1234 | 0.0953 | 0.0953 |
| `lum_class_ord` | 0.1787 | 0.0625 | 0.1008 | 0.1037 | 0.1037 |

## 2. Pearson Correlation Matrix (r)

| Host Feature | `FC_events` | `FC_clusters` | `FC_support` | `FC_coverage` | `FC_stability` |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `header_teff` | 0.1116 | -0.0080 | -0.0530 | 0.0682 | 0.0682 |
| `header_logg` | -0.0981 | 0.0957 | 0.1392 | -0.0249 | -0.0249 |
| `header_radius` | 0.1384 | 0.0717 | -0.0365 | 0.1326 | 0.1326 |
| `header_tessmag` | -0.0466 | -0.0339 | -0.0626 | -0.0144 | -0.0144 |
| `spectral_class_ord` | 0.1215 | -0.0260 | -0.0764 | 0.0605 | 0.0605 |
| `lum_class_ord` | -0.1023 | -0.0153 | 0.0601 | -0.0867 | -0.0867 |

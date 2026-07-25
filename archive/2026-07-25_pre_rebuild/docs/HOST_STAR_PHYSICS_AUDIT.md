# Audit 16.2 & 16.2B — Host-Star Physics & Stratification Audit

Measures correlations between host-star astrophysical properties and true planetary parameters, and stratifies ambiguity model performance across populations.

## 1. Host-Star x Planet Physics Matrix (Pearson r)

| Host-Star Feature | `period` | `duration` | `depth` | `expected_transit_count` | `estimated_snr` |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `header_teff` | 0.2077 | 0.4886 | 0.0645 | -0.1424 | 0.0954 |
| `header_logg` | -0.3153 | -0.5744 | -0.1107 | 0.1400 | -0.1227 |
| `header_radius` | 0.2779 | 0.5571 | 0.0997 | -0.1302 | 0.0949 |
| `header_tessmag` | -0.0948 | -0.1424 | 0.5609 | 0.1901 | -0.0983 |
| `spectral_class_ord` | 0.2419 | 0.5009 | 0.0718 | -0.1413 | 0.0914 |
| `lum_class_ord` | -0.1595 | -0.3198 | -0.1091 | 0.0135 | -0.0576 |
| `sector_count` | 0.4189 | 0.2736 | -0.3503 | -0.2630 | -0.1124 |
| `observation_count` | 0.4382 | 0.2099 | -0.3929 | -0.3798 | -0.1742 |

## 2. Host-Star x Planet Physics Matrix (Spearman rho)

| Host-Star Feature | `period` | `duration` | `depth` | `expected_transit_count` | `estimated_snr` |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `header_teff` | 0.1690 | 0.4965 | -0.1636 | -0.1594 | 0.0466 |
| `header_logg` | -0.1981 | -0.5401 | 0.0534 | 0.1898 | -0.1331 |
| `header_radius` | 0.1973 | 0.5533 | -0.0699 | -0.1888 | 0.1160 |
| `header_tessmag` | -0.1611 | -0.1496 | 0.5996 | 0.1528 | 0.0404 |
| `spectral_class_ord` | 0.1810 | 0.4966 | -0.1180 | -0.1700 | 0.0860 |
| `lum_class_ord` | -0.0206 | -0.2866 | -0.2552 | 0.0243 | -0.1661 |
| `sector_count` | 0.4411 | 0.1530 | -0.3269 | -0.4352 | -0.1769 |
| `observation_count` | 0.6053 | 0.1199 | -0.4408 | -0.6009 | -0.2241 |

## 3. Audit 16.2B — Population Stratification Audit

Evaluates the standalone ambiguity model (`family_complexity`) performance within physical sub-populations.

| Sub-Population | Train Size | Blind Size | CV Mean AUROC | CV Mean PR-AUC | Blind Split AUROC | Blind Split PR-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Dwarfs (logg >= 4.0)** | 1751 | 201 | 0.5370 | 0.8246 | 0.5694 | 0.7759 |
| **Giants/Subgiants (logg < 4.0)** | 124 | 6 | 0.5088 | 0.4902 | 0.2000 | 0.1000 |
| **Hot Stars (Teff >= 6000 K)** | 536 | 22 | 0.6092 | 0.5382 | 0.7059 | 0.9122 |
| **Cool Stars (Teff < 6000 K)** | 1416 | 191 | 0.5161 | 0.7942 | 0.5921 | 0.7320 |
| **Bright Stars (TessMag < 11.0)** | 1665 | 101 | 0.5437 | 0.7840 | 0.5220 | 0.7249 |
| **Faint Stars (TessMag >= 11.0)** | 306 | 124 | 0.5101 | 0.6464 | 0.7603 | 0.7868 |

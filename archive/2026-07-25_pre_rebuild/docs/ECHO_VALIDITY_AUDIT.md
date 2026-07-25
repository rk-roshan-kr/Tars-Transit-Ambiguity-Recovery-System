# Audit 14.5 — ECHO Validity Audit

Analyzes the validity and informational content of multi-sector consistency (ECHO) features stratified by single-sector vs multi-sector stars.

## Feature: `depth_consistency`

| Stratum | Target Count | Missing Fraction | Variance (Non-NaN) | Binned Entropy | MI with Label | Single-Feat AUROC |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Global | 225 | 0.0000 | 0.020230 | 1.2327 | 0.1201 | 0.5794 |
| Single-Sector (Count=1) | 65 | 0.0000 | 0.008582 | 1.4888 | 0.1978 | 0.5917 |
| Multi-Sector (Count>=2) | 160 | 0.0000 | 0.024772 | 1.2756 | 0.1568 | 0.5894 |

## Feature: `duration_consistency`

| Stratum | Target Count | Missing Fraction | Variance (Non-NaN) | Binned Entropy | MI with Label | Single-Feat AUROC |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Global | 225 | 0.0000 | 0.012385 | 0.0708 | 0.0008 | 0.5100 |
| Single-Sector (Count=1) | 65 | 0.0000 | 0.000000 | 0.0000 | 0.0000 | 0.5000 |
| Multi-Sector (Count>=2) | 160 | 0.0000 | 0.017321 | 0.0931 | 0.0090 | 0.5153 |

## Feature: `shape_consistency`

| Stratum | Target Count | Missing Fraction | Variance (Non-NaN) | Binned Entropy | MI with Label | Single-Feat AUROC |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Global | 225 | 0.0000 | 0.006311 | 0.4700 | 0.0000 | 0.5090 |
| Single-Sector (Count=1) | 65 | 0.0000 | 0.000986 | 0.2164 | 0.0000 | 0.5562 |
| Multi-Sector (Count>=2) | 160 | 0.0000 | 0.008244 | 0.5290 | 0.0396 | 0.5392 |


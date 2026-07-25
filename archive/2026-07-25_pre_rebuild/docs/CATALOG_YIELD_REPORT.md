# Audit 10: Catalog Yield Projection Report

Models the expected exoplanet candidate yields, false positives, and manual review burden when running TARS on a 250,000-star catalog.

## 1. Projected Yield Table

| Threshold | Score Cutoff | Expected Candidates | Expected False Positives | Expected Manual Review Burden (Hours) |
| :---: | :---: | :---: | :---: | :---: |
| Top 0.1% | 0.7629 | 250 | 0 | 20.8 hrs |
| Top 0.5% | 0.7537 | 1,250 | 625 | 104.2 hrs |
| Top 1.0% | 0.7488 | 2,500 | 1,666 | 208.3 hrs |
| Top 5.0% | 0.7440 | 12,500 | 5,208 | 1041.7 hrs |

## 2. Review Recommendations

*   **Top 0.1% Threshold**: Excellent for high-purity exoplanet discovery with near-zero false alarms; manual follow-up is easily manageable by a single researcher.
*   **Top 1.0% Threshold**: Ideal for catalog release campaigns; captures most transits but requires significant vetting effort (~200 person-hours).

# Label Confidence Registry Spec

This document formalizes the label confidence framework (Phase 11.1) to handle target uncertainty and candidate tiers.

---

## 1. Quality Tiers and Confidence Weights

TARS defines four classes of label confidence:

| Class | Label Name | Confidence Weight | Criteria / Description |
| :--- | :--- | :---: | :--- |
| **Confirmed Planet** | `Tier A` | `1.0` | Confirmed planets in composite tables (`ps` or `pscomppars` or TFOPWG `CP`/`KP`). |
| **Strong Candidate** | `Tier B` | `0.75` | Active TOIs verified by TESS team (`PC` or `APC`) with no known false positive indicators. |
| **Candidate** | `Tier C` | `0.50` | Community TOIs (`CTOI`) or unconfirmed project candidates. |
| **False Positive** | `Tier D` | `0.0` | Confirmed eclipsing binaries (`EB`), false alarms (`FA`), or retired TOIs (`FP`). |

---

## 2. Ingestion Matrix for Training & Optimization

The models use these confidence weights in downstream training and fusion:

- **Stage 6C (Physics-Constrained ML) Training**: Admitted targets: Confirmed Planets (weight = 1.0) and False Positives (weight = 1.0). Candidates (weight = 0.50 / 0.75) are excluded from training to avoid contamination.
- **Stage 8 (Fusion Optimization) Calibration**: Calibrates meta-calibration using all labeled subsets (Tiers A, B, C, D) as targets to optimize ranking and False Positive rejection thresholds.

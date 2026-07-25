# TARS Core — Statistical Reporting Rules

Every number that appears in a paper, table, figure, or result claim must follow these rules. No raw percentages alone. No point estimates without uncertainty.

---

## Mandatory Reporting Format

Every reported metric must include:

```
value ± uncertainty  (n = sample_size)
```

Example:
```
Precision: 79.3% ± 6.8%  (n = 29 candidates)
```

Never:
```
Precision: 79.3%
```

---

## Confidence Interval Policy

- **Method:** Bootstrap resampling
- **Resamples:** 1,000
- **Confidence level:** 95%
- **Seed:** 42 (fixed for reproducibility)
- **Reported as:** `mean ± half-width of 95% CI`

---

## Sample Size Requirements

| Context | Minimum n | Notes |
|---|---|---|
| Precision / Recall claims | ≥ 20 candidates | Below this, CI spans are too wide to be meaningful |
| Ablation comparisons | ≥ 20 per variant | All variants must use the same validation split |
| Sparse-regime stratification (N=2) | Report n explicitly | May be small — report with caveat |
| Injection recovery | ≥ 30 per cell | Each depth × period cell in the injection grid |

---

## Significance Testing Policy

- Statistical significance uses Wilcoxon signed-rank test (non-parametric)
- Significance threshold: p < 0.05
- Report exact p-values, not just "p < 0.05"
- Effect size must accompany every significance claim

**Example (from previous work):** The EEA F1 improvement of +0.018 was confirmed by bootstrap: 95% CI (+0.012, +0.024), Wilcoxon p < 0.008.

---

## Calibration Reporting

ML probability outputs must include calibration metrics alongside discrimination metrics:

| Metric | Report |
|---|---|
| ECE | Always |
| MCE | Always |
| Brier Score | Always |
| ROC AUC | Always |
| Calibration curve | In supplementary |

**Reason:** The polarity inversion bug in the previous implementation produced a validation AUC of 0.3675 on the raw model — indistinguishable from chance. Calibration reporting is mandatory to catch such failures early.

---

## Forbidden Practices

- Reporting only on the test split without also reporting on validation (test results must be preceded by validation results)
- Reporting precision without the corresponding recall
- Claiming improvement without reporting the baseline
- Reporting percentages without sample sizes when n < 100
- Optimizing any threshold after viewing test split results

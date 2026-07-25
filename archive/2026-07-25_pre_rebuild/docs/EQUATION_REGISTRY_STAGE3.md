# EQUATION REGISTRY (Stage 3)

The following equations represent the frozen scientific core of the Stage 3 Sparse Period Recovery engine. No undocumented heuristics or ad-hoc adjustments may be used in these mathematical definitions.

---

### EQ-S3-01: Period Difference
Computes the fundamental interval spacing between any two discrete transit events $i$ and $j$.
```math
P_{i,j} = |t_j - t_i|
```

---

### EQ-S3-02: Timing Residual
Calculates the observed-minus-computed ($O-C$) timing deviation for the $k$-th transit event against a linear ephemeris defined by epoch $t_0$ and period $P$.
```math
r_k = t_k - (t_0 + n_k P)
```
*(Where $n_k$ is the nearest integer transit number from the epoch).*

---

### EQ-S3-03: Residual RMS
Quantifies the root-mean-square error of the timing residuals across all $N$ supporting events for a given period hypothesis.
```math
RMS_r = \sqrt{\frac{1}{N} \sum_{k=1}^{N} r_k^2}
```

---

### EQ-S3-04: Residual MAD
Quantifies the Median Absolute Deviation of the timing residuals, providing a robust estimator resilient to individual false-positive outliers.
```math
MAD_r = \text{median}(|r_k - \text{median}(r)|)
```

---

### EQ-S3-05: Coverage Fraction
Calculates the proportion of expected transits that were successfully recovered, adjusted for sector gaps.
```math
C = \frac{N_{matched}}{N_{expected}}
```
*(Where $N_{expected}$ is calculated bounded by the observation baseline and adjusted for missing/flagged cadences).*

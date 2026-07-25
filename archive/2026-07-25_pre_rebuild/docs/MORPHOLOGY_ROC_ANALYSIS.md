# Morphological Coherence ROC Analysis

This document formulates the threshold-independent statistical framework for validating morphological coherence under realistic noise regimes.

---

## 1. Statistical Separation Metrics

Rather than using a rigid 95% threshold-dependent recall/rejection rate (which degrades under high photometric noise), the performance of the Morphological Coherence subsystem is evaluated using three statistical metrics.

### A. Kolmogorov-Smirnov (KS) Statistic ($D_{\text{KS}}$)
Measures the maximum distance between the empirical cumulative distribution functions (CDFs) of planet coherence scores ($F_P(x)$) and eclipsing binary coherence scores ($F_{EB}(x)$):
$$D_{\text{KS}} = \sup_x |F_P(x) - F_{EB}(x)|$$
- **Significance**: Calculated using the two-sample KS test. The separation is statistically significant if the $p$-value satisfies:
  $$p < 10^{-5}$$

### B. Cohen's $d$ (Effect Size)
Quantifies the standardized difference in mean coherence scores between planets ($\mu_P$) and eclipsing binaries ($\mu_{EB}$):
$$d = \frac{\mu_P - \mu_{EB}}{s_{\text{pooled}}}$$
where $s_{\text{pooled}}$ is the pooled standard deviation.
- **Significance**: An effect size $d \ge 1.5$ is considered a "very large" effect, demonstrating robust separation.

### C. Receiver Operating Characteristic (ROC) Area Under Curve (AUC)
Computes the probability that a randomly chosen planet has a higher coherence score than a randomly chosen eclipsing binary:
$$\text{AUC} = P(C_{\text{coh}, P} > C_{\text{coh}, EB})$$
- **Significance**: An AUC of $\ge 0.85$ indicates highly reliable discrimination.

---

## 2. Realistic Noise Regime Validation Criteria

Under realistic TESS noise sweeps, the target success criteria for the morphological coherence framework are locked as follows:

| Metric | Target Value | Verification command |
| :--- | :---: | :--- |
| **ROC-AUC** | $\ge 0.85$ | `pytest tests/test_stage5_echo.py` (via mock simulation experiment) |
| **KS p-value**| $< 10^{-5}$ | `pytest tests/test_stage5_echo.py` |
| **Cohen's d** | $\ge 1.5$ | `pytest tests/test_stage5_echo.py` |

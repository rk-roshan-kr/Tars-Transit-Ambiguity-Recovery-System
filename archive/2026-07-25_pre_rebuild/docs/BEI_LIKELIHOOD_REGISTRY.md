# BEI Likelihood Registry (v1.0)

This registry defines and freezes the exact mathematical equations used to compute Bayes Factor contributions for every admitted feature in Stage 6 Bayesian Evidence Integration. All equations are monotonic, bounded, and reproducible.

No implementation may deviate from these equations. Any revision requires a new registry version and governance re-approval.

---

## 1. General Form

All Bayes Factors are computed in log space:

$$\ln BF_i = \ln P(E_i | H) - \ln P(E_i | \neg H)$$

The total log Bayes Factor is:

$$\ln BF_{\text{total}} = \sum_{i \in \text{admitted}} \ln BF_i$$

For Version 1, prior to empirical calibration from SIM-P/SIM-FP datasets, each feature uses a **parametric approximation** based on physically motivated distribution shapes. Parameters will be updated with fitted values from simulation runs in Phase 10 validation.

---

## 2. Likelihood Equations by Feature

### LR-01: `coverage_fraction` (EV-T2)

$$\ln BF_{\text{cov}} = \ln \frac{\text{Beta}(f; \alpha_H, \beta_H)}{\text{Beta}(f; \alpha_{\neg H}, \beta_{\neg H})}$$

**Version 1 parameters**: $\alpha_H = 8, \beta_H = 2$ (mean 0.80); $\alpha_{\neg H} = 2, \beta_{\neg H} = 3$ (mean 0.40)

**Monotonicity**: $\partial \ln BF / \partial f > 0$ — confirmed by Beta ratio properties when $\alpha_H / \beta_H > \alpha_{\neg H} / \beta_{\neg H}$.

**Bounds**: $\ln BF \in (-\infty, +\infty)$; numerically bounded to $[-10, +10]$ to prevent degenerate posteriors.

**Missing data handling**: `None` → $\ln BF = 0.0$ (no evidence contributed).

---

### LR-02: `residual_mad` (EV-T6)

$$\ln BF_{\text{mad}} = \ln \frac{\text{Gamma}(\text{mad}; k_H, \theta_H)}{\text{Gamma}(\text{mad}; k_{\neg H}, \theta_{\neg H})}$$

**Version 1 parameters**: $k_H = 2, \theta_H = 0.001$ (tight residuals); $k_{\neg H} = 2, \theta_{\neg H} = 0.01$ (broader residuals)

**Monotonicity**: Smaller MAD → higher $BF$. Confirmed: when $\theta_H < \theta_{\neg H}$, $BF$ decreases as MAD increases.

**Bounds**: Clamped to $[-10, +10]$.

---

### LR-03: `baseline_span` (EV-T3)

> **AMENDED** — See [PHASE9_AMENDMENT_01.md](file:///d:/TARS/TarsCore/docs/PHASE9_AMENDMENT_01.md).
> Original Phase 9 specification was a step-function threshold model.
> Replaced with sigmoid by formal amendment during Phase 10 review.

$$\ln BF_{\text{base}} = \ln\left(1 + \tanh\left(\frac{T - r_0}{\sigma_r}\right)\right) - \ln 2$$

**Version 1 parameters**: $r_0 = 54.8$ days (= $2 \times 27.4$ day TESS sector), $\sigma_r = 5.0$

**Rationale for sigmoid**: Avoids runtime period-context dependency; smooth and differentiable for Phase 10.1 sensitivity analysis. Encodes the same physical constraint (short baselines are weak evidence) as the original step function.

**Monotonicity**: Strictly monotonically increasing — confirmed by $\tanh$ derivative.

**Asymptotic range**: $\ln BF \in [-0.69, +0.10]$ (weak contributor by design).

**Calibration**: $r_0$ and $\sigma_r$ will be updated from SIM-P/SIM-FP distributions in Phase 10.1.

---

### LR-04: `harmonic_order` (EV-H1)

$$\ln BF_{\text{ord}} = \ln \frac{P(\text{order} = k | H)}{P(\text{order} = k | \neg H)}$$

**Version 1 discrete table**:

| Order $k$ | $P(k|H)$ | $P(k|\neg H)$ | $\ln BF$ |
| :---: | :---: | :---: | :---: |
| 1 | 0.85 | 0.40 | $+0.754$ |
| 2 | 0.10 | 0.30 | $-1.099$ |
| 3 | 0.04 | 0.20 | $-1.609$ |
| $\ge 4$ | 0.01 | 0.10 | $-2.303$ |

**Monotonicity**: Higher order → lower $\ln BF$ by construction.

---

### LR-05: `alias_family_size` (EV-H2)

$$\ln BF_{\text{fam}} = \ln \frac{\text{Poisson}(n; \lambda_H)}{\text{Poisson}(n; \lambda_{\neg H})}$$

**Version 1 parameters**: $\lambda_H = 1.5$ (small families); $\lambda_{\neg H} = 4.0$ (larger alias cascades)

**Monotonicity**: Larger family → lower $\ln BF$. Confirmed by Poisson ratio when $\lambda_H < \lambda_{\neg H}$.

**Bounds**: Clamped to $[-8, +4]$.

---

### LR-06: `uncertainty_ratio` (EV-S3)

$$\ln BF_{\text{unc}} = \ln \frac{\text{LogNormal}(r; \mu_H, \sigma_H)}{\text{LogNormal}(r; \mu_{\neg H}, \sigma_{\neg H})}$$

**Version 1 parameters**: $\mu_H = -6.0, \sigma_H = 1.0$ (tight ephemeris); $\mu_{\neg H} = -3.0, \sigma_{\neg H} = 1.5$ (broad)

**Monotonicity**: Smaller ratio → higher $\ln BF$.

**Bounds**: Clamped to $[-10, +10]$.

---

### LR-07: `baseline_period_ratio` (EV-I2)

$$\ln BF_{\text{rat}} = \ln\left(1 + \tanh\left(\frac{r - r_0}{\sigma_r}\right)\right) - \ln 2$$

**Version 1 parameters**: $r_0 = 3.0$, $\sigma_r = 1.5$

**Properties**: Equals $0.0$ at $r = r_0$; positive for $r > r_0$; negative for $r < r_0$.

**Monotonicity**: Strictly monotonically increasing in $r$ — confirmed by $\tanh$ derivative.

**Bounds**: $\ln BF \in (-\ln 2, 0)$ for $r < r_0$; approaches $0$ asymptotically above.

---

### LR-08: `family_complexity` (EV-I4)

$$\ln BF_{\text{cmplx}} = \ln \frac{\text{Poisson}(c; \mu_H)}{\text{Poisson}(c; \mu_{\neg H})}$$

**Version 1 parameters**: $\mu_H = 2.0$; $\mu_{\neg H} = 5.0$

**Monotonicity**: Higher complexity → lower $\ln BF$.

---

### LR-09: `window_completeness` (EV-O3)

$$\ln BF_{\text{wc}} = \ln \frac{\text{Beta}(w; \alpha_H, \beta_H)}{\text{Beta}(w; \alpha_{\neg H}, \beta_{\neg H})}$$

**Version 1 parameters**: $\alpha_H = 7, \beta_H = 2$ (mean 0.78); $\alpha_{\neg H} = 3, \beta_{\neg H} = 4$ (mean 0.43)

**Monotonicity**: Higher completeness → higher $\ln BF$.

---

### LR-10: `period_duration_consistency` (EV-P1)

$$\ln BF_{\text{pdc}} = \ln \frac{\text{Beta}(c; \alpha_H, \beta_H)}{\text{Beta}(c; \alpha_{\neg H}, \beta_{\neg H})}$$

**Version 1 parameters**: $\alpha_H = 9, \beta_H = 2$ (mean 0.82); $\alpha_{\neg H} = 2, \beta_{\neg H} = 5$ (mean 0.29)

**Missing data**: `None` → $\ln BF = 0.0$.

---

### LR-11: `chain_coherence` (EV-P3)

$$\ln BF_{\text{cc}} = \ln \frac{\text{Beta}(\phi; \alpha_H, \beta_H)}{\text{Beta}(\phi; \alpha_{\neg H}, \beta_{\neg H})}$$

**Version 1 parameters**: $\alpha_H = 10, \beta_H = 2$ (mean 0.83); $\alpha_{\neg H} = 2, \beta_{\neg H} = 5$ (mean 0.29)

**Monotonicity**: Higher coherence → higher $\ln BF$.

---

### LR-12: `transit_spacing_regularity` (EV-P5)

$$\ln BF_{\text{tsr}} = \ln \frac{\text{LogNormal}(v; \mu_H, \sigma_H)}{\text{LogNormal}(v; \mu_{\neg H}, \sigma_{\neg H})}$$

**Version 1 parameters**: $\mu_H = -8.0, \sigma_H = 1.2$; $\mu_{\neg H} = -4.5, \sigma_{\neg H} = 1.5$

**Monotonicity**: Smaller variance → higher $\ln BF$. Calibrated threshold $0.010$ from Phase 8.1 survives as the inflection point.

---

### LR-13: `transit_number_monotonicity` (EV-P6)

$$\ln BF_{\text{tnm}} = \ln \frac{\text{Beta}(m; \alpha_H, \beta_H)}{\text{Beta}(m; \alpha_{\neg H}, \beta_{\neg H})}$$

**Version 1 parameters**: $\alpha_H = 10, \beta_H = 1.5$ (mean 0.87); $\alpha_{\neg H} = 3, \beta_{\neg H} = 4$ (mean 0.43)

---

### LR-14–16: Morphology (`depth_consistency`, `duration_consistency`, `shape_consistency`)

$$\ln BF_{\text{morph}} = \ln \frac{\text{Beta}(x; \alpha_H, \beta_H)}{\text{Beta}(x; \alpha_{\neg H}, \beta_{\neg H})}$$

**Version 1 parameters** (shared across all three):
$\alpha_H = 8, \beta_H = 2$ (mean 0.80); $\alpha_{\neg H} = 2, \beta_{\neg H} = 4$ (mean 0.33)

**Missing data**: `None` → $\ln BF = 0.0$.

---

## 3. Log BF Numerical Safety Rules

All log Bayes Factor values must be:
1. Computed in `float64` precision.
2. Clamped to $[-10.0, +10.0]$ before summing (prevents single feature dominating the posterior when distributions diverge at extremes).
3. Summed in log space — not converted to $BF$ first — to prevent floating-point overflow.
4. Stored individually in the audit trail before reduction.

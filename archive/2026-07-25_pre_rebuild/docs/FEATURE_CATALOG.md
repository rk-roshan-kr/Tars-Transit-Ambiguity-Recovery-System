# TARS Core — Feature Catalog

Every feature extracted by the pipeline is listed here before any code is written.

This document is the authoritative specification. If a feature is not in this catalog, it does not exist in the codebase. If a feature exists in the codebase but not here, it must be added to this catalog or removed.

---

## Detection Features
*(Produced by Stage 2 — Transit Event Detection)*

| Feature | Type | Unit | Description |
|---|---|---|---|
| `depth` | float | fractional flux | Transit depth relative to local baseline |
| `duration` | float | days | Transit duration (first to last contact) |
| `snr` | float | dimensionless | Signal-to-noise ratio: depth / sigma_local |
| `local_noise` | float | fractional flux | MAD-based local noise estimate at event time |
| `event_time` | float | BTJD | Mid-transit time |

---

## Period Recovery Features
*(Produced by Stage 3 — Sparse Period Recovery)*

| Feature | Type | Unit | Description |
|---|---|---|---|
| `period` | float | days | Best-fit trial orbital period |
| `period_stability` | float | dimensionless | Variance of residuals across candidate period hypotheses |
| `timing_residual_mean` | float | minutes | Mean timing residual across grouped events |
| `timing_residual_std` | float | minutes | Standard deviation of timing residuals |
| `timing_residual_mad` | float | minutes | MAD of timing residuals (robust) |
| `n_events` | int | count | Number of detected events in the candidate chain |

---

## Morphology Features
*(Produced by Stage 4A — EEA)*

| Feature | Type | Unit | Description |
|---|---|---|---|
| `depth_consistency` | float | dimensionless | C_coh coherence score ∈ [0, 1] |
| `duration_consistency` | float | dimensionless | Fractional duration variance across events |
| `shape_consistency` | float | dimensionless | Normalized shape coherence |
| `cross_correlation` | float | dimensionless | Cross-correlation of transit profiles (N≥2) |

---

## Geometry Features
*(Produced by Stage 4B — ECHO)*

| Feature | Type | Unit | Description |
|---|---|---|---|
| `expected_duration` | float | days | Duration predicted by orbital geometry |
| `observed_duration` | float | days | Measured transit duration |
| `duration_ratio` | float | dimensionless | GCP_dur: ratio of observed to expected duration |
| `duty_cycle` | float | dimensionless | Transit duration / orbital period |
| `asymmetry` | float | dimensionless | GCP_asym: ingress vs egress imbalance |
| `gcp` | float | dimensionless | Composite Geometric Consistency Proxy score ∈ [0, 1] |
| `echo_state` | str | — | "PASS", "GRAY", or "FAIL" |

---

## Noise Features
*(Produced by Stage 1 — Signal Conditioning)*

| Feature | Type | Unit | Description |
|---|---|---|---|
| `white_noise` | float | fractional flux | Gaussian noise component estimate |
| `red_noise` | float | fractional flux | Correlated noise component estimate |
| `beta_factor` | float | dimensionless | Red noise scaling factor (β) |
| `autocorrelation` | float | dimensionless | Lag-1 autocorrelation coefficient |
| `rms` | float | fractional flux | Overall RMS of conditioned light curve |

---

## Statistical Features
*(Produced by Stage 5 — Statistical Evidence Layer)*

| Feature | Type | Unit | Description |
|---|---|---|---|
| `log_likelihood_ratio` | float | dimensionless | ln(L_transit / L_noise) |
| `bic_penalty` | float | dimensionless | BIC = k·ln(N) complexity penalty |
| `bayes_factor` | float | dimensionless | Bayesian evidence ratio |
| `evidence_score` | float | dimensionless | Composite statistical support score ∈ [0, 1] |

---

## ML Features
*(Used as inputs to Stage 6 — ML Advisory Layer)*

The XGBoost classifier is trained on a subset of the above features. The exact feature vector used is:

| Feature | Source | Paper Reference |
|---|---|---|
| `period_stability` | Stage 3 | §3.4 |
| `depth_consistency` (C_coh) | Stage 4A (EEA) | §3.4 |
| `local_noise` | Stage 2 | §3.4 |
| `gcp` | Stage 4B (ECHO) | §3.4 |

> [!IMPORTANT]
> The paper (§3.4) lists: "period stability, depth variance, baseline noise, and the EEA coherence score." `depth_variance` maps to `depth_consistency` (C_coh from EEA). `gcp` is selected as the 4th feature over raw `depth_consistency` to avoid redundancy with C_coh. This decision is documented here and must be justified in `model_card.md`.

> [!IMPORTANT]
> The ML feature vector must never be modified without updating `stage6_ml/model_card.md` and re-running all validation suites. Feature drift is a primary cause of the polarity inversion bug in the previous implementation.

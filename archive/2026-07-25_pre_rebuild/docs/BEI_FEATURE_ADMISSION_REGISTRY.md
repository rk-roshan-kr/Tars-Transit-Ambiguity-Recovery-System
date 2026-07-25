# BEI Feature Admission Registry

This document is the official frozen whitelist and blacklist of features that may or may not contribute Bayes Factors to Stage 6 Bayesian Evidence Integration. It formalizes the dependency findings from `BEI_EVIDENCE_DEPENDENCY_AUDIT.md`.

No feature may enter Stage 6 implementation unless it appears in the **Admitted** section of this registry.

---

## 1. Admitted Features

These features have been reviewed for independence, traceability, and non-leakage. Each will receive a Bayes Factor likelihood mapping defined in `BEI_LIKELIHOOD_REGISTRY.md`.

### Family A — Temporal

| Feature | Field Path | EV Code | Admission Rationale |
| :--- | :--- | :--- | :--- |
| `coverage_fraction` | `ev.temporal.coverage_fraction` | EV-T2 | Independent ratio $N_{\text{matched}}/N_{\text{expected}}$. Most informative representative of the support/coverage/missing cluster. |
| `residual_mad` | `ev.temporal.residual_mad` | EV-T6 | Robust median absolute deviation of O-C residuals; preferred over RMS for outlier resistance. |
| `baseline_span` | `ev.temporal.baseline_span` | EV-T3 | Raw observation window in days; independent of timing scatter metrics. |

### Family B — Harmonic

| Feature | Field Path | EV Code | Admission Rationale |
| :--- | :--- | :--- | :--- |
| `harmonic_order` | `ev.harmonic.harmonic_order` | EV-H1 | Integer structural label; fully independent of all residual metrics. |
| `alias_family_size` | `ev.harmonic.alias_family_size` | EV-H2 | Total competing hypotheses; independent structural count. |

### Family C — Stability

| Feature | Field Path | EV Code | Admission Rationale |
| :--- | :--- | :--- | :--- |
| `uncertainty_ratio` | `ev.stability.uncertainty_ratio` | EV-S3 | $\sigma_P / P$; ephemeris precision. Independent of residual scatter metrics. |

### Family D — Information

| Feature | Field Path | EV Code | Admission Rationale |
| :--- | :--- | :--- | :--- |
| `baseline_period_ratio` | `ev.information.baseline_period_ratio` | EV-I2 | $T_{\text{baseline}}/P$; captures how many orbital periods are observed. Independent ratio. |
| `family_complexity` | `ev.information.family_complexity` | EV-I4 | Number of candidates in full family; independent structural count. |

### Family E — Observability

| Feature | Field Path | EV Code | Admission Rationale |
| :--- | :--- | :--- | :--- |
| `window_completeness` | `ev.observability.window_completeness` | EV-O3 | $N_{\text{obs}}/(N_{\text{obs}}+N_{\text{hidden}})$; gap-aware data quality ratio. Representative of the observability cluster. |

### Family F — Physics

| Feature | Field Path | EV Code | Admission Rationale |
| :--- | :--- | :--- | :--- |
| `period_duration_consistency` | `ev.physics.period_duration_consistency` | EV-P1 | Keplerian duration check. Admitted when non-`None` (requires stellar metadata). |
| `chain_coherence` | `ev.physics.chain_coherence` | EV-P3 | Event timing chain consistency; fully independent. |
| `transit_spacing_regularity` | `ev.physics.transit_spacing_regularity` | EV-P5 | Normalized spacing variance; calibrated at threshold $0.010$ in Phase 8.1. |
| `transit_number_monotonicity` | `ev.physics.transit_number_monotonicity` | EV-P6 | Fraction of monotonically increasing epoch assignments; independent. |

### Family G — Morphology (from ECHO)

| Feature | Field Path | Source | Admission Rationale |
| :--- | :--- | :--- | :--- |
| `depth_consistency` | `echo.morphology_assessment.depth_consistency` | EV-MC-01 | Fractional depth coherence; independent morphological measurement. |
| `duration_consistency` | `echo.morphology_assessment.duration_consistency` | EV-MC-02 | Fractional duration coherence; weakly correlated with depth_consistency but admitted independently. |
| `shape_consistency` | `echo.morphology_assessment.shape_consistency` | EV-MC-03 | Mean symmetry; independent of depth/duration metrics. |

---

## 2. Excluded Features

These features must never contribute a Bayes Factor. Any attempt to add them constitutes a protocol violation.

### Stage 3 Leakage — Hard Excluded

| Feature | Reason |
| :--- | :--- |
| `confidence_score` | Stage 3 ranking composite — not independent evidence |
| `ranking_trace` | Stage 3 ranking artifact |
| `ambiguity_score` | Stage 3 score delta — not a physical measurement |
| `ambiguity_index` | Stage 3 derived ranking residual |
| `information_content` | Stage 3 derived composite |
| `physics_score` | Neutralized ECHO ranking signal (set to `None` in Phase 8.1) |

### Redundant Features — Hard Excluded

| Feature | Reason |
| :--- | :--- |
| `missing_transits` | $= N_{\text{expected}} - N_{\text{matched}}$; functional of `coverage_fraction` |
| `support_count` | Numerator of `coverage_fraction`; zero independent information once ratio is admitted |
| `residual_rms` | Correlated (~0.9) with admitted `residual_mad` |
| `normalized_mad` | $= \text{residual\_mad}/P$; no independent information given known period |
| `normalized_rms` | $= \text{residual\_rms}/P$; no independent information |
| `event_density` | $= n_{\text{events}}/T_{\text{baseline}}$; functional of admitted `baseline_span` + `n_events` |
| `observable_transits` | Numerator component of `window_completeness` |
| `hidden_transits` | Denominator component of `window_completeness` |

### Prior Quantities — Structurally Misclassified

| Feature | Reason |
| :--- | :--- |
| `occurrence_log_prior` | Astrophysical occurrence rate prior. Must not be treated as evidence. Reserved for future prior upgrades. |

---

## 3. Conditional Features

These features carry partial independent signal but require explicit handling before admission:

| Feature | Condition for Admission |
| :--- | :--- |
| `gap_fraction` | Admit only if anti-correlation with `window_completeness` is confirmed < 0.85 in validation dataset. Otherwise exclude. |
| `kepler_plausibility` | Admit only when `period_duration_consistency` is `None` (stellar data absent) and kepler check provides independent constraint. |
| `alias_density` | Admit only when `alias_family_size` is unavailable. |
| `n_events` | Admit only when `coverage_fraction` is unavailable (e.g. no ephemeris prediction available). |
| `cross_correlation` | Admit only when raw profile cutouts are stored and `X_coh` is non-`None`. |

# BEI Evidence Dependency Audit

This document performs a complete dependency analysis of all 27 Stage 4 EEA features and Stage 5 ECHO morphology outputs to identify correlations that would violate the conditional independence assumption of naive Bayes Evidence Integration.

---

## 1. Methodology

Under naive Bayes, the combined Bayes Factor is:

$$\ln BF_{\text{total}} = \sum_i \ln BF_i$$

This product decomposition is only valid if features are **conditionally independent** given hypothesis $H$:

$$P(E_1, E_2, \ldots, E_n | H) = \prod_i P(E_i | H)$$

Admitting two strongly correlated features $E_i$ and $E_j$ means the same physical information is counted twice, inflating confidence without adding genuine evidence.

### Dependency Classification
- **ADMIT**: Feature is sufficiently independent; may contribute a Bayes Factor.
- **EXCLUDE**: Feature is redundant or a direct linear function of an admitted variable.
- **CONDITIONAL**: Feature carries partial independent signal; conditionally admitted as a representative for its correlation cluster, or admitted only in the absence of a stronger substitute.

---

## 2. Dependency Analysis by Evidence Family

### Family A — Temporal Evidence (`TemporalEvidence`)

| Feature | EV Code | Independence Assessment | Correlated With | Decision |
| :--- | :--- | :--- | :--- | :--- |
| `support_count` | EV-T1 | Partial — direct numerator of coverage fraction | `coverage_fraction` | **CONDITIONAL** |
| `coverage_fraction` | EV-T2 | Independent ratio $N_{\text{matched}}/N_{\text{expected}}$ | `support_count`, `missing_transits` | **ADMIT** (representative for cluster) |
| `baseline_span` | EV-T3 | Independent measurement of observation window | none | **ADMIT** |
| `missing_transits` | EV-T4 | Exact complement of `support_count`; $N_{\text{exp}} - N_{\text{matched}}$ | `coverage_fraction`, `support_count` | **EXCLUDE** |
| `residual_rms` | EV-T5 | Independent scatter metric | `residual_mad` (correlated ~0.9) | **CONDITIONAL** |
| `residual_mad` | EV-T6 | Robust complement of RMS | `residual_rms` | **ADMIT** (preferred; robust to outliers) |

**Cluster A-1**: {`support_count`, `coverage_fraction`, `missing_transits`} — admit `coverage_fraction` only.
**Cluster A-2**: {`residual_rms`, `residual_mad`} — admit `residual_mad` only (robust to outlier transits).

---

### Family B — Harmonic Evidence (`HarmonicEvidence`)

| Feature | EV Code | Independence Assessment | Correlated With | Decision |
| :--- | :--- | :--- | :--- | :--- |
| `harmonic_order` | EV-H1 | Integer structural descriptor; independent | none | **ADMIT** |
| `alias_family_size` | EV-H2 | Count of competing period hypotheses | `alias_density` (loose correlation) | **ADMIT** |
| `ambiguity_score` | EV-H3 | Stage 3 **ranking residual** — score delta to nearest alias | Stage 3 `confidence_score` | **EXCLUDE** — Stage 3 leakage |
| `alias_density` | EV-H4 | Count of aliases within tolerance band | `alias_family_size` | **CONDITIONAL** (admit only if family_size unavailable) |

---

### Family C — Stability Evidence (`StabilityEvidence`)

| Feature | EV Code | Independence Assessment | Correlated With | Decision |
| :--- | :--- | :--- | :--- | :--- |
| `normalized_mad` | EV-S1 | `residual_mad / P` — period-scaled version of EV-T6 | `residual_mad` | **EXCLUDE** — redundant with admitted EV-T6 given known period |
| `normalized_rms` | EV-S2 | `residual_rms / P` — period-scaled version of EV-T5 | `residual_rms` | **EXCLUDE** — redundant |
| `uncertainty_ratio` | EV-S3 | $\sigma_P / P$ — ephemeris precision independent of residuals | none | **ADMIT** |

**Rationale**: `normalized_mad` = `residual_mad / P`. Since both `residual_mad` and the period are known, `normalized_mad` adds zero independent information. Admitting both would double-count timing stability.

---

### Family D — Information Evidence (`InformationEvidence`)

| Feature | EV Code | Independence Assessment | Correlated With | Decision |
| :--- | :--- | :--- | :--- | :--- |
| `n_events` | EV-I1 | Total event count — independent of period | `support_count` (loose) | **CONDITIONAL** (useful when coverage unavailable) |
| `baseline_period_ratio` | EV-I2 | $T_{\text{baseline}} / P$ — independent ratio | `baseline_span`, `spacing_regularity` | **ADMIT** |
| `event_density` | EV-I3 | $n_{\text{events}} / T_{\text{baseline}}$ — sampling rate metric | `n_events`, `baseline_span` | **EXCLUDE** — functional of admitted EV-T3 + EV-I1 |
| `family_complexity` | EV-I4 | Total candidate family size — independent structural count | `alias_family_size` (loose) | **ADMIT** |

---

### Family E — Observability Evidence (`ObservabilityEvidence`)

| Feature | EV Code | Independence Assessment | Correlated With | Decision |
| :--- | :--- | :--- | :--- | :--- |
| `observable_transits` | EV-O1 | Raw count — numerator of window_completeness | `window_completeness`, `hidden_transits` | **EXCLUDE** — component of admitted ratio |
| `hidden_transits` | EV-O2 | Complement count — denominator element | `window_completeness` | **EXCLUDE** — component of admitted ratio |
| `window_completeness` | EV-O3 | $N_{\text{obs}} / (N_{\text{obs}} + N_{\text{hidden}})$ — independent ratio | `observable_transits`, `hidden_transits` | **ADMIT** (representative for cluster) |
| `gap_fraction` | EV-O4 | Gap duration / baseline — independent data quality metric | `window_completeness` (anti-correlated ~0.7) | **CONDITIONAL** (admit if anti-correlation confirmed < 0.85) |

**Cluster D-1**: {`observable_transits`, `hidden_transits`, `window_completeness`} — admit `window_completeness` only.

---

### Family F — Physics Evidence (`PhysicsEvidence`)

| Feature | EV Code | Independence Assessment | Correlated With | Decision |
| :--- | :--- | :--- | :--- | :--- |
| `period_duration_consistency` | EV-P1 | Physical consistency check; None when stellar data absent | `kepler_plausibility` (partial) | **ADMIT** (when non-None) |
| `kepler_plausibility` | EV-P2 | Kepler's Third Law constraint; None when stellar data absent | `period_duration_consistency` | **CONDITIONAL** (only if P1 unavailable or stellar data present) |
| `chain_coherence` | EV-P3 | Event timing chain internal consistency | none | **ADMIT** |
| `occurrence_log_prior` | EV-P4 | $\log p_{\text{occ}}(P)$ — period occurrence rate prior | none | **NOTE**: This is a prior, not evidence. Must be incorporated at the prior level, **not** as a Bayes Factor. |
| `transit_spacing_regularity` | EV-P5 | Variance of normalized spacing — independent timing metric | `residual_mad` (weak, ~0.4) | **ADMIT** |
| `transit_number_monotonicity` | EV-P6 | Monotonic epoch ordering fraction — independent | none | **ADMIT** |

**Note on EV-P4**: `occurrence_log_prior` is an astrophysical occurrence rate prior, not an evidence measurement. Incorporating it as a Bayes Factor would constitute prior double-counting. It must be reserved for future prior upgrades, not the BEI likelihood layer.

---

### Family G — Morphology Evidence (`MorphologyAssessment`, from ECHO)

| Feature | Source | Independence Assessment | Correlated With | Decision |
| :--- | :--- | :--- | :--- | :--- |
| `depth_consistency` | EV-MC-01 | Transit depth variation — independent morphological measurement | `duration_consistency` (weak, ~0.5) | **ADMIT** |
| `duration_consistency` | EV-MC-02 | Transit duration variation — independent measurement | `depth_consistency` (weak) | **ADMIT** |
| `shape_consistency` | EV-MC-03 | Mean symmetry score — independent shape metric | `depth_consistency` (weak) | **ADMIT** |
| `cross_correlation` | EV-MC-04 | Profile-level Pearson correlation — currently `None` for most candidates | — | **CONDITIONAL** (admit when profile storage is available) |

---

## 3. Admitted Feature Summary

| Family | Admitted Features |
| :--- | :--- |
| Temporal | `coverage_fraction`, `residual_mad`, `baseline_span` |
| Harmonic | `harmonic_order`, `alias_family_size` |
| Stability | `uncertainty_ratio` |
| Information | `baseline_period_ratio`, `family_complexity` |
| Observability | `window_completeness` |
| Physics | `period_duration_consistency`, `chain_coherence`, `transit_spacing_regularity`, `transit_number_monotonicity` |
| Morphology | `depth_consistency`, `duration_consistency`, `shape_consistency` |

**Total admitted: 15 features across 7 families.**

---

## 4. Excluded Features Summary

| Feature | Reason for Exclusion |
| :--- | :--- |
| `ambiguity_score` | Stage 3 ranking residual — information leakage |
| `ambiguity_index` | Stage 3 ranking artifact |
| `confidence_score` | Stage 3 composite heuristic |
| `ranking_trace` | Stage 3 ranking artifact |
| `physics_score` | Neutralized ECHO ranking artifact |
| `information_content` | Stage 3 derived composite |
| `missing_transits` | Functional of `coverage_fraction` |
| `support_count` | Numerator of `coverage_fraction` |
| `residual_rms` | Redundant with `residual_mad` |
| `normalized_mad` | = `residual_mad / P`; no additional information |
| `normalized_rms` | = `residual_rms / P`; no additional information |
| `event_density` | = `n_events / baseline_span`; functional of admitted features |
| `observable_transits` | Component of `window_completeness` |
| `hidden_transits` | Component of `window_completeness` |
| `occurrence_log_prior` | Prior quantity — must not be treated as evidence |

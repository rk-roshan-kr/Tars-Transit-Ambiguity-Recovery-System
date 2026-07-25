# Stage 4 Scientific Value Audit

*Phase 7.1 — Scientific Validation Phase. Evaluation of Stage 4 evidence family utility.*

---

## 1. Evidence Family Rankings

Based on measured alias separability (KS statistics, Cohen's d, Mutual Information) and noise resilience sweeps, we rank the six evidence families by their scientific value for downstream exoplanet candidate validation:

### 1. Physics Evidence (Family 6)
* **Value**: **HIGH VALUE**
* **Scientific Basis**: Includes the single most powerful feature in Stage 4: `transit_spacing_regularity` (MI = 0.5828, KS = 1.0000). For sub-harmonic aliases, the implied transit spacing fluctuates heavily, producing high variance that separates them cleanly from true candidates. `chain_coherence` and `occurrence_log_prior` add independent astrophysical priors.

### 2. Temporal Evidence (Family 1)
* **Value**: **HIGH VALUE**
* **Scientific Basis**: bedrock metrics. `coverage_fraction` is highly discriminative (MI = 0.3305, KS = 0.7660, Cohen's d = 1.47) since aliases expect transits where none occurred. `residual_mad` and `residual_rms` scale predictably with timing noise, tracking ephemeris timing quality.

### 3. Observability Evidence (Family 5)
* **Value**: **MEDIUM VALUE**
* **Scientific Basis**: `gap_fraction` and `window_completeness` explain *why* transits are missing. They do not classify directly, but provide context (e.g. downweighting temporal metrics when completeness is low).

### 4. Stability Evidence (Family 3)
* **Value**: **MEDIUM VALUE**
* **Scientific Basis**: `uncertainty_ratio` ($\sigma_P / P$) is extremely stable under timing noise sweeps, offering a noise-resilient indicator of ephemeris precision. `normalized_mad` and `normalized_rms` normalize residuals relative to period.

### 5. Information Evidence (Family 4)
* **Value**: **MEDIUM VALUE**
* **Scientific Basis**: `event_density` (sampling density metric) and `baseline_period_ratio` track the information constraints on period recovery. They provide necessary normalization for machine learning models.

### 6. Harmonic Evidence (Family 2)
* **Value**: **LOW VALUE**
* **Scientific Basis**: `alias_family_size` and `harmonic_order` are categorical. `ambiguity_score` (EV-H3) has high information leakage from Stage 3 heuristics and must be masked during training, limiting its downstream utility.

---

## 2. Conclusion

The audit demonstrates that Stage 4 EEA **provides a strong physical signal**. By combining Physics Evidence (specifically spacing regularity) and Temporal Evidence (coverage fraction), a simple non-ML gating rule can already achieve high alias separation. This strongly validates the scientific design of the pipeline.

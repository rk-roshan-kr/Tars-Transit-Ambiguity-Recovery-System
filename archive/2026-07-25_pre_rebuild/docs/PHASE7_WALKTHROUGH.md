# Stage 4 Evidence Evaluation Architecture (EEA) Implementation Walkthrough

This document serves as the authoritative scientific and technical record of the Stage 4 EEA implementation (Phase 7).

---

## 1. Objectives & Scientific Role

Stage 3 produces an **admissible candidate family** of periodic signals. 
Stage 4 (EEA) converts this candidate family into a **structured multi-dimensional evidence space**.

### Core Architecture Rules (FROZEN)
* **Measurement Only**: Stage 4 produces evidence vectors; it does not filter, weight, or re-rank candidates.
* **No Rejections**: Every candidate delivered by Stage 3 must be represented in Stage 4 output.
* **Graceful Degradation**: Physics-derived features that require stellar metadata default to `None` (never `0.0` or `nan`) when metadata is absent.

---

## 2. Naming Conflict Resolution

To avoid technical debt and name collisions:
* The Stage 2 event-level morphological coherence report (formerly `EEAReport` in `models.py`) is renamed to `MorphologicalCoherenceReport`.
* The field `eea` in `PhysicsReport` is renamed to `morphological_coherence`.
* The name `EEA` is reserved exclusively for the Stage 4 Candidate-level Evidence Evaluation Architecture.

---

## 3. Evidence Taxonomy (27 Features across 6 Families)

Every candidate receives a complete `EvidenceVector` containing all 27 features:

1. **Family 1 — Temporal Evidence** (6 features): `support_count`, `coverage_fraction`, `baseline_span`, `missing_transits`, `residual_rms`, `residual_mad`.
2. **Family 2 — Harmonic Evidence** (4 features): `harmonic_order`, `alias_family_size`, `ambiguity_score` (redefined as `candidate_score - nearest_alias_score`), `alias_density`.
3. **Family 3 — Stability Evidence** (3 features): `normalized_mad`, `normalized_rms`, `uncertainty_ratio` (period-relative ephemeris stability).
4. **Family 4 — Information Evidence** (4 features): `n_events`, `baseline_period_ratio`, `event_density` (redefined conceptually as a sampling density metric), `family_complexity`.
5. **Family 5 — Observability Evidence** (4 features): `observable_transits`, `hidden_transits`, `window_completeness`, `gap_fraction` (gaps calculated dynamically).
6. **Family 6 — Physics Evidence** (6 features): `period_duration_consistency` (optional, defaults to `None`), `kepler_plausibility` (optional, defaults to `None`), `chain_coherence`, `occurrence_log_prior`, `transit_spacing_regularity`, `transit_number_monotonicity`.

---

## 4. Pre-Implementation Refinements & User Feedback

Four crucial refinements were implemented based on review feedback before freezing Phase 7:
1. **EV-H3 Redefined**: Changed from family-level margin to candidate-specific margin: `candidate_score - nearest_alias_score`.
2. **Uncertainty-Aware Alias Check**: Alias family detection now propagates period uncertainties and checks whether the period difference is within `harmonic_tolerance_sigma_multiplier` $\times$ $\sigma_D$ where $\sigma_D = \sqrt{\sigma_{P_j}^2 + K^2 \cdot \sigma_{P_i}^2}$.
3. **Sampling Density Metric**: Changed wording from "information-theoretic proxy" to "sampling density metric" for event density.
4. **HEEA-3 Correlation Correction**: Shannon entropy (family ambiguity) is mathematically expected to correlate positively with `gap_fraction` (more gaps $\rightarrow$ more ambiguity $\rightarrow$ higher entropy).

---

## 5. Verification Results

### Unit Tests
All 38 unit tests run and pass successfully:
* Stage 1, 2, 3 regression checks: PASS
* Stage 4 EEA end-to-end extraction, validators, and warnings checks: PASS
* Naming changes check: PASS

### Verification Experiments
All 6 validation scripts under `research/` run successfully and produce CSV files in `results/`:
1. `run_eea_feature_distribution.py` $\rightarrow$ `results/eea_feature_distribution.csv`
2. `run_eea_alias_separation.py` $\rightarrow$ `results/eea_alias_separation.csv`
3. `run_eea_gap_resilience.py` $\rightarrow$ `results/eea_gap_resilience.csv`
4. `run_eea_noise_resilience.py` $\rightarrow$ `results/eea_noise_resilience.csv`
5. `run_eea_information_content.py` $\rightarrow$ `results/eea_information_content.csv`
6. `run_eea_ambiguity_quantification.py` $\rightarrow$ `results/eea_ambiguity_quantification.csv`

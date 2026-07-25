# Evidence Registry

*Phase 7 — Stage 4 EEA. All 27 evidence features frozen. No modifications permitted after Phase 7.1 begins.*

---

## Registry Rules

1. Every evidence feature must have a unique EV-ID.
2. Every feature must have a formula or computable definition.
3. Every feature must have a stated source (what data it requires).
4. No feature may be a weighted combination of other features.
5. Physics features that require stellar metadata must declare their fallback (always `None`).

---

## Evidence Family 1 — Temporal Evidence

Measures timing consistency of the candidate ephemeris against the observed events.

| EV-ID | Feature | Formula / Definition | Source | Units |
| :--- | :--- | :--- | :--- | :--- |
| EV-T1 | `support_count` | N events satisfying \|r_k\| < tolerance | Stage 3 forensics | count |
| EV-T2 | `coverage_fraction` | N_matched / N_expected [EQ-S3-05] | Stage 3 forensics | [0, 1] |
| EV-T3 | `baseline_span` | t_max − t_min across all events | Stage 2 events | days |
| EV-T4 | `missing_transits` | N_expected − N_matched | Stage 3 forensics | count |
| EV-T5 | `residual_rms` | √(Σr_k² / N) [EQ-S3-03] | Stage 3 forensics | days |
| EV-T6 | `residual_mad` | median(\|r_k − median(r)\|) [EQ-S3-04] | Stage 3 forensics | days |

**Consumer note**: Residuals are in days (native units). Stage 5 must convert to minutes if needed for display. Stage 4 never converts units.

---

## Evidence Family 2 — Harmonic Evidence

Describes the alias structure surrounding a candidate period.

| EV-ID | Feature | Formula / Definition | Source | Units |
| :--- | :--- | :--- | :--- | :--- |
| EV-H1 | `harmonic_order` | Integer ratio K such that P_candidate = P_primary / K | Harmonic resolver | integer |
| EV-H2 | `alias_family_size` | N candidates sharing the same harmonic cluster | Stage 3 candidates | count |
| EV-H3 | `ambiguity_score` | Score(top_1) − Score(top_2) from Stage 3 ranking trace | Stage 3 ranking trace | [0, ∞) |
| EV-H4 | `alias_density` | N candidates within harmonic_tolerance_sigma_multiplier × σ_P | Stage 3 harmonic clusters | count |

**Note**: EV-H3 `ambiguity_score` uses the Stage 3 heuristic score margin — it measures how ambiguous the current ranking is, not how ambiguous the evidence is. ECHO will compute its own evidence-based ambiguity.

---

## Evidence Family 3 — Stability Evidence

Period-relative ephemeris stability metrics using the Phase 6.1 normalization.

| EV-ID | Feature | Formula / Definition | Source | Units |
| :--- | :--- | :--- | :--- | :--- |
| EV-S1 | `normalized_mad` | MAD_r / P_candidate (fractional) | Stage 3 forensics + period | dimensionless |
| EV-S2 | `normalized_rms` | RMS_r / P_candidate (fractional) | Stage 3 forensics + period | dimensionless |
| EV-S3 | `uncertainty_ratio` | σ_P / P_candidate | Stage 3 WLS uncertainty | dimensionless |

**Formula source**: Phase 6.1 `PERIOD_RELATIVE_STABILITY_SPEC.md` — effective normalization uses min(fractional, absolute_floor / P).

---

## Evidence Family 4 — Information Evidence

Characterizes the information content available for period determination.

| EV-ID | Feature | Formula / Definition | Source | Units |
| :--- | :--- | :--- | :--- | :--- |
| EV-I1 | `n_events` | Total Stage 2 events delivered to Stage 3 | Stage 2 transfer | count |
| EV-I2 | `baseline_period_ratio` | baseline_span / P_candidate | Computed | dimensionless |
| EV-I3 | `event_density` | n_events / baseline_span | Computed | events/day |
| EV-I4 | `family_complexity` | N candidates in full Stage 3 output | Stage 3 output | count |

> [!IMPORTANT]
> EV-I3 is **`event_density`** (events per day of baseline). It is NOT `identifiability_score` (rejected — derived from Phase 5.2 experiments, not a raw measurement) and NOT `gap_fraction` (rejected — duplicates EV-O4 in Observability family).
>
> `gap_fraction` lives **exclusively** in the Observability family (EV-O4).

---

## Evidence Family 5 — Observability Evidence

Gap-aware observational window characterization.

| EV-ID | Feature | Formula / Definition | Source | Units |
| :--- | :--- | :--- | :--- | :--- |
| EV-O1 | `observable_transits` | N transits of period P falling inside observation windows | Observation window model | count |
| EV-O2 | `hidden_transits` | N transits of period P falling inside gap windows | Gap model | count |
| EV-O3 | `window_completeness` | EV-O1 / (EV-O1 + EV-O2) | Computed | [0, 1] |
| EV-O4 | `gap_fraction` | Total gap duration / baseline_span | Light curve | [0, 1] |

---

## Evidence Family 6 — Physics Evidence

Orbital mechanics and astrophysical prior measurements. **Measurement only** — no candidate rejection, no ranking.

| EV-ID | Feature | Formula / Definition | Source | Requires Stellar | Fallback |
| :--- | :--- | :--- | :--- | :---: | :--- |
| EV-P1 | `period_duration_consistency` | D_cons(P) from PF-02 | `STAGE3_PHYSICS_FEATURE_REGISTRY.md` | YES | `None` |
| EV-P2 | `kepler_plausibility` | K₃(P) from PF-01 | `STAGE3_PHYSICS_FEATURE_REGISTRY.md` | YES | `None` |
| EV-P3 | `chain_coherence` | Φ_chain(P) = 1 − N_breaks/(N_events−1) [PF-07] | Events + period | NO | — |
| EV-P4 | `occurrence_log_prior` | log(p_occ(P)) = −0.7 × log(P) + const [PF-03, Fressin 2013] | Period | NO | — |
| EV-P5 | `transit_spacing_regularity` | Var((t_{k+1} − t_k) / P) over consecutive events | Events + period | NO | — |
| EV-P6 | `transit_number_monotonicity` | Fraction of consecutive event pairs where n_{k+1} > n_k | Events + period | NO | — |

> [!CAUTION]
> EV-P1 and EV-P2 must return `None` when `StellarMetadata` is absent or when `stellar_mass_solar` / `stellar_radius_solar` is `None`. The physics extractor must emit a `WARNING_STELLAR_METADATA_ABSENT` flag in these cases.
>
> **NEVER substitute `0.0` or `nan`. Always use `None`.**

---

## Feature Count Summary

| Family | Count | Requires Stellar? |
| :--- | :---: | :---: |
| Temporal | 6 | No |
| Harmonic | 4 | No |
| Stability | 3 | No |
| Information | 4 | No |
| Observability | 4 | No |
| Physics | 6 (4 always, 2 conditional) | 2 of 6 |
| **Total** | **27** | **2 conditional** |

---

## Version

Frozen: Phase 7 implementation freeze.
Revision requires: User approval + new Phase designation.

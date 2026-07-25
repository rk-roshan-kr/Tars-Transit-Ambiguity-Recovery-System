# EEA Failure Modes

*Phase 7 — Stage 4 EEA. All failure modes are non-fatal: Stage 4 never terminates a candidate. Failures produce warnings and partial evidence only.*

---

## Handling Rule

All failures emit a string warning code into `CandidateEvidenceReport.warnings`. No failure may:
- Remove a candidate from the output
- Set a required (non-Optional) field to `None`, `0.0`, or `nan`
- Raise an unhandled exception (except `EvidenceComputationError` for truly unrecoverable cases)

---

## F-EEA-01: Insufficient Events

**Condition**: `n_events < 2`

**Behavior**:
- All temporal evidence features are computed from available events (may be a single event).
- `coverage_fraction` is computed but is expected to be unreliable.
- Emit: `WARNING_SPARSE`

**Impact**: Most temporal and stability features will be degenerate (e.g., MAD of a single residual is 0). This is not an error — it is a measurement of an under-constrained system. Stage 5 must handle sparse vectors.

**Scientific note**: The Phase 5.2 identifiability study confirms N=2 is the minimum for stable recovery. N=1 evidence vectors represent Class A generator failures (Stage 3 found no valid family).

---

## F-EEA-02: Extreme Harmonic Density

**Condition**: `alias_density > EEA_CONFIG["warning_high_alias_density"]` (default: 10)

**Behavior**:
- All harmonic evidence is computed normally.
- `ambiguity_index` is expected to be near 1.0 (fully degenerate).
- Emit: `WARNING_HIGH_ALIAS_DENSITY`

**Impact**: Highly degenerate alias families indicate very short baselines or periods near harmonic multiples of the observation cadence. Stage 5 may flag these for special treatment.

---

## F-EEA-03: Observation Window Collapse

**Condition**: `window_completeness < 0.1`

**Behavior**:
- All observability evidence is computed normally.
- Emit: `WARNING_WINDOW_COLLAPSE`

**Impact**: Less than 10% of expected transits occur inside observable windows. Period recovery from this candidate is information-theoretically very difficult. Stage 5 should weight this candidate's temporal evidence accordingly.

---

## F-EEA-04: Evidence Contradiction

**Condition**: `physics_evidence.chain_coherence < 0.3` AND `temporal_evidence.coverage_fraction > 0.8`

**Behavior**:
- All evidence is computed normally.
- Emit: `WARNING_EVIDENCE_CONTRADICTION`

**Impact**: A high-coverage candidate with low chain coherence suggests the ephemeris matches many events but their transit number sequence is inconsistent. This is a strong alias indicator. Stage 5 or Stage 6 may use this flag for discriminative reasoning.

**Rule**: Stage 4 NEVER rejects based on this contradiction. It only flags it.

---

## F-EEA-05: Low Information Content

**Condition**: `EvidenceFamilySummary.information_content < threshold` (to be calibrated from `run_eea_information_content.py` experiment)

**Behavior**:
- Emit: `WARNING_LOW_INFORMATION_CONTENT` on the `EvidenceFamilySummary`

**Impact**: A near-zero information content means all candidates in the family have essentially identical scores — the family is fully degenerate. Stage 5 may decline to reason over such families and escalate to Stage 6 ML.

> [!NOTE]
> F-EEA-05 was previously stated as "identifiability_score < 0.3." **Replaced.** `information_content` is a computable Shannon entropy over the family — a Stage 4 measurement. `identifiability_score` was a derived conclusion from Phase 5.2 experiments and does not belong in Stage 4.

---

## F-EEA-06: Stellar Metadata Absent

**Condition**: `stellar: Optional[StellarMetadata]` is `None`, or `stellar.stellar_mass_solar` / `stellar.stellar_radius_solar` is `None`

**Behavior**:
- `PhysicsEvidence.period_duration_consistency` = `None`
- `PhysicsEvidence.kepler_plausibility` = `None`
- Emit: `WARNING_STELLAR_METADATA_ABSENT`

**Rule**: NEVER substitute `0.0` or `nan`. Only `None`.

**Impact**: EV-P1 and EV-P2 are unavailable. The 4 remaining physics features (EV-P3 through EV-P6) are still computed. Stage 6 ML must handle `None` physics features via imputation or masking — never by treating them as zero.

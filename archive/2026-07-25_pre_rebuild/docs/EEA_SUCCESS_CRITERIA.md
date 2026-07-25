# EEA Success Criteria

*Phase 7 — Frozen. These are the pre-registered acceptance criteria for Phase 7.1 implementation.*

---

## Evaluation Rules

1. Every criterion must be measurable from CSV artifacts or import-time checks.
2. No criterion may require ranking or classification performance (those belong to Stage 5/6).
3. All criteria must be verifiable without real TESS data.

---

## SC-EEA-1: Complete Coverage

**Criterion**: Every candidate in the Stage 3 output receives a complete `CandidateEvidenceReport`.

**Measurement**: Run Phase 5.3 orchestrator with EEA attached. Count `len(evidence_reports)` vs `len(stage3_candidates)`.

**Pass threshold**: 100% — not 99%, not 99.9%. Every candidate must be measured.

**Failure action**: If any candidate is missing, it is a defect in `eea_engine.py`, not an expected failure mode.

---

## SC-EEA-2: Sparse Evidence Computability

**Criterion**: Evidence is computable for N_events ∈ [2, 20] without raising an unhandled exception.

**Measurement**: Run `run_eea_information_content.py` which sweeps N ∈ [2, 20] across 100 trials each. No trial may raise `EvidenceComputationError`.

**Pass threshold**: 0 exceptions across all 1,900 trials.

**Note**: Warnings (F-EEA-01 etc.) are expected and permitted. Exceptions are not.

---

## SC-EEA-3: Alias Family Measurability

**Criterion**: `ambiguity_index` is computable for ≥95% of multi-candidate families (families with ≥2 candidates).

**Measurement**: Run `run_eea_ambiguity_quantification.py`. Count trials where `ambiguity_index` is successfully computed vs total trials.

**Pass threshold**: ≥95% success rate across all tested populations.

---

## SC-EEA-4: Deterministic Reproducibility

**Criterion**: Identical inputs → identical `EvidenceVector` outputs across 1,000 repeated calls.

**Measurement**: Embedded in the Phase 7.1 verification step. Call `EEAEngine.evaluate()` 1,000 times with the same fixed input and compare all fields using `==`.

**Pass threshold**: 0 differences across all 1,000 repetitions and all 27 features.

---

## SC-EEA-5: Zero Ranking Logic

**Criterion**: No weight multiplication, no `sort()`, no `sorted()`, no `argsort()`, no score assignment exists in any file under `tarscore/stage4_eea/`.

**Measurement**: Static analysis — grep the package for `sort`, `argsort`, `weight`, `score =`, `rank`.

**Pass threshold**: 0 matches in production code (test code excluded).

---

## SC-EEA-6: ECHO Interface Compatibility

**Criterion**: All `EvidenceVector` instances pass type-checking as valid inputs for the future Stage 5 ECHO interface.

**Measurement**: At Phase 7.1 completion, verify that every field of `EvidenceVector` has a defined type and that `frozen=True` prevents mutation. Run `dataclasses.fields()` check on all 27 features.

**Pass threshold**: All fields present with correct types. No `Any`-typed required fields.

---

## SC-EEA-7: Feature Measurement Completeness

**Criterion**: ≥95% of evidence features are non-`None` for targets in the identifiable regime (N_events ≥ 4 and gap_fraction < 0.5).

**Measurement**: Run `run_eea_feature_distribution.py` on the Phase 5.3 realistic population. For each candidate in the identifiable regime, count non-None features / 27.

**Pass threshold**: Mean completeness ≥ 95% in the identifiable regime.

**Note**: `EV-P1` and `EV-P2` are expected `None` when stellar metadata is not provided. SC-EEA-7 is evaluated with stellar metadata absent (the default case). With stellar metadata present, the pass threshold applies to all 27 features.

---

## Criteria Not Included (and Why)

| Excluded Criterion | Reason |
| :--- | :--- |
| ROC AUC > 0.6 for alias separation | Stage 5/6 concern, not Stage 4 |
| Top-1 Recall improvement | Stage 3/6 metric, not Stage 4 |
| `identifiability_score` computable | Feature removed — it was a Stage 5 conclusion |
| `overall_quality` in acceptable range | Field removed — requires weighting |

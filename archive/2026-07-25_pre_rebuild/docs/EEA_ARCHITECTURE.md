# EEA Architecture Specification

*Phase 7 — Frozen. This document is the definitive architectural reference for `tarscore/stage4_eea/`.*

---

## Position in Pipeline

```
Stage 2 → TransitEvent[]
Stage 3 → PeriodRecoveryReport (PeriodCandidate[] + PeriodForensics)
Stage 4 → CandidateEvidenceReport[] + EvidenceFamilySummary
Stage 5 → (ECHO — Phase 8)
Stage 6 → (Bayesian + ML — Phase 9)
```

Stage 4 receives Stage 3's output and optional `StellarMetadata`. It returns one `CandidateEvidenceReport` per candidate plus one `EvidenceFamilySummary` for the whole family.

---

## Internal Pipeline

```
PeriodRecoveryReport
    │
    ├── alternative_solutions + top_solution → candidate list
    │
    └── audit_trail (PeriodForensics)
            │
            ▼
    ┌─────────────────────────────────────────────────────────────┐
    │  EEAEngine.evaluate()                                       │
    │                                                             │
    │  For each PeriodCandidate:                                  │
    │                                                             │
    │    TemporalEvidenceExtractor   → TemporalEvidence           │
    │    HarmonicEvidenceExtractor   → HarmonicEvidence           │
    │    StabilityEvidenceExtractor  → StabilityEvidence          │
    │    InformationEvidenceExtractor→ InformationEvidence        │
    │    ObservabilityEvidenceExtractor→ ObservabilityEvidence    │
    │    PhysicsEvidenceExtractor    → PhysicsEvidence            │
    │                                                             │
    │    EvidenceValidator           → schema + range checks      │
    │    EvidenceVectorBuilder       → EvidenceVector             │
    │    CandidateEvidenceReportBuilder → CandidateEvidenceReport │
    │                                                             │
    │  EvidenceFamilySummaryBuilder  → EvidenceFamilySummary      │
    └─────────────────────────────────────────────────────────────┘
```

---

## Architectural Invariants (FROZEN)

**INV-EEA-1: No rejection.** No extractor, validator, or builder may eliminate a candidate from the output list. Every candidate in the input must appear in the output.

**INV-EEA-2: No ranking.** No module may sort, score, or assign priority to candidates. The output list order must match the input list order exactly.

**INV-EEA-3: No weights.** No module may multiply any evidence feature by a scalar weight or combine features into an aggregate score. `EvidenceFamilySummary.information_content` is a Shannon entropy calculation — not a weighted sum.

**INV-EEA-4: Complete coverage.** Every candidate must receive a complete `EvidenceVector`. If any feature cannot be computed, it must be flagged `None` (for Optional features) or raise `EvidenceComputationError` (for required features).

**INV-EEA-5: Determinism.** The EEA engine must be a pure function of its inputs. No random state, no global mutable state, no timestamp-dependent behavior.

**INV-EEA-6: Independence.** Evidence extractors are called independently per candidate. No extractor may read another candidate's evidence during extraction.

---

## Module Responsibilities

### `eea_engine.py` — Master Orchestrator

```python
class EEAEngine:
    def evaluate(
        self,
        report: PeriodRecoveryReport,
        lc: ConditionedLightCurve,
        events: List[TransitEvent],
        stellar: Optional[StellarMetadata] = None,
    ) -> Tuple[List[CandidateEvidenceReport], EvidenceFamilySummary]:
```

Responsibilities:
- Assemble the candidate list from `report.top_solution` + `report.alternative_solutions`
- Call all six extractors per candidate
- Call `EvidenceValidator`
- Assemble `EvidenceVector` and `CandidateEvidenceReport`
- Assemble `EvidenceFamilySummary`

### `temporal_evidence.py`

Input: `PeriodCandidate`, `PeriodForensics`
Output: `TemporalEvidence`
EV features: EV-T1 through EV-T6

### `harmonic_evidence.py`

Input: `PeriodCandidate`, `PeriodForensics`, full candidate list
Output: `HarmonicEvidence`
EV features: EV-H1 through EV-H4

### `stability_evidence.py`

Input: `PeriodCandidate`, `PeriodForensics`
Output: `StabilityEvidence`
EV features: EV-S1 through EV-S3
Formula source: `PERIOD_RELATIVE_STABILITY_SPEC.md`

### `information_evidence.py`

Input: `PeriodCandidate`, `ConditionedLightCurve`, full candidate list
Output: `InformationEvidence`
EV features: EV-I1 through EV-I4
Note: `event_density` = n_events / baseline_span (events/day)

### `observability_evidence.py`

Input: `PeriodCandidate`, `ConditionedLightCurve`
Output: `ObservabilityEvidence`
EV features: EV-O1 through EV-O4
Uses: `ObservationWindow` model from `observation_window.py`

### `physics_evidence.py`

Input: `PeriodCandidate`, `List[TransitEvent]`, `Optional[StellarMetadata]`
Output: `PhysicsEvidence`
EV features: EV-P1 through EV-P6
EV-P1, EV-P2: `None` when stellar metadata absent → emit `WARNING_STELLAR_METADATA_ABSENT`

### `evidence_validators.py`

Validates each `EvidenceVector` against:
- Range constraints (e.g., coverage_fraction ∈ [0, 1])
- Non-negative constraints (e.g., support_count ≥ 0)
- Finiteness checks (no inf, no nan permitted for non-Optional fields)

### `evidence_report.py`

Builds `CandidateEvidenceReport` from a validated `EvidenceVector`.
Builds `EvidenceFamilySummary` from all `CandidateEvidenceReport` instances.
`information_content` = Shannon entropy H = −Σ p_i log(p_i) over normalized ambiguity scores.

### `evidence_registry.py`

Maps each EV-ID string (e.g., `"EV-T1"`) to its extractor function and field path. Used by validation scripts to programmatically enumerate all 27 features.

### `config.py`

Contains validation range constraints only. No scoring weights. No ranking thresholds.

```python
EEA_CONFIG = {
    "coverage_range": (0.0, 1.0),
    "ambiguity_range": (0.0, 1.0),
    "normalized_mad_max": 1.0,     # Hard ceiling: MAD cannot exceed the period itself
    "chain_coherence_range": (0.0, 1.0),
    "warning_sparse_n_events": 2,   # Emit WARNING_SPARSE below this
    "warning_high_alias_density": 10,
}
```

---

## Data Flow Diagram

```
PeriodRecoveryReport.audit_trail.residual_vectors[P]
    → TemporalEvidenceExtractor → EV-T5, EV-T6

PeriodRecoveryReport.audit_trail.support_vectors[P]
    → TemporalEvidenceExtractor → EV-T1, EV-T4

PeriodRecoveryReport.top_solution.coverage_fraction
    → TemporalEvidenceExtractor → EV-T2

max(event.event_time) - min(event.event_time)
    → TemporalEvidenceExtractor → EV-T3
    → InformationEvidenceExtractor → EV-I3 (event_density denominator)

PeriodRecoveryReport.audit_trail.harmonic_clusters
    → HarmonicEvidenceExtractor → EV-H1, EV-H2, EV-H4

PeriodRecoveryReport.audit_trail.ranking_trace
    → HarmonicEvidenceExtractor → EV-H3 (score margin)

WLS epoch + residuals + period
    → StabilityEvidenceExtractor → EV-S1, EV-S2, EV-S3

ConditionedLightCurve.quality_flags
    → ObservabilityEvidenceExtractor → EV-O1, EV-O2, EV-O3, EV-O4
    → InformationEvidenceExtractor → EV-I3 (baseline_span numerator)

StellarMetadata (optional)
    → PhysicsEvidenceExtractor → EV-P1, EV-P2 (or None)

List[TransitEvent] + PeriodCandidate
    → PhysicsEvidenceExtractor → EV-P3, EV-P4, EV-P5, EV-P6
```

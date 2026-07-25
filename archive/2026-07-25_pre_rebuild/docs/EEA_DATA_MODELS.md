# EEA Data Models

*Phase 7 — Stage 4. Documents all data structures introduced or modified by Stage 4. Authoritative source for Stage 5 (ECHO) interface design.*

---

## Source of Truth

All types defined here are implemented in `tarscore/models.py`. This document exists for human readability and Stage 5 interface planning. If this document and `models.py` ever conflict, `models.py` is authoritative.

---

## Modified Types

### `MorphologicalCoherenceReport` (formerly `EEAReport`)

Previously named `EEAReport`. Renamed in Phase 7 to prevent collision with Stage 4 EEA terminology.

```python
@dataclass(slots=True)
class MorphologicalCoherenceReport:
    coherence_score: float           # C_coh ∈ [0, 1]
    depth_consistency: float
    duration_consistency: float
    shape_consistency: float
    cross_correlation: float
    decision: DecisionState
```

**Location**: Stage 2 output, attached to `PhysicsReport`.

### `PhysicsReport`

Field renamed: `eea` → `morphological_coherence`.

```python
@dataclass(slots=True)
class PhysicsReport:
    morphological_coherence: MorphologicalCoherenceReport   # was: eea: EEAReport
    echo: ECHOReport
    physics_passed: bool
    physics_score: float
```

---

## New Types (Stage 4)

### `StellarMetadata`

Optional stellar context for physics evidence extraction.

```python
@dataclass(frozen=True)
class StellarMetadata:
    stellar_mass_solar: Optional[float]      # M* / M_sun
    stellar_radius_solar: Optional[float]    # R* / R_sun
    stellar_teff: Optional[float]            # Effective temperature (K)
    stellar_logg: Optional[float]            # log surface gravity (cgs)
    stellar_metallicity: Optional[float]     # [Fe/H] (dex)
    source: Optional[str]                    # Provenance: 'TIC', 'GAIA-DR3', 'ESTIMATED'
```

**Rules**:
- All fields `Optional[float]` — never `0.0`, never `nan` for absent data.
- When `source` is `None`, all other fields must also be `None`.

---

### `TemporalEvidence` (EV-T1 through EV-T6)

```python
@dataclass(frozen=True)
class TemporalEvidence:
    support_count: int               # EV-T1
    coverage_fraction: float         # EV-T2 ∈ [0, 1]
    baseline_span: float             # EV-T3 (days)
    missing_transits: int            # EV-T4 ≥ 0
    residual_rms: float              # EV-T5 (days) ≥ 0
    residual_mad: float              # EV-T6 (days) ≥ 0
```

---

### `HarmonicEvidence` (EV-H1 through EV-H4)

```python
@dataclass(frozen=True)
class HarmonicEvidence:
    harmonic_order: int              # EV-H1 ≥ 1 (1 = fundamental)
    alias_family_size: int           # EV-H2 ≥ 1
    ambiguity_score: float           # EV-H3 ≥ 0 (score margin from Stage 3 ranking)
    alias_density: int               # EV-H4 ≥ 0
```

---

### `StabilityEvidence` (EV-S1 through EV-S3)

```python
@dataclass(frozen=True)
class StabilityEvidence:
    normalized_mad: float            # EV-S1 ≥ 0 (MAD/P)
    normalized_rms: float            # EV-S2 ≥ 0 (RMS/P)
    uncertainty_ratio: float         # EV-S3 ≥ 0 (σ_P/P)
```

---

### `InformationEvidence` (EV-I1 through EV-I4)

```python
@dataclass(frozen=True)
class InformationEvidence:
    n_events: int                    # EV-I1 ≥ 0
    baseline_period_ratio: float     # EV-I2 ≥ 0
    event_density: float             # EV-I3 ≥ 0 (events/day)
    family_complexity: int           # EV-I4 ≥ 1
```

---

### `ObservabilityEvidence` (EV-O1 through EV-O4)

```python
@dataclass(frozen=True)
class ObservabilityEvidence:
    observable_transits: int         # EV-O1 ≥ 0
    hidden_transits: int             # EV-O2 ≥ 0
    window_completeness: float       # EV-O3 ∈ [0, 1]
    gap_fraction: float              # EV-O4 ∈ [0, 1]
```

---

### `PhysicsEvidence` (EV-P1 through EV-P6)

```python
@dataclass(frozen=True)
class PhysicsEvidence:
    period_duration_consistency: Optional[float]   # EV-P1 ∈ [0, 1] or None
    kepler_plausibility: Optional[float]           # EV-P2 ∈ {0, 1} or None
    chain_coherence: float                         # EV-P3 ∈ [0, 1]
    occurrence_log_prior: float                    # EV-P4 ≤ 0 (log probability)
    transit_spacing_regularity: float              # EV-P5 ≥ 0 (variance)
    transit_number_monotonicity: float             # EV-P6 ∈ [0, 1]
```

---

### `EvidenceVector`

Complete 27-feature evidence representation for one `PeriodCandidate`.

```python
@dataclass(frozen=True)
class EvidenceVector:
    candidate_id: str
    period_days: float
    temporal: TemporalEvidence
    harmonic: HarmonicEvidence
    stability: StabilityEvidence
    information: InformationEvidence
    observability: ObservabilityEvidence
    physics: PhysicsEvidence
```

**Invariant**: `candidate_id` must match the `PeriodCandidate.candidate_id` it was computed from. `period_days` must match `PeriodCandidate.period_days` exactly.

---

### `CandidateEvidenceReport`

Stage 4 output for a single candidate.

```python
@dataclass(slots=True)
class CandidateEvidenceReport:
    candidate: PeriodCandidate
    evidence_vector: EvidenceVector
    warnings: List[str]              # F-EEA-0x warning codes
    diagnostics: Mapping[str, Any]   # Raw intermediate values
```

---

### `EvidenceFamilySummary`

Family-level aggregate summary.

```python
@dataclass(frozen=True)
class EvidenceFamilySummary:
    family_size: int
    ambiguity_index: float           # ∈ [0, 1]: 0 = unambiguous, 1 = fully degenerate
    information_content: float       # Shannon entropy H in nats
```

> [!IMPORTANT]
> `overall_quality` was considered and **deliberately rejected**. Any aggregate quality metric requires weighting multiple evidence families — which violates INV-EEA-3. The three retained fields (`family_size`, `ambiguity_index`, `information_content`) are objective measurements that require no weighting.

---

## Stage 5 Interface Contract

Stage 5 (ECHO, Phase 8) receives `List[CandidateEvidenceReport]` and `EvidenceFamilySummary`. It must not access `PeriodForensics` directly. All raw Stage 3 information must be accessed through the evidence vector.

Stage 6 (Phase 9) receives the same types and additionally trains on `EvidenceVector` instances where `PeriodCandidate.candidate_id` maps to a known ground-truth label from Phase 5.3 artifacts.

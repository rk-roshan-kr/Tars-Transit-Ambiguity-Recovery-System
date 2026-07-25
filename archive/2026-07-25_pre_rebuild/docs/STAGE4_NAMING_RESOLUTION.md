# Stage 4 Naming Resolution

*Phase 7 — Frozen. Documents the naming decisions for Stage 4 packages and types.*

---

## The Conflict

Before Phase 7, the TARS codebase contained:

| Name | Location | What It Was |
| :--- | :--- | :--- |
| `EEAReport` | `models.py:196` | Stage 2 event-level morphological coherence (depth, shape, symmetry) |
| `stage4_physics/` | `tarscore/stage4_physics/` | Empty placeholder for a future physics layer |

Phase 7 introduces Stage 4 as the **Evidence Evaluation Architecture (EEA)** — a period-level, candidate-level evidence measurement system. Using "EEA" for Stage 2 morphology would have caused an irreversible naming disaster by Phase 8.

---

## Resolutions (FROZEN)

### 1. `EEAReport` → `MorphologicalCoherenceReport`

The old `EEAReport` in `models.py` is renamed to `MorphologicalCoherenceReport`.

**Reason**: It measures event-level morphological coherence — depth consistency, shape consistency, cross-correlation of transit profiles. This is Stage 2 evidence, not Stage 4 evidence. The name now correctly describes what it measures.

**Rule**: The string "EEA" may never be used for Stage 2 concepts again.

### 2. `PhysicsReport.eea` → `PhysicsReport.morphological_coherence`

The field in `PhysicsReport` that previously held an `EEAReport` is renamed to `morphological_coherence` and now holds a `MorphologicalCoherenceReport`.

### 3. `stage4_eea/` is the Stage 4 package

The new `tarscore/stage4_eea/` package contains the Evidence Evaluation Architecture implementation.

The existing `tarscore/stage4_physics/` directory is retained as an empty placeholder. It is reserved for any future pure-physics layer that may be introduced between Stage 4 EEA and Stage 5 ECHO. It is NOT the current Stage 4.

---

## Architecture Identity Table (FROZEN)

| Stage | Package | Primary Output | Purpose |
| :---: | :--- | :--- | :--- |
| 2 | `stage2_detection/` | `TransitEvent[]` + `MorphologicalCoherenceReport` | Event detection + morphology |
| 3 | `stage3_period_recovery/` | `PeriodRecoveryReport` | Candidate family generation |
| 4 | `stage4_eea/` | `CandidateEvidenceReport[]` + `EvidenceFamilySummary` | Evidence measurement |
| 5 | `stage5_statistical/` (future Stage 5 ECHO) | TBD | Geometric + physics reasoning |
| 6 | `stage6_ml/` (future Stage 6) | TBD | Bayesian + ML ranking |

> [!CAUTION]
> Do not use `stage4_physics/` for the EEA implementation. It is a reserved placeholder only.
> Do not use `stage5_statistical/` for ECHO until Phase 8 formally defines its interface.

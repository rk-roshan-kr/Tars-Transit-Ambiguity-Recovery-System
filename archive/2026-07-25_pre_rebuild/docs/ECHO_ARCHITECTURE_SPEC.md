# ECHO Architecture Specification

This document defines and freezes the scientific and architectural specification for Stage 5 ECHO (Exoplanet Candidate Heuristic Observer).

---

## 1. Pipeline Position & Interfaces

Stage 5 ECHO consumes the structured measurements from Stage 4 EEA and the raw event/stellar diagnostics, interpreting them to evaluate physical plausibility and find contradictions.

### Inputs
Stage 5 ECHO consumes:
- `List[CandidateEvidenceReport]` (Stage 4 output)
- `EvidenceFamilySummary` (Stage 4 output)
- `List[TransitEvent]` (Stage 2 output, referenced via `supporting_event_ids`)
- `Optional[StellarMetadata]`

No downstream module may access:
- `confidence_score` (Stage 3 ranking leakage)
- `ranking_trace`
- `ambiguity_score`
- `ambiguity_index`
- `information_content`

### Outputs
- `List[PhysicsReport]` (one per candidate)
- `ECHOReport` (embedded in `PhysicsReport`)

---

## 2. Architectural Invariants

- **INV-ECHO-1: No Candidate Deletion**: ECHO must process every candidate. No candidate may be filtered, deleted, or skipped. The output list must preserve the exact size and candidate elements of the input list.
- **INV-ECHO-2: No Reordering or Sorting**: ECHO must preserve the candidate order exactly as received from Stage 4. No sorting, ranking, or ordering is permitted.
- **INV-ECHO-3: No Heuristic Score Weighting**: ECHO must never multiply evidence features by scalar weights or combine features into an overall aggregate numeric score.
- **INV-ECHO-4: Boundedness**: All confidence/coherence scores calculated within the morphology or geometry sub-components must be strictly bounded in $[0, 1]$ or map to `None`.
- **INV-ECHO-5: Determinism**: ECHO must be a pure, side-effect-free function of its inputs. No random state, no system clock, and no global mutable state.
- **INV-ECHO-6: Missing Metadata Safety**: Missing stellar metadata must never raise exceptions. It must degrade gracefully by setting geometry evidence to `UNKNOWN`, generating a warning, and returning a decision of `UNKNOWN`.
- **SC-ECHO-8: Explanation Isolation**: Explanation generation may consume warnings, contradictions, decisions, and evidence values, but it is strictly prohibited from accessing Stage 3 heuristics (such as `confidence_score`, `ranking_trace`, `ambiguity_score`, or `ambiguity_index`) to prevent accidental heuristic ranking leakage in natural language outputs.

---

## 3. Allowed Vetting Decisions

Vetting decisions assigned by ECHO are restricted to:
- `PASS`: Strong physical consistency, consistent geometry, zero contradictions, and zero warnings.
- `WARN`: Physical plausibility but mild consistency degradation, or warning flags.
- `UNKNOWN`: Insufficient information (e.g. missing stellar metadata, sparse event support $N < 3$, or unknown morphology).
- `CONTRADICTED`: Highly regular timings but major physical/geometric contradictions or impossible transit geometry.

---

## 4. Prohibited Constructs

ECHO is strictly forbidden from executing or containing:
- `sort()`, `sorted()`, `argsort()` on the candidate list.
- Linear combinations or weighted averages to compute candidate quality or overall physics score.
- Vetoes that remove candidates from the pipeline.
- `physics_score` computations that combine morphology and geometry numerically (replaces old composite scores).

---

## 5. Architectural Risks & Conditions (Phase 8 Freeze)

As approved in the Phase 8 transition, the following risk mitigations and structural conditions are frozen into the architecture:

- **Condition A (Risk A): Cross-Correlation Classification**:
  Since Stage 2 raw transit cutout alignment profile storage is not guaranteed for every candidate, the `cross_correlation` metric (`X_coh`) is classified as an **OPTIONAL FEATURE**, not a **CORE FEATURE**, inside ECHO. When profile cutouts are unavailable, `X_coh` must gracefully fall back to `None` with a corresponding `WARNING_PROFILE_UNAVAILABLE` tag rather than blocking execution.

- **Condition B (Risk B): Threshold Interpretation**:
  The vetting thresholds used by the contradiction and geometry reasoning engines (such as the `0.5`, `0.7`, `0.8`, and `0.3` boundaries) are derived from physical principles and signal propagation models. Consequently, ECHO documentation and downstream users must explicitly classify these Version 1 thresholds as **physics-motivated priors**, rather than **empirically optimized or statistically optimal thresholds** calibrated against Kepler, TOI, or EB populations.

- **Condition C (Risk C): Coherence Metric Fusion Rule**:
  Because morphological coherence metrics ($C_{\text{coh}}$, $T_{\text{coh}}$, $S_{\text{coh}}$) are naturally correlated due to common systematic influences (e.g., poor event extraction affecting all three metrics simultaneously), they must not be fused using a linear weighted sum. Instead, a strict rule-based classification logic must determine the `overall_morphology_state`:
  - **STRONG**: if at least two metrics are $\ge 0.7$
  - **WEAK**: if at least two metrics are $< 0.5$
  - **MODERATE**: in all other cases.

# ECHO Decision Truth Table

This document defines the deterministic mapping from ECHO evidence states to the candidate decision state (`PASS`, `WARN`, `UNKNOWN`, `CONTRADICTED`).

---

## Decision Priority

Decisions are evaluated in order of priority:
1. **CONTRADICTED**: If any direct physical contradiction is detected, or if transit geometry is physically impossible.
2. **UNKNOWN**: If there is insufficient information to reach a verdict (e.g. missing stellar metadata, too few events, degenerate morphology).
3. **WARN**: If the candidate is physically plausible but shows mild consistency degradation or warning flags.
4. **PASS**: If the candidate exhibits strong morphology, consistent geometry, and zero warnings or contradictions.

---

## Decision Table

| Transit Geometry Consistency | Morphology State | Contradictions Count | Other Warnings | Decision |
| :--- | :--- | :---: | :--- | :---: |
| `IMPLAUSIBLE` | Any | Any | Any | `CONTRADICTED` |
| Any | Any | $\ge 1$ | Any | `CONTRADICTED` |
| `UNKNOWN` | Any | 0 | Any | `UNKNOWN` |
| `PLAUSIBLE` | `UNKNOWN` | 0 | Any | `UNKNOWN` |
| `PLAUSIBLE` | Any | 0 | `WARNING_SPARSE` (Support < 3) | `UNKNOWN` |
| `PLAUSIBLE` | `WEAK` | 0 | Any | `WARN` |
| `PLAUSIBLE` | `MODERATE` | 0 | Any | `WARN` |
| `PLAUSIBLE` | `STRONG` | 0 | `WARNING_STELLAR_METADATA_ABSENT` | `UNKNOWN` |
| `PLAUSIBLE` | `STRONG` | 0 | Any other warning | `WARN` |
| `PLAUSIBLE` | `STRONG` | 0 | None | `PASS` |

---

## Variable Definitions

### Transit Geometry Consistency
- `IMPLAUSIBLE`: If $T_{\text{obs}} \ge P$ or $T_{\text{obs}} \le 0$ or depth $D \le 0$ or depth $D \ge 1.0$.
- `UNKNOWN`: If stellar metadata is missing, preventing expected duration or density calculations.
- `PLAUSIBLE`: Otherwise.

### Morphology State
The overall morphology state is determined from individual consistency metrics (depth, duration, and shape consistency) using rule-based logic (Condition C):
- `STRONG`: If at least two metrics are $\ge 0.7$.
- `WEAK`: If at least two metrics are $< 0.5$.
- `MODERATE`: Otherwise.
- `UNKNOWN`: Fewer than 2 events, or no morphology metadata.

### Contradictions
List of contradictions detected by the contradiction engine:
- `CONTRADICTION_GEOMETRY_TEMPORAL`: High coverage fraction but inconsistent duration plausibility.
- `CONTRADICTION_MORPHOLOGY_PHYSICS`: Regular spacing but weak morphology coherence.
- `CONTRADICTION_OBSERVABILITY`: Strong temporal evidence but poor window completeness.
- Any other specific contradictions registered in `docs/ECHO_CONTRADICTION_REGISTRY.md`.

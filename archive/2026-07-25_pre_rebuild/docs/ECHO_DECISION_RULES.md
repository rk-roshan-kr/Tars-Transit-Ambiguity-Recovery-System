# ECHO Decision Rules

This document records the exact, frozen vetting decision logic rules for Stage 5 ECHO.

---

## Allowed Vetting Decisions
Decisions are restricted to the following four states:
- **PASS**: Strong physical consistency, consistent geometry, zero contradictions, and zero warnings.
- **WARN**: Physical plausibility but mild consistency degradation, or warning flags.
- **UNKNOWN**: Insufficient information (e.g. missing stellar metadata, sparse event support $N < 3$, or unknown morphology).
- **CONTRADICTED**: Highly regular timings but major physical/geometric contradictions or impossible transit geometry.

---

## Decision Priority & Mapping

The decision state is assigned using the following order of priority:

1. **CONTRADICTED**:
   - If transit geometry is physically impossible: `transit_geometry_consistency == "IMPLAUSIBLE"` (e.g., $T_{\text{obs}} \ge P$, $T_{\text{obs}} \le 0$, depth $D \le 0$ or $D \ge 1.0$).
   - OR if 1 or more contradictions are detected (e.g. `CONTRADICTION_GEOMETRY_TEMPORAL`, `CONTRADICTION_MORPHOLOGY_PHYSICS`, `CONTRADICTION_OBSERVABILITY`).

2. **UNKNOWN**:
   - If not CONTRADICTED, and:
     - `transit_geometry_consistency == "UNKNOWN"` (due to missing stellar metadata)
     - OR `overall_morphology_state == "UNKNOWN"`
     - OR if sparse observation warning `WARNING_SPARSE` is present (support count $N < 3$)
     - OR if `WARNING_STELLAR_METADATA_ABSENT` is present.

3. **WARN**:
   - If not CONTRADICTED or UNKNOWN, and:
     - `overall_morphology_state` is `WEAK` or `MODERATE`
     - OR `duration_plausibility` is `INCONSISTENT`
     - OR `stellar_density_consistency` is `INCONSISTENT`.

4. **PASS**:
   - If not CONTRADICTED, UNKNOWN, or WARN:
     - `overall_morphology_state` is `STRONG`
     - `transit_geometry_consistency` is `PLAUSIBLE`
     - `duration_plausibility` is `CONSISTENT`
     - `stellar_density_consistency` is `CONSISTENT`
     - `contradictions` list is empty
     - No warning flags.

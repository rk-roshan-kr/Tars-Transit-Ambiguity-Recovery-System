# STAGE 2 FREEZE CERTIFICATE
**Component:** Stage 2 Transit Event Detection (TARS Core)
**Audit Version:** 1.0 (Phase 3.1)
**Status:** 🔒 FROZEN

## Certification Statement
The Stage 2 detector architecture, encompassing local noise estimation, event significance scanning, contiguous morphology extraction, and baseline physical filtering, has been scientifically audited and mathematically verified.

This certificate guarantees that the Stage 2 detection methodology operates consistently, deterministically, and stably across the parameter space outlined below.

## Immutable Components
The following elements are permanently locked and may not be altered:
- **EQ-S2-01 to EQ-S2-06**: Scientific equations defining significance, depth, duration, area, symmetry, and sharpness.
- **Local MAD Noise Estimation**: The statistical foundation for estimating `sigma_local`.
- **Event Builder Logic**: The algorithm grouping contiguous cadences exceeding significance bounds.

## Stage 2 Scientific Invariants (S2-1 to S2-5)
The following regression tests form the permanent boundaries of the Stage 2 component:

1. **S2-1**: Gaussian FEPLC remains bounded under pure white noise conditions.
2. **S2-2**: Detection recall decreases monotonically as the significance threshold increases.
3. **S2-3**: False candidate count decreases monotonically as the significance threshold increases.
4. **S2-4**: The detector operates fully deterministically. The exact same `ConditionedLightCurve` yields byte-for-byte identical `TransitEvent` records over infinite trials.
5. **S2-5**: Processing runtime remains strictly bounded to `O(N)` scaling relative to cadence count.

## Permitted Evolutions
While the Stage 2 algorithms are frozen, the following external interfaces may be modified:
- Expansion of the `sigma_threshold` configuration for different missions.
- Fine-tuning of the experimental heuristic `H-S2-01` (event scoring) as directed by Stage 3 (Period Recovery).
- Modification of downstream logging, analytics, and diagnostics visualization.

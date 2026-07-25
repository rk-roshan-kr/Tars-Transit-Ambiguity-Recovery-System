# Stage 2 Traceability Matrix

This matrix maps every Stage 2 equation to its implementation function and corresponding unit test. Use this document to verify that the codebase and equation registry are synchronized.

---

| Equation | Formula (short) | Source Function | File | Unit Test | Invariant ID |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **EQ-S2-01** | $S_i = (1 - f_i) / \sigma_{\text{local},i}$ | `scan_significance()` | `stage2_detection/detector.py` | `test_clean_injection_detected` | INV-S2-01 |
| **EQ-S2-02** | $D = 1 - \min(f_i)$ | `extract_morphology()` | `stage2_detection/morphology.py` | `test_morphology_symmetry_range` | INV-S2-05 |
| **EQ-S2-03** | $T = t_{\text{end}} - t_{\text{start}}$ | `extract_morphology()` | `stage2_detection/morphology.py` | `test_morphology_symmetry_range` | INV-S2-05 |
| **EQ-S2-04** | $A = \int \max(0, 1-f)\, dt$ (trapz) | `extract_morphology()` | `stage2_detection/morphology.py` | `test_morphology_symmetry_range` | INV-S2-05 |
| **EQ-S2-05** | $\text{sym} = 1 - \|A_\text{in} - A_\text{eg}\| / (A_\text{in} + A_\text{eg})$ | `extract_morphology()` | `stage2_detection/morphology.py` | `test_morphology_symmetry_range` | INV-S2-05 |
| **EQ-S2-06** | $\text{sharp} = D / \overline{(1-f_i)}$ | `extract_morphology()` | `stage2_detection/morphology.py` | `test_polarity_only_dips` | INV-S2-04 |

---

## Physics Labelling Rules (not equations — threshold-based)

| Rule | Condition | Label Assigned | Source Function | File |
| :--- | :--- | :--- | :--- | :--- |
| Polarity | `depth ≤ 0` | `NON_TRANSIT` | `apply_physics_labels()` | `stage2_detection/physics_filters.py` |
| Duration (min) | `duration < 20 min` | `NON_TRANSIT` | `apply_physics_labels()` | `stage2_detection/physics_filters.py` |
| Duration (max) | `duration > 24 hr` | `NON_TRANSIT` | `apply_physics_labels()` | `stage2_detection/physics_filters.py` |
| Sharpness | `sharpness > 3.0` | `UNCERTAIN` | `apply_physics_labels()` | `stage2_detection/physics_filters.py` |
| Default | passes all above | `TRANSIT_LIKE` | `apply_physics_labels()` | `stage2_detection/physics_filters.py` |

---

## Experimental Heuristic (not frozen)

| ID | Description | Source Function | File | Registry entry |
| :--- | :--- | :--- | :--- | :--- |
| **H-S2-01** | Composite event ranking score (weighted sum of normalized peak σ, duration preference, log-depth) | `score_events()` | `stage2_detection/scoring.py` | **Not in EQUATION_REGISTRY_STAGE2.md** — empirical, configurable |

---

## Full Audit Chain

```
ConditionedLightCurve.sigma_local  [EQ-S1-02 — frozen in Stage 1]
        │
        ▼ EQ-S2-01
CandidatePoint.significance
        │
        ▼ grouping algorithm
TransitEvent  {event_time, depth, snr, peak_significance, mean_significance}
        │
        ▼ EQ-S2-02 to EQ-S2-06
TransitEvent.morphology  {depth, duration, area, symmetry, sharpness,
                          ingress_duration, egress_duration}
        │
        ▼ physics rules
TransitEvent.physics_label  {TRANSIT_LIKE | UNCERTAIN | NON_TRANSIT}
        │
        ▼ H-S2-01  (experimental)
TransitEvent.event_score  [0, 1]
        │
        ▼
Stage 3 — Sparse Period Recovery
```

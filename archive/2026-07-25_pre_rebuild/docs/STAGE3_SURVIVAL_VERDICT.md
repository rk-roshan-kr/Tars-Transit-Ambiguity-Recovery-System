# Stage 3 Architecture Survival Verdict

*Phase 5.4 — Component H. Selects one of four possible verdicts based on all Phase 5.4 audit documents. This verdict determines whether Phase 6 is Optimization or Architectural Evolution.*

---

## Evidence Summary

The following evidence informs the verdict:

| Source | Finding |
| :--- | :--- |
| `TARS_STAGE3_ORIGINAL_VISION.md` | Original vision is clear, scientifically motivated, and falsifiable. |
| `VISION_TO_CODE_TRACEABILITY.md` | 6 of 25 vision elements are NOT_IMPLEMENTED. 6 are PARTIALLY_IMPLEMENTED. |
| `ARCHITECTURE_IMPLEMENTATION_GAP.md` | 5 of 7 components have documented gaps between design intent and code. |
| `STAGE3_FAILURE_ROOT_CAUSE_ANALYSIS.md` | Dominant failure class (26%) is Stage 2 upstream — not a Stage 3 defect at all. |
| `MISSING_NOVELTY_AUDIT.md` | 6 major novelty items are fully missing from code. |
| `PHYSICS_CONSTRAINED_ML_AUDIT.md` | Paper title claim is ~35% accurate. ML layer does not yet exist. |
| `MEASUREMENT_TRUST_AUDIT.md` | 88% of metrics are HIGH_TRUST or MEDIUM_TRUST. No metrics are INVALID. |
| `PHASE5_3_WALKTHROUGH.md` | Family Recall = 70.7%. Generator Failure = 2.4%. Transfer Efficiency = 68%. |

---

## The Verdict

### VERDICT B: Architecture Incomplete — Novelty Missing — Requires Extension

> **The core mathematical architecture of Stage 3 is scientifically sound and correctly implemented at the generation layer. However, the novelty claimed in the paper title is substantially incomplete. The implementation has not yet realized the full original vision.**

---

## Justification

### Why Not Verdict A (Architecture Valid, Implementation Needs Revision)?

Verdict A implies the architecture is complete and only the code needs bug fixes. This is partially true — the ranking layer does have fixable bugs (epoch selection, absolute stability threshold, weight calibration). However, the deeper issue is that **six major novelty elements exist only in documentation**. The physics-constrained ML layer, Bayesian evidence accumulation, multi-planet separation, TTV handling, orbital architecture constraints, and the ML ranking model are not "implementation bugs" — they are **missing architectural components** that would require significant engineering work to add. Verdict A would understate the gap.

### Why Not Verdict C (Architecture Fundamentally Flawed, Major Redesign)?

Verdict C would be appropriate if the **generator itself** were broken — if the interval algebra were mathematically wrong, or if the interval-space approach were fundamentally incapable of solving the sparse period recovery problem. The evidence does not support this. The generator failure rate is only 2.4%. When Stage 2 delivers enough events, Stage 3 correctly places the true period in the candidate family 70.7% of the time under realistic conditions. The mathematical foundation is correct. Verdict C would be incorrect.

### Why Not Verdict D (Insufficient Evidence)?

We have 9 diagnostic sweeps, 2 independent validation populations, and a full failure root cause analysis. The evidence is substantial and self-consistent across both seeds. The measurements are MEDIUM-to-HIGH trust. The evidence is sufficient for a verdict.

---

## Specific Findings That Determine the Verdict

1. **The generation layer is the genuine scientific contribution.** Event-space period recovery via pairwise interval algebra is a correct, novel, and efficiently computable approach to the sparse regime problem.

2. **The ranking layer is a placeholder.** The consensus ranker (H-S3-01) uses hand-tuned weights with no physical or statistical justification. It is the primary source of Class B failures (8.9%) and must be replaced with a trained or physics-derived scoring model.

3. **The dominant failure is Stage 2 upstream loss (26.1%).** Improving Stage 3 alone cannot fix this. A significant improvement requires Stage 2 recall improvement, especially in the low-SNR regime (SNR < 7.1).

4. **The paper title claim is premature.** "Physics-Constrained Machine Learning" requires both physics constraints in the scoring layer and an ML model in the ranking layer. Neither exists. The title should be revised or the missing components should be implemented before submission.

5. **The architecture is extensible, not broken.** All 6 missing novelty items are additive extensions — they can be implemented on top of the existing foundation without rewriting the generation pipeline.

---

## Implication for Phase 6

Based on Verdict B, Phase 6 is:

### Architectural Evolution (Targeted)

Not a full redesign. Not pure optimization.

The following are the ordered Phase 6 priorities:

1. **Fix Class III Implementation Defects** (quick wins):
   - Fix epoch selection (remove hardcoded `min(event_time)` epoch).
   - Make stability threshold period-relative.
   - Implement harmonic tie-breaking rules from `HARMONIC_RESOLUTION_SPECIFICATION.md`.
   - Remove support score saturation at 5 events.

2. **Build ML Ranking Layer** (core novelty extension):
   - Generate labeled training data from Phase 5.3.
   - Train a binary classifier (TRUE vs ALIAS).
   - Replace H-S3-01 with the learned model.
   - Validate on held-out population.

3. **Add Physics Features to Ranker** (novelty claim):
   - Implement Kepler's third law consistency check.
   - Add occurrence rate prior.
   - Add resonance flag.

4. **Conduct Real TESS Validation** (credibility):
   - Query MAST for 20–50 confirmed TOIs.
   - Run the full LC → Stage1 → Stage2 → Stage3 pipeline.
   - Report real-world Family Recall.

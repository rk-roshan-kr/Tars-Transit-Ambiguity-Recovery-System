# Stage 3 Final Blueprint

*Phase 5.5 — Component I. The single authoritative document for Stage 3. Supersedes all prior roadmap discussions. Sources: All Phase 5.1–5.5 documents.*

---

## 1. What Stage 3 Is Today

Stage 3 is a **deterministic event-space sparse period recovery engine** that:
- Accepts a list of transit event timestamps from Stage 2.
- Generates an admissible family of period hypotheses via pairwise interval algebra.
- Filters candidates by timing residual stability and observational coverage.
- Sorts the candidate family using an uncalibrated heuristic linear blend (H-S3-01).
- Returns a ranked `PeriodCandidate[]` with per-candidate forensics.

**What it is NOT today**:
- Not a machine learning system.
- Not a physics-constrained scoring system.
- Not a Bayesian inference engine.
- Not validated on real TESS targets.
- Not benchmarked against BLS or TLS.

---

## 2. What Stage 3 Was Intended to Be

Stage 3 was designed as a **physics-constrained Bayesian period reasoning system** that:
- Reconstructs admissible orbital architectures from incomplete observational evidence.
- Uses physical priors (occurrence rates, Kepler dynamics) to constrain candidate scoring.
- Employs a trained ML classifier to discriminate true periods from harmonic aliases.
- Handles multi-planet systems via iterative residual decomposition.
- Provides calibrated posterior probabilities over the candidate family.
- Is validated against confirmed TESS exoplanets.

---

## 3. What Is Missing

| Missing Component | Phase 5.4 Source | Priority |
| :--- | :--- | :---: |
| Epoch phase-fitting (replaces `min(t)`) | ARCHITECTURE_IMPLEMENTATION_GAP.md | CRITICAL |
| Period-relative stability threshold | ARCHITECTURE_IMPLEMENTATION_GAP.md | CRITICAL |
| Harmonic tie-breaking rules | HARMONIC_RESOLUTION_SPECIFICATION.md | HIGH |
| Support score unbounded (remove saturation at 5) | ARCHITECTURE_IMPLEMENTATION_GAP.md | HIGH |
| Occurrence rate prior (PF-03) | STAGE3_PHYSICS_FEATURE_REGISTRY.md | HIGH |
| Event chain coherence score (PF-07) | STAGE3_PHYSICS_FEATURE_REGISTRY.md | HIGH |
| Kepler consistency gate (PF-01) | STAGE3_PHYSICS_FEATURE_REGISTRY.md | MEDIUM |
| Bayesian log-posterior scoring | STAGE3_RANKING_REPLACEMENT.md | MEDIUM |
| ML Ranking Layer | STAGE3_ML_TRAINING_BLUEPRINT.md | MEDIUM |
| Real TESS validation | STAGE3_PUBLICATION_READINESS.md | HIGH |
| BLS/TLS benchmark | BENCHMARK_PROTOCOL.md | HIGH |

---

## 4. What Is Scientifically Justified

The following are scientifically justified claims — backed by reproducible artifacts:

1. **The event-space domain is the correct computational choice** for the sparse-transit TESS regime. Justified by: algorithmic complexity analysis ($O(N_{events}^2)$ vs $O(N_{cadences} \cdot N_{freqs})$) and Phase 5.2 diagnostic studies.

2. **The interval algebra generates the correct period hypothesis** in 97.6% of cases when ≥2 events are available. Justified by: Phase 5.2 Generator Failure rate = 2.4%.

3. **The dominant failure driver is Stage 2 upstream information loss**, not Stage 3 generator deficiency. Justified by: Phase 5.3 Class C failure = 26.1% (failures due to < 2 events delivered).

4. **Harmonic alias identification works at 98.1% accuracy** in controlled conditions. Justified by: Phase 5.2 Harmonic Confusion Matrix.

5. **Period uncertainty estimates are correctly calibrated** (1σ = 70.8%, 2σ = 94.6%) when mode selection is correct. Justified by: Phase 5.2 Uncertainty Calibration (filtered).

6. **The identifiability boundary is N≥2** for 50% recovery and **N≥4** for stable recovery in moderate-gap regimes. Justified by: Phase 5.2 Identifiability Boundary study.

---

## 5. What Must Be Implemented Next

**Phase 6A — Implementation Defect Fixes** (no architectural decisions):
```
1. Fix epoch selection in recoverer.py
2. Make stability_threshold period-relative in config.py
3. Implement harmonic tie-breaking in harmonic_resolver.py
4. Remove support score saturation in consensus_ranker.py
```

**Phase 6B — Bayesian Scoring + Physics Features**:
```
5. Add occurrence rate prior (PF-03) to interval generator
6. Implement Bayesian log-posterior in a new scoring module
7. Add event chain coherence score (PF-07)
8. Replace H-S3-01 with Bayesian base score
```

**Phase 6C — ML Layer**:
```
9. Build MLTD-S3 from Phase 5.3 CSV artifacts
10. Train binary classifier (logistic regression baseline)
11. Train gradient-boosted model (production)
12. Replace H-S3-01 with hybrid Bayesian + ML score
```

**Phase 6D — Real TESS Validation and Benchmarks**:
```
13. Query MAST for 50-100 confirmed TESS TOIs
14. Run full LC → Stage1 → Stage2 → Stage3 pipeline
15. Execute BLS benchmark (astropy.timeseries)
16. Execute TLS benchmark (transitleastsquares library)
17. Report comparative recall metrics
```

---

## 6. What Must Never Be Claimed

The following claims may not appear in any paper, presentation, or summary until explicitly resolved:

| Forbidden Claim | Why Forbidden | Resolution Required |
| :--- | :--- | :--- |
| "Physics-Constrained ML Pipeline" (verbatim) | Neither physics-constrained scoring nor ML exist | Implement Phase 6B + 6C |
| "Validated on TESS data" | No real TESS targets tested | Execute Phase 6D |
| "Outperforms BLS/TLS" | No comparative benchmark exists | Execute Phase 6D |
| "High-precision detection" (as comparative claim) | No comparison context | Execute Phase 6D |
| "Multi-planet handling" | 100% contamination for non-integer ratios | Implement decomposition |
| "TTV-robust" | 72.6% failure at 60-min TTV | Implement non-linear ephemeris |
| "Production-ready" | Ranking heuristic is uncalibrated | At minimum Phase 6A required |

---

## 7. What Can Be Published Now

A workshop or methods paper may claim the following with full supporting artifacts:

```
1. Event-space sparse period recovery framework for short-baseline TESS data.
2. Admissible period family semantics for sparse, ambiguous transit timing.
3. Empirical identifiability boundary characterization (N_{events} ≥ 2 for 50%, ≥ 4 for stability).
4. Alias failure mode taxonomy (gap-induced, harmonic, information-theoretic).
5. Synthetic population validation suite with pre-registered success criteria.
6. Open-source implementation with full forensics trail and SHA256 provenance.
```

---

## 8. What Requires Future Validation

```
- Real TESS target validation (Phase 6D)
- BLS/TLS comparative benchmark (Phase 6D)
- ML ranking model training and test evaluation (Phase 6C)
- Physics-constrained scoring validation (Phase 6B)
- Multi-planet contamination mitigation (Post-Phase 6)
- TTV-aware non-linear ephemeris (Post-Phase 6)
```

---

## Authoritative Architecture Sequence

This is the frozen recommended implementation sequence. Any deviation requires explicit approval:

```
Phase 6A: Fix 4 implementation defects           → Eliminates Class B failures
Phase 6B: Bayesian scoring + 2 physics features  → Makes physics claim defensible
Phase 6C: ML training + GBT model               → Makes ML claim defensible
Phase 6D: Real TESS + BLS/TLS benchmarks         → Makes publication viable
```

No code claiming "Phase 6 complete" may be written until all four phases are executed and validated by the same artifact-backed protocol used in Phases 5.2–5.4.

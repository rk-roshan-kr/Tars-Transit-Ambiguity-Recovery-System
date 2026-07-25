# Vision-to-Code Traceability Matrix

*Phase 5.4 — Component B. Audits every major vision element against documentation, implementation, and experiment coverage.*

---

## Traceability Table

| Vision Element | Exists In Docs | Exists In Code | Exists In Experiments | Status |
| :--- | :---: | :---: | :---: | :--- |
| **Event-Space Period Recovery** | YES | YES | YES | `IMPLEMENTED` |
| **Admissible Period Family Generation** | YES | YES | YES | `IMPLEMENTED` |
| **Pairwise Interval Algebra (EQ-S3-01)** | YES | YES | YES | `IMPLEMENTED` |
| **O-C Timing Residual Computation (EQ-S3-02)** | YES | YES | YES | `IMPLEMENTED` |
| **Residual MAD Stability (EQ-S3-04)** | YES | YES | YES | `IMPLEMENTED` |
| **Coverage Fraction (EQ-S3-05)** | YES | YES | YES | `IMPLEMENTED` |
| **Harmonic Alias Detection (2P, P/2, 3P)** | YES | YES | YES | `IMPLEMENTED` |
| **Observation Window Gap Awareness** | YES | YES | PARTIAL | `PARTIALLY_IMPLEMENTED` |
| **Harmonic Ambiguity Flag** | YES | YES | YES | `IMPLEMENTED` |
| **Consensus Ranking Heuristic (H-S3-01)** | YES | YES | YES | `IMPLEMENTED` |
| **PeriodForensics Audit Trail** | YES | YES | NO | `PARTIALLY_IMPLEMENTED` |
| **Physics-Constrained Candidate Scoring** | YES | NO | NO | `NOT_IMPLEMENTED` |
| **Bayesian Evidence Accumulation** | YES (partial) | NO | NO | `NOT_IMPLEMENTED` |
| **Multi-Planet Signal Separation** | YES | NO | PARTIAL | `NOT_IMPLEMENTED` |
| **TTV Robustness (Beyond Linear Ephemeris)** | YES | NO | YES | `NOT_IMPLEMENTED` |
| **Orbital Architecture Constraints** | YES (docs) | NO | NO | `NOT_IMPLEMENTED` |
| **Event Chain Reconstruction** | YES | PARTIAL | YES | `PARTIALLY_IMPLEMENTED` |
| **Physics-Aware Scoring (not just heuristic)** | YES | NO | NO | `NOT_IMPLEMENTED` |
| **Uncertainty Propagation from Stage 2** | YES | PARTIAL | YES | `PARTIALLY_IMPLEMENTED` |
| **SNR-Weighted Event Trust** | YES | PARTIAL | YES | `PARTIALLY_IMPLEMENTED` |
| **False-Positive Event Suppression** | YES | NO | YES | `NOT_IMPLEMENTED` |
| **Sector Gap Boundary Awareness** | YES | PARTIAL | YES | `PARTIALLY_IMPLEMENTED` |
| **Per-Candidate Period Forensics** | YES | YES | NO | `PARTIALLY_IMPLEMENTED` |
| **ML-Optimized Ranking Layer** | YES | NO | NO | `NOT_IMPLEMENTED` |
| **Benchmark vs BLS/TLS** | YES | NO | NO | `NOT_IMPLEMENTED` |

---

## Critical Gap Summary

### NOT_IMPLEMENTED items (6)
These represent vision elements that exist only in documentation and have never entered the codebase:

1. **Physics-Constrained Candidate Scoring** — The paper title claims "physics-constrained ML." Current scoring is a pure phenomenological heuristic with three fixed weights. No physical orbital mechanics constrain candidate scoring.
2. **Bayesian Evidence Accumulation** — Mentioned in Phase 4 architecture documents as a target scoring framework. Never implemented. The current code uses a linear blend of phenomenological features, not a Bayesian posterior.
3. **Multi-Planet Signal Separation** — Phase 5.2 and 5.3 experiments demonstrated that this fails at 100% rate for non-integer period ratios. No code attempts to decompose multi-periodic event streams.
4. **TTV Robustness Beyond Linear Ephemeris** — The architecture documents acknowledge TTVs as a known class. The current implementation applies a strict linear $O-C$ model. TTV accommodation requires non-linear ephemeris fitting, which does not exist.
5. **Orbital Architecture Constraints** — The vision document states TARS should use "physics-constrained orbital architecture." No Keplerian constraints (e.g., period-radius-eccentricity relations, Hill stability) are applied.
6. **ML-Optimized Ranking Layer** — The Heuristic Registry explicitly declares H-S3-01 as *intended for future ML optimization*. No ML training loop, training data, or learning framework has been created.

### PARTIALLY_IMPLEMENTED items (6)
These represent vision elements that have code touching the concept, but the implementation is incomplete or diverges from the documented intent:

1. **Observation Window Gap Awareness** — The code identifies gaps via cadence spacing heuristics but does not use TESS sector boundary metadata. The gap detection is fragile for dense synthetic LCs.
2. **Event Chain Reconstruction** — The interval generator produces pairwise hypotheses, which is the mathematical foundation. However, the "chain" concept (linking events into multi-hop ephemeris trees) has not been implemented.
3. **SNR-Weighted Event Trust** — SNR enters only through `timing_uncertainty` estimation (`duration / SNR`). There is no per-event likelihood weighting in residual accumulation.
4. **Uncertainty Propagation** — Period uncertainty is computed from the covariance of the linear fit, but Stage 2 timing uncertainty is not formally propagated into Stage 3 as a prior.
5. **Sector Gap Boundary Awareness** — Covered by cadence-gap detection in `observation_window.py`, but the implementation does not specifically model TESS perigee patterns.
6. **Per-Candidate Period Forensics** — `forensics.py` exists and logs tested periods, residuals, rejections, and rankings. However, the forensics are never used to drive downstream decisions (they are currently read-only metadata).

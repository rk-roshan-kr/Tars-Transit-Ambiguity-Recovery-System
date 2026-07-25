# Physics-ML Title Traceability

*Phase 5.5 — Component C. Audits every significant word in the TARS paper title against current implementation evidence. Sources: PHYSICS_CONSTRAINED_ML_AUDIT.md, ARCHITECTURE_IMPLEMENTATION_GAP.md, stage3_period_recovery/ source files.*

---

## Paper Title Under Audit

> **"TARS Core: A Physics-Constrained Machine Learning Pipeline for High-Precision Exoplanet Detection in Short-Baseline TESS Data"**

---

## Word-by-Word Audit

### "TARS Core"
**Claim**: A named software system exists.
**Evidence**: `tarscore/` Python package exists. Installable. Documented.
**Status**: `IMPLEMENTED` ✓

---

### "A Pipeline"
**Claim**: A sequential processing pipeline exists from raw data to science output.
**Evidence**: LC → Stage 1 (detrending) → Stage 2 (event detection) → Stage 3 (period recovery) pipeline is implemented end-to-end in `recoverer.py`.
**Status**: `IMPLEMENTED` ✓

---

### "Physics-Constrained"

This is the most critical audit target.

**What "Physics-Constrained" requires**:
- Physics priors on candidate periods (e.g., Kepler's third law consistency, occurrence rate distributions).
- Orbital constraints that reject physically implausible solutions.
- Physical plausibility gates that cannot be bypassed by phenomenological statistics alone.

**Evidence in current code**:

| Physics Component | Present? | Evidence |
| :--- | :---: | :--- |
| Event-space domain (physics-motivated) | YES | Domain selection is physically justified. |
| Linear Keplerian ephemeris (O-C model) | YES | EQ-S3-02 implements Newtonian orbital mechanics. |
| Transit coverage geometry | YES | EQ-S3-05 encodes observational geometry. |
| Kepler's third law consistency gate | NO | Not implemented. |
| Occurrence rate prior | NO | Not implemented. |
| Stellar density consistency | NO | Not implemented. |
| Orbital stability constraints | NO | Not implemented. |
| Astrophysical plausibility rejection | NO | Not implemented. |

**Verdict**: `PARTIALLY_DEFENSIBLE`

Physics constrains the *mathematical domain* of Stage 3 (event-space, linear ephemeris), but does not constrain the *candidate scoring*. The consensus ranker can elevate a physically implausible period to Top-1 if its phenomenological statistics (coverage, stability, support) happen to be high. A referee specializing in orbital dynamics would immediately identify this gap.

**Defensibility path**: Add Kepler's third law consistency check as a scoring gate. This requires stellar mass/radius metadata during Stage 3 execution — currently absent from the pipeline.

---

### "Machine Learning"

**What "Machine Learning" requires**:
- A trained model with learned parameters.
- A training dataset.
- An inference step during production use.
- Validation of the learned model on held-out data.

**Evidence in current code**:

| ML Component | Present? | Evidence |
| :--- | :---: | :--- |
| Trained model | NO | No `.pkl`, `.pt`, `.joblib` file exists anywhere. |
| Learned parameters | NO | All weights (0.4, 0.4, 0.2) are hand-set constants. |
| Training dataset | NO | No labeled dataset of true/alias periods exists. |
| Inference step | NO | `consensus_ranker.py` is a formula, not inference. |
| Cross-validation | NO | No validation of the ranking model exists. |
| Feature engineering | PARTIAL | 6 candidate features exist; used in heuristic, not ML model. |

**Verdict**: `NOT_DEFENSIBLE`

There is no machine learning in Stage 3. A reviewer checking this claim would find a linear combination with fixed weights and correctly identify it as a hand-crafted heuristic. This is a factual inaccuracy in the paper title as written.

---

### "High-Precision"

**Claim**: TARS achieves high precision in period recovery.

**Evidence**:
- Phase 5.2 Uncertainty Calibration: $1\sigma$ coverage = 70.8% (near-perfect Gaussian behavior when mode recovery is correct).
- Phase 5.3 Top-1 Recall: 62.3% — not yet "high precision" by publication standards.
- No comparison against BLS/TLS precision exists.

**Verdict**: `CONDITIONALLY_DEFENSIBLE`

"High-precision" in the *uncertainty quantification* sense is defensible (calibrated $\sigma_P$ values). "High-precision" as a *comparative claim* against other methods is not defensible without BLS/TLS benchmarks.

---

### "Exoplanet Detection"

**Claim**: The pipeline detects exoplanets.

**Evidence**: The pipeline detects *period candidates consistent with transiting exoplanets*. It does not perform false positive discrimination, vetting, or confirmation. No real exoplanet has been recovered from actual TESS data in any Phase 5.x experiment.

**Verdict**: `CONDITIONALLY_DEFENSIBLE`

"Detection" must be qualified as *period candidate generation*, not confirmed detection. "Transit period candidate recovery" is more accurate.

---

### "Short-Baseline TESS Data"

**Claim**: Explicitly designed for short-baseline TESS observations.

**Evidence**: The 27-day sector baseline is the explicit design target documented in NOVELTY_POSITIONING_STAGE3.md. The simulation framework uses physically accurate TESS sector parameters.

**Verdict**: `IMPLEMENTED` ✓

---

## Overall Title Verdict

| Title Component | Status |
| :--- | :---: |
| TARS Core | `IMPLEMENTED` |
| A Pipeline | `IMPLEMENTED` |
| Physics-Constrained | `PARTIALLY_DEFENSIBLE` |
| Machine Learning | `NOT_DEFENSIBLE` |
| High-Precision | `CONDITIONALLY_DEFENSIBLE` |
| Exoplanet Detection | `CONDITIONALLY_DEFENSIBLE` |
| Short-Baseline TESS Data | `IMPLEMENTED` |

**Overall Title Defensibility: `PARTIALLY_DEFENSIBLE`**

The pipeline exists. The TESS target is correct. The physics motivations are real. But "Machine Learning" is factually absent, and "Physics-Constrained" is only partially realized. The title must be revised before submission.

---

## Recommended Title Revision

**For a Phase 6A submission (after implementation defect fixes)**:
> *"TARS: An Event-Space Sparse Period Recovery Framework for High-Gap TESS Exoplanet Candidate Detection"*

**For a Phase 6B submission (after ML layer built)**:
> *"TARS: A Machine Learning-Enhanced Event-Space Pipeline for Sparse Period Recovery in Short-Baseline TESS Data"*

**For a full Phase 6 submission (after physics scoring and real validation)**:
> *"TARS Core: A Physics-Constrained Machine Learning Pipeline for Sparse Period Recovery in Short-Baseline TESS Observations"*

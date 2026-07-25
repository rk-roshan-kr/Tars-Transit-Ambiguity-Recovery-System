# Physics-Constrained ML Audit

_Phase 5.4 — Component G. Evaluates the claim in the TARS paper title: "A Physics-Constrained Machine Learning Pipeline for High-Precision Exoplanet Detection in Short-Baseline TESS Data."_

---

## The Title Claim Under Review

```text
TARS Core: A Physics-Constrained Machine Learning Pipeline
for High-Precision Exoplanet Detection in Short-Baseline TESS Data
```

This audit will determine what portion of this claim is currently true, what portion is aspirational, and what would be required to make the full claim defensible.

---

## Where Is ML Currently Used?

**Answer: Nowhere in Stage 3.**

A complete audit of all Stage 3 source files:

| File                    | ML Component? | Notes                              |
| :---------------------- | :-----------: | :--------------------------------- |
| `interval_generator.py` |      NO       | Pure math: pairwise differences.   |
| `harmonic_resolver.py`  |      NO       | Clustering by absolute tolerance.  |
| `timing_residuals.py`   |      NO       | Linear algebra: O-C computation.   |
| `period_uncertainty.py` |      NO       | Weighted least squares.            |
| `observation_window.py` |      NO       | Deterministic coverage counting.   |
| `stability_engine.py`   |      NO       | Descriptive statistics (RMS, MAD). |
| `consensus_ranker.py`   |      NO       | Fixed-weight linear combination.   |
| `forensics.py`          |      NO       | Logging only.                      |
| `recoverer.py`          |      NO       | Pipeline orchestration.            |

**Result**: Stage 3 contains **zero ML components**. No trained model, no learned parameters, no inference step, no training loop, no training data. The "ML" claim in the paper title is not yet supported by the codebase.

---

## Where Is Physics Currently Used?

Physics enters Stage 3 through four narrow channels:

1. **Event-Space Domain Selection**: The decision to operate on event timestamps rather than flux arrays is physics-motivated — it exploits the physical fact that transit events are discrete, high-confidence signals.
2. **O-C Timing Model (EQ-S3-02)**: The linear ephemeris $r_k = t_k - (t_0 + n_k P)$ is a Newtonian orbital mechanics model (Keplerian motion = constant period, constant epoch).
3. **Coverage Fraction (EQ-S3-05)**: The concept of "expected transits in an observational window" encodes the physical geometry of transit probability.
4. **Harmonic Alias Identification**: The recognition that $P$, $2P$, $P/2$ are physically degenerate solutions is grounded in orbital mechanics.

**Result**: Physics enters at the level of _problem formulation and constraint identification_, but not at the level of _scoring or inference_. The physics-constraints stop at observation; they do not constrain the candidate selection.

---

## Where Are Constraints Enforced?

Current constraints in Stage 3:

1. **Stability Threshold**: Candidates are rejected if `MAD > stability_threshold`. This is a soft noise constraint, not a physics constraint.
2. **Coverage Threshold**: Candidates are rejected if `coverage_fraction < coverage_threshold`. This is a completeness constraint.
3. **Minimum Supporting Events**: Candidates require $N \geq 2$ supporting events. This is a data-sufficiency constraint.

**None of these are orbital physics constraints.** They do not enforce Keplerian dynamics, Hill stability, stellar mass consistency, or occurrence rate priors.

---

## Is Stage 3 Actually ML?

**No.** As documented above, Stage 3 is a deterministic algorithm with no learned parameters. It is an **expert-designed heuristic system** — a valuable and scientifically motivated one, but not ML in any standard sense.

---

## Is Stage 3 Currently a Heuristic System?

**Yes, partially.** Stage 3 is a hybrid:

- The **generation layer** (interval generator, harmonic resolver, timing residuals, uncertainty, coverage) is **deterministic mathematics** derived from physics.
- The **ranking layer** (consensus ranker) is a **phenomenological heuristic** with hand-tuned weights.

The generation layer is the genuine scientific contribution. The ranking layer is a placeholder.

---

## Current State vs Target State

| Dimension                | Current State                         | Target State                            | Gap                             |
| :----------------------- | :------------------------------------ | :-------------------------------------- | :------------------------------ |
| **ML Usage**             | None                                  | Trained ranker (logistic/GBT)           | No training data, no model      |
| **Physics Constraints**  | Minimal (domain selection, O-C model) | Full orbital prior + Kepler law scoring | No stellar metadata integration |
| **Candidate Scoring**    | Linear heuristic (H-S3-01)            | Physics-constrained Bayesian posterior  | No Bayesian framework           |
| **Multi-Planet**         | Not handled                           | Iterative residual decomposition        | No decomposition code           |
| **TTV Handling**         | Fails at 60 min                       | Non-linear ephemeris fit                | No TTV model                    |
| **Paper Title Accuracy** | 35% accurate                          | 100% accurate                           | Significant work remaining      |

---

## What Would Be Required to Make Stage 3 Genuinely Physics-Constrained ML?

A minimum viable path:

### Step 1: Build Training Data (1–2 weeks)

Use the Phase 5.3 dual-population datasets as a labeled training set. Label each candidate period as TRUE (within 1% of catalog period) or ALIAS. Extract the 6 candidate features (coverage, stability, support, residual_rms, residual_mad, n_support).

### Step 2: Train a Ranking Model (1–2 days)

Fit a binary classifier (logistic regression or gradient-boosted decision tree) to distinguish TRUE periods from ALIAS periods. Replace the hardcoded 0.4 / 0.4 / 0.2 weights with the learned model's output.

### Step 3: Add Physics Features (1 week)

Augment the candidate feature vector with physics-derived quantities:

- `period_stellar_consistency` (Kepler's third law: does $P$ imply a plausible semi-major axis given stellar mass?)
- `occurrence_rate_prior` (Is this period in the Kepler occurrence rate peak?)
- `resonance_flag` (Does this period form a near-integer ratio with other candidates?)

### Step 4: Validate and Freeze (1 week)

Re-run Phase 5.3 with the trained model replacing H-S3-01. Compare Top-1 Recall, Top-3 Recall, and Family Recall against the heuristic baseline. If Top-1 improves by ≥5%, adopt the ML model.

**After these four steps, the "Physics-Constrained ML" title claim would be fully defensible.**

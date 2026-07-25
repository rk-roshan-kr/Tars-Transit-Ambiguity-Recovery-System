# Missing Novelty Audit

*Phase 5.4 — Component F. The most important document in Phase 5.4. Identifies every novelty element in the TARS scientific vision that has not yet entered executable code.*

---

## What Makes TARS Different From BLS?

BLS (Box Least Squares) folds the **continuous flux array** over a dense frequency grid, accumulating signal by folding all cadences into a phase-folded light curve. Its mathematical domain is cadence-space.

TARS Stage 3 operates in **event-space** — a fundamentally different mathematical domain. Instead of folding flux, it reconstructs orbital hypotheses from the pairwise time separations of individually detected transit events.

**Documented differences**:
1. Domain: Event-space vs cadence-space.
2. Complexity: $O(N_{events}^2)$ vs $O(N_{cadences} \cdot N_{freqs})$.
3. Gap handling: TARS explicitly models observational windows; BLS folds gap cadences as zero-flux points.
4. Output: An admissible candidate family vs a peak periodogram power.

**Current code status**: All four differences exist in the implemented code. The BLS comparison claim is **architecturally defensible**.

---

## What Makes TARS Different From TLS?

TLS (Transit Least Squares) improves on BLS by using a physically accurate transit shape model and limb-darkening profiles. It still operates in cadence-space.

The key TARS differentiator over TLS is that TARS does not require **any flux information** — it only requires transit event timestamps. This makes TARS potentially useful for pre-processed event catalogs, for extremely sparse datasets where phase-folding produces unreliable shapes, and for long-baseline revisit architectures where the physical transit shape cannot be reliably reconstructed.

**Current code status**: True. Stage 3 uses no flux data whatsoever. The claim is defensible.

---

## Novelty Items Existing Only On Paper

### Missing Novelty 1: Physics-Constrained Candidate Scoring

**Original Idea**: The paper title claims "physics-constrained ML." The original vision (Phase 4 architecture documents) proposed that candidate period scoring should incorporate physical plausibility constraints derived from orbital mechanics — not just phenomenological statistics.

**Why It Matters**: A $2P$ harmonic alias and the true $P$ may have identical coverage fractions and residual MADs. Without physics constraints (e.g., Kepler's third law placing the orbit in or out of the stellar habitable zone, Hill stability criteria, eccentricity limits), no heuristic can distinguish them.

**Current State**: The `consensus_ranker.py` uses a linear blend of `coverage`, `stability`, and `support`. No orbital mechanics enter the score. This is a **pure heuristic**, not physics-constrained scoring.

**Required Future Work**: Implement a physical prior that penalizes periods inconsistent with known stellar parameters (stellar mass → period → semi-major axis → transit probability consistency check). This requires access to stellar metadata during Stage 3 execution.

---

### Missing Novelty 2: Bayesian Evidence Accumulation

**Original Idea**: Phase 4 architecture discussions proposed treating each transit event as a piece of Bayesian evidence, updating a posterior probability distribution over periods. The posterior would naturally handle missing events by reducing the likelihood of hypotheses that predict transits in observable windows but don't find them.

**Why It Matters**: The current MAD/coverage scoring is a proxy for likelihood but not a rigorous one. A Bayesian framework would provide formally calibrated probabilities, directly comparable across different targets and systems, and would explain the uncertainty in a mathematically principled way reviewers can verify.

**Current State**: Nothing. The ranker score is not a likelihood or posterior. No Bayesian framework exists.

**Required Future Work**: Define a generative model for transit events under a given period hypothesis. Compute a Poisson likelihood for the observed event count given the expected count under the coverage model. Use a log-posterior score instead of the current heuristic.

---

### Missing Novelty 3: Multi-Planet Signal Separation

**Original Idea**: TARS should identify whether the event stream contains signals from *multiple* distinct periodic sources (planets) and decompose the stream into independent period families.

**Why It Matters**: TESS multi-planet systems are not rare. The Phase 5.2 multi-planet contamination experiment showed 100% contamination for 10d / 15d non-integer period ratio systems. A reviewer will immediately ask whether TARS works for any real multi-planet system.

**Current State**: The interval generator creates hypotheses from ALL pairwise event differences, including cross-planet event pairs. No separation mechanism exists.

**Required Future Work**: Implement an iterative residual decomposition: after identifying a candidate period $P_1$, subtract its event contribution, then re-run Stage 3 on the remaining events to search for $P_2$.

---

### Missing Novelty 4: TTV-Aware Non-Linear Ephemeris

**Original Idea**: The architecture documents acknowledge Transit Timing Variations (TTVs) as a known failure class. A non-linear ephemeris model that treats timing residuals as TTV signal rather than noise was proposed as a future extension.

**Why It Matters**: Multi-planet resonances produce TTVs of 10–60 minutes — directly measured in Phase 5.2. At 60 minutes, recovery drops to 72.6%. For systems near mean-motion resonances, which TESS has characterized in high numbers, TARS would fail on scientifically interesting targets.

**Current State**: The linear ephemeris assumption is hardcoded throughout `timing_residuals.py`, `stability_engine.py`, and `period_uncertainty.py`. No TTV model exists.

**Required Future Work**: Add a quadratic or sinusoidal TTV model as an optional extension, fitting TTV amplitude and period alongside the linear ephemeris.

---

### Missing Novelty 5: Orbital Architecture Constraints

**Original Idea**: TARS should incorporate physical constraints from orbital architecture — period ratios consistent with mean-motion resonances, stability criteria (Lagrange stability, Hill stability), and occurrence rate priors from the Kepler/TESS demographic literature.

**Why It Matters**: These constraints would dramatically reduce the candidate family size in multi-period systems and would provide physically motivated confidence scores rather than phenomenological heuristics.

**Current State**: Zero orbital architecture constraints exist in any Stage 3 code file.

**Required Future Work**: This is a medium-complexity addition. At minimum, add a period-ratio resonance check that flags candidates forming known resonant pairs. At maximum, integrate a full dynamical stability classifier.

---

### Missing Novelty 6: ML-Optimized Ranking Layer

**Original Idea**: The HEURISTIC_REGISTRY_STAGE3.md explicitly states that H-S3-01 "may be optimized, evolved, or retrained via machine learning without changing the fundamental equations." This was the intended evolution path.

**Why It Matters**: The 0.4 / 0.4 / 0.2 weight vector in the ranker has never been calibrated. With a training set of confirmed planets and known aliases, a logistic regression or gradient-boosted classifier would almost certainly outperform the hand-tuned weights.

**Current State**: No ML component exists anywhere in Stage 3. No training dataset has been assembled. No training infrastructure exists.

**Required Future Work**: Generate a labeled training set from Phase 5.3 results (true periods labeled 1, aliases labeled 0), fit a binary classifier over the six candidate features, and replace the hardcoded weights with the learned model.

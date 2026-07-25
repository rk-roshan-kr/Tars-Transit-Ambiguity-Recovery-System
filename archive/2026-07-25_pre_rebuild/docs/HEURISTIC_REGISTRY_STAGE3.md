# Stage 3: Heuristic Registry

TARS distinguishes between immutable scientific equations (registered in `EQUATION_REGISTRY_STAGE3.md`) and experimental heuristics used for sorting and ranking. The following heuristics may evolve without violating the scientific freeze.

---

### H-S3-01: Consensus Ranking Score

**Status**: 🧪 EXPERIMENTAL HEURISTIC  
*(Not Frozen Science. Not part of Equation Registry.)*

**Objective**: Convert multi-dimensional period features into a single sortable scalar value to rank candidate periods.

**Inputs**:
* `coverage_fraction` (from Observation Window Model)
* `n_supporting_events` (count of matching events)
* `residual_mad` (timing residual median absolute deviation)
* `period_stability` (normalized stability score)

**Output**:
* `ranking_score` (float)

**Explicit Disclaimer**: 
The specific mathematical weighting used to combine these inputs (e.g., $Score = W_1 \times Coverage + W_2 \times Stability$) is considered a computational heuristic, not a physical law. These weights may be optimized, evolved, or retrained via machine learning without changing the fundamental equations that compute the features themselves.

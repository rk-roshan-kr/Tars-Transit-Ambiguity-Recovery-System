# Stage 4 Architecture Compliance Audit

*Phase 7.1 — Scientific Validation Phase. Verification of Stage 4 EEA pipeline invariants.*

---

## 1. No Ranking Invariant (INV-EEA-2)

### Rule
Stage 4 must not sort, re-order, or rank candidates. The output list of `CandidateEvidenceReport` must match the input list of `PeriodCandidate` exactly.

### Search Audit
A case-sensitive search for sorting keywords inside `tarscore/stage4_eea/` was conducted:
* `sorted` or `sort`: Found in `evidence_report.py` to order a temporary list of candidates for calculating family-wide Shannon entropy and ambiguity metrics. Crucially, this does not affect the engine output list order.
* `argsort` or `rank`: 0 occurrences.
* `eea_engine.py` evaluates candidates in a linear `for candidate in candidates` loop and returns the reports in the exact same index order.

### Verdict
> [!NOTE]
> **STATUS**: **PASS**

---

## 2. No Candidate Rejection Invariant (INV-EEA-1)

### Rule
No candidate may be filtered, vetoed, or removed from the pipeline by Stage 4. Input candidate count must exactly equal output report count.

### Audit
Across all 100 trials of `run_eea_feature_distribution.py`, the number of input candidates returned from Stage 3 was tracked and compared to the output candidate reports from Stage 4:
* Total input candidates across all trials: 389
* Total output reports across all trials: 389
* Candidate Recovery Rate: **100.0%**

### Verdict
> [!NOTE]
> **STATUS**: **PASS**

---

## 3. No Weights Invariant (INV-EEA-3)

### Rule
No module in Stage 4 may combine features using weighted linear combinations, scaling weights, or tuning constants to produce a composite candidate score.

### Search Audit
A search for weighting keywords inside `tarscore/stage4_eea/` was conducted:
* `weight`, `alpha`, `beta`, `gamma`: 0 occurrences of weight-based equations or scalars.
* `score =`: Found in `harmonic_evidence.py` to parse Stage 3 ranking score delta (`ambiguity_score`), which is an audit trail value from Stage 3 and not computed by Stage 4 itself.
* Static analysis confirms all 27 features remain independent dimensions of the `EvidenceVector`.

### Verdict
> [!NOTE]
> **STATUS**: **PASS**

---

## 4. Determinism Invariant (INV-EEA-5)

### Rule
EEA Engine must be a pure, side-effect-free function of its inputs. Identical inputs must yield bitwise identical outputs.

### Executable Audit
A determinism script evaluated a single mock recovery 1,000 times in a loop and compared the serialized byte structures of the outputs.
* Matches observed: **1,000 / 1,000**
* Output drift: **0.0%**

### Verdict
> [!NOTE]
> **STATUS**: **PASS**

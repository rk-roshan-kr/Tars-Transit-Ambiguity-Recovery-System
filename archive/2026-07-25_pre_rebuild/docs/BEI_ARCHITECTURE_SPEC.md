# BEI Architecture Specification

This document defines and freezes the scientific, architectural, and governance specification for Stage 6 Bayesian Evidence Integration (BEI).

---

## 1. Pipeline Position & Interfaces

Stage 6 BEI is the probabilistic inference layer. It consumes all structured outputs from Stage 4 EEA and Stage 5 ECHO, integrates independent evidence families via Bayes Factors, and produces a decomposable posterior belief for each candidate.

### Inputs
- `List[CandidateEvidenceReport]` — Stage 4 output (EvidenceVector per candidate)
- `List[PhysicsReport]` — Stage 5 ECHO output (ECHOReport per candidate)
- `Optional[StellarMetadata]` — host star parameters

### Outputs
- `List[CandidatePosteriorReport]` — one per candidate, containing full posterior decomposition

### Explicitly Prohibited Inputs
BEI must never access or consume:
- `confidence_score`
- `ranking_trace`
- `ambiguity_score` (raw Stage 3 ranking residual)
- `ambiguity_index`
- `information_content`
- `physics_score`
- Any composite score derived from admitted variables

---

## 2. Architectural Invariants

- **INV-BEI-1: No Candidate Creation.** BEI cannot generate candidates. It only consumes Stage 5 outputs.
- **INV-BEI-2: No Candidate Deletion.** Every candidate must receive a posterior report. Output list size equals input list size.
- **INV-BEI-3: No Ranking Weights.** Forbidden: `score = alpha*x + beta*y`. No weighted averages. No expert weighting. No scalar fusion.
- **INV-BEI-4: Posterior Traceability.** Every posterior must be decomposable into prior, per-family Bayes factors, and the resulting posterior to machine precision.
- **INV-BEI-5: Deterministic Execution.** Identical inputs must produce identical outputs. No random state, no system clock, no global mutable state.
- **INV-BEI-6: Admission Governance.** Only features in the frozen `BEI_FEATURE_ADMISSION_REGISTRY.md` whitelist may contribute Bayes Factors.
- **INV-BEI-7: Calibration Requirement.** No Bayes Factor may be implemented without a documented calibration pathway in `BEI_CALIBRATION_SPEC.md`.

---

## 3. Bayesian Framework

BEI applies the log-odds form of Bayes' theorem:

$$\ln O(H|E) = \ln O(H) + \sum_{i} \ln BF_i$$

where:
- $H$ = candidate is a physically real periodic astrophysical signal
- $\neg H$ = candidate is not real (noise, systematic, false alarm, eclipsing binary, etc.)
- $O(H) = P(H)/(1-P(H))$ = prior odds
- $BF_i = P(E_i|H) / P(E_i|\neg H)$ = Bayes Factor for evidence family $i$
- $P(H|E) = O(H|E) / (1 + O(H|E))$ = posterior probability

### Version 1 Prior
$$P(H) = 0.5 \implies O(H) = 1.0 \implies \ln O(H) = 0.0$$

This is a non-informative reference prior. It keeps inference clean while prior sensitivity is assessed via `run_prior_sensitivity.py`.

---

## 4. Posterior Categories

Posterior probabilities map to five categorical levels. These are interpretive labels — not ranks.

| Category | Probability Range |
| :--- | :--- |
| `VERY_STRONG` | $P \ge 0.99$ |
| `STRONG` | $0.95 \le P < 0.99$ |
| `MODERATE` | $0.80 \le P < 0.95$ |
| `WEAK` | $0.50 \le P < 0.80$ |
| `UNSUPPORTED` | $P < 0.50$ |

---

## 5. Evidence Families

Six evidence families contribute independent Bayes Factors. Feature admission is governed by `BEI_FEATURE_ADMISSION_REGISTRY.md`. Likelihood equations are defined in `BEI_LIKELIHOOD_REGISTRY.md`.

| Family | Label | Source |
| :--- | :--- | :--- |
| A | Temporal | `TemporalEvidence` |
| B | Harmonic | `HarmonicEvidence` (admitted features only) |
| C | Stability | `StabilityEvidence` |
| D | Observability | `ObservabilityEvidence` |
| E | Physics | `PhysicsEvidence` |
| F | Morphology | `MorphologyAssessment` (from ECHO) |

---

## 6. Scientific Success Criteria

| ID | Criterion |
| :--- | :--- |
| SC-BEI-1 | Posterior probabilities bounded $[0, 1]$ |
| SC-BEI-2 | Every posterior reproducible from audit trail to machine precision |
| SC-BEI-3 | No Stage 3 heuristic leakage |
| SC-BEI-4 | 100% candidate retention |
| SC-BEI-5 | Deterministic outputs |
| SC-BEI-6 | Every Bayes Factor documented in registry |
| SC-BEI-7 | Posterior decomposition exact to numerical precision |
| SC-BEI-8 | Independent audit can reconstruct posterior from artifacts alone |
| SC-BEI-9 | Posterior monotonicity: improving evidence never decreases posterior |
| SC-BEI-10 | Evidence ablation stability: removing one family does not collapse posterior |
| SC-BEI-11 | Double-counting audit: correlated features excluded or conditionally controlled |
| SC-BEI-12 | Prior sensitivity: conclusions stable across $P(H) \in \{0.1, 0.25, 0.5, 0.75\}$ |

---

## 7. Prohibited Constructs

BEI is strictly forbidden from:
- Sorting or ranking candidates by posterior probability.
- Deleting candidates below a posterior threshold.
- Using `sort()`, `sorted()`, `argsort()` on the candidate list.
- Any weighted linear combination of evidence values.
- Assigning Bayes Factors without a documented calibration entry.
- Consuming any Stage 3 variable listed under Prohibited Inputs.

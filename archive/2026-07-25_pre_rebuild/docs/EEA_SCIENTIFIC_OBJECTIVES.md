# EEA Scientific Objectives

*Phase 7 — Stage 4 Evidence Evaluation Architecture. Frozen before implementation.*

---

## Role in the TARS Pipeline

Stage 3 answers: **"What periods are admissible?"**

Stage 4 (EEA) answers: **"What evidence supports each admissible period?"**

Stage 4 does not rank. It does not reject. It measures.

The evidence vectors it produces are the sole inputs to Stage 5 (ECHO geometric reasoning) and Stage 6 (Bayesian + Physics-Constrained ML). No downstream stage may access raw Stage 3 forensics directly — all evidence must pass through Stage 4 first.

---

## Research Questions

### RQ-E1: Alias Disambiguation Evidence

**Question**: Do any evidence dimensions carry enough information to distinguish P from 2P from P/2 without ranking?

**Measurable Outcome**: Feature-by-feature separability (distribution overlap) between true-period candidates and alias candidates across all 27 EV features.

**Failure Condition**: All 27 features have fully overlapping distributions between P and P/2. If true, Stage 5 and Stage 6 cannot use EEA evidence for alias discrimination.

**What this is NOT**: A pass/fail criterion for Stage 4. Separability is a Stage 5 question. RQ-E1 is an observational diagnostic.

---

### RQ-E2: Evidence Correlation with True Recovery

**Question**: Which evidence dimensions most strongly correlate with correct period recovery?

**Measurable Outcome**: Pearson/Spearman correlation between each EV feature and the binary true/alias label across the Phase 5.3 population.

**Failure Condition**: No feature correlates above |r| = 0.1 with true recovery. This would indicate the evidence architecture is capturing noise, not signal.

---

### RQ-E3: Evidence Stability Under Adversarial Conditions

**Question**: Which evidence dimensions remain stable (low coefficient of variation) as gap fraction and timing noise increase?

**Measurable Outcome**: CV(feature) vs gap_fraction and vs σ_t for all 27 features across N=500 trials per condition.

**Failure Condition**: Every feature has CV > 50% at gap_fraction > 0.5. This would indicate evidence vectors are too noisy to be useful in the sparse-data regime.

---

### RQ-E4: Quantitative Ambiguity Measurement

**Question**: Can `ambiguity_index` be computed as a continuous, bounded quantity that monotonically tracks the difficulty of alias discrimination?

**Measurable Outcome**: Correlation between `ambiguity_index` and score margin (top-1 vs top-2 candidate score difference from Stage 3).

**Failure Condition**: `ambiguity_index` is not bounded in [0, 1], or does not correlate with score margin (r < 0.1). This would indicate the index is not measuring ambiguity.

---

### RQ-E5: Evidence Explainability

**Question**: Can candidate quality be described in human-interpretable terms using only the 27 EV features, without introducing weights?

**Measurable Outcome**: For a given candidate, the evidence report must support natural-language statements of the form: "This candidate has N_events supporting events, covers F% of expected transits, with normalized MAD of X% of the period, in a family of K candidates." No aggregated scores permitted.

**Failure Condition**: Evidence reports require aggregation to be interpretable, implying that the individual features are not self-explanatory.

---

## Scientific Constraints (FROZEN)

1. **No ranking**: Stage 4 may not sort, score, or select candidates.
2. **No rejection**: Stage 4 may not eliminate any candidate from the family.
3. **No weights**: Stage 4 may not multiply evidence features by any scalar weight.
4. **Complete coverage**: Every candidate in the Stage 3 output must receive a complete `EvidenceVector`.
5. **Graceful degradation**: Evidence features that require unavailable inputs (e.g., stellar metadata) must flag `None` and emit a warning — never default to 0.0 or nan.
6. **Determinism**: Identical inputs must produce identical outputs. No random state permitted.

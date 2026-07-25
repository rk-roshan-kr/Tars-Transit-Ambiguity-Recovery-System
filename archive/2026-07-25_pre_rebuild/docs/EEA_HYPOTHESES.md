# EEA Pre-Registered Hypotheses

*Phase 7 — Frozen before implementation. All hypotheses must be falsifiable from CSV artifacts alone.*

---

## Registration Rules

1. Each hypothesis must specify an exact falsification condition.
2. No hypothesis may be modified after Phase 7.1 implementation begins.
3. Each hypothesis maps to exactly one experiment script.
4. Hypotheses about ranking, classification, or ML performance are forbidden here — those belong to Stage 5 and Stage 6.

---

## HEEA-1: Support Count Separability

**Statement**: After WLS epoch fitting (Phase 6.1), the `support_count` distribution for true-period candidates is statistically distinguishable from the `support_count` distribution for P/2 alias candidates.

**Experiment**: `run_eea_alias_separation.py`

**Falsification**: Two-sample KS test p-value > 0.05 on support_count between true-period and P/2-alias populations (i.e., distributions are statistically indistinguishable).

**Scientific motivation**: WLS fitting improves residual quality, which should increase support_count for the true period relative to aliases that inherit fewer events.

---

## HEEA-2: Chain Coherence Discriminates Aliases

**Statement**: The `chain_coherence` score (PF-07) is higher for true-period candidates than for harmonic alias candidates in ≥60% of ambiguous cases.

**Experiment**: `run_eea_alias_separation.py`

**Falsification**: Mean chain_coherence(true) ≤ mean chain_coherence(alias) across the full Phase 5.3 population.

**Scientific motivation**: The P/2 alias assigns non-consecutive transit numbers to adjacent events, producing chain breaks that the true period does not.

---

## HEEA-3: Gap Fraction Positively Correlates with Shannon Entropy

**Statement**: `information_content` (Shannon entropy of the candidate family score distribution) increases monotonically as `gap_fraction` increases.

**Experiment**: `run_eea_gap_resilience.py`

**Falsification**: Spearman correlation between gap_fraction and information_content is not significantly positive (ρ < 0.3, p > 0.05).

**Scientific motivation**: Higher gap fraction means more missing transits, which reduces the effective evidence available for period discrimination, which should increase family entropy (ambiguity).

> [!NOTE]
> HEEA-3 was previously stated as "identifiability_score degrades monotonically with gap fraction." **Rejected and replaced.** Stage 4 measures raw observables. `information_content` is a computable summary statistic; `identifiability_score` was a derived conclusion belonging to Stage 5.

---

## HEEA-4: Ambiguity Index Boundedness

**Statement**: `ambiguity_index` is bounded in [0, 1] for all tested inputs (N ∈ [2, 20], gap_fraction ∈ [0, 0.9], σ_t ∈ [0, 0.1]).

**Experiment**: `run_eea_ambiguity_quantification.py`

**Falsification**: Any computed `ambiguity_index` value outside [0, 1] in 10,000 random trials.

**Scientific motivation**: The ambiguity index is defined as the normalized score margin. It must be bounded for ECHO to use it as a gating criterion.

---

## HEEA-5: Physics Evidence Adds Independent Information

**Statement**: The `chain_coherence` and `occurrence_log_prior` features contain information not already present in the temporal evidence family (i.e., they are not redundant with `coverage_fraction` and `support_count`).

**Experiment**: `run_eea_feature_distribution.py` (cross-family correlation analysis)

**Falsification**: Pearson correlation between chain_coherence and coverage_fraction > 0.95 AND correlation between occurrence_log_prior and support_count > 0.95 (i.e., physics features are linear proxies for temporal features).

**Scientific motivation**: Physics features are derived from different mathematical relationships than temporal features. If they are perfectly correlated, Stage 6 ML training receives redundant features.

---

## HEEA-6: Deterministic Reproducibility

**Statement**: EEA produces identical `EvidenceVector` outputs for identical inputs across 1,000 independent calls.

**Experiment**: Embedded in the verification step of Phase 7.1 implementation — not a standalone script.

**Falsification**: Any difference in any EvidenceVector field across repeated calls with identical inputs.

**Scientific motivation**: Stage 4 is a pure measurement function. Non-determinism indicates hidden state or floating-point order dependence, both of which are defects.

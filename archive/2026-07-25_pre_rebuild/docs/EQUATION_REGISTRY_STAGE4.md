# Equation Registry (Stage 4 EEA)

*Phase 7 — Frozen. All equations used in Stage 4 evidence extraction.*

---

## EQ-S4-01: Event Density

Computes the sampling density metric for how constrained the period can be from available events.

$$\rho_{ev} = \frac{N_{events}}{T_{baseline}}$$

where $T_{baseline} = t_{max} - t_{min}$ across all delivered Stage 2 events (days).

**Feature**: EV-I3 (`event_density`)
**Units**: events/day

---

## EQ-S4-02: Baseline-Period Ratio

$$R_{BP} = \frac{T_{baseline}}{P_{candidate}}$$

**Feature**: EV-I2 (`baseline_period_ratio`)
**Units**: dimensionless

---

## EQ-S4-03: Normalized MAD (Stability)

$$\text{MAD}_{norm} = \frac{\text{MAD}_r}{P_{candidate}}$$

where $\text{MAD}_r$ is from EQ-S3-04. Uses min-of-fractional-and-absolute formulation per `PERIOD_RELATIVE_STABILITY_SPEC.md`.

**Feature**: EV-S1 (`normalized_mad`)
**Units**: dimensionless

---

## EQ-S4-04: Normalized RMS (Stability)

$$\text{RMS}_{norm} = \frac{\text{RMS}_r}{P_{candidate}}$$

**Feature**: EV-S2 (`normalized_rms`)
**Units**: dimensionless

---

## EQ-S4-05: Uncertainty Ratio

$$U_r = \frac{\sigma_P}{P_{candidate}}$$

where $\sigma_P$ is the WLS-derived period uncertainty from Stage 3.

**Feature**: EV-S3 (`uncertainty_ratio`)
**Units**: dimensionless

---

## EQ-S4-06: Window Completeness

$$W_c = \frac{N_{obs}}{N_{obs} + N_{gap}}$$

where $N_{obs}$ = observable transits (period falls in observed window) and $N_{gap}$ = transits in gap windows.

**Feature**: EV-O3 (`window_completeness`)
**Units**: dimensionless ∈ [0, 1]

---

## EQ-S4-07: Chain Coherence Score (PF-07)

$$\Phi_{chain}(P) = 1 - \frac{N_{breaks}}{N_{events} - 1}$$

where a chain break occurs when $|n_{k+1} - n_k - 1| > K_{max}$ for consecutive events ordered by time.

**Feature**: EV-P3 (`chain_coherence`)
**Units**: dimensionless ∈ [0, 1]
**Reference**: `STAGE3_PHYSICS_FEATURE_REGISTRY.md` PF-07

---

## EQ-S4-08: Occurrence Rate Log-Prior (PF-03, Fressin 2013)

$$\log p_{occ}(P) = -0.7 \cdot \log_{10}(P) + C$$

where $C$ is a normalization constant chosen such that $p_{occ}(1) = 1$ (i.e., $C = 0$). The feature is unnormalized — only relative values matter.

**Feature**: EV-P4 (`occurrence_log_prior`)
**Units**: dimensionless (log probability, ≤ 0 for P ≥ 1 day)
**Reference**: Fressin et al. 2013, ApJ 766, 81

---

## EQ-S4-09: Transit Spacing Regularity

$$V_{spacing} = \text{Var}\left(\frac{t_{k+1} - t_k}{P_{candidate}}\right)$$

where the variance is computed over all consecutive event pairs $(t_k, t_{k+1})$.

**Feature**: EV-P5 (`transit_spacing_regularity`)
**Units**: dimensionless (variance of normalized spacing)
**Note**: For a perfect ephemeris, $V_{spacing} = 0$. Aliases with incorrect periods produce larger variance.

---

## EQ-S4-10: Transit Number Monotonicity

$$M_n = \frac{|\{k : n_{k+1} > n_k\}|}{N_{events} - 1}$$

where $n_k = \text{round}((t_k - t_0) / P)$ is the transit number of event $k$.

**Feature**: EV-P6 (`transit_number_monotonicity`)
**Units**: dimensionless ∈ [0, 1]
**Note**: For the true period with correct epoch, $M_n = 1.0$. Aliases may produce non-monotonic transit number assignments.

---

## EQ-S4-11: Ambiguity Index

$$A_{idx} = 1 - \frac{\Delta_{score}}{\Delta_{score,max}}$$

where $\Delta_{score}$ is the Stage 3 ranking score margin (top-1 minus top-2) and $\Delta_{score,max}$ is the maximum observed margin in the family.

**Feature**: Contributes to `EvidenceFamilySummary.ambiguity_index`
**Units**: dimensionless ∈ [0, 1]
**Note**: When `family_size = 1`, $A_{idx} = 0$ (no ambiguity by definition).

---

## EQ-S4-12: Family Information Content (Shannon Entropy)

$$H = -\sum_{i=1}^{K} p_i \log p_i$$

where $p_i$ is the normalized ambiguity score for candidate $i$: $p_i = s_i / \sum_j s_j$ and $s_i$ is the Stage 3 ranking score.

**Feature**: `EvidenceFamilySummary.information_content`
**Units**: nats
**Note**: $H = 0$ when one candidate dominates completely. $H = \log K$ when all candidates have equal scores (maximum ambiguity).

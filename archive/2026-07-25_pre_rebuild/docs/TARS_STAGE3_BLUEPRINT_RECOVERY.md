# TARS Stage 3: Blueprint Recovery

*Phase 5.4 — Component I. If we started from zero tomorrow, this is what the ideal Stage 3 would look like. Not what code exists — what should exist.*

---

## Preamble

This document is not a criticism of the current implementation. The current Stage 3 is a working first-generation sparse period recovery engine with correct mathematical foundations. This blueprint describes the second-generation design that would fully realize the original TARS scientific vision and make the paper title defensible.

---

## Scientific Objectives

The ideal Stage 3 solves exactly one problem better than any existing algorithm:

> **Given a sparse, discontinuous sequence of $N \geq 2$ high-confidence transit timestamps, recover the full probability distribution over orbital period hypotheses, explicitly quantifying harmonic degeneracy and information-theoretic ambiguity.**

This is different from what BLS and TLS do (maximize SNR via folding). It is different from what LS does (decompose spectral power). It is a **Bayesian reconstruction of the orbital period posterior from discrete timing evidence**.

---

## Architecture

The ideal Stage 3 has five layers (replacing the current 7-component flat pipeline):

### Layer 1: Event Preprocessor
- Input: `TransitEvent[]` from Stage 2.
- Responsibility: Assign per-event timing uncertainties from Stage 2 metadata (duration, SNR, detrending residual).
- Output: Weighted event set $\{(t_k, \sigma_{t_k})\}$.

### Layer 2: Hypothesis Generator (Keeps Current Design)
- Implements EQ-S3-01 with $K_{max}$ harmonic divisors.
- Adds: **Occurrence rate prior** — weight hypotheses by $p(P) \propto P^{-0.7}$ (consistent with Kepler demographic studies).
- Adds: **Consecutive-event ordering** — prefer hypotheses from consecutive transits over arbitrary pairs.

### Layer 3: Bayesian Period Posterior Engine (New)
- For each candidate period $P$:
  - Compute likelihood: $\mathcal{L}(P) = \prod_k \mathcal{N}(r_k; 0, \sigma_{t_k}^2 + \sigma_{TTV}^2)$
  - Incorporate observational coverage prior: penalize periods that predict unobserved transits in clean windows.
  - Compute posterior: $p(P | \text{events}) \propto \mathcal{L}(P) \cdot p(P)$
- Replaces the current heuristic score with a formally calibrated probability.

### Layer 4: Alias Resolution Engine (Upgrade of Current)
- Uses the posterior distribution to formally compare $P$ vs $2P$ vs $P/2$.
- Applies Bayesian model comparison: $\text{Bayes Factor} = p(\text{data} | P) / p(\text{data} | 2P)$.
- Returns the posterior-weighted candidate family, not a manually ranked list.
- Implements the formal tie-breaking rules from `HARMONIC_RESOLUTION_SPECIFICATION.md` using the Bayes Factor rather than heuristic score delta.

### Layer 5: Multi-Planet Decomposition (New)
- After identifying $P_1$, subtract its event contribution.
- Re-run Layers 2–4 on residual events.
- Iterate until no significant periodicity remains.
- Return structured multi-planet candidate families.

---

## Physics Constraints

Every candidate period should pass through three physics gates before being included in the output:

1. **Kepler Third Law Gate**: Given stellar mass $M_*$, compute implied semi-major axis. Reject periods placing the orbit inside the stellar radius.
2. **Hill Stability Gate** (multi-planet only): Verify that proposed multi-planet period ratios satisfy mutual Hill stability criteria.
3. **Occurrence Rate Gate**: Use empirical occurrence rate $p(R_p, P)$ from Fressin et al. 2013 / Petigura et al. 2018 as a Bayesian prior on the posterior.

---

## ML Components

The ideal ML component is narrow and specific: a **Period-Alias Discriminator** trained to distinguish true periods from harmonic aliases.

- **Training Data**: Confirmed planets (labeled TRUE) and their detected aliases (labeled ALIAS) from MAST + Kepler catalog.
- **Feature Vector**: $\{P, \text{Bayes Factor}, \text{coverage}, \text{residual MAD}, \text{SNR}_{\text{min}}, \text{occurrence prior}, \text{resonance flag}\}$.
- **Model**: Gradient-boosted binary classifier. Interpretable (SHAP values for each feature).
- **Output**: Replaces the raw posterior rank with a calibrated probability of being the true physical period.

---

## Candidate Generation Philosophy

The ideal Stage 3 outputs a **calibrated probability distribution** over periods, not a ranked list. The consumer (Stage 4 / Validation) receives:
- The maximum a posteriori (MAP) period estimate.
- The full posterior distribution.
- The Bayes Factor between TOP-1 and TOP-2 candidates.
- The explicit harmonic degeneracy flag with quantitative ambiguity probability.

---

## Ambiguity Reasoning

The ideal Stage 3 distinguishes three ambiguity regimes:

1. **Resolvable**: Bayes Factor > 10. Report the MAP period with confidence.
2. **Marginal**: Bayes Factor 3–10. Report TOP-1 and TOP-2 with explicit posterior probabilities.
3. **Unresolvable**: Bayes Factor < 3. Report the full candidate family as equally plausible. Flag for follow-up observation.

---

## Multi-Planet Reasoning

For multi-planet systems:
- After Period 1 is identified, flag events attributed to $P_1$.
- Run a second-pass Stage 3 on unattrited events.
- Report multi-planet candidate families with cross-period contamination scores.

---

## TTV Handling

The ideal Stage 3 has two ephemeris modes:
1. **Linear**: For standard planets. Current implementation.
2. **Sinusoidal TTV**: For planet pairs near mean-motion resonances. Adds amplitude and phase as free parameters to the ephemeris fit.

Mode selection is automatic based on the residual structure (linear vs oscillatory patterns in the $O-C$ diagram).

---

## Uncertainty Modeling

- Per-event uncertainty is propagated formally from Stage 2's detection metadata.
- Period uncertainty is a full posterior credible interval (not just a covariance-derived sigma).
- For $N=2$ systems, the uncertainty explicitly reports the period degeneracy family, not a false precision scalar.

---

## Ranking Philosophy

The ideal Stage 3 does not "rank" — it assigns calibrated posterior probabilities. The consumer decides what threshold to apply. This eliminates the ranking failure class entirely by reframing the question.

Instead of: *"Which candidate is ranked first?"*
Ask: *"What is the posterior probability that this candidate is the true physical period?"*

---

## Benchmark Philosophy

The ideal Stage 3 is benchmarked on three datasets:
1. **Synthetic**: Dual-population (Seeds 42 + 2026), validated against pre-registered criteria. (DONE)
2. **Realistic Population**: The Phase 5.3 suite. (DONE)
3. **Real TESS TOIs**: 50+ confirmed planets from MAST, run through the full LC → Stage1 → Stage2 → Stage3 pipeline. (PENDING — this is Phase 6's primary validation task)

---

## Publication Strategy

The paper should be structured as:
1. **Problem Identification**: The sparse multi-sector TESS sparse period recovery problem.
2. **Event-Space Framework**: Mathematical derivation of the pairwise interval algebra and Bayesian period posterior.
3. **Alias Resolution**: Formal Bayes Factor derivation for harmonic tie-breaking.
4. **Benchmarks**: Synthetic, Realistic Population, and Real TESS validation (all three required for submission).
5. **Limitations**: TTV failure, multi-planet contamination, Stage 2 dependency — all pre-registered in `FAILURE_MODES_STAGE3.md`.
6. **Comparison**: Explicit head-to-head with BLS and TLS in the sparse regime.

---

## The Final Answer to Phase 5.4

> **Did the original TARS idea fail?**
>
> **No. The original TARS idea is mathematically sound, physically motivated, and empirically supported.**
>
> **Did the implementation fail to fully realize the original TARS idea?**
>
> **Yes. The current implementation correctly realizes approximately 55% of the original vision. The generation layer is complete. The physics-constrained scoring, the ML ranking model, the Bayesian evidence framework, the multi-planet separation, and the TTV handling remain unimplemented.**
>
> **Therefore, Phase 6 is Architectural Evolution — not optimization and not a redesign.**

# Stage 3 End-State Architecture Specification

*Phase 5.5 — Component D. Defines the scientifically correct final architecture for Stage 3. This document supersedes all prior architecture diagrams and serves as the frozen blueprint for Phase 6 implementation work.*

---

## Current Architecture

```
Stage 2 TransitEvents
        ↓
  [1] Interval Generator          EQ-S3-01: P = Δt / k
        ↓
  [2] Harmonic Resolver           Cluster + alias link
        ↓
  [3] Timing Residuals            EQ-S3-02: r_k = t_k - (t₀ + n_k·P)
        ↓
  [4] Period Uncertainty          WLS fit → σ_P
        ↓
  [5] Observation Window          EQ-S3-05: C = N_matched / N_expected
        ↓
  [6] Stability Engine            EQ-S3-03/04: RMS, MAD
        ↓
  [7] Consensus Ranker (H-S3-01)  0.4·C + 0.4·S + 0.2·N (HEURISTIC)
        ↓
  PeriodCandidate[] sorted by score
```

**Known defects in current architecture** (from ARCHITECTURE_IMPLEMENTATION_GAP.md):
- Epoch hardcoded as `min(event_time)`.
- Stability threshold is absolute (not period-relative).
- Harmonic tie-breaking deferred but not executed.
- Support score saturates at 5 events.
- No physics gates exist between generator and ranker.
- Ranker weights are uncalibrated.

---

## Proposed Final Architecture

```
Stage 2 TransitEvents + Stellar Metadata
        ↓
 ┌─────────────────────────────────────┐
 │  LAYER 1: Event Preprocessor        │
 │  - Assign σ_t from Stage 2 metadata │
 │  - Weight events by SNR             │
 │  - Flag suspected false-positives   │
 └─────────────────────────────────────┘
        ↓
 ┌─────────────────────────────────────┐
 │  LAYER 2: Hypothesis Generator      │
 │  - Pairwise interval algebra        │
 │  - Occurrence rate prior weighting  │
 │  - Consecutive-event preference     │
 └─────────────────────────────────────┘
        ↓
 ┌─────────────────────────────────────┐
 │  LAYER 3: Physics Feature Extractor │
 │  - O-C residuals (EQ-S3-02)         │
 │  - Coverage fraction (EQ-S3-05)     │
 │  - Kepler consistency score         │
 │  - Transit duration consistency     │
 │  - Resonance likelihood             │
 │  - Occurrence rate prior            │
 └─────────────────────────────────────┘
        ↓
 ┌─────────────────────────────────────┐
 │  LAYER 4: Bayesian Evidence Layer   │
 │  - Compute log-likelihood per P     │
 │  - Apply observational prior        │
 │  - Compute Bayes Factor (P vs 2P)   │
 │  - Return posterior probability     │
 └─────────────────────────────────────┘
        ↓
 ┌─────────────────────────────────────┐
 │  LAYER 5: ML Ranking Layer          │
 │  - Feature vector: 10 dimensions    │
 │  - Trained binary classifier        │
 │  - Output: P(true period) score     │
 └─────────────────────────────────────┘
        ↓
 PeriodCandidate[] with calibrated
 posterior probabilities + Bayes Factors
 + harmonic flags + physics flags
```

---

## Layer Specifications

### Layer 1: Event Preprocessor

| Property | Specification |
| :--- | :--- |
| **Input** | `TransitEvent[]` from Stage 2, `StellarMetadata` |
| **Output** | Weighted `TransitEvent[]` with `sigma_t` per event |
| **Key Equation** | $\sigma_{t,k} = \text{duration}_k / \text{SNR}_k$ (current heuristic, to be validated against photometric noise model) |
| **Scientific Justification** | Different events carry different timing precision. A low-SNR event has higher timing scatter. Treating all events equally corrupts the residual statistics. |
| **Failure Modes** | If all events have SNR below threshold, the weighted residuals may diverge. Must retain minimum-trust floor. |

---

### Layer 2: Hypothesis Generator

| Property | Specification |
| :--- | :--- |
| **Input** | Weighted `TransitEvent[]` |
| **Output** | `IntervalHypothesis[]` |
| **Key Equation** | $P_{i,j,k} = |t_j - t_i| / k$, $k \in [1, K_{max}]$ |
| **New Addition** | Prior weight $w_{i,j,k} \propto p(P_{i,j,k})$ from Fressin et al. 2013 occurrence rate distribution |
| **Scientific Justification** | Not all periods are equally plausible. Occurrence rate distributions strongly favor $P < 10$ days. Weighting the proposal distribution improves posterior calibration. |
| **Failure Modes** | If $K_{max}$ is too small, long-period aliases are missed. If $K_{max}$ is too large, the hypothesis space becomes computationally degenerate. |

---

### Layer 3: Physics Feature Extractor

| Property | Specification |
| :--- | :--- |
| **Input** | `IntervalHypothesis[]`, `TransitEvent[]`, `ConditionedLightCurve`, `StellarMetadata` |
| **Output** | Feature vector per candidate: $\vec{f} = [C, \text{MAD}, \text{RMS}, N_s, K_3, D_{cons}, R_{res}, p_{occ}]$ |
| **Key Features** | See STAGE3_PHYSICS_FEATURE_REGISTRY.md for complete feature specifications |
| **Scientific Justification** | Physics features constrain the scoring space to physically plausible solutions, preventing heuristic weighting from elevating implausible periods. |
| **Failure Modes** | If stellar metadata is missing, $K_3$ and $D_{cons}$ cannot be computed. Must have graceful degradation to non-physics-gated scoring. |

---

### Layer 4: Bayesian Evidence Layer

| Property | Specification |
| :--- | :--- |
| **Input** | Feature vector per candidate |
| **Output** | Log-posterior $\log p(P \mid \text{events})$, Bayes Factor vs top alias |
| **Key Equation** | $\log \mathcal{L}(P) = -\sum_k \frac{r_k^2}{2\sigma_{t,k}^2}$ (Gaussian timing likelihood) |
| **Prior** | $\log p(P) = -0.7 \log P + \text{const}$ (power-law occurrence rate) |
| **Bayes Factor** | $\text{BF}(P, 2P) = \mathcal{L}(P) \cdot p(P) / [\mathcal{L}(2P) \cdot p(2P)]$ |
| **Scientific Justification** | The Bayes Factor provides a formally defensible criterion for alias selection that replaces the current score_delta threshold. |
| **Failure Modes** | For $N=2$, both $P$ and $2P$ may have identical likelihoods. The Bayes Factor reduces to the prior ratio — which at least enforces occurrence-rate physics. |

---

### Layer 5: ML Ranking Layer

| Property | Specification |
| :--- | :--- |
| **Input** | Feature vector + Bayesian log-posterior per candidate |
| **Output** | Calibrated $P(\text{true period})$ for each candidate |
| **Model Type** | Gradient-boosted binary classifier (scikit-learn GradientBoostingClassifier or XGBoost) |
| **Training Data** | Phase 5.3 dual-population results (labeled: TRUE_PERIOD / ALIAS / FALSE_PERIOD) |
| **Validation** | Hold-out Population B (Seed 2026) only; Population A (Seed 42) used for training |
| **Scientific Justification** | A data-driven model trained on physically labeled examples can learn non-linear separability between true periods and aliases that the hand-tuned linear heuristic cannot. |
| **Failure Modes** | If the training set is not representative of real TESS distributions, the learned model will overfit to simulator assumptions. Real TESS validation is required before deployment. |

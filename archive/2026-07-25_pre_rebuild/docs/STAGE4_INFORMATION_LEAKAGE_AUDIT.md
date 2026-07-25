# Stage 4 Information Leakage Audit

*Phase 7.1 — Scientific Validation Phase. Verification of Stage 4 independence from Stage 3 heuristic scores.*

---

## 1. Objective

To prevent downstream Stage 6 Machine Learning (XGBoost) models from accidentally learning to duplicate Stage 3's heuristic confidence scores rather than learning physical exoplanet signatures, we mapped the leakage profile of all Stage 4 features.

---

## 2. Feature Leakage Classifications

| Feature ID | Symbol | Leakage Level | Leakage Source | Description |
| :--- | :--- | :---: | :--- | :--- |
| **EV-H3** | `ambiguity_score` | **HIGH** | `candidate.confidence_score` | Computes candidate margin relative to alias scores. Inherits Stage 3 heuristic directly. |
| **Summary** | `ambiguity_index` | **HIGH** | `candidates[i].confidence_score`| Measures family score margin. Direct reflection of Stage 3 rank separation. |
| **Summary** | `information_content` | **HIGH** | `candidates[i].confidence_score`| Shannon entropy calculated over Stage 3 score distributions. |
| **EV-T1** to **EV-T6**| Temporal family | **NONE** | Raw event residuals | Purely mathematical measurements of residuals and event support times. |
| **EV-H1** | `harmonic_order` | **NONE** | Parsing string label | An integer order identifier. |
| **EV-H2** | `alias_family_size` | **NONE** | Period matching | Candidate count in harmonic range. |
| **EV-H4** | `alias_density` | **NONE** | Period matching | Candidate count in timing uncertainty range. |
| **EV-S1** to **EV-S3**| Stability family | **NONE** | Period / WLS output | Normalised MAD, RMS, and WLS uncertainty. |
| **EV-I1** to **EV-I4**| Information family | **NONE** | Event / candidate counts | Number of events, baseline period ratio, event density. |
| **EV-O1** to **EV-O4**| Observability family | **NONE** | LC gap calculation | Observation window completeness and gaps. |
| **EV-P1** to **EV-P6**| Physics family | **NONE** | Astrophysical equations | Kepler's law, duration model, prior, spacing, and monotonicity. |

---

## 3. Scientific Recommendation for ML Training (Stage 6)

* **Features to Mask**: When training the Stage 6 ML classifier, we must **exclude `EV-H3` (ambiguity_score), `ambiguity_index`, and `information_content`** from the training feature set.
* **Why**: If included, the ML model will easily overfit on these score-derived values, bypassing physical reasoning. The model would learn a circular map of:
  $$\text{ML Score} = f(\text{Stage 3 Heuristic})$$
* By masking them, Stage 6 is forced to learn independent physics and temporal features (e.g. `chain_coherence`, `normalized_mad`), satisfying the architectural goal of combining independent lines of evidence.

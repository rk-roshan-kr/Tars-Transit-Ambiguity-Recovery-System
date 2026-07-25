# Stage 3 Ranking Layer Scientific Replacement

*Phase 5.5 — Component E. Evaluates scientifically valid replacements for H-S3-01. No implementation. Specification only. Sources: HEURISTIC_REGISTRY_STAGE3.md, ARCHITECTURE_IMPLEMENTATION_GAP.md, PHYSICS_CONSTRAINED_ML_AUDIT.md.*

---

## The Problem With H-S3-01

The current consensus ranker implements:

$$\text{Score} = 0.4 \cdot C + 0.4 \cdot S + 0.2 \cdot N_s$$

where $C$ = coverage fraction, $S$ = stability score, $N_s$ = normalized support count.

**Known defects** (from ARCHITECTURE_IMPLEMENTATION_GAP.md):
1. Weights (0.4 / 0.4 / 0.2) have no physical or statistical derivation.
2. $N_s$ saturates at 5 events — 10-event planets score identically to 5-event planets.
3. A $2P$ alias with fewer expected transits (lower denominator in coverage fraction) can artificially match or exceed the true $P$'s coverage score.
4. No physics enter the score whatsoever.
5. The score is not a probability — it cannot be directly interpreted or thresholded.

---

## Candidate Ranking Architectures

### Option 1: Calibrated Handcrafted Heuristic (Baseline Improvement)

**Description**: Retain the linear blend structure but derive weights via cross-validation on the Phase 5.3 training set.

$$\text{Score} = w_1 \cdot C + w_2 \cdot S + w_3 \cdot \log(N_s) + w_4 \cdot K_3$$

where $K_3$ is the Kepler's third law consistency score (new physics term) and $w_i$ are fitted via ridge regression.

| Criterion | Rating |
| :--- | :---: |
| Interpretability | HIGH — linear model |
| Scientific defensibility | MEDIUM — weights require justification |
| Publication suitability | MEDIUM — improved over current |
| Reproducibility | HIGH — deterministic given weights |
| Training requirements | LOW — ridge regression on tabular data |

**Recommendation**: Use as Phase 6A fallback if ML classifier is unavailable.

---

### Option 2: Logistic Regression Classifier

**Description**: Train a binary logistic regression to classify candidates as TRUE_PERIOD (1) or ALIAS (0) using the 8-dimensional physics feature vector.

$$P(\text{true}) = \sigma(\mathbf{w}^T \vec{f} + b)$$

where $\sigma$ is the sigmoid function and $\vec{f}$ is the physics feature vector.

| Criterion | Rating |
| :--- | :---: |
| Interpretability | HIGH — coefficients directly interpretable |
| Scientific defensibility | HIGH — well-understood statistical model |
| Publication suitability | HIGH — standard, reproducible |
| Reproducibility | HIGH — deterministic given training data |
| Training requirements | LOW — converges in seconds |

**Recommendation**: Use as Phase 6B primary model. Simple, interpretable, and defensible. Logistic regression coefficients become directly reportable physical insights.

---

### Option 3: Random Forest Classifier

**Description**: Ensemble of decision trees trained to discriminate true periods from aliases.

| Criterion | Rating |
| :--- | :---: |
| Interpretability | MEDIUM — feature importance available via SHAP |
| Scientific defensibility | MEDIUM — harder to justify individual predictions |
| Publication suitability | MEDIUM — requires SHAP analysis for interpretability |
| Reproducibility | HIGH — deterministic given seed |
| Training requirements | LOW |

**Recommendation**: Use as comparison baseline alongside logistic regression in ablation study.

---

### Option 4: Gradient Boosting (XGBoost / LightGBM)

**Description**: Boosted decision trees — highest predictive performance on tabular data.

| Criterion | Rating |
| :--- | :---: |
| Interpretability | MEDIUM — SHAP required |
| Scientific defensibility | MEDIUM — "black-box" concern for reviewers |
| Publication suitability | MEDIUM — acceptable if SHAP analysis provided |
| Reproducibility | HIGH |
| Training requirements | LOW-MEDIUM |

**Recommendation**: Use as the production model after logistic regression baseline is established. Report SHAP feature importance to satisfy physics-interpretability requirements.

---

### Option 5: Bayesian Ranking (Log-Posterior Score)

**Description**: Replace the heuristic score with a formally derived log-posterior probability over period hypotheses.

$$\log p(P \mid \text{events}) = \log \mathcal{L}(P) + \log p(P) + \text{const}$$

| Criterion | Rating |
| :--- | :---: |
| Interpretability | HIGH — output is a probability |
| Scientific defensibility | VERY HIGH — reviewers cannot dispute Bayes theorem |
| Publication suitability | VERY HIGH — rigorously principled |
| Reproducibility | HIGH — deterministic given likelihood model |
| Training requirements | NONE — no training data needed |

**Recommendation**: This is the theoretically ideal solution. The Bayesian score is derivable from first principles and requires no training data — making it fully reproducible and publication-ready. It is, however, more complex to implement than the ML options.

---

### Option 6: Hybrid Physics + ML

**Description**: Use the Bayesian log-posterior as a physics-grounded base score, then learn a residual correction from a gradient-boosted classifier trained on Phase 5.3 data.

$$\text{Score}_{\text{hybrid}} = \alpha \cdot \log p(P \mid \text{events}) + (1-\alpha) \cdot f_{\text{ML}}(\vec{f})$$

where $\alpha$ is cross-validated.

| Criterion | Rating |
| :--- | :---: |
| Interpretability | MEDIUM |
| Scientific defensibility | HIGH — physics base prevents pure data-fitting |
| Publication suitability | HIGH |
| Reproducibility | MEDIUM |
| Training requirements | MEDIUM |

**Recommendation**: Target architecture for the full Phase 6 implementation. Combines Bayesian principled scoring with data-driven refinement.

---

## Recommended Ranking Architecture

**Phase 6A (immediate)**: Fix implementation defects in H-S3-01 (epoch, threshold, saturation). This is not a replacement — it is a bug fix.

**Phase 6B (primary target)**: Implement Bayesian log-posterior scoring (Option 5). No training data required. Immediately defensible. Replaces the heuristic completely.

**Phase 6C (production target)**: Add Hybrid Physics + ML (Option 6) on top of the Bayesian base. Use Phase 5.3 labeled data as training set.

**Publication strategy**: Report logistic regression (Option 2) as the interpretable ablation study alongside the full hybrid model. Provide SHAP analysis for all ML components.

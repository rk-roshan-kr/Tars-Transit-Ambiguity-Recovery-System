# Publication Readiness Report (Audit 20.8)

## Question
How do we summarize the core scientific contributions, structural flow, and validity threats of TARS v1 for publication?

## Experiment
We synthesized the structural flow and formulated the conceptual centerpiece mapping the audits to the evidence flow. We also compiled a comprehensive threats to validity analysis.

## Observation
### 1. Conceptual Centerpiece Flow
```
Raw Light Curve
        │
        ▼
Transit Recovery (Stage 2/3)
        │
        ▼ [Arrow 1: Validated via Audit 20.2 (Recovery vs. SNR & Period)]
Candidate Branching (Stage 3 candidates count / Alias Explosion)
        │
        ▼ [Arrow 2: Quantified via Audit 20.1 (Information Dependency CMI)]
Recovery Ambiguity (Unsupervised features)
        │
        ▼ [Arrow 3: Synthesized via RAI Formula]
Recovery Ambiguity Index (RAI)
        │
        ▼ [Arrow 4: Validated via Audit 20.4 (Robustness) & Audit 20.10 (Generalization)]
Candidate Reliability (Tier A vs Tier C)
```

### 2. Publication Statement
> **"We show that candidate recoverability ambiguity is the dominant predictor of exoplanet candidate reliability, and introduce an unsupervised Recovery Ambiguity Index that captures this phenomenon with a compact, interpretable representation."**

### 3. Defence Condition Warning
> **"This work characterizes recoverability ambiguity within the studied detection pipeline. Whether the same ambiguity measure generalizes to different survey architectures remains an empirical question."**

### 4. Threats to Validity
#### A. Internal Validity
*   **Pipeline Coupling**: The Recovery Ambiguity Index (RAI) is computed from the output of the TARS Stage 2/3 recovery pipeline. Variations in the pipeline parameters (e.g. signal search grids, SNR thresholds) may scale the absolute value of the index, although the relative ranking remains robust.
#### B. External Validity
*   **Instrument Specificity**: RAI is validated on TESS cadence structures. Generalization to different survey architectures (e.g. Kepler, PLATO) with different sampling rates and window functions remains an empirical question.
#### C. Dataset Limitations
*   **Giant Star Skew**: Subgroup audits indicate giant stars have limited effective sample size ($N_{\text{eff}} = 2.0$), meaning the robustness of the model on giants has wide statistical uncertainty compared to dwarfs.
#### D. Survey-Specific Assumptions
*   **Stationary Noise**: We assume that TESS systematics are effectively corrected by standard detrending pipelines. Residual non-stationary noise may introduce false candidate branches, elevating the RAI for quiet targets.
#### E. Future Work
*   **TARS Next**: Future research will replace the Stage 2 grid search with a physics-aware proposal network and a differentiable transit simulator to directly model transit probability density rather than counting candidates.

## Interpretation
The conceptual centerpiece maps the audits to each stage of the causal chain. Standardizing terminology prevents confusion across documents, and the Threats to Validity section ensures that the paper is defensible against reviewer critique.

## Conclusion
TARS v1 validation is complete and publication-ready.

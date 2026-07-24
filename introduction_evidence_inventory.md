# Evidence Inventory: Introduction

## 1. Relevant Repository Documents
- **[TARS_ARCHITECTURE.md](file:///d:/TARS/TarsEx/docs/TARS_ARCHITECTURE.md)**: Describes the global 6-stage exoplanet candidate vetting pipeline and modular stages.
- **[TARS_PRODUCTION_ARCHITECTURE_V1.md](file:///d:/TARS/TarsEx/docs/TARS_PRODUCTION_ARCHITECTURE_V1.md)**: Summarizes the conceptual flow (Raw Light Curve -> Transit Recovery -> Candidate Branching -> Recovery Ambiguity -> RAI -> Candidate Reliability).
- **[FAMILY_COMPLEXITY_PHYSICS.md](file:///d:/TARS/TarsEx/docs/FAMILY_COMPLEXITY_PHYSICS.md)**: Explains the physical origin of period recovery aliases caused by stellar rotation, pulsations, and spot cycles.
- **[STAGE1_METHODS.md](file:///d:/TARS/TarsEx/docs/STAGE1_METHODS.md)** and **[STAGE1_OPERATING_BOUNDARIES.md](file:///d:/TARS/TarsEx/docs/STAGE1_OPERATING_BOUNDARIES.md)**: Provide details on detrending timescales, window functions, and data preconditioning.
- **[STAGE2_METHODS.md](file:///d:/TARS/TarsEx/docs/STAGE2_METHODS.md)**: Explains Box Least Squares (BLS) period searching and transit SNR thresholds.
- **[STAGE3_METHODS.md](file:///d:/TARS/TarsEx/docs/STAGE3_METHODS.md)**: Documents the transition from raw transit timestamps to period candidate families.
- **[SCIENTIFIC_OBJECTIVES.md](file:///d:/TARS/TarsEx/docs/SCIENTIFIC_OBJECTIVES.md)**: Outlines the physical rationale for isolating signal recovery ambiguity as a metric of candidate falsifiability.

---

## 2. Key Evidence & Statistics to Extract
- The 6 pipeline stages:
  1. Signal Preconditioning (Stage 1)
  2. Transit Detection (Stage 2)
  3. Period Recovery & Ephemeris Fitting (Stage 3)
  4. Morphology Verification (Stage 4)
  5. Consistency Validation (Stage 5)
  6. Probabilistic Classification (Stage 6)
- The physical mechanisms of stellar activity that trigger false candidate branches (spot group lifetimes, rotation periods, convective noise).
- The definition of recovery ambiguity as epistemic uncertainty within the period recovery process (contrast with aleatoric uncertainty regarding blend sources).
- The parsimony principle: reducing inputs from 16 features to the 1-feature RAI.

---

## 3. Missing Information
- None.

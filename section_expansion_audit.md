# TARS v1 Section Expansion Audit

This document details the gap analysis between the current condensed manuscript and the available repository evidence, setting the baseline for the expansion.

---

### 1. Introduction
- **Current pages**: ~1 page
- **Evidence available**: `TARS_PRODUCTION_ARCHITECTURE_V1.md`, `SCIENTIFIC_OBJECTIVES.md`
- **Missing analyses**: Historical evolution, pipeline context, epistemic vs. aleatoric uncertainty, motivation for graph representations.
- **Missing figures**: Figure 1 (TARS 5-stage architecture flow).
- **Missing tables**: None.
- **Missing discussion**: Computational bottlenecks of prior pipelines.
- **Expansion priority**: High.

---

### 2. Related Work
- **Current pages**: ~1 page
- **Evidence available**: `REVIEWER_ATTACK_MATRIX.md`, `NOVELTY_DEFENSE.md`, `STAGE1_OPERATING_BOUNDARIES.md`, `STAGE2_LIMITATIONS.md`
- **Missing analyses**: Extended comparisons with Robovetter, Autovetter, Astronet, Vespa, and Triceratops.
- **Missing figures**: None.
- **Missing tables**: Table 1 (Novelty matrix).
- **Missing discussion**: Detailed comparison across feature count, runtime complexity, and calibration profiles.
- **Expansion priority**: High.

---

### 3. Methodology
- **Current pages**: ~1.5 pages
- **Evidence available**: `RECOVERY_AMBIGUITY_INDEX.md`, `CANDIDATE_FAMILY_ENTROPY.md`, `STAGE3_FINAL_BLUEPRINT.md`, `FORMULA_AUDIT.md`
- **Missing analyses**: Step-by-step candidate recovery, connected component extraction, detailed equations (E-01 to E-08), standardization, and logistic calibration parameters.
- **Missing figures**: Figure 2 (Alias graph nodes and edges).
- **Missing tables**: None.
- **Missing discussion**: Frozen parameters leakage prevention.
- **Expansion priority**: Critical.

---

### 4. Results
- **Current pages**: ~2 pages
- **Evidence available**: `BOOTSTRAP_STABILITY_ANALYSIS.md`, `RAI_COMPONENT_ABLATION.md`, `CALIBRATION_ANALYSIS.md`, `SENSITIVITY_ANALYSIS.md`, `NOISE_JITTER_PERTURBATION.md`, `RECOVERY_CURVE_VERIFICATION.md`, `GIANT_STAR_FAILURE_ANALYSIS.md`, `RAI_ONLY_DOMINANCE_ANALYSIS.md`
- **Missing analyses**: Individual standalone subsections for:
  - Overall Performance (Bootstrap)
  - Component Ablation Study
  - Reliability & Calibration Analysis
  - CMI Information-Theoretic Redundancy
  - Noise & Jitter Perturbation Robustness
  - Subgroup Recovery Verification (Period, mag, SNR)
  - Giant Star Failure Analysis
  - Forward Feature Selection Trace
- **Missing figures**: Figure 3 (Bootstrap AUROCs), Figure 4 (Reliability curve), Figure 5 (Perturbation curves), Figure 6 (Dwarf vs Giant graphs).
- **Missing tables**: Table 2 (Model metrics), Table 3 (Ablation study), Table 4 (Reliability data), Table 5 (Discretization sensitivity), Table 6 (Perturbation data), Table 7 (Subgroups), Table 8 (Giant star comparison), Table 9 (Forward selection trace).
- **Missing discussion**: Unit-mismatch scale anomaly, physical failure mechanisms.
- **Expansion priority**: Critical.

---

### 5. Discussion
- **Current pages**: ~1 page
- **Evidence available**: `REVIEWER_ATTACK_MATRIX.md`, `STAGE3_SCIENTIFIC_CLOSURE.md`
- **Missing analyses**: Detailed operational integration, PLATO/Roman implications, and information-theoretic parsimony.
- **Missing figures**: None.
- **Missing tables**: None.
- **Missing discussion**: CPU-hour savings and telescope scheduling optimization.
- **Expansion priority**: Medium.

---

### 6. Limitations
- **Current pages**: ~0.5 pages
- **Evidence available**: `LIMITATIONS_AND_NONCLAIMS.md`, `REVIEWER_ATTACK_MATRIX.md`
- **Missing analyses**: Systematic categorization of Dataset, Physical, Methodological, Statistical, Computational, and External validity limitations.
- **Missing figures**: None.
- **Missing tables**: None.
- **Missing discussion**: Threats to validity (Internal, External, Construct).
- **Expansion priority**: High.

---

### 7. Appendix
- **Current pages**: ~1.5 pages
- **Evidence available**: `FORMULA_AUDIT.md`, `PERIOD_RECOVERY_ARCHITECTURE.md`, `FAILURE_MODES_STAGE3.md`
- **Missing analyses**: Stage 3 algorithm pseudocode, complete math derivations for graph entropy, CMI, and joint entropy, failure galleries.
- **Missing figures**: Failure gallery examples.
- **Missing tables**: Complete reproducibility parameters, TIC list.
- **Missing discussion**: Machine-precision agreement details.
- **Expansion priority**: Critical.

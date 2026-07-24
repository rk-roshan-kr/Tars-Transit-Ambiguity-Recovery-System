# TARS v1 Code Traceability Map

This map traces forward from source scripts and functions through output artifacts to paper sections and claim IDs.

---

### `run_ambiguity_reconstruction.py`
*   `extract_ambiguity_features_single()` (L44–246)
    *   $\rightarrow$ Output: `ambiguity_candidates_raw.csv`
    *   $\rightarrow$ Section: Methodology §3.2 & 3.3
    *   $\rightarrow$ Claim IDs: **C-01**

### `run_production_consolidation.py`
*   `expected_calibration_error()` (L34–47)
    *   $\rightarrow$ Output: `real_labeled_features.csv`, `blind_labeled_features.csv`
    *   $\rightarrow$ Section: Methodology §3.6
    *   $\rightarrow$ Claim IDs: **C-02**

### `run_publication_readiness.py`
*   `prod_conditional_mutual_information()` (L46–54)
    *   $\rightarrow$ Output: `SENSITIVITY_ANALYSIS.md`
    *   $\rightarrow$ Section: Results §4.6
    *   $\rightarrow$ Claim IDs: **C-03**
*   `compute_z_scores()` (L132–139)
    *   $\rightarrow$ Output: `RECOVERY_CURVE_VERIFICATION.md`
    *   $\rightarrow$ Section: Results §4.8
    *   $\rightarrow$ Claim IDs: **C-04**
*   `main()` (bootstrap stability loop) (L347–369)
    *   $\rightarrow$ Output: `BOOTSTRAP_STABILITY_ANALYSIS.md`, `Figure1.png`
    *   $\rightarrow$ Section: Results §4.2 & 4.3
    *   $\rightarrow$ Claim IDs: **C-02**
*   `main()` (giant star cohort split) (L686–705)
    *   $\rightarrow$ Output: `GIANT_STAR_FAILURE_ANALYSIS.md`
    *   $\rightarrow$ Section: Results §4.9 & Limitations §6.2
    *   $\rightarrow$ Claim IDs: **C-05**

### `run_independent_verification.py`
*   `main()` (independent agreement checks)
    *   $\rightarrow$ Output: `FINAL_VERIFICATION_REPORT.md`
    *   $\rightarrow$ Section: Appendix C & F
    *   $\rightarrow$ Claim IDs: **C-01** to **C-05**

### `reproduce.ps1`
*   Master shell runner
    *   $\rightarrow$ Output: Programmatic clean state and assets regeneration
    *   $\rightarrow$ Section: Appendix E
    *   $\rightarrow$ Claim IDs: All claims

# TARS v1 Function Claim Index

This index maps key scientific functions in the TARS codebase directly to their purpose, calling scripts, manuscript sections, and supported claims.

---

| Function Name | Purpose | Calling Scripts | Manuscript Sections | Supported Claims |
| :--- | :--- | :--- | :---: | :---: |
| `prod_shannon_entropy()` | Computes Shannon entropy on degree arrays or binned feature vectors. | `run_publication_readiness.py` | Appendix A.2 | **C-01**, **C-03** |
| `prod_conditional_mutual_information()` | Computes the Conditional Mutual Information $I(Y; FC \mid z_{\text{RAI}})$. | `run_publication_readiness.py` | Results §4.6 & Appendix A.4 | **C-03** |
| `expected_calibration_error()` | Computes Expected Calibration Error (ECE) across prediction bins. | `run_publication_readiness.py`, `run_production_consolidation.py` | Results §4.5 & Methodology §3.6 | **C-02** |
| `compute_z_scores()` | Standardizes validation features using frozen training parameters ($\mu_i, \sigma_i$). | `run_publication_readiness.py` | Methodology §3.4 & Results §4.8 | **C-04** |
| `compute_custom_rai()` | Combines standardized sub-features using sign conventions. | `run_publication_readiness.py` | Methodology §3.4 & Results §4.4 | **C-01**, **C-02** |
| `evaluate_perturbation()` | Simulates Gaussian noise, dropouts, and systematic biases to measure performance decay. | `run_publication_readiness.py` | Results §4.7 | **C-02** |
| `calculate_uncertainty()` | Executes Weighted Least Squares (WLS) fit to return refined epoch and period uncertainty $\sigma_P$. | `run_ambiguity_reconstruction.py`, `test_models.py` | Methodology §3.2 | **C-01** |
| `compute_stability()` | Calculates residuals standard deviation and fractional Median Absolute Deviation (MAD/P). | `run_ambiguity_reconstruction.py`, `test_models.py` | Methodology §3.2 | **C-01** |
| `resolve_alias_pair()` | Implements the 3-rule preference hierarchy for harmonic alias tie-breaking. | `run_ambiguity_reconstruction.py` | Methodology §3.2 | **C-01** |

# TARS v1 Scientific Provenance Ledger

This master ledger connects every scientific claim in the TARS v1 manuscript directly to its exact direct code evidence, runtime outputs, and publication figures/tables.

---

| Claim ID | Claim | Manuscript Section | Script | Function | File | Line Range | Artifact | Figure/Table | Status |
| :---: | :--- | :---: | :--- | :--- | :--- | :---: | :--- | :---: | :---: |
| **C-01** | Exoplanet signal recovery ambiguity can be isolated and quantified as a single, physically interpretable graph-derived index ($z_{\text{RAI}}$) constructed from five standardized sub-features. | Sec 3.2 & 3.3 | `run_ambiguity_reconstruction.py` | `extract_ambiguity_features_single()` | `recoverer.py`, `harmonic_resolver.py` | L44–246 (script), L30–242 (source) | `ambiguity_candidates_raw.csv` | Figure 4 | **Directly verified** |
| **C-02** | The univariate RAI-only model achieves comparable ranking performance (mean AUROC = $0.6621 \pm 0.0694$) and superior calibration (mean ECE = $0.0646$) relative to a complex 16-feature Linear Stack (AUROC = $0.6243 \pm 0.0818$) on the blind validation partition. | Sec 4.2 & 4.3 | `run_publication_readiness.py` | `main()` (bootstrap stability loop) | `run_publication_readiness.py` | L347–369 | `BOOTSTRAP_STABILITY_ANALYSIS.md` | Table 3, Figure 5 | **Directly verified** |
| **C-03** | Legacy feature families contain no unique predictive information after controlling for the RAI within the evaluated Blind Validation Partition (Conditional Mutual Information $p \ge 0.20$). | Sec 4.6 | `run_publication_readiness.py` | `prod_conditional_mutual_information()` | `run_publication_readiness.py` | L46–54 & L474–492 | `SENSITIVITY_ANALYSIS.md` | Table 6, Figure 8 (Supplement) | **Directly verified** |
| **C-04** | Standardizing the sub-features using Z-scores isolates the classifier from raw scale anomalies (such as the parts-per-million vs. fractional flux SNR mismatch). | Sec 4.8 | `run_publication_readiness.py` | `compute_z_scores()` | `run_publication_readiness.py` | L132–139 | `RECOVERY_CURVE_VERIFICATION.md` | Table 8 | **Supported with inference** |
| **C-05** | Convective noise on giant host stars deforms the candidate graph topology, defining the physical boundary of the index's applicability. | Sec 4.9 & 6.2 | `run_publication_readiness.py` | `main()` (giant star cohort split) | `run_publication_readiness.py` | L686–705 | `GIANT_STAR_FAILURE_ANALYSIS.md` | Table 9, Figure 10 | **Directly verified** |

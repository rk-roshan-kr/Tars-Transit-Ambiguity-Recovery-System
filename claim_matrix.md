# TARS v1 Claim Matrix

This document maps all major scientific claims in the TARS v1 manuscript to their respective types, source sections, evidence targets, and verification statuses under the TARS Scientific Standard (TSS) v1.0.

---

| Claim ID | Claim Statement | Type | Source Section | Evidence / Equation / Table | Verification Status |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **C-01** | Recovery ambiguity can be isolated as a distinct, measurable graph-theoretic quantity. | **Mathematical** | Sec 3.1 | Equations (E-01) to (E-05) | **VERIFIED** |
| **C-02** | The univariate RAI-only model achieves comparable ranking performance (AUROC = 0.6621) and superior calibration (ECE = 0.0646) compared to a complex 16-feature stack. | **Empirical** | Sec 4.1 | Table 3, Figure 5 | **VERIFIED** |
| **C-03** | Legacy morphology features are statistically redundant once recovery ambiguity is controlled for (CMI is non-significant, $p \ge 0.20$ across sweeps). | **Empirical** | Sec 4.3 | Table 6 | **VERIFIED** |
| **C-04** | Z-score standardization on training stats isolates the classifier from raw scale anomalies (such as the ppm vs. fractional flux SNR mismatch). | **Interpretation** | Sec 4.4 | Table 8 | **VERIFIED** |
| **C-05** | Giant and subgiant host stars limit the index due to convective granulation noise producing false candidate multiplicity. | **Physical** | Sec 4.5 | Table 9 | **VERIFIED** |
| **C-06** | The RAI can serve as a lightweight pre-screening metric before more computationally intensive MCMC validation methods such as Vespa or Triceratops. | **Interpretation** | Sec 5.2 | Discussion | **VERIFIED** |
| **C-07** | Greedily adding legacy features beyond Step 4 systematically degrades the Blind Validation Partition AUROC from $0.6943$ down to $0.5868$ due to collinear overfitting. | **Empirical** | Sec 4.10 | Table 10 | **VERIFIED** |
| **C-08** | Independent validation on Kepler, K2, and PLATO will be required before claiming cross-mission generalization. | **Future Work** | Sec 6.6 | Limitations | **VERIFIED** |

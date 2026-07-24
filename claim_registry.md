# TARS v1 Claim Registry

This registry registers all core scientific claims asserted in the TARS v1 manuscript.

---

### C-01: Ambiguity Isolation
*   **Statement**: Exoplanet signal recovery ambiguity can be isolated and quantified as a single, physically interpretable graph-derived index ($z_{\text{RAI}}$) constructed from five standardized sub-features.
*   **Manuscript Section**: Abstract, Methods §3.2 & 3.3, Appendix A.1
*   **Support Type**: **Directly verified**
*   **Verification Evidence**: Stage 3 candidate period alias graph construction and component analysis.
*   **Qualifiers**: Applies to the evaluated TESS pipeline and candidate search parameters.

---

### C-02: Ranking and Calibration Performance
*   **Statement**: The univariate RAI-only model achieves comparable ranking performance (mean AUROC = $0.6621 \pm 0.0694$) and superior calibration (mean ECE = $0.0646$) relative to a complex 16-feature Linear Stack (AUROC = $0.6243 \pm 0.0818$) on the blind validation partition.
*   **Manuscript Section**: Abstract, Results §4.2 & 4.3, Table 3
*   **Support Type**: **Directly verified**
*   **Verification Evidence**: 1,000 bootstrap resamples on the independent $N=175$ Blind Validation Partition.
*   **Qualifiers**: Within the evaluated TESS Blind Validation Partition and validation protocol; observed bootstrap distributions overlap substantially.

---

### C-03: Information-Theoretic Redundancy
*   **Statement**: Legacy feature families contain no unique predictive information after controlling for the RAI (Conditional Mutual Information $p \ge 0.20$).
*   **Manuscript Section**: Abstract, Results §4.6, Table 6, Appendix A.4
*   **Support Type**: **Directly verified**
*   **Verification Evidence**: CMI discretization sensitivity sweep across bin counts $K \in [4, 20]$ with 1,000 permutation null shuffles.
*   **Qualifiers**: Within the evaluated Blind Validation Partition, feature family, and validation protocol.

---

### C-04: Normalization Robustness
*   **Statement**: Standardizing the sub-features using Z-scores isolates the classifier from raw scale anomalies (such as the parts-per-million vs. fractional flux SNR mismatch).
*   **Manuscript Section**: Results §4.8, Table 8
*   **Support Type**: **Supported with inference**
*   **Verification Evidence**: The model was completely insulated from the $10^6$ scale mismatch because downstream features are normalized using frozen training statistics.
*   **Qualifiers**: Applies within the evaluated pipeline.

---

### C-05: Giant Host Star Boundary
*   **Statement**: Convective noise on giant host stars deforms the candidate graph topology, defining the physical boundary of the index's applicability.
*   **Manuscript Section**: Abstract, Results §4.9, Table 9, Limitations §6.2
*   **Support Type**: **Directly verified**
*   **Verification Evidence**: Comparison of dwarf vs. giant host star ambiguity profiles (giant stars exhibit higher event count and denser alias graphs).
*   **Qualifiers**: Evaluated on the $N_{\text{stars}}=60$ Blind Validation Partition.

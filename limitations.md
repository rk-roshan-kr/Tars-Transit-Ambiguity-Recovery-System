# 6. Limitations and Threats to Validity

This section details the limitations of the TARS v1 framework and evaluates potential threats to its validity. Isolating and documenting these boundaries is a requirement of the TARS Scientific Standard (TSS) v1.0, ensuring that our claims remain proportionate to the empirical evidence.

---

## 6.1. Dataset Limitations
*   **TESS Cadence and Scope** (*Limitation of the available data*): The empirical validation presented in this work is restricted to light curves observed by the Transiting Exoplanet Survey Satellite (TESS). TESS light curves are monitored at cadences of 2 minutes and 20 seconds. The short duration of TESS sector observations (typically 27 days per sector) limits our ability to evaluate recovery ambiguity on long-period candidates ($P > 20$ days) where transit events are sparse.
*   **Sample Size and Class Balance** (*Limitation of the current evaluation*): Our Blind Validation Partition consists of $N = 175$ light curves across $N_{\text{stars}} = 60$ unique systems. While this sample size is sufficient to establish ranking performance and calibration (AUROC = 0.6621), the small count of confirmed planets (Tier A targets) in the Blind Validation Partition leads to large standard errors and confidence intervals under bootstrap resampling.

---

## 6.2. Physical Limitations
*   **Giant and Subgiant Host Stars** (*Inherent limitation of TARS*): As demonstrated in Section 4.9, the model exhibits performance collapse when evaluated on giant and subgiant host stars. These stars exhibit low-frequency convective granulation noise and photospheric oscillations. The Stage 3 period recovery algorithm misinterprets this convective noise as transits, leading to severe event inflation (46.07 events vs. 37.92 in dwarfs) and candidate multiplicity. This breaks the ambiguity assumptions of the RAI.
*   **Transit Timing Variations (TTVs)** (*Inherent limitation of TARS*): TARS assumes a rigid linear ephemeris ($t_k = T_0 + k \cdot P$). In dynamically active multi-planet systems, gravitational interactions between planets introduce Transit Timing Variations (TTVs). If these variations exceed our timing phase window, the stability engine fails to fit a linear ephemeris, resulting in the false rejection of true planet candidates (forensics register `FAILURE_TIMING_ERROR_EXPLOSION`).
*   **High-Frequency Pulsators and Eclipsing Binaries** (*Inherent limitation of TARS*): Rapid stellar pulsations or eclipsing binaries with highly eccentric orbits and asymmetric depths can mimic or deform transit shapes, creating complex connected components in the alias network that distort graph entropy calculations.

---

## 6.3. Methodological Limitations
*   **Harmonic Search Boundaries** (*Inherent limitation of TARS*): The harmonic matching algorithm is restricted to integer ratios $r \in \{2, 3, 4, 5\}$. While this covers the most common periodogram aliases, it fails to capture higher-order aliases (e.g., $r = 6$) or fractional aliases (e.g., $3/2$ or $4/3$ resonances). 
*   **Fixed Match Tolerance** (*Inherent limitation of TARS*): The tolerance is fixed at $\epsilon = 0.05$. A wider tolerance would falsely link independent candidates, while a tighter tolerance would fail to link related aliases under timing scatter.
*   **Frozen Standardization Statistics** (*Limitation of the current evaluation*): The Z-score standardization parameters ($\mu_i, \sigma_i$) and logistic coefficients ($\beta_0 = 0.5410, \beta_1 = 0.1582$) are frozen from our training set partition. If the pipeline is deployed on stellar populations with significantly different noise profiles, these parameters may lose calibration.

---

## 6.4. Statistical Limitations
*   **Bootstrap Assumptions** (*Limitation of the current evaluation*): Bootstrap resampling assumes that the empirical distribution of our Blind Validation Partition is a representative proxy for the true underlying population. If our evaluation partition contains selection biases (e.g. over-representation of bright, high-SNR targets), the bootstrap confidence intervals will be overly optimistic.
*   **Calibration and Discretization** (*Limitation of the current evaluation*): Expected Calibration Error (ECE) is sensitive to the number of bins $M$ and the bin boundary locations. Conditional Mutual Information (CMI) calculation requires discrete partitions; while our sensitivity sweeps across $K \in [4, 20]$ show that the redundancy result is robust, CMI estimates can still be biased by finite-sample sizes.

---

## 6.5. Computational Limitations
*   **$O(N^2)$ Graph Scaling** (*Inherent limitation of TARS*): Pairwise period comparisons in the alias graph scale quadratically with candidate count. While the number of surviving candidates is small ($N_{\text{final}} < 200$), making the calculation extremely fast ($< 0.1$ s), scaling this to massive all-sky catalogs with un-pruned period grids may introduce computational bottlenecks.

---

## 6.6. Threats to Validity
*   **Internal Validity** (*Limitation of the current evaluation*): Threats include preprocessing assumptions (detrending spline timescales) and label quality. If the labels in the master registry contain misclassifications, the classification weights will be biased. Additionally, data gap dropouts can falsely truncate period networks, triggering `FAILURE_GAP_DROPOUT` forensic flags that distort stability counts.
*   **External Validity** (*Limitation of the current evaluation*): Threats concern the generalization of the frozen Z-score parameters to other stellar populations or instrument cadences. An instrument-specific shift in TESS systematics could invalidate the calibration slope. The present results should be interpreted as applying to the evaluated TESS Blind Validation Partition. Independent validation on additional missions (such as Kepler and PLATO) will be required before claims of cross-mission generalization can be made.
*   **Construct Validity** (*Inherent limitation of TARS*): Concerns whether the five sub-features fully capture "recovery ambiguity." Alternate graph representations (e.g., directed graphs reflecting period search directions) or alternative entropy measures (e.g., Rényi or Tsallis entropy) could provide different representations of signal uncertainty.

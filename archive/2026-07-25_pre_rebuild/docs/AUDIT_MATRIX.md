# Stage 1 Audit Conclusion Matrix

This document maps the major conclusions and observations from the Phase 2.3 Scientific Audit of **TARS Core Stage 1 (Signal Conditioning & Noise Characterization)**. Every finding is classified according to the Audit Severity Framework to prioritize future work.

## Audit Severity Framework

* **LEVEL 0**: No issue found.
* **LEVEL 1**: Minor documentation issue (requires doc update).
* **LEVEL 2**: Metric interpretation issue (does not invalidate physical signal, but metrics require correction/clarification).
* **LEVEL 3**: Scientific assumption issue (requires adjustments to assumptions/priors).
* **LEVEL 4**: Invalidates operating-envelope conclusion (requires recalculation of specific boundary limits).
* **LEVEL 5**: Invalidates Stage 1 (requires structural logic overhaul of detrending/noise algorithms).

---

## Conclusion Matrix

| Conclusion / Finding | Survived? | Severity | Description & Justification |
| :--- | :--- | :--- | :--- |
| **Depth Boundary** | YES | **LEVEL 0** | The minimum recoverable transit depth boundary ($\ge 2.0\%$ for synthetic noise, $\ge 1.5\%$ for quiet TESS) is statistically robust. Verified via seed sweeps and false discovery checks. |
| **Duration Boundary** | YES | **LEVEL 0** | Transits with durations $\le 4.0$ hours are cleanly recovered. Long-duration transits ($\ge 22.0$ hours) suffer from severe filter-induced self-clipping. |
| **Variability Boundary** | PARTIAL | **LEVEL 2** | Extreme errors ($80\%\text{--}1800\%$) for variable stars are exaggerated by the relative depth error metric at shallow depths, but physical residuals are still present (absolute bias $\sim 0.001\text{--}0.002$). |
| **Stellar Spot Detrending Claim** | NO | **LEVEL 3** | The assumption that sliding median filters clean all stellar spot modulations is invalid. High-frequency or large-amplitude spots leave systematic residuals that corrupt transit depths. |
| **Statistical CI Stability** | YES | **LEVEL 0** | 95% bootstrap confidence intervals converge cleanly at $N_{\rm boot} \ge 1000$. Lower resample sizes ($N_{\rm boot} < 250$) show elevated variance in width estimates. |
| **Numerical Reproducibility** | YES | **LEVEL 0** | Operating boundaries are fully reproducible across multiple random seeds, Python, and NumPy versions (no machine mocking used). |
| **Boundary Significance** | YES | **LEVEL 0** | Shuffling transit associations (Track H) results in the complete divergence or absence (`nan`) of boundaries, yielding a p-value of $p < 0.01$. |
| **Detrending Performance** | YES | **LEVEL 0** | TARS Median filter detrending significantly outperforms Savitzky-Golay and Lightkurve `flatten()` by minimizing transit self-clipping (6.3% depth error vs 24% for Savitzky-Golay). |

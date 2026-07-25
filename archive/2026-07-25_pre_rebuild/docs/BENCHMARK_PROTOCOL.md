# Benchmark Fairness Protocol

This document establishes the scientific protocols for comparative evaluations between **TARS Core Stage 1** and competitor signal conditioning algorithms (e.g., standard Savitzky-Golay, Spline-fitting, and Lightkurve equivalents).

---

## 1. Competitor Algorithm Specifications

To ensure a fair benchmark, all competitor algorithms must be configured with equivalent sliding window timescales. 

### A. Savitzky-Golay (SG) Filter
* **Window Length**: Equivalent to `detrend_window_days` (1.0 day). In cadences, this translates to $N_{\rm window} = 1.0\text{ day} / \Delta t$.
* **Polynomial Order**: $d = 2$ (standard for local transit preservation).
* **NaN Handling**: Linear interpolation must be applied to NaNs prior to filtering, and the NaNs must be re-inserted post-filter to avoid trend leakage or polynomial explosion.

### B. Cubic Spline Fitting
* **Knot Spacing**: $1.0$ day (equivalent to the median filter window duration).
* **Iterative Re-weighting**: Must use 3-sigma rejection iterations to prevent transit events from pulling the spline trend downward.
* **Weights**: Per-point weights set to $1 / \sigma_i^2$.

### C. Lightkurve flatten() Equivalent
* **Window Length**: $1.0$ day.
* **Break Tolerance**: $0.5$ days (splitting light curves at gaps to avoid filtering across downlink interruptions).

---

## 2. Metric Uniformity

All models must be evaluated using the exact same downstream recovery metrics to prevent bias:
* **Transit Depth Recovery**: Evaluated using the robust median-based estimator defined in `evaluate_transit_recovery` in [test_stage1_conditioning.py](file:///d:/TARS/TarsCore/tests/test_stage1_conditioning.py).
* **Depth Error**: Computed as absolute percentage error relative to the true injected depth:
$$\text{Error} = \frac{|D_{\rm recovered} - D_{\rm true}|}{D_{\rm true}} \times 100\%$$

---

## 3. Environmental Metadata Logging

To prevent machine-specific bias from skewing comparative metrics (e.g. CPU speeds, memory cache sizes, library compilation flags), every benchmark run must record the following software metadata in the run directory's `PROVENANCE_MANIFEST.json`:
* **Python Interpreter**: Executable path and full version string (including build compiler).
* **Scientific Stack**: Exact versions of `numpy`, `scipy`, `pandas`, `scikit-learn`, `astropy`.
* **Hardware Architecture**: CPU details (cores, frequency) and operating system kernel version.

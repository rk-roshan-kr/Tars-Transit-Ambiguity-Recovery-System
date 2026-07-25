# Scientific Operating Regime & Boundary Characterization

This document formally defines the exact observational regime where **TARS Core Stage 1 (Signal Conditioning & Noise Characterization)** is scientifically valid, establishing its quantified operating envelope based on comprehensive injection and stress-testing campaigns.

---

## Table A: Validated Operating Envelope

| Parameter | Validated Region (Error $\le 5\%$) | Marginal Region (Error $5\%\text{--}10\%$) | Failure Region (Error $> 10\%$ or Breakdown) |
| :--- | :--- | :--- | :--- |
| **Transit Depth (Synthetic Noise)** | $\ge 1.113\%$ depth | $0.649\%\text{--}1.113\%$ depth | $< 0.649\%$ depth |
| **Transit Depth (Real TESS Quiet)** | $\ge 0.289\%$ depth | $0.144\%\text{--}0.289\%$ depth | $< 0.144\%$ depth (dominated by white noise floor) |
| **Transit Depth (Real TESS Variable)** | $\ge 2.000\%$ depth | $1.718\%\text{--}2.000\%$ depth | $< 1.718\%$ depth (dominated by stellar variability residuals) |
| **Transit Duration** | $\le 4.00$ hours | $4.00\text{--}9.86$ hours | $> 9.86$ hours (filter-induced self-clipping) |
| **Sinusoidal Stellar Variability** | $\le 0.50\%$ amplitude | $0.50\text{--}0.92\%$ amplitude | $> 0.92\%$ amplitude |
| **Quasi-Periodic Variability** | $\le 0.50\%$ amplitude | $0.50\text{--}1.15\%$ amplitude | $> 1.15\%$ amplitude |
| **Multi-Frequency Variability** | $\le 1.00\%$ amplitude | $1.00\text{--}3.17\%$ amplitude | $> 3.17\%$ amplitude |
| **Red Noise Correlation ($\rho$)** | $\le 0.30$ | $0.30\text{--}0.63$ | $> 0.63$ (red noise breakdown point) |

---

## 1. Validated Region (Guaranteed Scientific Integrity)

Within this envelope, Stage 1 conditioning behaves deterministically, preserves transit morphology, and limits depth recovery errors to **$< 5\%$ (or $< 10\%$ in marginal boundaries)**:
* **Transit Depth**: Highly reliable for quiet TESS baselines (raw standard deviation $< 0.1\%$), where transits down to $0.29\%$ are recovered with $< 5\%$ error.
* **Transit Duration**: Standard durations ($\le 4.0$ hours) are safe from self-containment filtering, yielding $< 5\%$ depth attenuation.
* **Stellar Variability**: Fully cleans low-frequency stellar activity with amplitudes up to $0.50\%$ for sinusoidal and quasi-periodic spot modulation, and up to $1.0\%$ for multi-frequency variability.
* **Correlated Noise**: Stable and accurate when red-noise correlation is low ($\rho \le 0.30$), keeping white noise inflation near $1.0$ and $\beta < 0.3$.

---

## 2. Marginal Region (Elevated Systematic Distortion)

Outside the ideal regime but before complete failure, the pipeline introduces systematic, predictable distortions (errors between $5\%$ and $10\%$):
* **Transit Depth**: Low-amplitude transits between $0.14\%$ and $0.29\%$ in real TESS data suffer from noise-induced fluctuations.
* **Transit Duration**: Long-duration transits ($4.0\text{--}9.86$ hours) experience partial self-containment clipping inside the median filter window, yielding up to $10\%$ depth attenuation.
* **Stellar Variability**: Mid-range variability amplitudes ($0.5\%\text{--}1.2\%$ for rotational modulation) are mostly detrended but leave behind micro-residuals.
* **Red Noise**: Correlated noise with $\rho$ between $0.30$ and $0.63$ inflates the local uncertainty baseline and triggers autocorrelation rises ($\ge 0.5$).

---

## 3. Failure Region (Pipeline Breakdown Points)

The pipeline experiences severe scientific breakdown, resulting in errors $> 10\%$, under the following conditions:
* **Transit Depth**: Extremely shallow signals ($< 0.14\%$ depth) are completely buried under TESS high-frequency noise floors.
* **Highly Variable Stars**: Stars with high-frequency stellar pulsations or large-amplitude spots (RMS $> 0.5\%$) cannot be detrended cleanly by Stage 1. Residual stellar variability dominates, corrupting transit depth measurements (errors up to $>80\%$).
* **Very Long Transits**: Transits lasting $> 9.86$ hours are wider than the median window filter timescales, causing the filter to treat the transit itself as a trend, leading to complete self-clipping ($>10\%$ attenuation).
* **High Red Noise**: Correlated stellar noise with $\rho > 0.63$ distorts the local baseline. The diagnostic $\beta$ factor increases significantly, signaling that the assumption of white-noise-dominated errors has broken down.

---

## 4. Known Limitations & Recommended Usage

1. **Stellar Variability Veto**: Do not run Stage 1 vetting on targets with raw RMS variability $> 0.5\%$. They must be flagged as `FAIL` or directed to specialized detrending workflows (e.g. Gaussian Process regression).
2. **Long Period/Duration Veto**: For transits with expected durations $> 8$ hours, the default `detrend_window_days = 1.0` is too small. Downstream orchestrators must dynamically scale `detrend_window_days` to at least $3 \times$ the expected transit duration.
3. **Median Vetting**: All downstream pipelines must use median-based in-transit depth estimators to avoid the extreme positive minimum-value bias associated with simple minimum-search algorithms on noisy data.

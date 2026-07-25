# Stage 1 Scientific Limitations & Unsupported Regimes

This document details the quantified physical limits, failure modes, and unsupported observational regimes for **TARS Core Stage 1 (Signal Conditioning & Noise Characterization)**. These limits are established to prevent downstream planet search algorithms from using corrupted data.

---

## 1. Quantified Physical Limits

### Minimum Recoverable Transit Depth
* **Limit**: $< 0.14\%$ in real TESS quiet baselines ($< 0.65\%$ in synthetic noise sweep).
* **Failure Mode**: At shallower depths, the transit signal is completely buried under the high-frequency noise floor. While the median estimator is unbiased, statistical fluctuations dominate recovery at this scale.
* **Prescription**: Veto any transit search for candidates with expected depths $< 0.15\%$ on raw standard deviation $\ge 0.1\%$ targets.

### Maximum Transit Duration
* **Limit**: $> 9.86$ hours (for default `detrend_window_days = 1.0`).
* **Failure Mode**: When the transit duration is comparable to or wider than the median filter window, the filter treats the transit itself as a low-frequency stellar trend. This leads to complete self-clipping (depth attenuation $> 10\%$).
* **Prescription**: The orchestrator must scale `detrend_window_days` to at least $3 \times$ the expected transit duration for long-duration candidates.

### Maximum Stellar Variability Amplitude
* **Limit**: Raw RMS variability $> 0.5\%$ (or sinusoidal amplitude $> 0.9\%$).
* **Failure Mode**: Sliding median filters are mathematically incapable of cleaning high-frequency stellar pulsations or rotational modulations with large amplitudes. Troughs and peaks systematically overlap with the transit profile, leaving behind residuals (amplitude $\sim 0.001\text{--}0.002$) that distort transit depths.
* **Prescription**: Automatically veto targets with raw RMS variability $> 0.5\%$. Direct these targets to specialized detrending workflows (e.g., Gaussian Processes).

---

## 2. Supported vs. Unsupported Regimes

| Observational Regime | Supported? | Vetting Action / Workaround |
| :--- | :--- | :--- |
| **Quiet Stars (RMS < 0.1%)** | YES | Direct processing via Stage 1. |
| **Short-duration transits (< 4h)** | YES | Direct processing via Stage 1. |
| **Shallow candidates (< 0.5% depth)** | MARGINAL | Apply noise-bias depth correction. |
| **Long-duration transits (> 8h)** | NO (with default window) | Dynamically scale detrending window to $3\times$ duration. |
| **Highly variable stars (RMS > 0.5%)** | NO | Veto from Stage 1; route to Gaussian Process detrending. |
| **High Red Noise correlation ($\rho > 0.63$)** | NO | Flag as `RED_NOISE_REJECT`; local uncertainty baseline is invalid. |

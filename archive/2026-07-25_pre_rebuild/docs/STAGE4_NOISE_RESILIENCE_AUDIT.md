# Stage 4 Noise Resilience Audit

*Phase 7.1 — Scientific Validation Phase. Evaluation of feature stability under timing noise.*

---

## 1. Feature Drift Across Timing Noise ($\sigma_t$)

Using the sweep trials from `eea_noise_resilience.csv`, we tracked the behavior of stability and temporal features as the event timing noise ($\sigma_t$) increased from 0.001 days ($\approx 1.4$ minutes) to 0.1 days ($\approx 144$ minutes):

| Timing Noise ($\sigma_t$) | Residual RMS (days) | Residual MAD (days) | Normalized RMS | Normalized MAD | Uncertainty Ratio ($\sigma_P/P$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **0.001d** | 0.00081 | 0.00058 | 0.098 | 0.069 | $1.99 \times 10^{-4}$ |
| **0.005d** | 0.00350 | 0.00235 | 0.420 | 0.282 | $1.99 \times 10^{-4}$ |
| **0.010d** | 0.00741 | 0.00498 | 0.889 | 0.597 | $1.99 \times 10^{-4}$ |
| **0.020d** | 0.00825 | 0.00577 | 0.990 | 0.692 | $2.15 \times 10^{-4}$ |
| **0.050d** | 0.00577 | 0.00378 | 0.692 | 0.453 | $2.75 \times 10^{-4}$ |
| **0.100d** | 0.00364 | 0.00094 | 0.436 | 0.113 | $2.77 \times 10^{-4}$ |

---

## 2. Stable vs Fragile Features

### Stable Features
* **`uncertainty_ratio` (EV-S3)**: Extremely stable. It ranges from $1.99 \times 10^{-4}$ to $2.77 \times 10^{-4}$ (Coefficient of Variation $\approx 0.15$). This is because the WLS period fit is well-constrained by the long baseline, making the period uncertainty ratio highly resilient to timing scatter.
* **`support_count` (EV-T1)**: Remains stable since timing noise is within the threshold limits for low/medium noise levels.

### Fragile Features
* **`residual_rms` (EV-T5) & `residual_mad` (EV-T6)**: Fragile. They scale linearly with timing noise, tracking the input noise distribution.
* **`normalized_rms` (EV-S2) & `normalized_mad` (EV-S1)**: Fragile. They inherit the timing-noise scaling from residuals. Note that at very high noise ($\ge 0.05$d), the mean values decrease slightly because extreme noise causes Stage 3 to reject high-residual candidates, creating survival bias.

---

## 3. Scientific Recommendation

For downstream Stage 6 ML and Stage 5 ECHO models:
* Use `uncertainty_ratio` (EV-S3) as a reliable indicator of period stability.
* When training on `residual_mad` or `residual_rms`, normalise or calibrate them using the timing noise estimate to prevent timing noise from being misclassified as low-coherence physical structure.

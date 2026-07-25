# Stage 1 Empirical Operating Boundaries

This document compiles the citable empirical operating boundaries for **TARS Core Stage 1 (Signal Conditioning & Noise Characterization)**. These limits are calibrated using large-scale injection simulations and real TESS population audits under the locked default configuration.

> [!NOTE]
> These boundaries are **empirical limits** specific to the locked default parameters (`detrend_window_days=1.0`, `noise_window_days=0.25`, `bin_duration_hours=3.0`). They are not absolute physical limitations. Configuration tuning can extend the operating envelope without violating the algorithm freeze — see [STAGE1_FREEZE_CERTIFICATE.md](file:///d:/TARS/TarsCore/docs/STAGE1_FREEZE_CERTIFICATE.md).

---

## 1. Operating Envelope Table

The following table classifies the performance zones for each physical parameter. Where available, 95% bootstrap confidence intervals (CI) and sample sizes ($N$) are reported. Parameters marked **CI: pending** require a dedicated injection sweep to quantify uncertainty.

| Parameter | Validated (Error $\le 5\%$) | Marginal (Error $5\%\text{--}10\%$) | Failure (Error $> 10\%$) | 95% CI (5% boundary) | $N$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Transit Depth — Synthetic** | $\ge 1.48\%$ depth | $0.74\%\text{--}1.48\%$ depth | $< 0.74\%$ depth | $[1.44\%, 1.52\%]$ | 10 seeds × 30 trials |
| **Transit Depth — Real TESS Quiet** | $\ge 0.289\%$ depth | $0.144\%\text{--}0.289\%$ depth | $< 0.144\%$ depth | CI: pending | Phase 2.3 audit |
| **Transit Depth — Real TESS Variable** | $\ge 2.000\%$ depth | $1.718\%\text{--}2.000\%$ depth | $< 1.718\%$ depth | CI: pending | Phase 2.3 audit |
| **Transit Duration** | $\le 4.00$ hr | $4.00\text{--}9.86$ hr | $> 9.86$ hr | CI: pending | Phase 2.3 audit |
| **Sinusoidal Stellar Variability** | $\le 0.50\%$ amp | $0.50\%\text{--}0.92\%$ amp | $> 0.92\%$ amp | CI: pending | Phase 2.3 audit |
| **Quasi-Periodic Spot Modulation** | $\le 0.50\%$ amp | $0.50\%\text{--}1.15\%$ amp | $> 1.15\%$ amp | CI: pending | Phase 2.3 audit |
| **Multi-Frequency Variability** | $\le 1.00\%$ amp | $1.00\%\text{--}3.17\%$ amp | $> 3.17\%$ amp | CI: pending | Phase 2.3 audit |
| **Red Noise Correlation ($\rho$)** | $\le 0.30$ | $0.30\text{--}0.63$ | $> 0.63$ | CI: pending | Phase 2.3 audit |

### Synthetic Boundary Details (Phase 2.4 — Track E)

The Transit Depth (Synthetic) boundaries were computed over **10 independent random seeds** with **30 trials per depth level**. Bootstrap confidence intervals ($B = 1000$ resamples, 95% two-tailed) are available for all three boundary levels:

| Boundary Level | Mean Depth | Std | 95% CI Lower | 95% CI Upper | CV |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **5% Error Boundary** | $1.479\%$ | $0.075\%$ | $1.437\%$ | $1.523\%$ | $5.06\%$ |
| **10% Error Boundary** | $0.744\%$ | $0.062\%$ | $0.711\%$ | $0.783\%$ | $8.39\%$ |
| **20% Error Boundary** | $0.354\%$ | $0.026\%$ | $0.340\%$ | $0.369\%$ | $7.28\%$ |

> [!IMPORTANT]
> **CI roadmap**: The "CI: pending" entries in the table above require a future dedicated injection sweep on real TESS data (Tracks B–D of a follow-on campaign) to assign proper bootstrap confidence intervals. These boundaries are currently point estimates derived from the Phase 2.3 audit sweeps. They should **not** be cited in publications without this caveat.

---

## 2. Key Physical Breakdown Mechanisms

* **White Noise Floor**: Below $\approx 0.29\%$ depth on quiet real TESS stars, signals are buried beneath the point-to-point noise floor.
* **Filter Self-Clipping**: Transits wider than $\approx 9.86$ hours exceed the 1-day median window timescale. The filter treats the transit as a trend and self-clips it ($> 10\%$ depth attenuation).
* **Stellar Variability Contamination**: Sinusoidal amplitudes above $\approx 0.92\%$ leave behind micro-residuals that distort the recovered transit depth.
* **Red Noise Breakdown**: At correlations $\rho > 0.63$, the point-to-point noise assumptions fail. The $\beta$ factor inflates, and the local baseline estimate becomes unreliable.

---

## 3. Cross-Sector Stability (Phase 2.4 — Track B)

Stage 1 was evaluated on an **evaluated sample** of 441 target-sector records from 100 unique stars with overlapping observations in Sectors 1–5. Median depth recovery errors are stable across sectors (range: $2.8\%$–$3.5\%$), and beta factors are stable (range: $0.056$–$0.093$).

> [!NOTE]
> This result applies to the **evaluated sample** (100 overlapping stars, Sectors 1–5) and should not be extrapolated to claim sector-general stability without a broader multi-sector study.

---

## 4. Configuration Refinement Guidance

The freeze covers the **algorithm**, not the **parameters**. Examples of permitted tuning:

* **Long-duration transits** ($> 8$ hr): Increase `detrend_window_days` from $1.0$ to $3.0$ days to shift the self-clipping limit beyond $24$ hours.
* **High-variability targets**: Replace the sliding median with a Gaussian Process or asymmetric filter to extend the validated amplitude range. This is a configuration change that does not alter the frozen equations.

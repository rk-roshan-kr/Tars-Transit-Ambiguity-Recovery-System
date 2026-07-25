# Stage Lock Freeze — TARS Core Stage 1

This document freezes Stage 1 (Signal Conditioning & Noise Characterization) of TARS Core.

---

## 1. Governance Signature

| Metric | Detail |
| :--- | :--- |
| **Pipeline Stage** | Stage 1 (Signal Conditioning & Noise Characterization) |
| **Status** | **LOCKED & FROZEN** |
| **Version** | v1.1-conditioning |
| **Lock Date** | 2026-06-03 |
| **Validation Results** | 18/18 Unit Tests Passed (models + conditioning) |

---

## 2. Scientific Assumptions

* **Timescale Separability**: Slow trends $\ge 1.0$ day are physical/systematic drift and must be removed. Rapid transit dips $\le 0.5$ days must be preserved.
* **Point-to-Point Noise Floor**: Measurement errors on short timescales are normally distributed.
* **Correlated Scaling**: Excess variance on a 3-hour binned scale indicates red noise.

---

## 3. Known Limitations

* **Transit Depth Attenuation**: Transits with durations $\ge 8$ hours will experience minor depth attenuation (up to 10%–15%) due to sliding window median bias.
* **Edge Artifacts**: Edge padding at boundaries or downlink gaps can cause minor distortion in the first/last few cadences.

---

## 4. Approved Default Parameters

The following parameters are frozen and must not be altered without formal review:

```python
PipelineConfig(
    sigma_threshold=3.0,
    coherence_pass=0.7,
    coherence_gray=0.5,
    gcp_pass=0.45,
    gcp_gray=0.60,
    random_seed=42
)
```

Additionally, Stage 1 conditioner parameters are locked at:
* `detrend_window_days = 1.0`
* `noise_window_days = 0.25`
* `bin_duration_hours = 3.0`

---

## 5. Approved Validation Datasets

* **Synthetic Verification Grid (Test 1–6)**: Enforces depth error $< 5\%$, duration error $< 10\%$, and red noise monotonicity.
* **Stellar Noise Sweep**: Validates $\beta$ factor and lag-1 autocorrelation bounds.

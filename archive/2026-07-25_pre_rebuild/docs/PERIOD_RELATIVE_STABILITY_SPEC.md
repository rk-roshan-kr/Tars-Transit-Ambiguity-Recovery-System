# Period-Relative Stability Specification

*Phase 6.1 — Component B. Documents the scientific justification for replacing the absolute stability threshold with a period-relative fractional threshold.*

---

## The Defect

Original configuration:

```python
"stability_threshold": 60.0  # minutes
```

Original check in `recoverer.py`:
```python
if mad_min > self.config["stability_threshold"]:  # 60.0 minutes absolute
    reject candidate
```

**Why this is wrong**: The 60-minute threshold is applied identically regardless of the orbital period. Consider:

| Period | Transit Duration (typical) | 60-min MAD significance |
| :--- | :--- | :--- |
| 1 day | ~1 hour | 60 min = 100% of transit duration. Catastrophic. |
| 10 days | ~2–3 hours | 60 min = 30–50% of transit duration. Still large. |
| 40 days | ~4–6 hours | 60 min = 10–25% of transit duration. Modest. |

The same 60-minute MAD would correctly reject a 1-day period candidate as jittery but incorrectly accept a 40-day period candidate with an equally imprecise ephemeris — or, depending on the direction of the bias, vice versa.

---

## The Scientific Correct Formulation

The physically meaningful measure of ephemeris stability is the **fractional period jitter**: the timing residual expressed as a fraction of the orbital period.

$$\text{MAD}_{norm} = \frac{\text{MAD}}{P}$$

A threshold of $\text{MAD}_{norm} < 0.02$ means the timing residuals must be less than 2% of the orbital period — a scale-invariant criterion applicable to periods from 1 day to 100 days.

**Physical interpretation**: 2% of a 10-day period = 4.8 hours. 2% of a 1-day period = 0.48 hours = 29 minutes. These are physically meaningful limits consistent with the expected timing precision of individual TESS transit detections.

---

## Implementation Fix

### `config.py`

```python
# Removed:
"stability_threshold": 60.0          # absolute minutes — period-independent

# Added:
"stability_threshold_fractional": 0.02  # MAD < 2% of orbital period
```

### `stability_engine.py`

`compute_stability()` now accepts an optional `period_days` parameter and returns four values:
```python
def compute_stability(residuals, period_days=None):
    ...
    return rms_minutes, mad_minutes, rms_norm, mad_norm
```

where `rms_norm = RMS / period_days` and `mad_norm = MAD / period_days`.

### `recoverer.py`

```python
rms_min, mad_min, rms_norm, mad_norm = compute_stability(fitted_residuals, period_days=refined_p)
if mad_norm >= self.config["stability_threshold_fractional"]:
    reject
```

---

## Threshold Value Justification

### Initial value: `stability_threshold_fractional = 0.02` (2%)
This was too restrictive. Phase 6.1 regression analysis showed that at P ≤ 1 day, the 2% threshold equates to 28.8 minutes — stricter than the old absolute 60-minute threshold. This caused valid short-period recoveries to fail stability, elevating half-period aliases.

### Calibrated value: Combined min-of-two formulation

```python
stability_threshold_fractional = 0.05   # 5% of period
stability_threshold_absolute_days = 0.05  # ~72 minutes absolute floor
eff_norm_thresh = min(fractional, absolute / P)
```

This formulation:
- At P = 1 day: effective = min(5%, 5%) = 5% = 72 minutes
- At P = 10 days: effective = min(5%, 0.5%) = 0.5% = 72 minutes  
- At P = 40 days: effective = min(5%, 0.125%) = 0.125% = 72 minutes

For long periods, the absolute floor (72 min) dominates and prevents the threshold from becoming arbitrarily permissive. For short periods, the fractional cap prevents it from becoming arbitrarily tight.

**This value is FROZEN after calibration.** It may be revised in Phase 6B based on real TESS timing error characterization.

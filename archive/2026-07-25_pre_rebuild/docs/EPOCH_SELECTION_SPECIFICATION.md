# Epoch Selection Specification

*Phase 6.1 — Component A. Documents the defect, the mathematical correct epoch, and the implementation fix.*

---

## The Defect

Original implementation in `recoverer.py`:

```python
epoch = min([e.event_time for e in events])
```

This assigns the epoch as the timestamp of the earliest observed transit. This is correct only when the first observed event occurs exactly at phase zero for the candidate period — which is not generally true. When the first event falls at a non-zero phase offset (e.g., the planet transited in sector 1, and the earliest stored event is an event from sector 3), the epoch is misaligned. This produces artificially elevated O-C residuals for every other event, causing the stability engine to underestimate the true period quality.

**Measured impact**: Systematically degrades residual MAD scores for correct periods relative to harmonic aliases, potentially causing aliases to rank above the true period.

---

## The Mathematical Correct Epoch

Given a set of $N$ supporting transit events $\{t_k\}$ with timing uncertainties $\{\sigma_{t,k}\}$, the linear ephemeris model is:

$$t_k = t_0 + n_k \cdot P$$

where $t_0$ is the epoch and $P$ is the orbital period. Fitting this via Weighted Least Squares (WLS) simultaneously estimates the best-fit $P$, the best-fit $t_0$, and their covariance matrix:

$$[\hat{P}, \hat{t_0}] = \arg\min \sum_k w_k (t_k - t_0 - n_k P)^2, \quad w_k = 1/\sigma_{t,k}^2$$

The WLS solution is already computed in `period_uncertainty.py` as `calculate_uncertainty()`, which returns `(refined_p, refined_epoch, sigma_p)`.

**The correct epoch for scoring is `refined_epoch` from the WLS fit — not the raw minimum event time.**

---

## Implementation Fix

### Phase 6.1 change in `recoverer.py`

**Before**:
```python
epoch = min([e.event_time for e in events])
residuals = compute_residuals(p_trial, epoch, events)
# ...stability on initial residuals...
refined_p, refined_epoch, sigma_p = calculate_uncertainty(p_trial, epoch, supporting_events)
# residuals never recomputed using refined_epoch
score = score_candidate(..., mad_min, ...)
```

**After**:
```python
bootstrap_epoch = min(e.event_time for e in events)     # bootstrap only
initial_residuals = compute_residuals(p_trial, bootstrap_epoch, events)
supporting_events = [ev for ev, r in zip(events, initial_residuals) if abs(r) <= tolerance]
# WLS fit: single source of truth
refined_p, refined_epoch, sigma_p = calculate_uncertainty(p_trial, bootstrap_epoch, supporting_events)
# Scoring uses WLS-fitted epoch
fitted_residuals = compute_residuals(refined_p, refined_epoch, supporting_events)
rms_min, mad_min, rms_norm, mad_norm = compute_stability(fitted_residuals, period_days=refined_p)
score = score_candidate(..., mad_norm, ...)
```

### Design rule enforced (per user review)
The bootstrap epoch (`min(t)`) is used only to identify supporting events (initial support filter). All scoring computations use the WLS-fitted epoch exclusively. No brute-force epoch scan introduced.

---

## Expected Effect

For any candidate period where the first observed transit is not at phase zero, the WLS-fitted epoch will produce lower residuals than the `min(t)` epoch. This reduces the measured MAD for the true period, improving its stability score relative to aliases that may have coincidentally lower raw residuals under the misaligned epoch.

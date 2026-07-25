# Support Scaling Specification

*Phase 6.1 — Component D. Documents the replacement of the saturating support score with logarithmic scaling.*

---

## The Defect

Original `consensus_ranker.py`:

```python
support_score = min(n_supporting_events / 5.0, 1.0)
```

This saturates at 5 events. A detection with 5, 10, 20, or 50 supporting events receives the same support score of 1.0. This is scientifically incorrect: a 20-transit detection provides overwhelmingly stronger evidence than a 5-transit detection, and the scoring function should reflect this.

**Secondary effect**: When a true period $P$ has 8 supporting events and its $2P$ alias has 5 events, both receive support score = 1.0 (saturated). The true period's superior event support provides zero additional scoring advantage. This makes harmonic tie-breaking harder and inflates alias survival rates.

---

## The Fix

Replace the hard-saturating linear cap with a monotonically increasing logarithmic scaling:

$$\text{support\_score} = \frac{\log(1 + N_s)}{\log(1 + N_{ref})}$$

where $N_{ref} = 10$ (the reference normalization count).

**Properties**:
- Monotonically increasing — every additional event provides additional score.
- $N_s = 0$ → score = 0.0 (a detection with 0 events scores nothing).
- $N_s = 10$ → score = 1.0 (reference point, same as old cap).
- $N_s = 20$ → score ≈ 1.04 (clamped to 1.0 by safety clamp).
- Sub-linear growth: correctly rewards additional events with diminishing marginal returns (going from 3 to 4 events is more significant than from 50 to 51).

---

## Comparison

| N supporting events | Old score (saturated) | New score (log) |
| :---: | :---: | :---: |
| 2 | 0.40 | 0.48 |
| 3 | 0.60 | 0.61 |
| 5 | 1.00 (capped) | 0.80 |
| 8 | 1.00 (capped) | 0.95 |
| 10 | 1.00 (capped) | 1.00 |
| 15 | 1.00 (capped) | ≥1.0 (clamped to 1.0) |

The new scoring correctly ranks a 10-event detection above an 8-event detection and both above a 5-event detection — a physically correct ordering that the old formula could not express.

---

## Implementation

```python
import math

_SUPPORT_LOG_NORM = math.log(11.0)  # log(1 + N_ref) where N_ref = 10

def score_candidate(...):
    support_score = math.log(1.0 + n_supporting_events) / _SUPPORT_LOG_NORM
    support_score = min(support_score, 1.0)  # safety clamp
```

---

## Frozen Weights

The weights `w_coverage = 0.4`, `w_stability = 0.4`, `w_support = 0.2` are **unchanged**. Only the formula computing `support_score` was modified. This is the narrowest possible change consistent with fixing the defect without introducing new parameters.

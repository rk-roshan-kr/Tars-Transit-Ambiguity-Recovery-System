# Stage 2 Methods

**TARS Core Stage 2 — Transit Event Detection**

This document describes the mathematical and algorithmic methods used by Stage 2 to convert a `ConditionedLightCurve` (Stage 1 output) into a ranked list of `TransitEvent` objects.

---

## 1. Overview

Stage 2 is a **detector**, not a classifier. Its design priority is:

> **Recall > Precision**

False positives are expected. They are removed by downstream stages (EEA, ECHO, Bayesian Evidence, ML Ranking). A missed transit at Stage 2 is unrecoverable — there is no second chance.

---

## 2. Stage 2.1 — Local Significance Scan

Every cadence is scored using a local signal-to-noise metric:

$$S_i = \frac{1 - f_i}{\sigma_{\text{local},i}} \quad \text{(EQ-S2-01)}$$

where $f_i$ is the detrended flux and $\sigma_{\text{local},i}$ is the MAD-based local noise estimate produced by Stage 1 (EQ-S1-02). The same noise floor is used throughout — Stage 2 does not recompute noise.

Cadences with $S_i \ge \sigma_{\text{threshold}}$ (default $3.0$, configurable) are flagged as `CandidatePoint` objects.

**Statistical basis:** At $\sigma = 3.0$ and Gaussian noise, the false alarm probability per cadence is approximately $0.00135$ (one-tailed). For $N = 2000$ cadences, the expected false candidate count is approximately $2.7$ cadences, grouping to typically $0$–$3$ false events per light curve.

---

## 3. Stage 2.2 — Candidate Grouping

Individual `CandidatePoint` objects are merged into `TransitEvent` objects.

**Algorithm:**
1. Sort candidate points by cadence index.
2. Merge consecutive candidates where the cadence gap is $\le$ `max_gap_cadences + 1` (default allows bridging 1 unflagged cadence to avoid splitting an event at a NaN mask).
3. For each merged group, compute:
   - `event_time` = median BTJD of the group
   - `depth` = $1 - \min(f_i)$
   - `duration` = $t_{\text{last}} - t_{\text{first}}$
   - `snr` = `depth / median(sigma_local)`
   - `peak_significance`, `mean_significance` from $S_i$ values

---

## 4. Stage 2.3 — Morphology Extraction

Six descriptors are computed for each event (EQ-S2-02 through EQ-S2-06):

| Descriptor | Equation | Physical Meaning |
| :--- | :--- | :--- |
| Depth | $D = 1 - \min(f_i)$ | Maximum fractional flux decrement |
| Duration | $T = t_{\text{end}} - t_{\text{start}}$ | First-to-last-contact duration |
| Area | $A = \int \max(0, 1-f)\, dt$ (trapz) | Integrated absorbed flux |
| Symmetry | $1 - \|A_\text{in} - A_\text{eg}\| / (A_\text{in} + A_\text{eg} + \varepsilon)$ | Ingress/egress balance |
| Sharpness | $(1 - f_{\min}) / \overline{(1 - f_i)}$ | Spike vs box shape |
| Ingress/Egress duration | Time from half-depth contact to minimum | For future EEA/ECHO use |

---

## 5. Stage 2.4 — Physics-Aware Quality Labelling

Each event receives a `physics_label` based on physical plausibility rules:

| Condition | Label |
| :--- | :--- |
| Duration < 20 min OR > 24 hr | `NON_TRANSIT` |
| `depth ≤ 0` (flux increased) | `NON_TRANSIT` |
| `sharpness > 3.0` (spike-like) | `UNCERTAIN` |
| Passes all above | `TRANSIT_LIKE` |

> [!IMPORTANT]
> **Labels are advisory metadata, not vetoes.** All events — including `NON_TRANSIT` — are passed to Stage 3. Stage 4 (EEA/ECHO) holds veto authority. This preserves maximum recall.

---

## 6. Heuristic H-S2-01 — Experimental Event Ranking

> [!WARNING]
> **This is an experimental heuristic, not a scientific equation.** Do not cite the weights as derived results. They are configurable defaults subject to revision.

$$\text{Score} = 0.4 \cdot S_{\text{peak,norm}} + 0.3 \cdot S_{\text{dur,norm}} + 0.3 \cdot S_{\text{depth,norm}}$$

Each component is min-max normalised across all events in the current light curve:
- $S_{\text{peak,norm}}$: normalised `peak_significance`
- $S_{\text{dur,norm}}$: Gaussian preference centred at 3 hours, normalised
- $S_{\text{depth,norm}}$: log-scaled depth to suppress deep EBs, normalised

Events are returned sorted by `event_score` descending. Stage 3 may process them in any order.

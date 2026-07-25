# Stage 2 Limitations

This document enumerates the known limitations of **TARS Core Stage 2 (Transit Event Detection)**. Reviewers of any publication using TARS Core are expected to ask about these directly. This document provides defensible, honest answers.

---

## L1 — No Phase Folding

**Limitation:** Stage 2 detects events within a single light curve (single sector, $\approx 27$ days). It does not phase-fold the light curve to boost the signal-to-noise of a shallow, repeating transit.

**Consequence:** For planets with periods comparable to the sector length, only one or two transits may be present. A single transit with depth near the noise floor may not exceed the significance threshold without phase folding.

**Why this is by design:** TARS Core is specifically targeting the sparse-transit regime (Stage 3: Sparse Period Recovery). Phase folding is the standard approach used by existing pipelines (BLS, TLS). The scientific novelty of TARS Core lies in recovering period candidates from individual, unconvincing transit events — not from phase-folded stacks.

**Implication for publication:** Claims about Stage 2 sensitivity must reference the single-sector context. Comparison against phase-folded pipelines is not valid without controlling for sector length and transit count.

---

## L2 — Stage 1 Attenuation of Long-Duration Transits

**Limitation:** Transits with durations approaching the Stage 1 detrending window ($\approx 9.86$ hr at default `detrend_window_days = 1.0`) are partially self-clipped before reaching Stage 2.

**Consequence:** Stage 2 receives an attenuated version of the transit. The recovered depth and significance are systematically lower than the true values. For transits $> 9.86$ hr at default settings, depth recovery errors exceed $10\%$ (Stage 1 operating boundary).

**Mitigation:** Increase `detrend_window_days` to $3.0$ before processing long-period targets. This is a configuration change, not an algorithm change, and does not violate the Stage 1 freeze.

**Implication for publication:** Figure S (Duration Detection Study) documents the detection probability as a function of duration. Results from Figure S apply only to the default configuration. Targets with transit durations $> 6$ hr should use the extended detrending window.

---

## L3 — Elevated FEPLC on Variable Stars

**Limitation:** On light curves with residual variability after Stage 1 conditioning (variable stars with $\beta > 0.5$), the false event rate per light curve (FEPLC) increases significantly even at $\sigma = 3.5$–$4.0$.

**Consequence:** Stage 3 receives more false event combinations to evaluate, increasing computational cost. Stage 4 (EEA/ECHO) must reject a larger fraction of candidate chains.

**Quantification:** Figure Q (Noise Regime Study) documents the FEPLC for the three main noise regimes at each threshold. The AR(1) and Variable Star regimes show elevated FEPLC compared to Gaussian noise.

**Implication for publication:** Results on variable stars must not be compared directly to results on quiet stars using only Stage 2 metrics. The relevant performance metric is the full pipeline's false positive rate after Stage 7, not Stage 2's FEPLC.

---

## L4 — Minimum Detectable Depth Inherits Stage 1 Boundary

**Limitation:** Stage 2 cannot detect events shallower than the Stage 1 noise floor. The minimum detectable depth is bounded by Stage 1's operating boundary:
- Quiet TESS stars: $\approx 0.29\%$ depth (CI: pending)
- Variable stars: $\approx 1.72\%$ depth (CI: pending)

**Consequence:** Sub-Earth transits ($< 0.01\%$) and Earth-Sun analogues around Sun-like stars ($\approx 0.008\%$) are not detectable by TARS Core Stage 2 in single-sector data without phase folding.

**Implication for publication:** The minimum detectable depth reported in any publication must reference the Stage 1 operating boundary, not the Stage 2 threshold alone.

---

## L5 — Scoring Heuristic H-S2-01 is Not Validated

**Limitation:** The `event_score` computed by Stage 2.5 uses empirically chosen weights $(0.4, 0.3, 0.3)$ that have not been optimized against a labelled dataset or grounded in physical theory.

**Consequence:** The ranking order of events entering Stage 3 may not be optimal. A false positive may rank higher than a genuine planet if its morphology happens to score well on the heuristic.

**Why this is acceptable:** Stage 3 processes all events regardless of rank order. The `event_score` influences computational priority, not inclusion. No events are excluded based on score.

**Implication for publication:** Do not cite `event_score` as a scientifically derived quantity. Report it as "an experimental pre-ranking heuristic subject to revision." The final pipeline result is insensitive to the ranking order of Stage 2 events as long as all events are passed to Stage 3.

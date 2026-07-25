# Stage 1 Assumptions — Physical and Statistical Limits

This document outlines the core scientific boundaries, assumptions, operational scope, and failure modes of TARS Core Stage 1.

---

## 1. Physical Assumptions

* **Separation of Timescales**:
  We assume that stellar signals and instrumental variations can be cleanly separated by frequency. Specifically, slow drifts (e.g. thermal settling, pointing jitter, rotational modulation) are assumed to have characteristic timescales $\ge 1.0$ day, whereas planetary transits are assumed to have durations $< 0.5$ days (12 hours).
* **Flux Division**:
  We assume that systematic noise and large-scale trend effects act multiplicatively on the stellar flux. Therefore, detrending is performed by dividing the raw flux by the estimated trend.

---

## 2. Statistical Assumptions

* **Gaussian White Noise Floor**:
  We assume that the high-frequency measurement noise (point-to-point scatter) is normally distributed. While outliers exist, they are handled via robust estimators (MAD).
* **Stationarity of Binned Noise**:
  We assume that the white noise and red noise properties are relatively stationary across a single observation sector (27.4 days). This justifies using a single global `white_noise` and `red_noise` value for diagnostics, while utilizing `sigma_local` for localized time-dependent thresholds.

---

## 3. Operational Scope

* **Observation Cadence**:
  Stage 1 is optimized for TESS high-cadence data (2-minute or 20-second cadence SPOC light curves). While it can ingest Kepler data, it requires uniform timestamps and a minimum of 5,000 cadences to establish stable median statistics.
* **Excluded Processing**:
  Stage 1 does not perform planet search, threshold crossing, or candidate grouping. It is strictly a conditioning and noise characterization pipeline.

---

## 4. Known Failure Modes

* **Transit Attenuation (Depth Dilution)**:
  If a planet has an exceptionally long transit duration (e.g. $T_{\text{transit}} \ge 8$ hours), self-containment of transit cadences within the sliding median window will pull the median trend down. This results in the transit depth being under-recovered (attenuated) in the detrended flux.
* **Edge Effects**:
  At the beginning and end of a sector, or around major gaps (e.g. data downlink gaps), the median window is asymmetric. This can cause the median trend line to deviate, resulting in fake transit-like dips (edge distortion).
* **High Stellar Variability (Flares/Rotational Harmonics)**:
  Rapid, large-amplitude stellar variations (such as massive flares or short-period active star pulsations) can violate the timescale separation assumption, leading to residual trends or inflated local noise metrics.

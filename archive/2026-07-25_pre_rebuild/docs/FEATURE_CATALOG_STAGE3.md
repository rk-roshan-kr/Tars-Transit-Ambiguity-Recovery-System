# Stage 3: Feature Catalog

All features utilized by the Component 5 Consensus Ranking algorithm must be defined here prior to implementation. 

### Core Features

* **`period_days`**: The primary proposed orbital period in days.
* **`n_supporting_events`**: The absolute count of discrete `TransitEvent`s that align with this period hypothesis.
* **`coverage_fraction`**: The ratio of observed supporting events vs. expected events (given the period and the observational baseline gaps).

### Stability Features

* **`residual_rms`**: The root-mean-square of the timing residuals (Observed - Expected) for this period. Lower is better.
* **`residual_mad`**: The median absolute deviation of the timing residuals. Lower is better.
* **`period_stability`**: A normalized score derived from the residual RMS/MAD, quantifying how rigidly the events adhere to a perfect linear clock.

### Ranking Features

* **`gap_adjusted_support`**: The event support count penalized for transits that *should* have been observed but were missing in clean data, and forgiving of transits missing in data gaps.
* **`harmonic_rank`**: An integer indicating the hypothesis' relationship to the fundamental period (e.g., $1$ for fundamental, $2$ for $2P$, $0.5$ for $P/2$).

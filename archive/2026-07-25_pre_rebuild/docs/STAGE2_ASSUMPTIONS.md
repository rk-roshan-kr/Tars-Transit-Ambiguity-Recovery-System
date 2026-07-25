# Stage 2 Assumptions

This document lists all assumptions made by **TARS Core Stage 2 (Transit Event Detection)**. Every assumption is a potential failure mode. Knowing these in advance is what allows reviewers to test them.

---

## A1 — Stage 1 Noise Accuracy

**Assumption:** The `sigma_local` array produced by Stage 1 accurately represents the local point-to-point flux scatter at every cadence.

**Where it is used:** EQ-S2-01 divides by `sigma_local` to compute significance. If `sigma_local` is systematically underestimated, the false alarm rate increases. If overestimated, recall decreases.

**When it may break:** On variable stars where the noise floor is non-stationary (e.g., during a stellar flare). Stage 1's operating boundary for variable stars is $\beta \lesssim 0.5$.

**Mitigation:** The Stage 1 noise estimate uses a sliding MAD window with a 0.25-day timescale, which tracks non-stationarity within its window. Events from variable stars will naturally have elevated `sigma_local` and reduced significance.

---

## A2 — Zero-Mean Detrended Flux Outside Transits

**Assumption:** After Stage 1 conditioning, the detrended flux is approximately zero-mean between transit events.

**Where it is used:** The significance formula $S_i = (1 - f_i) / \sigma_{\text{local},i}$ expects $f_i \approx 1$ (i.e., $1 - f_i \approx 0$) in the absence of a transit. Residual trends inflate significance.

**When it may break:** When the detrending window is narrower than the timescale of a stellar variability signal. Partially-detrended trends produce systematic cadences with $S_i > 0$, increasing FEPLC.

**Mitigation:** Stage 1 Phase 2.3 audit established that trends with amplitudes below $\approx 0.92\%$ are adequately detrended. Stars with larger amplitudes should be processed with `detrend_window_days` reduced to follow the variability timescale.

---

## A3 — Monolithic Flux Depression

**Assumption:** A transit event manifests as a single, contiguous region of flux depression.

**Where it is used:** The grouping algorithm in Stage 2.2 merges contiguous candidate points. It does not handle double-dip morphologies (e.g. eclipsing binary secondaries, planet-moon transits).

**When it may break:** For eccentric orbits, the primary and secondary eclipses may fall within the same baseline if the period is short. Stage 2 would merge or split them depending on cadence gap size.

**Mitigation:** Stage 4 (ECHO) specifically checks for EB-like morphology. This assumption is acceptable at Stage 2 given the Recall > Precision design priority.

---

## A4 — Stage 2 is a Filter, Not a Classifier

**Assumption:** Stage 2 does not distinguish between genuine planets, false positives, eclipsing binaries, or artefacts. It only identifies flux depressions that exceed a local noise threshold.

**Implication:** The reported `physics_label` is an advisory pre-filter based on physical plausibility, not a classification result. All events are passed downstream regardless of label.

**Why this matters for publication:** Any statement about Stage 2 "detecting planets" is incorrect. Stage 2 detects **transit-like events**. Whether an event corresponds to a planet is determined by the full TARS Core pipeline through Stages 3–7.

---

## A5 — Gaussian Noise Distribution

**Assumption:** Point-to-point noise is approximately Gaussian at each cadence (after Stage 1 conditioning).

**Where it is used:** The significance threshold $\sigma = 3.0$ is calibrated under the assumption that $S_i$ follows a standard normal distribution under the null hypothesis (no transit). The false alarm rate of 0.00135 per cadence is derived from $P(Z > 3.0)$.

**When it may break:** In the presence of unresolved red noise ($\beta > 0.5$), the effective degrees of freedom are reduced and the actual false alarm rate exceeds the Gaussian prediction. The Stage 1 $\beta$ factor should be checked before Stage 2 is run on high-variability targets.

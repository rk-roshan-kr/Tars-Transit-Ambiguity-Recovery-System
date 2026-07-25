# Architecture vs Implementation Gap

*Phase 5.4 — Component D. For every Stage 3 component, documents what the architecture intended, what the code actually does, what assumptions were silently introduced, and what was lost in translation.*

---

## Component 1: Interval Generator

### Architecture Intended
The interval generator was designed to produce an **admissible family of orbital hypotheses** from all pairwise event timestamps. It implements EQ-S3-01 ($P_{i,j} = |t_j - t_i| / k$ for $k = 1..K_{max}$). The intent was to generate *all* physically plausible periods before filtering — a complete hypothesis space.

### What Code Actually Does
[interval_generator.py](file:///d:/TARS/TarsCore/tarscore/stage3_period_recovery/interval_generator.py) correctly implements the pairwise interval algebra and harmonic divisor sweep. This component has the highest architecture fidelity of any Stage 3 module.

### Assumptions Introduced
- `Kmax` is fixed in `config.py`. The architecture never specified a global maximum harmonic divisor; it was introduced as a practical limit. If the true period is $P$ and two events are separated by $5P$, and $K_{max} < 5$, the generator silently misses it.

### What Was Lost
- No inter-event **ordering constraint**. The generator creates pairwise hypotheses between ALL events, including non-consecutive ones. This creates spurious hypotheses that the stability engine must filter at higher cost.
- No **probability weighting** of hypotheses by physical plausibility (e.g., shorter periods are a priori more likely under occurrence-rate distributions). All hypotheses enter the pipeline with equal prior weight.

---

## Component 2: Harmonic Resolver

### Architecture Intended
The harmonic resolver was designed to explicitly identify $P$, $2P$, $P/2$, $3P$ alias families, perform formal tie-breaking using the Harmonic Resolution Specification, and flag ambiguous cases so the consensus ranker can treat them explicitly.

### What Code Actually Does
[harmonic_resolver.py](file:///d:/TARS/TarsCore/tarscore/stage3_period_recovery/harmonic_resolver.py) performs period clustering and alias linking via pairwise ratio comparison. The `_link_aliases` function correctly identifies integer-ratio relationships.

### Assumptions Introduced
- **Tie-breaking is deferred to the consensus ranker** (line 76: "S3-9 / Harmonic Ambiguity tie-break is handled during final consensus ranking"). This means the harmonic resolver never actually *resolves* harmonics — it only *labels* them. The name is misleading.
- Cluster formation uses a hard `tolerance` value derived from `harmonic_tolerance_sigma_multiplier * timing_unc`. For low-SNR events, `timing_unc` is large, and this tolerance can merge fundamentally distinct periods into one cluster.

### What Was Lost
- **Active harmonic selection** — the resolver should choose between $P$ and $2P$ based on which better explains the full event set. Instead it passes *both* forward, leaving the heuristic ranker to break the tie.
- **Formal tie-breaking rules** referenced in `HARMONIC_RESOLUTION_SPECIFICATION.md` are documented but not reflected in code logic.

---

## Component 3: Timing Residual Engine

### Architecture Intended
Compute $O-C$ residuals for every transit event against a linear ephemeris. EQ-S3-02 is defined as $r_k = t_k - (t_0 + n_k P)$. Residuals are the core evidence metric for physical consistency.

### What Code Actually Does
[timing_residuals.py](file:///d:/TARS/TarsCore/tarscore/stage3_period_recovery/timing_residuals.py) correctly implements EQ-S3-02. This component is architecturally faithful.

### Assumptions Introduced
- **Epoch is always the minimum event time** (hardcoded in `recoverer.py` line 60: `epoch = min(...)`). This is not general — it ignores phases and can cause high residuals for events that precede the minimum by fractional periods.
- **All events are evaluated against each period**. There is no mechanism to exclude known false-positive events from the residual computation.

### What Was Lost
- **SNR-weighted residuals**. Each event should contribute to the $O-C$ sum weighted by its timing certainty. A low-SNR event at 2-minute timing uncertainty should count less than a high-SNR event at 30-second precision. This weighting is absent.

---

## Component 4: Period Uncertainty Engine

### Architecture Intended
Derive a formal period uncertainty $\sigma_P$ from the covariance of the linear ephemeris fit, propagating timing event errors correctly.

### What Code Actually Does
[period_uncertainty.py](file:///d:/TARS/TarsCore/tarscore/stage3_period_recovery/period_uncertainty.py) performs a weighted least-squares fit of the transit number vs event time to refine the period and compute `sigma_p`.

### Assumptions Introduced
- `sigma_t = duration / SNR` is used as the per-event timing uncertainty. This is a heuristic approximation, not a formally derived photometric precision limit.

### What Was Lost
- **Stage 2 uncertainty propagation**. The timing uncertainty entering Stage 3 should incorporate Stage 1's detrending residuals and Stage 2's detection threshold uncertainty, not a fresh approximation.

---

## Component 5: Observation Window Model

### Architecture Intended
Model the actual observational coverage of the TESS telescope — including sector boundaries, momentum dumps, and downlink gaps — to determine how many transits *should* have been observed. This gives coverage fraction a physical meaning grounded in the telescope's real cadence patterns.

### What Code Actually Does
[observation_window.py](file:///d:/TARS/TarsCore/tarscore/stage3_period_recovery/observation_window.py) detects gaps as regions where cadence spacing exceeds `5 × median_cadence`. It then counts expected transits that fall outside detected gaps.

### Assumptions Introduced
- The `5 × median_cadence` gap threshold is not documented anywhere. It was implicitly introduced and has never been validated.
- The model uses the raw time array from the Conditioned Light Curve. If Stage 1 resampled or compressed the LC, the cadence structure may not reflect the original TESS cadence.

### What Was Lost
- **TESS sector boundary metadata**. Real TESS data includes quality flags marking momentum dumps, thermal resettings, and data-link gaps. The current implementation is a generic gap detector.
- **Expected transit uncertainty bounds**. The model counts exact theoretical transit times but does not account for the transit duration window — a transit occurring at the edge of a gap window may be partially observed or missed.

---

## Component 6: Stability Engine

### Architecture Intended
Quantify the rigidity of the linear ephemeris fit using RMS and MAD of timing residuals. Both statistics implemented correctly per EQ-S3-03 and EQ-S3-04.

### What Code Actually Does
[stability_engine.py](file:///d:/TARS/TarsCore/tarscore/stage3_period_recovery/stability_engine.py) correctly implements both metrics. This is the most architecturally complete component.

### Assumptions Introduced
- Residuals are converted to minutes (`× 24 × 60`) before comparing against `stability_threshold`. The threshold in config is also in minutes. This is internally consistent but requires users to specify config values in minutes — a unit convention that could produce silent misconfigurations.

### What Was Lost
- No normalization by period. A 30-minute MAD for a 1-day period is catastrophic. A 30-minute MAD for a 40-day period is barely significant. The stability threshold should be period-relative, not absolute.

---

## Component 7: Consensus Ranker

### Architecture Intended
Sort the physically admissible candidate family by a score that reflects evidence quality — prioritizing candidates with high event support, low timing scatter, and high observable coverage.

### What Code Actually Does
[consensus_ranker.py](file:///d:/TARS/TarsCore/tarscore/stage3_period_recovery/consensus_ranker.py) applies a fixed linear blend: `0.4 × coverage + 0.4 × stability + 0.2 × support`.

### Assumptions Introduced
- **Weight values 0.4 / 0.4 / 0.2 were never derived**. They were manually chosen and have never been tuned, cross-validated, or derived from first principles.
- **Support score saturates at 5 events** (line 15: `min(n/5, 1.0)`). This creates a ceiling effect — a 10-event detection and a 5-event detection receive the same support score.

### What Was Lost
- **Any physics-constrained scoring**. The ranker contains zero orbital mechanics. A physically implausible period (e.g., sub-Roche limit, unstable multi-body resonance) would receive the same score as a stable orbit at the same coverage/stability values.
- **Anti-alias logic**. The ranker does not actively penalize known alias harmonics. A $2P$ harmonic can outscore the true $P$ simply by having fewer "missing" transits (because $2P$ has fewer expected transits in a given baseline).
- **Bayesian evidence accumulation** — the architecture vision included a probabilistic evidence-accumulation framework. The current heuristic is a purely phenomenological scalar score.

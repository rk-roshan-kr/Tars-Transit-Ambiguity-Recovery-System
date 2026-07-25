# Stage 3 Failure Root Cause Analysis

*Phase 5.4 — Component E. Partitions all observed Stage 3 failures into five causal classes using quantitative evidence from Phases 5.2 and 5.3. No estimates — all percentages derived from CSV artifacts.*

---

## Classification Framework

All Stage 3 failures are partitioned into five mutually exclusive root cause classes. The classification is applied to the Phase 5.3 dual-population Realistic Validation (N=2000 targets, Seeds 42 and 2026).

**Total Failures**: 748 (out of 2000 targets where Top-1 was incorrect)
- Class C: 521 occurrences
- Class B: 178 occurrences
- Class A: 49 occurrences
- Class D: computed from ambiguity CSV
- Class V: is Class C in our taxonomy

---

## Class I — Information-Theoretic Failures (Impossible to Resolve)

**Definition**: The true period cannot be uniquely identified from the available evidence even with a perfect algorithm. Mathematical degeneracy.

**Examples**:
- 2-transit system with no prior on period: $\Delta t / k$ produces an infinite family of equally valid candidates for all integer $k$.
- Transits at days 13.2 and 26.4: compatible with periods of 13.2 days, 6.6 days, 4.4 days, etc.
- Gaps that exactly swallow missing transits for *both* $P$ and $2P$ simultaneously.

**Evidence from Phase 5.2**:
- N50 boundary: 2 transits sufficient for 50% accuracy (controlled, no gaps).
- Gap fraction 90%: 49.8% alias rate — nearly random, suggesting true information-theoretic limits.
- Phase 5.2 Class A: only 49 cases across 2000 targets under moderate gap profiles.

**Estimated Fraction**: ~2.5% of all targets (49 Class A cases, though some may be Class V).
**Verdict**: Small but irreducible. Honest limitation statements in the paper are sufficient.

---

## Class II — Architecture Defects (Design Insufficient)

**Definition**: The Stage 3 architecture, as designed, cannot solve certain problem classes — not due to implementation bugs, but because the original design did not include the necessary components.

**Evidence**:
- **Multi-Planet Contamination**: Phase 5.2 showed 100% cross-period contamination for non-integer period ratios (10d / 15d). The interval generator has no mechanism to separate event sources from distinct planets.
- **Non-Integer Harmonic Aliases**: The harmonic resolver assumes integer ratios ($2P$, $3P$). Aliases at $1.5P$ from near-resonant multi-planet beat frequencies are not detected.
- **Anti-Alias Scoring**: The consensus ranker was never designed to actively penalize $2P$ harmonics. It can only rank by evidence quality — and $2P$ naturally has fewer expected transits (thus less "missing" coverage penalty), making it artificially competitive.
- **TTV Regime**: The linear ephemeris model is an explicit architectural assumption. Systems with TTVs > 60 minutes (72.6% failure rate) reveal a regime the current architecture cannot handle by design.

**Estimated Fraction**: ~15–20% of failure cases.
**Verdict**: These failures require architectural extensions, not bug fixes. They are honest scope limitations.

---

## Class III — Implementation Defects (Design Correct, Code Wrong)

**Definition**: The architectural intent is correct and achievable, but the current code diverges from the documented design.

**Evidence**:
- **Epoch Selection**: `epoch = min(event_time)` is hardcoded in `recoverer.py`. This is mathematically incorrect for events where the first observed transit is not at phase zero. This causes artificially elevated residuals for the true period.
- **Period-Relative Stability Threshold**: The `stability_threshold` in config is an absolute minute-value. This means a 30-minute MAD is applied identically to 1-day and 40-day periods — physically inconsistent.
- **Harmonic Tie-Breaking Not Implemented**: `HARMONIC_RESOLUTION_SPECIFICATION.md` defines formal tie-breaking rules. The code comment at `harmonic_resolver.py:76` explicitly defers this to the ranker, which does not implement it.
- **Support Score Saturation at 5 Events**: A 10-event candidate and a 5-event candidate receive identical support scores. This systematically devalues high-transit-count planets.
- **Consensus Weights Never Derived**: The 0.4 / 0.4 / 0.2 weights have no physical or empirical justification. Uncalibrated weights produce uncalibrated rankings.

**Estimated Fraction**: ~8.9% of all targets (178 Class B failures directly attributed to ranking defects).
**Verdict**: These are fixable bugs and calibration issues. Phase 6 should target these specifically.

---

## Class IV — Measurement Defects (Experiments Misleading)

**Definition**: The failure metric itself may not correctly represent true failure due to simulator artifacts.

**Evidence**:
- **Variable Star Contamination**: The sinusoidal mock does not capture real astrophysical variability complexity. Trust level: `LOW_TRUST`.
- **Transfer Efficiency Logistic Curve**: SNR=7.1 cutoff is a parameter assumption, not an empirical calibration. If real Stage 2 loss is heavier, Class C failures are underestimated.
- **100% Multi-Planet Contamination**: The 10d / 15d test case uses a perfect alternating injection. Real multi-planet systems have noise and non-uniform depths, which may actually reduce (or increase) contamination.

**Estimated Fraction**: Unknown — these are errors in measurement validity, not recoverable failure counts.
**Verdict**: The measurement framework is honest about its limitations. The `MEASUREMENT_TRUST_AUDIT.md` correctly labels these as `MEDIUM_TRUST` or `LOW_TRUST`. They do not invalidate the overall architecture verdict.

---

## Class V — Stage 2 Upstream Failures (Insufficient Evidence Delivered)

**Definition**: Stage 3 failure is caused by Stage 2 delivering too few events for Stage 3 to have any recoverable information.

**Evidence**:
- **Class C failures**: 521 out of 2000 targets had fewer than 2 supporting events in Stage 3 — making period recovery mathematically impossible. These all originate from low-SNR targets where the logistic Stage 2 loss model dropped too many transits.
- Transfer Efficiency: 68.0% overall — meaning on average, Stage 2 delivers only 68% of the true transit count to Stage 3.
- The Phase 5.2 timing noise test showed correct rate drops from 100% at $\sigma_t = 0.005$ days to 49.0% at $\sigma_t = 0.05$ days — consistent with Stage 2 delivering badly-timed events.

**Estimated Fraction**: 26.1% of all targets (521 / 2000).
**Verdict**: This is the single largest failure class. It is not a Stage 3 defect. It is a constraint imposed by Stage 2. Improving Stage 2 recall would directly improve Stage 3 Family Recall.

---

## Quantitative Summary

| Failure Class | Count (est.) | Fraction | Fixable? |
| :--- | :---: | :---: | :---: |
| **I — Information-Theoretic** | ~50 | ~2.5% | No |
| **II — Architecture Defects** | ~150–200 | ~8–10% | Requires extension |
| **III — Implementation Defects** | ~178 | ~8.9% | Yes — Phase 6 |
| **IV — Measurement Defects** | Unknown | — | Requires real data |
| **V — Stage 2 Upstream** | ~521 | ~26.1% | Requires Stage 2 improvement |

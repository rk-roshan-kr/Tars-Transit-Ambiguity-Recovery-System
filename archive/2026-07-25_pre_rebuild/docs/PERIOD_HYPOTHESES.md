# Stage 3: Period Hypotheses

The sparse period recovery engine is built on the following testable scientific hypotheses.

---

### H3-1: Period Stability Metric
**Hypothesis**: Period stability metric improves precision over raw interval matching.
* **Success Criterion**: Period ranking that incorporates stability (variance of $\Delta t$) achieves $>20\%$ higher accuracy on true period recovery than simply counting the maximum number of matched events.
* **Failure Criterion**: Stability metric provides no statistically significant uplift over raw event counting.
* **Audit Method**: Compare the top-1 recovery rate of a "Stability-Weighted Ranker" vs a "Raw Count Ranker" over Dataset D (Synthetic Injections).

---

### H3-2: Timing Residual Scoring
**Hypothesis**: Timing residual scoring reduces false period solutions.
* **Success Criterion**: Incorporating the RMS/MAD of timing residuals ($O-C$) reduces the false-period selection rate by at least $50\%$ compared to pure harmonic grid matching.
* **Failure Criterion**: Timing residual constraints reject true periods at an equal or greater rate than false periods.
* **Audit Method**: Evaluate False Alarm Rate on Dataset C (Random Noise) with and without residual scoring enabled.

---

### H3-3: Multi-Event Consensus
**Hypothesis**: Multi-event consensus improves recovery in sparse regimes.
* **Success Criterion**: Combining coverage fraction, event support, and residual score correctly prioritizes the true fundamental period over its aliases ($2P$, $P/2$) in $>90\%$ of cases with $\ge 3$ transits.
* **Failure Criterion**: The consensus ranking frequently selects integer multiples or fractions of the true period over the fundamental period.
* **Audit Method**: Harmonic alias recovery test using Dataset A (Confirmed Planets) and Dataset D (Synthetics).

---

### H3-4: Admissible Period Family Constriction
**Hypothesis**: TARS can constrain the admissible period family from only two observed transits.
* **Success Criterion**: The true astrophysical period remains mathematically bound inside the admissible solution family proposed by the two events.
* **Failure Criterion**: The true period is excluded from the admissible family, or the algorithm claims a unique single solution from only two timestamps (which is mathematically impossible).
* **Audit Method**: Injection recovery sweep restricted to the 2-transit regime, verifying true $P$ presence in the output set.

---

### H3-5: Harmonic Disambiguation
**Hypothesis**: TARS can distinguish the true fundamental period from integer harmonic aliases when three or more transits are available.
* **Success Criterion**: The true fundamental period is ranked strictly above its aliases in $>90\%$ of benchmark cases with $N \ge 3$.
* **Failure Criterion**: Harmonic aliases frequently outrank the true period.
* **Audit Method**: Evaluate recovery ranking on Dataset A and D where $N \ge 3$.

# Stage 3: Experiment Catalog

The following experiments must be implemented and executed to validate the Sparse Period Recovery engine prior to Stage 3 freeze.

---

### Experiment 1: Period Recovery vs Depth
* **Objective**: Measure the recovery boundary as transit depth approaches the noise floor.
* **Metric**: Recovery probability contour across Depth and $\sigma$ thresholds.

### Experiment 2: Period Recovery vs Number of Transits
* **Objective**: Quantify performance decay as the number of available transits decreases from 10 down to 2.
* **Metric**: Period precision and ranking accuracy as a function of $N_{transits}$.

### Experiment 3: Missing Transit Study
* **Objective**: Evaluate robustness against intermittently missing events.
* **Metric**: False Alarm Rate vs. Missing Epoch Fraction.

### Experiment 4: Sector Gap Study
* **Objective**: Test recovery across multi-sector baseline gaps.
* **Metric**: Harmonic alias fraction vs. Data Gap Duration (days).

### Experiment 5: False Alignment Study
* **Objective**: Ensure high-density noise environments do not trigger false periods.
* **Metric**: False positive period generation rate against simulated dense variability fields.

### Experiment 6: Long Period Planet Study
* **Objective**: Validate recovery for planets where $P >$ sector baseline, leaving only sparse transit events across years of observations.
* **Metric**: Recovery rate for $P \in [30, 100]$ days.

### Experiment 7: BLS Comparison
* **Objective**: Compare TARS Stage 3 directly against the Box Least Squares (BLS) algorithm.
* **Metric**: Relative recovery rates on Dataset E (Sparse Regime) to prove TARS superiority in ultra-low $N_{transits}$ scenarios. See `BENCHMARK_SUCCESS_CRITERIA.md` for explicit thresholds.

### Experiment 8: TLS Comparison
* **Objective**: Compare TARS Stage 3 directly against Transit Least Squares (TLS).
* **Metric**: Computational runtime vs. TLS on long baselines, and detection efficiency under significant sector gaps. See `BENCHMARK_SUCCESS_CRITERIA.md` for explicit thresholds.

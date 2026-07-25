# ECHO Spacing Regularity Validation Specification

This document defines the validation experiments and performance criteria required to certify the spacing regularity metric (`EV-P5`) and its threshold for publication-grade exoplanet vetting.

---

## 1. Validation Experiments

### Experiment SR-V1: Planet Injections (Timing Jitter Resilience)
- **Objective**: Validate that true periodic planet signals do not false-alarm (trigger a contradiction) under typical timing jitter and observation gap scenarios.
- **Method**:
  1. Inject synthetic transit sequences with periods $P \in [1.0, 50.0]$ days into real TESS data baselines ($27.4$ to $350.0$ days).
  2. Add Gaussian timing jitter $\sigma_t$ varying from $10^{-4} \cdot P$ to $10^{-2} \cdot P$.
  3. Induce active window gaps using real TESS sector data quality flags (completeness range $W_{\text{comp}} \in [0.3, 1.0]$).
  4. Measure the fraction of planet injections where `transit_spacing_regularity` stays below the config threshold ($\theta_{\text{regular}} = 0.01$).

### Experiment SR-V2: Random Event Injections (False Alarm Discrimination)
- **Objective**: Validate that random noise events that happen to align periodically are correctly identified as irregular.
- **Method**:
  1. Generate independent Poisson-distributed event sequences with average rates matching typical TESS threshold-crossing events.
  2. Perform period searches to find the best-fitting candidate period $P$.
  3. Calculate the spacing regularity of the resulting matched events.
  4. Measure the fraction of random alignments that exceed the config threshold ($\theta_{\text{regular}} = 0.01$).

### Experiment SR-V3: Eclipsing Binary (EB) Timing Simulations
- **Objective**: Validate the capability to discriminate true planet timing regularities from primary/secondary eclipsing binary variations and harmonic aliases.
- **Method**:
  1. Simulate eclipsing binary systems with distinct primary and secondary eclipse depths.
  2. Introduce typical EB timing variations (such as apsidal motion or light-travel time effects).
  3. Run the Stage 3 Period Recovery to produce candidates at both the true period and its half-period (alias).
  4. Calculate spacing regularity for each candidate to evaluate separation performance.

---

## 2. Performance Success Criteria

To certify Stage 5 ECHO as a scientifically robust instrument, the spacing regularity metric must satisfy at least one of the following statistical separation thresholds on the validation dataset:

1. **ROC-AUC $\ge 0.85$**: The area under the receiver operating characteristic curve for separating planet signals from false alarms must be greater than or equal to $0.85$.
2. **Cohen's $d \ge 1.5$**: The standardized mean difference (effect size) between the true planet distribution and the noise/EB distribution must be greater than or equal to $1.5$, indicating very low population overlap.

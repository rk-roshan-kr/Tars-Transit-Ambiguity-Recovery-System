# Morphological Coherence Validation Experiments

This document specifies the validation experiments for the Morphological Coherence equations before ECHO reasoning is calibrated.

---

## Experiment MC-V1: Eclipsing Binary (EB) Depth Separability

### Objective:
Verify that the depth coherence metric ($C_{\text{coh}}$) separates simulated planets from eclipsing binaries with alternating primary/secondary eclipse depths.

### Method:
1. Simulate 100 planetary targets with constant transit depths ($D = 10.0$ mmag).
2. Simulate 100 eclipsing binary targets with alternating depths ($D_{\text{primary}} = 15.0$ mmag, $D_{\text{secondary}} = 5.0$ mmag).
3. Compute $C_{\text{coh}}$ for each population.
4. Measure the fraction of each population correctly classified:
   - Planet: $C_{\text{coh}} \ge 0.7$ (PASS)
   - EB: $C_{\text{coh}} < 0.5$ (FAIL)

### Success Criteria:
- Planetary PASS rate $\ge 95\%$.
- Eclipsing Binary FAIL rate $\ge 95\%$.

---

## Experiment MC-V2: Duration Consistency under Measurement Jitter

### Objective:
Verify that duration consistency ($T_{\text{coh}}$) degrades gracefully as measurement uncertainty increases.

### Method:
1. Generate transit chains of $N=4$ transits with constant base duration $T = 0.1$ days.
2. Inject Gaussian measurement jitter $\sigma_T \in [0.0, 0.05]$ days into the durations.
3. Compute $T_{\text{coh}}$ across 100 trials per jitter level.
4. Confirm that mean $T_{\text{coh}}$ decreases monotonically with $\sigma_T$ and remains stable.

---

## Experiment MC-V3: Boundedness & Edge Cases Validation

### Objective:
Verify that $C_{\text{coh}}$ and $T_{\text{coh}}$ remain strictly in $[0, 1]$ even under extreme and mathematically degenerate edge cases.

### Method:
1. **Zero Mean Depth**: Generate event depth $\bar{D} = 0$, verify no division-by-zero crash and score defaults to 0.0 or 1.0.
2. **Extreme Scatter**: Generate depths where standard deviation is twice the mean ($\sigma_D = 2.0 \cdot \bar{D}$). Verify that the computed $C_{\text{coh}}$ is clipped to $0.0$ and never becomes negative.
3. **Single Event ($N=1$)**: Verify score is exactly $1.0$ (no variance defined).

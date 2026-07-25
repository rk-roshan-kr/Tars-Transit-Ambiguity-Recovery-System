# Statistical Compliance & Auditing Guidelines

This document details the statistical protocols and auditing guidelines for **TARS Core Stage 1** validation sweeps, ensuring mathematically rigorous and publication-grade reports.

---

## 1. Sample Size Requirements

Validation runs must achieve the following minimum sample sizes to ensure statistical significance:
* **Large-Scale Population Sweep**: Process all eligible local targets. At least $N \ge 1000$ unique light curves must be verified.
* **Overlapping Sector Sweep**: At least $N \ge 50$ stars observed across 3 or more sectors.
* **Synthetic Injection Trials**: For each grid cell (e.g., in recovery heatmaps), at least $N_{\rm trials} \ge 30$ independent noise realizations must be performed.

---

## 2. Bootstrap Confidence Intervals

All reported uncertainty bounds for population statistics must be computed using bootstrap resampling:
* **Resample Count**: $B = 1000$ iterations.
* **Confidence Level**: $95\%$ (two-tailed).
* **Resampling Method**: Percentile bootstrap method.
* **Estimator**: The statistic evaluated is the sample median.
* **Implementation**: Uses [calculate_bootstrap_ci](file:///d:/TARS/TarsCore/research/bootstrap_utils.py#L9-L63).

---

## 3. Random Seed Policies

To guarantee mathematical determinism and auditability, all random number generation (RNG) must follow these strict policies:
* **No Global State Modification**: Do not call `np.random.seed()` globally. Instead, instantiate local generators using `np.random.default_rng(seed)`.
* **Seed Offset Formula**: The seed for a specific trial must be computed deterministically from the sweep parameters and trial index. Example:
$$\text{seed} = \text{base\_seed} + \lfloor \text{depth} \times 100000 \rfloor + \text{trial}$$
* **Multiple Base Seeds**: Reproducibility audits must run over 10 pre-selected independent base seeds:
`[42, 123, 456, 789, 999, 1001, 2026, 7777, 8888, 9999]`.
* **Seed Variance Assertion**: The coefficient of variation (CV) for the operating boundaries across all 10 seeds must remain below $1.0\%$.

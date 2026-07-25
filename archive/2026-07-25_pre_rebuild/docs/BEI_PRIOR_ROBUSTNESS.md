# BEI Prior Robustness (Phase 10.1)

This report evaluates posterior sensitivity and category transitions under varying prior probabilities $P(H) \in \{0.01, 0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.99\}$, providing a stress-test of boundary values and numerical stability.

---

## 1. Prior Sensitivity Sweep

The table below summarizes the posterior shift and category stability compared to the reference prior $P(H) = 0.50$:

| Prior $P(H)$ | Mean Posterior Shift | $95^{\text{th}}$ Pct. Shift | Migrations Count | Stability % | Verdict |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **0.01** | $2.83 \times 10^{-5}$ | $7.97 \times 10^{-10}$ | 2 | $99.97\%$ | **STABLE** |
| **0.05** | $5.80 \times 10^{-6}$ | $1.63 \times 10^{-10}$ | 1 | $99.98\%$ | **STABLE** |
| **0.10** | $2.63 \times 10^{-6}$ | $8.52 \times 10^{-11}$ | 1 | $99.98\%$ | **STABLE** |
| **0.25** | $6.75 \times 10^{-7}$ | $2.29 \times 10^{-11}$ | 0 | $100.00\%$ | **STABLE** |
| **0.50** | $0.000$ | $0.000$ | 0 | $100.00\%$ | **STABLE** |
| **0.75** | $2.78 \times 10^{-7}$ | $1.02 \times 10^{-11}$ | 0 | $100.00\%$ | **STABLE** |
| **0.90** | $5.26 \times 10^{-7}$ | $1.64 \times 10^{-11}$ | 0 | $100.00\%$ | **STABLE** |
| **0.99** | $3.16 \times 10^{-6}$ | $3.52 \times 10^{-11}$ | 0 | $100.00\%$ | **STABLE** |

---

## 2. Category Transition Analysis

Transitions and category migrations logged during sweeps:

* **At $P(H) = 0.01$**:
  - 1 candidate migrated from `VERY_STRONG` to `STRONG`.
  - 1 candidate migrated from `VERY_STRONG` to `MODERATE`.
* **At $P(H) = 0.05$**:
  - 1 candidate migrated from `VERY_STRONG` to `STRONG`.
* **At $P(H) = 0.10$**:
  - 1 candidate migrated from `VERY_STRONG` to `STRONG`.

*All other sweeps (including $P(H) = 0.99$) recorded zero category transitions.*

---

## 3. Physical Interpretation

The extreme stability of the posterior categories under massive prior shifts (e.g. from $0.50$ to $0.01$ or $0.99$) is physically expected. The combined Bayes Factor evidence across the 16 features is highly informative, resulting in total log Bayes Factors that commonly reside in the range $[-30, +40]$.

Since the prior's contribution in log space is small (ranging from $\ln(0.01/0.99) \approx -4.6$ to $\ln(0.99/0.01) \approx +4.6$), the likelihood ratio completely dominates the posterior odds. This is a highly desirable property for astrophysical candidate validation: the final classification belief is driven by physical measurements rather than initial prior assumptions.

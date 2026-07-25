# Stage 4 Gap Resilience Audit

*Phase 7.1 — Scientific Validation Phase. Verification of Hypothesis HEEA-3 and gap-induced family behaviors.*

---

## 1. Correlation Analysis

Using the sweep trials from `eea_gap_resilience.csv`, we computed the Spearman rank correlation of the candidate family metrics with the observational `gap_fraction`:

* **`information_content` (Shannon Entropy) vs `gap_fraction`**:
  * Spearman correlation $r$: **$-0.9860$**
  * p-value: **$1.7 \times 10^{-140}$**
* **`ambiguity_index` vs `gap_fraction`**:
  * Spearman correlation $r$: **$+0.6511$**
  * p-value: **$4.4 \times 10^{-23}$**

---

## 2. Hypothesis HEEA-3 Verdict

### Statement
`information_content` (Shannon entropy of the candidate family score distribution) increases monotonically as `gap_fraction` increases.

### Falsification Condition
Spearman correlation between gap_fraction and information_content is not significantly positive ($\rho < 0.3, p > 0.05$).

### Scientific Analysis
* The measured correlation is **strongly negative** ($r = -0.9860$, $p \approx 0$).
* **Reason**: When the gap fraction is very large, Stage 3's coverage and support filters reject many of the weaker harmonic candidates *before* they reach Stage 4. Consequently, the family size ($K$) collapses (e.g. from 7 candidates down to 1 or 2). Since Shannon entropy is mathematically bounded by $\log K$, the entropy decreases as the family collapses.
* Therefore, the pre-registered hypothesis **HEEA-3 is falsified**.

### Verdict
> [!WARNING]
> **HEEA-3 Verdict**: **FAIL (FALSIFIED)**
> *Note: This is a scientifically valuable result. It proves that while gaps increase individual candidate ambiguity, they contract the global search space by filtering out unobservable periods, thereby reducing the family Shannon entropy.*

---

## 3. Ambiguity Index Trend

* The positive correlation ($r = +0.6511$) between `gap_fraction` and `ambiguity_index` demonstrates that as gaps increase, the score delta between the top 1 and top 2 solutions shrinks (they become closer in score), raising the ambiguity index (closer to 1.0).
* This confirms that **Stage 4 successfully tracks gap-induced ambiguity**.

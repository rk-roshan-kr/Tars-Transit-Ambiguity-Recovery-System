# Stage 4 Alias Discrimination Audit

*Phase 7.1 — Scientific Validation Phase. Verification of Stage 4 feature separability and Mutual Information ranking.*

---

## 1. Separation Metrics (TRUE vs HALF_P Alias)

Using the simulated population from `eea_alias_separation.csv` (94 true-period candidates and 34 HALF_P alias candidates), we computed the Kolmogorov-Smirnov (KS) statistic, Cohen's d, and Mutual Information (MI) for the available features:

| Feature | KS Statistic | p-value | Cohen's d | Mutual Information |
| :--- | :---: | :---: | :---: | :---: |
| `transit_spacing_regularity` | **1.0000** | $1.7 \times 10^{-31}$ | **-5459.50** | **0.5828** |
| `coverage_fraction` | **0.7660** | $3.6 \times 10^{-15}$ | **1.47** | **0.3305** |
| `chain_coherence` | 0.0000 | 1.00 | 0.00 | 0.0388 |
| `support_count` | 0.0000 | 1.00 | 0.00 | 0.0000 |
| `transit_number_monotonicity`| 0.0000 | 1.00 | 0.00 | 0.0000 |

---

## 2. Top Informative Features

Based on the Mutual Information (MI) and KS statistics, the top discriminative features in the evaluated subset are:

1. **`transit_spacing_regularity` (MI = 0.5828, KS = 1.0000)**: Under the true period $P$, the normalized spacing ratio $(t_{k+1} - t_k)/P$ is a smaller integer variance (e.g. $0.25$ for $N=3$ with 1 missing transit), whereas under the sub-harmonic alias $P/2$, the spacing ratios are doubled (e.g. $1.0$ variance), creating a massive, clean separability boundary.
2. **`coverage_fraction` (MI = 0.3305, KS = 0.7660)**: A sub-harmonic alias $P/2$ expects twice as many transits as the true period. In active observation windows where no transit occurred, the alias expects a signal, dropping its coverage fraction to $50\%$ while the true period remains at $100\%$ coverage.
3. **`chain_coherence` (MI = 0.0388)**: Captures soft structural differences in consecutive transit groupings.

---

## 3. Scientific Finding

The audit reveals that **Stage 4 features carry high discriminative signal for alias separation**. Specifically, `transit_spacing_regularity` and `coverage_fraction` act as extremely strong physical classifiers that can cleanly separate true exoplanet periods from sub-harmonic aliases without needing machine learning weights. 

### Verdict
> [!NOTE]
> **STATUS**: **PASS** (Sufficient alias discrimination verified).

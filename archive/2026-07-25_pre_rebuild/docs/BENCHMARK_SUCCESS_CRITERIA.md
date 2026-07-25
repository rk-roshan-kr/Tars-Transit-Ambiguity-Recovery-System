# Stage 3: Benchmark Success Criteria

To prevent post-hoc interpretation of scientific results, the exact criteria defining "success" for Stage 3 experiments must be declared in advance.

---

### Experiment 7: Box Least Squares (BLS) Comparison
**Objective**: Prove TARS superiority in ultra-sparse regimes vs BLS.
**Success Criterion**: 
TARS must achieve a statistically significant improvement in recovery rate on Dataset E (Sparse Regime). Specifically, TARS must recover the true period (or an admitted harmonic alias) in $\ge 15\%$ more injection scenarios than standard astropy BLS when the total number of transits is $N \le 3$. 
**Failure Criterion**: 
TARS recovery rate is $\le 15\%$ better, equal to, or worse than BLS on sparse datasets.

---

### Experiment 8: Transit Least Squares (TLS) Comparison
**Objective**: Prove TARS provides tangible advantages over TLS in specific domains.
**Success Criterion**: 
TARS must demonstrate AT LEAST ONE of the following relative to TLS:
1. **Sparse Recovery**: $>10\%$ higher true period recovery on $N \le 3$ gap-heavy datasets.
2. **Computational Scaling**: $O(N)$ runtime scaling vs TLS $O(N \log N)$ grid search, achieving $>5\times$ speedup on 1-million cadence baseline data.
3. **Robustness to Gaps**: Lower harmonic alias susceptibility when sector gaps exceed $50\%$ of the observation baseline.
**Failure Criterion**: 
TARS matches TLS recovery but remains computationally slower, or TARS runs faster but suffers degraded recovery accuracy across the board.

# Stage 3: Limitations and Non-Claims

To preserve scientific credibility and preempt hostile reviewer attacks, TARS explicitly registers the following limitations. We will **never** make the following claims in any publication, documentation, or codebase representation.

---

### TARS will NEVER claim:
1. **"TARS is a universally superior replacement for BLS or TLS."**
   * *Reality*: TARS is highly specialized for sparsity. BLS/TLS remain the gold standard for dense, continuous, low-SNR time series.
2. **"TARS outperforms TLS at low Signal-to-Noise Ratios."**
   * *Reality*: If an individual transit is too shallow to trigger Stage 2 detection, Stage 3 receives zero evidence. TLS can fold and average thousands of sub-threshold transits to pull them out of the noise. TARS cannot.
3. **"TARS guarantees a unique period recovery from two transits."**
   * *Reality*: Two transits separated by a gap mathematically yield an infinite family of harmonic solutions ($P$, $P/2$, $P/3$). TARS bounds the *admissible family*, but will never claim to magically guess the unique fundamental period without further evidence.
4. **"TARS is immune to stellar variability."**
   * *Reality*: If complex stellar activity produces discrete features that perfectly mimic transit morphology and align strictly on a linear ephemeris, TARS will recover them. TARS assumes Stage 2 has already filtered non-planetary morphologies.
5. **"The Consensus Ranking algorithm is derived from physical laws."**
   * *Reality*: Feature extraction (RMS, coverage) is physical; combining them into a sorting score is a computational heuristic (`H-S3-01`).
6. **"TARS requires zero configuration."**
   * *Reality*: While the architecture is dataset-independent, tuning the harmonic tolerance and stability thresholds requires domain knowledge of the target instrument's timing precision.

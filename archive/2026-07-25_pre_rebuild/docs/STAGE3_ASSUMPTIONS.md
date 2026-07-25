# Stage 3 Assumptions

1. **Linear Ephemeris**: TARS Stage 3 strictly assumes a linear, Keplerian orbit ($t_n = t_0 + n \times P$). Highly non-linear transit timing variations (TTVs) will result in elevated MAD residuals and potential rejection.
2. **Pre-filtered Events**: Stage 3 assumes that Stage 1 (Conditioning) and Stage 2 (Detection) have successfully localized high-probability transits. Massive false-positive crowds (e.g. dense background binaries) will computationally explode the $O(N_{events}^2)$ interval generation.
3. **Sector Agnosticism**: TARS assumes that data gaps represent missing data, not necessarily non-transit regions, and penalizes coverage only when expected transits land in valid observable regions.

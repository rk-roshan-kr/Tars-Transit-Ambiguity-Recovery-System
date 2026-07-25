# Stage 3: Reviewer Attack Matrix

This document anticipates and neutralizes scientific, statistical, and architectural criticisms from hostile reviewers.

| Attack ID | Reviewer Criticism | Severity | Response |
| :--- | :--- | :--- | :--- |
| **A-01** | "This is just interval matching." | Moderate | **Defense**: Raw interval matching fails on gaps and harmonics. TARS incorporates Observation Window modeling and physics-aware timing residuals to move beyond simple string-length matching. |
| **A-02** | "This is a simplified periodogram." | Low | **Defense**: Periodograms operate on continuous flux arrays. TARS operates strictly in discrete event-space, changing the computational domain from $O(N_{cadences})$ to $O(N_{events})$. |
| **A-03** | "This is BLS in disguise." | High | **Defense**: BLS folds the entire light curve and searches a dense frequency grid. TARS reconstructs chains from localized event data only. The mathematics are fundamentally distinct. |
| **A-04** | "There is no new science here." | Moderate | **Defense**: The novelty lies in formally resolving period topologies when data sparsity breaks continuous folding assumptions. |
| **A-05** | "Why not run Lomb-Scargle on the events?" | Low | **Defense**: Lomb-Scargle requires continuous amplitudes. Discrete events lack amplitude variance, violating LS assumptions. |
| **A-06** | "Event-chaining is already used in other fields." | Low | **Limitation**: We do not claim inventing event-chaining; we claim its novel formalization for exoplanetary sparse recovery in the TESS/PLATO era. |
| **B-01** | "Coverage fraction biases longer periods." | High | **Revision**: Implemented rigorous Observation Window Model. Coverage fraction now dynamically scales $N_{expected}$ by subtracting time lost in data gaps, eliminating long-period bias. |
| **B-02** | "Residual MAD favors shorter periods." | Moderate | **Defense**: Shorter periods have more transits, naturally shrinking the standard error. This reflects physical reality, not an algorithmic bias. |
| **B-03** | "Sparse events create unstable solutions." | Critical | **Limitation**: We formally acknowledge this in `FAILURE_MODES_STAGE3.md`. TARS explicitly returns an admissible family for $N=2$, not a unique scalar. |
| **B-04** | "Uncertainty estimates are optimistic." | High | **Defense**: Uncertainties are derived from the covariance matrix of the linear ephemeris fit, honoring true event-timing variance. |
| **B-05** | "Missing false positives in sparse regimes inflate confidence." | Moderate | **Defense**: The consensus ranker explicitly penalizes missing events in observable windows, driving down confidence if expected false positives don't align. |
| **B-06** | "Consensus score weights are arbitrary." | High | **Revision**: Extracted into `HEURISTIC_REGISTRY_STAGE3.md`. Explicitly declared as an experimental heuristic separated from physical equations. |
| **C-01** | "Transit timing variations violate assumptions." | Moderate | **Defense**: TTVs naturally inflate `residual_mad`. Highly non-linear TTVs will fail recovery, which is a stated limitation of linear ephemeris models. |
| **C-02** | "Sector gaps create aliases." | Critical | **Defense**: True. TARS addresses this by returning `WARNING_HARMONIC_AMBIGUITY` when multiple aliases perfectly fit the gaps. |
| **C-03** | "Missing transits bias period estimation." | High | **Defense**: If an event is missing during an observable window, `coverage_fraction` plummets, safely killing the hypothesis. |
| **C-04** | "Multi-planet systems break reconstruction." | Moderate | **Defense**: TARS groups intervals by harmonic clusters. Distinct planets form distinct clusters. Overlapping events increase background noise but do not break the fundamental math. |
| **C-05** | "Stellar spots mimic transits and create false chains." | High | **Defense**: Spot evolution scales dynamically. The probability of random spots forming a rigid linear ephemeris over long baselines is astronomically low. |
| **C-06** | "N=2 long periods could just be two separate planets." | Critical | **Limitation**: Acknowledged. We explicitly report `WARNING_HARMONIC_AMBIGUITY` and state that $N=2$ only identifies an admissible family, not a unique planet. |
| **D-01** | "BLS was tuned poorly in your benchmark." | High | **Defense**: TARS benchmarks use standard `astropy.timeseries.BoxLeastSquares` with grid oversampling factors recommended by literature. |
| **D-02** | "TLS comparison is unfair." | Moderate | **Defense**: TLS is designed for low-SNR, dense data. TARS explicitly documents that TLS is superior at low SNR. The comparison only targets sparse efficiency. |
| **D-03** | "Dataset E favors TARS." | Low | **Defense**: Dataset E isolates the exact mathematical regime (high sparsity) where continuous folders fail. It is designed to probe boundary limits, not general averages. |
| **D-04** | "Recovery metric is biased." | Moderate | **Defense**: Success criteria are pre-registered in `BENCHMARK_SUCCESS_CRITERIA.md` before experiments run. |
| **D-05** | "TARS has an unfair advantage using truth events." | High | **Defense**: TARS does not use truth events. The benchmark feeds the exact same raw Stage 2 output into TARS as the continuous flux fed into BLS. |
| **D-06** | "False Alarm rate in benchmarks doesn't match real data." | Moderate | **Defense**: We utilize Dataset B (real eclipsing binaries) and Dataset C (real random noise stars) specifically to validate empirical False Alarm rates. |
| **E-01** | "Algorithm is not scalable (O(N²) permutations)." | High | **Defense**: Interval generation is $O(N_{events}^2)$. Since $N_{events}$ is tiny ($\ll 100$), this is effectively $O(1)$ compared to $O(N_{cadences} \log N_{cadences})$ for continuous arrays. |
| **E-02** | "Results are irreproducible." | Critical | **Defense**: Every output `PeriodCandidate` is bundled with a `PeriodForensics` audit trail documenting exact features, residuals, and clustering decisions. |
| **E-03** | "Heuristic dominates scientific decisions." | High | **Defense**: As defined in Phase 4.1, heuristics only sort the output list. The generation and inclusion of periods is purely physical and mathematical. |
| **E-04** | "Failure modes are hidden." | Moderate | **Defense**: All failure modes are explicitly cataloged in `FAILURE_MODES_STAGE3.md` and injected into the forensics payload. |
| **E-05** | "Memory limits on massive clusters." | Low | **Defense**: Interval generation drops long-baseline arrays into compact sparse matrices. Memory footprint is infinitesimally small. |
| **E-06** | "Hardcoded assumptions hidden in code." | Critical | **Defense**: Zero hardcoded assumptions exist. All parameters are config-driven, and all equations are mathematically registered. |

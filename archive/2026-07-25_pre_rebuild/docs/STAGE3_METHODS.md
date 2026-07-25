# Stage 3 Methods

## Interval Generation
Stage 3 does not perform continuous grid searches. It generates a discrete set of admissible hypotheses by computing pairwise timing intervals $\Delta t = t_j - t_i$ and dividing them by harmonic orders $k \in [1, K_{max}]$. 

## Harmonic Resolution
Generated hypotheses are clustered agglomeratively based on a timing uncertainty tolerance ($\sigma_t$). Intractable harmonic ambiguities (where multiple integer multiples of a period explain the same gaps) are formally labeled as `WARNING_HARMONIC_AMBIGUITY`.

## Observation Window Modeling
The engine intersects theoretical ephemeris times with the actual valid cadences observed by the telescope. Transits expected to fall during known sector gaps or momentum dumps are discarded from the penalty pool, preventing long-period biases.

## Residual and Uncertainty Analysis
Timing residuals ($O-C$) are computed for all matching events. A weighted linear regression extracts the final covariance, bounding the recovered period with strict $\mu_P \pm \sigma_P$ limits.

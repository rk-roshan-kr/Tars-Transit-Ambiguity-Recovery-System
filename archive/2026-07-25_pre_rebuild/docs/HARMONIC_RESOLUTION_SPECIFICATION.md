# Stage 3: Harmonic Resolution Specification

This specification formalizes how TARS resolves, identifies, and handles harmonic ambiguities when recovering periods from sparse transit sequences. 

## 1. Harmonic Cluster Formation

When pairwise event intervals $\Delta t(i,j)$ are generated, they form clusters around specific time lengths. A cluster is formed using a **Tolerance Model** based on the underlying event timing uncertainties $\sigma_t$:

* **Clustering Method**: Agglomerative 1D clustering of all generated intervals.
* **Tolerance Limit**: Two intervals $\Delta t_a$ and $\Delta t_b$ belong to the same harmonic cluster if $|\Delta t_a - \Delta t_b| < (\sigma_{t_a} + \sigma_{t_b})$.

## 2. Alias Identification Rules

Once clusters are formed and a primary period $P$ is proposed, all other candidate periods $P_x$ are evaluated as potential aliases based on ratio $R = P_x / P$. They are formally labeled:

* `FUNDAMENTAL`: The selected baseline period $P$.
* `2P_ALIAS`: When $R \approx 2.0$.
* `3P_ALIAS`: When $R \approx 3.0$.
* `HALF_P_ALIAS`: When $R \approx 0.5$.
* `OTHER_ALIAS`: When $R \approx N$ or $R \approx 1/N$ for other integer $N$.

The precision required for $\approx$ is bound by the cumulative timing uncertainty across the baseline.

## 3. Fundamental Selection Rules

When multiple aliases (e.g., $P$ and $2P$) perfectly explain the observed events, TARS employs the following explicit preference hierarchy:

1. **Event Support Preference**: If $P$ aligns with $N=5$ events, but $2P$ aligns with only $N=3$ events (and the other $2$ are missing), $P$ is strongly preferred.
2. **Coverage Preference**: If $P$ expects $10$ transits and we observe $5$, while $2P$ expects $5$ transits and we observe $5$, $2P$ has higher coverage ($100\%$ vs $50\%$) and is preferred (Occam’s Razor).
3. **Residual Preference**: If support and coverage are equal, the alias producing the statistically tighter $MAD_r$ (lower timing residual dispersion) is preferred.

## 4. Tie-Break Rules and Intractable Ambiguity

If after applying the selection rules, two aliases remain statistically indistinguishable (e.g., $P$ and $2P$ have identical support, identical coverage due to data gaps, and statistically identical residuals):

* **Rule**: TARS MUST NOT force a winner.
* **Output**: The system must return both periods as co-top solutions.
* **Flag**: The result must explicitly include the flag `WARNING_HARMONIC_AMBIGUITY`. 

Scientific integrity requires explicitly acknowledging degenerate solutions rather than guessing.

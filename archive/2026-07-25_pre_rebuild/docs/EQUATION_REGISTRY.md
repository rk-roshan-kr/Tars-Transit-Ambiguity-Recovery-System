# Stage 1 Equation Registry

This registry lists all mathematical formulas and estimators employed in **TARS Core Stage 1 (Signal Conditioning & Noise Characterization)**. These equations are frozen for production-grade exoplanet detection audits.

---

## EQ-S1-01 — Sliding Median Detrending

### Equation:
$$f_{\text{detrended}, i} = \frac{f_i}{\text{median}(f_{[i - W/2 : i + W/2]})}$$

Where $W$ is the sliding window size in cadences (derived from `detrend_window_days` divided by typical cadence spacing $\Delta t$).

### Description:
Removes long-term stellar variability and instrumental drifts by dividing the raw normalized flux by a sliding median calculated over a centered temporal window. The division preserves the relative transit depth across varying stellar flux baselines.

### Inputs & Outputs:
* **Inputs**:
  * $f_i$: Raw/normalized cadence flux (unitless ratio)
  * $W$: Window size (integer cadences)
* **Outputs**:
  * $f_{\text{detrended}, i}$: Detrended flux (unitless ratio)

### Origin:
Physical / Empirical astronomy standard.

---

## EQ-S1-02 — Robust Local Noise Estimate (Local MAD)

### Equation:
$$\sigma_{\text{local}, i} = 1.4826 \times \text{median}\left(\left| f_{\text{detrended}, [i-W_{\text{noise}}/2 : i+W_{\text{noise}}/2]} - \text{median}\left(f_{\text{detrended}, [i-W_{\text{noise}}/2 : i+W_{\text{noise}}/2]}\right) \right|\right)$$

### Description:
Estimates the local noise level around each cadence using a sliding Median Absolute Deviation (MAD) scaled by $1.4826$ to serve as a consistent estimator for the standard deviation under Gaussian noise. The window size $W_{\text{noise}}$ is set by `noise_window_days`.

### Inputs & Outputs:
* **Inputs**:
  * $f_{\text{detrended}}$: Detrended flux array
  * $W_{\text{noise}}$: Sliding window size (integer cadences)
* **Outputs**:
  * $\sigma_{\text{local}, i}$: Per-cadence local noise standard deviation (unitless ratio)

### Origin:
Statistical.

---

## EQ-S1-03 — Robust White Noise Estimator (First-Difference MAD)

### Equation:
$$\sigma_{\text{white}} = 1.4826 \times \frac{\text{MAD}(\Delta r)}{\sqrt{2}}$$

Where:
$$\Delta r_i = r_{i+1} - r_i$$
$$r_i = f_{\text{detrended}, i} - 1.0$$
$$\text{MAD}(\Delta r) = \text{median}\left( |\Delta r - \text{median}(\Delta r)| \right)$$

### Description:
Isolates high-frequency point-to-point scatter (white noise) by calculating the first-difference of residuals. The first-difference operation cancels out low-frequency trends. Scaling by $1.4826 / \sqrt{2}$ converts the MAD of differences into a standard deviation of the underlying white noise.

### Inputs & Outputs:
* **Inputs**:
  * $r$: Residuals array ($f_{\text{detrended}} - 1.0$)
* **Outputs**:
  * $\sigma_{\text{white}}$: Global point-to-point white noise estimate (unitless ratio)

### Origin:
Statistical.

---

## EQ-S1-04 — Correlated (Red) Noise Estimator

### Equation:
$$\sigma_{\text{red}} = \sqrt{\max\left(0, \sigma_M^2 - \frac{\sigma_{\text{white}}^2}{M}\right)}$$

Where:
* $M$ is the number of cadences corresponding to `bin_duration_hours` (default = 3.0 hours)
* $\sigma_M$ is the binned residual standard deviation, calculated robustly as:
$$\sigma_M = 1.4826 \times \text{MAD}(r_M)$$
$$r_{M, k} = \frac{1}{M} \sum_{j=1}^{M} r_{(k-1)M + j}$$

### Description:
Quantifies correlated noise on typical transit timescales. The observed binned variance $\sigma_M^2$ is compared to the theoretical white noise expectation $\sigma_{\text{white}}^2 / M$. Any excess variance is attributed to correlated red noise $\sigma_{\text{red}}$.

### Inputs & Outputs:
* **Inputs**:
  * $r$: Residuals array
  * $\sigma_{\text{white}}$: Estimated white noise
  * $M$: Points per bin (integer cadences)
* **Outputs**:
  * $\sigma_{\text{red}}$: Correlated noise standard deviation on a 3-hour binned scale (unitless ratio)

### Origin:
Statistical / Empirical astrophysics.

---

## EQ-S1-05 — Lag-1 Autocorrelation

### Equation:
$$\rho_{\text{lag1}} = \frac{\sum_{i=1}^{N-1} (r_i - \bar{r}_1)(r_{i+1} - \bar{r}_2)}{\sqrt{\sum_{i=1}^{N-1} (r_i - \bar{r}_1)^2 \sum_{i=1}^{N-1} (r_{i+1} - \bar{r}_2)^2}}$$

Where $\bar{r}_1$ is the mean of $r_{1:N-1}$ and $\bar{r}_2$ is the mean of $r_{2:N}$.

### Description:
Measures the Pearson correlation coefficient between consecutive residuals. Values near 0 indicate white-noise dominance, while positive values indicate correlated red noise residuals from stellar variability or instrumental systematics.

### Inputs & Outputs:
* **Inputs**:
  * $r$: Residuals array
* **Outputs**:
  * $\rho_{\text{lag1}}$: Lag-1 autocorrelation coefficient ($\in [-1, 1]$)

### Origin:
Statistical.

---

## EQ-S1-06 — Red Noise Beta Factor

### Equation:
$$\beta = \frac{\sigma_{\text{red}}}{\sigma_{\text{white}}}$$

### Description:
The ratio of the binned correlated noise to the point-to-point white noise. A beta factor $\beta \ll 0.1$ signifies a white-noise-dominated light curve, whereas $\beta > 0.5$ signals significant red-noise contamination.

### Inputs & Outputs:
* **Inputs**:
  * $\sigma_{\text{red}}$: Correlated red noise
  * $\sigma_{\text{white}}$: White noise
* **Outputs**:
  * $\beta$: Red noise scaling factor (unitless)

### Origin:
Statistical / Empirical.

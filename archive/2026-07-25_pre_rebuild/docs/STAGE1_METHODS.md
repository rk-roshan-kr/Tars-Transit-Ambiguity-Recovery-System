# Stage 1 Methods — Signal Conditioning & Noise Characterization

This document describes the mathematical and statistical formulations implemented in Stage 1 of TARS Core.

---

## 1. Median Filter Detrending

### Equation
The trend line $T_i$ at cadence index $i$ is calculated using a centered sliding median filter:
$$T_i = \text{median}\left( \{f_j\}_{j \in W_i} \right)$$
where $f_j$ is the raw flux, and $W_i$ is a window of width $N_{\text{detrend}}$ cadences centered at index $i$:
$$W_i = \left[ i - \lfloor N_{\text{detrend}}/2 \rfloor, \, i + \lfloor N_{\text{detrend}}/2 \rfloor \right]$$

The detrended flux $f'_{i}$ is calculated by division:
$$f'_{i} = \frac{f_i}{T_i}$$

### Assumptions
* **Time Scale Separation**: The stellar rotation, instrumental drift, and other systematic trends vary on timescales significantly longer than the detrending window ($T_{\text{trend}} \gg \text{detrend\_window\_days}$).
* **Transit Conservation**: The duration of target transits is significantly shorter than the detrending window ($T_{\text{transit}} \ll \text{detrend\_window\_days}$), preventing the median filter from altering transit depths.

### Limitations
* **Transit Attenuation**: For long-duration transits (e.g. $T_{\text{transit}} \ge 8$ hours), self-containment of transit points within the sliding window will pull down the median, resulting in shallowing of the recovered transit depth (depth attenuation).

---

## 2. Local Noise Estimator

### Equation
The local noise $\sigma_{\text{local}, i}$ at index $i$ is computed using the robust Median Absolute Deviation (MAD) over a noise window $W_i$ of width $N_{\text{noise}}$ cadences:
$$\text{MAD}_i = \text{median}\left( \{|f'_j - \text{median}(\{f'_k\}_{k \in W_i})|\}_{j \in W_i} \right)$$
$$\sigma_{\text{local}, i} = 1.4826 \times \text{MAD}_i$$

### Rationale
MAD is a highly robust estimator of scale, meaning it is insensitive to outliers such as cosmic ray spikes, stellar flares, or transit dips. The factor $1.4826$ scales the MAD to be a consistent estimator of the standard deviation under a Gaussian distribution.

---

## 3. White Noise Estimation

### Equation
White noise $\sigma_{\text{white}}$ represents the uncorrelated point-to-point scatter and is estimated using first-difference residuals:
$$\Delta f_i = f'_{i+1} - f'_{i}$$
$$\sigma_{\text{white}} = 1.4826 \times \frac{\text{MAD}(\Delta f)}{\sqrt{2}}$$
where the division by $\sqrt{2}$ accounts for the variance addition of subtracting two independent, identically distributed variables.

### Rationale
By taking first differences, slow systematic trends or stellar variations are subtracted out, isolating the pure high-frequency white noise floor.

---

## 4. Red Noise Estimation

### Equation
Red noise $\sigma_{\text{red}}$ represents the correlated noise component and is estimated by binning the residuals $r_i = f'_i - 1.0$ into non-overlapping blocks of size $M$ cadences (representing a typical 3-hour transit duration):
$$R_{b, k} = \frac{1}{M} \sum_{j=kM}^{(k+1)M - 1} r_j$$
$$\sigma_M = 1.4826 \times \text{MAD}(R_b)$$
$$\sigma_{\text{red}} = \sqrt{\max\left(0, \, \sigma_M^2 - \frac{\sigma_{\text{white}}^2}{M}\right)}$$

### Rationale
In the presence of only white noise, the binned standard deviation $\sigma_M$ scales exactly as $\sigma_{\text{white}} / \sqrt{M}$. Any excess variance observed in binned data indicates the presence of correlated red noise.

---

## 5. Beta Factor

### Equation
$$\beta = \frac{\sigma_{\text{red}}}{\sigma_{\text{white}}}$$

> [!IMPORTANT]
> This is a TARS-specific diagnostic quantity measuring the ratio of correlated to uncorrelated noise on a 3-hour binned timescale. It is **not** the Carter & Winn (2009) $\beta$ factor (which is defined as $\sigma_{\text{binned}} / (\sigma_{\text{white}}/\sqrt{M})$ and scales to $\ge 1.0$). Here, $\beta \approx 0$ under pure Gaussian noise, providing a clean indicator of correlation.

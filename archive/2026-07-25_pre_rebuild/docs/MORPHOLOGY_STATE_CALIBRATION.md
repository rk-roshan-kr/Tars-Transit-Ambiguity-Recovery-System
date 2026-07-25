# Morphology State Calibration

This document presents the physical and statistical calibration of the morphology state boundaries used in the `MorphologicalCoherenceReport` decision framework.

---

## 1. Mathematical Framework

The depth coherence score is defined as:
$$C_{\text{coh}} = \max\left(0.0, 1.0 - \frac{\sigma_D}{\bar{D}}\right)$$
which represents $1.0$ minus the coefficient of variation (CV) of the transit depths.

Under Gaussian white noise with local standard deviation $\sigma_{\text{local}}$, the uncertainty of each depth measurement $D_i$ is:
$$\sigma_{D_i} \approx \frac{\sigma_{\text{local}}}{\sqrt{M}}$$
where $M$ is the number of cadences in the transit (typically $M \approx 6$ for a 3-hour transit at 30-minute cadence).

For a real planet with a constant physical transit depth $D_{\text{true}}$, the measured depths $D_i$ will scatter around $D_{\text{true}}$ with standard deviation $\sigma_{D_i}$. The expected coefficient of variation is:
$$\text{CV}_D = \frac{\sigma_D}{\bar{D}} \approx \frac{\sigma_{\text{local}}}{\bar{D} \sqrt{M}} = \frac{1}{\text{SNR}_D \sqrt{M}}$$
where $\text{SNR}_D = \bar{D} / \sigma_{\text{local}}$ is the transit depth signal-to-noise ratio.

---

## 2. Boundary Justifications

### STRONG State ($C_{\text{coh}} \ge 0.7$)
- **Condition**: $\text{CV}_D \le 0.3$.
- **Justification**: A coefficient of variation $\le 30\%$ represents tight clustering around the mean depth.
- **Physical context**: For a typical planet with $D = 1\%$ ($10$ mmag) and TESS white noise of $0.6$ mmag, $\text{SNR}_D = 16.7$. With $M = 6$, the expected $\text{CV}_D \approx 1 / (16.7 \cdot 2.45) \approx 0.024$, yielding $C_{\text{coh}} \approx 0.97$.
- Even at a marginal detection threshold of $\text{SNR}_D = 4.0$, the expected $\text{CV}_D \approx 0.10$, yielding $C_{\text{coh}} \approx 0.90$. Therefore, $C_{\text{coh}} \ge 0.7$ is a highly conservative threshold for planets.

### WEAK State ($C_{\text{coh}} < 0.5$)
- **Condition**: $\text{CV}_D > 0.5$.
- **Justification**: A coefficient of variation $> 50\%$ represents extreme depth scatter.
- **Physical context**: Such wide variation is physically incompatible with a stable occulting planetary disk. It is expected only in:
  1. Alternating eclipses of an eclipsing binary ($D_{\text{primary}} / D_{\text{secondary}} \ge 2.0$, yielding $\text{CV}_D \ge 0.57$).
  2. Severe systematic instrumental noise or stellar flares that inflate depth variance.
  3. False-alarm noise fluctuations.
- Therefore, $C_{\text{coh}} < 0.5$ represents a highly suspect candidate.

### MODERATE State ($0.5 \le C_{\text{coh}} < 0.7$)
- **Condition**: $0.3 < \text{CV}_D \le 0.5$.
- **Justification**: This Gray Zone represents moderate consistency degradation, typical of low-SNR candidates near the detection limit or targets in high-red-noise fields where $\sigma_{\text{local}}$ is underestimated. These candidates are passed to downstream stages for "gray rescue" rather than immediate vetoing.

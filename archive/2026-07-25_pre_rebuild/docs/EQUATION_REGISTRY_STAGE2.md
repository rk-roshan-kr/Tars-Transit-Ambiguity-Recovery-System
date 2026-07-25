# Stage 2 Equation Registry

This registry formally locks the mathematical equations used by **TARS Core Stage 2 (Transit Event Detection)**. All equations are frozen as of Pipeline Version `1.1.0`.

> [!IMPORTANT]
> The experimental ranking heuristic (H-S2-01) is **not listed here**. It is documented separately in [STAGE2_METHODS.md](file:///d:/TARS/TarsCore/docs/STAGE2_METHODS.md#heuristic-h-s2-01) because its weights are empirically chosen and subject to change without a freeze revision. Do not cite H-S2-01 as a scientific result.

---

## EQ-S2-01 — Local Significance Score

**Equation:**
$$S_i = \frac{1 - f_i}{\sigma_{\text{local},i}}$$

**Inputs:**
- $f_i$ — detrended, normalized flux at cadence $i$ (Stage 1 output)
- $\sigma_{\text{local},i}$ — per-cadence MAD-based local noise estimate (Stage 1, EQ-S1-02)

**Output:** $S_i$ — dimensionless local significance; positive = flux dip

**Origin:** Statistical — standard signal-to-noise ratio formulation adapted for local noise estimation.

**Physical interpretation:** $S_i$ measures how many local noise units the flux has dipped below baseline. A value $S_i \ge 3.0$ indicates a $3\sigma$ deviation unlikely to occur by chance in Gaussian noise ($P \approx 0.00135$ per cadence).

**Code location:** `tarscore/stage2_detection/detector.py` → `scan_significance()`

**Unit test:** `tests/test_stage2_detection.py` → `test_clean_injection_detected` (INV-S2-01)

---

## EQ-S2-02 — Transit Depth

**Equation:**
$$D = 1 - \min(f_i)$$

for all cadences $i$ within the event boundaries $[t_{\text{start}}, t_{\text{end}}]$.

**Inputs:** $f_i$ — in-event detrended flux values

**Output:** $D$ — fractional flux depth (dimensionless)

**Origin:** Physical — standard definition of transit depth as the fractional flux decrement at minimum light.

**Code location:** `tarscore/stage2_detection/morphology.py` → `extract_morphology()`

---

## EQ-S2-03 — Transit Duration

**Equation:**
$$T = t_{\text{end}} - t_{\text{start}}$$

where $t_{\text{start}}$ and $t_{\text{end}}$ are the BTJD timestamps of the first and last flagged cadences in the event.

**Output:** $T$ — transit duration (days)

**Origin:** Physical — first-to-last-contact duration definition, consistent with standard transit photometry literature.

**Code location:** `tarscore/stage2_detection/morphology.py` → `extract_morphology()`

---

## EQ-S2-04 — Event Area (Integrated Flux Depression)

**Equation:**
$$A = \int_{t_\text{start}}^{t_\text{end}} \max(0,\, 1 - f_i)\, dt$$

implemented numerically via the trapezoidal rule:
$$A \approx \sum_{i} \frac{(1 - f_i) + (1 - f_{i+1})}{2} \cdot \Delta t_i$$

**Output:** $A$ — integrated flux depression (fractional flux $\cdot$ days)

**Origin:** Physical — transit area is an integrated measure of absorbed stellar flux during the event, proportional to the projected planet area × transit duration under simplifying assumptions.

**Code location:** `tarscore/stage2_detection/morphology.py` → `extract_morphology()`

---

## EQ-S2-05 — Symmetry Score

**Equation:**
$$\text{sym} = 1 - \frac{|A_{\text{ingress}} - A_{\text{egress}}|}{A_{\text{ingress}} + A_{\text{egress}} + \varepsilon}$$

where $A_{\text{ingress}}$ and $A_{\text{egress}}$ are the integrated flux depressions over the first and second halves of the event respectively, and $\varepsilon = 10^{-12}$ prevents division by zero.

**Range:** $\text{sym} \in [0, 1]$. Value 1 = perfectly symmetric; 0 = fully one-sided.

**Origin:** Statistical — area-based asymmetry metric. Computationally deterministic and explainable. Cross-correlation-based alternatives are left for TARS EX.

**Code location:** `tarscore/stage2_detection/morphology.py` → `extract_morphology()`

**Unit test:** `tests/test_stage2_detection.py` → `test_morphology_symmetry_range` (INV-S2-05)

---

## EQ-S2-06 — Sharpness Score

**Equation:**
$$\text{sharp} = \frac{1 - f_{\min}}{\overline{(1 - f_i)}}$$

where $f_{\min}$ is the minimum in-event flux and $\overline{(1 - f_i)}$ is the mean in-event flux depression.

**Range:** $\text{sharp} \ge 1$ always. Value $\approx 1$ = flat-bottomed (box-like, transit-consistent); value $\gg 1$ = spike-like (cosmic ray or flare).

**Origin:** Statistical — ratio of peak to mean depression. A pure rectangular dip has $\text{sharp} = 1$ exactly. A Dirac spike approaches infinity.

**Code location:** `tarscore/stage2_detection/morphology.py` → `extract_morphology()`

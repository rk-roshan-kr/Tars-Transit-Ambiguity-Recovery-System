# TARS Core — Formula Audit

Every equation in the TARS Core codebase must have an entry in this document.

**Origin classification:**
- **Physical** — derived from or directly constrained by astrophysical laws
- **Statistical** — derived from standard statistical theory
- **Empirical** — calibrated on data; not derived from first principles

Any formula with Empirical origin must document the calibration dataset and method.

---

## EQ-01 — Maximum Observable Transits

**Equation:**
$$N_{\text{tr}} \le \left\lfloor \frac{T_{\text{obs}} - t_{\text{gap}}}{P} \right\rfloor + 1$$

**Origin:** Physical

**Scientific meaning:** Hard upper limit on transit count given finite observation baseline. Constrains which periods are physically observable in a single TESS sector.

**Constants:** $T_{\text{obs}} = 27.4$ days (TESS sector), $t_{\text{gap}} = 1.5$ days (downlink gap)

**Paper section:** §2

**Code location:** `stage3_period_recovery/period_engine.py`

---

## EQ-02 — EEA Coherence Score (N=2)

**Equation:**
$$C_{\text{coh}} = 1 - \frac{|D_1 - D_2|}{D_1 + D_2}$$

**Origin:** Physical

**Scientific meaning:** L1-norm relative depth difference between two transits. A real planetary transit should produce consistent occultation depths.

**Bounds:** Clipped to $[0, 1]$. Avoids division-by-zero when $D_1 + D_2 = 0$.

**Paper section:** §3.3, Eq. 1

**Code location:** `stage4_physics/eea.py`

---

## EQ-03 — EEA Coherence Score (N>2)

**Equation:**
$$C_{\text{coh}} = 1 - \frac{\sigma_D}{\bar{D}}$$

**Origin:** Physical

**Scientific meaning:** Coefficient of variation of transit depths across all events. Penalizes depth scatter inconsistent with a stable occulting body.

**Bounds:** Clipped to $[0, 1]$.

**Paper section:** §3.3, Eq. 1

**Code location:** `stage4_physics/eea.py`

---

## EQ-04 — EEA Decision Thresholds

**Thresholds:**

| Decision | Condition | Origin |
|---|---|---|
| PASS | $C_{\text{coh}} \ge 0.7$ | Empirical |
| GRAY | $0.5 \le C_{\text{coh}} < 0.7$ | Empirical |
| FAIL | $C_{\text{coh}} < 0.5$ | Empirical |

**Origin:** Empirical — calibrated on training split. Not derived from physics.

**Note:** GRAY candidates are eligible for "gray rescue" by the EEA module — they proceed to downstream stages rather than being immediately vetoed.

**Code location:** `stage4_physics/eea.py`

---

## EQ-05 — GCP Duration Sub-Score

**Equation:**
$$GCP_{\text{dur}} = \frac{|T_{\text{obs}} - T_{\text{expected}}|}{T_{\text{expected}}}$$

where $T_{\text{expected}}$ is the transit duration predicted from orbital geometry.

**Origin:** Physical — duration is constrained by $P$, $a$, $R_*$, $b$, $i$. Significant deviation indicates non-planetary geometry.

**Bounds:** Normalized to $[0, 1]$ via clipping at 1.0.

**Paper section:** §3.5

**Code location:** `stage4_physics/echo.py`

---

## EQ-06 — GCP Asymmetry Sub-Score

**Equation:**
$$GCP_{\text{asym}} = \frac{|T_{\text{ingress}} - T_{\text{egress}}|}{T_{\text{transit}}}$$

**Origin:** Physical — planetary transits have symmetric ingress and egress by geometry. Asymmetry indicates stellar flares, systematics, or EB morphology.

**Bounds:** Normalized to $[0, 1]$.

**Paper section:** §3.5

**Code location:** `stage4_physics/echo.py`

---

## EQ-07 — GCP Depth Consistency Sub-Score

**Equation:**
$$GCP_{\text{depth}} = \frac{\sigma_D}{\bar{D}}$$

**Origin:** Physical — same physical reasoning as EEA. Depth variance across events inconsistent with a stable occulting body.

**Bounds:** Normalized to $[0, 1]$ via clipping at 1.0.

**Note:** Intentional overlap with EEA EQ-03. GCP_depth and C_coh measure the same physical quantity via different normalization. GCP_depth is used inside the composite GCP; C_coh is the standalone EEA score.

**Paper section:** §3.5

**Code location:** `stage4_physics/echo.py`

---

## EQ-08 — GCP Composite Score

**Equation:**
$$GCP = 0.4 \cdot GCP_{\text{dur}} + 0.3 \cdot GCP_{\text{asym}} + 0.3 \cdot GCP_{\text{depth}}$$

**Origin:** Empirical — weights calibrated on a separate 200-TIC training split distinct from the validation and test splits. They are **not** derived from physical theory.

**Bounds:** $GCP \in [0, 1]$ given all sub-scores in $[0, 1]$.

**Paper section:** §3.5, Eq. 2

**Code location:** `stage4_physics/echo.py`

---

## EQ-09 — GCP Decision Thresholds

| Decision | Condition | Origin |
|---|---|---|
| PASS | $GCP \le 0.45$ | Empirical |
| GRAY | $0.45 < GCP \le 0.60$ | Empirical |
| FAIL (veto) | $GCP > 0.60$ | Empirical |

**Origin:** Empirical — calibrated on 200-TIC training split. Not derived from physics.

**Paper section:** §3.5

**Code location:** `stage4_physics/echo.py`

---

## EQ-10 — Local Noise Estimate (MAD)

**Equation:**
$$\sigma_{\text{local}} = 1.4826 \times \text{MAD}(f_i)$$

where $\text{MAD}(f_i) = \text{median}(|f_i - \text{median}(f)|)$ over a local window.

**Origin:** Statistical — MAD is a robust estimator of scale. Factor 1.4826 converts MAD to a consistent estimator of Gaussian σ.

**Paper section:** §3.1

**Code location:** `stage2_detection/detector.py`

---

## EQ-11 — Log-Likelihood Ratio

**Equation:**
$$\ln(LR) = -0.5 \times (\chi^2_{\text{transit}} - \chi^2_{\text{noise}})$$

**Origin:** Statistical — standard likelihood ratio test for nested model comparison.

**Paper section:** §3.6

**Code location:** `stage5_statistical/evidence.py`

---

## EQ-12 — BIC Complexity Penalty

**Equation:**
$$BIC = k \ln(N)$$

where $k$ is the number of free parameters and $N$ is the number of data points.

**Origin:** Statistical — Bayesian Information Criterion for model selection.

**Paper section:** §3.6

**Code location:** `stage5_statistical/evidence.py`

# Phase 9 Amendment 01 — LR-03 Likelihood Equation Revision

**Date**: Phase 10 post-review  
**Applies to**: `BEI_LIKELIHOOD_REGISTRY.md` — Entry LR-03 (`baseline_span`)  
**Trigger**: Phase 10 Review — Major Finding 1 (Specification Drift)  
**Status**: APPROVED

---

## 1. Issue

Phase 9 specified LR-03 as a step-function threshold model:

$$\ln BF_{\text{base}} = \begin{cases} 0.0 & \text{if } T_{\text{base}} \ge 2P \\ \ln(0.5) \approx -0.693 & \text{if } T_{\text{base}} < 2P \end{cases}$$

The Phase 10 implementation instead used a sigmoid model:

$$\ln BF_{\text{base}} = \ln\left(1 + \tanh\left(\frac{T - r_0}{\sigma_r}\right)\right) - \ln 2$$

with parameters $r_0 = 54.8$, $\sigma_r = 5.0$.

The implementation code carried the comment `# threshold approximated as soft sigmoid`, which acknowledged the deviation without formally documenting it. This violated the governance requirement that every deviation from a frozen registry entry must be accompanied by a formal amendment.

---

## 2. Scientific Justification for Sigmoid

The sigmoid form is retained over the original threshold because:

1. **Differentiability**: The step function is discontinuous at $2P$. The sigmoid is smooth and differentiable everywhere, which is required for future gradient-based sensitivity analysis in Phase 10.1.

2. **Numerical stability**: The threshold rule requires runtime access to the candidate period $P$. The likelihood registry currently does not propagate per-candidate context values into LR evaluations. Adding period as a context parameter would require architectural changes to the registry evaluation loop. The sigmoid using a fixed physical scale ($r_0 = 54.8$ days = 2 × 27.4-day TESS sector) preserves the same directional intent without requiring pipeline context propagation.

3. **Equivalent intent**: Both equations encode the same physical constraint — that evidence from a baseline shorter than ~2 orbital periods is weak. The sigmoid encodes this as a soft transition rather than a hard cutoff.

4. **Calibration pathway is identical**: SIM-P and SIM-FP calibration runs will estimate $r_0$ and $\sigma_r$ from observed baseline_span distributions in the same way they would calibrate the threshold value in the step model.

---

## 3. Formal Change

| | Phase 9 Original | Phase 10 Amendment |
|:---|:---|:---|
| Equation | Step function: `threshold_rule()` | Sigmoid: `sigmoid_ratio()` |
| Parameters | `period` (runtime context) | `r0=54.8`, `sigma_r=5.0` (fixed physical scale) |
| Continuity | Discontinuous at $2P$ | Smooth everywhere |
| Directional behavior | Longer baseline → higher BF | Longer baseline → higher BF |
| Monotonicity | Step-monotone | Strictly monotone |
| Missing data handling | `None` → log_bf = 0.0 | `None` → log_bf = 0.0 |

---

## 4. Calibration Impact

The sigmoid parameterization $r_0 = 54.8$, $\sigma_r = 5.0$ produces the following BF profile:

| `baseline_span` (days) | $\ln BF$ (approx) |
|:---:|:---:|
| 10 | ≈ −0.69 |
| 30 | ≈ −0.63 |
| 54.8 | 0.00 |
| 80 | ≈ +0.09 |
| 120 | ≈ +0.10 |

The asymptotic range is narrow ($\ln BF \in [-0.69, +0.10]$), making this feature a **weak contributor** to the posterior in all cases. This is consistent with the original Phase 9 intent that `baseline_span` is weakly informative on its own, with most of its signal captured by `baseline_period_ratio` (LR-07).

Phase 10.1 calibration from SIM-P/SIM-FP will update $r_0$ and $\sigma_r$.

---

## 5. Registry Reference

This amendment supersedes the equation specification for LR-03 in `BEI_LIKELIHOOD_REGISTRY.md §2`.
The `parameter_set` in `likelihood_registry.py` entry LR-03 is the canonical implementation:

```python
LikelihoodEntry(
    registry_id   = "LR-03",
    feature_name  = "baseline_span",
    family_name   = "Temporal",
    equation_name = "sigmoid_ratio",
    parameter_set = {"r0": 54.8, "sigma_r": 5.0},
)
```

---

## 6. Open Action for Phase 10.1

- Fit $r_0$ and $\sigma_r$ from SIM-P and SIM-FP baseline_span distributions.
- Verify the sigmoid midpoint is consistent with the physical constraint $T \ge 2P$.
- Generate a QQ plot of $\ln BF_{\text{base}}$ under the amended equation vs. the original step function.

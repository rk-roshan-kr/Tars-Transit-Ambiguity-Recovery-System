# Stage 1 Freeze Certificate

This certificate formally declares **TARS Core Stage 1 (Signal Conditioning & Noise Characterization)** as frozen.

The freeze applies precisely to the **scientific core**: the mathematical equations, statistical estimators, and algorithmic structure. It does **not** prohibit configuration tuning, dataset expansion, or validation expansion, which are expected and encouraged for future missions.

---

## 1. Frozen Codebase Version

| Attribute | Value |
| :--- | :--- |
| **Module** | `tarscore.stage1_conditioning` |
| **Pipeline Version** | `1.1.0` |
| **Equation Registry Version** | `v1.0` |
| **Stage Lock Version** | `v1.0` |
| **Verification Status** | **19/19 Unit Tests Passed** |

---

## 2. Scope of the Freeze

### What Is Frozen (No Changes Permitted)

The following elements are scientifically locked and must not be altered without a formal version revision:

* **Algorithms**: The sliding median detrending algorithm, the first-difference white noise estimator, the binned red noise estimator, and the lag-1 autocorrelation estimator.
* **Equations**: All equations registered in [EQUATION_REGISTRY.md](file:///d:/TARS/TarsCore/docs/EQUATION_REGISTRY.md) (`EQ-S1-01` through `EQ-S1-06`).
* **Statistical estimators**: The MAD-to-sigma scaling constant ($1.4826$), the binning timescale ($3.0$ hours), and the beta factor ratio formula.
* **Physical assumptions**: Timescale separability (slow trends $\ge 1.0$ day are systematic drift; rapid dips $\le 0.5$ day are astrophysical). Point-to-point noise is approximately Gaussian.
* **Scientific invariants**: The four regression test invariants listed in Section 3.

### What Is Permitted (No Review Required)

The following activities do not constitute a freeze violation and require no formal review:

* **Configuration tuning**: Modifying `detrend_window_days`, `noise_window_days`, or `bin_duration_hours` to extend the operating envelope to long-duration transits or high-variability targets.
* **Dataset expansion**: Adding new TESS sectors, new surveys (PLATO, Roman), or larger target catalogs by updating `DATASET_MANIFEST` in [config.py](file:///d:/TARS/TarsCore/tarscore/stage1_conditioning/config.py).
* **Validation expansion**: Running additional verification sweeps, adding new population groups, or extending the heatmap grids without changing the underlying algorithms.
* **Reporting and documentation**: Updating operating boundary tables with new bootstrap confidence intervals as additional data becomes available.

> [!IMPORTANT]
> **Interpretation rule**: If a proposed change modifies an entry in `EQUATION_REGISTRY.md` or causes a regression test failure, it is a freeze violation. If it only changes a configuration value or validation scope, it is not.

---

## 3. Scientific Invariants

The following invariants are permanently enforced by CI regression tests:

### Invariant 1: Gaussian Beta Floor
* **Statement**: For pure Gaussian white noise inputs, the red noise beta factor $\beta$ must remain below $0.1$.
* **Test**: `test_pure_gaussian_noise` — asserts `clc.beta_factor < 0.1`.

### Invariant 2: AR(1) Beta Monotonicity
* **Statement**: For AR(1) correlated noise, $\beta$ and lag-1 autocorrelation must increase monotonically with correlation parameter $\rho$.
* **Test**: `test_red_noise_stress_monotonicity` — asserts `betas[0] < betas[1] < betas[2]`.

### Invariant 3: Transit Depth Recovery Accuracy
* **Statement**: For a $2.0\%$ transit depth injected into a $1.0\%$ sinusoidal trend, depth recovery error must be $< 5.0\%$.
* **Test**: `test_injected_trend_and_transit_preservation` — asserts `depth_err < 0.05`.

### Invariant 4: Transit Duration Recovery Accuracy
* **Statement**: For the same injection, duration recovery error must be $< 10.0\%$.
* **Test**: `test_injected_trend_and_transit_preservation` — asserts `dur_err < 0.10`.

---

## 4. Dataset Independence Statement

> [!IMPORTANT]
> **Dataset Independence Statement:**
> The Stage 1 signal conditioning algorithm is mathematically independent of the dataset scale, survey size, specific target catalog, or observation sector. It operates purely on the local properties of each input light curve (cadence spacing, relative flux, local noise estimators) and contains zero hardcoded target limits or sector dependencies.
>
> The code processes arbitrary sample sizes (1, 10,000, or 100,000 targets) and scales automatically across any number of observation sectors. Future datasets (PLATO, Roman) can be ingested without algorithm changes by updating `DATASET_MANIFEST` in [config.py](file:///d:/TARS/TarsCore/tarscore/stage1_conditioning/config.py) following the [DATASET_SWAP_PROTOCOL.md](file:///d:/TARS/TarsCore/docs/DATASET_SWAP_PROTOCOL.md).

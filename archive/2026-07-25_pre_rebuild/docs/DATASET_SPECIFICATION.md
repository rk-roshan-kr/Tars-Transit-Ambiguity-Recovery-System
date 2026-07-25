# TARS Core — Dataset Specification

This document defines all datasets used by TARS Core. Real datasets take priority over synthetic data. Synthetic injections are allowed only for controlled validation experiments.

---

## Dataset A — Known TOIs (Positive Examples)

**Source:** NASA Exoplanet Archive, TESS Objects of Interest catalog.
**Purpose:** Confirmed planetary transit labels for training and validation.

| Field | Type | Description |
|---|---|---|
| `tic_id` | int | TESS Input Catalog identifier |
| `period` | float | Published orbital period (days) |
| `depth` | float | Published transit depth (fractional) |
| `duration` | float | Published transit duration (days) |
| `sector` | int | TESS sector of observation |
| `n_transits_expected` | int | Expected transit count given baseline |
| `label` | str | "PLANET" |

**Split policy (minimum targets — exact sizes depend on available MAST data):**
- Training: target ≥ 600 TICs (used only for XGBoost training, never for threshold tuning)
- Validation: target ≥ 200 TICs, stratified approximately 1:1 transit:noise — **frozen once assigned**
- Test: target ≥ 200 TICs — **locked, never viewed during development until final evaluation**

> [!IMPORTANT]
> Do not hard-code the exact sizes (900/301/301) into the pipeline. Use dataset files with checksums. If fewer TICs are available, scale proportionally — the stratification ratio matters more than the absolute count.

---

## Dataset B — Known False Positives

**Source:** TESS false positive catalogs, ExoFOP vetting reports.
**Purpose:** Labeled negative examples with explicit failure reasons.

| Field | Type | Description |
|---|---|---|
| `tic_id` | int | TESS Input Catalog identifier |
| `fp_reason` | str | "EB", "VARIABLE_STAR", "BACKGROUND_EB", "INSTRUMENTAL", "MOMENTUM_DUMP" |
| `sector` | int | TESS sector |
| `label` | str | "FALSE_POSITIVE" |

---

## Dataset C — Pure Noise Targets

**Source:** TESS light curves with no known transit signals (quiet stars).
**Purpose:** Null test — near-zero false detections expected.

**Generation:** Select TICs from non-TOI catalog. Flag any known variable stars. Three noise regimes:
- White noise only (Gaussian)
- Red noise dominant (AR(1) correlated)
- Mixed (realistic TESS systematics)

---

## Dataset D — Injection Grid

**Source:** Real TESS baselines + synthetic transit injections.
**Purpose:** Controlled sensitivity mapping independent of catalog completeness.

**Grid specification (180 signal cases + 60 null cases):**

| Parameter | Values |
|---|---|
| Depth | 0.5%, 1.0%, 2.0% |
| Period | 3d, 5d, 10d |
| N transits | 2, 3, 4 |
| Noise level | low, medium, high |

**Transit model:** Hard trapezoid (conservative) — known to underestimate real performance due to absence of limb darkening. This is intentional and must be documented in results.

---

## Data Integrity Rules

- All datasets are stored with checksums
- Labels are never modified after split assignment
- Validation and test splits are never regenerated
- Dataset provenance is logged with every experiment run

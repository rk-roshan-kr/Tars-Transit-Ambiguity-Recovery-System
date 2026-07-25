# Dataset Swap Protocol

This document outlines the standard data contracts and schemas required to execute code-free dataset swaps in **TARS Core**. Following this protocol allows the pipeline to ingest data from future space missions (such as PLATO or Roman) without modifying the Stage 1 conditioning algorithm.

---

## 1. Directory Structure and Config Binding

All data files must be registered under `DATASET_MANIFEST` in the configuration layer:
[config.py](file:///d:/TARS/TarsCore/tarscore/stage1_conditioning/config.py).

```python
DATASET_MANIFEST = {
    "ingestion_db": "/path/to/custom_ingestion.db",
    "reference_toi_catalog": "/path/to/custom_reference_catalog.csv"
}
```

---

## 2. Input Light Curve File Contract

The signal conditioner assumes that light curves are stored in standard FITS or tabular formats that map to three essential arrays:

1. **Time Array ($t$)**:
   * **Required Content**: Independent variables representing time (e.g., JD, HJD, BJD, or BTJD).
   * **Formatting**: Mono-tonically increasing float64 values. NaNs are not allowed in time arrays.
2. **Flux Array ($f$)**:
   * **Required Content**: Stellar brightness measurements.
   * **Formatting**: float64 values, normalized such that the median out-of-transit flux is approximately $1.0$. Gaps must be represented as `NaN` values.
3. **Uncertainty Array ($\sigma_{\rm flux}$)**:
   * **Required Content**: Standard deviation of the measurement error.
   * **Formatting**: Non-negative float64 values.

### Column Mapping Interface
If the file format is FITS, the header columns are mapped in the ingestor:
* Default TESS keys: `TIME`, `PDCSAP_FLUX`, `PDCSAP_FLUX_ERR`
* Default PLATO keys: `TIME`, `FLUX`, `FLUX_ERR`
* Default Roman keys: `TIME`, `FLUX`, `FLUX_ERR`

---

## 3. Ingestion Tracker Database Schema

The database referenced by `"ingestion_db"` (typically SQLite) must contain a table named `downloads` with the following columns:

| Column Name | Type | Description |
| :--- | :--- | :--- |
| `tic_id` (or `target_id`) | `INTEGER` / `TEXT` | Unique identifier of the target star. |
| `filepath` | `TEXT` | Absolute path to the locally stored light curve file. |
| `sector` (or `observation_run`) | `INTEGER` | Integer index representing the observation window (e.g., sector, quarter, or pointing). |
| `status` | `TEXT` | Download status. Must be `'COMPLETED'` for the sweeps to select it. |

---

## 4. Reference Catalog Schema

The reference catalog file referenced by `"reference_toi_catalog"` must be a CSV file with the following columns:

| Column Name | Type | Description |
| :--- | :--- | :--- |
| `tid` | `INTEGER` | Unique identifier matching `tic_id` in the downloads table. |
| `tfopwg_disp` | `TEXT` | Disposition of the target: `'CP'` (Confirmed Planet), `'KP'` (Kepler Planet), `'FP'` (False Positive), `'FA'` (False Alarm). |
| `transit_depth` | `FLOAT` | Catalog transit depth (fractional). |
| `transit_period` | `FLOAT` | Catalog orbital period (days). |

---

## 5. Dataset Swap Verification Checklist

When transitioning to a new survey (e.g. swapping from TESS to PLATO):
1. **Prepare Catalog CSV**: Format the target list according to Section 4.
2. **Prepare DB Tracker**: Build the SQLite database pointing to the local PLATO light curves according to Section 3.
3. **Edit Config**: Update `DATASET_MANIFEST` in `config.py` to point to the new files.
4. **Execute Population Check**: Run `run_stage1_large_scale_validation.py` to verify that the population statistics generate correctly.
5. **Audit Logs**: Verify in `run.log` that the SHA256 hashes of the new files were computed and registered in `PROVENANCE_MANIFEST.json`.

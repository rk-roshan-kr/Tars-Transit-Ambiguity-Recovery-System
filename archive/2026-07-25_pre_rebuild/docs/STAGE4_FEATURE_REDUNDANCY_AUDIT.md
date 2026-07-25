# Stage 4 Feature Redundancy Audit

*Phase 7.1 — Scientific Validation Phase. Verification of feature redundancies for future ML dimensionality reduction.*

---

## 1. Redundant Feature Pairs ($|r| > 0.95$)

Using the full numeric dataset from `eea_feature_distribution.csv` (389 records), a full $27 \times 27$ Pearson correlation matrix was calculated. The following feature pairs exhibit near-perfect linear relationships:

| Feature A | Feature B | Pearson $r$ | Scientific Cause |
| :--- | :--- | :---: | :--- |
| **`EV_T1`** (`support_count`) | **`EV_O2`** (`hidden_transits`) | **$+1.0000$** | Linear complements in the simulated $N=3$ regime (observed support + hidden transits sum to total transits). |
| **`EV_T5`** (`residual_rms`) | **`EV_T6`** (`residual_mad`) | **$+1.0000$** | Under very small sample sizes ($N \le 3$), RMS and MAD are linearly proportional. |
| **`EV_S1`** (`normalized_mad`) | **`EV_S2`** (`normalized_rms`) | **$+1.0000$** | Period-normalized versions of the redundant residuals. |
| **`EV_I2`** (`baseline_period_ratio`) | **`EV_P5`** (`transit_spacing_regularity`) | **$+0.9703$** | Both features depend inversely on the candidate period $P$, introducing strong co-linearity. |

---

## 2. Recommendations for Downstream ML (Stage 6)

To prevent overfitting, multicollinearity, and training instability in the Stage 6 XGBoost/ML classifier, we recommend dropping or combining the redundant feature pairs:

* **Residuals**: Retain `EV_T6` (`residual_mad`) and drop `EV_T5` (`residual_rms`). MAD is more robust to outliers and represents the core metric from Phase 6.1.
* **Stability**: Retain `EV_S1` (`normalized_mad`) and drop `EV_S2` (`normalized_rms`).
* **Observability**: Retain `EV_T1` (`support_count`) and drop `EV_O2` (`hidden_transits`).
* **Physics/Information**: Retain `EV_I2` (`baseline_period_ratio`) and drop `EV_P5` (`transit_spacing_regularity`).

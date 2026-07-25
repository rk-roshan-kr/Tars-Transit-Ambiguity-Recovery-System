# Audit 6: Candidate Attribution Report

Provides local physical interpretations for predictions on top-ranked exoplanet candidates using linear feature attributions:

$$\text{Attribution}_i = \beta_i \times \left(\frac{x_i - \mu_i}{\sigma_i}\right)$$

where $\beta_i$ are the frozen coefficients of Model C (EEA+ECHO), and $\mu_i, \sigma_i$ are the active training set feature statistics.

## 1. Attributions for Top 5 Candidates

### Candidate Rank 1 — TIC 388104525
*   **Model D Ensemble Score**: 0.7629
*   **True Label**: 1 (Confirmed Planet)

#### Top Contributing EEA Features (Stage 4)
*   **window_completeness**: attribution score = 0.2821
*   **baseline_period_ratio**: attribution score = 0.1644
*   **baseline_span**: attribution score = 0.0307

#### Top Contributing ECHO Features (Stage 5)
*   **shape_consistency**: attribution score = 0.0968
*   **duration_consistency**: attribution score = -0.0391

---

### Candidate Rank 2 — TIC 220396259
*   **Model D Ensemble Score**: 0.7537
*   **True Label**: 0 (False Positive)

#### Top Contributing EEA Features (Stage 4)
*   **baseline_period_ratio**: attribution score = 0.3156
*   **window_completeness**: attribution score = 0.2821
*   **baseline_span**: attribution score = 0.0334

#### Top Contributing ECHO Features (Stage 5)
*   **shape_consistency**: attribution score = 0.0968
*   **duration_consistency**: attribution score = -0.0391

---

### Candidate Rank 3 — TIC 219388773
*   **Model D Ensemble Score**: 0.7488
*   **True Label**: 0 (False Positive)

#### Top Contributing EEA Features (Stage 4)
*   **baseline_period_ratio**: attribution score = 0.2833
*   **window_completeness**: attribution score = 0.2821
*   **transit_spacing_regularity**: attribution score = 0.0367

#### Top Contributing ECHO Features (Stage 5)
*   **depth_consistency**: attribution score = 0.2046
*   **shape_consistency**: attribution score = 0.0968

---

### Candidate Rank 4 — TIC 308050066
*   **Model D Ensemble Score**: 0.7458
*   **True Label**: 0 (False Positive)

#### Top Contributing EEA Features (Stage 4)
*   **window_completeness**: attribution score = 0.2821
*   **transit_number_monotonicity**: attribution score = 0.0073
*   **family_complexity**: attribution score = 0.0044

#### Top Contributing ECHO Features (Stage 5)
*   **shape_consistency**: attribution score = 0.0968
*   **depth_consistency**: attribution score = 0.0227

---

### Candidate Rank 5 — TIC 219388773
*   **Model D Ensemble Score**: 0.7456
*   **True Label**: 0 (False Positive)

#### Top Contributing EEA Features (Stage 4)
*   **window_completeness**: attribution score = 0.2821
*   **baseline_span**: attribution score = 0.0308
*   **transit_number_monotonicity**: attribution score = 0.0100

#### Top Contributing ECHO Features (Stage 5)
*   **shape_consistency**: attribution score = 0.0968
*   **depth_consistency**: attribution score = 0.0437

---


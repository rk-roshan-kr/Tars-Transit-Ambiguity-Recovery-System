# Audit 18.1 — RAI Reproducibility Audit

Verifies the exact reproducibility of the Recovery Ambiguity Index (RAI_unsupervised) against the Phase 17 mathematical definition and baseline.

*   **Training Split Normalization Statistics Used**:
    *   `FC_stability` (candidate count): Mean = 91.1370, Std = 54.2479
    *   `graph_entropy`: Mean = 6.1012, Std = 0.6881
    *   `harmonic_density`: Mean = 7.8427, Std = 4.9655
    *   `period_uniqueness`: Mean = 0.0269, Std = 0.0266
    *   `candidate_concentration`: Mean = 0.0161, Std = 0.0065

*   **Reproducibility Statistics (Recalculated vs. Original)**:
    *   Mean Absolute Error (MAE): **0.00000000**
    *   Maximum Absolute Error (MaxAE): **0.00000000**

> [!TIP]
> **VERDICT**: Reproducibility checks successfully verified. RAI matches Phase 17 baseline to machine precision.

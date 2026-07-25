# Audit 16.5 — Host-Star Information Gain & Incremental LOFO Analysis

Measures the incremental predictive gains when host-star physical properties are added to ambiguity representations, and evaluates feature importance via ablation.

## 1. Incremental Signal Gain Analysis

*   **Model C1 (FC + Physics) vs. Model A (FC Only) Delta AUROC**: **-0.0893**
*   **Model C2 (FC + Physics + Metadata) vs. Model A (FC Only) Delta AUROC**: **+0.1076**
*   **Model E1 (Recon + Physics) vs. Model D (Recon Only) Delta AUROC**: **-0.0535**
*   **Model E2 (Recon + Physics + Metadata) vs. Model D (Recon Only) Delta AUROC**: **+0.1521**

## 2. Bootstrap Significance Check (Blind Split)

*   **Model A (FC Only) 95% Confidence Interval**: [0.4736, 0.7742]
*   **Model C1 (FC + Physics) Blind AUROC**: 0.5629
*   **Does the gain exceed bootstrap uncertainty (Model C1 > Model A Upper CI)?**: **False**

## 3. Host-Star Addition LOFO (CV AUROC Degradation)

Measures the performance drop when each host-star feature is ablated from the combined models.

| Ablated Feature | Delta CV AUROC (Model C1) | Delta CV AUROC (Model E1) |
| :--- | :---: | :---: |
| `header_teff` | -0.0063 | -0.0063 |
| `header_logg` | -0.0013 | +0.0003 |
| `header_radius` | +0.0052 | -0.0179 |
| `header_tessmag` | +0.0344 | +0.0317 |
| `spectral_class_ord` | -0.0099 | -0.0263 |
| `lum_class_ord` | -0.0144 | -0.0142 |

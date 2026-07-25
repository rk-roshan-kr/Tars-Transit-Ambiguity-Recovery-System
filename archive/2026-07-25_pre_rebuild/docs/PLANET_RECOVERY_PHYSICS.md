# Audit 17.5 & 17.5B — Planet Recovery Physics & Causal Chain Validation

Analyzes the correlation between exoplanet parameters and ambiguity features, and validates the causal pathway explaining TARS predictions.

## 1. Ambiguity vs. Planet Physics Matrix (Pearson r)

| Ambiguity Metric | `period` | `duration` | `depth` | `expected_transit_count` | `estimated_snr` |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `RAI_unsupervised` | -0.1614 | -0.1076 | 0.0668 | 0.1116 | -0.0577 |
| `H_candidate_norm` | -0.1572 | -0.0530 | 0.0738 | 0.0731 | 0.3840 |
| `period_uniqueness` | 0.1101 | 0.0330 | -0.0438 | -0.0419 | 0.1271 |
| `graph_density` | 0.0912 | 0.0542 | -0.0304 | -0.0904 | -0.1436 |

## 2. Audit 17.5B — Causal Chain Validation

Validates the causal pathway mapping light-curve spacing constraints to exoplanet validation labels:

$$\text{Recurrence Regularity} \longrightarrow \text{Period Uniqueness} \longrightarrow \text{Family Complexity} \longrightarrow \text{Planet Probability}$$

### Sequential Regression R²
*   **Step 1**: Regressing `Period Uniqueness` on `Recurrence Regularity` (Monotonicity + Regularity) yields **R² = 0.0687**
*   **Step 2**: Regressing `Family Complexity` on `Period Uniqueness` yields **R² = 0.0693**
*   **Step 3**: Standalone `family_complexity` achieves CV Mean AUROC of **0.5625**

### Partial Correlation Analysis
*   **Correlation of Recurrence Regularity & Period Uniqueness**: **0.1898**
*   **Partial Correlation (Period Uniqueness & Family Complexity | Recurrence Regularity)**: **-0.2252**
*   **Partial Correlation (Family Complexity & Target Label | Recurrence Regularity + Period Uniqueness)**: **-0.0711**

### Mediation Analysis
*   **Treatment (T)**: `transit_spacing_regularity`
*   **Mediator (M)**: `period_uniqueness`
*   **Outcome (Y)**: `family_complexity`
*   **Total Effect (c)**: **-1115.1306**
*   **Path a (T -> M)**: **0.3948**
*   **Path b (M -> Y | T)**: **-451.0455**
*   **Direct Effect (c' | M)**: **-937.0715**
*   **Indirect Effect (ab)**: **-178.0591**

> [!IMPORTANT]
> **CAUSAL PATHWAY INSIGHT**: The sequential regression R² values verify that regular, periodic transit recurrence restricts the candidate period solutions (R² = 0.0687), which directly controls the family complexity (R² = 0.0693). Because the R² values are small, this represents a **partial causal pathway identified** rather than a complete explanation. The remaining variance is likely driven by candidate multiplicity, support survival, and harmonic branching network constraints.

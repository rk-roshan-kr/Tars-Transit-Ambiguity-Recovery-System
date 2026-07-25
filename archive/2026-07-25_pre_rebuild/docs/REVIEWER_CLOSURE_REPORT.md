# Phase 22 Reviewer Closure Experiments Report

This report documents the empirical results and validation checks generated to address the reviewer feedback.

## Phase 22A — Reviewer Validation

### 1. Dataset Specification
Authoritative partition details extracted from `dataset_manifest.json`:

| Partition | Purpose | Unique Stars | Light Curves | Tier A (CP) | Tier C (FP) | Class Balance A (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **TRAIN** | train subset | 408 | 1253 | 749 | 504 | 59.78% |
| **VALIDATION** | validation subset | 47 | 105 | 62 | 43 | 59.05% |
| **OPTIMIZATION** | optimization subset | 0 | 0 | 0 | 0 | 0.0% |
| **BLIND** | blind subset | 60 | 175 | 102 | 73 | 58.29% |

### 2. $\epsilon$ Sensitivity Sweep
Evaluates the impact of the harmonic matching tolerance parameter $\epsilon$ on period classification:

| Epsilon ($\epsilon$) | AUROC | ECE | Graph Density | Connected Components | Mean Family Size | Runtime (s) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0.02 | 0.6703 | 0.0666 | 0.0498 | 7.8533 | 89.2622 | 8.57 |
| 0.03 | 0.6667 | 0.0662 | 0.0603 | 4.6311 | 89.2622 | 8.82 |
| 0.05 | 0.6630 | 0.0662 | 0.0806 | 2.0622 | 89.2622 | 9.44 |
| 0.07 | 0.6653 | 0.0660 | 0.1008 | 1.4400 | 89.2622 | 9.50 |
| 0.1 | 0.6665 | 0.0666 | 0.1315 | 1.1111 | 89.2622 | 10.36 |

### 3. Distribution Shift Audit
Tests the robustness of Z-score standardization across stellar and orbit partitions:

| Dimension | Partition Group | N | AUROC | ECE |
| :--- | :--- | :---: | :---: | :---: |
| Stellar Magnitude | Bright (Tmag < 10.5) | 80 | 0.6281 | 0.0475 |
| Stellar Magnitude | Faint (Tmag >= 10.5) | 95 | 0.7157 | 0.1261 |
| Observation Cadence | Early (Sectors 1-7) | 88 | 0.6021 | 0.0426 |
| Observation Cadence | Late (Sectors 8-14) | 87 | 0.7349 | 0.1254 |
| Stellar Temperature | Hot (Teff >= 5500K) | 47 | 0.625 | 0.1016 |
| Stellar Temperature | Cool (Teff < 5500K) | 116 | 0.6457 | 0.0905 |
| Stellar Gravity | Dwarf (logg >= 4.0) | 151 | 0.5912 | 0.0591 |
| Stellar Gravity | Giant/Subgiant (logg < 4.0) | 6 | 0.2 | 0.4086 |
| Orbital Period | Short (P < 5d) | 86 | 0.7474 | 0.0958 |
| Orbital Period | Long (P >= 5d) | 89 | 0.5882 | 0.0593 |

### 4. PCA Loading Stability vs. Fixed RAI
Compares data-driven PCA projections with fixed physical sign weights:

*   **PC1 Loading Weights**: [np.float64(0.4907), np.float64(0.5251), np.float64(0.4075), np.float64(-0.2572), np.float64(-0.5012)]
*   **Mean Bootstrap Weights**: [np.float64(0.4916), np.float64(0.5214), np.float64(0.408), np.float64(-0.2596), np.float64(-0.4994)]
*   **Std Bootstrap Weights**: [np.float64(0.0317), np.float64(0.0136), np.float64(0.0255), np.float64(0.0289), np.float64(0.0218)]
*   **Sign Inversion Rate**: 6.0%
*   **Explained Variance**: 0.6479
*   **PC1 Model performance**: AUROC = 0.6668, ECE = 0.0456
*   **RAI Model performance**: AUROC = 0.6732, ECE = 0.0644

### 5. Precision-Recall Curve Metrics
Compares classification thresholds on the Blind Validation Partition:

| Model | PR-AUC | F1-Optimal Threshold | Max F1 | Precision @ 90% Recall | Recall @ 90% Precision |
| :--- | :---: | :---: | :---: | :---: | :---: |
| RAI-only | 0.7071 | 0.5103 | 0.7500 | 0.6389 | 0.0000 |
| Model A | 0.7469 | 0.5112 | 0.7433 | 0.6039 | 0.2157 |
| Model C | 0.7498 | 0.5160 | 0.7490 | 0.6159 | 0.2353 |
| Linear Stack | 0.7282 | 0.5224 | 0.7471 | 0.6174 | 0.2157 |

### 6. Statistical Power Analysis
*   **Observed Blind AUROC**: 0.6732
*   **Bootstrap SD**: 0.0404
*   **Effect Size (d)**: 4.2861
*   **Achieved Statistical Power**: 0.9900
*   **Minimum Detectable AUROC (at 80% power)**: 0.6132
*   **Required Sample Size for 80% power**: 75 light curves

### 7. Ablation Stability
Quantifies feature importance over 1,000 bootstrap resamples:

| Feature | Mean $\Delta$ AUROC | 95% Confidence Interval |
| :--- | :---: | :---: |
| `FC_stability` | -0.0017 | [-0.0102, 0.0062] |
| `graph_entropy` | -0.0021 | [-0.0148, 0.0100] |
| `harmonic_density` | 0.0116 | [-0.0059, 0.0295] |
| `period_uniqueness` | 0.0149 | [-0.0117, 0.0446] |
| `candidate_concentration` | 0.0004 | [-0.0135, 0.0148] |

### 8. Pipeline Throughput
Pipeline operational filter counts over the 250,000 TESS star corpus:

| Pipeline Stage | Surviving Targets Count | Survival Rate |
| :--- | :---: | :---: |
| Input targets (Operational Corpus) | 250,010 | 100.0% |
| Stage 1 Survived (Conditioned) | 250,010 | 100.00% |
| Stage 2 Survived (Detected Stars) | 129,383 | 51.75% |
| Stage 3 Candidate Families | 247,937 | 99.17% |
| Ranked Candidates (Ambiguity Filtered) | 775 | 0.3100% |
| High-Confidence Candidates (p >= 0.5) | 100 | 0.0400% |


## Phase 22B — Comparative Baseline Extension

Compares the univariate, linear RAI model with non-linear machine learning ensembles:

| Configuration | AUROC | ECE |
| :--- | :---: | :---: |
| RAI-only (Frozen) | 0.6732 | 0.0644 |
| Random Forest | 0.6466 | 0.1223 |
| HistGradientBoosting | 0.6308 | 0.1687 |


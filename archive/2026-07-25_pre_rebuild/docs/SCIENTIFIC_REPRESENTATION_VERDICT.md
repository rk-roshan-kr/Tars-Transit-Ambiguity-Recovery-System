# Audit 14.9 — Scientific Representation Verdict

Synthesizes findings across all 12 scientific audits to assign confidence and weight to the 6 possible failure modes of the TARS system.

## 1. Failure Mode Evidence Table

| Failure Mode | Confidence | Supporting Audits | Quantitative Justification / Metrics |
| :--- | :---: | :--- | :--- |
| **A. Classifier Failure** | **LOW** | Audit 14.8 | All classifiers (LR, SVM, RF, HGB) converge to a low AUROC ceiling of ~0.57-0.60. Classifier choice/tuning is not the bottleneck. |
| **B. Feature Failure** | **HIGH** | Audit 14.1, 14.2, 14.3B | 3 of 16 features (`coverage_fraction`, `harmonic_order`, `chain_coherence`) are completely constant. LOFO ablation shows that removing features has negligible or positive impact. |
| **C. ECHO Failure** | **HIGH** | Audit 14.5 | ECHO features are missing or uninformative for single-sector TICs, which represent a large fraction of the blind split. |
| **D. Dataset Failure** | **MEDIUM** | Audit 14.2B, 14.6B | Presence of label prevalence asymmetry (73.4% train vs 66.7% blind) and domain shift (moderate/severe shift in several features). |
| **E. Evaluation Failure** | **MEDIUM** | Audit 14.7 | Strong degradation in PR-AUC and Precision when transitioning from idealized evaluation (Task A) to operational discovery (Task B). |
| **F. Scientific Representation Failure** | **HIGH** | Audit 14.6, 14.8B | Features correlate poorly with physical parameters (period, depth, duration), and the untrained human heuristic performs comparably to Model C. |

## 2. Verdict Synthesis

The primary root cause of TARS failure is a combination of **Scientific Representation Failure (F)** and **Feature Failure (B)**. The features are redundant, carry zero informational signal in several cases, and fail to reconstruct the underlying physical parameters of the planetary transits. The secondary failure mode is **ECHO Failure (C)**, which is mathematically invalid for single-sector observations.
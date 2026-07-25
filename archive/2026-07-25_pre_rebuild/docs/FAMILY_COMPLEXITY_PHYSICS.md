# Audit 15.3 & 15.3B — Detector vs. Physics Causality

Analyzes whether the components of `family_complexity` capture physical planet signatures or track detector activity and pipeline statistics.

## 1. Detector Influence Matrix (Pearson r)

| Component | `FC_events` | `FC_hypotheses` | `FC_clusters` | `FC_support` | `FC_coverage` | `FC_stability` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `FC_events` | 1.0000 | 0.8876 | 0.2721 | 0.0057 | 0.5237 | 0.5237 |
| `FC_hypotheses` | 0.8876 | 1.0000 | 0.1348 | -0.0640 | 0.3361 | 0.3361 |
| `FC_clusters` | 0.2721 | 0.1348 | 1.0000 | 0.8758 | 0.6124 | 0.6124 |
| `FC_support` | 0.0057 | -0.0640 | 0.8758 | 1.0000 | 0.5240 | 0.5240 |
| `FC_coverage` | 0.5237 | 0.3361 | 0.6124 | 0.5240 | 1.0000 | 1.0000 |
| `FC_stability` | 0.5237 | 0.3361 | 0.6124 | 0.5240 | 1.0000 | 1.0000 |

## 2. Planetary Physics Influence Matrix (Pearson r)

| Component | `depth` | `duration` | `period` | `estimated_snr` |
| :--- | :---: | :---: | :---: | :---: |
| `FC_events` | 0.0622 | -0.0603 | -0.1068 | 0.2982 |
| `FC_hypotheses` | 0.0192 | -0.0430 | -0.0589 | 0.1823 |
| `FC_clusters` | -0.0316 | -0.0946 | -0.0392 | -0.1063 |
| `FC_support` | -0.0973 | -0.0699 | 0.0020 | -0.2239 |
| `FC_coverage` | 0.0448 | -0.0855 | -0.0916 | 0.0787 |
| `FC_stability` | 0.0448 | -0.0855 | -0.0916 | 0.0787 |

## 3. Detector-to-Physics Influence (DPI) Analysis (Audit 15.3B)

*   **Detector Influence Score (mean |r| vs other detector components)**: 0.5992
*   **Physics Influence Score (mean |r| vs planetary parameters)**: 0.0751
*   **Detector-to-Physics Influence (DPI) Ratio**: **7.9752**
*   **Causality Classification**: **DETECTOR DOMINATED**

> [!WARNING]
> **DETECTOR DOMINANCE DETECTED**: family_complexity is primarily measuring detector combinatorics and pipeline activity rather than exoplanet physics.

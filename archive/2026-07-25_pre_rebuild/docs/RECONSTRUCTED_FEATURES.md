# Audit 15.6 & 15.6B — Reconstructed Features & LOCO Necessity Analysis

Evaluates the candidate reconstructed features built directly from internal components, and ranks the components by ablation necessity.

## 1. Reconstructed Candidate Features Performance Matrix

| Feature | CV Mean AUROC | CV Mean PR-AUC | Blind Split AUROC | Blind Split PR-AUC |
| :--- | :---: | :---: | :---: | :---: |
| `FC_RECON_RATIO_SUPPORT` | 0.5905 | 0.7871 | 0.5946 | 0.7429 |
| `FC_RECON_COVERAGE` | 0.5620 | 0.7711 | 0.6523 | 0.7603 |
| `FC_RECON_CLUSTERS` | 0.5595 | 0.7744 | 0.6147 | 0.7875 |
| `FC_RECON_EVENTS` | 0.5587 | 0.7667 | 0.5559 | 0.6911 |
| `FC_RECON_DENSITY` | 0.5587 | 0.7667 | 0.5559 | 0.6911 |
| `FC_RECON_COMBINED` | 0.5426 | 0.7650 | 0.6274 | 0.7894 |
| `FC_RECON_RATIO_COVERAGE` | 0.5065 | 0.7278 | 0.4689 | 0.7076 |
| `FC_RECON_MULTIPLICITY` | 0.5000 | 0.8671 | 0.5000 | 0.8333 |
| `FC_RECON_HYPOTHESES` | 0.4962 | 0.7220 | 0.5559 | 0.6911 |
| `FC_RECON_SUPPORT` | 0.4834 | 0.7323 | 0.6042 | 0.7774 |

## 2. Audit 15.6B — Leave-One-Component-Out (LOCO) Necessity Analysis

Evaluates the degradation in performance when each of the 6 components is ablated from the full internal model.

| Ablated Component | Delta CV Mean AUROC | Delta CV Mean PR-AUC | Component Category |
| :--- | :---: | :---: | :--- |
| `FC_events` | -0.0431 | -0.0280 | Redundant (degradation <= 0.005) |
| `FC_hypotheses` | -0.0214 | -0.0170 | Redundant (degradation <= 0.005) |
| `FC_clusters` | +0.0118 | +0.0062 | **Supporter** (0.005 < degradation <= 0.02) |
| `FC_support` | -0.0060 | -0.0114 | Redundant (degradation <= 0.005) |
| `FC_coverage` | +0.0000 | +0.0000 | Redundant (degradation <= 0.005) |
| `FC_stability` | +0.0000 | +0.0000 | Redundant (degradation <= 0.005) |

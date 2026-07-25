# Audit 15.1 — Family Complexity Mathematical Dissection

Identifies the exact mathematical construction of `family_complexity` and measures statistical distributions and mutual information.

## 1. Formula & Pipeline Stages
`family_complexity` in TARS represents the count of candidates surviving the full chain of Stage 3 recoverer filters:
1. **Stage 2 trigger events** -> `FC_events` ($N_{\text{events}}$)
2. **Pairwise interval generator** -> `FC_hypotheses` ($N_{\text{hypotheses}}$)
3. **Harmonic clustering resolver** -> `FC_clusters` ($N_{\text{clusters}}$)
4. **Supporting events threshold (>= 2)** -> `FC_support` ($N_{\text{support\_pass}}$)
5. **Observation coverage fraction threshold (>= 0.1)** -> `FC_coverage` ($N_{\text{coverage\_pass}}$)
6. **Timing residuals stability threshold** -> `FC_stability` ($N_{\text{stability\_pass}}$, the final `family_complexity`)

## 2. Component Demographics & Information Metrics (Active Split)

| Component | Mean | Std | Min | Max | Variance | Shannon Entropy | Mutual Information |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `FC_events` | 39.53 | 37.62 | 12.0 | 577.0 | 1415.15 | 3.8673 | 0.0336 |
| `FC_hypotheses` | 14691.09 | 60678.55 | 660.0 | 1661760.0 | 3681885872.33 | 3.8673 | 0.0338 |
| `FC_clusters` | 3779.98 | 2640.53 | 51.0 | 29626.0 | 6972409.40 | 6.2318 | 0.1903 |
| `FC_support` | 322.43 | 151.27 | 20.0 | 1468.0 | 22883.84 | 5.5950 | 0.1294 |
| `FC_coverage` | 91.14 | 54.23 | 19.0 | 688.0 | 2941.34 | 4.6904 | 0.0662 |
| `FC_stability` | 91.14 | 54.23 | 19.0 | 688.0 | 2941.34 | 4.6904 | 0.0662 |

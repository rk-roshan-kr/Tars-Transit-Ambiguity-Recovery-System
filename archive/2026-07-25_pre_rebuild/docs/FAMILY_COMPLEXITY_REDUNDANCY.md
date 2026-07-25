# Audit 15.5 & 15.5B — Family Complexity Redundancy & Stability

Analyzes multicollinearity and generalizes component distributions across active and blind splits.

## 1. Component Multicollinearity Metrics (Audit 15.5)

*   **Effective Rank (R_eff)**: **2.81** (out of 6 components)
*   **Participation Ratio (PR)**: **2.33**

## 2. Split Stability Matrix (Audit 15.5B)

| Component | KS Distance | Population Stability Index (PSI) | Wasserstein Distance | Stability Status |
| :--- | :---: | :---: | :---: | :---: |
| `FC_events` | 0.0816 | 0.2006 | 5.8758 | **MARGINAL** |
| `FC_hypotheses` | 0.0816 | 0.2006 | 7577.3798 | **MARGINAL** |
| `FC_clusters` | 0.1597 | 0.3294 | 410.8037 | **UNSTABLE** |
| `FC_support` | 0.1433 | 0.4965 | 32.7936 | **UNSTABLE** |
| `FC_coverage` | 0.1235 | 0.1631 | 6.0836 | **MARGINAL** |
| `FC_stability` | 0.1235 | 0.1631 | 6.0836 | **MARGINAL** |

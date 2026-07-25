# Audit 17.1 — Candidate Family Entropy Analysis

Analyzes Shannon entropy, normalized entropy metrics, and raw candidate counts across recovery stages to determine whether candidate counts or candidate uncertainty is responsible for the family_complexity signal.

| Entropy / Count Metric | CV Mean AUROC | CV Mean PR-AUC | Blind Split AUROC | KS Statistic | Cliff's Delta | Cohen's d | Pearson r | Spearman rho |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `H_candidate` | 0.5625 | 0.7717 | 0.6492 | 0.1208 | -0.1259 | -0.2591 | -0.1138 | -0.0963 |
| `H_candidate_norm` | 0.4368 | 0.6966 | 0.5339 | 0.1114 | -0.0870 | -0.0245 | -0.0108 | -0.0666 |
| `FC_stability` | 0.5620 | 0.7711 | 0.6523 | 0.1133 | -0.1252 | -0.2244 | -0.0987 | -0.0958 |
| `H_harmonic` | 0.5595 | 0.7744 | 0.6147 | 0.1125 | -0.1110 | -0.2166 | -0.0953 | -0.0850 |
| `FC_clusters` | 0.5595 | 0.7744 | 0.6147 | 0.1125 | -0.1110 | -0.2287 | -0.1006 | -0.0850 |
| `H_support` | 0.5149 | 0.7523 | 0.6042 | 0.0659 | -0.0247 | -0.0820 | -0.0362 | -0.0189 |
| `FC_support` | 0.4834 | 0.7323 | 0.6042 | 0.0659 | -0.0247 | -0.0699 | -0.0309 | -0.0189 |
| `H_coverage` | 0.5620 | 0.7711 | 0.6523 | 0.1133 | -0.1252 | -0.2593 | -0.1139 | -0.0958 |
| `FC_coverage` | 0.5620 | 0.7711 | 0.6523 | 0.1133 | -0.1252 | -0.2244 | -0.0987 | -0.0958 |

# Audit 17.3 — Alias Network Reconstruction

Evaluates network-based representations of candidate periods and their harmonic connections to check if family_complexity measures network topology.

| Network Metric | CV Mean AUROC | CV Mean PR-AUC | Blind Split AUROC | KS Statistic | Cliff's Delta | Cohen's d | Pearson r | Spearman rho |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `graph_density` | 0.4728 | 0.7249 | 0.5631 | 0.0779 | 0.0177 | -0.0186 | -0.0082 | 0.0135 |
| `graph_clustering` | 0.5121 | 0.7486 | 0.4777 | 0.0481 | -0.0246 | -0.1316 | -0.0581 | -0.0188 |
| `graph_components` | 0.5513 | 0.7723 | 0.5631 | 0.0903 | 0.1023 | 0.1918 | 0.0845 | 0.0828 |
| `graph_entropy` | 0.5639 | 0.7758 | 0.6454 | 0.1148 | -0.1282 | -0.2819 | -0.1236 | -0.0981 |
| `graph_spectral_radius` | 0.5482 | 0.7744 | 0.6616 | 0.1140 | -0.0959 | -0.2667 | -0.1171 | -0.0734 |

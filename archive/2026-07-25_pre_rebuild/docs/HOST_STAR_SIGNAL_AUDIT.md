# Audit 16.1 — Host-Star Signal Audit

Evaluates each catalog and observation metadata feature independently to assess standalone predictive power and statistical diagnostics.

| Feature | CV Mean AUROC | CV Mean PR-AUC | Mutual Info | KS Statistic | KS p-value | Cliff's Delta | Pearson r | Spearman rho |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `header_teff` | 0.7138 | 0.8247 | 0.3994 | 0.3897 | 1.5051e-51 | -0.4088 | -0.2193 | -0.2811 |
| `header_logg` | 0.6560 | 0.7643 | 0.3862 | 0.3661 | 3.1133e-40 | 0.4083 | 0.4225 | 0.3895 |
| `header_radius` | 0.7342 | 0.8064 | 0.4119 | 0.4017 | 9.7697e-54 | -0.4721 | -0.2671 | -0.2977 |
| `header_tessmag` | 0.5755 | 0.7340 | 0.4105 | 0.2203 | 7.5795e-17 | -0.1774 | -0.1489 | -0.1359 |
| `spectral_class_ord` | 0.6981 | 0.8531 | 0.0448 | 0.3187 | 2.6771e-34 | -0.3755 | -0.2600 | -0.2640 |
| `lum_class_ord` | 0.6048 | 0.8836 | 0.0482 | 0.2221 | 2.0860e-16 | 0.2248 | 0.3480 | 0.3601 |
| `sector_count` | 0.4681 | 0.7147 | 0.0813 | 0.1606 | 3.9389e-09 | -0.1032 | -0.0701 | -0.0797 |
| `observation_count` | 0.6894 | 0.8923 | 0.2119 | 0.5225 | 7.7660e-97 | 0.3849 | 0.3654 | 0.2955 |

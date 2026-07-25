# Audit 18.3 — Full Pipeline Replacement Test

Evaluates the impact of replacing family_complexity with RAI_unsupervised across all model architectures in the production stack.

### Model A

| Version | Blind Split AUROC [95% CI] | Blind Split PR-AUC [95% CI] | ECE | Brier Score |
| :--- | :---: | :---: | :---: | :---: |
| Legacy (Version L) | 0.5789 [0.3895, 0.7057] | 0.7335 [0.4038, 0.8794] | 0.0966 | 0.2255 |
| Replacement (Version R) | 0.5947 [0.4096, 0.7209] | 0.7246 [0.4266, 0.8586] | 0.1054 | 0.2266 |

### Model B

| Version | Blind Split AUROC [95% CI] | Blind Split PR-AUC [95% CI] | ECE | Brier Score |
| :--- | :---: | :---: | :---: | :---: |
| Legacy (Version L) | 0.4333 [0.3185, 0.5921] | 0.6400 [0.4440, 0.8200] | 0.0814 | 0.2283 |
| Replacement (Version R) | 0.4333 [0.3138, 0.5781] | 0.6400 [0.4379, 0.8174] | 0.0814 | 0.2283 |

### Model C

| Version | Blind Split AUROC [95% CI] | Blind Split PR-AUC [95% CI] | ECE | Brier Score |
| :--- | :---: | :---: | :---: | :---: |
| Legacy (Version L) | 0.5868 [0.4040, 0.7076] | 0.7398 [0.4985, 0.8896] | 0.0995 | 0.2259 |
| Replacement (Version R) | 0.5996 [0.3675, 0.7229] | 0.7394 [0.4694, 0.8797] | 0.1149 | 0.2269 |

### Model D

| Version | Blind Split AUROC [95% CI] | Blind Split PR-AUC [95% CI] | ECE | Brier Score |
| :--- | :---: | :---: | :---: | :---: |
| Legacy (Version L) | 0.5683 [0.3632, 0.7009] | 0.7045 [0.4561, 0.8834] | 0.0615 | 0.2253 |
| Replacement (Version R) | 0.4804 [0.3710, 0.5978] | 0.6400 [0.3966, 0.7901] | 0.0706 | 0.2274 |


# Audit 9: Latent Dimension Sweep Ablation Study

Evaluates representation collapse and classification utility across varying latent dimensions $D$.

## 1. Latent Dimension Sweep Summary

| Latent Dimension ($D$) | Normalized Rank ($R_{\text{norm}}$) | Normalized Participation Ratio ($PR_{\text{norm}}$) | Probe AUROC | Status |
| :---: | :---: | :---: | :---: | :---: |
| 8 | 0.1573 | 0.1251 | 0.4872 | COLLAPSED |
| 16 | 0.0992 | 0.0626 | 0.5613 | COLLAPSED |
| 32 | 0.0797 | 0.0318 | 0.4467 | COLLAPSED |
| 64 | 0.0304 | 0.0157 | 0.5704 | COLLAPSED |
| 128 | 0.0198 | 0.0079 | 0.5501 | COLLAPSED |
| 256 | 0.0092 | 0.0039 | 0.5411 | COLLAPSED |

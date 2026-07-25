# Audit 2: Representation Collapse Diagnostics

This report diagnoses potential dimensional collapse of the latent space of SSL models.

## 1. Dimensional Metrics

| Model Architecture | Normalized Effective Rank ($R_{\text{norm}}$) | Normalized Participation Ratio ($PR_{\text{norm}}$) | Variance Floor | Status |
| :--- | :---: | :---: | :---: | :---: |
| Autoencoder | 0.0219 | 0.0157 | 6.44e+00 | COLLAPSED |
| VAE | 0.5181 | 0.0226 | 6.35e-04 | COLLAPSED |
| Contrastive (SimCLR) | 0.1541 | 0.0169 | 1.75e+01 | COLLAPSED |
| Masked Autoencoder | 0.0237 | 0.0156 | 2.05e-01 | COLLAPSED |

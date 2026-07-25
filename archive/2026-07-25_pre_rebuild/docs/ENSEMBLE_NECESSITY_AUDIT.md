# Audit 19.7 — Ensemble Necessity Audit

Determines whether Model D (the non-linear ensemble) outperforms simpler architectures beyond bootstrap uncertainty.

*   **Model C (EEA+ECHO) Blind AUROC [95% CI]**: **0.5996** [0.4118, 0.7343]
*   **Model D (Ensemble) Blind AUROC [95% CI]**: **0.4948** [0.3813, 0.6363]
*   **Model D Standalone Gain**: **-0.1048**
*   **Model D Exceeds Model C Upper CI**: **False**

> [!IMPORTANT]
> **ENSEMBLE NECESSITY VERDICT: REDUNDANT**
> Model D fails to statistically outperform the linear Model C. The complexity cost is unjustified.

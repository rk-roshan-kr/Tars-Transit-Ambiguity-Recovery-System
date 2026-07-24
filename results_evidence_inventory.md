# Evidence Inventory: Results

## 1. Relevant Repository Documents
- **[BOOTSTRAP_STABILITY_ANALYSIS.md](file:///d:/TARS/TarsEx/docs/BOOTSTRAP_STABILITY_ANALYSIS.md)**: Details the bootstrap mean AUROC and standard deviations (Model A, Model C, Linear Stack, RAI-only).
- **[RAI_COMPONENT_ABLATION.md](file:///d:/TARS/TarsEx/docs/RAI_COMPONENT_ABLATION.md)**: Details the ablation of individual components of the RAI and their delta AUROCs.
- **[CALIBRATION_ANALYSIS.md](file:///d:/TARS/TarsEx/docs/CALIBRATION_ANALYSIS.md)**: Details ECE, Brier Score, calibration slope/intercept, and binned reliability matrix.
- **[SENSITIVITY_ANALYSIS.md](file:///d:/TARS/TarsEx/docs/SENSITIVITY_ANALYSIS.md)**: Details CMI discretization sensitivity across different bin counts ($K \in [4, 20]$).
- **[NOISE_JITTER_PERTURBATION.md](file:///d:/TARS/TarsEx/docs/NOISE_JITTER_PERTURBATION.md)**: Details performance decay under Gaussian noise, missing features, and systematic bias.
- **[RECOVERY_CURVE_VERIFICATION.md](file:///d:/TARS/TarsEx/docs/RECOVERY_CURVE_VERIFICATION.md)**: Details subgroup recovery counts and rates across SNR, orbital period, and stellar magnitude.
- **[RAI_ONLY_DOMINANCE_ANALYSIS.md](file:///d:/TARS/TarsEx/docs/RAI_ONLY_DOMINANCE_ANALYSIS.md)**: Details Leave-One-Feature-Out (LOFO) and Forward Feature Selection traces.
- **[GIANT_STAR_FAILURE_ANALYSIS.md](file:///d:/TARS/TarsEx/docs/GIANT_STAR_FAILURE_ANALYSIS.md)**: Details failure modes on subgiants/giants host stars.
- **[INFORMATION_THEORY_VERIFICATION.md](file:///d:/TARS/TarsEx/docs/INFORMATION_THEORY_VERIFICATION.md)**: Details numerical agreement between production and clean-room reference estimators.

---

## 2. Key Evidence & Statistics to Extract
- Model comparison bootstrap AUROC (RAI-only: $0.6621 \pm 0.0694$; Stack: $0.6243 \pm 0.0818$).
- Ablation of individual sub-features (Harmonic density delta AUROC: $-0.0116$; Uniqueness delta: $-0.0149$).
- Calibration error: $\text{ECE} = 0.0646$, Brier Score = $0.2309$.
- CMI sensitivity sweeps showing legacy feature redundancy is robust to bin counts ($p \ge 0.20$ across $K \in [4, 20]$).
- Noise robustness: Graceful decay to $0.6276$ under $\sigma = 1.0$ noise, rank-preserving invariance under bias.
- Subgroup rates: Bright stars ($96.1\%$), Medium stars ($97.7\%$), Faint stars ($100.0\%$).
- LOFO drops: `family_complexity` ($0.0534$), `baseline_span` ($0.0311$).
- Forward Feature Selection degradation from $0.6943$ to $0.5868$ as non-ambiguity features are added.
- Failure analysis: event inflation (46.07 vs. 37.92 events) and lower period spacing on giants (0.2465 vs. 0.2666).

---

## 3. Missing Information
- None.

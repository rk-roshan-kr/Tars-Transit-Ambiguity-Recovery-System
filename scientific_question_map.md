# TARS v1 Scientific Question Map

This map organizes the manuscript expansion around key scientific questions rather than file structures, directing where each repository document contributes.

---

| Scientific Question | Repository Documents | Target Section |
| :--- | :--- | :---: |
| Can recovery ambiguity be isolated as a distinct, measurable quantity during transit vetting? | `RECOVERY_AMBIGUITY_INDEX.md`, `SCIENTIFIC_OBJECTIVES.md` | Introduction & Methods |
| What is the mathematical formulation of the Recovery Ambiguity Index (RAI)? | `RECOVERY_AMBIGUITY_INDEX.md`, `CANDIDATE_FAMILY_ENTROPY.md`, `FORMULA_AUDIT.md` | Methodology §3.x |
| How does TARS v1 construct the period recovery alias network and extract connected components? | `PERIOD_RECOVERY_ARCHITECTURE.md`, `STAGE3_FINAL_BLUEPRINT.md` | Methodology §3.x |
| Does the single-feature RAI model achieve comparable ranking performance to complex multi-feature stacks? | `BOOTSTRAP_STABILITY_ANALYSIS.md`, `RAI_ONLY_DOMINANCE_ANALYSIS.md` | Results §4.2 |
| Do the 5 individual sub-features of the RAI contribute uniquely to ranking and probability calibration? | `RAI_COMPONENT_ABLATION.md`, `LOFO_ABLATION_REPORT.md` | Results §4.4 |
| Is the predicted probability link calibrated and operationally reliable? | `CALIBRATION_ANALYSIS.md`, `CALIBRATION_ROOT_CAUSE.md` | Results §4.5 |
| Are legacy exoplanet vetting features statistically redundant after conditioning on the RAI? | `SENSITIVITY_ANALYSIS.md`, `INFORMATION_THEORY_VERIFICATION.md` | Results §4.6 |
| How robust is the RAI model under Gaussian noise, feature dropouts, and systematic bias? | `NOISE_JITTER_PERTURBATION.md`, `FINAL_ROBUSTNESS_AUDIT.md` | Results §4.7 |
| What is the recovery rate across orbital period, stellar magnitude, and signal-to-noise ratio (SNR) subgroups? | `RECOVERY_CURVE_VERIFICATION.md` | Results §4.8 |
| What are the physical limits of TARS v1, and why does performance degrade on giant host stars? | `GIANT_STAR_FAILURE_ANALYSIS.md`, `FAILURE_MODES_STAGE3.md`, `HOST_STAR_PHYSICS_AUDIT.md` | Results §4.9 & Limitations §6.x |

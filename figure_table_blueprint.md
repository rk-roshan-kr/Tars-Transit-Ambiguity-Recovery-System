# TARS v1 Figure, Table, and Equation Blueprint

This blueprint defines the final list of figures, tables, and equations that will appear in the expanded manuscript.

---

## 1. Figures

| Figure | Source Document(s) | Target Section | Scientific Purpose |
| :---: | :--- | :---: | :--- |
| **Figure 1** | `TARS_PRODUCTION_ARCHITECTURE_V1.md` | Introduction §1.2 | Pipeline flow diagram showing the 5-stage TARS architecture and information flow. |
| **Figure 2** | `PERIOD_RECOVERY_ARCHITECTURE.md` | Methodology §3.2 | Period recovery alias graph construction example with nodes and matching edges. |
| **Figure 3** | `BOOTSTRAP_VERIFICATION.md` | Results §4.2 | Bootstrap AUROC distribution density curves comparing RAI-only vs Linear Stack. |
| **Figure 4** | `CALIBRATION_ANALYSIS.md` | Results §4.5 | Reliability diagram (predicted probability vs empirical fraction) with confidence bands. |
| **Figure 5** | `NOISE_JITTER_PERTURBATION.md` | Results §4.7 | Robustness perturbation decay curves (AUROC vs. noise scale $\sigma$ and drop rate $p_{\text{drop}}$). |
| **Figure 6** | `GIANT_STAR_FAILURE_ANALYSIS.md` | Results §4.9 | Comparative alias graph topologies of a quiet dwarf system vs. an active giant host star. |

---

## 2. Tables

| Table | Source Document(s) | Target Section | Scientific Purpose |
| :---: | :--- | :---: | :--- |
| **Table 1** | `REVIEWER_ATTACK_MATRIX.md`, `NOVELTY_DEFENSE.md` | Related Work §2.4 | Novelty positioning matrix comparing TARS v1 vs Robovetter, Astronet, and Vespa. |
| **Table 2** | `BOOTSTRAP_STABILITY_ANALYSIS.md` | Results §4.1 | Overall classifier complexity and performance comparison (AUROC, std, var, ECE). |
| **Table 3** | `RAI_COMPONENT_ABLATION.md` | Results §4.4 | RAI component ablation study matrix (delta AUROC and delta ECE for each sub-feature). |
| **Table 4** | `CALIBRATION_ANALYSIS.md` | Results §4.5 | Binned reliability metrics showing binned confidence vs empirical positive rate. |
| **Table 5** | `SENSITIVITY_ANALYSIS.md` | Results §4.6 | Conditional Mutual Information (CMI) discretization sensitivity table ($K \in [4, 20]$). |
| **Table 6** | `NOISE_JITTER_PERTURBATION.md` | Results §4.7 | Model performance under noise, missing features, and systematic offsets. |
| **Table 7** | `RECOVERY_CURVE_VERIFICATION.md` | Results §4.8 | Subgroup recovery rates across period, magnitude, and SNR bins. |
| **Table 8** | `GIANT_STAR_FAILURE_ANALYSIS.md` | Results §4.9 | Dwarf vs. giant host star sub-feature and ambiguity profiles comparison. |
| **Table 9** | `RAI_ONLY_DOMINANCE_ANALYSIS.md` | Results §4.11 | Forward Feature Selection trace on the blind validation partition. |

---

## 3. Equations

| Equation | Source Document(s) | Target Section | Scientific Purpose |
| :---: | :--- | :---: | :--- |
| **E-01** | `CANDIDATE_FAMILY_ENTROPY.md` | Methodology §3.3 | normalized Shannon entropy $x_{\text{ent}}$ of degree distribution. |
| **E-02** | `EQUATION_REGISTRY_STAGE3.md` | Methodology §3.3 | Harmonic matching density $x_{\text{hden}}$ ratio. |
| **E-03** | `EQUATION_REGISTRY_STAGE3.md` | Methodology §3.3 | Period uniqueness $x_{\text{uniq}}$ average cluster spacing. |
| **E-04** | `EQUATION_REGISTRY_STAGE3.md` | Methodology §3.3 | Candidate concentration $x_{\text{conc}}$ power ratio. |
| **E-05** | `RECOVERY_AMBIGUITY_INDEX.md` | Methodology §3.4 | Standardized signed sum index $\text{RAI}_{\text{raw}}$ formula. |
| **E-06** | `FORMULA_AUDIT.md` | Methodology §3.5 | Logistic calibration link probability mapping function. |
| **E-07** | `FORMULA_AUDIT.md` | Methodology §3.5 | Expected Calibration Error (ECE) metric definition. |
| **E-08** | `FORMULA_AUDIT.md` | Methodology §3.5 | Conditional Mutual Information (CMI) Shannon entropy formula. |

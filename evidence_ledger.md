# TARS v1 Evidence Ledger

This ledger indexes all scientifically relevant repository documents used for the TARS v1 manuscript expansion, categorized by Category and Scientific Priority (P1 to P4).

---

| Document | Category | Priority | Scientific Question | Main Text | Appendix | Excluded | Justification |
| :--- | :---: | :---: | :--- | :---: | :---: | :---: | :--- |
| `RECOVERY_AMBIGUITY_INDEX.md` | A | P1 | What is the mathematical definition and formula of the RAI? | Yes | No | No | Core definition of the RAI. |
| `CANDIDATE_FAMILY_ENTROPY.md` | A | P1 | How is Shannon entropy calculated on the candidate family graph? | Yes | Yes | No | Analytical derivation of graph entropy. |
| `TARS_PRODUCTION_ARCHITECTURE_V1.md` | A | P1 | What is the overall architectural flow of TARS v1? | Yes | No | No | Core pipeline description. |
| `BOOTSTRAP_STABILITY_ANALYSIS.md` | A | P1 | What are the bootstrap AUROC confidence intervals and variance of TARS v1? | Yes | No | No | Baseline validation statistical significance. |
| `RAI_COMPONENT_ABLATION.md` | A | P1 | What is the impact of ablating individual sub-features on calibration (ECE) and ranking (AUROC)? | Yes | No | No | Justification for all 5 sub-features. |
| `CALIBRATION_ANALYSIS.md` | A | P1 | Is TARS v1 calibrated, and does it exhibit binned linear scaling? | Yes | No | No | Calibration reliability validation. |
| `SENSITIVITY_ANALYSIS.md` | A | P1 | How sensitive is the Conditional Mutual Information (CMI) to discretization bin count $K$? | Yes | Yes | No | Bin count sensitivity verification. |
| `NOISE_JITTER_PERTURBATION.md` | A | P1 | How robust is the model under Gaussian noise, missing features, and systematic bias? | Yes | No | No | Robustness stress-testing. |
| `RECOVERY_CURVE_VERIFICATION.md` | A | P1 | What is the recovery rate across period, magnitude, and SNR subgroups? | Yes | No | No | Subgroup performance analysis. |
| `RAI_ONLY_DOMINANCE_ANALYSIS.md` | A | P1 | Does a single-feature RAI model dominate multi-feature stacks? | Yes | No | No | Forward selection & LOFO trace. |
| `GIANT_STAR_FAILURE_ANALYSIS.md` | A | P1 | Why does the model fail on subgiants and giant stars? | Yes | No | No | Photospheric convective granulation limits. |
| `INFORMATION_THEORY_VERIFICATION.md` | A | P1 | Do the production information theory estimators agree with the clean-room reference implementation? | Yes | Yes | No | Precision verification. |
| `FORMULA_AUDIT.md` | B | P2 | What are the detailed derivations of CMI and degree-based Shannon entropy? | No | Yes | No | Supplementary math proofs. |
| `PERIOD_RECOVERY_ARCHITECTURE.md` | B | P2 | What is the exact implementation of the Stage 3 recovery algorithm? | No | Yes | No | Supplementary algorithm specs. |
| `REVIEWER_ATTACK_MATRIX.md` | B | P2 | What are the common reviewer objections and our defenses? | Yes | Yes | No | Promoted to related work and threats to validity. |
| `FAILURE_MODES_STAGE3.md` | B | P2 | What are the core forensic registers and failures for Stage 3? | Yes | Yes | No | Failure galleries. |
| `STAGE3_FINAL_BLUEPRINT.md` | B | P2 | What are the parameters and settings used in the Stage 3 engine? | No | Yes | No | Supplementary parameter tables. |
| `TARS_STAGE3_BLUEPRINT_RECOVERY.md` | B | P3 | How did the Stage 3 blueprint evolve during design phases? | No | No | Yes | Internal planning history (replaced by FINAL_BLUEPRINT). |
| `STAGE3_SCIENTIFIC_CLOSURE.md` | B | P2 | What is the scientific closure checklist and consensus of Stage 3? | Yes | No | No | Promoted to Conclusion section. |
| `STAGE1_OPERATING_BOUNDARIES.md` | A | P2 | What are the sector boundaries and beta scaling limits for Stage 1? | Yes | No | No | Background context on prior stages. |
| `STAGE2_LIMITATIONS.md` | A | P2 | What are the detection thresholds and limitations of Stage 2? | Yes | No | No | Background context on prior stages. |

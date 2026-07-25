# Evidence Traceability Matrix (Audit 21.9)

| Manuscript Result | Source Script | Function | Output File |
| :--- | :--- | :--- | :--- |
| Blind AUROC (0.6630) | `scripts/run_independent_verification.py` | `roc_auc_score` | `docs/BOOTSTRAP_VERIFICATION.md` |
| CMI Point Estimate (0.0285) | `scripts/run_independent_verification.py` | `prod_conditional_mutual_information` | `docs/INFORMATION_THEORY_VERIFICATION.md` |
| Calibration slope (slope) | `scripts/run_publication_readiness.py` | `stats.linregress` | `docs/CALIBRATION_ANALYSIS.md` |
| Figure 1 (Parsimony) | `scripts/run_publication_readiness.py` | `plt.savefig` | `paper/figures/Figure1.png` |
| Figure 3 (Calibration) | `scripts/run_publication_readiness.py` | `plt.savefig` | `paper/figures/Figure3.png` |
| Figure 4 (Reliability) | `scripts/run_publication_readiness.py` | `plt.savefig` | `paper/figures/Figure4.png` |
| Table 1 (Parsimony) | `scripts/run_publication_readiness.py` | `to_csv` | `paper/tables/table1.csv` |
| Table 2 (Subgroup) | `scripts/run_publication_readiness.py` | `to_csv` | `paper/tables/table2.csv` |

# Catalog Coverage Report

This report presents the scientific audit of labeled coverage in the `TARS-250K-R1` corpus after the unified label expansion cross-match.

---

## 1. Summary of Ingested Labels

The coverage audit script `scripts/run_coverage_audit.py` compiled the completed targets:

*   **Total unique TICs in Completed Corpus**: 131,324
*   **Total Labeled TICs Matched**: 1,347
*   **Confirmed Planets (Tier A)**: 335
*   **Planet Candidates (Tier B)**: 818
*   **False Positives / Alarms (Tier C)**: 194
*   **Unlabeled Field Stars (Tier D / Unknowns)**: 129,977

---

## 2. STOP-GATE-11 Exit Gate Verdict

- **Requirement**: Labeled TICs $\ge 20,000$ to proceed with standard supervised-focused training.
- **Observed Count**: 1,347 unique TICs.
- **Verdict**: **REDIRECT (Exit Gate Triggered) [WARNING]**
- **Required Action**: Since the labeled sample size is below the 20,000 threshold, the framework automatically reprioritizes:
  *   **Primary Priority**: Self-Supervised representation learning (Phase 12) to extract latent features from all 131,000+ unlabeled targets.
  *   **Secondary Priority**: Weak label expansion (Phase 14) to generate pseudo-labels for high-confidence targets, boosting training data volumes deterministically.
  *   **Gating Rule**: Supervised model training will employ confidence-weighted loss functions to prevent overfitting to the small confirmed planet subset.

# TARS Core — Experiment Catalog

Every experiment that produces a figure, table, or claimed result must have an entry here. If a result is not in this catalog, it cannot appear in the paper.

---

## Experiment 1 — Detection Threshold Sweep

**Objective:** Objective 4 (What limits sparse-transit recovery?)
**Scientific Question:** What is the optimal local sigma threshold for event detection?

**Method:** Sweep `sigma_local` detection threshold from 2.5σ to 4.0σ in 8 steps. Run full pipeline at each threshold on the stratified validation split (301 TICs).

**Thresholds:** 2.50, 2.71, 2.93, 3.14, 3.36, 3.57, 3.79, 4.00 (σ)

**Measurements per threshold:**
- TP, FP, FN, TN
- Precision ± 95% CI
- Recall ± 95% CI
- F1-Score ± 95% CI

**Produces:** Metrics used in paper Table 6 (Threshold Sensitivity Sweep)

---

## Experiment 2 — Sparse Transit Scaling

**Objective:** Objective 4 (What limits recovery?) + Objective 1 (Can sparse chains be recovered?)
**Scientific Question:** How does pipeline performance degrade from N=6 down to N=2?

**Method:** Stratify validation set by transit count. Compute precision, recall, F1 separately for N=2, N=3, N=4, N=5, N=6 subgroups.

**Measurements:**
- Precision, Recall, F1 by N
- Period recovery accuracy by N (residual error)
- Stage survival rate by N

**Produces:** Potentially the most important figure in the paper. Directly validates the sparse-transit claim.

---

## Experiment 3 — Period Recovery Accuracy

**Objective:** Objective 1 (Sparse chain recovery without phase folding)
**Scientific Question:** How accurately does pairwise period search recover the true orbital period?

**Method:** On injection dataset (Dataset D), compare recovered period to injected period. Compute relative error: `|P_recovered - P_true| / P_true`.

**Measurements:**
- Mean relative period error by N
- Period recovery rate (within 30-min tolerance) by N
- Recovery rate vs. period length

**Produces:** Metrics used in injection recovery analysis

---

## Experiment 4 — Physics Ablation (EEA)

**Objective:** Objective 5 (What information contributes most?)
**Scientific Question:** What is the contribution of EEA morphological coherence?

**Method:** Run pipeline on validation split with EEA disabled (C_coh forced to 1.0 — neutral). Compare against full pipeline.

**Measurements:** TP, FP, FN, TN, Precision, Recall, F1, 95% CI for all.

**Produces:** Metrics used in paper Table 3, Variant B

---

## Experiment 5 — Physics Ablation (ECHO)

**Objective:** Objective 5 (What information contributes most?) + Objective 3 (Geometry-based FP reduction)
**Scientific Question:** What is the contribution of ECHO geometric vetting?

**Method:** Run pipeline on validation split with ECHO disabled (GCP threshold set to ∞ — all pass). Compare against full pipeline.

**Measurements:** TP, FP, FN, TN, Precision, Recall, F1, 95% CI for all.

**Produces:** Metrics used in paper Table 3, Variant C

---

## Experiment 6 — ML Ablation

**Objective:** Objective 2 (Physics vs. statistics vs. ML) + Objective 5
**Scientific Question:** Does ML contribute meaningfully beyond physics + statistics alone?

**Method:** Run pipeline on validation split with ML layer completely disabled (ML score set to 0.5 — neutral). Compare against full pipeline.

**Key scientific question this answers:** Can physics alone (Stages 1–5) achieve acceptable precision without any ML? This is critical for defending the "Physics > ML" thesis.

**Measurements:** TP, FP, FN, TN, Precision, Recall, F1, 95% CI for all.

**Produces:** Metrics used in paper Table 3, Variant A

---

## Experiment 7 — Failure Taxonomy

**Objective:** Objective 4 (What limits recovery?)
**Scientific Question:** Where in the pipeline are real planets lost?

**Method:** For every false negative in the validation set, record the stage at which it was rejected. Categorize by failure reason.

**Failure categories:**
- `FAIL_DETECTION` — dip below sigma threshold
- `FAIL_PERIOD` — no consistent period found
- `FAIL_EEA` — coherence score too low
- `FAIL_ECHO` — GCP veto
- `FAIL_STATISTICS` — insufficient statistical evidence
- `FAIL_ML` — ML ranking too low

**Produces:** Metrics used in paper Table 4 (Failure Taxonomy). Also directly drives the `CandidateForensics` object in every run.

---

## Experiment 8 — Statistical Layer Ablation

**Objective:** Objective 5 (What information contributes most?)
**Scientific Question:** What is the contribution of the statistical evidence layer (likelihood + BIC)?

**Method:** Run pipeline on validation split with statistical layer set to neutral evidence (log_LR = 0). Compare against full pipeline.

**Produces:** Supplementary ablation metrics

---

## Experiment 9 — Full Deployment Run

**Objective:** All 5 objectives
**Scientific Question:** What is the system-level performance on the real Sector 40 deployment?

**Method:** Run full pipeline on all 1,502 TICs from TESS Sector 40. Cross-reference detections against NASA Exoplanet Archive.

**Measurements:**
- Catalog precision (confirmed TOIs / total ACCEPT)
- Catalog recall (recovered TOIs / all observable TOIs)
- Candidate attrition waterfall
- Execution time per TIC

**Produces:** Deployment-level metrics, Figure 1 (Waterfall), Figure 2 (Yield by N)

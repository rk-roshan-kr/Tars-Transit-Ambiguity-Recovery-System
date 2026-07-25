# Stage 3 ML Training Dataset Blueprint

*Phase 5.5 — Component G. Defines the complete specification for the future ML training dataset. Sources: Phase 5.3 results (stage3_candidate_family_recall.csv, stage3_real_cp_replay.csv, stage3_real_ambiguity_analysis.csv). No implementation.*

---

## Dataset Purpose

The ML Training Dataset (MLTD-S3) is the labeled dataset from which the Stage 3 ML Ranking Layer (Phase 6B) will be trained. It must be generated strictly from existing Phase 5.3 CSV artifacts — no new experiments are required.

---

## Data Sources

| Source File | Contents | Role |
| :--- | :--- | :--- |
| `results/stage3_candidate_family_recall.csv` | Per-target: top1/top3/family success, true_rank, MRR | Label derivation |
| `results/stage3_real_cp_replay.csv` | Per-target: candidate_count, true_period_present, true_period_rank | Label derivation |
| `results/stage3_real_ambiguity_analysis.csv` | Per-target: confusion class (CORRECT, P_VS_2P, etc.) | Label derivation |
| `results/stage3_failure_catalog.csv` | Per-target: failure category (A/B/C/D/E/F) | Failure type label |

---

## Label Schema

Each record in MLTD-S3 represents a **single candidate period** evaluated against one target. The label is the candidate's classification:

| Label | Code | Definition |
| :--- | :---: | :--- |
| `TRUE_PERIOD` | 1 | Candidate satisfies $|P_{cand} - P_{true}| / P_{true} < 1\%$ |
| `HARMONIC_ALIAS` | 0 | Candidate is a harmonic of the true period ($2P$, $P/2$, $3P$, etc.) |
| `FALSE_PERIOD` | -1 | Candidate does not correspond to any known physical period |

**Label balance strategy**: The training dataset will be inherently imbalanced (few TRUE_PERIOD, many ALIAS and FALSE). Apply class-weighted training (inverse frequency weights) rather than oversampling to preserve realistic distribution.

---

## Feature Vector

Each record contains the following 10 features:

| Feature | Symbol | Source | Type |
| :--- | :--- | :--- | :--- |
| Coverage fraction | $C$ | Stage 3 observation window | Float [0,1] |
| Residual MAD (minutes) | $\text{MAD}$ | Stage 3 stability engine | Float ≥ 0 |
| Residual RMS (minutes) | $\text{RMS}$ | Stage 3 stability engine | Float ≥ 0 |
| N supporting events | $N_s$ | Stage 3 residual filter | Integer ≥ 2 |
| Candidate period (days) | $P$ | Stage 3 interval generator | Float > 0 |
| Harmonic class | $k$ | Stage 3 interval generator | Integer [1, Kmax] |
| Has aliases | $A$ | Stage 3 harmonic resolver | Binary |
| Ambiguity flagged | $F_{amb}$ | Stage 3 recoverer | Binary |
| N total candidates | $N_{cand}$ | Stage 3 recoverer | Integer ≥ 1 |
| Rank within candidate family | $r$ | Stage 3 recoverer (sorted output) | Integer ≥ 1 |

**Future physics features** (added in Phase 6C):
- $K_3$: Kepler consistency score (PF-01)
- $D_{cons}$: Transit duration consistency (PF-02)
- $p_{occ}$: Occurrence rate prior (PF-03)
- $\Phi_{chain}$: Event chain coherence (PF-07)

---

## Train / Validation / Test Split

```
Population A (Seed 42, N=1000 targets) → TRAINING SET
Population B (Seed 2026, N=1000 targets) → TEST SET
```

**Rules**:
- No data from Population B may be used during training or hyperparameter tuning.
- Hyperparameter tuning uses 5-fold cross-validation within Population A only.
- Population B is used for final evaluation only — it is held out until the model is frozen.

**Scientific justification**: Dual-population split prevents overfitting to simulator artifacts. If results differ substantially between populations, the model has overfit to Seed 42 specifics.

---

## Dataset Size Estimate

From Phase 5.3 dual-population runs (2000 targets × avg. ~5 candidates per target):

| Class | Estimated Records |
| :--- | :---: |
| TRUE_PERIOD | ~2000 (1 per target) |
| HARMONIC_ALIAS | ~5000–8000 |
| FALSE_PERIOD | ~1000–2000 |
| **Total** | ~8000–12000 records |

This is sufficient for logistic regression and random forest training. Gradient boosting may benefit from augmentation via additional Phase 5.2 diagnostic runs.

---

## Frozen Dataset Specification

When MLTD-S3 is built, it must be stored as:

```
results/mltd_stage3_train.csv   (Population A records)
results/mltd_stage3_test.csv    (Population B records)
results/mltd_stage3_metadata.json  (schema, sha256, seed, generation script)
```

The dataset is immutable once built. Any change to the feature set requires building a new version with an incremented version number.

---

## Evaluation Metrics

The ML Ranking Layer will be evaluated on:

| Metric | Definition | Target |
| :--- | :--- | :---: |
| Top-1 Recall | % targets where True Period is ranked 1st | ≥ 70% |
| Alias Discrimination AUC | ROC-AUC for TRUE_PERIOD vs HARMONIC_ALIAS | ≥ 0.85 |
| False Period Rejection | TRUE_PERIOD precision | ≥ 90% |
| Calibration Error (ECE) | Expected Calibration Error of P(true) scores | ≤ 0.05 |

These thresholds are pre-registered before any training is performed.

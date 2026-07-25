# TARS Dataset Governance Specification

**Status:** FROZEN — Phase 10.2
**Release Governed:** TARS-250K-R1
**Governed By:** Phase 10.2 — Dataset Governance, ML Architecture Integration & Corpus Freeze

---

## 1. Purpose

This document establishes the governance rules for the TARS scientific corpus.
Every dataset used in TARS training, validation, or testing must comply with
these rules.

Failure to comply is a scientific integrity violation, not a software bug.

---

## 2. Release Naming Convention

Corpus releases follow the naming schema:

```
TARS-{SIZE}K-R{RELEASE_NUMBER}
```

| Component | Description | Example |
|:---|:---|:---|
| `TARS` | Project namespace | `TARS` |
| `{SIZE}K` | Approximate corpus size in thousands | `250K` |
| `R{N}` | Sequential release number | `R1` |

**Current release:** `TARS-250K-R1`
**Next trigger:** Sectors 15+ ingested, or quality policy revised → `TARS-250K-R2`

A new release number is **required** whenever:
- Sector coverage expands
- Quality grade thresholds change
- Data source changes (e.g., SPOC → QLP)
- Any record is added or removed after freeze

---

## 3. Quality Grade Policy

Only Grade A, B, and C files are admitted to the corpus.
Grade F files are discarded at download time by the ingestion engine.

| Grade | Condition | Min Valid Cadences |
|:---:|:---|:---:|
| A | High quality | ≥ 16,000 |
| B | Standard | ≥ 12,000 |
| C | Marginal | ≥ 8,000 |
| **F** | **Discarded** | < 8,000 |

> [!IMPORTANT]
> Grade F files must never appear in the corpus. `run_dataset_audit.py`
> checks C4 (`C4_NO_GRADE_F`) to enforce this.

---

## 4. Reproducibility Requirements

Every experiment run that uses the corpus must record the following fields:

| Field | Source | Format |
|:---|:---|:---|
| `dataset_release_id` | `dataset_manifest.json → release_id` | String: `TARS-250K-R1` |
| `manifest_sha256` | `DatasetRegistry.get_sha256()` | 64-char hex |
| `pipeline_commit_hash` | `git rev-parse HEAD` | 40-char hex |
| `feature_registry_version` | `docs/BEI_FEATURE_ADMISSION_REGISTRY.md` | String |
| `likelihood_registry_version` | `docs/BEI_LIKELIHOOD_REGISTRY.md` | String |

These fields must appear in every `audit_trail` dict and every published result.

---

## 5. Split Policy

Corpus splits are assigned once and never regenerated.

| Split | Fraction | Purpose |
|:---|:---:|:---|
| Train | 70% | ML model training only |
| Validation | 15% | Hyperparameter tuning, calibration |
| Test | 15% | Final evaluation only — **sealed** |

**Rules:**
- Labels are assigned at split time and never modified.
- The test split is **sealed**: no development-time access.
- Splits are stratified by sector, then by quality grade.
- Split assignments are recorded in a versioned split manifest.

> [!CAUTION]
> Accessing the test split before final evaluation is a scientific integrity
> violation. The test split must remain unseen until the paper evaluation stage.

---

## 6. ML Governance Constraints

These constraints apply to any ML model trained on TARS corpus data:

### 6.1 Forbidden Features

ML models are forbidden from consuming the following Stage 6A BEI outputs:

| Feature | Reason |
|:---|:---|
| `posterior_probability` | Double-counting |
| `posterior_category` | ML would rank its own posterior |
| `log_posterior` | Derivative of posterior_probability |
| `physics_score` | Stage 6A intermediate |
| `confidence_score` | Stage 6A confidence metric |
| `ambiguity_score` | Stage 6A ambiguity metric |
| `ranking_trace` | Stage 3 heuristic leakage |
| `consensus_score` | Stage 3 heuristic leakage |
| `audit_trail` | Governance metadata |

These are enforced at runtime by `FeatureAdapter` and `validate_feature_vector()`.

### 6.2 Physics Veto Invariant

```
Stage 5 ECHO FAIL → final_category = FAIL
```

This cannot be overridden by ML output under any circumstances.
It is structurally enforced by `FusionDecision.__post_init__`.

### 6.3 Training Permission

ML training on the corpus requires:
1. Corpus release is `FROZEN`
2. `training_permitted = true` in the manifest
3. Train/Validation/Test splits are assigned and frozen

In Phase 10.2, `training_permitted = false`. Phase 11 will update this.

---

## 7. Dataset Versioning Protocol

### Freeze Protocol

A corpus release is frozen when:

1. The ingestion target is met (`completed_count ≥ target_count`)
2. `run_dataset_audit.py` passes all 10 governance checks
3. `manifest_sha256` is computed and recorded
4. `status` in the manifest is changed to `FROZEN`
5. The manifest is committed to version control

After freeze, the manifest is **read-only**. Any change requires a new release ID.

### Version Control

`data_registry/dataset_manifest.json` must be tracked in git.
The commit SHA at freeze time becomes the corpus's `pipeline_commit_hash`.

---

## 8. Audit Trail

The `run_dataset_audit.py` script produces `results/dataset_audit_report.json`
which records:

- All 10 governance check results (PASS/FAIL)
- Corpus statistics (counts, grades, sectors)
- Manifest SHA256
- Timestamp

This report must be re-run and archived whenever:
- A new corpus release is created
- A training run is initiated
- A paper result is submitted

---

## 9. Current Corpus State (TARS-250K-R1)

| Metric | Value |
|:---|:---|
| Release ID | `TARS-250K-R1` |
| Status | `FROZEN` |
| FITS on disk | 250,011 |
| Completed (DB) | 250,010 |
| Grade A | 109,573 (43.8%) |
| Grade B | 138,580 (55.4%) |
| Grade C | 1,857 (0.7%) |
| Sectors | 1 – 14 |
| Storage | `E:\dataset\tars` |
| Governance frozen | 2026-06-04 |

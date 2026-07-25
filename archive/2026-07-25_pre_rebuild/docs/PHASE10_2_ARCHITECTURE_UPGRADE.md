# Phase 10.2 — Architecture Upgrade Decision Record

**Phase:** 10.2 — Dataset Governance, ML Architecture Integration & Corpus Freeze
**Date:** 2026-06-04
**Status:** COMPLETE

---

## Decision

Upgrade the TARS architecture from a pure Physics+Bayesian system to a
**Physics-Constrained Hybrid Bayesian–ML Framework**.

---

## Architectural Change

### Before Phase 10.2

```
Stage 4 EEA → Stage 5 ECHO → Stage 6 BEI → Stage 7 Decision
```

### After Phase 10.2

```
Stage 4 EEA → Stage 5 ECHO
                  ├── Stage 6A BEI (Physics Posterior)     [ACTIVE]
                  └── Stage 6B ML Engine (Learned Post.)   [SCAFFOLD]
                            ↓
                    Stage 7 Decision (Fusion)               [SCAFFOLD]
```

The physics evidence hierarchy is unchanged:
**Physics First → Statistics Second → ML Third**

---

## Rationale

The existing Stage 6A BEI system (frozen in Phase 10) provides a scientifically
auditable Bayesian posterior over 16 admitted features. However, Bayesian inference
assumes a fixed likelihood model. A trained ML engine can learn:

1. **Non-linear feature interactions** not captured by Naive Bayes independence.
2. **Sector-specific systematic effects** from 250K real TESS light curves.
3. **Rare morphological patterns** not well-described by parametric distributions.

The ML engine is **auxiliary**, not authoritative. The physics veto from Stage 5
ECHO remains the terminal rejection gate.

---

## Governance Invariants Introduced

| ID | Invariant | Location |
|:---|:---|:---|
| ML-GOV-1 | Stage 6B forbidden from consuming Stage 6A outputs | `ml_engine_spec.py` |
| ML-GOV-2 | Physics veto is authoritative (ECHO FAIL → final FAIL) | `fusion_spec.py` |
| ML-GOV-3 | ML training corpus must be a frozen versioned release | `dataset_manifest.json` |
| ML-GOV-4 | No Stage 3 ranking leakage may enter Stage 6B | `ml_engine_spec.py` |
| S7-GOV-1 | Physics veto evaluated before any fusion | `fusion_spec.py` |
| S7-GOV-2 | BEI posterior is primary signal; ML is auxiliary | `fusion_spec.py` |
| S7-GOV-3 | Fusion weights frozen per release | `FusionPolicy` |
| S7-GOV-4 | FusionDecision is fully auditable | `FusionDecision` dataclass |
| INV-DR-1 | Manifests are read-only after freeze | `dataset_registry.py` |
| INV-DR-2 | SHA256 computed on canonical JSON | `dataset_registry.py` |
| INV-FA-1 | `adapt()` validates feature vector before returning | `feature_adapter.py` |
| INV-FA-2 | Adapter never adds features — only removes | `feature_adapter.py` |
| INV-FA-3 | Adapter logs every stripped key | `feature_adapter.py` |
| INV-FA-4 | Empty result after adaptation raises error | `feature_adapter.py` |

---

## Corpus Freeze: TARS-250K-R1

The 250K-star corpus was frozen at the following state:

| Metric | Value |
|:---|:---|
| FITS files on disk | **250,011** |
| COMPLETED (DB) | **250,010** |
| FAILED | 1,500 |
| PENDING (replacement queue) | 16,284 |
| Grade A (≥16K cadences) | 109,573 (43.8%) |
| Grade B (12K–16K cadences) | 138,580 (55.4%) |
| Grade C (8K–12K cadences) | 1,857 (0.7%) |
| Grade F (discarded) | 1,500 |
| Sectors covered | 1 – 14 (TESS SPOC 2-min) |
| Storage path | `E:\dataset\tars` |

---

## New Infrastructure

| File | Purpose |
|:---|:---|
| `data_registry/dataset_manifest.json` | Frozen corpus manifest (TARS-250K-R1) |
| `data_registry/dataset_registry.py` | `DatasetRegistry` class with SHA256 + validation |
| `tarscore/stage6_ml/ml_engine_spec.py` | ML governance: forbidden features, veto helper |
| `tarscore/stage6_ml/feature_adapter.py` | Feature isolation boundary (strips Stage 6A outputs) |
| `tarscore/stage7_decision/fusion_spec.py` | `FusionDecision`, `FusionPolicy`, `apply_physics_veto()` |
| `scripts/run_dataset_audit.py` | 10-point governance audit of the corpus |
| `docs/DATASET_GOVERNANCE_SPEC.md` | Dataset governance rules |
| `docs/TARS_ARCHITECTURE.md` | Master architecture reference |

---

## What This Phase Does NOT Include

- No ML model training (deferred to Phase 11)
- No changes to Stage 6A BEI (remains frozen)
- No changes to Stage 1–5 (remain frozen)
- No Stage 7 fusion implementation (weight=1.0 BEI, weight=0.0 ML until Phase 11)

---

## Next Phase

**Phase 11: ML Training & Fusion Calibration**

Prerequisites:
- TARS-250K-R1 corpus frozen ✓ (this phase)
- Stage 6B scaffold implemented ✓ (this phase)
- Stage 7 fusion scaffold implemented ✓ (this phase)
- Feature extraction pipeline from FITS → ML feature vector (Phase 11)
- XGBoost / LightGBM training on Train split (Phase 11)
- Fusion weight calibration on Validation split (Phase 11)

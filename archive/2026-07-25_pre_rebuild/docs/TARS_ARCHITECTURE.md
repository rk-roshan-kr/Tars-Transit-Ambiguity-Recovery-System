# TARS Architecture — Master Reference

*Phase 10.2 — Authoritative architecture document. All other architecture
references defer to this document when conflicts exist.*

---

## System Overview

TARS Core is a **Physics-Constrained Hybrid Bayesian–Machine Learning Framework**
for exoplanet transit candidate validation in sparse-transit regimes (N = 2, 3, 4
transits).

The system operates a 7-stage pipeline with a hybrid Stage 6 fork:

```
Raw Light Curve (TESS SPOC 2-min FITS)
        │
Stage 1  Signal Conditioning
        │  Detrending · Normalization · Noise estimation · Outlier removal
        │
Stage 2  Transit Event Detection
        │  MAD threshold · Adaptive SNR · Temporal clustering
        │
Stage 3  Sparse Period Recovery
        │  Pairwise intervals · Harmonic resolver · O-C timing · Consensus ranking
        │
Stage 4  Event Evidence Aggregation (EEA)
        │  Depth consistency · Duration consistency · Shape correlation · Phase coherence
        │
Stage 5  ECHO — Physics Firewall
        │  Geometric plausibility · Symmetry · Secondary eclipse veto
        │  → Decision: PASS | GRAY | FAIL
        │
        ├─── Stage 6A  BEI — Physics Posterior (Bayesian Evidence Integration)
        │         Naive Bayes over 16 admitted features
        │         → posterior_probability, posterior_category
        │
        └─── Stage 6B  ML Engine — Learned Posterior  [SCAFFOLD — Phase 11]
                  Physics-constrained feature vector (Stage 4/5 raw features only)
                  → ml_score, ml_category
                  (forbidden from consuming any Stage 6A output)
        │
Stage 7  Decision Fusion
         Physics veto applied first (ECHO FAIL → final FAIL)
         BEI posterior (weight=1.0) + ML score (weight=0.0 in Phase 10.2)
         → FusionDecision(final_category, physics_veto_applied, ...)
```

---

## Scientific Philosophy

The system enforces a strict evidence hierarchy:

| Priority | Layer | Role |
|:---:|:---|:---|
| 1 | **Physics (Stage 5 ECHO)** | Authoritative veto. Geometrically impossible transits are rejected. Cannot be overridden. |
| 2 | **Statistics (Stage 6A BEI)** | Bayesian posterior over physically plausible evidence. Primary classification signal. |
| 3 | **Machine Learning (Stage 6B)** | Auxiliary learned signal. Ranking and prioritization only. Never overrides physics. |

---

## Stage 6 Architecture: Feature Isolation Boundary

The central governance rule of the hybrid architecture is the **feature isolation
boundary** between Stage 6A and Stage 6B.

### What Stage 6B ML May NOT Consume (Forbidden Features)

| Feature | Source | Reason |
|:---|:---|:---|
| `posterior_probability` | Stage 6A BEI | Double-counting BEI evidence |
| `posterior_category` | Stage 6A BEI | ML would rank BEI's own output |
| `log_posterior` | Stage 6A BEI | Redundant with posterior_probability |
| `physics_score` | Stage 6A BEI | Derived Stage 6A intermediate |
| `confidence_score` | Stage 6A BEI | BEI confidence metric |
| `ambiguity_score` | Stage 6A BEI | BEI ambiguity metric |
| `ranking_trace` | Stage 3 | Stage 3 heuristic leakage |
| `consensus_score` | Stage 3 | Stage 3 heuristic leakage |
| `audit_trail` | Stage 6A BEI | Governance metadata, not a feature |

### What Stage 6B ML MAY Consume (Admitted Feature Families)

- **Temporal**: `coverage_fraction`, `transit_count`, `gap_fraction`, `cadence_regularity`
- **Harmonic**: `harmonic_ratio`, `alias_count`, `harmonic_confidence`
- **Stability**: `residual_rms`, `residual_mad`, `depth_consistency`, `duration_consistency`
- **Information**: `snr_mean`, `snr_min`, `information_content`
- **Observability**: `window_efficiency`, `baseline_days`, `sector_count`
- **Physics (raw)**: `transit_depth_ppm`, `transit_duration_hrs`, `rp_rs_ratio`
- **Morphology**: `symmetry_score`, `flatness_score`, `v_shape_score`
- **ECHO Flags (binary only)**: `depth_constant_flag`, `symmetry_flag`, `secondary_eclipse_flag`

The `FeatureAdapter` class (`tarscore/stage6_ml/feature_adapter.py`) enforces
this boundary at runtime. It strips all forbidden features before any ML inference.

---

## Stage 7 Physics Veto Invariant

```
IF Stage 5 ECHO → FAIL
THEN final_category = FAIL
     physics_veto_applied = True
     (no fusion performed)
```

This is structurally enforced by `FusionDecision.__post_init__`. A
`FusionDecision` with `echo_decision="FAIL"` and `final_category ≠ "FAIL"`
raises `FusionGovernanceError` at construction time — it cannot be created.

---

## Corpus: TARS-250K-R1

| Field | Value |
|:---|:---|
| Release ID | `TARS-250K-R1` |
| Status | `FROZEN` |
| FITS on disk | 250,011 |
| Completed (DB) | 250,010 |
| Grade A | 109,573 (43.8%) |
| Grade B | 138,580 (55.4%) |
| Grade C | 1,857 (0.7%) |
| Sectors | 1 – 14 (TESS SPOC 2-min) |
| Storage | `E:\dataset\tars` |
| Manifest | `data_registry/dataset_manifest.json` |

---

## Reproducibility Requirements

Every experiment report must record:

| Field | Source |
|:---|:---|
| `dataset_release_id` | `data_registry/dataset_manifest.json` |
| `manifest_sha256` | `DatasetRegistry.get_sha256(release_id)` |
| `pipeline_commit_hash` | `git rev-parse HEAD` |
| `feature_registry_version` | `BEI_FEATURE_ADMISSION_REGISTRY_v1` |
| `likelihood_registry_version` | `BEI_LIKELIHOOD_REGISTRY_v1` |

---

## Module Map

| Path | Stage | Status |
|:---|:---|:---|
| `tarscore/stage1_conditioning/` | 1 — Signal Conditioning | FROZEN |
| `tarscore/stage2_detection/` | 2 — Event Detection | FROZEN |
| `tarscore/stage3_period_recovery/` | 3 — Period Recovery | FROZEN |
| `tarscore/stage4_eea/` | 4 — EEA | FROZEN |
| `tarscore/stage4_physics/` | 4 — Physics | FROZEN |
| `tarscore/stage5_echo/` | 5 — ECHO Firewall | FROZEN |
| `tarscore/stage5_statistical/` | 5 — Statistical | FROZEN |
| `tarscore/stage6_bei/` | 6A — BEI Posterior | FROZEN (Phase 10) |
| `tarscore/stage6_ml/` | 6B — ML Engine | SCAFFOLD (Phase 11) |
| `tarscore/stage7_decision/` | 7 — Fusion | SCAFFOLD (Phase 11) |
| `data_registry/` | Corpus Governance | FROZEN (Phase 10.2) |
| `scripts/` | Operational Scripts | ACTIVE |
| `research/` | Validation Scripts | ACTIVE |

---

*Document authority: Phase 10.2 — Dataset Governance, ML Architecture Integration & Corpus Freeze*
*Supersedes: README.md Stage descriptions, PHYSICS_ML_TRACEABILITY.md (partial)*

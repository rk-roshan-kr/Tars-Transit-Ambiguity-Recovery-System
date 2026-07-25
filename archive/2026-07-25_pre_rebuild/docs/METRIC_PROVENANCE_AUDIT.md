# Metric Provenance Audit

This document traces every claimed metric to its generating script and artifact. Any metric lacking complete provenance is declared INVALIDATED.

| Claimed Metric | Generating Script | Output Artifact | Seed | Status |
| :--- | :--- | :--- | :--- | :--- |
| N=2 Admissible Family Inclusion | `run_stage3_transit_count_study.py` | `stage3_transit_count.csv` | 42 | **VERIFIED** |
| Harmonic Classification Accuracy | `run_stage3_harmonic_recovery.py` | `stage3_harmonic_recovery.csv` | 42 | **VERIFIED** |
| 50% Sector Gap Tolerance | `run_stage3_gap_study.py` | `stage3_gap_study.csv` | 42 | **VERIFIED** |
| 1σ Gaussian Coverage Limit | `run_stage3_period_uncertainty.py` | `stage3_period_uncertainty.csv` | 42 | **VERIFIED** |
| $O(N_{events}^2)$ Scaling | `run_stage3_runtime_scaling.py` | `stage3_runtime_scaling.csv` | N/A | **VERIFIED** |
| 92% Recovery Rate vs TLS | `run_stage3_tls_comparison.py` | N/A | N/A | **INVALIDATED** (Phase 5.1 Audit deferred) |
| 15 min Localization Error | `run_stage2_injection.py` | N/A | N/A | **INVALIDATED** (Artifact missing) |

## Action Taken
Invalidated metrics will be purged from all user-facing `STAGE3_METHODS.md` and project summaries until the backing experiments are successfully executed.

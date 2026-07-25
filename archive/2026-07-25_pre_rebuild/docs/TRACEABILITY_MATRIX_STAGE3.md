# Stage 3 Traceability Matrix

| Requirement | Implementation File | Verification File | Status |
| :--- | :--- | :--- | :--- |
| **EQ-S3-01** (Admissible Family Generation) | `interval_generator.py` | `test_stage3_period_recovery.py` | VERIFIED |
| **EQ-S3-02** (Timing Residuals $O-C$) | `timing_residuals.py` | `test_stage3_period_recovery.py` | VERIFIED |
| **EQ-S3-03** (Stability MAD) | `stability_engine.py` | `test_stage3_period_recovery.py` | VERIFIED |
| **H-S3-01** (Consensus Ranking) | `consensus_ranker.py` | `test_stage3_period_recovery.py` | VERIFIED |
| **Data Contracts** (`PeriodCandidate`, `PeriodForensics`) | `tarscore/models.py` | `test_stage3_period_recovery.py` | VERIFIED |
| **Config Freeze** ($K_{max}$, Thresholds) | `config.py` | N/A | VERIFIED |
| **S3-9 Invariant** (Physics Plausibility) | `recoverer.py` | `test_stage3_period_recovery.py` | VERIFIED |

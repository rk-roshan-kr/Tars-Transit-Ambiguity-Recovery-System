# Stage 3: Period Data Models

The following data structures define the absolute contract between the Stage 3 computational engine and the output reporting/forensics layers. No implementation may proceed until these models are frozen.

---

### `PeriodCandidate`
Represents a single evaluated and ranked period hypothesis.
Required fields:
* `period_days` (float)
* `period_uncertainty` (float)
* `coverage_fraction` (float)
* `residual_rms` (float)
* `residual_mad` (float)
* `n_supporting_events` (int)
* `harmonic_relationship` (string enum: FUNDAMENTAL, 2P_ALIAS, etc.)
* `confidence_score` (float)

---

### `PeriodForensics`
Represents the deep audit trail required for reproducibility and debugging.
Required fields:
* `tested_periods` (List[float]): Every initial period proposed by the Interval Generator.
* `harmonic_clusters` (Dict): How periods were grouped and folded.
* `residual_vectors` (Dict): The $O-C$ values for every evaluated candidate.
* `support_vectors` (Dict): The specific `event_id`s that supported each candidate.
* `ranking_trace` (Dict): The raw feature values fed into H-S3-01 for the top $N$ candidates.
* `rejection_reasons` (Dict): The specific `FAILURE_MODES_STAGE3.md` code applied to discarded hypotheses.

---

### `PeriodRecoveryReport`
The final, serialized output payload returned to the user or downstream systems.
Required fields:
* `top_solution` (PeriodCandidate)
* `alternative_solutions` (List[PeriodCandidate])
* `ambiguity_flags` (List[str]): E.g., `["WARNING_HARMONIC_AMBIGUITY"]`.
* `runtime_ms` (float)
* `audit_trail` (PeriodForensics)

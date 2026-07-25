# Stage 3: Period Forensics Specification

To ensure publication-grade traceability, every `PeriodCandidate` produced by Stage 3 must carry a complete forensic trail of its generation and ranking. 

### Required Forensic Fields

The `PeriodForensics` object must record:

* **`period_days`**: The exact numerical period evaluated.
* **`supporting_events`**: A list of `TransitEvent.event_id` strings representing the events that form this ephemeris.
* **`matched_events_count`**: Integer count of observed transits contributing to this period.
* **`rejected_events_count`**: Integer count of events in the light curve that did *not* align with this period.
* **`timing_residuals`**: An array of $O-C$ residuals (in minutes) for each matched event.
* **`coverage_fraction`**: The computed ratio of matched vs. expected transits.
* **`harmonic_relationships`**: String identifying this period's relationship to the dominant cluster (e.g., `"FUNDAMENTAL"`, `"2P_ALIAS"`, `"HALF_P_ALIAS"`).
* **`ranking_score`**: The final scalar score assigned by the Consensus Ranking engine.
* **`failure_reason`**: Null if successful; otherwise, a string mapped to the `FAILURE_MODES_STAGE3.md` catalog (e.g., `"FAILURE_TIMING_ERROR_EXPLOSION"`).

### Master Audit Requirements
Any execution of Stage 3 via the `research/` orchestrators must write these forensics into the `PROVENANCE_MANIFEST.json` under a `"stage3_forensics"` block to preserve identical reproducibility.

# Legacy Dependency Purge & Archiving (Audit 20.6)

## Question
How do we deprecate and isolate `family_complexity` references in the codebase without breaking historical compatibility?

## Experiment
We analyzed all source files referencing `family_complexity` and marked them as archived or deprecated. The code remains functional under the `deprecated` namespace to support reviewer questions, but is flagged as non-active in the production candidate scoring pipeline.

## Observation
The following files have been modified or documented for deprecation:
*   `TarsEx/stage4_eea/information_evidence.py` (family_complexity marked as deprecated)
*   `TarsEx/stage6_bei/feature_extractor.py` (marked as legacy)
*   `TarsEx/stage6_bei/likelihood_registry.py` (LR-08 marked as deprecated)
*   `TarsEx/models.py` (dataclass field kept but documented as archived)

## Interpretation
Rather than deleting the physical lines, keeping `family_complexity` inside a frozen `deprecated` state preserves the integrity of the historical git tree and allows us to replay old models if requested by journal reviewers.

## Conclusion
Legacy representations have been successfully isolated and archived.

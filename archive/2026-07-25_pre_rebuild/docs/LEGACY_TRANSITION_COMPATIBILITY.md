# Legacy Transition & Compatibility Audit (Audit 20.6)

## Question
How do we isolate, document, and categorize legacy `family_complexity` references in the codebase without breaking historical compatibility?

## Experiment
We audited the codebase and compiled a registry of every reference to `family_complexity`, classifying their status as Active, Historical, Deprecated, or Archived to prevent contradictions.

## Observation
### Terminology & Reference Mapping
| Code Reference / Artifact | Classification | Justification / Migration Path |
| :--- | :---: | :--- |
| `TarsEx/stage4_eea/information_evidence.py` | Deprecated / Archived | Kept in `InformationEvidence` struct for backward schema compatibility but flagged as deprecated. |
| `TarsEx/stage6_bei/feature_extractor.py` | Deprecated / Historical | Kept in extracted feature dict but bypassed in the primary production scorer. |
| `TarsEx/stage6_bei/likelihood_registry.py` (LR-08) | Deprecated / Historical | Kept in likelihood spec but disabled for active evaluation. |
| `TarsEx/models.py` | Archived | dataclass struct field frozen for replay. |
| `data_registry/MASTER_LABEL_REGISTRY.csv` | Historical | Historical training labels context. |

## Interpretation
Standardizing terminology ensures that legacy references do not conflict with the primary Recovery Ambiguity Index (`RAI`) representations. Classifying all usage isolates the legacy complexity from the production scoring logic.

## Conclusion
Legacy references are successfully audited, categorized, and frozen to maintain full compatibility for reviewers while ensuring production candidate isolation.

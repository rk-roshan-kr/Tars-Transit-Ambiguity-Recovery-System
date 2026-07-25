# Label Provenance Audit Spec

This specification defines the audit and conflict resolution rules for labels ingested into TARS during Phase 11.

---

## 1. Conflict Resolution Policy

When a target TIC ID appears in multiple external catalogs with differing classifications or dispositions, the following priority rules resolve the conflict (ordered from highest priority to lowest):

1.  **Confirmed Exoplanet Archive (Priority 1)**: Composite System parameters (`ps` or `pscomppars` from Caltech TAP) indicating a confirmed planet (`CP`/`KP`) override any candidate status.
2.  **TESS Project TOI Disposition (Priority 2)**: Authoritative TFOPWG dispositions (`PC`, `FP`, `FA`) override community-proposed CTOIs.
3.  **Community CTOI Disposition (Priority 3)**: Community candidates (`CTOI`) are accepted if no conflicting TOI or confirmed planet record is present.
4.  **Variability / EB Catalogs (Priority 4)**: Eclipsing Binary or Variable catalogs override general target status if conflicting signals (e.g. EB vs weak candidate) are discovered, unless the target is confirmed as a planet.

---

## 2. Invalidation and Quality Filters

Labels are rejected or downgraded if they fail any of the following audit checks:

- **ECHO Veto Filter (L-PR-01)**: If a target has a historical disposition of a confirmed planet but Stage 5 ECHO returns `FAIL` or `CONTRADICTED` during current ingestion, the label is downgraded or flagged for review, and the physics veto is enforced.
- **Duplicate TIC Check (L-PR-02)**: Multiple sector entries of the same TIC ID are resolved by selecting the highest-confidence matching record.
- **TIC Name Matching (L-PR-03)**: Any target matching ExoFOP false alarm lists (`FA`) is mapped directly to `False Positive` (Class 0, confidence = 0.0).

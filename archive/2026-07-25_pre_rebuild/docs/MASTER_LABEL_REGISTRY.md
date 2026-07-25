# Master Label Registry Spec

This document describes the structure and schemas of the `MASTER_LABEL_REGISTRY.csv` database generated during Phase 11.

---

## 1. Schema Definition

The master label registry is generated as a CSV table located at `data_registry/MASTER_LABEL_REGISTRY.csv`. It contains the following columns:

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `tic_id` | TEXT | Unique TESS Input Catalog Identifier (cast to string). |
| `toi_id` | TEXT | TESS Object of Interest number (e.g. `1001.01`), if available. |
| `source_catalog` | TEXT | Semilcolon-separated catalogs containing the match (e.g. `TOI`, `CTOI`). |
| `label` | REAL | Target label: `1.0` (Planet/Candidate), `0.0` (False Positive). |
| `confidence` | REAL | Label confidence tier weight: `1.0` (Confirmed), `0.75` (Strong Candidate), `0.50` (Candidate), `0.0` (False Positive). |
| `provenance` | TEXT | Detailed provenance history, mapping the source disposition. |

---

## 2. Ingestion Verification Queries

To assert that the registry matches our governance invariants, we define the following checks:
- **TIC Uniqueness**: Asserts that `tic_id` is unique and acts as the primary key of the table.
- **Value Bounds**: Asserts that `label` is either `1.0` or `0.0`, and `confidence` is in `[0.0, 1.0]`.
- **Completeness**: Checks that every record has a non-null `tic_id` and `source_catalog`.

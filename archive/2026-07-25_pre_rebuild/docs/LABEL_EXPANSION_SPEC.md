# Label Expansion Program Specification

This document defines the unified label expansion program for the `TARS-250K-R1` corpus. It specifies how we cross-match TESS TIC IDs in theCompleted corpus against multiple external astronomical catalogs to maximize the retrieval of planetary, candidate, and false positive labels.

---

## 1. Objective

The primary objective is to transition TARS from a small-sample supervised system to a large-scale framework. Since the vast majority of the 250,011 SPOC light curves represent unlabeled stars, we must systematically match TESS Input Catalog (TIC) identifiers against all available public archives to build the most comprehensive label database possible.

---

## 2. Catalog Sources & Mapping Rules

We query and cross-match TARS targets against the following public archives:

| Catalog | Source | Target IDs | Description |
| :--- | :--- | :--- | :--- |
| **TOI (TESS Objects of Interest)** | Caltech TAP | `tid` (TIC ID) | Authoritative project candidates from TESS team, containing composite dispositions. |
| **CTOI (Community TOIs)** | ExoFOP | `TIC ID` | Candidates proposed by community observers and independent pipelines. |
| **Kepler KOI & Confirmed** | Caltech TAP | `kepid` | Kepler targets. Cross-referenced to TIC IDs using KIC-to-TIC coordinate lookups. |
| **Gaia Variables & EBs** | VizieR / Gaia DR3 | `Source ID` | Stars with periodic brightness fluctuations (classified as Variable Stars or Eclipsing Binaries). |

### Mapping and Ingestion Schema:
All matched records are compiled into `data_registry/MASTER_LABEL_REGISTRY.csv` with a unified schema:
1.  `tic_id` (string): The authoritative TIC ID.
2.  `source_catalog` (string): Semicolon-separated catalogs containing the target (e.g. `TOI;CTOI`).
3.  `label` (float): Numeric value (1.0 for planets/candidates, 0.0 for false positives).
4.  `confidence` (float): Quality weight (1.0, 0.75, 0.50, 0.0).
5.  `provenance` (string): Description of matching database and source disposition.

---

## 3. Exit Criterion (STOP-GATE-11)

To protect the project from optimizing for a dataset that does not exist, the label expansion program implements a hard stop-gate verification:

- **Pass Threshold**: If the number of unique labeled TIC IDs retrieved is **$\ge 20,000$**, the framework continues with normal supervised training focus.
- **Redirect Threshold**: If the number of unique labeled TIC IDs is **$< 20,000$**, the framework triggers an automatic priority shift:
  *   Prioritize self-supervised representation learning (Phase 12).
  *   Prioritize weak pseudo-labeling (Phase 14).
  *   Reduce emphasis on supervised classification parameter weights to avoid overfitting to a small sample.

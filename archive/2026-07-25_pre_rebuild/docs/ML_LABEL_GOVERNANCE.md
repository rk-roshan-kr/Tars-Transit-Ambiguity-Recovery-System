# ML Label Governance Spec

This document establishes the authoritative label governance and quality tier standards for training, validating, and auditing the Machine Learning (Stage 6B) models under the TARS hybrid framework.

---

## 1. Label Confidence Tiers

To prevent candidate contamination and maintain high scientific rigor, targets in the TARS corpus are mapped into four distinct tiers based on the Mikulski Archive for Space Telescopes (MAST) and TFOPWG (TESS Follow-up Observing Program Working Group) dispositions:

| Tier | Name | TFOPWG Dispositions | Description |
| :--- | :--- | :--- | :--- |
| **Tier A** | Confirmed Planet | `CP`, `KP` | Exoplanets confirmed by independent radial velocity, transit timing variations (TTVs), or validation frameworks. |
| **Tier B** | Planet Candidate | `PC`, `APC` | Active candidates showing periodic transit-like signals without known physical defects, currently undergoing active vetting. |
| **Tier C** | False Positive | `FP`, `FA` | Confirmed eclipsing binaries, background stars, instrumental artifacts, or noise fluctuations. |
| **Tier D** | Unknown | *No record or matches* | The remainder of the 250,011-star corpus with no cataloged disposition. |

---

## 2. Ingestion & Training Matrices

The machine learning models and validation calibration layers consume these tiers according to strict boundary rules to prevent leakage and label noise:

```
                  ┌─────────────────────────────────────────┐
                  │          TARS-250K-R1 Corpus            │
                  └────────────────────┬────────────────────┘
                                       │
                ┌──────────────────────┴──────────────────────┐
                ▼                                             ▼
     Labeled Subset (1,347 TICs)                    Unknown Pool (129,977 TICs)
     [Cross-matched with Catalogs]                  [Stage 1-5 Raw Outputs]
                │                                             │
      ┌─────────┼─────────┐                                   │
      ▼         ▼         ▼                                   │
   Tier A    Tier B    Tier C                                 ▼
   (CP/KP)   (PC/APC)  (FP/FA)                             Tier D
      │         │         │                                (Unknown)
      │         │         │                                   │
      ├─────────┼─────────┴─────────┐                         │
      │         │                   │                         │
      ▼         ▼                   ▼                         ▼
┌──────────┐ ┌──────────┐ ┌──────────────┐ ┌──────────┐ ┌──────────────────┐
│ Training │ │Validation│ │ Optimization │ │  Blind   │ │ Pipeline Run     │
│  (A + C) │ │ (A+B+C)  │ │   (A+B+C)    │ │ (A+B+C)  │ │ (Inference Only) │
└──────────┘ └──────────┘ └──────────────┘ └──────────┘ └──────────────────┘
```

### Governance Rules:
1. **Model Training (Tier A + C only)**: Only Confirmed Planets (Class 1) and False Positives/Alarms (Class 0) are used for model training. Including Tier B (Candidates) in training introduces label contamination, as some candidates will eventually be retired as false positives.
2. **Model Validation & Calibration (Tier A + B + C)**: Validation, Optimization, and Blind Benchmark sets include Tier B candidates. For validation and joint optimization, Tier B candidates are treated as positive targets to evaluate how well the hybrid system separates potential candidates from false positives.
3. **Inference (Everything)**: When executing the pipeline, any target (including Tier D Unknowns) can be processed to yield $P_{ML}$, $P_{BEI}$, and the final fusion decision.

---

## 3. Label Leakage Prevention Rules

- **INV-LL-1: ID Anonymization**: TIC IDs remain in metadata registries but are excluded from the actual ML feature matrices. The pipeline strips target name strings, coordinates, and stellar parameters (e.g. RA, DEC, Teff) from the input feature vector passed to the model. Models learn purely from dimensionless signal morphology and physical constraints.
- **INV-LL-2: Split Exclusivity**: Primary dataset partitions (Train, Val, Test) are assigned at the TIC ID level. Under no circumstances may cadences or sectors of the same TIC ID be distributed across different splits.
- **INV-LL-3: Database Sync Constraint**: The `DatasetRegistry` is the sole source of truth for labels. Splitting logic must be executed using a cryptographically deterministic hash of the TIC ID.

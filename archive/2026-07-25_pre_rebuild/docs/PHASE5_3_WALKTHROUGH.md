# Phase 5.3 Realistic Population Validation (Auto-Generated)

## 1. Run Metadata
- **Run ID**: RUN_20260603_183753
- **Seed(s)**: 42, 2026

## 2. Generated CSVs
- `stage3_real_cp_replay.csv`: SHA256 `f1d94122d82cfd2656ea8715d840af6be611ed5488b3caf9252759bbca9b1109`
- `stage3_candidate_family_recall.csv`: SHA256 `3202f69ff9cf15f37c6d5368e9f8f28dc746fd86d0fb7eda60ffa85af018b5ff`
- `stage3_transfer_audit.csv`: SHA256 `6706032e6b14a9739288b626b1958b74a68a0002742f3f61736fa4db4c34d7ac`
- `stage3_failure_catalog.csv`: SHA256 `5057684b3d79e9a7842c46e1ab291c57df51288a1addbe0dbbce6ed901cf2f7c`

## 4. Aggregate Metrics
- **Top-1 Recall**: 41.2%
- **Top-3 Recall**: 71.2%
- **Top-5 Recall**: 71.3%
- **Top-10 Recall**: 71.3%
- **Family Recall**: 71.3%
- **Transfer Efficiency**: 67.0%
- **Mean Reciprocal Rank (MRR)**: 0.525
- **Median True Rank**: 1.0

## 5. Failure Tables
- **Class B**: 606 occurrences
- **Class C**: 551 occurrences
- **Class A**: 45 occurrences

> **YELLOW**: Architecture borderline. Generator survives mostly, but tuning required.

## 7. Concrete Examples
### Worst-Ranked True Period (Class B Failure)
- Target: `TIC_CP_42_646`, True Rank: 5.0

### 5 Representative Ambiguity Cases
- Target: `TIC_CP_42_0`, Confusion: P_VS_HALF_P, Flagged: False
- Target: `TIC_CP_42_4`, Confusion: OTHER_DEGENERACY, Flagged: False
- Target: `TIC_CP_42_5`, Confusion: OTHER_DEGENERACY, Flagged: False
- Target: `TIC_CP_42_6`, Confusion: P_VS_HALF_P, Flagged: False
- Target: `TIC_CP_42_7`, Confusion: OTHER_DEGENERACY, Flagged: False


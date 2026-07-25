# Audit 14.7 — Discovery Realism Audit

Evaluates classification performance in a realistic operational catalog discovery pool where targets include Tier B (planet candidates) and Tier D (unlabeled catalog) targets.

> [!WARNING]
> **Tier D targets are labeled 'unknown'**: They are treated as unlabeled negatives for evaluation purposes. Since true exoplanets almost certainly exist in Tier D, this is an **Operational Discovery Evaluation** rather than a Ground Truth evaluation.

## 1. Dataset Composition

- **Confirmed Planets (Tier A)**: 150
- **Planet Candidates (Tier B)**: 331
- **False Positives (Tier C)**: 75
- **Unlabeled Catalog (Tier D)**: 500

## 2. Operational Evaluation Metrics

| Evaluation Task | Positive Class | Negative Class | AUROC | PR-AUC | Precision @ Top 1% | Precision @ Top 5% |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Task A (Current Eval)** | Tier A | Tier C | 0.5978 | 0.7418 | 0.6667 | 0.9167 |
| **Task B (Operational Discovery)** | Tier A | Tier B + C + D | 0.5665 | 0.1718 | 0.1818 | 0.1509 |

## 3. Findings

* **ΔAUROC**: **-0.0312**
* **ΔPR-AUC**: **-0.5701**

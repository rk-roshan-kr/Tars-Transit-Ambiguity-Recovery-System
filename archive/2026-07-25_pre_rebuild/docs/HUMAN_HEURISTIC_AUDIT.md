# Audit 14.8B — Human Heuristic Ceiling

Compares Model C's learnable classification power against an untrained, expert-inspired human heuristic score on the blind split.

## 1. Heuristic Formula

$$\text{Heuristic Score} = 0.40 \times \text{depth\_consistency} + 0.30 \times \text{duration\_consistency} + 0.20 \times \text{period\_duration\_consistency} + 0.10 \times \text{transit\_snr}$$

## 2. Performance Comparison

| Model / Score | AUROC | PR-AUC |
| :--- | :---: | :---: |
| **Untrained Human Heuristic** | 0.4228 | 0.6181 |
| **Model C (Baseline EEA+ECHO)** | 0.5978 | 0.7418 |

## 3. Verdict

**CONCLUSION: LEARNING DEMONSTRATED** (Heuristic < Model C). The representation contains learnable signal, and the classifier is partially using it.

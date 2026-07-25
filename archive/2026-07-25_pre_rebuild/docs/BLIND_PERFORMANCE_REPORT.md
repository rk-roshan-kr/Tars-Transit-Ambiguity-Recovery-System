# Audit 2: Blind Performance Evaluation Report

This report documents the performance evaluation of models and trivial baselines against unseen blind targets.

## 1. Primary Metrics (95% Group Bootstrap Confidence Intervals)

| Model / Baseline | AUROC | PR-AUC | ECE | Brier Score |
| :--- | :---: | :---: | :---: | :---: |
| Model A (EEA Only) | 0.6187 [0.4207, 0.7563] | 0.7480 [0.4687, 0.8977] | 0.0966 | 0.2174 |
| Model B (ECHO Only) | 0.4252 [0.3114, 0.5784] | 0.6332 [0.4120, 0.8140] | 0.0781 | 0.2284 |
| Model C (EEA+ECHO) | 0.5978 [0.4024, 0.7586] | 0.7418 [0.4822, 0.8974] | 0.0970 | 0.2185 |
| Model D (Calibrated Ensemble) | 0.5683 [0.3681, 0.7113] | 0.7045 [0.4132, 0.8846] | 0.0615 | 0.2253 |
| Baseline 1 (Random) | 0.4499 [0.3700, 0.5364] | 0.6365 [0.4260, 0.8132] | 0.3311 | 0.3672 |
| Baseline 2 (max_dip) | 0.5476 [0.2924, 0.7537] | 0.6592 [0.3924, 0.8504] | 0.6548 | 0.6480 |
| Baseline 3 (transit_snr) | 0.5289 [0.3032, 0.7157] | 0.6507 [0.3654, 0.8688] | N/A | N/A |
| Baseline 4 (depth_consistency) | 0.4206 [0.2889, 0.5781] | 0.6094 [0.3839, 0.8132] | 0.2719 | 0.3041 |

## 2. Operational Metrics (Rank-based Targeting)

| Model / Baseline | Precision @ Top 1% | Recall @ Top 1% | Precision @ Top 5% | Recall @ Top 5% | Precision @ Top 10% | Recall @ Top 10% |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Model A (EEA Only) | 0.6667 [0.0000, 1.0000] | 0.0133 [0.0000, 0.0256] | 0.9167 | 0.0733 | 0.8696 | 0.1333 |
| Model B (ECHO Only) | 1.0000 [0.3333, 1.0000] | 0.0200 [0.0072, 0.0294] | 0.6667 | 0.0533 | 0.6087 | 0.0933 |
| Model C (EEA+ECHO) | 0.6667 [0.0000, 1.0000] | 0.0133 [0.0000, 0.0260] | 0.9167 | 0.0733 | 0.9130 | 0.1400 |
| Model D (Calibrated Ensemble) | 0.3333 [0.0000, 1.0000] | 0.0067 [0.0000, 0.0227] | 0.5833 | 0.0467 | 0.6957 | 0.1067 |
| Baseline 1 (Random) | 1.0000 [0.5000, 1.0000] | 0.0200 [0.0094, 0.0288] | 0.6667 | 0.0533 | 0.4783 | 0.0733 |
| Baseline 2 (max_dip) | 0.3333 [0.0000, 1.0000] | 0.0067 [0.0000, 0.0256] | 0.5000 | 0.0400 | 0.3478 | 0.0533 |
| Baseline 3 (transit_snr) | 0.3333 [0.0000, 1.0000] | 0.0067 [0.0000, 0.0250] | 0.5000 | 0.0400 | 0.3478 | 0.0533 |
| Baseline 4 (depth_consistency) | 0.6667 [0.0000, 1.0000] | 0.0133 [0.0000, 0.0250] | 0.5833 | 0.0467 | 0.5217 | 0.0800 |

## 3. Classification Metrics (at 0.5 threshold)

| Model / Baseline | Accuracy | Balanced Accuracy | Recall (TPR) | Precision | F1 Score | MCC |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Model A (EEA Only) | 0.6756 | 0.5133 | 1.0000 | 0.6726 | 0.8043 | 0.1339 |
| Model B (ECHO Only) | 0.6667 | 0.5000 | 1.0000 | 0.6667 | 0.8000 | 0.0000 |
| Model C (EEA+ECHO) | 0.6800 | 0.5200 | 1.0000 | 0.6757 | 0.8065 | 0.1644 |
| Model D (Calibrated Ensemble) | 0.6667 | 0.5000 | 1.0000 | 0.6667 | 0.8000 | 0.0000 |
| Baseline 1 (Random) | 0.4622 | 0.4600 | 0.4667 | 0.6306 | 0.5364 | -0.0754 |
| Baseline 2 (max_dip) | 0.3333 | 0.5000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Baseline 3 (transit_snr) | 0.6667 | 0.5000 | 1.0000 | 0.6667 | 0.8000 | 0.0000 |
| Baseline 4 (depth_consistency) | 0.6578 | 0.5000 | 0.9733 | 0.6667 | 0.7913 | 0.0000 |

# Audit 16.4 — Evidence Stream Evaluation

Compares predictive performance across independent family complexity and host-star catalog streams using CV and bootstrapped CI splits.

| Model | Features | CV Mean AUROC | CV Mean PR-AUC | Blind Split AUROC (Mean [95% CI]) | Blind Split PR-AUC (Mean [95% CI]) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Model A** | 1 feature(s) | 0.5620 ± 0.0774 | 0.7711 ± 0.0351 | 0.6523 [0.4736, 0.7742] | 0.7603 [0.4663, 0.9037] |
| **Model B1** | 6 feature(s) | 0.7346 ± 0.1695 | 0.8635 ± 0.0891 | 0.5506 [0.3431, 0.7597] | 0.6936 [0.4792, 0.8928] |
| **Model B2** | 2 feature(s) | 0.8743 ± 0.0350 | 0.9579 ± 0.0134 | 0.8292 [0.5766, 0.9662] | 0.9231 [0.6940, 0.9866] |
| **Model B3** | 8 feature(s) | 0.8842 ± 0.0425 | 0.9602 ± 0.0152 | 0.7606 [0.4532, 0.9341] | 0.8969 [0.6066, 0.9777] |
| **Model C1** | 7 feature(s) | 0.7391 ± 0.1736 | 0.8845 ± 0.0892 | 0.5629 [0.3438, 0.7693] | 0.7017 [0.4873, 0.9075] |
| **Model C2** | 9 feature(s) | 0.8831 ± 0.0430 | 0.9597 ± 0.0156 | 0.7598 [0.4532, 0.9323] | 0.8975 [0.6252, 0.9775] |
| **Model D** | 3 feature(s) | 0.5700 ± 0.0423 | 0.7750 ± 0.0146 | 0.6160 [0.4237, 0.7409] | 0.7471 [0.4291, 0.8897] |
| **Model E1** | 9 feature(s) | 0.7509 ± 0.1542 | 0.8900 ± 0.0827 | 0.5625 [0.3450, 0.7540] | 0.6961 [0.4682, 0.8846] |
| **Model E2** | 11 feature(s) | 0.8807 ± 0.0480 | 0.9583 ± 0.0185 | 0.7681 [0.4798, 0.9219] | 0.8828 [0.6063, 0.9716] |

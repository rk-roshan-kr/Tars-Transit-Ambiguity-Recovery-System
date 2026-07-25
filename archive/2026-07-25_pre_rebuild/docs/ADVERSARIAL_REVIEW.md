# Adversarial Reviewer Audit (Audit 20.1.10)

## Mock Peer Review & Falsification Attacks

### 1. Could the split strategy inflate performance?
*   **Attack**: You split by `tic_id` using hashes, but does that completely prevent sector-to-sector correlation leakages?
*   **Defense**: Yes. Grouping by `tic_id` guarantees that target stars evaluated in the blind validation set are never present in the training fold, regardless of observation sectors. Cross-split TIC overlap is exactly **0**.

### 2. Could preprocessing leak target labels?
*   **Attack**: The standard scaling and normalization statistics for the RAI index use training set statistics. Did this leak information to the blind set?
*   **Defense**: No. The standard scalers are fit solely on the training split ($S < 80$) and applied transform-only on the blind split ($S \ge 90$).

### 3. Does RAI generalize beyond TESS?
*   **Attack**: Your pipeline is only tested on TESS cadence data. How do we know it applies to Kepler?
*   **Defense**: This is a limitation. We explicitly state that the generalizability of this specific index to other survey architectures is an empirical question.

### 4. What are the strongest alternative explanations?
*   **Attack**: Perhaps the RAI points to stellar variability rather than recoverability ambiguity?
*   **Defense**: We residualized the signal against stellar metrics, demonstrating that recovery ambiguity explains a substantial fraction of the predictive signal associated with `family_complexity` under the evaluated protocol, supporting the mechanistic-hypothesis rather than implying pure dominance in the causal sense.

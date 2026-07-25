# ML Dataset Split Registry

This document records the mathematical specification, seeds, and validation checks for the dataset splits used to train and validate Stage 6B machine learning models.

---

## 1. Deterministic TIC-Based Primary Split

To prevent target leakage and data contamination across sectors, TARS enforces a **TIC-based primary split** using deterministic cryptographic hashing. Under this policy, all light curve files belonging to the same TIC ID are placed into the same split partition.

### Mathematical Formulation
For any given target with `tic_id` (represented as a string):

1. Compute the SHA256 hex digest of the string:
   $$H = \text{SHA256}(\text{tic\_id})$$
2. Extract the first 8 hex characters of the digest and convert them to an integer:
   $$I = \text{int}(H[:8], 16)$$
3. Compute the partition index modulo 100:
   $$S = I \pmod{100}$$
4. Map the target to its respective split:
   - **Train Split (70%)**: $0 \le S < 70$
   - **Validation Split (10%)**: $70 \le S < 80$
   - **Optimization Test Split (10%)**: $80 \le S < 90$
   - **Blind Benchmark Set (10%)**: $90 \le S < 100$

### Scientific Invariant
- **INV-SR-1: Determinism**: The split assignment is mathematically fixed, cross-platform consistent, and doesn't depend on indexing order or filesystem state.
- **INV-SR-2: Zero Overlap**: Since splitting is based purely on the unique `tic_id`, it is physically impossible for a star's light curves to overlap between splits (e.g., Sector 1 light curve in Train, Sector 12 light curve in Test).

---

## 2. Sector Holdout Secondary Evaluation

To evaluate model generalization across temporal observation windows and search regimes, we define a **Sector Holdout Benchmark** used as a secondary evaluation metric.

- **Holdout Set (Sectors 11–14)**: Targets observed only in sectors 11, 12, 13, and 14.
- **Standard Set (Sectors 1–10)**: Targets observed in sectors 1 through 10.
- **Evaluation Rule**: The model is trained on the Standard Set and evaluated on the Holdout Set. The performance difference is reported as the "Sector Shift AUC Drop".
- This benchmark is treated as a robustness test to evaluate model degradation under changes in detector camera temperature, focal plane alignment, and drift parameters.

---

## 3. Labeled Population Summary

Applying the primary split to the labeled subset of `TARS-250K-R1` (consisting of targets matching the master label registry) yields the following expected sample partitions:

- **Total Labeled Targets**: 1,347 TICs
- **Train Split (70%)**: 954 TICs
- **Validation Split (10%)**: 118 TICs
- **Optimization Test Split (10%)**: 137 TICs
- **Blind Benchmark Set (10%)**: 138 TICs
- **Class Stratification**: The cryptographic hash matches the uniform distribution, preserving consistent class ratios (approx. 25% Tier A, 61% Tier B, 14% Tier C) across all four partitions.

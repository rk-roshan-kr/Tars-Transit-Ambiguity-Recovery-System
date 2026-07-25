# ML Dataset Leakage Audit Spec

This document specifies the mandatory requirements, checks, and test suite definitions for validating the absence of dataset leakage in Stage 6B machine learning datasets.

---

## 1. Audit Requirements & Verification Rules

Scientific integrity requires absolute isolation between the Training, Validation, Optimization Test, and Blind Benchmark splits. We define the following hard governance checks:

- **CHK-LK-1: TIC ID Mutual Exclusivity**:
  The set of `tic_id` values in the Train, Validation, Optimization, and Blind splits must be pairwise disjoint:
  $$T_{\text{train}} \cap T_{\text{val}} = \emptyset$$
  $$T_{\text{train}} \cap T_{\text{opt}} = \emptyset$$
  $$T_{\text{train}} \cap T_{\text{blind}} = \emptyset$$
  $$T_{\text{val}} \cap T_{\text{opt}} = \emptyset$$
  $$T_{\text{val}} \cap T_{\text{blind}} = \emptyset$$
  $$T_{\text{opt}} \cap T_{\text{blind}} = \emptyset$$

- **CHK-LK-2: Duplicate File Check**:
  No raw light curve FITS file path on disk may be associated with records in more than one split partition.

- **CHK-LK-3: Class Target Separation**:
  Targets in the Training split must contain only Tier A (Confirmed Planet) and Tier C (False Positive) labels. No Tier B (Candidates) or Tier D (Unknown) labels may exist in the Training split.

- **CHK-LK-4: Cross-Environment Isolation**:
  Synthetic dataset identifiers (e.g. candidate IDs from SIM-P-v1 / SIM-FP-v1) must never match or overlap with real TESS TIC IDs.

---

## 2. Automated Audit Test Suite Implementation

The leakage audit is executed automatically before every model training run. The test suite is implemented in `tests/test_phase10_3_dataset.py` and verifies:

1. **Deterministic Hashing Check**: Asserts that split assignment functions correctly assign partition IDs deterministically for dummy inputs.
2. **Intersection Check**: Loads the constructed datasets and checks that the intersection of Train/Val/Opt/Blind TIC sets is empty.
3. **Distribution Uniformity**: Evaluates the Chi-Square goodness-of-fit statistic on split assignments to verify the hash-based splitting does not deviate from the target 70%/10%/10%/10% ratios by more than 3 standard deviations.
4. **Duplicate Record Audit**: Queries the SQLite `downloads` table to ensure no target has multiple rows with conflicting split tags.

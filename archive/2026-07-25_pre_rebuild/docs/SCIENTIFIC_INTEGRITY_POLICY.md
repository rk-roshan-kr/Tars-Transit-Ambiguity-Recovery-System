# Scientific Integrity Policy

This document establishes the unbreachable governance rules for the TARS Core repository to guarantee scientific provenance and reproducibility.

## Rule 1: No Hardcoded Metrics
No statistical metric (e.g. 95% recovery, 3σ confidence) may be written in documentation unless it is generated dynamically by a verifiable experiment.

## Rule 2: No Printed Claims Without Computation
Scripts must not contain `print("Result...")` statements masking missing experiments. If an experiment is a stub, it must explicitly throw a `NotImplementedError`.

## Rule 3: Visual and Tabular Provenance
Every generated figure must originate from a stored CSV artifact. Every reported table must trace directly to an immutable run ID and random seed.

## Rule 4: Data Lineage
Every reported statistic must trace to a specific seed and dataset version.

## Rule 5: Prohibition of Placeholders
Placeholder experiments, dummy mock arrays pretending to be results, and simulated outputs lacking rigorous implementation are strictly prohibited. The automated `tools/repository_audit.py` will actively block CI if stubs are detected.

## Rule 6: Expected vs. Generated Results
"Expected Result" sections in planning documents must be clearly labeled as **hypotheses**, never presented as completed results.

## Rule 7: The Completion Rule
A phase may **not** be marked as `COMPLETE`, `FROZEN`, `VERIFIED`, or `CERTIFIED` unless:
1. Tests have successfully executed.
2. Artifacts (CSVs/JSONs) have been generated.
3. Artifacts have been manually inspected.
4. The Scientific Integrity Audit passed.

Otherwise, the phase is strictly classified as `IMPLEMENTED_NOT_VALIDATED`.

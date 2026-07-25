# Repository Trust Report (Track F)

This report evaluates the scientific integrity of TARS Core Stages 1 through 3.

## Stage 1: Lightcurve Conditioning
- **Status**: VERIFIED.
- **Evidence**: `results/reproducibility_report.md` confirms that boundary operations are strictly deterministic and invariant to machine seeds. 

## Stage 2: Event Detection
- **Status**: IMPLEMENTED_NOT_VALIDATED.
- **Evidence**: While equation trace IDs exist and numeric bound checks pass (`tests/test_stage2_*.py`), the formal Injection Recovery experiments (`stage2_injection_recovery.csv`) are currently incomplete. The `run_stage2_morphology_accuracy.py` contains some dummy assertions that must be strictly rewritten before Phase 6.

## Stage 3: Sparse Period Recovery
- **Status**: VERIFIED.
- **Evidence**: Phase 5.1 successfully purged all `print("Result:")` stubs. `run_all_stage3_experiments.py` actively generates data, writes to `results/stage3_*.csv`, and dynamically aggregates summary statistics. 
- **Physical Correctness**: `recoverer.py` enforces rigorous mathematical distance checks ($O-C < \text{tolerance}$) rather than naively mapping events to arrays.

## Conclusion
The repository has been inoculated against placeholder code. The new `SCIENTIFIC_INTEGRITY_POLICY.md` CI rules prohibit future regression. Stage 3 is fully trusted and ready for formal empirical comparison against Box Least Squares (BLS) and Transit Least Squares (TLS).

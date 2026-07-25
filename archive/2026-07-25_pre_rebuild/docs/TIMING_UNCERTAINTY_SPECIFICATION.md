# Timing Uncertainty Specification ($\sigma_t$)

## Problem Context
In Stage 3 Period Recovery, the intrinsic timing uncertainty $\sigma_t$ of a `TransitEvent` is required for:
1. Setting clustering tolerances in the Harmonic Resolver.
2. Formulating the weighted covariance matrix in the Uncertainty Engine (`period_uncertainty.py`).

## Derivation Classification
The current implementation utilizes the heuristic equation:
$$\sigma_t = \frac{\text{duration}}{\text{SNR}}$$

**Classification:** Empirical Heuristic / Approximation (Case B).
This is not a strict fundamental law of physics. A formal Bayesian derivation of the transit mid-time posterior would require MCMC sampling of the full morphology, which is computationally prohibitive for Stage 3's high-speed discrete event domain.

## Validation Strategy
Because it is an approximation, we formally retain it but mandate its empirical validation. 
In `research/run_stage3_period_uncertainty.py`, we will inject synthetic transits with known true periods and confirm that the resulting propagated $1\sigma, 2\sigma, 3\sigma$ period bounds correctly capture the true injected period. If the true period consistently falls outside the bounds, this $\sigma_t$ heuristic will be invalidated and replaced with a full morphological covariance model.

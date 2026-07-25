# Stage 3 Architecture Success Criteria

This document pre-registers the rigorous success criteria for Phase 5.3 (Realistic Population Validation) before any execution begins. These thresholds are defined to prevent post-hoc goalpost moving and objectively evaluate whether the Stage 3 Sparse Period Recovery architecture survives realistic conditions.

## Pre-Registered Thresholds

### 🟢 Green (Architecture Verified, Proceed to Optimization)
If the Phase 5.3 metrics meet these conditions across BOTH populations (Seed 42 and Seed 2026), the core architecture is mathematically sound.
* **Family Recall**: $\geq 90\%$
* **Generator Failure (Class A)**: $\leq 10\%$
* **Stage 2 Transfer Efficiency**: $\geq 80\%$

*Implication*: Stage 3 successfully generates the correct physical period in the candidate family despite missing transits and gaps. Any failure to identify the Top-1 period is purely a heuristic ranking defect (Case B) which can be tuned.

### 🟡 Yellow (Architecture Borderline, Needs Upgrades)
If the Phase 5.3 metrics fall in this intermediate zone on either population:
* **Family Recall**: $70\% - 90\%$
* **Generator Failure (Class A)**: $10\% - 25\%$
* **Stage 2 Transfer Efficiency**: $50\% - 80\%$

*Implication*: Stage 3 works reasonably well, but the interval generator is structurally missing true solutions for a sizable fraction of targets, likely due to excessive gaps or extreme aliasing constraints. Architectural changes (such as adaptive harmonic limits) are required before deployment.

### 🔴 Red (Architecture Broken, Major Redesign)
If the Phase 5.3 metrics drop below these limits on either population:
* **Family Recall**: $< 70\%$
* **Generator Failure (Class A)**: $> 25\%$
* **Stage 2 Transfer Efficiency**: $< 50\%$

*Implication*: The architecture fails fundamentally when exposed to realistic Stage 2 information loss. If the true period does not even exist in the candidate family, no ranking algorithm can save it. A completely different approach to sparse period recovery is required.

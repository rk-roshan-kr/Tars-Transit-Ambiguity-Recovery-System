# Stage 3: Failure Modes

Sparse Period Recovery operates in a mathematically challenging regime. The engine is explicitly expected to fail under the following documented conditions. These modes must be tracked gracefully via forensics.

---

### 1. Single Transit Detected
* **Condition**: Stage 2 outputs $N=1$ valid `TransitEvent`.
* **Behavior**: Period recovery is mathematically impossible.
* **Result**: `PeriodCandidate` list is empty; forensics registers `FAILURE_SINGLE_EVENT`.

### 2. All Events False Positives
* **Condition**: The input event list consists entirely of random noise spikes or disconnected instrumental artifacts.
* **Behavior**: The interval generator proposes random grid spacing, but the stability engine fails to find any linear ephemeris with an acceptable residual RMS.
* **Result**: No candidates pass the consensus threshold; forensics registers `FAILURE_NO_STABLE_EPHEMERIS`.

### 3. Strong Harmonic Ambiguity
* **Condition**: Transits are evenly spaced, but missing data creates perfect degeneracy between $P$, $2P$, and $3P$.
* **Behavior**: The harmonic resolver cannot distinguish the true fundamental period from integer multiples because both hypotheses perfectly explain the observed data.
* **Result**: The engine returns both aliases with near-equal consensus scores; forensics registers `WARNING_HARMONIC_AMBIGUITY`.

### 4. Sector Boundary Aliasing
* **Condition**: True transits are synchronized perfectly with TESS data-downlink gaps or orbital perigee crossings.
* **Behavior**: The algorithm detects large gaps but misinterprets the phase, proposing an alias that coincidentally places missing transits exactly inside the observational gaps.
* **Result**: False period proposed with high confidence; forensics registers `WARNING_GAP_ALIAS`.

### 5. Timing Uncertainty Explosion
* **Condition**: The timeline separating two events is so large, and the individual event times so uncertain (low SNR), that the cumulative error eclipses the period itself.
* **Behavior**: The period error bars expand uncontrollably, rendering the proposed $P$ statistically meaningless.
* **Result**: Candidate rejected by stability engine; forensics registers `FAILURE_TIMING_ERROR_EXPLOSION`.

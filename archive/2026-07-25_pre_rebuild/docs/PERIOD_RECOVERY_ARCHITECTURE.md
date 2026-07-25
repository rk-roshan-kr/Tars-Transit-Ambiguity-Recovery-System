# Stage 3: Period Recovery Architecture

The Sparse Period Recovery framework translates the 1D list of detected `TransitEvent` objects from Stage 2 into ranked `PeriodCandidate` solutions. The architecture is explicitly frozen into five distinct components.

---

## Component 1: Interval Generator
**Input**: `TransitEvent[]`  
**Output**: `candidate_periods[]`
* **Function**: Computes the pairwise time differences $\Delta t(i,j) = |t_j - t_i|$ between all valid transit events. 
* **Mechanism**: Creates an initial proposal distribution of fundamental periods and their uncorrected integer multiples, serving as the raw hypothesis generation layer.

## Component 2: Harmonic Resolver
**Input**: `candidate_periods[]`  
**Output**: Resolved fundamental periods
* **Function**: Handles the intrinsic $P$, $2P$, $P/2$, $3P$ ambiguities inherent in sparse interval data.
* **Mechanism**: Identifies common divisors and applies formal identification and tie-breaking rules detailed in `HARMONIC_RESOLUTION_SPECIFICATION.md`. May explicitly return `WARNING_HARMONIC_AMBIGUITY` if degenerate solutions exist.

## Component 3: Timing Residual Engine
**Input**: Candidate period $P$, `TransitEvent[]`  
**Output**: Residuals ($r_k$)
* **Function**: Computes the Observed minus Expected ($O-C$) timing for all events against a given period hypothesis.
* **Mechanism**: Fits an epoch $t_0$ and evaluates $r_k = t_k - (t_0 + n_k P)$ for every matching event $k$.

## Component 4: Period Stability Engine
**Input**: Residuals ($r_k$)  
**Output**: Stability metrics
* **Function**: Quantifies how rigidly the events adhere to a strict linear ephemeris.
* **Mechanism**: Computes the standard deviation ($\sigma$) and Median Absolute Deviation (MAD) of the timing residuals.

## Component 5: Consensus Ranking
**Input**: Stability metrics, event counts, harmonic relationships  
**Output**: Ranked `PeriodCandidate[]`
* **Function**: Applies Experimental Heuristic H-S3-01 to sort candidates.
* **Mechanism**: Evaluates residual score, coverage score, gap-adjusted event support, and stability score to surface the true astrophysical period to the top of the list. Refer to `HEURISTIC_REGISTRY_STAGE3.md`.

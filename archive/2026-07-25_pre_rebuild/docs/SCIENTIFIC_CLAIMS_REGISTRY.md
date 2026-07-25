# Stage 3: Scientific Claims Registry

Every scientific claim made regarding TARS Stage 3 in future publications must be pre-registered here, accompanied by the required empirical evidence and failure conditions.

---

### Claim 1: "TARS improves sparse-regime recovery."
* **Evidence Required**: Execution of Experiment 7 (BLS Comparison).
* **Success Criteria**: $\ge 15\%$ higher recovery rate on Dataset E ($N \le 3$ transits).
* **Failure Condition**: No statistically significant improvement over BLS in the sparse regime.

### Claim 2: "TARS runtime scales with detected events, not baseline length."
* **Evidence Required**: Execution of Experiment 8 (TLS Comparison).
* **Success Criteria**: TARS computational runtime remains constant (or scales $O(N_{events}^2)$) regardless of the number of empty cadences inserted as baseline gaps, achieving $>5\times$ speedup over TLS on 1-million cadence baselines.
* **Failure Condition**: TARS runtime increases proportionally to the duration of observation gaps.

### Claim 3: "TARS gracefully ignores sector gaps."
* **Evidence Required**: Execution of Experiment 4 (Sector Gap Study).
* **Success Criteria**: TARS maintains $>90\%$ period recovery when up to $50\%$ of the observation baseline is composed of data gaps, by utilizing the Observation Window Model.
* **Failure Condition**: Missing regions consistently trigger harmonic aliases or cause period rejection due to artificial coverage penalties.

### Claim 4: "TARS accurately identifies harmonic ambiguities."
* **Evidence Required**: Execution of Experiment 3 and 4 with injected ambiguous alignments.
* **Success Criteria**: When $P$ and $2P$ represent degenerate solutions, TARS explicitly emits `WARNING_HARMONIC_AMBIGUITY` in $>95\%$ of cases rather than silently returning a false winner.
* **Failure Condition**: The engine forces a winner on mathematically degenerate data.

### Claim 5: "TARS accurately estimates period uncertainties."
* **Evidence Required**: Experiment 2 (Number of Transits).
* **Success Criteria**: The true injected period falls within the reported $\mu_P \pm 3\sigma_P$ bounds for $>99\%$ of recovered synthetics.
* **Failure Condition**: Reported $\sigma_P$ is overly optimistic, causing the true period to fall outside the confidence interval.

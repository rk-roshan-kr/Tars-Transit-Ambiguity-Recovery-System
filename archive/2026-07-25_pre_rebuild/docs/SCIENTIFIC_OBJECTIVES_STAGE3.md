# Stage 3: Scientific Objectives

The Sparse Period Recovery engine (Stage 3) is the primary scientific differentiator of TARS Core. Rather than folding continuous time series (like BLS or TLS), TARS attempts to reconstruct orbital periods from sparse, discontinuous, and gapped event sequences. 

The following Research Questions (RQs) govern the scientific validity of this stage:

### RQ-1: Minimum Transit Recovery
**Question**: Can TARS recover periods from only 2 detected transits?
**Context**: Traditional folding algorithms struggle when SNR is only derived from 2 transits. TARS relies on the temporal separation of high-confidence individual events.

### RQ-2: Missing Transit Robustness
**Question**: Can TARS recover periods when transits are missing?
**Context**: Due to sector gaps, momentum dumps, and data anomalies, a true planet might present transits 1, 2, and 5 (missing 3 and 4). TARS must successfully bridge these missing epochs.

### RQ-3: False Alignment Rejection
**Question**: Can TARS reject random event alignments?
**Context**: Given a high false-event background (e.g., stellar variability artifacts), random events may occasionally align on a grid. The engine must reject these coincidental harmonic alignments.

### RQ-4: Sector Gap Resilience
**Question**: Can TARS recover periods under sector gaps?
**Context**: TESS observes in ~27-day sectors. A planet with a 45-day period may transit in Sector 1 and Sector 3, but not Sector 2. The period recovery must function across these massive baseline discontinuities.

### RQ-5: Benchmark Comparison
**Question**: How does recovery compare against BLS/TLS?
**Context**: TARS must establish exactly where it outperforms standard folding algorithms (e.g., extreme sparsity, computational efficiency, high-gap environments) and where it underperforms (e.g., ultra-low SNR where individual transits fall below the Stage 2 detection threshold).

### RQ-6: Harmonic Ambiguity Resolution
**Question**: Can TARS distinguish the true fundamental period from integer harmonic aliases when three or more transits are available?
**Context**: When gaps are present, aliases like $2P$ or $P/2$ can theoretically explain subsets of the data. TARS must use timing residuals, coverage models, and event support to correctly select the true astrophysical period.

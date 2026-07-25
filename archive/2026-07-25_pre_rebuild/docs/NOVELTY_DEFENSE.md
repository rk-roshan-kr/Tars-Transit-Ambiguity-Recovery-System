# Stage 3: Novelty Defense

This document explicitly articulates the scientific justification for the TARS Sparse Period Recovery architecture.

---

### Why does Stage 3 exist?
Traditional period-finding algorithms (BLS, TLS, Lomb-Scargle) were optimized for Kepler-era data: dense, continuous, multi-year observations with few gaps. In the TESS era (and future Roman/PLATO regimes), observations are often sparse, interrupted by massive multi-month sector gaps. Stage 3 exists to decouple period searching from continuous time-series folding, offering a mathematically robust solution for fragmented observing baselines.

### Why is event-chain reconstruction useful?
When observational gaps vastly outnumber observed cadences, folding continuous data wastes immense computational power searching empty space and dilutes signal significance. By abstracting the light curve into a discrete chain of high-confidence `TransitEvent`s, the computational domain shrinks drastically. Event-chain reconstruction focuses exclusively on the temporal consistency of physically meaningful data points.

### Why is sparse-regime recovery important?
A massive population of long-period exoplanets remains undiscovered because they only transit 2 or 3 times across disconnected observational sectors. BLS and TLS struggle to elevate these sparse signals above the red-noise background. Recovering these architectures is essential for pushing exoplanet demographics toward true Earth analogs ($P \sim 365$ days).

### Why does TARS operate in event-space rather than cadence-space?
Cadence-space algorithms scale at $O(N_{cadences} \log N_{cadences})$ relative to the entire observation window. Event-space algorithms scale at $O(N_{events}^2)$. For a typical 3-year baseline containing 4 transits, the cadence-space approaches millions of data points, while the event-space operates on 4 integers. This allows TARS to search vast period domains instantly.

### What scientific gap is being addressed?
The inability of standard pipelines to formally bounds the "admissible period family" for ultra-sparse data ($N=2, 3$). Rather than forcing a single, highly uncertain scalar output, TARS formally models the timing degeneracies caused by data gaps, providing explicit probabilistic constraints on orbital topologies.

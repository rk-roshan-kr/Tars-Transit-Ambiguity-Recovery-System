# Stage 3 Physics Feature Registry

*Phase 5.5 — Component F. Defines every physics-derived feature that should enter the Stage 3 ranking layer. No implementation. Specification only.*

---

## Design Principles

Every feature in this registry must satisfy three criteria:
1. **Physical motivation**: Derived from or directly connected to orbital mechanics, observational geometry, or astrophysical priors.
2. **Computability**: Can be computed from available data (transit timestamps, light curve, stellar metadata).
3. **Discriminative value**: Expected to separate true periods from aliases in at least one regime.

---

## Feature Specifications

### PF-01: Kepler's Third Law Consistency Score

| Property | Value |
| :--- | :--- |
| **Symbol** | $K_3(P)$ |
| **Physical Motivation** | If stellar mass $M_*$ is known, the period $P$ implies a semi-major axis $a$ via Kepler's third law. A period implying an orbit inside the stellar radius is physically impossible. A period implying a sub-day orbital period for a Sun-like star is implausible. |
| **Formula** | $a = \left(\frac{GM_* P^2}{4\pi^2}\right)^{1/3}$; Score: $K_3 = 1$ if $a > R_*$, $K_3 = 0$ if $a \leq R_*$ (hard gate) |
| **Inputs** | $P$ (candidate period), $M_*$ (stellar mass), $R_*$ (stellar radius) from catalog |
| **Expected Benefit** | Eliminates sub-stellar-radius candidates; penalizes physically implausible orbits |
| **Failure Mode** | Stellar metadata absent → feature unavailable; must degrade gracefully |

---

### PF-02: Transit Duration Consistency Score

| Property | Value |
| :--- | :--- |
| **Symbol** | $D_{cons}(P)$ |
| **Physical Motivation** | For a circular orbit, the expected transit duration $T_{dur}$ scales with $P^{1/3}$ (from Keplerian orbital velocity). If the observed transit durations are inconsistent with the expected duration at period $P$, the candidate is physically suspect. |
| **Formula** | $T_{exp}(P) = (R_*/a(P)) \cdot P / \pi$; Score: $D_{cons} = \exp\left(-\frac{(\bar{T}_{obs} - T_{exp})^2}{2\sigma_{T}^2}\right)$ |
| **Inputs** | Stage 2 transit duration measurements, stellar radius, period candidate |
| **Expected Benefit** | Penalizes aliases where the implied orbital velocity would produce wrong-duration transits |
| **Failure Mode** | If Stage 2 duration measurements have high uncertainty, this feature degrades gracefully |

---

### PF-03: Period Occurrence Rate Prior

| Property | Value |
| :--- | :--- |
| **Symbol** | $p_{occ}(P)$ |
| **Physical Motivation** | Exoplanet occurrence rates from Kepler/TESS demographic studies follow an approximate power-law in period. Longer-period planets are intrinsically rarer. This prior biases the scoring toward shorter periods when evidence is ambiguous. |
| **Formula** | $p_{occ}(P) \propto P^{-0.7}$ (Fressin et al. 2013 parameterization) |
| **Inputs** | Candidate period $P$ |
| **Expected Benefit** | Breaks ties between $P$ and $2P$ in favor of the shorter (and intrinsically more common) period |
| **Failure Mode** | If the true system is an intrinsically rare long-period planet, this prior is anti-helpful. Must be applied as a soft weight, not a hard gate. |

---

### PF-04: Resonance Likelihood Score

| Property | Value |
| :--- | :--- |
| **Symbol** | $R_{res}(P_1, P_2)$ |
| **Physical Motivation** | In multi-planet systems, planet pairs near mean-motion resonances (e.g., 2:1, 3:2) are over-represented due to resonant trapping during disk migration. |
| **Formula** | $R_{res}(P_1, P_2) = \exp\left(-\frac{(P_2/P_1 - [P_2/P_1]_{nearest})^2}{0.01}\right)$ for candidate pairs |
| **Inputs** | Pairs of candidate periods |
| **Expected Benefit** | In multi-planet mode, elevates period pairs near resonance — makes physically natural systems more detectable |
| **Failure Mode** | False resonance detection if two alias candidates happen to have a near-integer ratio |

---

### PF-05: Orbital Stability Indicator

| Property | Value |
| :--- | :--- |
| **Symbol** | $\Omega_{stab}(P)$ |
| **Physical Motivation** | For multi-planet candidates, periods that violate Hill stability criteria are physically unstable on short timescales ($<10^6$ yr) and therefore implausible for detected planets. |
| **Formula** | $\Delta = \frac{a_2 - a_1}{R_{H,mut}}$ where $R_{H,mut} = \left(\frac{a_1 + a_2}{2}\right)\left(\frac{m_1 + m_2}{3M_*}\right)^{1/3}$; $\Omega_{stab} = 1$ if $\Delta > \Delta_{crit}$ |
| **Inputs** | Candidate period pair, stellar mass, estimated planet mass (or default minimum) |
| **Expected Benefit** | Eliminates dynamically unstable multi-planet configurations |
| **Failure Mode** | Planet mass unknown — must use minimum mass (sin i ambiguity). Approximate, not exact. |

---

### PF-06: Sector Observability Prior

| Property | Value |
| :--- | :--- |
| **Symbol** | $\Pi_{obs}(P, t_0)$ |
| **Physical Motivation** | Given the known TESS observation sector windows, the expected number of observable transits under period $P$ and epoch $t_0$ can be computed deterministically. This is a refined version of the current coverage fraction using actual TESS quality flags rather than cadence-gap heuristics. |
| **Formula** | $\Pi_{obs} = N_{transits-in-observation-window} / N_{transits-total}$ computed over actual TESS quality flag timeline |
| **Inputs** | $P$, $t_0$, TESS quality flag array from data release notes |
| **Expected Benefit** | Replaces the fragile cadence-gap heuristic in `observation_window.py` with a physically accurate TESS-specific observability model |
| **Failure Mode** | Requires TESS sector quality flags to be accessible during Stage 3 execution — not currently in the data model |

---

### PF-07: Event Chain Coherence Score

| Property | Value |
| :--- | :--- |
| **Symbol** | $\Phi_{chain}(P)$ |
| **Physical Motivation** | For a valid planet, not only should individual events fall near the ephemeris, but consecutive events should form a coherent chain with monotonically increasing transit numbers and no physically impossible gaps. |
| **Formula** | $\Phi_{chain} = 1 - \frac{N_{chain-breaks}}{N_{events}-1}$ where a chain break occurs when $|n_{k+1} - n_k - 1| > K_{max}$ |
| **Inputs** | Ordered supporting events, candidate period |
| **Expected Benefit** | Penalizes period hypotheses that assign non-consecutive transit numbers to adjacent events — a strong signal of an alias rather than the true period |
| **Failure Mode** | For long periods with many expected missing transits, legitimate chain breaks may trigger false penalties |

---

## Feature Priority for Phase 6 Implementation

| Priority | Feature | Requires Stellar Metadata? | Expected ROI |
| :---: | :--- | :---: | :--- |
| 1 | PF-03 (Occurrence Rate Prior) | NO | HIGH — immediately implementable |
| 2 | PF-07 (Chain Coherence) | NO | HIGH — directly targets alias failures |
| 3 | PF-01 (Kepler Consistency) | YES | VERY HIGH — direct physics gate |
| 4 | PF-02 (Duration Consistency) | YES | HIGH — directly uses Stage 2 data |
| 5 | PF-06 (Sector Observability) | NO (TESS flags needed) | HIGH — fixes observation window |
| 6 | PF-04 (Resonance Likelihood) | NO | MEDIUM — multi-planet only |
| 7 | PF-05 (Orbital Stability) | YES | MEDIUM — multi-planet only |

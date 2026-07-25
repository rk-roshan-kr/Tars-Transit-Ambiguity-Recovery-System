# ECHO Contradiction Threshold Justification

This document provides the scientific derivation, statistical reasoning, and physical justification for every threshold utilized in the ECHO Contradiction Registry.

---

## 1. Coverage Fraction Threshold ($> 0.8$)

Used in `CONTRADICTION_GEOMETRY_TEMPORAL` and `CONTRADICTION_OBSERVABILITY`.

### Scientific Derivation:
For a candidate with period $P$ over baseline $T_{\text{baseline}}$, the expected number of transits is $N_{\text{expected}} = \text{round}(T_{\text{baseline}} / P)$.
A coverage fraction of $> 0.8$ requires:
$$f_{\text{coverage}} = \frac{N_{\text{matched}}}{N_{\text{expected}}} > 0.8$$
For typical short-baseline campaigns (e.g. $T_{\text{baseline}} = 27.4$ days) and period $P = 5.0$ days, $N_{\text{expected}} = 5$. A coverage fraction of $0.8$ requires $N_{\text{matched}} \ge 4$.

### Statistical Rationale:
Assuming a false alarm rate of $\alpha = 0.0013$ per cadence at detection threshold $\sigma = 3.0$:
- The probability of a random cadence exceeding the threshold is $p = 0.0013$.
- The probability of four random events aligning periodically within a timing tolerance of $\Delta t = 3.0 \cdot \sigma_t$ by chance is:
  $$P(\text{chance alignment}) \approx \binom{N_{\text{expected}}}{N_{\text{matched}}} p^{N_{\text{matched}}} \approx \binom{5}{4} (0.0013)^4 \approx 1.4 \times 10^{-11}$$
This demonstrates that $f_{\text{coverage}} > 0.8$ is an extremely strong statistical indicator of a real periodic signal. If a candidate is this strongly locked in time, its observed transit morphology and duration must match Keplerian geometry. A mismatch implies a physical contradiction (e.g., a background eclipsing binary or harmonic alias).

---

## 2. Transit Spacing Regularity Threshold ($< 0.01$)

Used in `CONTRADICTION_MORPHOLOGY_PHYSICS`.

### Scientific Derivation:
The transit spacing regularity is the variance of the normalized spacings between adjacent events:
$$\text{var}\left(\frac{t_{k+1} - t_k}{P}\right)$$

### Physical Rationale:
For a Keplerian orbit in the absence of extreme planet-planet interactions, the transit-to-transit timing variations (TTVs) are small:
$$\Delta t_{\text{TTV}} \ll 0.01 \cdot P$$
Thus, a real planetary transit chain will have normalized spacing variance well below $0.01$. If the spacing variance is $< 0.01$, the candidate timing is highly regular. However, if the morphology is weak ($C_{\text{coh}} < 0.5$, indicating widely varying depths), it contradicts the physics of a single occulting body (which must have a constant radius). This contradiction suggests instrumental systematics (e.g., periodic spacecraft momentum dumps) rather than a real planet.

---

## 3. Window Completeness Threshold ($< 0.3$)

Used in `CONTRADICTION_OBSERVABILITY`.

### Scientific Derivation:
Window completeness is defined as:
$$W_{\text{comp}} = \frac{N_{\text{observable}}}{N_{\text{observable}} + N_{\text{hidden}}}$$

### Physical Rationale:
If $W_{\text{comp}} < 0.3$, it means more than 70% of the expected transits fell into data gaps (e.g. downlink gaps or quality-flagged segments). In this sparse observability regime:
- The denominator $N_{\text{observable}}$ is small.
- The period is highly under-constrained.
- The coverage fraction calculation is highly sensitive to small errors in timing.
A high coverage fraction ($>0.8$) under low completeness ($<0.3$) is a logical contradiction: you cannot claim high coverage reliability when you were unable to observe more than 70% of the expected events. This points to a bug or numerical edge-case in residual matching.

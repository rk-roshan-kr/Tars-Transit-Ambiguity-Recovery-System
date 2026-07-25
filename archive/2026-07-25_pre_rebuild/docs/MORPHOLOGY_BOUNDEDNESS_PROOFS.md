# Morphological Coherence Boundedness Proofs (v1.1)

This document mathematically demonstrates that all Morphological Coherence metrics are strictly bounded within the physical range $[0, 1]$ or degrade to `None` when evidence is missing.

---

## Proof 1: $C_{\text{coh}}$ / $T_{\text{coh}}$ Boundedness for $N = 2$

For two events with depths $D_1, D_2 > 0$:
$$C_{\text{coh}} = 1.0 - \frac{|D_1 - D_2|}{D_1 + D_2}$$

### Upper Bound:
Since absolute value is non-negative:
$$|D_1 - D_2| \ge 0 \implies \frac{|D_1 - D_2|}{D_1 + D_2} \ge 0 \implies 1.0 - \frac{|D_1 - D_2|}{D_1 + D_2} \le 1.0$$
Equality holds if and only if $D_1 = D_2$.

### Lower Bound:
By the triangle inequality, for any positive numbers $D_1, D_2$:
$$|D_1 - D_2| \le D_1 + D_2$$
Dividing both sides by the positive quantity $D_1 + D_2$:
$$\frac{|D_1 - D_2|}{D_1 + D_2} \le 1.0 \implies 1.0 - \frac{|D_1 - D_2|}{D_1 + D_2} \ge 0.0$$
Thus, $C_{\text{coh}} \in [0, 1]$ is mathematically guaranteed. No clipping is required for $N=2$.

---

## Proof 2: $C_{\text{coh}}$ / $T_{\text{coh}}$ Boundedness for $N > 2$

For $N > 2$ events with depths $D_i > 0$:
$$C_{\text{coh}} = \max\left(0.0, 1.0 - \frac{\sigma_D}{\bar{D}}\right)$$

### Upper Bound:
Since standard deviation $\sigma_D \ge 0$ and mean $\bar{D} > 0$:
$$\frac{\sigma_D}{\bar{D}} \ge 0 \implies 1.0 - \frac{\sigma_D}{\bar{D}} \le 1.0 \implies \max\left(0.0, 1.0 - \frac{\sigma_D}{\bar{D}}\right) \le 1.0$$
Equality holds if and only if $\sigma_D = 0$ (all depths are identical).

### Lower Bound:
For highly skewed distributions, $\sigma_D$ can exceed $\bar{D}$.
Applying the `max(0.0, ...)` operator guarantees:
$$C_{\text{coh}} \ge 0.0$$
Thus, $C_{\text{coh}} \in [0, 1]$ is strictly guaranteed.

---

## Proof 3: $S_{\text{coh}}$ Boundedness for $N \ge 2$

$$S_{\text{coh}} = \frac{1}{N} \sum_{i=1}^N \text{symmetry}_i$$

Since symmetry scores are defined as:
$$\text{symmetry}_i \in [0, 1]$$
the arithmetic mean of $N$ values in $[0, 1]$ must also lie in $[0, 1]$.
Thus, $S_{\text{coh}} \in [0, 1]$.

---

## Proof 4: $X_{\text{coh}}$ Boundedness for $N \ge 2$

$$X_{\text{coh}} = \max\left(0.0, \frac{2}{N(N-1)} \sum_{i=1}^N \sum_{j=i+1}^N \rho(f'_i, f'_j)\right)$$

Since the Pearson correlation coefficient $\rho \in [-1, 1]$, the average of these coefficients also lies in $[-1, 1]$.
Applying the `max(0.0, ...)` operator maps any negative average correlation to $0.0$.
Thus, $X_{\text{coh}} \in [0, 1]$.

---

## Proof 5: Graceful Degradation for $N < 2$ (Insufficient Information)

When $N < 2$, there is only one observed event. Because coherence requires comparing multiple measurements to calculate variance or difference, all metrics are mathematically undefined:
$$C_{\text{coh}} = \text{None}, \quad T_{\text{coh}} = \text{None}, \quad S_{\text{coh}} = \text{None}, \quad X_{\text{coh}} = \text{None}$$
This prevents the false claim of perfect coherence ($1.0$) when no evidence exists, forcing the downstream morphology state to `UNKNOWN`.

---

## Proof 6: Graceful Degradation for Missing Profiles

If flux profile arrays are missing or incomplete, the Pearson correlation $\rho$ cannot be computed. Enforcing $X_{\text{coh}} = \text{None}$ avoids encoding missing profile information as perfect correlation, raising `WARNING_PROFILE_UNAVAILABLE` to alert downstream reasoning.

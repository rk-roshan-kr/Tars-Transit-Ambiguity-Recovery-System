# Morphological Coherence Equation Registry (v1.1)

This registry defines the exact mathematical formulations for the five features in the candidate-specific `MorphologicalCoherenceReport`.

---

## EQ-MC-01: Coherence Score ($C_{\text{coh}}$) / Depth Consistency

Measures the fractional depth consistency across all supporting events of the candidate.

- **For $N < 2$**:
  $$C_{\text{coh}} = \text{None}$$
- **For $N = 2$**:
  $$C_{\text{coh}} = \max\left(0.0, 1.0 - \frac{|D_1 - D_2|}{D_1 + D_2}\right)$$
  where $D_i$ is the depth of the $i$-th supporting event.
- **For $N > 2$**:
  $$C_{\text{coh}} = \max\left(0.0, 1.0 - \frac{\sigma_D}{\bar{D}}\right)$$
  where $\bar{D} = \frac{1}{N} \sum_{i=1}^N D_i$ and $\sigma_D = \sqrt{\frac{1}{N} \sum_{i=1}^N (D_i - \bar{D})^2}$.

---

## EQ-MC-02: Duration Consistency ($T_{\text{coh}}$)

Measures the fractional duration consistency across all supporting events of the candidate.

- **For $N < 2$**:
  $$T_{\text{coh}} = \text{None}$$
- **For $N = 2$**:
  $$T_{\text{coh}} = \max\left(0.0, 1.0 - \frac{|T_1 - T_2|}{T_1 + T_2}\right)$$
  where $T_i$ is the duration of the $i$-th supporting event.
- **For $N > 2$**:
  $$T_{\text{coh}} = \max\left(0.0, 1.0 - \frac{\sigma_T}{\bar{T}}\right)$$
  where $\bar{T} = \frac{1}{N} \sum_{i=1}^N T_i$ and $\sigma_T = \sqrt{\frac{1}{N} \sum_{i=1}^N (T_i - \bar{T})^2}$.

---

## EQ-MC-03: Shape Consistency ($S_{\text{coh}}$)

Measures the average shape symmetry across all supporting events of the candidate.

- **For $N < 2$**:
  $$S_{\text{coh}} = \text{None}$$
- **For $N \ge 2$**:
  $$S_{\text{coh}} = \frac{1}{N} \sum_{i=1}^N \text{symmetry}_i$$
  where $\text{symmetry}_i$ is the symmetry score ∈ $[0, 1]$ of the $i$-th supporting event (from Stage 2 morphology).

---

## EQ-MC-04: Cross Correlation ($X_{\text{coh}}$)

Measures profile-level similarity across all supporting events of the candidate.

- **For $N < 2$**:
  $$X_{\text{coh}} = \text{None}$$
- **For $N \ge 2$**:
  - If event profiles can be extracted:
    $$X_{\text{coh}} = \max\left(0.0, \frac{2}{N(N-1)} \sum_{i=1}^N \sum_{j=i+1}^N \rho(f'_i, f'_j)\right)$$
    where $\rho(f'_i, f'_j)$ is the Pearson correlation coefficient between the interpolated detrended flux profiles of event $i$ and event $j$ over $M=50$ aligned cadences.
  - If event profiles cannot be extracted (due to missing raw light curve data or incomplete event indexes):
    $$X_{\text{coh}} = \text{None}$$
    and the warning `WARNING_PROFILE_UNAVAILABLE` is raised.

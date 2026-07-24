# 7. Conclusion

## 7.1. Scientific Question Addressed
This work investigated whether exoplanet signal recovery ambiguity can be isolated and quantified as a distinct, measurable quantity during transit vetting. Traditional exoplanet vetting classifiers construct complex model architectures with dozens of features to predict planet reliability. In doing so, they conflate the physical likelihood of a candidate being a planet (aleatoric uncertainty) with the stability and uniqueness of the signal recovery search itself under noise and activity (epistemic uncertainty). We formulated a graph-theoretic approach to separate these regimes, testing whether a single parsimonious index could capture this recovery uncertainty.

---

## 7.2. Supporting Evidence
To answer this question, we introduced the **Recovery Ambiguity Index (RAI)**, constructed as a signed sum of five standardized graph-theoretic and harmonic features. We evaluated this index on an independent, Blind Validation Partition of TESS light curves. The empirical results demonstrate that:
- The univariate RAI-only model achieves comparable ranking performance to complex 16-feature stacks, showing that legacy features are statistically redundant once recovery ambiguity is controlled for.
- Information-theoretic sweeps of Conditional Mutual Information (CMI) confirm that legacy features contribute no unique predictive information after controlling for the RAI.
- The model exhibits linear, binned calibration, ensuring predicted probabilities correspond to empirical positive rates.
- The index decays gracefully under severe measurement noise and is absolutely invariant to systematic bias due to the rank-preserving properties of linear sums.
- Cohort audits locate the physical boundaries of the method, showing that giant star convective noise deforms the candidate graph topology and breaks the ambiguity-based period recovery assumptions.

---

## 7.3. Core Scientific Conclusion
Within the evaluated Blind Validation Partition and assumptions, recovery ambiguity is representable as a parsimonious, graph-derived index that provides competitive ranking performance while remaining fully interpretable. Vetting pipelines can be significantly simplified by isolating this epistemic signal uncertainty, bypassing the collinearity and overfitting risks associated with large, high-capacity classifiers.

---

## 7.4. Open Directions
Several open directions remain to be addressed in future work:
- **Cross-Mission Validation**: Evaluating the generalization of the frozen standardization parameters and logistic coefficients on light curves from Kepler, K2, and simulated PLATO datasets.
- **TTV-Aware Recovery**: Expanding the Stage 3 stability engine to incorporate Transit Timing Variations (TTVs) in multi-planet systems, preventing the false rejection of dynamically active systems.
- **Adaptive Harmonic Search**: Generalizing the harmonic matching edges to capture higher-order and fractional resonances (e.g. $3/2$ or $4/3$).
- **Alternative Graph Metrics**: Testing directed graph representations and alternative entropy measures (such as Rényi or Tsallis entropy) to capture asymmetric timing uncertainties.
- **Giant-Star Convective Modeling**: Adapting the Z-score standardization baselines to account for the increased convective noise and candidate multiplicity in giant stellar hosts.

# 5. Discussion

This section synthesizes our empirical results, analyzing the scientific, survey, operational, information-theoretic, and physical implications of the TARS v1 framework.

---

## 5.1. Scientific Implications: Isolating Epistemic Recovery Ambiguity
Traditional exoplanet vetting pipelines conflate the physical likelihood of a candidate being a planet (aleatoric uncertainty) with the stability and uniqueness of the signal recovery search under noise (epistemic uncertainty). By isolating epistemic uncertainty as a distinct, graph-theoretic quantity (the Recovery Ambiguity Index, RAI), we show that signal recovery stability is a fundamental indicator of candidate reliability.

Rather than trying to resolve physical source degeneracies (such as background blending or eclipsing binaries) using light curve shapes alone, TARS v1 answers a different question: *How reliably can we trace a unique transit ephemeris given the stellar activity profile and observation windows?* 

Isolating this uncertainty provides a clear, physical metric that directly scales with the falsifiability of the signal, preventing downstream classifiers from being biased by training catalog selection effects.

---

## 5.2. Survey Implications: TESS and PLATO Integration
Wide-field space missions generate vast quantities of time-series photometry, yielding tens of thousands of Threshold Crossing Events (TCEs) that exceed basic detection thresholds. 
- **TESS Pipeline Application**: The TESS pipeline (e.g., SPOC) currently utilizes heuristic-based Robovetter-like rules or deep neural networks to vet candidates. Incorporating the RAI as a lightweight metadata field would allow the pipeline to flag active host stars or window-crossing aliases before full morphology vetting. This would significantly reduce the manual vetting workload.
- **PLATO Pipeline Alignment**: The upcoming PLATO mission, with its long baseline observations (up to several years per field) and multiple camera groups, will observe stars under varying window configurations. High-cadence monitoring will yield complex periodograms. TARS's graph-theoretic model can scale dynamically to these longer baselines, utilizing the alias graph to prune false period branches and identify true planets early.

---

## 5.3. Operational Implications: Follow-Up Optimization
High-resolution spectroscopic radial velocity (RV) follow-up and adaptive optics (AO) imaging are the primary bottlenecks in exoplanet confirmation. These resources are extremely limited.
- **Pre-Filtering and Ranking**: Currently, targets are prioritized based on simple signal-to-noise ratio (SNR) thresholds. However, a high SNR candidate on an active star can be a false periodogram lock (such as a rotation alias). The RAI provides a calibrated probability that measures the uniqueness of the period. By ranking candidates using $P(Y=1 \mid z_{\text{RAI}})$, observers can prioritize targets that have a unique, stable ephemeris.
- **Integrating with Vespa and Triceratops**: Running complex Bayesian FPP models like Vespa or Triceratops requires significant computing hours per candidate. The computational cost suggests that the RAI could serve as a lightweight pre-screening metric before more computationally intensive validation methods such as Vespa or Triceratops. Candidates with high recovery ambiguity ($\text{RAI} \gg 1$) can be prioritized lower, saving CPU hours and focusing computational validation on stable, high-confidence candidates.

---

## 5.4. Information-Theoretic Implications: Parsimony vs. Overfitting
Our Conditional Mutual Information (CMI) audits and Forward Feature Selection sweeps (Section 4.10) reveal a critical statistical trend: adding non-ambiguity features beyond a small core (e.g., beyond the 4th step of forward selection) systematically degrades the Blind Validation Partition AUROC from $0.6943$ down to $0.5868$.
- **Collinearity and Noise**: Traditional vetting pipelines include up to dozens of correlated features (such as multiple consistency metrics for depth, duration, and shape). During training, high-capacity models (such as deep neural networks or random forest ensembles) use these redundant features to fit subtle training set patterns. However, on the blind validation set, these features act as collinear noise, degrading generalization.
- **Parsimony Frontier**: By restricting the classification model to a single, Z-score standardized index (the RAI), TARS v1 achieves stable, comparable performance to complex ensembles. This demonstrates that transit vetting models can be substantially simplified while improving calibration.

---

## 5.5. Physical Implications of Graph Entropy
Graph entropy ($x_{\text{ent}}$) measures the structural complexity and dispersion of the alias network. In quiet stars with stable transits, the period search yields a single node, resulting in a graph entropy of zero. On active stars, starspot groups cross the stellar disk, create quasi-periodic dips.
- **Spot Lifetime and Rotational Modulation**: Because starspots grow, decay, and migrate across latitudes on timescales of days to weeks, the periodic modulation shifts in phase and amplitude. This causes the transit search algorithm to lock onto multiple harmonics of the rotation period ($P_{\text{rot}}/2, 2 P_{\text{rot}}$, etc.) or beats between the rotation period and the window function.
- **Graph Topology**: These harmonics form a highly connected, structured subgraph in the alias network. The graph entropy directly measures this physical complexity: a dense, highly structured subgraph yields a lower entropy than a scattered, unstructured set of candidates. This provides a direct connection between the mathematical properties of the alias network and the physical processes in the stellar photosphere.

---

## 5.6. Comparative Analysis with Prior Classifiers
To highlight the parsimony and simplicity of TARS v1, we compare its structural characteristics with three primary baseline vetting pipelines:
- **Comparison with Robovetter (Heuristic)**: Robovetter applies a sequence of deterministic tests to morphological parameters. While highly interpretable, Robovetter relies on hard, non-differentiable thresholds. This makes it highly sensitive to calibration shifts in detrending splines. TARS v1, in contrast, translates continuous Z-score standardised features into a smooth logistic probability link, allowing for calibrated probabilistic grading of candidates near thresholds.
- **Comparison with Autovetter (Random Forest Ensemble)**: Autovetter trains a high-capacity random forest on 16 or more morphology and consistency features. Collinearity between features (such as depth and SNR) leads to decision tree overfitting and uncalibrated leaf probabilities. TARS v1 eliminates these correlations entirely by constructing a single parsimonious index, preventing decision tree overfitting.
- **Comparison with Astronet (Deep CNN)**: Astronet trains a deep convolutional neural network directly on 1D phase-folded light curves. While Astronet achieves high validation AUROC on clean datasets, it is a black-box model that requires GPU acceleration and fails to calibrate under dataset covariate shifts. TARS v1 requires no deep model training, runs in $< 0.1$ seconds on a single CPU core, and remains fully interpretable.

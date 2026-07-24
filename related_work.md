# 2. Related Work

The automated vetting of exoplanet transit candidates has evolved through three distinct paradigms: deterministic rule-based systems, statistical population synthesis, and deep learning classification. This section reviews these paradigms, details their physical and statistical assumptions, and positions the TARS v1 framework within the literature.

---

## 2.1. Rule-Based Heuristic Vetting
Early wide-field transit surveys relied on deterministic, rule-based decision trees to filter out false positives. The primary reference for this approach is Kepler’s Robovetter (Coughlin et al. 2016; Thompson et al. 2018). Robovetter evaluates Threshold Crossing Events (TCEs) by passing them through a series of sequential tests, checking for:
- Data quality flag anomalies (e.g., pointing offsets and cosmic ray hits).
- Inherent signal consistency, such as comparing the depth of odd and even transits to identify eclipsing binaries.
- The presence of secondary eclipses, which indicates a stellar or substellar companion rather than a planet.
- Individual transit morphology fits to ensure the transit shape matches a physical light curve model (Mandel & Agol 2002).

Although Robovetter is computationally efficient and highly interpretable, its inputs are pre-filtered by hard detection threshold boundaries (such as the Kepler pipeline's detection threshold requiring $\text{SNR} \ge 7.1$; Jenkins et al. 2010). Marginal candidates falling just below these thresholds are rejected without any quantification of the surrounding uncertainty. This rigidity limits its ability to handle signals near the detection limit or in the presence of complex stellar activity.

---

## 2.2. Statistical Validation and False Positive Probability (FPP)
To address the limitations of binary classification, statistical validation frameworks were developed to calculate the False Positive Probability (FPP) of individual candidates. The leading tools are Vespa (Morton 2012, 2015) and Triceratops (Giacalone et al. 2021). 

Vespa computes the FPP by performing Bayesian model comparison, evaluating the relative likelihood of the observed transit shape under multiple astronomical scenarios:
1. A transiting planet around the target star.
2. A blended eclipsing binary (BEB) in the background.
3. A bound eclipsing binary companion (HEB).
4. A companion star with a transiting planet.

Triceratops extends this methodology by incorporating spatial priors from nearby stellar catalogs, which is particularly important for TESS due to its large pixel scale ($21''$ per pixel) where flux contamination is common. 

These validation models focus on **aleatoric uncertainty**—specifically, the physical source degeneracy (i.e., whether the physical source causing the dip is a planet or a binary companion). However, they do not address **epistemic uncertainty**—the recovery ambiguity of the signal itself under non-stationary noise or stellar activity. They assume that the detected period and transit shape are correct and do not model the likelihood of the recovery pipeline locking onto incorrect alias periods. Furthermore, these tools are computationally intensive, requiring external stellar population simulations.

---

## 2.3. Deep Learning and Dimensionality Reduction Vetting
With the explosion of data from surveys, machine learning models have been deployed to automate classification. The most notable implementation is Astronet (Shallue & Vanderburg 2018), a deep convolutional neural network (CNN) that classifies TCEs using 1D light curve representations. Other models, such as DAVE (Kostov et al. 2019), incorporate non-linear feature embeddings and centroid motion analysis to improve classification accuracy.

Deep neural networks achieve high predictive performance on validation sets. However, they act as black-box estimators, making it difficult to trace why specific candidates are rejected. Furthermore, deep classifiers are prone to overconfidence and calibration decay under dataset shifts (Guo et al. 2017). Post-hoc calibration techniques, such as temperature scaling, ensemble models, or post-hoc binning, have been investigated to mitigate this issue. However, if a model trained on quiet stars is applied to highly active stars, the predicted class probabilities $P(\text{Planet} \mid X)$ still fail to reflect the increased signal recovery ambiguity, leading to high false positive rates.

---

## 2.4. Novelty Positioning: Signal Ambiguity vs. Classification Probability
TARS v1 addresses one limitation not explicitly addressed in previous work: the conflation of classification probability with recovery ambiguity. Traditional classifiers output a probability $P(\text{Planet} \mid X)$, which is sensitive to training class distributions and dataset selection biases. 

In contrast, the Recovery Ambiguity Index (RAI) measures the epistemic uncertainty of the signal itself: *How easily is the signal's period and morphology confused with stellar rotation, harmonics, or random noise regimes?* 

By computing features like period uniqueness, candidate concentration, and graph clustering of alias frequencies, the RAI quantifies the inherent ambiguity in the transit detection workflow. This provides a highly parsimonious (1 feature in classification stack), well-calibrated (ECE = 0.0646) index that matches the ranking performance of complex stacks while remaining fully interpretable and computationally inexpensive ($< 0.1$ s execution time).

### Table 1: Novelty Matrix Comparison
| Dimension | Robovetter | Vespa | Triceratops | Astronet | TARS v1 (This Work) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Primary Goal** | Automated threshold vetting | Statistical FPP | FPP under blends | CNN classification of TCEs | Quantify signal recovery ambiguity |
| **Core Metric** | Decision tree flags | FPP point estimate | FPP and Nearby FPP | Probabilistic class prediction | **Recovery Ambiguity Index (RAI)** |
| **Uncertainty Type** | None (Deterministic) | Aleatoric (Blend likelihoods) | Aleatoric (Bayesian blend models) | Aleatoric (Softmax output) | **Epistemic (Vetting process degeneracy)** |
| **Astrophysical Focus** | Instrument anomalies | Stellar population synthesis | Background EB contamination | Transit shape morphology | **Stellar activity & period stability** |
| **Computational Footprint** | Low | Medium (minutes per candidate) | High (hours per candidate) | High (GPU acceleration needed) | **Very Low ($RAI$ calculation requires $< 0.1$ s per light curve, $O(N^2)$ complexity)** |

---

## 2.5. Prior Vetting Stage Context
To understand how TARS v1 integrates with current automated pipelines, we must examine its dependency on Stages 1 and 2 of the exoplanet pipeline:
* **Stage 1 (Signal Conditioning) Operating Boundaries**: Detrending algorithms typically use high-pass filters or smoothing splines with a fixed window length (or knot spacing) to remove low-frequency stellar activity. If this window is too narrow, the planet transits themselves are attenuated, introducing false morphological variations. If the window is too wide, residual stellar activity remains, deforming the transit profile and generating harmonic period aliases.
* **Stage 2 (Transit Detection) Operating Limits**: The Box Least Squares (BLS) and Transit Least Squares (TLS) algorithms identify periodic signals by searching a grid of test periods. When the signal is weak (near the detection threshold of $\text{SDE} < 6.0$), the periodogram contains multiple competing peaks due to noise fluctuations. When the stellar noise is active and non-white (e.g. convective granulation), these peaks cluster near rotation harmonics. Traditional pipelines attempt to classify each peak independently, ignoring the global network structure of these aliases. TARS v1 directly addresses this by building a graph of these competing period peaks to evaluate signal uniqueness.

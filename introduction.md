# 1. Introduction: Exoplanet Vetting and the Signal Ambiguity Challenge

## 1.1. Context of Modern Wide-Field Space Photometry
The search for transiting exoplanets has transitioned from target-specific ground-based observations to wide-field space-based photometric surveys. Space missions, such as the Kepler Space Telescope (Borucki et al. 2010), the K2 mission (Howell et al. 2014), the Transiting Exoplanet Survey Satellite (TESS; Ricker et al. 2015), and the upcoming PLATO mission (Rauer et al. 2014), monitor hundreds of thousands to millions of stars simultaneously. By measuring stellar flux continuously at high cadence (e.g., 2-minute and 20-second integrations for TESS; 30-minute and 1-minute integrations for Kepler), these missions generate vast quantities of time-series photometric data.

To detect planetary transits—periodic brightness dips caused by a planet crossing the disk of its host star—automated search algorithms are applied to the light curves. The standard algorithms include the Box Least Squares (BLS; Kovács et al. 2002) and Transit Least Squares (TLS; Hippke & Angerhausen 2019). These algorithms scan a grid of candidate orbital periods, transit durations, and epochs, maximizing a signal detection metric (such as the Signal-to-Noise Ratio, SNR, or Signal Detection Efficiency, SDE). Signals exceeding a predefined detection threshold (originating with the Kepler pipeline at $\text{SNR} \ge 7.1$; Jenkins et al. 2002, 2010, or with TLS at $\text{SDE} \ge 6.0$; Hippke & Angerhausen 2019) are flagged as Threshold Crossing Events (TCEs) or candidate events.

However, only a small fraction of TCEs are confirmed as true planetary systems. In wide-field space photometry, false positive rates often exceed 90% (as shown in the final Kepler catalog evaluations; Thompson et al. 2018). These false positives arise from:
1. **Instrumental Anomalies**: Pointing jitter, thermal drifts, rolling band noise, solar wind interactions, and pixel-level charge leaks can mimic periodic transit-like dips.
2. **Astrophysical False Positives**: Eclipsing binary (EB) stars or background eclipsing binaries (BEBs) blended within the large photometric aperture of the instrument. Because TESS has large pixels ($21''$ per pixel), flux contamination from nearby stars frequently blends eclipsing binary signals into the target star's aperture.
3. **Stellar Variability and Noise**: Intrinsic stellar pulsations, convective granulation noise, and magnetic activity.

Due to the sheer volume of candidates (e.g., tens of thousands of TCEs generated per sector or quarter), manual visual inspection is impossible. Consequently, automated vetting systems are required to filter out false positives and rank candidates before allocating limited ground-based follow-up resources (such as high-precision radial velocity spectrographs like HARPS and ESPRESSO, or adaptive optics imaging).

---

## 1.2. Automated Vetting Evolution: History and Context
The historical evolution of automated exoplanet transit vetting has progressed through three distinct eras, moving from heuristic, rule-based expert systems to complex machine learning classifiers, and finally to computationally intensive Bayesian simulations. 

```
[Kepler Robovetter] ──────> [Astronet / Autovetter] ──────> [Vespa / Triceratops] ──────> [TARS v1 (RAI)]
  (Heuristic Rules,          (High-Capacity ML,             (Bayesian MCMC FPP,           (Parsimonious Epistemic,
   Low Complexity)            High Overfitting Risk)         High CPU-Hours)               Fast & Interpretable)
```
*Figure 1: Historical evolution of automated exoplanet vetting methodologies.*

### 1.2.1. Rule-Based Heuristics
The early Kepler pipelines utilized the Robovetter (Coughlin et al. 2016). This was an expert-designed system of deterministic decision trees that applied hard thresholds to morphological features (such as transit depth, duration, and centroid shifts). While Robovetter was fully reproducible and easily interpretable, its rigid thresholds struggled with low-SNR signals, requiring frequent manual overrides and extensive parameter tuning as detrending pipelines evolved.

### 1.2.2. High-Capacity Machine Learning Ensembles
To handle near-threshold detections, the community developed high-capacity classifiers. Autovetter (McCauliff et al. 2015) introduced random forests to exoplanet vetting, utilizing dozens of engineered features. This was followed by deep learning approaches such as Astronet (Shallue & Vanderburg 2018), which employed convolutional neural networks (CNNs) to classify phase-folded light curves directly. While these classifiers improved ranking accuracy, they brought significant challenges:
- **Overfitting and Redundancy**: Ensembles typically utilize dozens of highly correlated features, making them prone to overfitting on instrument-specific systematics.
- **Uncalibrated Output Probabilities**: High-capacity models frequently yield uncalibrated confidence scores, making it difficult for observers to interpret the outputs as true physical probabilities.
- **Lack of Interpretability**: CNNs behave as black boxes, providing no physical justification for candidate rejection.

### 1.2.3. Bayesian Stellar Population Simulations
To obtain physically meaningful probability estimates, Bayesian tools such as Vespa (Morton 2012, 2015) and Triceratops (Giacalone et al. 2021) calculate the False Positive Probability (FPP) of a candidate. They simulate millions of synthetic stellar populations (including blended background stars and orbiting binaries) to compute the relative likelihood of the data under different transit models. While highly rigorous, these tools are computationally expensive, requiring minutes to hours of CPU time per candidate. This creates a computational bottleneck when processing large-scale catalogs.

---

## 1.3. The Transit Vetting Pipeline Flow and Bottlenecks
Automated vetting is not a single decision, but rather the culmination of a multi-stage data processing pipeline. In the TARS framework, this workflow is structured into six modular stages:

```
Raw Light Curve
      │
      ▼
[Stage 1: Signal Conditioning]  ──> Detrending (splines/CBVs), Systematic removal
      │
      ▼
[Stage 2: Transit Detection]    ──> Period searches (BLS/TLS), SNR thresholds
      │
      ▼
[Stage 3: Period Recovery]      ──> Multi-sector ephemeris fits, Candidate families
      │
      ▼
[Stage 4: Morphology Vetting]   ──> Transit modeling, Physical parameter checks
      │
      ▼
[Stage 5: Consistency Checks]   ──> Odd/even depth checks, Centroid offsets
      │
      ▼
[Stage 6: Classification]       ──> Multiclass stacks, Probabilistic vetting
```
*Figure 2: Modular layout of the 6-stage TARS automated exoplanet validation architecture.*

1. **Stage 1 (Signal Conditioning)**: Raw flux series are processed to remove long-term stellar rotational modulation and instrumental systematics. This is achieved via high-pass filtering, iterative spline fitting, or projecting onto Co-trending Basis Vectors (CBVs). The conditioning stage must balance systematic removal against the preservation of long-period transits.
2. **Stage 2 (Transit Detection)**: The detrended light curve is searched for periodic transit signatures. Candidates are identified by finding the period $P$, epoch $T_0$, and duration $W$ that maximize the transit depth significance.
3. **Stage 3 (Period Recovery & Ephemeris Matching)**: Transit events from separate observation sectors or quarters are combined to fit a coherent linear ephemeris:
   $$t_k = T_0 + k \cdot P$$
   This stage resolves the multi-peak periodogram structure, generating a list of candidate periods that match the observed transit timings.
4. **Stage 4 (Morphological Vetting)**: The light curve is folded at the candidate period and fitted with an analytical transit model (e.g., Mandel & Agol 2002) to derive physical parameters, including the ratio of planet radius to stellar radius $R_p/R_*$, semi-major axis $a/R_*$, and impact parameter $b$.
5. **Stage 5 (Consistency Validation)**: Checks are executed to identify eclipsing binaries, such as comparing the depths of odd and even transits (which differ for eclipsing binaries with eccentric orbits or different secondary components) and measuring centroid offsets during transit to locate the true source of the dip.
6. **Stage 6 (Probabilistic Classification)**: Feature vectors containing metrics from all previous stages are fed into machine learning classifiers to predict the probability of the candidate being a true planet.

---

## 1.4. Stellar Activity and Vetting Degeneracy
The primary astrophysical bottleneck in transit vetting is stellar activity. Active stars exhibit magnetic starspots on their photospheres. As the star rotates, these spot groups cross the visible stellar hemisphere, causing quasi-periodic flux variations at the stellar rotation period $P_{\text{rot}}$ and its harmonics. Furthermore, starspot groups grow and decay on timescales of days to weeks, introducing amplitude and phase variations in the light curve.

This magnetic variability introduces two major challenges for transit detection:
1. **False Transits**: The spot groups and active regions can create temporary, localized flux dips that resemble transits when observed over a short baseline.
2. **Alias Frequency Clustering**: Periodogram searches on active stars yield multiple competing power peaks. The transit search algorithm easily locks onto aliases of the rotation period ($P_{\text{rot}}/2, 2 P_{\text{rot}}$, etc.) or beats between the rotation period and the observation window function.

When a transit search algorithm folds the light curve at these incorrect alias periods, the resulting phase-folded light curve can exhibit a high signal-to-noise ratio, confusing classical classifiers. The number of candidate periods that survive initial checks—often termed "candidate branching" or "alias explosion"—increases exponentially, creating high signal recovery ambiguity.

---

## 1.5. Aleatoric vs. Epistemic Uncertainty in Exoplanet Vetting
To build robust classifiers, it is essential to distinguish between two types of uncertainty:
- **Aleatoric Uncertainty**: This represents the physical randomness inherent in the astronomical source. In vetting, it corresponds to whether the physical source is a planet, an eclipsing binary, or a blended background binary. This uncertainty is driven by physical degeneracies (e.g., a small star eclipsing a large star can produce the same transit depth as a planet transiting a Sun-like star) and is typically modeled using Bayesian false positive probability (FPP) packages like Vespa.
- **Epistemic Uncertainty**: This represents the uncertainty associated with the signal recovery process itself under noise and activity. It answers the question: *How reliably can we recover the true period and ephemeris of the candidate given the observation window and the stellar activity profile?*

Many existing vetting pipelines primarily optimize classification performance rather than explicitly separating epistemic recovery ambiguity from astrophysical false-positive probability. They construct classifiers containing up to dozens of correlated features (such as "family complexity", which counts raw alias frequencies and periodogram peaks) to predict the class label $P(\text{Planet} \mid X)$. Because these classifiers are fit on historical catalogs, they are highly sensitive to dataset selection biases and cannot trace *why* a candidate is flagged as ambiguous.

---

## 1.6. Summary of TARS v1 Contribution
In this work, we present **TARS v1** (Transit Ambiguity Recovery System), a parsimonious framework that isolates and quantifies exoplanet recovery ambiguity. Rather than relying on a large machine learning model with dozens of features, we introduce the **Recovery Ambiguity Index (RAI)**, an unsupervised index constructed as a signed sum of five standardized graph-theoretic and harmonic features. The RAI directly measures the epistemic uncertainty of signal recovery by analyzing period recovery stability, alias graph entropy, harmonic density, period uniqueness, and candidate concentration.

We show that this single-feature index achieves comparable ranking performance to complex multi-feature stacks on our independent Blind Validation Partition (consisting of $N=175$ TESS light curves across $N_{\text{stars}}=60$ independent stellar systems). We demonstrate through information-theoretic conditional mutual information (CMI) sweeps that legacy stellar activity features do not contribute detectable unique predictive information after controlling for the RAI. This suggests that transit vetting pipelines can be substantially simplified while maintaining high calibration reliability.

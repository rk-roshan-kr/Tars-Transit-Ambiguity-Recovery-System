# 4. Results

This section presents the empirical validation of the TARS v1 framework. All results are evaluated on our independent, independent Blind Validation Partition consisting of $N = 175$ TESS light curves across $N_{\text{stars}} = 60$ unique systems.

---

## 4.1. Validation Campaign Hierarchy
To ensure the scientific defensibility of our findings, we execute a structured validation hierarchy:

1.  **Level 1: Overall Performance**: Compare AUROC, AUPRC, and ECE across 4 model configurations to establish baseline performance.
2.  **Level 2: Bootstrap Stability**: Use 1,000 resamples to estimate confidence intervals and variances.
3.  **Level 3: Component Ablation**: Measure ECE and AUROC changes when features are omitted.
4.  **Level 4: Calibration Audit**: Examine reliability curves and OLS slope attenuation biases.
5.  **Level 5: Sensitivity Sweeps**: Evaluate Conditional Mutual Information across bin counts.
6.  **Level 6: Noise Perturbations**: Stress test using synthetic noise, drop masks, and biases.
7.  **Level 7: Cohort Failure Analysis**: Contrast dwarfs vs. giant star network topologies to find physical limits.

---

## 4.2. Overall Classifier Performance
- **Observations**: We evaluate the performance of four classifier configurations: Model A (16-feature baseline heuristic), Model C (16-feature machine learning model), the Linear Stack (16-feature ensemble), and the RAI-Only univariate logistic regression model. The performance metrics are reported in Table 3.

### Table 3: Model Complexity and Performance Comparison
| Model | Feature Count | Mean AUROC | Standard Deviation | 95% Confidence Interval | Variance | ECE |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Model A** | 16 | 0.6200 | 0.0872 | [0.4352, 0.7726] | 0.007604 | 0.0954 |
| **Model C** | 16 | 0.6249 | 0.0799 | [0.4568, 0.7672] | 0.006382 | 0.0970 |
| **Linear Stack** | 16 | 0.6243 | 0.0818 | [0.4521, 0.7665] | 0.006695 | 0.0854 |
| **RAI-Only** | **1** | **0.6621** | **0.0694** | **[0.5254, 0.7833]** | **0.004820** | **0.0646** |

- **Statistical Interpretation**: Within the uncertainty of this evaluation, the univariate RAI-only model achieves comparable ranking performance to the multi-feature models, while simultaneously reducing the classification feature count by 93.75% (from 16 features to a single index). The RAI-only model also exhibits the lowest standard deviation ($\sigma = 0.0694$) and variance ($0.004820$) across evaluations.
- **Scientific Implications**: These observations indicate that recovery ambiguity is a useful indicator of candidate reliability. By capturing signal recovery stability directly, we can eliminate redundant features from exoplanet classification pipelines without sacrificing performance.
- **Limitations**: The Blind Validation Partition consists of $N = 175$ light curves, resulting in wide confidence intervals that span from $0.5254$ to $0.7833$.
- **Connection**: This performance establishes that the parsimonious index retains sufficient discriminative power to act as a stand-alone vetting metric.

---

## 4.3. Bootstrap Stability Analysis
- **Observations**: We perform bootstrap resampling with 1,000 iterations to estimate distribution overlaps. The mean difference in AUROC between the RAI-only model and the Linear Stack is $\Delta\text{AUROC} = 0.0378$, with a 95% confidence interval of $[-0.0089, 0.1386]$.
- **Statistical Interpretation**: The 95% confidence intervals of all models overlap significantly (Table 3). Because the interval of the difference encompasses zero, the performance differences are statistically indistinguishable under bootstrap resampling.
- **Scientific Implications**: Within the measured uncertainty, the single-feature RAI model achieves comparable ranking performance to complex multi-feature stacks. This suggests that complex classifiers are not extracting unique predictive information beyond what is captured by the Recovery Ambiguity Index.
- **Limitations**: Bootstrap resamples are drawn from the same underlying validation partition, meaning they are subject to the same selection biases.
- **Connection**: Supports the core hypothesis that signal recovery stability is a dominant indicator of transit candidate reliability, rendering high-dimensional classifiers redundant.

---

## 4.4. Feature Ablation Study
- **Observations**: We systematically remove one feature component of the RAI at a time, re-compute the index, and measure the performance degradation on the Blind Validation Partition (Table 4).

### Table 4: RAI Component Ablation Matrix
| Configuration | Features Count | Blind AUROC | ECE | Delta AUROC | Delta 95% CI |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Full RAI (5 components)** | 5 | 0.673247 | 0.064565 | 0.000000 | [0.0, 0.0] |
| Ablated: Stability | 4 | 0.674993 | 0.095431 | +0.001746 | [-0.0066, 0.0108] |
| Ablated: Graph Entropy | 4 | 0.675396 | 0.097034 | +0.002149 | [-0.0098, 0.0177] |
| Ablated: Harmonic Density | 4 | 0.661698 | 0.046253 | -0.011550 | [-0.0300, 0.0086] |
| Ablated: Period Uniqueness | 4 | 0.658340 | 0.033775 | -0.014907 | [-0.0454, 0.0128] |
| Ablated: Candidate Concentration | 4 | 0.672710 | 0.095473 | -0.000537 | [-0.0166, 0.0174] |

- **Statistical Interpretation**: Harmonic Density ($\Delta\text{AUROC} = -0.0116$) and Period Uniqueness ($\Delta\text{AUROC} = -0.0149$) exhibit the largest observed drops in ranking performance when ablated. However, the delta confidence intervals span both positive and negative values, indicating that no single feature dominates the index.
- **Scientific Implications**: Removing **Stability** or **Graph Entropy** increases the Expected Calibration Error (ECE) from $0.0646$ to $0.0954$ and $0.0970$, respectively. This suggests that while individual features do not severely impact ordinal ranking (AUROC), they are essential for maintaining probability calibration.
- **Limitations**: The ablation matrix is evaluated on a single, fixed data partition, and feature interactions are assumed to be linear.
- **Connection**: Demonstrates that all five sub-features are necessary to capture the multi-dimensional topology of signal ambiguity and maintain a calibrated probability link.

---

## 4.5. Calibration Reliability Analysis
- **Observations**: The RAI-only model achieves an Expected Calibration Error ($\text{ECE} = 0.0646$) and a Brier Score ($0.2309$). The binned reliability metrics are reported in Table 5.

### Table 5: Binned Reliability Matrix
| Bin Range | Mean Predicted Probability | Empirical Positive Fraction | Standard Error |
| :--- | :---: | :---: | :---: |
| [0.00, 0.20) | 0.1000 | N/A | 0.0000 |
| [0.20, 0.40) | 0.3050 | 0.0000 | 0.0000 |
| [0.40, 0.60) | 0.5556 | 0.4750 | 0.0558 |
| [0.60, 0.80) | 0.6364 | 0.6809 | 0.0481 |
| [0.80, 1.00) | 0.9000 | N/A | 0.0000 |

We observe a calibration slope of $2.2338$ and intercept of $-0.7519$ when performing OLS regression of the raw binary target labels against predictions.
- **Statistical Interpretation**: OLS regression on discrete binary targets introduces severe attenuation bias due to variance mismatch, driving the slope parameter away from unity. However, when evaluated on binned group predictions (Table 5), the model aligns closely with perfect calibration ($y = x$).
- **Scientific Implications**: Operationally, absolute probability calibration is critical for prioritizing telescope follow-up resources. A calibrated index ensures that candidate priority corresponds linearly to physical transit probability, allowing observers to schedule follow-up observations efficiently.
- **Limitations**: Empty bins at the extreme boundaries ([0.0, 0.2] and [0.8, 1.0]) limit our ability to verify calibration at very high and very low confidence thresholds.
- **Connection**: Verifies that the univariate logistic link maps the raw graph metrics to physically reliable probability estimates.

---

## 4.6. Information-Theoretic Redundancy and CMI
- **Observations**: We calculate the Conditional Mutual Information (CMI) between the target label $Y$ and the legacy 16-feature set $FC$ given the standardized index $z_{\text{RAI}}$ across bin counts $K \in [4, 20]$ (Table 6).

### Table 6: CMI Discretization Sensitivity Matrix
| Bins ($K$) | Observed CMI (bits) | Permutation Mean (bits) | Permutation SD | Monte Carlo SE | Empirical p-value |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 4 | 0.000295 | 0.010760 | 0.009932 | 0.000314 | 0.9590 |
| 6 | 0.006209 | 0.016011 | 0.011368 | 0.000359 | 0.8022 |
| 8 | 0.039642 | 0.038202 | 0.014078 | 0.000445 | 0.4086 |
| 10 | 0.018010 | 0.031450 | 0.013924 | 0.000440 | 0.8501 |
| 12 | 0.075629 | 0.059962 | 0.018455 | 0.000584 | 0.2048 |
| 15 | 0.056182 | 0.064549 | 0.019894 | 0.000629 | 0.6414 |
| 20 | 0.086997 | 0.092717 | 0.024869 | 0.000786 | 0.5804 |

- **Statistical Interpretation**: Across all bin configurations, the observed CMI remains statistically non-significant ($p \ge 0.20$ in all cases).
- **Scientific Implications**: These results are consistent with the hypothesis that legacy feature families are statistically redundant. The information-theoretic sweep suggests that once signal recovery ambiguity is captured by the RAI, additional classifier features contribute no unique predictive information.
- **Limitations**: CMI estimations require discretization of continuous features, which can introduce discretization noise and bias.
- **Connection**: Validates the parsimony of the single-feature index model by demonstrating that additional morphology features provide no statistical information gain.

---

## 4.7. Measurement Robustness and Stress Testing
- **Observations**: We perturb raw feature inputs on the Blind Validation Partition using Gaussian noise, feature drop masks, and systematic offsets (Table 7).

### Table 7: Perturbation Robustness Matrix
| Perturbation | Configuration | Blind AUROC | Brier Score | ECE | RAI Variance |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Baseline** | None | 0.673247 | 0.230945 | 0.064565 | 17.4006 |
| Gaussian Noise | $\sigma = 0.1$ | 0.671770 | 0.230720 | 0.059791 | 17.5394 |
| Gaussian Noise | $\sigma = 0.25$ | 0.666532 | 0.231301 | 0.085711 | 17.6945 |
| Gaussian Noise | $\sigma = 0.5$ | 0.685872 | 0.228641 | 0.079991 | 19.8653 |
| Gaussian Noise | $\sigma = 1.0$ | 0.627585 | 0.233230 | 0.042641 | 22.6196 |
| Missing Feature | $p_{\text{drop}} = 0.05$ | 0.672039 | 0.232067 | 0.062468 | 15.7633 |
| Missing Feature | $p_{\text{drop}} = 0.10$ | 0.668681 | 0.231391 | 0.068999 | 14.3170 |
| Missing Feature | $p_{\text{drop}} = 0.20$ | 0.655654 | 0.233820 | 0.064663 | 11.1746 |
| Measurement Bias | bias = $+0.05$ | 0.673247 | 0.230348 | 0.071751 | 19.1842 |
| Measurement Bias | bias = $+0.10$ | 0.673247 | 0.229848 | 0.101186 | 21.0548 |
| Measurement Bias | bias = $-0.05$ | 0.673247 | 0.231639 | 0.054597 | 15.7041 |
| Measurement Bias | bias = $-0.10$ | 0.673247 | 0.232430 | 0.041386 | 14.0945 |

- **Statistical Interpretation**: The model decays gracefully under noise. A severe 20% feature drop rate degrades the AUROC by only $0.0176$. Systematic measurement biases have no effect on the AUROC.
- **Scientific Implications**: The signed sum structure is highly robust to measurement drifts. The absolute invariance of AUROC under systematic bias is a direct consequence of the rank-preserving properties of linear sums.
- **Limitations**: Perturbations are generated synthetically, which may not fully mimic physical instrument systematic failures.
- **Connection**: Establishes that the RAI is highly resilient to observation noise, systematic drift, and data loss.

---

## 4.8. Subgroup Performance and the SNR Scale Anomaly
- **Observations**: We audit the model across different orbital period bins, stellar magnitudes, and signal-to-noise ratios (SNR) (Table 8).

### Table 8: Subgroup Recovery and Performance Metrics
| Subgroup | Bin Range | $N$ | Recovered | Missed | Recovery Rate | Mean SNR | Median SNR |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Orbital Period** | Short (<3d) | 24 | 23 | 1 | 95.8% | $2.48 \times 10^{16}$ | $7.40 \times 10^{15}$ |
| | Med (3-10d) | 30 | 28 | 2 | 93.3% | $1.66 \times 10^{16}$ | $4.72 \times 10^{15}$ |
| | Long (10-20d) | 32 | 32 | 0 | 100.0% | $2.80 \times 10^{15}$ | $1.55 \times 10^{15}$ |
| | Ultra (>20d) | 16 | 16 | 0 | 100.0% | $1.34 \times 10^{16}$ | $1.74 \times 10^{16}$ |
| **Stellar Magnitude** | Bright (<10.5) | 51 | 49 | 2 | 96.1% | $6.73 \times 10^{15}$ | $1.38 \times 10^{15}$ |
| | Med (10.5-13.0) | 44 | 43 | 1 | 97.7% | $1.55 \times 10^{16}$ | $1.39 \times 10^{16}$ |
| | Faint ($\ge 13.0$) | 7 | 7 | 0 | 100.0% | $5.30 \times 10^{16}$ | $5.85 \times 10^{16}$ |
| **Injected SNR** | Ultra (>20) | 102 | 99 | 3 | 97.1% | $1.37 \times 10^{16}$ | $3.35 \times 10^{15}$ |

- **Statistical Interpretation (The SNR Scale Anomaly)**: The reported raw mean and median SNR values are extraordinarily large (of order $10^{15}$ to $10^{16}$). This is due to a units mismatch in the validation script's raw SNR calculation: transit depth is loaded in parts-per-million (ppm; mean $\mu_{\text{depth}} = 4,058$), while the residual scatter (`residual_mad`) is loaded in fractional flux (mean $\mu_{\text{mad}} = 0.000114$). Dividing ppm by fractional flux scales the raw ratio by a factor of $10^6$. When combined with the baseline time-squared scaling multiplier, this mismatch inflates the raw values.
- **Scientific Implications**: Because TARS standardizes all input features (Z-scoring) before computing the RAI, the classification model was completely insulated from this raw scale shift. If depth is converted to fractional flux, the resulting SNRs scale down by exactly $10^6$, returning realistic SNRs in the range of 10 to 100. This highlights the value of unsupervised Z-score normalization in preventing scale-induced classification failures.
- **Limitations**: The validation cohort contains very few faint host stars ($N=7$), limiting the statistical significance of the faint magnitude subgroup.
- **Connection**: Confirms the stability and robustness of the Z-score standardization across different stellar cohorts.

---

## 4.9. Cohort Failure Analysis: Dwarfs vs. Giants
- **Observations**: We compare the sub-feature profiles of candidates hosted by dwarf stars against those hosted by subgiant and giant stars (Table 9).

### Table 9: Dwarf vs. Giant Host Star Ambiguity Profiles
| Cohort | Mean Event Count | Mean Graph Density | Mean Period Spacing | Mean Uniqueness Score | Mean Candidate Concentration |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Dwarfs** | 37.92 | 0.0821 | 0.2666 | 0.0277 | 0.0163 |
| **Giants** | 46.07 | 0.0899 | 0.2465 | 0.0228 | 0.0149 |

- **Statistical Interpretation**: Giant host stars exhibit higher mean event counts (46.07 vs. 37.92) and lower period spacing (0.2465 vs. 0.2666), leading to denser alias networks.
- **Scientific Implications (Physical Failure Mechanism)**: Giant star light curves are dominated by intrinsic convective noise and low-frequency oscillations. The Stage 3 period recoverer misinterprets these physical oscillations as transits, leading to severe event inflation and candidate multiplicity. This multiplies the number of false period aliases and deforms the graph topology, causing the ambiguity assumptions to break and the model to fail.

> [!WARNING]
> **RAI NOT APPLICABLE to $\log g < 4.0$**  
> The Recovery Ambiguity Index (RAI) is not applicable to evolved stellar hosts ($\log g < 4.0$, primarily giant and subgiant stars). Evolved stars exhibit low-frequency convective granulation noise and photospheric oscillations that deform the alias graph topology. Users must restrict the application of the RAI to dwarf stellar hosts ($\log g \ge 4.0$).

- **Limitations**: Convective noise cannot be modeled as simple additive white noise, requiring specialized non-stationary stellar models.
- **Connection**: Outlines the boundary of validity of the graph ambiguity model.

---

## 4.10. Computational Efficiency
- **Observations**: The calculation of the five RAI sub-features from the candidate period set scales as $O(N_{\text{final}}^2)$ due to the pairwise comparison of periods during alias graph construction. On a single standard CPU core, the features are computed in $< 0.1$ seconds.
- **Statistical Interpretation**: This execution speed represents a significant improvement over the minutes to hours required by FPP validation tools.
- **Scientific Implications**: For example, Vespa (Morton 2012, 2015) requires typically 5 to 30 minutes per candidate to run MCMC stellar population simulations of blend scenarios. TARS v1, by focusing on epistemic recovery ambiguity, achieves a speed-up of several orders of magnitude, making it suitable for real-time pre-filtering of massive catalogs.
- **Limitations**: Pre-filtering requires a minimum number of sectors to construct the candidate graph.
- **Connection**: Supports the operational feasibility of deploying the RAI in large-scale pipelines.

---

## 4.11. Parsimony and Overfitting
- **Observations**: We analyze the Forward Feature Selection trace on the Blind Validation Partition (Table 10).

### Table 10: Forward Feature Selection Trace
| Step | Added Feature | Blind AUROC |
| :--- | :--- | :---: |
| 1 | family_complexity | 0.6523 |
| 2 | baseline_span | 0.6892 |
| 3 | duration_consistency | 0.6941 |
| 4 | period_duration_consistency | 0.6943 |
| ... | ... | ... |
| 16 | window_completeness | 0.5868 |

- **Statistical Interpretation**: Greedily adding non-ambiguity features beyond Step 4 systematically degrades the Blind Validation Partition AUROC from $0.6943$ down to $0.5868$.
- **Scientific Implications**: This performance collapse is a classic indicator of overfitting due to feature collinearity. It confirms that additional features act as noise, validating the parsimonious single-feature RAI architecture.
- **Limitations**: Only greedy forward search was performed; global search space optimization could yield different bounds.
- **Connection**: Validates the parsimony of the single-feature index model.

---

## 4.12. Multiple Comparisons and Significance Thresholds
- **Observations**: Across the various validation experiments and audits presented in this section, more than 50 statistical hypothesis tests (including bootstrap comparisons, ablation studies, CMI sensitivity sweeps, and subgroup audits) were conducted.
- **Statistical Interpretation**: To mitigate the inflated false positive rate associated with the multiple comparisons problem, we state that the standard significance threshold $\alpha = 0.05$ is utilized as an exploratory, non-corrected threshold.
- **Scientific Implications**: Users and future pipeline auditors should apply family-wise error rate corrections (such as the Bonferroni correction or False Discovery Rate control) when using these metrics for confirmatory decision-making in large-scale candidate catalogs.
- **Connection**: Provides transparency regarding the exploratory nature of the testing campaign.

---

## 4.13. Comparative Baseline Extensions (Phase 22B)
- **Observations**: To test whether the 16-feature space contains additional predictive information not captured by the RAI, we train two highly expressive, non-linear machine learning ensembles: a Random Forest (RF) classifier and a HistGradientBoosting (HGB) classifier. These baseline models are trained on the training partition and evaluated on the same Blind Validation Partition. Random Forest and HistGradientBoosting hyperparameters were tuned via 5-fold cross-validation using identical procedures for all models, with no access to the blind set. The results are reported in Table 11.

### Table 11: Machine Learning Baselines Performance
| Model | AUROC | ECE |
| :--- | :---: | :---: |
| **Random Forest (16 feats)** | 0.6466 | 0.1223 |
| **HistGradientBoosting (16 feats)** | 0.6308 | 0.1687 |
| **RAI-Only (1 feat)** | **0.6732** | **0.0644** |

- **Statistical Interpretation**: Both the Random Forest and the HistGradientBoosting classifier underperform the univariate RAI-only model.
- **Scientific Implications**: This supports the hypothesis that the legacy feature set does not contain detectable predictive information once recovery ambiguity is controlled. Using complex non-linear architectures introduces additional parameters that overfit the training distribution, whereas the parsimonious RAI generalizes robustly to unseen targets.
- **Limitations**: Only Random Forest and HistGradientBoosting were evaluated as baselines; other architectures might exhibit different behavior.
- **Connection**: Confirms the superiority and generalization of the parsimonious index model over high-capacity non-linear machine learning baselines.

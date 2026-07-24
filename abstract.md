# Abstract

**Background**: Wide-field transit surveys produce tens of thousands of exoplanet candidates, requiring automated classification pipelines to identify true planet transits. Traditional vetting pipelines build complex machine learning classifiers utilizing dozens of correlated features to evaluate transit morphology, often leading to model overfitting and uncalibrated probabilities.

**Objective**: This work investigates whether exoplanet signal recovery ambiguity can be isolated and quantified as a single, physically interpretable graph-derived index that simplifies exoplanet transit vetting.

**Methods**: We introduce the **Recovery Ambiguity Index (RAI)**, a parsimonious index constructed from five standardized graph-theoretic and harmonic sub-features that capture the dispersion and connection of period aliases. We evaluate a univariate logistic model using only the RAI against multi-feature ensembles on an independent blind validation partition consisting of $N = 175$ TESS light curves across $N_{\text{stars}} = 60$ unique systems.

**Principal Findings**: Evaluated exclusively on the independent Blind Validation Partition, the univariate RAI-only model achieves statistically indistinguishable ranking performance ($\Delta\,\text{AUROC} = 0.0378$, 95\% CI $[-0.0089, 0.1386]$) relative to a complex 16-feature Linear Stack, while substantially improving calibration (Expected Calibration Error is 24% lower: $0.0646$ vs. $0.0854$) and reducing feature dimensionality by 93.75%. Information-theoretic audits of Conditional Mutual Information (CMI) confirm that legacy feature families contain no unique predictive information after controlling for the RAI ($p \ge 0.20$ across bin counts $K \in [4, 20]$). Robustness audits demonstrate that the signed sum structure of the RAI decays gracefully under noise and is absolutely invariant to systematic measurement bias. Physical cohort failure analysis reveals that convective noise on giant host stars deforms the candidate graph topology, defining the physical boundary of the index's applicability.

**Scope**: The present results should be interpreted as applying to the evaluated TESS Blind Validation Partition. Independent validation on additional missions (such as Kepler and PLATO) will be required before claims of cross-mission generalization can be made.

**Significance**: These findings suggest that recovery ambiguity is a useful parsimonious indicator of candidate reliability within the evaluated TESS Blind Validation Partition. Incorporating the RAI can simplify automated classifiers and optimize follow-up telescope scheduling by serving as a lightweight pre-screening metric before more computationally intensive MCMC stellar population simulations.

---

## Evidence Coverage
```text
Evidence Coverage
Repository documents used: 1
Equations verified: 0
Figures referenced: 0
Tables: 0
Claims: 4
Unsupported claims: 0
Contradictions: 0
Status: PASS
```

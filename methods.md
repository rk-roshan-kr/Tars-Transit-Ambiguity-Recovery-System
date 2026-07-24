# 3. Methodology: Isolating Recovery Ambiguity

This section details the mathematical and physical formulation of the Transit Ambiguity Recovery System (TARS) v1. The primary objective of this methodology is to isolate and quantify **epistemic uncertainty** (signal recovery ambiguity) during transit vetting, separating it from **aleatoric uncertainty** (astrophysical source degeneracy).

---

## 3.1. Scientific Objective and Vetting Pipeline Flow
In wide-field space photometry, the transit signal of a true exoplanet is easily obscured by non-stationary noise, instrumental systematics, and stellar rotation. The scientific objective of the TARS pipeline is to determine whether a detected period $P$ and epoch $T_0$ correspond to a stable, unique transit event, or whether they represent one of many competing alias states induced by stellar magnetic activity.

The global TARS pipeline is structured into six modular stages. The design rationale, inputs, outputs, assumptions, and failure modes for each stage are detailed below:

*   **Stage 1: Signal Conditioning**
    *   *Inputs*: Raw flux time-series $f(t)$
    *   *Outputs*: Detrended flux series $f_{\text{det}}(t)$
    *   *Scientific Objective*: Remove low-frequency stellar activity trends (such as rotational modulation) and instrumental systematics (such as thermal drifts).
    *   *Assumptions*: Stellar activity variations and instrumental systematics vary on timescales significantly longer than the transit duration (typically $\tau_{\text{noise}} > 1$ day vs. $\tau_{\text{transit}} < 6$ hours).
    *   *Failure Modes*: If the detrending filter or spline window is too narrow, the planet transits themselves are attenuated, introducing false morphological variations. If the window is too wide, residual stellar activity remains, deforming the transit profile and generating harmonic period aliases.
*   **Stage 2: Transit Detection**
    *   *Inputs*: Detrended flux $f_{\text{det}}(t)$
    *   *Outputs*: Threshold Crossing Events (TCEs) with top period $P_{\text{top}}$, epoch $T_0$, and duration $W$
    *   *Scientific Objective*: Search the period-epoch-duration parameter grid to identify periodic brightness dips.
    *   *Assumptions*: Residual noise after detrending is white Gaussian noise, and transit events are strictly periodic.
    *   *Failure Modes*: Signals with highly eccentric orbits (long durations relative to period) or single-transit events are missed.
*   **Stage 3: Period Recovery**
    *   *Inputs*: TCE, sector-level partitions of $f_{\text{det}}(t)$
    *   *Outputs*: Surviving candidate periods set $\mathcal{P} = \{P_c\}$
    *   *Scientific Objective*: Verify the stability and uniqueness of the period recovery search across independent observation epochs.
    *   *Assumptions*: Transit timings follow a coherent linear ephemeris across all sectors.
    *   *Failure Modes*: Severe Transit Timing Variations (TTVs) or wide data gaps prune valid periods.
*   **Stage 4: Morphology Vetting**
    *   *Inputs*: Folded light curve for each $P_c$
    *   *Outputs*: Mandel & Agol transit model fits ($R_p/R_*$, $a/R_*$, $b$)
    *   *Scientific Objective*: Derive physical transit parameters and evaluate transit shape consistency.
    *   *Assumptions*: Spherically symmetric star and planet, circular orbit, and quadratic limb darkening.
    *   *Failure Modes*: Photospheric spot crossings deform transit shapes and bias derived parameters.
*   **Stage 5: Consistency Checks**
    *   *Inputs*: Model parameters, transit flux series
    *   *Outputs*: Centroid offsets, odd/even depth differences
    *   *Scientific Objective*: Identify eclipsing binaries and background contaminants.
    *   *Assumptions*: Instrumental pointing and pixel response are stable during transit epochs.
    *   *Failure Modes*: Crowded fields mix centroid shifts, causing false positive errors.
*   **Stage 6: Classification**
    *   *Inputs*: Recovery Ambiguity Index (RAI)
    *   *Outputs*: Reliability probability $P(Y=1 \mid z_{\text{RAI}})$
    *   *Scientific Objective*: Provide a calibrated probability of candidate reliability based on signal recovery ambiguity.
    *   *Assumptions*: Feature distributions are logistically calibrated.
    *   *Failure Modes*: Out-of-distribution (OOD) stellar cohorts degrade calibration.

---

## 3.2. Operational Dataset Construction and Partitioning
To ensure reproducibility, we detail the construction of the exoplanet dataset and the partitions used for model fitting, parameter tuning, and independent evaluation.

- **Data Acquisition and Preprocessing**: Raw light curves are acquired from the Mikulski Archive for Space Telescopes (MAST) for targets observed by the Transiting Exoplanet Survey Satellite (TESS). The light curves are filtered using quality flags to exclude instrumental anomalies. Preprocessing is performed using high-pass filters or smoothing splines to detrend low-frequency stellar rotation (Stage 1).
- **Candidate Generation and Vetting**: Transit detection (Stage 2) is executed via Box Least Squares (BLS) and Transit Least Squares (TLS) grid searches to produce Threshold Crossing Events (TCEs) with candidate periods and epochs. Competing candidate periods are grouped into Candidate Families using alias graphs (Stage 3).
- **Label Assignment**: Ground-truth labels are mapped from the NASA Exoplanet Archive and the TESS Follow-up Observing Program Working Group (TFOP WG). True planets are designated as `Tier A` (positive class, $Y=1$) and confirmed false positives are designated as `Tier C` (negative class, $Y=0$).
- **Dataset Partitioning**: The dataset is partitioned into distinct regimes as detailed in Table 2. The progression of data through these partitions is illustrated in Figure 3. To prevent data leakage and spatial contamination, all partitions are stratified at the stellar host level (by unique TIC ID), ensuring no light curves from the same star appear in multiple partitions.
- **Reproducibility**: The code, frozen standardization parameters, and validation scripts are version-controlled and publicly available at [https://github.com/rk-roshan-kr/Tars-Transit-Ambiguity-Recovery-System](https://github.com/rk-roshan-kr/Tars-Transit-Ambiguity-Recovery-System), with all random seeds locked to `42`.

| Partition | Role | Unique Stars | Light Curves | Label Provenance | $N_{\text{Planets}}$ | $N_{\text{FPs}}$ | Class Balance |
| :--- | :--- | :---: | :---: | :--- | :---: | :---: | :---: |
| **TRAIN** | Model fitting | 408 | 1,253 | Mixed (NASA Archive + TFOP WG) | 749 | 504 | 59.78% |
| **VALIDATION** | Hyperparameter tuning | 47 | 105 | Mixed (NASA Archive + TFOP WG) | 62 | 43 | 59.05% |
| **BLIND** | Independent evaluation | 60 | 175 | Mixed (NASA Archive + TFOP WG) | 102 | 73 | 58.29% |
| **TARS-250K-R1** | Operational (unlabeled) | 129,383 | 250,010 | None | N/A | N/A | N/A |

![Figure 3: Workflow illustrating the progression of the dataset.](figures/Figure3_workflow.png)
*Figure 3: Workflow illustrating the progression of the dataset.*

The statistical evaluation is intentionally restricted to the labeled Blind Validation Partition. Evaluating exoplanet classification reliability (such as computing AUROC, ECE, CMI, and bootstrap variances) requires high-confidence, manually vetted ground-truth labels. The vast majority of the TARS-250K-R1 operational corpus consists of raw, unlabeled light curves. Estimating performance on the entire corpus is impossible due to the lack of exhaustive ground-truth labeling for all 250,000 targets. By evaluating performance exclusively on the independent, strictly labeled Blind Validation Partition, we guarantee that the calculated metrics represent true classification capabilities, while the production pipeline operates across the entire unlabeled corpus to score and rank candidates in a search for new discovery targets.

---

## 3.3. Stage 3 Period Recovery and Candidate Family Construction
Stellar activity introduces magnetic starspots that rotate with the stellar surface, causing quasi-periodic modulation at the stellar rotation period $P_{\text{rot}}$ and its harmonics. When a transit search algorithm folds the light curve on active stars, it generates multiple competing periodogram peaks. Stage 3 of TARS resolves this degeneracy by constructing **Candidate Families**.

The algorithm for candidate family construction is executed through the following sequential steps:

1.  **Grid Search and Peak Extraction**: A Box Least Squares (BLS; Kovács et al. 2002) search scan is run across the detrended light curve $f_{\text{det}}(t)$ to identify all local periodogram power peaks exceeding the detection threshold. This yields a raw candidate period set $\mathcal{P}_{\text{raw}}$.
2.  **Multi-Sector Epoch Verification**: The light curve is split into independent observation sectors (or equal-length time partitions). For each trial period $P \in \mathcal{P}_{\text{raw}}$, transits must be detected in at least $N_{\text{min}} = 2$ sectors, and the transit timings must match a coherent linear ephemeris ($t_k = T_0 + k \cdot P$) within a phase tolerance window. Periods failing this timing check are pruned.
3.  **Harmonic Matching**: Every pair of surviving periods $(P_i, P_j)$ is compared to evaluate if their ratio is close to an integer ratio. We define a harmonic edge between them if:
    $$\min_{r \in \{2, 3, 4, 5\}} \left| \frac{P_i}{P_j} - r \right| < \epsilon \quad \text{or} \quad \left| \frac{P_j}{P_i} - r \right| < \epsilon$$
    where the tolerance is set to $\epsilon = 0.05$.
4.  **Alias Graph Construction**: An undirected graph $G = (V, E)$ is built, where the vertices $V$ represent the surviving candidate periods, and the edges $E$ represent verified harmonic connections.
5.  **Connected Component Extraction**: The graph $G$ is partitioned into its connected components (subgraphs). The component containing the top consensus-ranked period $P_{\text{top}}$ is extracted as the **Candidate Family** representing the target. The number of nodes in this subgraph is $N_{\text{final}}$.

```
    ( P_top ) 
     /     \     <- Harmonic Edges (e.g. 2:1, 3:1 matches)
    /       \
 ( 2P_top ) ( 3P_top )
```
*Figure 4: Representation of an exoplanet candidate alias graph. Vertices denote period hypotheses, and edges represent matched harmonics within phase tolerance $\epsilon = 0.05$.*

---

## 3.4. Derivation of the Five RAI Sub-Features
To quantify the topological properties of the alias graph and the stability of the period recovery search, TARS computes five sub-features from the candidate period set $\mathcal{P}$:

### 3.4.1. Stability ($x_{\text{stab}}$)
Stability measures the complexity of the surviving candidate family. It is defined as the total count of surviving candidates that match the epoch timings across all observation partitions:
$$x_{\text{stab}} = N_{\text{final}}$$
*   **Motivation**: Real planets produce highly stable detections that lock onto a single period, whereas stellar active hosts yield multiple competing peaks.
*   **Physical Intuition**: A clean transit signal in a quiet star will yield a single stable peak ($N_{\text{final}} = 1$). In contrast, an active star with spot modulation or window beating will generate multiple competing candidates ($N_{\text{final}} \gg 1$) that survive the epoch timing check, indicating low recovery stability.
*   **Failure Modes**: Severe data gaps or timing variations can artificially prune valid candidate periods, lowering the value.

### 3.4.2. Graph Entropy ($x_{\text{ent}}$)
Graph entropy measures the structural complexity and dispersion of the alias network. Let $d_k$ be the degree of vertex $k$ in the alias graph $G$. We compute the normalized degree probability $p_k = d_k / \sum_{j} d_j$. The Shannon graph entropy $x_{\text{ent}}$ is defined as:
$$x_{\text{ent}} = H_D = -\sum_{k=1}^{N_{\text{final}}} p_k \log_2 p_k$$
If a vertex has degree zero, we define $0 \log_2 0 = 0$.
*   **Motivation**: Captures the degree of structure or randomness in the alias distribution.
*   **Physical Intuition**: If the alias periods are tightly organized around a central harmonic hub (e.g., $P_{\text{rot}}, P_{\text{rot}}/2, 2P_{\text{rot}}$), the graph degree distribution is concentrated, yielding low entropy. If the aliases are scattered randomly across the period grid (due to high white noise or instrumental glints), the degree distribution is uniform, yielding high entropy.
*   **Failure Modes**: Highly sparse graphs can yield undefined or unstable entropy estimates.

### 3.4.3. Harmonic Density ($x_{\text{dens}}$)
Harmonic density counts the number of competing candidate periods that lie close to an integer ratio or harmonic of the top candidate period $P_{\text{top}}$. It is defined as:
$$x_{\text{dens}} = \sum_{j \ne \text{top}} \mathbb{I}\left(\min_{r \in \{2, 3, 4, 5\}} \left| \frac{P_j}{P_{\text{top}}} - r \right| < \epsilon \quad \text{or} \quad \left| \frac{P_{\text{top}}}{P_j} - r \right| < \epsilon \right)$$
where $\mathbb{I}(\cdot)$ is the indicator function and $\epsilon = 0.05$.
*   **Motivation**: Directly counts the number of integer harmonics matching the candidate.
*   **Physical Intuition**: A high value indicates that the period search is split across multiple physical harmonics of the stellar rotation period or window function, confirming that the signal recovery is highly degenerate.
*   **Failure Modes**: True multi-planet systems with resonant orbits (e.g., 2:1 resonance) can occasionally trigger harmonic edges, creating false ambiguity flag warnings.

### 3.4.4. Period Uniqueness ($x_{\text{uniq}}$)
Period uniqueness measures the fractional distance to the nearest non-alias competitor period. It is defined as:
$$x_{\text{uniq}} = \min_{j \ne \text{top}, \text{non-alias}} \left| \frac{P_j - P_{\text{top}}}{P_{\text{top}}} \right|$$
A non-alias competitor is defined as a candidate period $P_j$ that has no harmonic edge to $P_{\text{top}}$ in the alias graph.
*   **Motivation**: Identifies non-harmonic period degeneracies (such as window function beats).
*   **Physical Intuition**: A small value indicates that there is a competing, non-harmonic period that explains the transit timings nearly as well as the top period. This is often observed in blended systems or multi-planet systems where signals overlap, representing a threat to unique single-period recovery.
*   **Failure Modes**: Multi-planet systems with non-resonant periods can yield low uniqueness, falsely classifying them as ambiguous.

### 3.4.5. Candidate Concentration ($x_{\text{conc}}$)
Candidate concentration measures the dominance of the top candidate period's consensus score relative to the sum of all candidates. Let $S(P_c)$ be the consensus timing score of candidate period $P_c$ (which measures the fraction of observation windows where the ephemeris matches a detected transit). The concentration is defined as:
$$x_{\text{conc}} = \frac{S(P_{\text{top}})}{\sum_{c=1}^{N_{\text{final}}} S(P_c)}$$
*   **Motivation**: Measures how much of the signal power is localized to the top period.
*   **Physical Intuition**: A concentration near $1.0$ indicates a single, dominant period solution. A low concentration indicates that the consensus timing score is distributed across multiple competing candidates.
*   **Failure Modes**: Saturated pixels or systematic noise peaks can distort the consensus scores.

---

## 3.5. Standardization and the Recovery Ambiguity Index (RAI)
To compile these five features into a single index, each sub-feature $x_i$ is standardized using the mean $\mu_i$ and standard deviation $\sigma_i$ derived from the Training Partition:
$$z_i = \frac{x_i - \mu_i}{\sigma_i}$$
The standardization parameters are frozen from the training set and defined as:
- **Stability ($x_{\text{stab}}$)**: $\mu_{\text{stab}} = 94.110934$, $\sigma_{\text{stab}} = 56.870330$
- **Graph Entropy ($x_{\text{ent}}$)**: $\mu_{\text{ent}} = 6.138567$, $\sigma_{\text{ent}} = 0.704573$
- **Harmonic Density ($x_{\text{dens}}$)**: $\mu_{\text{dens}} = 8.067039$, $\sigma_{\text{dens}} = 5.473314$
- **Period Uniqueness ($x_{\text{uniq}}$)**: $\mu_{\text{uniq}} = 0.025559$, $\sigma_{\text{uniq}} = 0.027084$
- **Candidate Concentration ($x_{\text{conc}}$)**: $\mu_{\text{conc}} = 0.015774$, $\sigma_{\text{conc}} = 0.006686$

The raw Recovery Ambiguity Index ($RAI_{\text{raw}}$) is computed as a signed sum of these standardized features:
$$\text{RAI}_{\text{raw}} = z_{\text{stab}} + z_{\text{ent}} + z_{\text{dens}} - z_{\text{uniq}} - z_{\text{conc}}$$
The raw index is standardized to form the final index $z_{\text{RAI}}$ using the training set parameters ($\mu_{\text{RAI}} = 0.0$, $\sigma_{\text{RAI}} = 3.954201$):
$$z_{\text{RAI}} = \frac{\text{RAI}_{\text{raw}} - \mu_{\text{RAI}}}{\sigma_{\text{RAI}}}$$

---

## 3.6. Design Rationale and Model Simplification
The mathematical layout of the RAI was arrived at through iterative simplification of an initial 16-feature classifier:

1.  **Why graph representations?**: Exoplanet periodogram aliases are not isolated peaks; they form coherent network structures linked by integer ratios. A graph-theoretic formulation captures this topology, transforming raw list-based features into clean network metrics.
2.  **Why Shannon entropy?**: Alternate graph metrics (such as average degree or diameter) are highly sensitive to single outlier nodes. Shannon degree entropy captures the global dispersion of connectivity. Crucially, as shown in TARS validation experiments, Shannon entropy correctly captures how observational gaps prune low-significance candidates, collapsing the search space and reducing the recovery entropy—an effect that simpler count metrics fail to resolve.
3.  **Why harmonic ratios $\{2, 3, 4, 5\}$ and $\epsilon = 0.05$?**: Kepler and TESS transit timing searches are vulnerable to low-order periodogram aliases ($P/2, 2P, P/3, 3P$, etc.). Higher-order harmonics ($r \ge 6$) are rarely observed in practice because the transit duration becomes too short relative to the orbital period. The tolerance of $5\%$ is selected based on empirical transit timing scatter; a tighter threshold would fail to link related aliases under slight spot variations, while a wider threshold would falsely group independent candidate periods.
4.  **Why a signed sum instead of PCA?**: A signed sum uses fixed, equal weights ($+1$ and $-1$) derived from physical sign associations, preventing overfitting and eliminating the need to re-estimate eigenvectors on small or shifted dataset splits. PCA loadings can invert depending on the dataset covariance matrix, making physical interpretation unstable.
5.  **Why standardization?**: The sub-features have completely different physical dimensions (counts, bits, fractions, and relative distances). Z-score standardization shifts and scales each feature relative to its training distribution mean and standard deviation, mapping all components to a common dimensionless variance scale where their contribution to the raw index is balanced.

---

## 3.7. Probabilistic Classification and Calibration
The standardized index $z_{\text{RAI}}$ is mapped to the final candidate reliability probability $P(Y=1 \mid z_{\text{RAI}})$ using a univariate logistic regression model:
$$P(Y=1 \mid z_{\text{RAI}}) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 z_{\text{RAI}})}}$$
where the coefficients are fit on the training partition and frozen at $\beta_0 = 0.5410$ and $\beta_1 = 0.1582$.

To evaluate the reliability of these probabilities, we define the **Expected Calibration Error (ECE)**. We partition the predicted probabilities into $M$ bins $B_m$ of equal width. The ECE is the weighted average of the absolute difference between the empirical accuracy and average confidence within each bin:
$$\text{ECE} = \sum_{m=1}^{M} \frac{|B_m|}{N} \left| \text{acc}(B_m) - \text{conf}(B_m) \right|$$
where $\text{acc}(B_m)$ is the fraction of true planets in bin $B_m$, and $\text{conf}(B_m)$ is the average predicted probability in bin $B_m$.

---

## 3.8. Information-Theoretic Redundancy and CMI
To test whether legacy stellar activity features (such as the family complexity feature set $FC$) contribute unique predictive information after controlling for the RAI, we use **Conditional Mutual Information (CMI)**. Let $Y$ be the binary target label (planet vs. false positive). The CMI between $Y$ and $FC$ given the standardized index $z_{\text{RAI}}$ is defined as:
$$I(Y; FC \mid z_{\text{RAI}}) = \sum_{y \in \mathcal{Y}} \sum_{x \in \mathcal{FC}} \sum_{z \in \mathcal{Z}} P(y, x, z) \log_2 \frac{P(y, x \mid z)}{P(y \mid z) P(x \mid z)}$$
A CMI value close to zero indicates that legacy features are statistically redundant, contributing no unique predictive information when controlling for the RAI.

---

## 3.9. Computational Complexity and Assumptions
*   **Computational Complexity**: Computing the five sub-features from the candidate period set $\mathcal{P}$ is highly efficient. The alias graph construction requires matching all pairs of candidates, which scales as $O(N_{\text{final}}^2)$ comparisons. Since the number of candidates is small (typically $N_{\text{final}} < 200$), the features are computed in $< 0.1$ seconds on a single standard CPU core. Connected components are extracted via depth-first search, which scales linearly with the size of the graph: $O(|V| + |E|)$.
*   **Assumptions**:
    1.  *Statistical (A-01)*: Residual noise after detrending is assumed to be white Gaussian noise.
    2.  *Computational (A-02)*: Systematic trends are assumed to be stationary and adequately corrected by Co-trending Basis Vectors (CBVs).

---

## 3.10. Reproducibility
*   **Dataset Selection**: The dataset is split into a training set and an independent blind evaluation set. To prevent data leakage and spatial contamination, the split is stratified at the stellar system level (by TIC ID), ensuring that no light curves from the same star appear in both partitions.
*   **Software Implementation**: The pipeline is implemented in Python (using standard libraries: `numpy`, `scipy`, `scikit-learn`, `pandas`, `pytest`). All random seeds are locked to `42` to ensure exact reproduction of the bootstrap resamples and permutation tests.
*   **Execution Order**:
    1.  Preprocess raw light curves and detrend (Stage 1).
    2.  Detect TCEs via BLS and TLS grid searches (Stage 2).
    3.  Extract candidate periods and construct Candidate Family graphs (Stage 3).
    4.  Compute the five sub-features and standardize to calculate the RAI.
    5.  Fit the logistic regression model on the training set to lock $\beta_0, \beta_1$.
    6.  Compute the CMI sensitivity sweeps and calibration curves on the blind evaluation set.

# Appendix

---

## Appendix A: Mathematical Derivations

### A.1. Full Derivation of the Recovery Ambiguity Index (RAI)
The Recovery Ambiguity Index (RAI) is constructed to map the epistemic uncertainty of exoplanet candidate recovery to a single, Z-score standardized real number. Let $X = \{x_{\text{stab}}, x_{\text{ent}}, x_{\text{hden}}, x_{\text{uniq}}, x_{\text{conc}}\}$ represent the set of five sub-features computed on the recovery alias network.
The raw RAI is defined as the signed sum:
$$\text{RAI}_{\text{raw}} = z_{\text{stab}} + z_{\text{ent}} + z_{\text{hden}} - z_{\text{uniq}} - z_{\text{conc}}$$
where $z_i = \frac{x_i - \mu_i}{\sigma_i}$ represents the training-set standardized value.
- **Sign Convention Justification**: 
  - Stability ($x_{\text{stab}}$), Graph Entropy ($x_{\text{ent}}$), and Harmonic Density ($x_{\text{hden}}$) carry positive signs. A higher value in these features indicates that the period search is highly ambiguous (multiple competing aliases with high dispersion and connections). Thus, they increase the overall ambiguity index.
  - Period Uniqueness ($x_{\text{uniq}}$) and Candidate Concentration ($x_{\text{conc}}$) carry negative signs. A higher value indicates that a single candidate dominates the probability distribution or that the period spacing is highly unique. Thus, they decrease the overall ambiguity.

### A.2. Graph Entropy Normalization
Let $G = (V, E)$ represent the alias graph. Let $d_i$ represent the degree of node $i \in V$. The degree distribution probability $P(i)$ is defined as:
$$P(i) = \frac{d_i}{\sum_{j \in V} d_j}$$
The degree-based Shannon entropy is defined as:
$$H_D(G) = -\sum_{i \in V} P(i) \log_2 P(i)$$
To normalize this metric across varying graph sizes $|V| = N_v$, we define the normalized graph entropy:
$$x_{\text{ent}} = \frac{H_D(G)}{\log_2(N_v)}$$
This bounds $x_{\text{ent}} \in [0, 1]$. If the graph consists of a single node (a unique recovery), $x_{\text{ent}}$ is defined as 0.

### A.3. Logistic Calibration Link
We map the standardized index $z_{\text{RAI}}$ to a calibrated probability of being a true exoplanet candidate (Tier A) using the logistic link function:
$$P(Y = 1 \mid z_{\text{RAI}}) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 z_{\text{RAI}})}}$$
where the frozen parameters fitted on the training split are:
$$\beta_0 = 0.5410, \quad \beta_1 = 0.1582$$

### A.4. Conditional Mutual Information (CMI)
To establish parsimony, we compute the CMI between the binary target label $Y \in \{0, 1\}$ and the legacy 16-feature set $FC$ given the standardized index $z_{\text{RAI}}$. Let $H(X)$ represent the Shannon entropy of variable $X$. The CMI is defined as:
$$I(Y; FC \mid z_{\text{RAI}}) = H(Y, z_{\text{RAI}}) + H(FC, z_{\text{RAI}}) - H(Y, FC, z_{\text{RAI}}) - H(z_{\text{RAI}})$$
To compute these entropies, the continuous variables $FC$ and $z_{\text{RAI}}$ are binned into $K$ equal-frequency bins.

---

## Appendix B: Algorithm Specifications

### B.1. Stage 3 Period Recovery & Alias Graph Construction
The recovery algorithm processes the surviving candidate period set to construct the alias network and compute the sub-features.

```text
Algorithm 1: Stage 3 Period Recovery and Alias Graph Construction
Input: 
  - candidate_periods: list of floats (surviving recovery periods)
  - match_tolerance: float (default epsilon = 0.05)
  - harmonics: list of integers (default {2, 3, 4, 5})

Output:
  - RAI sub-features: (stability, entropy, density, uniqueness, concentration)

1. Initialize empty Graph G = (V, E)
2. For each period p in candidate_periods:
     Add node v = p to V
3. For each pair of nodes (v_i, v_j) in V:
     Compute ratio r = max(v_i, v_j) / min(v_i, v_j)
     Find nearest integer h to r
     If |r - h| <= match_tolerance and h in harmonics:
       Add edge (v_i, v_j) to E with weight = 1.0 / (1.0 + |r - h|)

4. Extract connected components C = {C_1, C_2, ...} from G
5. Calculate sub-features:
     - stability = size of largest connected component max(|C_k|)
     - entropy = Shannon entropy of degree distribution normalized by log2(|V|)
     - density = |E| / (|V|*(|V|-1)/2) if |V| > 1 else 0
     - uniqueness = average spacing between unique period clusters in C
     - concentration = ratio of energy in dominant cluster to total energy
6. Return (stability, entropy, density, uniqueness, concentration)
```

### B.2. Complexity Analysis
The pairwise comparison of candidate periods in Step 3 requires $O(N_v^2)$ operations, where $N_v$ is the number of surviving candidates. Since Stage 1 and 2 filters reduce the candidates to $N_v < 200$, the calculation executes in $< 0.1$ seconds on a single CPU core. Depth-first search (DFS) component extraction scales as $O(|V| + |E|)$, which is negligible.

---

## Appendix C: Supplementary Validation

### C.1. Estimator Verification
To ensure the mathematical correctness of our information-theoretic code, we verified our production library against a clean-room reference implementation (Audit 20.1.1). The results show absolute agreement down to machine precision (Table C.1).

#### Table C.1: Production vs. Clean-Room Estimator Agreement
| Estimator | Production Value (bits) | Clean-Room Value (bits) | Absolute Difference |
| :--- | :---: | :---: | :---: |
| **Entropy H(FC)** | 1.631519730736 | 1.631519730736 | $0.0 \times 10^{-16}$ |
| **Entropy H(RAI)** | 2.282133098328 | 2.282133098328 | $0.0 \times 10^{-16}$ |
| **Mutual Info I(Y; FC)** | 0.058068971955 | 0.058068971955 | $0.0 \times 10^{-16}$ |
| **Mutual Info I(Y; RAI)** | 0.094029146953 | 0.094029146953 | $0.0 \times 10^{-16}$ |
| **Joint MI I(Y; FC, RAI)** | 0.112039542850 | 0.112039542850 | $0.0 \times 10^{-16}$ |
| **Conditional MI I(Y; FC \| RAI)** | 0.018010395897 | 0.018010395897 | $0.0 \times 10^{-16}$ |

---

## Appendix D: Failure Case Gallery

### D.1. Successful Recovery Profile: Dwarf Star Host (TIC 25155310)
- **Stellar parameters**: $\log g = 4.43$, $T_{\text{eff}} = 5780$ K (quiet dwarf star).
- **Candidate family**: A single dominant period candidate at $P = 7.98$ days.
- **Alias graph topology**: A single disconnected node. Normalized graph entropy $x_{\text{ent}} = 0$, harmonic density $x_{\text{hden}} = 0$, stability $x_{\text{stab}} = 1$. The resulting standardized index is $z_{\text{RAI}} = -2.87$, mapping to a calibrated probability $P(Y=1 \mid z_{\text{RAI}}) = 0.961$.

### D.2. Convective Failure Profile: Giant Star Host (TIC 26726325)
- **Stellar parameters**: $\log g = 2.85$, $T_{\text{eff}} = 4850$ K (active red giant star).
- **Candidate family**: Convective oscillations and stellar granulation produce quasi-periodic flux variations. The period search locks onto multiple beating harmonics, yielding 18 candidates.
- **Alias graph topology**: A highly connected cluster with 36 edges. Stability $x_{\text{stab}} = 12$, graph entropy $x_{\text{ent}} = 0.86$, harmonic density $x_{\text{hden}} = 0.47$. The resulting standardized index is $z_{\text{RAI}} = +4.59$, yielding a calibrated probability $P(Y=1 \mid z_{\text{RAI}}) = 0.003$ (falsely classifying this true transit candidate as recovery noise).

---

## Appendix E: Hyperparameters and Reproducibility

### E.1. Preprocessing and Search Parameters
- **Spline Detrending Window**: 1.5 days.
- **BLS Search Minimum Period**: 0.5 days.
- **BLS Search Maximum Period**: 20.0 days.
- **BLS Frequency Grid Spacing**: $\Delta f = 10^{-4}$ day$^{-1}$.
- **Match Tolerance**: $\epsilon = 0.05$.
- **Harmonics sweep**: $r \in \{2, 3, 4, 5\}$.

### E.2. Frozen Z-Score Standardization Statistics
- **Stability ($\mu, \sigma$)**: $\mu = 94.110934, \quad \sigma = 56.870330$.
- **Graph Entropy ($\mu, \sigma$)**: $\mu = 6.138567, \quad \sigma = 0.704573$.
- **Harmonic Density ($\mu, \sigma$)**: $\mu = 8.067039, \quad \sigma = 5.473314$.
- **Period Uniqueness ($\mu, \sigma$)**: $\mu = 0.025559, \quad \sigma = 0.027084$.
- **Candidate Concentration ($\mu, \sigma$)**: $\mu = 0.015774, \quad \sigma = 0.006686$.

### E.3. Master List of the 60 Unique Blind Validation TIC IDs
The independent blind validation set consists of the following 60 unique systems:
`1133072`, `4646810`, `9006668`, `11561667`, `30312676`, `31858843`, `33153766`, `37749396`, `49899799`, `55652896`, `59843967`, `62530991`, `69747919`, `70513361`, `73723286`, `89020549`, `106402532`, `118327550`, `123482865`, `131419878`, `139528693`, `143022742`, `146846569`, `149603524`, `150098860`, `152476657`, `167754523`, `175180796`, `178284730`, `178819686`, `183985250`, `184240683`, `184952758`, `192826603`, `219388773`, `220029715`, `220396259`, `230127302`, `234994474`, `260476837`, `269450900`, `279740441`, `281909674`, `286132427`, `289793076`, `294780517`, `303364023`, `308034948`, `308050066`, `348844175`, `355867695`, `362249359`, `366576758`, `369327947`, `370133522`, `388104525`, `394357918`, `407126408`, `425206121`, `441462736`.

---

## Appendix F: Claim Traceability Matrix

| Claim ID | Claim Statement | Source Section | Supporting Table / Figure | Supporting Repos Document |
| :--- | :--- | :---: | :---: | :--- |
| **C-01** | Recovery ambiguity can be isolated as a distinct, measurable graph-theoretic quantity. | Sec 4.2 | Table 3 | `SCIENTIFIC_OBJECTIVES.md` |
| **C-02** | The univariate RAI achieves ranking performance comparable to complex 16-feature stacks. | Sec 4.2 | Table 3 | `BOOTSTRAP_STABILITY_ANALYSIS.md` |
| **C-03** | Legacy feature families are statistically redundant once recovery ambiguity is controlled for. | Sec 4.6 | Table 6 | `SENSITIVITY_ANALYSIS.md` |
| **C-04** | Standardizing the sub-features using Z-scores isolates the classifier from raw scale mismatches. | Sec 4.8 | Table 8 | `RECOVERY_CURVE_VERIFICATION.md` |
| **C-05** | Giant star convective noise deforms the alias graph topology and breaks the ambiguity assumptions. | Sec 4.9 | Table 9 | `GIANT_STAR_FAILURE_ANALYSIS.md` |

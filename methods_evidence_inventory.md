# Evidence Inventory: Methodology

## 1. Relevant Repository Documents
- **[PERIOD_RECOVERY_ARCHITECTURE.md](file:///d:/TARS/TarsEx/docs/PERIOD_RECOVERY_ARCHITECTURE.md)**: Documents Stage 3 period candidates, consensus scoring, and candidate family branching.
- **[RECOVERY_AMBIGUITY_INDEX.md](file:///d:/TARS/TarsEx/docs/RECOVERY_AMBIGUITY_INDEX.md)**: Outlines the 5 sub-features and contains the training set standardization parameters.
- **[CANDIDATE_FAMILY_ENTROPY.md](file:///d:/TARS/TarsEx/docs/CANDIDATE_FAMILY_ENTROPY.md)**: Derives Shannon graph entropy $x_{\text{ent}}$.
- **[EQUATION_REGISTRY.md](file:///d:/TARS/TarsEx/docs/EQUATION_REGISTRY.md)**: Formal mathematical definitions of the 5 features.
- **[TARS_ARCHITECTURE.md](file:///d:/TARS/TarsEx/docs/TARS_ARCHITECTURE.md)**: Details the Stage 6 univariate logistic model parameters ($\beta_0 = 0.5410$, $\beta_1 = 0.1582$).
- **[CALIBRATION_ANALYSIS.md](file:///d:/TARS/TarsEx/docs/CALIBRATION_ANALYSIS.md)**: Formulates Expected Calibration Error (ECE).
- **[SENSITIVITY_ANALYSIS.md](file:///d:/TARS/TarsEx/docs/SENSITIVITY_ANALYSIS.md)**: Formulates Conditional Mutual Information (CMI).

---

## 2. Key Evidence & Statistics to Extract
- The exact definitions and mathematical formulas for the 5 sub-features:
  1. **Stability ($x_{\text{stab}}$)**:
     $$x_{\text{stab}} = N_{\text{final}}$$
     where $N_{\text{final}}$ is the count of final period candidates surviving.
  2. **Graph Entropy ($x_{\text{ent}}$)**:
     $$x_{\text{ent}} = H_D = -\sum_{k} p_k \log_2 p_k$$
     where $p_k = d_k / \sum_j d_j$, and $d_k$ is the degree of node $k$ in the alias graph.
  3. **Harmonic Density ($x_{\text{dens}}$)**:
     $$x_{\text{dens}} = \sum_{j \ne \text{top}} \mathbb{I}\left(\min_{r \in \{2, 3, 4, 5\}} \left| \frac{P_j}{P_{\text{top}}} - r \right| < \epsilon \text{ or } \left| \frac{P_{\text{top}}}{P_j} - r \right| < \epsilon \right)$$
     with $\epsilon = 0.05$.
  4. **Period Uniqueness ($x_{\text{uniq}}$)**:
     $$x_{\text{uniq}} = \min_{j \ne \text{top}, \text{non-alias}} \left| \frac{P_j - P_{\text{top}}}{P_{\text{top}}} \right|$$
  5. **Candidate Concentration ($x_{\text{conc}}$)**:
     $$x_{\text{conc}} = \frac{S(P_{\text{top}})}{\sum_{c} S(P_c)}$$
- The training set standardization parameters for the 5 features:
  - Stability ($x_{\text{stab}}$): $\mu_{\text{stab}} = 94.1109$, $\sigma_{\text{stab}} = 56.8703$
  - Graph Entropy ($x_{\text{ent}}$): $\mu_{\text{ent}} = 6.1386$, $\sigma_{\text{ent}} = 0.7046$
  - Harmonic Density ($x_{\text{dens}}$): $\mu_{\text{dens}} = 8.0670$, $\sigma_{\text{dens}} = 5.4733$
  - Period Uniqueness ($x_{\text{uniq}}$): $\mu_{\text{uniq}} = 0.0256$, $\sigma_{\text{uniq}} = 0.0271$
  - Candidate Concentration ($x_{\text{conc}}$): $\mu_{\text{conc}} = 0.0158$, $\sigma_{\text{conc}} = 0.0067$
  - Raw Index ($RAI_{\text{raw}}$): $\mu_{\text{RAI}} = 0.0$, $\sigma_{\text{RAI}} = 3.9542$
- The signed sum formula for the Raw RAI:
  $$RAI_{\text{raw}} = z_{\text{stab}} + z_{\text{ent}} + z_{\text{dens}} - z_{\text{uniq}} - z_{\text{conc}}$$
- The univariate logistic model linking $z_{\text{RAI}}$ to candidate reliability probability:
  $$z_{\text{RAI}} = \frac{RAI_{\text{raw}} - \mu_{\text{RAI}}}{\sigma_{\text{RAI}}}$$
  $$P(Y=1 \mid z_{\text{RAI}}) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 z_{\text{RAI}})}}$$
  where $\beta_0 = 0.5410$ and $\beta_1 = 0.1582$.

---

## 3. Missing Information
- None.

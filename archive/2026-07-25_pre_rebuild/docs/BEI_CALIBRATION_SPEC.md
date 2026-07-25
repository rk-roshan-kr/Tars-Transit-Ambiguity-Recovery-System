# BEI Calibration Specification

This document defines the formal calibration protocols for estimating the probability distributions $P(E|H)$ and $P(E|\neg H)$ for every feature admitted to the Bayesian Evidence Integration layer. No Bayes Factor may be implemented without an entry in this document.

---

## 1. Calibration Framework

A Bayes Factor requires two empirical or modelled distributions:

$$BF = \frac{P(E | H)}{P(E | \neg H)}$$

where:
- $H$: candidate is a physically real periodic astrophysical signal
- $\neg H$: candidate is a false positive (noise, systematic, eclipsing binary, or alias)

For Version 1 (Phase 10 implementation), distributions are estimated from **synthetic injection/recovery simulations** using TARS Stage 1–3 with controlled ground truth. In future phases these may be replaced by empirical Kepler/TESS/TOI population posteriors.

### Distribution Models

| Model | Use Case |
| :--- | :--- |
| **Beta distribution** $\text{Beta}(\alpha, \beta)$ | Bounded ratio metrics $\in [0, 1]$ |
| **Gamma distribution** $\text{Gamma}(k, \theta)$ | Strictly positive unbounded metrics |
| **Log-normal** $\text{LogNormal}(\mu, \sigma)$ | Positive right-skewed metrics (e.g. variance metrics) |
| **Empirical KDE** | When distribution shape is unknown; kernel density estimate on simulated samples |

---

## 2. Simulation Datasets

### Dataset SIM-P: Planet Population
- **Size**: 5,000 synthetic transit sequences
- **Period range**: $P \in [1.0, 50.0]$ days
- **Baseline**: $T \in [27.4, 365.25]$ days (TESS-equivalent)
- **SNR range**: $[3.5, 30.0]$
- **Timing jitter**: Gaussian $\sigma_t \sim U(10^{-4} P, 10^{-2} P)$
- **Completeness**: $W_{\text{comp}} \sim U(0.3, 1.0)$
- **Ground truth**: all candidates known to be real

### Dataset SIM-FP: False Positive Population
Composed of three sub-populations:
- **SIM-FP-A** (1,500): Poisson-distributed random events aligned by chance to a period
- **SIM-FP-B** (1,500): Eclipsing binary primary/secondary eclipse sequences at $P_{\text{true}}$ and $P_{\text{true}}/2$
- **SIM-FP-C** (1,000): Instrumental systematics — periodic momentum dump artifacts at known spacecraft frequencies

---

## 3. Calibration Entries by Admitted Feature

### CA-01: `coverage_fraction` (EV-T2)

| | |
| :--- | :--- |
| **Planet model** | $P(f | H) = \text{Beta}(\alpha_H, \beta_H)$; expected mean ~0.85 for well-recovered planets |
| **FP model** | $P(f | \neg H) = \text{Beta}(\alpha_{\neg H}, \beta_{\neg H})$; expected mean ~0.45 for random alignments |
| **Estimation** | Fit Beta distributions to SIM-P and SIM-FP coverage_fraction histograms using MLE |
| **Monotonicity** | Higher coverage $\Rightarrow$ higher $BF$ — confirmed by expected distribution separation |
| **Validation** | KS statistic between populations; target $> 0.6$ |

---

### CA-02: `residual_mad` (EV-T6)

| | |
| :--- | :--- |
| **Planet model** | $P(\text{mad} | H) = \text{Gamma}(k_H, \theta_H)$; expected small residuals for real orbits |
| **FP model** | $P(\text{mad} | \neg H) = \text{Gamma}(k_{\neg H}, \theta_{\neg H})$; larger and more scattered |
| **Estimation** | Fit Gamma distributions to SIM-P and SIM-FP residual_mad values using MLE |
| **Monotonicity** | Smaller MAD $\Rightarrow$ higher $BF$ — requires inverted likelihood ratio |
| **Validation** | Cohen's $d$ between populations; target $> 1.0$ |

---

### CA-03: `baseline_span` (EV-T3)

| | |
| :--- | :--- |
| **Planet model** | Uniform over observational baseline; informative only in conjunction with period |
| **FP model** | Same distribution by design of simulation |
| **Decision** | **Weakly informative.** $BF \approx 1.0$ unless baseline is extremely short ($< 2P$). Model as threshold: $BF = 1.0$ for $T > 2P$; $BF = 0.5$ otherwise. |
| **Monotonicity** | Longer baseline $\Rightarrow$ higher baseline_period_ratio, already captured by CA-07 |
| **Note** | May be demoted to CONDITIONAL or combined with `baseline_period_ratio` |

---

### CA-04: `harmonic_order` (EV-H1)

| | |
| :--- | :--- |
| **Planet model** | Concentrated at order 1 (fundamental); orders 2, 3 indicate sub-harmonic detection |
| **FP model** | Elevated at non-unity orders (harmonic aliases of EB periods) |
| **Model** | Discrete probability table: $P(\text{order}=k | H)$ and $P(\text{order}=k | \neg H)$ from simulation |
| **Estimation** | Empirical frequency table from SIM-P and SIM-FP |
| **Monotonicity** | $\text{order} = 1 \Rightarrow$ highest $BF$; higher orders $\Rightarrow$ decreasing $BF$ |

---

### CA-05: `alias_family_size` (EV-H2)

| | |
| :--- | :--- |
| **Planet model** | $P(\text{size} | H)$: small families (1–3); real planets rarely generate extensive alias cascades |
| **FP model** | $P(\text{size} | \neg H)$: larger families; EBs and systematics generate many period multiples |
| **Model** | Poisson or negative binomial; fit from simulation |
| **Monotonicity** | Larger family $\Rightarrow$ lower $BF$ (ambiguity burden) |

---

### CA-06: `uncertainty_ratio` (EV-S3)

| | |
| :--- | :--- |
| **Planet model** | $P(\sigma_P/P | H) = \text{LogNormal}(\mu_H, \sigma_H)$; real planets have tight period constraint |
| **FP model** | $P(\sigma_P/P | \neg H) = \text{LogNormal}(\mu_{\neg H}, \sigma_{\neg H})$; broad, uncertain periods |
| **Estimation** | Fit log-normal to SIM-P and SIM-FP uncertainty_ratio samples |
| **Monotonicity** | Smaller uncertainty ratio $\Rightarrow$ higher $BF$ |

---

### CA-07: `baseline_period_ratio` (EV-I2)

| | |
| :--- | :--- |
| **Planet model** | Higher ratios enable better period constraint; informative above ratio = 3 |
| **FP model** | Similar distribution by construction; BF contribution mainly through edge effects |
| **Model** | Sigmoid threshold model: $BF = 1 + \tanh((r - r_0)/\sigma_r)$ where $r_0 \approx 3$, calibrated from simulation |
| **Monotonicity** | Higher ratio $\Rightarrow$ higher $BF$ |

---

### CA-08: `family_complexity` (EV-I4)

| | |
| :--- | :--- |
| **Planet model** | $P(\text{complexity} | H)$: low complexity (few candidates per family) for clean detections |
| **FP model** | $P(\text{complexity} | \neg H)$: higher complexity; confused or crowded period families |
| **Model** | Poisson or empirical frequency table |
| **Monotonicity** | Higher complexity $\Rightarrow$ lower $BF$ |

---

### CA-09: `window_completeness` (EV-O3)

| | |
| :--- | :--- |
| **Planet model** | $P(W | H) = \text{Beta}(\alpha_H, \beta_H)$; high completeness expected for confirmed cadence |
| **FP model** | $P(W | \neg H) = \text{Beta}(\alpha_{\neg H}, \beta_{\neg H})$; gap artifacts may produce low completeness |
| **Estimation** | Fit Beta to SIM-P and SIM-FP window_completeness values |
| **Monotonicity** | Higher completeness $\Rightarrow$ higher $BF$ |

---

### CA-10: `period_duration_consistency` (EV-P1)

| | |
| :--- | :--- |
| **Planet model** | $P(\text{cons} | H) = \text{Beta}(\alpha_H, \beta_H)$; high consistency for real Keplerian orbits |
| **FP model** | $P(\text{cons} | \neg H) = \text{Beta}(\alpha_{\neg H}, \beta_{\neg H})$; low or random consistency |
| **Missing data** | When `None`: $BF = 1.0$ (no evidence contributed) |
| **Monotonicity** | Higher consistency $\Rightarrow$ higher $BF$ |

---

### CA-11: `chain_coherence` (EV-P3)

| | |
| :--- | :--- |
| **Planet model** | $P(\phi | H) = \text{Beta}(\alpha_H, \beta_H)$; high chain coherence for real periodic signals |
| **FP model** | $P(\phi | \neg H) = \text{Beta}(\alpha_{\neg H}, \beta_{\neg H})$; lower coherence for aliases or noise |
| **Monotonicity** | Higher coherence $\Rightarrow$ higher $BF$ |

---

### CA-12: `transit_spacing_regularity` (EV-P5)

| | |
| :--- | :--- |
| **Planet model** | $P(\text{var} | H) = \text{LogNormal}(\mu_H, \sigma_H)$; very low variance for Keplerian orbits |
| **FP model** | $P(\text{var} | \neg H) = \text{LogNormal}(\mu_{\neg H}, \sigma_{\neg H})$; wider spread |
| **Calibrated threshold** | $0.010$ (Phase 8.1); KS = 0.971, Cohen's $d$ = 2.21 |
| **Monotonicity** | Lower variance $\Rightarrow$ higher $BF$ |

---

### CA-13: `transit_number_monotonicity` (EV-P6)

| | |
| :--- | :--- |
| **Planet model** | $P(m | H) = \text{Beta}(\alpha_H, \beta_H)$; near-unity for well-ordered Keplerian sequence |
| **FP model** | $P(m | \neg H)$: lower monotonicity fraction for mis-ordered or alias-contaminated events |
| **Monotonicity** | Higher fraction $\Rightarrow$ higher $BF$ |

---

### CA-14–16: Morphology (`depth_consistency`, `duration_consistency`, `shape_consistency`)

| | |
| :--- | :--- |
| **Planet model** | $\text{Beta}(\alpha_H, \beta_H)$; high consistency expected for stable planetary occultation |
| **FP model** | $\text{Beta}(\alpha_{\neg H}, \beta_{\neg H})$; lower consistency for EBs (alternating depths), systematics |
| **Missing data** | When `None` (N < 2): $BF = 1.0$ |
| **Monotonicity** | Higher consistency $\Rightarrow$ higher $BF$ |

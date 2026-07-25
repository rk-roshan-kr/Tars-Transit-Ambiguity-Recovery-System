# Measurement Trust Audit

*Phase 5.4 — Component C. Audits every Phase 5.1–5.3 metric for computation integrity, measurement validity, and trust classification.*

---

## Methodology

Every metric in Phases 5.1–5.3 is evaluated on four axes:
- **Computed**: Was it derived from actual calculation at runtime?
- **Assumed**: Were any constants hard-wired into the measurement?
- **Simulated**: Did the data used to compute it come from a synthetic simulator?
- **Trust Level**: Final classification based on the above.

---

## Metric Trust Table

| Metric | Computed? | Assumed? | Simulated? | Trust Level | Notes |
| :--- | :---: | :---: | :---: | :--- | :--- |
| **Harmonic Confusion Matrix** | YES | NO | YES | `HIGH_TRUST` | Controlled injection, deterministic seeds. |
| **N50/N90 Identifiability Boundary** | YES | NO | YES | `HIGH_TRUST` | Sweep over N, clearly defined pass criterion. |
| **Gap-Induced Alias Rate** | YES | NO | YES | `HIGH_TRUST` | Gap fraction varied systematically; alias rate directly measured. |
| **Timing Noise Correct Rate** | YES | NO | YES | `HIGH_TRUST` | sigma_t varied over 5 decades, deterministic outcome. |
| **Baseline Length Influence** | YES | NO | YES | `HIGH_TRUST` | All 100% correct — clean regime with no gaps. Likely a ceiling effect. |
| **1-sigma Uncertainty Coverage** | YES | NO (filtered) | YES | `MEDIUM_TRUST` | Filtering to correct-mode-only recoveries is scientifically valid but introduces selection bias. |
| **2-sigma Uncertainty Coverage** | YES | NO (filtered) | YES | `MEDIUM_TRUST` | Same selection bias concern as 1-sigma. |
| **Correct Top-Rank Rate (5.2)** | YES | NO | YES | `HIGH_TRUST` | 79.3% — directly computed from CSV. |
| **Case A Generator Failure Rate** | YES | NO | YES | `HIGH_TRUST` | Boolean presence check. Robust measurement. |
| **Case B Ranking Failure Rate** | YES | NO | YES | `HIGH_TRUST` | Rank > 1 for true period. Robust. |
| **TTV Correct Rate (60 min)** | YES | NO | YES | `HIGH_TRUST` | Linearly injected TTV; clean measurement. |
| **Multi-Planet Contamination Rate** | YES | NO | YES | `MEDIUM_TRUST` | 100% contamination for 10/15d pair is plausible but may reflect simulator construction rather than fundamental math. |
| **Top-1 Recall (Phase 5.3)** | YES | NO | YES (Pop. A+B) | `MEDIUM_TRUST` | Depends on realism of Stage 2 loss simulation. Not measured on real TESS data. |
| **Top-3 Recall (Phase 5.3)** | YES | NO | YES (Pop. A+B) | `MEDIUM_TRUST` | Same caveat as Top-1. |
| **Top-5 Recall (Phase 5.3)** | YES | NO | YES (Pop. A+B) | `MEDIUM_TRUST` | Population-consistent across seeds. |
| **Family Recall (Phase 5.3)** | YES | NO | YES (Pop. A+B) | `MEDIUM_TRUST` | 70.7% — architecturally meaningful, but still synthetic input. |
| **Transfer Efficiency (Phase 5.3)** | YES | NO | YES | `MEDIUM_TRUST` | Transfer loss modeled via logistic curve centered at SNR=7.1. The 7.1 cutoff is a parameter choice, not an empirically fitted value. |
| **MRR (Phase 5.3)** | YES | NO | YES | `MEDIUM_TRUST` | Correct formula, but rank distribution is driven by heuristic weights — circular measurement if we are evaluating those same weights. |
| **Median True Rank (Phase 5.3)** | YES | NO | YES | `HIGH_TRUST` | Raw rank distribution; no weighting assumptions. |
| **Class A/B/C Failure Breakdown** | YES | NO | YES | `HIGH_TRUST` | Classification logic is deterministic and rule-based. |
| **Ambiguity Flag Rate** | YES | NO | YES | `MEDIUM_TRUST` | Flag is triggered by score_delta threshold — depends on heuristic weight. |
| **Runtime Scaling** | YES | NO | YES | `HIGH_TRUST` | Direct timer measurement. |
| **False Recovery Rate (FP targets)** | YES | NO | YES | `MEDIUM_TRUST` | Depends on EB alternating-depth model being realistic. |
| **Variable Star Contamination Rate** | YES | NO | YES | `LOW_TRUST` | Sinusoidal mock does not capture real astrophysical variability (spots, limb darkening, convection patterns). |

---

## Summary

| Trust Level | Count | Fraction |
| :--- | :---: | :---: |
| `HIGH_TRUST` | 12 | 48% |
| `MEDIUM_TRUST` | 10 | 40% |
| `LOW_TRUST` | 1 | 4% |
| `INVALID` | 0 | 0% |

**Overall assessment**: The measurement framework is honest and computationally solid. No metric is invalid. The primary limitation is systematic: all Phase 5.2–5.3 measurements are synthetic and cannot replace real TESS validation. The Transfer Efficiency (68%) and Family Recall (70.7%) numbers should be treated as directionally informative, not as publication-ready ground-truth values.

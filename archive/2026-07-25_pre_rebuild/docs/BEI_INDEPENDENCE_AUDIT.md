# BEI Independence Audit (Phase 10.1)

This report evaluates the conditional independence assumption of Stage 6 Naive Bayes Evidence Integration. We quantify the information-theoretic dependencies between all 16 admitted features using Pearson, Spearman, Mutual Information (MI), and Conditional Mutual Information (CMI).

---

## 1. Independence Verdict Rule

We establish the following objective criteria for the Naive Bayes assumption:

| Verdict | Condition | Status |
| :--- | :--- | :---: |
| **PASS** | 0 feature pairs exceed the CMI Review threshold ($\text{CMI} \ge 0.25$ bits) | — |
| **CONDITIONAL PASS** | 1–3 feature pairs exceed the CMI Review threshold but are physically justified | **ACHIEVED** |
| **FAIL** | $>3$ feature pairs exceed the CMI Review threshold or remain undocumented | — |

---

## 2. Verdict Summary: CONDITIONAL PASS

The audit analyzed all $120$ unique feature pairs. 

* **PASS** ($\text{CMI} < 0.10$ bits): **116 pairs**
* **WARN** ($0.10 \le \text{CMI} < 0.25$ bits): **3 pairs**
* **REVIEW REQUIRED** ($\text{CMI} \ge 0.25$ bits): **1 pair**

Because exactly **1 pair** exceeded the CMI review threshold, the system receives a **CONDITIONAL PASS**, contingent on the physical justification of the flagged dependency.

---

## 3. Flagged Feature Dependencies

| Feature 1 | Feature 2 | CMI (bits) | Status | Physical Justification / Action |
| :--- | :--- | :---: | :---: | :--- |
| `depth_consistency` | `duration_consistency` | 0.278 | **REVIEW** | Both are morphological metrics measuring TESS light curve transit geometry. High correlation is physically expected because transit misalignments affect both transit depth and duration. **Justification**: Admitted because their combined physical separation signal exceeds the minor double-counting risk (confirmed in ablation study). |
| `duration_consistency` | `shape_consistency` | 0.216 | **WARN** | Morphological metrics. Coherence of duration weakly couples with shape symmetry. Safe to retain. |
| `depth_consistency` | `shape_consistency` | 0.161 | **WARN** | Morphological metrics. Safe to retain. |
| `coverage_fraction` | `window_completeness` | 0.135 | **WARN** | Temporal support vs gap fraction completeness. Weak correlation. Safe to retain. |

---

## 4. Key Takeaways

1. **High Conditional Independence**: $96.7\%$ of feature pairs ($116/120$) show negligible conditional dependency ($\text{CMI} < 0.10$ bits), strongly validating the Naive Bayes product model.
2. **Morphology Clustering**: The only non-trivial dependency resides in the Stage 5 ECHO Morphology family. This clustering does not threaten pipeline validity, but should be noted as a calibration baseline for future models.

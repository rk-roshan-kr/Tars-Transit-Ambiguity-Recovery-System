# TARS Core — Benchmark Policy

Every performance claim requires a comparison. "Better than what?" must always have a definitive answer.

---

## Required Baselines

TARS Core must be evaluated against the following four baselines. A result without a comparison is not a publishable result.

---

### Baseline A — BLS (Box Least Squares)

**Reference:** Kovács, Zucker & Mazeh (2002)

**Why:** BLS is the standard discovery algorithm for transit detection. It represents the industry baseline for periodic transit search.

**Mode of comparison:** Run BLS on the same validation set, with the same detection threshold. Compare precision, recall, and F1 directly against TARS Core.

**Expected outcome:** BLS recall >> TARS recall (BLS is a discovery engine). TARS precision >> BLS precision (TARS is a validation pipeline). This is not a failure — it is the expected operating point difference.

---

### Baseline B — TLS (Transit Least Squares)

**Reference:** Hippke & Heller (2019)

**Why:** TLS improves on BLS by using a physical transit shape model. It is a more direct competitor to the transit detection component.

**Feasibility note:** TLS is computationally expensive. If benchmark runs exceed reasonable time limits (> 10× TARS execution time), report timing comparison alongside performance metrics.

---

### Baseline C — Physics-Only (No ML)

**Description:** TARS Core Stages 1–5 only, with Stage 6 (ML) completely disabled. ML score is set to neutral (0.5).

**Why:** This directly tests H2. Isolates the contribution of physics and statistics without any learned component.

**Implementation:** Built into Experiment 6 (ML Ablation). No external code required.

---

### Baseline D — ML-Only (No Physics)

**Description:** XGBoost classifier on raw features only, with no physics vetting (EEA and ECHO disabled). Standard train/val/test split.

**Why:** This is the "naive ML" baseline that TARS Core must outperform in precision. If TARS Core does not outperform ML-only in precision, the physics layer provides no value.

**Implementation:** Built into Experiments 4 + 5 (Physics Ablation). No external code required.

---

## Reporting Policy

For every baseline comparison, report:

| Metric | TARS Core | Baseline |
|---|---|---|
| Precision ± 95% CI | | |
| Recall ± 95% CI | | |
| F1-Score ± 95% CI | | |
| AUC | | |
| Execution time (s/TIC) | | |

---

## Benchmark Philosophy

> TARS Core does not claim to be the best recall engine. It claims to be the most reliable precision engine in the sparse-transit regime.

Benchmarks must be framed accordingly. A reviewer who criticizes TARS Core's low recall without acknowledging its precision-first design philosophy is misunderstanding the operating point.

The benchmark comparison table must appear in the paper alongside a clear statement of the intended operating regime.

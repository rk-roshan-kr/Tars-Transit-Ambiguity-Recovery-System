# TARS Core — Scientific Hypotheses

A scientific project must be falsifiable. This document defines the hypotheses TARS Core explicitly tests, and the conditions under which each would be falsified.

Without hypotheses, you have experiments but not science.

---

## H1 — Physics + Statistics outperforms statistics alone

**Claim:** Adding physics constraints (EEA + ECHO) to the statistical evidence layer produces a measurably higher precision than the statistical layer alone.

**Test:** Experiments 4, 5, 8 (Physics Ablation: EEA, ECHO, Statistical Layer)

**Falsification condition:**
> H1 is falsified if removing EEA and ECHO produces precision ≥ precision of the full pipeline on the validation split, within the 95% confidence interval.

---

## H2 — Physics + Statistics outperforms ML alone

**Claim:** The physics validation layer (Stages 1–4) achieves higher catalog precision than an ML-only classifier trained on the same data.

**Test:** Experiment 6 (ML Ablation), Baseline D (ML-only benchmark)

**Falsification condition:**
> H2 is falsified if the ML-only baseline achieves precision ≥ the physics+statistics pipeline precision, within the 95% confidence interval.

**Why this matters:** This directly validates the "Physics > ML" hierarchy that is the defining principle of TARS Core.

---

## H3 — Sparse-transit recovery remains viable at N=2

**Claim:** The pairwise period search recovers valid orbital periods for N=2 candidates at an accuracy sufficient for follow-up prioritization.

**Test:** Experiment 2 (Sparse Transit Scaling), Experiment 3 (Period Recovery Accuracy)

**Falsification condition:**
> H3 is falsified if N=2 period recovery rate (within 30-minute tolerance) falls below 50% on the injection dataset, or if N=2 precision is statistically indistinguishable from random chance.

---

## H4 — ECHO rejects false positives more efficiently than random filtering

**Claim:** The ECHO Geometric Consistency Proxy selectively rejects astrophysical and instrumental false positives at a rate significantly above the rate expected by random candidate elimination.

**Test:** Dataset B (Known False Positives), Experiment 5 (ECHO Ablation)

**Falsification condition:**
> H4 is falsified if the ECHO false-positive rejection rate on Dataset B (Known FPs) is not statistically significantly higher than the rejection rate on Dataset A (Known TOIs), at p < 0.05.

---

## Hypothesis Testing Policy

- All hypothesis tests use the stratified validation split only
- Test split is reserved for final confirmation after hypotheses are settled
- All tests require 95% bootstrap confidence intervals (1,000 resamples, seed=42)
- A hypothesis is "supported" only if the effect survives the 95% CI — not just point estimates

# TARS Stage 3: Original Vision Reconstruction

*Phase 5.4 — Component A. Reconstructed from all architecture, novelty, hypothesis, and reviewer defense documents. No algorithm changes were made in generating this document.*

---

## What Problem Was TARS Trying to Solve?

Traditional exoplanet period recovery algorithms — Box Least Squares (BLS), Transit Least Squares (TLS), and Lomb-Scargle (LS) — operate by folding the *entire continuous flux array* over a dense frequency grid to accumulate transit signal. This approach fails characteristically in one specific regime:

**The Sparse Multi-Sector TESS Regime.**

When a planet's period is long (e.g., 15–40 days), TESS observes only 2–4 transits in a standard 27-day sector. When multi-sector baselines extend that to 2–3 years with year-scale sector gaps, BLS/TLS must fold enormous empty gap-space into their signal averages, dramatically diluting detection significance. TARS was designed to operate in precisely this regime — not by ignoring the problem, but by operating in a fundamentally different mathematical domain.

---

## What Assumptions Motivated Event-Space Reasoning?

The foundational TARS assumption is:

> *If Stage 2 successfully detects individual transit events above threshold, those timestamps contain all the information necessary to reconstruct the orbital period — without needing the full flux array.*

This assumption holds when:
1. $N_{events} \geq 2$ — at least two distinct transit times exist.
2. Individual event SNR is high enough for Stage 2 to detect them.
3. Transit timing errors are small relative to the orbital period.

The implication is profound: rather than searching a dense frequency grid of $O(N_{cadences})$ points, TARS reconstructs an **admissible family** of period hypotheses from $O(N_{events}^2)$ pairwise interval differences — a fundamentally smaller search space when $N_{events} \ll N_{cadences}$.

---

## Why Was Cadence-Space Rejected?

Cadence-space algorithms (BLS, TLS) were rejected as the Stage 3 architecture for three specific reasons documented during Phase 4 design:

1. **Gap Dilution**: In multi-sector TESS data with year-scale gaps, folding the entire array includes vast regions of empty data that dilute signal power and produce elevated false alarm rates.
2. **Computational Domain Mismatch**: When $N_{events}$ is small (2–10), reconstructing from timestamps is computationally trivial ($O(N^2)$) compared to folding millions of cadences.
3. **Forced Continuity Assumption**: BLS and LS assume a quasi-continuous observation baseline. The TARS Stage 1 pipeline explicitly operates on *discontinuous* Conditioned Light Curves, and passing these to a continuous folding algorithm introduces documented artefact classes.

The decision was not that cadence-space folding is wrong — it is explicitly acknowledged as superior for ultra-low SNR — but that *for sparse, high-SNR, discontinuous TESS data, event-space reconstruction is the better-matched algorithm class*.

---

## What Scientific Gap Was Being Targeted?

The gap targeted is the **long-period, sparse-event recovery problem for short-baseline space telescopes**.

TESS single-sector baselines are 27 days. A planet with a 20-day period has at most 1–2 transits per sector. Multi-sector revisits may extend baselines to years, but with multi-month year-scale gaps. No existing pipeline was specifically architectured to handle the *3–8 transit, year-scale gap, sparse-evidence* regime as its primary design target.

---

## What Evidence Would Prove Success?

From `SCIENTIFIC_OBJECTIVES_STAGE3.md`, the following Research Questions constitute the proof criteria:

- **RQ-1**: Family Recall $\geq 90\%$ for $N_{events} \geq 2$ systems.
- **RQ-2**: Successful period recovery with missing transits (gaps up to 75% of expected).
- **RQ-3**: False recovery rate on false-positive targets $< 15\%$.
- **RQ-4**: Correct period recovery across multi-sector TESS gaps.
- **RQ-5**: Explicit quantification of where TARS outperforms and underperforms BLS/TLS.
- **RQ-6**: Harmonic disambiguation success rate $> 85\%$ for $N_{events} \geq 3$.

---

## What Evidence Would Falsify the Idea?

The TARS event-space hypothesis would be formally falsified if:

1. **Family Recall < 70%** under realistic Stage 2 loss conditions — proving the generator cannot produce the right period at all.
2. **Class A (Generator Failure) > 25%** — proving the interval algebra itself is missing the true period, not just ranking it wrong.
3. **Transfer Efficiency < 30%** — proving Stage 2 destroys too much information for Stage 3 to have any usable input.
4. **False Positive Recovery Rate > 50%** — proving Stage 3 cannot distinguish periodic signals from random events.

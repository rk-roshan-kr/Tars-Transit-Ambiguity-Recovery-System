# TARS Core — Scientific Objectives

> TARS Core is a physics-constrained experimental framework for studying sparse-transit exoplanet vetting, where the detector is only one component of the scientific investigation.

---

## What TARS Core Is NOT

TARS Core is not simply "a detector." It is a scientific investigation into the fundamental limits of sparse-transit validation. Every module, formula, and experiment exists to answer one or more of the objectives below.

---

## Objective 1

**Can sparse transit chains be recovered without phase folding?**

Traditional BLS and TLS assume many transits and rely on phase folding to build statistical power. TARS Core operates where this assumption breaks down: N=2, N=3, N=4.

- What is the minimum event count required for reliable period recovery?
- What is the period recovery accuracy as a function of N?
- At what N does the pipeline become competitive with classical methods?

---

## Objective 2

**Can physics constraints improve candidate quality over purely statistical ranking?**

The central thesis of TARS Core is that physical consistency checks (EEA, ECHO) provide a better discrimination signal than statistical ranking alone in the sparse-transit regime.

- Does adding physics constraints increase precision?
- Does the physics layer recover candidates that ML alone misses?
- Is the EEA "gray rescue" mechanism statistically significant?

---

## Objective 3

**Can geometry-based vetting reduce false positives in short-baseline observations?**

Short-baseline surveys (27.4-day TESS sectors) are dominated by systematic noise that mimics transit morphology. The ECHO Geometric Consistency Proxy exists to exploit physical constraints that are impossible for statistical classifiers to learn.

- What is the false-positive rejection rate of ECHO alone?
- How does it compare to ML-only vetting?
- What classes of false positives does ECHO catch that ML misses?

---

## Objective 4

**What limits sparse-transit recovery?**

Understanding failure modes is as important as maximizing performance. This objective maps the recovery limits across four axes:

- **Noise:** At what SNR does the pipeline fail?
- **Geometry:** Which transit shapes cause ECHO to over-reject?
- **Period ambiguity:** At what period does pairwise search become degenerate?
- **Event count:** How does performance degrade from N=6 down to N=2?

---

## Objective 5

**What information contributes most to successful vetting?**

A systematic ablation study across all pipeline components directly tests which modules carry the most discriminative power. This validates the Physics > Statistics > ML hierarchy.

- Does removing EEA degrade performance? By how much?
- Does removing ECHO degrade performance? By how much?
- Does removing ML degrade performance? By how much?
- Can physics alone (no ML) achieve acceptable precision?

The answers to these questions either confirm or challenge the core TARS philosophy.

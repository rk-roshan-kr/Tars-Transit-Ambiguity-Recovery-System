# Phase 15 Recommendation: Scientific Representation Redesign

Based on the 14 Phase 14.0 scientific audits, we recommend selecting **PATH C: Scientific Representation Redesign**.

## 1. Selected Path

### **PATH C: Scientific Representation Redesign**

## 2. Justification & Supporting Evidence

- **Physical Decoupling**: Audit 14.6 demonstrated that our feature space is physically decoupled from the fundamental exoplanetary parameters (period, depth, duration).
- **Heuristic Equivalence**: Audit 14.8B showed that a simple, untrained human heuristic score matches or approaches the performance of the trained Model C. This proves that the machine learning classifier is not extracting any additional learnable information from the current representation.
- **Feature Redundancy**: Audit 14.2 demonstrated that the feature space is extremely low-dimensional and redundant, with 3 constant features and a low effective rank.

## 3. Expected Performance Gain

- **Target AUROC Gain**: +0.20 to +0.25 (achieving a blind split AUROC of 0.80+).
- **Explanation**: By redesigning the features to directly capture physical morphology, noise statistics, and sparse-transit geometry, we can resolve the bottleneck currently limiting all classifiers to ~0.60 AUROC.

## 4. Risk Analysis

- **Risk 1 (Feature Drift)**: New features may introduce additional domain shift between sectors. *Mitigation*: Include robust normalization layers based on stellar noise characteristics.
- **Risk 2 (Computational Complexity)**: Higher physical fidelity might increase feature extraction latency. *Mitigation*: Implement optimized, vectorised transit folding algorithms.

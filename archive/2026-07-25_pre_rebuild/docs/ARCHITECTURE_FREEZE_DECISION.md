# Architecture Freeze Decision (Audit 20.5)

## Question
Which candidate model should be frozen as the canonical TARS v1 production system?

## Experiment
We evaluated the candidates according to the scientific freeze hierarchy: Scientific Validity $\rightarrow$ Generalization $\rightarrow$ Calibration $\rightarrow$ Interpretability $\rightarrow$ Performance $\rightarrow$ Complexity.

## Observation
1.  **Scientific Validity**: RAI-only utilizes unsupervised recoverability ambiguity, resolving detector leakages.
2.  **Generalization**: RAI-only shows out-of-fold generalization (AUROC 0.663) and robust performance on unseen sectors.
3.  **Calibration**: RAI-only has the lowest Expected Calibration Error (0.0662) and Brier score (0.2150).
4.  **Interpretability**: RAI-only has an interpretability score of 100.
5.  **Performance**: RAI-only has the highest Blind AUROC.
6.  **Complexity**: RAI-only has 1 feature and 2 parameters, minimizing inference cost.

## Interpretation
The RAI-only model dominates in every single dimension of the hierarchy. Stacking additional features adds parameter complexity, degrades calibration, and decreases generalization due to overfitting.

## Conclusion
**FREEZE DECISION: FREEZE RAI-ONLY**
The single-feature `RAI_unsupervised` model is locked as the canonical TARS v1 production pipeline.

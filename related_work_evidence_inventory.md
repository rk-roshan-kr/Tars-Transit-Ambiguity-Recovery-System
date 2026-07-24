# Evidence Inventory: Related Work

## 1. Relevant Repository Documents
- **[REVIEWER_ATTACK_MATRIX.md](file:///d:/TARS/TarsEx/docs/REVIEWER_ATTACK_MATRIX.md)**: Highlights vulnerabilities in deep learning and FPP-based pipelines (such as Vespa/Triceratops) and maps how TARS addresses them.
- **[NOVELTY_DEFENSE.md](file:///d:/TARS/TarsEx/docs/NOVELTY_DEFENSE.md)**: Details the comparative positioning of TARS against classical rule-based and deep learning vetting models.
- **[MISSING_NOVELTY_AUDIT.md](file:///d:/TARS/TarsEx/docs/MISSING_NOVELTY_AUDIT.md)**: Establishes comparisons with prior Kepler-era pipeline statistics.

---

## 2. Key Evidence & Statistics to Extract
- The main comparative paradigms of exoplanet candidate vetting:
  - **Rule-based heuristic vetting**: Hard decision boundaries, lack of probability calibration (e.g. Kepler Robovetter).
  - **False Positive Probability (FPP) estimation**: Physical blend scenarios, high computational cost (e.g. Vespa, Triceratops).
  - **Deep learning classifiers**: High raw performance, black-box predictions, severe calibration degradation under dataset shifts (e.g. Astronet).
- The definition of Table 1 (Novelty Matrix comparison).
- Clear identification of the **Novelty Guard**: how TARS v1 differs specifically from these methods (focuses on *epistemic signal recovery ambiguity* rather than dispositional class likelihood, with an order-of-magnitude reduction in feature count and full interpretability).

---

## 3. Missing Information
- None.

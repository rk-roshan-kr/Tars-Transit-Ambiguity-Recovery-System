# TARS v1 Equation Code Map

This map connects every mathematical equation in the TARS v1 paper to the exact python function and source file that implements it in the codebase.

---

| Equation ID | Equation Name | Implementation Function | Source File | Line Number |
| :---: | :--- | :--- | :--- | :---: |
| **E-01** | Degree-based Normalized Shannon Entropy ($x_{\text{ent}}$) | `shannon_entropy()` (normalized by `np.log2(n_final)`) | `run_ambiguity_reconstruction.py` | L140 & L219 |
| **E-02** | Harmonic Matching Density ($x_{\text{hden}}$) | `harmonic_alias_count` edge loops | `run_ambiguity_reconstruction.py` | L159–171 |
| **E-03** | Period Uniqueness ($x_{\text{uniq}}$) | `period_uniqueness` search | `run_ambiguity_reconstruction.py` | L170 |
| **E-04** | Candidate Concentration ($x_{\text{conc}}$) | `candidate_concentration` ratio | `run_ambiguity_reconstruction.py` | L183 |
| **E-05** | Standardized signed sum index ($\text{RAI}_{\text{raw}}$) | `df_blind_full["RAI_unsupervised"]` & `compute_custom_rai()` | `run_publication_readiness.py` | L148 & L251 |
| **E-06** | Logistic Calibration Link | `predict_proba` call on `lr_rai` | `run_publication_readiness.py` | L157 |
| **E-07** | Expected Calibration Error (ECE) | `expected_calibration_error()` | `run_publication_readiness.py` | L60–74 |
| **E-08** | Conditional Mutual Information (CMI) | `prod_conditional_mutual_information()` | `run_publication_readiness.py` | L46–54 |

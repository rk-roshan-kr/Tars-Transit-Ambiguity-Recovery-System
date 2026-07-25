# Stage 3: Dataset Specification

The following benchmark datasets are required to execute the Stage 3 experiments and audits. 

---

### Dataset A: Confirmed Planets
* **Composition**: Real TESS light curves containing known, confirmed exoplanets with established orbital periods.
* **Purpose**: Verifies that the recovery engine can correctly derive standard periods from real data artifacts.

### Dataset B: False Positives
* **Composition**: Real TESS light curves of known eclipsing binaries, background eclipsing binaries, and variable stars that trigger Stage 2 but do not represent simple planetary periods.
* **Purpose**: Tests the robustness of the consensus ranking and its ability to down-weight alias-heavy false positive scenarios.

### Dataset C: Random Noise Stars
* **Composition**: Quiet stars with pure Gaussian or AR(1) noise profiles, yielding only false-alarm candidate events in Stage 2.
* **Purpose**: Provides a baseline for evaluating the absolute False Alarm Period rate.

### Dataset D: Synthetic Injections
* **Composition**: Clean or noise-injected theoretical light curves with precisely controlled artificial transits (varying depth, duration, and $P$).
* **Purpose**: Enables exact ground-truth comparison for timing residuals, phase errors, and algorithmic correctness.

### Dataset E: Sparse Regime Injections
* **Composition**: Highly curated synthetic dataset specifically constructed to isolate sparse recovery limits.
  * **2-Transit Case**: Only 2 transits separated by large gaps.
  * **3-Transit Case**: 3 transits, testing missing interior epochs.
  * **4-Transit Case**: 4 transits, testing harmonic alias breaking.
* **Purpose**: Direct evaluation of RQ-1 and H3-4 (ultra-sparse functionality).

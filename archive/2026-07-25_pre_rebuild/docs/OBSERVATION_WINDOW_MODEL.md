# Stage 3: Observation Window Model

To correctly evaluate harmonic aliases and calculate `coverage_fraction`, TARS must possess a formal understanding of when observations were occurring and when they were impossible.

## 1. Model Definitions

* **Observable Regions**: Continuous intervals of time where the telescope collected valid, non-flagged photometry.
* **Missing Regions**: Data gaps caused by momentum dumps, cosmic ray hits, or downlink interruptions within a sector.
* **Sector Boundaries**: Massive baseline gaps (often weeks or months) where the telescope pointed away from the target field.

## 2. Expected Transit Generator

To compute $N_{expected}$ for a proposed period hypothesis $P$ and epoch $t_0$:

1. Generate all theoretical transit times $t_m = t_0 + m P$ within the absolute bounds of the entire dataset $[\text{Time}_{min}, \text{Time}_{max}]$.
2. For each theoretical time $t_m$:
   * If $t_m$ falls within an **Observable Region**, increment `N_expected`.
   * If $t_m$ falls within a **Missing Region** or **Sector Boundary**, ignore it (it was impossible to observe).

## 3. Formal Coverage Fraction

The coverage fraction $C$ is rigorously defined as:
$$C = \frac{N_{observed\_and\_matched}}{N_{expected}}$$

This ensures that a 45-day period planet with 3 observed transits and 5 transit epochs lost to sector gaps achieves $C = 3/3 = 1.0$ (100% coverage of expected events), whereas an alias period that expected 6 observable transits but only matched 3 achieves $C = 3/6 = 0.5$, penalizing the alias appropriately.

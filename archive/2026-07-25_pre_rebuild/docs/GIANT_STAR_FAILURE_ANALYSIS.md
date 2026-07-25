# Audit 17.6 — Giant-Star Failure Analysis

Investigates the physical causes of model performance collapse on giant/subgiant hosts by comparing dwarfs against giants.

| Subgroup | Mean Event Count | Mean Graph Density | Mean Period Spacing | Mean Uniqueness Score | Mean Candidate Concentration |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Dwarfs** | 37.92 | 0.0821 | 0.2666 | 0.0277 | 0.0163 |
| **Giants** | 46.07 | 0.0899 | 0.2465 | 0.0228 | 0.0149 |

> [!WARNING]
> **PHYSICAL ROOT CAUSE**: Giant host stars have a higher mean event count and lower period spacing, leading to denser alias networks. Because giant star light curves are dominated by intrinsic convective noise and oscillations, the Stage 3 recoverer experiences severe event inflation and candidate multiplicity. This breaks the ambiguity-based period recovery assumptions and causes model failure.

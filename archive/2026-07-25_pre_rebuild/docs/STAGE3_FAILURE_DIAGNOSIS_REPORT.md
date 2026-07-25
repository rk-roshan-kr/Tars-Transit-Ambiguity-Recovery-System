# Stage 3 Alias Failure Diagnosis Report

## 1. Harmonic Failure Modes
| Class | Fraction (%) |
| :--- | :--- |
| CORRECT | 98.1 |
| DOUBLE_PERIOD | 1.9 |

## 2. Identifiability Boundary
- **N50 Boundary**: 2 transits required for 50% accuracy.
- **N90 Boundary**: 2 transits required for 90% accuracy.

## 3. Gap-Induced Aliasing
| Gap Fraction | Alias Rate (%) |
| :--- | :--- |
| 0% | 0.0 |
| 10% | 0.0 |
| 25% | 0.4 |
| 50% | 2.0 |
| 75% | 1.4 |
| 90% | 49.8 |

## 4. Timing Precision Stress Test
| Sigma_t (days) | Correct Rate (%) |
| :--- | :--- |
| 0.0001 | 100.0 |
| 0.001 | 100.0 |
| 0.005 | 100.0 |
| 0.01 | 98.2 |
| 0.02 | 80.2 |
| 0.05 | 49.0 |

## 5. Baseline Length Influence
| Baseline/P Ratio | Correct Rate (%) |
| :--- | :--- |
| 2x | 100.0 |
| 3x | 100.0 |
| 5x | 100.0 |
| 10x | 100.0 |
| 20x | 100.0 |
| 50x | 100.0 |

## 6. Uncertainty Calibration
Evaluating strictly for correctly identified modes:
- 1σ Coverage: 70.8% (Expected: ~68%)
- 2σ Coverage: 94.6% (Expected: ~95%)
- 3σ Coverage: 100.0% (Expected: ~99.7%)

## 7. Candidate Ranking Analysis
- **Correct Top Rank**: 79.3%
- **Case A (Generator Failure - True Period Absent)**: 8.4%
- **Case B (Ranking Failure - True Period Misranked)**: 12.3%

## 8. Multi-Planet Alias Contamination
| Planet Pair (days) | Found A (%) | Found B (%) | Cross Contamination (%) |
| :--- | :--- | :--- | :--- |
| 10.0 / 15.0 | 0.0 | 0.0 | 100.0 |
| 12.0 / 24.0 | 0.0 | 0.0 | 0.0 |
| 20.0 / 40.0 | 0.0 | 0.0 | 0.0 |

## 9. Transit Timing Variation (TTV) Stress Test
| TTV Amplitude (mins) | Correct Rate (%) |
| :--- | :--- |
| 0 | 100.0 |
| 2 | 100.0 |
| 5 | 100.0 |
| 10 | 100.0 |
| 20 | 99.2 |
| 60 | 72.6 |

## 10. Final Diagnosis
> **Is the dominant failure caused by information-theoretic ambiguity or implementation defects?**

**Conclusion**: The primary failure mode is an **Implementation Defect (Ranking Failure)**. The generator successfully produces the true period, but the heuristic scoring algorithm incorrectly prioritizes aliases (P/2 or 2P) above it. The Stage 3 architecture requires a formal mathematical revision of its ranking heuristic.

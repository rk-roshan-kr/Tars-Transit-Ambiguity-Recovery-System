# Simulation Validity Statement

Because Phase 5.3 relies on a simulated realistic population of TESS targets rather than direct active queries to the MAST TOI database, this document explicitly justifies all physical and statistical distributions used in `research/realistic_tess_catalog.py`. 

This guarantees the simulation does not artificially favor the TARS architecture.

## 1. Population Sizing
* **Size**: Minimum $N = 1000$ per class (Confirmed Planets, False Positives, Variable Stars).
* **Justification**: $N=1000$ guarantees the 95% bootstrap confidence interval width on recall metrics is $\leq 3\%$, providing a highly stable statistical estimator.
* **Source**: Standard statistical sampling practice for rare-event detection classification.

## 2. Period Distribution
* **Range**: Log-uniform between 1.0 and 40.0 days.
* **Justification**: Known TESS yield is heavily biased toward short periods ($P < 10$ days) due to geometric transit probability and the standard 27-day sector baseline. Log-uniform sampling physically accurately simulates this bias while ensuring long-period ($>25$ day) single-transit or dual-transit outliers exist.
* **Source**: NASA Exoplanet Archive (TESS Confirmed Planet properties).

## 3. Transit Count Distribution
* **Range**: $N_{transits} \in [2, 30]$ based on $P_{true}$ and observation baseline.
* **Justification**: A continuous 27-day observation will yield ~27 transits for a 1-day period, and ~2 transits for a 13.5-day period. 
* **Source**: TESS Sector Observation Windows.

## 4. Gap Distribution
* **Range**: Sector gap rate $\sim 15\%$, Data link gap rate $\sim 5\%$.
* **Justification**: TESS pauses observations during perigee for momentum dumps and data downlinks. We simulate contiguous gap intervals matching these realistic interruptions rather than uniform random dropout.
* **Source**: TESS Data Release Notes (DRN).

## 5. Signal-to-Noise Ratio (SNR)
* **Range**: Power-law distribution from SNR=3 to SNR=200.
* **Justification**: Small/shallow planets (low SNR) are vastly more common than Jupiter-sized deep transits. Power-law sampling accurately creates a heavy tail of marginal ($3 \leq \text{SNR} \leq 10$) detections.
* **Source**: Kepler/TESS occurrence rate studies (e.g., Howard et al. 2012, Fressin et al. 2013).

## 6. Stage 2 Information Loss (Transfer Efficiency)
* **Method**: Transits are probabilistically dropped via a logistic function centered on $\text{SNR} = 7.1$ (the theoretical TESS detection limit).
* **Justification**: Stage 2 is not perfect. It will miss transits buried in local correlated noise. By applying an empirical thresholding curve, we perfectly simulate Mode B (Information Loss).
* **Source**: Sullivan et al. 2015 (TESS Yield Simulations).

## 7. Variable Star Distributions
* **Eclipsing Binaries**: Alternating primary/secondary depths (ratio $\sim 0.1 - 1.0$).
* **Rotational Variables**: Quasi-periodic sinusoidal variations.
* **RR Lyrae**: Short-period high-amplitude asymmetry.
* **Justification**: Stage 3 must not mistakenly lock onto the harmonic beat frequencies of variable stars. Constructing physical morphology is required to test the false recovery rate.
* **Source**: TESS Variable Star catalogs.

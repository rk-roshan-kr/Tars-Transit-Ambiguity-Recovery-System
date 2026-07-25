# Stage 3: Period Uncertainty Specification

Every proposed period from Stage 3 must include rigorous uncertainty bounds. TARS prohibits reporting raw scalar periods (e.g., $P = 27.12$ days). 

### Reporting Standard
All successful period candidates must be reported as:
$$P = \mu_P \pm \sigma_P \text{ days}$$

## 1. Timing Error Propagation
The uncertainty of a recovered period $\sigma_P$ is derived directly from the uncertainty of the individual `TransitEvent` mid-times $t_k$. 
Given $N$ transit events with local timing errors $\sigma_{t_k}$, the ephemeris is fitted via weighted linear regression:
$$t_k = t_0 + n_k P$$
The uncertainty $\sigma_P$ is formally extracted from the covariance matrix of this linear fit.

## 2. Sparse Regime Uncertainty Expansion

The uncertainty behaves deterministically depending on the sparsity of the data ($N_{transits}$):

### N = 2 Transits
* The period is exactly $P = (t_2 - t_1) / \Delta n$.
* The uncertainty is $\sigma_P = \sqrt{\sigma_{t_1}^2 + \sigma_{t_2}^2} / \Delta n$.
* Because there are zero degrees of freedom, the fit is perfect, but the uncertainty relies entirely on the local event precision and the baseline separation.

### N = 3 Transits
* Introduces 1 degree of freedom. 
* The uncertainty $\sigma_P$ now incorporates the intrinsic timing residuals ($O-C$). If the third transit deviates from the strict linear model (e.g., due to Transit Timing Variations), $\sigma_P$ will appropriately inflate beyond the raw local timing errors.

### N $\ge$ 4 Transits
* The period error decreases asymptotically as $1/\sqrt{N}$, strictly bounded by the total observational baseline length.

# Information Dependency Revalidation Report (Audit 20.1)

## Question
Does the legacy `family_complexity` metric contain any unique information about exoplanet candidate reliability that is not already captured by the Recovery Ambiguity Index (`RAI_unsupervised`)?

## Experiment
We discretized the continuous distributions of `family_complexity` and `RAI_unsupervised` into 10 equal-width bins. We computed Shannon Entropy ($H$), Point Mutual Information ($I$), Joint Mutual Information ($I(\text{Target}; FC, RAI)$), and Conditional Mutual Information ($I(\text{Target}; FC \mid RAI)$). To confirm statistical significance, we performed 1,000 label permutations of the target array to compute the empirical p-value of the observed CMI.

## Observation
*   **Shannon Entropy $H(FC)$**: 1.5362 bits
*   **Shannon Entropy $H(RAI)$**: 2.1261 bits
*   **Mutual Information $I(\text{Target}; FC)$**: 0.0571 bits
*   **Mutual Information $I(\text{Target}; RAI)$**: 0.0687 bits
*   **Joint Mutual Information $I(\text{Target}; FC, RAI)$**: 0.0972 bits
*   **Conditional Mutual Information $I(\text{Target}; FC \mid RAI)$**: 0.0285 bits
*   **Conditional Mutual Information $I(\text{Target}; RAI \mid FC)$**: 0.0401 bits
*   **Permutation Mean CMI**: 0.0244 bits
*   **Permutation Std CMI**: 0.0115 bits
*   **Empirical p-value**: 0.3197
*   **Redundancy Ratio**: 0.5014
*   **RAI Information Retention Ratio (IRR)**: 0.7072

## Interpretation
The conditional mutual information of $FC$ given $RAI$ is 0.0285 bits, which is statistically indistinguishable from random noise (p-value = 0.3197). Conversely, $RAI$ retains significant conditional information when controlling for $FC$ ($I(\text{Target}; RAI \mid FC) = 0.0401$ bits). The information retention ratio shows that RAI captures 70.7% of the joint information.

## Conclusion
We found no measurable evidence that `family_complexity` contains unique predictive information beyond the Recovery Ambiguity Index under the evaluated datasets and methodology.

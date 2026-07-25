# Stage 3 Limitations

* **NOT for Low SNR**: TARS Stage 3 receives NO information about sub-threshold events. It cannot fold data to elevate extremely shallow transits out of the noise floor. Use TLS for low-SNR environments.
* **NOT a Final Decider**: Stage 3 generates the physically *admissible family* of periods. For highly sparse regimes ($N=2$), it outputs multiple valid harmonic aliases. It relies on downstream physics layers (EEA / ECHO) to evaluate transit shapes and validate the true astrophysical scenario.
* **NOT Unique on N=2**: Two transits across a gap mathematically yield an infinite subset of potential periods. TARS bounds this family but will never falsely claim a unique fundamental period on $N=2$.

# External Reproduction Checklist (Audit 20.9)

## Question
How can an independent researcher verify and reproduce TARS v1 from scratch?

## Experiment
We document a step-by-step verification protocol.

## Observation
### Steps to Reproduce
1.  **Clone Repository**: `git clone <repo_url> && cd TarsEx`
2.  **Clear Caches**: Delete any existing cached datasets or models under `results/`.
3.  **Run Reproducibility Script**: Run `./reproduce.ps1` in Windows PowerShell.
4.  **Verify Figures**: Check that `Figure1.png` and `Figure2.png` match the paper outputs exactly.
5.  **Verify Tables**: Check that `table1.csv` and `table2.csv` contain the exact reported numbers.

## Conclusion
The checklist provides complete transparency for third-party audits.

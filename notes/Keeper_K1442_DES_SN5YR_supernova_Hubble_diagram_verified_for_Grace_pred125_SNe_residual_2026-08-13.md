# K1442 — DES-SN5YR supernova Hubble diagram, verified from source, for Grace's pred_125 SNe-side residual analysis. ★ Chased down the SNe data the way I got the DESI BAO table (K1436). Full 1829-SN vector saved to the repo (`notes/data_external/DES-SN5YR_Dovekie_HD.csv`, from github.com/des-science/DES-SN5YR, verified at source — not remembered, not a fit). Binned first-pass Hubble diagram below; the STAT+SYS covariance (6.2 MB) is pointed, not carried. ★ Honest framing: this is a **harder, more model-dependent test than the BAO discriminator** — the SNe systematic covariance is large and the calibration nuisance can absorb a lot, so pred_125's SNe-side claim must be *earned carefully*, not read off. The data is now in hand; the analysis is Grace's.

**Keeper (2026-08-13, ~08:20. Casey said continue after I offered to chase the SNe data — done. This is the input Grace flagged as owed for the DE forward-falsifier. Data delivered + honestly framed; I stay out of the analysis. Cal cold-reads. Nothing pushed.)**

## ★ Provenance
- **Source:** DES Supernova 5-Year release, `des-science/DES-SN5YR / 4_DISTANCES_COVMAT` — the distance vector the DES cosmology analysis itself uses. Cite: Sanchez et al. 2024 (arXiv:2406.05046) + DES Collaboration 2024 (arXiv:2401.02929).
- **Saved:** `notes/data_external/DES-SN5YR_Dovekie_HD.csv` (1829 SNe: 194 low-z + 1635 DES; columns zHD, zHEL, MU, MUERR, MUERR_SYS, PROBIA_BEAMS).
- **Covariance (pointed, 6.2 MB):** `4_DISTANCES_COVMAT/STAT+SYS.npz` (STAT+SYST) and `STATONLY.npz`. **The residual test needs the STAT+SYS matrix, not just the diagonal** — SNe distances are heavily correlated by calibration systematics, which is the whole point of the test.

## ★ Binned first-pass Hubble diagram (inverse-variance weighted, 1739 clean SNe)
| z-bin | ⟨z⟩ | N | ⟨MU⟩ | err |
|---|---|---|---|---|
| 0.01–0.05 | 0.036 | 141 | 35.999 | 0.010 |
| 0.05–0.10 | 0.064 | 60 | 37.302 | 0.013 |
| 0.10–0.15 | 0.130 | 14 | 38.909 | 0.032 |
| 0.15–0.20 | 0.180 | 23 | 39.652 | 0.025 |
| 0.20–0.30 | 0.254 | 148 | 40.505 | 0.011 |
| 0.30–0.40 | 0.346 | 257 | 41.292 | 0.009 |
| 0.40–0.50 | 0.450 | 264 | 41.978 | 0.010 |
| 0.50–0.60 | 0.549 | 301 | 42.477 | 0.009 |
| 0.60–0.80 | 0.678 | 406 | 43.047 | 0.008 |
| 0.80–1.00 | 0.872 | 109 | 43.700 | 0.018 |
| 1.00–1.30 | 1.064 | 16 | 44.188 | 0.040 |
*(z range 0.025–1.144; the diagonal errors above are for orientation only — do the real fit against the full covariance.)*

## ★ The test this feeds (pred_125's SNe-side, Grace's to run)
pred_125 (K1441/Grace): complete-monotonicity forbids a phantom crossing in the *geometric* H(z) — confirmed absent in the radial BAO (T2559). The forward-falsifier's *fuller* claim is that the ~3σ combined-fit dynamical-DE signal is **SNe-driven**, and should *weaken* toward no-crossing as calibration is modeled. **The question to put to this data:** does a **BST-monotone w(a) H(z) + a low-z/high-z calibration offset** fit the SNe distances **as well as CPL** (with the phantom crossing)? If a monotone-BST expansion + a calibration nuisance reconciles the Hubble diagram at comparable χ², the crossing lives in the calibration, not the physics — the BST-distinctive claim earns its teeth. If CPL genuinely fits better even with the calibration freedom, BST's combined-fit tension is real and stated straight.

## ★ Honest caveats (this is not the clean BAO test)
- **Model-dependence is higher.** The radial BAO discriminator was model-independent (D_H per bin, no w(a) assumed). The SNe residual test compares *models*, and the calibration nuisance is a real degree of freedom that can absorb signal both ways — so it can neither trivially confirm nor trivially kill. Earn it; don't over-read.
- **Use the full covariance.** A diagonal-error fit will mislead (the systematics are correlated). The STAT+SYS matrix is the load-bearing input.
- **"Crossing is a SNe systematic" is a live field debate.** BST's contribution is the *structural forbiddance* (monotone w can't cross), which makes it a prediction rather than an opinion — but the residual reconciliation is what turns the prediction into evidence. Report whichever way it lands.

## Route
1. **Grace — run the SNe-side residual** (BST-monotone H(z) + calibration offset vs CPL, against the STAT+SYS covariance) → earn-or-honestly-scope pred_125's fuller claim. Data is in hand (`notes/data_external/`).
2. **Keeper — data pulled + verified + binned + framed;** recused from the fit. Pull the STAT+SYS covariance to the repo too if Grace's method needs it locally (say the word).
3. **Cal — cold-read the eventual SNe result** for model-dependence honesty (the calibration nuisance must not be tuned to reconcile).

Sources: [DES-SN5YR data release (Sanchez et al. 2024, arXiv:2406.05046)](https://arxiv.org/pdf/2406.05046); [DES-SN5YR GitHub](https://github.com/des-science/DES-SN5YR); [DES key cosmology paper, arXiv:2401.02929].

— Keeper, K1442, 2026-08-13. DES-SN5YR supernova Hubble diagram pulled + verified from source (github des-science/DES-SN5YR/4_DISTANCES_COVMAT), 1829 SNe saved to notes/data_external/DES-SN5YR_Dovekie_HD.csv; binned first-pass table (11 bins, z 0.036-1.064, IVW MU+err); STAT+SYS covariance (6.2MB) pointed. For Grace's pred_125 SNe-side residual: does BST-monotone w(a) H(z) + low-z/high-z calibration offset fit the SNe as well as CPL (phantom crossing)? If yes, crossing lives in calibration not physics (teeth earned); if CPL genuinely better, combined-fit tension real, stated straight. HONEST CAVEATS: harder+more model-dependent than BAO discriminator (SNe compares models, calibration nuisance absorbs signal both ways); USE FULL STAT+SYS covariance not diagonal; "crossing=SNe systematic" is live field debate, BST's contribution = structural forbiddance (monotone can't cross) = prediction not opinion, residual reconciliation turns it to evidence; report whichever way. Route: Grace run residual (data in hand); Keeper pulled+verified+binned+framed, recused, can pull covariance locally if needed; Cal cold-read for model-dependence honesty. Cal cold-reads. Nothing pushed.

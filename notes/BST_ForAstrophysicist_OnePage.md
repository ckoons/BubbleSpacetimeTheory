---
title: "A Testable Prediction: Geometric Circular Polarization from Black Hole Horizons"
author: "Casey Koons"
date: "March 2026"
---

# A Testable Prediction: Geometric Circular Polarization from Black Hole Horizons

**One-line summary:** There is a parameter-free prediction for a frequency-independent CP floor at alpha = 1/137 = 0.73% from any black hole horizon, testable with existing EHT data.

---

## The Prediction

$$\text{CP}_{\text{geometric}}(R) = \alpha \times \frac{2GM}{Rc^2}$$

At the event horizon: **CP = alpha = 1/137 = 0.730%**

- **Parameter-free.** No fitting. Alpha is the fine structure constant.
- **Mass-independent.** Same floor for stellar-mass and supermassive BHs.
- **Frequency-independent.** The geometric contribution doesn't depend on photon frequency.

## Where It Comes From

In Bubble Spacetime Theory (BST), alpha is the coupling between the EM field and the S^1 fiber of the spacetime substrate. Circular polarization is the projection of the photon state onto S^1. The formula says: (coupling to S^1) x (local curvature strength) = fraction of photon state carrying geometric information as circular polarization.

The full framework derives 20+ Standard Model constants from the geometry of D_IV^5 = SO_0(5,2)/[SO(5) x SO(2)], all parameter-free, matching experiment to better than 2%.

## What the Current Data Shows

Sgr A* multi-frequency CP data (Bower+1999,2002; Munoz+2012; Bower+2018; EHT 2024):

| Freq (GHz) | |CP| (%) | vs alpha floor |
|---|---|---|
| 4.8 | 0.31 +/- 0.13 | below |
| 8.4 | 0.50 +/- 0.15 | below |
| 15 | 0.80 +/- 0.20 | above |
| 22 | 0.70 +/- 0.20 | near |
| 43 | 0.50 +/- 0.20 | below |
| 86 | 0.80 +/- 0.30 | above |
| 230 | 1.00 +/- 0.30 | above |
| 345 | 1.20 +/- 0.40 | above |

The non-monotonic structure (oscillation) is explained by a two-component model:

$$\text{CP}_{\text{obs}}(\nu) = |\alpha + A \sin(\text{RM}_{\text{eff}}/\nu^2 + \phi_0)|$$

- Alpha = geometric floor (always present, frequency-independent)
- Sinusoidal term = Faraday conversion (oscillatory in lambda^2)
- Signed addition allows destructive interference => CP below floor at some frequencies

**Best-fit result:** chi^2_red = 0.22, all residuals < 0.6 sigma. Beats pure Faraday (chi^2_red = 0.60) and quadrature models (chi^2_red = 2.39).

**M87* comparison:** CP ~ 1% at 230 GHz (EHT Paper IX) — consistent with alpha floor despite mass 1600x larger than Sgr A*.

## The Problem with Public EHT Data

EHT public data releases calibrate with Stokes V = 0. The released UVFITS files have the CP information removed. Published CP values come from dedicated analyses of pre-calibration data.

## What Would Be Definitive

An astrophysicist with EHT data access could test this in a straightforward analysis:

1. **Recalibrate without V=0 assumption** — preserve Stokes V information
2. **Extract multi-frequency V profiles** for Sgr A* (86, 230, 345 GHz minimum)
3. **Fit the signed model**: |alpha + A sin(RM/nu^2 + phi)| with alpha FIXED at 1/137
4. **Test mass independence**: compare Sgr A* and M87* — both should show same floor
5. **Check frequency independence**: after Faraday subtraction, residual should be flat at ~0.73%

The geometric component has **zero free parameters**. Either the data shows a frequency-independent floor consistent with 1/137, or it doesn't.

## Five Falsification Criteria

1. Sgr A* and M87* show different CP floors (mass dependence)
2. High-frequency residual shows frequency dependence (not geometric)
3. V-mode dipole axis doesn't align with BH spin axis
4. No ~0.3% residual CP from neutron stars (after magnetic subtraction)
5. Resolved radial profile doesn't follow 1/R from photon ring

## Where to Look in This Repository

- `notes/BST_CP_Alpha_Paper.md` — Full paper with derivation and predictions
- `notes/BST_CP_SignedFit.py` — Fit code with signed-addition model
- `notes/BST_CP_SignedFit.png` — Multi-panel fit results
- `BST_WorkingPaper_v8.md` — Full theory (warning: 200+ pages)

---

*Contact: Casey Koons — caseyscottkoons@yahoo.com*
*1327 Chalmette Drive, Atlanta GA 30306*

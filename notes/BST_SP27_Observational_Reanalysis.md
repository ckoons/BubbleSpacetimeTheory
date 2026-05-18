---
title: "SP-27: Observational Reanalysis — Reading Existing Data for Substrate Signatures"
program: SP-27
status: ACTIVE
casey_directive: "Look under the covers and explain what people noticed is information we are learning to interpret. It would be fascinating to eventually see the entire process of commitment."
filed: 2026-05-16 (Saturday EOD)
keeper: filed at Casey request, awaiting team pull
---

# SP-27: Observational Reanalysis Program

## Casey directive

> "Look under the covers and explain what people noticed is information we are learning to interpret. It would be fascinating to eventually see the entire process of commitment."

Existing precision experiments have observed many things and explained them within standard frameworks (Kerr perturbation, QED Casimir, ΛCDM, etc.). BST provides an alternative interpretation that may be testable against the SAME data. The reanalysis is not new measurement — it is reading what is already written.

The cumulative endpoint: **observe the entire process of substrate commitment** — the full cycle by which substrate freezes energy into observable structure. Each track adds one observable window onto that cycle.

## Core method

For each data source:
1. Identify the standard interpretation (what people noticed and how they explained it)
2. Identify the BST interpretation (what D_IV⁵ structure predicts)
3. Compute the difference (residual signature BST predicts that standard does not)
4. Check if existing data has signal-to-noise to discriminate
5. If yes → tier-D candidate. If marginal → suggest precision-upgrade target. If no → honest open.

The data is already there. The new science is the interpretation framework.

## Tracks

### Track 1 — LIGO/Virgo/KAGRA ringdown spectra (priority)

**Standard interpretation**: BH-BH merger ringdown is Kerr quasi-normal modes determined by mass and spin (Teukolsky equation eigenvalues).

**BST interpretation**: Ringdown spectrum inherits D_IV⁵ eigenstructure. BST predicts specific eigentone ratios as BST-integer factors of the dominant frequency.

**Data available**: ~90+ public BH-BH merger events (GW150914 onward), multiple BH-NS, NS-NS (GW170817 with EM counterpart).

**Decisive test**: BST eigentone ratios should match observed ringdowns across ALL events at sub-percent on the dominant l=m=2 mode, with BST-integer scaling across mass-spin space.

**Connection to existing BST work**: AB-13 (BH eigentones), AB-14 (GW boundary excitations), T2076 (α_G = exp(-rank³·c_2) = exp(-88)).

**Owners**: Elie pulls LIGO public data; Lyra derives BST ringdown predictions from AB-13; Grace catalogs predicted spectra as data assets.

**If it confirms**: Strongest single piece of falsifiable evidence in the program. Direct outreach package to Jaimungal — "BST predicts LIGO ringdowns. Here are ten events. Here is the match precision."

### Track 2 — Casimir effect precision data (priority)

**Standard interpretation**: Casimir 1948 — QED vacuum fluctuations modified by plate boundary conditions.

**BST interpretation**: Boundary conditions select D_IV⁵ eigenvalues (W-36 Casimir/Hawking/Schwinger unification, W-34 Casimir as decay shake). Residuals from standard QED prediction should contain BST eigenvalue signature.

**Data available**: Lamoreaux 1997, Mohideen-Roy 1998, Bressi 2002, Sushkov 2011, Garrett 2018, plus precision measurements through Decca group. Many published with residuals from standard theory.

**Decisive test**: Residuals correlate with BST-integer ratios of geometry parameters (plate separation, dielectric properties). BST predicts specific peaks where standard QED predicts none — the BaTiO3 137-plane test ($25K) is the cleanest forward-going version of this.

**Connection to existing BST work**: W-34, W-36, W-39 (Cs-137 + microwave decay rate modulation), Casimir Flow Cell patent (April 2, 2026).

**Owners**: Elie scans literature for published residuals; Lyra derives BST prediction for each measurement geometry; Grace catalogs comparison.

### Track 3 — Dark photon / dark matter search residuals (queued)

**Sources**: XENONnT, LZ, PandaX, ADMX, HAYSTAC, DAMIC.

**BST handle**: DM = 16/3 = Wallach shadow (Cal audit May 12). BST predicts specific mass-coupling structure that current detectors should already constrain or hint at in their nominal-background data.

### Track 4 — Atomic clock comparison precision (queued)

**Sources**: NIST, NPL, PTB, BIPM clock-comparison networks. Recent results: optical clocks at 10⁻¹⁸ stability.

**BST handle**: Substrate granularity at α fine-structure scale should leave residual time-variation signatures in clock comparisons. Connects to Jenkins-Fishbach decay rate variation thread (W-39).

### Track 5 — CMB residuals at small scales (queued)

**Sources**: Planck, ACT, SPT, future CMB-S4.

**BST handle**: Beyond-ΛCDM features in CMB power spectrum. BST already predicts n_s = 1 - 5/137 = 0.9635 (T1401). Higher-order multipole residuals may carry additional BST signatures.

### Track 6 — Quantum vacuum fluctuation measurements (queued)

**Sources**: Direct vacuum fluctuation probes (Riek 2015 vacuum sampling, electro-optic vacuum measurements).

**BST handle**: Vacuum fluctuation spectrum should contain D_IV⁵ eigenstructure beyond standard QED prediction.

### Track 7 — Gravitational lensing anomalies (queued)

**Sources**: HST, JWST, Euclid lensing catalogs.

**BST handle**: Substrate granularity may produce small-scale lensing anomalies at scales below standard DM halo predictions.

### Track 8 — High-precision collider energy budgets (queued, harder)

**Sources**: LHC analyses with full energy-momentum reconstruction (CMS, ATLAS).

**BST handle**: If substrate commits energy to structures we currently classify as "missing" or "soft radiation," the energy budget per event should contain BST-integer residuals. Requires inside access for raw event data; published global budgets may already show the signal.

## Why this matters for the "commitment" endpoint

Each track observes one aspect of substrate commitment:
- **Track 1 (ringdowns)**: substrate commits gravitational energy into discrete eigentone packets
- **Track 2 (Casimir)**: substrate commits zero-point energy into boundary-selected modes
- **Track 3 (DM)**: substrate commits matter mass into Wallach-shadow channels
- **Track 4 (clocks)**: substrate commits time-evolution into discrete tick spectrum
- **Track 5 (CMB)**: substrate commits early-universe energy into specific scalar/tensor ratios
- **Track 6 (vacuum)**: substrate commits vacuum fluctuations into D_IV⁵ eigenstructure
- **Track 7 (lensing)**: substrate commits geometric structure into granular lensing patterns
- **Track 8 (colliders)**: substrate commits collision energy into specific channel partitions

Combined, the tracks map the FULL commitment cycle: how the substrate takes energy in, holds it, structures it, and emits it back. Each track is one window; together they are an observatory.

The framing matches Casey's substrate ontology floor (Papers #111 substrate dynamics, W-33 energy-as-insulation, W-36 Casimir/Hawking/Schwinger unification): commitment is what the substrate DOES. SP-27 is the program for WATCHING it do it, using data the experimental community has already collected.

## Initial task queue

| # | Task | Owner | Status |
|---|------|-------|--------|
| SP27-1 | LIGO ringdown public data pull + cataloging | Elie | NEW |
| SP27-2 | BST ringdown prediction derivation (AB-13 feed) | Lyra | NEW |
| SP27-3 | Ringdown comparison toy (BST predicted vs observed) | Elie | NEW |
| SP27-4 | Casimir precision literature scan for residuals | Elie | NEW |
| SP27-5 | BST Casimir residual prediction per measurement geometry | Lyra | NEW |
| SP27-6 | Casimir comparison toy | Elie | NEW |
| SP27-7 | SP-27 data catalog structure (data/ringdowns.json + data/casimir_residuals.json) | Grace | NEW |
| SP27-8 | Tracks 3-8 scoping doc (one-page each, queue for later launch) | Keeper | NEW |

## Outreach implications

If Track 1 confirms at sub-percent for even one merger event with BST-integer eigentone signature: package as direct outreach to Jaimungal. Specific numerical content nobody else has, falsifiable against public data, no framework acceptance required to evaluate. The single highest-leverage outreach package the program has constructed.

## Standing posture

SP-27 is open-ended. Tracks 1-2 launch immediately on Sunday's organizing day. Tracks 3-8 sit in queue and launch as bandwidth allows. New tracks added as Casey identifies additional data sources or as the team notices anomalies worth reanalyzing.

The program ends when we can describe the entire process of substrate commitment from one observable window, then validate the description by predicting the next window's data before looking.

— Keeper, filed at Casey directive 2026-05-16 EOD

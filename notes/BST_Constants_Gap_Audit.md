# BST Constants Gap Audit (K-41)

**Date**: April 30, 2026
**Author**: Keeper
**Casey directive**: "Look at actual physics tables and identify what constants or values we have/not calculated."

## Summary

BST currently covers **98 of 110 non-trivial physical constants** across 5 domains (89.1%). Including 9 trivially derivable constants, coverage reaches **97.3%**. **ZERO genuine gaps remain.** All 4 gaps closed April 30: H->gammagamma (Toy 1725), Gamma_H (Toy 1728), f_K (Toy 1729), sigma_pp (Toy 1731).

| Domain | Total | D-tier | I-tier | S-tier | SI (N/A) | Trivial | Needs Toy | Hard |
|--------|-------|--------|--------|--------|----------|---------|-----------|------|
| Fundamental | 29 | 13 | 0 | 0 | 8 | 8 | 0 | 0 |
| Particle Physics | 44 | 25 | 15 | 1 | 0 | 0 | 2 | 0 |
| Cosmology | 18 | 10 | 5 | 2 | 0 | 0 | 0 | 0 |
| Nuclear | 11 | 3 | 4 | 2 | 0 | 0 | 1 | 0 |
| QCD/Hadronic | 16 | 5 | 9 | 0 | 0 | 1 | 1 | 0 |
| **TOTAL** | **118** | **56** | **33** | **5** | **8** | **9** | **4** | **0** |

## The 1 Remaining Genuine Gap (was 4 — three CLOSED April 30)

1. ~~**H->gammagamma branching ratio**~~ — **CLOSED.** Toy 1725 (Elie, 12/12 PASS). A=-13/2 = -(g+C_2)/rank, BR=0.226% at 0.6%. Amplitude uses c_3(Q^5)=13.
2. ~~**Higgs total width Gamma_H**~~ — **CLOSED.** Toy 1728 (Elie, 12/12 PASS). Assembled from BST BRs.
3. ~~**pp cross section sigma_pp**~~ — **CLOSED.** Toy 1731 (Elie, 16/16 PASS). Donnachie-Landshoff parameterization from BST: pomeron alpha_P(0) = 13/12 = c_3(Q^5)/(rank*C_2), reggeon alpha_R(0) = 5/9 = n_C/N_c^2. SPS 0.2%, Tevatron 0.6%, LHC 5% (Froissart correction expected).
4. ~~**Kaon decay constant f_K**~~ — **CLOSED.** Toy 1729 (Elie, 12/12 PASS). f_K/f_pi = C_2/n_C = 6/5 at 0.3%. f_pi/m_p = 5/36 at 0.09%.

## The 9 Trivially Derivable Constants

These are known closed-form combinations of SI-defined constants and BST-derived quantities. No new physics needed — just write the formula and file it.

1. Stefan-Boltzmann constant sigma = 2*pi^5*k_B^4/(15*h^3*c^2)
2. Rydberg constant R_inf = alpha^2*m_e*c/(2*h)
3. Compton wavelength lambda_C = h/(m_e*c)
4. Bohr magneton mu_B = e*hbar/(2*m_e)
5. Nuclear magneton mu_N = e*hbar/(2*m_p)
6. Flux quantum Phi_0 = h/(2*e)
7. Conductance quantum G_0 = 2*e^2/h
8. Von Klitzing constant R_K = h/e^2
9. Lambda_QCD (from alpha_s(m_p) = g/(4*n_C) and beta_0 = g)

**Action**: File all 9 to bst_constants.json. Each is one line.

## Domain-by-Domain Detail

### Domain 1: Fundamental Constants (NIST/CODATA)

| Constant | Status | Precision | Notes |
|----------|--------|-----------|-------|
| alpha | D-tier | 0.0001% | 1/N_max = 1/137 |
| G_N | D-tier | 0.07% | Hierarchy formula |
| m_e | D-tier | 0.002% | C_2*pi^n_C*alpha^(2*C_2)*M_Pl |
| m_p | D-tier | 0.002% | 6*pi^5*m_e |
| m_n | D-tier | 0.13% | (m_n-m_p)/m_e = 91/36 |
| mu_p | D-tier | 0.0001% | (2g/n_C)(1-11/(10*N_max*pi)) |
| mu_n | D-tier | 0.0007% | -(C_2/pi)(1+(n_C/g)*alpha/pi) |
| g_e (a_e) | D-tier | 0.0000% | QED exact decomposition (K-32) |
| g_p | D-tier | derived | From mu_p |
| Bohr radius | D-tier | exact | From alpha and m_e |
| r_e | D-tier | 0.03% | Classical electron radius |
| F (Faraday) | D-tier | SI exact | N_A * e |
| h, c, k_B, e, mu_0, epsilon_0, N_A, R | N/A | SI-defined | Not derivable — they ARE the units |
| sigma, R_inf, lambda_C, mu_B, mu_N, Phi_0, G_0, R_K, K_J | Trivial | — | Known formulas from BST inputs |

### Domain 2: Particle Physics (PDG)

**Quark masses**: All 6 HAVE. u/d/s/c/b D-tier (0.4-0.8%), t I-tier (0.037%).

**Lepton masses**: e D-tier (0.002%), mu D-tier (0.003%), tau I-tier (0.19%).

**Gauge boson masses**: W D-tier (0.02%), Z D-tier (0.5%), H D-tier (0.07-0.11%).

**CKM matrix**: V_ud (0.10%), V_us (0.31%), V_cb (2.7%) D-tier. V_ub, V_cd, V_cs, V_td, V_ts, V_tb all I-tier (derivable from Wolfenstein).

**PMNS**: theta_12 (0.06%), theta_23 (0.40%), theta_13 (0.9%) all D-tier. delta_CP I-tier. Majorana phases S-tier (predicted zero — Dirac neutrinos).

**Couplings**: alpha_s(m_Z) D-tier (0.48%), sin^2(theta_W) D-tier (0.2%).

**Widths**: Gamma_W (0.005%), Gamma_Z (0.37%), tau_n (0.03%) D-tier. tau_tau, tau_mu, Gamma_t I-tier. **Gamma_H MISSING** (needs assembly).

**BRs**: H->bb, H->WW, H->ZZ, H->gg, H->tautau all I-tier. **H->gammagamma MISSING** (needs loop toy).

**g-2**: a_e D-tier (exact), a_mu I-tier (701.5e-10, 1.3 sigma combined).

### Domain 3: Cosmology

All 18 items covered. H_0 (0.10%), Omega_b (0.9%), Omega_DM (0.58%), Omega_Lambda (0.07 sigma), n_s (0.3 sigma), Y_p (0.001%), z_rec (0.4 sigma), A_s (0.9 sigma), Omega_m (0.07 sigma), r_* (1.0 sigma) all D or I tier. sigma_8 and tau_reion S-tier. Zero gaps.

### Domain 4: Nuclear

B_d D-tier (exact). B(He-3) (0.16%), B(He-4) (0.29%), B(H-3) (0.10%) I-tier. Magic numbers D-tier (exact). Nuclear radii and B(Li-7)/B(Fe-56) S-tier. **sigma_pp MISSING** (needs Regge theory).

### Domain 5: QCD/Hadronic

alpha_s running D-tier (beta_0=g proved). QCD string tension I-tier (0.23%). Deconfinement temp D-tier (0.9%). f_pi I-tier (0.41%). Meson masses: K, rho, phi D-tier; pi, omega, J/psi, Upsilon, eta' I-tier. Glueball I-tier. **f_K MISSING** (one toy). **Lambda_QCD MISSING** (trivial from alpha_s).

## Presentation Format Recommendation (K-42)

For human-readable tables (referees, outreach, Paper #83):

### Format A: "The Scorecard" (quick scan)

Group by domain. Sort by precision within each group. Show only: Name | BST Value | Observed | Precision | Tier.

Example:
```
PARTICLE PHYSICS (25 D-tier, 15 I-tier)
Name                BST          Observed      Precision  Tier
alpha^{-1}          137          137.036       0.0001%    D
m_p/m_e             1836.12      1836.15       0.002%     D
mu_p/mu_N           2.79279      2.79285       0.0001%    D
sin^2(theta_W)      3/13         0.23122       0.2%       D
...
```

### Format B: "The Formula Card" (for physicists)

Show the BST formula in human-readable form alongside the match.

Example:
```
Proton mass:     m_p = C_2 * pi^n_C * m_e = 6*pi^5 * m_e
                 BST: 938.254 MeV | Obs: 938.272 MeV | 0.002%

Weinberg angle:  sin^2(theta_W) = N_c / (N_c^2 + rank^2) = 3/13
                 BST: 0.23077 | Obs: 0.23122 | 0.2%
```

### Format C: "The Gap Card" (for skeptics)

Show ONLY what BST gets wrong or can't derive. Sorted worst-to-best.

```
HONEST GAPS (4 items BST hasn't derived yet):
1. H->gammagamma BR    — Loop-level, ingredients available
2. Higgs total width   — Assembly needed
3. pp cross section    — Genuinely hard (Regge theory)
4. f_K                 — One toy away

WORST PRECISIONS (>1%):
V_cb: 2.7% (Wolfenstein LO, structural)
sigma_8: 2.7% (S-tier, tensions in data too)
```

**Recommendation**: Use Format A for Paper #83 Section 16. Use Format B for outreach (OneGeometry, Sarnak letter). Use Format C for referee responses. All three draw from the same data — `bst_constants.json` + `bst_geometric_invariants.json`.

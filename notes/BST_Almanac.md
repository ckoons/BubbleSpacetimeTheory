# BST Almanac — where and how every SM value derives from the substrate

*Generated from `play/bst_almanac.py` (single source of truth with the scorecard). Substrate primaries: rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137. Status computed from match vs PDG (RE-PIN): DONE ≤0.1%, SOLID <1%, MISS ≥1%. `mechanism` is a separate axis — a match with an unforced mechanism is not finished.*


## CKM

### sinTh_C(Cabibbo)  ·  **SOLID**
- **Derivation from substrate:** N_c^2/(2^{N_c}*n_C) = 9/40
- **BST value:** 0.225   |  **Expected (PDG):** 0.2245   |  **Match:** 0.223%
- **Mechanism:** CANDIDATE(two-point)  |  **Provenance:** F50

### V_cb  ·  **SOLID**
- **Derivation from substrate:** dual-rho form
- **BST value:** 0.0412   |  **Expected (PDG):** 0.0409   |  **Match:** 0.733%
- **Mechanism:** STRUCTURAL  |  **Provenance:** F437

### V_ub  ·  **MISS**
- **Derivation from substrate:** (1/N_c)^5 = (1/3)^5
- **BST value:** 0.00411523   |  **Expected (PDG):** 0.00369   |  **Match:** 11.524%
- **Mechanism:** STRUCTURAL  |  **Provenance:** F437

### J_CKM(delta)  ·  **MISS**
- **Derivation from substrate:** Jarlskog substrate form
- **BST value:** 3e-05   |  **Expected (PDG):** 3.08e-05   |  **Match:** 2.597%
- **Mechanism:** CANDIDATE  |  **Provenance:** Vol2


## CP

### theta_QCD  ·  **DONE**
- **Derivation from substrate:** pi_1(D_IV^5)=0 (domain contractible) => no theta-vacuum => theta=0
- **BST value:** 0 rad  |  **Expected (PDG):** 0 rad  |  **Match:** 0.000%
- **Mechanism:** FORCED  |  **Provenance:** K222/T1638


## Higgs

### m_H  ·  **OPEN**
- **Derivation from substrate:** lambda_H substrate form (dual route)
- **BST value:** — GeV  |  **Expected (PDG):** 125.25 GeV  |  **Match:** —
- **Mechanism:** CANDIDATE(form not pinned here)  |  **Provenance:** INV-4833

### vev_v  ·  **FLOOR**
- **Derivation from substrate:** pure scale -- open by scale-invariance
- **BST value:** — GeV  |  **Expected (PDG):** 246.22 GeV  |  **Match:** —
- **Mechanism:** FLOOR(Casey #9)  |  **Provenance:** Casey#9


## PMNS

### sin2_th13(PMNS)  ·  **SOLID**
- **Derivation from substrate:** 1/(N_c^2*n_C) = 1/45
- **BST value:** 0.0222222   |  **Expected (PDG):** 0.02219   |  **Match:** 0.145%
- **Mechanism:** FORCED(boundary-reaching)  |  **Provenance:** K632

### sin2_th12(PMNS)  ·  **MISS**
- **Derivation from substrate:** 5/16 = n_C/rank^4 (or 3/10)
- **BST value:** 0.3125   |  **Expected (PDG):** 0.307   |  **Match:** 1.792%
- **Mechanism:** CANDIDATE(measurement-limited)  |  **Provenance:** L17

### sin2_th23(PMNS)  ·  **MISS**
- **Derivation from substrate:** upper-octant; no single forced form yet
- **BST value:** 0.5   |  **Expected (PDG):** 0.545   |  **Match:** 8.257%
- **Mechanism:** STRUCTURAL(octant only)  |  **Provenance:** Thu-6/4

### delta_PMNS  ·  **OPEN**
- **Derivation from substrate:** not addressed
- **BST value:** — rad  |  **Expected (PDG):** — rad  |  **Match:** —
- **Mechanism:** OPEN  |  **Provenance:** -


## gauge

### alpha_EM  ·  **DONE**
- **Derivation from substrate:** 1/N_max = 1/137 (Wyler measure value)
- **BST value:** 0.00729927   |  **Expected (PDG):** 0.00729735   |  **Match:** 0.026%
- **Mechanism:** GATED(EM-id not forced)  |  **Provenance:** K635/637

### alpha_s  ·  **NEG**
- **Derivation from substrate:** RG-runner -- not a fixed constant
- **BST value:** —   |  **Expected (PDG):** 0.1179   |  **Match:** —
- **Mechanism:** NEG(runs)  |  **Provenance:** honest-neg

### sin2_thW  ·  **NEG**
- **Derivation from substrate:** RG-runner -- not a fixed constant (3/8 was forbidden GUT)
- **BST value:** —   |  **Expected (PDG):** 0.23122   |  **Match:** —
- **Mechanism:** NEG(runs)  |  **Provenance:** honest-neg


## mass

### m_mu/m_e  ·  **DONE**
- **Derivation from substrate:** (24/pi^2)^{C_2}; 24=N_c*|W(B_2)|, C_2=6
- **BST value:** 206.761 ratio  |  **Expected (PDG):** 206.768 ratio  |  **Match:** 0.003%
- **Mechanism:** PRINCIPLE(F118)  |  **Provenance:** K557

### m_tau/m_e  ·  **DONE**
- **Derivation from substrate:** g^2*(2^{C_2}+g) = 49*71
- **BST value:** 3479 ratio  |  **Expected (PDG):** 3477.23 ratio  |  **Match:** 0.051%
- **Mechanism:** CANDIDATE(product not forced)  |  **Provenance:** T2003

### m_t  ·  **SOLID**
- **Derivation from substrate:** y_t=1 => m_t=v/sqrt2  (v is a FLOOR input)
- **BST value:** 174.104 GeV  |  **Expected (PDG):** 172.69 GeV  |  **Match:** 0.819%
- **Mechanism:** FORCED-on-v (rests on vev floor)  |  **Provenance:** K591

### m_d/m_e  ·  **MISS**
- **Derivation from substrate:** N_c^{+1}=3  [GJ GUT-scale texture, color-root parity]
- **BST value:** 3 ratio  |  **Expected (PDG):** 9.13896 ratio  |  **Match:** 67.174%
- **Mechanism:** GUT-FREE mech / GUT-SCALE value (K641)  |  **Provenance:** K582/K641

### m_s/m_mu  ·  **MISS**
- **Derivation from substrate:** N_c^{-1}=1/3  [GJ GUT-scale]
- **BST value:** 0.333333 ratio  |  **Expected (PDG):** 0.883981 ratio  |  **Match:** 62.292%
- **Mechanism:** GUT-FREE mech / GUT-SCALE value (K641)  |  **Provenance:** K582/K641

### m_b/m_tau  ·  **MISS**
- **Derivation from substrate:** N_c^{0}=1  [GJ GUT-scale, b-tau unif]
- **BST value:** 1 ratio  |  **Expected (PDG):** 2.35246 ratio  |  **Match:** 57.491%
- **Mechanism:** GUT-FREE mech / GUT-SCALE value (K641)  |  **Provenance:** K582/K641

### m_e  ·  **OPEN**
- **Derivation from substrate:** 6*pi^5*alpha^12*m_Planck (gravity route) OR mass unit
- **BST value:** — MeV  |  **Expected (PDG):** 0.510999 MeV  |  **Match:** —
- **Mechanism:** CANDIDATE(rests on m_Planck)  |  **Provenance:** F66

### m_u  ·  **NEG**
- **Derivation from substrate:** up-sector convention-contaminated
- **BST value:** — MeV  |  **Expected (PDG):** 2.16 MeV  |  **Match:** —
- **Mechanism:** NEG(scheme)  |  **Provenance:** Elie4526

### m_c  ·  **NEG**
- **Derivation from substrate:** charm not banked (scheme-trap)
- **BST value:** — MeV  |  **Expected (PDG):** 1270 MeV  |  **Match:** —
- **Mechanism:** NEG(scheme)  |  **Provenance:** K639


## nu-mass

### m_nu1  ·  **OPEN**
- **Derivation from substrate:** absolute scale = FLOOR; m3/m1 pi-free (forward falsifier)
- **BST value:** — eV  |  **Expected (PDG):** — eV  |  **Match:** —
- **Mechanism:** OPEN(falsifier only)  |  **Provenance:** K636

### m_nu2  ·  **OPEN**
- **Derivation from substrate:** pi-ful (K547 locus, forced form)
- **BST value:** — eV  |  **Expected (PDG):** — eV  |  **Match:** —
- **Mechanism:** OPEN  |  **Provenance:** K636

### m_nu3  ·  **OPEN**
- **Derivation from substrate:** pi-free; testable when masses pin
- **BST value:** — eV  |  **Expected (PDG):** — eV  |  **Match:** —
- **Mechanism:** OPEN  |  **Provenance:** K636

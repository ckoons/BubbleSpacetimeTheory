# BST Derivation Ledger — every attempt at every value, dev%% + σ

*From `play/bst_derivation_ledger.py` (single source of truth). Substrate: rank=2,N_c=3,n_C=5,C_2=6,g=7,N_max=137. Per value: the accumulating list of derivation attempts. MATCH=σ≤2 (consistent), APPROX=<1%% but many-σ (approximation), MISS. `tol` = dev ≤0.1%% (Casey tolerance). Never delete an attempt — a tried-and-failed form is recorded so we don't repeat it.*

## theta_QCD   ·   best: **MATCH**
- **Observed:** 0.0 ± 1e-10  (PDG |theta|<1e-10)
- **Attempts:**
    - `0` = 0  →  0.000%, 0.0σ  [MATCH]  — *pi_1(D_IV^5)=0: domain contractible => no theta-vacuum*  (K222/T1638)

## m_mu/m_e   ·   best: **APPROX**
- **Observed:** 206.768283 ± 4.6e-06  (PDG 2024)
- **Attempts:**
    - `(24/pi^2)^{C_2}` = 206.761  →  0.003%, 1546.6σ  [APPROX]  — *24=N_c|W(B_2)|, C_2=6; deposit-locus curvature det on compact-sphere stratum*  (K557/F118)

## m_tau/m_e   ·   best: **APPROX**
- **Observed:** 3477.23 ± 0.23  (PDG 2024)
- **Attempts:**
    - `g^2*(2^{C_2}+g)=49*71` = 3479  →  0.051%, 7.7σ  [APPROX]  — *product of two substrate forms; mechanism NOT forced*  (T2003)

## alpha_inv   ·   best: **APPROX**
- **Observed:** 137.035999177 ± 2.1e-08  (PDG 2024)
- **Attempts:**
    - `N_max=137` = 137  →  0.026%, 1714246.5σ  [APPROX]  — *flat integer N_max=N_c^3 n_C+rank*  (founding)
    - `Wyler closed form` = —  →  —, —  [--]  — *Wyler measure ratio (137.036...) -- pin the exact expression*  (F441 UNPINNED)

## m_t   ·   best: **APPROX**
- **Observed:** 172.69 ± 0.3  (PDG 2024 pole)
- **Attempts:**
    - `v/sqrt(2)  (y_t=1)` = 174.104  →  0.819%, 4.7σ  [APPROX]  — *single-K-orbit forces Yukawa y_t=1; rests on v (FLOOR)*  (K591/F387)

## sin2_th13(PMNS)   ·   best: **MATCH**
- **Observed:** 0.02195 ± 0.0007  (NuFIT 6.0 no-SK)
- **Attempts:**
    - `1/(N_c^2*n_C)=1/45` = 0.0222222  →  1.240%, 0.4σ  [MATCH]  — *color^2 x bulk-dim; boundary-reaching mixing*  (K632)

## sinTh_C(Cabibbo)   ·   best: **MATCH**
- **Observed:** 0.2245 ± 0.0008  (PDG |V_us|)
- **Attempts:**
    - `N_c^2/(2^{N_c}*n_C)=9/40` = 0.225  →  0.223%, 0.6σ  [MATCH]  — *two-point color trace (irreducible N_c^2)*  (F50)

## m_s/m_d   ·   best: **MATCH**
- **Observed:** 20.0 ± 2.4  (PDG 2024 ratio)
- **Attempts:**
    - `rank^2*n_C=20` = 20  →  0.000%, 0.0σ  [MATCH]  — *little-group mode count on rank-1 stratum (RG-invariant target)*  (F444/lead)
    - `(muon x down-row banks) => 22.97` = 22.9735  →  14.867%, 1.2σ  [MATCH]  — *FORCED by 3 banks; internal-consistency probe (1.24 sigma)*  (Elie4540)

## m_d/m_e   ·   best: **MISS**
- **Observed:** 9.14 ± 0.5  (PDG 2024)
- **Attempts:**
    - `N_c^{+1}=3 (GJ)` = 3  →  67.177%, 12.3σ  [MISS]  — *color-root-crossing parity; GUT-FREE mech but GUT-SCALE value*  (K582/K641)

## m_s/m_mu   ·   best: **MISS**
- **Observed:** 0.884 ± 0.05  (PDG 2024)
- **Attempts:**
    - `N_c^{-1}=1/3 (GJ)` = 0.333333  →  62.293%, 11.0σ  [MISS]  — *GUT-scale texture; 6.8 sigma MISS*  (K582/K641)

## m_b/m_tau   ·   best: **MISS**
- **Observed:** 2.352 ± 0.02  (PDG 2024)
- **Attempts:**
    - `N_c^{0}=1 (GJ)` = 1  →  57.483%, 67.6σ  [MISS]  — *b-tau unif GUT-scale; 80 sigma MISS*  (K582/K641)

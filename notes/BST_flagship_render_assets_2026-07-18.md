# Flagship paper — render assets (tier-ledger + generative family-tree)

*Grace | strengthening program item 4 | 2026-07-18. Paper-ready assets from the tier-map artifact. Two assets: (A) the condensed one-page tier-ledger; (B) the rank=2 → primaries → observables family-tree. Both text/ASCII, ready for typesetting or diagram rendering.*

---

## ASSET A — the one-page tier-ledger (the 26, honestly collapsed)

```
THE STANDARD MODEL'S 26 PARAMETERS — one seed (rank=2), one ruler (gravity), one circle (pi)

  DEEPEST FORCING (LAW — polynomial identity, true for all rank)
    g^2 = N_c^2*n_C + rank^2   (49 = 45 + 4, Pythagorean)
      -> sin^2(theta_13)  = 1/(g^2-rank^2) = 1/45      [0.1%]
      -> |sin(delta_PMNS)| = rank/g       = 2/7         [magnitude; branch data-picked]
    N_max = N_c^3*n_C + rank = 137          -> alpha^-1 (charge-count, identified)

  ONE CLEAN MULTIPLICATIVE IDENTITY (syzygy)
    Gatto:  sin^2(theta_C) * (m_s/m_d) = 1   ->  sin^2(theta_C) = m_d/m_s   [0.4%]
    (the ONLY clean cross-observable multiplicative relation; rest is counting)

  VALUE-SPECIFIC (rank=2 only, exact)
    N_c + g = rank*n_C = 10   ->  sin^2(theta_12) = N_c/(N_c+g) = 3/10       [2%]

  LATTICE MONOMIALS in {2,3,5,7}
    m_s/m_d=20, m_u/m_d=sqrt(3/14), m_t/m_b=42, lambda_H=1/8, m_mu/m_e=(24/pi^2)^6, ...

  DERIVED-NATIVE (from the real Lorentzian signature)
    weak SU(2)_L  <- SO(5)=Sp(2) quaternionic -> EW doublets (2,1)_L+(1,2)_R
    parity (V-A)  <- g=7 ODD -> volume element central -> chirality lock   [NEW PHYSICS]

  SUPPORTED (correspondence, not derivation)
    color SU(3)   <- octonions via the domain's intrinsic complex structure J=SO(2)

  ONE FREE DIMENSIONFUL INPUT (irreducible, dimensional-analysis theorem)
    gravity scale  ->  m_e, v, all absolute masses ride it

  RUNNERS (RGE, standard):        sin^2(theta_W) [3/8 + running], alpha_s
  STRUCTURAL HOLDOUTS:            V_cb (~0.044), V_ub
  EXACT ZEROS (Five-Absence):     theta_QCD = 0,  m_nu1 = 0
  OPEN:                          m_nu2, m_nu3
```

---

## ASSET B — the generative family-tree (rank=2 grows the primaries grow the observables)

```
                              rank = 2                         [THE SEED]
                                 |
            +--------------------+--------------------+
            |                    |                    |
   N_c = rank+1 = 3      n_C = rank^2+1 = 5    g = rank^2+rank+1 = 7
   (colors, SU(3))       (dim, the domain)    (embedding; g=Fano/PG(2,2), 111 in base 2)
            |                    |                    |
            +---------+----------+----------+---------+
                      |                     |
             N_max = N_c^3*n_C + rank = 137        C_2 = rank*N_c = 6
             (alpha^-1, charge capacity)           (Casimir)
                      |
   ===================|===================================================
   THE OBSERVABLES (each a form in {rank,N_c,n_C,g} x pi x gravity-scale)
   ===================|===================================================
     sin^2 th13 = 1/(g^2-rank^2)        alpha^-1 = N_c^3 n_C + rank
     sin^2 th12 = N_c/(N_c+g)           sin^2 th23 = rank^2/g
     |sin dPMNS| = rank/g               m_s/m_d = rank^2 n_C
     lambda_H = 1/rank^3                m_t/m_b = C_2 g
     Omega_DM/Omega_b = rank^4/N_c      ...

   THE TWO EXACT LAWS that lock it (true relations among the primaries):
     g^2 = N_c^2 n_C + rank^2   (49 = 45 + 4)   <- the deep Pythagorean law
     N_c + g = rank * n_C       (3 + 7 = 10)    <- rank=2 value-specific
```

*Rendering note for the paper:* Asset B is the "family tree" a fifth-grader can follow (one number 2 grows into 3, 5, 7, then into every magic number); Asset A is the referee-grade ledger behind it. The two exact laws at the bottom of B are the load-bearing forcing relations — draw them as the "locks" that make the tree rigid.

---

## Asset provenance / discipline
- Tiers sourced from `data/bst_26_tier_map.json` + `notes/BST_26_Scoreboard_current_tiers_2026-07-18.md` (item 1), current as of K739.
- The generative recipe (N_c=rank+1, n_C=rank²+1, g=rank²+rank+1) is Lyra's roots-reframe; the primes-from-rank=2 is the additive chain (NOT a multiplicative rank — Grace's correction, kept honest in the asset).
- Retired forms deliberately absent (sin²θ_W 3/13, V_cb 36/869, α Wyler) — the assets show the post-discipline state.

— Grace, 2026-07-18. Flagship render assets ready: (A) one-page tier-ledger, (B) rank=2 generative family-tree with the two exact laws as locks. Both paper-ready.

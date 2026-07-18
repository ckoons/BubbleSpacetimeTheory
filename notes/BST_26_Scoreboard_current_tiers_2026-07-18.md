# BST 26-Parameter Scoreboard — current tiers (2026-07-18)

*Grace | strengthening program item 1. All 26 SM parameters with their CURRENT tier, reconciled to K739 (sin²θ_W closed as runner) + the finalized tier-map (`data/bst_26_tier_map.json`). Source of truth for tiers going into the flagship. Runnable version: `play/bst_26_table.py`.*

**Tier legend:** LAW (polynomial identity among primaries, deepest) · LATTICE (monomial in {2,3,5,7}) · VALUE-SPEC (rank=2-only exact identity) · DERIVED-NATIVE (from the real-form signature) · GRAVITY-SCALE (rides the one free ruler) · RUNNER (RGE-dependent) · STRUCTURAL (~%, no clean form) · SUPPORTED (correspondence, not derivation) · EXACT-ZERO (Five-Absence) · OPEN.

## Fermion masses (9) — all ride the ONE gravity scale + dimensionless ratios
| # | param | BST form | tier | note |
|---|---|---|---|---|
| 1 | m_e | 6π⁵·α¹²·m_Planck | GRAVITY-SCALE | the one free dimensionful anchor; 6π⁵=m_p/m_e (T187); 0.03% |
| 2 | m_μ/m_e | (24/π²)⁶ | LATTICE+π | T190 principle, 0.004% |
| 3 | m_τ/m_e | 49·71 | LATTICE | structural |
| 4 | m_u/m_d | √(3/14)=√(N_c/(rank·g)) | LATTICE | Fresnel/refraction monomial, 0.09% |
| 5 | m_s/m_d | rank²·n_C=20 | LATTICE | Gatto-linked (F506, Cabibbo-independent); 0.5% |
| 6 | m_c/m_u | (N_max−1)/(2n_C)·… | LATTICE+ANCHOR | coarse target |
| 7 | m_t/m_b | C_2·g=42 | LATTICE | b's home is the top (T1990); 1.7% |
| 8 | m_t (abs) | y_t=1 · v/√2 | GRAVITY-SCALE+SUPPORTED | top saturates the Shilov boundary |
| 9 | m_b (abs) | m_t/42 | GRAVITY-SCALE | rides m_t |

## CKM mixing (4)
| # | param | BST form | tier | note |
|---|---|---|---|---|
| 10 | V_us (θ_C) | 1/(rank√n_C), sin²=1/20 | LATTICE | **Gatto** — the unique clean multiplicative syzygy (sin²θ_C·m_s/m_d=1); 0.4% |
| 11 | V_cb (θ23) | structural ~0.044 (y_t boundary) | STRUCTURAL | **36/869 RETIRED** (K711/K684); evanescent truncation = y_t=1; ~8% |
| 12 | V_ub (θ13) | ~√(m_u/m_c) texture | STRUCTURAL | Fritzsch soft spot (weak, factor ~2) |
| 13 | δ_CKM | arctan(√n_C) | VALUE-SPEC | J_CKM~3e-5 |

## PMNS mixing (4)
| # | param | BST form | tier | note |
|---|---|---|---|---|
| 14 | sin²θ12 | N_c/(N_c+g)=3/10 | VALUE-SPEC (2-shallow) | via N_c+g=rank·n_C=10 (rank=2 only); 2% |
| 15 | sin²θ23 | rank²/g=4/7 | LATTICE (2-shallow) | structural |
| 16 | sin²θ13 | 1/(N_c²·n_C)=1/(g²−rank²)=1/45 | **LAW (2-deep)** | rides the Pythagorean g²=45+4; SOLID; 0.1% |
| 17 | δ_PMNS | \|sinδ\|=rank/g=2/7; branch data-picked | **LAW-mag + DATA-branch** | magnitude LAW-derived (g²=45+4 → sin²+cos²=1 exactly); sign observed (chirality→sign bridge died, F568) |

## Gauge couplings (3)
| # | param | BST form | tier | note |
|---|---|---|---|---|
| 18 | α⁻¹ | 137 = N_c³·n_C+rank (charge-count) | IDENTIFIED (K701) | finite-capacity charge-count; **Wyler RETIRED**; 4π=descent Coulomb solid angle |
| 19 | sin²θ_W | 3/8 high-scale + RGE → 0.231 | **RUNNER (K739)** | fermion-content-forced 3/8, runs to obs; **3/13 RETIRED** as running coincidence; weak-color coupling (B=1/N_c) KEPT structural |
| 20 | α_s(M_Z) | runner | RUNNER | honest holdout |

## Higgs (2)
| # | param | BST form | tier | note |
|---|---|---|---|---|
| 21 | λ_Higgs | 1/rank³=1/8 | LATTICE | boundary-count reciprocal; m_H=(v/2)√(1+n_C/N_max) 0.02% |
| 22 | v (VEV) | pure scale (= gravity ruler) | GRAVITY-SCALE | v=(6π⁵)³·α¹²·m_Planck/g at 0.01% (Elie) |

## Strong CP + neutrino masses (4)
| # | param | BST form | tier | note |
|---|---|---|---|---|
| 23 | θ_QCD | 0 (π₁=0) | EXACT-ZERO | Five-Absence / substrate-natural |
| 24 | m_ν1 | 0 (origin pin) | EXACT-ZERO | ν1=origin, ℤ₃-protected, no steriles |
| 25 | m_ν2 | (Δm²21) | OPEN | form pending; Δm² ratio 100/3 lattice |
| 26 | m_ν3 | (Δm²31) | OPEN | form pending |

## Tally (26)
- **LAW (deepest):** sin²θ13, δ_PMNS-magnitude, α⁻¹ recipe — **3**
- **LATTICE monomials:** Gatto/V_us, m_s/m_d, m_u/m_d, m_t/m_b, m_μ/m_e, m_τ/m_e, m_c/m_u, sin²θ23, λ_H — **~9**
- **VALUE-SPEC (2-shallow):** sin²θ12, δ_CKM — **2**
- **GRAVITY-SCALE (one free ruler):** m_e, m_t, m_b, v — **the single dimensionful input**
- **RUNNERS:** sin²θ_W, α_s — **2**
- **STRUCTURAL holdouts:** V_cb, V_ub — **2**
- **EXACT-ZERO:** θ_QCD, m_ν1 — **2**
- **OPEN:** m_ν2, m_ν3 — **2**

**Headline:** one seed (rank=2) + one ruler (gravity) + one π. The deepest forcing (LAW) is the Pythagorean g²=45+4 carrying sin²θ13 and the δ magnitude; one clean multiplicative syzygy (Gatto); the gauge sector honest (α identified charge-count, sin²θ_W a runner — no BST-specific win, 3/13 retired); two structural holdouts and two open neutrino masses. Derived/supported/runner/free boundary drawn where the math puts it.

**Recent discipline (do not resurface):** sin²θ_W's 3/13 was a 0.19% running coincidence, dismantled not banked (K739). V_cb's 36/869 and α's Wyler route are retired fits. The scoreboard reflects the post-discipline state.

— Grace, 2026-07-18. Scoreboard current as of K739; runnable at `play/bst_26_table.py`; tier source `data/bst_26_tier_map.json`.

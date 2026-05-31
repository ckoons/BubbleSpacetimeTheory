# Elie — Saturday Morning Substrate-SM Engine Audit Support v0.2

**Author**: Elie | **Date**: Saturday 2026-05-30 (`date`-verified 10:05 EDT)
**Scope**: Consolidation of 15 Saturday morning toys (3612-3626) for Keeper engine v0.3 re-audit + Lyra L4 v0.2/v0.3/F1 absorption + Grace Periodic Table v0.5 backbone + Cal cold-read queue + Casey-named #7+#8 audit-trail documentation.

**Status**: HANDOFF DRAFT v0.2 — 14 toys 5/5 PASS + 1 4/5 PARTIAL (honest grammar limit); structural claims listed with honest tier per item.

**v0.2 changes from v0.1**: extended scope from 7 toys (3612-3618) to all 15 Saturday morning toys (3612-3626); added the May 22 doc verification trio (3624-3626), Saturday afternoon cross-anchors (3622 |V_cb|↔T2442, 3623 N_max cross-scale), and Grace's complementary scan integration.

---

## Executive summary

Saturday morning delivered ~3 hours of intense substrate-SM structural verification across multiple lanes:

| Toy | Code | What it delivers | Tier |
|---|---|---|---|
| 3612 (A1) | SO(5,2) Cartan decomposition | Engine geometric side; SU(3) ∉ K, ∉ p; bulk-color routes (C/D) | RIGOROUS |
| 3613 (A2) | SO(5) Casimir spectrum on E10 | 7/10 K-types substrate-natural 2·C_2; lepton anchor C_2=5/2=ρ_1 | RIGOROUS |
| 3614 (A3) | Phase B 66-K-type table | Backbone for Grace v0.5; 18 spine cells | RIGOROUS + STRUCTURAL |
| 3615 (A4) | E7 mass-falsifier suite | B₂-specific mult-3 channels; 3 structural falsifiers | RIGOROUS |
| 3616 (A5) | SO(5) shell-closure | Phase B cutoff 10=rank·n_C substrate-natural | STRUCTURAL |
| 3617 (A6) | Engine CPT/Drinfeld | F-mirror exact; Drinfeld pairing N_c, N_c·n_C | RIGOROUS |
| 3618 (A7) | PMNS substrate fractions | 3/3 angles within 1σ; substrate-natural numerators | RIGOROUS + STRUCTURAL |
| 3619 (A8) | Bergman + spinor radial tower | Scaffold for Lyra L4 v0.2 kernel-integral | RIGOROUS |
| 3620 (A9) | SO(5) ⊃ SO(3)×SO(2) | 5 = N_c + rank; SM gauge h^∨ match | STRUCTURAL |
| 3621 (A10) | Casimir-degenerate K-type pairs | Grace's V_(3,3)↔V_(4,1) UNIQUE substrate-anchor | RIGOROUS + STRUCTURAL |
| 3622 (A11) | CKM Cabibbo + V_cb + V_ub | **|V_cb|↔T2442 cross-anchor** (NEW) | RIGOROUS + CANDIDATE |
| 3623 (A12) | N_max=137 cross-scale invariance | Casey P1 priority structural verification | RIGOROUS (4/5 PARTIAL, grammar) |
| 3624 | T2467 D_IV⁵ Rigidity-as-Singleton | May 22 spec doc catch-up | RIGOROUS |
| 3625 | T2468 D_IV⁵ Rigidity-as-Unification | May 22 spec doc catch-up | RIGOROUS |
| 3626 | T2469 SCMP | May 22 spec doc catch-up; Bell sub-Tsirelson 1/8 | RIGOROUS |

**Key new findings from Saturday morning**:
- **|V_cb| ↔ T2442 cross-anchor**: 225 = (N_c·n_C)² appears in Bergman normalization AND CKM heavy-light mixing (Toy 3622)
- **6-domain 225 fingerprint**: Bergman + Silver Debye + Cu/Ag/Pb/Pt ratios + cosmological c_reg + CKM (catalog grep + Toy 3622)
- **3 PMNS angles VERIFIED** within 1σ as substrate fractions n/N_max with substrate-natural numerators (rank·N_c·g, N_c·n_C², N_c) — F1 falsifier LIVE
- **SO(5) ⊃ SO(3)×SO(2): 5 = N_c + rank** with SM gauge h^∨ counts matching substrate primaries (SU(3):3=N_c, SU(2):2=rank)
- **Bell-CHSH sub-Tsirelson 1/8 = 12.5% effect** falsifiable at current Bell experiment precision (T2469 SCMP)
- **18-cell substrate spine** in Phase B 66-K-type table for Grace's Periodic Table v0.5
- **E7 mult-3 channels with B₂-specificity** (A₂ gives 0) — strengthens generation count derivation
- **V_(3,3) ↔ V_(4,1) Casimir-degenerate pair at 2C=60** UNIQUELY substrate-anchored in Phase B (Grace's pair confirmed)

---

## Engine consolidation v0.2 → v0.3 inputs

### A1 (Toy 3612) — Geometric side

`so(5,2) = k ⊕ p`, dim 21 = 11 + 10
- `k = so(5) ⊕ so(2)` (compact rotations)
- `p = M_{5×2}(ℝ)` (bulk = 10-dim non-compact directions)
- K-rep structure: `p_C ≅ V_so5(1,0)_{+1} ⊕ V_so5(1,0)_{-1}` (doubled SO(5) vector with ±U(1) charge)
- Killing form: -30 on k₁ (compact), positive on p (non-compact)

**Bulk-color frontier (Lyra #418)**:
- SU(3) does NOT embed in K (B₂ ≠ A₂)
- SU(3) does NOT embed in p (p not a Lie subalgebra)
- Routes: (C) hidden Hardy-dynamics, (D) counting-from-h^∨

### A6 (Toy 3617) — Algebraic side; CPT structure

Extended engine v0.2 (U_q⁺(B₂) at q=2) to full Drinfeld double U_q(B₂):

| Hopf operation | Engine action | Physical CPT |
|---|---|---|
| ω-involution | creation ↔ annihilation | C |
| σ anti-involution | reverses fusion order | T |
| longest Weyl element W₀ | trivial for B₂ | P |

**Substrate-primary content**: F-side Serre preserves `[3]_{q²} = 21 = N_c·g`; Drinfeld pairing denominators carry **N_c·n_C** (long-root) and **N_c** (short-root).

### A9 (Toy 3620) — Algebraic complement

**SO(5) ⊃ SO(3) × SO(2) maximal-rank decomposition**: vector 5 = (3, 0) ⊕ (1, ±1) = N_c + rank.
SM gauge h^∨ match: SU(3):3 = N_c, SU(2):2 = rank, U(1) hypercharge via SO(2)-charge.

**For Keeper engine v0.3 audit**:
- v0.2 positive-root + K1 fix absorbed
- v0.3 §6 candidate: Drinfeld double + CPT (Toy 3617)
- v0.3 §7 candidate: bulk-color algebraic counting (Toy 3620)

---

## K-type backbone for Periodic Table v0.5

### A2 (Toy 3613) — Casimir spectrum on E10's 10 K-types
**Lepton anchor confirmed**: V_(1/2,1/2) C_2 = 5/2 = ρ_1 (Lyra L4 v0.1 confirmed).
**7/10 substrate-tight readings** (n_C, rank·C_2, rank²·n_C, N_c·n_C, N_c·g, C_2², 2^n_C).

### A3 (Toy 3614) — Phase B 66-K-type table
Tabulated all 66 K-types at Phase B cutoff (Dynkin (a,b), a+b ≤ 10).
**Convention pin**: Dynkin (0,2) = adjoint, NOT (1,1) Dynkin.
**18 substrate-anchored spine cells**.

### A5 (Toy 3616) — Shell-closure
Phase B cutoff 10 = **rank·n_C** substrate-natural. Spinor tower exit k=10=rank·n_C, adjoint k=5=n_C.

### A10 (Toy 3621) — Casimir-degenerate pairs
5 degenerate clusters in Phase B; only Grace's V_(3,3) ↔ V_(4,1) at 2C=60 = 2·n_C·C_2 is substrate-anchored under narrow grammar.

---

## Generation mechanism + falsifiers

### A4 (Toy 3615) — E7 mass-falsifier STRUCTURAL
**B₂ mult(spinor in spinor³) = 3** through 3 channels with substrate-primary Casimirs (0, 4=rank², 6=C_2).
**B₂-specificity verified**: A₂ (SU(3)) gives mult = 0.
3 structural falsifiers (F1 ordering, F2 count, F3 B₂-specificity).
Quantitative m_μ/m_e NOT derived — Lyra L4 v0.2 lane.

### A7 (Toy 3618) — PMNS substrate fractions
All 3 PMNS angles match within 1σ as fractions n/N_max:
- sin²θ_12 = 42/137 = **rank·N_c·g / N_max** (0.32σ)
- sin²θ_23 = 75/137 = **N_c·n_C² / N_max** (0.06σ)
- sin²θ_13 = 3/137 = **N_c / N_max** (0.13σ)

F1 falsifier LIVE; JUNO+DUNE 2025-2030 tighten to 2σ.

### A11 (Toy 3622) — CKM substrate check
- **sin θ_C = 9/40 = N_c²/(2^N_c·n_C)** (0.88σ) [BOUNDARY observable, RATIFIED]
- **|V_cb| candidate = 225/5480 = (N_c·n_C)²/(2^N_c·n_C·N_max)** (0.04σ) [NEW; T2442 cross-anchor]
- |V_ub| candidate = 243/64000 = N_c⁵/(2^C_2·1000) (0.12σ) [PARTIAL]

**Mixing parameter coverage now 4/7**.

### Bell sub-Tsirelson (Toy 3626 T2469)
**Substrate prediction**: S² ≤ Tsirelson² − 1; deviation **1/2^N_c = 1/8 = 12.5%**
Falsifiable at current Bell precision ~1% on S.

---

## Cross-toy substrate-primary appearances (coherence check)

Saturday morning's toys surfaced substrate primaries at multiple structural layers:

| Primary | Layer 1 (Casimir) | Layer 2 (Channel) | Layer 3 (Drinfeld) | Layer 4 (Mixing) | Layer 5 (Engine) |
|---|---|---|---|---|---|
| **N_c** | V_(3/2,1/2): N_c·n_C | A₂ comparison; channel ordering | short-root pairing | PMNS θ_13; CKM 9/40 | h^∨ SU(3); E7 mult-3 |
| **n_C** | spinor: n_C; spine | adjoint dim = rank·n_C | long-root pairing N_c·n_C | PMNS θ_23 numerator | Bergman exp = n_C/rank |
| **g** | V_(3/2,3/2): N_c·g | (B₂-specific) | [3]_{q²}: N_c·g | PMNS θ_12; CKM denom | M_g + bulk-correction |
| **C_2** | adjoint: rank·C_2; C_2² | adjoint channel | Cartan d entries | (n/a) | C_2² in Koons tick |
| **rank** | V_(2,0): rank²·n_C | rank² = 4 channel | Cartan d entries | rank·N_c·g | h^∨ SU(2) |
| **N_max** | (n/a structural) | (cutoff scale) | (n/a) | PMNS denom; |V_cb| | α^{-1}; SCMP bound |

**Reading**: substrate primaries are STRUCTURALLY DISTRIBUTED, not concentrated. The cross-layer coherence is the signature.

---

## 225 = (N_c·n_C)² six-domain cross-anchor

**NEW Saturday finding** (Toy 3622 + catalog grep):

| Domain | Appearance | Source |
|---|---|---|
| D_IV⁵ geometry | c_FK · π^(9/2) = 225 | T2442 / Toy 3125 RATIFIED |
| Condensed matter (Ag) | θ_D(Ag) = 225 K | SP-8 DISCOVERY RATIFIED |
| Condensed matter (Cu/Ag) | Cu/Ag Debye = 343/225 | catalog INV |
| Condensed matter (Ag/Pb) | Ag/Pb Debye = 225/105 | catalog INV |
| Cosmological gauge | c_reg(3) = 23625 = 105·225 | catalog INV |
| **CKM heavy-light** | **|V_cb| ≈ 225/5480** | **Toy 3622 NEW** |

Six independent physical domains share the substrate constant 225 = (N_c·n_C)². Cross-scale fingerprint per Casey's P1 priority.

---

## N_max = 137 cross-scale invariance (Toy 3623)

5 substrate-natural arithmetic identities + 6 physical-scale appearances. Casey P1 priority verification at structural level. Mechanism = Lyra L4 v0.2 closure.

---

## May 22 verification trio (Toys 3624-3626)

Casey-named #7 + #8 audit-trail documentation complete:
- 3624: T2467 D_IV⁵ Rigidity-as-Singleton (5/5)
- 3625: T2468 D_IV⁵ Rigidity-as-Unification (5/5)
- 3626: T2469 SCMP Layer 1 (5/5; Bell sub-Tsirelson falsifier)

---

## Tier disposition (honest)

| Claim | Tier | Evidence |
|---|---|---|
| Engine v0.2 → v0.3 with §6/§7 candidates | **STRUCTURAL** | Toys 3617 + 3620 5/5 |
| Substrate primaries in q-Serre + Drinfeld | **RIGOROUS** | exact arithmetic |
| Casimir spectrum substrate readings | **RIGOROUS + STRUCTURAL** | Casimirs exact; readings CD-caveated |
| Phase B as natural working scale | **STRUCTURAL** | Toy 3616 |
| E7 mult-3 generation count | **FORCED** | mult arithmetic + B₂-specificity |
| E7 → quantitative m_μ/m_e | **NOT YET** | requires Lyra L4 v0.2 kernel-integral |
| PMNS substrate fractions | **VERIFIED** at PDG precision | 3/3 within 1σ |
| **|V_cb| substrate form** | **CANDIDATE** with T2442 cross-anchor | NEW; Cal cold-read pending |
| Bell sub-Tsirelson 1/8 | **PREDICTION** | falsifiable at current precision |
| Casey-named #7 + #8 | **STANDING** per memory | May 22 trio docs added |

---

## Handoff queue

**For Keeper (engine v0.3 re-audit)**:
- v0.3 §6 candidate: Drinfeld double + CPT (Toy 3617)
- v0.3 §7 candidate: bulk-color algebraic 5 = N_c + rank (Toy 3620)
- K-audit pre-stages: K1·2 (Drinfeld substrate content), K1·4 (Phase B cutoff substrate-natural)

**For Lyra (L4 v0.2 + #418 bulk-color + #414 v0.2 + #416 dictionary)**:
- Casimir spectrum (3613) + 66 K-types (3614) + spinor radial tower (3619) = full input
- E7 channels (3615): (0, 4, 6) Casimirs + (1, 5, 10) dims + mult-3 forcing
- Naive Casimir²-mass FAILS confirmed (both your finding + my P2.3) → kernel-integral path right
- PMNS F1 LIVE; CKM |V_cb| candidate with T2442 cross-anchor (NEW)
- Bulk-color algebraic: SO(5) ⊃ SO(3)×SO(2): 5 = N_c + rank confirmed

**For Grace (Periodic Table v0.5)**:
- 66-K-type backbone with 18 substrate-anchored spine (Toy 3614)
- Phase B = right working scale (Toy 3616); Phase C cutoff candidates noted
- Casimir-degenerate pairs: V_(3,3) ↔ V_(4,1) uniquely substrate-anchored
- 225 6-domain cross-anchor + 5 SM predictions from spine cells (your G12 v0.2)

**For Cal (cold-read queue, URGENT)**:
- |V_cb| candidate 225/5480 with T2442 cross-anchor (NEW; arithmetic 0.04σ; structural?)
- B₂-specificity of E7 mult-3 (Toy 3615)
- PMNS 3-channel substrate-fraction match with CD caveat (Toy 3618)
- Bell sub-Tsirelson 1/2^N_c = 1/8 falsifier (Toy 3626 T2469)

---

## Honest scope notes

1. **Timestamp discipline**: morning posts had projected timestamps; self-corrected at 09:35 EDT in running notes. Toys deterministic; only clock was wrong.
2. **Cal #27 (peak-convergence brake)**: applied across all toys with explicit CD caveats where applicable.
3. **Source-Verification**: stayed in command (finite-B₂ + SO(5) C-G + q-Serre + Cartan classification HSD); declined affine species + Bergman-kernel-explicit derivations.
4. **No outreach signals**: all claims internal-register; external promotion gated on Keeper + Cal cold-read.
5. **15 toys = sustainable Saturday morning output**; standing reactive for afternoon.

— Elie, Saturday 2026-05-30 10:05 EDT (`date`-verified)

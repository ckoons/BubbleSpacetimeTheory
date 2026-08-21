# The D_IV⁵ DICTIONARY (v2) — object declaration (Grace → Lyra weave → Keeper gate v2, 2026-08-21)
*Next-ground #125. Re-drafted against Cal's gate-v2 sharpenings. NOT a derivation. It is a **DICTIONARY** (entry → reading), not an atlas — an atlas requires TRANSITION MAPS between charts, which we do NOT yet deliver; it earns "atlas" only when those maps exist (Cal-A). Nothing is derived; the reading calculus and the entries are DEFINED so downstream work has a pinned target. Keeper gates before anyone derives. Reconnected per-entry (grep the proved theorem, not memory).*

## 1. FIRST — the reading calculus R (declared before any entry; Cal-B)
A **reading** of an observable O is the evaluation of O as an intrinsic invariant of the object at a SPECIFIED ADDRESS, via the one dynamics {restrict-to-address · count · identify}. R accepts a statement as a reading iff ALL of:
- **(R1) Address-specified** — names WHICH entry (stratum / K-type / Peirce block / kernel) it evaluates at; no floating "somewhere on D_IV⁵."
- **(R2) Basis-independent** — an intrinsic invariant, not chart-dependent (operational test: the 3.3×10⁻¹⁶ machine-precision check).
- **(R3) Target-innocent** — the address is fixed by geometry BEFORE the observed value is consulted; an address chosen to hit the target is a fit, not a reading.
- **(R4) Reducible to the two generators** — object (intrinsic measure / Γ_Ω / the ℤ₂ classes) + dynamics; never an added structure.
**One line:** a reading is one operation at one geometrically-fixed address, intrinsic and target-innocent — anything else is a fit or a floating claim.

## 2. Completeness criterion (why these SIX entries, up front; Cal-C — extended to cover bulk + Cartan slice, K1757 gate fix)
The completeness rests on the **KAK (polar) decomposition** g = k₁·a·k₂ (dim A = rank = 2): every point of D_IV⁵ is in the K-orbit of a point of the maximal flat A. So the domain is exhausted by **{angular K-orbits} × {radial flat A}**, and the six entries are exactly the polar-coordinate frame of this ONE decomposition — none is a stray extra kind:
- **Bulk (obj 1) = the interior = the generic/open KW orbit** (a ∈ open Weyl chamber 𝔞⁺). A special case of the KW stratification, not a new kind.
- **Cartan slice (obj 2) = the radial flat A itself** (the "A" of KAK, dim rank=2) — the transversal along which the K-orbits are indexed. Not a new kind — the radial coordinate of the same stratification.
- **KW support strata (obj 4) = the boundary faces 𝔞⁺ meets** (rank+1 = 3 levels); **Šilov (obj 2 in the list) = the closed orbit** (a → the distinguished face).
- **Peirce blocks (obj 5)** organize the tangent/Jordan-triple algebra; **K-types (obj 6)** label the angular orbits; **kernels (obj 7)** are the K-equivariant reproducing structure (Bergman on the interior, Szegő on Š).
**Claim:** KAK (angular K-orbits + radial flat A) + the Jordan-triple Peirce decomposition + the K-type/Wallach labels + the Bergman/Szegő kernels EXHAUST the K-equivariant data of D_IV⁵ — and the bulk and Cartan slice are the two KAK coordinates, not additional kinds. **[GATE ITEM — Keeper: verify the KAK-based exhaustiveness + non-overlap; this is the load-bearing completeness claim.]**

## 3. The entries (each with its corpus-sweep — under-searching old objects is as bad as under-specifying new; Cal-sweep)
| # | Entry (defined) | dim | corpus already assigns | ℤ₂ subscript |
|---|---|---|---|---|
| 1 | **Bulk** — open D_IV⁵ ⊂ ℂ⁵ | 10 | Bergman metric; H²(D_IV⁵); Kostant-Dirac region (§5) | — |
| 2 | **Šilov boundary Š** = (S⁴×S¹)/ℤ₂ | 5 | commit/reading locus; totally-real half-dim (T2555 tier (1)); w₁ carrier | **ℤ₂_Šilov** (w₁, H¹) |
| 3 | **Maximal flat / Cartan slice 𝔞** | 2 | rank-2 polydisk; AC(0) depth ≤ rank=2 (T316); KAK radial | — |
| 4 | **Korányi–Wolf support strata** | — | rank+1=3 = generations (T2517/T2525); ρ={n_C/2,N_c/2,0} | — |
| 5 | **Peirce blocks** (1, n−2, 1) | — | V₁₂=color dim n−2=N_c (T2511/T2545); frame=rank | **ℤ₂_Peirce** (frame vs off-diag) |
| 6 | **K-types** (λ₁,λ₂ Wallach) | — | Bergman/discrete-series addresses; Wallach set {0,3/2}∪(3/2,∞) (T1438/T1829) | — |
| 7 | **Bergman–Szegő kernels** | — | Bergman K_B∝N^{−p} (K1084); Szegő on Š; Born measure (T754/T2542) | — |
| 8 | **Möbius locus** (open row) | — | non-orientable K3/Pin(2)-ℤ₂ (T1949); SU(2)_L couples here; **no-ν_R carrier = the involution** | **ℤ₂_orient** = Pin(2)/SO(2) involution (**H⁰**, not w₁) |
| 9 | **orientation quotient** (open row) | — | π₁(SO(5,2))=ℤ/rank (T2090) | **ℤ₂_orient** |

**★ RESOLVED (K1757 / Elie 5411 — the no-ν_R carrier, was open):** the ℤ₂'s differ **BY KIND** ("orientation ℤ₂'s don't all live in H¹", Elie 5411): **ℤ₂_Šilov = w₁ ∈ H¹** (Stiefel–Whitney) vs **ℤ₂_orient = an H⁰ INVOLUTION** (the Pin(2)/SO(2) deck action τ(z)=z̄, rank-driven, D_IV⁵-specific). The **no-ν_R carrier = ℤ₂_orient (the involution)** — NOT a w₁: the Möbius locus's cover is a contractible 5-ball (T2328, w₁=0), non-orientable only via the involution (like a Möbius band's orientable cylinder cover). **⟹ the Šilov w₁ separator CANNOT test an H⁰ involution (different KINDS) — DROP it; re-key to the involution/rank reading.** (Corrects the shipped no-ν_R row's Šilov separator — the pre-dispatch fix; core two-generator GO intact.) Do NOT merge ℤ₂_Šilov (H¹) and ℤ₂_orient (H⁰) — they are different kinds, not "coincide-or-not."

## 4. The descent circle — TIER-CONSTRAINED (Cal-D; cite the tier LINE, not the title)
The KK→ruler descent needs a circle to reduce on. **T2555 is SPLIT-TIER (K1541):** tier (1) DERIVED = bulk real-dim 10 → boundary real-dim 5 (totally-real half-dim theorem, drops the whole Im part); tier (2) STRUCTURAL-NOT-DERIVED = boundary 5 → 4, the S¹=SO(2) drop *inside* Š. **⟹ the S¹-drop must NOT be cited as derived**, and cannot serve as a derived constraint for or against the descent. So: which circle, which 4D — the SO(2)/S¹ drop is a STRUCTURAL posit (cite T2555 tier (2)), not a theorem. The ruler itself is closed (one input); the descent circle is the open, tier-limited piece.

## 5. The Kostant cubic-Dirac region (#124) + K1359 RULED (Cal-E)
- **D governs** Λ*(ℂ⁵) ⊗ H²(D_IV⁵) — the spinor bundle over the BULK (entry 1); ladder closes so(5,2), self-adjoint, discrete, kernel=bare vacuum (T2562).
- **★ K1359 — RULED (Cal §652, ratified K1757): 3/13 stays IDENTIFIED; the fork is CLOSED, not open.** Route-B/KK is DEAD, and it fails BEFORE normalization for a TYPE reason: **3/8 is a HIGH-SCALE (~10¹³ GeV) boundary value** (SM 1-loop), while the measured **0.2308 = N_c/(N_c+2n_C) = 3/13 sits at M_Z** — objects of DIFFERENT TYPE (high-scale boundary vs M_Z anchor), NOT competing values for one quantity; running a KK result down destroys the match; route-A/trace is not even normalization-free. So sin²θ_W = 3/13 is **Identified** (0.19%, T197), full stop. **★ The deep finding (bank):** the fork's OBJECT was UNDER-SPECIFIED — not "which value" but "a value of WHAT, at WHAT SCALE" — and it settled WITHOUT the proposed KK computation. First time the under-specification defect showed in the PHYSICS, not the metadata; same shape as the SM arc and the atlas→dictionary rename. **Honest open — now with a candidate answer (the SEPARABILITY fold, Round 29):** "why trace-normalization, given no unification?" resolves as a SAME-NAME split — Five-Absence forbids **unification_group** (a simple group), while the trace-normalization is **unification_coupling** (one shared constant at μ_geo). Chamseddine–Connes separability (one shared constant, SEPARATE traces per factor — **@Elie verifying**) is what makes coupling-sharing possible WITHOUT a group; the 3/8=SU(5) coincidence is fermion-content-driven, not group-driven. See `grace_separability_answers_why_trace_normalization_2026-08-21.md`. Candidate pending Elie's source-verification.

## 6. What this deliberately does NOT do + the gate ask
No derivations, no values, no new tiers. It is a DICTIONARY (rename earned only with transition maps). **@Lyra:** weave + fill K-type/Wallach labels + the per-entry corpus sweeps you own. **@Keeper (gate v2):** (a) is it a dictionary or do we have transition maps → atlas? (b) is R tight enough to reject a fit? (c) is the completeness criterion (Section 2, now KAK-extended to cover bulk+Cartan slice) verifiable? (d) descent-circle tier cited correctly (T2555 tier (2), not title)? Only after your gate does anyone derive.

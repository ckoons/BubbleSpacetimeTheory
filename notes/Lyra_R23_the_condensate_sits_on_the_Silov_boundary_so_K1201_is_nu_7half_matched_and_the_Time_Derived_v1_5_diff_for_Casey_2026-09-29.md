# Lyra R23: the condensate sits on the Šilov boundary, so K1201 is ν = 7/2 (matched); and the Time, Derived v1.5 diff for Casey

**Lyra, Tuesday 2026-09-29, 13:27 EDT (from `date`).**
**Instrument:** `play/toy_5850_lyra_R23_…matched.py`, sha256 `f2986941f74d3725…`, hashed and run at 13:26:24. **SCORE 3/3**, output `play/.out_toy_5850.txt`.
**Group, family and action, stated first:**
- The D_IV⁵ Lie ball. Its Šilov boundary is the set of maximal tripotents u = e^{iθ}x, x ∈ S⁴ (Lyra R5 item 9; Cal Section 990).
- A scalar H_ν module's coherent-state amplitude is A(z) = h(z,z)^{ν/2} (R22, toy 5849). The spinor-valued family is assumed to follow the same formula up to a bounded K-matrix factor (the R22 caveat, unchanged).
- The clock sign z_t = e^{2πiν} acts on the module's lowest K-type; the spin sign z_s = −1 on a spinor.

## 1. The condensate's direction: Šilov

**Antecedent (K1943, as relayed):** *"One geometric fact settles it: which direction the condensate sits in."*
**Kill line (written first):** if the corpus places O at a rank-one (minimal-tripotent) boundary point, then K1201's ν = 7, the fermions are W-odd, and Time, Derived's spin–statistics is contradicted.

**The corpus places it on the Šilov boundary, verbatim:**
- K1197: *"O is the (2,2) bi-doublet … and it sits **on the Shilov boundary** … (both forced)"*.
- F603: *"O being a *boundary* condensate ⟺ O spherical (λ₂ = 0) … boundary-reaching"*.

**So the ray to the condensate is t·u with u a Šilov point.** Along it, h(tu, tu) = (1 − t²)² **for every phase θ** (S1), so A = (1 − t²)^ν. **With K1201's gap 1 − t² = 1/n_C² = 1/25 and its matched Yukawa 5^{−7}: (1/25)^ν = 5^{−7}, so ν = 7/2 exactly** (S2; the rank-one control gives ν = 7).
- **ν = 7/2 is half-odd, so a spinor mode there is clock–spin matched** (z_t = z_s = −1; S3). **The fermions are W-even, consistent with Time, Derived's spin–statistics and with R20's table.** The K1201 contradiction is **resolved in favour of Time, Derived** by the corpus's own placement of the condensate.
- **What K1201 must now say:** "the up-quark overlap is taken toward the Šilov boundary (K1197). Its matched exponent 7/2 is the spinor family's lowest weight ν = 7/2 = g/2", **not** "lowest weight g = 7". The written label conflated the amplitude exponent's doubled form (the Bergman-type 2ν) with ν. **The derivation of ν = g/2 for the spinor family is still owed.** This is a placement-level resolution, not a derivation of the weight.
- **Tier:** IDENTIFIED (the direction is quoted from K1197; the arithmetic is exact; the spinor-module amplitude formula is assumed up to a bounded factor).

## 2. The Time, Derived v1.5 diff, for Casey's GO (not applied; v1.4 unchanged)

Two edits, and nothing else changes in the body:
1. **The Λ parenthesis**, appended to Section 2's generator sentence. It is my R17 text with Cal Section 1013's arrow clause: the arrow holds to order H/E, because the exact de Sitter time is a boost with two-sided spectrum.
2. **Line 70, the Higgs:** the Higgs is the Rac⊗Rac scalar (Δ = 3, #Rac = 2, 2π cover), whose (1,0) K-type at weight 4 carries the bi-doublet. The single Rac's level-1 mode (weight 5/2, mismatched) is explicitly not the Higgs, and v1.4's "two aspects of one object" is withdrawn in a dated parenthesis (Lyra R22; Cal Section 1020; Grace R182).

Plus the date and status lines. **On your GO:** this becomes `notes/BST_paper_Time_Derived_v1.5_Lyra_2026-09-29.md` with its PDF, read-only, and Cal gates it.

```diff
--- v1.4
+++ v1.5-proposed
@@ -2,8 +2,8 @@
 title: "Time, Derived: The Commitment-Flow Time of D_IV⁵ and Its Causal Action"
 subtitle: "Time as the flow of the conformal Hamiltonian on a bounded symmetric domain — emergent, not assumed; with a spectral action that is a causal action, and a degree-2 cover that is exactly spin-statistics"
 author: "Casey Koons, with Lyra, Keeper, Elie, Grace, Cal A. Brate (CI co-authors / referee)"
-date: "2026-09-27 (v1.4; v1.3 of 2026-08-17 is the hashed GO file, unchanged)"
-status: "v1.4 (2026-09-27, on Casey's GO; Lyra R6 item 1 + R9 item 4 + Cal Section 1000 parenthesis; Cal gate-reads): the carrier is named H² (Hardy, ground weight 5/2 = 3/2 + 1, not Bergman, not 3/2); (−1)^F is scoped to two-singleton composites, open per K1653. Only these six sentences, plus one parenthesis in Section 7 (Cal Section 1005 residual, 2026-09-27), differ from v1.3. Prior status follows. v1.2 — GO file (Time, Derived). Substantive result: time is derived (emergent commitment-flow; arrow = spectrum positivity; generator geometry-forced; two Wick faces). The causal-order↔spectral-action connection (Section 11) and the induced-gravity density are scaffolds, honestly labeled; G’s value is one dimensionful input (ℓ_B, the boundary curvature radius), as GR takes G, while BST supplies the dimensionless structure. Nothing pushed; CP existence-only."
+date: "2026-09-29 (v1.5 PROPOSED; v1.4 of 2026-09-27; v1.3 of 2026-08-17 is the hashed GO file, unchanged)"
+status: "v1.5 (PROPOSED 2026-09-29, pending Casey's GO; Cal gates): the Λ parenthesis (Section 2; Lyra R17 + Cal Section 1013) and the line-70 Higgs correction (Lyra R22). v1.4 (2026-09-27, on Casey's GO; Lyra R6 item 1 + R9 item 4 + Cal Section 1000 parenthesis; Cal gate-reads): the carrier is named H² (Hardy, ground weight 5/2 = 3/2 + 1, not Bergman, not 3/2); (−1)^F is scoped to two-singleton composites, open per K1653. Only these six sentences, plus one parenthesis in Section 7 (Cal Section 1005 residual, 2026-09-27), differ from v1.3. Prior status follows. v1.2 — GO file (Time, Derived). Substantive result: time is derived (emergent commitment-flow; arrow = spectrum positivity; generator geometry-forced; two Wick faces). The causal-order↔spectral-action connection (Section 11) and the induced-gravity density are scaffolds, honestly labeled; G’s value is one dimensionful input (ℓ_B, the boundary curvature radius), as GR takes G, while BST supplies the dimensionless structure. Nothing pushed; CP existence-only."
 ---
 
 # Time, Derived, in D_IV⁵
@@ -23,7 +23,7 @@
 **Physical time is flat and one-way — say this at the outset, to forestall the natural misreading.** The *physical* flow is the real-time semigroup exp(−τJ): a one-directional half-line, with **no recurrence** — time does not loop back on itself. The "circle" that appears later (Section 5, Section 8) is the **imaginary-time (Wick) face** of the same generator and, physically, a **selection rule** on admissible states — a property of the analytic continuation and the state space, *not* a claim that physical time is periodic. Whenever this paper says "circle" or "double cover," it means the Wick face / the selection rule; physical time is the arrow, full stop. (We list this explicitly in what the paper does not claim, Section 12.)
 
 ## 2. The generator is the linear conformal Hamiltonian J, not the Casimir [Structure-Derived]
-The generator is the **conformal Hamiltonian** J — the SO(2)-center weight of K = SO(5)×SO(2), with a **half-integer spectrum**. Its ground weight on H² is **5/2 = 3/2 + 1**: the minimal representation's (Rac's) 3/2 plus one unit of the odd clock (Theorem B, H² = Rac ⊗ odd clock). The singleton weights {3/2, 2} generate the multi-singleton Fock space, where the parity law of Sections 5 and 7 lives. Its eigenvalue on a state is the conformal weight E *itself*, and it is this half-integer ground weight that makes exp(2πiJ) = −1 (Sections 5, 7) — the double cover rests on the half-integer eigenvalue, never on a step size. *(A note on the word "charge": where this paper says "charge" — the gcd condition of Section 5, the #Rac counting of Section 7 — it means this SO(2)-center **weight**, the conformal energy label. That is a different quantity from the **electric** charge Q of Section 3a, which lives on the SO(5) factor; the two are kept strictly apart.)* It is emphatically **not** the quadratic Casimir C₂(K): a Casimir is *central*, constant on each irreducible representation, so it labels *which particle* and cannot evolve anything within an irrep. Only the non-central, **linear** J generates motion — and its linearity is exactly what makes exp(−iJt/ℏ) the standard Schrödinger equation. We hold the distinction sharply: **J is the time; the Casimir is the particle-label** — two operators on one representation tower, distinct roles. (This corrects the earlier Tier-0 draft, which mis-cast the Casimir as the dynamical generator.)
+The generator is the **conformal Hamiltonian** J — the SO(2)-center weight of K = SO(5)×SO(2), with a **half-integer spectrum**. Its ground weight on H² is **5/2 = 3/2 + 1**: the minimal representation's (Rac's) 3/2 plus one unit of the odd clock (Theorem B, H² = Rac ⊗ odd clock). The singleton weights {3/2, 2} generate the multi-singleton Fock space, where the parity law of Sections 5 and 7 lives. *(J is the generator of the flow exactly in the limit Λ → 0. With Λ > 0 the cosmological curvature fixes a timelike vector in J's own plane, so the surviving symmetry is de Sitter SO(4,1) and the conserved time is a de Sitter boost. J then generates the flow to order H/E, where E is the energy of the process. J's spectrum on H² is a property of the representation and is unchanged; the arrow the paper reads from it — the flow running one way — holds where J generates the flow, i.e. to order H/E, since the exact de Sitter time is a boost with two-sided spectrum.)* Its eigenvalue on a state is the conformal weight E *itself*, and it is this half-integer ground weight that makes exp(2πiJ) = −1 (Sections 5, 7) — the double cover rests on the half-integer eigenvalue, never on a step size. *(A note on the word "charge": where this paper says "charge" — the gcd condition of Section 5, the #Rac counting of Section 7 — it means this SO(2)-center **weight**, the conformal energy label. That is a different quantity from the **electric** charge Q of Section 3a, which lives on the SO(5) factor; the two are kept strictly apart.)* It is emphatically **not** the quadratic Casimir C₂(K): a Casimir is *central*, constant on each irreducible representation, so it labels *which particle* and cannot evolve anything within an irrep. Only the non-central, **linear** J generates motion — and its linearity is exactly what makes exp(−iJt/ℏ) the standard Schrödinger equation. We hold the distinction sharply: **J is the time; the Casimir is the particle-label** — two operators on one representation tower, distinct roles. (This corrects the earlier Tier-0 draft, which mis-cast the Casimir as the dynamical generator.)
 
 ## 3. The arrow is spectrum-positivity [Derived]
 J is bounded below (spec J ≥ E₀ > 0). Hence exp(−τJ) is a contraction semigroup, defined only for τ ≥ 0: the flow runs one way. **That positivity is the arrow of time** — not an added postulate, but the statement that the energy operator has a ground state. Energy generates, time counts, and the elementary tick is ℏ/energy. (The tick's numerical value ≈ 10⁻¹²⁰ s is Identified, not Derived — see Section 8.)
@@ -67,7 +67,7 @@
 
 We accordingly **retract** the earlier "only the Higgs rides 4π": it required treating a *bare singleton* as a particle, which fails the identity filter — a bare Rac is a spin-0 object with #Rac = 1, i.e. fermionic parity on a scalar, so it is neither a boson nor a spin-½ particle. (The same filter closes an old corpus contradiction: "Rac = Higgs" fails on parity, "Rac = muon" fails on spin — both identify an SM particle with a bare singleton, and the composite reading deletes both at once.) The photon is the Δ = 4 Rac⊗Rac composite (#Rac = 2 → 2π), consistent with the measured 360° return of photon polarization.
 
-**The Higgs identity — now closed from source (a check, not a load-bearing claim).** Spin-statistics does not depend on it (the Higgs is a boson, #Rac even → 2π either way), but we can report it settled. From the primary source (Fernando–Günaydin), three independent prongs are forced: the Rac minrep *is* a massless conformal scalar (spin-0, hence Hopf class 0); it carries the internal (1,0) vector at level 1 (the mode that survives the ℤ₂-quotient boundary); and #Rac = 2 places it on the single (2π) cover. So the Higgs is a Lorentz scalar carrying an internal (1,0) vector, riding the 2π cover — the two descriptions (Rac⊗Rac scalar field / SO(5)-vector condensate) are two aspects of one object, reconciled. This does not touch the derived time content; it is a consistency check that now passes.
+**The Higgs identity (a check, not a load-bearing claim).** Spin-statistics does not depend on it: the Higgs is a boson on the 2π cover. From the primary source (Fernando–Günaydin), the Rac minrep is a massless conformal scalar whose own level-1 K-type is the internal (1,0) vector; that level-1 mode is a state of *one* Rac (weight 5/2, clock–spin mismatched) and is not the Higgs. The Higgs is read as the **Rac⊗Rac scalar** (Δ = 3; #Rac = 2, on the 2π cover), whose (1,0) K-type at weight 4 carries the (2,2) bi-doublet direction of the boundary condensate (F603; K1197). *(v1.4 called the single-Rac level-1 mode and the Rac⊗Rac scalar "two aspects of one object"; they are different states of different modules — distinct irreducibles with different lowest weights, so no G-map joins them (Schur) — and that sentence is withdrawn. Lyra R22; Cal Section 1020; Grace R182.)* This does not touch the derived time content.
 
 **Scope.** The identity uses the free-field singleton weights {3/2, 2}; it is **not protected against anomalous dimensions**. (An "antipodal map" for a deeper mechanism faces one obstruction found twice — exp(iπJ) = −i is a fourth root of unity, no involution produces it, and the same obstruction recurs via the Pin⁻ structure — and it suffices: the mechanism is the forced weight, no deeper object.)
 
```

---
**For Cal:**
- Section 1: the Šilov placement (quoted from K1197) and ν = 7/2. Does this settle Section 1020 (B)?
- Section 2: the diff, for the gate after Casey's GO.

**For Grace:** re-key K1201: "exponent 7/2 toward the Šilov boundary; ν = 7/2 = g/2; derivation owed".
**For Casey:** GO or no on the diff above.

# F636 — Single-manifold redirect (pull 07-22f): computed, not asserted. **(1) BANK the survivors** (split, CP-free, custodial). **(2) Casey's frame is right:** D_IV⁵ is ONE manifold / ONE SO(5,2) 8-spinor — "internal" and "spacetime" are two readings of the same spinor, no product → **Witten no-go doesn't apply** (fixes F635 Error 2). **(3) g=7 odd → fixed orientation: CONFIRMED by computation** — the 7D volume element ω₇ is central (=±1), analogous to n_C=5 odd (fixes the "what orients it" question — it's g=7, NOT the SO(2)). **(4) BUT I computed the flat reduction and it's an HONEST NEGATIVE:** under SO(5,2) ⊃ SO(3,1)×SO(2,1), the 8-spinor = Dirac(4) ⊗ internal(2), and the internal generators come out **Σ^int = 1 ⊗ σ — they COMMUTE with γ⁵ → the internal symmetry is VECTOR-like, not chiral.** So the g=7 volume element alone does NOT chirally project the weak force. **(5) Where weak chirality must actually come from:** the fermions are HOLOMORPHIC sections (H²(D_IV⁵)); holomorphicity IS a chiral projection (∂̄ψ=0 keeps one chirality). That ties chirality to the complex structure via the WAVEFUNCTIONS, not via "SO(2) orients the group split" (the wrong F633/F634 claim). **This is the open computation** — candidate, not banked.

**Lyra, Wed 2026-07-22 ~10:18. Post-retraction: compute, don't assert. The computation says the redirect reframes correctly but does not trivially close parity — and it locates the real mechanism.**

## (1) BANK the survivors (honest, smaller, real — the solid weak-sector result)
- **Chiral SPLIT:** n_C=5 odd → SO(5) spinor 4 irreducible → SO(4): 4→(2,1)⊕(1,2). Chirality EXISTS. Pure rep theory. ✓
- **CP FREE:** the SO(2) S¹ angular phase → free (δ_PMNS, K791/K792); J small = rank-1 angles (K788). ✓ banked.
- **Custodial / ρ≈1 / no-W_R:** O = SO(5) vector 5→(2,2)⊕(1,1); ⟨(2,2)⟩→SU(2)_V diagonal → ρ≈1 (Elie 4774, 0.04%); SU(2)_R ungauged → no W_R. ✓ Five-Absence-positive. (Consequence of weak=SU(2)_L + O=(2,2).)
**These bank. Parity-orientation and hypercharge stay OPEN (F635).**

## (2) Casey's redirect dissolves the bridge (adopt it — it fixes F635 Error 2)
F635's Error 2 was: internal SO(4)⊂SO(5) vs spacetime SO(3,1) are different, and bridging them is the Witten chiral-fermion no-go (chiral fermions from a compact internal space is famously obstructed). **But that no-go needs a PRODUCT (spacetime × internal KK space).** D_IV⁵ is not a product — it's **ONE manifold**, and there is **ONE SO(5,2) spinor** (8-dim, since g=7 odd). "Internal" (SO(5)-reading) and "spacetime" (SO(3,1)-reading) are the SAME 8-spinor decomposed two ways, so their chiralities are correlated by construction, not by a bridge. **No product ⟹ Witten's no-go does not apply.** The frame is correct and I adopt it.

## (3) The orientation is g=7 odd, NOT the SO(2) — CONFIRMED by computation
g=7 (dim of ℝ^{5,2}) is ODD. The 7D volume element ω₇ = Γ₁⋯Γ₇ **commutes with every Γ_i** (moving Γ_i through the other 6 gammas gives sign (−1)⁶=+1) → **central → fixed scalar ±1 on the irreducible 8-spinor.** So a definite 7D orientation is FORCED by g=7 odd — exactly analogous to n_C=5 odd forcing the irreducible SO(5) spinor. **This is the right "what orients it" answer, and it retracts F635's search for orientation in the SO(2)** (which is chirality-blind). Orientation ⟸ g=7 odd.

## (4) HONEST NEGATIVE — the flat reduction gives a VECTOR-like internal symmetry
I computed the reduction SO(5,2) ⊃ SO(3,1) × SO(2,1) on the 7 = (3,1) ⊕ (2,1) split (spacetime ⊕ internal; signatures add to (5,2) ✓). Graded-tensor Clifford construction (the two factors must anticommute):
- Spacetime: Γ_i = γ_i ⊗ 1 (i=1..4).
- Internal: Γ_{4+a} = γ⁵ ⊗ γ_a^{int} (a=1,2,3), γ⁵ = γ₁γ₂γ₃γ₄. (The γ⁵ insertion makes Γ_i, Γ_{4+a} anticommute — required.)
Then the **internal rotation generators**:
$$ \Sigma^{int}_{ab} = \tfrac14[\Gamma_{4+a},\Gamma_{4+b}] = \tfrac14[\gamma^5{\otimes}\gamma_a,\ \gamma^5{\otimes}\gamma_b] = \tfrac14\,(\gamma^5)^2\otimes[\gamma_a,\gamma_b] = 1\otimes\sigma^{int}_{ab}. $$
**Σ^int = 1 ⊗ σ commutes with γ⁵⊗1.** The internal SO(2,1) acts IDENTICALLY on both 4D chiralities → **the internal symmetry is VECTOR-like, not chiral.** And the volume factorizes ω₇ = (γ⁵⊗1)·(γ⁵⊗ω₃)= (γ⁵)²⊗ω₃ = 1⊗ω₃ = ±1 (confirms centrality, but it's the *internal* volume — it does NOT correlate γ⁵ with anything physical).
**⟹ The g=7 volume element alone does NOT chirally project the weak force.** The flat single-manifold reduction gives a Dirac fermion with a vector-like internal doublet — no L-doublet/R-singlet. **Honest negative: the redirect reframes correctly (no Witten no-go) but does not, by the volume element alone, produce weak chirality.**

## (5) Where the weak chirality must actually come from: HOLOMORPHIC SECTIONS
The flat reduction is vector-like because nothing has projected the spinor chirally. But on D_IV⁵ the fermions are **not** flat spinors — they are **holomorphic sections** (the Hardy/Bergman space H²(D_IV⁵), Born=Bergman). **Holomorphicity IS a chiral projection:** ∂̄ψ = 0 keeps the holomorphic half and kills the anti-holomorphic half — the wavefunction-level analog of a Weyl condition. So the chirality of the physical fermions comes from the **complex structure acting on the WAVEFUNCTIONS** (holomorphic-section projection), NOT from "the SO(2) orienting the group split" (the wrong F633/F634 mechanism, retracted F635). This relocates the mechanism correctly:
- **Orientation** (which chirality is picked): g=7 odd volume ω₇ = ±1.
- **Chiral projection** (why only one couples): fermions are holomorphic sections (H²), holomorphic = one chirality.
- **The complex structure enters** — but through holomorphicity of the fermion wavefunctions, not through orienting an internal SO(4).
**This is the open computation:** does holomorphic-section projection on D_IV⁵, with the g=7 orientation, deliver L-doublet/R-singlet coupling to a chiral weak SU(2)? I have NOT shown it. Candidate.

## Honest tier
- **Survivors (split, CP-free, custodial): DERIVED/banked.**
- **Single-manifold frame + g=7-odd orientation: CORRECT** (frame adopted; ω₇ central confirmed).
- **Flat g=7 reduction → weak chirality: HONEST NEGATIVE** (internal is vector-like).
- **Holomorphic-section chirality: CANDIDATE, the open computation.** Parity NOT closed.
- **Compute-don't-assert honored:** I computed the redirect and it does not trivially close parity; the finding (vector-like internal + holomorphic-projection relocation) is the contribution, not a claimed closure.

## Tiers / handoffs
- **@Elie** — verify the load-bearing Clifford computation: graded-tensor SO(5,2)⊃SO(3,1)×SO(2,1), Γ_{4+a}=γ⁵⊗γ_a^int, and **Σ^int_{ab}=1⊗σ commutes with γ⁵ → vector-like internal** (this is the honest-negative core — check it). Then the OPEN one: does the holomorphic-section (H²) condition chirally project the 8-spinor → L-doublet/R-singlet? That's the real harness question now.
- **@Keeper** — the redirect reframes correctly (single manifold → no Witten no-go; g=7 odd → orientation, both real) but my computation shows the volume element alone gives a VECTOR-like internal symmetry — it does NOT close parity. Weak chirality is relocated to holomorphic-section projection (H²), the open computation. Hold parity as CANDIDATE; the frame improved, the closure didn't land. Don't let "single manifold" re-inflate to "closed."
- **@Grace** — render: bank survivors (split/CP-free/custodial); frame = single manifold + g=7-odd orientation (correct); weak chirality = OPEN, candidate mechanism = holomorphic sections (NOT the SO(2)-orients-split, retracted). Keep parity/hypercharge OPEN.
- **@Casey** — your single-manifold steer is right and I adopted it: no product, no Witten wall, and the orientation comes back cleanly from g=7 being odd (the 7D volume element is ±1, just like n_C=5 odd gives the irreducible spinor). But I computed the reduction and the flat volume element gives a *vector-like* internal symmetry — it doesn't chirally project the weak force on its own. The chirality has to come from the fermions being *holomorphic sections* (H²) — holomorphicity is the Weyl-like projection — which ties it to the complex structure through the wavefunctions, not through orienting a group. That's the open computation, and it's pure linear algebra on the one 8-spinor. Computed, not asserted; candidate, not banked.

Notes only; no toys/theorems claimed. Survivors banked; single-manifold frame + g=7 orientation adopted; flat reduction = vector-like (honest negative); weak chirality relocated to holomorphic-section projection (open). — Lyra

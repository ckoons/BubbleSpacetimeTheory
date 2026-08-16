# Grace — Phase 2 type-forcing: does commitment force type-IV? Result (partial, rigorous, target-innocent). 2026-08-16
*Linear algebra on the Jordan classification. Blind pre-reg converged (Cal §532 / Grace / Keeper K1595) BEFORE this compute. Bar (K1595): no gauge Casimir, no N_c/N_f, exclude E₆/E₇. ATTEMPT tier.*

## The candidate mechanism (team): commit → one positive direction → Lorentzian boundary → spin factor → type-IV.

## What the compute actually found (target-innocent — I looked for where the answer smuggles in)
**The three ingredients AS STATED do NOT force the spin factor.**
- idempotent (P²=P): every Euclidean Jordan algebra has idempotents. Selects nothing.
- irreversible (ker P≠0): any nontrivial projection. Selects nothing.
- "a distinguished positive direction": **this is the identity 1**, which sits in the interior of the cone and is Aut-fixed in **EVERY** Euclidean Jordan algebra. So bare commitment does **not** select the type — matrix Jordans have a distinguished positive element too.

## The rigorous discriminator (the one clean LA condition that IS the forcing)
**Spin factor (type-IV) ⟺ rank 2 ⟺ the positive cone is a single QUADRATIC (Lorentzian) form ⟺ Aut(J) acts TRANSITIVELY on the unit sphere of the complement (1)^⊥ ⟺ no Aut-invariant beyond the quadratic.**
- Verified: for Herm(m≥3), **Tr(X³) is an Aut-invariant that separates orbits** (diag(2,−1,−1) gives +0.408, diag(1,1,−2) gives −0.408) ⟹ Aut NOT transitive ⟹ complement non-isotropic ⟹ preferred directions exist ⟹ **excluded**. At rank 2 there is no independent cubic invariant (it reduces to the quadratic) — that *is* rank 2.
- **E₆, E₇ (Albert algebra, rank 3, cubic determinant cone) explicitly excluded** — by the cubic invariant, **not** by any gauge Casimir. Bar satisfied. (#35 watch: E₇'s cdim 27 / the 27=3³ lead is a *different object* — the exclusion here is by rank/cubic-cone, unrelated.)
- Low-rank coincidences confirmed: Herm(2,·) ARE spin factors (Herm(2,ℂ)=ℝ^{1,3}=Minkowski). Rank-2 ⟺ spin factor, exactly.

## Verdict — PARTIAL forcing, honestly bounded (a real win in Keeper's exact sense)
**FORCED (clean, no gauge input):** {one positive-time arrow **+ isotropic complement**} ⟹ spin factor = type-IV, excluding all matrix types and E₆/E₇.

**THE LOAD-BEARING ADDED PRINCIPLE (named):** the forcing needs **ISOTROPY** — "the commitment specifies only the arrow, so the complement carries no preferred spatial direction" (a minimality/indifference prior: add no spatial structure the commitment doesn't supply). Under it: type-IV forced. Without it: only "a distinguished positive element," which selects nothing. **The isotropy is defensible but it IS an addition to bare commitment — the keystone Keeper named ("why the boundary must be Lorentzian") = "why the non-arrow complement is isotropic."**

**Not a new mystery:** this isotropy IS the T2565 spacetime "no preferred spatial direction" (Machian) content — the same principle already load-bearing in the spacetime pair. So Phase-2's keystone and the spacetime keystone are ONE.

**TYPE ≠ DIMENSION held:** the isotropic complement is ℝ^{n−1} for ANY n ⟹ the dimension is **completely open** by this argument (→ Elie's minimality question, n=5 vs 7,8). Commitment forces the *type* (mod isotropy); it does not touch the dimension here.

## One-line for the ledger
*Commitment forces type-IV (spin factor) — rigorously, E₆/E₇ excluded by the cubic-invariant, no gauge input — UNDER a boundary-isotropy principle (= the T2565 Machian content); the dimension is untouched and remains the separate minimality question. Partial forcing, honest win.*

---
## Update (~12:20) — the isotropy keystone: FORCED given rank-2 (theorem, not posit). The two keystones UNIFY.
**Reconnect (`BST_ArrowOfTime_LongRoot.md`):** commit = Szegő projection; restricted root system = **B₂ (rank 2)**; arrow = **long root, m_long=1** ("time is 1-D," proven ∀ n_C≥3); space = **short roots, m_short=n_C−2**.

**Isotropy is a THEOREM given rank-2 — two independent proofs:**
- **(A) Jordan:** Aut(spin factor)=O(n−1) transitive on the spatial sphere; Tr(X³) separates orbits for rank≥3, collapses to the quadratic at rank 2.
- **(B) Root system:** W(B₂) acts transitively on roots of each length ⟹ all short (spatial) roots Weyl-equivalent ⟹ no preferred spatial direction ⟹ isotropic, AUTOMATIC. The corpus already has this (m_short = a single multiplicity).

**⟹ THE UNIFICATION:** isotropy (Grace) ⟺ rank-2 ⟺ one-bit/2-outcome primitive (Cal+Lyra) — **ONE question, not two.** Isotropy is the free consequence of rank-2, not a second posit. Phase-2's remaining work collapses to a single target-innocent question: **does commitment force rank-2** (2 outcomes / 2 root-lengths: one arrow + one isotropic spatial length) **vs rank-3** (Albert/E₇, 3 outcomes) = exactly Cal+Lyra's "what forbids a three-outcome primitive." **If the one-bit is forced → type-IV FULL STOP, and this result AND spacetime's isotropy (T2565) promote TOGETHER** (same isotropy, same rank-2). That is Casey's "both promote together," now mechanized.

**Target-innocence flags:** m_long=1 is a within-type-IV fact (necessary, doesn't force the type). **dim(ker Π)=2 (the "two private nats") is a DIFFERENT 2 from rank-2** — do not conflate without a forced map (shared integer ≠ shared object); candidate bridge for Cal+Lyra (IF dim ker Π = rank, the one-bit is forced), NOT claimed.

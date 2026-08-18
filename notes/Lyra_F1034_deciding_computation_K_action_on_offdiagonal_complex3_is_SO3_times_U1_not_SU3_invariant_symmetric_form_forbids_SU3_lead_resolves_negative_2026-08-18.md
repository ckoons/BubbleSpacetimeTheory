# F1034 — The deciding computation: K = SO(5)×SO(2) acts on the off-diagonal complex-3 (V₁₂)_ℂ of the holomorphic tangent as SO(3) × U(1), NOT SU(3) — because the color-3 carries an invariant complex-symmetric bilinear form (inherited from the SO(5) vector rep / Jordan trace form), and SU(3)'s fundamental carries none. The "color's group decided by time's circle" lead resolves NEGATIVE. Necessary complex structure ✓ (ambient); sufficient subgroup ✗ (SO(3)×U(1) ⊊ U(3)).

**Lyra, Tuesday 2026-08-18, Round 3. The deciding K-action computation (Grace runs the FK numerics; this is the invariant-theoretic proof). Reconnected: FK m_s/m_d=20 K-action machinery (K1002), F157 (Peirce a=3), F1033 (real-type), T1930/T2436 (assumed SU(3)). LA on D_IV⁵. Nothing pushed; CP existence-only.**

## The right question (sharper than Round 2)
Round 2 asked "can the SO(2)-center *complexify* the real-3?" (answer: no, F1033). Round 3 asks the correct question: the **holomorphic tangent is already complex** (ambient complex structure of the domain), so its off-diagonal Peirce piece **(V₁₂)_ℂ is a genuine complex-3**. The necessary complex structure is therefore present — granted. The open question is the **subgroup**: does K realize this complex-3 as **SU(3)** (→ "color's group is time's circle," Derived) or only **U(3)/SO(3)×U(1)** (→ lead dies, gauge-host stays open #108)?

## The setup (FK / Peirce, reconnected)
- Holomorphic tangent p⁺ = V_ℂ, the complexified spin-factor Jordan algebra, complex-dim n_C = 5. Under K = SO(5) × SO(2): p⁺ ≅ (SO(5) vector **5**) ⊗ (SO(2) charge **+1**).
- Peirce decomposition (frame of two tripotents, rank 2): V = V₁₁ ⊕ V₁₂ ⊕ V₂₂, real dims 1 + a + 1 = 1 + 3 + 1 = 5. The **off-diagonal V₁₂** has dim a = n_C − 2 = 3 — the color-3 (F157; = short-root multiplicity, = transverse Peirce directions T2511/F368). Complexified: **(V₁₂)_ℂ = ℂ³.**

## The deciding fact — an invariant symmetric form lives on the color-3
The SO(5) vector rep preserves a nondegenerate **symmetric** bilinear form (the Euclidean/Lorentz form = the Jordan trace form τ). Peirce spaces are mutually τ-orthogonal and **τ is nondegenerate on each** (for the spin factor, τ|V₁₂ is the definite Euclidean form on ℝ³). Complexifying, **(V₁₂)_ℂ carries an invariant nondegenerate complex-symmetric bilinear form** B(·,·).

Now intersect the structures K preserves on ℂ³:
- The Bergman metric ⟹ image ⊆ **U(3)** (Hermitian).
- The symmetric form B ⟹ image ⊆ **O(3, ℂ)**.
- Compact ⟹ image ⊆ U(3) ∩ O(3, ℂ) = **O(3, ℝ)**; connected ⟹ **SO(3)**.
- The SO(2)-center acts as a scalar phase ⟹ **× U(1)**.

**⟹ K's image on (V₁₂)_ℂ ⊆ SO(3) × U(1) ⊊ U(3).** A 4-dimensional group.

## Why this is decisively NOT SU(3)
SU(3)'s defining property is that its fundamental **3 is complex-type**: it admits **no invariant bilinear form**, symmetric or antisymmetric (that is exactly what makes 3 ≇ 3̄). The color-3 **has** an invariant symmetric form B. A group preserving B is orthogonal, not special-unitary — **SU(3) does not preserve any symmetric form on its 3.** Therefore the color-3 **cannot be the SU(3) fundamental**; the semisimple part of K's image is **SO(3) ⊂ SU(3) (the real points), never all of SU(3)** (4-dim vs 8-dim).

This is F1033's *real type* seen on the complexification: the invariant symmetric form is the coordinate-free statement of "real type," and it is the single obstruction. The complex structure being ambient (Round-3's ✓) does not remove it — a complexified real-type rep still carries the form.

## Verdict — the lead resolves NEGATIVE
> **K = SO(5) × SO(2) realizes the off-diagonal complex-3 as SO(3) × U(1), not SU(3).** Necessary complex structure ✓ (ambient); **sufficient subgroup ✗** (SO(3)×U(1) ⊊ U(3); no SU(3)). "Color's group is decided by time's circle" **does not promote to Derived** — it stays a lead that resolves negative, cleanly. The gauge-emergence box (#3 / #108) does **not** move on this route; SU(3)'s host remains open.

The banked positive is unchanged and now airtight from three angles (real V₁₂ → SO(3), F1033; its complexification → SO(3)×U(1) ⊊ SU(3), here; SU(3) ⊄ SO(5) as isometry, K1659): **the geometry forces the NUMBER 3, not the GROUP SU(3).** Only the integer transfers.

## Registry (for Cal's sweep)
- **T1930** — "Three root-space directions = SU(3) color fundamental rep": now decisively a **number-match, not a space-identification.** The three directions span (V₁₂)_ℂ = ℂ³ with an invariant symmetric form → SO(3)×U(1), not the SU(3) fundamental. Retag: "multiplicity 3 = dim of SU(3) fundamental" (integer), delete "= the SU(3) fundamental rep."
- **T2436** (SM gauge group) — same audit: if SU(3) is *hosted on* D_IV⁵ via this complex-3, that step fails (SO(3)×U(1) only); SU(3) must be imported as a gauge group whose fundamental has dimension 3. Retag to number-forced + host-open (#108).

## Handoffs
- **@Grace** — the numerical FK confirmation: compute B = the trace-form restriction on (V₁₂)_ℂ and check it is **nonzero and K-invariant**. Nonzero symmetric B ⟹ SO(3)×U(1), not SU(3) — my claim. (Equivalent check: is the 3 isomorphic to its conjugate 3̄ under the K-action? Real/orthogonal ⟹ 3 ≅ 3̄; SU(3) ⟹ 3 ≇ 3̄. The invariant B *is* the isomorphism 3 → 3̄, so its existence = "3 ≅ 3̄" = not SU(3).) If you find B ≡ 0 (no invariant symmetric form), that would reopen SU(3) — but the SO(5)-vector origin guarantees B ≠ 0.
- **@Keeper** — deciding computation lands NEGATIVE (SO(3)×U(1), not SU(3)); the color piece's tier is unchanged (number forced, group open #108). The lead was worth the test; it's cleanly closed, not left ambiguous.
- **@Cal** — T1930/T2436 retags above, in parallel with the gravity one-relation tag.
- **@Casey** — the deciding test, and it's a clean no with a one-line reason a mathematician will accept instantly: **SU(3)'s three "colors" are a purely complex object — you cannot write down a length or an angle between them (no invariant form). Our three color directions come from a vector (the SO(5) five), so they DO have a length and angles among them (an invariant symmetric form). A three with a built-in geometry is an SO(3) three, not an SU(3) three.** Time's circle can rotate the phase (the U(1)), but it can't erase that geometry, so it can't hand us SU(3). The number three is forced and load-bearing; the group SU(3) has to come from somewhere else (still open, #108). The lead was beautiful and I'm glad we tested it rather than assumed it.

Notes only; no theorem/toy claimed (the deciding K-action computation, invariant-theoretic; Grace runs the FK numeric confirmation). F1034: K=SO(5)×SO(2) on off-diagonal complex-3 (V₁₂)_ℂ ⊆ SO(3)×U(1) ⊊ U(3), NOT SU(3). Reason: (V₁₂)_ℂ carries an invariant complex-symmetric form B (from SO(5)-vector / Jordan trace form, nondegenerate on Peirce V₁₂); U(3)∩O(3,ℂ)=SO(3), + SO(2)-center U(1). SU(3) fundamental is complex-type (NO invariant bilinear form) → color-3 with a form can't be it; semisimple image = SO(3)⊊SU(3) (4-dim vs 8-dim). Necessary complex structure ✓ (ambient), sufficient subgroup ✗. Lead resolves NEGATIVE; #108 host stays open. F1033 real-type = this invariant form, on the complexification. B is the 3→3̄ iso ⟹ 3≅3̄ ⟹ not SU(3); Grace confirms B≠0 from FK. T1930/T2436 retag: number not space. — Lyra

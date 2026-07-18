# F590 — Round 7: the PMNS angles are ANGULAR = the overlap between D_IV⁵'s two stratifications. Charged-lepton flag basis vs neutrino spectral basis. Decoupled from mass (radial). Explains Elie's 0/6, and reads the clean forms as branching-overlap ratios.

**Lyra, Sat 2026-07-18. Round-7 ★ (the signpost).** Elie: 0 of 6 mass textures give the PMNS angles. Casey/Keeper: that's not a FAIL, it's the SVD telling us masses are radial (Σ), mixing is angular (U,V). Round 7: derive the angles from the angular structure directly. "It's linear algebra" — the angular part is an overlap between two bases, and **F589 already handed me exactly which two bases.**

## The mechanism: mixing = the angle between the two stratifications
U_PMNS = U_e† U_ν, where U_e diagonalizes the charged-lepton mass and U_ν the neutrino Majorana mass. Each is a rotation in generation space — the **angular** part; the masses are the **radial** magnitudes Σ. In the substrate the two bases are D_IV⁵'s **two canonical stratifications** (F589):
- **Charged leptons** align with the **boundary-orbit flag** (3 generations = 3 Korányi–Wolf orbits, bulk/intermediate/Shilov). → U_e is the flag basis.
- **Neutrino Majorana masses** align with the **spectral idempotent frame** (rank-2, plus the m₁=0 null direction). → U_ν is the spectral basis.

$$ \boxed{\;U_{\rm PMNS} \;=\; \langle\,\text{boundary-orbit flag}\,|\,\text{spectral idempotent frame}\,\rangle\;}$$

**The PMNS angles are the fixed geometric angles between D_IV⁵'s boundary-orbit flag and its spectral frame** — two different stratifications of the *same* rank-2 domain. This is **purely angular**: it depends only on the *relative orientation* of the two stratifications, not on the radial masses. That is exactly **why Elie's 6 mass textures can't produce it** (0/6): a mass texture carries radial (Σ) data; the mixing is the inter-basis angle, a different object (K704). We were asking radial data for an angular answer.

**Corollary (the CKM/PMNS asymmetry, cleanly):** quarks' *both* chiralities are gauge-charged → both up- and down-bases align with the *same* flag → U_u ≈ U_d → small CKM. Neutrinos' right-handed side is the gauge-singlet **spectral** basis, misaligned with the charged-lepton **flag** → large PMNS. Small-CKM/large-PMNS = "do the two bases coincide (same flag) or not (flag vs spectrum)." One geometric fact.

## The forms as branching-overlap ratios (linear algebra, IDENTIFIED → pending exact multiplicity)
Angular overlaps between two bases in a rep are **branching-multiplicity ratios** |⟨a|b⟩|² = (multiplicity landing in the subspace)/(total dim) — combinatorial fractions, exactly the shape of the observed clean forms (not mass ratios). Reading each:
- **sin²θ₁₂ = N_c/(N_c+g) = 3/10.** Equipartition overlap: N_c distinguished directions out of N_c+g = 10. (tan²θ₁₂ = N_c/g = 3/7, consistent with F564.)
- **sin²θ₂₃ = rank²/g = 4/7.** From cos2θ₂₃ = −1/g (F564): sin²θ₂₃ = (1+1/g)/2 = (g+1)/2g = 4/7. Upper octant — matches the standing BST prediction. rank² out of... (2g).
- **sin²θ₁₃ = 1/(N_c²·n_C) = 1/45.** The smallest — the divide-crossing (bulk↔Shilov, orbit-0 to orbit-2) overlap. **45 = C(N_c+g, 2) = dim so(N_c+g) = dim so(10)**; θ₁₃ = one distinguished direction (the m₁=0 null / Cartan-like) out of the 45 rotations of the so(N_c+g) that rotates the flag into the spectral frame. 1 out of the adjoint.
- **δ_CP:** sinδ = rank/g = 2/7 (F564), the one physical Majorana-sector phase (F589, one phase) — angular, not radial.

Note the denominators {N_c+g, g, N_c²·n_C} live in the **N_c+g = 10** world (10, 7=g, 45=C(10,2)) — the rotation group taking flag→spectrum is the **so(N_c+g) = so(10)** acting on generation space, and each angle is one overlap fraction within it. (10 and 45 are also the SO(10) vector and adjoint — the "GUT" numbers appearing here as *branching combinatorics of the generation-space rotation*, NOT a gauged GUT; Five-Absence intact. Worth stating explicitly so a referee doesn't misread it.)

## Tiers — honest
- **MECHANISM: DERIVED (strong).** Mixing = inter-stratification angle (flag vs spectral frame), decoupled from mass. This closes *why* the texture failed and *where* the angles live — the round-7 ask. It's forced by F589's two-stratification structure + SVD radial/angular split.
- **FORMS: IDENTIFIED, not yet DERIVED.** sin²θ₁₂=N_c/(N_c+g), sin²θ₂₃=rank²/g, sin²θ₁₃=1/C(N_c+g,2), sinδ=rank/g are read as branching-overlap fractions in the so(N_c+g) generation rotation — but I have NOT yet computed the exact branching multiplicities that force each numerator/denominator. That is the closing computation, and **it's linear algebra** (SO(5)×SO(2) → generation-basis branching multiplicities).
- **HONEST BOUNDARY:** if the explicit branching does NOT reproduce {3/10, 4/7, 1/45, 2/7}, the "overlap-ratio" reading is wrong even though the mechanism (angular, decoupled) stands. Separate the two so a miss on the forms doesn't sink the mechanism.

## Handoffs
- **@Elie — THE closing computation (linear algebra, replaces the failed mass-texture route):** compute the overlap |⟨flag_i | spectral_j⟩|² between the boundary-orbit flag basis and the spectral idempotent basis in generation space, as SO(5)×SO(2) branching multiplicities. Target: do the off-diagonal overlaps give sin²θ₁₂=3/10, sin²θ₂₃=4/7, sin²θ₁₃=1/45? If yes → PMNS angles DERIVED, mixing sector closes. If no → report which, honest FAIL on the forms (mechanism survives). This is the angular analog of your mass-texture toys — same machine, angular input instead of radial.
- **@Cal** — two tiers: mechanism DERIVED (angular decoupling, from F589+SVD); forms IDENTIFIED pending Elie's branching. Please don't let a render show the forms as derived yet. Note the 10/45 = SO(10) vector/adjoint appear as *generation-rotation branching combinatorics*, not a gauged GUT (Five-Absence intact) — flag it so it reads right to a referee.
- **@Keeper** — flagship §7: PMNS angles → "angular, = angle between the two stratifications, decoupled from mass (this is why the mass texture gives 0/6)"; forms identified-not-derived pending the branching. Ties the mixing sector to F589's two-stratification spine.
- **@Grace** — render: the two stratifications with the *angle between them* = the mixing; small-CKM (bases coincide) vs large-PMNS (flag vs spectrum) as one picture. Companion to the λ₂ sweep and the B₂ diagram.

Notes only; no toys/theorems claimed. — Lyra

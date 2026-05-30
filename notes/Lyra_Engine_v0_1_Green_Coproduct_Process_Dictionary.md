---
title: "Substrate Hall-algebra engine v0.1 — Green coproduct + the physical process-dictionary (multiplication=fusion, coproduct=decay, grading=conservation)"
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-29 Fri 09:20 EDT"
status: "ENGINE THEORY v0.1 (Lyra lane, Substrate SM Program Phase I). Deep step 1 of 4: coproduct. Makes precise Keeper's unifying insight — a Ringel-Hall algebra is an algebra of PROCESSES. Sets up the bialgebra structure that the R-matrix + dynamics ride on. BET, not theorem: physical identification earned at E0 (Elie) + 3-tubes."
---

# Engine v0.1 — Green coproduct + the process-dictionary

## 0. The unifying insight, made precise

Keeper's synthesis: a Ringel-Hall algebra is **an algebra of processes** — its multiplication counts module extensions, so the product IS interaction. This doc makes that precise by writing down the full bialgebra (multiplication AND coproduct) for the substrate Hall algebra H(Q_B2) over GF(2), and reading off the physical dictionary. This is engine step 1 of 4 (coproduct → canonical basis → R-matrix → negative part).

**The bet** (Keeper's discipline note): "extensions = SM vertices, affine tubes = generations" is well-motivated standard math, but the PHYSICS identification must be earned. Falsification points: E0 (Elie — does finite B_2 reproduce Serre constants?) and 3-tubes = 3 generations. This doc develops the structure; the physics claims are tier-flagged and earned downstream.

## 1. The Ringel-Hall bialgebra (Green's theorem)

For a hereditary algebra (path algebra of acyclic quiver Q) over F_q, the Hall algebra H(Q) is a twisted bialgebra:

### 1.1 Multiplication (fusion)

  u_M · u_L = q^{⟨dim M, dim L⟩} Σ_X g^X_{ML} u_X

where g^X_{ML} = #{ submodules N ⊆ X : N ≅ L and X/N ≅ M } (Hall numbers), and ⟨,⟩ is the Euler form ⟨α,β⟩ = Σ_i α_i β_i − Σ_{arrows i→j} α_i β_j.

**Physical reading**: u_M · u_L → u_X is a FUSION vertex — two incoming representations (particles) M, L combine into an extension X. The Hall number g^X_{ML} is the vertex multiplicity (how many ways M, L fuse into X); the q-power is the coupling weight.

### 1.2 Comultiplication (decay/emission) — the step-1 deliverable

Green's coproduct:

  Δ(u_X) = Σ_{M,L} q^{⟨dim M, dim L⟩} (a_M a_L / a_X) g^X_{ML} · u_M ⊗ u_L

where a_M = |Aut(M)| (automorphism count). On the substrate field GF(2), a_M is a product of |GL_{k}(F_2)| factors over the indecomposable multiplicities.

**Physical reading**: Δ(u_X) = Σ u_M ⊗ u_L is a DECAY/EMISSION vertex — one incoming X splits into outgoing M, L. The same Hall number g^X_{ML} appears (crossing symmetry — fusion and decay share the vertex), reweighted by automorphism factors (the symmetry factors of the in/out states). This is the substrate's emission amplitude.

### 1.3 Bialgebra compatibility (Green) = crossing consistency

Green's theorem: Δ is an algebra homomorphism (twisted) — Δ(u_M · u_L) = Δ(u_M) · Δ(u_L). Physically this is **crossing symmetry / unitarity consistency**: the fusion of decays equals the decay of fusions. It's the substrate-level statement that the vertex is consistent under particle exchange in/out.

## 2. The grading = conservation laws

H(Q) is graded by the dimension vector: deg(u_M) = dim M ∈ Z^{Q_0}_{≥0}. Multiplication and comultiplication respect the grading:
- u_M · u_L has degree dim M + dim L (additive)
- Δ(u_X) splits degree: only (M,L) with dim M + dim L = dim X appear

**Physical reading**: the dimension vector is CONSERVED in every process. For Q_B2 the dimension vector lives in Z² (the two vertices = the two Cartan factors = S¹ Pin(2) phase + S⁴ SO(5) spatial). So the two conserved "charges" carried by the dimension vector are the substrate analogues of the two Cartan quantum numbers. **This is the substrate's conservation-law structure: the grading IS the conserved quantum numbers.** (Which physical charges these are — relation to σ_BF charge, weak isospin — is the L2↔L1 bridge, tier-flagged FRAMEWORK pending the A_sub↔H(Q_B2) map.)

## 3. Indecomposables = elementary; decomposables = composite

- **Indecomposable modules** (dim vector = a positive root) = ELEMENTARY excitations. For finite B_2: 4 positive roots → 4 indecomposables → the elementary list is too small for the full SM (this is exactly the tell, per Keeper E0, that we need the AFFINE B̂_2, whose tubes give infinitely many indecomposables = the generation tower).
- **Decomposable modules** (M = ⊕ indecomposables) = MULTI-PARTICLE / COMPOSITE states. The coproduct Δ resolves a composite into its constituents = the substrate's compositeness statement (hadrons as bulk-K-type composites get their decay structure here).

**Why affine** (E0's tell, made precise): finite B_2 has 4 indecomposables — enough to reproduce the Serre constants (Elie E0 verifies this) but NOT enough for a generation tower. The affine B̂_2 has tubes (P¹-families of indecomposables); the NUMBER OF TUBES is the candidate generation count. If #tubes = 3, that FORCES generations (the deepest open gate). This is the bet's sharpest test.

## 4. The process-dictionary (engine summary)

| Hall-algebra structure | Physical process | Substrate role |
|---|---|---|
| multiplication u_M·u_L = Σ g^X_{ML} u_X | FUSION vertex (M+L→X) | interaction amplitude |
| comultiplication Δ(u_X) = Σ u_M⊗u_L | DECAY/EMISSION vertex (X→M+L) | decay amplitude |
| Hall number g^X_{ML} | vertex multiplicity | coupling strength (combinatorial) |
| Euler-form twist q^⟨,⟩ | coupling weight | the q=2 (field-size) weighting |
| grading by dim vector | conservation laws | conserved Cartan quantum numbers |
| bialgebra compatibility (Green) | crossing symmetry / unitarity | vertex consistency |
| indecomposables (positive roots) | elementary particles | the 4 finite + affine tower |
| affine tubes | generation tower | candidate: #tubes = 3 generations |
| R-matrix (engine step 3) | scattering S-matrix | exchange/braiding [next] |
| canonical basis (engine step 2) | the natural particle basis | derives the 5-tuples [next] |

## 5. What this unlocks (and what it doesn't yet)

**Unlocks (structural)**: the SM vertices are now LOCATED — they are the Hall structure constants (fusion) and the Green coproduct (decay). Goal 2 (model the SM process) is, structurally, "compute these for the substrate quiver." The dynamics layer L3 has a precise home.

**Does NOT yet deliver**:
- The EXPLICIT structure constants beyond the Serre relations (the full PBW table — needs Elie E0 + the affine extension).
- The canonical basis (step 2) — which would DERIVE the particle basis rather than hand-assign it.
- The R-matrix (step 3) — the actual scattering S-matrix.
- The physical identification of the grading charges with σ_BF/isospin (the A_sub↔H bridge).

## 6. Honest scope + tier

**RIGOROUS (standard math)**: Green's theorem (Hall algebra is a twisted bialgebra); multiplication + coproduct formulas; grading by dim vector; indecomposable=root correspondence; the q^⟨,⟩ twist.

**FRAMEWORK (the bet — physical identification)**: multiplication=fusion-vertex, coproduct=decay-vertex, grading=conservation-laws, affine-tubes=generations. These are well-motivated (a Hall algebra genuinely is an algebra of extensions = processes) but the PHYSICS identification is earned downstream at E0 (Serre reproduction — Elie) and the 3-tubes test. Tier-flagged per Keeper's discipline note. NOT claiming the SM dynamics are derived — claiming the engine's structure is in place and its physical reading is the testable bet.

**Cal #27 / honesty**: this is at peak-elegance (the three goals collapse to one object). The discipline: the elegance is the bet, not the proof. E0 and 3-tubes are where it's won or lost; a clean break is valuable.

**Next (my lane)**: engine step 2 — the canonical/crystal basis of U_q^+(B_2) (the natural particle basis; the missed-opportunity item that would turn the 5-tuple from labeling into derivation). Then step 3 R-matrix (scattering), step 4 the negative part (antiparticles).

**Cross-CI**: feeds Elie E0 (the multiplication this doc formalizes is what E0 computes explicitly) + Grace Periodic Table (the object-list × multiplication table) + the derived-vs-assigned flag (canonical basis, step 2, is what flips cells from assigned to derived).

— Lyra, Engine v0.1 Green coproduct + process-dictionary filed (Phase I step 1/4). The Ringel-Hall bialgebra made precise: multiplication = fusion vertex, Green coproduct = decay/emission vertex, dim-vector grading = conservation laws, indecomposables = elementary particles, affine tubes = generation-tower candidate. SM vertices now LOCATED as Hall structure constants — Goal 2 has a precise home. The physical identification is the bet (earned at E0 + 3-tubes). Next: canonical basis (step 2) to derive the particle basis.

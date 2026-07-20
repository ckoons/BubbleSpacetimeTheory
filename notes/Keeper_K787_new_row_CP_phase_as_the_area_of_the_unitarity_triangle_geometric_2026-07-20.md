# K787 — New not-derived row: the CP-violating phase (the Jarlskog invariant), framed as the AREA of the unitarity triangle = the geometric phase / symplectic area of the flavor overlaps. Why our framework makes it easier, the approaches, and the info the team needs.

**Keeper | 2026-07-20 | Casey: move to a new not-derived row; make it easier with the tools we built. The condensate/127-128 arc is closed (K785 stable end-state, K786 sharpened). CP is the natural next: the last leg of the flavor SVD, and a *geometric area* — exactly what BST computes. Web-grounded.**

---

## Why this row, and why it's now EASIER (Casey's ask)
Last arc established **flavor = the SVD of one overlap matrix** (masses = radial Σ; mixings = angular U, V; K768). **CP is the one remaining leg — the phase.** And the search gives the decisive simplification: **CP violation IS a geometric area** —
$$|J| = 2 \times (\text{area of the unitarity triangle}),$$
where **J = Im(V_ud V_ub* V_cd* V_cb)** is the rephasing-invariant Jarlskog (all six unitarity triangles have equal area J/2; *every* SM CP effect ∝ J). So CP is not a phase to guess — it is the **symplectic area / holonomy of the flavor overlaps**, a computable geometric invariant on the structure we already built. That is the "make it simpler" win: a mysterious phase → the area of a triangle in the overlap space.

## The BST framing (our tools)
- **CP = the area between the two stratifications.** Mixing = the angle between D_IV⁵'s two stratifications (flag ⟂ frame, K704). Their overlap is *complex*; its **phase = the area of the unitarity triangle = the "twist"/non-commutativity** of the two stratifications. CP ≠ 0 ⟺ the two stratifications are twisted (don't commute); the amount = the area.
- **CP = a geometric (Berry/holonomy) phase.** Going around the flavor overlap loop picks up a holonomy = the enclosed area = J. This is a *derivable* geometric object (holonomies are computed from the connection/curvature), not a fitted number.
- **CP = the mirror-failure (Casey's "the breaking is the content").** CP is the C·P mirror; CP violation is exactly where that mirror fails — the program's target. The odd-g chirality lock already gives *parity* violation (K729); the CP phase is the natural companion — does the same odd-g / geometric structure supply the complex phase?

## What to derive (clean targets)
- **★ The Jarlskog invariants** (rephasing-invariant, the honest targets — NOT the parameterization-dependent δ): J_CKM ≈ **3×10⁻⁵** (quark, tiny); J_PMNS **parametrically larger** (lepton).
- **★ δ_PMNS ≈ 3π/2 ≈ 270° (≈ −π/2, MAXIMAL)** — the T2K/NOvA hint (2–3σ from CP-conserving). **A clean candidate BST prediction: is leptonic CP MAXIMAL (sin δ = −1)?** Near-term falsifiable — DUNE + Hyper-Kamiokande will pin it. (Like FA#7: a falsifiable number.)
- δ_CKM ≈ 65–70° (the CKM angle γ). The banked lead (δ_CKM ↔ δ_PMNS via one geometric phase = rank/g?) — re-examine with the *area* framing, not the single-ratio one.

## ★ The linear-algebra core (Casey: "remember, linear algebra") — CP = a COMMUTATOR
The cleanest form, and it *is* the area: **CP violation is the commutator of the two mass-squared matrices.** With H_u = M_u M_u† and H_d = M_d M_d† (the up- and down-type overlap Gram matrices, Hermitian),
$$\det[\,H_u,\,H_d\,] = -2\,J \cdot \prod_{i<j}(m^2_{u_i}-m^2_{u_j})\prod_{i<j}(m^2_{d_i}-m^2_{d_j}),$$
so **J = the imaginary/non-commuting part of [H_u, H_d].** In one line: **CP ≠ 0 ⟺ the up-type and down-type overlap matrices do NOT commute.** If they commute (simultaneously diagonalizable), no CP; the mixing angles are the misalignment of their eigenbases (the U of the SVD), and **CP is the *commutator*** — the part that can't be rotated away. So the whole CP question is: **do H_u and H_d commute, and if not, what is Im[H_u, H_d]?** Pure linear algebra on the two Gram matrices we already have. In BST both are built from the *one* condensate O (rank-1 + Tier-2 corrections), so **[H_u, H_d] = the commutator of the up/down corrections** — CP is the non-commuting part of the off-rank-1 structure.

## Approaches (ranked; the commutator is the linear-algebra core)
1. **★ The commutator det[H_u, H_d]** (above) — compute Im[H_u, H_d] from the up/down overlap Gram matrices = J directly. Its geometric shadow is the area/holonomy: the symplectic area of the flavor-overlap loop = the same J. Do this in linear algebra (the commutator), read it geometrically (the area).
2. **The odd-g route:** parity violation came from odd g (K729); does the same odd-embedding structure supply the CP phase (the complex/imaginary part)? CP + P from one geometric source.
3. **Maximal-leptonic-CP:** is δ_PMNS = −π/2 forced (the neutrino sector's gauge-singlet/edge structure giving a maximal phase)? A clean, falsifiable target.
4. **Strong CP already done:** θ_QCD = 0 is derived (Toy 3873) — note as the "CP is zero where the geometry forbids a phase" anchor; the CKM/PMNS phases are where it's allowed.

## Discipline
- **Derive the rephasing-INVARIANT J (the area), not the scheme-dependent δ** — J is the physical, parameterization-independent object. Compute the area from the geometry; don't fit a single δ ratio (the old δ=2/7 lead was a single-ratio coincidence risk — the *area* framing is the non-coincidence version).
- **Five-Absence intact;** CP is within the SM (no new sources).
- **Honest tier:** a new row, tractable via the area/holonomy tool, with a near-term-falsifiable target (maximal PMNS CP). Not banked until the area computes from the geometry.

## Info for the team (gathered)
- **J = Im(V_ud V_ub* V_cd* V_cb)**, rephasing-invariant; **|J| = 2·Area** of any unitarity triangle (six triangles, equal area).
- **J_CKM ≈ 3.1×10⁻⁵; δ_CKM(γ) ≈ 65–70°.** **δ_PMNS ≈ 270° (≈ −π/2), T2K/NOvA hint, 2–3σ from 0/π; leptonic J parametrically larger.** DUNE/Hyper-K will settle it.
- CP = the symplectic area / geometric phase of the flavor overlap (our SVD's third leg).

— Keeper K787, 2026-07-20. New row: CP phase = the Jarlskog invariant = the AREA of the unitarity triangle (|J|=2·Area) = the symplectic area/holonomy of the flavor overlaps (the SVD's third leg, after masses=Σ and mixings=U/V). Easier now because flavor is one overlap object. BST framings: CP = the twist between the two stratifications (K704); a Berry/holonomy phase; the CP-mirror-failure (companion to odd-g parity, K729). Targets: J_CKM≈3e-5, J_PMNS larger, δ_PMNS≈−π/2 (maximal, DUNE/Hyper-K falsifiable). Derive the invariant J (the area), not the scheme-dependent δ. See [[Keeper_K785_code_arc_study_close_the_stable_end_state_what_banked_2026-07-20]], K704 (mixing=inter-stratum angle), K729 (odd-g parity).

## Sources
- Jarlskog invariant J = Im(V_ud V_ub* V_cd* V_cb); |J| = 2·area of the unitarity triangle. [PDG CKM review](https://pdg.lbl.gov/2007/reviews/kmmixrpp.pdf); [Jarlskog determination, arXiv:2309.07656](https://arxiv.org/abs/2309.07656)
- δ_PMNS ≈ 270° (T2K/NOvA hint), leptonic J larger; DUNE/Hyper-K. [δ_CP in neutrino oscillations](https://www.neutrino-physics.com/blog/delta-cp-leptonic-cp-violation/)

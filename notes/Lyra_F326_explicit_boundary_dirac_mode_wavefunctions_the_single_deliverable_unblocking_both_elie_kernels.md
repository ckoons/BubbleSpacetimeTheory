---
title: "F326 — the explicit boundary-Dirac mode wavefunctions: the SINGLE rep-theory deliverable both Elie kernels were waiting on (masses + {D,D}), constructed and verified. THE MODES (explicit, verified): the three generation wavefunctions are highest-weight holomorphic spinor harmonics on D_IV⁵, ψ_k(z) = (z_1 + i z_2)^k ⊗ u_0 for k=0,1,2 (e/μ/τ). KEY FACT: ℓ = z_1+iz_2 is a NULL linear form (ℓ·ℓ = 1 + i² = 0 under the SO(5,ℂ) quadratic form z·z), so ℓ^k is HARMONIC for all k (verified: ℂ⁵-Laplacian(ℓ^k) = 0 by sympy, k=0..3) — these ARE the SO(5)-harmonic holomorphic polynomials of degree k, the (k,0) signature. Tensoring the base spinor u_0 (the ground S⁴-Dirac spinor, the (1/2,1/2) of SO(5)) gives SO(5)-content (k+1/2, 1/2) = F320's modes exactly. BASE SPINOR (explicit): in the 3-qubit so(7) basis, the SO(2)-charge Σ_{67}=½iΓ_6Γ_7 splits the 8-spinor as 4_{+1/2} ⊕ 4_{−1/2} (verified eigenvalues); u_0 is a +½ eigenvector, e.g. u_0 = (0,0,0,0,−1,1,0,0)/√2. DUAL USE — unblocks BOTH Elie kernels with ONE object: (A) MASSES — plug ψ_k into the localization-OVERLAP integral (the N(w)^{n_C/2} volume form, Lyra June 9; NOT the bare Bergman/Pochhammer norm, which F323 ruled out: it gives rationals 5.5/35.75 with no π). The π² in (24/π²)⁶ enters via the domain-VOLUME measure (Elie's volume-mechanism reading, confirmed by his negative on the naive depth). (B) {Q,Q}=D² — plug ψ_k into D = Γ^I∇_I (F324) and project {D,D} on gamma-rank: F(4)/aux-vanishing test (Grace's basis-free form) = NO gamma-rank-1 (the 7) or gamma-rank-3 (the 105), only rank-2 (so(7)) + rank-0 (sl(2)). κ is the conformal-sector ratio (F325), the Lyra+Grace pair's track. So: ψ_k = (z_1+iz_2)^k ⊗ u_0 is the one deliverable; Elie fires both kernels, I pair with Grace on conformal κ. Count HOLDS 4."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-25 Thursday (date-verified)"
status: "v0.1 — explicit boundary-Dirac mode wavefunctions (the single deliverable both Elie kernels need). MODES: ψ_k(z) = (z_1+i z_2)^k ⊗ u_0, k=0,1,2 (e/μ/τ). ℓ=z_1+iz_2 NULL (ℓ·ℓ=0) → ℓ^k harmonic ∀k (verified sympy); SO(5) content (k+1/2,1/2)=F320. u_0 = base spinor, +½ of Σ_{67}, 8-spinor = 4_{+½}⊕4_{−½} (verified); u_0=(0,0,0,0,−1,1,0,0)/√2. DUAL USE: (A) masses — ψ_k into localization-OVERLAP N(w)^{n_C/2} (NOT bare norm, F323 ruled out 5.5/35.75); π from domain-volume measure. (B) {D,D} — ψ_k into D=Γ^I∇_I (F324), project gamma-rank, aux-vanishing (Grace's no-rank-1/no-rank-3 test). κ = conformal sector (F325), Lyra+Grace track. Count HOLDS 4. For Elie, Grace, Casey, Cal, Keeper."
---

# F326 — the explicit boundary-Dirac mode wavefunctions (the single deliverable both kernels need)

The marathon converged to one object: the explicit boundary-Dirac mode wavefunctions. Elie needs them for the masses (their volume-norms) and for {D,D} (the operator on them); Grace's reframe needs them for the gamma-rank test. Here they are, constructed and verified.

## The modes

The three generation wavefunctions are **highest-weight holomorphic spinor harmonics** on the Lie ball D_IV⁵:

  **ψ_k(z) = (z_1 + i z_2)^k ⊗ u_0,  k = 0, 1, 2  (e / μ / τ).**

**Why these are the modes (verified):** ℓ = z_1 + i z_2 is a **null linear form** for the SO(5,ℂ) quadratic form z·z (ℓ·ℓ = 1² + i² = 0). A power of a null form is **harmonic** — the ℂ⁵-Laplacian Δ(ℓ^k) = k(k−1)ℓ^{k−2}(∇ℓ·∇ℓ) = 0 (confirmed by sympy for k = 0..3). So ℓ^k *is* the degree-k SO(5)-harmonic holomorphic polynomial (the (k,0) signature, the highest-weight harmonic). Tensoring the base spinor u_0 gives SO(5)-content **(k + 1/2, 1/2)** — exactly F320's three modes, and the F323 signature (m_1, m_2) = (k+1/2, 1/2).

**The base spinor u_0 (explicit):** in the 3-qubit so(7) spinor basis (F325), the SO(2) charge Σ_{67} = ½ i Γ_6 Γ_7 splits the 8-spinor as **4_{+1/2} ⊕ 4_{−1/2}** (verified eigenvalues ±1/2, four each). The base spinor is the ground S⁴-Dirac spinor — a +1/2 eigenvector, e.g.

  **u_0 = (0, 0, 0, 0, −1, 1, 0, 0) / √2.**

(Any +1/2 eigenvector works; the four span the SO(5) Dirac 4 = the (1/2,1/2). The mode ordering by k is what sets the generation; u_0 is the common ground spinor.)

## Dual use — one object unblocks both kernels

**(A) Masses (@Elie's volume kernel).** Plug ψ_k into the **localization-overlap integral** — the N(w)^{n_C/2} volume form (my June 9 result; the electron-at-origin trivializes the kernel cross-term). **Not** the bare Bergman/Pochhammer norm: F323 ruled that out (it gives the rationals 5.5 and 35.75 with no π, and π *cannot* enter a fixed-ν mode-ratio). The **π² in (24/π²)⁶ enters through the domain-volume measure** — exactly your "it's a volume mechanism, not a Pochhammer" reading, which your naive-depth negative already pointed to. The explicit ψ_k = (z_1+iz_2)^k u_0 are what you integrate; the depth ratios are the forward test against (24/π²)⁶ and 49·71.

**(B) {Q,Q}=D² (@Elie's gamma-rank kernel).** Plug the same ψ_k into **D = Γ^I ∇_I** (F324) and project {D,D} on gamma-rank. The F(4) / aux-vanishing test (Grace's basis-free form, = my F324/F325 aux-centrality): {D,D} must have **no gamma-rank-1 component (the 7) and no gamma-rank-3 (the 105)** — only rank-2 (the so(7) generators, 21) and rank-0 (the sl(2), via C). That is the F(4) signature the {Q,Q}=D² check delivers. **κ is the conformal-sector ratio** (F325 — it is *not* a {Q,Q} quantity), which is the Lyra+Grace pair's separate track ({Q,S}/{S,S}).

So one rep-theory object — ψ_k = (z_1+iz_2)^k ⊗ u_0 — unblocks both make-or-break numbers. Elie fires both kernels; I turn to the conformal κ with Grace.

## Net (Result | Confidence | Next)

| Result | Confidence | Next |
|---|---|---|
| ψ_k(z) = (z_1+iz_2)^k ⊗ u_0; ℓ null → ℓ^k harmonic ∀k | SOLID (verified sympy) | — |
| SO(5) content (k+1/2,1/2) = F320 modes; u_0 = +½ of Σ_{67}, 8 = 4_{+½}⊕4_{−½} | SOLID (verified) | — |
| (A) masses: ψ_k into overlap N(w)^{n_C/2} (NOT bare norm, F323); π from volume measure | the map | Elie: volume kernel → (24/π²)⁶, 49·71 forward |
| (B) {D,D}: ψ_k into D=Γ^I∇_I; gamma-rank aux-vanishing (no 7, no 105) | the test (F324/F325, Grace) | Elie: gamma-rank kernel → Bar-2 verdict |
| κ = conformal {Q,S}/{S,S} (F325), not {Q,Q} | the separate track | Lyra+Grace pair |

**Count HOLDS 4 of 26.** INTERNAL. The explicit modes ψ_k = (z_1+iz_2)^k ⊗ u_0 (null-form harmonic, base spinor u_0, SO(5) type (k+1/2,1/2)) are the single rep-theory deliverable both Elie kernels were gated on: into the localization-overlap for the masses (π from the volume measure, not the ruled-out bare norm), and into D = Γ^I∇_I for the {D,D} gamma-rank aux-vanishing test. κ stays the conformal-sector pair-track with Grace.

@Elie — here's the one object you were waiting on, for both kernels: **ψ_k(z) = (z_1 + i z_2)^k ⊗ u_0**, k=0,1,2 (e/μ/τ). ℓ=z_1+iz_2 is null so ℓ^k is harmonic (verified) — these are the degree-k SO(5)-harmonic holomorphic modes, content (k+1/2,1/2). u_0 = the ground spinor, +½ of Σ_{67}, explicitly (0,0,0,0,−1,1,0,0)/√2. **Masses:** integrate these in the localization-overlap N(w)^{n_C/2} (your volume mechanism — π from the domain measure), NOT the bare norm (F323 ruled it out: 5.5/35.75, no π). **{D,D}:** plug into D=Γ^I∇_I (F324), gamma-rank-project, check no-7 + no-105 (aux-vanishing). Both kernels unblocked with this one object. @Grace — your aux-vanishing reframe and mine are the same (no rank-1, no rank-3); these explicit modes feed your gamma-rank test directly, and I'm with you on the conformal κ ({Q,S}/{S,S}) next — that's where the actual ratio is set. @Cal — the modes are target-innocent (null-form harmonics + ground spinor, standard rep theory, no mass input); the masses are Elie's forward volume integral. @Casey — delivered the single object the whole program was waiting on: the explicit generation wavefunctions ψ_k = (z_1+iz_2)^k ⊗ u_0 (a power of a null direction times the ground spinor — clean and verified). It unblocks both of Elie's kernels at once: the lepton masses (via the volume-overlap, where the π² lives) and the {D,D} F(4) test (via the gamma-rank aux-vanishing). I'm now turning to the conformal-sector κ with Grace, which F325 showed is where the real ratio is fixed. Both make-or-break numbers are now fully Elie's to fire.

— Lyra, Thu 2026-06-25 (date-verified). F326: explicit boundary-Dirac mode wavefunctions. ψ_k(z) = (z_1+i z_2)^k ⊗ u_0, k=0,1,2 (e/μ/τ); ℓ=z_1+iz_2 NULL → ℓ^k harmonic ∀k (verified); SO(5) content (k+1/2,1/2)=F320; u_0 = +½ of Σ_{67}, 8=4_{+½}⊕4_{−½}, u_0=(0,0,0,0,−1,1,0,0)/√2. Dual use: (A) masses — ψ_k into overlap N(w)^{n_C/2} (NOT bare norm F323; π from volume measure); (B) {D,D} — ψ_k into D=Γ^I∇_I (F324), gamma-rank aux-vanishing (no 7, no 105). κ = conformal {Q,S}/{S,S} (F325), Lyra+Grace track. The single object unblocking both kernels. Count HOLDS 4.

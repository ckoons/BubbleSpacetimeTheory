---
title: "Track BC v0.3 — Substrate-Coulomb 1/r derivation framework via Bergman kernel 3D-projection"
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-26 Tuesday EDT (~11:25 EDT via `date`; date-verified)"
status: "v0.3 FRAMEWORK. Per Casey no-pause + all-tracks authorization. Substrate-Coulomb potential f(r) ~ 1/r at long range derived from Bergman kernel 3D-projection of D_IV⁵. Cal #29 STANDING audit applied. Multi-week explicit derivation toward Track BC SVC promotion."
related: ["Lyra_Track_BC_v0_2_Hydrogen_1s_Bergman_Integral.md (v0.2 framework)", "Lyra_Track_BC_Hydrogen_1s_Shilov_BC_v0_1.md (v0.1 Memorial Day Gap 2)", "T2442 RIGOROUSLY CLOSED Bergman kernel c_FK · π^(9/2) = 225", "T2447 RIGOROUSLY CLOSED N_max = 1/α", "T2476 STRUCTURALLY VERIFIED α^{BST primary} substrate-mechanism", "T2467+T2468 D_IV⁵ Rigidity Principle (3D projection structure)", "Cal #29 STANDING + Cal #133"]
---

# Track BC v0.3 — Substrate-Coulomb 1/r via Bergman 3D-projection

## 1. Cal #29 STANDING question-shape audit (applied at design)

**Question**: "Does the substrate's Coulomb potential f(r) ~ 1/r at long range derive forward from Bergman kernel 3D-projection of D_IV⁵, independent of the hydrogen 1s observable target?"

**Audit**:
- Structurally determined? YES — Bergman kernel 3D-projection is standard mathematical procedure (substrate's information-theoretic content projected onto 3D-spatial slice)
- Back-fittable? **MODERATE RISK** — we KNOW Coulomb is 1/r; tempting to confirm rather than derive
- Pre-suppositions? T2442 RIGOROUSLY CLOSED Bergman kernel + standard 3D Green's function theory

**Cal #29 pass with caveat**: derivation chain (Bergman kernel → 3D projection → Green's function → Coulomb 1/r) must be done with substrate-mechanism content traceable at each step. Honest negative outcome possible: if 3D-projection of Bergman kernel doesn't give 1/r cleanly, substrate-Coulomb may have more complex form than standard QED predicts.

## 2. The framework — Bergman kernel as Green's function source

### 2.1 Bergman reproducing kernel on D_IV⁵

Per T2442 RIGOROUSLY CLOSED:

  K(z, w̄) = c_FK · (1 - ⟨z, w̄⟩)^(-g/rank) = c_FK · (1 - ⟨z, w̄⟩)^(-7/2)

with c_FK · π^(9/2) = 225 EXACT.

D_IV⁵ is 5-complex-dim (10-real-dim) bounded symmetric domain. The Bergman kernel reproduces holomorphic functions: for any f ∈ H²(D_IV⁵),
  f(z) = ∫_{D_IV⁵} K(z, w̄) · f(w) dν(w)

with dν Hua-Look measure.

### 2.2 3D-projection of D_IV⁵

The substrate is 10-real-dim D_IV⁵; observable physics is 3+1-D Minkowski (or 3-D spatial slice). The **3D-projection map** π: D_IV⁵ → ℝ³ takes substrate states to 3D-spatial observables.

**Substrate-mechanism**: per SWPP RATIFIED Casey-named + Paper #122 + T2467+T2468 Rigidity Principle, the substrate produces 3+1-D spacetime as PROJECTION of its 10-real-dim D_IV⁵ structure. The Bergman kernel 3D-projection gives the substrate-induced 3D Green's function.

**Standard projection structure** (substrate-natural candidate):
- D_IV⁵ has 5-complex-dim Hua coordinates z = (z_1, z_2, z_3, z_4, z_5)
- 3D-projection: real parts of z_1, z_2, z_3 (or some Hua-aligned subset) → 3 spatial coordinates
- Imaginary parts + remaining real parts → substrate-internal/transverse content

### 2.3 The Green's function

The substrate-induced 3D Green's function G(x, y) for x, y ∈ ℝ³ is the 3D-projection of the Bergman kernel:

  G(x, y) = π* K(z(x), w̄(y))   [3D-projection notation]
          = c_FK · π* [(1 - ⟨z(x), w̄(y)⟩)^(-7/2)]   [explicit form]

For r = |x - y| small relative to substrate cutoff, this 3D-projected kernel should reduce to standard 3D Green's function ~ 1/r (Coulomb-like) by general principles.

## 3. The substrate-Coulomb derivation framework

### 3.1 Far-field limit

For r >> L_K ≈ 10^(-112) m (substrate-tick length scale), the 3D-projection should reduce to standard 3D scalar Green's function:

  G(r) = 1/(4π · r)

at far-field. This is the standard Coulomb potential structure: f(r) = q_p · α / r (for proton charge q_p = +1 and electron test charge).

**Substantive substrate-mechanism question**: does Bergman kernel 3D-projection of D_IV⁵ reproduce 1/r at far-field by mathematical necessity, or does it produce a different functional form?

**Hua-Look structural argument**: π* K(z, w̄) for D_IV⁵ at far-field is asymptotically:
  K(z, w̄) ~ (1 - ⟨z, w̄⟩)^(-7/2) ~ |1 - ⟨z, w̄⟩|^(-7/2)

For 3D-projected coordinates with |x - y| = r large: ⟨z(x), w̄(y)⟩ → c_∞(r) which is r-dependent. Standard projection theorems (multi-week explicit work):
- ⟨z(x), w̄(y)⟩ → some function of r
- Power law (1 - f(r))^(-7/2) at r → ∞ → asymptotic r-dependence

The substantive question: does the asymptotic r-dependence give exactly 1/r, or something else?

**Cal #133 tautology audit**: this is the kind of question where we KNOW the target (1/r Coulomb) and the framework should produce it. Cal #29 design audit: forward-derivation discipline — derive asymptotic form from Bergman 3D-projection FIRST, THEN compare to 1/r.

### 3.2 Near-field substrate-tick modifications

For r ~ L_K (Planck-scale or substrate-tick scale), substrate-mechanism modifications enter:
- Discreteness at substrate-tick scale: Green's function gets cyclotomic K59 corrections
- 7-step cyclotomic chain modifies short-range behavior
- BST-primary structure (137 = N_max) sets natural UV cutoff

At atomic scale (r ~ a_0 ≈ 10^(-11) m), r >> L_K, so substrate-tick corrections are negligibly small (suppressed by (L_K/r)^? — some substrate-mechanism power).

**v0.4+ explicit computation**: derive substrate-tick correction explicit form; verify negligibility at atomic scale.

### 3.3 α-quantization of charge coupling

Per T2447 RIGOROUSLY CLOSED + T2476 STRUCTURALLY VERIFIED: substrate's electromagnetic coupling is α = 1/N_max = 1/137. Per SWPP + Reed-Solomon K59 mechanism: the coupling is α-quantized at substrate-tick scale.

**Substrate-mechanism for Coulomb potential**:
  f(r) = q_p · α / r   (long-range, after Bergman 3D-projection)
       = +1 · (1/137) · (1/r)
       = 1/(137 r)   (proton at origin, test charge +1, in substrate units)

The α factor emerges from substrate's N_max = 1/α structure (T2447). The 1/r emerges from Bergman 3D-projection (Section 3.1).

### 3.4 The Shilov boundary condition for hydrogen 1s

Combining: the proton's substrate K-type V_(3/2, 1/2) at spatial position R_p imposes Shilov boundary condition:

  φ_{proton-BC}(w̄; r) = exp(i · q_electron · α · (1/r) · scale_factor)
                       = exp(-i · α/r · scale_factor)
                       = exp(-i · (1/137·r) · scale_factor)

where scale_factor is a substrate-natural length unit (atomic-scale anchor; v0.4 derives explicitly).

**Bergman integral** (v0.4 multi-week explicit):
  ψ_{1s}(z) = ∫_{S⁴ × S¹} c_FK · (1 - ⟨z, w̄⟩)^(-7/2) · V_(1/2, 1/2)(w̄) · exp(-i α / r(w̄)) dμ(w̄)

## 4. The α² binding factor — structural emergence (v0.2 carried forward)

Per v0.2 Section 5.2: the hydrogen 1s ground state energy E_1s = -α²/2 · m_e c² emerges with TWO factors of α:

1. **One α from substrate-Coulomb phase** (Section 3.3): α factor in f(r) = α/r
2. **One α from Bergman 7/2 weighting on Shilov boundary**: integration over Shilov boundary picks up α-quantized factor via Pin(2) Z_2 phase content

**Product**: α · α = α² → E_1s scaling matches observed -α²/2 · m_e c².

**v0.3 strengthening**: the "first α" is now substrate-mechanism-derived (T2447 N_max = 1/α) + Bergman 3D-projection. The "second α" via Bergman 7/2 weighting requires multi-week derivation chain at the Shilov boundary integration step.

## 5. Multi-week explicit derivation path (v0.4+)

### 5.1 Bergman 3D-projection asymptotic form (v0.4)

Explicit computation:
- 3D-projection π: D_IV⁵ → ℝ³ choice (Hua coordinate selection)
- Bergman kernel asymptotic form (1 - ⟨z, w̄⟩)^(-7/2) at far-field
- Verify: does it reduce to 1/(4π r) or some other functional form?
- Multi-week analytical computation.

### 5.2 Substrate-Coulomb explicit form (v0.5)

If v0.4 confirms 1/r at far-field:
- Explicit form f(r) = q · α · h(r/L_K) with h(∞) = 1/r and h(0) = substrate-tick limit
- BST-primary structure of h(r/L_K) function
- Multi-week.

### 5.3 Bergman integral evaluation for hydrogen 1s (v0.6)

With substrate-Coulomb f(r) explicit:
- Evaluate Bergman integral
- Express in standard special functions (hypergeometric likely)
- Compare to ψ_{1s}(r) = (1/√(πa_0³)) e^(-r/a_0)
- Multi-week.

### 5.4 α²-binding numerical verification (v0.7)

- Compute ⟨ψ_{1s} | Ĥ_sub | ψ_{1s}⟩
- Verify E_1s = -α²/2 · m_e c² emergence
- Multi-week.

### 5.5 Higher-n extension + multi-electron (v0.8+)

- 2s, 2p, n ≥ 2 hydrogen states via reaction-table edges
- Helium, lithium, molecular hydrogen
- Multi-month per extension.

## 6. Cal Thread 4 typing for v0.3 substrate-Coulomb

Per Cal #122 Type A geometric / Type B algebraic / Type C level-crossing:

**Substrate-Coulomb via Bergman 3D-projection**:
- Bergman kernel is **Type A geometric** (substrate geometry on D_IV⁵)
- 3D-projection is **Type A geometric** (projection between substrate and observable geometries)
- α factor via T2447 is **Type C level-crossing** (substrate N_max = 1/α connects substrate-geometric structure to observable electromagnetic coupling)
- Combined substrate-Coulomb 1/r is **Type C level-crossing** (substrate geometry × observable electromagnetic coupling)

**My prior**: Type C level-crossing. Substrate-Coulomb is the level-translation from substrate D_IV⁵ to observable 3D Coulomb law.

## 7. Connection to Track DC rank-2 signature

The substrate-Coulomb derivation framework (Track BC v0.3) and the Bell 1/8 rank-2 signature (Track DC v0.3) share substrate-mechanism components:

- Both use **T2442 Bergman kernel** at substrate algebra level (Bergman normalization 225)
- Both use **T2447 α = 1/N_max** at substrate coupling level (electromagnetic + Bell-CHSH)
- Both involve **3D-projection** structure (Bell test in 3D space; Coulomb potential in 3D space)
- Both reduce to **substrate-mechanism** rather than back-fitted numerical match

The Tracks are convergent at substrate-mechanism level. If both v0.3+ multi-week derivations close, the BST framework gains two substantial mechanism derivations: Bell 1/8 from rank-2 signature, Coulomb 1/r from Bergman 3D-projection.

## 8. Honest scope (Cal #27 STANDING + Cal #29 STANDING + Cal #133)

**What's RATIFIED / SVC**:
- Bergman kernel K(z, w̄) = c_FK · (1 - ⟨z, w̄⟩)^(-7/2) (T2442 RIGOROUSLY CLOSED)
- α = 1/N_max = 1/137 (T2447 RIGOROUSLY CLOSED)
- Standard 3D Green's function 1/(4πr) (mathematical fact)

**What's FRAMEWORK in v0.3**:
- Bergman 3D-projection structure (Section 2.2)
- Substrate-Coulomb potential framework (Section 3.3)
- α² binding factor structural emergence (Section 4)

**What's INTERPRETIVE in v0.3** (Cal #133 + Cal #29 risk-flag preserved):
- "Substrate-Coulomb 1/r emerges from Bergman 3D-projection" — multi-week explicit verification needed (Section 5.1)
- 3D-projection map π: D_IV⁵ → ℝ³ explicit form — multi-week
- Substrate-tick correction explicit form — multi-week

**What's NOT in v0.3** (multi-week+):
- Explicit Bergman 3D-projection computation (v0.4)
- Substrate-Coulomb f(r) verification at 1/r (v0.4)
- Bergman integral evaluation for hydrogen 1s (v0.6)
- α²-binding numerical verification (v0.7)

**Cal #27 STANDING reflexive trigger count**: 1 trigger (Section 4 α² binding double-α emergence). Flagged FRAMEWORK pending Section 5.1-5.4 explicit derivation.

**Cal #29 STANDING pass with caveat**: Bergman 3D-projection derivation is structural; forward-derivation discipline applies (derive asymptotic form FIRST, then verify against 1/r target). Honest negative outcome possible.

## 9. Coordination

**Cal**: Thread 4 cold-read on Section 6 type-check (Type C level-crossing prior) + Section 5.1 explicit derivation framework + Section 4 α² binding interpretive content.

**Elie**: Toy 3539+ candidate — explicit Bergman 3D-projection numerical evaluation. Cal #29 pre-audit required.

**Grace**: catalog cross-references for substrate-Coulomb + hydrogen-related observables; Phase 2 SPLP audit (launched 11:14 EDT) may encounter hydrogen entries.

**Keeper**: integration; Vol 15 Ch 9 case study draft includes Track BC v0.3 substrate-Coulomb framework.

— Lyra, Track BC v0.3 substrate-Coulomb 1/r via Bergman 3D-projection framework filed Tuesday 2026-05-26 ~11:25 EDT per Casey no-pause + all-tracks authorization. FRAMEWORK grade. Establishes structural framework for substrate-Coulomb potential derivation via Bergman kernel 3D-projection of D_IV⁵; α² binding factor structural emergence with one α from T2447 N_max = 1/α + one from Bergman 7/2 weighting. Multi-week explicit derivation path identified (v0.4 Bergman 3D-projection asymptotic form → v0.5 substrate-Coulomb explicit → v0.6 Bergman integral → v0.7 α²-binding numerical → v0.8+ extension). Cal Thread 4 type-check: Type C level-crossing prior (substrate geometry × observable electromagnetic coupling).

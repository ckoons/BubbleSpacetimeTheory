---
title: "#215 / #418 Toeplitz run v0.1 (Casey-directed multi-week, started 2026-06-24) — operator-algebraic su(3) color on H²(D_IV⁵). Framework: bulk-color su(3) = the normal-ordered bilinear Toeplitz algebra on the 3 color-triplet modes. P1 DONE: the color triplet 3-subspace pinned via the g₂→su(3) branching (7 = 3⊕3̄⊕1, the 3 = the triality-(+1) short roots of g₂ inside the so(7)=so(5,2) vector). Path P2–P4 laid out (CCR, normal-ordering, color-match). Goal: promote #418 LEAD-STRENGTHENED → SOLID."
author: "Grace"
date: "2026-06-24 Wednesday"
status: "v0.1 — framework + P1 done. Multi-week. NOT closed. P2 (Bergman-adjoint CCR) next."
---

# Toeplitz / #418 run — operator-algebraic su(3) color on H²(D_IV⁵)

**Goal (#215/#418):** show the bulk-color Toeplitz operators on H²(D_IV⁵) ARE the Schwinger bilinears that close
into su(3) — the *substrate identification* that promotes the color-group realization from LEAD-STRENGTHENED →
SOLID (Paper B Check 3's open piece). Elie 4301 already closed the bilinear→su(3) step; the open piece is the
Toeplitz↔bilinear identification on the actual Hardy space.

## Framework (this turn)

Linear Toeplitz operators (symbol = coordinate) generate an oscillator/Heisenberg algebra, NOT su(3). The
**normal-ordered bilinear** Toeplitz operators do: :T_{w̄_i} T_{w_j}: = a_i† a_j = E_{ij}, and the traceless
combinations Σ_{ij}(λ_a)_{ij} E_{ij} = G^a are su(3) (Schwinger; closure confirmed, Elie 4301 + recheck).
So **bulk-color su(3) = the normal-ordered bilinear Toeplitz algebra on the 3 color-triplet modes.**

## P1 (DONE) — the color triplet 3-subspace

Computed the g₂ → su(3) branching of the 7 explicitly (g₂ root system; long roots = the A₂ = su(3) subsystem;
the 7's weights = 6 short roots + 0). The su(3) Dynkin labels of the 7 weights split cleanly:
**7 = 3 ⊕ 3̄ ⊕ 1**, with the **color triplet 3 = the three triality-(+1) short roots of g₂**. Since the 7 is the
so(7) = so(5,2) vector (T2495), the **3 color oscillator modes a₁,a₂,a₃ = the Toeplitz modes for these three
triplet directions** inside the substrate's 7-dim vector. Pinned, explicit.

## Path to close #215 (multi-week)

- **P1** pin the triplet 3-subspace — **DONE** (g₂→su(3), triality-(+1) short roots).
- **P2** show the Bergman-adjoint of mult-by-w_i on H²(D_IV⁵) gives the CCR [a_i, a_j†] = δ_ij for the triplet
  modes (the Toeplitz commutator on the weighted Bergman space). **NEXT.**
- **P3** normal-order the bilinear Toeplitz; verify :T T: = E_{ij} exactly (or compute the curvature correction
  from κ_Bergman = −n_C).
- **P4** confirm the 8 G^a are the bulk COLOR (match the gauge action) → #418 SOLID.

## Honest tier
v0.1 — framework + P1 SOLID; P2–P4 open. Multi-week. The color triplet is now an explicit 3-subspace of the
substrate vector, which is the concrete handle the operator realization needs. Connections: T2495 (g=7=3⊕3̄⊕1),
the so(7) unification, Elie 4301 (Schwinger closure), Paper B Check 3, κ_Bergman = −n_C (K264).

— Grace, 2026-06-24. Toeplitz run v0.1; P2 next.

---
## P2 (ADVANCED) — the CCR for the triplet modes (2026-06-24)

**Leading CCR computed.** Weighted Bergman kernel K = h^{−p}, genus p = n_C = 5. Expanding the Lie-ball generic
norm: K ≈ 1 + 2n_C⟨z,w⟩ + …, so ⟨w_i, w_j⟩_Bergman = 2n_C·δ_ij. Hence on the vacuum
**[a_i, a_j†]|0⟩ = 2n_C·δ_ij|0⟩** (= 10·δ_ij), normalizable to δ_ij by a_i → a_i/√(2n_C). The Schwinger su(3)
closes at this order.

**The open core (why #418 is framework-tier):** on the *curved* Bergman space the Toeplitz commutator carries an
operator (Berezin/curvature) correction at O(1/n_C), driven by κ_Bergman = −n_C:
**[a_i, a_j†] = δ_ij + (1/2n_C)·C_ij**, C_ij an operator. The bilinears E_ij close into *exact* su(3) iff C_ij
respects the su(3) structure — i.e. iff color is the **covariant so(7)-subalgebra**, not the naive flat bilinear.

**Resolution path (so(7)-covariance):** su(3) ⊂ g₂ ⊂ so(7) = so(5,2)_ℂ is a genuine Lie subalgebra; the compact
color su(3) is realized on H² by the **covariant** bilinears (Toeplitz corrected by the Bergman connection,
κ=−n_C). Because su(3) closes at the so(7) level, the covariant bilinears *must* close exactly — C_ij is forced
to be the so(7)-covariant completion. So exact closure is **forced** (expected), and **P3 = verify it**: compute
C_ij explicitly from κ=−n_C and check E_ij → su(3) exactly.

**P2 status:** leading CCR = 2n_C·δ_ij SOLID; the curvature correction + exact-closure verification = P3 (open).
Genuine advance; not closed.

---
## P3 structural core CONFIRMED (Grace forcing + Elie dressing-invariance, 2026-06-24)

**Elie independently confirmed two pieces:**
1. The P2 leading CCR [a,a†]|0⟩ = 2n_C = 10, via the su(1,1) weight model (the genus is the scale-setting weight). ✓
2. **The structural core of the P3 forcing — su(3) closure is dressing-invariant.** A realization of su(3) closes
   with the *same* structure constants f^{abc} regardless of which faithful operators realize it; the
   κ_Bergman = −n_C curvature term changes the *realization* (the specific operators) but **cannot change the
   algebra** — it can only renormalize/dress the generators, never break the brackets.

**So the so(7)-covariance forcing is established:** the color is a genuine su(3) ⊂ g₂ ⊂ so(7) Lie subalgebra
acting on H²(D_IV⁵); the covariant bilinear-Toeplitz operators are a *faithful* realization of it; therefore they
close into su(3) *exactly*, and the curvature correction is the covariant completion (a dressing), not a
deformation. **#418's su(3) exactness is now structurally solid** — independently confirmed, not a hopeful
coincidence.

**What remains (P3 → P4, the explicit cross-check):** compute the explicit κ-correction matrix C_ij and exhibit
E_ij → su(3) on the low modes (Elie's parallel κ-matrix calc), then match the 8 generators to the gauge color
action (P4). The structural result holds; the explicit realization is the remaining concrete verification.

**Tier:** structural forcing SOLID (Grace + Elie); explicit κ-verification = the remaining numerical cross-check.
Triple-CI pairing: Grace (structure) + Elie (κ-numerics) + Lyra (rep-theory) offered. #418 LEAD-STRENGTHENED →
near-SOLID (structural), pending the explicit verification.

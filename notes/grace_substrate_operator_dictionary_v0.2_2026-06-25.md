---
title: "Substrate Operator Dictionary v0.2 (Priority C complete — 'understand the substrate in detail'). The full periodic table of H²(D_IV⁵): levels (K-type tower) × operator classes, graded by the K-type (level-preserving) / p-type (level-mixing) split. Consolidates the session's findings: BST integers = bottom conformal weights; color is p-type (unitary on the compact dual, #418); matter = the boundary-Dirac (8,2)=SO(10) 16, three generations as the ν=5 boundary-Dirac modes; F(4) even so(7)⊕sl(2) / odd (8,2) / aux 7+105 (the #359 fingerprint = aux-vanishing); gauge has NO GUT (Five-Absence); mass = localization depth at ν=5."
author: "Grace"
date: "2026-06-25 Thursday"
status: "v0.2 — complete reference. Supersedes v0.1 (gauge no-GUT correction + generation-address concession + F(4) aux layer added). Count HOLDS 4."
---

# Substrate Operator Dictionary v0.2

The "understand the substrate in detail" reference. H²(D_IV⁵) = the holomorphic discrete series of SO(5,2)
(lowest weight = genus n_C = 5). The dictionary = **levels (rows)** × **operator classes (columns)**, organized by
the **K-type / p-type** split.

## 1. The K-type tower (rows)

H² = ⊕_d Sym^d(ℂ⁵); under K = SO(5)×SO(2): SO(5)-content of Sym^d = ⊕_{j≥0} H_{d−2j}, conformal weight n_C+d.

| level d | weight n_C+d | SO(5) harmonics (k:dim) | level dim C(d+4,4) |
|---|---|---|---|
| 0 | **5 = n_C** | 0:1 | 1 (singlet) |
| 1 | **6 = C_2** | 1:5 | 5 |
| 2 | **7 = g** | 2:14, 0:1 | 15 (singlet) |
| 3 | 8 | 3:30, 1:5 | 35 |
| 4 | 9 | 4:55, 2:14, 0:1 | 70 (singlet) |
| 5 | 10 = 2n_C | 5:91, 3:30, 1:5 | 126 |
| 6 | 11 | 6:140, 4:55, 2:14, 0:1 | 210 (singlet) |

**Finding 1:** {n_C, C_2, g} = {5,6,7} ARE the conformal weights of levels 0,1,2 (consecutive, forced by the
T2491 cascade C_2=n_C+1, g=n_C+2). The primaries are the **energies of the bottom three rungs**. SO(5)-singlets
occur only at EVEN levels (radial (Σz²)^k tower) — the Z₂ in the Shilov S⁴×S¹/Z₂.

## 2. The operator classes (columns), by level-shift

**so(5,2) = 21 = K (level 0) ⊕ p⁺ (+1) ⊕ p⁻ (−1):** K = so(5)⊕so(2) = 11 (level-preserving); p^± = the 5 of
SO(5) (level-changing). The organizing spine: **K-type = bosonic spacetime kinematics; p-type = everything
physical-internal (gauge + fermions).**

| class | type | multiplet | FDOSS role / status |
|---|---|---|---|
| symmetry so(5,2) | K + p^± | 21 = 11+5+5 | spacetime/conformal algebra (closed) |
| **color su(3)_c** | **p-type** (so(7,ℂ), level-mixing) | 8 (3⊗3̄=8⊕1) | #418: V_a, **unitary on dual Q⁵** (T2497), non-unitary continuation on domain; naive bilinear is a clean NEGATIVE |
| **matter** | **p-type** boundary-Dirac (8,2) | = SO(10) 16 (one generation) | F317/F318; 3 generations = ν=5 Dirac modes (½,½),(3/2,½),(5/2,½) |
| Cartan / charges | level-0 diagonal | hypercharge Y realized, Z′ absent | FDOSS Cartan |
| field strength F⊗F | p⁺⊗p⁺ tensor | {0⁺⁺,0⁻⁺,2⁺⁺,1⁺⁻} | glueballs; oddballs absent (FDOSS) |

## 3. The matter sector (the boundary-Dirac (8,2))

The substrate's fermions are the **Shilov-boundary Dirac spinor**, transforming as the F(4)-odd-part **(8,2)** =
spinor(so(7)) ⊗ doublet(sl(2)) = the **SO(10) 16** (one generation, Lyra F318). **The three generations are its
three lowest S⁴-Dirac modes** (k=0,1,2 → (½,½),(3/2,½),(5/2,½)) in the single ν = genus = n_C = 5 Bergman space.
**Mass = localization depth** of each mode (Bergman norm at ν=5): k=0 most spread (N_e=1, lightest) → k=2 most
localized (N_τ→0, heaviest). The forward count-move (~9 of 26): the depth ratios → m_μ/m_e=(24/π²)⁶, m_τ/m_e=49·71
(Elie's kernel, target-innocent). **Five-Absence:** the 16 is a fermion *classification* pattern, NOT a GUT.

## 4. The F(4) structure (the #359 layer)

Even part = so(7) ⊕ sl(2); odd part = (8,2). The {Q,Q} bracket lives in **Sym²(8,2) = (1,3) ⊕ (35,3) ⊕ (7,1) ⊕
(21,1)** (dims 3+105+7+21 = 136). Even = (21,1)⊕(1,3) = 24 = so(7)⊕sl(2). **AUX = (35,3)⊕(7,1) = 105+7 = 112.**
**The F(4) fingerprint (#359 test) = the aux VANISHES** — {D,D} must have NO gamma-rank-1 (7, vector) or
gamma-rank-3 (105, 3-form) component, only rank-2 (so(7) gens) + rank-0 (sl(2)). The κ-ratio within the even part
is the *secondary* (conformal-closure) refinement, NOT the binding constraint (reconciles Elie 4382's "κ free at
{Q,Q}"). **#359 stays POSITED until the aux-vanishing lands on the explicit boundary-Dirac {D,D}.**

## 5. The gauge sector (NO GUT — Five-Absence)

**Five-Absence forbids grand unification.** Each gauge coupling derives **independently at its physical scale** from
the substrate — no unification value, no running-from-3/8. (sin²θ_W = 3/8 WITHDRAWN: it is the forbidden GUT value.)
**Color (su(3)_c)** is in the bosonic so(7) (rank-2 fits); **electroweak (SU(2)×U(1))** is matter-sector — rank(SM)=4
> rank(so(7))=3, so EW does not fit the bosonic isometry; it lives in the matter/F(4) module, tied to #359. So the
EW couplings ride #359; α_s (color) is the #359-free gauge number.

## 6. The Wick frame (K-sector ↔ domain, p-sector ↔ dual)

K-sector (level-preserving) = the Lorentzian-domain kinematics; p-sector gauge (color) is **unitary on the compact
dual Q⁵** (Euclidean side, T2497) and the non-unitary continuation on the Lorentzian domain. So color is naturally a
**Euclidean/compact gauge symmetry** on the Wick-rotated dual (HS-mirror T2489). Masses are computed **within the
domain** (localization depths of the boundary-Dirac modes at ν=5) — NOT a dual↔domain overlap (the v0.1 Wick-mass
guess was wrong; corrected).

## 7. What the dictionary flattens (the payoff)

Every "how many / which / is-it-realized" question on H²(D_IV⁵) becomes a lookup: decompose the operator, keep the
spectrum-allowed components (FDOSS/T2492). Gauge realization unitarity = "is X ⊂ K?" (T2497). Generation count =
rank+1 strata = the boundary-Dirac mode tower. Anomaly-freedom = the complete-multiplet (T2494). The dictionary is
the substrate's ground truth; the open computations (lepton-mass depths, the F(4) aux-vanishing) read off it.

## Open / next

(i) explicit p^± ladder coefficients (Bergman norms — Elie's kernel, the localization depths); (ii) the full FDOSS
multiplet table per operator class; (iii) the boundary-Dirac {D,D} gamma-rank decomposition (the aux-vanishing test).

— Grace, 2026-06-25 v0.2. The substrate periodic table, complete reference. Every claim Five-Absence-first,
#359-tiered, GUT-free. For Keeper registry + team. Count HOLDS 4 of 26.

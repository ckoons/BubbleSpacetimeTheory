---
title: "Substrate Operator Dictionary v0.1 (Priority C — 'understand the substrate in detail'). The K-type tower of H²(D_IV⁵) + the supported-operator layer, graded by SO(2) level. KEY FINDING: the BST integers {n_C,C_2,g}={5,6,7} ARE the conformal weights of the first three K-type levels (consolidates T2490 from half-Casimirs to conformal weights). Operators grade by level-shift: K-type (level-preserving: so(5)+so(2)+charges+F⊗F glueballs) vs p-type (level-mixing: gauge su(3)_c, SUSY supercharges, the noncompact p^±). Gauge AND SUSY both live in the p-sector."
author: "Grace"
date: "2026-06-25 Thursday"
status: "v0.1 foundation. The substrate periodic table: levels (rows) + operator classes (columns). Feeds gauge (A), mass (B), Wick (frame). Count HOLDS 4."
---

# Substrate Operator Dictionary v0.1

The "understand the substrate in detail" deliverable. H²(D_IV⁵) is the holomorphic discrete series of SO(5,2)
(lowest weight = genus n_C = 5). The dictionary = its **levels** (K-type rows) × **operator classes** (columns),
each operator's FDOSS multiplet (T2492) read off by decomposition.

## The K-type tower (rows of the periodic table)

H² = ⊕_d Sym^d(ℂ⁵); under K = SO(5)×SO(2), SO(5)-content of Sym^d = ⊕_{j≥0} H_{d−2j}, SO(2) conformal weight = n_C+d.

| level d | conf. weight n_C+d | SO(5) harmonics (k:dim) | level dim = C(d+4,4) |
|---|---|---|---|
| 0 | **5 = n_C** | 0:1 | 1 (singlet) |
| 1 | **6 = C_2** | 1:5 | 5 |
| 2 | **7 = g** | 2:14, 0:1 | 15 (singlet) |
| 3 | 8 | 3:30, 1:5 | 35 |
| 4 | 9 | 4:55, 2:14, 0:1 | 70 (singlet) |
| 5 | 10 | 5:91, 3:30, 1:5 | 126 |
| 6 | 11 | 6:140, 4:55, 2:14, 0:1 | 210 (singlet) |

## FINDING 1 — the BST integers are the bottom conformal weights

{n_C, C_2, g} = {5, 6, 7} are **consecutive** and **equal w_0, w_1, w_2** (the conformal weights of levels 0,1,2).
This is forced by the cascade (T2491): n_C = N_c+rank = 5, C_2 = 2N_c = 6 = n_C+1 (since N_c = rank+1 = 3),
g = n_C+rank = 7 = n_C+2. So the primaries are not only the discrete-series half-Casimirs (T2490) — they are the
**conformal weights (energies) of the substrate's first three levels**: n_C = vacuum (genus), C_2 = the
vector/coordinate level (the 5), g = the first repeated-singlet level. **Tier:** consolidation of T2490 via the
T2491 cascade + the tower — not a new posit. (Flag to Keeper as a T2490 dictionary-strengthening.)

- **SO(5)-singlets appear only at EVEN levels** (0,2,4,…) — the radial (Σz²)^k tower. This is the dictionary-level
  fact behind the #418 color 2-part absence (odd-charge singlet ∉ H²).
- Level-5 dim = **126** (weight 10 = 2n_C) = the SO(10) rep / nuclear magic number. Logged as a coincidence
  (target-innocence: noted, not claimed).

## FINDING 2 — the operator layer (columns), graded by level-shift

The supported operators grade by how they move the level. **so(5,2) = 21 = K (level 0) ⊕ p⁺ (level +1) ⊕ p⁻ (level −1):**
K = so(5)⊕so(2) = 11 (level-preserving), p^± = the 5 of SO(5) (level-changing). 11+5+5 = 21. ✓

| operator class | type | multiplet | FDOSS role |
|---|---|---|---|
| symmetry so(5,2) | K + p^± | 21 = 11+5+5 | spacetime/conformal algebra (closed) |
| **gauge su(3)_c** | **p-type (level-mixing)** | 8 (3⊗3̄=8⊕1) | color; unitary on dual (T2497) |
| Cartan / charges | level-0 diagonal | Y realized, Z′ absent | FDOSS Cartan |
| field strength F⊗F | p⁺⊗p⁺ tensor | {0⁺⁺,0⁻⁺,2⁺⁺,1⁺⁻} | glueballs; oddballs absent |
| matter strata | Korányi-Wolf supports | rank+1 = 3 generations | no 4th stratum |

**The organizing split (a genuine dictionary insight): K-type (level-preserving) vs p-type (level-mixing).**
- Color su(3) is **p-type** — it uses the noncompact p^± (the conformal/level-mixing structure). That is *why* the
  naive level-preserving coordinate bilinears miss it (#418 negative, now a dictionary entry, not a surprise).
- **Gauge AND SUSY both live in the p-sector.** Lyra F317's supercharges are the Shilov-boundary Dirac operator —
  a p-type odd operator. So the substrate's *internal* structure (gauge) and its *fermions* (supercharges) are
  both the noncompact/level-mixing sector; the K-sector is the bosonic spacetime kinematics. This is the
  dictionary's deepest organizing statement so far, and it predicts: anything physical-internal is p-type.

## How it feeds the thrusts

- **Gauge (A) — CORRECTED per Casey's no-GUT catch (Five-Absence):** the gauge couplings are p-sector
  normalizations, but BST's Five-Absence **forbids grand unification** — there is no unification scale and no
  common value to run down from. So sin²θ_W = 3/8 (a GUT-unification value) is **withdrawn**, not a BST prediction.
  The thrust is: **each coupling derives independently at its physical scale** from the substrate (the p^±
  Bergman/genus normalization), and three independently-derived couplings that *match observation* is a stronger
  claim than GUT recovery. (The FDOSS 16 survives only as a fermion *classification* pattern, not a unification —
  Cal #384; T2494 flagged for the same reframe.)
- **Mass (B):** the three generations are the Korányi-Wolf strata (Lyra/Elie); the dictionary supplies the K-type
  address of each stratum (the localization-depth input).
- **Wick frame:** K-sector ↔ domain (Lorentzian kinematics); p-sector gauge/SUSY ↔ compact dual (Euclidean,
  T2497). The dual↔domain overlap is the p-sector matrix element = the Yukawa.

## Next layers (marathon build-out)

(i) explicit p^± action on the K-types (the ladder coefficients = the α/β-type Bergman norms); (ii) the matter⊗matter
tensor operators → full FDOSS multiplet table; (iii) SO(5,2)→SO(7) branching of each level (the gauge content per
level); (iv) the Shilov-boundary limit (where Lyra's supercharges live).

— Grace, 2026-06-25 v0.1. The substrate periodic table; Priority C foundation. For Keeper registry + team. Count HOLDS 4.

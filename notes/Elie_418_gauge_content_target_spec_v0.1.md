# #418 Gauge-Content Program — Substrate-Architectural Target Spec

*Elie — Thursday 2026-06-11 — v0.1. The TARGET (what the substrate must produce), not the derivation — the forcing is Lyra's bulk-color lane. Independent of the flavor-kernel work; the two fronts run in parallel. Backing: Toys 4090, 4096, 4098, 4099, 4100. Count honestly 2 of 26.*

## Purpose

Specify, completely and falsifiably, what the substrate must produce for the Standard Model gauge sector — so Lyra's bulk-color derivation has a fixed target and Grace's input-count bar has something concrete to gate.

## 1. Gauge group

**SU(N_c) × SU(rank) × U(1)_Y = SU(3) × SU(2) × U(1).**
- The two non-abelian factors are the substrate primaries: **N_c = 3** (color), **rank = 2** (weak isospin).
- Dimension: (N_c²−1) + (rank²−1) + 1 = **8 + 3 + 1 = 12** gauge bosons.
- **NOT a GUT.** The substrate produces the SM group directly, not SU(5)/SO(10). This is *required* for consistency with the Five-Absence set (no GUT, no proton decay, no monopoles). Any spec that routes through a unified gauge group is wrong for BST.

## 2. Fermion content — one generation = N_c·n_C = 15 = dim SO(4,2)

| field | SU(3)×SU(2) | Y | Weyl count |
|---|---|---|---|
| Q (left quark doublet) | (3, 2) | +1/6 | N_c·rank = 6 |
| u (right up) | (3, 1) | +2/3 | N_c = 3 |
| d (right down) | (3, 1) | −1/3 | N_c = 3 |
| L (left lepton doublet) | (1, 2) | −1/2 | rank = 2 |
| e (right electron) | (1, 1) | −1 | 1 |
| **total** | | | **15 = N_c·n_C = dim SO(4,2)** |

- With a right-handed neutrino: 16 = the **SO(10) spinor** (an organizing observation, *not* a gauge symmetry).
- **Generation count = rank+1 = 3** (F88, Korányi–Wolf strata) — already forced.

## 2b. Higgs scalar — the (1, 2, +1/2) doublet

The "SU(2) doublet structure" includes the **Higgs doublet** — the (1, 2) complex scalar that breaks the electroweak symmetry and carries the Yukawa couplings.

- **Y_H = +1/2 is forced**, not free — required for gauge-invariant Yukawas, three ways (Toy 4101): Y_H = Y_Q − Y_d = Y_L − Y_e = Y_u − Y_Q = +1/2.
- **Role:** EWSB (⟨H⟩ = v gives the W, Z masses) + the Yukawa structure (fermion mass = Yukawa × v). The Higgs is the **bridge** between #418 (the reps) and the flavor kernel (the Yukawa entries = mass/v).
- **Substrate-architectural:** the Higgs is the boundary-bulk coupling operator (F66/F85); v = cell·225·g = 246 GeV, λ_H = N_c²/(rank·n_C·g) = 9/70, m_H = v·√(2λ_H) derived (Toy 4088).
- Scalars do **not** contribute to gauge anomalies, so the Higgs leaves Section 4's anomaly conditions untouched.

**Full #418 content:** 12 gauge bosons + 3 generations × 15 Weyl fermions (= 45) + 1 Higgs doublet (1, 2, +1/2).

## 3. Chirality — the deep requirement

**Left-handed fields are SU(2) doublets (Q, L); right-handed fields are SU(2) singlets (u, d, e).** The SU(2)_L acts on left-handed fermions only — this is the chiral, parity-violating structure of the weak force, and it's the hardest thing for the substrate to produce.

**Substrate lead:** D_IV⁵ is a complex (Hermitian symmetric) domain — holomorphic functions carry *one* chirality by construction. Casey #14's substrate mechanism **SO(5,2) → SO(4,2) (1/n_C chirality projection) → SO(3,1)** is the candidate source of the left/right asymmetry. The doublet-vs-singlet split *is* the chirality split. This is where the #418 derivation will be hardest and most decisive.

## 4. Hypercharges — anomaly-constrained (verified anomaly-free)

All four gauge-anomaly conditions cancel for the 15 = N_c·n_C content (Toy 4100):

| condition | value |
|---|---|
| SU(3)²·U(1): 2Y_Q − Y_u − Y_d | 0 |
| SU(2)²·U(1): 3Y_Q + Y_L | 0 |
| U(1)³: Σ Y³ | 0 |
| grav·U(1): Σ Y | 0 |

Given the reps, **anomaly cancellation fixes the hypercharges up to normalization** — so Y is not a free per-field dial. The substrate must produce anomaly-free Y; if it produces the reps + chirality, the anomaly constraint does much of the rest.

## 5. Load-bearing — #418 secures three pieces of the reduction (Grace)

- **(a) Running band B.** The reps + Y give b₂ = −19/6 and b₁ = −41/10 (Toy 4099; b₃ = g from 4090) → the running of α_s and sin²θ_W. #418 closes Band B's first step.
- **(b) Forced mixing.** The SU(2) doublet L = (ν, e)_L is one object, so the charged-lepton and neutrino sectors share one frame by construction → CKM/PMNS are forced mismatches, no free angle (Toy 4096).
- **(c) Matter content / chirality.** #418 produces the fermion reps and the chiral doublet/singlet split themselves — the existence and structure of matter.

One program, three pieces — which is why it's the right second front.

## 6. Substrate-natural now vs. must-be-forced

| Substrate-natural (verified) | Must be forced (Lyra's bulk-color derivation) |
|---|---|
| gauge group from the primaries | the chiral rep assignment (which fields are doublets vs singlets) |
| content count = N_c·n_C = 15 = dim SO(4,2) | the anomaly-consistent hypercharges |
| generation count rank+1 = 3 | the chirality projection itself (SO(5,2)→SO(4,2)) |
| content is anomaly-free | |
| the doublet as the mixing common-frame | |

## 7. The bar (Grace's input-count)

#418 *reduces* the parameter count iff the substrate **forces** the reps + chirality + Y from few inputs (vs. the SM taking them as given). The gauge group is near-forced (primaries); the content count is N_c·n_C; the reduction hinges on **forcing the chiral rep assignment and the (anomaly-constrained) hypercharges** from the substrate geometry. That forcing is the open derivation — and the chirality projection is its crux.

---

*The forcing is the next step (Lyra's bulk-color lane); this is the spec. Count: 2 of 26 — scoping the target does not move it. The decisive, hardest piece is the chirality (the SU(2)_L-on-left-only structure) from D_IV⁵'s holomorphic/Casey-#14 projection.*

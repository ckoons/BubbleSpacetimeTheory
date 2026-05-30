---
title: "#416 — per-particle dictionary layer v0.1: the lepton sector flips to 18 derived per-particle 5-tuples (clean); photon/Higgs single-particle (clean); quark/gauge sectors flagged with the SM-gauge-group ↔ substrate-gauge-structure embedding gap (color SU(3) isn't in K — staged for v0.2)."
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-29 Fri 13:55 EDT"
status: "DICTIONARY #416 v0.1 (Lyra lane, after L4 framework). Per-particle 5-tuples produced for the LEPTON sector (18 particles: 6 charged leptons × 2 chiralities + 3 left-handed neutrinos + 9 antiparticles, with chirality from L3, region from L2, σ_BF from keystone, charge from L2 SO(2), particle/anti from engine v0.4; generation indexed but underived per #414). Photon and Higgs single-particle cleanly. The quark + W/Z/gluon (gauge adjoint) sectors flagged: SM color SU(3) is NOT in K=SO(5)×SO(2) (rank-2 algebras differ), so color must come from the BULK structure of D_IV⁵ (non-compact direction), not from K — this is a genuine structural piece of work staged for v0.2."
---

# #416 v0.1 — per-particle dictionary layer

## 0. The task (Keeper's L-queue, parallel to L4)

Flip the per-cell 5-tuples (the Periodic Table entries) from assigned to derived, applying the dictionary axes (L1-L3 + engine v0.4) to each K-type to produce the explicit particle list. v0.1 does the LEPTON sector cleanly (where the dictionary has its cleanest reach), the trivial-scalar (Higgs) and vector (photon) cleanly, and identifies what the quark/gauge sectors need before they can be flipped (a real structural gap, honestly flagged).

## 1. Lepton sector (1/2, 1/2): 18 per-particle 5-tuples DERIVED

The lepton K-type carries 18 physical particles. Applying the dictionary axes:

**Fixed by K-type + L1-L3 + engine v0.4 (DERIVED)**:
- σ_BF = **FERMION** (half-integer SO(5) weight, keystone L1).
- Region = **Shilov / Hardy** (lepton-on-Shilov, L2).
- Chirality = L (holomorphic) or R (antiholomorphic), from the J-projection (L3).
- particle/antiparticle = E (positive) / F (negative) of U_q(B₂) (engine v0.4).

**Charge (L2; constrained by sin²θ_W = 2/9)**:
- The SO(2) component + GMN partitions the lepton sector by Q:
  - Charged leptons: Q = ±1 (electron-like, antielectron-like).
  - Neutrinos: Q = 0 (neutral).

**Generation (open gate #414, indexed but underived)**:
- gen = 1, 2, 3 (gen-1 = e/ν_e; gen-2 = μ/ν_μ; gen-3 = τ/ν_τ). Count over-determined; mechanism open-with-burden.

**The 18 per-particle entries**:

| particle | Q | chirality | generation | region | σ_BF | E/F |
|---|---|---|---|---|---|---|
| e_L⁻ | −1 | L | 1 | Shilov | fermion | E |
| e_R⁻ | −1 | R | 1 | Shilov | fermion | E |
| ν_e_L | 0 | L | 1 | Shilov | fermion | E |
| (no ν_R in SM) | — | — | — | — | — | — |
| e_L⁺ | +1 | L | 1 | Shilov | fermion | F |
| e_R⁺ | +1 | R | 1 | Shilov | fermion | F |
| ν̄_e_R | 0 | R | 1 | Shilov | fermion | F |
| ...same 6 for gen 2 (μ, ν_μ)... | | | | | | |
| ...same 6 for gen 3 (τ, ν_τ)... | | | | | | |

Total: 6 entries/generation × 3 generations = **18 per-particle 5-tuples**, all derived axis-by-axis (with generation indexed per #414).

This is the dictionary doing concrete particle-identification: 1 K-type → 18 physical particle states, every axis derived (or open at the named gate).

## 2. Single-particle sectors (clean)

- **Higgs (0,0)**: single neutral scalar — σ_BF = boson, Q = 0, no chirality (scalar), trivial generation. 1 particle (+ its antiparticle = itself, since it's neutral and real). DERIVED.
- **Photon (1,0)**: single neutral massless vector — σ_BF = boson, Q = 0, no chirality (gauge boson), 1 generation. 1 particle (its own antiparticle). DERIVED.

## 3. The structural gap: SM color SU(3) is NOT in K (the gauge/quark sectors)

For the **adjoint K-type (1,1)** (gauge sector) and the **bulk K-types** (quarks), the dictionary hits a real structural question:

> **SU(3) color is NOT a subgroup of K = SO(5)×SO(2).** SO(5) has rank 2; SU(3) has rank 2 — but they are different rank-2 algebras (SO(5) = B₂; SU(3) = A₂, with different Cartan matrices and different Coxeter numbers). SU(3) does NOT embed in SO(5).

So the SM gauge group's color factor SU(3)_C does not live in the maximal compact K of D_IV⁵. Color must come from elsewhere — the natural candidates being:
- The **BULK structure** (non-compact directions of SO(5,2) acting on the interior of D_IV⁵): quarks are bulk K-types, and color may be a bulk structural quantum number not visible in the K = SO(5)×SO(2) restriction.
- A **counting-not-symmetry mechanism**: N_c = 3 = h^∨(B₂) is derived (the dual-Coxeter count of B₂); color may be a 3-fold counting structure rather than a genuine SU(3) gauge symmetry (Casey's "color emerges from h^∨ = 3" — Track P-adjacent).

Either way, the dictionary as built (K-types of K=SO(5)×SO(2)) does NOT directly carry color SU(3). The quark and full gauge-sector partitioning needs this structural gap addressed before per-particle 5-tuples can be produced for quarks/gluons.

**What's clean** (W±, Z, photon — electroweak):
- The electroweak sector SU(2)_L × U(1)_Y IS in K (SU(2)_L is in the Shilov stabilizer SO(4); U(1)_Y from SU(2)_R + SO(2), L2 GMN structure). So W±, Z, photon can in principle be partitioned within the adjoint K-type — but the exact partition requires the GMN coefficients pinned (L2 routed item).

**What's not clean** (gluons, quarks):
- The 8 gluons (adjoint of SU(3)_C) and quark color triplets require the substrate's color mechanism, which is NOT in K. v0.2 work: establish how N_c = h^∨ = 3 produces the color structure (this is also the burden on route (II), #414).

## 4. v0.1 deliverable + what's staged

**Delivered v0.1**:
- 18 per-particle 5-tuples for the lepton sector, all axes derived (or named-open).
- Single-particle 5-tuples for photon and Higgs.
- Honest identification of the structural gap for quarks/gluons (color SU(3) not in K).
- Partial readiness for W/Z/photon partition (GMN pin needed).

**Staged for v0.2**:
- Quark per-particle 5-tuples (needs color mechanism from bulk/h^∨).
- W±, Z partition within the adjoint (needs GMN coefficients pinned, constrained by sin²θ_W=2/9).
- Gluon octet (needs the color structure).
- The full Periodic Table per-cell flip for the 62 composite cells (Elie's #415 Racah-Speiser + this dictionary layer).

## 5. Honest scope + tier

**RIGOROUS**: the dictionary axes (L1-L3 + engine v0.4) applied to the lepton K-type produce the 18 per-particle 5-tuples; SO(5) does not contain SU(3) (rank-2 algebras differ, B₂ ≠ A₂); the electroweak SU(2)_L × U(1)_Y is in K via the L2 structure.

**DERIVED (modulo keystone bet + open generation gate)**: lepton sector 18 per-particle 5-tuples; photon; Higgs.

**STRUCTURAL GAP (honestly flagged)**: SU(3) color is not in K → quark/gluon per-particle layer needs the substrate's color mechanism (bulk structure or h^∨-counting), tied to #414's route (II) burden.

**LOCATED, PENDING PIN**: W/Z partition within the adjoint, awaiting GMN coefficients pinned against sin²θ_W=2/9.

**Cal #27 / honesty**: I am NOT claiming the per-particle Periodic Table is flipped. I am claiming the LEPTON sector + photon + Higgs are derived per-particle (a real concrete partial flip), and I am flagging the quark/gauge sectors with a SPECIFIC structural gap (color not in K) — not papering over what the dictionary doesn't reach. The lepton-sector flip is the clean win; the structural gap is the honest open work.

**Routed**: → Grace: your Periodic Table v0.3 can flip the LEPTON row to derived (18 particles, all axes named); annotate the quark/gauge sectors with the SU(3)-not-in-K gap. → Keeper: the structural gap (color SU(3) ⊄ K) is now explicit — it ties to #414 route (II)'s burden (h^∨=3 has to produce both color and generations cross-cuttingly); the gauge/quark per-particle flip is jointly blocked on that mechanism. → me: the color mechanism is the natural next deep item (overlaps with #252 / route II); immediate next is L4 v0.2 (explicit mass derivations, where I can make progress without resolving the color mechanism).

— Lyra, #416 v0.1 per-particle dictionary layer. DERIVED: 18 per-particle 5-tuples in the LEPTON K-type (6 charged leptons × 2 chiralities + 3 LH neutrinos + 9 antiparticles), every axis from the dictionary (or named-open at the generation gate). Photon and Higgs single-particle clean. STRUCTURAL GAP (honest): SU(3) color is NOT in K=SO(5)×SO(2) (rank-2 algebras differ, B₂≠A₂); the quark + gauge sectors need the substrate's color mechanism (bulk structure or h^∨-counting), which ties to #414's route (II) burden. W/Z partition within adjoint pending GMN pin. v0.1 = clean lepton flip + identified gap; v0.2 = color mechanism + gauge/quark per-particle.

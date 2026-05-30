---
title: "Substrate Hall-algebra engine v0.4 — the negative part (antimatter) via the Drinfeld double; engine complete (4/4); + honest cyclotomic cross-check status"
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-29 Fri 10:26 EDT"
status: "ENGINE THEORY v0.4 (Lyra lane, Phase I step 4/4 — ENGINE STRUCTURE COMPLETE). Negative part (F-generators) = antiparticles; full U_q(B_2) = particles + antiparticles + conserved charges. Baryogenesis gets its algebraic home. + honest cyclotomic cross-check status (count forced, value-correspondence is separate). Engine structure done; explicit computations + Phase-2 dictionary remain."
---

# Engine v0.4 — negative part (antimatter); engine structure complete

## 0. Completing the engine

Engine lane: step 1 (coproduct = fusion/decay vertices) → step 2 (canonical basis = elementary particles + ladder) → step 3 (R-matrix = scattering) → **step 4 (negative part = antimatter)**. This completes the ENGINE STRUCTURE — the four pieces that make the substrate Hall algebra a full process-engine.

## 1. The negative part (rigorous, standard)

The full quantum group has the triangular decomposition:

  U_q(B_2) = U_q^+ ⊗ U_q^0 ⊗ U_q^-

- **U_q^+ (E_i, the Hall algebra)** = PARTICLES (modules/representations — what steps 1-3 built).
- **U_q^- (F_i, the dual Hall algebra)** = ANTIPARTICLES.
- **U_q^0 (K_i, the Cartan)** = the CONSERVED CHARGES (the grading — the quantum numbers).

The Drinfeld double construction builds U_q(B_2) from the Hall algebra U_q^+ and its dual U_q^-, with the Hopf pairing ⟨E_i, F_j⟩ = δ_{ij}/(q_i − q_i^{−1}) (q = 2 substrate-natural). So the negative part is not new input — it is the canonical dual of the Hall algebra we already have.

## 2. The physical dictionary (engine step 4)

| Structure | Physical role |
|---|---|
| U_q^+ (E_i) — positive part | particles |
| U_q^- (F_i) — negative part | **antiparticles** |
| U_q^0 (K_i) — Cartan grading | conserved charges / quantum numbers |
| bar involution / antipode (E ↔ F) | **CPT** (the substrate's particle↔antiparticle conjugation) |
| Hopf pairing ⟨E_i, F_j⟩ | particle-antiparticle annihilation amplitude |
| E↔F sector asymmetry | **baryogenesis** (matter-antimatter asymmetry) algebraic home |

**Antimatter is now in the engine**: it is the negative part of the Drinfeld double, the canonical dual of the particle (Hall) algebra. CPT is the bar/antipode symmetry relating E and F.

## 3. Baryogenesis gets an algebraic home

Matter-antimatter asymmetry (baryogenesis) requires CP violation + the Sakharov conditions. In the engine:
- The E↔F duality is exact at the symmetric point (matter = antimatter).
- Baryogenesis = a substrate-level ASYMMETRY between the E (particle) and F (antiparticle) sectors — a CP-violating difference in the structure constants or the pairing.
- This connects to the CKM/PMNS CP phases (we have the mixing angles; the CP phase is where the E/F asymmetry would live).

Honest: this LOCATES baryogenesis (it's the E/F sector asymmetry) but does not yet DERIVE the asymmetry magnitude — that needs the explicit CP structure (Phase 2+). The algebraic home is the deliverable; the magnitude is downstream.

## 4. Engine structure complete (4/4) — what's done, what remains

**ENGINE STRUCTURE COMPLETE** (the four pieces):
1. Multiplication + Green coproduct = fusion/decay vertices ✓
2. Canonical/crystal basis = elementary particles + state ladder (Lusztig positivity = they count) ✓
3. R-matrix = scattering S-matrix + braiding statistics ✓
4. Negative part = antiparticles + CPT + baryogenesis home ✓

This is Goal 1's STRUCTURE: the substrate Hall algebra is a full quasi-triangular Hopf algebra (Drinfeld double) — particles, antiparticles, vertices, scattering, conservation, statistics, CPT — all in one object.

**What remains (explicit + physical)**:
- The EXPLICIT structure constants / R-matrix entries / canonical basis at all weights (Elie's reaction table #405 + multi-week computation).
- The affine extension throughout (the generation tower — tubes/imaginary roots).
- **The Phase-2 A_sub↔H(Q_B2) dictionary** — the gate that maps the algebra's structures onto the PHYSICAL 5-tuple coordinates (region/σ_BF/chirality/charge). Until this lands, the physical IDENTIFICATIONS (which E = which particle) are the bet.

## 5. Honest cyclotomic cross-check status (per Keeper — kept alive)

Keeper: keep the cyclotomic generation route alive (it carries generations if the tube number pins ≠3). Honest status of the cross-check:

- **|Φ⁺(B_2)| = 4 is a FORCED root-count** (no theorem-scope issue, unlike the tubes). The chain length is also 4 → the COUNT matches, and the count is forced.
- **BUT** the chain VALUES {rank,N_c,n_C,g} = {2,3,5,7} = first 4 primes are INTEGERS, not the root vectors {α_1, α_2, α_1+α_2, 2α_1+α_2}. So the value-correspondence is a SEPARATE (Mersenne/cyclotomic) fact, NOT a bijection chain↔roots.
- **Honest conclusion**: the cyclotomic route's robust forced ingredient is the COUNT (|Φ⁺|=4); generations = |Φ⁺|−1 = 3 via base/seed (Gate 1). This is cleaner than the tube route (|Φ⁺|=4 is forced; the tube number is not) — BUT the full forcing still needs the structural link "why the substrate commitment chain has exactly |Φ⁺(B_2)| levels." The count match is forced; the mechanism link is the remaining open piece.

So generation-forcing remains OPEN, with the cyclotomic |Φ⁺|−1 route the better-footed candidate (forced count) — and the tube route the rep-theoretic test (Dlab-Ringel pin) that could either reinforce or break. Neither is closed; both matched. No "generations forced" headline (per #407 v0.2).

## 6. Honest scope + tier

**RIGOROUS (standard)**: triangular decomposition U_q(B_2) = U_q^+ ⊗ U_q^0 ⊗ U_q^-; Drinfeld double; Hopf pairing; bar/antipode; |Φ⁺(B_2)|=4.

**FRAMEWORK (the bet)**: F = antiparticles, E↔F asymmetry = baryogenesis, Cartan grading = physical conserved charges — all ride on the Phase-2 A_sub↔H dictionary for the physical identification.

**ENGINE STRUCTURE COMPLETE; EXPLICIT + PHYSICAL pending**: the four-piece structure is in place (Goal 1 structurally); the explicit entries (Elie) + the physical 5-tuple dictionary (Phase 2) are the remaining work to make the dynamics (Goal 2) concrete.

**Cal #27 / honesty**: "engine structure complete" is a STRUCTURE claim (the four algebraic pieces exist), NOT "the SM dynamics are derived." The physical identifications are the bet, earned via the dictionary + E0/reaction-table + the generation-forcing resolution. I'm stating the structure is complete and the physics is the bet — not conflating them.

**Next (my lane)**: Phase 2 — the A_sub↔H(Q_B2) dictionary (the gate that converts the physical 5-tuple cells to derived; the single highest-leverage remaining item — it's what turns "engine structure" into "physical model"). Plus support Elie's reaction table (#405) with the engine structure.

— Lyra, Engine v0.4 negative part / antimatter filed — ENGINE STRUCTURE COMPLETE (4/4). Negative part (F) = antiparticles; full U_q(B_2) = particles + antiparticles + conserved charges + CPT (bar/antipode); baryogenesis = E↔F asymmetry (algebraic home). Goal 1 structurally complete: the substrate Hall algebra is a full quasi-triangular Hopf algebra with vertices/ladder/scattering/statistics/CPT in one object. Cyclotomic cross-check (honest): |Φ⁺(B_2)|=4 forced (count), value-correspondence separate; generation-forcing still OPEN, cyclotomic |Φ⁺|−1 better-footed than tubes. Remaining: explicit entries (Elie) + Phase-2 A_sub↔H dictionary (the physical-identification gate). Next: the dictionary.

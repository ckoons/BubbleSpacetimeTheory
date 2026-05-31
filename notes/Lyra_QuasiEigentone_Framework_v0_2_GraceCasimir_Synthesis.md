---
title: "Quasi-Eigentone Framework v0.2 — synthesis of Grace intermediate-Casimir {0,4,6} prediction + Elie bulk radial towers (Toy 3627) + L4 v0.2 T190 tension. Refines v0.1 with specific channel→Casimir labels; addresses the T190 exponent tension by proposing Gen-2 = ADJOINT-channel (not vector); decay-rate framework now has explicit kernel-integral target."
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-30 Saturday 10:42 EDT (date-verified)"
status: "QUASI-EIGENTONE v0.2 (synthesis update). Absorbs Grace 1.5 Pair α prediction (spinor³ intermediate Casimirs {0, 4=rank², 6=C_2}) + Elie Toy 3627 three radial towers + L4 v0.2 T190 exponent tension. Refines v0.1 channel→generation mapping: Gen-2 may be ADJOINT-channel (C_int=6=C_2), not vector-channel (C_int=4), based on T190 exponent C_2=6. Decay-rate framework now has explicit target: derive T190's (rank³·N_c/π²)^{C_2} from quasi-eigentone overlap × kernel-integral on the adjoint channel."
---

# Quasi-Eigentone Framework v0.2 — Grace + Elie + L4 synthesis

## 0. What v0.2 absorbs

v0.1 (Saturday earlier) gave the structural distinction (true vs quasi vs confined eigentone) and the decay mechanism (Green coproduct + grading conservation). v0.2 absorbs three pieces that landed today:

1. **Grace 1.5 Two-Structures Pair α prediction**: spinor³ multiplicity-3 (Elie E7) via three channels with intermediate Casimirs {0, 4=rank², 6=C_2}. Proposed mapping: Gen 1 = trivial-channel; Gen 2 = vector-channel; Gen 3 = adjoint-channel.

2. **Elie Toy 3627 bulk radial towers** (closed-form Casimirs):
   - Vector tower V_(k,0): C = k(k+3) → 0, 4, 10, 18.
   - Adjoint tower V_(k,k) = V_(0,2k): C = 2k(k+2) → 0, 6, 16, 30.
   - Spinor tower V_(k+1/2,k+1/2) = V_(0,2k+1): C = (k+1/2)(2k+5) → 5/2, 21/2, 45/2, 77/2.

3. **My L4 v0.2 tension finding**: T190 m_μ/m_e = (24/π²)^{C_2=6} has exponent 6 = adjoint Casimir; per Grace's mapping this is "gen-3 channel" but T190 is gen-1→gen-2 ratio. Tension flagged.

## 1. Resolving the Grace-T190 tension

T190's exponent C_2 = 6 corresponds to Grace's "adjoint channel" (intermediate Casimir 6). The natural resolutions:

### Resolution A — Gen-2 IS the adjoint-channel (reorder Grace's mapping)

Mass hierarchy says m_μ ≫ m_e, m_τ ≫ m_μ. The "ascending intermediate Casimir" intuition is:
- Gen 1 = trivial channel (C_int = 0): ground state, low mass.
- Gen 2 = adjoint channel (C_int = 6 = C_2): higher excitation, more mass.
- Gen 3 = vector channel (C_int = 4 = rank²): yet different excitation pattern.

But this gives Gen 3 LOWER intermediate Casimir than Gen 2 — counterintuitive.

### Resolution B — The "channel" is not directly the mass scale; it's the GAUGE MEDIATOR

T190's exponent C_2 = 6 is the **adjoint Casimir of the GAUGE SECTOR mediating the e→μ transition** — NOT the intermediate Casimir of the spinor³ decomposition. In this reading:
- Grace's {0, 4, 6} intermediate Casimirs are STRUCTURAL labels of the three channels (not direct mass parameters).
- T190's 6 is the gauge-mediator Casimir (the adjoint of so(5) governing the weak-interaction-like transition between generations).
- The two are STRUCTURALLY RELATED (both = C_2 = 6) but play different roles.

**Resolution B is cleaner**: T190's exponent and Grace's prediction are both substrate-natural but address different aspects of the gen-2 sector.

### Resolution C — The mapping is generation = vector-channel for Gen 2, but the EXPONENT in T190 comes from elsewhere

Possibly the exponent 6 in T190 = (something else) × something with C_2 in it. Multi-week to disentangle.

**Working hypothesis (v0.2)**: Resolution B — Grace's intermediate-Casimir prediction labels the SPINOR³ DECOMPOSITION channels; T190's exponent is the GAUGE-MEDIATOR Casimir of the e→μ transition. Both involve C_2 = 6 but for different structural reasons.

## 2. Refined quasi-eigentone decay mechanism (v0.2)

With Elie's three bulk towers + Grace's channel structure + L4 closed-form anchor, the decay mechanism is:

**Quasi-eigentone Q (excited K-type) decays via:**
1. **Green coproduct**: Δ(Q) = Σ_{channels} (allowed lower K-type pairs) with grading conservation (Q, B, L).
2. **Channel structure**: the spinor³ multiplicity-3 organizes the 3 lepton generations; each generation's coproduct decomposition goes through a specific bosonic intermediate (trivial/vector/adjoint per Grace).
3. **Decay rate**: |overlap|² × kernel-integral × phase-space.
   - **Overlap** = Green coproduct coefficient (structural, integer-Mersenne for substrate Hall algebra).
   - **Kernel-integral** = Bergman kernel matrix element between initial K-type and decay-product K-types, evaluated at the bulk radial tower level (Elie Toy 3627 Casimirs).
   - **Phase-space** = standard particle-physics phase space, kinematics.
4. **Substrate-primary structure**: the closed-form decay rate emerges as (substrate-primary)^{gauge-mediator-Casimir} × kernel-integral residue.

This is the v0.2 mechanism — same skeleton as v0.1 but with explicit channel/Casimir structure now identified.

## 3. The concrete L4 v0.2 derivation target

The v0.1+v0.2 framework predicts T190 m_μ/m_e = (24/π²)^{C_2} from:
- **Base (24/π²)** = rank³·N_c / π² = (kernel-integral-derived substrate-natural ratio for the e→μ overlap).
- **Exponent C_2 = 6** = gauge-mediator adjoint Casimir.
- The exact closed form emerges from kernel-integral computation on the adjoint channel of the spinor³ decomposition.

**Multi-week explicit derivation** (Elie's lane after affine pin ratification):
1. Compute the Bergman kernel integral ⟨V_(1/2,1/2)_gen1 | adjoint-channel-mediator | V_(1/2,1/2)_gen2⟩ at the substrate's Hardy/Bergman structure.
2. Show this integral evaluates to (rank³·N_c/π²)^{C_2} via substrate-natural normalizations.
3. Repeat for m_τ/m_μ (T2003 49·71 = g²·71 — need 71 substrate-natural identification).

## 4. Updated SM particle classification (v0.2, refined)

The v0.1 classification table stands; v0.2 refines the lepton sector with channel structure:

| Particle | K-type | Channel (Grace) | Quasi-mechanism |
|---|---|---|---|
| electron | V_(1/2,1/2) gen-1 | trivial-channel (C_int=0) | TRUE eigentone (lowest) |
| muon | V_(1/2,1/2) gen-2 | **adjoint-channel (C_int=6=C_2)** per Resolution B | QUASI; coproduct via adjoint mediator |
| tau | V_(1/2,1/2) gen-3 | vector-channel (C_int=4) per Resolution B | QUASI; coproduct via vector mediator |

OR Grace's original (Resolution A would reorder):

| Particle | Channel (Grace original) |
|---|---|
| electron | trivial-channel (C_int=0) |
| muon | vector-channel (C_int=4) |
| tau | adjoint-channel (C_int=6) |

Both orderings are consistent with the spinor³ = trivial+vector+adjoint structure; the e→μ→τ mass hierarchy alone doesn't pin which mapping. v0.2 leans **Resolution B** based on T190's exponent matching C_2 = 6 = adjoint, suggesting muon's transition is mediated by the adjoint channel.

Honest: this mapping is INTERNAL to the v0.2 framework; experimental observables (decay branching ratios, CP phases) would pin which mapping is correct.

## 5. Honest scope + tier

**RIGOROUS** (Saturday-team work):
- Grace's intermediate Casimirs {0, 4, 6} (Pair α prediction; rep-theoretic).
- Elie's three bulk radial tower Casimirs (Toy 3627, closed forms).
- T190 closed form = (24/π²)^{C_2} (existing BST, anchor).

**SYNTHESIS (v0.2)**: connects three pieces; identifies and proposes resolution to Grace-T190 tension (Resolution B: T190 exponent is gauge-mediator Casimir, not direct intermediate Casimir); refines decay mechanism with explicit channel structure.

**OPEN (multi-week)**:
- Kernel-integral computation deriving T190 closed form explicitly (Elie's lane).
- Definitive disambiguation of Grace's mapping (Resolution A vs B) via experimental observables.
- Generalization to T2003 (m_τ/m_e closed form) and beyond.

**Cal #27 / honesty**: v0.2 is SYNTHESIS, not new derivation. Grace's prediction + Elie's towers + my tension finding combine into a refined framework with explicit Resolution B proposal. Multi-week kernel-integral work for actual derivation. The Resolution A vs B disambiguation may need experimental input.

**Routed**: → Grace: Resolution B proposes Gen-2 = adjoint-channel (your original was vector-channel). Reconsider Pair α mapping with T190 exponent constraint. → Elie: kernel-integral computation deriving T190 closed form from adjoint channel of spinor³ is in your command lane (multi-week). → Keeper: v0.2 framework + Grace-T190 tension productive synthesis. → me: queue continues — next v0.2 candidate is Spectral Score v0.2 (absorbing today's tower data).

— Lyra, Quasi-Eigentone Framework v0.2. Synthesis of Grace Pair α {0,4,6} + Elie Toy 3627 radial towers + L4 v0.2 T190 tension. Proposed RESOLUTION B for the tension: T190 exponent C_2=6 is the GAUGE-MEDIATOR Casimir (adjoint of so(5)), not the direct intermediate-channel Casimir; Grace's {0,4,6} labels the spinor³ decomposition channels (structural labels), and the gauge mediator is what enters the closed-form mass formula. Refined decay mechanism: quasi-eigentone overlap × kernel-integral on the relevant channel × phase-space. Explicit derivation of T190 from substrate kernel-integrals = multi-week target.

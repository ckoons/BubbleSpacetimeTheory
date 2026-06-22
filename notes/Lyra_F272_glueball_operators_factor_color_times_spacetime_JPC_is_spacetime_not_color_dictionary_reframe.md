---
title: "F272 — rep-theory classification of the quarkless glueball operator-assemblies (Lyra's part of Casey's operator reframe), and it REFRAMES the dictionary in linear algebra. The glueball operators are quartic-in-fundamentals (bilinear-of-bilinear) operators on H²(D_IV⁵), and as a linear-algebra object each FACTORIZES: Operator = (su(3)-invariant COLOR part) ⊗ (Lorentz×Hodge SPACETIME part). VERIFIED (Gell-Mann computation): (1) su(3) has exactly TWO Casimirs (rank 2) — the quadratic C_2 (Tr) and the cubic C_3 (symmetric d^{abc}); the cubic exists ONLY for SU(N≥3) (SU(2) has none) — a genuine SU(3) marker. (2) The antisymmetric cubic f^{abc}T_aT_bT_c reduces to the QUADRATIC Casimir (∝ C_2, computed: ratio 3/2·i·𝟙), NOT independent. (3) DECISIVE: the J^PC channel split is NOT a color (f-vs-d) distinction — the COLOR part is the SAME quadratic trace Tr(F·F) for 0⁺⁺/0⁻⁺/2⁺⁺; the split lives entirely in the SPACETIME (Lorentz × Hodge-*) structure: 0⁺⁺ = Tr(F²) scalar (self-dual); 0⁻⁺ = Tr(F·F̃) pseudoscalar (anti-self-dual, via the Hodge dual ε-tensor — NOT f^{abc}, correcting my conversational first-pass); 2⁺⁺ = Tr(F_μα F_ν^α) symmetric-traceless (stress tensor); 1⁺⁻ = Tr(F[D,F]) which needs a DERIVATIVE D_μ (bulk transport). CONSEQUENCE — the dictionary reframe: the cross-channel mass operator is BLOCK-DIAGONAL in the color⊗spacetime factorization; the color block is a scalar (C_2, common to all channels = the floor), and ALL the channel structure lives in the SPACETIME block (the operator's conformal dimension Δ via its Lorentz×Hodge rep). So computing per-channel color SO(7) towers (Sunday) was the wrong object — the channels SHARE color (C_2) and differ by SPACETIME Δ. The mass = color-floor(C_2) + spacetime-operator-dimension(Δ_channel). CLASSES: Class A/B (substrate-natural pure-quartic assemblies, differ only by spacetime tensor): 0⁺⁺ (lowest Δ, Tr F² = the Casimir density — the one clean closure), 0⁻⁺ (Tr F F̃, Hodge-dual), 2⁺⁺ (stress tensor); Class C (derivative-transport, mixes color with bulk position): 1⁺⁻ — genuinely different, may not be a pure quarkless assembly. Connects to Casey's energy-threshold/dump picture: Δ = activation threshold; 0⁺⁺ lowest (most observable before dumping); higher-Δ channels activate higher and dump faster; 1⁺⁻ (Class C transport) is the odd one out. TIER: factorization + J^PC=spacetime + f→C_2 + su(3) two-Casimirs = SOLID (standard QFT + computed); the dictionary reframe (mass = color-floor + spacetime-Δ; class structure) = LEAD-substantive; hand to Elie: compute the SPACETIME operator dimensions Δ per channel on H² (the Lorentz×Hodge sector, NOT the color SO(7) tower)."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-22 Monday 11:05 EDT"
status: "v0.1 — rep-theory classification of glueball operator-assemblies (Casey reframe, Lyra part). Operator = COLOR ⊗ SPACETIME factorization. VERIFIED: su(3) two Casimirs (C_2 quadratic + C_3 cubic, cubic SU(3)-only); f^{abc} cubic reduces to C_2; J^PC split is SPACETIME (Lorentz×Hodge), NOT color (color = common Tr). Dictionary reframe: mass operator block-diagonal; color block = scalar C_2 floor (common); ALL channel structure in SPACETIME block (Δ). Per-channel color SO(7) towers were the wrong object. Class A/B (0⁺⁺/0⁻⁺/2⁺⁺ pure quartic) vs Class C (1⁺⁻ derivative-transport). Hand to Elie: spacetime Δ per channel on H². Count HOLDS 4. For Elie, Grace, Casey, Cal, Keeper."
---

# F272 — the glueball operators factor as color ⊗ spacetime; the dictionary lives in the spacetime block

Casey's reframe: glueballs are quarkless, the "glue" is *built* (Elie's bilinear Schwinger su(3)), and we should look at the *operators* to see what quarkless assemblies are possible. My part — the rep-theory classification — and it reframes the dictionary problem in clean linear algebra.

## The linear-algebra structure: every glueball operator factorizes

The glueball operators are quartic-in-fundamentals (bilinear-of-bilinear) operators on H²(D_IV⁵), built from the bilinear-Schwinger gluon T^a = a_i† T^a_{ij} a_j. As a linear-algebra object, each one **factorizes**:

  **Operator = (su(3)-invariant COLOR part) ⊗ (Lorentz × Hodge-* SPACETIME part).**

The cross-channel "mass operator" is therefore **block-diagonal** in this tensor factorization — and the two blocks play completely different roles.

## Verified (Gell-Mann computation)

1. **su(3) has exactly two Casimirs** (rank 2): the quadratic **C_2** (Tr) and the cubic **C_3** (symmetric d^{abc}). The cubic exists **only for SU(N ≥ 3)** — SU(2) has none — so C_3 is a genuine SU(3) marker (the anomaly/d-symbol).
2. The antisymmetric cubic **f^{abc} T_a T_b T_c reduces to the quadratic Casimir** (computed: ∝ (3/2)i·𝟙 = ∝ C_2), so it is **not** an independent invariant.
3. **Decisive:** the J^PC channel split is **not** a color (f-vs-d) distinction. The **color block is the same** quadratic trace Tr(F·F) for 0⁺⁺/0⁻⁺/2⁺⁺. The split lives entirely in the **spacetime block** (Lorentz × Hodge-*):

| channel | operator | color block | spacetime block |
|---|---|---|---|
| 0⁺⁺ | Tr(F²) | C_2 (quadratic) | scalar (self-dual) |
| 0⁻⁺ | Tr(F·F̃) | C_2 (quadratic) | pseudoscalar (**anti-self-dual**, via Hodge dual — *not* f^{abc}) |
| 2⁺⁺ | Tr(F_μα F_ν^α) | C_2 (quadratic) | symmetric-traceless (stress tensor) |
| 1⁺⁻ | Tr(F [D, F]) | C_2 | **needs a DERIVATIVE D_μ** (bulk transport) |

(This corrects my conversational first-pass, which mis-attributed 0⁻⁺ to an f^{abc} color contraction — the pseudoscalar is the *spacetime* Hodge dual, exactly Grace's self-dual/anti-self-dual split.)

## The dictionary reframe (the payoff)

Because the mass operator is block-diagonal:
- the **color block is a scalar** — the quadratic Casimir **C_2 = 6, common to all channels** = the **floor** (and the proton sits here too, on the *compact* C_2 = 6 reading, consistent with Grace's Monday retraction that the proton is compact);
- **all the channel structure lives in the spacetime block** — the operator's conformal dimension Δ, set by its **Lorentz × Hodge-*** representation.

So **the per-channel color SO(7) towers we computed Sunday were the wrong object** — the channels *share* color (C_2) and differ by *spacetime* Δ. The dictionary is:

  **mass(channel) = [color floor C_2] ⊕ [spacetime operator dimension Δ_channel],**

with Δ_channel determined by the Lorentz×Hodge rep, not the color tower. This is why five color-based assemblies failed: they varied the wrong block.

## The operator-assembly classes (Casey's classification, made precise)

- **Class A/B — substrate-natural pure-quartic assemblies** (color = C_2, differ only by the spacetime tensor): **0⁺⁺** = Tr(F²), the *lowest-Δ* operator (the Casimir density itself) — the **one clean closure** (c_2 = 11); **0⁻⁺** = Tr(F·F̃) (Hodge-dual, higher Δ); **2⁺⁺** = stress tensor (higher Δ). These should differ by their *spacetime* Δ alone.
- **Class C — derivative-transport assembly**: **1⁺⁻** = Tr(F[D,F]) requires a bulk-position derivative, mixing color with spatial transport. **Not a pure quarkless assembly** — genuinely a different object (may be a Class-D lattice resonance without a clean substrate-natural counterpart).

## Connection to Casey's energy-threshold / dump picture

The spacetime operator dimension **Δ is the activation-energy threshold**: 0⁺⁺ (lowest Δ) activates first and is most observable before dumping; higher-Δ channels (0⁻⁺, 2⁺⁺) activate higher and radiate away faster; 1⁺⁻ (Class C transport) is the odd one. So "5-of-6 don't close on one color tower" is **expected** — they're different spacetime-Δ classes, not one tower, exactly as the quarkless-assembly picture predicts.

## Net (Result | Confidence | Next)

| Result | Confidence | Next |
|---|---|---|
| glueball operator = COLOR ⊗ SPACETIME factorization; mass operator block-diagonal | SOLID (standard QFT + computed) | — |
| J^PC split is SPACETIME (Lorentz×Hodge), color block = common C_2 | SOLID | — |
| su(3) two Casimirs (C_2, C_3 cubic SU(3)-only); f^{abc}→C_2 | SOLID (computed) | — |
| dictionary = color-floor(C_2) + spacetime-Δ; color towers were wrong block | LEAD-substantive | Elie: compute spacetime Δ per channel on H² |
| Class A/B (0⁺⁺/0⁻⁺/2⁺⁺ pure quartic) vs Class C (1⁺⁻ derivative) | LEAD-substantive | test which close at substrate-clean Δ |

**Count HOLDS 4 of 26.** SU(3) scope. The glueball operators factor color⊗spacetime; the channel mass-splitting lives in the SPACETIME block (Δ), not the color tower — so the dictionary reframe is to compute the spacetime operator dimensions, and the "non-closure" was varying the wrong block. INTERNAL.

@Elie — the bilinear-Schwinger machinery (4301) gives the color block (C_2, common). The NEW computation is the SPACETIME block: the operator dimension Δ for each Lorentz×Hodge structure (Tr F² scalar, Tr F F̃ anti-self-dual, T_μν sym-traceless, Tr F[D,F] derivative) on H²(D_IV⁵) — NOT the color SO(7) tower. The 1⁺⁻ derivative case is the one that may not be a pure quartic assembly (Class C). @Grace — this is why the per-channel color towers didn't close: the channels share color (C_2) and differ by spacetime Δ; your proton-is-compact finding fits (the color floor C_2 = 6 is the compact reading, common to proton + all glueballs). @Casey — your "look at the operators" reframe lands: glueballs factor into a common color Casimir (the C_2 floor) times a spacetime structure that carries the J^PC and the energy threshold; 0⁺⁺ is the lowest-threshold pure-Casimir assembly (the clean one), and 1⁺⁻ needs derivative-transport (not a pure quarkless assembly). @Cal — honest tiers: factorization + J^PC=spacetime + computed Casimir facts SOLID; the dictionary reframe + class structure LEAD-substantive, handed to Elie for the spacetime-Δ computation.

— Lyra, Mon 2026-06-22 11:05 EDT (date-verified). F272: glueball operators factor COLOR ⊗ SPACETIME. Verified (Gell-Mann): su(3) two Casimirs (C_2 + cubic C_3, SU(3)-only); f^{abc}T_aT_bT_c → C_2 (not independent); J^PC split is SPACETIME (Lorentz×Hodge), color block = common Tr (0⁺⁺ scalar / 0⁻⁺ Hodge-dual anti-self-dual / 2⁺⁺ stress tensor; 1⁺⁻ needs derivative D_μ). DICTIONARY REFRAME: mass operator block-diagonal; color block = scalar C_2 floor (common); ALL channel structure in SPACETIME block (Δ). Per-channel color SO(7) towers = wrong block. Class A/B (0⁺⁺/0⁻⁺/2⁺⁺ pure quartic) vs Class C (1⁺⁻ derivative-transport). Δ = energy threshold (Casey dump picture). Hand to Elie: spacetime Δ per channel on H². Count HOLDS 4.

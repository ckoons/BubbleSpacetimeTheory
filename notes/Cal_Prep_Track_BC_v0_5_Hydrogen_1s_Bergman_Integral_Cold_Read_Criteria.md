---
title: "Cal Cold-Read Criteria — Track BC v0.5+ hydrogen 1s explicit Bergman integral evaluation (Lyra)"
author: "Cal A. Brate (outside-voice prep)"
date: 2026-05-27 Wednesday ~10:50 EDT
status: "Prep document — written BEFORE Lyra v0.5+ lands; criteria fixed in advance"
purpose: "Cal cold-read criteria for Track BC v0.5+ explicit Bergman integral evaluation for hydrogen 1s ground state via substrate-Coulomb 1/r framework"
discipline: "Cal #27 STANDING + Cal #29 STANDING + Cal #126 FRAMEWORK-PLUS + Cal #133 partial-tautology"
companion: "Cal_Prep_Multi_Phase_Quiver + Cal_Prep_Track_DC_v0_3_K59 + Cal_Prep_Toy_3541_GF32 + Cal_Prep_Multi_Scale + Cal_Prep_P4 (all Wednesday morning)"
---

# Cal Prep — Track BC v0.5+ hydrogen 1s explicit Bergman integral cold-read

## Context

Track BC v0.4 (delivered Wednesday morning) provides Bergman integral asymptotic methodology FRAMEWORK. v0.5+ targets explicit hydrogen 1s ground state Bergman integral evaluation via substrate-Coulomb 1/r framework + α²-binding emergence.

Substrate-mechanism claim: substrate's 5-dim Hua-tube structure projects to 3D-Coulomb 1/r potential; α²-binding for hydrogen ground state emerges from Bergman kernel asymptotic evaluation.

## Background — standard mathematics

### Bergman kernel for D_IV⁵

For D_IV⁵ = Type IV bounded symmetric domain of dimension 5:
- Bergman kernel K(z, w̄) = c_FK · (1 − z·w̄)^(−g/rank) per T2442 RIGOROUSLY CLOSED
- c_FK · π^(9/2) = 225 (Faraut-Koranyi normalization, EXACT)
- Bergman exponent g/rank = 7/2 substrate-fixed

### Hydrogen ground state 1s

Standard QM:
- Bohr radius a_0 = ℏ² / (m_e · e²) = 4πε_0 ℏ² / (m_e e²)
- Ground state energy E_1s = -13.6 eV = -α² m_e c² / 2 = -m_e c²/2 · (1/137)²
- Wave function ψ_1s ∝ exp(-r/a_0)
- Binding energy scales as α² · m_e c²

### Substrate-Coulomb 1/r via Bergman 3D-projection

Standard 5D → 3D dimensional reduction would project D_IV⁵ structure (5-dim Hua tube) to 3D Coulomb potential. Specifically:
- D_IV⁵ has rank 2 + complex dim n_C = 5
- 3D = n_C - 2 = 3 may be the "boundary" dimension after rank-2 projection
- Bergman integral over Hua-tube structure → 1/r potential in 3D projection (standard for symmetric domain analysis)

### α²-binding emergence

α = 1/137 = 1/N_max in BST. α² binding for hydrogen is standard QM:
- E_1s = -α² · m_e c² / 2
- Comes from balance of Coulomb attraction + kinetic energy via virial theorem

Substrate-mechanism claim: α² emerges from double-evaluation of substrate-α at Bergman 3D-projection level. Cold-read should check WHERE the α² structure comes from in substrate-mechanism (not just numerical match).

## Cold-read criteria — 10 questions for v0.5+

### Q1 — Bergman integral explicit form

- Does v0.5 give the explicit integral I(r) = ∫_{D_IV⁵} K(z, w̄) f(z) g(w) dz dw̄ for hydrogen 1s? What are f, g (the ground state functions on substrate)?
- Convergence verified? Bergman kernel is integrable over the unit ball; verify in v0.5.
- Limits of integration: over D_IV⁵ entire, or restricted to a specific Hua-tube slice?

### Q2 — Hua-tube 5-to-3 dimensional reduction

- Explicit dimensional reduction: 5-dim → 3-dim via what projection? Rank-2 reduction? Specific Hua-tube slice?
- Reduction must produce 1/r potential, not just generic 3D form. The 1/r specific form is load-bearing.
- **Cal #29 audit**: was the projection chosen to produce 1/r (back-fit), or substrate-forced?

### Q3 — α²-binding via double-α

- Where does α² (not α) emerge?
- "Double-α emergence" needs explicit derivation chain: α appears at step X via mechanism, then squared at step Y via mechanism, producing α² in observable
- Most natural: α appears once in coupling (e² in Coulomb), once in dimensional structure (Bergman exponent or normalization), squaring in binding energy
- **Cal #27 audit**: forward derivation chain α → α² → E_1s, or identification (chosen to make α² match)?

### Q4 — Connection to T2442 Bergman kernel RIGOROUSLY CLOSED

T2442 establishes c_FK · π^(9/2) = 225 EXACT. v0.5 should LEVERAGE T2442 not redefine. Specifically:
- Bergman kernel evaluation uses T2442 c_FK formula
- π^(9/2) factor enters integral evaluation
- 225 = (N_c·n_C)² appears as substrate-natural normalization

If v0.5 introduces NEW Bergman normalization, structural-confusion risk.

### Q5 — Cal #122 typing

Track BC framework typing:
- **Type A (Level 1 geometric)**: D_IV⁵ Hua-tube structure → 3D Coulomb via geometric projection
- **Type B (Level 4 algebraic)**: Bergman integral as algebraic identity matching hydrogen 1s
- **Type C (level-crossing)**: geometric projection + algebraic Bergman + operational hydrogen observable

**Cal default expectation**: Type C. The Bergman 3D-projection bridges geometric structure ↔ algebraic kernel ↔ operational hydrogen observable.

### Q6 — Cal #29 question-shape audit

The hydrogen 1s binding energy is precisely known (-13.6 eV). v0.5 derivation should not be question-shaped to produce -13.6 eV. Substantive content:
- Derive expression for binding energy in terms of substrate quantities (a_0 substrate, α substrate, m_e substrate)
- THEN evaluate substrate quantities and check match to -13.6 eV
- BAD: design Bergman integral to produce -13.6 eV (back-fit)
- GOOD: substrate-mechanism specifies integral structure; evaluation matches

### Q7 — Cal #133 partial-tautology check

- Standard QM derives -13.6 eV via Schrödinger equation + Coulomb potential
- Substrate-Coulomb claim: substrate FORCES the 1/r form (rather than 1/r being assumed)
- Substrate-mechanism content: WHY does substrate produce 1/r and not 1/r² or other?
- Cal #133: the 1/r form is partial mathematical convention; substrate-specific content is in the 1/r FORCING mechanism

### Q8 — Mode 6 multi-decomposability check

Bohr radius a_0 = ℏ² / (m_e · e²) in SI; in natural units a_0 = 1 / (α m_e c). Multiple BST-primary expressions could match:
- a_0 = 1/(α m_e) in natural units; α = 1/N_max
- 1/N_max factor enters; N_max = 137 = N_c³·n_C + rank (definitional)
- Mode 6 Tier: Bohr radius value is observable-precision; structural identity is N_max-anchored
- Cal cold-read: explicit Mode 6 enumeration on a_0 BST-primary expressions

### Q9 — Predictive consequences beyond hydrogen 1s

v0.5+ should produce specific predictions beyond just hydrogen 1s ground state:
- Hydrogen 2s, 2p, etc. → α²/n² scaling (Rydberg formula). Does substrate-Bergman framework reproduce?
- Hydrogen fine structure → α⁴ corrections. Does substrate-Bergman extend?
- Helium / multi-electron atoms? Cal #136 σ_BF Bose-Fermi statistics + substrate-Bergman?

Without extending predictions, hydrogen 1s match is identification at one observable; FRAMEWORK-PLUS ceiling.

### Q10 — Substrate-mechanism closure at SVC tier

For SVC promotion:
1. **Explicit Bergman integral evaluation** to closed form
2. **Substrate-Coulomb 1/r derived** from substrate structure, not assumed
3. **α² emergence from double-α mechanism** explicitly derived
4. **T2442 connection** preserved (not redefined)
5. **Predictive consequences** beyond hydrogen 1s ground state energy

Without #5, SVC ceiling at FRAMEWORK-PLUS.

## Honest expectations

- **Most likely v0.5 disposition**: FRAMEWORK / FRAMEWORK-PLUS. Multi-week scope; v0.5 might produce closed-form Bergman integral evaluation; SVC tier requires predictive consequences extending hydrogen 2s+ + helium scope.
- **Most likely typing**: Type C per Cal #122.
- **Partial-tautology risk per Cal #133**: 1/r Coulomb is general physics; substrate-specific content is in the 1/r FORCING.
- **Mode 6 concern**: low for hydrogen specifically (Bohr radius via single dominant decomposition); higher for Rydberg / fine-structure extensions.

## What would change disposition

1. **Closed-form Bergman integral** evaluated explicitly (not just framework asymptotic)
2. **Substrate-Coulomb 1/r forced** from substrate (not assumed)
3. **α² emergence derived** via specific double-α chain
4. **Rydberg formula reproduced** for n>1 states
5. **Multi-electron extension** at framework level

## Cross-reference

- **Lyra Track BC v0.4 Bergman integral methodology** (Wednesday May 27 morning)
- **T2442 RIGOROUSLY CLOSED**: c_FK · π^(9/2) = 225 EXACT
- **Cal #122**: Type A/B/C tier-discipline
- **Cal #126**: FRAMEWORK-PLUS tier
- **Cal #27 / Cal #29 / Cal #133**: discipline frameworks
- **Cal_Methodology_Mode_6_Threshold_Formalization.md** (Cal, 2026-05-27 morning)
- **CLAUDE.md Bergman exp = g/rank = 7/2** standing reference

## Cal cadence note

Thirteenth Cal output Wednesday. Casey "keep pulling until blocked" engaged. Remaining own-menu pullable items: A_sub [Ŝ_i, Ŝ_j] prep doc; potentially P1 cross-CI matrix detailing; further outside-voice content.

After this pull, leverage on remaining menu items continues to diminish. Will assess block condition vs continue.

— Cal A. Brate, 2026-05-27 Wednesday ~10:50 EDT. Track BC v0.5+ hydrogen 1s Bergman integral cold-read criteria fixed in advance; standard QM background calibrated; substrate-mechanism vs identification distinguished at each cold-read question.

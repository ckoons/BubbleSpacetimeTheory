---
title: "F313 — P3 rep-theory seat (Lyra, Casey-approved pairing with Grace + Elie): the EXACT su(3)-closure criterion in linear algebra, sharpening what the explicit κ-computation must show. The color modes a_1,a_2,a_3 are the su(3) fundamental 3; the generators E_ij = a_i†a_j close into su(3) EXACTLY iff [a_i, a_j†] is color-central, i.e. color-SCALAR (∝ δ_ij). Write the curvature-corrected commutator [a_i, a_j†] = (leading 2n_C)δ_ij + M_ij; decompose the correction matrix M under su(3): 3⊗3̄ = 8 ⊕ 1, so M_ij = (1/3)Tr(M)δ_ij [SINGLET] + M̃_ij [OCTET, traceless]. EXACT-CLOSURE CRITERION: **M̃_ij = 0** — the OCTET (traceless) part of the curvature correction must vanish; the singlet part only renormalizes the decoupled u(1) and never touches the 8 traceless brackets. This sharpens Grace+Elie's explicit target from 'compute the whole κ-matrix' to 'compute its octet part and show it's zero' — one 8-component object, not the full matrix. WHERE M comes from: M_ij = the Bergman curvature tensor R contracted on the color triplet; M̃ = 0 ⟺ R restricted to the 3 color directions is su(3)-invariant. DUAL side (Grace, confirmed): R is so(7)-invariant, su(3) ⊂ g₂ ⊂ so(7) ⟹ R|triplet su(3)-invariant ⟹ M̃ = 0 ⟹ exact. DOMAIN side: R is so(5,2)-invariant and su(3) ⊄ so(5,2) (F258), so M̃ need NOT vanish a priori — the explicit octet M̃_ij is THE obstruction to compute, and M̃ = 0 ⟹ #418 SOLID on the domain. So the P3 explicit target is now sharp and minimal: the octet part of the κ-correction on the color triplet. This is the rep-theory seat done in linear algebra (Casey 'linear algebra'); the explicit κ-numerics stay Grace+Elie's lane, now with a precise pass/fail criterion (octet norm = 0). Count HOLDS 4."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-25 Thursday (date-verified)"
status: "v0.1 — P3 rep-theory seat (Casey-approved pairing). EXACT closure criterion: [a_i,a_j†] = 2n_C·δ_ij + M_ij; M decomposes 3⊗3̄ = 8⊕1; su(3) closes EXACTLY ⟺ OCTET part M̃_ij = 0 (singlet part only renormalizes the decoupled u(1)). Sharpens Grace+Elie's target to 'octet part of κ-correction = 0' (one 8-component object). M_ij = Bergman R on the triplet; M̃=0 ⟺ R|triplet su(3)-invariant — forced on the DUAL (so(7)-invariant), the explicit obstruction on the DOMAIN (so(5,2)⊉su(3), F258). M̃=0 ⟹ #418 SOLID on domain. Linear-algebra criterion; κ-numerics stay Grace+Elie. Count HOLDS 4. For Grace, Elie, Casey, Cal, Keeper."
---

# F313 — P3: the exact su(3)-closure criterion is "the octet part of the curvature correction vanishes"

Casey approved the P3 third seat and said "linear algebra." The seat's job is to give Grace and Elie the *exact closure criterion* in matrix terms, so the explicit κ-computation knows precisely what it must show — and it sharpens the target to one minimal object.

## The criterion

The color modes a_1, a_2, a_3 are the su(3) fundamental **3**; the generators E_ij = a_i† a_j. su(3) closes **exactly** —

  [E_ij, E_kl] = δ_jk E_il − δ_li E_kj —

iff [a_i, a_j†] is **color-central**, i.e. a color **scalar** (∝ δ_ij). Write the curvature-corrected commutator

  **[a_i, a_j†] = (leading 2n_C)·δ_ij + M_ij**,

and decompose the correction matrix M under su(3) (**3 ⊗ 3̄ = 8 ⊕ 1**):

  **M_ij = (1/3)Tr(M)·δ_ij  [SINGLET]  +  M̃_ij  [OCTET, traceless].**

  **EXACT-CLOSURE CRITERION:  M̃_ij = 0.**

The octet (traceless) part of the curvature correction must vanish. The singlet part (1/3)Tr(M) only renormalizes the decoupled u(1) — it never touches the eight traceless brackets. So the explicit target is **one 8-component object** (the octet), not the full matrix: compute M̃ and show its norm is zero.

## Where M comes from, and the dual/domain split

M_ij is the Bergman **curvature tensor R** contracted on the color triplet (the curvature correction to the CCR). Therefore

  **M̃ = 0  ⟺  R restricted to the 3 color directions is su(3)-invariant.**

- **Dual side (Grace, confirmed):** R is so(7)-invariant, and su(3) ⊂ g₂ ⊂ so(7), so R|triplet is su(3)-invariant ⟹ M̃ = 0 ⟹ exact closure. SOLID on the dual.
- **Domain side:** R is so(5,2)-invariant, and su(3) ⊄ so(5,2) (F258), so M̃ need **not** vanish a priori. The explicit octet M̃_ij is **the obstruction** to compute. **M̃ = 0 ⟹ #418 SOLID on the domain** (Cal's bar: explicit operator-realization, not just covariance).

## What this gives the pairing

The P3 explicit target is now sharp and minimal:

  **compute the octet part M̃_ij of the κ-correction on the color triplet; M̃ = 0 ⟹ su(3) closes exactly on the domain ⟹ #418 SOLID.**

Grace's structural forcing says M̃ *should* vanish (the correction is "color-singlet" because κ is geometric); this criterion turns that into a definite pass/fail computation — octet norm = 0 or not. The explicit κ-numerics remain Grace + Elie's lane; this is the rep-theory criterion they run against.

## Net (Result | Confidence | Next)

| Result | Confidence | Next |
|---|---|---|
| su(3) closes exactly ⟺ [a_i,a_j†] color-scalar ⟺ M̃ (octet) = 0 | SOLID (rep theory) | — |
| M decomposes 3⊗3̄ = 8⊕1; only the octet can break closure | SOLID | — |
| M̃ = 0 ⟺ R|triplet su(3)-invariant | SOLID | — |
| dual: so(7)-invariant ⟹ M̃ = 0 (exact) | SOLID (confirms Grace) | — |
| domain: so(5,2)⊉su(3) ⟹ M̃ is the explicit obstruction | the P3 target | Grace κ-matrix / Elie numerics: compute M̃, show = 0 → #418 SOLID |

**Count HOLDS 4 of 26.** INTERNAL. P3 rep-theory seat: the exact closure criterion is M̃ = 0 (octet part of the κ-correction vanishes) — sharpening the explicit target to one 8-component object, forced on the dual, the explicit obstruction on the domain.

@Grace — the seat's contribution, in linear algebra: su(3) closes exactly ⟺ the **octet** part M̃_ij of your κ-correction vanishes (M decomposes 3⊗3̄ = 8⊕1; the singlet just renormalizes the decoupled u(1)). So your explicit κ-matrix only needs its **traceless part** checked — M̃ = 0 is the whole pass/fail. Your structural forcing predicts M̃ = 0 because R is geometric; this is the definite computation that confirms it on the domain (where so(5,2)⊉su(3) makes it non-automatic). @Elie — the numerical target is sharp: compute M̃_ij (octet of the κ-correction), report ‖M̃‖. Zero ⟹ #418 SOLID on the domain. @Cal — this is the explicit-realization criterion for your SOLID bar, stated as one rep-theory condition (octet vanishes), not a covariance hand-wave. @Casey — P3 seat done in linear algebra: the whole question reduces to whether the octet (traceless) part of the curvature correction on the color triplet is zero — forced on the dual, the one explicit number-set Grace+Elie now compute on the domain.

— Lyra, Thu 2026-06-25 (date-verified). F313: P3 rep-theory seat. su(3) closes EXACTLY ⟺ the octet part M̃_ij of the curvature correction [a_i,a_j†] = 2n_C·δ_ij + M_ij vanishes (3⊗3̄ = 8⊕1; singlet only renormalizes the decoupled u(1)). M = Bergman R on the triplet; M̃=0 ⟺ R|triplet su(3)-invariant — forced on the DUAL (so(7)-invariant, su(3)⊂g₂⊂so(7)), the explicit obstruction on the DOMAIN (so(5,2)⊉su(3), F258). Sharpens the P3 target to one 8-component object; M̃=0 ⟹ #418 SOLID on domain. κ-numerics stay Grace+Elie. Count HOLDS 4.

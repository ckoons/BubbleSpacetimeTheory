---
title: "Affine-type pin v0.1 — B₂⁽¹⁾ vs C₂⁽¹⁾: substrate's natural affinization is B₂⁽¹⁾ (marks 1,1,2). Argument from keystone (K=SO(5)→ŝo(5)=B₂⁽¹⁾); both give same finite Serre coefficients ([2]₂=3, [3]₄=21) so the finite algebra is the same; the affine choice is Langlands-dual labeling, decided by 'which loop algebra is the substrate's spatial-symmetry one.'"
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-30 Saturday 09:45 EDT"
status: "PIN PROPOSAL v0.1 (P1.3, joint Lyra + Keeper + Elie). RECOMMENDATION: substrate affine is B₂⁽¹⁾ (marks 1,1,2; δ=α_0+α_1+2α_2; affine node single-bond to long end). Keeper-derived C₂⁽¹⁾ (marks 1,2,1) is the Langlands dual — same finite algebra (B₂≅C₂=so(5)=sp(4)), different affine labeling. Choice depends on substrate's natural realization; keystone K=SO(5) leans to B₂⁽¹⁾. Pending Keeper+Elie ratification."
---

# Affine-type pin — B₂⁽¹⁾ vs C₂⁽¹⁾

## 0. The question

E5 (Elie) failed because the wrong affine type was built (Ã₂ marks 1,1,1 instead of correct h=4). Keeper corrected with C₂⁽¹⁾ (marks 1,2,1) from "highest root of C₂ is θ = 2α_1 + α_2." My catch: B₂⁽¹⁾ (marks 1,1,2) is the alternate Langlands-dual affinization, naturally derived from B₂'s highest root α_1 + 2α_2. **Both sum to h=4. Which is the substrate's?**

## 1. Finite-algebra ambiguity (both work equally)

B₂ and C₂ are isomorphic as finite simple Lie algebras (both = so(5) = sp(4)). The choice between calling it "B₂" or "C₂" is purely a node-labeling convention. Elie's E0 + E9 verify the substrate Serre coefficients:
- Short root: [2]_{q^d_short} = [2]_2 = 3 = N_c (with d_short = 1)
- Long root: [3]_{q^d_long} = [3]_4 = 21 = N_c·g (with d_long = 2)

BOTH B₂ and C₂ conventions reproduce these (since they're the same algebra). The finite Serre relations cannot distinguish B₂ from C₂.

## 2. Affine ambiguity (Langlands-dual diagrams)

B₂⁽¹⁾ and C₂⁽¹⁾ are GENUINELY DIFFERENT affine algebras — Langlands dual:

| | diagram | marks (a_0, a_1, a_2) | δ | affine attachment |
|---|---|---|---|---|
| **B₂⁽¹⁾** | α_0 — α_1 ⇒ α_2 | (1, 1, 2) | α_0 + α_1 + 2α_2 | SINGLE bond to LONG end (α_1) |
| **C₂⁽¹⁾** | α_0 ⇒ α_1 ⇐ α_2 | (1, 2, 1) | α_0 + 2α_1 + α_2 | DOUBLE bond to SHORT end (α_1) |

Both have h = sum of marks = 4 ✓; both give h^∨ = 3 = N_c ✓; both have the doubling in δ on the SHORT root. Different node labeling (B₂: node 1 long, node 2 short; C₂: node 1 short, node 2 long), different affine attachment (B₂: single bond to long; C₂: double bond to short).

Their tube structures (the open #409 question) likely differ — this is part of why the count question is non-trivial.

## 3. The decisive argument (recommendation: B₂⁽¹⁾)

**The keystone (#408, K-audit PASS)** identifies K = SO(5) × SO(2) explicitly — the substrate's compact spatial symmetry is **SO(5)**, not Sp(4). While so(5) ≅ sp(4) as Lie algebras, the geometric realization on D_IV⁵ is SO(5)-natural (the maximal compact factor of SO_0(5,2) is SO(5)×SO(2), in the SO(5) presentation, not the Sp(4) presentation).

So the natural loop-algebra affinization is:

  **ŝo(5) = B₂⁽¹⁾, marks (1, 1, 2)**

C₂⁽¹⁾ would be the substrate's affine extension only if the geometric/Hall-algebra realization picks the Sp(4)/C_2 labeling — which it doesn't, per the keystone. The substrate's "affine direction" (the generation tower / imaginary-root extension) is naturally read off the SO(5) loop algebra.

## 4. Cross-checks (consistency, not independent confirmation)

- **Keeper's C₂⁽¹⁾ derivation is correct as math** — θ(C₂) = 2α_1 + α_2 in C-conventions IS the highest root. But this is the C-labeling. In the B-labeling (which the keystone uses), θ(B₂) = α_1 + 2α_2.
- **Both affines give h=4** — so the marks-sum criterion (Elie's E5 diagnostic for catching Ã₂) is satisfied by both. The pin is the labeling, not the sum.
- **Both give h^∨ = 3 = N_c** — so the dual-Coxeter color identification (route II) is unchanged.
- **The tube structure (#409) is affine-dependent** — different tube counts for B₂⁽¹⁾ vs C₂⁽¹⁾ possible. This is part of why #409 needs the right affine pinned BEFORE recomputing (Elie's E5 failure mode).

## 5. Implications for the open work

- **#409 tube count** (route I, currently secondary per #414 reframe): if Elie reattempts on B₂⁽¹⁾, the simply-laced prior Σ(rank−1) = V−2 still gives ≤2 for V=3, but the non-simply-laced VALUATION of B₂⁽¹⁾ specifically (single bond to long + double pointing to short) may differ from C₂⁽¹⁾'s. Both still likely lean ≤3, consistent with the gate disposition.
- **L4 v0.2 explicit lepton mass ratios**: Elie's bulk K-type radial tower for the spinor uses the affine δ-direction. For B₂⁽¹⁾, δ = α_0 + α_1 + 2α_2 with the doubling on α_2 (short, the spinor direction). This is the right structure for matter-tower computations.
- **Generation tower / route II mechanism**: the cross-cutting fermion tower (P1.6) lives in δ. B₂⁽¹⁾'s δ structure (doubling on short = spinor direction) is the natural seat for the spinor-tower investigation.

## 6. Honest scope + tier

**RIGOROUS**: B₂⁽¹⁾ and C₂⁽¹⁾ are distinct affine algebras (Langlands dual); both extend B₂≅C₂=so(5)≅sp(4) finite; both sum to h=4; marks/δ structures as stated; finite Serre coefficients don't distinguish them.

**PIN RECOMMENDATION**: B₂⁽¹⁾ (marks 1,1,2), based on the keystone identifying the substrate's spatial algebra as SO(5)=B₂ specifically. The substrate's natural affinization is the loop algebra of SO(5), which is B₂⁽¹⁾.

**HONEST CAVEAT**: this is a CONVENTION decision driven by the keystone's labeling. C₂⁽¹⁾ would be the right choice if a geometric/Hall-algebra argument picked the Sp(4) labeling instead. I don't see such an argument, but Keeper/Elie may.

**Cal #27 / honesty**: I'm NOT claiming this is forced by a deep argument — it's the natural choice given the keystone's SO(5) labeling. If you think of the substrate as a sp(4) loop, you'd pick C₂⁽¹⁾. The choice matters for the δ-tower structure and the tube count, so the team should ratify.

**Routed**: → Keeper: pin recommendation B₂⁽¹⁾ — concur or push back? Your C₂⁽¹⁾ derivation is correct as math; the difference is which labeling the substrate naturally uses. → Elie: once Keeper concurs/redirects, the bulk K-type radial tower / L4 v0.2 work + any #409 recompute uses the pinned affine type. → me: continuing to P1.2 bulk-color push assuming B₂⁽¹⁾.

— Lyra, affine-type pin v0.1. RECOMMEND **B₂⁽¹⁾ (marks 1,1,2; δ=α_0+α_1+2α_2)** as the substrate's natural affinization, from the keystone K=SO(5)×SO(2) → loop algebra ŝo(5) = B₂⁽¹⁾. Keeper-derived C₂⁽¹⁾ (marks 1,2,1) is the Langlands dual, same finite algebra under Sp(4) labeling. Both sum to h=4; both give h^∨=N_c=3; finite Serre coefficients don't distinguish. The pin decision matters for the δ-tower structure (doubling on α_2 short = spinor direction for B₂⁽¹⁾) and the tube count. Pending Keeper+Elie ratification.

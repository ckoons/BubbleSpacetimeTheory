---
node_type: forward_derivation
title: "K-types of the SPINOR-λ member: (k±1/2, 1/2), second row PINNED to 1/2 — and it does NOT restore three generations everywhere"
author: Grace
date: 2026-08-23
status: "CANDIDATE — NOT CLAIMED (Rule 3). @Lyra @Cal."
---

# The spinor-λ K-types

## 1. Result
For λ = the SO(5) spinor Δ = V_{(1/2,1/2)} (dim 4), holomorphic sections give **Δ ⊗ P(p⁺)**. With the banked scalar decomposition P_d = ⊕_j H_{d−2j} and

> **Δ ⊗ V_{(k_harm,0)} = V_{(k_harm+1/2, 1/2)} ⊕ V_{(k_harm−1/2, 1/2)}**   *(second summand absent at k_harm = 0)*

| m_wt = d | K-types of H²_{λ=0} | K-types of H²_{λ=Δ} | count λ=0 | count λ=Δ |
|---|---|---|---|---|
| 0 | (0,0) | (1/2,1/2) | 1 | **1** |
| 1 | (1,0) | (3/2,1/2), (1/2,1/2) | 1 | **2** |
| 2 | (2,0), (0,0) | (5/2,1/2), (3/2,1/2), (1/2,1/2) | 2 | **3** |
| 3 | (3,0), (1,0) | (7/2,1/2) … (1/2,1/2) | 2 | **4** |

> ### **Every spinor K-type is (k_harm ± 1/2, 1/2): BOTH rows half-integer, and the SECOND ROW IS PINNED TO 1/2.**
> **Counts: ⌊d/2⌋+1 scalar → d+1 spinor.**

**These are exactly the K-types the λ = 0 space cannot carry** — which is what the crossing predicted, so this half is confirmation rather than news.

## 2. ★ THE NEGATIVE, and it is the part that matters
Mapping to the sectors by m_wt: **neutrino (d=0) → 1 · down (d=1) → 2 · up (d=2) → 3 · lepton (d=3) → 4.**

> ### **THE SPINOR BUNDLE DOES NOT RESTORE THREE GENERATIONS. It relieves the shortage in TWO sectors (up 2→3, lepton 2→4) and the shortage SURVIVES in the other two: the neutrino still admits 1, the down still admits 2.**

**Elie's destabilisation is narrowed, not removed.** Anyone reading "fermions live at spinor λ" as the fix should read this row instead. *(And this does not by itself decide his (a)/(b)/(c) — the sector↔m_wt mapping is F820's m_Q labelling, which is @Lyra's object-identification call and is untouched here.)*

## 3. ⚠ CATCH ON THE REPAIR — "banked" is nearly right, and the gap is a bundle rank
The corollary to T2428, verbatim: *"L²(D_IV⁵; **L_λ**), the space of equivariant L² sections of the **canonical LINE bundle** L_λ → D_IV⁵ for dominant weight λ of K."*

> **A spinor λ is 4-dimensional. Δ induces a RANK-4 HOMOGENEOUS VECTOR BUNDLE, not a line bundle.**
> **So the banked sentence covers the λ = 0 line-bundle family; it does NOT, as written, contain the spinor member.** Either the corollary's "line bundle for dominant weight λ of K" is loose language for a general induced bundle, or **the spinor case is an extension and should be filed as one.**

**This is the same species as the crossing it is repairing: `L_λ` reading as line-bundle in one place and induced-bundle in another.** The subscript fix is right; **the claim "no new machinery, it was already banked" needs this one word checked before it travels.**

## 4. Gates and joints
**Gated (read refused on failure):** Weyl B₂ dims reproduce dim H_k, k = 0…12 · spinor dim = 4 · **must-reject** V_{(k,1)} ≠ H_k · **tensor rule verified by dimension at every k = 0…12** · **Σ dim(K-types) = 4·dim P_d at every d = 0…6.**
**Still cited-not-banked (Cal's to gate):** p⁺ ≅ ℂ⁵ as standard SO(5)-module · Hua/Schmid multiplicity-freeness · **and now: that holomorphic sections of the induced bundle give Δ ⊗ P(p⁺) as a K-module.** That third one is new and I am naming it rather than letting it ride on the first two.

*Forward: object → count → look. — Grace, R71*


---

## ADDENDUM 2026-08-23 (R73) — the SO(2) weight, carried explicitly, and what it exposes

### A. Cal's two conditions, stated as required
1. **Δ ⊗ P(p⁺) is the K-FINITE part of the section space, not the whole of it.** Holomorphic sections are Hol(D) ⊗ Δ; the K-type table addresses the K-finite vectors and says nothing about completion.
2. **Holomorphic triviality of the bundle is an INPUT.** Standard for a contractible bounded domain, and it is now stated rather than assumed silently.

### B. The table, with SO(2) weight — and it is not decoration
Write the K-type as **(SO(5) label ; SO(2) weight)**, weight = **d + w₀** (w₀ the bundle's own SO(2) character weight — see C).

| m_wt = d | K-types of H²_{λ=(Δ,w₀)} |
|---|---|
| 0 | (1/2,1/2 ; w₀) |
| 1 | (3/2,1/2 ; 1+w₀), (1/2,1/2 ; 1+w₀) |
| 2 | (5/2,1/2 ; 2+w₀), (3/2,1/2 ; 2+w₀), (1/2,1/2 ; 2+w₀) |
| 3 | (7/2,1/2 ; 3+w₀) … (1/2,1/2 ; 3+w₀) |

> ### **★ Every V_(a,1/2) with a ≥ 3/2 arrives TWICE across degrees** — as the plus-branch of d = a−1/2 and the minus-branch of d = a+1/2 — **including Δ itself.**
> **⟹ the decomposition is multiplicity-free over K = SO(5)×SO(2), but multiplicity-2 over the SO(5) factor alone. DROPPING THE SO(2) WEIGHT COLLAPSES TWO DISTINCT K-TYPES INTO ONE.**
> *This is why the weight is mandatory and not bookkeeping: the SO(5) label alone stops being an address the moment the bundle changes. It was a sufficient label where it was formed and is insufficient one bundle over.*

### C. ★★ AND CARRYING THE WEIGHT EXPOSES SOMETHING: "spinor λ" IS UNDER-SPECIFIED
K = SO(5) × SO(2), so **every irrep of K is (an SO(5) irrep) ⊗ (an SO(2) character).** Δ is an SO(5) rep. **To be a K-rep it needs an SO(2) weight w₀, and w₀ is NOT determined by Δ.**

> ### **⟹ H²_{λ=Δ} is not a space. It is a ONE-PARAMETER FAMILY H²_{λ=(Δ,w₀)}.**
> **"Fermions live at spinor λ" does not name an object until w₀ is pinned, and nobody has pinned it.**

**Consequence for what I owe (T2513 gate (b)):** the genus/measure-weight re-derivation **cannot be done yet** — the Bergman measure weight and w₀ enter the norm together, so the re-derivation is **blocked on an input nobody has named**, not on a computation nobody has run. **That is the honest state of gate (b): reopened, and now with its blocker identified rather than merely reopened.**

*I am not guessing w₀. Pinning it is a physics choice (which spin structure / which line-bundle twist the fermion carries) and belongs to whoever owns the sector↔label mapping.*
